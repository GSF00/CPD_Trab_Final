import os
import struct
import data_extraction
import math


class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        self.index_list = []
        # How many times this character appeared in the addition process
        self.counter = 1

    def add(self, word: str, index: int):
        node = self
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    child.index_list.append(index)
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
                node.index_list.append(index)
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True

    def find_prefix(root, prefix: str):
        node = root
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not root.children:
            return False, []
        for char in prefix:
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return False, []
        # Well, we are here means we have found the prefix. Return true to indicate that
        # And also the counter of the last node. This indicates how many words have this
        # prefix
        return True, node.index_list


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def menu_interaction():
    os.system('cls')
    print("*" * 65)
    print("\tCatálogo de cartas de Yu-Gi-Oh! Trading Card Game\n")
    print("\t\t\t\tMENU\n")
    print("Sair \t\t\t\t\t-\t 0")
    print("Adicionar cartas com arquivo '.csv' \t-\t 1")
    print("Adicionar carta manualmente \t\t-\t 2")
    print("Procurar carta \t\t\t\t-\t 3\n")
    print("*" * 65)

    return int(input("Digite a operação a realizar: "))


def data_search(trie_tree):
    # Arquivo principal do catálogo
    main_file = open("main.dat", "rb")

    # Arquivos de índices para o TYPE
    type_normal_file = open("type_normal_posting.dat", "rb")
    type_effect_file = open("type_effect_posting.dat", "rb")
    type_flip_file = open("type_flip_posting.dat", "rb")
    type_tuner_file = open("type_tuner_posting.dat", "rb")
    type_normal_tuner_file = open("type_normal_tuner_posting.dat", "rb")
    type_token_file = open("type_token_posting.dat", "rb")
    type_fusion_file = open("type_fusion_posting.dat", "rb")
    type_ritual_file = open("type_ritual_posting.dat", "rb")
    type_ritual_effect_file = open("type_ritual_effect_posting.dat", "rb")
    type_synchro_file = open("type_synchro_posting.dat", "rb")
    type_XYZ_file = open("type_XYZ_posting.dat", "rb")
    type_pendulum_normal_file = open("type_pendulum_normal_posting.dat", "rb")
    type_pendulum_effect_file = open("type_pendulum_effect_posting.dat", "rb")
    type_trap_file = open("type_trap_posting.dat", "rb")
    type_spell_file = open("type_spell_posting.dat", "rb")
    type_other_file = open("type_other_posting.dat", "rb")

    # Arquivos de índices para o LEVEL
    level_1_file = open("level_1_posting.dat", "rb")
    level_2_file = open("level_2_posting.dat", "rb")
    level_3_file = open("level_3_posting.dat", "rb")
    level_4_file = open("level_4_posting.dat", "rb")
    level_5_file = open("level_5_posting.dat", "rb")
    level_6_file = open("level_6_posting.dat", "rb")
    level_7_file = open("level_7_posting.dat", "rb")
    level_8_file = open("level_8_posting.dat", "rb")
    level_9_file = open("level_9_posting.dat", "rb")
    level_10_file = open("level_10_posting.dat", "rb")
    level_11_file = open("level_11_posting.dat", "rb")
    level_12_file = open("level_12_posting.dat", "rb")
    level_other_file = open("level_other_posting.dat", "rb")

    # Arquivos de índices para o RACE
    race_aqua_file = open("race_aqua_posting.dat", "rb")
    race_beast_file = open("race_beast_posting.dat", "rb")
    race_beast_warrior_file = open("race_beast_warrior_posting.dat", "rb")
    race_cyberse_file = open("race_cyberse_posting.dat", "rb")
    race_dinosaur_file = open("race_dinosaur_posting.dat", "rb")
    race_divine_beast_file = open("race_divine_beast_posting.dat", "rb")
    race_dragon_file = open("race_dragon_posting.dat", "rb")
    race_fairy_file = open("race_fairy_posting.dat", "rb")
    race_fiend_file = open("race_fiend_posting.dat", "rb")
    race_fish_file = open("race_fish_posting.dat", "rb")
    race_insect_file = open("race_insect_posting.dat", "rb")
    race_machine_file = open("race_machine_posting.dat", "rb")
    race_plant_file = open("race_plant_posting.dat", "rb")
    race_psychic_file = open("race_psychic_posting.dat", "rb")
    race_pyro_file = open("race_pyro_posting.dat", "rb")
    race_reptile_file = open("race_reptile_posting.dat", "rb")
    race_rock_file = open("race_rock_posting.dat", "rb")
    race_sea_serpent_file = open("race_sea_serpent_posting.dat", "rb")
    race_spellcaster_file = open("race_spellcaster_posting.dat", "rb")
    race_thunder_file = open("race_thunder_posting.dat", "rb")
    race_warrior_file = open("race_warrior_posting.dat", "rb")
    race_winged_beast_file = open("race_winged_beast_posting.dat", "rb")
    race_wyrm_file = open("race_wyrm_posting.dat", "rb")
    race_zombie_file = open("race_zombie_posting.dat", "rb")
    race_other_file = open("race_other_posting.dat", "rb")

    # Arquivos de índices para o ATTRIBUTE
    attribute_dark_file = open("attribute_dark_posting.dat", "rb")
    attribute_divine_file = open("attribute_divine_posting.dat", "rb")
    attribute_earth_file = open("attribute_earth_posting.dat", "rb")
    attribute_fire_file = open("attribute_fire_posting.dat", "rb")
    attribute_light_file = open("attribute_light_posting.dat", "rb")
    attribute_water_file = open("attribute_water_posting.dat", "rb")
    attribute_wind_file = open("attribute_wind_posting.dat", "rb")
    attribute_other_file = open("attribute_other_posting.dat", "rb")

    # Arquivos de índices para o ATK
    atk_0_999_file = open("atk_0_999_posting.dat", "rb")
    atk_1000_1999_file = open("atk_1000_1999_posting.dat", "rb")
    atk_2000_2999_file = open("atk_2000_2999_posting.dat", "rb")
    atk_3000_3999_file = open("atk_3000_3999_posting.dat", "rb")
    atk_4000_4999_file = open("atk_4000_4999_posting.dat", "rb")
    atk_5000_infinity_file = open("atk_5000_infinity_posting.dat", "rb")

    # Arquivos de índices para o DEF
    def_0_999_file = open("def_0_999_posting.dat", "rb")
    def_1000_1999_file = open("def_1000_1999_posting.dat", "rb")
    def_2000_2999_file = open("def_2000_2999_posting.dat", "rb")
    def_3000_3999_file = open("def_3000_3999_posting.dat", "rb")
    def_4000_4999_file = open("def_4000_4999_posting.dat", "rb")
    def_5000_infinity_file = open("def_5000_infinity_posting.dat", "rb")

    type_dict = {
        "Normal Monster": type_normal_file,
        "Effect Monster": type_effect_file,
        "Flip Effect Monster": type_flip_file,
        "Tuner Monster": type_tuner_file,
        "Normal Tuner Monster": type_normal_tuner_file,
        "Token": type_token_file,
        "Fusion Monster": type_fusion_file,
        "Ritual Monster": type_ritual_file,
        "Ritual Effect Monster": type_ritual_effect_file,
        "Synchro Monster": type_synchro_file,
        "XYZ Monster": type_XYZ_file,
        "Pendulum Normal Monster": type_pendulum_normal_file,
        "Pendulum Effect Monster": type_pendulum_effect_file,
        "Trap Card": type_trap_file,
        "Spell Card": type_spell_file
    }

    level_dict = {
        1: level_1_file,
        2: level_2_file,
        3: level_3_file,
        4: level_4_file,
        5: level_5_file,
        6: level_6_file,
        7: level_7_file,
        8: level_8_file,
        9: level_9_file,
        10: level_10_file,
        11: level_11_file,
        12: level_12_file,
    }

    race_dict = {
        "Aqua": race_aqua_file,
        "Beast": race_beast_file,
        "Beast-Warrior": race_beast_warrior_file,
        "Cyberse": race_cyberse_file,
        "Dinosaur": race_dinosaur_file,
        "Divine-Beast": race_divine_beast_file,
        "Dragon": race_dragon_file,
        "Fairy": race_fairy_file,
        "Fiend": race_fiend_file,
        "Fish": race_fish_file,
        "Insect": race_insect_file,
        "Machine": race_machine_file,
        "Plant": race_plant_file,
        "Psychic": race_psychic_file,
        "Pyro": race_pyro_file,
        "Reptile": race_reptile_file,
        "Rock": race_rock_file,
        "Sea Serpent": race_sea_serpent_file,
        "Spellcaster": race_spellcaster_file,
        "Thunder": race_thunder_file,
        "Warrior": race_warrior_file,
        "Winged Beast": race_winged_beast_file,
        "Wyrm": race_wyrm_file,
        "Zombie": race_zombie_file
    }

    attribute_dict = {
        "DARK": attribute_dark_file,
        "DIVINE": attribute_divine_file,
        "EARTH": attribute_earth_file,
        "FIRE": attribute_fire_file,
        "LIGHT": attribute_light_file,
        "WATER": attribute_water_file,
        "WIND": attribute_wind_file
    }

    atk_dict = {
        1: atk_0_999_file,
        2: atk_1000_1999_file,
        3: atk_2000_2999_file,
        4: atk_3000_3999_file,
        5: atk_4000_4999_file,
        6: atk_5000_infinity_file
    }

    def_dict = {
        1: def_0_999_file,
        2: def_1000_1999_file,
        3: def_2000_2999_file,
        4: def_3000_3999_file,
        5: def_4000_4999_file,
        6: def_5000_infinity_file
    }

    card_type_list = ["Normal Monster", "Effect Monster", "Flip Effect Monster", "Tuner Monster",
                      "Normal Tuner Monster",
                      "Token", "Fusion Monster", "Ritual Monster", "Ritual Effect Monster", "Synchro Monster",
                      "XYZ Monster",
                      "Pendulum Normal Monster", "Pendulum Effect Monster", "Trap Card", "Spell Card"]

    level_list = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    race_list = ["Aqua", "Beast", "Beast-Warrior", "Cyberse", "Dinosaur", "Divine-Beast", "Dragon",
                 "Fairy", "Fiend", "Fish", "Insect", "Machine", "Plant", "Psychic", "Pyro", "Reptile",
                 "Rock", "Sea Serpent", "Spellcaster", "Thunder", "Warrior", "Winged Beast", "Wyrm", "Zombie"]

    attribute_list = ["DARK", "DIVINE", "EARTH", "FIRE", "LIGHT", "WATER", "WIND"]

    option_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    option = -1
    index_list = []

    while option != 0:
        os.system('cls')
        print("*" * 63)
        print("\t\t\tBUSCA DE CARTAS\n")
        print("Sair \t\t\t\t-\t 0")
        print("Pesquisar cartas \t\t-\t 1")
        print("Filtrar por Name \t\t-\t 2")
        print("Filtrar por Type \t\t-\t 3")
        print("Filtrar por Level \t\t-\t 4")
        print("Filtrar por Race \t\t-\t 5")
        print("Filtrar por Attribute \t\t-\t 6")
        print("Filtrar por ATK \t\t-\t 7")
        print("Filtrar por DEF \t\t-\t 8\n")
        print("*" * 63)

        option = int(input("Digite a operação a realizar: "))

        while option not in option_list:
            option = int(input("Digite a operação a realizar: "))

        if option == 0:
            pass
        elif option == 1:
            # Pesquisa de todas as cartas
            if len(index_list) == 0:
                main_file.seek(0, os.SEEK_END)
                registry_amount = int(main_file.tell() / struct.calcsize("60s30si30s20sii"))
                main_file.seek(0)

                registry_per_page = 25
                number_of_pages = int(math.ceil(registry_amount / registry_per_page))
                current_page: int = 0

                # Paginação dos resultados obtidos
                while True:
                    if current_page < number_of_pages - 1:
                        main_file.seek(current_page*registry_per_page*struct.calcsize("60s30si30s20sii"))

                        packed_page_data = main_file.read(
                            struct.calcsize("60s30si30s20sii")*registry_per_page) # Lê os dados da página atual

                        i = 0

                        os.system('cls')

                        print("Name, Card Type, Level, Race, Attribute, ATK, DEF\n")

                        while i < registry_per_page:
                            name, card_type, level, race, attribute, atk, dfs = struct.unpack(
                                "60s30si30s20sii", packed_page_data[i*156:(i+1)*156])

                            print(name.decode('utf-8').rstrip('\x00'), card_type.decode('utf-8').rstrip('\x00'), level,
                                  race.decode('utf-8').rstrip('\x00'), attribute.decode('utf-8').rstrip('\x00'), atk, dfs)

                            i += 1

                        print(f"\nPágina {current_page + 1}/{number_of_pages}\n")
                        search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        while search_option not in range(0, number_of_pages + 1):
                            search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        if search_option == 0:
                            break

                        current_page = search_option - 1

                    else:
                        registry_on_last_page = registry_amount % registry_per_page

                        main_file.seek(current_page * registry_per_page * struct.calcsize("60s30si30s20sii"))

                        packed_page_data = main_file.read(
                            struct.calcsize("60s30si30s20sii") * registry_on_last_page)  # Lê os dados da página atual

                        i = 0

                        os.system('cls')

                        print("Name, Card Type, Level, Race, Attribute, ATK, DEF\n")

                        while i < registry_on_last_page:
                            name, card_type, level, race, attribute, atk, dfs = struct.unpack(
                                "60s30si30s20sii", packed_page_data[i * 156:(i + 1) * 156])

                            print(name.decode('utf-8').rstrip('\x00'), card_type.decode('utf-8').rstrip('\x00'), level,
                                  race.decode('utf-8').rstrip('\x00'), attribute.decode('utf-8').rstrip('\x00'), atk,
                                  dfs)

                            i += 1

                        print(f"\nPágina {current_page + 1}/{number_of_pages}\n")
                        search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        while search_option not in range(0, number_of_pages + 1):
                            search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        if search_option == 0:
                            break

                        current_page = search_option - 1

            # Pesquisa das cartas filtradas
            else:
                registry_amount = len(index_list)

                registry_per_page = 25
                number_of_pages = int(math.ceil(registry_amount / registry_per_page))
                current_page: int = 0

                # Paginação dos resultados obtidos
                while True:
                    if current_page < number_of_pages - 1:
                        os.system('cls')
                        print("Name, Card Type, Level, Race, Attribute, ATK, DEF\n")

                        for index in index_list[current_page*registry_per_page:(current_page+1)*registry_per_page]:
                            main_file.seek(index*struct.calcsize("60s30si30s20sii"))

                            packed_page_data = main_file.read(struct.calcsize("60s30si30s20sii")) # Lê os dados da página atual

                            name, card_type, level, race, attribute, atk, dfs = struct.unpack(
                                "60s30si30s20sii", packed_page_data)

                            print(name.decode('utf-8').rstrip('\x00'), card_type.decode('utf-8').rstrip('\x00'), level,
                                  race.decode('utf-8').rstrip('\x00'), attribute.decode('utf-8').rstrip('\x00'), atk,
                                  dfs)

                        print(f"\nPágina {current_page + 1}/{number_of_pages}\n")
                        search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        while search_option not in range(0, number_of_pages + 1):
                            search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        if search_option == 0:
                            index_list = []
                            break

                        current_page = search_option - 1

                    else:
                        os.system('cls')
                        print("Name, Card Type, Level, Race, Attribute, ATK, DEF\n")

                        for index in index_list[current_page*registry_per_page:]:
                            main_file.seek(index*struct.calcsize("60s30si30s20sii"))

                            packed_page_data = main_file.read(struct.calcsize("60s30si30s20sii")) # Lê os dados da página atual

                            name, card_type, level, race, attribute, atk, dfs = struct.unpack(
                                "60s30si30s20sii", packed_page_data)

                            print(name.decode('utf-8').rstrip('\x00'), card_type.decode('utf-8').rstrip('\x00'), level,
                                  race.decode('utf-8').rstrip('\x00'), attribute.decode('utf-8').rstrip('\x00'), atk,
                                  dfs)

                        print(f"\nPágina {current_page + 1}/{number_of_pages}\n")
                        search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        while search_option not in range(0, number_of_pages + 1):
                            search_option = int(input("Digite a página a ser acessada (0 para sair): "))

                        if search_option == 0:
                            index_list = []
                            break

                        current_page = search_option - 1

        # Filtragem pelo nome da carta
        elif option == 2:
            name_search = input('Digite o nome da carta a ser procurada: ').lower()

            trie_index = trie_tree.find_prefix(name_search)

            if len(index_list) == 0:
                index_list = trie_index[1]

            else:
                index_list = intersection(index_list, trie_index[1])

        # Filtragem pelo tipo da carta
        elif option == 3:
            type_search = input('Digite o tipo da carta a ser procurada: ')

            while type_search not in card_type_list:
                type_search = input('Digite o tipo da carta a ser procurada: ')

            file_search = type_dict[type_search]
            file_search.seek(0, os.SEEK_END)
            registry_amount = int(file_search.tell() / struct.calcsize("i"))
            file_search.seek(0)

            i = 0
            file_search_list = []

            while i < registry_amount:
                file_search_list.append(struct.unpack("i", file_search.read(struct.calcsize("i")))[0])
                i += 1

            if len(index_list) == 0:
                index_list = file_search_list

            else:
                index_list = intersection(index_list, file_search_list)

        # Filtragem pelo nivel da carta
        elif option == 4:
            level_search = int(input('Digite o nível da carta a ser procurada: '))

            while level_search not in level_list:
                level_search = int(input('Digite o nível da carta a ser procurada: '))

            file_search = level_dict[level_search]
            file_search.seek(0, os.SEEK_END)
            registry_amount = int(file_search.tell() / struct.calcsize("i"))
            file_search.seek(0)

            i = 0
            file_search_list = []

            while i < registry_amount:
                file_search_list.append(struct.unpack("i", file_search.read(struct.calcsize("i")))[0])
                i += 1

            if len(index_list) == 0:
                index_list = file_search_list

            else:
                index_list = intersection(index_list, file_search_list)

        # Filtragem pela raça da carta
        elif option == 5:
            race_search = input('Digite a raça da carta a ser procurada: ')

            while race_search not in race_list:
                race_search = input('Digite a raça da carta a ser procurada: ')

            file_search = race_dict[race_search]
            file_search.seek(0, os.SEEK_END)
            registry_amount = int(file_search.tell() / struct.calcsize("i"))
            file_search.seek(0)

            i = 0
            file_search_list = []

            while i < registry_amount:
                file_search_list.append(struct.unpack("i", file_search.read(struct.calcsize("i")))[0])
                i += 1

            if len(index_list) == 0:
                index_list = file_search_list

            else:
                index_list = intersection(index_list, file_search_list)

        # Filtragem pelo atributo da carta
        elif option == 6:
            attribute_search = input('Digite o atributo da carta a ser procurada: ').upper()

            while attribute_search not in attribute_list:
                attribute_search = input('Digite o atributo da carta a ser procurada: ').upper()

            file_search = attribute_dict[attribute_search]
            file_search.seek(0, os.SEEK_END)
            registry_amount = int(file_search.tell() / struct.calcsize("i"))
            file_search.seek(0)

            i = 0
            file_search_list = []

            while i < registry_amount:
                file_search_list.append(struct.unpack("i", file_search.read(struct.calcsize("i")))[0])
                i += 1

            if len(index_list) == 0:
                index_list = file_search_list

            else:
                index_list = intersection(index_list, file_search_list)

        # Filtragem pelo ATK da carta
        elif option == 7:
            print('ATK:[0 - 999]\t\t-\t1')
            print('ATK:[1000 - 1999]\t-\t2')
            print('ATK:[2000 - 2999]\t-\t3')
            print('ATK:[3000 - 3999]\t-\t4')
            print('ATK:[4000 - 4999]\t-\t5')
            print('ATK:[5000 - inf]\t-\t6')

            atk_search = int(input('Digite o intervalo de ATK da carta a ser procurada: '))

            while atk_search not in [1, 2, 3, 4, 5, 6]:
                atk_search = int(input('Digite o intervalo de ATK da carta a ser procurada: '))

            file_search = atk_dict[atk_search]
            file_search.seek(0, os.SEEK_END)
            registry_amount = int(file_search.tell() / struct.calcsize("i"))
            file_search.seek(0)

            i = 0
            file_search_list = []

            while i < registry_amount:
                file_search_list.append(struct.unpack("i", file_search.read(struct.calcsize("i")))[0])
                i += 1

            if len(index_list) == 0:
                index_list = file_search_list

            else:
                index_list = intersection(index_list, file_search_list)

        # Filtragem pela DEF da carta
        elif option == 8:
            print('DEF:[0 - 999]\t\t-\t1')
            print('DEF:[1000 - 1999]\t-\t2')
            print('DEF:[2000 - 2999]\t-\t3')
            print('DEF:[3000 - 3999]\t-\t4')
            print('DEF:[4000 - 4999]\t-\t5')
            print('DEF:[5000 - inf]\t-\t6')

            def_search = int(input('Digite o intervalo de DEF da carta a ser procurada: '))

            while def_search not in [1, 2, 3, 4, 5, 6]:
                def_search = int(input('Digite o intervalo de DEF da carta a ser procurada: '))

            file_search = def_dict[def_search]
            file_search.seek(0, os.SEEK_END)
            registry_amount = int(file_search.tell() / struct.calcsize("i"))
            file_search.seek(0)

            i = 0
            file_search_list = []

            while i < registry_amount:
                file_search_list.append(struct.unpack("i", file_search.read(struct.calcsize("i")))[0])
                i += 1

            if len(index_list) == 0:
                index_list = file_search_list

            else:
                index_list = intersection(index_list, file_search_list)

    # Fechamento dos arquivos
    main_file.close()

    type_normal_file.close()
    type_effect_file.close()
    type_flip_file.close()
    type_tuner_file.close()
    type_normal_tuner_file.close()
    type_token_file.close()
    type_fusion_file.close()
    type_ritual_file.close()
    type_ritual_effect_file.close()
    type_synchro_file.close()
    type_XYZ_file.close()
    type_pendulum_normal_file.close()
    type_pendulum_effect_file.close()
    type_trap_file.close()
    type_spell_file.close()
    type_other_file.close()

    level_1_file.close()
    level_2_file.close()
    level_3_file.close()
    level_4_file.close()
    level_5_file.close()
    level_6_file.close()
    level_7_file.close()
    level_8_file.close()
    level_9_file.close()
    level_10_file.close()
    level_11_file.close()
    level_12_file.close()
    level_other_file.close()

    race_aqua_file.close()
    race_beast_file.close()
    race_beast_warrior_file.close()
    race_cyberse_file.close()
    race_dinosaur_file.close()
    race_divine_beast_file.close()
    race_dragon_file.close()
    race_fairy_file.close()
    race_fiend_file.close()
    race_fish_file.close()
    race_insect_file.close()
    race_machine_file.close()
    race_plant_file.close()
    race_psychic_file.close()
    race_pyro_file.close()
    race_reptile_file.close()
    race_rock_file.close()
    race_sea_serpent_file.close()
    race_spellcaster_file.close()
    race_thunder_file.close()
    race_warrior_file.close()
    race_winged_beast_file.close()
    race_wyrm_file.close()
    race_zombie_file.close()
    race_other_file.close()

    attribute_dark_file.close()
    attribute_divine_file.close()
    attribute_earth_file.close()
    attribute_fire_file.close()
    attribute_light_file.close()
    attribute_water_file.close()
    attribute_wind_file.close()
    attribute_other_file.close()

    atk_0_999_file.close()
    atk_1000_1999_file.close()
    atk_2000_2999_file.close()
    atk_3000_3999_file.close()
    atk_4000_4999_file.close()
    atk_5000_infinity_file.close()

    def_0_999_file.close()
    def_1000_1999_file.close()
    def_2000_2999_file.close()
    def_3000_3999_file.close()
    def_4000_4999_file.close()
    def_5000_infinity_file.close()

    return trie_tree


def main():
    menu_option = -1

    trie_tree = TrieNode("*")

    while menu_option != 0:
        menu_option = menu_interaction()

        while menu_option not in [0, 1, 2, 3]:
            menu_option = menu_interaction()

        if menu_option == 0:
            pass

        elif menu_option == 1:
            trie_tree = data_extraction.card_insertion_csv(trie_tree)

        elif menu_option == 2:
            trie_tree = data_extraction.card_insertion_manual(trie_tree)

        elif menu_option == 3:
            trie_tree = data_search(trie_tree)

    os.system('cls')

if __name__ == "__main__":
    main()
