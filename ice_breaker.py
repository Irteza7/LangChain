import json
from re import template
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from config import settings
from third_parties.linkedin import scrape_linkedin_profile, scrape_linkedin_profile_gist


# information = """Elon Reeve Musk (born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of September 2023, according to the Bloomberg Billionaires Index, and $253 billion according to Forbes, primarily from his ownership stakes in both Tesla and SpaceX.[4][5]

# Musk was born in Pretoria, South Africa, and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University in Kingston, Ontario. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics there. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and with $12 million of the money he made, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.  """


if __name__ == "__main__":
    print("Hello LangChain")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary 30 words
        2. two interesting facts about them (keep it in 3-4 words)
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0.2, model="gpt-3.5-turbo", openai_api_key=settings.openai_api_key
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_url = linkedin_lookup_agent(name="M. Irteza Khan")

    linkdin_data = scrape_linkedin_profile_gist(
        "https://gist.githubusercontent.com/Irteza7/16ba2fa6b8f9f5b00c95a2d139f428e7/raw/fda63aab2a0a9ce533aec555f0332710984db4de/gistfile1.txt"
    )

    linkdin_data_real = scrape_linkedin_profile(linkedin_url)
    print(chain.run(information=linkdin_data))

    # linkdin_data_json = json.dumps(linkdin_data)
    # print(linkdin_data_json)
