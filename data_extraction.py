import struct


# Função que separa os atributos em um registro
def attributeSeparator(line):
    if line[0] == '"':
        i = 1
        while line[i] != '"':
            i = i + 1

        name = line[1:i]
        i = i + 1
    else:
        i = 1
        while line[i] != ',':
            i = i + 1

        name = line[0:i]

    i = i + 1  # i apontando para o segundo campo
    i2 = i + 1

    while line[i2] != ',':
        i2 = i2 + 1

    card_type = line[i:i2]

    i2 = i2 + 1  # i2 apontando para o terceiro campo

    if line[i2] == ',':
        level = -1
        i3 = i2 + 1
    else:
        i3 = i2 + 1

        while line[i3] != ',':
            i3 = i3 + 1

        level = int(line[i2:i3])

        i3 = i3 + 1

    i4 = i3 + 1

    while line[i4] != ',':
        i4 = i4 + 1

    race = line[i3:i4]

    i4 = i4 + 1  # i4 aponta para o quinto atributo

    if line[i4] == ',':
        attribute = ''
        # i5 = i4 + 1
        atk = -1
        dfs = -1
    else:
        i5 = i4 + 1

        while line[i5] != ',':
            i5 = i5 + 1

        attribute = line[i4:i5]

        i5 = i5 + 1

        i6 = i5 + 1

        while line[i6] != ',':
            i6 = i6 + 1

        atk = int(line[i5:i6])

        i6 = i6 + 1

        i7 = i6 + 1

        while i7 < len(line) - 1:
            i7 = i7 + 1

        dfs = int(line[i6:i7])

    return name, card_type, level, race, attribute, atk, dfs


