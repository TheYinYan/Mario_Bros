from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

bg = Entity(model="quad", scale=(40,30), position=(10,10), texture="assets/sky", z=1)

duplicate(bg, x=43)
duplicate(bg, x=50)
duplicate(bg, x=80)
duplicate(bg, x=100)
duplicate(bg, x=110)
duplicate(bg, x=-30)

ground = Entity(model="quad", scale=(40,1,1), position=(0,-2.1), collider="cube", texture="grass")
ground2 = Entity(model="quad", scale=(100,1,1), position=(75,-2.1), collider="cube", texture="grass")

game_over = Text(text="Game Over", scale=3, position=(-0.22,0.2), color= color.red, visible=False, font = 'assets/GrapeSoda.ttf' ) 
game_over2 = Text(text="Pulsa tabulador para continuar", scale=1, position=(-0.2,0.1), color= color.white, visible=False, font = 'assets/GrapeSoda.ttf' ) 

scocer_text =Text(text="Score:", scale=2, position=(-0.81, 0.4), color = color.yellow, font = 'assets/GrapeSoda.ttf'  )
Time_text =Text(text="Time:", scale=2, position=(0.66, 0.46), color = color.yellow, font = 'assets/GrapeSoda.ttf'  )

scocer_text2 =Text(text="Your Score is ", scale=1, position=(-0.2, 0.05), color = color.white, font = 'assets/GrapeSoda.ttf',visible=False)
Time_text2 =Text(text="En un tiempo de ", scale=1, position=(-0.2, 0.01), color = color.white, font = 'assets/GrapeSoda.ttf',visible=False,)

Win_text = Text(text="You Win", scale=3, position=(-0.17,0.2), color = color.green, visible=False, font = 'assets/GrapeSoda.ttf' )
Win_text2 = Text(text="Pulsa tabulador para continuar", scale=1, position=(-0.2,0.1), color= color.white, visible=False, font = 'assets/GrapeSoda.ttf' ) 

score = 0
Time = 0 
hitBandera = 1 

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
hitchampiñon3 = 1

hitflorfuego = 1

hitbloque_moneda = 5

# Vida 

Life = Entity(model="quad", texture="assets/3lifes.png", scale=(3,1,1), position=(-13,17,0.4),visible=True)

# Flor de fuego

UpFlor = Entity(model="quad", texture="assets/flor_de_fuego.png", scale=(1,1.1,1), position=(-22,17,0.4),visible=False)

bola_fuego = Entity(model="quad", color = color.clear, scale=(0.5,0.5,0.5), position=(50,100,0),visible=True, collider="sphere")

Animetion_bola_fuego = SpriteSheetAnimation ("assets/bola_fuego2", x=0, y=0, scale=(1,1), tileset_size=(4,1), fps=10, parent=bola_fuego,
            animations={
                'idle':((0,0),(3,0))
            } )
Animetion_bola_fuego.play_animation('idle')

# personaje

player = PlatformerController2d( x=-9.5, y=1, z=0, scale_y=1.95,scale_x=1, scale_z=1, max_jumps=2, color = color.clear, 
                                
                                jump_height = 5.7, gravity = 0.6, jump_duration = 0.7, air_time = 1, collider = 'box' )

animation_player = SpriteSheetAnimation('assets/Mario2', 
    x=0, 
    y=0.5, 
    scale=(1,1), 
    tileset_size=(9,1), 
    fps=8, 
    parent=player, 
        animations={
            'idle': ((4,0), (4,0)), 
            'walk_right': ((5,0),(7,0)),#((5,0),(8,0))
            'walk_left': ((0,0),(3,0)),
            'salto': ((8,0),(8,0))
        })

# Crear Enemigos

enemy = Entity(model="quad", color = color.clear, scale =(1,1), position = (1,-1.1,0), collider = "cube",)
enemy2 = Entity(model="quad", color = color.clear, scale =(1,1), position = (16,7,0), collider = "cube")

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

tuberia = Entity(model='cube', scale=(2,2,0), position=(8.5,-0.6), collider='cube', texture="assets/tuberia.png")

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

duplicate(bloque,x=65,y=6)
lucky11 = Entity(model='cube', scale=(1,1,1), position=(66, 6), collider='cube', texture="assets/lucky.jpeg")
lucky12 = Entity(model='cube', scale=(1,1,1), position=(67, 6), collider='cube', texture="assets/lucky.jpeg")
duplicate(bloque,x=68,y=6)

