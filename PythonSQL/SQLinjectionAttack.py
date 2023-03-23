import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number: ")
update_sql = f"UPDATE contacts SET email = '{new_email}' " \
             f"WHERE phone = {phone}"

update_cursor = db.cursor()
update_cursor.executescript(update_sql)

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()
