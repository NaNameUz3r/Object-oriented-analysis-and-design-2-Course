class PhysicalAttack():
    def __init__(self):
        self.base_damage = 10
        self.crit_chance = 21
        self.attack_speed = 5.6

    def make_attack(self):
        self._launch_attack(self._calc_damage())
        print("Hit with physical!")

    def _calc_damage(self) -> int:
        "calc base on attack type specs"
        pass

    def _launch_attack(self, damage_amount):
        pass

class EnchantedAttack(PhysicalAttack):
    def __init__(self):
        self.base_damage = 15
        self.crit_chance = 41
        self.attack_speed = 5.1
        self.enchanment_type = "fire"

    def make_attack(self):
        self._launch_attack(self._calc_damage())
        print(f"Hit with enchanted magic {self.enchanment_type} attack!")

    def _calc_damage(self) -> int:
        "calc base on attack type specs"
        pass

    def _launch_attack(self, damage_amount):
        pass

class LaunchAttack():
    def __init__(self):
        self._attack = None

    def set_attack_type(self, damage_type):
        self._attack = damage_type

    def engade_attack(self):
        self._attack.make_attack()
