from flask import Flask, render_template, request
from urllib.parse import quote

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sent = False
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        tattoo = request.form.get('tattoo', '').strip()
        date = request.form.get('date', '').strip()
        message = quote(f"Hello Ryan Tattoos and Art Studio!\nName: {name}\nPhone: {phone}\nTattoo idea: {tattoo}\nPreferred date: {date or 'Not specified'}")
        return render_template('index.html', whatsapp_message=message, sent=True)
    return render_template('index.html', whatsapp_message='', sent=False)

if __name__ == '__main__':
    app.run(debug=True)
