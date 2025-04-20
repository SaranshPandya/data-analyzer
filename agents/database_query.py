from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from psycopg2.extensions import connection
import psycopg2
import pwinput


def connect_to_database(
    user: str,
    dbname: str,
    host: str="localhost",
    port: int=5432
    ) -> connection:
        password = pwinput.pwinput("\nEnter password: ", mask='*')
        print("Connecting...")
        conn = psycopg2.connect(
        user=user,
        dbname=dbname,
        host=host,
        password=password,
        port=port
        )
        
        print("Database connected successfully!")
        return conn
    

db_connect = connect_to_database(user="saranshpandya", dbname="bitcoindb", host="host.docker.internal")

    
    
