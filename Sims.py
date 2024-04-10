import random


class Gun:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def shoot(self):
        damage = random.randint(10, 20)  # Random damage between 10 and 20
        print(f"You shoot the target with {self.name} for {damage} damage!")
        return damage


class Target:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage


def main():
    my_gun = Gun("Pistol", 20)
    target = Target("Bullseye", 100)

    while target.health > 0:
        print(f"Target Health: {target.health}")
        choice = input("Press 's' to shoot or 'q' to quit: ")
        if choice.lower() == 's':
            damage_dealt = my_gun.shoot()
            target.take_damage(damage_dealt)
            if target.health <= 0:
                print("Target destroyed!")
        elif choice.lower() == 'q':
            print("Quitting the game...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
