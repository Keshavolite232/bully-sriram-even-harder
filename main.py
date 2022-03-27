@namespace
class SpriteKind:
    Object = SpriteKind.create()
    DashOrb = SpriteKind.create()
    DeathCam = SpriteKind.create()
    Enemy_Projectile = SpriteKind.create()
    Chest = SpriteKind.create()
    End_Portal = SpriteKind.create()
    Level_1_Boss = SpriteKind.create()
    Boss_Projectile = SpriteKind.create()

def on_on_overlap(sprite33, otherSprite23):
    global Playerwamoushindeiru
    Playerwamoushindeiru = True
    
    def on_after():
        game.over(False)
    timer.after(15, on_after)
    
sprites.on_overlap(SpriteKind.Enemy_Projectile,
    SpriteKind.player,
    on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy()
    if BossFightStage == 2:
        statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite).value += -5 - weapons_list.index(current_weapon)
    if BossFightStage == 3:
        statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite).value += -10 - weapons_list.index(current_weapon)
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.Level_1_Boss,
    on_on_overlap2)

def Harambe_Shot():
    global shot_1
    if Harambewamoushindeiru == False:
        for value32 in sprites.all_of_kind(SpriteKind.Level_1_Boss):
            if Player_1.tilemap_location().column >= value32.tilemap_location().column:
                shot_1 = sprites.create(assets.image("""
                        Boss Shot Image
                    """),
                    SpriteKind.Boss_Projectile)
                tiles.place_on_tile(shot_1,
                    tiles.get_tile_location(Harambe.tilemap_location().column,
                        Harambe.tilemap_location().row))
                shot_1.vx = 100
            else:
                shot_1 = sprites.create(assets.image("""
                        Boss Shot Image
                    """),
                    SpriteKind.Boss_Projectile)
                tiles.place_on_tile(shot_1,
                    tiles.get_tile_location(Harambe.tilemap_location().column,
                        Harambe.tilemap_location().row))
                shot_1.vx = -100
def setplayerdirection():
    animation.stop_animation(animation.AnimationTypes.ALL, Player_1)
    if lastdirection:
        Player_1.set_image(assets.image("""
            Player Facing Right
        """))
    else:
        Player_1.set_image(assets.image("""
            Player facing backward
        """))

