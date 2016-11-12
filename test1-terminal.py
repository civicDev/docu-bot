from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

bot = ChatBot("DocuBot",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="data/database.db"
    )
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "data/romana"
)
print("porniti discutia... scrie-ti ceva (ctrl+c pentru oprire)")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break