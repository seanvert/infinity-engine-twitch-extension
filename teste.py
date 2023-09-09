GAM_GAME_TIME = "Elapsed game time (seconds)"
GAM_SELECTED_FORMATION = "Selected formation"
GAM_FORMATION_BUTTON_FMT = "Formation button %d"
GAM_PARTY_GOLD = "Party gold"
GAM_VIEW_PLAYER_AREA = "View area of party member at"
GAM_WEATHER = "Weather"
GAM_OFFSET_PARTY_MEMBERS = "Party members offset"
GAM_NUM_PARTY_MEMBERS = "# party members"
GAM_OFFSET_PARTY_INVENTORY = "Party inventory offset"
GAM_NUM_PARTY_INVENTORY = "# party inventory items"
GAM_OFFSET_NON_PARTY_MEMBERS = "Non-party characters offset"
GAM_NUM_NON_PARTY_MEMBERS = "# non-party characters"
GAM_OFFSET_GLOBAL_VARIABLES = "Global variables offset"
GAM_NUM_GLOBAL_VARIABLES = "# global variables"
GAM_WORLD_AREA = "World area"
GAM_CURRENT_LINK = "Current link"
GAM_NUM_JOURNAL_ENTRIES = "# journal entries"
GAM_OFFSET_JOURNAL_ENTRIES = "Journal entries offset"
GAM_REPUTATION = "Reputation"
GAM_MASTER_AREA = "Master area"
GAM_MASTER_AREA_2 = "Master area 2"
GAM_CONFIGURATION = "Configuration"
GAM_SAVE_VERSION = "Save version"
GAM_NUM_UNKNOWN = "Unknown section count"
GAM_OFFSET_UNKNOWN = "Unknown section offset"
GAM_NIGHTMARE_MODE = "Nightmare mode"
GAM_OFFSET_MODRON_MAZE = "Modron maze offset"
GAM_OFFSET_KILL_VARIABLES = "Kill variables offset"
GAM_NUM_KILL_VARIABLES = "# kill variables"
GAM_OFFSET_BESTIARY = "Bestiary offset"
GAM_OFFSET_FAMILIAR_INFO = "Familiar info offset"
GAM_OFFSET_STORED_LOCATIONS = "Stored locations offset"
GAM_NUM_STORED_LOCATIONS = "# stored locations"
GAM_REAL_TIME = "Elapsed real time (ticks)"
GAM_OFFSET_POCKET_PLANE_LOCATIONS = "Pocket plane locations offset"
GAM_NUM_POCKET_PLANE_LOCATIONS = "# pocket plane locations"
GAM_ZOOM_LEVEL = "Zoom level"
GAM_RANDOM_ENCOUNTER_AREA = "Random encounter area"
GAM_WORLDMAP = "Worldmap"
GAM_CAMPAIGN = "Campaign"
GAM_FAMILIAR_OWNER = "Familiar owner"
GAM_ENCOUNTER_ENTRY = "Encounter entry"
GAM_BESTIARY = "Bestiary"
GAM_OFFSET_END_OF_UNKNOWN_STRUCTURE = "End of unknown structure offset"
GAM_UNKNOWN_STRUCTURE = "Unknown structure"
GAM_POCKET_PLANE = "Pocket plane"

in_file = open(
    'C:\\Users\\Usuario\\OneDrive\\Documentos\\Icewind Dale - Enhanced Edition\\save\\000000001-Quick-Save\\Baldur.gam', 'rb')
