#rule based on ai python chatbot
print("hello! welcome to chatbot")
print("you can ask me basic quetion, type 'bye' to exit from the bot")
#dictionary
responses = {
    "hello!": "hi, welcome. how i can help you",
    "how are you": "good. thankyou",
    "who are you": "i am ai chatbot",
    "motivate me": "go with flow",
    "happy": "great to hear that",
}

# use function to get response of chatbot
def get_responseofbot(userquestion):
    userquestion= userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
    return "i dont know yet."

# user input
while True:
    userinput = input("please ask your question:")
    reply = get_responseofbot(userinput)
    print("bot response :", reply)

    if "bye" in userinput.lower():
        break

