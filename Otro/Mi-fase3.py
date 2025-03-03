from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

bg = Entity(model="quad", scale=(40,30), position=(10,10), texture="assets/sky", z=1)

duplicate(bg, x=43)
duplicate(bg, x=50)
duplicate(bg, x=80)
duplicate(bg, x=-30)

ground = Entity(model="quad", scale=(40,1,1), position=(0,-2.1), collider="cube", texture="grass")
ground2 = Entity(model="quad", scale=(100,1,1), position=(75,-2.1), collider="cube", texture="grass")

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
hitlucky3 = 1
hitlucky4 = 1
hitlucky5 = 1
hitlucky6 = 1
hitlucky7 = 1
hitlucky8 = 1
hitlucky9 = 1
hitlucky10 = 1
hitlucky11 = 1
hitlucky12 = 1

hitchampiñon = 1
hitchampiñon2 = 1

hitbloque_moneda = 5

# Vida 

Life = Entity(model="quad", texture="assets/3lifes.png", scale=(3,0.7,1), position=(-13,17,0.4),visible=True)

# personaje

# limite = Entity(model="quad", scale=(1,10,1), position=(-10,1,0),color= color.red, visible=False)

player = Entity(model="quad", texture="assets/Mario1.png", scale=(1.4,1.4,1), position=(0,0.3),visible=True, collider ="box")

# Crear Enemigos

enemy = Entity(model="quad", color = color.clear, scale =(1,1), position = (1,-1.1), collider = "cube",)
enemy2 = Entity(model="quad", color = color.clear, scale =(1,1), position = (-10,7.1), collider = "cube", visible =False)

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
lucky2 = Entity(model='cube', scale=(1,1,1), position=(-6,2), collider='cube', texture="assets/lucky.jpeg")

bloque = Entity(model='cube', scale=(1,1,1), position=(-1,2), collider='cube', texture="assets/bloque.png")
lucky = Entity(model='cube', scale=(1,1,1), position=(0,2), collider='cube', texture="assets/lucky.jpeg")
duplicate(bloque,x=1)
lucky3 = Entity(model='cube', scale=(1,1,1), position=(2,2), collider='cube', texture="assets/lucky.jpeg")
duplicate(bloque,x=3)

lucky4 = Entity(model='cube', scale=(1,1,1), position=(1,6), collider='cube', texture="assets/lucky.jpeg")

tuberia = Entity(model='cube', scale=(2,2,1), position=(8.5,-0.6), collider='cube', texture="assets/tuberia.png")

duplicate(bloque,x=13)
lucky5 = Entity(model='cube', scale=(1,1,1), position=(14,2), collider='cube', texture="assets/lucky.jpeg")
duplicate(bloque,x=15)

duplicate(bloque,x=16,y=6)
duplicate(bloque,x=17,y=6)
duplicate(bloque,x=18,y=6)
duplicate(bloque,x=19,y=6)
duplicate(bloque,x=20,y=6)
duplicate(bloque,x=21,y=6)
duplicate(bloque,x=22,y=6)

duplicate(bloque,x=28,y=6)
duplicate(bloque,x=29,y=6)
duplicate(bloque,x=30,y=6)
duplicate(bloque,x=31,y=6)
lucky6 = Entity(model='cube', scale=(1,1,1), position=(32, 6), collider='cube', texture="assets/lucky.jpeg")

bloque_monda = Entity(model='cube', scale=(1,1,1), position=(32,2), collider='cube', texture="assets/bloque.png")

duplicate(bloque,x=38)
bloque_estrella = Entity(model='cube', scale=(1,1,1), position=(39,2), collider='cube', texture="assets/bloque.png")

lucky7 = Entity(model='cube', scale=(1,1,1), position=(43,2), collider='cube', texture="assets/lucky.jpeg")
lucky8 = Entity(model='cube', scale=(1,1,1), position=(46,2), collider='cube', texture="assets/lucky.jpeg")
lucky9 = Entity(model='cube', scale=(1,1,1), position=(49,2), collider='cube', texture="assets/lucky.jpeg")

