from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

from dotenv import load_dotenv

load_dotenv()


def lanchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
        tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run("What is the average age of a dog? Multiply the age by 3 twice")

    return result


if __name__ == "__main__":
    print(lanchain_agent())
