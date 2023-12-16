import pandas as pd
import mysql.connector

def CSVtoDataFrame(file_name):
	data = pd.read_csv (file_name)
	df = pd.DataFrame(data)
	return df

def connectToDB(server, db, user, password):
	connection = mysql.connector.connect(host= server,user=user,  password=password,  database=db)
	return connection


if __name__ == "__main__":
	conn = connectToDB('localhost','store_monitoring','test', 'test')
	cursor = conn.cursor()
	
	
	cursor.execute("DROP TABLE IF EXISTS store_timezone;")
	cursor.execute("DROP TABLE IF EXISTS store_status;")
	cursor.execute("DROP TABLE IF EXISTS store_hours;")
	
	cursor.execute('''
		CREATE TABLE store_timezone (
    		store_id BIGINT,
    		timezone_str VARCHAR(50)
		)
	''')
	cursor.execute('''
		CREATE TABLE store_status (
    		store_id BIGINT,
    		status VARCHAR(10),
    		timestamp_utc VARCHAR(50)
		)
	''')
	cursor.execute('''
		CREATE TABLE store_hours (
    		store_id BIGINT,
    		day INT,
    		start_time_local TIME,
    		end_time_local TIME
		)
	''')

	df = CSVtoDataFrame('sample_data/store_timezone.csv')
	for row in df.itertuples():
		cursor.execute("INSERT INTO store_timezone (store_id, timezone_str) VALUES (%s, %s)", (row.store_id, row.timezone_str))
	
	
	df = CSVtoDataFrame('sample_data/store_status.csv')
	for row in df.itertuples():
		cursor.execute("INSERT INTO store_status (store_id, status, timestamp_utc) VALUES (%s, %s, %s)", 
			(row.store_id, row.status, row.timestamp_utc))
	
	df = CSVtoDataFrame('sample_data/store_hours.csv')
	for row in df.itertuples():
		cursor.execute("INSERT INTO store_hours (store_id, day, start_time_local, end_time_local) VALUES (%s, %s, %s, %s)", 
			(row.store_id, row.day, row.start_time_local, row.end_time_local))

	conn.commit()
	conn.close()	