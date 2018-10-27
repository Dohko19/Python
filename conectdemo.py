import mysql.connector

db = mysql.connector.connect(
	host="127.0.0.1",
	user="root",
	passwd="",
	database="python"
	)

c = db.cursor()

sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
val = ("87654321", "Fernando")

c.execute(sql, val)

db.commit()

print(c.rowcount, "Registro agregado")

db.close()
#sql = 'INSERT INTO registro (nombres, apellidos, telefono) VALUES (%s, %s, %s, )',
#(self.txtNombres.text(),self.txtApellidos.text(), self.txtTelefono.text()) 

# c.execute("CREATE TABLE users (id VARCHAR(255), name VARCHAR(255))")

# c.execute("SHOW TABLES")

# for x in c:
# 	print(x)
# c.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
# 
# c.execute("SELECT * FROM users")
# r = c.fetchall()
# db.close()
# for x in r:
# 	print(x)
# c = db.cursor()

#c.execute("CREATE DATABASE python")