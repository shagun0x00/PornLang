import os
import sys

STACK = []

def get_code(file_name: str, list_format=False) -> str:
    with open(file_name, "r") as f:
        if list_format:
            return f.readlines()
        else:
            return f.read()


def check_validity(list_of_lines):
    if list_of_lines[0].strip() == "ah" and list_of_lines[-1].strip() == "ahhhhhhh":
        return True
    else:
        return False


def get_main_code(list_of_instructions):
    code = list_of_instructions
    code = list(code)
    code.remove("ah\n")
    try:
        code.remove("ahhhhhhh")
    except:
        code.remove("ahhhhhhh\n")
    return code



def execute_instructions(instruction_list: list):
    #print(instruction_list)
    for index, instruction in enumerate(instruction_list):
        instruction_counter = index+2
        instruction = instruction.replace("\n", "")

        parsed_line_list = instruction.split(" ")
        if parsed_line_list[0].lower() == "baby" and parsed_line_list[1].lower() == "say":
            print(" ".join(parsed_line_list[2:]))

        elif parsed_line_list[0].lower() == "take" and parsed_line_list[2] == "baby":
            value = parsed_line_list[1]
            STACK.append(value)
            #print(STACK)
        elif parsed_line_list[0].lower() == "give" and parsed_line_list[2] == "to" and parsed_line_list[3] == "me" and parsed_line_list[4] == "baby":
            try:
                value = STACK.pop()
            except IndexError:
                print(f"\033[91mbaby!! you didn't give me anything....\nat line {instruction_counter}")
                exit()
            print(value)
        else:
            print("\033[91mbaby! i'm not understanding what are you saying.")
            exit()


def main():
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("""
            Usage: python main.py <filename.prn>
        """)
        return
    try:
        filename = arguments[0]
        code = get_code(file_name=filename, list_format=True)
        if check_validity(code):
            main_code = get_main_code(code)
            execute_instructions(main_code)

    except Exception as e:
        print("fuckbbkbkhh", e)


if __name__ == "__main__":
    main()
