import pygame
import random
import math
import sys, os 

pygame.init()
current_path_directory = (str(os.path.dirname(os.path.abspath(__file__))) +"\\").replace("c:", "C:")
current_path_directory = current_path_directory.replace('\\', "/")
print(current_path_directory)


BLACK       = (  50,  50,  50)
WHITE       = ( 255, 255, 255)
GREEN       = (   0, 255,   0)
RED         = ( 255,   0,   0)
BLUE        = (   0,   0, 255)
LIGHT_BLUE  = (   0, 179, 255)
YELLOW      = ( 255, 255,   0)
ORANGE      = ( 255, 166,  33)
SECRET_BLUE = (   0, 102, 255)
# rectangle = pygame.rect.Rect(300,300,100,100)
# rectangle_dragging = False

screen_width = 1000
screen_height = 600

size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)
game_over = False
retry = False
pygame.display.set_caption("Perspecs")
clock = pygame.time.Clock()
prototype = "prototype.png"
frames_per_second = 120
time_per_frame = 1/frames_per_second

# musictrackpath = current_path_directory +("audio/perspecssolotrack.mp3").replace("\\", "/")
# print(musictrackpath)



# bgmusic = pygame.mixer.music.load(musictrackpath)



boxsquare = current_path_directory +("textures/boxsquare.png")
boxrectangle = current_path_directory +("textures/boxrectangle.png")

exitdoorimage = pygame.image.load(current_path_directory +("textures/exitdoor.png"))

background1 = pygame.image.load(current_path_directory +("textures/background1.png")).convert()
background1 = pygame.transform.scale(background1, (1000, 600))

background2 = pygame.image.load(current_path_directory +("textures/background2.png")).convert()
background2 = pygame.transform.scale(background2, (1000, 600))

background3 = pygame.image.load(current_path_directory +("textures/background3.png")).convert()
background3 = pygame.transform.scale(background3, (1000, 600))

background4 = pygame.image.load(current_path_directory +("textures/background4.png")).convert()
background4 = pygame.transform.scale(background4, (1000, 600))

background5 = pygame.image.load(current_path_directory +("textures/background5.png")).convert()
background5 = pygame.transform.scale(background5, (1000, 600))

background6 = pygame.image.load(current_path_directory +("textures/background6.png")).convert()
background6 = pygame.transform.scale(background6, (1000, 600))

background7 = pygame.image.load(current_path_directory +("textures/background7.png")).convert()
background7 = pygame.transform.scale(background7, (1000, 600))

background8 = pygame.image.load(current_path_directory +("textures/background8.png")).convert()
background8 = pygame.transform.scale(background8, (1000, 600))

backgroundimage = background1

leftplayer = current_path_directory +("textures/left.png")
rightplayer = current_path_directory +("textures/right.png")

ending = False

guntextureright = current_path_directory +("textures/guntexturerightextension.png")
guntextureleft = current_path_directory +("textures/guntextureleftextension.png")

level = 0
levelincremention = False
loadedlevel = False

# class DragOperator:
#     def __init__(self, rect):
#         self.rect = rect
#         self.dragging = False
#         self.rel_pos = (0, 0)
#     def update(self, event_list):
#         global game_over
#         for event in event_list:
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 self.dragging = self.rect.collidepoint(event.pos)
#                 self.rel_pos = event.pos[0] - self.rect.x, event.pos[1] - self.rect.y
#             if event.type == pygame.MOUSEBUTTONUP:
#                 self.dragging = False
#             if event.type == pygame.MOUSEMOTION and self.dragging:
#                 self.rect.topleft = event.pos[0] - self.rel_pos[0], event.pos[1] - self.rel_pos[1]
            



# class Quit(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface([100,100])
#         self.image.fill(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.x =100
#         self.rect.y = 100 
        
#     def update(self):
#         pass

###### DRAW LASER USING SELF.IMAGE = PYGAME.DRAW.AALINE(XYZ)
# class Laser(pygame.sprite.Sprite):
#     def __init__(self, colour, startingx, startingy, endingx, endingy):
#         super().__init__()

class Gun(pygame.sprite.Sprite):
    def __init__(self, width, height, objector):
        super().__init__()
        self.player = objector
        self.width = width
        self.height = height
        
        

        self.guntextureright = pygame.image.load(guntextureright)
        self.guntextureleft = pygame.image.load(guntextureleft)

        
        self.picture = pygame.transform.scale(self.guntextureleft, (width, height))
        self.image = self.picture

        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + ((self.player.width) + 10)
        self.rect.y = self.player.rect.y + (int(round(self.player.height/2)) - 5)

        self.gunrotationangle = 0
        self.gun_line_colour = "transparent"

    def update(self):
        
        player_center_x = self.player.rect.x + round(self.player.width/2)
        player_center_y = self.player.rect.y + round(self.player.height/2)

        if self.player.direction == "right":
            self.rect.x = self.player.rect.x + ((self.player.width) - 10)
            self.rect.y = self.player.rect.y + (int(round(self.player.height/2)) - 20)
            self.picture = pygame.transform.scale(self.guntextureright, (self.width, self.height))
            self.image = self.picture
        elif self.player.direction == "left":
            self.rect.x = self.player.rect.x - ((self.width) - 10)
            self.rect.y = self.player.rect.y + (int(round(self.player.height/2)) - 20)
            self.picture = pygame.transform.scale(self.guntextureleft, (self.width, self.height))
            self.image = self.picture

        xdist = self.player.mouse_rect.x - player_center_x #self.player.mouse_rect.x - self.rect.x
        ydist = player_center_y - self.player.mouse_rect.y #(self.rect.y + round(self.player.width/2)) - self.player.mouse_rect.y
        
        if xdist != 0:
            if round(math.degrees(math.atan(ydist/xdist)), 3) > -26 and round(math.degrees(math.atan(ydist/xdist)), 3) < 26:
                self.gunrotationangle = round(math.degrees(math.atan(ydist/xdist)), 3)
        
        # print(self.gunrotationangle)
        tempx = self.rect.x
        tempy = self.rect.y

        if self.player.direction == "right":
            gun_x_pivot = tempx
        elif self.player.direction == "left":
            gun_x_pivot = tempx + self.width
        
        gun_y_pivot = tempy + round(self.height/2)
        
        self.image = pygame.transform.rotate(self.image, self.gunrotationangle)
        self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))
        #self.rect = self.image.get_rect(center=self.image.get_rect(center= (gun_x_pivot, gun_y_pivot)).center)
        
        # if self.player.direction == "right":
        #     self.rect.x += 15
        if self.player.direction == "left":
            self.rect.x += self.width
            
        self.rect.y = self.rect.y + 30
        gun_width = 50
        gun_height = 20

        if self.player.direction == "right":
            gun_rect_x = self.player.rect.x + self.player.width + gun_width -10 # value of +50px difference 
        elif self.player.direction == "left":
            gun_rect_x = self.player.rect.x - gun_width + 5

        gun_rect_y = self.player.rect.y + round(gun_height/2) + round(self.player.height/2) #+47 difference
            

        
        # gun

        # print(gun_rect_x, self.player.mouse_rect.x, gun_rect_y, self.player.mouse_rect.y)
        
        
        if self.gun_line_colour != "transparent":
            if self.player.direction == "right":
                self.gun_line = pygame.draw.line(screen, self.gun_line_colour, (gun_x_pivot+30, gun_y_pivot+10), (int(self.player.mouse_rect.x), int(self.player.mouse_rect.y)), 3)
            elif self.player.direction == "left":
                self.gun_line = pygame.draw.line(screen, self.gun_line_colour, (gun_x_pivot-10, gun_y_pivot+10), (int(self.player.mouse_rect.x), int(self.player.mouse_rect.y)), 3)
            # self.gun_line = pygame.draw.line(screen, self.gun_line_colour, ((gun_rect_x), gun_rect_y), (int(self.player.mouse_rect.x), int(self.player.mouse_rect.y)), 3)
        

        #print(xdist, ydist)

