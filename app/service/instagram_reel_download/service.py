from random import randint

from yt_dlp import YoutubeDL


class Service:
    __FORMAT = 'mp4'

    def download(self, url: str) -> str:
        filename = f'content/{randint(0, 1000000000)}.mp4'

        ydl_opts = {
            'format': self.__FORMAT,
            'outtmpl': filename,
            'merge_output_format': self.__FORMAT,
            'quiet': False,
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"❌ Error: {e}")


service = Service()