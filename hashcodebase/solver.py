
import random
import time

class Solver():
    def solve(self, data):
        pass

    def score(self, data):
        pass

    def error(self, data):
        pass

class Solver2019(Solver):

    def solve(self, data):

        start_time = time.time()
        best_order = []
        best_score = 0
        run_time = 10
        print(data)
        print()
        slices_to_order = data["slices_to_order"]
        types_of_pizza = data["types_of_pizza"]
        number_of_slices = data["number_of_slices"]
        slice_lookup = data["slice_lookup"]

        order_data = dict()
        order_data["slice_lookup"] = slice_lookup

        while(time.time() < start_time + run_time):
            number_of_slices = random.randint(0, types_of_pizza)
            my_order = random.sample(range(types_of_pizza), number_of_slices)

            order_data["order"] = my_order
            my_score = self.score(order_data)
            if my_score > slices_to_order:
                continue

            if my_score == slices_to_order:
                best_order = my_order
                best_score = my_score
                break

            if my_score > best_score:
                best_order = my_order
                best_score = my_score
            print("Score: ", my_score, "/", best_score)

        print()
        print("Score: ", my_score, "/", best_score)
        return best_order


    def score(self, data):
        slice_lookup = data["slice_lookup"]
        order = data["order"]
        return sum(slice_lookup[i] for i in order)

    def error(self, data):
        slice_lookup = data["slice_lookup"]
        order = data["order"]
        return slices_to_order - self.score(order)