import random

class RunescapeTaskManager():
    def __init__(self) -> None:
        self.tm = []

    def task_manager(self):

        self.tm = [ 'Melee Training', 
            'Range', 
            'Magic', 
            'Prayer', 
            'Necro', 
            'Summoning', 
            'Farming', 
            'Herb', 
            'Craftin', 
            'Blacksmithing', 
            'Mining', 
            'Fishing', 
            'Ancient Magick', 
            'Curses'
            'Melee', 
        'Ranged', 
        'Magic', 
        'Necro', 
        'Ancient Magick', 
        'Curses'
        'Prayer', 
        'Summoning - farm it yourself', 
        'Farming', 
        'Herblore', 
        'Crafting - Farm it yourself', 
        'Blacksmithing', 
        'Mining', 
        'Fishing',
        'Barbarian Assault', 
                        'Barrows', 
                        'Burgh de Rott Ramble', 
                        'Castle Wars', 
                        'Clan Wars', 
                        'Conquest', 
                        'Dominion Tower', 
                        'Fist of Guthix', 
                        'Mage Arena', 
                        'Pest Control', 
                        'Soul Wars', 
                        'Temple Trekking', 
                        'TzHaar Fight Cave', 
                        'TzHaar Fight Pit',
                        'All Fired Up', 
                        'Blast Furnace', 
                        'Brimhaven Agility Arena', 
                        'Fishing Trawler', 
                        'Flash Powder Factory', 
                        'Gnome Ball', 
                        'Gnome Restaurant', 
                        'Great Orb Project', 
                        'Impetuous Impulses', 
                        'Mage Training Arena', 
                        'Pyramid Plunder', 
                        'Ranging minigame', 
                        'Sorceress\'s Garden', 
                        'Trouble Brewing', 
                        'Vinesweeper',
                        'Shades of Mort\'ton', 
                                    'Stealing Creation', 
                                    'Tai Bwo Wannai Cleanup',
                                    'Burthorpe Games Room', 
                    'Cabbage Facepunch Bonanza', 
                    'Rogue Trader',
                    'The Death of Chivalry',
                        'New Foundations (Full)',
                        'Rune Memories',
                        'Bringing Home the Bacon' ,
                        'Broken Home',
                        'Diamond in the Rough',
                        'Missing, Presumed Death' ,
                        'Once Upon a Time in Giinor',
                        'One Piercing Note',
                        'Rage and Bone minigame',
                        'Rune Mysteries',
                        'Stolen Hearts',
                        'Tower of Life',
                        'Biohazard',
                        'Call of teh Ancestors',
                        'Dwarf Cannon',
                        'Eagles\' Peak',
                        'Earnest the Chicken',
                        'Fur \'n Seek',
                        'Gertrude\'s Cat' ,
                        'Murder Mystery',
                        'Murder on the Border',
                        'Myths of the White Lan',
                        'Observatory Quest' ,
                        'Perils of Ice Mountain' ,
                        'Priest in Peril' ,
                        'Recruitment Drive' ,
                        'A Shadow over Ashdale' ,
                        'Sheep Herder' ,
                        'Shield of Arrav' ,
                        'The Tale of the Muspah' ,
                        'Violet is Blue Too' ,
                        'What\'s Mine is Yours' ,
                        'Buyers and Cellars' ,
                        'Chef\'s Assistant' ,
                        'Gunnar\'s Ground',
                        'Heartstealer',
                        'The Jack of Spades',
                        'Let Them Eat Pie' ,
                        'Nature Spirit' ,
                        'Once Upon a Slime',
                        'Plage City',
                        'Rune Mythos' ,
                        'Song from the Depths' ,
                        'A Soul\'s Bane' ,
                        'Swept Away',
                        'Wolf Whistle',
                        '80 Smithing - If Finished, Do It Again',
                        '80 Crafting',
                        '80 Divination',]
        task = []
        task.append(random.choice(self.tm))
        # random_choice = []

        print(random.choice(task))


    
    def runner(self):
        while True:
            options = input("Would you like to start your next adventure? Yes or No:  ").lower()
            if options == 'no':
                print("I thought you'd be more brave.")
                break
            else:
                print("Hope you like pain!")
                break
        self.task_manager()

tasker = RunescapeTaskManager()
tasker.runner()