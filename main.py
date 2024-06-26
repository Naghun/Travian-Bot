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

    with open('scripts/refresh.py', 'r') as file:
        code = compile(file.read(), 'refresh.py', 'exec')
        exec(code, globals(), locals())

    ref_time = locals().get('refresh_time', None)
    ref_id = locals().get('refresh_id', None)
    print("Refresh time is: ", ref_time.strftime('%H:%M:%S'))
    print("ID is: ", ref_id)

    try:
        bot = TravianBot()
        bot.login_to_gmail()
        bot.open_login_page()
        bot.enter_login_data()
        while True:
            current_time = datetime.datetime.now()
            with open('scripts/refresh.py', 'r') as file:
                code = compile(file.read(), 'refresh.py', 'exec')
                exec(code, globals(), locals())

            ref_time = locals().get('refresh_time', None)
            ref_id = locals().get('refresh_id', None)
            if ref_time <= current_time:
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
                new_time_id = locals().get('refresh_id', None)

                print()
                print("#"*10)
                print()

                bot.execute_tasks()
                
                print()
                print("BOT CLOSED!!!")
                print("#"*50)
                print("Refresh time is: ", new_time.strftime('%H:%M:%S'))
                print("ID is: ", new_time_id)
                print()

            time.sleep(60)

    except KeyboardInterrupt:
        print("Program terminated.")


main()