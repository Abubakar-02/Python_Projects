import yt_dlp

def download_video(url, path = '-'):
    ydl_opts ={
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print("╔══════════════════════════════════╗")
print("║   📥 YOUTUBE DOWNLOADER 📥       ║")
print("╚══════════════════════════════════╝")
print()

while True:

    print("1. Download video")
    print("2. Exit")

    choice = input("Enter your choice : ")

    if choice == '1':
        url = input("Enter your YouTube video link(URL): ")
        print("Downloading video....")
        download_video(url)
        print("Video downloaded successfully......! ")
    elif choice == "2":
        print("GoodBye!------------")
        break
    else:
        print("Invalid choice. Please try again.")
