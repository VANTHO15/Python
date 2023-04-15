def Count(*data):
    Dis={}
    for L in data:
        for Li in L:
            Li=Li.upper()
            if(Li in Dis):
                Dis[Li]+=1
            else:
                Dis[Li]=1
    return Dis
dem= Count("Vamtho","123","anhyeuEm")
print(dem)

