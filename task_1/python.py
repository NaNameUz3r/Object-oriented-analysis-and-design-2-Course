class Weapon:
    def __init__(self, weapon_name):
        self.weapon_name = weapon_name
        self.is_equiped = False

    def equip(self):
        self.is_equiped = True

    def unenquip(self):
        self.is_equiped = False

# Пример обычного наследования. Физическое оружие наследует метакласс Оружие
class PhysicalWeapon(Weapon):
    def __init__(self, weapon_name):
        super().__init__(weapon_name)
        self.physical_damage = None 
    
    def set_physical_damage(self, phys_damage):
        self.physical_damage = phys_damage

    def inflict_damage(self):
        print(f"Inflicting a physical damage equal to = {self.physical_damage} with {self.weapon_name}")

# Магическое оружие наследует метакласс Оружие, но тут мы видим метод с таким же именем. Это пример полиморфизма — в зависимости от создания конкретного 
# "обычного" экземпдляра оружия оно будет наносить физический или магический урон
class MagicalWeapon(Weapon):
    def __init__(self, weapon_name):
        super().__init__(weapon_name)
        self.magical_damage = None
    
    def set_magical_damage(self, magical_damage):
        self.magical_damage = magical_damage 

    def inflict_damage(self):
        print(f"Inflicting a magical damage equal to = {self.magical_damage} with {self.weapon_name}")


# Опишем ещё несколько классов, для демонстрации композиции чуть дальше. 
# Метакласс Магического эффекта, и несколько классов наследников — DoT, мгновенного маг. урона и мгновенного излечения.
# опять с применением полиморфизма для метода "trigger_magical_effect"
class MagicalEffect:
    def __init__(self, effect_name):
        self.effect_name = effect_name

class DamageOverTime(MagicalEffect):
    def __init__(self, effect_name, damage_amount):
        super().__init__(effect_name)
        self.DoT_per_second = damage_amount
    
    def trigger_magical_effect(self):
        print(f"Inflicting {self.effect_name} that deals {self.DoT_per_second} damage every second.")

class InstantMagicDamage(MagicalEffect):
    def __init__(self, effect_name, damage_amount):
        super().__init__(effect_name)
        self.instant_damage = damage_amount

    def trigger_magical_effect(self):
        print(f"Inflicting {self.effect_name} that deals {self.instant_damage} damage instantly.")

class InstantHealing(MagicalEffect):
    def __init__(self, effect_name, healing_amount):
        super().__init__(effect_name)
        self.instant_healing_amount = healing_amount

    def trigger_magical_effect(self):
        print(f"Healing self by {self.effect_name} that restores {self.instant_healing_amount} health points instantly.")


# Итак, соберем классическое overpowered легендарное оружие.
# Сперва пример множественного наследования. Зачарованное оружие наносит смешанный постоянный урон, поэтому насследуем оба класса — физическое и магическое оружие.
class EnchantedWeapon(PhysicalWeapon, MagicalWeapon):

    def __init__(self, weapon_name):
        super().__init__(weapon_name)

        # здесь мы применяем композицию. Оружие зачарованное, и помимо постоянного магического урона могут быть или не быть дополнительные эффекты
        self.magical_effects = []
    
    def add_enchant(self, effect_type, effect_name, infliction_amount):
        self.magical_effects.append(effect_type(effect_name, infliction_amount))

        
    # Уже знакомый нам "полиморфический метод" из обычного оружия, который вернет в данном случае смешанный константный урон задаваемый в родительских
    # классах, а так же вызовет срабатывание всех зачарований, если они есть. 
    def inflict_damage(self):
        print(f"Inflicting a mixed constant damage (physical + magical) equal to = {self.magical_damage + self.physical_damage} with {self.weapon_name}")
        if not len(self.magical_effects) < 1:
            print(f"With following magical effects of {self.weapon_name}:") 
            for effect in self.magical_effects:
                # как видим тут снова применяется молиморфизм, для срабатывания эффекта.
                effect.trigger_magical_effect()


rusty_sword = PhysicalWeapon("rusty_sword")
rusty_sword.set_physical_damage(1)
rusty_sword.inflict_damage()
# Выведет: 
# Inflicting a physical damage equal to = 1 with rusty_sword

magic_wand = MagicalWeapon("Potter Blunt")
magic_wand.set_magical_damage(6)
magic_wand.inflict_damage()
# Выведет:
# Inflicting a magical damage equal to = 6 with Potter Blunt


mace = EnchantedWeapon("Paladin Mace")
mace.set_physical_damage(5)
mace.set_magical_damage(5)
mace.add_enchant(DamageOverTime, "Holy Flame", 3)
mace.add_enchant(InstantMagicDamage, "Spark of Vigor", 15)
mace.add_enchant(InstantHealing, "Blessing of innocence", 2)
mace.inflict_damage()

# Выведет:
# Inflicting a mixed constant damage (physical + magical) equal to = 10 with Paladin Mace
# With following magical effects of Paladin Mace:
# Inflicting Holy Flame that deals 3 damage every second.
# Inflicting Spark of Vigor that deals 15 damage instantly.
# Healing self by Blessing of innocence that restores 2 health points instantly.