def on_up_pressed():
    if Cutscene == False:
        if Player_1.vy == 0:
            Player_1.vy = -200
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite2, location):
    global Playerwamoushindeiru
    Playerwamoushindeiru = True
    
    def on_after2():
        game.over(False)
    timer.after(15, on_after2)
    
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Spike
    """),
    on_overlap_tile)

def updateScreen():
    global Dash_Orb, End_Portal2, Chest_sprite, Player_1, Cutscene
    if Screen == 2:
        scene.set_background_image(assets.image("""
            Level 1 Background
        """))
        tiles.set_current_tilemap(tilemap("""
            level1 tilemap
        """))
        Dash_Orb = sprites.create(assets.image("""
            Dash Orb
        """), SpriteKind.DashOrb)
        End_Portal2 = sprites.create(assets.image("""
                End Portal Sprite
            """),
            SpriteKind.End_Portal)
        Chest_sprite = sprites.create(assets.image("""
            Closed Chest
        """), SpriteKind.Chest)
        tiles.place_on_tile(End_Portal2, tiles.get_tile_location(49, 4))
        tiles.place_on_tile(Chest_sprite, tiles.get_tile_location(49, 10))
        tiles.place_on_tile(Dash_Orb, tiles.get_tile_location(0, 6))
        Player_1 = sprites.create(assets.image("""
                Player Facing Right
            """),
            SpriteKind.player)
        Player_1.ay = 550
        scene.camera_follow_sprite(Player_1)
        tiles.place_on_tile(Player_1, tiles.get_tile_location(48, 4))
        Cutscene = False
        # SpawnEnemies()
        story.print_text("\"Level 1 - Start\"", 80, 200)
        controller.move_sprite(Player_1, 75, 0)
    if Screen == 3:
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        scene.set_background_image(assets.image("""
            Level 1 Background
        """))
        tiles.set_current_tilemap(tilemap("""
            Level 1 Boss Fight Tilemap
        """))
        Dash_Orb.destroy()
        Chest_sprite.destroy()
        End_Portal2.destroy()
        tiles.place_on_tile(Player_1, tiles.get_tile_location(0, 15))
        SpawnEnemies()
def SpawnEnemies():
    global Sriram
    for value in tiles.get_tiles_by_type(assets.tile("""
        Spawn Tile
    """)):
        Sriram = sprites.create(assets.image("""
                Monkey Facing Right
            """),
            SpriteKind.enemy)
        tiles.place_on_tile(Sriram, value)
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
def GainDash():
    global Cutscene, Dash_Unlocked
    animation.run_image_animation(Dash_Orb,
        assets.animation("""
            Orb Gain Animation
        """),
        75,
        False)
    Cutscene = True
    controller.move_sprite(Player_1, 0, 0)
    setplayerdirection()
    story.print_text("\"Dash Gained\"", 80, 60)
    story.print_text("\"Press SPACE to dash\"", 80, 60)
    
    def on_after3():
        global Cutscene
        Cutscene = False
        controller.move_sprite(Player_1, 75, 0)
        Player_1.vx = 0
    timer.after(400, on_after3)
    
    Dash_Unlocked = True

def on_on_overlap3(sprite32, otherSprite22):
    global enemywamoushindeiru
    enemywamoushindeiru = True
    sprite32.destroy()
    
    def on_after4():
        tiles.set_tile_at(otherSprite22.tilemap_location(),
            assets.tile("""
                Tombstone
            """))
    timer.after(50, on_after4)
    
    otherSprite22.destroy()
    
    def on_after5():
        global enemywamoushindeiru
        enemywamoushindeiru = False
    timer.after(500, on_after5)
    
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def dash():
    global dashing
    Player_1.ay = 0
    Player_1.set_velocity(0, 0)
    if lastdirection:
        controller.move_sprite(Player_1, 0, 0)
        Player_1.vx = 200
        
        def on_after6():
            Player_1.vx = 200
        timer.after(70, on_after6)
        
        
        def on_after7():
            Player_1.vx = 200
        timer.after(140, on_after7)
        
        
        def on_after8():
            Player_1.vx = 200
        timer.after(210, on_after8)
        
        
        def on_after9():
            Player_1.vx = 200
        timer.after(280, on_after9)
        
        
        def on_after10():
            Player_1.vx = 200
        timer.after(350, on_after10)
        
        dashing = True
        Player_1.set_image(assets.image("""
            Dash right
        """))
        
        def on_after11():
            global dashing
            controller.move_sprite(Player_1, 75, 0)
            Player_1.vx = 0
            Player_1.set_image(assets.image("""
                Player Facing Right
            """))
            dashing = False
        timer.after(350, on_after11)
        
    else:
        controller.move_sprite(Player_1, 0, 0)
        Player_1.vx = -200
        
        def on_after12():
            Player_1.vx = -200
        timer.after(70, on_after12)
        
        
        def on_after13():
            Player_1.vx = -200
        timer.after(140, on_after13)
        
        
        def on_after14():
            Player_1.vx = -200
        timer.after(210, on_after14)
        
        
        def on_after15():
            Player_1.vx = -200
        timer.after(280, on_after15)
        
        
        def on_after16():
            Player_1.vx = -200
        timer.after(350, on_after16)
        
        dashing = True
        Player_1.set_image(assets.image("""
            Dashleft
        """))
        
        def on_after17():
            global dashing
            controller.move_sprite(Player_1, 75, 0)
            Player_1.vx = 0
            Player_1.set_image(assets.image("""
                Player facing backward
            """))
            dashing = False
        timer.after(350, on_after17)
        
    
    def on_after18():
        Player_1.ay = 550
    timer.after(350, on_after18)
    

def on_on_zero(status):
    global Harambewamoushindeiru, BossFightStage
    Harambewamoushindeiru = True
    status.sprite_attached_to().destroy()
    BossFightStage = 3
    
    def on_after19():
        global Harambewamoushindeiru
        Harambewamoushindeiru = False
    timer.after(500, on_after19)
    
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_on_overlap4(sprite22, otherSprite2):
    GainDash()
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.DashOrb, on_on_overlap4)

def SpawnHarambe():
    global Harambe, tile_loc, Harambe_health
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        HarambeTile
    """)):
        Harambe = sprites.create(assets.image("""
                MonkeyBoss
            """),
            SpriteKind.Level_1_Boss)
        tile_loc = tiles.get_tiles_by_type(assets.tile("""
            HarambeTile
        """))
        tiles.place_on_tile(Harambe, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))
        Harambe.set_velocity(0, 50)
        Harambe_health = statusbars.create(20, 4, StatusBarKind.enemy_health)
        Harambe_health.attach_to_sprite(Harambe)