duplicate(bloque,x=66)
duplicate(bloque,x=67)

# Escalera 1

duplicate(bloque,x=72,y=-1.1),duplicate(bloque,x=73,y=-1.1),duplicate(bloque,x=74,y=-1.1),duplicate(bloque,x=75,y=-1.1)
duplicate(bloque,x=73,y=-0.1),duplicate(bloque,x=74,y=-0.1),duplicate(bloque,x=75,y=-0.1)
duplicate(bloque,x=74,y=0.9),duplicate(bloque,x=75,y=0.9)
duplicate(bloque,x=75,y=1.9)

# Escaleara 2

duplicate(bloque,x=78,y=-1.1),duplicate(bloque,x=79,y=-1.1),duplicate(bloque,x=80,y=-1.1),duplicate(bloque,x=81,y=-1.1)
duplicate(bloque,x=78,y=-0.1),duplicate(bloque,x=79,y=-0.1),duplicate(bloque,x=80,y=-0.1)
duplicate(bloque,x=78,y=0.9),duplicate(bloque,x=79,y=0.9)
duplicate(bloque,x=78,y=1.9)

# Escalera 3 

duplicate(bloque,x=85,y=-1.1),duplicate(bloque,x=86,y=-1.1),duplicate(bloque,x=87,y=-1.1),duplicate(bloque,x=88,y=-1.1),duplicate(bloque,x=89,y=-1.1),duplicate(bloque,x=90,y=-1.1),duplicate(bloque,x=91,y=-1.1),duplicate(bloque,x=92,y=-1.1),duplicate(bloque,x=93,y=-1.1)
duplicate(bloque,x=86,y=-0.1),duplicate(bloque,x=87,y=-0.1),duplicate(bloque,x=88,y=-0.1),duplicate(bloque,x=89,y=-0.1),duplicate(bloque,x=90,y=-0.1),duplicate(bloque,x=91,y=-0.1),duplicate(bloque,x=92,y=-0.1),duplicate(bloque,x=93,y=-0.1)
duplicate(bloque,x=87,y=0.9),duplicate(bloque,x=88,y=0.9),duplicate(bloque,x=89,y=0.9),duplicate(bloque,x=90,y=0.9),duplicate(bloque,x=91,y=0.9),duplicate(bloque,x=92,y=0.9),duplicate(bloque,x=93,y=0.9)
duplicate(bloque,x=88,y=1.9),duplicate(bloque,x=89,y=1.9),duplicate(bloque,x=90,y=1.9),duplicate(bloque,x=91,y=1.9),duplicate(bloque,x=92,y=1.9),duplicate(bloque,x=93,y=1.9)
duplicate(bloque,x=89,y=2.9),duplicate(bloque,x=90,y=2.9),duplicate(bloque,x=91,y=2.9),duplicate(bloque,x=92,y=2.9),duplicate(bloque,x=93,y=2.9)
duplicate(bloque,x=90,y=3.9),duplicate(bloque,x=91,y=3.9),duplicate(bloque,x=92,y=3.9),duplicate(bloque,x=93,y=3.9)
duplicate(bloque,x=91,y=4.9),duplicate(bloque,x=92,y=4.9),duplicate(bloque,x=93,y=4.9)
duplicate(bloque,x=92,y=5.9),duplicate(bloque,x=93,y=5.9)

# Bandera

Bandera = Entity(model='cube', scale=(0.1,10), position=(100,3.4), collider='cube', texture="assets/bandera3.png")
Bandera2 = Entity(model='cube', scale=(0.5,0.5), position=(100,8.65), collider='cube', texture="assets/bandera2.png")
Bandera1 = Entity(model='cube', scale=(1,1), position=(99.45,7.75), collider='cube', texture="assets/bandera1.png")

# Castillo

Castillo  = Entity(model='cube', scale=(6,6,1), position=(110,1.41), collider='cube', texture="assets/castillo1.png")

#  Objetos 