lucky10 = Entity(model='cube', scale=(1,1,1), position=(46,6), collider='cube', texture="assets/lucky.jpeg")

duplicate(bloque,x=55)

duplicate(bloque,x=58,y=6)
duplicate(bloque,x=59,y=6)
duplicate(bloque,x=60,y=6)
duplicate(bloque,x=61 ,y=6)

# lucky11 = Entity(model='cube', scale=(1,1,1), position=(6, 2), collider='cube', texture="assets/lucky.jpeg")
# lucky12 = Entity(model='cube', scale=(1,1,1), position=(-6, 2), collider='cube', texture="assets/lucky.jpeg")

# duplicate(tuberia, x = 30)

#  Objetos 

champiñon = Entity(model='quad', scale=(1,1,2),position=(0,2), collider='quad', texture="assets/champiñon.png",visible=True)
champiñon2 = Entity(model='quad', scale=(1,1,2),position=(14,2), collider='quad', texture="assets/champiñon.png",visible=True)

# Camara

camera.orthographic = True
camera.position = (10/2,8)
camera.fov = 20


is_game_over = False
enemy_speed = 2.5
enemy2_speed = 2.5

champiñon_speed = 0
champiñon2_speed = 0

champiñon_gravity = 0
champiñon2_gravity = 0

def update():

    global is_game_over
    global enemy_speed
    global enemy2_speed

    global champiñon_speed
    global champiñon
    global hitchampiñon

    global champiñon2_speed
    global champiñon2
    global hitchampiñon2

    global score
    global Time

    global num_life
    global hitlucky
    global hitlucky2
    global hitlucky3
    global hitlucky4
    global hitlucky5
    global hitlucky6
    global hitlucky7
    global hitlucky8
    global hitlucky9
    global hitlucky10
    global hitlucky11
    global hitlucky12
    global champiñon_gravity
    global champiñon2_gravity
    global hitbloque_moneda

    # Gravedad de Champiñon

    champiñon.y -= champiñon_gravity * time.dt

    if champiñon.y >= -0.9 and hitlucky == 0 and champiñon.x >= 3.7:

        champiñon_gravity += 0.9
    
    else:

        champiñon_gravity = 0

    # Gravedad de Champiñon2

    champiñon2.y -= champiñon2_gravity * time.dt

    if champiñon2.y >= -0.9 and hitlucky5 == 0 and champiñon2.x >= 15.7:

        champiñon2_gravity += 0.9
    
    else:

        champiñon2_gravity = 0

    # live
    
    Life.position =(player.x-15,17,0.4)
    Life_text.text = f'x{num_life}'
    scocer_text.text = f'Score:{score}'

    # Tiempo

    if Time >= 0:
        Time += time.dt
        Time_text.text = f'Time: {int(Time)}'

    # Camara

    camera.position = (player.x, 8)

    # Movimientos

    enemy.x += enemy_speed * time.dt
    enemy2.x += enemy2_speed * time.dt
    champiñon.x += champiñon_speed * time.dt

    champiñon2.x += champiñon2_speed * time.dt

    if enemy.x <= -19 or enemy.x >= 7.3:

        enemy_speed *= -1
    
    if enemy2.x >= -5 or enemy2.x <= -10:

        enemy2_speed *= -1

    if champiñon.x <= -19 or champiñon.x >= 7.3:

        champiñon_speed *= -1
    
    if champiñon2.x <= 9.8 or champiñon2.x >= 19:

        champiñon2_speed *= -1

    # Game over por caida
    
    if player.y < -5:

        player.position = (-9,1)
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

    # Limite

    if player.x <= -12:

        player.position = (-11.9,-1.5)

        # if camera.position  == (-10/2,8):

        #     camera.position = (-10/2,8)

    # Game over por enemigo 

    if player.intersects(enemy).hit:

        player.position = (-9,1)

        score -=1 

        num_life -=1

        audio_enemy.play()

        scocer_text.text = f'Score:{score}'

    if player.intersects(enemy2).hit:

        player.position = (-9,1)

        score -=1 

        num_life -=1

        audio_enemy.play()

        scocer_text.text = f'Score:{score}'
 
    #  Contador de Vida  

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

    if player.intersects(lucky).hit and hitlucky == 1 :

        lucky.texture = "assets/lucky_off.png"

        champiñon.position=(0,3)
        champiñon_speed = 1.5
        champiñon.visible = True
        
        hitlucky -=1

    if player.intersects(champiñon).hit and num_life < 3 and hitchampiñon == 1 :

            num_life +=1
        
            champiñon.position=(0,2)
            champiñon_speed = 0
            champiñon.visible =False
            hitchampiñon -=1
    
    elif num_life == 3 and player.intersects(champiñon).hit and hitchampiñon == 1:

            score +=1

            champiñon.position=(0,2)
            champiñon_speed = 0
            champiñon.visible =False
            hitchampiñon -=1
        
    if player.intersects(lucky2).hit and hitlucky2 == 1:

        score +=1

        lucky2.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky2 -=1

    if player.intersects(lucky3).hit and hitlucky3 == 1:

        score +=1

        lucky3.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky3 -=1

    if player.intersects(lucky4).hit and hitlucky4 == 1:

        score +=1

        lucky4.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky4 -=1
    
    if player.intersects(lucky5).hit and hitlucky5 == 1:

        lucky5.texture = "assets/lucky_off.png"

        champiñon2.position=(14,3)
        champiñon2_speed = 1.5
        champiñon2.visible = True
        
        hitlucky5 -=1

    if player.intersects(champiñon2).hit and num_life < 3 and hitchampiñon2 == 1 :

            num_life +=1
        
            champiñon2.position=(14,2)
            champiñon2_speed = 0
            champiñon2.visible =False
            hitchampiñon2 -=1
    
    elif num_life == 3 and player.intersects(champiñon2).hit and hitchampiñon2 == 1:

            score +=1

            champiñon2.position=(14,2)
            champiñon2_speed = 0
            champiñon2.visible =False
            hitchampiñon2 -=1

    if player.intersects(lucky6).hit and hitlucky6 == 1:

        score +=1

        lucky6.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky6 -=1
    
    # Bloque

    if player.intersects(bloque_monda).hit and hitbloque_moneda > 0:

        score +=1

        audio_coin.play()

        hitbloque_moneda -=1
    
    if hitbloque_moneda == 0:
            
        bloque_monda.texture = "assets/lucky_off.png"