def attack():
    global shot
    if current_weapon == weapons_list[1]:
        shot = sprites.create(assets.image("""
            Common Shot
        """), SpriteKind.projectile)
        
        def on_after20():
            shot.destroy()
        timer.after(100, on_after20)
        
        if lastdirection:
            shot.set_velocity(500, 0)
        else:
            shot.set_velocity(-500, 0)
    elif current_weapon == weapons_list[2]:
        shot = sprites.create(assets.image("""
                Uncommon Shot
            """),
            SpriteKind.projectile)
        
        def on_after21():
            shot.destroy()
        timer.after(110, on_after21)
        
        if lastdirection:
            shot.set_velocity(500, 0)
        else:
            shot.set_velocity(-500, 0)
    else:
        pass
    shot.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
    shot.set_flag(SpriteFlag.AUTO_DESTROY, True)
    shot.set_position(Player_1.x, Player_1.y)

def on_on_overlap5(sprite34, otherSprite24):
    global Cutscene, current_weapon, Reload_Time
    animation.run_image_animation(Chest_sprite,
        assets.animation("""
            Chest Animation
        """),
        250,
        False)
    Cutscene = True
    Player_1.set_velocity(0, 0)
    controller.move_sprite(Player_1, 0, 0)
    setplayerdirection()
    story.print_text("New Weapon Unlocked:    Rapier",
        sprite34.x,
        sprite34.y - 30)
    current_weapon = weapons_list[2]
    Cutscene = False
    controller.move_sprite(Player_1, 75, 0)
    Player_1.vx = 0
    Reload_Time = 750
    tiles.set_tile_at(Chest_sprite.tilemap_location(),
        assets.tile("""
            Opened Chest
        """))
    Chest_sprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Chest, on_on_overlap5)

def on_on_overlap6(sprite35, otherSprite25):
    global Screen
    animation.run_image_animation(otherSprite25,
        assets.animation("""
            Portal open
        """),
        75,
        False)
    pause(525)
    Screen += 1
    if Screen == 4:
        game.over(True)
    updateScreen()
sprites.on_overlap(SpriteKind.player, SpriteKind.End_Portal, on_on_overlap6)

