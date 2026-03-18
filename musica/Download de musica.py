from pytubefix import *
from moviepy import VideoFileClip
import os



    


print("=-"*20)
print("Programa de dowload de músicas")
print("=-"*20)

print("Para iniciar o dowload, escolha uma dentre as opções abaixo: ")
print("""
      [1] Dowload da música e vídeo clipe(.mp4)
      [2] Download apenas da música(.mp3)
      [3] Donwload de várias músicas juntas(Utilize espaço para separar os links)
      """)
escolha = input("Escolha: ")
url = input("Cole a Url: ")
if escolha == "1" or escolha == "2":
    yt = YouTube(url)
    print(yt.title)
    print(yt.thumbnail_url)
    stream = yt.streams.get_highest_resolution()
    video_path = stream.download(output_path="C:/Users/T-GAMER/Music")
    print(video_path)

    if escolha == "2":
        video = VideoFileClip(video_path)
        audio = video.audio
        audio_path = video_path.replace(".mp4", ".mp3")
        audio.write_audiofile(audio_path)
        
        video.close()  # Fecha o objeto para liberar o arquivo
        os.remove(video_path)

elif escolha == "3":
    lista = url.split(" ")
    n = 1
    for i in lista:
        yt = YouTube(i)
        print(f"Dowload da música {n}")
        print(yt.title + "\n")
        
        stream = yt.streams.get_highest_resolution()
        video_path = stream.download(output_path="C:/Users/T-GAMER/Music")
        print(video_path)
        
        video = VideoFileClip(video_path)
        audio = video.audio
        audio_path = video_path.replace(".mp4", ".mp3")
        audio.write_audiofile(audio_path)
        
        video.close()  # Fecha o objeto para liberar o arquivo
        os.remove(video_path)
        
        n += 1