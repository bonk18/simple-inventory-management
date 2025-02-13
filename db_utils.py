import psycopg2
def get_connection():
 return psycopg2.connect( 
    dbname='database_name',
    user='user_name',
    password='database_password',
    host='host',
    port='port'
)