from tabnanny import verbose
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from config import settings
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo", openai_api_key=settings.openai_api_key
    )
    template = """given full name {name_of_person} I want you to get me a link to their LinkedIn profile page.
      Your answer should only contain the URL of the profile page and nothing else"""

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 LinkedIn profile page",
            func=get_profile_url,
            description="useful for when you need to get the LinkedIn page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linkedin_profile_url
