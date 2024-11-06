from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Ana sayfa rotası
@app.route('/')
def home():
    return render_template('index.html')

# Chatbot için cevap döndüren rota
@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    response_text = "Bu konuyla ilgili bir yanıt bulamadım."

    # Veritabanına bağlan ve anahtar kelimeleri ara
    with sqlite3.connect('/home/esa/Desktop/end_game/deneme_website/db/kullaniciGirdileri') as conn:
        cursor = conn.cursor()
        query = """
        SELECT botCevabi FROM kullaniciGirdileri
        WHERE kullaniciCevap1 LIKE ? OR kullaniciCevap2 LIKE ? OR kullaniciCevap3 LIKE ?
        """
        cursor.execute(query, ('%' + user_message + '%', '%' + user_message + '%', '%' + user_message + '%'))
        result = cursor.fetchone()
        if result:
            response_text = result[0]

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
