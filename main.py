import subprocess
import pyautogui


# teams auto joiner
def class_join ():
    subprocess.run("\"Microsoft Teams.lnk\"",
                   shell=True,
                   cwd="C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")
    while True:
        allteams = pyautogui.locateOnScreen("assets\\sss.png")
        if allteams != None:
            pyautogui.click(allteams)
            print("clicked allteams ")
            break
        else:
            print("not clicked all teams")
            continue

    while True:
        team = pyautogui.locateOnScreen("assets\\ssss.png")
        if team != None:
            pyautogui.click(team)
            print("clicked team")
            break
        else:
            print("not clicked team")
            continue

    while True:
        join1 = pyautogui.locateOnScreen("assets\\s.png")
        if join1 != None:
            pyautogui.click(join1)
            print("clicked join1")
            break
        else:
            print("not clicked join1")
            continue

    while True:
        join2 = pyautogui.locateOnScreen("assets\\ss.png")
        if join2 != None:
            pyautogui.click(join2)
            print("clicked join 2")
            break
        else:
            print("not clicked join 2 ")
            continue

class_join()