class Ground(pygame.sprite.Sprite):
    def __init__(self, width, height, x_pos, y_pos):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
    def update(self):
        pass

class RectShader(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0
        self.colour = RED
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.xoffset = 0
        self.yoffset = 0
        self.active = False

    def set_pos(self, xpos, ypos):
        self.box_x = xpos
        self.box_y = ypos
    
    def set_colour(self, colour):
        self.colour = colour
    
    def set_width_height(self, width, height):
        self.width = width + (width/5)
        self.height = height + (height/5)
        self.xoffset = width/10
        self.yoffset = height/10

    def update(self):
        if self.active == True:
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(self.colour)
            self.image.set_alpha(155)
            self.rect = self.image.get_rect()
            self.rect.x = self.box_x - self.xoffset
            self.rect.y = self.box_y - self.yoffset
        else:
            self.image.set_alpha(0)
        


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, x_pos, y_pos):
        super().__init__()
        
        
        self.width = width
        self.height = height
        picture = pygame.image.load(rightplayer)
        picture = pygame.transform.scale(picture, (width, height))
        self.image = picture
        # self.image = pygame.Surface([width, height])
        # self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.xspeed = 0
        self.yspeed = 0
        

        self.grounded = False
        self.ygroundposition = 10000
        self.xgroundposition = -10000
        self.xgroundpositionending = 20000

        self.xwallstart = 10000
        self.xwallend = 20000

        self.able_to_scale = False

        self.left_tracer_ground = 0
        self.right_tracer_ground = 1
        self.left_tracer_box = 2
        self.right_tracer_box = 3
        self.direction = ""

        self.mouse = pygame.Surface((5,5))
        self.mouse_rect = self.mouse.get_rect()
        (self.mouse_rect.x, self.mouse_rect.y) = pygame.mouse.get_pos()

        self.resetxpos = self.rect.x
        self.resetypos = self.rect.y

    def resetygroundposition(self):
        self.ygroundposition = 10000
    
    def playerdirection(self, inputdirection):
        self.direction = inputdirection
    
    def resetwallposition(self):
        self.xwallstart = 10000
        self.xwallend = 20000
    
    def glitch_into_wall(self, startxpos, endxpos):
        self.xwallstart = startxpos
        self.xwallend = endxpos
    
    def set_left_tracer(self, ypos):
        self.left_tracer_ground = ypos
    
    def set_right_tracer(self, ypos):
        self.right_tracer_ground = ypos
    
    def set_left_tracer_box(self, ypos):
        self.left_tracer_box = ypos
    
    def set_right_tracer_box(self, ypos):
        self.right_tracer_box = ypos

    def setypos(self, y):
        self.rect.y = y - self.height
        self.ygroundposition = self.rect.y

    def setxpos(self, xstarting, xending):
        self.xgroundposition = xstarting
        self.xgroundpositionending = xending+xstarting

    def setxspeed(self, horzspeed):
        self.xspeed = horzspeed
    
    def setyspeed(self, vertspeed):
        self.yspeed = vertspeed
    
    def getyspeed(self):
        return self.yspeed

    def update(self):
        (self.mouse_rect.x, self.mouse_rect.y) = pygame.mouse.get_pos()

        if self.mouse_rect.x >= self.rect.x + round(self.width/2) and self.direction != "right":  # == "right":
            picture = pygame.image.load(rightplayer)
            picture = pygame.transform.scale(picture, (self.width, self.height))
            self.image = picture
            self.direction = "right"
            player_gun.gunrotationangle = player_gun.gunrotationangle*-1 
        elif self.mouse_rect.x <= self.rect.x + round(self.width/2)  and self.direction != "left":  # == "left":
            picture = pygame.image.load(leftplayer)
            picture = pygame.transform.scale(picture, (self.width, self.height))
            self.image = picture
            self.direction = "left"
            player_gun.gunrotationangle = player_gun.gunrotationangle*-1 
        
        
        if self.left_tracer_ground == self.right_tracer_ground and self.rect.y < self.left_tracer_ground:
            self.ygroundposition = self.left_tracer_ground
        
        #print(self.rect.y, self.ygroundposition)
        

        if self.rect.y >= self.ygroundposition:
            #print(self.ygroundposition-1, (self.rect.y))
            #print(self.ygroundposition)
            self.rect.y = self.ygroundposition - self.height - 1
            self.grounded = True
        
        if self.rect.x+self.width > self.xwallstart and self.rect.x+self.width < self.xwallend:
            self.rect.x = self.xwallstart - self.width - 1
        elif self.rect.x < self.xwallend and self.rect.x > self.xwallstart:
            self.rect.x = self.xwallend + 1
        
        if self.rect.y > self.ygroundposition - 10:
            self.grounded = False

        if self.grounded == False:
            self.setyspeed(self.yspeed + 0.37)
        else:
            self.setyspeed(0)
        

        if self.rect.y > 1000:
            global level, levelincremention, all_shapes, all_grounds, all_grounds_shapes, rectangletracers, exitdoors, loadedlevel, retry
            
            if level == 7:
                retry = True
                level = 0
                self.rect.x = 0
                self.rect.y = 350
                levelincremention = True
                all_shapes = pygame.sprite.Group()
                all_grounds = pygame.sprite.Group()
                all_grounds_shapes = pygame.sprite.Group()
                rectangletracers = pygame.sprite.Group()
                exitdoors = pygame.sprite.Group()
                loadedlevel = False
            else:
                self.setyspeed(0.1)
                #self.rect.x = self.resetxpos
                self.rect.y = self.resetypos
        
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if (self.rect.x + self.width + 2) < self.xgroundposition or (self.rect.x - 2) > self.xgroundpositionending:
            self.grounded = False
        
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x+self.width >1000:
            self.rect.x = 1000-self.width
        
        # print(self.rect.y, self.ygroundposition, self.grounded)
        
        # if self.rect.x > 640-self.speed - self.width:
        #     self.rect.x = 640 - self.width
        # if self.rect.x < 1+self.speed:
        #     self.rect.x = 1
    

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, width, height, x_pos, y_pos, weight):
        super().__init__()
        self.width = width
        self.height = height
        self.ratio = self.width/self.height
        # self.image = pygame.Surface([200,200])
        # self.image.fill(WHITE)
        

        if self.ratio == 1:
            self.texture = boxsquare
        elif self.ratio == 2:
            self.texture = boxrectangle
        
        self.picture1 = pygame.image.load(self.texture)
        self.picture = pygame.transform.scale(self.picture1, (width, height))
        self.image = self.picture
        
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        
        self.yspeed = 0
        self.grounded = False

        self.ygroundposition = 10000
        self.xgroundstarting = 10000
        self.xgroundending = 20000
        self.ywallposition = 100000

        self.xgroundstartingleft = 10000
        self.xgroundendingleft = 20000

        self.xgroundstartingright = 10000
        self.xgroundendingright = 20000

        if weight == "light":
            self.gravitationalspeed = 0.15
        elif weight == "medium":
            self.gravitationalspeed = 0.23
        elif weight == "heavy":
            self.gravitationalspeed = 0.4

        self.resetwidth = width
        self.resetheight = height
        self.resetx = x_pos
        self.resety = y_pos
        
        # self.drag = DragOperator(self.rect)
        self.mouse = pygame.Surface((5,5))
        self.mouse_rect = self.mouse.get_rect()
        self.mouse_offset_monitor = False
        self.xdist_mouse = 0
        self.ydist_mouse = 0
        (self.mouse_rect.centerx , self.mouse_rect.centery) = pygame.mouse.get_pos()

        self.player_box_initialdisplacement = -1337
        self.player_box_set_initialdisplacement = False
        self.scaling_percentage = 1
        self.tempscalingpercentage = 1
        self.scaling_potential_width = self.width
        self.scaling_potential_height = self.height

        self.resetxpos = self.rect.x
        self.resetypos = self.rect.y

    def reset_attributes(self):
        self.width = self.resetwidth
        self.height = self.resetheight
        self.scaling_potential_width = self.resetwidth
        self.scaling_potential_height = self.resetheight
        self.picture1 = pygame.image.load(self.texture)
        self.picture = pygame.transform.scale(self.picture1, (self.width, self.height))
        self.image = self.picture
        self.rect = self.image.get_rect()
        self.rect.x = self.resetxpos
        self.rect.y = self.resetypos


    def resetygroundposition(self):
        self.ygroundposition = 10000
    
    def reset_wall_barriers(self):
        self.xgroundstarting = 10000
        self.xgroundending = 20000
    
    def glitch_into_wall(self, startxpos, endxpos, ypos):
        self.xgroundstarting = startxpos
        self.xgroundending = endxpos
        self.ywallposition = ypos

    def set_right_tracer(self, ypos):
        self.rightygroundposition = ypos

    def set_left_tracer(self, ypos):
        self.leftygroundposition = ypos
    
    def set_bottomtracer(self, xstart, xend, yground):
        self.ywallposition = yground
        self.xgroundstarting = xstart
        self.xgroundending = xend
    
    def setgroundypos(self, ypos):
        self.ygroundposition = ypos
    
    def setleftgroundxcords(self, xpos, width):
        self.xgroundstartingleft = xpos
        self.xgroundendingleft = xpos+width
    
    def setrightgroundxcords(self, xpos, width):
        self.xgroundstartingright = xpos
        self.xgroundendingright = xpos+width

    def setyspeed(self, speed):
        self.yspeed = speed

    def move(self):
        if pygame.MOUSEBUTTONDOWN:
            click = (pygame.mouse.get_pressed())
            if click[0] == 1 and self.mouse_rect.colliderect(self.rect) and click[2] == 0:
                self.grounded = False
                self.yspeed = 0
                
                player_gun.gun_line_colour = BLUE

                if self.mouse_offset_monitor == False:
                    self.xdist_mouse = self.mouse_rect.x - self.rect.x
                    self.ydist_mouse = self.mouse_rect.y - self.rect.y
                    self.mouse_offset_monitor = True

                self.rect.x = self.mouse_rect.x - self.xdist_mouse
                self.rect.y = self.mouse_rect.y - self.ydist_mouse

                if self.rect.y + self.scaling_potential_height > self.ygroundposition:
                    self.rect.y = self.ygroundposition - self.scaling_potential_height
                
                if self.rect.y + self.scaling_potential_height > self.ywallposition:
                    if self.rect.x+self.scaling_potential_width > self.xgroundstarting and self.rect.x+self.scaling_potential_width  < self.xgroundending:
                        self.rect.x = self.xgroundstarting - self.scaling_potential_width
                    elif self.rect.x < self.xgroundending and self.rect.x > self.xgroundstarting:
                        self.rect.x = self.xgroundending
                
                

                player_box_xdistance = self.rect.x - player.rect.x
                player_box_ydistance = self.rect.y - player.rect.y
                player_box_hypotenuse = round(math.sqrt(((player_box_xdistance)**2) + ((player_box_ydistance)**2)))
                

                if self.player_box_set_initialdisplacement == False:
                    self.player_box_initialdisplacement = player_box_hypotenuse
                    self.player_box_set_initialdisplacement = True
                
                

                scaling_difference = (player_box_hypotenuse - self.player_box_initialdisplacement)/500
                
                
                self.scaling_percentage = scaling_difference #* -1
                
                tempx = self.rect.x
                tempy = self.rect.y
                
                
                
                
                
                if 1+self.scaling_percentage != self.tempscalingpercentage and self.scaling_percentage != 0:
                    self.scaling_potential_width = int(self.width * (1+ (self.scaling_percentage)))
                    self.scaling_potential_height = int(self.height* (1+ (self.scaling_percentage)))
                    
                    if self.ratio == 1:
                        if self.scaling_potential_width > 400:
                            self.scaling_potential_width = 400
                        if self.scaling_potential_height > 400/self.ratio:
                            self.scaling_potential_height = 400/self.ratio
                    elif self.ratio == 2:
                        if self.scaling_potential_width > 400:
                            self.scaling_potential_width = 400
                        if self.scaling_potential_height > 200:
                            self.scaling_potential_height = 200
                        

                    self.image = pygame.transform.scale(self.picture1, (int(round(self.scaling_potential_width)), int(round(self.scaling_potential_height))))
                    self.rect = self.image.get_rect()
                    self.rect.x = tempx
                    self.rect.y = tempy

                # print(self.scaling_potential_width, self.scaling_potential_height)
                
                
                # if self.scaling_percentage + 1 == self.tempscalingpercentage:
                #     self.player_box_set_initialdisplacement = False
                
                self.tempscalingpercentage = 1+self.scaling_percentage

                # if self.rect.y + self.height < self.ywallposition:
                #     self.reset_wall_barriers()

                # if self.rect.x+self.width > self.xgroundstarting and self.rect.x+self.width < self.xgroundending:
                #     self.rect.x = self.xgroundstarting - self.width - 1
                # elif self.rect.x < self.xgroundending and self.rect.x > self.xgroundstarting:
                #     self.rect.x = self.xgroundending + 1

                rectanglesshaders.active = True

                rectanglesshaders.set_pos(self.rect.x, self.rect.y)
                rectanglesshaders.set_colour(BLUE)
                rectanglesshaders.set_width_height(self.scaling_potential_width, self.scaling_potential_height)

            elif click[2] == 1 and self.mouse_rect.colliderect(self.rect) and click[0] == 0:
                self.grounded = False
                self.yspeed = 0
                
                player_gun.gun_line_colour = ORANGE

                if self.mouse_offset_monitor == False:
                    self.xdist_mouse = self.mouse_rect.x - self.rect.x
                    self.ydist_mouse = self.mouse_rect.y - self.rect.y
                    self.mouse_offset_monitor = True

                self.rect.x = self.mouse_rect.x - self.xdist_mouse
                self.rect.y = self.mouse_rect.y - self.ydist_mouse

                if self.rect.y + self.scaling_potential_height > self.ygroundposition:
                    self.rect.y = self.ygroundposition - self.scaling_potential_height
                
                if self.rect.y + self.scaling_potential_height > self.ywallposition:
                    if self.rect.x+self.scaling_potential_width > self.xgroundstarting and self.rect.x+self.scaling_potential_width  < self.xgroundending:
                        self.rect.x = self.xgroundstarting - self.scaling_potential_width
                    elif self.rect.x < self.xgroundending and self.rect.x > self.xgroundstarting:
                        self.rect.x = self.xgroundending
                
                rectanglesshaders.active = True

                rectanglesshaders.set_pos(self.rect.x, self.rect.y)
                rectanglesshaders.set_colour(ORANGE)
                rectanglesshaders.set_width_height(self.scaling_potential_width, self.scaling_potential_height)

                
            else:
                self.mouse_offset_monitor = False
                self.player_box_set_initialdisplacement = False
                self.player_box_initialdisplacement = -1337
                self.scaling_percentage = 1
                self.size = self.image.get_size()
                self.width = self.size[0]
                self.height = self.size[1]
                self.scaling_potential_width = self.size[0]
                self.scaling_potential_height = self.size[1]
                player_gun.gun_line_colour = "transparent"
                rectanglesshaders.active = False

        #print(xdist_mouse)


    def update(self):#, event_list):
        #print(self.mouse_rect.centerx, self.mouse_rect.centery)
        #print(self.rect.x, self.mouse_rect.centerx)
        # print(self.leftygroundposition, self.rightygroundposition,self.ygroundposition)
            
        if self.rect.y < self.leftygroundposition or self.rect.y > self.rightygroundposition:
            if self.leftygroundposition == self.rightygroundposition or self.leftygroundposition < self.rightygroundposition:
                self.ygroundposition = self.leftygroundposition
            elif self.leftygroundposition > self.rightygroundposition:
                self.ygroundposition = self.rightygroundposition

        # print(self.leftygroundposition, self.rightygroundposition,self.ygroundposition)

        (self.mouse_rect.centerx, self.mouse_rect.centery) = pygame.mouse.get_pos()
        
        # print("mouse", self.mouse_rect.x , self.mouse_rect.y)

        # print(self.rect.y + self.height, self.ywallposition)
        if player.able_to_scale == True:
            self.move()
    
        # print(self.rect.x, self.rect.x + self.width, self.xgroundstarting, self.xgroundending)
        # print(self.rect.y + self.height, self.ywallposition)
        

        
        if self.grounded == False:
            self.setyspeed(self.yspeed+self.gravitationalspeed)
        else:
            self.setyspeed(0)
            self.rect.y = self.ygroundposition - self.scaling_potential_height
        
        
        #if self.rect.y + self.height - 10 > self.ygroundposition:

        if self.rect.y + self.scaling_potential_height > self.ygroundposition:
            self.rect.y = self.ygroundposition - self.scaling_potential_height
            self.grounded = True
        
        

        
        self.rect.y += self.yspeed

        if self.rect.y > 1500:
            self.setyspeed(0.1)
            self.rect.y = -250
            self.rect.x = self.resetxpos
        
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.scaling_potential_width > 1000:
            self.rect.x = 1000 - self.scaling_potential_width
        rectanglesshaders.set_pos(self.rect.x, self.rect.y)



