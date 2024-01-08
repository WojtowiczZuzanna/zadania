def f(arr2D):
    row_count = len(arr2D)
    column_count = len(arr2D[0]) if arr2D else 0

    column_sums = []
    for col in range(column_count):
        column_sums.append(sum(arr2D[row][col] for row in range(row_count)))

    for element in column_sums:
        column_sums.remove(element)
        if element in column_sums:
            return True
        else:
            return False

if __name__ == "__main__":
    print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,7]]))
    print(f([[3,4],[5,1],[4,7]]))
    print(f([[3,4],[5,9],[4,7]])) 
