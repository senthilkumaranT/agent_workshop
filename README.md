# Agno Multi-Agent System

This project demonstrates the use of [Agno](https://docs.agno.com/introduction), a Python framework for building multi-agent systems with shared memory, knowledge, and reasoning.

## What is Agno?

Agno is a Python framework for building multi-agent systems with shared memory, knowledge, and reasoning. Engineers and researchers use Agno to build:

- **Level 1:** Agents with tools and instructions
- **Level 2:** Agents with knowledge and storage  
- **Level 3:** Agents with memory and reasoning
- **Level 4:** Agent Teams that can reason and collaborate
- **Level 5:** Agentic Workflows with state and determinism

## Project Overview

This repository contains examples of Agno agents:

### Files

- `agno_agent.py` - Basic Agno agent implementation
- `agno_multi_agent.py` - Multi-agent system with web search and finance capabilities
- `manual_agent.py` - Manual agent configuration example

### Multi-Agent System Features

The `agno_multi_agent.py` file demonstrates a sophisticated multi-agent system with three specialized agents:

1. **Web Agent** - Searches the web for information and news using DuckDuckGo
2. **Finance Agent** - Retrieves financial data and stock information using YFinance
3. **Multi-Agent Coordinator** - Coordinates between web search and finance agents


## Getting Started

1. Install Agno:
```bash
pip install agno
```

2. Run the multi-agent example:
```bash
python agno_multi_agent.py
```

## Documentation

For more information about Agno, visit the official documentation:
- [Agno Documentation](https://docs.agno.com/introduction)

