from flask import Flask, request, render_template
import json
import downloader
from watsoncloud import transcribe

app = Flask(__name__)
base_url = "https://www.youtube.com/watch?v="

@app.route("/watch", methods=['GET'])
def home():
    video_id = request.args.get('v')
    if video_id is not None:
        downloader.get_video(base_url+video_id)
        transcribe.speech_to_text('projects/obama-weekly-address-2015-10-31/')
        return video_id
    else:
        return "Invalid parameters, usage: http://youtubeseek.com/watch?v=abcdefg"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
