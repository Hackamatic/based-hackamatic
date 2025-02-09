# Based Hackamatic Setup Guide

This guide will help you set up the Based Hackamatic AI agent for hackathon participation. The agent uses Coinbase's AgentKit to participate in hackathons and manage its own funds.

## Prerequisites

Before starting, ensure you have the following:

1. **Development Environment**
   - Python 3.10 or higher
   - Node.js 18 or higher
   - Git
   - A code editor (VSCode recommended)

2. **Required Accounts**
   - Coinbase Developer Platform account
   - OpenAI API account
   - GitHub account

3. **API Keys**
   - Coinbase CDP API credentials
   - OpenAI API key
   - GitHub access token

## Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/based-hackamatic.git
   cd based-hackamatic
   ```

2. **Set Up Python Environment**

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Unix/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**

   ```bash
   # Create .env file from template
   cp .env.example .env

   # Edit .env with your credentials
   nano .env  # or use your preferred editor
   ```

   Required variables in `.env`:

   ```plaintext
   # API Keys
   CDP_API_KEY_NAME=your_cdp_key_name
   CDP_API_KEY_PRIVATE_KEY=your_cdp_private_key
   OPENAI_API_KEY=your_openai_key

   # Network Configuration
   NETWORK_ID=base-sepolia
   ```

## Verification Steps

1. **Test Installation**

   ```bash
   # Verify the agent setup
   python src/cli.py setup
   ```

2. **Check Wallet**

   ```bash
   # View wallet information
   python src/cli.py wallet
   ```

## Available Commands

### Basic Operations

1. **Setup and Verification**

   ```bash
   python src/cli.py setup
   ```

   - Validates environment
   - Initializes agent
   - Creates wallet
   - Displays status

2. **Wallet Management**

   ```bash
   python src/cli.py wallet
   ```

   - Shows wallet address
   - Displays balance
   - Lists transactions

3. **Hackathon Registration**

   ```bash
   python src/cli.py register
   ```

   - Guides through registration
   - Prompts for hackathon details
   - Sets up project structure

4. **Status Check**

   ```bash
   python src/cli.py status
   ```

   - Shows current tasks
   - Displays project status
   - Lists active operations

5. **Task Execution**

   ```bash
   python src/cli.py execute "your task description"
   ```

   - Runs specific tasks
   - Handles project operations
   - Manages development workflow

## Project Structure

```plaintext
based-hackamatic/
├── src/                  # Source code
│   ├── core/            # Core functionality
│   │   ├── agent.py     # Agent implementation
│   │   └── config.py    # Configuration
│   ├── cli.py           # Command interface
│   ├── api/             # API integrations
│   ├── utils/           # Utilities
│   └── contracts/       # Smart contracts
├── tests/               # Test suite
├── docs/                # Documentation
├── data/                # Data storage
└── logs/                # Log files
```

## Development Guidelines

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use type hints
   - Document functions
   - Write unit tests

2. **Git Workflow**
   - Create feature branches
   - Write clear commit messages
   - Submit pull requests
   - Review code changes

3. **Testing**

   ```bash
   # Run test suite
   pytest tests/

   # Run with coverage
   pytest --cov=src tests/
   ```

## Troubleshooting

### Common Issues

1. **Environment Setup**
   - Issue: Missing dependencies
   - Solution: `pip install -r requirements.txt`
   - Check: Python and Node.js versions

2. **API Configuration**
   - Issue: Invalid API keys
   - Solution: Verify credentials in `.env`
   - Check: Network connectivity

3. **Wallet Issues**
   - Issue: Connection failures
   - Solution: Check network settings
   - Check: Balance and permissions

### Debug Mode

Run commands with verbose output:

```bash
python src/cli.py setup --verbose
```

Check logs:

```bash
tail -f logs/hackamatic.log
```

## Security Best Practices

1. **API Key Management**
   - Never commit `.env` file
   - Rotate keys regularly
   - Use environment variables

2. **Wallet Security**
   - Set transaction limits
   - Monitor activities
   - Regular backups

3. **Development Security**
   - Use testnet for development
   - Regular security audits
   - Keep dependencies updated

## Maintenance

1. **Regular Updates**

   ```bash
   # Update repository
   git pull

   # Update dependencies
   pip install -r requirements.txt --upgrade
   ```

2. **System Checks**
   - Monitor logs
   - Check dependencies
   - Verify API access
   - Test wallet connection

3. **Backup Procedures**
   - Backup `.env` securely
   - Export wallet data
   - Archive important logs

## Next Steps

1. Complete the installation
2. Run verification tests
3. Create test project
4. Review documentation
5. Start development

## Support

- Check documentation
- Review logs
- Submit issues
- Contribute improvements

Remember to always use the testnet for development and testing before moving to mainnet.
