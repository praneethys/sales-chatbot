from os import environ
from typing import List
from langchain import HuggingFaceHub, PromptTemplate
from langchain.chains import ConversationalRetrievalChain, ConversationChain
from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface_hub import HuggingFaceHubEmbeddings
from langchain.docstore.document import Document
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from dotenv import load_dotenv, find_dotenv
from os import getenv, path

load_dotenv(find_dotenv())  # read local .env file


class LLM:
    def __init__(self) -> None:
        # self.huggingface_repo_id = 'decapoda-research/llama-7b-hf' # model keeps timing out
        # self.huggingface_repo_id = 'mosaicml/mpt-7b-chat' # model times out
        self.huggingface_repo_id = 'bigscience/bloom' # works

        self.huggingface_api_token = getenv('HUGGINGFACEHUB_API_TOKEN')

        environ['HUGGINGFACEHUB_API_TOKEN'] = self.huggingface_api_token

        # List of all tasks can be found here: https://github.com/huggingface/hub-docs/blob/main/tasks/src/const.ts
        self.llm = HuggingFaceHub(repo_id=self.huggingface_repo_id,
                                  huggingfacehub_api_token=self.huggingface_api_token,
                                  verbose=True
                                  )
        self.conversation_memory = ConversationBufferMemory(return_messages=True,
                                                            memory_key='chat_history', 
                                                            input_key='question')

    def init_conversation_retrieval_chain(self, data: List[Document]) -> ConversationalRetrievalChain:
        embeddings = HuggingFaceHubEmbeddings(
            huggingfacehub_api_token=self.huggingface_api_token)
        vectorstore = FAISS.from_documents(data, embeddings)
        print(f'vector_store: {vectorstore}')

        # prompt = ChatPromptTemplate.from_messages([
        #     SystemMessagePromptTemplate.from_template(
        #         "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
        #     MessagesPlaceholder(variable_name="history"),
        #     HumanMessagePromptTemplate.from_template("{input}")
        # ])

#         template = """You are a sales person assisting customers choosing a bundle for their kids. \
#             Be kind, compelling and get them to buy a bundle. If you don't know the answer to a question \
#             simply answer that you don't know and that they need to speak to a human to get that answer. \
#             Provide answers in a tabular format if asked to compare bundles.
# {chat_history}
# Human: {question}
# Salesbot:"""

#         prompt = PromptTemplate(
#             input_variables=['chat_history', 'question'],
#             template=template,
#             validate_template=True
#         )

        chain = ConversationalRetrievalChain.from_llm(llm=self.llm,
                                                      retriever=vectorstore.as_retriever(),
                                                      verbose=True,
                                                      memory=self.conversation_memory,
                                                    #   condense_question_prompt=prompt
                                                      )

        print(f'conversation_retrieval_chain: {chain}')
        return chain

    def init_conversation_chain(self) -> ConversationChain:
        chain = ConversationChain(llm=self.llm,
                                  verbose=True,
                                #   memory=self.conversation_memory
                                  )
        print(f'conversation_chain: {chain}')
        return chain
