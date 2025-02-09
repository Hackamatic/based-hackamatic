# 🔧 Development Environment Setup

This comprehensive guide will walk you through setting up and using Hackamatic for your hackathon project, from initial setup to final deployment.

## 📋 Prerequisites

1. **Cursor IDE**

   - Download and install [Cursor](https://cursor.sh/) - A modern code editor with AI capabilities
   - Sign in to enable AI features
   - Cursor works like VS Code but with built-in AI assistance
   - No coding experience is required, the AI will guide you

2. **Git**

   - Download Git from [git-scm.com](https://git-scm.com/downloads)
   - During installation, accept all default options if unsure
   - Open Terminal (Mac/Linux) or Command Prompt (Windows)
   - Set up Git with your name and email:

     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```

3. **GitHub Account**

   - Create a free account at [github.com](https://github.com)
   - Sign in to your account
   - Remember your GitHub username and password

## 🚀 Initial Project Setup

1. **Fork the Repository**

   - Visit the Hackamatic repository at [github.com/MatheusDaros/hackamatic](https://github.com/MatheusDaros/hackamatic)
   - Click the "Fork" button in the top-right corner
   - Wait for GitHub to create your copy of the repository
   - You'll be redirected to your forked version at `github.com/your-username/hackamatic`

2. **Customize Repository Settings**

   - On your forked repository page:
     1. Click "Settings" tab
     2. Under "Repository name", enter your project name
     3. Click "Rename" to update
     4. Scroll down to "Description" and add your project description
     5. Click "Save changes"

3. **Clone the Repository**

   - Click the green "Code" button
   - Copy the HTTPS URL (looks like `https://github.com/your-username/your-project-name.git`)
   - Open Terminal/Command Prompt
   - Navigate to your projects folder:

     ```bash
     # On Windows
     cd C:\Projects
     # On Mac/Linux
     cd ~/Projects
     ```

   - Clone your fork:

     ```bash
     git clone https://github.com/your-username/your-project-name.git
     cd your-project-name
     ```

4. **Configure Cursor**

   - Open Cursor IDE
   - Click "File" → "Open Folder"
   - Select the `hackamatic` folder you just created
   - Wait for Cursor to load and index the project
   - Ensure the `.cursor` directory is visible in the file explorer

## 📂 Project Structure

```plaintext
hackamatic/
├── src/           # Your project code will go here
├── docs/          # Project documentation
│   ├── REQUIREMENTS.md
│   ├── SETUP.md
│   └── ...
└── .cursor/       # Cursor IDE configuration and rules
    └── rules/     # AI guidance rules
```

## 🎯 Development Phases

### Phase 1: Ideation

1. **Bounty Setup**

   - Have your hackathon bounty link ready
   - Open Cursor IDE
   - Open the chat tab by clicking on the chat icon on the left or by pressing `Ctrl+L`
   - Select the Composer tab and toggle the `agent` switch to on
   - Type in the chat: "I want to start a new project with this bounty: [your-bounty-link]"
   - The AI will create a `BOUNTY-DESCRIPTION.md` file with analyzed requirements

2. **Project Ideation**

   - The AI will guide you through brainstorming
   - Discuss your ideas with the AI
   - Ask for suggestions and feedback
   - The AI will help document your final idea

### Phase 2: Architecture

1. **System Design**

   - The AI will help create `ARCHITECTURE.md`
   - Discuss your technical preferences
   - No technical knowledge required - the AI will explain everything
   - Ask questions about any terms you don't understand

2. **Technology Selection**

   - The AI will suggest appropriate technologies
   - Explain your preferences or constraints
   - The AI will document all technical decisions

### Phase 3: Development

1. **Project Initialization**

   - The AI will set up your project structure
   - Create necessary configuration files
   - Initialize the development environment
   - Command explanations:

     ```bash
     # Create project directories
     mkdir src
     mkdir src/components  # For UI components
     mkdir src/services    # For backend services
     ```

2. **Development Process**

   - Start with small components
   - Type in chat: "Help me create [feature-name]"
   - The AI will guide you through implementation
   - Test each feature as it's built

3. **Code Organization**

   - Follow the AI's suggested structure
   - Keep related files together
   - Ask the AI to explain any code it generates
   - Regular commits:

     ```bash
     git add .
     git commit -m "Add feature: [feature-name]"
     ```

### Phase 4: Deployment

1. **Preparation**

   - The AI will help create deployment configurations
   - Set up necessary accounts (the AI will guide you)
   - Prepare environment variables
   - Test the application locally

2. **Deployment Steps**

   - Follow AI-guided deployment process
   - Verify each step before proceeding
   - Document deployment details
   - Test the deployed application

## 🔍 Using AI Assistance

1. **Basic Commands**

   - "Help me with [task]" - Get guidance on any task
   - "Explain [concept]" - Get detailed explanations
   - "Show me how to [action]" - Get step-by-step instructions
   - "What does [term] mean?" - Get terminology explanations

2. **Best Practices**

   - Ask questions frequently
   - Request explanations for unclear terms
   - Let the AI guide your development
   - Save and commit changes regularly

## ❓ Troubleshooting

If you encounter issues:

1. **Cursor IDE Issues**

   - Ensure Cursor is up to date
   - Try restarting Cursor
   - Check internet connection
   - Verify AI features are enabled

2. **Git Issues**

   - Common error: "Permission denied"

     ```bash
     # Fix by checking your credentials
     git config --list
     ```

   - Error: "Changes not staged"

     ```bash
     # Check status and add changes
     git status
     git add .
     ```

3. **Development Issues**

   - Ask the AI for help with error messages
   - Request step-by-step debugging
   - Save work frequently

## 📚 Additional Resources

- [Cursor Documentation](https://cursor.sh/docs) - Learn more about Cursor IDE
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) - Learn Git fundamentals
- [Markdown Guide](https://www.markdownguide.org/) - Learn how to write documentation
- Project [README.md](../README.md) - Project overview and quick start

## 🤝 Getting Help

- Type your questions in the Cursor AI chat
- Be specific about what you need help with
- Don't hesitate to ask for clarification
- The AI will guide you through each step

Remember: There are no "stupid questions" - the AI is here to help you learn and build your project!
