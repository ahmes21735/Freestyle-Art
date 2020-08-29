##############################
#### Sunflower Field #########
#### By Sarah Ahmed ##########
#### March 16th, 2020 ########
##############################
from tkinter import*
from random import*
from time import*
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="#c4dce6" )
screen.pack()

#########
###SKY###
#########
mediumSky = screen.create_polygon(0,0, 700,0, 780,80, 700,200, 560,220,
                                 0,240, fill = "#b6cbdc", outline = "#b6cbdc")
darkSky = screen.create_polygon(0,0, 600,0, 545,75, 245,235, 0,240,
                                fill = "#adbacd", outline = "#adbacd")
###############
###MOUNTAINS###
###############
mountainOutline = screen.create_polygon(0,300, 80,270, 145,280, 200,270, 270,240,
                                        310,250, 495,235, 800,330, 800,370, 0, 370,
                                        fill = "#aec3be", outline = "#aec3be")
mountainShading1 = screen.create_polygon(0,300, 80,270, 70,280, 60,300, 40,320,
                                         0, 345, fill = "#92a2bb", outline = "#92a2bb")
mountainShading2 = screen.create_polygon(145,280, 200,270, 260,245, 250,260, 230,265,
                                         220,270, 210,275, 195,285, 200,300, 260,280,
                                         310,255, 320,260, 340,240, 400,230, 495,310,
                                         470,340, 400,300, 360,260, 320,270, 350,310,
                                         330,305, 320,360, 0,400, 0,360, 40,370, 80,320,
                                         100,340, 160,300, 145,280,
                                         fill = "#92a2bb", outline = "#92a2bb")
mountainHighlight1 = screen.create_polygon(0,345, 60,305, 70,280, 85,270, 140,275,
                                           160,300, 140,290, 120,280, 100,290, 85,310,
                                           70,300, 60,315, 30,340, 0,355, fill = "#d5d3c4",
                                           outline = "#d5d3c4")
mountainHighlight2 = screen.create_polygon(260,245, 250,260, 230,265, 220,270, 210,275,
                                           195,285, 200,300, 210,290, 220,295, 230,285,
                                           250,270, 270,250, 290,245, 275,240, fill = "#d5d3c4",
                                           outline = "#d5d3c4")

######################
###BACKGROUND TREES###
######################
for tree in range(150):
    treeThickness = randint(15,30)
    xTree = 0 + 10*tree
    yTree = randint(350, 365)
    x2Tree = xTree + treeThickness
    y2Tree = 390 + treeThickness
    screen.create_oval(xTree,yTree, x2Tree,y2Tree, fill = "#546f80", outline = "#546f80")


#######################  
###BACKGROUND FIELD####
#######################
screen.create_polygon(40,400, 120,380, 280,375, 380,370, 400,370, 440,370, 500,375, 600,380,
                      800,360, 800,500, 600,450, 200,430, 100,400, fill = "#5d837b", outline = "#5d837b")


#################
###FRONT FIELD###
#################
screen.create_polygon(230,430, 100,400, 0,380, 0,490, 120,440,
                      fill = "#4b554e", outline = "#4b554e")

for cropLine in range(15):
    xCrop = 200 - 15*cropLine
    yCrop = 420 - 3.2*cropLine
    xxCrop = 140 - 20*cropLine
    yyCrop = 440 + 5*cropLine
    cropWidth = randint(5, 7)
    screen.create_line(xCrop,yCrop, xxCrop + 5,yyCrop + 5, fill = "#818a61",
                       width = cropWidth)
for n in range(25):
    xplant = randint(0,120)
    xxplant = xplant +4
    yplant = randint(400,450)
    yyplant = yplant +4
    screen.create_rectangle(xplant,yplant, xxplant,yyplant, fill = "#907c53", outline = "#907c53")


###############
###FARMHOUSE###
###############

#windmill
topwing = screen.create_rectangle(645,242, 665,260, fill = "#656972", outline = "#656972")
for n in range(5):
    screen.create_rectangle(641 -5*n, 220-20*n, 647-5*n, 240-20*n, fill = "#9598a4", outline = "#9598a4")
    screen.create_rectangle(648-5*n, 220-20*n, 652-5*n,240-20*n, fill = "#676d79", outline = "#676d79")
    screen.create_line(658-5*n, 220-20*n, 658-5*n,242-20*n, fill = "#676d79", width = 3)
    screen.create_line(642-3.5*n,242-21*n, 670-2*n,242-21*n, fill = "#9598a4", width = 2.5)
    screen.create_line(670-2*n,218-20*n, 670-2*n,242-20*n, fill = "#9598a4", width = 2.5)
    screen.create_line(642-3.5*n,230-21*n, 670-2*n,230-21*n, fill = "#9598a4", width = 2.5)
    screen.create_line(672-2*n,218-20*n, 672-2*n,242-20*n, fill = "#ccdeed", width = 2.5)
