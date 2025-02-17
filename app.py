from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=100
    )

    return jsonify({"response": response["choices"][0]["text"].strip()})

if __name__ == "__main__":
    app.run(debug=True)
