namespace SpriteKind {
    export const Health = SpriteKind.create()
}
let catspeed = 0
let wavecount = 0
let ogscorevalue = 0
let powerup = false
let bulletfirerate = 0
let enemyaddvalue = 0
let enemyspeed = 0
let enemyactspeed = 0
let heartspawn = 0
let mySprite4: Sprite = null
sprites.onOverlap(SpriteKind.Player, SpriteKind.Health, function (sprite, otherSprite) {
	
})
forever(function () {
    let mySprite: Sprite = null
    controller.moveSprite(mySprite, catspeed, catspeed)
    if (info.score() == wavecount * ogscorevalue) {
        wavecount = 1 + wavecount
        ogscorevalue = ogscorevalue + 1
        powerup = true
        if (game.ask("A for firerate", "B for speed")) {
            if (powerup == true) {
                powerup = false
                bulletfirerate = bulletfirerate - 0.05
                mySprite.sayText("+firerate", 5000, false)
            }
        } else {
            if (powerup == true) {
                powerup = false
                catspeed = catspeed + 25
                mySprite.sayText("+speed", 5000, false)
            }
        }
    }
    if (info.score() == 10 * enemyaddvalue) {
        enemyaddvalue = enemyaddvalue + 1
        enemyspeed = enemyspeed - 50
        enemyactspeed = enemyactspeed + 5
        mySprite.sayText("difficulty increase!", 500, false)
    }
})
forever(function () {
    pause(5000)
    heartspawn = randint(1, 3)
    if (heartspawn == 3) {
        mySprite4 = sprites.create(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, SpriteKind.Health)
        mySprite4.setPosition(randint(10, 150), randint(10, 110))
    }
})