class GroundWallTracer(pygame.sprite.Sprite):
    def __init__(self, objecter, typeofobject, side):
        super().__init__()
        self.tracing = objecter
        self.side = side
        if typeofobject == "player":
            self.object = "player"
            self.image = pygame.Surface([1, 1000])
            self.image.fill(LIGHT_BLUE)
            self.image.set_alpha(0)
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0
        else:
            self.object = "rectangle"
            if side == "top" or side == "bottom":
                self.image = pygame.Surface([self.tracing.scaling_potential_width+(self.tracing.scaling_potential_width/2), 1])
            elif side =="left" or side == "right":
                self.image = pygame.Surface([1, 2000])
            self.image.fill(LIGHT_BLUE)
            self.image.set_alpha(0)
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0
    
    def update(self):
        if self.object == "player":
            if self.side =="left":
                self.rect.x = self.tracing.rect.x              
            elif self.side == "right":
                self.rect.x = (self.tracing.rect.x + self.tracing.width) - 1
            
            self.rect.y = self.tracing.rect.y + self.tracing.height
        else:
            if self.side == "left" or self.side == "right":
                
                self.image = pygame.Surface([1,2000])
                self.image.fill(LIGHT_BLUE)
                self.rect = self.image.get_rect()
                if self.side == "left":
                    self.rect.x = self.tracing.rect.x
                elif self.side == "right":
                    self.rect.x = (self.tracing.rect.x + self.tracing.scaling_potential_width) - 3
                self.rect.y = self.tracing.rect.y + self.tracing.scaling_potential_height
            elif self.side == "top" or self.side == "bottom":
                self.image = pygame.Surface([self.tracing.scaling_potential_width+(self.tracing.scaling_potential_width/2), 1])
                self.image.fill(LIGHT_BLUE)
                self.rect = self.image.get_rect()
                if self.side == "top":
                    self.rect.y = self.tracing.rect.y
                elif self.side == "bottom":
                    self.rect.y = self.tracing.rect.y + self.tracing.scaling_potential_height - 2
                self.rect.x = self.tracing.rect.x - (self.tracing.scaling_potential_width/4)
            self.image.set_alpha(0)
            
