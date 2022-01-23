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

def downloadPlayList(p):
    #print Playlist title....
    print(p.title)

    # for v in p.video_Info:
    #     try:
            
    #     except Exception as e:
    #         print(e,type(e))

    print("Playlist is Downoaded")

link = input()
yt = YouTube(link)

video_Info(yt)