champiñon = Entity(model='quad', scale=(1,1,1),position=(6,2), collider='quad', texture="assets/champiñon.png", visible= False)
champiñon2 = Entity(model='quad', scale=(1,1,1),position=(14,2), collider='quad', texture="assets/champiñon.png",visible= False)
champiñon3 = Entity(model='quad', scale=(1,1,1),position=(46,6), collider='quad', texture="assets/champiñon.png", visible=False)

FlorFuego = Entity(model='quad', scale=(1,1,1), position=(-6,2), collider='quad', texture="assets/flor_de_fuego.png", visible= False )

# Camara

camera.orthographic = True
camera.position = (10/2,8)
camera.fov = 20

is_you_win = False

is_up_flor = False
bola_fuego_speed = 0


is_game_over = False
enemy_speed = 2.5
enemy2_speed = 2.5

champiñon_speed = 0
champiñon2_speed = 0
champiñon3_speed = 0

champiñon_gravity = 0
champiñon2_gravity = 0
champiñon3_gravity = 0

def update():

    global is_game_over
    global enemy_speed
    global enemy2_speed

    global is_you_win

    global is_up_flor
    global bola_fuego_speed
    global hitflorfuego

    global champiñon_speed
    global champiñon
    global hitchampiñon
    global champiñon_gravity

    global champiñon2_speed
    global champiñon2
    global hitchampiñon2
    global champiñon2_gravity

    global champiñon3_speed
    global champiñon3
    global hitchampiñon3
    global champiñon3_gravity

    global score
    global Time
    global hitBandera
    global time2

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

    # Gravedad de Champiñon3

    champiñon3.y -= champiñon3_gravity * time.dt

    if champiñon3.y >= -0.9 and hitlucky10 == 0 and champiñon3.x >= 46.5:

        champiñon3_gravity += 0.9
    
    else:

        champiñon3_gravity = 0

    # live
    
    Life.position =(player.x-15,17,0.4)
    scocer_text.text = f'Score: {score}'

    # Indicador de Flor de fuego 

    UpFlor.position =(player.x-12,17,0.4)

    # Tiempo

    if Time >= 0:
        Time += time.dt
        Time_text.text = f'Time: {int(Time)}'

    # Camara

    camera.position = (player.x, 8)

    # Movimientos

    bola_fuego.x += bola_fuego_speed * time.dt 

    enemy.x += enemy_speed * time.dt
    enemy2.x += enemy2_speed * time.dt

    champiñon.x += champiñon_speed * time.dt
    champiñon2.x += champiñon2_speed * time.dt
    champiñon3.x += champiñon3_speed * time.dt

    if enemy.x <= -19 or enemy.x >= 7.1:

        enemy_speed *= -1
    
    if enemy2.x >=22  or enemy2.x <=16 :

        enemy2_speed *= -1

    if champiñon.x <= -19 or champiñon.x >= 7.1:

        champiñon_speed *= -1
    
    if champiñon2.x <= 9.8 or champiñon2.x >= 19:

        champiñon2_speed *= -1

    if champiñon3.x <= 20 or champiñon3.x >= 80:

        champiñon3_speed *= -1

    # Game over por caida
    
    if player.y < -5:

        player.position = (-9,1)
        player.visible = False

        game_over.visible = True
        game_over2.visible = True
        is_game_over = True

        is_up_flor = False
        UpFlor.visible =False

        scocer_text.visible = False

        Life.visible = False
        Time_text.visible = False

        Time_text.visible = False

        audio_gameover.play()
        audio_music.stop()

    # Limite

    if player.x <= -12:

        player.position = (-11.9,-1.5)

    # Game over enemy

    if player.intersects(enemy).hit:

        player.position = (-9,1)

        score -=1 

        num_life -=1

        audio_enemy.play()

        scocer_text.text = f'Score:{score}'

        is_up_flor = False

        UpFlor.visible =False

    if player.intersects(enemy2).hit:

        player.position = (-9,1)

        score -=1 

        num_life -=1

        audio_enemy.play()

        scocer_text.text = f'Score:{score}'

        is_up_flor = False

        UpFlor.visible =False

    #  Contador de Vida  

    if num_life == 3:
        
        Life.texture = 'assets/3lifes.png'

    if num_life == 2:
        
        Life.texture = 'assets/2lifes.png'
    
    if num_life == 1:
        
        Life.texture = 'assets/1lifes.png'
    
    if num_life == 0 and is_game_over == False:
        
        Life.visible = False
        Time_text.visible = False

        player.visible = False

        game_over.visible = True
        game_over2.visible = True
        is_game_over = True
    
        audio_gameover.play()
        audio_music.stop()

        scocer_text.visible = False


    # lucky bloque 

    if player.intersects(lucky).hit and hitlucky == 1:

        lucky.texture = "assets/lucky_off.png"

        champiñon.position=(0,3)
        champiñon_speed = 1.5
        champiñon.visible = True
        
        hitlucky -=1

    if player.intersects(champiñon).hit and num_life < 3 and hitchampiñon == 1:

            num_life +=1
        
            champiñon.position=(0,2)
            champiñon_speed = 0
            champiñon.visible =False
            hitchampiñon -=1
    
    elif num_life == 3 and player.intersects(champiñon).hit and hitchampiñon == 1:

            score +=1

            champiñon.position=(0,2)
            champiñon_speed = 0
            champiñon.visible = False
            hitchampiñon -=1

    # lucky bloque Flor de Fuego 

    if player.intersects(lucky2).hit and hitlucky2 == 1:

        lucky2.texture = "assets/lucky_off.png"

        FlorFuego.position=(-6,3)
        FlorFuego.visible = True

        hitlucky2 -=1

    if player.intersects(FlorFuego).hit and hitflorfuego == 1:
                
        FlorFuego.position=(-6,2)
        FlorFuego.visible =False

        UpFlor.visible = True
        is_up_flor = True

        hitflorfuego -=1

    # lucky bloque 3

    if player.intersects(lucky3).hit and hitlucky3 == 1:

        score +=1

        lucky3.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky3 -=1

    # lucky bloque 4 

    if player.intersects(lucky4).hit and hitlucky4 == 1:

        score +=1

        lucky4.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky4 -=1
    
    # lucky bloque 5

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

    # lucky bloque 6 

    if player.intersects(lucky6).hit and hitlucky6 == 1:

        score +=1

        lucky6.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky6 -=1

    # lucky bloque 7

    if player.intersects(lucky7).hit and hitlucky7 == 1:

        score +=1

        lucky7.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky7 -=1
    
    # lucky bloque 8

    if player.intersects(lucky8).hit and hitlucky8 == 1:

        score +=1

        lucky8.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky8 -=1
    
    # lucky bloque 9

    if player.intersects(lucky9).hit and hitlucky9 == 1:

        score +=1

        lucky9.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky9 -=1
    
    # lucky bloque 10

    if player.intersects(lucky10).hit and hitlucky10 == 1:

        lucky10.texture = "assets/lucky_off.png"

        champiñon3.position=(46,7)
        champiñon3_speed = 1.5
        champiñon3.visible = True
        
        hitlucky10 -=1

    if player.intersects(champiñon3).hit and num_life < 3 and hitchampiñon3 == 1 :

            num_life +=1
        
            champiñon3.position=(46,6)
            champiñon3_speed = 0
            champiñon3.visible =False
            hitchampiñon3 -=1
    
    elif num_life == 3 and player.intersects(champiñon3).hit and hitchampiñon3 == 1:

            score +=1

            champiñon3.position=(46,6)
            champiñon3_speed = 0
            champiñon3.visible =False
            hitchampiñon3 -=1

    # lucky bloque 11

    if player.intersects(lucky11).hit and hitlucky11 == 1:

        score +=1

        lucky11.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky11 -=1

    # lucky bloque 12

    if player.intersects(lucky12).hit and hitlucky12 == 1:

        score +=1

        lucky12.texture = "assets/lucky_off.png"

        audio_coin.play()

        hitlucky12 -=1

    # Bloque

    if player.intersects(bloque_monda).hit and hitbloque_moneda > 0:

        score +=1

        audio_coin.play()

        hitbloque_moneda -=1
    
    if hitbloque_moneda == 0:
            
        bloque_monda.texture = "assets/lucky_off.png"
    
    # Ganar

    if  player.intersects(Bandera2).hit and hitBandera == 1 or  player.intersects(Bandera).hit and hitBandera == 1 or  player.intersects(Bandera1).hit and hitBandera == 1:

        scocer_text.visible = False
        
        Life.visible = False
        Time_text.visible = False

        Time_text.visible = False
         
        is_you_win = True
        Win_text.visible = True
        Win_text2.visible = True

        time2= Time
        hitBandera -= 1
        Bandera1.position = (99.45,0)

        Time_text2.text = f'En un tiempo de {int(time2)} segundos'
        scocer_text2.text = f'Tu puntuacion es de {score} puntos'

        Time_text2.visible = True
        scocer_text2.visible = True

        player.visible = False

        UpFlor.visible = False

        audio_music.stop()

    # destruir enemy 

    if bola_fuego.intersects(enemy).hit:

        bola_fuego.position = (100,100,100)
        enemy.position = (100,100,50) 

        score +=1  

    if bola_fuego.intersects(enemy2).hit:

        bola_fuego.position = (100,100,100)
        enemy2.position = (100,100,50)  
       
        score +=1  

    if bola_fuego.intersects(tuberia).hit or bola_fuego.intersects(bloque).hit or bola_fuego.intersects(lucky).hit:

        bola_fuego.position = (100,100,100)

     
       
    
