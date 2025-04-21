from urllib.parse import urlparse

from aiogram.filters import BaseFilter
from aiogram.types import Message

class InstagramVideoDownloadMiddleware(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        url = urlparse(message.text)

        if url.scheme == '':
            # not url message
            return False

        return url.netloc.endswith('instagram.com') and url.path.startswith('/reel/')