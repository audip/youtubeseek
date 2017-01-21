from flask import Flask, request, render_template
import json
from watsoncloud import downloader
from watsoncloud import transcribe
from watsoncloud import compilator

app = Flask(__name__)
base_url = "https://www.youtube.com/watch?v="

@app.route("/watch", methods=['GET'])
def home():
    video_id = request.args.get('v')
    if video_id is not None:
        # Download file and get path
        downloaded_file = downloader.get_video(base_url+video_id, video_id)
        print("DL file:"+downloaded_file)
        # Transcribe the downloaded file
        transcribed_file = transcribe.speech_to_text(downloaded_file)
        print("TC file:"+transcribed_file)
        # Compile words for transcribed file
        compiled_file = compilator.compile_word_transcript(transcribed_file)
        print("CL file:"+compiled_file)
        # Return [{keyword: timestamp}]
        return video_id
    else:
        return "Invalid parameters, usage: http://youtubeseek.com/watch?v=abcdefg"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
