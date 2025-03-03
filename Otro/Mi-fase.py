from ursina import *


app = Ursina()

bg = Entity(model="quad", scale=(40,30), position=(10,10), texture="assets/sky", z=1)

duplicate(bg, x=43)
duplicate(bg, x=-13)

ground = Entity(model="quad", scale=(24,1,1), position=(0,-2), collider="cube", texture="grass")

game_over = Text(text="Game Over", scale=3, position=(-0.2,0.2), color= color.red, visible=False) 
game_over2 = Text(text="Pulsa tabulador para continuar", scale=1, position=(-0.2,0.1), color= color.black, visible=False) 


scocer_text =Text(text="Score:", scale=1.4, position=(-0.80, 0.4), color = color.yellow )
Time_text =Text(text="Score:", scale=1.4, position=(0.66, 0.48), color = color.yellow )

score = 0

Time = 0 

num_life = 3

gravity = 2.5

# Vida 

Life = Entity(model="quad", texture="assets/3lifes.png", scale=(3,0.7,1), position=(-13,17,0.4),visible=True)

#Crear personaje

player = Entity(model="quad", texture="assets/Mario1.png", scale=(1.4,1.4,1), position=(0,0.3),visible=True, collider ="box")

    # Sonido player 

audio_player = Audio('assets/CasualGameSounds/DM-CGS-07.wav', autoplay=False)

# Crear Enemigos

enemy = Entity(model="quad", color = color.clear, scale =(1,1), position = (10,7), collider = "cube",)


    # Modelo enemy

Animetion_Enemy = SpriteSheetAnimation ("assets/baddie", x=0, y=0, scale=(1,1), tileset_size=(4,1), fps=10, parent=enemy,
            animations={
                'idle':((0,0),(3,0))
            } )
Animetion_Enemy.play_animation('idle')

 # Sonido enemy
audio_enemy = Audio('assets/CasualGameSounds/DM-CGS-09.wav', autoplay=False)

#Crear plataformas 

bloque = Entity(model='cube', scale=(1,1,1), position=(5, 6), collider='cube', texture="assets/bloque.png")

lucky = Entity(model='cube', scale=(1,1,1), position=(6, 2), collider='cube', texture="assets/lucky.jpeg")
lucky2 = Entity(model='cube', scale=(1,1,1), position=(-6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky3 = Entity(model='cube', scale=(1,1,1), position=(3, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky4 = Entity(model='cube', scale=(1,1,1), position=(6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky5 = Entity(model='cube', scale=(1,1,1), position=(-6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky6 = Entity(model='cube', scale=(1,1,1), position=(3, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky7 = Entity(model='cube', scale=(1,1,1), position=(3, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky8 = Entity(model='cube', scale=(1,1,1), position=(6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky9 = Entity(model='cube', scale=(1,1,1), position=(-6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky10 = Entity(model='cube', scale=(1,1,1), position=(3, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky11 = Entity(model='cube', scale=(1,1,1), position=(6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky12 = Entity(model='cube', scale=(1,1,1), position=(-6, 2), collider='cube', texture="assets/lucky.jpeg")

tuberia = Entity(model='cube', scale=(2,2,1), position=(0, -0.5), collider='cube', texture="assets/tuberia.png")

duplicate(bloque, x=6, y=6)
duplicate(bloque, x=7, y=6), duplicate(bloque, x=8, y=6), duplicate(bloque, x=9, y=6), duplicate(bloque, x=10, y=6)

duplicate(bloque, x=-5, y=6)
duplicate(bloque, x=-6, y=6), duplicate(bloque, x=-7, y=6), duplicate(bloque, x=-8, y=6), duplicate(bloque, x=-9, y=6), duplicate(bloque, x=-10, y=6)

duplicate(bloque, x=-5, y=2), duplicate(bloque, x=-7, y=2),duplicate(bloque, x=5, y=2) , duplicate(bloque, x=7, y=2)

duplicate(tuberia, x = 30)

# Camara

camera.orthographic = True
camera.position = (20/2,8)
camera.fov = 20


is_game_over = False
enemy_speed = 2

def update():
    global is_game_over
    global enemy_speed
    global score
    global Time
    global num_life
    global gravity

# Gravedad

    player.y -= gravity * time.dt

    Life.position =(player.x-15,17,0.4)

    if player.intersects(ground).hit or player.intersects(bloque).hit:

        gravity = 0

    else:

        gravity =2.5

    if time.dt * 1:
        
        Time +=1

        Time_text.text = f'Time:{Time}'

    camera.position = (player.x, 8)

    enemy.x += enemy_speed * time.dt

    if enemy.x >= 10 or enemy.x <= 5:

        enemy_speed *= -1
    
# Game over por caida 

    if player.y < -5:

        player.position = (2,2)

        player.visible = False

        game_over.visible = True

        game_over2.visible = True

        is_game_over = True

        score = 0

        scocer_text.text = f'Score:{score}'

# Game over por enemigo 

    if player.intersects(enemy).hit:

        player.position = (2,2)

        score -=1 

        num_life -=1

        scocer_text.text = f'Score:{score}'

        audio_enemy.play()


    if num_life == 3:
        
        Life.texture = 'assets/3lifes.png'

        score = 0
    
    if num_life == 2:
        
        Life.texture = 'assets/2lifes.png'
    
    if num_life == 1:
        
        Life.texture = 'assets/1lifes.png'
    
    if num_life == 0:
        
        player.position = (2,2)

        player.visible = False

        game_over.visible = True

        game_over2.visible = True

        is_game_over = True

        score -=1 

        scocer_text.text = f'Score:{score}'

        audio_enemy.play()

        scocer_text.visible = False

        Time_text.visible = False

def input(key):

    global is_game_over
    global Time
    global num_life

    if key == "tab" and is_game_over:

        player.visible = True

        game_over.visible = False

        game_over2.visible = False

        is_game_over = False

        scocer_text.visible = True

        Time = 0

        Time_text.text = f'Time:{Time}'

        Time_text.visible = True

        num_life = 3

        score = 0

        scocer_text.text = f'Score:{score}'

    if held_keys['a']:
        player.x -= 0.5
        # player.texture

    if held_keys['d']:
        player.x += 0.5

    if held_keys['w']:
        player.y += 2

    if held_keys['s']:
        player.y -= 1

app.run()



