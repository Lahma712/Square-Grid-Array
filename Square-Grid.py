from PIL import Image, ImageDraw
width = int(input("screen width: "))
height = int(input("screen height: "))
bgColor = eval(input("Background color: ( '(x, x, x)'): "))
gColor = eval(input("Grid color : ( '(x, x, x)''): ") )
Im = Image.new("RGB", (width, height), bgColor)
draw = ImageDraw.Draw(Im)

def raster(Axis, a, b, size, CellPixelPool, CellCount, CellWidth, gridWidth, ExcessPixels):
    for i in range(size):
        Axis[a] += [i]
    C = -1 #counter for grid pixel position
    for _ in range(gridWidth):
        C = C + 1
        Axis[b] += [C]
        
    for _ in range(ExcessPixels):
        C += CellWidth + 2
        Axis[b] += [C]
        for _ in range(gridWidth-1):
            C = C + 1
            Axis[b] += [C]

    
    C += CellWidth+1

    for _ in range(CellCount - ExcessPixels):
        Axis[b] += [C]
        for _ in range(gridWidth-1):
            C = C + 1
            Axis[b] += [C]
        C += CellWidth + 1

def Draw(Axis, a, b):
    for y in Axis[b]:
        for x in Axis[a]:
            draw.point([x,y], gColor)

hCellCount = int(input("number of horizonal cells: "))
gridWidth = int(input("grid width: ")) #thickness of grid

hCellPixelPool = Im.size[0] - (hCellCount +1)*gridWidth #available pixels for cells (grid pixels are subtracted)
print("hCellPixelPool: "+str(hCellPixelPool))

hCellWidth = hCellPixelPool//hCellCount #Pixel width per cell (horizontal pixels)
print("hCellWidth: "+str(hCellWidth))

hExcessPixels = hCellPixelPool % hCellCount
print("hExcessPixels: " + str(hExcessPixels))

vCellCount = Im.size[1]//hCellWidth # number of vertical cells
print("vCellCount: "+str(vCellCount))

vCellPixelPool = Im.size[1] - (vCellCount +1)*gridWidth #available pixels per cell (grid pixels are subtracted)
print("vCellPixelPool: "+str(vCellPixelPool))

vCellWidth = vCellPixelPool // vCellCount#Pixel height per cell (vertical pixels)
print("vCellWidth: "+str(vCellWidth))

vExcessPixels = vCellPixelPool % vCellCount
print("vExcessPixels: "+ str(vExcessPixels))

HGrid = [[], []]
VGrid = [[], []]

raster(VGrid, 1, 0, Im.size[1], hCellPixelPool, hCellCount, hCellWidth, gridWidth, hExcessPixels)
raster(HGrid, 0, 1, Im.size[0], vCellPixelPool, vCellCount, vCellWidth, gridWidth, vExcessPixels )

Draw(HGrid, 0, 1)
Draw(VGrid, 0, 1)
print(HGrid)
print(VGrid)
Im.show()
Im.save(r"Grid.png")               
