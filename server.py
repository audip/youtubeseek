from flask import Flask, request, render_template
import json
from watsoncloud import downloader
from watsoncloud import transcribe
from watsoncloud import compilator
import pafy


app = Flask(__name__)
base_url = "https://www.youtube.com/watch?v="

@app.route("/watch", methods=['GET'])
def home():
    video_id = request.args.get('v')
    if video_id is None:
        return "Invalid parameters, usage: http://youtubeseek.com/watch?v=abcdefg"
    # Download file and get path
    # TODO: Lowest quality MP4 download
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

@app.route("/audiosearch",methods=['GET'])
def audio_search():
    keywords = request.args.get('q')
    video_id = request.args.get('v')
    # Form youtube url
    url = base_url+video_id
    # Fetch video transcript_filename
    video = pafy.new(url)
    title = video.title
    filename = title + '-' + video_id + '.json'
    print(filename)
    # Form saved file name
    if keywords is None:
        return "Invalid parameters, usage: http://youtubeseek.com/audiosearch?v=abcedfg&q=man,woman"
    # Open file and
    with open('watsoncloud/projects/'+filename) as f:
        result = find_transcript_timestamps(f, keywords)
        # @return: dict {keyword1:[ts1,ts2,ts3],keyword2:[ts1,ts2,ts3],keyword3:[ts1,ts2,ts3]}
        return json.dumps(result)

@app.route("/videosearch",methods=['GET'])
def video_search():
    keywords = request.args.get('q')
    if keywords is None:
        return "Invalid parameters, usage: http://youtubeseek.com/videosearch?v=abcdefg&q=man,woman"
    result = find_tag_timestamps(f, keywords)
    # @return: dict {keyword1:[ts1,ts2,ts3],keyword2:[ts1,ts2,ts3],keyword3:[ts1,ts2,ts3]}
    return json.dumps(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
