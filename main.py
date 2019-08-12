#import colorama
from colorama import init
from colorama import Fore, Style

#import main menu handler
from handler.mainMenuHandler import MainMenu
from inc import MainChecker

#initialize colorama
init()

def main():
    # try:
    #     __checker = MainChecker()
    #     #check API's
    #     __checker.getAPI()
    #     if __checker.getAPI() == False:
    #         __checker.checkAPIs() #recheck values
    #     else:
    #         #check internet connection
    #         __checker.getNet()
    #         if __checker.getNet() == False:
    #             __checker.checkNet() #recheck connection
    #         else:
    #             __track3r = MainMenu()
    #             return __track3r.getMain()
    # #catch other error
    # except Exception as err:
    #     print(Fore.RED + "\n\t\t  [!] Err! " + err)
    #     pass
    __tracker = MainMenu()
    return __tracker.getMain()
    

if __name__ == '__main__':
    print(Fore.YELLOW + "\n\t [i] Starting...")
    print(Fore.LIGHTYELLOW_EX + "\n\t [.] Checking requirements...")
    main()