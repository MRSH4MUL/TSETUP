from os import system as Shimul
import sys
import time
Shimul('xdg-open https://facebook.com/groups/team.acs//')

def line():
    print("_________________________________________")

baner = """
\033[1;32m
 _____ ______________  ____   ___   __      _____ _____ _____ _   _______ 
|_   _|  ___| ___ \  \/  | | | \ \ / /     /  ___|  ___|_   _| | | | ___ \
  | | | |__ | |_/ / .  . | | | |\ V /______\ `--.| |__   | | | | | | |_/ /
  | | |  __||    /| |\/| | | | |/   \______|`--. \  __|  | | | | | |  __/ 
  | | | |___| |\ \| |  | | |_| / /^\ \     /\__/ / |___  | | | |_| | |    
  \_/ \____/\_| \_\_|  |_/\___/\/   \/     \____/\____/  \_/  \___/\_|    
\033[1;36m

 \033[1;91m┏━━━━━━━━━━━\033[1;93m┃━A━┃━B━┃\033[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 \033[1;91m┃ \033[1;92m┏━━━━━━━━━\033[1;91m┃━C━┃━D━┃\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ \033[1;91m1┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┏━━━━━━━\033[1;92m┃━E━┃━F━┃\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━┓ \033[1;92mH┃ \033[1;91m2┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] AUTHOR   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mMD Shimul         \033[1;93mA┃ \033[1;92mI┃ \033[1;91m3┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] TOOL     \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mTERMUX SET UP           \033[1;93mB┃ \033[1;92mJ┃ \033[1;91m4┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] TOOL FREE \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m04                     \033[1;93mC┃ \033[1;92mK┃ \033[1;91m5┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] STATUS   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mFREE                  \033[1;93mD┃ \033[1;92mK┃ \033[1;91m6┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] VERSION  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m4.4                    \033[1;93mE┃ \033[1;92mK┃ \033[1;91m7┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] SYSTEM   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mDATA & WIFI            \033[1;93mF┃ \033[1;92mL┃ \033[1;91m8┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] NETWORK  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m3G - 4G -5G            \033[1;93mG┃ \033[1;92mM┃ \033[1;91m9┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] FACEBOOK \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mMD Shimul    \033[1;93mH┃ \033[1;92mN┃ \033[1;91mA┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] GITHUB   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mMRSH4MUL        \033[1;93mI┃ \033[1;92mP┃ \033[1;91mB┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] WHATSAPP \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m+88019****         \033[1;93mJ┃ \033[1;92mQ┃ \033[1;91mC┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┗━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m┃━1━┃━2━┃\033[1;93m━━━━━━━┛ \033[1;92mR┃ \033[1;91mD┃
 \033[1;91m┃ \033[1;92m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;91m┃━3━┃━4━┃\033[1;92m━━━━━━━━━━┛ \033[1;91mE┃
 \033[1;91m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;93m┃━5━┃━6━┃\033[1;91m━━━━━━━━━━━━━┛
"""
def clear():
    Shimul('clear')
    print(baner)
    line()
    print('\x1b[1;37m[\x1b[38;5;46m+\x1b[1;37m] AUTHOR   : MD Shimul  ')
    print('\x1b[1;37m[\x1b[38;5;46m+\x1b[1;37m] GITHUB   : MRSH4MUL ')
    print('\x1b[1;37m[\x1b[38;5;46m+\x1b[1;37m] PROJECT  : TERMUX SETUP ')
    print('\x1b[1;37m[\x1b[38;5;46m+\x1b[1;37m] FACEBOOK : MD Shimul  ')
    line()


def basic():
    Shimul('apt update')
    Shimul('apt upgrade')
    Shimul('pkg install nano')
    Shimul('gem install lolcat')
    Shimul('pkg install ruby')
    Shimul('pip install requests')
    Shimul('pip install mechanize')
    Shimul('pip install bs4')
    Shimul('pip install features')
    Shimul('pip install futures')
    clear()
    print('YOUR TERMUX IS READY TO USE ')


def full():
    Shimul('apt update')
    Shimul('apt upgrade')
    Shimul('pkg install nano')
    Shimul('gem install lolcat')
    Shimul('pkg install ruby')
    Shimul('pip install requests')
    Shimul('pip install mechanize')
    Shimul('pip install bs4')
    Shimul('pip install features')
    Shimul('pip install futures')
    Shimul('pip2 install mechanize')
    Shimul('pip2 install requests')
    Shimul('pip2 install bs4')
    Shimul('pkg install python2')
    Shimul('apt install tmux')
    Shimul('pkg install curl')
    Shimul('pkg install toilet')
    Shimul('pkg install cowsay')
    Shimul('pkg install figlet')
    Shimul('pkg install awesomeshot')
    Shimul('pkg install inotify-tools')
    Shimul('pkg install clang')
    Shimul('pkg install bat')
    Shimul('pkg install imagemagick')
    Shimul('pkg install exa')
    Shimul('pkg install lf')
    Shimul('pkg install mpd')
    Shimul('pkg install neovim')
    Shimul('pkg install openssh')
    Shimul('pkg install neofetch')
    Shimul('pkg install termux-api')
    Shimul('pkg install tmux')
    Shimul('pkg install zsh')
    Shimul('pkg i -y git bc')
    clear()
    print('YOUR TERMUX IS READY TO USE')

def main():
	clear()
	print("(1) TERMUX BASIC SETUP")
	print("(2) TERMUX FULL SETUP")
	print("(3) CONTACT ADMIN")
	line()
	kingboss=input("(??) CHOICE : ")
	if kingboss in ['1','01']:
		basic()
	if kingboss in ['2','02']:
		full()
	else:
		main()
main()
