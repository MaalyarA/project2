#main file
from project2_gui import *

def main() -> None:
    """
    Main function for GUI
    :return: None
    """
    window = Tk()
    window.geometry("400x400")
    window.title("Voting App")
    window.resizable(False, False,)
    MenuGUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