def input(key):

    global is_game_over
    global is_you_win
    global hitBandera
    global Time
    global score
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

    global champiñon3_speed
    global hitchampiñon3 

    global hitflorfuego
    global bola_fuego_speed
    global is_up_flor

    global hitbloque_moneda

    # Bola de fuego 

    if is_up_flor and  held_keys['d']and key == "f" or key == "f" and is_up_flor: 

        bola_fuego.position =(player.x + 1,player.y +0.5,0)
        bola_fuego_speed = 2.5

    if is_up_flor  and  held_keys['a'] and key == "f":

        bola_fuego.position =(player.x - 1.5,player.y +0.5,0)
        bola_fuego_speed = -2.5

    #  Renicio 

    if key == "tab" and is_game_over or key == "tab" and is_you_win: 

        player.visible = True
        player.position = (-9,1)

        champiñon.position=(0,2)
        champiñon_speed = 0
        champiñon.visible =False
        hitchampiñon = 1

        champiñon2.position=(14,2)
        champiñon2_speed = 0
        champiñon2.visible =False
        hitchampiñon2 = 1

        champiñon3.position=(46,6)
        champiñon3_speed = 0
        champiñon3.visible =False
        hitchampiñon3 = 1
        
        UpFlor.visible = False
        hitflorfuego = 1
        is_up_flor = False  
        bola_fuego_speed = 0
        bola_fuego.position = (100,100,100)

        enemy.position = (1,-1.1,0)
        enemy2.position = (16,7,0)  

        game_over.visible = False
        game_over2.visible = False
        is_game_over = False

        Win_text.visible = False
        Win_text2.visible = False
        is_you_win = False
        Bandera1.position = (99.45,7.75)
        hitBandera = 1

        Time *= 0
        Time_text.text = f'Time:{Time}'
        Time_text.visible = True
        Time_text2.visible = False

        Life.visible = True
        num_life = 3

        score *= 0
        scocer_text.text = f'Score:{score}'
        scocer_text.visible = True
        scocer_text2.visible = False

        lucky.texture = "assets/lucky.jpeg"
        lucky2.texture = "assets/lucky.jpeg"
        lucky3.texture = "assets/lucky.jpeg"
        lucky4.texture = "assets/lucky.jpeg"
        lucky5.texture = "assets/lucky.jpeg"
        lucky6.texture = "assets/lucky.jpeg"
        lucky7.texture = "assets/lucky.jpeg"
        lucky8.texture = "assets/lucky.jpeg"
        lucky9.texture = "assets/lucky.jpeg"
        lucky10.texture = "assets/lucky.jpeg"
        lucky11.texture = "assets/lucky.jpeg"
        lucky12.texture = "assets/lucky.jpeg"
        bloque_monda.texture = "assets/bloque.png"

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

        hitbloque_moneda = 5

        audio_music.play()
        audio_gameover.stop()

    # Animacion player

    if held_keys['a']:

        animation_player.play_animation('walk_left')
        animation_player.scale_x = -1

    elif held_keys['d']:
        animation_player.play_animation('walk_right')
        animation_player.scale_x = 1

    elif held_keys['space']:
        animation_player.play_animation('salto')
        audio_player.play()  

    else:        
        animation_player.play_animation('idle')

app.run()