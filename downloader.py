from pytube import YouTube

# Function Takes Youtube Object as Argument.import

def video_Info(yt):
    print("Title: ",yt.title)
    print("Author: ",yt.author)
    print("Total Length: " ,yt.length, "Seconds")
    print("Total Views: ", yt.views)
    print("Is Age Restricted: ", yt.age_restricted)
    print("Thumbnail Url: ", yt.thumbnail_url)
    print(yt.description)


def download_Video(yt):
    my_streams = yt.streams.filter(file_extension='mp4',only_video= True)
    for streams in my_streams:
        print(f"Video Tag : {streams.itag} Resolution : {streams.resolution}")

    input_itag = input("Enter itag Value: ")

    video = yt.streams.get_by_itag(input_itag)

    video.download()
    print("Video is Downloading as ", yt.title , ".mp4")



def download_Audio(yt):
    my_streams = yt.streams.filter(only_audio= True)
    for streams in my_streams:
        print(f"Audio Tag : {streams.itag} Resolution : {streams.abr}")

    input_itag = input("Enter itag Value: ")

    audio = yt.streams.get_by_itag(input_itag)

    audio.download()
    print("Audio is Downloading as ", yt.title , ".mp3")



def downloadPlayList(p):
    #print Playlist title....
    print(p.title)

    for v in p.videos:
        try:
            # Download all videos in best resolution
            v.streams.first().download(v.title)
        except Exception as e:
            print(e,type(e))

    print("Playlist is Downoaded")


while True:
    print("1. Youtube Video Download")
    print("2. Youtube Audio Download")
    print("3. Youtube Playlist Download")
    print("4. Video Info")
    print("5. Exit")

    op = int(input())

    if op == 5:
        break
    elif op == 1:
        print("Enter Video Link: ")
        link = input()
        yt = YouTube(link)
        download_Video(yt)
    elif op == 2:
        print("Enter Video Link: ")
        link = input()
        yt = YouTube(link)
        download_Audio(yt)
    elif op == 3:
        print("Enter Playlist Link: ")
        link = input()
        yt = YouTube(link)
        downloadPlayList(yt) 

    elif op == 4:
        print("Enter Video Link: ")
        link = input()
        yt = YouTube(link)
        video_Info(yt)  