screen.create_line(621,140, 663,140, fill = "#9598a4", width = 4)

rightwing = screen.create_rectangle(670,255, 682,275, fill = "#656972", outline = "#656972")
for n in range(5):
    screen.create_rectangle(682+20*n,247-5*n, 700+20*n,255-5*n, fill = "#9598a4", outline = "#9598a4")
    screen.create_line(682+20*n,255-5*n, 700+20*n,255-5*n, fill = "#676d79", width = 5)
    screen.create_line(682+20*n,262-5*n, 703+20*n,262-5*n, fill = "#676d79", width = 3)
    screen.create_line(682+20*n,275-5*n, 703+20*n,275-5*n, fill = "#9598a4", width = 3)
    screen.create_line(682+20*n,278-5*n, 703+20*n,278-5*n, fill = "#676d79", width = 3)
    screen.create_line(682+20*n,250-5*n, 682+20*n,278-3*n, fill = "#9598a4", width = 3)
    screen.create_line(690+20*n,250-5*n, 690+20*n,278-5*n, fill = "#9598a4", width = 2)
screen.create_line(780,230, 780, 253, fill = "#9598a4", width = 3)
screen.create_line(782,230, 782, 253, fill = "#ccdeed", width = 3)

for n in range(5):
    screen.create_line(562+20*n,270-5*n, 562+20*n,300-5*n, fill = "#9598a4", width = 3)
    screen.create_line(562+20*n,270-5*n, 580+20*n,270-5*n, fill = "#9598a4", width = 3)
    screen.create_line(562+20*n,300-5*n, 580+20*n,300-5*n, fill = "#676d79", width = 3)
    screen.create_line(564+20*n,273-5*n, 580+20*n,273-5*n, fill = "#676d79", width = 3)
    screen.create_line(564+20*n,280-5*n, 580+20*n,280-5*n, fill = "#676d79", width = 3.5)
    screen.create_line(562+20*n,297-5*n, 580+20*n,297-5*n, fill = "#9598a4", width = 3)
    screen.create_line(568+20*n,270-5*n, 568+20*n,300-5*n, fill = "#9598a4", width = 3)    


#building shades
baseShade = screen.create_rectangle(600,340, 660,400, fill = "#520704", outline = "#520704")
for n in range(6):
    xBase = 600
    yBase = 400 - 10*n
    xxBase = 660
    yyBase = 400 - 10*n
    screen.create_line(xBase,yBase, xxBase,yyBase, width = 3.5, fill = "#46050b")
lineShade1 = screen.create_line(600,340, 600,403, fill = "#685b5b", width = 5)
    
midShade = screen.create_rectangle(605,315, 655,340, fill = "#520704", outline = "#520704")
for n in range(3):
    xBase = 605
    yBase = 340 - 10*n
    xxBase = 655
    yyBase = 340 - 10*n
    screen.create_line(xBase,yBase, xxBase,yyBase, width = 3.5, fill = "#46050b")
lineShade2 = screen.create_line(605,315, 605,340, fill = "#685b5b", width = 5)

topShade = screen.create_rectangle(610,275, 650,315, fill = "#520704", outline = "#520704")
for n in range(4):
    xBase = 610
    yBase = 310 - 10*n
    xxBase = 650
    yyBase = 310 - 10*n
    screen.create_line(xBase,yBase, xxBase,yyBase, width = 3.5, fill = "#46050b")
lineShade3 = screen.create_line(610,275, 610,315, fill = "#685b5b", width = 5)


#building highlights
baseHighlight = screen.create_rectangle(660,340, 690,400, fill = "#a31c1b", outline = "#a31c1b")
for n in range(6):
    xBase = 660
    yBase = 400 - 10*n
    xxBase = 690
    yyBase = 400 - 10*n
    screen.create_line(xBase,yBase, xxBase,yyBase, width = 3.5, fill = "#7a0907")
lineHighlight1 = screen.create_line(660,340, 660,403, fill = "#a17d84", width = 5)
borderLine1 = screen.create_line(690,340, 690,403, fill = "#957274", width = 5)

