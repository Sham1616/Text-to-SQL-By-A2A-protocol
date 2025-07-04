import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
# cursor.execute("drop table customers")

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    contact TEXT UNIQUE,
    email TEXT UNIQUE
)
''')

fixed_customers = [
    ('Selwin', 'Karaikudi'),
    ('Sham', 'Sathiyamangalam post'),
    ('Gowtham', 'Krishnagiri'),
    ('Nagaraj', 'Manjore'),
    ('Kaazir', 'Kallakurichi'),
    ('Santhosh', 'Tirunelveli'),
    ('Karthik', 'Trichy'),
    ('Vishnu', 'Chennai'),
    ('Arjun', 'Dindigul'),
    ('Ravi', 'Thanjavur'),
    ('Vikram', 'Kanchipuram'),
    ('Saran', 'Nagapattinam'),
    ('Praveen', 'Karur'),
    ('Manoj', 'Pudukkottai'),
    ('Bala', 'Vellore'),
    ('Dinesh', 'Tiruvannamalai'),
    ('Harish', 'Cuddalore'),
    ('Surya', 'Namakkal'),
    ('Anand', 'Thoothukudi'),
    ('Kiran', 'Sivakasi'),
    ('Rajesh', 'Nagercoil'),
    ('Deepak', 'Chidambaram'),
    ('Saravanan', 'Ariyalur'),
    ('Sathish', 'Perambalur'),
    ('Ramesh', 'Dharmapuri'),
    ('Suresh', 'Krishnagiri'),
    ('Vicky', 'Villupuram'),
    ('Ashwin', 'Kumbakonam'),
    ('Balaji', 'Tenkasi'),
    ('Mohan', 'Ranipet'),
    ('Yogesh', 'Chennai'),
    ('Aravind', 'Madurai'),
    ('Prem', 'Coimbatore'),
    ('Vimal', 'Erode'),
    ('Naresh', 'Trichy')
]

tn_cities = [
    'Chennai', 'Coimbatore', 'Madurai', 'Salem', 'Tirunelveli', 'Trichy', 'Erode', 'Vellore',
    'Thoothukudi', 'Nagapattinam', 'Kanchipuram', 'Thanjavur', 'Cuddalore', 'Namakkal', 'Karur',
    'Pudukkottai', 'Tiruvannamalai', 'Villupuram', 'Kumbakonam', 'Ranipet'
]

additional_names = [
    "Ajay", "Bharath", "Chitra", "Divya", "Eashwar", "Feroz", "Ganesh", "Hari",
    "Ishaan", "Jeeva", "Kamal", "Latha", "Magesh", "Naveen", "Omprakash", "Pranav",
    "Raghav", "Sakthi", "Tharani", "Uday", "Vasanth", "Wasantha", "Xavier", "Yash",
    "Zahir", "Abin", "Bhavana", "Charan", "Deepa", "Elango", "Farooq", "Gayathri",
    "Hema", "Indira", "Jayanth", "Kiran", "Lakshmi", "Manikandan", "Nithya", "Oviya",
    "Pavithra", "Ramesh", "Sangeetha", "Thilak", "Uma", "Vignesh", "Waqas", "Yuvraj",
    "Zoya", "Anitha", "Balamurugan", "Chandru", "Dharani", "Eswari", "Fathima", "Gopi",
    "Harin", "Ilango", "Jaya", "Krishna", "Lalitha", "Meena", "Nandan", "Padma", "Ravi"
]

for idx, (name, city) in enumerate(fixed_customers, start=1):
    contact = f"9000000{idx:03d}"  
    email = f"{name.lower().replace(' ', '')}{idx}@example.com"
    cursor.execute(
        "INSERT INTO customers (name, city, contact, email) VALUES (?, ?, ?, ?)",
        (name, city, contact, email)
    )

start_idx = len(fixed_customers) + 1
for i in range(65):
    name = additional_names[i]
    city = tn_cities[i % len(tn_cities)]
    contact = f"9000010{start_idx + i:03d}"  
    email = f"{name.lower().replace(' ', '')}{start_idx + i}@example.com"
    cursor.execute(
        "INSERT INTO customers (name, city, contact, email) VALUES (?, ?, ?, ?)",
        (name, city, contact, email)
    )

conn.commit()
conn.close()

print("Database created and populated with 100 customers!")