def Mini_Harambe_shots():
    global x, shot_12, shot_2
    if Harambewamoushindeiru == False:
        if MiniHarambe.is_hitting_tile(CollisionDirection.BOTTOM):
            x = randint(0, 1)
            for value3 in sprites.all_of_kind(SpriteKind.Level_1_Boss):
                if Player_1.tilemap_location().column >= value3.tilemap_location().column:
                    shot_12 = sprites.create(assets.image("""
                            Boss Shot Image
                        """),
                        SpriteKind.Boss_Projectile)
                    if x == 0:
                        tiles.place_on_tile(shot_12, tiles.get_tile_location(49, 26))
                    else:
                        tiles.place_on_tile(shot_12, tiles.get_tile_location(49, 28))
                    shot_12.vx = 100
                else:
                    shot_2 = sprites.create(assets.image("""
                            Boss Shot Image
                        """),
                        SpriteKind.Boss_Projectile)
                    if x == 1:
                        tiles.place_on_tile(shot_2, tiles.get_tile_location(62, 26))
                    else:
                        tiles.place_on_tile(shot_2, tiles.get_tile_location(62, 28))
                    shot_2.vx = -100
def EnemyShot(Enemy_shooter: Sprite):
    global shot
    if Playerwamoushindeiru == False:
        if Screen == 2 or Screen == 3:
            if enemywamoushindeiru == False:
                shot = sprites.create(assets.image("""
                        Monkey Shot
                    """),
                    SpriteKind.Enemy_Projectile)
                shot.set_position(Enemy_shooter.x, Enemy_shooter.y)
                if enemywamoushindeiru == False:
                    if Player_1.tilemap_location().column > Enemy_shooter.tilemap_location().column:
                        shot.set_velocity(150, 0)
                        Enemy_shooter.set_image(assets.image("""
                            Monkey Facing Right
                        """))
                    else:
                        shot.set_velocity(-150, 0)
                        Enemy_shooter.set_image(assets.image("""
                            Monkey Facing Left
                        """))
                    shot.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
                    shot.set_flag(SpriteFlag.AUTO_DESTROY, True)

def on_on_overlap7(sprite3, otherSprite3):
    global Playerwamoushindeiru
    Playerwamoushindeiru = True
    sprites.destroy_all_sprites_of_kind(SpriteKind.End_Portal)
    
    def on_after22():
        game.over(False)
    timer.after(15, on_after22)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.Level_1_Boss, on_on_overlap7)

def on_on_overlap8(sprite4, otherSprite4):
    global Playerwamoushindeiru
    Playerwamoushindeiru = True
    sprites.destroy_all_sprites_of_kind(SpriteKind.End_Portal)
    
    def on_after23():
        game.over(False)
    timer.after(15, on_after23)
    
sprites.on_overlap(SpriteKind.player,
    SpriteKind.Boss_Projectile,
    on_on_overlap8)

def Spawn_mini_Harambe():
    global MiniHarambe, tile_loc2, MiniHarambe_health
    for value22 in tiles.get_tiles_by_type(assets.tile("""
        MiniHarambeSpawn
    """)):
        MiniHarambe = sprites.create(assets.image("""
                MonkeyBoss
            """),
            SpriteKind.Level_1_Boss)
        tile_loc2 = tiles.get_tiles_by_type(assets.tile("""
            MiniHarambeSpawn
        """))
        tiles.place_on_tile(MiniHarambe, value22)
        tiles.set_tile_at(value22, assets.tile("""
            transparency16
        """))
        MiniHarambe.ay = 200
        MiniHarambe_health = statusbars.create(20, 4, StatusBarKind.enemy_health)
        MiniHarambe_health.attach_to_sprite(MiniHarambe)
def Harambe_jump():
    global x
    x = randint(1, 3)
    if Harambe.is_hitting_tile(CollisionDirection.BOTTOM):
        if Player_1.tilemap_location().column > Harambe.tilemap_location().column:
            Harambe.set_velocity(15 * x, -110)
            Harambe.ay = 200
        if Player_1.tilemap_location().column < Harambe.tilemap_location().column:
            Harambe.set_velocity(-15 * x, -110)
            Harambe.ay = 200
