class StreamHandler():
    def open(self, file_path):
        pass

    def write(self, file_path, write_object):
        pass

class StreamHandler2019():
    def open(self, file_path):
        with open(file_path, "r") as f:
            first_line = f.readline().strip()
            slices_to_order, types_of_pizza = map(int, first_line.split(" "))
            second_line = f.readline().strip()
            number_of_slices = list(map(int, second_line.split(" ")))

        # BUILDING DATA STRUCTURES
        slice_lookup = {i: x for i, x in enumerate(number_of_slices)}
        result = dict()
        result["slices_to_order"] = slices_to_order
        result["types_of_pizza"] = types_of_pizza
        result["number_of_slices"] = number_of_slices
        result["slice_lookup"] = slice_lookup
        return result

    def write(self, file_path, write_object):
        with open(file_path, "w") as f:
            f.write(str(len(write_object)) + "\n")
            f.write(" ".join(map(str, write_object)))