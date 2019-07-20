import unittest

import ocr_parser
import reader


class FileInputTest(unittest.TestCase):
    def test_read_file(self):
        data = reader.read_scanner_result('data/testcase1.txt')
        self.assertIsNotNone(data)
        self.assertEqual(3, len(data))
        self.assertTrue(reader.validate_scanner_result(data))

    def test_read_not_existing_file(self):
        data = reader.read_scanner_result('data/unknown.txt')
        self.assertIsNone(data)

    def test_read_missing_lines_file(self):
        data = reader.read_scanner_result('data/missinglines.txt')
        self.assertIsNone(data)

    def test_read_short_file(self):
        data = reader.read_scanner_result('data/2lines.txt')
        self.assertFalse(reader.validate_scanner_result(data))

    def test_read_long_file(self):
        data = reader.read_scanner_result('data/4lines.txt')
        self.assertFalse(reader.validate_scanner_result(data))

    def test_read_different_lines_file(self):
        data = reader.read_scanner_result('data/differentlength.txt')
        self.assertFalse(reader.validate_scanner_result(data))


class FileParserTest(unittest.TestCase):
    def test_parse_zeros(self):
        data = reader.read_scanner_result('data/testcase1.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('000000000', str(account_number))

    def test_parse_ones(self):
        data = reader.read_scanner_result('data/testcase2.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('111111111 ERR', str(account_number))

    def test_parse_twos(self):
        data = reader.read_scanner_result('data/testcase3.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('222222222 ERR', str(account_number))

    def test_parse_123456789(self):
        data = reader.read_scanner_result('data/testcase4.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('123456789', str(account_number))
        print(f'account number: {account_number}, {account_number!r}')

    def test_parse_12ERR456709(self):
        data = reader.read_scanner_result('data/testcase5.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual('12?456709 ILL', str(account_number))
        print(f'account number: {account_number}, {account_number!r}')

    def test_parse_checksum_ok1(self):
        data = reader.read_scanner_result('data/testcase4.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual(0, account_number.calculate_checksum())

    def test_parse_checksum_ok2(self):
        data = reader.read_scanner_result('data/checksum.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual(0, account_number.calculate_checksum())
        self.assertEqual('457508000', str(account_number))

    def test_parse_checksum_wrong1(self):
        data = reader.read_scanner_result('data/checksum_wrong1.txt')
        ocr_characters = ocr_parser.parse(data)
        self.assertEqual(9, len(ocr_characters))
        account_number = ocr_parser.translate(ocr_characters)
        self.assertEqual(2, account_number.calculate_checksum())
        self.assertEqual('664371495 ERR', str(account_number))


