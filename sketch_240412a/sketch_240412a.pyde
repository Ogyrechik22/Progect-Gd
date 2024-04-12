def col(x,y,w,h,x2,y2,w2,h2):
   if (x + w >= x2) and (x <= x2 + w2) and (y + h >= y2) and (y <= y2 + h2):
       return True
   else:
       return False
x = 50
y = 950
ysp = 0
grav = 0.2
jump = False
pr = -6
dp = 0
a = 0
def setup():
    size(1920,1000)
    rectMode(CENTER)
def draw():
    background(1)
    global x,y,ysp,grav,jump,pr,dp,a
    rect(x,y,50,50)
    ysp += grav
    y += ysp
    if y > height - 50:
        y = height - 50
        ysp = 0
        jump = False
        dp = 1
    if keyPressed == True:
        if key == 'W' or key == 'w' and not jump:
            if jump == False:
                rotate(radians(90))
                ysp = pr
                jump = True
                
    x += 6
            
