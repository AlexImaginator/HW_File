class CookPlanner:
    def __init__(self, recipes_file):
        self.recipes_file = recipes_file
        self.recipes_dict = {}
        self.ingridient_dict = {}
        self.not_found_dishes = []

    def read_recipes(self, dishes_list):
        found_dishes = []
        with open(self.recipes_file, encoding='utf-8') as file:
            for line in file:
                line_list = line.split('\n')
                line = line_list[0] if line_list[0] else ''
                if line in dishes_list:
                    self.recipes_dict[line] = []
                    found_dishes.append(line)
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
        self.not_found_dishes = list(set(dishes_list) - set(found_dishes))

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

    def print_shop_list(self, dishes_list, person_count):
        self.get_shop_list_by_dishes(dishes_list, person_count)
        if self.not_found_dishes:
            print(f'Блюда {", ".join(self.not_found_dishes)} не найдены в файле рецептов.\n'
                  f'Список ингридиентов на {person_count} персон:'
                  )
            for ingridient, estimation in self.ingridient_dict.items():
                print(f'{ingridient} - {estimation["quantity"]} {estimation["measure"]}')
        else:
            print(f'Список ингридиентов на {person_count} персон:')
            for ingridient, estimation in self.ingridient_dict.items():
                print(f'{ingridient} - {estimation["quantity"]} {estimation["measure"]}')
