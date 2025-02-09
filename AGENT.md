# AGENT INSTRUCTIONS

## Project Metadata

```json
{
  "project_name": "Hackamatic",
  "project_type": "hackathon_template",
  "primary_purpose": "AI-powered hackathon project generator",
  "development_status": "template",
  "target_users": "hackathon_participants",
  "repository_structure": {
    "src": "main source code directory",
    "docs": "documentation files",
    ".cursor/rules": "AI assistant rules and guidelines"
  }
}
```

## Project Phases

```json
{
  "development_workflow": {
    "phase_1": {
      "name": "ideation",
      "activities": [
        "bounty_analysis",
        "project_ideation",
        "requirements_definition"
      ],
      "artifacts": ["docs/REQUIREMENTS.md"]
    },
    "phase_2": {
      "name": "architecture",
      "activities": [
        "system_design",
        "component_architecture",
        "technical_specifications"
      ],
      "artifacts": ["docs/ARCHITECTURE.md"]
    },
    "phase_3": {
      "name": "development",
      "activities": [
        "implementation",
        "testing",
        "documentation"
      ],
      "artifacts": ["src/*"]
    },
    "phase_4": {
      "name": "deployment",
      "activities": [
        "infrastructure_setup",
        "environment_configuration",
        "application_deployment"
      ],
      "artifacts": ["docs/DEPLOYMENT.md"]
    }
  }
}
```

## File Organization Schema

```json
{
  "documentation": {
    "root_level": [
      "README.md",
      "AGENT.md",
      "LICENSE"
    ],
    "docs_directory": [
      "REQUIREMENTS.md",
      "SETUP.md",
      "ARCHITECTURE.md",
      "DEPLOYMENT.md"
    ]
  },
  "source_code": {
    "primary_directory": "src/",
    "test_directory": "tests/",
    "configuration_files": [
      "package.json",
      "requirements.txt",
      "config/*"
    ]
  }
}
```

## AI Assistant Instructions

```json
{
  "cursor_rules_location": ".cursor/rules/",
  "available_rules": [
    "architecture-phase",
    "deployment-phase",
    "development-phase",
    "markdown-standards",
    "project-organization"
  ],
  "documentation_standards": {
    "format": "markdown",
    "emoji_usage": true,
    "header_hierarchy": "max_3_levels",
    "code_blocks": "language_specified"
  }
}
```

## Project Dependencies

```json
{
  "development_environment": {
    "ide": "Cursor",
    "ai_assistance": true,
    "version_control": "git"
  },
  "required_setup": {
    "repository_clone": true,
    "environment_initialization": true,
    "documentation_review": true
  }
}
```

## Interaction Guidelines

```json
{
  "ai_agent_tasks": {
    "project_initialization": {
      "priority": "high",
      "required_actions": [
        "clone_repository",
        "read_requirements",
        "setup_environment"
      ]
    },
    "development_assistance": {
      "priority": "high",
      "capabilities": [
        "code_generation",
        "documentation_updates",
        "testing_support",
        "deployment_guidance"
      ]
    },
    "documentation_maintenance": {
      "priority": "medium",
      "focus_areas": [
        "technical_documentation",
        "setup_guides",
        "architecture_updates"
      ]
    }
  }
}
```

## Project Constraints

```json
{
  "documentation": {
    "format": "markdown",
    "standards": "strict",
    "validation_required": true
  },
  "code_quality": {
    "linting_required": true,
    "testing_required": true,
    "documentation_required": true
  },
  "deployment": {
    "environment_setup_required": true,
    "configuration_management_required": true
  }
}
```

## Error Handling

```json
{
  "documentation_errors": {
    "action": "auto_fix",
    "validation_required": true
  },
  "code_errors": {
    "action": "report_and_suggest",
    "logging_required": true
  },
  "deployment_errors": {
    "action": "halt_and_report",
    "rollback_required": true
  }
}
```
