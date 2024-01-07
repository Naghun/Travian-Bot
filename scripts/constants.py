

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
    def __init__(self, slot_number, tribe = None):
        self.empty_building = f"#villageContent > div.buildingSlot.a{slot_number}.g0.aid{slot_number}.{tribe} > svg > path"
        self.building_slot= f"#villageContent > div.buildingSlot.a{slot_number}.g15.aid{slot_number}.{tribe}"

class ResourceFieldSlots:
    def __init__(self, resource_field_type, resource_field_slot):
        self.resource_field = f"#resourceFieldContainer > svg.resourceField.resourceField{resource_field_type} > path.buildingSlot{resource_field_slot}"
    
    resource_field_button = '#build > div.upgradeBuilding > div.upgradeButtonsContainer > div.section1 > button[value*="Unaprijedi"]'