from enum import Enum


class Fruit(str, Enum):
    # Синтаксис: имя = значение.
    APPLE = 110
    PEAR = 128
    PLUM = 256


for fr in Fruit:
    print(fr.upper())
