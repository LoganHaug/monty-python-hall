import random

class Gameshow:
    def __init__(self, runs=100):
        self.runs = runs
        self.switch_successes = 0
        self.fg_successes = 0

    def _get_doors(self) -> dict:
        """The index that is True represents the prize"""
        doors = [False] * 3
        doors[random.randint(0,2)] = True
        return tuple(doors)

    def _reveal_door(self, doors, guess):
        indicies = list(range(0,3))
        indicies.pop(guess)
        if doors[indicies[0]]:
            return indicies[1]
        elif doors[indicies[1]]:
            return indicies[0]
        return random.choice(indicies)

    def _switch(self, guess, reveal):
        switch = list(range(0,3))
        switch.remove(guess)
        switch.remove(reveal)
        return switch[0]

    def simulate(self):
        """Runs the simulation"""
        for _ in range(0, self.runs):
            doors = self._get_doors()
            guess = random.randint(0, 2)
            switch_guess = self._switch(guess, self._reveal_door(doors, guess))
            if doors[guess]:
                self.fg_successes += 1
            elif doors[switch_guess]:
                self.switch_successes += 1
        print(f"Total runs: {self.runs}")
        print(f"Correct guesses switching: {self.switch_successes}")
        print(f"Correct guesses not switching: {self.fg_successes}")