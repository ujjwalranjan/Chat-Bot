from flask import Flask, render_template, request, jsonify
import aiml
import os
from tf_idf import *
# kernel = aiml.Kernel()

# def load_kern(forcereload):
# 	if os.path.isfile("bot_brain.brn") and not forcereload:
# 		kernel.bootstrap(brainFile= "bot_brain.brn")
# 	else:
# 		kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
# 		kernel.saveBrain("bot_brain.brn")
#

app = Flask(__name__)
@app.route("/")
def hello():
	#load_kern(False)
	return render_template('chat.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
	message = str(request.form['chatmessage'])
	# # if message == "save":
	# #     kernel.saveBrain("bot_brain.brn")
	# #     return jsonify({"status":"ok", "answer":"Brain Saved"})
	# # elif message == "reload":
	# # 	load_kern(True)
	# # 	return jsonify({"status":"ok", "answer":"Brain Reloaded"})
	# # elif message == "quit":
	# # 	exit()
	# # 	return jsonify({"status":"ok", "answer":"exit Thank You"})
	# #
	# # # kernel now ready for use
	# else:
		# while True:
		#bot_response = kernel.respond(message)
		# print bot_response
	bot_response = previous_chats(message)
	#print(type(message))
	#return message
	return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(debug=True)
