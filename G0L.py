from PIL import Image, ImageDraw
Im = Image.new("RGB", (1080, 2220))
draw = ImageDraw.Draw(Im)

def raster(Axis, a, b, size, WHp, CWH, P):

    for i in range(size):
        Axis[a] += [i]
    A = WHp % CWH
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
    for _ in range(CWH - A):
        Axis[b] += [C]
        for _ in range(G-1):
            C = C + 1
            Axis[b] += [C]
        C += P+ 1

def Draw(Axis, a, b):
    for y in Axis[b]:
        for x in Axis[a]:
            draw.point([x,y], (166,166,166))

CW = int(input("number of cells in width: "))
G = int(input("grid width: "))
Wp = Im.size[0] - (CW +1)*G
print("Wp: "+str(Wp))
Pw = Wp//CW
print("Pw: "+str(Pw))
CH = Im.size[1]//Pw
print("CH: "+str(CH))
Hp = Im.size[1] - (CH +1)*G
print("Hp: "+str(Hp))
Ph = Hp // CH
print("Ph: "+str(Ph))
HGrid = [[], []]
VGrid = [[], []]

raster(HGrid, 0, 1, Im.size[0], Hp, CH, Ph)
raster(VGrid, 1, 0, Im.size[1], Wp, CW, Pw)

Draw(HGrid, 0, 1)
Draw(VGrid, 0, 1)
print(HGrid)
print(VGrid)
Im.show()
Im.save(r"C:\Users\Max\Desktop\G0L.png")