class ExitDoor(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        # self.image = pygame.Surface([60, 130])
        # self.image.fill(BLACK)
        picture = pygame.transform.scale(exitdoorimage, (60, 130))
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.instantiated = False
        self.x = xpos
        self.y = ypos
    
    def set_pos(self, xpos, ypos):
        self.instantiated = False
        self.x = xpos
        self.y = ypos

    def update(self):
        if self.instantiated == False:
            self.rect.x = self.x
            self.rect.y = self.y
            self.instantiated = True


all_shapes = pygame.sprite.Group()
playergroup = pygame.sprite.Group()
all_grounds = pygame.sprite.Group()
all_grounds_shapes = pygame.sprite.Group()
tracers = pygame.sprite.Group()
rectangletracers = pygame.sprite.Group()
exitdoors = pygame.sprite.Group()

shaders = pygame.sprite.Group()
rectanglesshaders = RectShader()
shaders.add(rectanglesshaders)


# rectangle2 = Rectangle(200, 100, 500, 150)
# all_shapes.add(rectangle2)



#base ground
#width, height, x, y

def load_level_1():
    exitdoors.add(Exit1)
    all_grounds.add(ground1)
    all_grounds_shapes.add(ground1)
    all_grounds.add(ground2)
    all_grounds_shapes.add(ground2)
    all_grounds.add(ground3)
    all_grounds_shapes.add(ground3)
    all_shapes.add(rectangle1)
    all_grounds_shapes.add(rectangle1)
    rectangletracers.add(rectangle1_left_groundtracer)
    rectangletracers.add(rectangle1_right_groundtracer)
    rectangletracers.add(rectangle1_bottom_walltracer)

def load_level_2():
    exitdoors.add(Exit2)
    all_grounds.add(ground2)
    all_grounds_shapes.add(ground2)
    all_grounds.add(ground4)
    all_grounds_shapes.add(ground4)
    all_grounds.add(ground5)
    all_grounds_shapes.add(ground5)
    all_shapes.add(rectangle2)
    all_grounds_shapes.add(rectangle2)
    rectangletracers.add(rectangle2_left_groundtracer)
    rectangletracers.add(rectangle2_right_groundtracer)
    rectangletracers.add(rectangle2_bottom_walltracer)

def load_level_3():
    exitdoors.add(Exit3)
    all_grounds.add(ground4)
    all_grounds_shapes.add(ground4)
    all_grounds.add(ground6)
    all_grounds_shapes.add(ground6)
    all_grounds.add(ground7)
    all_grounds_shapes.add(ground7)
    all_shapes.add(rectangle3)
    all_grounds_shapes.add(rectangle3)
    rectangletracers.add(rectangle3_left_groundtracer)
    rectangletracers.add(rectangle3_right_groundtracer)
    rectangletracers.add(rectangle3_bottom_walltracer)

def load_level_4():
    exitdoors.add(Exit4)
    all_grounds.add(ground7)
    all_grounds_shapes.add(ground7)
    all_grounds.add(ground8)
    all_grounds_shapes.add(ground8)
    all_grounds.add(ground9)
    all_grounds_shapes.add(ground9)
    all_shapes.add(rectangle4)
    all_grounds_shapes.add(rectangle4)
    rectangletracers.add(rectangle4_left_groundtracer)
    rectangletracers.add(rectangle4_right_groundtracer)
    rectangletracers.add(rectangle4_bottom_walltracer)

def load_level_5():
    exitdoors.add(Exit5)
    all_grounds.add(ground9)
    all_grounds_shapes.add(ground9)
    all_grounds.add(ground10)
    all_grounds_shapes.add(ground10)
    all_grounds.add(ground11)
    all_grounds_shapes.add(ground11)
    all_grounds.add(ground12)
    all_grounds_shapes.add(ground12)
    all_shapes.add(rectangle5)
    all_grounds_shapes.add(rectangle5)
    rectangletracers.add(rectangle5_left_groundtracer)
    rectangletracers.add(rectangle5_right_groundtracer)
    rectangletracers.add(rectangle5_bottom_walltracer)

def load_level_6():
    exitdoors.add(Exit6)
    all_grounds.add(ground11)
    all_grounds_shapes.add(ground11)
    all_grounds.add(ground13)
    all_grounds_shapes.add(ground13)

def load_level_7():
    exitdoors.add(Exit7)
    all_grounds.add(ground13)
    all_grounds_shapes.add(ground13)
    all_grounds.add(ground14)
    all_grounds_shapes.add(ground14)
    all_grounds.add(ground15)
    all_grounds_shapes.add(ground15)
    all_shapes.add(rectangle6)
    all_grounds_shapes.add(rectangle6)
    rectangletracers.add(rectangle6_left_groundtracer)
    rectangletracers.add(rectangle6_right_groundtracer)
    rectangletracers.add(rectangle6_bottom_walltracer)

def load_ending():
    all_grounds.add(ground15)
    all_grounds_shapes.add(ground15)




#####################                      level 1
Exit1 = ExitDoor(880, 20)
ground1 = Ground(1337, 350, -171, 500)
ground2 = Ground(200, 2000, 800, 150)
ground3 = Ground(200, 500, 600, 300)

rectangle1 = Rectangle(100, 100, 200, 400, "light")

rectangle1_left_groundtracer = GroundWallTracer(rectangle1, "rectangle", "left")
rectangle1_right_groundtracer = GroundWallTracer(rectangle1, "rectangle", "right")
# rectangle1_top_walltracer = GroundWallTracer(rectangle1, "rectangle", "top")
# rectangletracers.add(rectangle1_top_walltracer)
rectangle1_bottom_walltracer = GroundWallTracer(rectangle1, "rectangle", "bottom")

#####################                      level 2
Exit2 = ExitDoor(60, 270)
ground4 = Ground(350, 2000, 0, 400)
ground5 = Ground(450, 200, 350, 2100)
rectangle2 = Rectangle(200, 100, 140, 250, "heavy")
rectangle2_left_groundtracer = GroundWallTracer(rectangle2, "rectangle", "left")
rectangle2_right_groundtracer = GroundWallTracer(rectangle2, "rectangle", "right")
rectangle2_bottom_walltracer = GroundWallTracer(rectangle2, "rectangle", "bottom")

#####################                      level 3
Exit3 = ExitDoor(900, 430)
ground6 = Ground(450, 200, 350, 2100)
ground7 = Ground(200, 500, 800, 560)
rectangle3 = Rectangle(40, 20, 310, 380, "medium")
rectangle3_left_groundtracer = GroundWallTracer(rectangle3, "rectangle", "left")
rectangle3_right_groundtracer = GroundWallTracer(rectangle3, "rectangle", "right")
rectangle3_bottom_walltracer = GroundWallTracer(rectangle3, "rectangle", "bottom")

#####################                      level 4
Exit4 = ExitDoor(30, 70)
ground8 = Ground(500, 700, 300, 500)
ground9 = Ground(300, 900, 0, 200)
rectangle4 = Rectangle(100, 100, 150, 50, "light")
rectangle4_left_groundtracer = GroundWallTracer(rectangle4, "rectangle", "left")
rectangle4_right_groundtracer = GroundWallTracer(rectangle4, "rectangle", "right")
rectangle4_bottom_walltracer = GroundWallTracer(rectangle4, "rectangle", "bottom")

#####################                       level 5
Exit5 = ExitDoor(920, 370)
ground10 = Ground(200, 500, 300, 500)
ground11 = Ground(250, 200, 750, 500)
ground12 = Ground(250, 200, 500, 2100)
rectangle5 = Rectangle(200, 200, 700, 300, "light")
rectangle5_left_groundtracer = GroundWallTracer(rectangle5, "rectangle", "left")
rectangle5_right_groundtracer = GroundWallTracer(rectangle5, "rectangle", "right")
rectangle5_bottom_walltracer = GroundWallTracer(rectangle5, "rectangle", "bottom")

#####################                       level 6
Exit6 = ExitDoor(30, 70)
ground13 = Ground(200, 700, 0, 200)

#####################                       level 7
Exit7 = ExitDoor(850, 370)
ground14 = Ground(500, 700, 200, 200)
ground15 = Ground(300, 300, 700, 500)
rectangle6 = Rectangle(200, 200, 500, 0, "light")
rectangle6_left_groundtracer = GroundWallTracer(rectangle6, "rectangle", "left")
rectangle6_right_groundtracer = GroundWallTracer(rectangle6, "rectangle", "right")
rectangle6_bottom_walltracer = GroundWallTracer(rectangle6, "rectangle", "bottom")



player = Player(60, 94, 0, 350)
playergroup.add(player)

player_gun = Gun(120, 40, player)
playergroup.add(player_gun)

player_left_groundtracer = GroundWallTracer(player, "player", "left")
tracers.add(player_left_groundtracer)

player_right_groundtracer = GroundWallTracer(player, "player", "right")
tracers.add(player_right_groundtracer)



# rectangle2_left_groundtracer = GroundWallTracer(rectangle2, "rectangle", "left")
# rectangletracers.add(rectangle2_left_groundtracer)

# rectangle2_right_groundtracer = GroundWallTracer(rectangle2, "rectangle", "right")
# rectangletracers.add(rectangle2_right_groundtracer)
# if str(audio)!= "0":
#     pygame.mixer.music.play(100)

while not game_over:
    if loadedlevel == False:
        loadedlevel = True
        levelincremention = False
        if level == 0:
            backgroundimage = background1
            load_level_1()
        elif level == 1:
            backgroundimage = background2
            load_level_2()
        elif level == 2:
            backgroundimage = background3
            load_level_3()
        elif level == 3:
            backgroundimage = background4
            load_level_4()
        elif level == 4:
            backgroundimage = background5
            load_level_5()
        elif level == 5:
            backgroundimage = background6
            load_level_6()
        elif level == 6:
            backgroundimage = background7
            load_level_7()
        elif level == 7:
            backgroundimage = background8
            load_ending()
            ending = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                #print("left down")
                player.setxspeed(-3)
                player.playerdirection("left")
            if event.key == pygame.K_d:
                #print("right down")
                player.setxspeed(3)
                player.playerdirection("right")
            if event.key == pygame.K_w:
                if player.grounded == True:
                    player.grounded = False
                    player.able_to_scale = False
                    player.setyspeed(-11)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                #print("left up")
                player.setxspeed(0)
            if event.key == pygame.K_d:
                #print("right up")
                player.setxspeed(0)
            # if event.key == pygame.K_UP:
            #     player.setyspeed(0)
            # if event.key == pygame.K_RIGHT:
            #     player.setxspeed(0)
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:            
        #         if rectangle.collidepoint(event.pos):
        #             rectangle_dragging = True
        #             mouse_x, mouse_y = event.pos
        #             offset_x = rectangle.x - mouse_x
        #             offset_y = rectangle.y - mouse_y
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:            
        #         rectangle_dragging = False
        # elif event.type == pygame.MOUSEMOTION:
        #     if rectangle_dragging == True:
        #         mouse_x, mouse_y = event.pos
        #         rectangle.x = mouse_x + offset_x
        #         rectangle.y = mouse_y + offset_y
    #next event

    #game logic
    # keys_pressed = pygame.key.get_pressed()
    # if keys_pressed[pygame.K_RIGHT]:
    #     #print("2 right down")
    #     player.setxspeed(3)
     
    # if keys_pressed[pygame.K_LEFT]:
    #     #print("2 left down")
    #     player.setxspeed(-3)


    # if keys_pressed[pygame.K_UP]:
    #     pass
    # if keys_pressed[pygame.K_DOWN]:
    #     pass
    player.able_to_scale = True
    
    player_ground_left_tracercollision = pygame.sprite.spritecollide(player_left_groundtracer, all_grounds_shapes, False, False)
    for foo in player_ground_left_tracercollision:
        player.set_left_tracer(foo.rect.y)
        player_ground_left_tracercollision = []
    
    player_box_left_tracercollision = pygame.sprite.spritecollide(player_left_groundtracer, all_shapes, False, False)
    for foo in player_box_left_tracercollision:
        player.set_left_tracer_box(foo.rect.y)
        player.able_to_scale = False
        player_box_left_tracercollision = []
    
    player_ground_right_tracercollision = pygame.sprite.spritecollide(player_right_groundtracer, all_grounds_shapes, False, False)
    for foo in player_ground_right_tracercollision:
        player.set_right_tracer(foo.rect.y)
        player_ground_right_tracercollision = []
    
    player_box_right_tracercollision = pygame.sprite.spritecollide(player_right_groundtracer, all_shapes, False, False)
    for foo in player_box_right_tracercollision:
        player.set_right_tracer_box(foo.rect.y)
        player.able_to_scale = False
        player_box_right_tracercollision = []



    


    
    rectangle1_ground_left_tracercollision = pygame.sprite.spritecollide(rectangle1_left_groundtracer, all_grounds, False, False)
    for foo in rectangle1_ground_left_tracercollision:
        rectangle1.set_left_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle1.setleftgroundxcords(foo.rect.x, foo.width)
        rectangle1_ground_left_tracercollision = []

    rectangle1_ground_right_tracercollision = pygame.sprite.spritecollide(rectangle1_right_groundtracer, all_grounds, False, False)
    for foo in rectangle1_ground_right_tracercollision:
        rectangle1.set_right_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle1.setrightgroundxcords(foo.rect.x, foo.width)
        rectangle1_ground_right_tracercollision = []

    if rectangle1.grounded == False:
        rectangle1groundcollision = pygame.sprite.spritecollide(rectangle1, all_grounds, False, False)
        for foo in rectangle1groundcollision:
            if foo.rect.y > (rectangle1.rect.y + player.height - 20):
                rectangle1.grounded = True
                rectangle1.setgroundypos(foo.rect.y)
                playergroundcollision = []

    rectangle1wallcollision = pygame.sprite.spritecollide(rectangle1, all_grounds, False, False)
    for foo in rectangle1wallcollision:
        if foo.rect.y < 1 + rectangle1.rect.y + rectangle1.height:
            if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
                rectangle1.glitch_into_wall(foo.rect.x, foo.width+foo.rect.x, foo.rect.y)
                rectangle1wallcollision = []
    
    rectangle1_bottom_walltracer_collision = pygame.sprite.spritecollide(rectangle1_bottom_walltracer, all_grounds, False, False)
    for foo in rectangle1_bottom_walltracer_collision:
        rectangle1.set_bottomtracer(foo.rect.x, foo.rect.x + foo.width, foo.rect.y)
        rectangle1_bottom_walltracer_collision = []

    # rectangle1_top_walltracer_collision = pygame.sprite.spritecollide(rectangle1_top_walltracer, all_grounds_shapes, False, False)
    # for foo in rectangle1_top_walltracer_collision:
    #     rectangle1.set_toptracer(foo.rect.x, foo.rect.x + foo.width)
    #     rectangle1_top_walltracer_collision = []
    
    rectangle2_ground_left_tracercollision = pygame.sprite.spritecollide(rectangle2_left_groundtracer, all_grounds, False, False)
    for foo in rectangle2_ground_left_tracercollision:
        rectangle2.set_left_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle2.setleftgroundxcords(foo.rect.x, foo.width)
        rectangle2_ground_left_tracercollision = []

    rectangle2_ground_right_tracercollision = pygame.sprite.spritecollide(rectangle2_right_groundtracer, all_grounds, False, False)
    for foo in rectangle2_ground_right_tracercollision:
        rectangle2.set_right_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle2.setrightgroundxcords(foo.rect.x, foo.width)
        rectangle2_ground_right_tracercollision = []

    if rectangle2.grounded == False:
        rectangle2groundcollision = pygame.sprite.spritecollide(rectangle2, all_grounds, False, False)
        for foo in rectangle2groundcollision:
            if foo.rect.y > (rectangle2.rect.y + player.height - 20):
                rectangle2.grounded = True
                rectangle2.setgroundypos(foo.rect.y)
                playergroundcollision = []

    rectangle2wallcollision = pygame.sprite.spritecollide(rectangle2, all_grounds, False, False)
    for foo in rectangle2wallcollision:
        if foo.rect.y < 1 + rectangle2.rect.y + rectangle2.height:
            if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
                rectangle2.glitch_into_wall(foo.rect.x, foo.width+foo.rect.x, foo.rect.y)
                rectangle2wallcollision = []
    
    rectangle2_bottom_walltracer_collision = pygame.sprite.spritecollide(rectangle2_bottom_walltracer, all_grounds, False, False)
    for foo in rectangle2_bottom_walltracer_collision:
        rectangle2.set_bottomtracer(foo.rect.x, foo.rect.x + foo.width, foo.rect.y)
        rectangle2_bottom_walltracer_collision = []
    

    rectangle3_ground_left_tracercollision = pygame.sprite.spritecollide(rectangle3_left_groundtracer, all_grounds, False, False)
    for foo in rectangle3_ground_left_tracercollision:
        rectangle3.set_left_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle3.setleftgroundxcords(foo.rect.x, foo.width)
        rectangle3_ground_left_tracercollision = []

    rectangle3_ground_right_tracercollision = pygame.sprite.spritecollide(rectangle3_right_groundtracer, all_grounds, False, False)
    for foo in rectangle3_ground_right_tracercollision:
        rectangle3.set_right_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle3.setrightgroundxcords(foo.rect.x, foo.width)
        rectangle3_ground_right_tracercollision = []

    if rectangle3.grounded == False:
        rectangle3groundcollision = pygame.sprite.spritecollide(rectangle3, all_grounds, False, False)
        for foo in rectangle3groundcollision:
            if foo.rect.y > (rectangle3.rect.y + player.height - 20):
                rectangle3.grounded = True
                rectangle3.setgroundypos(foo.rect.y)
                playergroundcollision = []

    rectangle3wallcollision = pygame.sprite.spritecollide(rectangle3, all_grounds, False, False)
    for foo in rectangle3wallcollision:
        if foo.rect.y < 1 + rectangle3.rect.y + rectangle3.height:
            if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
                rectangle3.glitch_into_wall(foo.rect.x, foo.width+foo.rect.x, foo.rect.y)
                rectangle3wallcollision = []
    
    rectangle3_bottom_walltracer_collision = pygame.sprite.spritecollide(rectangle3_bottom_walltracer, all_grounds, False, False)
    for foo in rectangle3_bottom_walltracer_collision:
        rectangle3.set_bottomtracer(foo.rect.x, foo.rect.x + foo.width, foo.rect.y)
        rectangle3_bottom_walltracer_collision = []
    
    rectangle4_ground_left_tracercollision = pygame.sprite.spritecollide(rectangle4_left_groundtracer, all_grounds, False, False)
    for foo in rectangle4_ground_left_tracercollision:
        rectangle4.set_left_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle4.setleftgroundxcords(foo.rect.x, foo.width)
        rectangle4_ground_left_tracercollision = []

    rectangle4_ground_right_tracercollision = pygame.sprite.spritecollide(rectangle4_right_groundtracer, all_grounds, False, False)
    for foo in rectangle4_ground_right_tracercollision:
        rectangle4.set_right_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle4.setrightgroundxcords(foo.rect.x, foo.width)
        rectangle4_ground_right_tracercollision = []

    if rectangle4.grounded == False:
        rectangle4groundcollision = pygame.sprite.spritecollide(rectangle4, all_grounds, False, False)
        for foo in rectangle4groundcollision:
            if foo.rect.y > (rectangle4.rect.y + player.height - 20):
                rectangle4.grounded = True
                rectangle4.setgroundypos(foo.rect.y)
                playergroundcollision = []

    rectangle4wallcollision = pygame.sprite.spritecollide(rectangle4, all_grounds, False, False)
    for foo in rectangle4wallcollision:
        if foo.rect.y < 1 + rectangle4.rect.y + rectangle4.height:
            if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
                rectangle4.glitch_into_wall(foo.rect.x, foo.width+foo.rect.x, foo.rect.y)
                rectangle4wallcollision = []
    
    rectangle4_bottom_walltracer_collision = pygame.sprite.spritecollide(rectangle4_bottom_walltracer, all_grounds, False, False)
    for foo in rectangle4_bottom_walltracer_collision:
        rectangle4.set_bottomtracer(foo.rect.x, foo.rect.x + foo.width, foo.rect.y)
        rectangle4_bottom_walltracer_collision = []

    
    rectangle5_ground_left_tracercollision = pygame.sprite.spritecollide(rectangle5_left_groundtracer, all_grounds, False, False)
    for foo in rectangle5_ground_left_tracercollision:
        rectangle5.set_left_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle5.setleftgroundxcords(foo.rect.x, foo.width)
        rectangle5_ground_left_tracercollision = []

    rectangle5_ground_right_tracercollision = pygame.sprite.spritecollide(rectangle5_right_groundtracer, all_grounds, False, False)
    for foo in rectangle5_ground_right_tracercollision:
        rectangle5.set_right_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle5.setrightgroundxcords(foo.rect.x, foo.width)
        rectangle5_ground_right_tracercollision = []

    if rectangle5.grounded == False:
        rectangle5groundcollision = pygame.sprite.spritecollide(rectangle5, all_grounds, False, False)
        for foo in rectangle5groundcollision:
            if foo.rect.y > (rectangle5.rect.y + player.height - 20):
                rectangle5.grounded = True
                rectangle5.setgroundypos(foo.rect.y)
                playergroundcollision = []

    rectangle5wallcollision = pygame.sprite.spritecollide(rectangle5, all_grounds, False, False)
    for foo in rectangle5wallcollision:
        if foo.rect.y < 1 + rectangle5.rect.y + rectangle5.height:
            if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
                rectangle5.glitch_into_wall(foo.rect.x, foo.width+foo.rect.x, foo.rect.y)
                rectangle5wallcollision = []
    
    rectangle5_bottom_walltracer_collision = pygame.sprite.spritecollide(rectangle5_bottom_walltracer, all_grounds, False, False)
    for foo in rectangle5_bottom_walltracer_collision:
        rectangle5.set_bottomtracer(foo.rect.x, foo.rect.x + foo.width, foo.rect.y)
        rectangle5_bottom_walltracer_collision = []

    rectangle6_ground_left_tracercollision = pygame.sprite.spritecollide(rectangle6_left_groundtracer, all_grounds, False, False)
    for foo in rectangle6_ground_left_tracercollision:
        rectangle6.set_left_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle6.setleftgroundxcords(foo.rect.x, foo.width)
        rectangle6_ground_left_tracercollision = []

    rectangle6_ground_right_tracercollision = pygame.sprite.spritecollide(rectangle6_right_groundtracer, all_grounds, False, False)
    for foo in rectangle6_ground_right_tracercollision:
        rectangle6.set_right_tracer(foo.rect.y)
        if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
            rectangle6.setrightgroundxcords(foo.rect.x, foo.width)
        rectangle6_ground_right_tracercollision = []

    if rectangle6.grounded == False:
        rectangle6groundcollision = pygame.sprite.spritecollide(rectangle6, all_grounds, False, False)
        for foo in rectangle6groundcollision:
            if foo.rect.y > (rectangle6.rect.y + player.height - 20):
                rectangle6.grounded = True
                rectangle6.setgroundypos(foo.rect.y)
                playergroundcollision = []

    rectangle6wallcollision = pygame.sprite.spritecollide(rectangle6, all_grounds, False, False)
    for foo in rectangle6wallcollision:
        if foo.rect.y < 1 + rectangle6.rect.y + rectangle6.height:
            if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
                rectangle6.glitch_into_wall(foo.rect.x, foo.width+foo.rect.x, foo.rect.y)
                rectangle6wallcollision = []
    
    rectangle6_bottom_walltracer_collision = pygame.sprite.spritecollide(rectangle6_bottom_walltracer, all_grounds, False, False)
    for foo in rectangle6_bottom_walltracer_collision:
        rectangle6.set_bottomtracer(foo.rect.x, foo.rect.x + foo.width, foo.rect.y)
        rectangle6_bottom_walltracer_collision = []




    player_actual_shapes_collision = pygame.sprite.spritecollide(player, all_shapes, False, False)
    for foo in player_actual_shapes_collision:
        player.able_to_scale = False
        player_actual_shapes_collision = []
        

    if player.grounded == False:
        player_actual_ground_collision = pygame.sprite.spritecollide(player, all_grounds, False, False)
        for foo in player_actual_ground_collision:
            if foo.rect.y > (player.rect.y+player.height-20):
                player.able_to_scale = True
                player_actual_ground_collision = []

        playergroundcollision = pygame.sprite.spritecollide(player, all_grounds_shapes, False, False)
        for foo in playergroundcollision:
            # print(foo.rect.y)
            # print(player.rect.y+player.height)
            #if the top of the ground is bigger than the foot of the player (remove 15 because player glitches in ground), then the player is "grounded"
            #CHANGED TO 20 SINCE PLAYER WAS GLITCHING THROUGH THE FLOOR
            if foo.rect.y > (player.rect.y+player.height-20):
                player.grounded = True
                player.setypos(foo.rect.y)
                player.setxpos(foo.rect.x, foo.width)
                playergroundcollision = []
    
        
    
    
    playerwallcollision = pygame.sprite.spritecollide(player, all_grounds_shapes, False, False)
    for foo in playerwallcollision:
        if foo.rect.y < player.rect.y + player.height:
            #print(foo.rect.x, foo.width+foo.rect.x)
            if foo.rect.x != (-171) and foo.width+foo.rect.x != 1166:
                player.glitch_into_wall(foo.rect.x, foo.width+foo.rect.x)
                
        playerwallcollision = []
        
    #player's ground position reset to get rid of bug involving glitched above ground

    player.resetygroundposition()


    playerexitcollision = pygame.sprite.spritecollide(player, exitdoors, False, False)
    for foo in playerexitcollision:
        if levelincremention == False:
            player.resetxpos = player.rect.x
            player.resetypos = -100
            level += 1
            player.movemement = False
            levelincremention = True
            all_shapes = pygame.sprite.Group()
            all_grounds = pygame.sprite.Group()
            all_grounds_shapes = pygame.sprite.Group()
            rectangletracers = pygame.sprite.Group()
            exitdoors = pygame.sprite.Group()
            loadedlevel = False
        playerexitcollision = []

    if retry == True:
        retry = False
        rectangle1.reset_attributes()
        rectangle2.reset_attributes()
        rectangle3.reset_attributes()
        rectangle4.reset_attributes()
        rectangle5.reset_attributes()
        rectangle6.reset_attributes()

    screen.blit(backgroundimage, (0,0))
        
    #print(pygame.mouse.get_pressed()[0])
    all_shapes.update()
    playergroup.update()
    tracers.update()
    rectangletracers.update()
    shaders.update()
    player.resetwallposition()
    exitdoors.update()

    #graphics


    shaders.draw(screen)
    all_shapes.draw(screen)
    rectangletracers.draw(screen)
    all_grounds.draw(screen)
    exitdoors.draw(screen)
    playergroup.draw(screen)
    tracers.draw(screen)
    

    #update what has been drawn
    
    pygame.display.flip()

    #limit to 60 fps
    clock.tick(frames_per_second)

pygame.quit()
exit()
