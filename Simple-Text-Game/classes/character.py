class Character:

    def __init__(self, **kwargs):
        self.stats = kwargs['stats']
        self.description = kwargs['description']

    def __str__(self):
        return self.description

    def show_stats(self):
        print(f"level:{self.stats['level']}\nHP:{self.stats['hp']}\nMP:{self.stats['mp']}\n"
              f"ATTACK:{self.stats['attack']}\nDEFENCE{self.stats['defence']}")


class Hero(Character):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inventory = kwargs['inventory']
        self.max_inventory = kwargs['max inventory']
        self.weapon = kwargs['weapon type']

    def __str__(self):
        return self.description

    def add_item(self, item):
        if len(self.inventory) < self.max_inventory:
            self.inventory.append(item)
        else:
            print("You cannot carry any more items!")

    def remove_item(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            print("Your backpack is empty!")

    def show_inventory(self):
        if len(self.inventory) > 0:
            print('----INVENTORY----')
            for item in self.inventory:
                print(item)
            print('-----------------')
        else:
            print("There's nothing in your backpack")


class Enemy(Character):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enemy_class = kwargs['class']

    def __str__(self):
        return self.description

    def show_stats(self):
        return f"level:{self.stats['level']}\nHP:{self.stats['hp']}\nMP:{self.stats['mp']}\n" \
               f"ATTACK:{self.stats['attack']}\nDEFENCE{self.stats['defence']}"
