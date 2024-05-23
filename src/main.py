from utils.genericUtils import calculate_square_root

def runner(num):
    sq = calculate_square_root(num)
    return sq

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(runner(num))