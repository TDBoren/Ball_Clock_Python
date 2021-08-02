def run_12h(balls):
    hour = []
    five_min = []
    one_min = []
    # Define how many minutes in a 12 hour period
    for i in range(12 * 60):
        ball, balls = balls[0], balls[1:]
        # Define row 1 of the ball clock
        if len(one_min) < 4:
            one_min.append(ball)
        else:
            one_min.reverse()
            balls.extend(one_min)
            one_min = []
            # Define row 2 of the ball clock
            if len(five_min) < 11:
                five_min.append(ball)
            else:
                five_min.reverse()
                balls.extend(five_min)
                five_min = []
                # Define row 3 of the ball clock
                if len(hour) < 11:
                    hour.append(ball)
                else:
                    hour.reverse()
                    balls.extend(hour)
                    hour = []
                    balls.append(ball)
    return balls


# Create a table to store the number of balls

def shift_table(balls):
    table = balls[:]
    for i, ball in enumerate(balls):
        table[ball] = i
    return table


# Count the number of balls in the circle table

def circle(table):
    def lookup(i):
        old = i
        count = 1
        while table[old] != i:
            count += 1
            old = table[old]
        return count

    return map(lookup, range(len(table)))


# Solve for how many times a ball returns to its original position

def get_common_denominator(x, y):
    if y == 0:
        return x
    else:
        return get_common_denominator(y, x % y)


def least_common_multiplier(x, y):
    return x * y / get_common_denominator(x, y)


def solve(n):
    return reduce(least_common_multiplier, circle(shift_table(run_12h(range(n))))) / 2


if __name__ == '__main__':
    print('Please put in a number between 27 and 127')
    user_range = int(input())
    print("{} balls take {} days".format(user_range, solve(user_range)))
