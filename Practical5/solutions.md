# Practical 5: solution guide

## problem 1

is pretty much just some of the root locus sketching rules, but having them basically discover them themselves in a guided manner.

### 1a

max(# of poles, # of zeros)

### 1b

The loci go from poles to zeros (connect poles and zeros) (this is best to be tested out if # of zeros = # of poles)

### 1c

Gain 0 puts them at poles, gain infinity puts them at zeros (also best tested with # of zeros = # of poles)

### 1d

The ones we can't pair up go to infinity - if there's more poles than zeros then the excess have loci that go to infinity (also works with excess zeros)

### 1e

One - goes horizontally to negative infinity. Two: two going vertically in opposite directions. Three: at 120 degree angles. 4: at 90 degree angles basically the asymptotes divide themselves evenly over a circle (this is easier drawn than explained in words)

## problem 2

for problem 2 putting a pole to -7 and zero to -5 works, 

## problem 3

putting a pole to -0.01 and zero to -0.285 (or also pole to -0.001 and zero to -0.0285,
or you can go more insane if you want,
but if you need to do this in real life with electronics components,
for example,
then it starts becoming impractical due to the component values you need to implement a corresponding circuit)

## troubleshooting resources

- [pytest](https://pypi.org/project/pytest/)
- [pyControl docs (v0.9.3)](https://python-control.readthedocs.io/en/0.9.3.post2/control.html)
- [pypi: control - releases](https://pypi.org/project/control/#history)
- [gColab, jckantor: transfer functions demo](https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/05.01-Getting-Started-with-Transfer-Functions.ipynb#scrollTo=xSvoZ1FK9itT)
- [Brian Douglas: Root Locus Playlist](https://www.youtube.com/watch?v=NMpmb0ihoFo&list=PLUMWjy5jgHK3-ca6GP6PL0AgcNGHqn33f&index=4)
- [pyContro docs - sisotool](https://python-control.readthedocs.io/en/latest/generated/control.sisotool.html)
