def parse(lines):
    ocr_characters = []
    for index in range(0, len(lines[0]) // 3):
        offset = index * 3
        grid = [lines[0][offset:offset + 3], lines[1][offset:offset + 3], lines[2][offset:offset + 3]]
        ocr_characters.append(OCRCharacter(grid))
    return ocr_characters


def translate(ocr_characters):
    translate_chars = []
    for ocr in ocr_characters:
        translate_chars.append(ocr.translate())
    return AccountNumber(translate_chars)



class OCRCharacter:
    ZERO = [' _ ', '| |', '|_|']
    ONE = ['   ', '  |', '  |']
    TWO = [' _ ', ' _|', '|_ ']
    THREE = [' _ ', ' _|', ' _|']
    FOUR = ['   ', '|_|', '  |']
    FIVE = [' _ ', '|_ ', ' _|']
    SIX = [' _ ', '|_ ', '|_|']
    SEVEN = [' _ ', '  |', '  |']
    EIGHT = [' _ ', '|_|', '|_|']
    NINE = [' _ ', '|_|', ' _|']

    def __init__(self, grid):
        self.grid = grid

    def print(self):
        for row in self.grid:
            print(row)

    def translate(self):
        if self.grid == self.ZERO:
            return 0
        if self.grid == self.ONE:
            return 1
        if self.grid == self.TWO:
            return 2
        if self.grid == self.THREE:
            return 3
        if self.grid == self.FOUR:
            return 4
        if self.grid == self.FIVE:
            return 5
        if self.grid == self.SIX:
            return 6
        if self.grid == self.SEVEN:
            return 7
        if self.grid == self.EIGHT:
            return 8
        if self.grid == self.NINE:
            return 9
        return None


class AccountNumber:
    def __init__(self, account_number):
        self.account_number = account_number

    def __str__(self):
        as_string = ''
        illegal_character = False
        for digit in self.account_number:
            if digit == None:
                illegal_character = True
                as_string += '?'
            else:
                as_string += str(digit)
        if illegal_character:
            return as_string + ' ILL'
        else:
            checksum_ok =  self.calculate_checksum() == 0
            if checksum_ok:
                return as_string
            else:
                return as_string + ' ERR'

    def calculate_checksum(self):
        checksum = 0
        for index in range(len(self.account_number)):
            digit = self.account_number[index]
            multiplier = 9 - index
            checksum += digit * multiplier
        return checksum % 11

