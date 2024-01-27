import requests

class igdown():
    @staticmethod
    def getCsrf() -> None:
        try:
            url = "https://instagram.com/data/shared_data/"
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            try:
                return requests.get(url, headers=headers).json()['config']['csrf_token']
            except:
                return None
        except Exception as e:
            print(str(e))
    
    
    @staticmethod
    def downloadVideo(link: str) -> str:
        try:
            url = "https://i.instagram.com/api/v1/oembed?url={}".format(link)
            vardxg = requests.get(url)
            if (vardxg.json()['thumbnail_url'] or vardxg.status_code != 404):
                try:
                    with open(f"{vardxg.json()['media_id']}.jpg", 'wb') as file:
                        picture = vardxg.json()['thumbnail_url']
                        res = requests.get(picture).content
                        file.write(res)
                        file.close()
                    return print("Downloaded Picure!")
                except FileNotFoundError:
                    print("File not saved and not find")
            else:
                print("Failed download picture or picture not found!")
        except Exception as e:
            print(str(e))