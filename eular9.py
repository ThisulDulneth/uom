# Euler 9: Special Pythagorean triplet

def find_triplet_product(sum_total):
    for a in range(1, sum_total // 3):
        for b in range(a + 1, sum_total // 2):
            c = sum_total - a - b
            if a * a + b * b == c * c:
                return a * b * c

if __name__ == "__main__":
    result = find_triplet_product(1000)
    print(result)