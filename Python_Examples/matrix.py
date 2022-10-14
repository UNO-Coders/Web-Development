import pygame, pygame.font
import random

COLOR = (0, 200, 200)  # The Color of the Matrix
ZERO_ONE = False  # Makes a rain of zeros and ones instead of random ASCII character


def is_written():
    def_temp = True
    for x in range(
        (lettersOnScreen[0] / 2) - (len(str) / 2),
        (lettersOnScreen[0] / 2) + (len(str) / 2) + 1,
    ):
        if xHeads[x] == -1:
            def_temp = False
    return def_temp


def get_color(fx, fy):
    def_temp = xHeads[fx] - fy

    if maxCol > def_temp > 0:
        return def_temp
    else:
        return maxCol - 1


try:
    fo = open("indata.txt", "r+")
    str = fo.readline()
    # Close opend file
    fo.close()
except Exception as e:
    str = ""
str = str.upper()  # for better placement


# Pygame init
pygame.init()
temp = pygame.display.Info()
displLength = (temp.current_w, temp.current_h)
surface = pygame.display.set_mode(displLength, pygame.FULLSCREEN)
# Font init
pygame.font.init()
fontObj = pygame.font.Font(pygame.font.get_default_font(), 14)
sampleLetter = fontObj.render("_", False, (0, 111, 0))
letterSize = (sampleLetter.get_width(), sampleLetter.get_height())
lettersOnScreen = (
    int(displLength[0] / letterSize[0]),
    int(displLength[1] / letterSize[1]),
)

# color init
colorList = [(255, 255, 255)]
primeColors = len(colorList) + 1
R, G, B = COLOR
colorList += [(R + 10, G + 10, B + 10)] * (lettersOnScreen[1] - 10)
endColors = len(colorList)
colorList += [
    (R - 50 if R else 0, B - 50 if B else 0, G - 50 if G else 0),
    (R - 100 if R else 0, B - 100 if B else 0, G - 100 if G else 0),
    (0, 0, 0),
]
endColors = len(colorList) - endColors + 1

maxCol = len(colorList)


# char generator
letters = [
    [0 for _ in range(lettersOnScreen[1] + 1)] for _ in range(lettersOnScreen[0])
]
if ZERO_ONE:
    char = chr(random.randint(48, 49))
else:
    char = chr(random.randint(32, 126))

for y in range(lettersOnScreen[1] + 1):
    for x in range(lettersOnScreen[0]):
        letters[x][y] = [
            fontObj.render(char, False, colorList[col]) for col in range(maxCol)
        ]
        if ZERO_ONE:
            char = chr(random.randint(48, 49))
        else:
            char = chr(random.randint(32, 126))


# word write
wordMode = False
if len(str) > 0:
    wordMode = True
    for x in range(
        (lettersOnScreen[0] / 2) - (len(str) / 2),
        (lettersOnScreen[0] / 2) + (len(str) / 2),
    ):
        letters[x][lettersOnScreen[1] / 2] = [
            fontObj.render(
                str[x - ((lettersOnScreen[0] / 2) - (len(str) / 2))],
                False,
                (255, 255, 255),
            )
            for _ in range(maxCol)
        ]

    for y in range(lettersOnScreen[1] / 2 + 1, lettersOnScreen[1] + 1):
        for x in range(
            (lettersOnScreen[0] / 2) - (len(str) / 2),
            (lettersOnScreen[0] / 2) + (len(str) / 2),
        ):
            letters[x][y] = [
                fontObj.render(char, False, (0, 0, 0)) for _ in range(maxCol)
            ]
            char = chr(random.randint(32, 126))

    if len(str) % 2 == 1:

        letters[(lettersOnScreen[0] / 2) + (len(str) / 2)][lettersOnScreen[1] / 2] = [
            fontObj.render(str[len(str) - 1], False, (255, 255, 255))
            for _ in range(maxCol)
        ]

        for y in range(lettersOnScreen[1] / 2 + 1, lettersOnScreen[1] + 1):
            letters[(lettersOnScreen[0] / 2) + (len(str) / 2)][y] = [
                fontObj.render(char, False, (0, 0, 0)) for _ in range(maxCol)
            ]
            char = chr(random.randint(32, 126))

if wordMode:
    xHeads = [-1 for _ in range(lettersOnScreen[0] + 1)]
else:
    xHeads = [0 for _ in range(lettersOnScreen[0] + 1)]


