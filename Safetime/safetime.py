#-*- coding: utf-8 -*-

import os
from datetime import date


def main():

    # get the date actual date
    today = date.today()

    hj = date(today.year, 10, 14)

    if today == hj:
        notification()


def notification():
    os.system(
        'notify-send \'Título da minha notificação\' \'Texto da minha pequena notificação\'')


if __name__ == '__main__':
    main()
