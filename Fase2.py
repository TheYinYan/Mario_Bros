from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

bg = Entity(model="quad", scale=(40,30), position=(10,10), texture="assets/sky", z=1)

duplicate(bg, x=43)
duplicate(bg, x=-30)

ground = Entity(model="quad", scale=(24,1,1), position=(0,-2), collider="cube", texture="grass")
ground = Entity(model="quad", scale=(24,1,1), position=(-30,-2), collider="cube", texture="grass")
ground = Entity(model="quad", scale=(24,1,1), position=(30,-2), collider="cube", texture="grass")

game_over = Text(text="Game Over", scale=3, position=(-0.22,0.2), color= color.red, visible=False) 
game_over2 = Text(text="Pulsa tabulador para continuar", scale=1, position=(-0.2,0.1), color= color.black, visible=False) 

scocer_text =Text(text="Score:", scale=1.4, position=(-0.81, 0.4), color = color.yellow )
Time_text =Text(text="Time:", scale=1.4, position=(0.66, 0.46), color = color.yellow )
Life_text =Text(text="x", scale=1.4, position=(-0.67, 0.46), color = color.yellow )

score = 0
Time = 0 
num_life = 3
hitlucky = 1
hitlucky2 = 1

# Vida 

Life = Entity(model="quad", texture="assets/3lifes.png", scale=(3,0.7,1), position=(-13,17,0.4),visible=True)

# personaje

player = PlatformerController2d( x=0, y=1, z=0, scale_y=1, scale_z=1, max_jumps=3, color = color.clear)

animation_player = SpriteSheetAnimation('assets/dude', 
    x=0, 
    y=0.5, 
    scale=(1,1), 
    tileset_size=(9,1), 
    fps=8, 
    parent=player, 
        animations={
            'idle': ((4,0), (4,0)), 
            'walk_right': ((5,0),(8,0)),
            'walk_left': ((0,0),(3,0))
        })

# Crear Enemigos

enemy = Entity(model="quad", color = color.clear, scale =(1,1), position = (10,7), collider = "cube",)
enemy2 = Entity(model="quad", color = color.clear, scale =(1,1), position = (-10,7), collider = "cube",)

Animetion_Enemy = SpriteSheetAnimation ("assets/baddie", x=0, y=0, scale=(1,1), tileset_size=(4,1), fps=10, parent=enemy,
            animations={
                'idle':((0,0),(3,0))
            } )
Animetion_Enemy.play_animation('idle')

Animetion_Enemy = SpriteSheetAnimation ("assets/baddie", x=0, y=0, scale=(1,1), tileset_size=(4,1), fps=10, parent=enemy2,
            animations={
                'idle':((0,0),(3,0))
            } )
Animetion_Enemy.play_animation('idle')

# audios 

audio_gameover = Audio('assets/CasualGameSounds/mario-bros game over.mp3', autoplay=False)
audio_player = Audio('assets/CasualGameSounds/salto-mario.mp3', autoplay=False)
audio_enemy = Audio('assets/CasualGameSounds/mario-bros-die.mp3', autoplay=False)
audio_music = Audio('assets/CasualGameSounds/SuperMarioBros.mp3', autoplay=True)
audio_coin = Audio('assets/CasualGameSounds/mario-bros-coin.mp3', autoplay=False)

#Crear plataformas 

bloque = Entity(model='cube', scale=(1,1,1), position=(5, 6), collider='cube', texture="assets/bloque.png")

