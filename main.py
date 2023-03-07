def on_a_pressed():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 5 5 . . . . . . . 
                    . . . . . . . 5 5 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    mySprite2.set_position(mySprite.x, mySprite.y)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def checkstate(bool2: bool):
    return randint(1, 2)

def on_on_overlap(sprite, otherSprite):
    mySprite3.destroy()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

mySprite3: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . b 5 5 b . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
            . . b 5 5 b 5 d 1 f 5 d 4 f . . 
            . . b d 5 5 b 1 f f 5 4 4 c . . 
            b b d b 5 5 5 d f b 4 4 4 4 b . 
            b d d c d 5 5 b 5 4 4 4 4 4 4 b 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
scene.set_background_color(11)
controller.move_sprite(mySprite)

def on_update_interval():
    global mySprite3
    mySprite3 = sprites.create(img("""
            e e e . . . . e e e . . . . 
                    c d d c . . c d d c . . . . 
                    c b d d f f d d b c . . . . 
                    c 3 b d d b d b 3 c . . . . 
                    f b 3 d d d d 3 b f . . . . 
                    e d d d d d d d d e . . . . 
                    e d f d d d d f d e . b f b 
                    f d d f d d f d d f . f d f 
                    f b d d b b d d 2 f . f d f 
                    . f 2 2 2 2 2 2 b b f f d f 
                    . f b d d d d d d b b d b f 
                    . f d d d d d b d d f f f . 
                    . f d f f f d f f d f . . . 
                    . f f . . f f . . f f . . .
        """),
        SpriteKind.enemy)
    mySprite3.follow(mySprite)
    mySprite3.set_position(0, 0)
game.on_update_interval(1000, on_update_interval)
