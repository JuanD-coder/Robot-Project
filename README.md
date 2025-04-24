# 🤖 Robot Battle Arena - Proyecto de Aprendizaje en Python

Este proyecto es un juego simple de batalla de robots por turnos desarrollado en Python. Fue creado como ejercicio práctico para aprender la sintaxis básica del lenguaje Python mientras se desarrolla una mecánica divertida e interactiva.

## 📚 Objetivos del proyecto

- Aprender la estructura básica de **clases y objetos** en Python.
- Practicar el uso de **diccionarios**, **listas** y estructuras condicionales.
- Implementar la **interacción entre objetos** dentro del juego.
- Desarrollar una lógica de combate basada en **atributos dinámicos**.
- Representar gráficamente el estado del robot con **arte ASCII**.

## 🦾 Robot structure


``` py
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
```

## 🕹️ ¿Cómo se juega?

- El jugador selecciona las partes activas del robot.
- Cada parte tiene estadísticas únicas de **ataque, defensa y consumo de energía**.
- Los turnos se alternan entre jugadores para atacar o defenderse.
- El objetivo es **debilitar las partes del oponente** hasta que ya no pueda combatir.

## 💻 Iniciar el juego

- Clona el repositorio 
- Ejecuta el juego desde terminal:

``` bash
python3 robot_battle.py
```
