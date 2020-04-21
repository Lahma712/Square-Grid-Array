from PIL import Image, ImageDraw
import getpass
host = getpass.getuser()
Width = int(input("screen width: "))
Height = int(input("screen height: "))
bgColor = eval(input("Background color: ( eg, '(0, 0, 0)'): "))
gColor = eval(input("Grid color : (eg. '(255, 255, 255)'): "))
Im = Image.new("RGB", (Width, Height), bgColor)
draw = ImageDraw.Draw(Im)


def grid(Axis, CellCount, CellWidth, ExcessPixels):
    check = False
    C = 0  # counter for grid pixel position

    if ExcessPixels > 0:
        ExcessPixels -= 1
        check = True

    for _ in range(ExcessPixels):
        C += CellWidth + 1
        Axis += [C]


    if ExcessPixels == 0 and check != True:
        C += CellWidth - 1
    else:
        C += CellWidth

    for _ in range(CellCount - ExcessPixels):
        Axis += [C]
        C += CellWidth


def Draw(a, b):
    for y in a:
        for x in b:
            draw.point([x, y], gColor)
            

hCellCount = int(input("How many columns?: "))
hCellWidth = Width // hCellCount  # Pixel width per cell (horizontal pixels)
hExcessPixels = Width % hCellCount
vCellCount = Height // hCellWidth  # number of vertical cells
vCellWidth = Height // vCellCount  # Pixel height per cell (vertical pixels)
vExcessPixels = Height % vCellCount

HGrid = [0]
VGrid = [0]

grid(VGrid, hCellCount, hCellWidth, hExcessPixels)
grid(HGrid, vCellCount, vCellWidth, vExcessPixels)

Draw(HGrid, range(Width))
Draw(range(Height), VGrid)

Im.show()
Im.save(r"C:\Users\{}\Desktop\Grid.png".format(host))
