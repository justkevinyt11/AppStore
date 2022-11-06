import os
import PySimpleGUI as sg
import wget

layout = [
    [sg.Text("App Store", background_color='#2C2825')],
    [sg.Button("Minecraft", button_color='#343434'), sg.Button("Discord", button_color='#343434'), sg.Button("OBS", button_color='#343434'),
     sg.Button("Streamlabs", button_color='#343434'), sg.Button("Brave", button_color='#343434'), sg.Button("Winrar", button_color='#343434')],
    [sg.Button('Warzone', button_color='#343434'), sg.Button('Opera', button_color='#343434'), sg.Button('Greenshot', button_color='#343434'),
     sg.Button('Steam', button_color='#343434'), sg.Button('Resolve', button_color='#343434'), sg.Button('Lightworks', button_color='#343434')],
    [sg.Button("VLC", button_color='#343434'), sg.Button('Onix', button_color='#343434'), sg.Button('Notepad++', button_color='#343434'),
     sg.Button('Audacity', button_color='#343434'), sg.Button("Spotify", button_color='#343434'), sg.Button('Badlion', button_color='#343434')],
    [sg.Button('Lunar', button_color='#343434'), sg.Button('Vs Code', button_color='#343434')],
    [sg.Button("Exit", button_color='#343434')]
]
sg.theme('DarkAmber')
window = sg.Window(title="Project App Store", layout=layout, margins=(300, 200), element_justification='c')

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Minecraft":
        url = "https://launcher.mojang.com/download/MinecraftInstaller.exe"
        wget.download(url, 'MinecraftInstaller.exe')
        os.system('MinecraftInstaller.exe')
        print('Installer Opened')
    elif event == "Discord":
        url = "https://download1507.mediafire.com/hoaiye5dknng/zgd35748hngfqge/DiscordSetup.exe"
        wget.download(url, 'DiscordSetup.exe')
        os.system('DiscordSetup.exe')
        print('Installer Opened')
    elif event == "OBS":
        url = 'https://cdn-fastly.obsproject.com/downloads/OBS-Studio-28.0.3-Full-Installer-x64.exe'
        wget.download(url, 'OBS.exe')
        os.system('OBS.exe')
        print('Installer Opened')
    elif event == "Brave":
        url = 'https://laptop-updates.brave.com/latest/winx64'
        wget.download(url, 'Brave.exe')
        os.system('Brave.exe')
        print('Installer Opened')
    elif event == "Streamlabs":
        url = 'https://streamlabs.com/streamlabs-desktop/download?sdb=0'
        wget.download(url, 'Stream-Labs.exe')
        os.system('Stream-labs.exe')
        print('Installer Opened')
    elif event == "Winrar":
        url = 'https://www.rarlab.com/rar/winrar-x64-611.exe'
        wget.download(url, 'winrar.exe')
        os.system('winrar.exe')
        print('Installer Opened')
    elif event == "Warzone":
        sg.Popup('This is a large app, while downloading this app the app store will hang')
        url = 'https://www.battle.net/download/getInstallerForGame?os=win&gameProgram=CODMW&version=Live'
        wget.download(url, "Warzone.exe")
        os.system('Warzone.exe')
        print('Installer Opened')
    elif event == "Opera":
        url = 'https://net.geo.opera.com/opera_gx/stable/windows?utm_tryagain=yes&utm_source=PWNgames&utm_medium=pa&utm_campaign=PWN_US&edition=std-1&utm_content=3191_11000&utm_id=25495247d8974a2383b5d34927dc3a90&http_referrer=missing&utm_site=opera_com&&utm_lastpage=opera.com/'
        wget.download(url, 'operagx.exe')
        os.system('operagx.exe')
        print('Installer Opened')
    elif event == "Greenshot":
        url = 'https://github.com/greenshot/greenshot/releases/download/Greenshot-RELEASE-1.2.10.6/Greenshot-INSTALLER-1.2.10.6-RELEASE.exe'
        wget.download(url, "Greenshot.exe")
        os.system('Greenshot.exe')
        print('Installer Opened')
    elif event == "Steam":
        url = 'https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe'
        wget.download(url, 'Steam.exe')
        os.system('Steam.exe')
        print('Installer Opened')
    elif event == 'Resolve':
        sg.Popup('This is a large app, while downloading this app the app store will hang')
        url = 'https://sw.blackmagicdesign.com/DaVinciResolve/v18.0.4/DaVinci_Resolve_18.0.4_Windows.zip?Key-Pair-Id=APKAJTKA3ZJMJRQITVEA&Signature=BdbWvCoh7LlGRzd/duFXDSajMdvh+z/2M5BrS6MqjK9t9XDqm5vE3JZkw8TuGbUjaQVsfAbKc8G7uyPdccRpeUwxLqz/73Qb6A32ebRd6ToVmiS/zGAYwZ3mlusaIqubv+nS6WlrK2LhhOJ829HGJ1GTTDkOwaMVN75Yju8R2MG2zEQEgBiCJnMyuAUwC8dI3ZQMiJUCs+W3PugpK+8RQPSU0BnI/t33EzJQZoYFtRNSUxhZdzQAXSgYxSQg5+UwJNH1z+VxLme+QaW408n5Dtt//1d+xu1+hddS8+i1IWehHmR/DwWJjXLwTd3bTd5YkJbfS2Q3xcyViEC1IMMpmQ==&Expires=1665702078'
        wget.download(url, 'Resolve.exe')
        os.system('Resolve.exe')
        print('Installer Opened')
    elif event == "Lightworks":
        url = 'https://cdn.lwks.com/releases/2022.3/lightworks_2022.3_r137309_64bit_setup.exe'
        wget.download(url, 'lkws.exe')
        os.system('lkws.exe')
        print('Installer Opened')
    elif event == "VLC":
        sg.Popup('This is a large app, while downloading this app the app store will hang')
        url = 'https://mirror2.sandyriver.net/pub/software/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
        wget.download(url, 'VLC.exe')
        os.system('VLC.exe')
        print('Installer Opened')
    elif event == "Onix":
        os.system('powershell.exe $code = Invoke-RestMethod'
                  ' "https://raw.githubusercontent.com/bernarddesfosse/onixclientautoupdate/main/zLauncherInstallScript.ps1"; foreach($a in $code) {iex $a;}')
        print('Installer Opened')
    elif event == "Notepad++":
        url = 'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.6/npp.8.4.6.Installer.x64.exe'
        wget.download(url, 'notepadPlusPlus.exe')
        os.system('notepadPlusPlus.exe')
        print('Installer Opened')
    elif event == "Audacity":
        url = 'https://github.com/audacity/audacity/releases/download/Audacity-3.2.1/audacity-win-3.2.1-64bit.exe'
        wget.download(url, 'Audacity.exe')
        os.system('Audacity.exe')
        print('Installer Opened')
    elif event == "Spotify":
        url = 'https://download.scdn.co/SpotifySetup.exe'
        wget.download(url, 'SpotifySetup.exe')
        os.system('SpotifySetup.exe')
        print('Installer Opened')
    elif event == "Badlion":
        sg.Popup('This is a large app, while downloading this app the app store might hang')
        url = 'https://download940.mediafire.com/ctyl9gpthvig/xzk4xb87tt0136q/Badlion+Client+Setup+3.12.0.exe'
        wget.download(url, 'badlionSetup.exe')
        os.system('badlionSetup.exe')
    elif event == "Lunar":
        url = 'https://download1514.mediafire.com/4j3fxhr4ppqg/jdjgqaky0cjqh16/Lunar+Client+v2.14.0.exe'
        wget.download(url, 'LunarClient.exe')
        os.system('LunarClient.exe')
    elif event == "Vs Code":
        sg.Popup('This is a large app, while downloading this app the app store might hang')
        url = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user'
        wget.download(url, 'vscode.exe')
        os.system('vscode.exe')

window.close()
