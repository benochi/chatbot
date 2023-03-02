from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
bot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot using the english corpus
trainer.train('chatterbot.corpus.english')

# Start the chatbot
while True:
    user_input = input('You: ')
    bot_response = bot.get_response(user_input)
    print('Bot: ', bot_response)
