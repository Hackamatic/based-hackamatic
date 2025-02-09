#!/usr/bin/env python3
"""
Command-line interface for Based Hackamatic
"""
import click
import asyncio
from core.agent import HackamaticAgent
import logging
from core.config import LOGGING_CONFIG
import logging.config

# Configure logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

@click.group()
def cli():
    """Based Hackamatic - AI Agent for Hackathon Participation"""
    pass

@cli.command()
def setup():
    """Initialize and test the agent setup"""
    try:
        agent = HackamaticAgent()
        click.echo(f"Agent initialized successfully!")
        click.echo(f"Wallet address: {agent.get_wallet_address()}")
        click.echo(f"Current balance: {agent.get_wallet_balance()}")
    except Exception as e:
        click.echo(f"Error during setup: {str(e)}", err=True)

@cli.command()
@click.argument('task')
def execute(task):
    """Execute a specific task"""
    try:
        agent = HackamaticAgent()
        result = asyncio.run(agent.execute_task(task))
        if result["status"] == "success":
            click.echo(f"Task completed successfully!")
            click.echo(f"Result: {result['result']}")
        else:
            click.echo(f"Task failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"Error executing task: {str(e)}", err=True)

@cli.command()
def wallet():
    """Show wallet information"""
    try:
        agent = HackamaticAgent()
        click.echo(f"Wallet Address: {agent.get_wallet_address()}")
        balance = agent.get_wallet_balance()
        click.echo(f"Current Balance: {balance}")
    except Exception as e:
        click.echo(f"Error retrieving wallet info: {str(e)}", err=True)

@cli.command()
@click.option('--name', prompt='Hackathon name', help='Name of the hackathon')
@click.option('--track', prompt='Track name', help='Name of the track (e.g., Base, Coinbase)')
def register(name, track):
    """Register for a hackathon"""
    try:
        agent = HackamaticAgent()
        task = f"Register for hackathon: {name}, Track: {track}"
        result = asyncio.run(agent.execute_task(task))
        if result["status"] == "success":
            click.echo(f"Registration process initiated!")
            click.echo(f"Please follow the instructions: {result['result']}")
        else:
            click.echo(f"Registration failed: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"Error during registration: {str(e)}", err=True)

@cli.command()
def status():
    """Check current status and active tasks"""
    try:
        agent = HackamaticAgent()
        result = asyncio.run(agent.execute_task("Get current status and active tasks"))
        if result["status"] == "success":
            click.echo(f"Current Status: {result['result']}")
        else:
            click.echo(f"Error getting status: {result['error']}", err=True)
    except Exception as e:
        click.echo(f"Error checking status: {str(e)}", err=True)

if __name__ == '__main__':
    cli() 