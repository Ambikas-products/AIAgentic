import requests
import openai
# Load API keys
with open("keys/openweather_key.txt", "r") as f:
    weather_key = f.read().strip()
with open("keys/openai_key.txt", "r") as f1:
    openai_key = f1.read().strip()

def router_agent(prompt):
    # Initialize OpenAI client with API key
    client = openai.OpenAI(api_key=openai_key)
    
    # First, get routing decision
    route_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are an LLM router agent. You are to route the user input to the correct model.
                If the user input requires extensive reasoning, respond with 'ROUTE: REASONING_AGENT'
                If the user request involves mathematical calculations or coding tasks, respond with 'ROUTE: REASONING_AGENT'
                If the user request just needs a simple conversational answer, respond with 'ROUTE: CONVERSATIONAL_AGENT'
                
                The routing decision is based on:
                - Complexity of reasoning required
                - Presence of mathematical or coding elements
                - Overall task difficulty
                
                Respond ONLY with the routing decision in the format 'ROUTE: AGENT_NAME'."""},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Get the routing decision
    route = route_response.choices[0].message.content.strip()
    
    # Route to appropriate agent based on decision
    if route == "ROUTE: REASONING_AGENT":
        return reasoning_agent(prompt)
    elif route == "ROUTE: CONVERSATIONAL_AGENT":
        return conversational_agent(prompt)
    else:
        return "Error: Invalid routing decision"

def reasoning_agent(prompt):
    client = openai.OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a LLM Reasoning agent. You excel at complex problem-solving, mathematical calculations, and coding tasks. Provide detailed, step-by-step explanations when appropriate."""},
            {"role": "user", "content": prompt}
        ]
    )
    # Return just the message content from the response
    return response.choices[0].message.content

def conversational_agent(prompt):
    client = openai.OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a LLM Conversational agent. You excel at friendly, natural dialogue and providing helpful responses to general queries. Keep responses concise and engaging."""},
            {"role": "user", "content": prompt}
        ]
    )
    # Return just the message content from the response
    return response.choices[0].message.content

def main():
    # Test case 1: Simple conversational query
    print("\n=== Test Case 1: Simple Greeting ===")
    print("User Input: Hello!")
    response = router_agent("Hello!")
    print("Response:", response)

    # Test case 2: Complex reasoning query
    print("\n=== Test Case 2: Mathematical Problem ===")
    print("User Input: Calculate the fibonacci sequence")
    response = router_agent("Calculate the fibonacci sequence")
    print("Response:", response)

if __name__ == "__main__":
    main()
    