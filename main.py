from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

'''
See the HipChat api documentation for how to get a user access token.
https://developer.atlassian.com/hipchat/guide/hipchat-rest-api/api-access-tokens
'''

# gitter api token 291b8aa0b216cbf5d6429b215f979ada5e0a4ba9

chatbot = ChatBot(
    "PetBot",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    #_host="https://archbang.hipchat.com",
    gitter_room="autio/main",
    gitter_api_token="291b8aa0b216cbf5d6429b215f979ada5e0a4ba9",
    gitter_only_respond_to_mentions=False,
    input_adapter="chatterbot.input.Gitter", #TerminalAdapter",
    output_adapter="chatterbot.output.Gitter",
    database="./database.json"
)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "What's up?",
    "Things are swell.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

while True:
    try:
        bot_input = chatbot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

