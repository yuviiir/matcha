import mysql.connector
from mysql.connector import errorcode

def create_conn():
	config = {
	'user' : 'root',
	'password' : 'anything',
	'host' : 'localhost'
	}
	db = mysql.connector.connect(pool_name = "pooly_pool", pool_size = 32, pool_reset_session = True,**config)
	return db

def close_conn(db):
	db.close()
	return db

db = create_conn()
cursor = db.cursor()

DB_NAME = 'matcha_sql'
TABLES = {}

TABLES['users'] = (
	"CREATE TABLE `users` ("
	" `id` INT(11)  AUTO_INCREMENT,"
	" `Pref` VARCHAR(5),"
	" `Verify` VARCHAR(5),"
	" `Matches` VARCHAR(500),"
	" `Chats` VARCHAR(500),"
	" `NewMessage` VARCHAR(10),"
	" `Likes` VARCHAR(1000),"
	" `Dislikes` VARCHAR(1000),"
	" `Name` VARCHAR(250),"
	" `Surname` VARCHAR(250),"
	" `Age` INT(10),"
	" `Email` VARCHAR(250),"
	" `username` VARCHAR(250),"
	" `Password` VARCHAR(250),"
	" `Gender` VARCHAR(250),"
	" `Popularity` INT(10),"
	" `Blocked` VARCHAR(500),"
	" `ProfileViews` VARCHAR(500),"
	" `ProfileLikes` VARCHAR(500),"
	" `Suburb` VARCHAR(250),"
	" `Postal Code` INT(10),"
	" `Sexual Orientation` VARCHAR(25),"
	" `Bio` VARCHAR(500),"
	" `Animals` VARCHAR(500),"
	" `Music` VARCHAR(500),"
	" `Sports` VARCHAR(500),"
	" `Food` VARCHAR(500),"
	" `Movies` VARCHAR(500),"
	" `Noti` VARCHAR(5),"
	" `Images` VARCHAR(500),"
	" `Token` VARCHAR(500),"
	" `ConnectionStatus` VARCHAR(500),"
	" PRIMARY KEY (`id`)"
	") ENGINE=InnoDB"
)

TABLES['notifications'] = (
	"CREATE TABLE `notifications` ("
	" `username` varchar(250),"
	" `Subject` varchar(250),"
	" `content` varchar(250),"
	" `status` varchar(50)"
	") ENGINE=InnoDB"
)

TABLES['chats'] = (
	"CREATE TABLE `chats` ("
	" `FromUser` varchar(250),"
	" `ToUser` varchar(250),"
	" `Message` varchar(500),"
	" `Read` varchar(10)"
	") ENGINE=InnoDB"
)

def create_db():
	cursor.execute(
		"CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	print("Database {} created!".format(DB_NAME))

def create_tables():
	cursor.execute("USE {}".format(DB_NAME))

	for table_name in TABLES:
		table_description = TABLES[table_name]
		try:
			print("Creating table ({}) ".format(table_name), end="\n")
			cursor.execute(table_description)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
				print(f'({table_name}) already exists')
			else:
				print(err.msg)

create_db()
create_tables()

def add_log():
	sql = "INSERT INTO users (Name, Surname) VALUES (%s, %s)"
	val = ("asfdsa", "difuhdjf")
	cursor.execute(sql, val)
	db.commit()
	log_id = cursor.lastrowid
	print("Added log {}".format(log_id))