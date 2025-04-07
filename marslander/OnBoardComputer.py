from DescentEvent import DescentEvent

class OnBoardComputer:


    def get_next_burn(self, status):
        a = status.get_altitude()
        v = status.get_velocity()
        burn = 0

        if a > 6500:
            if v >= 1000:
                burn = 200
        elif 1000 < a <= 6500:
            if v == 0:
                burn = 0
            else:
                burn = 200

        elif 100 < a <= 1000:
            if v > 102:
                burn = 200
            elif 100 <= v < 102:
                burn = 100

        elif a < 100:
            if v >= 100:
                burn = 200
            elif v == 0:
                burn = 98
            elif v < 5:
                burn = 100

        print(burn)  # hack!
        return burn

