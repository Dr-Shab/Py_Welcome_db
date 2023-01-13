from dotenv import load_dotenv
import os

load_dotenv('.env')

dbname = os.getenv('USER')

print(dbname)