game = in_file.read(4)
version = in_file.read(4)
game_time = in_file.read(4)
selected_formation = in_file.read(2)
formation_button_1 = in_file.read(2)
formation_button_2 = in_file.read(2)
formation_button_3 = in_file.read(2)
formation_button_4 = in_file.read(2)
formation_button_5 = in_file.read(2)
party_gold = in_file.read(4)
view_area_of_pt_member = in_file.read(2)
weather = in_file.read(2)
party_members_offset = int.from_bytes(in_file.read(4), byteorder='little', signed=False)
n_party_members = int.from_bytes(in_file.read(4), byteorder='little', signed=False)
party_inventory_offset = in_file.read(4)
n_of_party_inventory_items = in_file.read(4)
non_party_characters_offset = in_file.read(4)
n_non_party_characters = in_file.read(4)
global_variables_offset = in_file.read(4)
n_of_global_variables = in_file.read(4)
world_area = in_file.read(8)
current_link = in_file.read(4)
n_journal_entries = in_file.read(4)
journal_entries_offset = in_file.read(4)
reputation = in_file.read(4)
master_area = in_file.read(8)
configuration = in_file.read(4)
save_version = in_file.read(4)
familiar_info_offset = in_file.read(4)
stored_location_offset = in_file.read(4)
n_of_stored_locations = in_file.read(4)
elapsed_real_time = in_file.read(4)
pocket_plane_locations_offset = in_file.read(4)
n_of_pocket_plane_locations = in_file.read(4)
zoom_level = in_file.read(4)
random_encounter_area = in_file.read(8)
world_map = in_file.read(8)
campaign = in_file.read(8)
familiar_owner = in_file.read(4)
encounter_entry = in_file.read(20)


