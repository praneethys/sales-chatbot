from app import App
from llm import LLM
from langchain.document_loaders.csv_loader import CSVLoader

if __name__ == '__main__':
    print('-----------------------------------------')
    app = App()
    llm = LLM()

    loader = CSVLoader(file_path='/Users/praneeth/Documents/ml/marketing-chatbot/data/pricing.csv',
                       encoding="utf-8", 
                       csv_args={'delimiter': ','})
    data = loader.load()
    print(f'data: {data}')

    conversation_retrieval_chain = llm.init_conversation_retrieval_chain(data)
    conversation_chain = llm.init_conversation_chain()

    input = app.get_user_input()

    if input:
        # output = conversation_chain.predict(input=input)
        # print(f'conversation_chain output: {output}')

        output = conversation_retrieval_chain(inputs={"question": input, 
                                                      "chat_history": app.get_history()},
                                              return_only_outputs=True)

        print(f'conversation_retrieval_chain output: {output}')
        app.set_generated_message_state(output['answer'])
        app.set_history(input, output['answer'])

    app.create_chat_component()
