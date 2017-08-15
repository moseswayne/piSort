def getDigitCounts(array):
    digitCounts = {}
    for element in array:
        numDigits = len(str(element))
        if numDigits in digitCounts:
            digitCounts[numDigits] += 1
        else:
            digitCounts[numDigits] = 1
    return digitCounts

def isSorted(array):
    previous = None
    for element in array:
        if previous and previous > element:
            return False
        previous = element
    return True


# This is the main bottleneck (consider getting digits from file
# or using an actually efficient algorithm
def getDigit(config=None):
    q, r, t, k, n, l = config if config else (1, 0, 1, 1, 3, 3)

    while 4 * q + r - t >= n * t:
        nr = (2 * q + r) * l
        nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
        q *= k
        t *= l
        l += 2
        k += 1
        n = nn
        r = nr
    digit = n
    nr = 10 * (r - n * t)
    n = ((10 * (3 * q + r)) // t) - 10 * n
    q *= 10
    r = nr
    return digit, (q, r, t, k, n, l)

def getWindowedDigits(digits, window):
    stringDigits = ''.join(str(digit) for digit in digits)
    windowedDigits = []
    #print window
    for numDigits in window:
        windowedDigits.append(int(stringDigits[:numDigits]))
        stringDigits = stringDigits[numDigits:]
    return windowedDigits

def testGetDigit():
    config = None
    for i in range(30):
        digit, config = getDigit(config)
        print digit

def pisort(array, returnIndex=False):
    piIndex = 0
    sortedList = []
    if len(array) == 0:
        piIndex = -1
        sortedList = array
    else:
        digitCounts = getDigitCounts(array)
        keyList = list(digitCounts.keys())
        print 'Digit Counts:', digitCounts
        print 'Key List:', keyList
        window = []
        windowOrder = keyList

        # if we have more than one key, we need to sort this list
        if len(keyList) > 1:
            print '-------------- Calling pisort recursively ---------------'
            windowOrder = pisort(keyList)
            print '---------------  Done with recusive call ----------------'

        print 'Window Order:', windowOrder
        # get teh window by expanding the key list
        for digitKey in windowOrder:
            window += [digitKey] * digitCounts[digitKey]

        print 'Window:', window
        # start finding
        arraySet = set(array)
        config = None;

        # populate initial digits window
        digits = []
        for i in xrange(sum(window)):
            digit, config = getDigit(config)
            digits.append(digit)

        print 'Initial Digits:', digits
        while True:
            windowedDigits = getWindowedDigits(digits, window)
            if set(windowedDigits) == arraySet and isSorted(windowedDigits):
                sortedList = windowedDigits
                break
            # shift
            del digits[0]
            newDigit, config = getDigit(config)
            digits.append(newDigit)
            piIndex += 1
            if piIndex % 100 == 0:
                print 'Currently at digit', piIndex

    if returnIndex:
        return sortedList, piIndex
    return sortedList
                


def test(inputList=[15, 14, 3, 92]):
    sortedList, index = pisort(inputList, True)
    print 'Input List:     ', inputList
    print 'Sorted List:    ', sortedList
    print 'Found at index: ', index
