def max_value(histogram):
    return (max(histogram))
#------------------------------
def find_row(histogram, rightMove, leftMove):


#-----------------------------
def cycle_find(histogram, index):
    rightMove = index + 1
    leftMove = index -1
    find_row(histogram, rightMove, leftMove)


#------------------------------
def largest_histogram(histogram):
    maxVal = max_value(histogram)
    index = histogram.index(maxVal)
    cycle_find(histogram, index)

    #return max(histogram)

#-------------------------------
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")