def input(key):

    global is_game_over
    global Time
    global num_life
    global hitlucky
    global hitlucky2
    global hitlucky3
    global hitlucky4
    global hitlucky5
    global hitlucky6
    global hitlucky7
    global hitlucky8
    global hitlucky9
    global hitlucky10
    global hitlucky11
    global hitlucky12
    global champiñon_speed
    global hitchampiñon 
    global champiñon2_speed
    global hitchampiñon2 
    global hitbloque_moneda

    #  Renicio 

    if key == "tab" and is_game_over:

        player.visible = True

        champiñon.position=(0,2)
        champiñon_speed = 0
        champiñon.visible =False
        hitchampiñon = 1

        champiñon2.position=(14,2)
        champiñon2_speed = 0
        champiñon2.visible =False
        hitchampiñon2 = 1

        enemy.position = (1,-1.1)
        enemy2.position = (-10,7.1)  

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
        lucky3.texture = "assets/lucky.jpeg"
        lucky4.texture = "assets/lucky.jpeg"
        lucky5.texture = "assets/lucky.jpeg"
        lucky6.texture = "assets/lucky.jpeg"

        bloque_monda.texture = "assets/bloque.png"

        hitlucky = 1
        hitlucky2 = 1
        hitlucky3 = 1
        hitlucky4 = 1
        hitlucky5 = 1
        hitlucky6 = 1

        hitbloque_moneda = 5

        audio_music.play()
        audio_gameover.stop()

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