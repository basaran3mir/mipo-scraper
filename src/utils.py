class Utils:
    def __init__(self):
        pass

    def list_to_unique_list(self, list):
        unique_list = []
        for element in list:
           if element not in unique_list:
               unique_list.append(element)
        return unique_list