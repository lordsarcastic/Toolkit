from random import choice


START_TIME = 8
END_TIME = 16
GAP = 2


def show_time(sequence):
    for i in sequence:
        print(f"""
                Time in: {i[0]}
                Time out: {i[1]}
                ---------------
        """)

def generate_time(count):
    times = list()

    for i in range(count):
        start_hour = choice(
            range(START_TIME, END_TIME - GAP - 1)
        )
        start_minute = choice(range(0, 60))
        end_hour = start_hour + GAP
        start_time = f'{start_hour}:{start_minute}'
        end_time = f'{end_hour}:{start_minute}'
        times.append([start_time, end_time])

    show_time(times)


if __name__  == '__main__':
    generate_time(30)
