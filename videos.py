from pathlib import Path

from things import Thing
from templater import apply_template


class Video(Thing):
    def validate(self):
        pass

def get_videos():
    videos = {}
    fnames = Path('videos').rglob('*.yaml')
    for fname in fnames:
        vid = Video(fname)
        videos[vid.key] = vid
    return videos


def write_videos(videos):
    for key, vid in videos.items():
        filename = f'video_{key}.html'
        apply_template('video.html', filename, keys_from=vid)
