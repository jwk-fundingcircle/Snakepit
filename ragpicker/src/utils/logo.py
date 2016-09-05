#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright (C) 2013-2015 Ragpicker Developers.
# This file is part of Ragpicker Malware Crawler - http://code.google.com/p/malware-crawler/

import sys
import os
import random

def color(text, color_code):
    """Colorize text.
    @param text: text.
    @param color_code: color.
    @return: colorized text.
    """
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text
    return "\x1b[%dm%s\x1b[0m" % (color_code, text)

def logo():
    logos = []

    logos.append("""
                           k            
                   ii      k k          
  rrr  aa ggg ppp      ccc kk   eee rrr 
  r   a a g g p  p ii c    k k  e e r   
  r   aaa ggg ppp  ii  ccc k  k ee  r   
            g p                         
          ggg p              """)           



    logos.append("""
         _           _                   _              _        _           _             _              _            _      
        /\ \        / /\                /\ \           /\ \     /\ \       /\ \           /\_\           /\ \         /\ \    
       /  \ \      / /  \              /  \ \         /  \ \    \ \ \     /  \ \         / / /  _       /  \ \       /  \ \   
      / /\ \ \    / / /\ \            / /\ \_\       / /\ \ \   /\ \_\   / /\ \ \       / / /  /\_\    / /\ \ \     / /\ \ \  
     / / /\ \_\  / / /\ \ \          / / /\/_/      / / /\ \_\ / /\/_/  / / /\ \ \     / / /__/ / /   / / /\ \_\   / / /\ \_\ 
    / / /_/ / / / / /  \ \ \        / / / ______   / / /_/ / // / /    / / /  \ \_\   / /\_____/ /   / /_/_ \/_/  / / /_/ / / 
   / / /__\/ / / / /___/ /\ \      / / / /\_____\ / / /__\/ // / /    / / /    \/_/  / /\_______/   / /____/\    / / /__\/ /  
  / / /_____/ / / /_____/ /\ \    / / /  \/____ // / /_____// / /    / / /          / / /\ \ \     / /\____\/   / / /_____/   
 / / /\ \ \  / /_________/\ \ \  / / /_____/ / // / /   ___/ / /__  / / /________  / / /  \ \ \   / / /______  / / /\ \ \     
/ / /  \ \ \/ / /_       __\ \_\/ / /______\/ // / /   /\__\/_/___\/ / /_________\/ / /    \ \ \ / / /_______\/ / /  \ \ \    
\/_/    \_\/\_\___\     /____/_/\/___________/ \/_/    \/_________/\/____________/\/_/      \_\_\\/__________/\/_/    \_\/""")
    
    logos.append("""
 _  .-')     ('-.                  _ (`-.                   .-. .-')     ('-.  _  .-')   
( \( -O )   ( OO ).-.             ( (OO  )                  \  ( OO )  _(  OO)( \( -O )  
 ,------.   / . --. /  ,----.    _.`     \ ,-.-')   .-----. ,--. ,--. (,------.,------.  
 |   /`. '  | \-.  \  '  .-./-')(__...--'' |  |OO) '  .--./ |  .'   /  |  .---'|   /`. ' 
 |  /  | |.-'-'  |  | |  |_( O- )|  /  | | |  |  \ |  |('-. |      /,  |  |    |  /  | | 
 |  |_.' | \| |_.'  | |  | .--, \|  |_.' | |  |(_//_) |OO  )|     ' _)(|  '--. |  |_.' | 
 |  .  '.'  |  .-.  |(|  | '. (_/|  .___.',|  |_.'||  |`-'| |  .   \   |  .--' |  .  '.' 
 |  |\  \   |  | |  | |  '--'  | |  |    (_|  |  (_'  '--'\ |  |\   \  |  `---.|  |\  \  
 `--' '--'  `--' `--'  `------'  `--'      `--'     `-----' `--' '--'  `------'`--' '--'""")

    logos.append("""
         _           _                   _              _        _           _             _              _            _      
        /\ \        / /\                /\ \           /\ \     /\ \       /\ \           /\_\           /\ \         /\ \    
       /  \ \      / /  \              /  \ \         /  \ \    \ \ \     /  \ \         / / /  _       /  \ \       /  \ \   
      / /\ \ \    / / /\ \            / /\ \_\       / /\ \ \   /\ \_\   / /\ \ \       / / /  /\_\    / /\ \ \     / /\ \ \  
     / / /\ \_\  / / /\ \ \          / / /\/_/      / / /\ \_\ / /\/_/  / / /\ \ \     / / /__/ / /   / / /\ \_\   / / /\ \_\ 
    / / /_/ / / / / /  \ \ \        / / / ______   / / /_/ / // / /    / / /  \ \_\   / /\_____/ /   / /_/_ \/_/  / / /_/ / / 
   / / /__\/ / / / /___/ /\ \      / / / /\_____\ / / /__\/ // / /    / / /    \/_/  / /\_______/   / /____/\    / / /__\/ /  
  / / /_____/ / / /_____/ /\ \    / / /  \/____ // / /_____// / /    / / /          / / /\ \ \     / /\____\/   / / /_____/   
 / / /\ \ \  / /_________/\ \ \  / / /_____/ / // / /   ___/ / /__  / / /________  / / /  \ \ \   / / /______  / / /\ \ \     
/ / /  \ \ \/ / /_       __\ \_\/ / /______\/ // / /   /\__\/_/___\/ / /_________\/ / /    \ \ \ / / /_______\/ / /  \ \ \    
\/_/    \_\/\_\___\     /____/_/\/___________/ \/_/    \/_________/\/____________/\/_/      \_\_\\/__________/\/_/    \_\/""")
    
    logos.append("""
                                                             ______                                                          _____                    
___________          _____                _____        _____|\     \   ____________         _____   ______   _______    _____\    \ ___________       
\          \       /      |_         _____\    \_     /     / |     | /            \   _____\    \_|\     \  \      \  /    / |    |\          \      
 \    /\    \     /         \       /     /|     |   |      |/     /||\___/\  \\___/| /     /|     |\\     \  |     /|/    /  /___/| \    /\    \     
  |   \_\    |   |     /\    \     /     / /____/|   |      |\____/ | \|____\  \___|//     / /____/| \|     |/     //|    |__ |___|/  |   \_\    |    
  |      ___/    |    |  |    \   |     | |_____|/   |\     \    | /        |  |    |     | |____|/   |     |_____// |       \        |      ___/     
  |      \  ____ |     \/      \  |     | |_________ | \     \___|/    __  /   / __ |     |  _____    |     |\     \ |     __/ __     |      \  ____  
 /     /\ \/    \|\      /\     \ |\     \|\        \|  \     \       /  \/   /_/  ||\     \|\    \  /     /|\|     ||\    \  /  \   /     /\ \/    \ 
/_____/ |\______|| \_____\ \_____\| \_____\|    |\__/|\  \_____\     |____________/|| \_____\|    | /_____/ |/_____/|| \____\/    | /_____/ |\______| 
|     | | |     || |     | |     || |     /____/| | || \ |     |     |           | /| |     /____/||     | / |    | || |    |____/| |     | | |     | 
|_____|/ \|_____| \|_____|\|_____| \|_____|     |\|_|/  \|_____|     |___________|/  \|_____|    |||_____|/  |____|/  \|____|   | | |_____|/ \|_____| 
                                          |____/                                            |____|/                         |___|/""")
    
    logos.append("""
'########:::::'###:::::'######:::'########::'####::'######::'##:::'##:'########:'########::
 ##.... ##:::'## ##:::'##... ##:: ##.... ##:. ##::'##... ##: ##::'##:: ##.....:: ##.... ##:
 ##:::: ##::'##:. ##:: ##:::..::: ##:::: ##:: ##:: ##:::..:: ##:'##::: ##::::::: ##:::: ##:
 ########::'##:::. ##: ##::'####: ########::: ##:: ##::::::: #####:::: ######::: ########::
 ##.. ##::: #########: ##::: ##:: ##.....:::: ##:: ##::::::: ##. ##::: ##...:::: ##.. ##:::
 ##::. ##:: ##.... ##: ##::: ##:: ##::::::::: ##:: ##::: ##: ##:. ##:: ##::::::: ##::. ##::
 ##:::. ##: ##:::: ##:. ######::: ##::::::::'####:. ######:: ##::. ##: ########: ##:::. ##:
..:::::..::..:::::..:::......::::..:::::::::....:::......:::..::::..::........::..:::::..::""")
    
    logos.append("""
   _     _      _     _      _     _      _     _      _     _      _     _      _     _      _     _      _     _   
  (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)    (c).-.(c)  
   / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \      / ._. \   
 __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__  __\( Y )/__ 
(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)(_.-/'-'\-._)
   || R ||      || A ||      || G ||      || P ||      || I ||      || C ||      || K ||      || E ||      || R ||   
 _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._  _.' `-' '._ 
(.-./`-`\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-'\.-.)(.-./`-`\.-.)
 `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'  `-'     `-'""")
    
    logos.append("""                                                                                                                        
8 888888888o.            .8.           ,o888888o.    8 888888888o    8 8888     ,o888888o.    8 8888     ,88' 8 8888888888   8 888888888o.   
8 8888    `88.          .888.         8888     `88.  8 8888    `88.  8 8888    8888     `88.  8 8888    ,88'  8 8888         8 8888    `88.  
8 8888     `88         :88888.     ,8 8888       `8. 8 8888     `88  8 8888 ,8 8888       `8. 8 8888   ,88'   8 8888         8 8888     `88  
8 8888     ,88        . `88888.    88 8888           8 8888     ,88  8 8888 88 8888           8 8888  ,88'    8 8888         8 8888     ,88  
8 8888.   ,88'       .8. `88888.   88 8888           8 8888.   ,88'  8 8888 88 8888           8 8888 ,88'     8 888888888888 8 8888.   ,88'  
8 888888888P'       .8`8. `88888.  88 8888           8 888888888P'   8 8888 88 8888           8 8888 88'      8 8888         8 888888888P'   
8 8888`8b          .8' `8. `88888. 88 8888   8888888 8 8888          8 8888 88 8888           8 888888<       8 8888         8 8888`8b       
8 8888 `8b.       .8'   `8. `88888.`8 8888       .8' 8 8888          8 8888 `8 8888       .8' 8 8888 `Y8.     8 8888         8 8888 `8b.     
8 8888   `8b.    .888888888. `88888.  8888     ,88'  8 8888          8 8888    8888     ,88'  8 8888   `Y8.   8 8888         8 8888   `8b.   
8 8888     `88. .8'       `8. `88888.  `8888888P'    8 8888          8 8888     `8888888P'    8 8888     `Y8. 8 888888888888 8 8888     `88.""")
    
    logos.append("""
                                                      .                    ..                              
                                                     @88>            < .z@8"`                              
   .u    .                            .d``           %8P              !@88E                      .u    .   
 .d88B :@8c        u          uL      @8Ne.   .u      .          .    '888E   u         .u     .d88B :@8c  
="8888f8888r    us888u.   .ue888Nc..  %8888:u@88N   .@88u   .udR88N    888E u@8NL    ud8888.  ="8888f8888r 
  4888>'88"  .@88 "8888" d88E`"888E`   `888I  888. ''888E` <888'888k   888E`"88*"  :888'8888.   4888>'88"  
  4888> '    9888  9888  888E  888E     888I  888I   888E  9888 'Y"    888E .dN.   d888 '88%"   4888> '    
  4888>      9888  9888  888E  888E     888I  888I   888E  9888        888E~8888   8888.+"      4888>      
 .d888L .+   9888  9888  888E  888E   uW888L  888'   888E  9888        888E '888&  8888L       .d888L .+   
 ^"8888*"    9888  9888  888& .888E  '*88888Nu88P    888&  ?8888u../   888E  9888. '8888c. .+  ^"8888*"    
    "Y"      "888*""888" *888" 888&  ~ '88888F`      R888"  "8888P'  '"888*" 4888"  "88888%       "Y"      
              ^Y"   ^Y'   `"   "888E    888 ^         ""      "P'       ""    ""      "YP'                 
                         .dWi   `88E    *8E                                                                
                         4888~  J8%     '8>                                                                
                          ^"===*"`       "                                                                 
""")
    
    logos.append("""    
                                            _/            _/                            
   _/  _/_/    _/_/_/    _/_/_/  _/_/_/          _/_/_/  _/  _/      _/_/    _/  _/_/   
  _/_/      _/    _/  _/    _/  _/    _/  _/  _/        _/_/      _/_/_/_/  _/_/        
 _/        _/    _/  _/    _/  _/    _/  _/  _/        _/  _/    _/        _/           
_/          _/_/_/    _/_/_/  _/_/_/    _/    _/_/_/  _/    _/    _/_/_/  _/            
                         _/  _/                                                         
                    _/_/    _/                                                          """)
    
    logos.append("""
   .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
  | |  _______     | || |      __      | || |    ______    | || |   ______     | || |     _____    | || |     ______   | || |  ___  ____   | || |  _________   | || |  _______     | |
  | | |_   __ \    | || |     /  \     | || |  .' ___  |   | || |  |_   __ \   | || |    |_   _|   | || |   .' ___  |  | || | |_  ||_  _|  | || | |_   ___  |  | || | |_   __ \    | |
  | |   | |__) |   | || |    / /\ \    | || | / .'   \_|   | || |    | |__) |  | || |      | |     | || |  / .'   \_|  | || |   | |_/ /    | || |   | |_  \_|  | || |   | |__) |   | |
  | |   |  __ /    | || |   / ____ \   | || | | |    ____  | || |    |  ___/   | || |      | |     | || |  | |         | || |   |  __'.    | || |   |  _|  _   | || |   |  __ /    | |
  | |  _| |  \ \_  | || | _/ /    \ \_ | || | \ `.___]  _| | || |   _| |_      | || |     _| |_    | || |  \ `.___.'\  | || |  _| |  \ \_  | || |  _| |___/ |  | || |  _| |  \ \_  | |
  | | |____| |___| | || ||____|  |____|| || |  `._____.'   | || |  |_____|     | || |    |_____|   | || |   `._____.'  | || | |____||____| | || | |_________|  | || | |____| |___| | |
  | |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")
    
    logos.append("""
  .------..------..------..------..------..------..------..------..------.
  |R.--. ||A.--. ||G.--. ||P.--. ||I.--. ||C.--. ||K.--. ||E.--. ||R.--. |
  | :(): || (\/) || :/\: || :/\: || (\/) || :/\: || :/\: || (\/) || :(): |
  | ()() || :\/: || :\/: || (__) || :\/: || :\/: || :\/: || :\/: || ()() |
  | '--'R|| '--'A|| '--'G|| '--'P|| '--'I|| '--'C|| '--'K|| '--'E|| '--'R|
  `------'`------'`------'`------'`------'`------'`------'`------'`------'
""")

    logos.append("""
     ____         _         ____     ____                     ____     _  __    U _____ u    ____     
  U |  _"\ u  U  /"\  u  U /"___|u U|  _"\ u      ___      U /"___|   |"|/ /    \| ___"|/ U |  _"\ u  
   \| |_) |/   \/ _ \/   \| |  _ / \| |_) |/     |_"_|     \| | u     | ' /      |  _|"    \| |_) |/  
    |  _ <     / ___ \    | |_| |   |  __/        | |       | |/__  U/| . \\u    | |___     |  _ <    
    |_| \_\   /_/   \_\    \____|   |_|         U/| |\u      \____|   |_|\_\     |_____|    |_| \_\   
    //   \\_   \\    >>    _)(|_    ||>>_    .-,_|___|_,-.  _// \\  ,-,>> \\,-.  <<   >>    //   \\_  
   (__)  (__) (__)  (__)  (__)__)  (__)__)    \_)-' '-(_/  (__)(__)  \.)   (_/  (__) (__)  (__)  (__) 
""")
    
    logos.append("""
       !!!         |                        #                 #   .      .                      ___           |"|           !!!      
    `  _ _  '      |.===.        __MMM__    #=ooO=========Ooo=# .  .:::.         ,,,,,         /\#/\         _|_|_       `  _ _  '   
   -  (OXO)  -     {}o o{}        (o o)     #  \\  (o o)  //  #   :(o o):  .    /(o o)\       /(o o)\        (o o)      -  (OXO)  -  
  ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo---------(_)--------ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-
""")
    print(color(random.choice(logos), random.randrange(31, 37)))
    print
    print(" Malware Crawler")
    print(" Robby Zeitfuchs")
    print(" Mark Lawrenz")
    print(" Copyright (c) 2013-2015")
    print
    sys.stdout.flush()