def card_insertion_csv(trie_tree):
    # Arquivo CSV
    file_name = input("Digite o nome do arquivo a ser importado: ")
    input_file = open(file_name, "r", encoding="utf-8")

    # Arquivo principal do catálogo
    main_file = open("main.dat", "ab")

    # Arquivos de índices para o TYPE
    type_normal_file = open("type_normal_posting.dat", "ab")
    type_effect_file = open("type_effect_posting.dat", "ab")
    type_flip_file = open("type_flip_posting.dat", "ab")
    type_tuner_file = open("type_tuner_posting.dat", "ab")
    type_normal_tuner_file = open("type_normal_tuner_posting.dat", "ab")
    type_token_file = open("type_token_posting.dat", "ab")
    type_fusion_file = open("type_fusion_posting.dat", "ab")
    type_ritual_file = open("type_ritual_posting.dat", "ab")
    type_ritual_effect_file = open("type_ritual_effect_posting.dat", "ab")
    type_synchro_file = open("type_synchro_posting.dat", "ab")
    type_XYZ_file = open("type_XYZ_posting.dat", "ab")
    type_pendulum_normal_file = open("type_pendulum_normal_posting.dat", "ab")
    type_pendulum_effect_file = open("type_pendulum_effect_posting.dat", "ab")
    type_trap_file = open("type_trap_posting.dat", "ab")
    type_spell_file = open("type_spell_posting.dat", "ab")
    type_other_file = open("type_other_posting.dat", "ab")

    # Arquivos de índices para o LEVEL
    level_1_file = open("level_1_posting.dat", "ab")
    level_2_file = open("level_2_posting.dat", "ab")
    level_3_file = open("level_3_posting.dat", "ab")
    level_4_file = open("level_4_posting.dat", "ab")
    level_5_file = open("level_5_posting.dat", "ab")
    level_6_file = open("level_6_posting.dat", "ab")
    level_7_file = open("level_7_posting.dat", "ab")
    level_8_file = open("level_8_posting.dat", "ab")
    level_9_file = open("level_9_posting.dat", "ab")
    level_10_file = open("level_10_posting.dat", "ab")
    level_11_file = open("level_11_posting.dat", "ab")
    level_12_file = open("level_12_posting.dat", "ab")
    level_other_file = open("level_other_posting.dat", "ab")

    # Arquivos de índices para o RACE
    race_aqua_file = open("race_aqua_posting.dat", "ab")
    race_beast_file = open("race_beast_posting.dat", "ab")
    race_beast_warrior_file = open("race_beast_warrior_posting.dat", "ab")
    race_cyberse_file = open("race_cyberse_posting.dat", "ab")
    race_dinosaur_file = open("race_dinosaur_posting.dat", "ab")
    race_divine_beast_file = open("race_divine_beast_posting.dat", "ab")
    race_dragon_file = open("race_dragon_posting.dat", "ab")
    race_fairy_file = open("race_fairy_posting.dat", "ab")
    race_fiend_file = open("race_fiend_posting.dat", "ab")
    race_fish_file = open("race_fish_posting.dat", "ab")
    race_insect_file = open("race_insect_posting.dat", "ab")
    race_machine_file = open("race_machine_posting.dat", "ab")
    race_plant_file = open("race_plant_posting.dat", "ab")
    race_psychic_file = open("race_psychic_posting.dat", "ab")
    race_pyro_file = open("race_pyro_posting.dat", "ab")
    race_reptile_file = open("race_reptile_posting.dat", "ab")
    race_rock_file = open("race_rock_posting.dat", "ab")
    race_sea_serpent_file = open("race_sea_serpent_posting.dat", "ab")
    race_spellcaster_file = open("race_spellcaster_posting.dat", "ab")
    race_thunder_file = open("race_thunder_posting.dat", "ab")
    race_warrior_file = open("race_warrior_posting.dat", "ab")
    race_winged_beast_file = open("race_winged_beast_posting.dat", "ab")
    race_wyrm_file = open("race_wyrm_posting.dat", "ab")
    race_zombie_file = open("race_zombie_posting.dat", "ab")
    race_other_file = open("race_other_posting.dat", "ab")

    # Arquivos de índices para o ATTRIBUTE
    attribute_dark_file = open("attribute_dark_posting.dat", "ab")
    attribute_divine_file = open("attribute_divine_posting.dat", "ab")
    attribute_earth_file = open("attribute_earth_posting.dat", "ab")
    attribute_fire_file = open("attribute_fire_posting.dat", "ab")
    attribute_light_file = open("attribute_light_posting.dat", "ab")
    attribute_water_file = open("attribute_water_posting.dat", "ab")
    attribute_wind_file = open("attribute_wind_posting.dat", "ab")
    attribute_other_file = open("attribute_other_posting.dat", "ab")

    # Arquivos de índices para o ATK
    atk_0_999_file = open("atk_0_999_posting.dat", "ab")
    atk_1000_1999_file = open("atk_1000_1999_posting.dat", "ab")
    atk_2000_2999_file = open("atk_2000_2999_posting.dat", "ab")
    atk_3000_3999_file = open("atk_3000_3999_posting.dat", "ab")
    atk_4000_4999_file = open("atk_4000_4999_posting.dat", "ab")
    atk_5000_infinity_file = open("atk_5000_infinity_posting.dat", "ab")

    # Arquivos de índices para o DEF
    def_0_999_file = open("def_0_999_posting.dat", "ab")
    def_1000_1999_file = open("def_1000_1999_posting.dat", "ab")
    def_2000_2999_file = open("def_2000_2999_posting.dat", "ab")
    def_3000_3999_file = open("def_3000_3999_posting.dat", "ab")
    def_4000_4999_file = open("def_4000_4999_posting.dat", "ab")
    def_5000_infinity_file = open("def_5000_infinity_posting.dat", "ab")

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

    line = input_file.readline()  # Primeira linha "Name, Type, Level, ..."
    line = input_file.readline()  # Primeira linha efetivamente de dados

    posicao = int(int(main_file.tell()) / int(struct.calcsize("60s30si30s20sii")))

    # Iteração de cada linha do arquivo CSV
    while line != '':
        name, card_type, level, race, attribute, atk, dfs = attributeSeparator(line)

        # Adiciona o nome na árvore TRIE
        trie_tree.add(name.lower(), posicao)

        # Empacota os dados lidos do arquivo CSV
        packed_data = struct.pack("60s30si30s20sii", name.encode('utf-8'), card_type.encode('utf-8'), level,
                                  race.encode('utf-8'), attribute.encode('utf-8'), atk, dfs)

        # Escreve os dados no arquivo principal
        main_file.write(packed_data)

        # Adiciona os índices nos arquivos invertidos
        try:
            type_dict[card_type].write(struct.pack("I", posicao))
        except KeyError:
            type_other_file.write(struct.pack("I", posicao))

        try:
            level_dict[level].write(struct.pack("I", posicao))
        except KeyError:
            level_other_file.write(struct.pack("I", posicao))

        try:
            race_dict[race].write(struct.pack("I", posicao))
        except KeyError:
            race_other_file.write(struct.pack("I", posicao))

        try:
            attribute_dict[attribute].write(struct.pack("I", posicao))
        except KeyError:
            attribute_other_file.write(struct.pack("I", posicao))

        if atk >= 0:
            if atk < 1000:
                atk_0_999_file.write(struct.pack("I", posicao))
            elif atk < 2000:
                atk_1000_1999_file.write(struct.pack("I", posicao))
            elif atk < 3000:
                atk_2000_2999_file.write(struct.pack("I", posicao))
            elif atk < 4000:
                atk_3000_3999_file.write(struct.pack("I", posicao))
            elif atk < 5000:
                atk_4000_4999_file.write(struct.pack("I", posicao))
            else:
                atk_5000_infinity_file.write(struct.pack("I", posicao))

        if dfs >= 0:
            if dfs < 1000:
                def_0_999_file.write(struct.pack("I", posicao))
            elif dfs < 2000:
                def_1000_1999_file.write(struct.pack("I", posicao))
            elif dfs < 3000:
                def_2000_2999_file.write(struct.pack("I", posicao))
            elif dfs < 4000:
                def_3000_3999_file.write(struct.pack("I", posicao))
            elif dfs < 5000:
                def_4000_4999_file.write(struct.pack("I", posicao))
            else:
                def_5000_infinity_file.write(struct.pack("I", posicao))

        # Lê próxima linha
        line = input_file.readline()
        posicao = posicao + 1


    # Fechamento dos arquivos
    main_file.close()
    input_file.close()

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


