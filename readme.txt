Building Effective Agents Cookbook :: Inspiration Anthropic blog published 12/19/24 on Agentic Routing
 

This repository contains example minimal implementations of common agent workflows discussed in the blog:

Basic Building Blocks
Prompt Chaining
Routing

# AI Router Agent System

A Python-based routing system that intelligently directs user queries to specialized AI agents based on the query's complexity and nature.

## Overview

This system uses OpenAI's GPT-3.5 Turbo model to create a three-agent architecture:
- **Router Agent**: Analyzes user input and routes to appropriate specialized agent
- **Reasoning Agent**: Handles complex queries, mathematical problems, and coding tasks
- **Conversational Agent**: Manages simple, conversational interactions

## How It Works

1. User submits a query to the router agent
2. Router agent analyzes the query and determines the appropriate specialized agent
3. Query is forwarded to either the reasoning or conversational agent
4. Selected agent processes the query and returns the response

## Requirements

- Python 3.x
- OpenAI API key
- Requests library

## Setup

1. Create a `keys` directory in the project root
2. Add your OpenAI API key to `keys/openai_key.txt`
3. Add your OpenWeather API key to `keys/openweather_key.txt` (if weather functionality is needed)

## Usage


response = router_agent("Hello!")
from router import router_agent

python
python
from router import router_agent

Simple query (will route to conversational agent)
response = router_agent("Hello!")
Complex query (will route to reasoning agent)
response = router_agent("Calculate the fibonacci sequence")

=== Test Case 1: Simple Greeting ===
User Input: Hello!
Response: [Conversational agent response]
=== Test Case 2: Mathematical Problem ===
User Input: Calculate the fibonacci sequence
Response: [Reasoning agent response]


## Features

- Automatic query routing based on complexity
- Specialized agents for different types of queries
- Clear separation of concerns between routing and processing
- Easy to extend with additional specialized agents

This README provides:
1. A clear overview of the system
2. Setup instructions
3. Usage examples
4. System requirements
5. Example output
6. Key features
