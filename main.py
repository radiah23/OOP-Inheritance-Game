import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from my_sprite import my_sprite
from colliding_object import colliding_object
from moving_vehicle import moving_vehicle

class InitializeTheGame: 
    def initialize_game(self):  
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        return screen 
class Vehicle:     
    def vehicles(self): 
        car1 = moving_vehicle("./images_orig/vehicles/green_car.png", (200,100))
        car2 = moving_vehicle("./images_orig/vehicles/red_car.png", (150,50))
        vehicles = [car1, car2] 
        return vehicles
class Colliding : 
    def colliding(self): 
        colliding_one = colliding_object("./images_orig/vehicles/blueish_van.png", (300,90))
        colliding_two = colliding_object("./images_orig/vehicles/orange_truck.png", (250, 100))
        colliding_three = colliding_object("./images_orig/road/road_bend_down.png", (200,50))
        colliding_four = colliding_object("./images_orig/road/road_turn_down.png", (180,90))
        colliding_five = colliding_object("./images_orig/road/road_turn_up.png", (450,100))
        colliding_objects= [colliding_one, colliding_two, colliding_three, colliding_four, colliding_five]
        return colliding_objects
class Decor : 
    def decor(self): 
        decor1 = my_sprite("./images_orig/decor/tree.png", (90,30))
        decor2=  my_sprite("./images_orig/decor/Finish.png", (190,60))
        decor3=  my_sprite("./images_orig/decor/Start.png", (200,80))
        decor4=  my_sprite("./images_orig/decor/tree.png", (90,100))
        decor5= my_sprite("./images_orig/decor/tree.png", (90,200))
        decors= [decor1, decor2, decor3, decor4, decor5] 
        return decors
class MovementHandle: 
    def control_movement(self, vehicles): 
        keys = pygame.key.get_pressed()
        x1,y1 = vehicles[0].loc
        if keys[pygame.K_LEFT]: 
            x1 = x1-5 
        if keys[pygame.K_RIGHT]:
            x1 = x1+5 
        if keys[pygame.K_DOWN]: 
            y1 = y1 - 5
        if keys[pygame.K_UP]: 
            y1 = y1 + 5 
        vehicles[0].set_location((x1,y1))
        x2, y2 = vehicles[1].loc
        if keys[pygame.K_a]: x2 = x2- 5
        if keys[pygame.K_d]: x2 =x2+ 5
        if keys[pygame.K_w]: y2 = y2- 5
        if keys[pygame.K_s]: y2 = y2+ 5
        vehicles[1].set_location((x2, y2))
class CollisionCheck: 
        def check(self, vehicles, colliding_objects): 
            for vehicle in vehicles : 
                for object in colliding_objects: 
                    if vehicle.is_colliding_with(object): 
                        print("Vehicle crashed!!") 
class drawing_handle: 
        def draw(self, screen, decors, colliding_objects, vehicles): 
            screen.fill((0,0,0))
            for decor in decors : 
                screen.blit(decor.get_image(), decor.loc)
            for object in colliding_objects: 
                screen.blit(object.get_image(), object.loc)
            for vehicle in vehicles : 
                screen.blit(vehicle.get_image(), vehicle.loc)
            pygame.display.flip() 

class main_game: 
        def __init__(self,screen,vehicles,colliding_objects, decors): 
            self.screen = screen 
            self.vehicles= vehicles
            self.colliding_objects = colliding_objects
            self.decors = decors 
            self.running = True
            self.movement = MovementHandle()
            self.collision = CollisionCheck() 
            self.drawing = drawing_handle()
        def run(self):
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        
                self.movement.control_movement(self.vehicles)
                self.collision.check(self.vehicles, self.colliding_objects)
                self.drawing.draw(self.screen, self.decors, self.colliding_objects, self.vehicles)

def main () :    
    screen = InitializeTheGame().initialize_game()
    vehicles = Vehicle().vehicles()
    objects = Colliding().colliding()
    decorations = Decor().decor()
    
    play = main_game(screen,vehicles, objects, decorations)
    play.run()
   

    pygame.quit()
if __name__=="__main__": 
    main()
        
    

        

        




            




 

