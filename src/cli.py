#!/usr/bin/env python3
"""
Command-line interface for Based Hackamatic - An AI Agent for Hackathon Participation
"""
import click
import asyncio
from typing import Dict, Any
from core.agent import HackamaticAgent
from core.config import AGENT_CONFIG, WALLET_CONFIG, PROJECT_TEMPLATES
import logging
import logging.config
from core.config import LOGGING_CONFIG
from pathlib import Path

# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

class HackamaticCLI:
    def __init__(self):
        self.agent = HackamaticAgent()

@click.group()
@click.pass_context
def cli(ctx):
    """Based Hackamatic - AI Agent for Hackathon Participation and Prize Collection"""
    ctx.obj = HackamaticCLI()

@cli.group()
def wallet():
    """Wallet management commands"""
    pass

@wallet.command('info')
@click.pass_obj
def wallet_info(cli_obj):
    """Show wallet information and balances"""
    try:
        address = cli_obj.agent.get_wallet_address()
        balance = cli_obj.agent.get_wallet_balance()
        click.echo(f"🔑 Wallet Address: {address}")
        click.echo(f"💰 Current Balance: {balance} ETH")
        click.echo(f"⚙️  Network: {AGENT_CONFIG['network_id']}")
    except Exception as e:
        click.echo(f"❌ Error retrieving wallet info: {str(e)}", err=True)

