from Grid import Grid
import os
import PIL
import getpass
host = getpass.getuser()
kivy.require("1.11.1")

class Drw(Widget):
    Width = int(input("\nWidth: "))
    Height = int(input("\nHeight: "))
    cellAdd = int(input("\nCell add: "))
    time.sleep(1)
    Window.size = (Width, Height)
    Im = (PIL.Image.new("RGB", (Width, Height), (0,0,0))).save(r"C:\Users\{}\Desktop\Grid.png".format(host))
    def __init__(self,**kwargs):
        super(Drw, self).__init__(**kwargs)
        self.CellCount = 1

        
        with self.canvas:
            self.bg = Image(source= r"C:\Users\{}\Desktop\Grid.png".format(host), pos=(0,0), size = (self.Width, self.Height))
            
            self.add = Button(text = "zoom out", font_size =self.Height*0.05, size= (self.Width * 0.25, self.Height*0.10), pos = (0, 0))
            self.sub = Button(text="zoom in", font_size=self.Height*0.05, size= (self.Width * 0.25, self.Height*0.10), pos=(self.Width - self.Width * 0.25, 0))
            self.sub.bind(on_press= self.Sub)
            self.add.bind(on_press=self.Add)
            self.add_widget(self.sub)
            self.add_widget(self.add)
            
    def Add(self, instance):
        self.CellCount += self.cellAdd
        self.AddSub(instance)
    def Sub(self, instance):
        self.CellCount -= self.cellAdd
        self.AddSub(instance)
    def AddSub(self, instance):
        Grid(self.CellCount, self.Width, self.Height)
        with self.canvas:
            self.bg.reload()
            os.remove(r"C:\Users\{}\Desktop\Grid.png".format(host))


class G0L(App):
    def build(self):
        return Drw()

if __name__ == "__main__":
    G0L().run()
