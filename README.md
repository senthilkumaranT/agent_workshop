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

## Key Features

- **Model Agnostic**: Unified interface to 23+ model providers
- **Highly Performant**: Agents instantiate in ~3μs and use ~6.5Kib memory on average
- **Reasoning Support**: Built-in reasoning capabilities for complex autonomous agents
- **Multi-Modal**: Native support for text, image, audio, and video
- **Advanced Multi-Agent Architecture**: Industry-leading agent teams with reasoning, memory, and shared context
- **Built-in Search**: Agentic search with 20+ vector databases
- **Memory & Storage**: Built-in memory and session storage drivers
- **Structured Outputs**: Fully-typed responses using model-provided structured outputs
- **FastAPI Integration**: Pre-built FastAPI routes for production deployment
- **Monitoring**: Real-time agent monitoring on agno.com

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

## Why Agno?

Agno helps you build best-in-class, highly-performant agentic systems, saving you hours of research and boilerplate. The framework provides:

- Model agnostic approach with no lock-in
- Lightning-fast agent instantiation
- First-class reasoning capabilities
- Native multi-modal support
- Advanced multi-agent architecture
- Built-in agentic search and RAG
- Comprehensive memory and storage solutions
- Structured output support
- Production-ready FastAPI integration
- Real-time monitoring capabilities

## Examples

The project includes examples of:
- Basic agent setup with Ollama models
- Multi-agent coordination
- Web search integration
- Financial data retrieval
- Tool integration and reasoning

Explore the code files to see these concepts in action! 