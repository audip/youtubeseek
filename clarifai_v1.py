from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi("HKu2ARzbvjumCPiD8tJ9Go7wiFQRol8DYF80QKz2", "6wTENoEslZ14tEBLhbu_51JtQdodUhvHWz0qc3Ha", language="en")
import pafy


def get_video_url(url):
# Get mp4 video URL based on youtube link
    video = pafy.new(url)
    streams = video.streams
    video_pref = ["256x144","320x240","640x360","720x480","1280x720"]
    mp4_streams = {}
    # Needs optimization for speed
    for s in streams:
        if str(s.extension)!="mp4":
            continue
        mp4_streams[str(s.resolution)]=str(s.url)

    for v in video_pref:
        if v in mp4_streams:
            return mp4_streams[v]

    return None

def fetch_video_tags(url, tags):
# Fetch tags using Clarif.AI
    video_url = get_video_url(url)
    if video_url is None:
        raise ConnectionError("URL not found, check again.")
    result = clarifai_api.tag_urls(video_url, select_classes=tags)
    return result

# Local File
# result = clarifai_api.tag_image_base64(open('/Users/USER/my_video.mp4'))
if __name__=='__main__':
    print(fetch_video_tags(url, keywords))
