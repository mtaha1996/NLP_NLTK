import sys
import os


# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# for i in sys.argv:
#     print(str(i))

def get_args():
    if len(sys.argv) == 2:
        input_file = sys.argv[1]

        if input_file == "fables":
            print(input_file)
            pass
        elif input_file == "blogs":
            print(input_file)
            pass

        else:
            print("Error in name")

    else:
        print("Error in getting arg!")


if __name__ == "__main__":
    get_args()
else:
    print("Executed when imported")
