import os, sys, time

DOWNLOAD_LINK = "https://tinyurl.com/4tz6xz46"


def slow_print(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def banner():
    os.system("clear" if os.name != "nt" else "cls")
    slow_print("""
███╗   ██╗███████╗██╗  ██╗███████╗██████╗  █████╗ 
████╗  ██║██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗
██╔██╗ ██║█████╗   ╚███╔╝ █████╗  ██████╔╝███████║
██║╚██╗██║██╔══╝   ██╔██╗ ██╔══╝  ██╔══██╗██╔══██║
██║ ╚████║███████╗██╔╝ ██╗███████╗██║  ██║██║  ██║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
""", 0.002)
    slow_print("        Nexera Installer V.09\n", 0.05)


def fake_loading(text, blocks=25, delay=0.07):
    slow_print(text)
    for _ in range(blocks):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")


def install():
    banner()
    fake_loading("Initializing installation...")
    fake_loading("Checking system compatibility...")
    fake_loading("Preparing secure package...")
    fake_loading("Finalizing installation...")

    slow_print("[✓] Installation ready!", 0.04)
    slow_print("\nDownload Nexera from official link:\n", 0.04)
    slow_print(f"👉 {DOWNLOAD_LINK}\n", 0.04)
    slow_print("Open this link in your browser to download.", 0.04)

    input("\nPress Enter to return to menu...")


def instagram():
    banner()
    slow_print("Follow me on Instagram\n", 0.05)
    slow_print("👉 @nexera.exe ---------------------/", 0.05)
    input("\nPress Enter to return to menu...")


def menu():
    while True:
        banner()
        slow_print("1) Install Nexera", 0.03)
        slow_print("2) Follow me on Instagram", 0.03)
        slow_print("3) Exit\n", 0.03)

        choice = input("Select option ➜ ")
        if choice == "1":
            install()
        elif choice == "2":
            instagram()
        elif choice == "3":
            slow_print("Exiting Installer... 👋", 0.05)
            sys.exit()
        else:
            slow_print("Invalid option!", 0.05)
            time.sleep(1)


menu()