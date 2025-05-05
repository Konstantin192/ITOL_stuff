// class Character {
//     constructor(name, health, strength, hairColor, clothesColor, goldCoins) {
//         this.name = name;
//         this.health = health;
//         this.strength = strength;
//         this.hairColor = hairColor;
//         this.clothesColor = clothesColor;
//         this.goldCoins = goldCoins;
//     }
// }

// const player = new Character("HeMan", 100, 20, "yellow", "brown", 0);
// const enemy = new Character("Skeletor", 80, 15, "black", "purple", 100);

// console.log(player);
// console.log(enemy);
// console.log(player.name);


class Chest {
    constructor(isOpen, coins) {
        this.isOpen = isOpen;
        this.coins = coins;
    }

    openChest() {
        if (!this.isOpen) {
            this.isOpen = true;
            console.log(`Chest opened! Collected ${this.coins} coins!`);
            this.coins = 0;
        }
    }
}

const myChest = new Chest(false, 100);

myChest.openChest();

console.log(myChest.coins);