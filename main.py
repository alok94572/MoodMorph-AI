from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatOllama(model="llama3")

print("chosse your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode ")
print("press 3 for sad mode")

choice = int(input("tell your response :- "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

message = [
    SystemMessage(content=mode)
]
print("---------------- Welcome type 0 to exit the application ----------------")

while True:
    

    prompt = input("You: ")
    message.append(HumanMessage(content=prompt))
    if prompt == "0":
        break

    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot: ", response.content)

print(message)