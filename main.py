import os

from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",

)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)
set_tracing_disabled(True)

agent = Agent(
    name="Greeting Agent",
    instructions="You are a greeting agent, your task is to greet the user with a friendly massage, when someine say hi you've reply back salam from Shumila, when some when say bye you've reply back Allah hafiz from Shumaila, when someone ask other than greeting say Shumaila is here just for greeting, can't answer anything else, sorry.",
    model=model
)
user_question = input("Enter your question: ")

result = Runner.run_sync(agent, user_question)

print(result.final_output)
