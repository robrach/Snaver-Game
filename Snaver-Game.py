from blessed import Terminal
import time
import random
# from time import sleep

term = Terminal()

key = ''

lines = [
    "░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
]

line_with_snake = \
    "S░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

countdown_timer = 30
score = 0


def print_headers():
    print("Score:", score)
    print("Countdown timer:", round(countdown_timer))


def draw_lines():
    for line in lines:
        print(line)


def draw_line_with_snake():
    print(line_with_snake)


def check_if_the_snake_caught_the_block(lines, snake_position):
    block_position = lines[-1].find("█")
    if snake_position == block_position:
        return True


def read_the_key():
    with term.cbreak():
        time_start = time.time()
        val = term.inkey(timeout=0.2)
        remaining_time = time.time() - time_start
        # if val:
        #     sleep(remaining_time)
        return val.name, remaining_time


def find_snake_position(line_with_snake):
    snake_position = line_with_snake.find("S")
    return snake_position


def move_the_snake(snake_position, key, line_with_snake):
    characters_list = list(line_with_snake)
    characters_list[snake_position] = "░"
    if key == "KEY_RIGHT":
        characters_list[snake_position+1] = "S"
    elif key == "KEY_LEFT":
        characters_list[snake_position-1] = "S"
    else:
        characters_list[snake_position] = "S"
    new_line_with_snake = "".join(characters_list)
    return new_line_with_snake


def modify_lines(lines):
        lines.pop()
        possibilities = ["empty_line", "line_with_block"]
        random_line = random.choice(possibilities)
        new_line = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
        if random_line == "line_with_block":
            block_position = random.randint(0, (len(new_line)-1))
            print("Block position:", block_position)    # This print is just for analysis / debugging.
            new_line_list = list(new_line)
            new_line_list[block_position] = "█"
            new_line = "".join(new_line_list)
        lines.insert(0, new_line)
        return lines


if __name__ == '__main__':
    while countdown_timer > 0:
        start = time.time()
        # print(term.clear)   # I can comment that line if I want to see printing the game board step by step.
        print_headers()
        draw_lines()
        draw_line_with_snake()
        key, remaining_time = read_the_key()
        snake_position = find_snake_position(line_with_snake)
        point = check_if_the_snake_caught_the_block(lines, snake_position)
        if point:
            score += 1
        line_with_snake = move_the_snake(snake_position, key, line_with_snake)
        print(remaining_time)   # This print is just for analysis / debugging.
        lines = modify_lines(lines)
        time_lapse = time.time() - start
        countdown_timer -= time_lapse