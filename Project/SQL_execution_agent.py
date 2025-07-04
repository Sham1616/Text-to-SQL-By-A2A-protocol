from agent_card import AgentCard
from MCP_Protocol import MCPMessageType
import sqlite3

class SQLExecutionAgent:
    def __init__(self, db_path="hospital_patients.db", check_same_thread=True):
        self.conn = sqlite3.connect(db_path, check_same_thread=check_same_thread)
        self.cursor = self.conn.cursor()
        self.card = AgentCard(
            name="SQLExecutionAgent",
            supported_messages=[MCPMessageType.QUERY_REQUEST.name],
            capabilities=["execute_sql"],
            version="1.0"
        )

    def execute_sql(self, sql_query):
        try:
            self.cursor.execute(sql_query)
            rows = self.cursor.fetchall()
            columns = [desc[0] for desc in self.cursor.description]
            dict_results = [dict(zip(columns, row)) for row in rows]
            return dict_results
        except Exception as e:
            return str(e)

    def handle_message(self, message):
        if message["type"] != MCPMessageType.QUERY_REQUEST.name:
            raise Exception("Unsupported message type")

        content = message["content"]
        result = self.execute_sql(content["sql_query"])

        response_content = {
            "original_query": content.get("original_query"),
            "sql_query": content.get("sql_query"),
        }

        if isinstance(result, str):  # error case
            response_content["error"] = result
        else:
            response_content["result"] = result

        return {
            "sender": self.card.name,
            "receiver": message["sender"],
            "type": MCPMessageType.QUERY_RESULT.name,
            "content": response_content
        }

    def close(self):
        self.conn.close()