@wallet.command('fund')
@click.option('--amount', type=float, prompt=True, help='Amount in ETH to fund')
@click.pass_obj
def fund_wallet(cli_obj, amount):
    """Fund the wallet with specified amount"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task(f"Fund wallet with {amount} ETH"))
        if result["status"] == "success":
            click.echo(f"✅ Funding successful! New balance: {result['result']} ETH")
        else:
            click.echo(f"❌ Funding failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error funding wallet: {str(e)}", err=True)

@cli.group()
def hackathon():
    """Hackathon participation commands"""
    pass

@hackathon.command('register')
@click.option('--name', prompt='Hackathon name', help='Name of the hackathon')
@click.option('--track', prompt='Track name', help='Name of the track (e.g., Base, Coinbase)')
@click.option('--project', prompt='Project name', help='Name of your project')
@click.pass_obj
def register_hackathon(cli_obj, name: str, track: str, project: str):
    """Register for a hackathon"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "register_hackathon",
            "params": {
                "name": name,
                "track": track,
                "project": project
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Registration successful!")
            click.echo(f"📝 Project: {project}")
            click.echo(f"🎯 Track: {track}")
            click.echo(f"📅 Hackathon: {name}")
        else:
            click.echo(f"❌ Registration failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error during registration: {str(e)}", err=True)

@hackathon.command('submit')
@click.option('--project', prompt='Project name', help='Name of your project')
@click.option('--description', prompt='Project description', help='Brief description of your project')
@click.pass_obj
def submit_project(cli_obj, project: str, description: str):
    """Submit a project to the hackathon"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "submit_project",
            "params": {
                "project": project,
                "description": description
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Project submitted successfully!")
            click.echo(f"🔗 Submission URL: {result['result']['url']}")
        else:
            click.echo(f"❌ Submission failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error submitting project: {str(e)}", err=True)

@cli.group()
def project():
    """Project development commands"""
    pass

@project.command('init')
@click.option('--name', prompt='Project name', help='Name of your project')
@click.option('--template', type=click.Choice(['default', 'web3', 'defi']), default='default')
@click.pass_obj
def init_project(cli_obj, name: str, template: str):
    """Initialize a new project"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "init_project",
            "params": {
                "name": name,
                "template": template
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Project initialized successfully!")
            click.echo(f"📁 Project directory: {result['result']['path']}")
        else:
            click.echo(f"❌ Project initialization failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error initializing project: {str(e)}", err=True)

@project.command('develop')
@click.option('--feature', prompt='Feature description', help='Description of the feature to develop')
@click.pass_obj
def develop_feature(cli_obj, feature: str):
    """Develop a new feature using AI assistance"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "develop_feature",
            "params": {
                "description": feature
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Feature development completed!")
            click.echo(f"📝 Changes made:")
            for file, changes in result['result']['changes'].items():
                click.echo(f"  - {file}: {changes}")
        else:
            click.echo(f"❌ Feature development failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error developing feature: {str(e)}", err=True)

@cli.group()
def prize():
    """Prize collection and management commands"""
    pass

@prize.command('collect')
@click.option('--hackathon', prompt='Hackathon name', help='Name of the hackathon')
@click.pass_obj
def collect_prize(cli_obj, hackathon: str):
    """Collect prizes from a hackathon"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "collect_prize",
            "params": {
                "hackathon": hackathon
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Prize collection initiated!")
            click.echo(f"💰 Amount: {result['result']['amount']} ETH")
            click.echo(f"📜 Transaction: {result['result']['tx_hash']}")
        else:
            click.echo(f"❌ Prize collection failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error collecting prize: {str(e)}", err=True)

@prize.command('reinvest')
@click.option('--amount', type=float, prompt=True, help='Amount in ETH to reinvest')
@click.pass_obj
def reinvest_prize(cli_obj, amount: float):
    """Reinvest collected prizes"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "reinvest_prize",
            "params": {
                "amount": amount
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Reinvestment successful!")
            click.echo(f"💰 Amount reinvested: {amount} ETH")
            click.echo(f"📊 New investment balance: {result['result']['balance']} ETH")
        else:
            click.echo(f"❌ Reinvestment failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error reinvesting prize: {str(e)}", err=True)

@cli.command()
@click.pass_obj
def status(cli_obj):
    """Show current agent status and active tasks"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task("get_status"))
        if result["status"] == "success":
            status_data = result['result']
            click.echo("📊 Current Status:")
            click.echo(f"🤖 Agent State: {status_data['agent_state']}")
            click.echo(f"🎯 Active Tasks: {len(status_data['active_tasks'])}")
            click.echo(f"💰 Total Prizes: {status_data['total_prizes']} ETH")
            click.echo("\n📝 Active Tasks:")
            for task in status_data['active_tasks']:
                click.echo(f"  - {task['name']}: {task['status']}")
        else:
            click.echo(f"❌ Error getting status: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error checking status: {str(e)}", err=True)

@cli.group()
def setup():
    """Project setup and initialization commands"""
    pass

@setup.command('init')
@click.option('--name', prompt='Project name', help='Name of your project')
@click.option('--description', prompt='Project description', help='Brief description of your project')
@click.pass_obj
def setup_init(cli_obj, name: str, description: str):
    """Initialize a new Hackamatic project"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "setup_init",
            "params": {
                "name": name,
                "description": description
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Project initialized successfully!")
            click.echo(f"📁 Project structure created")
            click.echo(f"📝 Documentation generated")
            click.echo("\n📋 Next steps:")
            click.echo("1. Run 'setup environment' to configure your development environment")
            click.echo("2. Run 'setup dependencies' to install required packages")
            click.echo("3. Run 'setup verify' to verify your setup")
        else:
            click.echo(f"❌ Project initialization failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error initializing project: {str(e)}", err=True)

@setup.command('environment')
@click.pass_obj
def setup_environment(cli_obj):
    """Configure development environment"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "setup_environment",
            "params": {}
        }))
        if result["status"] == "success":
            click.echo(f"✅ Environment setup completed!")
            click.echo(f"🐍 Python environment configured")
            click.echo(f"🔧 Development tools installed")
            click.echo(f"⚙️  Configuration files created")
        else:
            click.echo(f"❌ Environment setup failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error setting up environment: {str(e)}", err=True)

