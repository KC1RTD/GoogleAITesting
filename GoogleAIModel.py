# Import the Python SDK
import google.generativeai as genai

# Used to securely store your API key
genai.configure(api_key='xxxxxxxxxxxxxxxxxxx')


model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about sad 58 year old guy whose name is XXXX")

print(response.text)
