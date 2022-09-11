import threading

from multiprocessing import Process

import datetime

def lucky_ticket1 (range_start, range_finish):
    lucky_tickets = []
    for itm in range(range_start, range_finish):
        ticket = f"{itm:06}"
        sum_first_part_of_ticket = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
        sum_second_part_of_ticket = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
        if sum_first_part_of_ticket == sum_second_part_of_ticket:
            lucky_tickets.append(ticket)


    return len(lucky_tickets)

if __name__ == '__main__':
    proc1 = Process(target=lucky_ticket1, args=(1, 500000))
    proc2 = Process(target=lucky_ticket1, args=(500001, 999999))

    thread1 = threading.Thread(target=lucky_ticket1, args=(1, 500000))
    thread2 = threading.Thread(target=lucky_ticket1, args=(500001, 999999))


    start_processes = datetime.datetime.now()
    print(f">>>>>>>>>>>>>>  start Processes in {start_processes.strftime('%H:%M:%S:%f')}")

    proc1.start()
    proc2.start()


    proc1.join()
    proc2.join()

    finish_processes = datetime.datetime.now()
    print(f">>>>>>>>>>>>>>  finish Processes in {finish_processes.strftime('%H:%M:%S:%f')}")

    start_thread = datetime.datetime.now()
    print(f">>>>>>>>>>>>>>  start Thread in {start_thread.strftime('%H:%M:%S:%f')}")

    thread1.start()
    thread2.start()


    thread1.join()
    thread2.join()
    finish_thread = datetime.datetime.now()
    print(f">>>>>>>>>>>>>>  finish Thread in {finish_thread.strftime('%H:%M:%S:%f')}")

    delta_proc = finish_processes - start_processes
    print(f"Delta time of Processes {delta_proc}")

    delta_thread = finish_thread - start_thread
    print(f"Delta time of Threads {delta_thread}")


