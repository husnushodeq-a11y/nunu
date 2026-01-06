"""
This code is only made for educational and practice purposes. 
Author and Async Development are not responsible for misuse.

GhoSty OwO V4 Alpha Build
Stable Alpha Build Version: 011125.4.0.2

GitHub: https://github.com/WannaBeGhoSt
Discord: https://discord.gg/SyMJymrV8x
"""

import os as brutality_ghosty

brutality_ghosty.system("pip install -r requirements.txt")
brutality_ghosty.system(
    "sleep 2 && clear >/dev/null 2>&1 &"
    if brutality_ghosty.name == "posix"
    else "timeout /t 2 >nul 2>&1 && cls"
)

import json as ghostop
from colorama import Fore, Style, init
from core.utils import ghosty
from core.heart import ghosty_start_time, ghosty_commands_sent, ghosty_gems_used, running

print(
    f"""{Fore.BLUE}
           ▒▒                    ▒▒            ▒▒       ▒▒▒     ░░     ░░
        ▒▒▒▒▒▒▒   ▒▒▒     ▒▒▒▒ ▒▒▒▒▒▒▒▒        ▒▒▒▒     ▒▒▒▒   ░░░░   ░░░░░
      ▒▒▒▒████▒▒ ▒▒█▒▒  ▒▒▒█▒▒▒▒░█████▒        ▒█▒▒   ▒▒▒██▒   ░░█░░░░░█░░░
     ▒▒▒▒██░░██▒▒▒██▒▒ ▒▒░██▒░▒██░░░░█▒        ▒██▒▒ ▒▒██░▒▒  ░░█░░░░░█░░░
     ▒▒██░░░░██▒▒██▒▒▒ ▒░██▒▒██░░░░░░█▒        ▒▒█▒▒▒▒██▒▒▒   ░░█░░░░░█░░░
    ▒▒██░░█░░█▒▒▒█▒▒▒▒▒▒░█▒▒▒█░░░█░░██▒         ▒█▒▒▒██▒▒    ░░██░░░░██░░░░
    ▒▒█░░░░░░█▒▒█░░██░▒░█▒▒ ▒█░░░░░█▒▒▒         ▒░█▒██▒▒      ░███████████░░░
    ▒▒█░░░░██▒▒▒████████▒▒  ▒██░░███▒▒          ▒▒██░▒       ░░░░░░███░░░░░░
     ▒██████▒▒▒███▒▒▒██▒▒   ▒▒████▒▒▒            ▒█▒▒         ░░░░░██░░░░
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒              ▒▒▒          ░░░░░██░░░░░░ 
     ▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒               ▒▒▒          ░░░░██░░░░░░
               ▒▒   ▒▒        ▒▒                 ▒▒             ░░░░░░
               
               
                                                 Async Development Alpha Build Version: 011125.4.0.2{Style.RESET_ALL}"""
)

init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}\n\n > Made By GhoSty [Async Development]{Style.RESET_ALL}")

with open("config.json", "r") as config_file:
    config = ghostop.load(config_file)

ghostyopaf = config["TOKEN"]  
ghosty.run(ghostyopaf, bot=False)