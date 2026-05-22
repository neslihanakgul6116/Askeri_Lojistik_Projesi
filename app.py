import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from worker import buyuk_veri_analiz_et

current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder_path = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_folder_path)
CORS(app)

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def dosya_yukle():
    dosya_adi = "hava_ussu_envanter_loglari.csv"
    gorev = buyuk_veri_analiz_et.delay(dosya_adi)
    return jsonify({"task_id": gorev.id, "mesaj": "Askeri envanter analizi arka planda basladi!"})

@app.route('/durum/<task_id>', methods=['GET'])
def durum_kontrol_et(task_id):
    gorev = buyuk_veri_analiz_et.AsyncResult(task_id)
    
    if gorev.state == 'PROGRESS':
        yuzde = gorev.info.get('current', 0)
        return jsonify({'yuzde': yuzde, 'durum': 'DEVAM_EDİYOR'})
    elif gorev.state == 'SUCCESS':
        return jsonify({'yuzde': 100, 'durum': 'BİTTİ'})
    else:
        return jsonify({'yuzde': 0, 'durum': 'BAŞLIYOR'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)