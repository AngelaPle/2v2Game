import random
import math

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.max_health = health  # Per la barra della salute
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def deal_damage(self, target):
        damage = random.randint(self.attack // 2, self.attack)
        if random.random() < 0.1:  # 10% di probabilità di colpo critico
            damage = int(damage * 1.5)
            return damage, "critico"
        return damage, None

    def get_health_percentage(self):
        return self.health / self.max_health if self.max_health > 0 else 0

    def special_ability(self, target, output_callback):
        """Metodo per l'abilità speciale (da sovrascrivere nelle sottoclassi)"""
        return 0, ""

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150, 20)

    def special_ability(self, target, output_callback):
        fury_damage = int(self.attack * 1.2)
        target.take_damage(fury_damage)
        output_callback(f"{self.name} usa Furia! Infligge {fury_damage} danni aggiuntivi!")
        return fury_damage, "Furia"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15)
        self.mana = 50

    def special_ability(self, target, output_callback):
        if self.mana >= 20:
            self.mana -= 20
            fireball_damage = random.randint(25, 35)
            target.take_damage(fireball_damage)
            output_callback(f"{self.name} lancia Palla di Fuoco! Infligge {fireball_damage} danni.")
            return fireball_damage, "Palla di Fuoco"
        else:
            output_callback(f"{self.name} non ha abbastanza mana per lanciare Palla di Fuoco.")
            return 0, "Mana insufficiente"

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 120, 18)
        self.arrows = 10

    def special_ability(self, target, output_callback):
        if self.arrows > 0:
            self.arrows -= 1
            piercing_shot_damage = int(self.attack * 1.1) + 5
            target.take_damage(piercing_shot_damage)
            output_callback(f"{self.name} scaglia Tiro Perforante! Infligge {piercing_shot_damage} danni.")
            return piercing_shot_damage, "Tiro Perforante"
        else:
            output_callback(f"{self.name} non ha frecce per il Tiro Perforante.")
            return 0, "Senza frecce"

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, character):
        self.members.append(character)

    def alive_members(self):
        return [member for member in self.members if member.is_alive()]

    def random_alive_member(self):
        alive = self.alive_members()
        if alive:
            return random.choice(alive)
        return None

def battle(team1, team2, output_callback, delay_ms=500):
    output_callback(f"\n--- Battaglia Inizia! ---")
    output_callback(f"{team1.name}: {[c.name for c in team1.members]}")
    output_callback(f"{team2.name}: {[c.name for c in team2.members]}")
    output_callback("---")

    turn = 0
    while team1.alive_members() and team2.alive_members():
        turn += 1
        output_callback(f"\n--- Turno {turn} ---")

        attacker_team = team1 if turn % 2 == 1 else team2 # Alterna le squadre ad attaccare
        defender_team = team2 if attacker_team == team1 else team1

        attacker = attacker_team.random_alive_member()
        defender = defender_team.random_alive_member()

        if attacker and defender:
            # Azione di attacco base
            damage, crit = attacker.deal_damage(defender)
            attack_text = f"{attacker.name} attacca {defender.name} per {damage} danni."
            if crit:
                attack_text += " Colpo critico!"
            output_callback(attack_text)
            output_callback(f"Salute di {defender.name}: {defender.health}/{defender.max_health}")

            if not defender.is_alive():
                output_callback(f"{defender.name} è stato sconfitto!")
                if not defender_team.alive_members():
                    break # La battaglia finisce se una squadra è completamente sconfitta
                continue # Passa al prossimo turno

            # Probabilità di usare l'abilità speciale
            if random.random() < 0.3: # 30% di probabilità di usare l'abilità
                special_damage, special_text = attacker.special_ability(defender, output_callback)
                if special_text:
                    output_callback(f"{attacker.name} usa {special_text}.")
                    output_callback(f"Salute di {defender.name}: {defender.health}/{defender.max_health}")
                    if not defender.is_alive():
                        output_callback(f"{defender.name} è stato sconfitto!")
                        if not defender_team.alive_members():
                            break
                        continue

        else:
            break

    if team1.alive_members():
        output_callback(f"\n--- {team1.name} Ha Vinto! ---")
        return team1.name
    else:
        output_callback(f"\n--- {team2.name} Ha Vinto! ---")
        return team2.name

if __name__ == "__main__":
    team_a = Team("Team Alpha")
    team_a.add_member(Warrior("Grog"))
    team_a.add_member(Mage("Zaltar"))

    team_b = Team("Team Beta")
    team_b.add_member(Archer("Elara"))
    team_b.add_member(Character("Tank", 200, 10)) # Un personaggio base

    def console_output(text):
        print(text)

    winner = battle(team_a, team_b, console_output)
    print(f"Il vincitore finale è: {winner}")