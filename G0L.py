from PIL import Image, ImageDraw
Im = Image.new("RGB", (1080, 2220))
draw = ImageDraw.Draw(Im)

def raster(Axis, a, b, size, HVp, CVH, P):
    for i in range(size):
        Axis[a] += [i]
    A = HVp % CVH
    print(A)
    C = -1
    for _ in range(G):
        C = C + 1
        Axis[b] += [C]
        
    for _ in range(A):
        C += P + 2
        Axis[b] += [C]
        for _ in range(G-1):
            C = C + 1
            Axis[b] += [C]

    if A > 0:
        C += P+1

    for _ in range(CVH - A):
        Axis[b] += [C]
        for _ in range(G-1):
            C = C + 1
            Axis[b] += [C]
        C += P+ 1

def Draw(Axis, a, b):
    for y in Axis[b]:
        for x in Axis[a]:
            draw.point([x,y], (166,166,166))

CH = int(input("number of horizonal cells: "))
G = int(input("grid width: ")) #thickness of grid
Hp = Im.size[0] - (CH +1)*G #available pixels for cells (grid pixels are subtracted)
print("Wp: "+str(Hp))
PH = Hp//CH #Pixel width per cell (horizontal pixels)
print("Pw: "+str(PH))
CV = Im.size[1]//PH # number of vertical cells
print("CH: "+str(CV))
Vp = Im.size[1] - (CV +1)*G #available pixels per cell (grid pixels are subtracted)
print("Hp: "+str(Vp))
PV = Vp // CV #Pixel height per cell (vertical pixels)
print("Ph: "+str(PV))
HGrid = [[], []]
VGrid = [[], []]

raster(VGrid, 1, 0, Im.size[1], Hp, CH, PH)
raster(HGrid, 0, 1, Im.size[0], Vp, CV, PV)

Draw(HGrid, 0, 1)
Draw(VGrid, 0, 1)
print(HGrid)
print(VGrid)
Im.show()
Im.save(r"C:\Users\Max\Desktop\G0L.png")