lucky = Entity(model='cube', scale=(1,1,1), position=(6, 2), collider='cube', texture="assets/lucky.jpeg")
lucky2 = Entity(model='cube', scale=(1,1,1), position=(-6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky3 = Entity(model='cube', scale=(1,1,1), position=(3, 2), collider='cube', texture="assets/lucky.jpeg")

tuberia = Entity(model='cube', scale=(2,2,1), position=(0, -0.5), collider='cube', texture="assets/tuberia.png")

duplicate(bloque, x=6, y=6)
duplicate(bloque, x=7, y=6), duplicate(bloque, x=8, y=6), duplicate(bloque, x=9, y=6), duplicate(bloque, x=10, y=6)

duplicate(bloque, x=-5, y=6)
duplicate(bloque, x=-6, y=6), duplicate(bloque, x=-7, y=6), duplicate(bloque, x=-8, y=6), duplicate(bloque, x=-9, y=6), duplicate(bloque, x=-10, y=6)

duplicate(bloque, x=-5, y=2), duplicate(bloque, x=-7, y=2),duplicate(bloque, x=5, y=2) , duplicate(bloque, x=7, y=2)



duplicate(tuberia, x = 30)


# platform5 = Entity(model='cube', scale=(3, 0.5,1), position=(0, 4), collider='cube', texture="brick")
# platform5.animate('rotation_z', value=360, duration=10, loop=True, delay=0)

# platform2 = Entity(model='cube', scale=(3, 0.5,1), position=(15, 10), collider='cube', texture="brick")
# platform2.animate('rotation_z', value=360, duration=2, loop=True, delay=0)

# platform4 = Entity(model='cube', scale=(1,1,1), position=(7, 2), collider='cube', texture="assets/bloque.png")

# Camara

camera.orthographic = True
camera.position = (20/2,8)
camera.fov = 20


is_game_over = False
enemy_speed = 2.5
enemy2_speed = 2.5

def update():

    global is_game_over
    global enemy_speed
    global enemy2_speed
    global score
    global Time
    global num_life
    global hitlucky
    global hitlucky2

    Life.position =(player.x-15,17,0.4)
    Life_text.text = f'x{num_life}'
    scocer_text.text = f'Score:{score}'

    if Time >= 0:
        Time += time.dt
        Time_text.text = f'Time: {int(Time)}'
    
    # if time.dt * 1:
        
    #     Time +=1

    #     Time_text.text = f'Time:{Time}'

    camera.position = (player.x, 8)

    enemy.x += enemy_speed * time.dt
    enemy2.x += enemy2_speed * time.dt


    if enemy.x >= 10 or enemy.x <= 5:

        enemy_speed *= -1
    
    if enemy2.x >= -5 or enemy2.x <= -10:

        enemy2_speed *= -1
       
# Game over por caida
    
    if player.y < -5:

        player.position = (0,1)
        player.visible = False

        game_over.visible = True
        game_over2.visible = True
        is_game_over = True

        score = 0
        scocer_text.visible = False

        audio_gameover.play()
        audio_music.stop()

        Time = 0
        Time_text.visible = False

# Game over por enemigo 

    if player.intersects(enemy).hit:

        player.position = (0,1)

        score -=1 

        num_life -=1

        audio_enemy.play()

        scocer_text.text = f'Score:{score}'

    if player.intersects(enemy2).hit:

        player.position = (0,1)

        score -=1 

        num_life -=1

        audio_enemy.play()

        scocer_text.text = f'Score:{score}'
 
 
#  Vida contador 

    if num_life == 3:
        
        Life.texture = 'assets/3lifes.png'

    
    if num_life == 2:
        
        Life.texture = 'assets/2lifes.png'

    
    if num_life == 1:
        
        Life.texture = 'assets/1lifes.png'
    
    if num_life == 0:
        
        Life.visible = False

        player.visible = False

        game_over.visible = True
        game_over2.visible = True
        is_game_over = True
    
        audio_gameover.play()
        audio_music.stop()

        score = 0
        scocer_text.visible = False

        Time_text.visible = False


# lucky bloque 

    if player.intersects(lucky).hit and hitlucky == 1:

        score +=1

        lucky.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky -=1
        
    
    if player.intersects(lucky2).hit and hitlucky2 == 1:

        score +=1

        lucky2.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky2 -=1

def input(key):

    global is_game_over
    global Time
    global num_life
    global hitlucky2
    global hitlucky

#  Renicio 

    if key == "tab" and is_game_over:

        player.visible = True

        game_over.visible = False
        game_over2.visible = False
        is_game_over = False

        Time = 0
        Time_text.text = f'Time:{Time}'
        Time_text.visible = True

        Life.visible = True
        num_life = 3

        score = 0
        scocer_text.text = f'Score:{score}'
        scocer_text.visible = True

        lucky.texture = "assets/lucky.jpeg"
        lucky2.texture = "assets/lucky.jpeg"

        audio_music.play()
        audio_gameover.stop()

        hitlucky = 1
        hitlucky2 = 1

# Animacion player

    if held_keys['a']:

        animation_player.play_animation('walk_left')
        animation_player.scale_x = -1

    elif held_keys['d']:
        animation_player.play_animation('walk_right')
        animation_player.scale_x = 1
    else:        
        animation_player.play_animation('idle')

    if held_keys['space']:

        audio_player.play()

app.run()