@setup.command('dependencies')
@click.option('--requirements', is_flag=True, help='Install from requirements.txt')
@click.option('--dev', is_flag=True, help='Install development dependencies')
@click.pass_obj
def setup_dependencies(cli_obj, requirements: bool, dev: bool):
    """Install project dependencies"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "setup_dependencies",
            "params": {
                "from_requirements": requirements,
                "include_dev": dev
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Dependencies installed successfully!")
            click.echo(f"📦 Core packages installed")
            if dev:
                click.echo(f"🔧 Development tools installed")
            click.echo(f"📋 Requirements file updated")
        else:
            click.echo(f"❌ Dependency installation failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error installing dependencies: {str(e)}", err=True)

@setup.command('verify')
@click.pass_obj
def setup_verify(cli_obj):
    """Verify project setup and configuration"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "setup_verify",
            "params": {}
        }))
        if result["status"] == "success":
            verification = result['result']
            click.echo(f"🔍 Verification Results:")
            click.echo(f"\n✅ Environment Check:")
            click.echo(f"  - Python Version: {verification['python_version']}")
            click.echo(f"  - Virtual Environment: {verification['venv_status']}")
            
            click.echo(f"\n📦 Dependencies Check:")
            click.echo(f"  - Core Dependencies: {'✅' if verification['core_deps'] else '❌'}")
            click.echo(f"  - Development Tools: {'✅' if verification['dev_deps'] else '❌'}")
            
            click.echo(f"\n⚙️  Configuration Check:")
            click.echo(f"  - Environment Variables: {'✅' if verification['env_vars'] else '❌'}")
            click.echo(f"  - Project Structure: {'✅' if verification['project_structure'] else '❌'}")
            
            if verification['issues']:
                click.echo(f"\n⚠️  Issues Found:")
                for issue in verification['issues']:
                    click.echo(f"  - {issue}")
                click.echo(f"\n🔧 Run 'setup fix' to resolve these issues")
            else:
                click.echo(f"\n🎉 All checks passed! Your project is ready for development.")
        else:
            click.echo(f"❌ Verification failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error during verification: {str(e)}", err=True)

@setup.command('fix')
@click.pass_obj
def setup_fix(cli_obj):
    """Fix common setup issues"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "setup_fix",
            "params": {}
        }))
        if result["status"] == "success":
            fixes = result['result']
            click.echo(f"🔧 Applied Fixes:")
            for fix in fixes['applied']:
                click.echo(f"  ✅ {fix}")
            
            if fixes['pending']:
                click.echo(f"\n⚠️  Pending Issues:")
                for issue in fixes['pending']:
                    click.echo(f"  - {issue}")
                click.echo(f"\n❗ Some issues require manual intervention")
            else:
                click.echo(f"\n🎉 All issues have been resolved!")
        else:
            click.echo(f"❌ Fix attempt failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error applying fixes: {str(e)}", err=True)

@setup.command('docs')
@click.option('--type', type=click.Choice(['user', 'dev', 'api']), default='user', help='Type of documentation to generate')
@click.pass_obj
def setup_docs(cli_obj, type: str):
    """Generate project documentation"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "setup_docs",
            "params": {
                "doc_type": type
            }
        }))
        if result["status"] == "success":
            click.echo(f"✅ Documentation generated successfully!")
            click.echo(f"📚 Generated documentation type: {type}")
            click.echo(f"📂 Location: {result['result']['path']}")
            click.echo(f"\n📖 Available documents:")
            for doc in result['result']['files']:
                click.echo(f"  - {doc}")
        else:
            click.echo(f"❌ Documentation generation failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error generating documentation: {str(e)}", err=True)

@cli.group()
def venice():
    """Venice Protocol VVV token management and AI inference payments"""
    pass

@venice.command('balance')
@click.pass_obj
def check_vvv_balance(cli_obj):
    """Check VVV token balance and price"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "check_vvv_balance",
            "params": {}
        }))
        if result["status"] == "success":
            balance_data = result['result']
            click.echo(f"💰 VVV Token Balance:")
            click.echo(f"  Balance: {balance_data['balance']} VVV")
            click.echo(f"  USD Value: ${balance_data['usd_value']}")
            click.echo(f"  Current Price: ${balance_data['token_price']} per VVV")
            click.echo(f"\n🔄 Recent Transactions:")
            for tx in balance_data['recent_txs']:
                click.echo(f"  - {tx['type']}: {tx['amount']} VVV ({tx['date']})")
        else:
            click.echo(f"❌ Balance check failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error checking balance: {str(e)}", err=True)

@venice.command('buy')
@click.option('--amount', type=float, prompt='Amount of VVV tokens to buy', help='Amount of VVV tokens to purchase')
@click.option('--max-slippage', type=float, default=0.5, help='Maximum slippage percentage allowed')
@click.pass_obj
def buy_vvv_tokens(cli_obj, amount: float, max_slippage: float):
    """Purchase VVV tokens on Base"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "buy_vvv_tokens",
            "params": {
                "amount": amount,
                "max_slippage": max_slippage
            }
        }))
        if result["status"] == "success":
            purchase = result['result']
            click.echo(f"✅ VVV Token Purchase Successful!")
            click.echo(f"  Tokens Bought: {purchase['tokens_bought']} VVV")
            click.echo(f"  ETH Spent: {purchase['eth_spent']} ETH")
            click.echo(f"  Average Price: ${purchase['avg_price']} per VVV")
            click.echo(f"  Transaction Hash: {purchase['tx_hash']}")
        else:
            click.echo(f"❌ Purchase failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error buying tokens: {str(e)}", err=True)