playerstill = False
attacking = False
downdash = False
MiniHarambe_health: StatusBarSprite = None
tile_loc2: List[tiles.Location] = []
shot_2: Sprite = None
shot_12: Sprite = None
x = 0
MiniHarambe: Sprite = None
shot: Sprite = None
Harambe_health: StatusBarSprite = None
tile_loc: List[tiles.Location] = []
dashing = False
enemywamoushindeiru = False
Sriram: Sprite = None
Chest_sprite: Sprite = None
End_Portal2: Sprite = None
Dash_Orb: Sprite = None
Harambe: Sprite = None
shot_1: Sprite = None
Player_1: Sprite = None
Harambewamoushindeiru = False
BossFightStage = 0
Playerwamoushindeiru = False
lastdirection = False
Dash_Unlocked = False
Screen = 0
Cutscene = False
Reload_Time = 0
current_weapon = ""
weapons_list: List[str] = []
weapons_list = ["fist", "sword", "rapier", "broadsword", "excaliber"]
current_weapon = weapons_list[1]
Reload_Time = 1000
Cutscene = True
Screen = 2
Dash_Unlocked = False
lastdirection = True
story.set_sound_enabled(False)
updateScreen()

def on_on_update():
    global dashing, downdash
    if downdash:
        if Player_1.is_hitting_tile(CollisionDirection.BOTTOM):
            dashing = False
            controller.move_sprite(Player_1, 75, 0)
            downdash = False
            if lastdirection:
                Player_1.set_image(assets.image("""
                    Player Facing Right
                """))
            else:
                Player_1.set_image(assets.image("""
                    Player facing backward
                """))
game.on_update(on_on_update)

def on_on_update2():
    global downdash, dashing
    stompunlocked = 0
    if stompunlocked:
        if Cutscene == False:
            if controller.down.is_pressed() and Player_1.tile_kind_at(TileDirection.BOTTOM,
                assets.tile("""
                    transparency16
                """)):
                Player_1.set_image(assets.image("""
                    Downward Strike Sprite Image
                """))
                controller.move_sprite(Player_1, 0, 0)
                downdash = True
                dashing = True
                Player_1.set_velocity(0, 400)
game.on_update(on_on_update2)

def on_on_update3():
    if Cutscene == False:
        if controller.B.is_pressed():
            
            def on_throttle():
                global attacking
                attacking = True
                if lastdirection:
                    animation.run_image_animation(Player_1,
                        assets.animation("""
                            Attack Common Sword Right
                        """),
                        100,
                        False)
                    
                    def on_after24():
                        global Cutscene, attacking
                        if playerstill:
                            if lastdirection:
                                animation.run_image_animation(Player_1,
                                    assets.animation("""
                                        Run forward animation
                                    """),
                                    75,
                                    True)
                            else:
                                animation.run_image_animation(Player_1,
                                    assets.animation("""
                                        Run Backward animation
                                    """),
                                    75,
                                    True)
                        elif lastdirection:
                            Player_1.set_image(assets.image("""
                                Player Facing Right
                            """))
                        else:
                            Player_1.set_image(assets.image("""
                                Player facing backward
                            """))
                        Cutscene = False
                        attacking = False
                    timer.after(300, on_after24)
                    
                    attack()
                else:
                    animation.run_image_animation(Player_1,
                        assets.animation("""
                            Attack Common Sword Left
                        """),
                        100,
                        False)
                    
                    def on_after25():
                        global Cutscene, attacking
                        if playerstill:
                            if lastdirection:
                                animation.run_image_animation(Player_1,
                                    assets.animation("""
                                        Run forward animation
                                    """),
                                    75,
                                    True)
                            else:
                                animation.run_image_animation(Player_1,
                                    assets.animation("""
                                        Run Backward animation
                                    """),
                                    75,
                                    True)
                        elif lastdirection:
                            Player_1.set_image(assets.image("""
                                Player Facing Right
                            """))
                        else:
                            Player_1.set_image(assets.image("""
                                Player facing backward
                            """))
                        Cutscene = False
                        attacking = False
                    timer.after(300, on_after25)
                    
                    attack()
            timer.throttle("attack", Reload_Time, on_throttle)
            
