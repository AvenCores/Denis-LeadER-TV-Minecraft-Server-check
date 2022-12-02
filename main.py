from mcstatus import JavaServer
from termcolor import colored
from os import system,name
from time import sleep

while True:
    server = JavaServer.lookup("play.leadertv.ru")
    status = server.status()
    query = server.query()
    system('cls' if name == 'nt' else 'clear')
    print(colored("Сервер - ", "red") + ("play.leadertv.ru\n") + colored("Версия - ", "cyan") + ("1.19.2\n"))
    print(colored(f"На сервере онлайн {status.players.online} игрока(ов)", "yellow"))
    print(colored(f"На сервере онлайн следующие игроки: {', '.join(query.players.names)}", "blue"))
    sleep(5)
