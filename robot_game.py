class Robot:
  def __init__(self, name, color_code):
      self.name = name
      self.color = color_code
      self.energy = 100
      self.parts = [
          Part("Head", attack_level = 5, defense_level = 10, energy_consumption = 5),
          Part("Weapon", attack_level = 15, defense_level = 0, energy_consumption = 10),
          Part("Left Arm", attack_level = 3, defense_level = 20, energy_consumption = 10),
          Part("Right Arm", attack_level = 6, defense_level = 20, energy_consumption = 10),
          Part("Left Leg", attack_level = 4, defense_level = 20, energy_consumption = 15),
          Part("Right Leg", attack_level = 8, defense_level = 20, energy_consumption = 15),
      ]


  def great(self):
      print("Hi, My name is:", self.name)

  def print_energy(self):
      print(f"We have {self.energy} percent energy letf \n")

  def print_status(self):
      print(self.color)
      str_robot = robot_art.format(**self.get_part_status(), color_defense = colors['color_defense_red'], reset_color_defense = self.color)
      self.great()
      self.print_energy()
      print(str_robot)
      print(colors ["White"])

  def attack(self, enemy_robot, part_to_use, part_to_attack):
      enemy_part =  enemy_robot.parts[part_to_attack]
      attack_power = self.parts[part_to_use].attack_level

      enemy_part.defense_level -= attack_power

      print(f"\n{self.color}{self.name} attacks {enemy_robot.name}'s {enemy_part.name} with {attack_power} attack power. "
            f"{colors['color_defense_red']} Defense reduced by {attack_power}!{self.color}")

      self.energy -= self.parts[part_to_use].energy_consumption

  def is_on(self):
      return self.energy > 0

  def is_there_avalilable_part(self):
    for part in self.parts:
      if part.is_available():
        return True
    return False

  def get_part_status(self):
      part_status = {}
      for part in self.parts:
        status_dic = part.get_status_dict()
        part_status.update(status_dic)
      return part_status
  
class Part:
  def __init__ (self, name, attack_level = 0, defense_level = 0, energy_consumption = 0):
      self.name = name
      self.attack_level = attack_level
      self.defense_level = defense_level
      self.energy_consumption = energy_consumption

  def get_status_dict(self):

      formatted_name = self.name.replace(" ", "_").lower()

      return {
          "{}_name".format(formatted_name): self.name.upper(),
          "{}_status".format(formatted_name): self.is_available(),
          "{}_attack".format(formatted_name): self.attack_level,
          "{}_defense".format(formatted_name): self.defense_level,
          "{}_energy_consump".format(formatted_name): self.energy_consumption,
      }

  def is_available(self):
      return self.defense_level >= 0

colors = {
    "Black": '\x1b[90m',
    "Blue": '\x1b[94m',
    "Cyan": '\x1b[96m',
    "Green": '\x1b[38;5;46m',
    "Magenta": '\x1b[95m',
    "White": '\x1b[97m',
    "Yellow": '\x1b[93m',
    "color_defense_red": '\x1b[38;5;196m',
}

robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}
      Defense: {color_defense}{head_defense}{reset_color_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {color_defense}{weapon_defense}{reset_color_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {color_defense}{left_arm_defense}{reset_color_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {color_defense}{right_arm_defense}{reset_color_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/
      | ||        || |          |4: {left_leg_name}
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {color_defense}{left_leg_defense}{reset_color_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {color_defense}{right_leg_defense}{reset_color_defense}
                                |Energy consumption: {right_leg_energy_consump}

"""

## Functions

def get_valid_color():
    while True:
      color = input("Select a color: ")
      color_capitalized = color.capitalize()

      if color_capitalized in colors:
        return colors[color_capitalized]
      else:
        print("Invalid color")

def play_game():
    playing = True

    print("Welcome to the game \n")
    round = 0

    print(""" Colors to select:
          [Black] [Blue] [Cyan] [Green]
         [Magenta] [White] [Yellow] \n""")

    playerOne = input("Enter a name for player 1: ")
    colorPlayerOne = get_valid_color()

    playerTwo = input("\nEnter a name for player 2: ")
    colorPlayerTwo = get_valid_color()

    robot_one = Robot(playerOne, colorPlayerOne)
    robot_two = Robot(playerTwo, colorPlayerTwo)

    while playing:
      if round % 2 == 0:
        current_robot = robot_one
        enemy_robot = robot_two
      else:
        current_robot = robot_two
        enemy_robot = robot_one

      current_robot.print_status()
      print("What part should I use to attack? ")
      try:
        part_to_use = int(input("- Choose a number part: "))
      except ValueError:
        print("Invalid input, please enter a number")
        continue


      if part_to_use <= 5:
         if not current_robot.parts[part_to_use].is_available():
            print(f"{colors['color_defense_red']}This part is not available! Please select another one.\n{colors['White']}")
            continue
          
         enemy_robot.print_status()
         print("Which part of the enemy should we attack? ")
         part_to_attack = int(input("- Choose a enemy part to attack: "))

         if part_to_attack <= 5:
            current_robot.attack(enemy_robot , part_to_use, part_to_attack)
            round += 1

      else:
        print(f"\n{colors['color_defense_red']}non-existent part")

      if not enemy_robot.is_on() or enemy_robot.is_there_avalilable_part() == False:
        playing = False
        print(f"Congratulations {current_robot.name}, you win!!!")

play_game()
