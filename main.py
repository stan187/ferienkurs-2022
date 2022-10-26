from browser import document, window, alert
import random 
def sketch(p) :
  #this p is needed. it will be the processing sketch itself  .
  # to do things like background(0) instead do p.background(0)
    def setup():
      p.createCanvas(700, 410)
      #die hintergrundfarbe kann verändert werden,in dem wir den übergebenen wertverändern
      #diesen übergebenen wert nennt man einen parameter.
      #die runde klammern >()< die diesen wert umschließen,bezeichnet man als parameterliste.
      p.background(90)
      p.rectMode(p.CENTER)
      # Die >fill< methode gibt an,welche farbe fortan zum zeichnen verwendet wird. 
      #Als parameter werden RGB-Werte übergeben oder 1 Parameter für den Grauton.
      #RGB werte sind auf >farb-tabelle.de< zu finden.
      p.fill(13,42,26)
      p.circle(175,200,50)
      
      p.fill(100,62,54)
      p.rect(175,200,50,100)

      p.fill(65,98.150)
      p.circle(175,200,25)

      p.fill(70,700,500)
      p.circle(175,200,20)
    p.setup = setup

myp5 = window.p5.new(sketch)