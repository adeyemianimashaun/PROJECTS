from tkinter import *
import time
window=Tk()
HEIGHT=500
WIDTH=500
canvas=Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()


class Balls:
    def __init__(self,canvas,x,y,color,diameter,xvelocity,yvelocity):
        self.canvas=canvas
        self.id=canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xvelocity=xvelocity
        self.yvelocity=yvelocity
        #[self.canvas.move(self.id,self.xvelocity,self.yvelocity)
    def move(self):
        cood=self.canvas.coords(self.id)
        if cood[2]>=WIDTH or cood[0]<0:
            self.xvelocity=-self.xvelocity
        if cood[3]>=HEIGHT or cood[0]<0:
            self.yvelocity=-self.yvelocity
        self.canvas.move(self.id,self.xvelocity,self.yvelocity)


volley=Balls(canvas,0,0,'red',100,2,1)
football=Balls(canvas,0,0,'white',100,3,5)
tenis=Balls(canvas,0,0,'green',30,1,2)

while True:
    volley.move()
    football.move()
    tenis.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
    


        

















