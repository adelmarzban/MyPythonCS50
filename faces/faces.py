def facemaker(txt):
    new=txt.replace(":)","🙂").replace(":(","🙁")
    return new



def printer():
    txt=input("give your txt please ")
    print(facemaker(txt))
printer()