from pexels_api.video import VideoPexels

api_key = "YOUR_API_KEY"
api = VideoPexels(api_key)

# api.search_videos("nature", orientation="portrait")
result = api.get_vimeo_video_as_bytes("https://player.vimeo.com/external/408365061.sd.mp4?s=9722472a80e91b760847038bd35bdfbbe0aa6ce5&profile_id=139&oauth2_token_id=57447761")
with open("video.mp4", "wb") as f:
    f.write(result)