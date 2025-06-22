import yt_dlp

def download_tiktok_audio(url, filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Скачано: {filename}")
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")

if __name__ == "__main__":
    import os
    os.makedirs("downloads", exist_ok=True)

    with open("links.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for i, url in enumerate(urls, 1):
        print(f"Скачиваем аудио #{i} из {url}")
        download_tiktok_audio(url, f"downloads/audio_{i}.mp3")