game.on_update(on_on_update3)

def on_on_update4():
    if Cutscene == False:
        if controller.A.is_pressed():
            if Dash_Unlocked:
                
                def on_throttle2():
                    dash()
                timer.throttle("dash", 3000, on_throttle2)
                
game.on_update(on_on_update4)

def on_on_update5():
    global BossFightStage
    if Screen == 3:
        if Math.floor(Player_1.tilemap_location().column) == 29:
            if Math.floor(Player_1.tilemap_location().row) > 25:
                tiles.set_tile_at(tiles.get_tile_location(28, 25), sprites.dungeon.floor_dark2)
                tiles.set_tile_at(tiles.get_tile_location(28, 26), sprites.dungeon.floor_dark2)
                tiles.set_tile_at(tiles.get_tile_location(28, 27), sprites.dungeon.floor_dark2)
                tiles.set_tile_at(tiles.get_tile_location(28, 28), sprites.dungeon.floor_dark2)
                tiles.set_wall_at(tiles.get_tile_location(28, 25), True)
                tiles.set_wall_at(tiles.get_tile_location(28, 26), True)
                tiles.set_wall_at(tiles.get_tile_location(28, 27), True)
                tiles.set_wall_at(tiles.get_tile_location(28, 28), True)
                sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
                
                def on_throttle3():
                    global shot
                    shot = sprites.create(assets.image("""
                            Boss Shot Image
                        """),
                        SpriteKind.Boss_Projectile)
                    if randint(0, 1) == 0:
                        tiles.place_on_tile(shot, tiles.get_tile_location(50, 28))
                    else:
                        tiles.place_on_tile(shot, tiles.get_tile_location(50, 26))
                    shot.vx = -135
                timer.throttle("action", 1000000000, on_throttle3)
                
                BossFightStage = 1
        if Math.floor(Player_1.tilemap_location().column) == 47:
            sprites.destroy_all_sprites_of_kind(SpriteKind.Boss_Projectile)
            BossFightStage = 2
        if Math.floor(Player_1.tilemap_location().column) == 48:
            tiles.set_tile_at(tiles.get_tile_location(47, 25), sprites.dungeon.floor_dark2)
            tiles.set_tile_at(tiles.get_tile_location(47, 26), sprites.dungeon.floor_dark2)
            tiles.set_tile_at(tiles.get_tile_location(47, 27), sprites.dungeon.floor_dark2)
            tiles.set_tile_at(tiles.get_tile_location(47, 28), sprites.dungeon.floor_dark2)
            tiles.set_wall_at(tiles.get_tile_location(47, 25), True)
            tiles.set_wall_at(tiles.get_tile_location(47, 26), True)
            tiles.set_wall_at(tiles.get_tile_location(47, 27), True)
            tiles.set_wall_at(tiles.get_tile_location(47, 28), True)
            sprites.destroy_all_sprites_of_kind(SpriteKind.Boss_Projectile)
game.on_update(on_on_update5)

def on_on_update6():
    for value222 in sprites.all_of_kind(SpriteKind.Boss_Projectile):
        if value222.tilemap_location().column == 29:
            value222.destroy()
game.on_update(on_on_update6)

def on_on_update7():
    if BossFightStage == 2:
        SpawnHarambe()
        animation.run_image_animation(Harambe, assets.animation("""
            myAnim
        """), 100, True)
game.on_update(on_on_update7)

def on_on_update8():
    if BossFightStage == 3:
        for value223 in sprites.all_of_kind(SpriteKind.Boss_Projectile):
            if value223.tilemap_location().column == 48:
                value223.destroy()
            elif value223.tilemap_location().column == 63:
                value223.destroy()
game.on_update(on_on_update8)

def on_on_update9():
    if BossFightStage == 3:
        
        def on_after26():
            global BossFightStage
            if len(sprites.all_of_kind(SpriteKind.Level_1_Boss)) == 0:
                BossFightStage += 1
        timer.after(1500, on_after26)
        
