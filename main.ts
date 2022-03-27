namespace SpriteKind {
    export const Object = SpriteKind.create()
    export const DashOrb = SpriteKind.create()
    export const DeathCam = SpriteKind.create()
    export const Enemy_Projectile = SpriteKind.create()
    export const Chest = SpriteKind.create()
    export const End_Portal = SpriteKind.create()
    export const Level_1_Boss = SpriteKind.create()
    export const Boss_Projectile = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Enemy_Projectile, SpriteKind.Player, function (sprite33, otherSprite23) {
    Playerwamoushindeiru = true
    timer.after(15, function () {
        game.over(false)
    })
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Level_1_Boss, function (sprite, otherSprite) {
    sprite.destroy()
    if (BossFightStage == 2) {
        statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite).value += -5 - weapons_list.indexOf(current_weapon)
    }
    if (BossFightStage == 3) {
        statusbars.getStatusBarAttachedTo(StatusBarKind.EnemyHealth, otherSprite).value += -10 - weapons_list.indexOf(current_weapon)
    }
})
function Harambe_Shot () {
    if (Harambewamoushindeiru == false) {
        for (let value32 of sprites.allOfKind(SpriteKind.Level_1_Boss)) {
            if (Player_1.tilemapLocation().column >= value32.tilemapLocation().column) {
                shot_1 = sprites.create(assets.image`Boss Shot Image`, SpriteKind.Boss_Projectile)
                tiles.placeOnTile(shot_1, tiles.getTileLocation(Harambe.tilemapLocation().column, Harambe.tilemapLocation().row))
                shot_1.vx = 100
            } else {
                shot_1 = sprites.create(assets.image`Boss Shot Image`, SpriteKind.Boss_Projectile)
                tiles.placeOnTile(shot_1, tiles.getTileLocation(Harambe.tilemapLocation().column, Harambe.tilemapLocation().row))
                shot_1.vx = -100
            }
        }
    }
}
function setplayerdirection () {
    animation.stopAnimation(animation.AnimationTypes.All, Player_1)
    if (lastdirection) {
        Player_1.setImage(assets.image`Player Facing Right`)
    } else {
        Player_1.setImage(assets.image`Player facing backward`)
    }
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Cutscene == false) {
        if (Player_1.vy == 0) {
            Player_1.vy = -200
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Spike`, function (sprite2, location) {
    Playerwamoushindeiru = true
    timer.after(15, function () {
        game.over(false)
    })
})
function updateScreen () {
    if (Screen == 2) {
        scene.setBackgroundImage(assets.image`Level 1 Background`)
        tiles.setCurrentTilemap(tilemap`level1 tilemap`)
        Dash_Orb = sprites.create(assets.image`Dash Orb`, SpriteKind.DashOrb)
        End_Portal2 = sprites.create(assets.image`End Portal Sprite`, SpriteKind.End_Portal)
        Chest_sprite = sprites.create(assets.image`Closed Chest`, SpriteKind.Chest)
        tiles.placeOnTile(End_Portal2, tiles.getTileLocation(49, 4))
        tiles.placeOnTile(Chest_sprite, tiles.getTileLocation(49, 10))
        tiles.placeOnTile(Dash_Orb, tiles.getTileLocation(0, 6))
        Player_1 = sprites.create(assets.image`Player Facing Right`, SpriteKind.Player)
        Player_1.ay = 550
        scene.cameraFollowSprite(Player_1)
        tiles.placeOnTile(Player_1, tiles.getTileLocation(48, 4))
        Cutscene = false
        // SpawnEnemies()
        story.printText("\"Level 1 - Start\"", 80, 200)
        controller.moveSprite(Player_1, 75, 0)
    }
    if (Screen == 3) {
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
        scene.setBackgroundImage(assets.image`Level 1 Background`)
        tiles.setCurrentTilemap(tilemap`Level 1 Boss Fight Tilemap`)
        Dash_Orb.destroy()
        Chest_sprite.destroy()
        End_Portal2.destroy()
        tiles.placeOnTile(Player_1, tiles.getTileLocation(0, 15))
        SpawnEnemies()
    }
}
function SpawnEnemies () {
    for (let value of tiles.getTilesByType(assets.tile`Spawn Tile`)) {
        Sriram = sprites.create(assets.image`Monkey Facing Right`, SpriteKind.Enemy)
        tiles.placeOnTile(Sriram, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
    }
}
function GainDash () {
    animation.runImageAnimation(
    Dash_Orb,
    assets.animation`Orb Gain Animation`,
    75,
    false
    )
    Cutscene = true
    controller.moveSprite(Player_1, 0, 0)
    setplayerdirection()
    story.printText("\"Dash Gained\"", 80, 60)
    story.printText("\"Press SPACE to dash\"", 80, 60)
    timer.after(400, function () {
        Cutscene = false
        controller.moveSprite(Player_1, 75, 0)
        Player_1.vx = 0
    })
    Dash_Unlocked = true
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite32, otherSprite22) {
    enemywamoushindeiru = true
    sprite32.destroy()
    timer.after(50, function () {
        tiles.setTileAt(otherSprite22.tilemapLocation(), assets.tile`Tombstone`)
    })
    otherSprite22.destroy()
    timer.after(500, function () {
        enemywamoushindeiru = false
    })
})
function dash () {
    Player_1.ay = 0
    Player_1.setVelocity(0, 0)
    if (lastdirection) {
        controller.moveSprite(Player_1, 0, 0)
        Player_1.vx = 200
        timer.after(70, function () {
            Player_1.vx = 200
        })
        timer.after(140, function () {
            Player_1.vx = 200
        })
        timer.after(210, function () {
            Player_1.vx = 200
        })
        timer.after(280, function () {
            Player_1.vx = 200
        })
        timer.after(350, function () {
            Player_1.vx = 200
        })
        dashing = true
        Player_1.setImage(assets.image`Dash right`)
        timer.after(350, function () {
            controller.moveSprite(Player_1, 75, 0)
            Player_1.vx = 0
            Player_1.setImage(assets.image`Player Facing Right`)
            dashing = false
        })
    } else {
        controller.moveSprite(Player_1, 0, 0)
        Player_1.vx = -200
        timer.after(70, function () {
            Player_1.vx = -200
        })
        timer.after(140, function () {
            Player_1.vx = -200
        })
        timer.after(210, function () {
            Player_1.vx = -200
        })
        timer.after(280, function () {
            Player_1.vx = -200
        })
        timer.after(350, function () {
            Player_1.vx = -200
        })
        dashing = true
        Player_1.setImage(assets.image`Dashleft`)
        timer.after(350, function () {
            controller.moveSprite(Player_1, 75, 0)
            Player_1.vx = 0
            Player_1.setImage(assets.image`Player facing backward`)
            dashing = false
        })
    }
    timer.after(350, function () {
        Player_1.ay = 550
    })
}
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    Harambewamoushindeiru = true
    status.spriteAttachedTo().destroy()
    BossFightStage = 3
    timer.after(500, function () {
        Harambewamoushindeiru = false
    })
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.DashOrb, function (sprite22, otherSprite2) {
    GainDash()
    otherSprite2.destroy()
})
function SpawnHarambe () {
    for (let value2 of tiles.getTilesByType(assets.tile`HarambeTile`)) {
        Harambe = sprites.create(assets.image`MonkeyBoss`, SpriteKind.Level_1_Boss)
        tile_loc = tiles.getTilesByType(assets.tile`HarambeTile`)
        tiles.placeOnTile(Harambe, value2)
        tiles.setTileAt(value2, assets.tile`transparency16`)
        Harambe.setVelocity(0, 50)
        Harambe_health = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
        Harambe_health.attachToSprite(Harambe)
    }
}
function attack () {
    if (current_weapon == weapons_list[1]) {
        shot = sprites.create(assets.image`Common Shot`, SpriteKind.Projectile)
        timer.after(100, function () {
            shot.destroy()
        })
        if (lastdirection) {
            shot.setVelocity(500, 0)
        } else {
            shot.setVelocity(-500, 0)
        }
    } else if (current_weapon == weapons_list[2]) {
        shot = sprites.create(assets.image`Uncommon Shot`, SpriteKind.Projectile)
        timer.after(110, function () {
            shot.destroy()
        })
        if (lastdirection) {
            shot.setVelocity(500, 0)
        } else {
            shot.setVelocity(-500, 0)
        }
    } else {
    	
    }
    shot.setFlag(SpriteFlag.DestroyOnWall, true)
    shot.setFlag(SpriteFlag.AutoDestroy, true)
    shot.setPosition(Player_1.x, Player_1.y)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Chest, function (sprite34, otherSprite24) {
    animation.runImageAnimation(
    Chest_sprite,
    assets.animation`Chest Animation`,
    250,
    false
    )
    Cutscene = true
    Player_1.setVelocity(0, 0)
    controller.moveSprite(Player_1, 0, 0)
    setplayerdirection()
    story.printText("New Weapon Unlocked:    Rapier", sprite34.x, sprite34.y - 30)
    current_weapon = weapons_list[2]
    Cutscene = false
    controller.moveSprite(Player_1, 75, 0)
    Player_1.vx = 0
    Reload_Time = 750
    tiles.setTileAt(Chest_sprite.tilemapLocation(), assets.tile`Opened Chest`)
    Chest_sprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.End_Portal, function (sprite35, otherSprite25) {
    animation.runImageAnimation(
    otherSprite25,
    assets.animation`Portal open`,
    75,
    false
    )
    pause(525)
    Screen += 1
    if (Screen == 4) {
        game.over(true)
    }
    updateScreen()
})
function Mini_Harambe_shots () {
    if (Harambewamoushindeiru == false) {
        if (MiniHarambe.isHittingTile(CollisionDirection.Bottom)) {
            x = randint(0, 1)
            for (let value3 of sprites.allOfKind(SpriteKind.Level_1_Boss)) {
                if (Player_1.tilemapLocation().column >= value3.tilemapLocation().column) {
                    shot_12 = sprites.create(assets.image`Boss Shot Image`, SpriteKind.Boss_Projectile)
                    if (x == 0) {
                        tiles.placeOnTile(shot_12, tiles.getTileLocation(49, 26))
                    } else {
                        tiles.placeOnTile(shot_12, tiles.getTileLocation(49, 28))
                    }
                    shot_12.vx = 100
                } else {
                    shot_2 = sprites.create(assets.image`Boss Shot Image`, SpriteKind.Boss_Projectile)
                    if (x == 1) {
                        tiles.placeOnTile(shot_2, tiles.getTileLocation(62, 26))
                    } else {
                        tiles.placeOnTile(shot_2, tiles.getTileLocation(62, 28))
                    }
                    shot_2.vx = -100
                }
            }
        }
    }
}
function EnemyShot (Enemy_shooter: Sprite) {
    if (Playerwamoushindeiru == false) {
        if (Screen == 2 || Screen == 3) {
            if (enemywamoushindeiru == false) {
                shot = sprites.create(assets.image`Monkey Shot`, SpriteKind.Enemy_Projectile)
                shot.setPosition(Enemy_shooter.x, Enemy_shooter.y)
                if (enemywamoushindeiru == false) {
                    if (Player_1.tilemapLocation().column > Enemy_shooter.tilemapLocation().column) {
                        shot.setVelocity(150, 0)
                        Enemy_shooter.setImage(assets.image`Monkey Facing Right`)
                    } else {
                        shot.setVelocity(-150, 0)
                        Enemy_shooter.setImage(assets.image`Monkey Facing Left`)
                    }
                    shot.setFlag(SpriteFlag.DestroyOnWall, true)
                    shot.setFlag(SpriteFlag.AutoDestroy, true)
                }
            }
        }
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Level_1_Boss, function (sprite3, otherSprite3) {
    Playerwamoushindeiru = true
    sprites.destroyAllSpritesOfKind(SpriteKind.End_Portal)
    timer.after(15, function () {
        game.over(false)
    })
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Boss_Projectile, function (sprite4, otherSprite4) {
    Playerwamoushindeiru = true
    sprites.destroyAllSpritesOfKind(SpriteKind.End_Portal)
    timer.after(15, function () {
        game.over(false)
    })
})
function Spawn_mini_Harambe () {
    for (let value22 of tiles.getTilesByType(assets.tile`MiniHarambeSpawn`)) {
        MiniHarambe = sprites.create(assets.image`MonkeyBoss`, SpriteKind.Level_1_Boss)
        tile_loc2 = tiles.getTilesByType(assets.tile`MiniHarambeSpawn`)
        tiles.placeOnTile(MiniHarambe, value22)
        tiles.setTileAt(value22, assets.tile`transparency16`)
        MiniHarambe.ay = 200
        MiniHarambe_health = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
        MiniHarambe_health.attachToSprite(MiniHarambe)
    }
}
function Harambe_jump () {
    x = randint(1, 3)
    if (Harambe.isHittingTile(CollisionDirection.Bottom)) {
        if (Player_1.tilemapLocation().column > Harambe.tilemapLocation().column) {
            Harambe.setVelocity(15 * x, -110)
            Harambe.ay = 200
        }
        if (Player_1.tilemapLocation().column < Harambe.tilemapLocation().column) {
            Harambe.setVelocity(-15 * x, -110)
            Harambe.ay = 200
        }
    }
}
let playerstill = false
let attacking = false
let downdash = false
let MiniHarambe_health: StatusBarSprite = null
let tile_loc2: tiles.Location[] = []
let shot_2: Sprite = null
let shot_12: Sprite = null
let x = 0
let MiniHarambe: Sprite = null
let shot: Sprite = null
let Harambe_health: StatusBarSprite = null
let tile_loc: tiles.Location[] = []
let dashing = false
let enemywamoushindeiru = false
let Sriram: Sprite = null
let Chest_sprite: Sprite = null
let End_Portal2: Sprite = null
let Dash_Orb: Sprite = null
let Harambe: Sprite = null
let shot_1: Sprite = null
let Player_1: Sprite = null
let Harambewamoushindeiru = false
let BossFightStage = 0
let Playerwamoushindeiru = false
let lastdirection = false
let Dash_Unlocked = false
let Screen = 0
let Cutscene = false
let Reload_Time = 0
let current_weapon = ""
let weapons_list: string[] = []
weapons_list = [
"fist",
"sword",
"rapier",
"broadsword",
"excaliber"
]
current_weapon = weapons_list[1]
Reload_Time = 1000
Cutscene = true
Screen = 2
Dash_Unlocked = false
lastdirection = true
story.setSoundEnabled(false)
updateScreen()
game.onUpdate(function () {
    if (downdash) {
        if (Player_1.isHittingTile(CollisionDirection.Bottom)) {
            dashing = false
            controller.moveSprite(Player_1, 75, 0)
            downdash = false
            if (lastdirection) {
                Player_1.setImage(assets.image`Player Facing Right`)
            } else {
                Player_1.setImage(assets.image`Player facing backward`)
            }
        }
    }
})
game.onUpdate(function () {
    let stompunlocked = 0
    if (stompunlocked) {
        if (Cutscene == false) {
            if (controller.down.isPressed() && Player_1.tileKindAt(TileDirection.Bottom, assets.tile`transparency16`)) {
                Player_1.setImage(assets.image`Downward Strike Sprite Image`)
                controller.moveSprite(Player_1, 0, 0)
                downdash = true
                dashing = true
                Player_1.setVelocity(0, 400)
            }
        }
    }
})
game.onUpdate(function () {
    if (Cutscene == false) {
        if (controller.B.isPressed()) {
            timer.throttle("attack", Reload_Time, function () {
                attacking = true
                if (lastdirection) {
                    animation.runImageAnimation(
                    Player_1,
                    assets.animation`Attack Common Sword Right`,
                    100,
                    false
                    )
                    timer.after(300, function () {
                        if (playerstill) {
                            if (lastdirection) {
                                animation.runImageAnimation(
                                Player_1,
                                assets.animation`Run forward animation`,
                                75,
                                true
                                )
                            } else {
                                animation.runImageAnimation(
                                Player_1,
                                assets.animation`Run Backward animation`,
                                75,
                                true
                                )
                            }
                        } else if (lastdirection) {
                            Player_1.setImage(assets.image`Player Facing Right`)
                        } else {
                            Player_1.setImage(assets.image`Player facing backward`)
                        }
                        Cutscene = false
                        attacking = false
                    })
                    attack()
                } else {
                    animation.runImageAnimation(
                    Player_1,
                    assets.animation`Attack Common Sword Left`,
                    100,
                    false
                    )
                    timer.after(300, function () {
                        if (playerstill) {
                            if (lastdirection) {
                                animation.runImageAnimation(
                                Player_1,
                                assets.animation`Run forward animation`,
                                75,
                                true
                                )
                            } else {
                                animation.runImageAnimation(
                                Player_1,
                                assets.animation`Run Backward animation`,
                                75,
                                true
                                )
                            }
                        } else if (lastdirection) {
                            Player_1.setImage(assets.image`Player Facing Right`)
                        } else {
                            Player_1.setImage(assets.image`Player facing backward`)
                        }
                        Cutscene = false
                        attacking = false
                    })
                    attack()
                }
            })
        }
    }
})
game.onUpdate(function () {
    if (Cutscene == false) {
        if (controller.A.isPressed()) {
            if (Dash_Unlocked) {
                timer.throttle("dash", 3000, function () {
                    dash()
                })
            }
        }
    }
})
game.onUpdate(function () {
    if (Screen == 3) {
        if (Math.floor(Player_1.tilemapLocation().column) == 29) {
            if (Math.floor(Player_1.tilemapLocation().row) > 25) {
                tiles.setTileAt(tiles.getTileLocation(28, 25), sprites.dungeon.floorDark2)
                tiles.setTileAt(tiles.getTileLocation(28, 26), sprites.dungeon.floorDark2)
                tiles.setTileAt(tiles.getTileLocation(28, 27), sprites.dungeon.floorDark2)
                tiles.setTileAt(tiles.getTileLocation(28, 28), sprites.dungeon.floorDark2)
                tiles.setWallAt(tiles.getTileLocation(28, 25), true)
                tiles.setWallAt(tiles.getTileLocation(28, 26), true)
                tiles.setWallAt(tiles.getTileLocation(28, 27), true)
                tiles.setWallAt(tiles.getTileLocation(28, 28), true)
                sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
                timer.throttle("action", 1000000000, function () {
                    shot = sprites.create(assets.image`Boss Shot Image`, SpriteKind.Boss_Projectile)
                    if (randint(0, 1) == 0) {
                        tiles.placeOnTile(shot, tiles.getTileLocation(50, 28))
                    } else {
                        tiles.placeOnTile(shot, tiles.getTileLocation(50, 26))
                    }
                    shot.vx = -135
                })
                BossFightStage = 1
            }
        }
        if (Math.floor(Player_1.tilemapLocation().column) == 47) {
            sprites.destroyAllSpritesOfKind(SpriteKind.Boss_Projectile)
            BossFightStage = 2
        }
        if (Math.floor(Player_1.tilemapLocation().column) == 48) {
            tiles.setTileAt(tiles.getTileLocation(47, 25), sprites.dungeon.floorDark2)
            tiles.setTileAt(tiles.getTileLocation(47, 26), sprites.dungeon.floorDark2)
            tiles.setTileAt(tiles.getTileLocation(47, 27), sprites.dungeon.floorDark2)
            tiles.setTileAt(tiles.getTileLocation(47, 28), sprites.dungeon.floorDark2)
            tiles.setWallAt(tiles.getTileLocation(47, 25), true)
            tiles.setWallAt(tiles.getTileLocation(47, 26), true)
            tiles.setWallAt(tiles.getTileLocation(47, 27), true)
            tiles.setWallAt(tiles.getTileLocation(47, 28), true)
            sprites.destroyAllSpritesOfKind(SpriteKind.Boss_Projectile)
        }
    }
})
game.onUpdate(function () {
    for (let value222 of sprites.allOfKind(SpriteKind.Boss_Projectile)) {
        if (value222.tilemapLocation().column == 29) {
            value222.destroy()
        }
    }
})
game.onUpdate(function () {
    if (BossFightStage == 2) {
        SpawnHarambe()
        animation.runImageAnimation(
        Harambe,
        assets.animation`myAnim`,
        100,
        true
        )
    }
})
game.onUpdate(function () {
    if (BossFightStage == 3) {
        for (let value223 of sprites.allOfKind(SpriteKind.Boss_Projectile)) {
            if (value223.tilemapLocation().column == 48) {
                value223.destroy()
            } else if (value223.tilemapLocation().column == 63) {
                value223.destroy()
            }
        }
    }
})
game.onUpdate(function () {
    if (BossFightStage == 3) {
        timer.after(1500, function () {
            if (sprites.allOfKind(SpriteKind.Level_1_Boss).length == 0) {
                BossFightStage += 1
            }
        })
    }
})
game.onUpdate(function () {
    if (Cutscene == false) {
        if (Player_1.vx < 0) {
            playerstill = false
            lastdirection = false
        }
        if (Player_1.vx > 0) {
            playerstill = false
            lastdirection = true
        }
        if (Player_1.vx == 0) {
            playerstill = true
        }
        if (controller.right.isPressed()) {
            if (dashing == false) {
                if (attacking == false) {
                    if (downdash == false) {
                        timer.throttle("move", 300, function () {
                            animation.runImageAnimation(
                            Player_1,
                            assets.animation`Run forward animation`,
                            75,
                            true
                            )
                        })
                    }
                }
            }
        } else if (controller.left.isPressed()) {
            if (dashing == false) {
                if (attacking == false) {
                    if (downdash == false) {
                        timer.throttle("move", 300, function () {
                            animation.runImageAnimation(
                            Player_1,
                            assets.animation`Run Backward animation`,
                            75,
                            true
                            )
                        })
                    }
                }
            }
        } else if (lastdirection) {
            if (attacking == false) {
                if (dashing == false) {
                    Player_1.setImage(assets.image`Player Facing Right`)
                }
            }
        } else if (attacking == false) {
            if (dashing == false) {
                Player_1.setImage(assets.image`Player facing backward`)
            }
        } else {
        	
        }
    }
    if (dashing) {
        if (downdash == false) {
            if (lastdirection) {
                Player_1.setImage(assets.image`Dash right`)
            } else {
                Player_1.setImage(assets.image`Dashleft`)
            }
        }
    }
})
game.onUpdate(function () {
    if (BossFightStage == 4) {
        End_Portal2 = sprites.create(assets.image`End Portal Sprite`, SpriteKind.End_Portal)
        tiles.placeOnTile(End_Portal2, tiles.getTileLocation(63, 28))
    }
})
game.onUpdateInterval(randint(750, 1250), function () {
    for (let value322 of sprites.allOfKind(SpriteKind.Enemy)) {
        if (randint(1, 6) != 6) {
            if (Playerwamoushindeiru == false) {
                if (enemywamoushindeiru == false) {
                    if (Player_1.tilemapLocation().column > value322.tilemapLocation().column) {
                        value322.setImage(assets.image`Monkey Facing Right`)
                    } else {
                        value322.setImage(assets.image`Monkey Facing Left`)
                    }
                    if (Player_1.tilemapLocation().column > value322.tilemapLocation().column) {
                        animation.runImageAnimation(
                        value322,
                        assets.animation`Monkey Shoot Left0`,
                        50,
                        false
                        )
                        timer.after(300, function () {
                            EnemyShot(value322)
                            value322.setImage(assets.image`Monkey Facing Right`)
                        })
                    } else {
                        animation.runImageAnimation(
                        value322,
                        assets.animation`Monkey Shoot Left`,
                        50,
                        false
                        )
                        timer.after(300, function () {
                            EnemyShot(value322)
                            value322.setImage(assets.image`Monkey Facing Left`)
                        })
                    }
                }
            }
        }
    }
})
game.onUpdateInterval(1500, function () {
    if (BossFightStage == 1) {
        shot = sprites.create(assets.image`Boss Shot Image`, SpriteKind.Boss_Projectile)
        if (randint(0, 1) == 0) {
            tiles.placeOnTile(shot, tiles.getTileLocation(55, 28))
        } else {
            tiles.placeOnTile(shot, tiles.getTileLocation(55, 26))
        }
        shot.vx = -135
    }
    if (BossFightStage == 2) {
        Harambe_jump()
    }
    if (BossFightStage == 3) {
        Spawn_mini_Harambe()
        if (Harambewamoushindeiru == false) {
            Mini_Harambe_shots()
        }
    }
})
