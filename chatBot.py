from multiflow import Workflow
import os

os.environ['MULTIFLOW_API_KEY'] = "b3d199d0-3f40-4ab8-a473-c81b5d2bc4e6"

def run_chatbot():
    w = Workflow("Chat")
    prev_messages = []
    while True:
        your_message = input("Me: ")
        response = w.run("\n".join(prev_messages), your_message)["outputs"][-1].lstrip().rstrip()
        prev_messages.append("SweinternBot: " + response)
        print("SweinternBot: ", response)
    
if __name__ =="__main__":
    run_chatbot()