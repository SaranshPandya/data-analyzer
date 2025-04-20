"""
Creates and inserts csv file into the postgres database.
"""
 
import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
import pwinput

from colorama import Fore, Style


class DatabaseManager:
    def __init__(
        self,
        user: str,
        host: str,
        dbname: str,
        port: str = "5432"
    ):
        self.user = user
        self.host = host.strip()
        self.dbname = dbname
        self.port = port
        self.password = None
    
    # take password for database password
    def _get_password(self):
        if self.password is None:
            self.password = pwinput.pwinput(prompt="Enter PostgreSQL password: ", mask="*") 
    
    # Create a database
    def create_database(self):
        self._get_password()
        try:
            conn = psycopg2.connect(
                user=self.user,
                dbname="postgres",
                host=self.host,
                password=self.password,
                port=self.port
            )
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor=conn.cursor()
            cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", (self.dbname,))
            exists = cursor.fetchone()
            
            if exists:
                print(Fore.LIGHTGREEN_EX + f"Database {self.dbname} already exists" + Style.RESET_ALL)
             
            else:
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.dbname)))
                print(Fore.LIGHTGREEN_EX + f"Database {self.dbname} created successfully" + Style.RESET_ALL)

            cursor.close()
            cursor.close()

        except psycopg2.OperationalError as e:
            print(Fore.RED + f"Unable to connect to PostgreSQL: {str(e)}")
        
        except psycopg2.Error as e:
            print(Fore.RED + f"PostgreSQL Error: {str(e)}" + Style.RESET_ALL)
        
        except Exception as e:
            raise Exception(Fore.RED + f"ERROR: {str(e)}" + Style.RESET_ALL) from e
        
            
    # Currently only supports postgres.
    def insert_csv(
        self,
        file: str,
        table_name: str
    ):
        self._get_password()
        try:
            df = pd.read_csv(file)
            print(f"Inserting {df.shape[1]} columns and {df.shape[0]} rows")
            engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.dbname}")
            
            try:
                df.to_sql(table_name, if_exists="replace", index=False, con=engine)
                print(Fore.GREEN + f"Data successfully inserted into {self.dbname}" + Style.RESET_ALL) 
            except Exception as e:
                print(f"Error: {str(e)}")
        
        except FileNotFoundError as e:
            raise FileExistsError(Fore.RED + f"File Not Found {str(e)}" + Style.RESET_ALL) from e

if __name__ == "__main__":
    db_inst = DatabaseManager(user="saranshpandya", host="host.docker.internal", dbname="test_from_python")
    db_inst.create_database() 
    db_inst.insert_csv(table_name="student_data", file="test_dataset.csv")