# 1st loop - word write, no char switch
notDone = True
ticksLeft = lettersOnScreen[1] + maxCol
while ticksLeft > 0 and (notDone) and (wordMode):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notDone = False
        if event.type == pygame.KEYDOWN:
            notDone = False
    if is_written():
        ticksLeft -= 1
    if random.randint(1, 2) == 1:
        randomInt = random.randint(0, lettersOnScreen[0])
        if wordMode:
            if xHeads[randomInt] == -1:
                xHeads[randomInt] = 1
            if random.randint(1, 6):
                randomInt = random.randint(
                    (lettersOnScreen[0] / 2) - len(str),
                    (lettersOnScreen[0] / 2) + len(str) + 1,
                )
                if xHeads[randomInt] == -1:
                    xHeads[randomInt] = 1
        else:
            if xHeads[randomInt] == 0:
                xHeads[randomInt] = 1
    for x in range(lettersOnScreen[0]):
        col = 0
        counter = xHeads[x]
        while (counter > 0) and (col < maxCol):
            if (counter < lettersOnScreen[1] + 2) and (
                col < primeColors or col > (maxCol - endColors)
            ):
                surface.blit(
                    letters[x][counter - 1][col],
                    (x * letterSize[0], (counter - 1) * letterSize[1]),
                )
            col += 1
            counter -= 1
        if xHeads[x] > 0:
            xHeads[x] += 1
        if xHeads[x] - maxCol > lettersOnScreen[1]:
            xHeads[x] = 0

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(20)

# word delete
if len(str) % 2 == 1:
    strLen = int((lettersOnScreen[0] / 2) + (len(str) / 2) + 1)
else:
    strLen = int((lettersOnScreen[0] / 2) + (len(str) / 2))

for x in range(int((lettersOnScreen[0] / 2) - (len(str) / 2)), strLen):
    letters[x][lettersOnScreen[1] / 2] = [
        fontObj.render(
            str[x - ((lettersOnScreen[0] / 2) - (len(str) / 2))], False, colorList[col]
        )
        for col in range(maxCol)
    ]

char = chr(random.randint(32, 126))
for y in range(int(lettersOnScreen[1] / 2 + 1), int(lettersOnScreen[1] + 1)):
    for x in range(
        int((lettersOnScreen[0] / 2) - (len(str) / 2)),
        int((lettersOnScreen[0] / 2) + (len(str) / 2) + 1),
    ):
        letters[x][y] = [
            fontObj.render(char, False, colorList[col]) for col in range(maxCol)
        ]
        char = chr(random.randint(32, 126))


# main matrix, has char switch
while notDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notDone = False
        if event.type == pygame.KEYDOWN:
            notDone = False
    if random.randint(1, 2) == 1:
        randomInt = random.randint(0, lettersOnScreen[0])
        if xHeads[randomInt] <= 0:
            xHeads[randomInt] = 1
    for x in range(lettersOnScreen[0]):
        col = 0
        counter = xHeads[x]
        # main loop for redraw
        while (counter > 0) and (col < maxCol):
            if (counter < lettersOnScreen[1] + 2) and (
                col < primeColors or col > (maxCol - endColors)
            ):
                surface.blit(
                    letters[x][counter - 1][col],
                    (x * letterSize[0], (counter - 1) * letterSize[1]),
                )
            col += 1
            counter -= 1

        # charswirch
        randomInt = random.randint(1, maxCol - 1)
        charPosY = xHeads[x] - randomInt
        if lettersOnScreen[1] - 1 > charPosY > 0:
            temp = letters[x][charPosY]
            randomX = random.randint(1, lettersOnScreen[0] - 1)
            randomY = random.randint(1, lettersOnScreen[1] - 1)

            surface.blit(
                letters[x][charPosY][maxCol - 1],
                (x * letterSize[0], charPosY * letterSize[1]),
            )
            surface.blit(
                letters[randomX][randomY][maxCol - 1],
                (randomX * letterSize[0], randomY * letterSize[1]),
            )
            # char swap
            letters[x][charPosY] = letters[randomX][randomY]
            letters[randomX][randomY] = temp

            surface.blit(
                letters[x][charPosY][randomInt],
                (x * letterSize[0], charPosY * letterSize[1]),
            )
            surface.blit(
                letters[randomX][randomY][get_color(randomX, randomY)],
                (randomX * letterSize[0], randomY * letterSize[1]),
            )
        # check if is out of screen
        if xHeads[x] > 0:
            xHeads[x] += 1
        if xHeads[x] - maxCol > lettersOnScreen[1]:
            xHeads[x] = 0

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(20)
