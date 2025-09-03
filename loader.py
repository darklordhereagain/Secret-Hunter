import os
import sys
import time
import random
try:
    from colorama import init, Fore, Style
    init(autoreset=True)  # Initialize colorama for Windows
    USE_COLORAMA = True
except ImportError:
    USE_COLORAMA = False
    class Colors:
        GREEN = ''
        RED = ''
        RESET = ''
    Fore = Colors()
    Style = Colors()

# Platform-specific beep for Hollywood effect
def beep(frequency=800, duration=200):
    try:
        import winsound
        winsound.Beep(frequency, duration)
    except ImportError:
        print('\a', end='')  # Terminal bell as fallback

# Clear screen and set title
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_console_title(title):
    if os.name == 'nt':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)

# Hollywood-style ASCII art banner
HACKER_BANNER = f"""
{Fore.GREEN}{Style.BRIGHT}
    .-'''/.\ 
   (_.--'  | | == | o-._ .--..--. _.-o | || | ;--|`--: |. | | | ;_ .| |_____ | /| '|\\ //`----'\\\\ ////| | \\\\ / | | \\ /| |\\ / \\ / \\ / \\/ \\ / \\ | | || /\\ || || , . || dlK
    HACK THE PLANET!
    Secret Hunter v1.0 - Powered by One Man Code
{Style.RESET_ALL}
"""

# Fake scrolling code lines
def scroll_code_lines(num_lines=10):
    code_phrases = [
        "Initializing Gibson Supercomputer...",
        "Bypassing firewall... 0xFF00A4C3",
        "Decrypting neural net... ACCESS GRANTED",
        "Phreak mode engaged... Tone: 2600Hz",
        "Loading virus payload... Crash Override active",
        "Scanning for backdoors... 127.0.0.1:1337",
        "Matrix breach detected... Red pill engaged",
        "Uploading to mainframe... 99% complete",
        "Lord Nikon: Photographic memory scan...",
        "Acid Burn: pH levels nominal"
    ]
    for _ in range(num_lines):
        line = random.choice(code_phrases) + f" [{random.randint(0x0000, 0xFFFF):04X}]"
        print(f"{Fore.GREEN}{line}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.1)

# Animated loading bar
def loading_bar(progress, total=100, bar_length=40):
    filled = int(bar_length * progress // total)
    bar = '#' * filled + '-' * (bar_length - filled)
    percent = progress / total * 100
    print(f"\r{Fore.GREEN}[{bar}] {percent:.1f}% {Style.RESET_ALL}", end='')
    sys.stdout.flush()

# Hollywood-style loader function
def run_hacker_loader():
    clear_screen()
    set_console_title("HACK THE PLANET - Secret Hunter Loading...")
    
    # Beep intro
    for freq in [800, 1000, 800]:
        beep(freq, 150)
        time.sleep(0.2)
    
    # Display banner
    print(HACKER_BANNER)
    time.sleep(1)
    
    # Scroll fake code
    print(f"{Fore.GREEN}Initiating Secret Hunter boot sequence...{Style.RESET_ALL}")
    scroll_code_lines(15)
    time.sleep(1)
    
    # Animated loading bar
    print(f"{Fore.GREEN}Decrypting core modules...{Style.RESET_ALL}")
    for i in range(101):
        loading_bar(i)
        time.sleep(0.05)
    print()
    
    # Final beep and message
    beep(1200, 300)
    print(f"\n{Fore.GREEN}{Style.BRIGHT}LOADED! Access Granted. Hack the Planet!{Style.RESET_ALL}")
    time.sleep(2)

# Main function to load .pyd and run Secret Hunter
def main():
    try:
        # Run Hollywood-style loader
        run_hacker_loader()
        
        # Clear screen for Secret Hunter
        clear_screen()
        
        # Ensure .pyd directory is in sys.path
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        # Import and run the compiled module
        import Secret_Hunter
        Secret_Hunter.main_menu()
        
    except ImportError as e:
        print(f"{Fore.RED}Error: Failed to load Secret_Hunter.cp313-win_amd64.pyd - {str(e)}{Style.RESET_ALL}")
        print(f"{Fore.RED}Ensure Secret_Hunter.cp313-win_amd64.pyd is in {os.path.dirname(os.path.abspath(__file__))}{Style.RESET_ALL}")
        input(f"{Fore.RED}Press Enter to exit...{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Runtime error: {str(e)}{Style.RESET_ALL}")
        input(f"{Fore.RED}Press Enter to exit...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()