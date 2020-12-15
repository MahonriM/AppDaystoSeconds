import kivy
from kivy.app import App
from kivy.uix.scatter import ScatterPlane
from kivy.uix.label import Label
class LabelMimapTest(App):
    def build(self):
        s= ScatterPlane(scale=.5)
        l2=Label(text='Benchmarking',font_size=80,pos=(700,750))
        l1=Label(text='Proceso sistemático de investigar, identificar, comparar y aprender de las mejores prácticas de otras organizaciones', font_size=30,pos=(700,560), mipmap=True)
        l3=Label(text='abbbb',font_size=30,pos=(700,510))
        s.add_widget(l2)
        s.add_widget(l1)
        s.add_widget(l3)
        return s
if __name__ =='__main__':
    LabelMimapTest().run()
