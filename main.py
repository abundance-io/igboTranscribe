from flask import Flask,render_template,request, send_file,json
from utils import process_text
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def main():
    if request.method == "POST":
        text = request.form.get('entry')
        if text:
            sound_map = process_text(text)        
            sound_times = list(map(lambda x:x[1], sound_map))
            print(sound_map)
        return render_template("index.html",show_audio=True,sound_map=sound_map,sound_times = sound_times)

    else: 
        return render_template('index.html',show_audio=False)




@app.route("/audio")
def get_audio():
    return send_file("merged",mimetype="audio/mp3")

