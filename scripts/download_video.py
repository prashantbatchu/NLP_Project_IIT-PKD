import yt_dlp
import os

nda_urls = [
    # "https://www.youtube.com/live/V0I-UH0tleE?si=QQBKgJc0rc-DxURS ",
    # "PASTE_NDA_URL_2",
    # "https://www.youtube.com/live/V0I-UH0tleE?si=QQBKgJc0rc-DxURS ",
    # "https://www.youtube.com/live/ZIGV6RlNSnc?si=bWEYj2EJ5cSW3m1P" ,
    # "https://www.youtube.com/live/lX3uyD1Dg_I?si=cimWj0zxrkjRQkkG",
    # "https://www.youtube.com/live/q0rdJycUsSw?si=TTYy2oPjNoSVI2dx",
    # "https://www.youtube.com/live/cSSploT1J1E?si=JA5e7XXaaykIsirQ",
]

mahagathbandhan_urls = [
    # "PASTE_MAHAGATHBANDHAN_URL_1",
    # "PASTE_MAHAGATHBANDHAN_URL_2",
    # "https://www.youtube.com/live/6lEnnfMSFDM?si=YLW2aUEtJ5tBMGnb", 
    # "https://www.youtube.com/live/PCyBbVsRTXY?si=fCrwwLvB3KhCdfgQ",
    "https://www.youtube.com/live/nCItmNzLJRo?si=Z0Lua20JKe6Deqr4",
]

os.makedirs("../data/raw_audios/NDA", exist_ok=True)
os.makedirs("../data/raw_audios/Mahagathbandhan", exist_ok=True)


def download_audio(urls, folder_name):
    for i, url in enumerate(urls, start=1):

        output_path = f"../data/raw_audios/{folder_name}/%(title)s.%(ext)s"

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'quiet': False
        }

        print(f"\nDownloading {folder_name} audio{i} ...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"{folder_name} audio{i} downloaded successfully.")

# download_audio(nda_urls, "NDA")
download_audio(mahagathbandhan_urls,"Mahagathbandhan")

print("\nAll downloads completed successfully.")