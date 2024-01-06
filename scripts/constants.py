

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


class VillageSlots:
    def __init__(self, slot_number, tribe = ''):
        self.building = self.building_slot = f"#villageContent > div.buildingSlot.a{slot_number}.aid{slot_number}.{tribe} > svg > path"
        self.empty_building_slot= self.building.replace('.g0', '').replace(' > svg > path', '')