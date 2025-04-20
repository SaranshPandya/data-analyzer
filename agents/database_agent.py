from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class Agent:
    def __init__(
        self,
        uri: str,
        llm_name: str,
        api_key_env: str,
        temperature: float = 0.5,
        verbose: bool = False
        ):
        
        self.uri=uri
        self.llm_name=llm_name
        self.api_key_env=api_key_env
        self.temperature=temperature
        self.verbose = verbose
    
    def _get_api_key(self):
        api_key = os.environ.get(self.api_key_env)
        return api_key
 
    def __init_db(self) -> SQLDatabase:
        db = SQLDatabase.from_uri(self.uri)
        return db
    
    def __init_llm(self) -> ChatGoogleGenerativeAI:
        llm = ChatGoogleGenerativeAI(
            model=self.llm_name,
            api_key=self._get_api_key(),
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
        response = agent.run(query)
        
        return response