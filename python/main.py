import os
from flask import Flask, jsonify, request
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Initialiser l'application Flask
app = Flask(__name__)

# Définir la clé API pour MistralAI
api_key = os.environ["MISTRAL_API_KEY"]
client = MistralClient(api_key=api_key)
model = "codestral-mamba-latest"

@app.route('/', methods=['GET'])
def get_response():
    # Récupérer la question de l'utilisateur depuis les paramètres de la requête
    user_question = request.args.get('ask', 'Write a code python triange de Pascal')

    # Créer les messages de chat
    messages = [
        ChatMessage(role="user", content=user_question)
    ]

    # Obtenir la réponse du modèle
    chat_response = client.chat(
        model=model,
        messages=messages
    )

    # Récupérer le contenu de la réponse
    response_content = chat_response.choices[0].message.content

    # Définir le titre et la signature
    title = "❤️Bruno dev ❤️"

    # Retourner la réponse avec le titre dans la réponse JSON
    return jsonify({
        "title": title,
        "response": response_content
    })

if __name__ == '__main__':
    # Démarrer le serveur Flask
    app.run(host='0.0.0.0', port=5000)