def card_insertion_manual(trie_tree):
    card_type_list = ["Normal Monster", "Effect Monster", "Flip Effect Monster", "Tuner Monster", "Normal Tuner Monster",
                      "Token", "Fusion Monster", "Ritual Monster", "Ritual Effect Monster", "Synchro Monster", "XYZ Monster",
                      "Pendulum Normal Monster", "Pendulum Effect Monster", "Trap Card", "Spell Card"]

    level_list = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    race_list = ["Aqua", "Beast", "Beast-Warrior", "Cyberse", "Dinosaur", "Divine-Beast", "Dragon",
        "Fairy", "Fiend", "Fish", "Insect", "Machine", "Plant", "Psychic", "Pyro", "Reptile",
        "Rock", "Sea Serpent", "Spellcaster", "Thunder", "Warrior", "Winged Beast", "Wyrm", "Zombie"]

    attribute_list = ["DARK", "DIVINE", "EARTH", "FIRE", "LIGHT", "WATER", "WIND"]

    # Arquivo principal do catálogo
    main_file = open("main.dat", "ab")

    # Arquivos de índices para o TYPE
    type_normal_file = open("type_normal_posting.dat", "ab")
    type_effect_file = open("type_effect_posting.dat", "ab")
    type_flip_file = open("type_flip_posting.dat", "ab")
    type_tuner_file = open("type_tuner_posting.dat", "ab")
    type_normal_tuner_file = open("type_normal_tuner_posting.dat", "ab")
    type_token_file = open("type_token_posting.dat", "ab")
    type_fusion_file = open("type_fusion_posting.dat", "ab")
    type_ritual_file = open("type_ritual_posting.dat", "ab")
    type_ritual_effect_file = open("type_ritual_effect_posting.dat", "ab")
    type_synchro_file = open("type_synchro_posting.dat", "ab")
    type_XYZ_file = open("type_XYZ_posting.dat", "ab")
    type_pendulum_normal_file = open("type_pendulum_normal_posting.dat", "ab")
    type_pendulum_effect_file = open("type_pendulum_effect_posting.dat", "ab")
    type_trap_file = open("type_trap_posting.dat", "ab")
    type_spell_file = open("type_spell_posting.dat", "ab")
    type_other_file = open("type_other_posting.dat", "ab")

    # Arquivos de índices para o LEVEL
    level_1_file = open("level_1_posting.dat", "ab")
    level_2_file = open("level_2_posting.dat", "ab")
    level_3_file = open("level_3_posting.dat", "ab")
    level_4_file = open("level_4_posting.dat", "ab")
    level_5_file = open("level_5_posting.dat", "ab")
    level_6_file = open("level_6_posting.dat", "ab")
    level_7_file = open("level_7_posting.dat", "ab")
    level_8_file = open("level_8_posting.dat", "ab")
    level_9_file = open("level_9_posting.dat", "ab")
    level_10_file = open("level_10_posting.dat", "ab")
    level_11_file = open("level_11_posting.dat", "ab")
    level_12_file = open("level_12_posting.dat", "ab")
    level_other_file = open("level_other_posting.dat", "ab")

    # Arquivos de índices para o RACE
    race_aqua_file = open("race_aqua_posting.dat", "ab")
    race_beast_file = open("race_beast_posting.dat", "ab")
    race_beast_warrior_file = open("race_beast_warrior_posting.dat", "ab")
    race_cyberse_file = open("race_cyberse_posting.dat", "ab")
    race_dinosaur_file = open("race_dinosaur_posting.dat", "ab")
    race_divine_beast_file = open("race_divine_beast_posting.dat", "ab")
    race_dragon_file = open("race_dragon_posting.dat", "ab")
    race_fairy_file = open("race_fairy_posting.dat", "ab")
    race_fiend_file = open("race_fiend_posting.dat", "ab")
    race_fish_file = open("race_fish_posting.dat", "ab")
    race_insect_file = open("race_insect_posting.dat", "ab")
    race_machine_file = open("race_machine_posting.dat", "ab")
    race_plant_file = open("race_plant_posting.dat", "ab")
    race_psychic_file = open("race_psychic_posting.dat", "ab")
    race_pyro_file = open("race_pyro_posting.dat", "ab")
    race_reptile_file = open("race_reptile_posting.dat", "ab")
    race_rock_file = open("race_rock_posting.dat", "ab")
    race_sea_serpent_file = open("race_sea_serpent_posting.dat", "ab")
    race_spellcaster_file = open("race_spellcaster_posting.dat", "ab")
    race_thunder_file = open("race_thunder_posting.dat", "ab")
    race_warrior_file = open("race_warrior_posting.dat", "ab")
    race_winged_beast_file = open("race_winged_beast_posting.dat", "ab")
    race_wyrm_file = open("race_wyrm_posting.dat", "ab")
    race_zombie_file = open("race_zombie_posting.dat", "ab")
    race_other_file = open("race_other_posting.dat", "ab")

    # Arquivos de índices para o ATTRIBUTE
    attribute_dark_file = open("attribute_dark_posting.dat", "ab")
    attribute_divine_file = open("attribute_divine_posting.dat", "ab")
    attribute_earth_file = open("attribute_earth_posting.dat", "ab")
    attribute_fire_file = open("attribute_fire_posting.dat", "ab")
    attribute_light_file = open("attribute_light_posting.dat", "ab")
    attribute_water_file = open("attribute_water_posting.dat", "ab")
    attribute_wind_file = open("attribute_wind_posting.dat", "ab")
    attribute_other_file = open("attribute_other_posting.dat", "ab")

    # Arquivos de índices para o ATK
    atk_0_999_file = open("atk_0_999_posting.dat", "ab")
    atk_1000_1999_file = open("atk_1000_1999_posting.dat", "ab")
    atk_2000_2999_file = open("atk_2000_2999_posting.dat", "ab")
    atk_3000_3999_file = open("atk_3000_3999_posting.dat", "ab")
    atk_4000_4999_file = open("atk_4000_4999_posting.dat", "ab")
    atk_5000_infinity_file = open("atk_5000_infinity_posting.dat", "ab")

    # Arquivos de índices para o DEF
    def_0_999_file = open("def_0_999_posting.dat", "ab")
    def_1000_1999_file = open("def_1000_1999_posting.dat", "ab")
    def_2000_2999_file = open("def_2000_2999_posting.dat", "ab")
    def_3000_3999_file = open("def_3000_3999_posting.dat", "ab")
    def_4000_4999_file = open("def_4000_4999_posting.dat", "ab")
    def_5000_infinity_file = open("def_5000_infinity_posting.dat", "ab")

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

    # Atributos inseridos manualmente
    name = input("Digite o nome da carta: ")

    card_type = input("Digite o tipo da carta: ")

    while card_type not in card_type_list:
        card_type = input("Digite o tipo da carta: ")

    level = int(input("Digite o nível da carta: "))

    while level not in level_list:
        level = int(input("Digite o nível da carta: "))

    race = input("Digite a raça da carta: ")

    while race not in race_list:
        race = input("Digite a raça da carta: ")

    attribute = input("Digite o atributo da carta: ").upper()

    while attribute not in attribute_list:
        attribute = input("Digite o atributo da carta: ").upper()

    atk = int(input("Digite o ATK da carta: "))

    dfs = int(input("Digite o DEF da carta: "))

    packed_data = struct.pack("60s30si30s20sii", name.encode('utf-8'), card_type.encode('utf-8'), level,
                              race.encode('utf-8'), attribute.encode('utf-8'), atk, dfs)

    posicao = int(int(main_file.tell()) / int(struct.calcsize("60s30si30s20sii")))

    # Escreve os dados no arquivo principal
    main_file.write(packed_data)

    # Adiciona o nome na árvore TRIE
    trie_tree.add(name.lower(), posicao)

    # Adiciona os índices nos arquivos invertidos
    try:
        type_dict[card_type].write(struct.pack("I", posicao))
    except KeyError:
        type_other_file.write(struct.pack("I", posicao))

    try:
        level_dict[level].write(struct.pack("I", posicao))
    except KeyError:
        level_other_file.write(struct.pack("I", posicao))

    try:
        race_dict[race].write(struct.pack("I", posicao))
    except KeyError:
        race_other_file.write(struct.pack("I", posicao))

    try:
        attribute_dict[attribute].write(struct.pack("I", posicao))
    except KeyError:
        attribute_other_file.write(struct.pack("I", posicao))

    if atk >= 0:
        if atk < 1000:
            atk_0_999_file.write(struct.pack("I", posicao))
        elif atk < 2000:
            atk_1000_1999_file.write(struct.pack("I", posicao))
        elif atk < 3000:
            atk_2000_2999_file.write(struct.pack("I", posicao))
        elif atk < 4000:
            atk_3000_3999_file.write(struct.pack("I", posicao))
        elif atk < 5000:
            atk_4000_4999_file.write(struct.pack("I", posicao))
        else:
            atk_5000_infinity_file.write(struct.pack("I", posicao))

    if dfs >= 0:
        if dfs < 1000:
            def_0_999_file.write(struct.pack("I", posicao))
        elif dfs < 2000:
            def_1000_1999_file.write(struct.pack("I", posicao))
        elif dfs < 3000:
            def_2000_2999_file.write(struct.pack("I", posicao))
        elif dfs < 4000:
            def_3000_3999_file.write(struct.pack("I", posicao))
        elif dfs < 5000:
            def_4000_4999_file.write(struct.pack("I", posicao))
        else:
            def_5000_infinity_file.write(struct.pack("I", posicao))

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