# in_file.seek(party_members_offset)
def read_character():
    # put a offset
    selection_state = in_file.read(2).decode("utf-8")
    party_position = in_file.read(2).decode("utf-8")
    cre_structure_offset = int.from_bytes(in_file.read(4), byteorder="little")
    cre_structure_size = int.from_bytes(in_file.read(4), byteorder="little")
    character = in_file.read(8).decode("utf-8")
    orientation = int.from_bytes(in_file.read(4), byteorder="little")
    current_area = in_file.read(8).decode("utf-8")
    location_x = int.from_bytes(in_file.read(2), byteorder="little")
    location_y = int.from_bytes(in_file.read(2), byteorder="little")
    viewport_location_x = int.from_bytes(in_file.read(2), byteorder="little")
    viewport_location_y = int.from_bytes(in_file.read(2), byteorder="little")
    modal_state = int.from_bytes(in_file.read(2), byteorder="little")
    happiness = int.from_bytes(in_file.read(2), byteorder="little")
    unused = in_file.read(96)
    quick_weapon_slot_1 = in_file.read(2).decode("utf-8")
    quick_weapon_slot_2 = in_file.read(2).decode("utf-8")
    quick_weapon_slot_3 = in_file.read(2).decode("utf-8")
    quick_weapon_slot_4 = in_file.read(2).decode("utf-8")
    quick_weapon_1_ability = int.from_bytes(
        in_file.read(2), byteorder="little")
    quick_weapon_2_ability = int.from_bytes(
        in_file.read(2), byteorder="little")
    quick_weapon_3_ability = int.from_bytes(
        in_file.read(2), byteorder="little")
    quick_weapon_4_ability = int.from_bytes(
        in_file.read(2), byteorder="little")
    quick_spell_1 = in_file.read(8).decode("utf-8")
    quick_spell_2 = in_file.read(8).decode("utf-8")
    quick_spell_3 = in_file.read(8).decode("utf-8")
    try:
        quick_item_slot_1 = in_file.read(2).decode("utf-8")
    except:
        quick_item_slot_1 = -1
        pass
    try:
        quick_item_slot_2 = in_file.read(2).decode("utf-8")
    except:
        quick_item_slot_2 = -1
        pass
    try:
        quick_item_slot_3 = in_file.read(2).decode("utf-8")
    except:
        quick_item_slot_3 = -1
        pass
    quick_item_1_ability = int.from_bytes(in_file.read(2), byteorder="little")
    quick_item_2_ability = int.from_bytes(in_file.read(2), byteorder="little")
    quick_item_3_ability = int.from_bytes(in_file.read(2), byteorder="little")
    character_name = in_file.read(32).decode("utf-8")
    times_talked_to = int.from_bytes(in_file.read(4), byteorder="little")
    most_powerful_foe_vanquished = in_file.read(4)
    xp_for_most_powerful_foe = int.from_bytes(
        in_file.read(4), byteorder="little")
    time_in_party = int.from_bytes(in_file.read(4), byteorder="little")
    join_time = int.from_bytes(in_file.read(4), byteorder="little")
    currently_in_party = in_file.read(1).decode("utf-8")
    unknown = in_file.read(2)
    initial_character = in_file.read(1).decode("utf-8")
    kill_xp_chapter = int.from_bytes(in_file.read(4), byteorder="little")
    kills_chapter = int.from_bytes(in_file.read(4), byteorder="little")
    kill_xp_game = int.from_bytes(in_file.read(4), byteorder="little")
    kills_game = int.from_bytes(in_file.read(4), byteorder="little")
    favorite_spell_1 = in_file.read(8).decode("utf-8")
    favorite_spell_2 = in_file.read(8).decode("utf-8")
    favorite_spell_3 = in_file.read(8).decode("utf-8")
    favorite_spell_4 = in_file.read(8).decode("utf-8")
    favorite_spell_count_1 = int.from_bytes(
        in_file.read(2), byteorder="little")
    favorite_spell_count_2 = int.from_bytes(
        in_file.read(2), byteorder="little")
    favorite_spell_count_3 = int.from_bytes(
        in_file.read(2), byteorder="little")
    favorite_spell_count_4 = int.from_bytes(
        in_file.read(2), byteorder="little")
    favorite_weapon_1 = in_file.read(8).decode("utf-8")
    favorite_weapon_2 = in_file.read(8).decode("utf-8")
    favorite_weapon_3 = in_file.read(8).decode("utf-8")
    favorite_weapon_4 = in_file.read(8).decode("utf-8")
    favorite_weapon_counter_1 = int.from_bytes(
        in_file.read(2), byteorder="little")
    favorite_weapon_counter_2 = int.from_bytes(
        in_file.read(2), byteorder="little")
    favorite_weapon_counter_3 = int.from_bytes(
        in_file.read(2), byteorder="little")
    favorite_weapon_counter_4 = int.from_bytes(
        in_file.read(2), byteorder="little")
    voice_set = in_file.read(8).decode("utf-8")

    data = {
        "selection_state": selection_state,
        "party_position": party_position,
        "cre_structure_offset": cre_structure_offset,
        "cre_structure_size": cre_structure_size,
        "character": character,
        "orientation": orientation,
        "current_area": current_area,
        "location_x": location_x,
        "location_y": location_y,
        "viewport_location_x": viewport_location_x,
        "viewport_location_y": viewport_location_y,
        "modal_state": modal_state,
        "happiness": happiness,
        "unused": unused,
        "quick_weapon_slot_1": quick_weapon_slot_1,
        "quick_weapon_slot_2": quick_weapon_slot_2,
        "quick_weapon_slot_3": quick_weapon_slot_3,
        "quick_weapon_slot_4": quick_weapon_slot_4,
        "quick_weapon_1_ability": quick_weapon_1_ability,
        "quick_weapon_2_ability": quick_weapon_2_ability,
        "quick_weapon_3_ability": quick_weapon_3_ability,
        "quick_weapon_4_ability": quick_weapon_4_ability,
        "quick_spell_1": quick_spell_1,
        "quick_spell_2": quick_spell_2,
        "quick_spell_3": quick_spell_3,
        "quick_item_slot_1": quick_item_slot_1,
        "quick_item_slot_2": quick_item_slot_2,
        "quick_item_slot_3": quick_item_slot_3,
        "quick_item_1_ability": quick_item_1_ability,
        "quick_item_2_ability": quick_item_2_ability,
        "quick_item_3_ability": quick_item_3_ability,
        "character_name": character_name,
        "times_talked_to": times_talked_to,
        "most_powerful_foe_vanquished": most_powerful_foe_vanquished,
        "xp_for_most_powerful_foe": xp_for_most_powerful_foe,
        "time_in_party": time_in_party,
        "join_time": join_time,
        "currently_in_party": currently_in_party,
        "unknown": unknown,
        "initial_character": initial_character,
        "kill_xp_chapter": kill_xp_chapter,
        "kills_chapter": kills_chapter,
        "kill_xp_game": kill_xp_game,
        "kills_game": kills_game,
        "favorite_spell_1": favorite_spell_1,
        "favorite_spell_2": favorite_spell_2,
        "favorite_spell_3": favorite_spell_3,
        "favorite_spell_4": favorite_spell_4,
        "favorite_spell_count_1": favorite_spell_count_1,
        "favorite_spell_count_2": favorite_spell_count_2,
        "favorite_spell_count_3": favorite_spell_count_3,
        "favorite_spell_count_4": favorite_spell_count_4,
        "favorite_weapon_1": favorite_weapon_1,
        "favorite_weapon_2": favorite_weapon_2,
        "favorite_weapon_3": favorite_weapon_3,
        "favorite_weapon_4": favorite_weapon_4,
        "favorite_weapon_counter_1": favorite_weapon_counter_1,
        "favorite_weapon_counter_2": favorite_weapon_counter_2,
        "favorite_weapon_counter_3": favorite_weapon_counter_3,
        "favorite_weapon_counter_4": favorite_weapon_counter_4,
        "voice_set": voice_set
    }
    return data


