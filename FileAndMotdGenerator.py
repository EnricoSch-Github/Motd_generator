import os
import tempfile
import shutil
import random

Modpackname = input('Enter the Modpack name:')

# Creating here a Folder with the Modpackname and overwrites it when they have the same Name

dir_name = Modpackname

if(os.path.exists("C:\MotdList\ " + dir_name)):
    tmp = tempfile.mktemp(dir=os.path.dirname("C:\MotdList\ " + dir_name))
    shutil.move("C:\MotdList\ " + dir_name, tmp)
    shutil.rmtree(tmp)

os.makedirs("C:\MotdList\ " + dir_name)

# Creating here an Arry with all Modpacknames / and create BString with 3 random Modpacks with the Motd Prefix and without duplication of the modpacks name

ModpackNames = ["Legend of the Eyes", "Better MC", "Encrpted", "Sky Vault Hunters", "Stoneblock 3", "RAD2", "Odyssey:Space - A New Beginning", "Tekkit 2", "FTB Interactions", 
"Nomifactory (GTCEu Port)", "Technological Journey", "Enigmatica 2:Expert - Extended", "MeatballCraft", "Divine Journey 2", "Project Ozone 3", "FTB Skyfactory 3", 
"GT New Horizons", "TerraFirmaPunk", "Regrowth"]

# 19 Modpacks
def CreateModpackNames():
    RandomPacks = random.sample(ModpackNames, 3)
    String =" &7&l&e ".join(map(str,RandomPacks))
    return " &7&l&e " + String


# Creating here a .txt file where the motd code is inside

File = open('C:\MotdList\ 'f"{Modpackname}\custommotdlist.txt",'w+')
for x in range(20):
    File.write("\n &7&l//- &6&l" + f"{Modpackname} &r&7&l-\\|"+ CreateModpackNames() +str(x))
File.close()

File = open('C:\MotdList\ 'f"{Modpackname}\customplayerlist.txt",'w+')
File.write("\n &6&k{radio}&r&f&l Valhalla MC Network &r&6&k{radio}&r")
File.write("\n &7==========================&r")
File.write("\n &7- &6&oDoes have discord integration :D")
File.write("\n &7- &9&oAlways chunkloaded (offline)")
File.write("\n &7- Free Cakes from Alp :3")
File.write("\n ")
File.write("\n &7==========================&r")
File.write("\n &l&oPlayers Online: {playercount}/{maxplayers}")
File.write("\n Difficulty: {difficulty}")
File.write("\n &8Minecraft Version: &8&l{mcversion}")
File.close()
