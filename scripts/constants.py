

class Login:
    login_page_link = "https://sow.x1.arabics.travian.com/"

    login_name = "Naghun"
    login_password = "sifraboliglava97"

    login_name_field = "#loginForm > tbody > tr.account > td > input"
    login_password_field = "#loginForm > tbody > tr.pass > td > input"

    login_button_submit = "#loginForm > tbody > tr.loginButtonRow > td > button"

class Base:
    def __init__(self, village_number=1, village=1):
        self.village_statistic_table_rows = f"#overview > tbody > tr:nth-child({village_number}) > td"
        self.village = f"#sidebarBoxVillagelist > div.content > div.villageList > div.dropContainer:nth-child({village}) > div.listEntry > a"
    resource_page = "#navigation > a.village.resourceView"
    village_Page = "#navigation > a.village.buildingView"
    map_page = "#navigation > a.map"
    statistic_page = "#navigation > a.statistics"

    village_statistic = "#sidebarBoxVillagelist > div.header > div > a"

    current_wood = "#l1"
    current_clay = "#l2"
    current_iron = "#l3"
    current_wheat = "#l4"

