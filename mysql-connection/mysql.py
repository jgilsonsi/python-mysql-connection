import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

# database credentials
host = "localhost"
user = "root"
password = "master"
db = "manager"
port = 3306

con = MySQLdb.connect (host, user, password, db)
c = con.cursor(MySQLdb.cursors.DictCursor)


def select(fields, tables, where=None):

	global c

	query = "SELECT " + fields + " FROM " + tables
	if (where):
		query = query + " WHERE " + where

	c.execute(query)
	return c.fetchall()


def insert(values, table, fields=None):

	global c, con

	query = "INSERT INTO " + table
	if (fields):
		query = query + " (" + fields + ") "
	query = query + " VALUES " + ", ".join(["(" + v + ")" for v in values])	 

	c.execute(query)
	con.commit()

def update(sets, table, where=None):

	global c, con

	query = "UPDATE " + table
	query = query + " SET " + ", ".join([field + " = '" + value + "'" for field, value in sets.items()])
	if (where):
		query = query + " WHERE " + where

	c.execute(query)
	con.commit()	


def delete(table, where):

	global c, con

	query = "DELETE FROM " + table + " WHERE " + where

	c.execute(query)
	con.commit()


# ----------------------------------------------------------
values = [
	"DEFAULT, 'Maria Rosa', 'maria@gmail.com', '42'",
	"DEFAULT, 'José Cândido', 'candido@gmail.com', '80'",
	]
insert(values, "users")

result = select("name, age", "users")
print(result)

update({"name":"José Rosa","email":"joserosa@gmail.com"}, "users", "email = 'candido@gmail.com'")

result = select("name, age", "users")
print(result)

delete("users", "email = 'maria@gmail.com'")

result = select("*", "users")
print(result)