import pytube

link = input('Input URL: ')
yt = pytube.YouTube(link)
yt.streams.first().download()

print("Downloaded", link)