game.on_update(on_on_update9)

def on_on_update10():
    global playerstill, lastdirection
    if Cutscene == False:
        if Player_1.vx < 0:
            playerstill = False
            lastdirection = False
        if Player_1.vx > 0:
            playerstill = False
            lastdirection = True
        if Player_1.vx == 0:
            playerstill = True
        if controller.right.is_pressed():
            if dashing == False:
                if attacking == False:
                    if downdash == False:
                        
                        def on_throttle4():
                            animation.run_image_animation(Player_1,
                                assets.animation("""
                                    Run forward animation
                                """),
                                75,
                                True)
                        timer.throttle("move", 300, on_throttle4)
                        
        elif controller.left.is_pressed():
            if dashing == False:
                if attacking == False:
                    if downdash == False:
                        
                        def on_throttle5():
                            animation.run_image_animation(Player_1,
                                assets.animation("""
                                    Run Backward animation
                                """),
                                75,
                                True)
                        timer.throttle("move", 300, on_throttle5)
                        
        elif lastdirection:
            if attacking == False:
                if dashing == False:
                    Player_1.set_image(assets.image("""
                        Player Facing Right
                    """))
        elif attacking == False:
            if dashing == False:
                Player_1.set_image(assets.image("""
                    Player facing backward
                """))
        else:
            pass
    if dashing:
        if downdash == False:
            if lastdirection:
                Player_1.set_image(assets.image("""
                    Dash right
                """))
            else:
                Player_1.set_image(assets.image("""
                    Dashleft
                """))
game.on_update(on_on_update10)

def on_on_update11():
    global End_Portal2
    if BossFightStage == 4:
        End_Portal2 = sprites.create(assets.image("""
                End Portal Sprite
            """),
            SpriteKind.End_Portal)
        tiles.place_on_tile(End_Portal2, tiles.get_tile_location(63, 28))
game.on_update(on_on_update11)

def on_update_interval():
    for value322 in sprites.all_of_kind(SpriteKind.enemy):
        if randint(1, 6) != 6:
            if Playerwamoushindeiru == False:
                if enemywamoushindeiru == False:
                    if Player_1.tilemap_location().column > value322.tilemap_location().column:
                        value322.set_image(assets.image("""
                            Monkey Facing Right
                        """))
                    else:
                        value322.set_image(assets.image("""
                            Monkey Facing Left
                        """))
                    if Player_1.tilemap_location().column > value322.tilemap_location().column:
                        animation.run_image_animation(value322,
                            assets.animation("""
                                Monkey Shoot Left0
                            """),
                            50,
                            False)
                        
                        def on_after27():
                            EnemyShot(value322)
                            value322.set_image(assets.image("""
                                Monkey Facing Right
                            """))
                        timer.after(300, on_after27)
                        
                    else:
                        animation.run_image_animation(value322,
                            assets.animation("""
                                Monkey Shoot Left
                            """),
                            50,
                            False)
                        
                        def on_after28():
                            EnemyShot(value322)
                            value322.set_image(assets.image("""
                                Monkey Facing Left
                            """))
                        timer.after(300, on_after28)
                        
game.on_update_interval(randint(750, 1250), on_update_interval)

def on_update_interval2():
    global shot
    if BossFightStage == 1:
        shot = sprites.create(assets.image("""
                Boss Shot Image
            """),
            SpriteKind.Boss_Projectile)
        if randint(0, 1) == 0:
            tiles.place_on_tile(shot, tiles.get_tile_location(55, 28))
        else:
            tiles.place_on_tile(shot, tiles.get_tile_location(55, 26))
        shot.vx = -135
    if BossFightStage == 2:
        Harambe_jump()
    if BossFightStage == 3:
        Spawn_mini_Harambe()
        if Harambewamoushindeiru == False:
            Mini_Harambe_shots()
game.on_update_interval(1500, on_update_interval2)
