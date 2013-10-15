#-*- coding: utf-8 -*-

import os
import time
from daemon import runner


# Função main
def main():
    notifier = Runner()
    daemon_runner = runner.DaemonRunner(notifier)
    daemon_runner.do_action()


# Função de notificação
def notification():
    os.system('notify-send \'1 hora de utilização\' \'Descansar.\'')


# Função de notificação de sucesso na ativação do notificador
def success():
    os.system('notify-send \'Notificador ativado\'')


class Runner():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/tmp/foo.pid'
        self.pidfile_timeout = 5

    def run(self):
        success()
        while(True):
            time.sleep(3600)
            notification()


if __name__ == '__main__':
    main()
