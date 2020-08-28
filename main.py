from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import os

bot = ChatBot('Celien')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

data = []
for files in os.listdir(r'\chatterbot-corpus-1.2.0'):
        if files.endswith('.yml'):
                data.append(open(files))
                bot.train(data)
				
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get("msg")
	return str(bot.get_response(userText))

if __name__ == "__main__":
	app.run()