midHighlight = screen.create_rectangle(655,315, 685,340, fill = "#a31c1b", outline = "#a31c1b")
for n in range(3):
    xBase = 655
    yBase = 340 - 10*n
    xxBase = 685
    yyBase = 340 - 10*n
    screen.create_line(xBase,yBase, xxBase,yyBase, width = 3.5, fill = "#7a0907")
lineHighlight2 = screen.create_line(655,315, 655,343, fill = "#a17d84", width = 5)
borderLine2 = screen.create_line(685,315, 685,343, fill = "#957274", width = 5)

topHighlight = screen.create_rectangle(650,275, 680,315, fill = "#a31c1b", outline = "#a31c1b")
for n in range(4):
    xBase = 650
    yBase = 310 - 10*n
    xxBase = 680
    yyBase = 310 - 10*n
    screen.create_line(xBase,yBase, xxBase,yyBase, width = 3.5, fill = "#7a0907")
lineShade3 = screen.create_line(650,275, 650,318, fill = "#a17d84", width = 5)
borderLine3 = screen.create_line(680,285, 680,318, fill = "#957274", width = 5)


#roof
roofShade = screen.create_polygon(650,285, 600,285, 625,250, fill = "#494f55", outline = "#494f55")

roofHighlight = screen.create_polygon(650,285, 625,250, 665,250, 685,285, fill = "#969aa3",
                                      outline = "#969aa3")
for n in range(1, 5):
    xRoof = 650 +7.5*n
    yRoof = 285
    xxRoof = 625 +7.5*n
    yyRoof = 250
    roofDetails = screen.create_line(xRoof,yRoof, xxRoof,yyRoof, fill = "#656972", width = 2.5)


######################
###FOREGROUND FENCE###
######################
for n in range(50):
    xFence = 390 + n*10
    yFence = 370
    xxFence = xFence - 15
    yyFence = yFence + 100
    xxxFence = xFence + 15
    yyyFence = yFence + 100

    screen.create_polygon(xFence,yFence, xxFence,yyFence, xxxFence,yyyFence, fill = "#29252a", smooth = True)


#####################
###SUNFLOWER FIELD###
#####################

#background
screen.create_polygon(800,430, 600,430, 200,430, 130,435, 120,440, 0,490, 0,600, 800,600,
                      fill = "#151f24", outline = "#151f24")

#sunflower field
for n in range(35):
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#962115", "#ba4318"] )
    screen.create_oval(790 -20*n,470, 800-20*n,480, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(780 -20*n,460, 790-20*n,470, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(760 -20*n,460, 770-20*n,470, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(782 -20*n,452, 788-20*n,458, fill = centreColour,
                       outline = petalColour, width = 2.5)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(780 -15*n,452, 786-15*n,458, fill = centreColour,
                       outline = petalColour, width = 2.5)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(782 -20*n,442, 788-20*n,447, fill = centreColour,
                       outline = petalColour, width = 2.5)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(772 -20*n,442, 778-20*n,447, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(772 -20*n,437, 778-20*n,442, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(782 -20*n,432, 788-20*n,437, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(794 -20*n,427, 800-20*n,432, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f", "#620e00"])
    petalColour = choice(["#de5a29", "#de5a29", "#962115"] )
    screen.create_oval(844 -20*n,423, 850-20*n,428, fill = centreColour,
                       outline = petalColour, width = 3)
    centreColour = choice(["#81120f"])
    petalColour = choice(["#de5a29", "#e54401", "#ba4318"] )
    screen.create_oval(780 -30*n,480, 800-30*n,500, fill = centreColour,
                       outline = petalColour, width = 5)
    centreColour = choice(["#81120f"])
    petalColour = choice(["#de5a29", "#e54401", "#ba4318"] )
    screen.create_oval(770 -30*n,500, 790-30*n,520, fill = centreColour,
                       outline = petalColour, width = 5)
    centreColour = choice(["#81120f"])
    petalColour = choice(["#e54401", "#ba4318"] )
    screen.create_oval(820 -50*n,520, 860-50*n,560, fill = centreColour,
                       outline = petalColour, width = 10)
    centreColour = choice(["#81120f"])
    petalColour = choice(["#e54401", "#ba4318"] )
    screen.create_oval(820 -60*n,560, 880-60*n,620, fill = centreColour,
                       outline = petalColour, width = 15)