def read_creature_cre_info():
    signature = in_file.read(4).decode("utf-8")
    version = in_file.read(4).decode("utf-8")
    try:
        name = in_file.read(4).decode("utf-8")
    except:
        name = -1
        pass
    try:
        tooltip = in_file.read(4).decode("utf-8")
    except:
        tooltip = -1
        pass
    flags = int.from_bytes(in_file.read(4), byteorder="little")
    xp_value = int.from_bytes(in_file.read(4), byteorder="little")
    xp_power_level = int.from_bytes(in_file.read(4), byteorder="little")
    gold = int.from_bytes(in_file.read(4), byteorder="little")
    status = in_file.read(4).decode("utf-8")
    current_hp = int.from_bytes(in_file.read(2), byteorder="little")
    maximum_hp = int.from_bytes(in_file.read(2), byteorder="little")
    animation = in_file.read(4).decode("utf-8")
    metal_color = int.from_bytes(in_file.read(1), byteorder="little")
    minor_color = int.from_bytes(in_file.read(1), byteorder="little")
    major_color = int.from_bytes(in_file.read(1), byteorder="little")
    skin_color = int.from_bytes(in_file.read(1), byteorder="little")
    leather_color = int.from_bytes(in_file.read(1), byteorder="little")
    armor_color = int.from_bytes(in_file.read(1), byteorder="little")
    hair_color = int.from_bytes(in_file.read(1), byteorder="little")
    effect_version = int.from_bytes(in_file.read(1), byteorder="little")
    small_portrait = in_file.read(8).decode("utf-8")
    large_portrait = in_file.read(8).decode("utf-8")
    reputation = int.from_bytes(in_file.read(1), byteorder="little")
    hide_in_shadows = int.from_bytes(in_file.read(1), byteorder="little")
    natural_ac = int.from_bytes(in_file.read(2), byteorder="little")
    effective_ac = int.from_bytes(in_file.read(2), byteorder="little")
    crushing_ac_modifier = int.from_bytes(in_file.read(2), byteorder="little")
    missile_ac_modifier = int.from_bytes(in_file.read(2), byteorder="little")
    piercing_ac_modifier = int.from_bytes(in_file.read(2), byteorder="little")
    slashing_ac_modifier = int.from_bytes(in_file.read(2), byteorder="little")
    thac0 = int.from_bytes(in_file.read(1), byteorder="little")
    attacks_per_round = int.from_bytes(in_file.read(1), byteorder="little")
    save_vs_death = int.from_bytes(in_file.read(1), byteorder="little")
    save_vs_wand = int.from_bytes(in_file.read(1), byteorder="little")
    save_vs_polymorph = int.from_bytes(in_file.read(1), byteorder="little")
    save_vs_breath = int.from_bytes(in_file.read(1), byteorder="little")
    save_vs_spell = int.from_bytes(in_file.read(1), byteorder="little")
    fire_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    cold_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    electricity_resistance = int.from_bytes(
        in_file.read(1), byteorder="little")
    acid_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    magic_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    magic_fire_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    magic_cold_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    slashing_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    crushing_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    piercing_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    missile_resistance = int.from_bytes(in_file.read(1), byteorder="little")
    detect_illusion = int.from_bytes(in_file.read(1), byteorder="little")
    set_traps = int.from_bytes(in_file.read(1), byteorder="little")
    lore = int.from_bytes(in_file.read(1), byteorder="little")
    open_locks = int.from_bytes(in_file.read(1), byteorder="little")
    move_silently = int.from_bytes(in_file.read(1), byteorder="little")
    find_traps = int.from_bytes(in_file.read(1), byteorder="little")
    pick_pockets = int.from_bytes(in_file.read(1), byteorder="little")
    fatigue = int.from_bytes(in_file.read(1), byteorder="little")
    intoxication = int.from_bytes(in_file.read(1), byteorder="little")
    luck = int.from_bytes(in_file.read(1), byteorder="little")
    # Continuing from the previous code...

