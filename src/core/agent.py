"""
Based Hackamatic - Main Agent Module
"""
from typing import Dict, Any
from langchain.chat_models import ChatOpenAI
from coinbase.agentkit import (
    AgentKit,
    CdpWalletProvider,
    wethActionProvider,
    walletActionProvider,
    erc20ActionProvider,
    cdpApiActionProvider,
    cdpWalletActionProvider,
    pythActionProvider,
)
from coinbase.agentkit_langchain import getLangChainTools
from langchain.agents import AgentExecutor
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HackamaticAgent:
    """
    Main agent class for Based Hackamatic project.
    Handles hackathon participation, project development, and fund management.
    """
    
    def __init__(self):
        """Initialize the Hackamatic agent with required configurations."""
        self.validate_environment()
        self.setup_agent()
        
    def validate_environment(self) -> None:
        """Validate that all required environment variables are set."""
        required_vars = [
            'CDP_API_KEY_NAME',
            'CDP_API_KEY_PRIVATE_KEY',
            'OPENAI_API_KEY',
            'NETWORK_ID'
        ]
        
        missing = [var for var in required_vars if not os.getenv(var)]
        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}"
            )
            
    def setup_agent(self) -> None:
        """Set up the AgentKit configuration and LLM integration."""
        try:
            # Initialize LLM
            self.llm = ChatOpenAI(
                model="gpt-4",
                temperature=0.2
            )
            
            # Configure CDP Wallet Provider
            wallet_config = {
                'apiKeyName': os.getenv('CDP_API_KEY_NAME'),
                'apiKeyPrivateKey': os.getenv('CDP_API_KEY_PRIVATE_KEY'),
                'networkId': os.getenv('NETWORK_ID', 'base-sepolia')
            }
            
            self.wallet_provider = CdpWalletProvider.configureWithWallet(wallet_config)
            
            # Initialize AgentKit with all required providers
            self.agent_kit = AgentKit(
                walletProvider=self.wallet_provider,
                actionProviders=[
                    wethActionProvider,
                    walletActionProvider,
                    erc20ActionProvider,
                    cdpApiActionProvider,
                    cdpWalletActionProvider,
                    pythActionProvider
                ]
            )
            
            # Get LangChain tools
            self.tools = getLangChainTools(self.agent_kit)
            
            logger.info("Agent setup completed successfully")
            
        except Exception as e:
            logger.error(f"Error setting up agent: {str(e)}")
            raise
            
    async def execute_task(self, task: str) -> Dict[str, Any]:
        """
        Execute a task using the agent.
        
        Args:
            task: The task description or command to execute
            
        Returns:
            Dict containing the task result and any relevant metadata
        """
        try:
            # Create agent executor
            agent_executor = AgentExecutor.from_agent_and_tools(
                agent=self.agent_kit.get_agent(),
                tools=self.tools,
                verbose=True
            )
            
            # Execute task
            result = await agent_executor.arun(task)
            return {"status": "success", "result": result}
            
        except Exception as e:
            logger.error(f"Error executing task: {str(e)}")
            return {"status": "error", "error": str(e)}
            
    def get_wallet_address(self) -> str:
        """Get the agent's wallet address."""
        return self.wallet_provider.getAddress()
        
    def get_wallet_balance(self) -> Dict[str, Any]:
        """Get the current wallet balance."""
        return self.wallet_provider.getBalance() 