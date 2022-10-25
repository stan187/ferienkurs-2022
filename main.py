from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(700, 410)
      
      #die hintergrundfarbe kann verändert werden,in dem wir den übergebenen wertverändern
      #diesen übergebenen wert nennt man einen parameter.
      #die runde klammern >()< die diesen wert umschließen,bezeichnet man als parameterliste.
      
        p.background(192)
        p.rectMode(p.CENTER)
      
    p.setup = setup
  
myp5 = window.p5.new(sketch)
