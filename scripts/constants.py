

class Login:
    login_page_link = "https://sow.x1.arabics.travian.com/"

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
    new_building_button_rallypoint = f'#contract_building16 > div.contractLink > button[value = "Izgraditi građevinu"]'
    new_building_button_main_building = f'#contract_building15 > div.contractLink > button[value = "Izgraditi građevinu"]'
    building_button = f'#build > div.upgradeBuilding > div.upgradeButtonsContainer.section2Enabled > div.section1 > button[value*="Unaprijedi"]'


class ResourceFieldSlots:
    def __init__(self, resource_field_slot):
        self.resource_field = f"#resourceFieldContainer > a.level.colorLayer.buildingSlot{resource_field_slot}"
    
    resource_field_button = '#build > div.upgradeBuilding > div.upgradeButtonsContainer > div.section1 > button[value*="Unaprijedi"]'

class FarmsRaidsAttacks:
    rallypoint = f'#villageContent > div.buildingSlot.a39.g16.aid39 > a'
    send_troops_tab = f'#content > div.contentNavi.subNavi > div > div.content.favor.favorKey2 > a'
    farm_list_tab = f'#content > div.contentNavi.subNavi > div > div.content.favor.favorKey99 > a'
    start_all_farms = f'#stickyWrapper > button.textButtonV2.buttonFramed.startAllFarmLists.rectangle.withText.green > div'
    #stickyWrapper > button.textButtonV2.buttonFramed.startAllFarmLists.rectangle.withText.green

class Market:
    market = f'#villageContent > div.buildingSlot.a32.g17.aid32 > a'
    npc_button = f'#build > div.npcMerchant > button'