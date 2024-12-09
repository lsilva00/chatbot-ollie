from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Carregar perguntas e respostas do arquivo de texto
def load_questions(file_path):
    questions = {}
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        question, answer = None, None
        for line in lines:
            if line.startswith("Pergunta:"):
                question = line.replace("Pergunta:", "").strip()
            elif line.startswith("Resposta:"):
                answer = line.replace("Resposta:", "").strip()
                if question and answer:
                    questions[question] = answer
                    question, answer = None, None
    return questions

questions_data = load_questions("questions.txt")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "").strip()
    response = questions_data.get(question, "Desculpe, ainda não sei sobre este assunto!")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

