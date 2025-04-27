import base64
import httpx
import time
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


class ModelManager:
    def __init__(self, model_name: str, api_key: str):
        """
        Class for managing large language models.
        Args:
            model_name (str): _description_
            api_key (str): _description_
        """
        self.model_name=model_name
        self.api_key=api_key
  
    def init_gemini(self, temperature: float=0.5) -> ChatGoogleGenerativeAI:
        """
        Initialize gemini model

        Args:
            temperature (float, optional): _description_. Defaults to 0.5.

        Returns:
            ChatGoogleGenerativeAI
        """
        
        llm = ChatGoogleGenerativeAI(model=self.model_name,
                                     api_key=self.api_key,
                                     temperature=temperature)
        
        return llm


if __name__ == "__main__":
    llm_instance = ModelManager(model_name="gemini-2.0-flash",
                                api_key="nothing")
    
    llm = llm_instance.init_gemini(temperature=0.7)
    
    response = llm.invoke("What is the peer to peer protocol?")
    print(response.content) 
