from pprint import pprint


class CookPlanner:
    def __init__(self, recipes_file):
        self.recipes_file = recipes_file
        self.recipes_dict = {}
        self.ingridient_dict = {}

    def read_recipes(self, dishes_list):
        with open(self.recipes_file, encoding='utf-8') as file:
            for line in file:
                line_list = line.split('\n')
                line = line_list[0] if line_list[0] else ''
                if line in dishes_list:
                    self.recipes_dict[line] = []
                    file.readline()
                    for ingridient in file:
                        if ingridient != '\n':
                            ingridient_values = ingridient.split(' | ')
                            ingridient_dict = {'ingridient_name': ingridient_values[0].strip(),
                                               'quantity': ingridient_values[1].strip(),
                                               'measure': ingridient_values[2].strip()}
                            self.recipes_dict[line].append(ingridient_dict)
                        else:
                            break

    def get_shop_list_by_dishes(self, dishes_list, person_count):
        self.read_recipes(dishes_list)
        for ingridient_list in self.recipes_dict.values():
            for ingridient in ingridient_list:
                if ingridient['ingridient_name'] not in self.ingridient_dict:
                    self.ingridient_dict[
                        ingridient['ingridient_name']
                        ] = {'quantity': float(ingridient['quantity']) * person_count, 'measure': ingridient['measure']}
                else:
                    self.ingridient_dict[
                        ingridient['ingridient_name']
                    ]['quantity'] += float(ingridient['quantity']) * person_count
        return self.ingridient_dict


person_count = 5
dishes_list = ['Омлет', 'Утка по-пекински', 'Запеченный картофель']
planner = CookPlanner('recipes.txt')
pprint(planner.get_shop_list_by_dishes(dishes_list, person_count))
