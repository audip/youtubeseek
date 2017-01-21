from __future__ import unicode_literals
import youtube_dl


class ErrorLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def a_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting to wav')

def get_video(url):
    ydl_opts = {
        'format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '64',
        }],
        'logger': ErrorLogger(),
        'progress_hooks': [a_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # ydl.download(['https://www.youtube.com/watch?v=urU_0Qaz9Ao'])
        ydl.download([url])
