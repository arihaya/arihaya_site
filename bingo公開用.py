#Libraryのimport
from tkinter import*
import pygame
import random
import tkinter as tk
import time

#スタート準備
a=1
b=1
d=0
check=0
datalist=[]
detalist=[0,0,0,0,0,0]
detalist_tyuusyutu=[]
while a<=75:
    datalist.append(a)
    a+=1
#定義
def game_start():
    global show_text
    pygame.mixer.init() #初期化



    pygame.mixer.music.play(1) #再生
    time.sleep(0.3)
    pygame.mixer.music.stop()
    start_frame.pack_forget()
    game_frame.place(x=0,y=0)
    game_button.place(x=300,y=700)
    deta_frame.place(x=1000,y=0)   
    kirikae_frame.place(x=100,y=700)
    list_button.pack()
    ingame_button.pack()

    
    
    
    

def ingame():
    global derukazu,datalist,tyuusen,show_text,check,detalist,detakazu1,detakazu2,detakazu3,detakazu4,detakazu5,detalist_tyuusyutu
    global b,random_kazu,d,random_text
    c=0
    pygame.mixer.init() #初期化


    pygame.mixer.music.play(1)
    if d==0:
        random_text=tk.Label(game_frame,text=random,font=("Helvetica",500),bg="white")
        random_text.place(x=100,y=-100)
        while c<=170:
            
            random_kazu=random.randint(1,75)
            random_text["text"]=random_kazu
            root.update()
            
            time.sleep(0.02)
            c+=1
        d=1
    else:
        show_text.place_forget()
        random_text.place(x=100,y=-100)
        while c<=170:
            
            random_kazu=random.randint(1,75)
            random_text["text"]=random_kazu
            root.update()
            time.sleep(0.02)
            c+=1
    random_text.place_forget()
    

    tyuusen=random.choice(datalist)
    detalist.append(tyuusen)
    detalist_tyuusyutu.append(tyuusen)
    datalist.remove(tyuusen)
    detashow_list.insert(b,tyuusen)
    b+=1
    
    if check==0:
        show_text=tk.Label(game_frame,text=tyuusen,font=("Helvetica",500),bg="white")
        detakazu1=tk.Label(deta_frame,text=detalist[-1],font=("Helvetica",100))
        detakazu2=tk.Label(deta_frame,text=detalist[-2],font=("Helvetica",100))
        detakazu3=tk.Label(deta_frame,text=detalist[-3],font=("Helvetica",100))
        detakazu4=tk.Label(deta_frame,text=detalist[-4],font=("Helvetica",100))
        detakazu5=tk.Label(deta_frame,text=detalist[-5],font=("Helvetica",100))
        show_text.place(x=100,y=-100)
        detakazu1.place(x=200,y=0)
        detakazu2.place(x=200,y=150)
        detakazu3.place(x=200,y=300)
        detakazu4.place(x=200,y=450)
        detakazu5.place(x=200,y=600)
        check=1 
    show_text.place(x=100,y=-100) 
    show_text["text"]=tyuusen
    detakazu1["text"]=detalist[-1]
    detakazu2["text"]=detalist[-2]
    detakazu3["text"]=detalist[-3]
    detakazu4["text"]=detalist[-4]
    detakazu5["text"]=detalist[-5]

    root.update()

def imamade():
    detashow_frame.place(x=900,y=0)
    detashow_list.pack()
    deta_frame.place_forget()
    game_frame.place_forget()



def gameframe():
    detashow_frame.place_forget()
    detashow_list.place_forget()
    deta_frame.place(x=1000,y=0)
    game_frame.place(x=0,y=0)

   

    

#変数定義


#Tkinterフレームの作成
root=Tk()
root.title("bingo")
root.state('zoomed')

#スタート用フレーム
start_frame=tk.Frame(root,width=500,height=600)
start_button=tk.Button(start_frame,text="start",font=("10"),command=game_start,width=30,height=5,bg="blue")
start_text=tk.Label(start_frame,text="ボタンを押して抽選スタート",font=("30"))
start_frame.pack()
start_text.place(x=150,y=100)
start_button.place(x=100,y=200)

#ゲーム用フレーム
game_frame=tk.Frame(root,width=1000,height=1000,bg="white")
game_button=tk.Button(game_frame,text="抽選",font=("30"),command=ingame,width=20,height=2)

#出た数字表示フレーム
deta_frame=tk.Frame(root,width=600,height=900)

#出た数リストフレーム
detashow_frame=tk.Frame(root,width=600,height=900)
detashow_list=tk.Listbox(detashow_frame,width=50,height=10,font=("Helvetica",50))


#切り替えボタン
kirikae_frame=tk.Frame(root)
list_button=tk.Button(kirikae_frame,text="今まで出た数",command=imamade)
ingame_button=tk.Button(kirikae_frame,text="抽選画面",command=gameframe)









#フレームを有効か
root.mainloop()