from flask import Flask, request
import csv
from flask_ngrok import run_with_ngrok
from datetime import datetime

app = Flask (__name__)
run_with_ngrok(app)

@app.route('/', methods = ['POST'])
def webhook():
    data = request.get_json()
    try:
        with open('STT_statistics.csv', 'a', encoding=('utf-8-sig'), newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([datetime.now(), data["stt_answer"]])
    except PermissionError:
        input('Close the window and press Enter.\n')
        with open('STT_statistics.csv', 'a', encoding=('utf-8-sig'), newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([datetime.now(), data["stt_answer"]])

    return 'Webhook recieved successfully', 200

if __name__ == '__main__':
    app.run()