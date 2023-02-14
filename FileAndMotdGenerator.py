import os
import tempfile
import shutil

Modpackname = input('Enter the Modpack name:')

# Creating here a Folder with the Modpackname and overwrites it when they have the same Name

dir_name = Modpackname

if(os.path.exists("C:\MotdList\ " + dir_name)):
    tmp = tempfile.mktemp(dir=os.path.dirname("C:\MotdList\ " + dir_name))
    shutil.move("C:\MotdList\ " + dir_name, tmp)
    shutil.rmtree(tmp)

os.makedirs("C:\MotdList\ " + dir_name)

# Creating here a .txt file where the motd code is inside

radio = "{radio}"

File = open('C:\MotdList\ 'f"{Modpackname}\custommotdlist.txt",'w+')
File.write("\n &7&l//- &6&l" + f"{Modpackname} &r&7&l-\\|&7{radio}&l&e ATM7S &7- &l&eNF &7- &l&eNFu &7- &l&eTekkit 2 &7{radio}")
File.write("\n &7&l//- &6&l" + f"{Modpackname} &r&7&l-\\|&7{radio}&l&e CU &7- &l&eCC &7- &l&eEE2E &7- &l&eDH - &l&eIEE - &l&eKP3 &7{radio}")
File.close()