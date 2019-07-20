import pathlib


def read_scanner_result(filename):
    path = pathlib.Path(filename)
    if not path.exists():
        return None

    with path.open('r') as testfile:
        lines = testfile.read().splitlines()
        testfile.close()
    return lines


def validate_scanner_result(lines):
    if lines is None:
        print('leere Datei')
        return False

    if len(lines) != 3:
        print(f'Die Datei hat {len(lines)} Zeilen, anstatt der erforderlichen 3')
        return False

    for line in lines:
        if len(line) % 3 != 0:
            print ('Die Zeilenlänge muss durch 3 teilbar sein.')
            return False

    if len(lines[0]) != len(lines[1]) or len(lines[1]) != len(lines[2]):
        print ('Unterschiedliche Zweilenlängen')
        return False

    return True
