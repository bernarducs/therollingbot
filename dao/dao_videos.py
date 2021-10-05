from time import sleep
from re import findall
from youtubesearchpython import VideosSearch, CustomSearch, VideoSortOrder
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import fadein, fadeout
from moviepy.audio.fx.all import audio_fadein, audio_fadeout
from twitter_api.twitter_api import conn


api = conn()


def search_videos(search, limit):
    results = VideosSearch(search, limit=limit)
    return results.result()


def find_three_links(search):
    searches = search_videos(search, 3)
    results = list()
    for search in searches['result']:
        name = search['title']
        link = search['link']
        channel = search['channel']['name']
        results.append((name, link, channel))
    return results


def last_24h_new_videos(search, limit=24):
    custom_search = CustomSearch(search,
                                VideoSortOrder.uploadDate,
                                limit=limit)

    results = custom_search.result()['result']
    last_24h = [
        v for v in results
        if v['publishedTime'] is not None and
        findall(r'hour', v['publishedTime'])
    ]
    return last_24h


def post_news_videos():
    new_videos = last_24h_new_videos("rolling stones")
    if new_videos:
        vid_twt_id = None
        intro = "recently uploaded videos on youtube: "
        for nv in new_videos[::-1]:
            title = nv.get("title")
            link = nv.get("link")
            nv_txt = f"{intro} {title} {link}"
            intro = ""
            print(nv_txt)
            nv_twt = api.update_status(nv_txt, vid_twt_id)
            vid_twt_id = nv_twt.id
            sleep(5)


def video_song(song_name):
    # grab the first video
    searches = find_three_links(f"the rolling stones {song_name}")
    for search in searches:
        if search[2] in ['The Rolling Stones', 'ABKCOVEVO']:
            link = search[1]
            break
        else:
            link = search[1]

    if not link:
        return False

    yt = YouTube(link)
    name_video = "clip.mp4"

    # download the vid
    try:
        yt.streams.filter(progressive=True,
                          res='360p',
                          file_extension='mp4').first().download(
            filename=name_video)

        # cut the vid, add fade in and out, the save it
        clip = VideoFileClip(name_video).subclip(5, 35)
        # clip = clip.resize(480, 360)
        clip = fadein(clip, duration=1)
        clip = fadeout(clip, duration=5)
        clip = audio_fadein(clip, duration=1)
        clip = audio_fadeout(clip, duration=5)
        clip.write_videofile(name_video, codec="libx264", audio_codec="aac")

        media = api.media_upload(filename=name_video,
                                 media_category="tweet_video")
        return media
    except AttributeError as e:
        print(e)
