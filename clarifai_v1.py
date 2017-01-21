from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi("YQhKk98oRlSgA5aTidpw4eAV1OM7QYCrADEjApdf", "DRSbu9eVjQG7laNamJzS3c2nMFAvyDLDJYSPPKa_", language="en")
import pafy


def get_video_url(url):
# Get mp4 video URL based on youtube link
    video = pafy.new(url)
    streams = video.streams
    for s in streams:
        if str(s.extension)!="mp4":
            continue
        return s.url
    return None

def fetch_video_tags(url):
# Fetch tags using Clarif.AI
    video_url = get_video_url(url)
    if video_url is None:
        raise ConnectionError("URL not found, check again.")
    result = clarifai_api.tag_urls(video_url)
    return result["results"]

def match_tags(tags):
# Search tags in video
    pass

# Local File
# result = clarifai_api.tag_image_base64(open('/Users/USER/my_video.mp4'))
if __name__=='__main__':
    print(fetch_video_tags('https://www.youtube.com/watch?v=PT2_F-1esPk'))
