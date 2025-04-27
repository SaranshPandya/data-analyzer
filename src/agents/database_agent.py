"""
Agent for accessing database.
"""

from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from colorama import Fore, Style
import getpass

# import sys

# sys.path.append("/workspaces/data-analyzer/")
# from model import init_model

# REFAC: Make tools and LLM in saperate files to make the code moduler.
class Agent:
    def __init__(
        self,
        uri: str,
        llm_name: str,
        api_key: str = None,
        temperature: float = 0.5,
        verbose: bool = False
        ):
        
        self.uri=uri
        self.llm_name=llm_name
        self.api_key = api_key
        self.temperature=temperature
        self.verbose = verbose

        # prompt user if the api_key is None.
        self._get_api_key()
        
    # TODO: Store the user given API key
    # FEAT: Add the ability to change or delete the API key.
    def _get_api_key(self):
        try:
            # api_key = os.environ.get(self.api)
            if self.api_key is None:
                self.api_key = getpass.getpass("Enter Gemini API key: ")
            return self.api_key
        
        except Exception as e:
            raise Exception(Fore.RED + f"Unable to fetch the API key: {e}" + Style.RESET_ALL)
         
    def __init_db(self) -> SQLDatabase:
        db = SQLDatabase.from_uri(self.uri)
        return db
    
    def __init_llm(self) -> ChatGoogleGenerativeAI:
        # if not self.api_key:
        #     self.api_key = self._get_api_key()
        llm = ChatGoogleGenerativeAI(
            model=self.llm_name,
            api_key=self.api_key,
            temperature=self.temperature
            )
        
        return llm
       
    def __init_SQL_toolkit(self) -> SQLDatabaseToolkit:
        toolkit = SQLDatabaseToolkit(db=self.__init_db(),
                                     llm=self.__init_llm())
        return toolkit
    
    def __init_agent(self):
        agent = create_sql_agent(
            llm=self.__init_llm(),
            toolkit=self.__init_SQL_toolkit(),
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=self.verbose
        )
        
        return agent
    
    def run_agents(self, query: str):
        agent = self.__init_agent()
        response = agent.invoke(query)
        
        return response
