from flask import Flask, render_template, request, jsonify
import random
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Sample responses with CBT principles
responses = {
    "anxiety": [
        "I understand that anxiety can be overwhelming. Have you tried deep breathing exercises?",
        "It might help to challenge negative thoughts. What's the worst that could happen?"
    ],
    "depression": [
        "You're not alone. Have you talked to someone about how you're feeling?",
        "Try engaging in an activity you enjoy. Small steps can help."
    ],
    "stress": [
        "Stress is a natural response. Have you tried mindfulness or meditation?",
        "It might help to take a break and refocus. What usually helps you relax?"
    ],
    "default": [
        "I'm here to listen. Could you tell me more about how you're feeling?",
        "That sounds tough. Would you like some grounding techniques to help?"
    ],
    "hi": [
        "Hello, how are you today?"
    ],
    "good": [
        "Good to hear! How can I help you?"
    ],
    "no": [
        "That's okay! Here are some techniques you can try:\n\n"
        "- **4-7-8 Breathing**: Inhale for 4 seconds, hold for 7 seconds, exhale for 8 seconds.\n"
        "- **Progressive Muscle Relaxation**: Tense and relax each muscle group slowly.\n"
        "- **Grounding Technique**: Name 5 things you can see, 4 things you can touch, 3 things you hear, 2 things you smell, 1 thing you taste."
    ],
    "dance": [
        "Dancing is a great way to relieve stress! Put on your favorite song and dance it out!",
        "Moving your body can lift your mood. Try a short dance break!"
    ],
    "sing":[
        "Wow,so let's starts with your favorite song,my favorite song is 'lag ja gale' by Lata Mangeshkar,tell me yours?"
    ],
    "favorite":[
        "Exciting,breath for 1 minute and sing"
        "ohh let's go for it"
    ],
    "make me relax": [
        "Here are some relaxation techniques you can try:\n\n"
        "- **Meditation**: Close your eyes and focus on your breathing for a few minutes.\n"
        "- **Listening to Music**: Play some calming or favorite tunes.\n"
        "- **Stretching**: Try light stretching to relieve tension.\n"
        "- **Visualization**: Imagine a peaceful place like a beach or forest."
    ]
}

def get_response(user_input):
    doc = nlp(user_input.lower())
    for token in doc:
        if token.lemma_ in responses:
            return random.choice(responses[token.lemma_])
    return random.choice(responses["default"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)