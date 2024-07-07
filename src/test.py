from sqlalchemy import create_engine
import os
from sqlalchemy import text


# Construct the database URL
#db_url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
aws_rds_database_connection = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

print(aws_rds_database_connection)
# Create the SQLAlchemy engine
engine = create_engine(aws_rds_database_connection, echo=True)
print(engine)
# Test the connection
#try:
#    with engine.connect() as connection:
#        result = connection.execute("SELECT c.client_name from clients c")
#        print("Successfully connected to the database!")
#except Exception as e:
#    print(f"Error connecting to the database: {e}")
    
# Test the connection and execute a query
try:
    with engine.connect() as connection:
        # Wrap the query in a text object
        query = text("SELECT c.client_name FROM clients c")
        result = connection.execute(query)
        rows = result.fetchall()
        for row in rows:
            print(row)
    print("Successfully connected to the database and executed the query!")
except Exception as e:
    print(f"Error connecting to the database: {e}")