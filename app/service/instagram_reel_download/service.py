from yt_dlp import YoutubeDL


class Service:
    __CONTENT_DIR = 'content'
    __FORMAT = 'mp4'

    def download(self, url: str, filename: str):
        ydl_opts = {
            'format': self.__FORMAT,
            'outtmpl': f'{self.__CONTENT_DIR}/{filename}',
            'merge_output_format': self.__FORMAT,
            'quiet': False,
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            print(f"❌ Error: {e}")


service = Service()