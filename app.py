from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

classmates = ["Sophia", "Valentina", "Julia W", "Lilian", "Julia W", 
              "Valerie", "Leonie M", "Hannah", "Leonie L", "Marie", 
              "Rosalie", "Zoe", "Elisabet", "John-Otto", "Philipp", 
              "Lena", "Antonia", "Caroline", "Sara", "Elina", "Irina", 
              "Georg", "Nicholas", "Marko", "Paul",]

def match():
    return random.randint(0, 100)

@app.route('/')
def home():
    return render_template('index.html', classmates=classmates)

@app.route('/match', methods=['POST'])
def match_names():
    data = request.json
    Per1 = data.get('person1')
    Per2 = data.get('person2')

    if Per1 not in classmates or Per2 not in classmates:
        return jsonify({"error": "Please enter valid names from the list of classmates."}), 400
    
    match_percent = match()
    
    if match_percent >= 80:
        message = f"Woah, you two really make a good couple at {match_percent}%!"
    elif 50 <= match_percent < 80:
        message = f"You two will have some ups and downs at {match_percent}%, but it'll work!"
    elif 20 <= match_percent < 50:
        message = f"Mm.. This will end up in a fight at {match_percent}%, I wouldn't if I were you.."
    elif 10 <= match_percent < 20:
        message = f"Ehh? No, just no, {match_percent}%"
    elif match_percent < 10:
        message = f"Yikes! Please do yourselves a favour and do NOT date at {match_percent}%!"
    else:
        message = f"HOLY MOLY?!? YOU TWO ARE THE PERFECT FIT AT {match_percent}%!!"

    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
