

class Login:
    login_page_link = "https://nys.x1.arabics.travian.com/"

    login_name = "Naghun"
    login_password = "sifraboliglava97"

    login_name_field = "#loginForm > tbody > tr.account > td > input"
    login_password_field = "#loginForm > tbody > tr.pass > td > input"

    login_button_submit = "#loginForm > tbody > tr.loginButtonRow > td > button"

class Base:
    def __init__(self, village_number_statistic=1, village_number=1):
        self.village_statistic_table_rows = f"#overview > tbody > tr:nth-child({village_number_statistic}) > td"
        self.village = f"#sidebarBoxVillagelist > div.content > div.villageList > div.dropContainer:nth-child({village_number}) > div.listEntry > a"
    resource_page = "#navigation > a.village.resourceView"
    village_Page = "#navigation > a.village.buildingView"
    map_page = "#navigation > a.map"
    statistic_page = "#navigation > a.statistics"


    current_wood = "#l1"
    current_clay = "#l2"
    current_iron = "#l3"
    current_wheat = "#l4"

    wood_for_construction = "#contract > div.inlineIconList.resourceWrapper > div:nth-child(1) > span"
    clay_for_construction = "#contract > div.inlineIconList.resourceWrapper > div:nth-child(2) > span"
    iron_for_construction = "#contract > div.inlineIconList.resourceWrapper > div:nth-child(3) > span"
    wheat_for_construction = "#contract > div.inlineIconList.resourceWrapper > div:nth-child(4) > span"


class VillageSlots:
    def __init__(self, slot_number, tribe = None, new_building_number = None, build_type = 1):
        self.empty_building = f"#villageContent > div.buildingSlot.a{slot_number}.g0.aid{slot_number}.{tribe} > svg > path"
        self.building_slot= f"#villageContent > div.buildingSlot.a{slot_number}.aid{slot_number}.{tribe} > a"
        self.new_building_button = f'#contract_building{new_building_number} > div.contractLink > button[value = "Izgraditi građevinu"]'
        self.change_build_types = f'#build > div.contentNavi.subNavi > div > div:nth-child({build_type}) > a'
    new_building_button_rallypoint = '#contract_building16 > div.contractLink > button[value = "Izgraditi građevinu"]'
    new_building_button_main_building = '#contract_building15 > div.contractLink > button[value = "Izgraditi građevinu"]'
    building_button = '#build > div.upgradeBuilding > div.upgradeButtonsContainer > div.section1 > button[value*="Unaprijedi"]'


class ResourceFieldSlots:
    def __init__(self, resource_field_slot):
        self.resource_field = f"#resourceFieldContainer > a.level.colorLayer.buildingSlot{resource_field_slot}"
    
    resource_field_button = '#build > div.upgradeBuilding > div.upgradeButtonsContainer > div.section1 > button[value*="Unaprijedi"]'

class FarmsRaidsAttacks:
    rallypoint = '#villageContent > div.buildingSlot.a39.g16.aid39 > a'
    send_troops_tab = '#content > div.contentNavi.subNavi > div > div.content.favor.favorKey2 > a'
    farm_list_tab = '#content > div.contentNavi.subNavi > div > div.content.favor.favorKey99 > a'
    start_all_farms = '#stickyWrapper > button.textButtonV2.buttonFramed.startAllFarmLists.rectangle.withText.green > div'
    quick_link = "#sidebarBoxLinklist > div.content > ul > li > a"
    farm_list1 = '#rallyPointFarmList > div.villageWrapper > div:nth-child(2) > div > div.farmListHeader > button'
    farm_list2 = '#rallyPointFarmList > div.villageWrapper > div:nth-child(3) > div > div.farmListHeader > button'
    farm_list3 = '#rallyPointFarmList > div.villageWrapper > div:nth-child(4) > div > div.farmListHeader > button'
    farm_list4 = '#rallyPointFarmList > div.villageWrapper > div:nth-child(5) > div > div.farmListHeader > button'



class Market:
    market = '#villageContent > div.buildingSlot.a32.g17.aid32 > a'
    npc_button = '#build > div.npcMerchant > button'
    wood_input = '#npc > tbody > tr:nth-child(1) > td:nth-child(1) > input'
    clay_input = '#npc > tbody > tr:nth-child(1) > td:nth-child(2) > input'
    iron_input = '#npc > tbody > tr:nth-child(1) > td:nth-child(3) > input'
    wheat_input = '#npc > tbody > tr:nth-child(1) > td:nth-child(4) > input'
    npc_button_allocate = '#submitText > button'
    npc_button_confirm = '#submitButton > button'

class Map:
    x_coordinates = '#xCoordInput'
    y_coordinates = '#yCoordInput'
    raid_checkbox = '#build > div > form > div.option > label:nth-child(5) > input'
    hero_input = '#troops > tbody > tr:nth-child(3) > td.line-last.column-last.small > input'
    hero_input_click = "#troops > tbody > tr:nth-child(3) > td.line-last.column-last.small > a"
    send_troops_link = "#sidebarBoxLinklist > div.content > ul > li:nth-child(2) > a"
    oasis_decider = '#troop_info > tbody > tr:nth-child(1) > td'
    send_raid = '#tileDetails > div.detailImage > div:nth-child(1) > div:nth-child(2) > a'
    confirm_sending_hero1 = "#ok"
    confirm_sending_hero2 = '#rallyPointButtonsContainer > button[value="Potvrdi"]'
