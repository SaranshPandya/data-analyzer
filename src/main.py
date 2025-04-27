# FEAT: Automated setup for local postgreSQL setup, if user wants.
from tools.database import DatabaseManager
from agents.database_agent import Agent
from colorama import Fore, Style
import warnings

print(Fore.LIGHTGREEN_EX + "Starting Service..." + Style.RESET_ALL)

warning = """IMPORTANT:
As of now, you must manually enter database details and Gemini API keys every time.
Persistence support is coming soon!"""

print(Fore.LIGHTRED_EX + f"\n{warning}\n" + Style.RESET_ALL)

db_instance = DatabaseManager()

uri = db_instance.return_uri()

agent_insstance = Agent(uri=uri,
                        llm_name="gemini-2.0-flash",
                        temperature=0.6,
                        verbose=True)

while True:
    try:
        query = input(Fore.LIGHTBLUE_EX + "\nUser: ")
        print(Style.RESET_ALL)
        if query.lower() in ['q']:
            print("Alright Bye...")
            break
        
        agent_insstance.run_agents(query=query)
    
    except Exception as e:
        raise Exception(Fore.RED + f"ERROR OCCURED: {str(e)}" + Style.RESET_ALL)

