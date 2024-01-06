from scripts.travian_bot import TravianBot
from scripts.timers import TimeManager
import time, datetime

def main():

    ###################################################################
    ########################      SETUP      ##########################
    ###################################################################

    timers = TimeManager()

    ###################################################################
    ########################      START      ##########################
    ###################################################################

    print("*"*50)
    print("Starting App")
    print("*"*50)
    print("Preparing Databases and refresh timers...")
    print("-"*40)
    timers.make_start_timers()
    print("-"*40)
    print("Setting first refresh!")
    print("-"*40)
    timers.set_first_refresh()


    ###################################################################
    #######################      PROGRAM      #########################
    ###################################################################

    print("#"*60)
    print("-"*20, " Program starts! ", "-"*20)
    print("#"*60)

    ref = None

    with open('scripts/refresh.py', 'r') as file:
        code = compile(file.read(), 'refresh.py', 'exec')
        exec(code, globals(), locals())

    ref_time = locals().get('refresh_time', None)
    ref_id = locals().get('refresh_id', None)
    print("Refresh time is: ", ref_time.strftime('%H:%M:%S'))

    try:
        while True:
            current_time = datetime.datetime.now()
            with open('scripts/refresh.py', 'r') as file:
                code = compile(file.read(), 'refresh.py', 'exec')
                exec(code, globals(), locals())

            ref_time = locals().get('refresh_time', None)
            ref_id = locals().get('refresh_id', None)
            if ref_time <= current_time:
                bot = TravianBot()
                print("#"*50)
                print("Refresh time reached!!!")
                print("#"*50)
                timers.get_refresh_timer()
                bot.get_tasks_for_current_timer(ref_id)
                timers.delete_first_timer_add_last_timer()

                with open('scripts/refresh.py', 'r') as file:
                    code = compile(file.read(), 'refresh.py', 'exec')
                    exec(code, globals(), locals())

                new_time = locals().get('refresh_time', None)
                print("Refresh time is: ", new_time.strftime('%H:%M:%S'))

                print()
                print("#"*10)
                print()

                bot.execute_tasks()
                
                print()
                print("#"*10)
                print()

            time.sleep(60)

    except KeyboardInterrupt:
        print("Petlja je prekinuta tastaturom.")


    ###################################################################
    ########################      TESTING     #########################
    ###################################################################


    #timers = TimeManager()
    #bot = TravianBot()
        

    #timer.delete_timers()
    #timer.make_start_timers()
    #timer.get_refresh_timer()
    #timer.create_starter_tasks()
    #timer.delete_tasks()
    #timer.execute_tasks()
    #timer.make_task()

    #bot.open_login_page()
    #bot.enter_login_data()
    #bot.get_villages_data()
    #bot.wait()
    #bot.perform_task()
    #bot.change_village()
    #bot.wait()
    #bot.check_construction()
    #bot.execute_tasks(refresh=4)


main()