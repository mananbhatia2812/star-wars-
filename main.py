def on_b_pressed():
    global rocket
    scene.set_background_image(img("""
        ff88888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888887777778fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888887777778fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888887777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888887777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888887777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777778ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777778ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777778ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888887777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777778fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888777777777778ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888877777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888777777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888877777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888877777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888877777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888877777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888887777777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888877777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888887777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888777777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888887777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888877777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888887777788888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888887777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888887777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888887777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888877777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888877777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888777777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888777777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888887777777778888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888887777777778888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888887777777777888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888887777777777888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888877777777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888877777777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888877777777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888877777777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888877777777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888877777777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888877777777778888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888887777777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888887777777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888877777788888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888888888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888888887777788fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888887777778ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888888777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888887777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888887777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888877777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888887777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888888777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888887777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888887777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888877777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888887777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888877777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888887777777ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888777777fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                8888888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                88888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    """))
    effects.blizzard.start_screen_effect()
    info.set_life(3)
    info.set_score(0)
    rocket = sprites.create(img("""
            e e . . . . . . . . . . . . . . 
                    e e e . . . . . . . . . . . . . 
                    e e e e . . . . . . . . . . . . 
                    e e e f . . . . . . . . . . . . 
                    e e e f e . . . . . . . . . . . 
                    e e 2 f e c . . . . . . . . . . 
                    2 2 2 c 4 c e e . . . . . . . . 
                    2 2 4 c 4 c 4 e e f c f c c c c 
                    4 4 4 2 4 2 5 5 4 f 4 f b d d d 
                    4 4 4 2 5 2 2 2 . . . . . . . . 
                    4 4 4 f 2 2 . . . . . . . . . . 
                    4 5 5 f 2 . . . . . . . . . . . 
                    5 4 4 2 . . . . . . . . . . . . 
                    4 4 2 2 . . . . . . . . . . . . 
                    2 2 2 . . . . . . . . . . . . . 
                    2 2 . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    rocket.set_velocity(100, -8)
    controller.move_sprite(rocket)
    rocket.set_stay_in_screen(True)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global item
    item = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . 2 2 2 2 2 2 2 2 2 . . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . . . 2 2 2 2 2 2 2 2 2 . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        rocket,
        0,
        -8)
    item.set_velocity(100, -8)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_life_zero():
    game.over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap(sprite, otherSprite):
    myEnemy.destroy(effects.fire, 500)
    info.change_score_by(10)
    if info.score() == 1000:
        game.over(True)
        game.reset()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global rocket
    rocket.destroy(effects.disintegrate, 500)
    info.change_life_by(-1)
    info.change_score_by(-50)
    scene.camera_shake(15, 1000)
    if info.life() == 2:
        effects.blizzard.end_screen_effect()
        effects.star_field.start_screen_effect()
        rocket = sprites.create(img("""
                e e . . . . . . . . . . . . . . 
                            e e e . . . . . . . . . . . . . 
                            e e e e . . . . . . . . . . . . 
                            e e e f . . . . . . . . . . . . 
                            e e e f e . . . . . . . . . . . 
                            e e 2 f e c . . . . . . . . . . 
                            2 2 2 c 4 c e e . . . . . . . . 
                            2 2 4 c 4 c 4 e e f c f c c c c 
                            4 4 4 2 4 2 5 5 4 f 4 f b d d d 
                            4 4 4 2 5 2 2 2 . . . . . . . . 
                            4 4 4 f 2 2 . . . . . . . . . . 
                            4 5 5 f 2 . . . . . . . . . . . 
                            5 4 4 2 . . . . . . . . . . . . 
                            4 4 2 2 . . . . . . . . . . . . 
                            2 2 2 . . . . . . . . . . . . . 
                            2 2 . . . . . . . . . . . . . .
            """),
            SpriteKind.player)
        controller.move_sprite(rocket)
    if info.life() == 1:
        effects.star_field.end_screen_effect()
        effects.clouds.start_screen_effect()
        rocket = sprites.create(img("""
                e e . . . . . . . . . . . . . . 
                            e e e . . . . . . . . . . . . . 
                            e e e e . . . . . . . . . . . . 
                            e e e f . . . . . . . . . . . . 
                            e e e f e . . . . . . . . . . . 
                            e e 2 f e c . . . . . . . . . . 
                            2 2 2 c 4 c e e . . . . . . . . 
                            2 2 4 c 4 c 4 e e f c f c c c c 
                            4 4 4 2 4 2 5 5 4 f 4 f b d d d 
                            4 4 4 2 5 2 2 2 . . . . . . . . 
                            4 4 4 f 2 2 . . . . . . . . . . 
                            4 5 5 f 2 . . . . . . . . . . . 
                            5 4 4 2 . . . . . . . . . . . . 
                            4 4 2 2 . . . . . . . . . . . . 
                            2 2 2 . . . . . . . . . . . . . 
                            2 2 . . . . . . . . . . . . . .
            """),
            SpriteKind.player)
        controller.move_sprite(rocket)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

myEnemy: Sprite = None
item: Sprite = None
rocket: Sprite = None
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffff8888888888ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff88ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff8ffffffffffffffffff88ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999999fffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff8ffffffffffffffffffff888888888888888888888888fffffffffff55555555555fffffffffffffffffffffffff9fffff9fffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff8ffffffffffffffffffffffffffffffffffffffffffffffffffffff5555555555555ffffffffffffffffffffff99fffffff9ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff8ffffffffffffffffffffffffffffffff8fffffffffffffffffff55555555555555555ffffffffffffffffffff9ffffffff9ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff8ffffffffffffffffffffffffffffffff8ffffffffffffffffff5555555555555555555fffffffffffffffffff9ffffffff9ffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffff8fffffffffffffffffffffffffffffff8fffffffffffffffff555555555555555555555ffffffffffffffffff9ffffffff9ffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffff8fffffffffffffffffffffffffffffff8fffffffffffffffff555555555555555555555ffffffffffffffffff9ffffffff9ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffff88fffffffffffffffffffffffffffff8ffffffffffffffff55555555555555555555555fffffffffffffffff9ffffffff9ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffff88fffffffffffffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9ffffffff9ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffff88fffffffffffffffffffffffff8fffffffffffffff5555555555555555555555555fffffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffff88fffffffffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9fffffff9fffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffff888ffffffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9fffffff9fffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffff88ffffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9fffffff9fffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffff88fffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9fffffff9fffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff8fffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9ffffff9ffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff8ffffffffffffffffffffff8fffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9fffff9fffffffffffffffffffffffffffffffffffffffffff
        ffffffffffff88fffffffffffffffffffff8fffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9ffff99fffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffff88ffffffffffffffffff8ffffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9f999fffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffff88fffffffffffffff8fffffffffffffffffff8fffffffffffffff5555555555555555555555555ffffffffffffffff9ff9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffff88fffffffffff88ffffffffffffffffffff8ffffffffffffffff55555555555555555555555fffffffffffffffff9fff99ffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffff8888fffff88fffffffffffffffffffffff8ffffffffffffffff555555555555555555555ffffffffffffffffff9fffff9fffffffffffffff9fffffffffffffffffffffffffff
        ffffffffffffffffffffffff88888fffffffffffffffffffffffff8ffffffffffffffff555555555555555555555ffffffffffffffffff9ffffff9ffffffffffffff9fffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffff5555555555555555555fffffffffffffffffff9fffffff9ffffffffffff9ffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffffffffffffffff55555555555555555ffffffffffffffffffff9ffffffff9ffffffffff9fffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff8ffffffffffffffffffff5555555555555fffffffffffffffffffff9ffffffffff99ffffff99ffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffffffffffffff55555555555ffffffffffffffffffffff9ffffffffffff999999ffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffff9999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffff9ffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff9fffff9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffff9fffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffff9ffffffff9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff6666666666fffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffff9fffffffff9ffffffffffffffffffffff9ffffffffffffffffffffffffffffffffffffffffffffff6fffffffff666ffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffff9ffffff9999fffffffffffffffffffffffffffffffffff6fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffff9fffffff9fff99fffffffffffffff6666ffffffffffffff6fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffff9fffffff9fffff9fffffffffffff6ffff66ffffffffffff6fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffffff9fffffff9ffffff9fffffffffffffffffff6fffffffffff6fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffff9ffffffff9ffffff9fffffffffff6ffffffff6ffffffffff6fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9ffffffffffffffffff9fffffff9ffffffff9ffffffffff6fffffffff6fffffffff6fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffff9ffffffff9ffffffff9ffffffffff6fffffffff6fffffffff66ffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9fffff9fffffffffff9ffffffff9ffffffff9ffffffffff6fffffffff6fffffffffff6fffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9ffff99ffffffffff9ffffffff9fffffffff9ffffffffff6fffffffff6ffffffffffff66fffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9fff9ff9fffffffff9ffffffff9fffffffff9ffffffffff6fffffffff6ffffffffffffff6ffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9fff9fff9ffffffff9ffffffff9fffffffff9ffffffffff6fffffffff6fffffffffffffff666fffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9fff9fff9ffffffff9fffffff999999999999ffffffffff6ffffffff6fffffffffffffffffff666ffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9ff9ffff9ffffffff9fffffff9ffffffffff9fffffffff6ffffffff6fffffffffffffffffffffff66ffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9f9ffffff9ffffff9ffffffff9ffffffffff9fffffffff6ffffffff6ffffffffffffffffffffffff66fffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9f9ffffff9ffffff9ffffffff9ffffffffff9fffffffff6fffffff6ffffffffffffffffffffffffff66ffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99ffffffff9fffff9ffffffff9ffffffffff9fffffffff66666666fffffffffffffffff6ffffffffff6ffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99ffffffff9ffff9fffffffff9ffffffffff9fffffffff6f6ffffffffffffffffffffff66fffffffff6ffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9ffffffffff9fff9ffffffff9fffffffffff9fffffffff6ff666ffffffffffffffffffff66ffffff666ffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9fffffffffff9ff9ffffffff9fffffffffff9fffffffff6fffff6fffffffffffffffffffff6666666ffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9ffffffffffff9f9ffffffff9fffffffffff9fffffffff6ffffff6fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9f9fffffff9ffffffffffff9fffffffff6fffffff6ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99fffffff9ffffffffffff9fffffffff6ffffffff6fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99fffffff9ffffffffffff9fffffffff6fffffffff6ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99fffffff9fffffffffffffffffffffffffffffffff666fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9fffffffffffffffffffffffffffffffffff666fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222fffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22f2fffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22ff2fffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11fffffffffffff11fff1ffffffffff2fff2fffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11f1f111fff111ff1fff11ffffffffff2fff2fffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1f1f1ff1fffff1fff1fffffffffff22222fffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111f1f1ff1fffff111f11ffffffffff2fff22ffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11fff111fffff1ff111ffffffff2ffff2ffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff111ff1ffffffff1fff1ffffffff2ffff2ffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff1f11f1f111f11f1fff1ffffffff222f22ffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff1ff111ffffff11ff111ffffffffff222fffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
rocket_3 = sprites.create(img("""
        . . . . . . . . . . . . . . 8 8 
            . . . . . . . . . . . . . 8 8 8 
            . . . . . . . . . . . . 8 8 6 6 
            . . . . . . . . . . . . 8 6 6 9 
            . . . . . . . . . . . 8 f 9 9 6 
            . . . . . . . . . . 8 8 f 6 6 6 
            . . . . . . . . 8 8 8 9 e 6 6 6 
            d d d b f 6 f 6 9 9 8 6 e 6 6 6 
            c c c c f c f 8 8 6 c 6 c 6 8 8 
            . . . . . . . . 8 8 c 6 c 8 8 8 
            . . . . . . . . . . c 8 f 8 8 8 
            . . . . . . . . . . . 8 f 8 8 8 
            . . . . . . . . . . . . f 8 8 8 
            . . . . . . . . . . . . 8 8 8 8 
            . . . . . . . . . . . . . 8 8 8 
            . . . . . . . . . . . . . . 8 8
    """),
    SpriteKind.food)
_1 = sprites.create(img("""
        . . . . . . . . . . . . . . a a 
            . . . . . . . . . . . . . a a a 
            . . . . . . . . . . . . a a 3 3 
            . . . . . . . . . . . . a 3 3 1 
            . . . . . . . . . . . a f 1 1 3 
            . . . . . . . . . . a a f 3 3 3 
            . . . . . . . . a a a 1 a 3 3 3 
            d d d b f 3 f 3 1 1 a 3 a 3 3 3 
            c c c c f c f 8 8 3 c 3 c 3 a a 
            . . . . . . . . 8 8 c 3 c a a a 
            . . . . . . . . . . c 8 f a 8 8 
            . . . . . . . . . . . 8 f 8 8 8 
            . . . . . . . . . . . . f 8 8 8 
            . . . . . . . . . . . . 8 8 8 8 
            . . . . . . . . . . . . . 8 8 8 
            . . . . . . . . . . . . . . 8 8
    """),
    SpriteKind.food)
_2 = sprites.create(img("""
        . . . . . . . . . . . . . . 2 2 
            . . . . . . . . . . . . . 2 2 2 
            . . . . . . . . . . . . 2 2 4 4 
            . . . . . . . . . . . . 2 4 4 5 
            . . . . . . . . . . . 2 f 5 5 4 
            . . . . . . . . . . 2 2 f 4 4 4 
            . . . . . . . . 2 2 2 5 2 4 4 4 
            d d d b f 4 f 4 5 5 2 4 2 4 4 4 
            c c c c f c f e e 4 c 4 c 4 2 2 
            . . . . . . . . e e c 4 c 2 2 2 
            . . . . . . . . . . c e f 2 e e 
            . . . . . . . . . . . e f e e e 
            . . . . . . . . . . . . f e e e 
            . . . . . . . . . . . . e e e e 
            . . . . . . . . . . . . . e e e 
            . . . . . . . . . . . . . . e e
    """),
    SpriteKind.food)
_3 = sprites.create(img("""
        . . . . . . . . . . . . . . 7 7 
            . . . . . . . . . . . . . 7 7 7 
            . . . . . . . . . . . . 7 7 2 2 
            . . . . . . . . . . . . 7 2 2 4 
            . . . . . . . . . . . 7 f 4 4 2 
            . . . . . . . . . . e 7 f 2 2 7 
            . . . . . . . . 7 7 7 4 e 7 2 7 
            d d d b f 2 7 2 4 4 7 2 e 7 7 7 
            c c c c f c 7 e 7 7 c 2 c 7 7 e 
            . . . . . . . . e 7 c 2 c e e e 
            . . . . . . . . . . 7 7 f 7 7 c 
            . . . . . . . . . . . 7 7 c 7 c 
            . . . . . . . . . . . . f c c c 
            . . . . . . . . . . . . c 7 c c 
            . . . . . . . . . . . . . c 7 c 
            . . . . . . . . . . . . . . 7 7
    """),
    SpriteKind.food)
for index in range(4):
    rocket_3.set_velocity(100, -10)
    rocket_3.x = scene.screen_width()
    rocket_3.vx = -100
    rocket_3.y = randint(10, scene.screen_height() - -10)
for index2 in range(4):
    _1.set_velocity(100, -10)
    _1.x = scene.screen_width()
    _1.vx = -100
    _1.y = randint(10, scene.screen_height() - -15)
for index3 in range(4):
    _2.set_velocity(100, -10)
    _2.x = scene.screen_width()
    _2.vx = -120
    _2.y = randint(10, scene.screen_height() - -20)
for index4 in range(4):
    _3.set_velocity(100, -10)
    _3.x = scene.screen_width()
    _3.vx = -80
    _3.y = randint(10, scene.screen_height() - 5)

def on_update_interval():
    global myEnemy
    myEnemy = sprites.create(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f1111111df.......
                    ......fd1111111ddf......
                    ......fd111111dddf......
                    ......fd111ddddddf......
                    ......fd1dfbddddbf......
                    ......fbddfcdbbbcf......
                    .......f11111bbcf.......
                    .......f1b1fffff........
                    .......fbfc111bf........
                    ........ff1b1bff........
                    .........fbfbfff.f......
                    ..........ffffffff......
                    ............fffff.......
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.enemy)
    myEnemy.x = scene.screen_width()
    myEnemy.vx = -100
    myEnemy.y = randint(10, scene.screen_height() - -10)
    animation.run_image_animation(myEnemy,
        [img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f1111111df.......
                    ......fd1111111ddf......
                    ......fd111111dddf......
                    ......fd111ddddddf......
                    ......fd1dfbddddbf......
                    ......fbddfcdbbbcf......
                    .......f11111bbcf.......
                    .......f1b1fffff........
                    .......fbfc111bf........
                    ........ff1b1bff........
                    .........fbfbfff.f......
                    ..........ffffffff......
                    ............fffff.......
                    ........................
                    ........................
                    ........................
                    ........................
        """)],
        100,
        False)
game.on_update_interval(500, on_update_interval)
