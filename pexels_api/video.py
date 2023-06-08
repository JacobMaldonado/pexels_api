import requests

class VideoPexels:
    
    def __init__(self, token) -> None:
        self.token = token
        
    def search_videos(self, query, per_page=80, page=1, orientation="landscape"):
        url = "https://api.pexels.com/videos/search"
        response = requests.get(
            url, 
            headers={"Authorization": self.token}, 
            params={"query": query, "per_page": per_page, "page": page, "orientation": orientation}
            )
        return response.json()
    
    def get_vimeo_video_as_bytes(self, vimeo_url):
        response = requests.get(vimeo_url, stream=True)
        if response.status_code == 200:
            video_data = response.content
            return video_data
        else:
            print(f"Failed to download video: {response.status_code}")
            return None