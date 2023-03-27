import random
from collections import Counter
import copy


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, counts in kwargs.items():
            self.contents += [color] * counts
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_counter = Counter(expected_balls)
    count_success = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counter = Counter(drawn_balls)

        success = True
        for ball, count in expected_counter.items():
            if drawn_counter[ball] < count:
                success = False
                break

        if success:
            count_success += 1
    
    return count_success/num_experiments
        
        


