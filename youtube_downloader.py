from pytube import YouTube
import os

def download_video(url, download_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download(output_path=download_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the path where you want to save the video (or press enter to save in the current directory): ")
    if not download_path:
        download_path = os.getcwd()
    download_video(url, download_path)

if __name__ == "__main__":
    main()
