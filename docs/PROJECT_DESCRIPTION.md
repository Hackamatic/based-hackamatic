# Based Hackamatic

## Project Overview

Based Hackamatic is an AI agent built with Coinbase's AgentKit framework that participates in hackathons and manages its own funds. The agent will compete in Base and Coinbase tracks at Ethglobal hackathons, collecting prize money to fund future participations. Through this self-funding mechanism, the agent will continuously participate in hackathons, improving its capabilities and growing its fund pool over time.

## System Architecture

The system is built on AgentKit framework with three main components working together:

The Agent System forms the core, handling project development and human interactions. It uses LLM integration for code generation and project development, while providing an interface for humans to handle hackathon registration and key decisions.

The Wallet Management system handles all financial operations through CDP MPC Wallet implementation. It manages prize collection, fund handling through Coinbase, and maintains transaction records.

The Development Engine generates projects, maintains code quality, produces documentation, and runs tests. It interfaces with GitHub for project management and version control.

## Implementation Process

The implementation will proceed in four main phases:

Phase 1 begins with setting up the development environment. We'll install AgentKit dependencies, configure CDP authentication, set up LLM integration, and initialize the wallet system. Once the environment is ready, we'll implement the basic agent functionality, creating the human interaction interface and setting up project generation capabilities.

Phase 2 focuses on wallet integration. We'll implement the CDP wallet with proper security measures and transaction handling capabilities. This includes setting up the prize collection system and fund management logic. We'll also implement comprehensive monitoring systems for tracking transactions, balances, and generating alerts and reports.

Phase 3 develops the project generation capabilities. We'll build a pipeline for code generation, implement quality assurance checks, and set up the testing framework. This phase also includes setting up GitHub automation for repository management, handling issues, and managing pull requests.

Phase 4 implements the financial system. We'll automate prize collection through smart contract integration, handle payment processing, and implement fund distribution and reinvestment logic. This phase includes setting up monitoring and reporting systems for tracking performance and managing risks.

## User Flow

1. Initial Setup:
   The user installs the system and configures necessary API keys for CDP, OpenAI, and GitHub. The system initializes a new CDP wallet for managing funds.

2. Hackathon Participation:
   When a new hackathon begins, the user notifies the agent. The agent guides the user through the registration process for the hackathon, ensuring all necessary information is provided.

3. Project Development:
   Once registered, the agent begins the project development cycle:
   - Generates project ideas based on hackathon tracks and requirements
   - Creates a new GitHub repository
   - Generates initial project structure and code
   - Implements features and documentation
   - Manages testing and quality assurance
   - Prepares project submission

4. Prize Collection:
   After the hackathon, if prizes are won:
   - The agent's wallet automatically collects prize money
   - Funds are managed through Coinbase
   - A portion is reserved for future hackathon participation
   - Transaction records and reports are generated

## Development Environment

The system requires Python 3.10+ and Node.js 18+. Configuration is managed through environment variables:

```plaintext
CDP_API_KEY_NAME=your_key_name
CDP_API_KEY_PRIVATE_KEY=your_private_key
OPENAI_API_KEY=your_openai_key
NETWORK_ID=base-sepolia
```

## 📚 Documentation

- [AgentKit Documentation](https://docs.cdp.coinbase.com/agentkit/docs/welcome)
- [CDP Documentation](https://docs.cdp.coinbase.com)
- [Base Blockchain Documentation](https://docs.base.org/)
