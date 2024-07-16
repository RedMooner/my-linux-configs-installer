import enquiries
import subprocess
import getpass

username = getpass.getuser()
print ("Добро пожаловать в утилиту настройки конфигурации Linux (by Motyrev)")

packages = [
    'alacritty',
    'ranger',
    'tmux'
]
packages_config_files = [
    '/home/' + username + "/.config/alacritty/alacritty.yml",
    '',
    '~/.tmux.conf'
]

package_managers = [
    'dnf',
    'yum',
    'pacman',
    'apt'
]
package_managers_install_cmds = [
    'dnf install',
    'yum install',
    'apt install'
]
print("Доступные пакеты: " + str(packages));
selected_pm = enquiries.choose('Выберете пакетный менеджер: ', package_managers)

for i in range((package_managers.__len__()-1)):
    print("###Установка - 0" , packages[i] + "###")
    subprocess.call("sudo " + selected_pm + " install " + packages[i],shell=True)

print("---------------------------------------------------------")
print("Завершено!")
print("Настройка конфигурации установленного ПО")
print("Клонирование репозитория my-linux-configs")
subprocess.call("git clone https://github.com/RedMooner/my-linux-configs.git", shell=True)
print("---------------------------------------------------------")
print("Завершено!")
print("Применение конфигурационных файлов...")

print("alacritty: ")
subprocess.call("mkdir /home/" + username + "/.config/alacritty" ,shell=True)
subprocess.call("cat my-linux-configs/alacritty.yml > " + packages_config_files[0], shell=True)
print("Готово.")
