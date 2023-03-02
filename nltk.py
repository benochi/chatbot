import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hello",
        ["Hello", "Hi there"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot. Nice to meet you!"]
    ],
    [
        r"how are you?",
        ["I'm doing well. Thanks for asking."]
    ],
    [
        r"bye",
        ["Bye!", "Goodbye!"]
    ],
]

def chatbot():
    print("Hello, I'm Chatbot! How can I help you today?")

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
