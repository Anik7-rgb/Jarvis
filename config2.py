import openai

# Set the new API key
openai.api_key = "API KEY"

try:
    # Make a simple request (like listing models)
    response = openai.Model.list()
    print(response)
except openai.error.AuthenticationError:
    print("Authentication failed. Please check your new API key.")
except Exception as e:
    print(f"Error: {e}")