@venice.command('inference')
@click.option('--model', type=click.Choice(['gpt-4', 'claude-3', 'llama-2']), prompt='AI model to use', help='AI model for inference')
@click.option('--max-cost', type=float, help='Maximum VVV tokens to spend on inference')
@click.option('--auto-buy', is_flag=True, help='Automatically buy VVV if balance is insufficient')
@click.pass_obj
def pay_inference(cli_obj, model: str, max_cost: float, auto_buy: bool):
    """Pay for AI model inference using VVV tokens"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "pay_inference",
            "params": {
                "model": model,
                "max_cost": max_cost,
                "auto_buy": auto_buy
            }
        }))
        if result["status"] == "success":
            inference = result['result']
            click.echo(f"✅ Inference Payment Successful!")
            click.echo(f"  Model: {model}")
            click.echo(f"  VVV Spent: {inference['tokens_spent']} VVV")
            click.echo(f"  USD Value: ${inference['usd_value']}")
            click.echo(f"  Transaction Hash: {inference['tx_hash']}")
            click.echo(f"\n📊 Usage Stats:")
            click.echo(f"  Remaining Balance: {inference['remaining_balance']} VVV")
            click.echo(f"  Total Spent Today: {inference['daily_spent']} VVV")
        else:
            click.echo(f"❌ Payment failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error processing payment: {str(e)}", err=True)

@venice.command('usage')
@click.option('--period', type=click.Choice(['day', 'week', 'month']), default='day', help='Usage statistics period')
@click.pass_obj
def check_usage(cli_obj, period: str):
    """Check AI inference usage and costs"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "check_inference_usage",
            "params": {
                "period": period
            }
        }))
        if result["status"] == "success":
            usage = result['result']
            click.echo(f"📊 Usage Statistics for past {period}:")
            click.echo(f"\n💰 Token Usage:")
            click.echo(f"  Total Spent: {usage['total_spent']} VVV (${usage['usd_value']})")
            click.echo(f"  Average Cost: {usage['avg_cost']} VVV per inference")
            
            click.echo(f"\n🤖 Model Breakdown:")
            for model, stats in usage['model_stats'].items():
                click.echo(f"  {model}:")
                click.echo(f"    Calls: {stats['calls']}")
                click.echo(f"    Tokens: {stats['tokens_spent']} VVV")
                click.echo(f"    Cost: ${stats['usd_cost']}")
            
            click.echo(f"\n📈 Usage Trend:")
            for day in usage['daily_trend']:
                click.echo(f"  {day['date']}: {day['tokens_spent']} VVV")
        else:
            click.echo(f"❌ Usage check failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error checking usage: {str(e)}", err=True)

@venice.command('auto-fund')
@click.option('--min-balance', type=float, prompt='Minimum VVV balance to maintain', help='Minimum VVV token balance')
@click.option('--max-daily', type=float, prompt='Maximum daily VVV spend', help='Maximum daily VVV token spend')
@click.pass_obj
def configure_auto_funding(cli_obj, min_balance: float, max_daily: float):
    """Configure automatic VVV token purchases"""
    try:
        result = asyncio.run(cli_obj.agent.execute_task({
            "action": "configure_auto_funding",
            "params": {
                "min_balance": min_balance,
                "max_daily_spend": max_daily
            }
        }))
        if result["status"] == "success":
            config = result['result']
            click.echo(f"✅ Auto-funding Configuration Updated!")
            click.echo(f"\n⚙️  Settings:")
            click.echo(f"  Minimum Balance: {config['min_balance']} VVV")
            click.echo(f"  Maximum Daily Spend: {config['max_daily_spend']} VVV")
            click.echo(f"  Auto-buy Threshold: {config['buy_threshold']} VVV")
            
            if config['next_purchase']:
                click.echo(f"\n📅 Next Scheduled Purchase:")
                click.echo(f"  Amount: {config['next_purchase']['amount']} VVV")
                click.echo(f"  Date: {config['next_purchase']['date']}")
        else:
            click.echo(f"❌ Configuration failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"❌ Error configuring auto-funding: {str(e)}", err=True)

if __name__ == '__main__':
    cli() 