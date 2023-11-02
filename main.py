from random import randint
DEFAULT_ATTACK = 5
DEFAULT_DEFENSE = 10

class Character():
    SPECIAL_SKILL = ''
    SPECIAL_BUFF =''
    RANGE_VALUE_DEF=(1,5)
    RANGE_VALUE_ATTACK = (1, 3)
    BRIEF_DESC_CHAR_CLASS = ''
    def __init__(self, name, bonus_atk=0) -> None:
        self.name = name
        self.atack = DEFAULT_ATTACK + (DEFAULT_ATTACK*bonus_atk)
        pass

    def attack(self) -> str:
        value_attack = self.atack + randint(*self.RANGE_VALUE_ATTACK)
        return (f"{self.name} causo {value_attack} de daño al enemigo")
    
    def defense(self) -> str:
        def_ = DEFAULT_DEFENSE - randint(*self.RANGE_VALUE_DEF)
        return f'{self.name} se ha defendido correctramente, anulando {def_} puntos de daño'

    def special(self) -> str:
        return (f'{self.name} ha utilixado la habilidad {self.SPECIAL_SKILL}\n'
                f'{self.name} {self.SPECIAL_BUFF}')
        pass

    def __str__(self):
        return (f"{self.__class__.__name__}: " 
                f"{self.BRIEF_DESC_CHAR_CLASS}")

class Warrior(Character):
    SPECIAL_SKILL = 'Charge'
    SPECIAL_BUFF = f'Ha cargado, inflingiendo 12 puntos de daño'
    BRIEF_DESC_CHAR_CLASS = 'un feroz luchador cuerpo a cuerpo. ''Fuerte, resiliente y valiente.'
    def __init__(self, name, bonus_atk=0.8) -> None:
        super().__init__(name, bonus_atk)

class Magician(Character):
    SPECIAL_SKILL = 'Fire Ball'
    SPECIAL_BUFF = 'Ha hecho 15 puntos de daño magico'
    BRIEF_DESC_CHAR_CLASS = 'un brillante luchador de largo alcance. ''Maestro de poderes mágicos.'
    def __init__(self, name, bonus_atk=0.3) -> None:
        super().__init__(name, bonus_atk)

class Healer(Character):
    SPECIAL_SKILL = 'Heal'
    SPECIAL_BUFF = 'Ha curado 10 puntos de salud'
    BRIEF_DESC_CHAR_CLASS = 'un poderoso chamán. ''Extrae fuerza de la naturaleza, la fe y los espíritus.'
    def __init__(self, name, bonus_atk=0.1) -> None:
        super().__init__(name, bonus_atk)



char = Warrior('Michael')

print(char.attack())
print(char.defense())
print(char.special())
print(char)
