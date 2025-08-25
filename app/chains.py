import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain.output_parsers import OutputFixingParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama3-70b-8192"
        )

    def _split_text(self, text, chunk_size=2000, chunk_overlap=200):
        """Split large scraped text into smaller chunks for LLM processing."""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.split_text(text)

    def extract_jobs(self, cleaned_text):
        """Extract job postings from scraped page text."""
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE
            {page_data}
            
            ### INSTRUCTIONS
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format
            containing the following keys: `role`, `experience`, `skills`, and `description`.
            
            Only return **valid JSON**. Do not include explanations or preambles.
            ### VALID JSON (NO PREAMBLE)
            """
        )

        chain_extract = prompt_extract | self.llm
        json_parser = JsonOutputParser()
        fixing_parser = OutputFixingParser.from_llm(parser=json_parser, llm=self.llm)

        all_jobs = []
        chunks = self._split_text(cleaned_text)

        for chunk in chunks:
            try:
                result = chain_extract.invoke({"page_data": chunk})
                res = fixing_parser.parse(result.content)
                if isinstance(res, list):
                    all_jobs.extend(res)
                else:
                    all_jobs.append(res)
            except OutputParserException:
                # skip bad chunks instead of breaking everything
                continue  

        return all_jobs

    def write_mail(self, jobs, links):
        """Generate a cold email for a given job description and portfolio links."""
        prompt_email = PromptTemplate.from_template(
            '''
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Kirtirajsinh Parmar, a Business Development Executive at NexaCore Solutions. 
            NexaCore is an AI and Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools.

            Over our experience, we have empowered numerous enterprises with tailored solutions, 
            fostering scalability, process optimisation, cost reduction, and heightened overall efficiency.

            Your job is to write a cold email to the client regarding the job mentioned above, 
            describing the capability of NexaCore in fulfilling their needs.

            Also add the most relevant ones from the following links to showcase NexaCore's portfolio: {link_list}

            Remember that you are Kirtirajsinh Parmar, BDE at NexaCore Solutions.
            ### EMAIL (NO PREAMBLE)
            '''
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({
            "job_description": str(jobs),
            "link_list": links
        })
        return res.content


if __name__ == "__main__":
    print("GROQ_API_KEY loaded:", os.getenv("GROQ_API_KEY") is not None)
