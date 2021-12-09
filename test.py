from unittest import TestCase
from img_processing import plate_to_text
from img_processing import plate_recognition

from difflib import SequenceMatcher


class Test(TestCase):
    def test_1_plate_recognition(self):
        img = plate_recognition("test_pics/pass1.jpg")
        res = plate_to_text(img)

        strtrue = "DB 40223"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.90)
        self.assertEqual(strtrue, res)

    def test_2_plate_recognition(self):
        img = plate_recognition("test_pics/pass2.jpg")
        res = plate_to_text(img)

        strTrue = "BU 57199"
        ratio = SequenceMatcher(None, res, strTrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strTrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.70)

    def test_3_plate_recognition(self):
        img = plate_recognition("test_pics/pass3.jpg")
        res = plate_to_text(img)

        strTrue = "CD 80515"
        ratio = SequenceMatcher(None, res, strTrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strTrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.90)
        self.assertEqual(strTrue, res)

    def test_4_plate_recognition(self):
        img = plate_recognition("test_pics/semipass4.jpg")
        res = plate_to_text(img)

        strtrue = "AU 73671"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.60)

    def test_5_plate_recognition(self):
        img = plate_recognition("test_pics/semipass5.jpg")
        res = plate_to_text(img)

        strtrue = "CC 19084"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.58)


    def test_6_plate_recognition(self):
        img = plate_recognition("test_pics/semipass6.jpg")
        res = plate_to_text(img)

        strtrue = "AS 73424"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.49)


    def test_7_plate_recognition(self):
        img = plate_recognition("test_pics/semipass1.jpg")
        res = plate_to_text(img)

        strtrue = "BR 86363"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.9)


    def test_8_plate_recognition(self):
        img = plate_recognition("test_pics/semipass3.jpg")
        res = plate_to_text(img)

        strtrue = "NVR GLTY"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.9)

    def test_9_plate_recognition(self):
        img = plate_recognition("test_pics/semipass7.jpg")
        res = plate_to_text(img)

        strtrue = "BZ 64963"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.85)