# Assign values to variables based on attribute size
    large_sword_proficiency = int.from_bytes(
        in_file.read(1), byteorder="little")
    small_sword_proficiency = int.from_bytes(
        in_file.read(1), byteorder="little")
    bow_proficiency = int.from_bytes(in_file.read(1), byteorder="little")
    spear_proficiency = int.from_bytes(in_file.read(1), byteorder="little")
    blunt_proficiency = int.from_bytes(in_file.read(1), byteorder="little")
    spiked_proficiency = int.from_bytes(in_file.read(1), byteorder="little")
    axe_proficiency = int.from_bytes(in_file.read(1), byteorder="little")
    missile_proficiency = int.from_bytes(in_file.read(1), byteorder="little")
    unknown = in_file.read(7).hex()
    nightmare_mode = int.from_bytes(in_file.read(1), byteorder="little")
    translucency = int.from_bytes(in_file.read(1), byteorder="little")
    reputation_gained_when_killed = int.from_bytes(
        in_file.read(1), byteorder="little")
    reputation_gained_when_joining_party = int.from_bytes(
        in_file.read(1), byteorder="little")
    reputation_gained_when_leaving_party = int.from_bytes(
        in_file.read(1), byteorder="little")
    turn_undead_level = int.from_bytes(in_file.read(1), byteorder="little")
    tracking = int.from_bytes(in_file.read(1), byteorder="little")
    target = in_file.read(32).decode("utf-8")
    # skip 400 because of sound files
    in_file.read(400)

    # Define variables for each attribute
    level_first_class = in_file.read(1).decode()
    level_second_class = in_file.read(1).decode()
    level_third_class = in_file.read(1).decode()
    sex = in_file.read(1).decode()
    strength = in_file.read(1).decode()
    strength_bonus = in_file.read(1).decode()
    intelligence = in_file.read(1).decode()
    wisdom = in_file.read(1).decode()
    dexterity = in_file.read(1).decode()
    constitution = in_file.read(1).decode()
    charisma = in_file.read(1).decode()
    morale = in_file.read(1).decode()
    morale_break = in_file.read(1).decode()
    racial_enemy = in_file.read(1).decode()
    morale_recovery = in_file.read(2).decode()
    kit = in_file.read(4).decode()
    override_script = in_file.read(8).decode()
    class_script = in_file.read(8).decode()
    race_script = in_file.read(8).decode()
    general_script = in_file.read(8).decode()
    default_script = in_file.read(8).decode()
    allegiance = in_file.read(1).decode()
    general = in_file.read(1).decode()
    race = in_file.read(1).decode()
    class_type = in_file.read(1).decode()
    specifics = in_file.read(1).decode()
    gender = in_file.read(1).decode()
    object_spec_1 = in_file.read(1).decode()
    object_spec_2 = in_file.read(1).decode()
    object_spec_3 = in_file.read(1).decode()
    object_spec_4 = in_file.read(1).decode()
    object_spec_5 = in_file.read(1).decode()
    alignment = in_file.read(1).decode()
    global_identifier = int.from_bytes(in_file.read(2), byteorder="little")
    local_identifier = int.from_bytes(in_file.read(2), byteorder="little")
    script_name = in_file.read(32).decode()
    known_spells_offset = int.from_bytes(in_file.read(4))
    num_known_spells = in_file.read(4).decode()
    memorization_info_offset = int.from_bytes(in_file.read(4))
    num_memorization_info = in_file.read(4).decode()
    memorized_spells_offset = int.from_bytes(in_file.read(4))
    num_memorized_spells = int.from_bytes(in_file.read(4), byteorder="little")
    item_slots_offset = int.from_bytes(in_file.read(4), byteorder="little")
    items_offset = int.from_bytes(in_file.read(4), byteorder="little")
    num_items = int.from_bytes(in_file.read(4), byteorder="little")
    effects_offset = int.from_bytes(in_file.read(4), byteorder="little")
    num_effects = int.from_bytes(in_file.read(4), byteorder="little")
    dialogue = in_file.read(8).decode()
    known_spell_0 = in_file.read(12).decode()
    memorization_info_0 = in_file.read(16).decode()
    memorization_info_1 = in_file.read(16).decode()
    memorization_info_2 = in_file.read(16).decode()
    memorization_info_3 = in_file.read(16).decode()
    memorization_info_4 = in_file.read(16).decode()
    memorization_info_5 = in_file.read(16).decode()
    memorization_info_6 = in_file.read(16).decode()
    memorization_info_7 = in_file.read(16).decode()
    memorization_info_8 = in_file.read(16).decode()
    memorization_info_9 = in_file.read(16).decode()
    memorization_info_10 = in_file.read(16).decode()
    memorization_info_11 = in_file.read(16).decode()
    memorization_info_12 = in_file.read(16).decode()
    memorization_info_13 = in_file.read(16).decode()
    memorization_info_14 = in_file.read(16).decode()
    memorization_info_15 = in_file.read(16).decode()
    memorization_info_16 = in_file.read(16).decode()
    Helmet = in_file.read(2)
    Armor = in_file.read(2)
    Shield = in_file.read(2)
    Gloves = in_file.read(2)
    Left_ring = in_file.read(2)
    Right_ring = in_file.read(2)
    Amulet = in_file.read(2)
    Belt = in_file.read(2)
    Boots = in_file.read(2)
    Weapon_1 = in_file.read(2)
    Weapon_2 = in_file.read(2)
    Weapon_3 = in_file.read(2)
    Weapon_4 = in_file.read(2)
    Quiver_1 = in_file.read(2)
    Quiver_2 = in_file.read(2)
    Quiver_3 = in_file.read(2)
    Quiver_4 = in_file.read(2)
    Cloak = in_file.read(2)
    Quick_item_1 = in_file.read(2)
    Quick_item_2 = in_file.read(2)
    Quick_item_3 = in_file.read(2)
    Inventory_1 = in_file.read(2)
    Inventory_2 = in_file.read(2)
    Inventory_3 = in_file.read(2)
    Inventory_4 = in_file.read(2)
    Inventory_5 = in_file.read(2)
    Inventory_6 = in_file.read(2)
    Inventory_7 = in_file.read(2)
    Inventory_8 = in_file.read(2)
    Inventory_9 = in_file.read(2)
    Inventory_10 = in_file.read(2)
    Inventory_11 = in_file.read(2)
    Inventory_12 = in_file.read(2)
    Inventory_13 = in_file.read(2)
    Inventory_14 = in_file.read(2)
    Inventory_15 = in_file.read(2)
    Inventory_16 = in_file.read(2)
    Magically_created_weapon = in_file.read(2)
    Weapon_slot_selected = in_file.read(2)
    Weapon_ability_selected = in_file.read(2)
    item_0 = in_file.read(20)
    item_1 = in_file.read(20)
    item_2 = in_file.read(20)
    item_3 = in_file.read(20)
    item_4 = in_file.read(20)
    item_5 = in_file.read(20)
    item_6 = in_file.read(20)
    item_7 = in_file.read(20)
    item_8 = in_file.read(20)
    item_9 = in_file.read(20)
    item_10 = in_file.read(20)
    item_11 = in_file.read(20)
    item_12 = in_file.read(20)
    item_13 = in_file.read(20)
    item_14 = in_file.read(20)
    item_15 = in_file.read(20)
    item_16 = in_file.read(20)
    item_17 = in_file.read(20)
    item_18 = in_file.read(20)
    item_19 = in_file.read(20)
    item_20 = in_file.read(20)
    item_21 = in_file.read(20)
    item_22 = in_file.read(20)
    item_23 = in_file.read(20)
    item_24 = in_file.read(20)
    item_25 = in_file.read(20)
    # Create a dictionary with the variables as properties and assign the variables
    data = {
        "signature": signature,
        "version": version,
        "name": name,
        "tooltip": tooltip,
        "flags": flags,
        "xp_value": xp_value,
        "xp_power_level": xp_power_level,
        "gold": gold,
        "status": status,
        "current_hp": current_hp,
        "maximum_hp": maximum_hp,
        "animation": animation,
        "metal_color": metal_color,
        "minor_color": minor_color,
        "major_color": major_color,
        "skin_color": skin_color,
        "leather_color": leather_color,
        "armor_color": armor_color,
        "hair_color": hair_color,
        "effect_version": effect_version,
        "small_portrait": small_portrait,
        "large_portrait": large_portrait,
        "reputation": reputation,
        "hide_in_shadows": hide_in_shadows,
        "natural_ac": natural_ac,
        "effective_ac": effective_ac,
        "crushing_ac_modifier": crushing_ac_modifier,
        "missile_ac_modifier": missile_ac_modifier,
        "piercing_ac_modifier": piercing_ac_modifier,
        "slashing_ac_modifier": slashing_ac_modifier,
        "thac0": thac0,
        "attacks_per_round": attacks_per_round,
        "save_vs_death": save_vs_death,
        "save_vs_wand": save_vs_wand,
        "save_vs_polymorph": save_vs_polymorph,
        "save_vs_breath": save_vs_breath,
        "save_vs_spell": save_vs_spell,
        "fire_resistance": fire_resistance,
        "cold_resistance": cold_resistance,
        "electricity_resistance": electricity_resistance,
        "acid_resistance": acid_resistance,
        "magic_resistance": magic_resistance,
        "magic_fire_resistance": magic_fire_resistance,
        "magic_cold_resistance": magic_cold_resistance,
        "slashing_resistance": slashing_resistance,
        "crushing_resistance": crushing_resistance,
        "piercing_resistance": piercing_resistance,
        "missile_resistance": missile_resistance,
        "detect_illusion": detect_illusion,
        "set_traps": set_traps,
        "lore": lore,
        "open_locks": open_locks,
        "move_silently": move_silently,
        "find_traps": find_traps,
        "pick_pockets": pick_pockets,
        "fatigue": fatigue,
        "intoxication": intoxication,
        "luck": luck,
        "large_sword_proficiency": large_sword_proficiency,
        "small_sword_proficiency": small_sword_proficiency,
        "bow_proficiency": bow_proficiency,
        "spear_proficiency": spear_proficiency,
        "blunt_proficiency": blunt_proficiency,
        "spiked_proficiency": spiked_proficiency,
        "axe_proficiency": axe_proficiency,
        "missile_proficiency": missile_proficiency,
        "unknown": unknown,
        "nightmare_mode": nightmare_mode,
        "translucency": translucency,
        "reputation_gained_when_killed": reputation_gained_when_killed,
        "reputation_gained_when_joining_party": reputation_gained_when_joining_party,
        "reputation_gained_when_leaving_party": reputation_gained_when_leaving_party,
        "turn_undead_level": turn_undead_level,
        "tracking": tracking,
        "target": target,

        "level_first_class": level_first_class,
        "level_second_class": level_second_class,
        "level_third_class": level_third_class,
        "sex": sex,
        "strength": strength,
        "strength_bonus": strength_bonus,
        "intelligence": intelligence,
        "wisdom": wisdom,
        "dexterity": dexterity,
        "constitution": constitution,
        "charisma": charisma,
        "morale": morale,
        "morale_break": morale_break,
        "racial_enemy": racial_enemy,
        "morale_recovery": morale_recovery,
        "kit": kit,
        "override_script": override_script,
        "class_script": class_script,
        "race_script": race_script,
        "general_script": general_script,
        "default_script": default_script,
        "allegiance": allegiance,
        "general": general,
        "race": race,
        "class_type": class_type,
        "specifics": specifics,
        "gender": gender,
        "object_spec_1": object_spec_1,
        "object_spec_2": object_spec_2,
        "object_spec_3": object_spec_3,
        "object_spec_4": object_spec_4,
        "object_spec_5": object_spec_5,
        "alignment": alignment,
        "global_identifier": global_identifier,
        "local_identifier": local_identifier,
        "script_name": script_name,
        "known_spells_offset": known_spells_offset,
        "num_known_spells": num_known_spells,
        "memorization_info_offset": memorization_info_offset,
        "num_memorization_info": num_memorization_info,
        "memorized_spells_offset": memorized_spells_offset,
        "num_memorized_spells": num_memorized_spells,
        "item_slots_offset": item_slots_offset,
        "items_offset": items_offset,
        "num_items": num_items,
        "effects_offset": effects_offset,
        "num_effects": num_effects,
        "dialogue": dialogue,
        "known_spell_0": known_spell_0,
        "memorization_info_0": memorization_info_0,
        "memorization_info_1": memorization_info_1,
        "memorization_info_2": memorization_info_2,
        "memorization_info_3": memorization_info_3,
        "memorization_info_4": memorization_info_4,
        "memorization_info_5": memorization_info_5,
        "memorization_info_6": memorization_info_6,
        "memorization_info_7": memorization_info_7,
        "memorization_info_8": memorization_info_8,
        "memorization_info_8": memorization_info_8,
        "memorization_info_9": memorization_info_9,
        "memorization_info_10": memorization_info_10,
        "memorization_info_11": memorization_info_11,
        "memorization_info_12": memorization_info_12,
        "memorization_info_13": memorization_info_13,
        "memorization_info_14": memorization_info_14,
        "memorization_info_15": memorization_info_15,
        "memorization_info_16": memorization_info_16,

        "Helmet": Helmet,
        "Armor": Armor,
        "Shield": Shield,
        "Gloves": Gloves,
        "Left_ring": Left_ring,
        "Right_ring": Right_ring,
        "Amulet": Amulet,
        "Belt": Belt,
        "Boots": Boots,
        "Weapon_1": Weapon_1,
        "Weapon_2": Weapon_2,
        "Weapon_3": Weapon_3,
        "Weapon_4": Weapon_4,
        "Quiver_1": Quiver_1,
        "Quiver_2": Quiver_2,
        "Quiver_3": Quiver_3,
        "Quiver_4": Quiver_4,
        "Cloak": Cloak,
        "Quick_item_1": Quick_item_1,
        "Quick_item_2": Quick_item_2,
        "Quick_item_3": Quick_item_3,
        "Inventory_1": Inventory_1,
        "Inventory_2": Inventory_2,
        "Inventory_3": Inventory_3,
        "Inventory_4": Inventory_4,
        "Inventory_5": Inventory_5,
        "Inventory_6": Inventory_6,
        "Inventory_7": Inventory_7,
        "Inventory_8": Inventory_8,
        "Inventory_9": Inventory_9,
        "Inventory_10": Inventory_10,
        "Inventory_11": Inventory_11,
        "Inventory_12": Inventory_12,
        "Inventory_13": Inventory_13,
        "Inventory_14": Inventory_14,
        "Inventory_15": Inventory_15,
        "Inventory_16": Inventory_16,
        "Magically_created_weapon": Magically_created_weapon,
        "Weapon_slot_selected": Weapon_slot_selected,
        "Weapon_ability_selected": Weapon_ability_selected,

        "item_0": item_0,
        "item_1": item_1,
        "item_2": item_2,
        "item_3": item_3,
        "item_4": item_4,
        "item_5": item_5,
        "item_6": item_6,
        "item_7": item_7,
        "item_8": item_8,
        "item_9": item_9,
        "item_10": item_10,
        "item_11": item_11,
        "item_12": item_12,
        "item_13": item_13,
        "item_14": item_14,
        "item_15": item_15,
        "item_16": item_16,
        "item_17": item_17,
        "item_18": item_18,
        "item_19": item_19,
        "item_20": item_20,
        "item_21": item_21,
        "item_22": item_22,
        "item_23": item_23,
        "item_24": item_24,
        "item_25": item_25

    }
    return data

character_size_in_bytes = 352

def party():
    party = []
    # iterate through party members
    for i in range(0, n_party_members):
        in_file.seek(party_members_offset + i * character_size_in_bytes)
        pt_member = read_character()
        print(pt_member['character_name'])
        offset = pt_member['cre_structure_offset']
        in_file.seek(offset)
        cre = read_creature_cre_info()
        party.append({ 'member': pt_member,
                       'creature': cre })
