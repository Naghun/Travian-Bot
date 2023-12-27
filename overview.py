# functions

def first_app_timers():
    """
    take current time
    make first timer refresh and set it to refresh variable
    take next 24 timer resets for 15minutes
    save it in database in db called reset_timers
    if 15minutes refresh read every if 30 read every second starting from 1 not 0
    """

def set_timer():
    """
    get time list from database
    read first item and pop it
    read whole list
    take last time frame
    make new time frame from last plus ~30minutes
    append to list
    save list to db
    display list to pyside
    """

    #set next refresh at ----


def main():
    # if app_first_open: -> start first_app_timers()
    refresh= '' #time we take when we open app for the first time
    # call start_bot() ----> set bot to automatically open at refresh time
    # bot will start new window and do all the tasks
    # call set_timer to set new refresh time
    # close the window

def preparations():
    """
    get_cookies from database
    prepare undetected chrome driver
    start_bot()
    """

def start_bot():
    """
    get_url
    open login and login with data given
    do_tasks()
    """

def get_info():
    """
    get info for all villages get tribe
    get resources
    get resource_field_levels
    get building_field_levels
    get troops
    get incoming_attacks
    get construction_slots with info about tribe (romans 3 slots)
    """

def send_farms():
    # open village1
    # open farm_lists
    # choose option and start farms
    pass

def do_tasks():
    """
    get all tasks from db
    loop over them
    if task.id == 1
        open_desired_village(1)
    etc...
    after looping over one task get another village task
    """

def open_desired_village():
    """
    after get_info() is completed scan for tasks from database
    start from village1 tasks
    if start_farm then start_farm
    open resource_page
    check_tribe and check construction
    if roman const slots needs to be 3
    if resource_tasks then build_resource()
    if village_task then build_building
    if train_troops then train_troops
    if train_expansion_units then -||-
    if research_unit then research_unit
    if advance_armor then advance_armor
    if solo_attack then solo_attack()
    if conquer oasis then conquer oasis
    if make_npc then make_npc
    # later option send_resources
    # later option destroy_building
    """

def close_bot():
    #just quittting bot
    pass

def resource_task():
    """
    open_resources_page()
    choose_field(argument about field)
    read_construction_requirements and read_current_resources
    if all_requirements_satisfied start_building if not break action and send correct information
    push_task into next refresh timer at first place
    """

def building_task():
    """
    open_village_page()
    get_building_slot()     -   to check weather field is empty or just needs upgrade
    open_building_slot()
    if empty ---> find building ---> check construction cost ---> get current_resources ---> if satisfied start_build()
    if not_empty ---> check construction cost ---> get current_resources ---> if satisfied start_build()
    if not satisfied send message and push into next refresh timer
    """

def set_npc():
    """
    open db and clear all
    fill out the form about resource division
    send_form to database and save
    """

def make_npc():
    """
    get npc details from databse
    divide resources into variables wood, clay, wheat, iron
    open npc_time in sidebar
    open npc tab
    in fields enter resources amounts accordingly
    read text in button if divide then press and wait for npc if npc press npc
    """

def train_other():
    pass