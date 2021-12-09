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

        self.assertGreater(ratio, 0.90)

    def test_3_plate_recognition(self):
        img = plate_recognition("test_pics/try1.jpg")
        res = plate_to_text(img)

        strTrue = "CD 80515"
        ratio = SequenceMatcher(None, res, strTrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strTrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.90)
        self.assertEqual(strTrue, res)

    def test_4_plate_recognition(self):
        img = plate_recognition("test_pics/try2.jpg")
        res = plate_to_text(img)

        strtrue = "AG 23353"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.90)
        self.assertEqual("AG 23353", res)


    def test_5_plate_recognition(self):
        img = plate_recognition("test_pics/try3.png")
        res = plate_to_text(img)

        strtrue = "CUBS"
        ratio = SequenceMatcher(None, res, strtrue).ratio()

        print("ratio: ", ratio)
        print("Expected: ", strtrue)
        print("Actual: ", res)

        self.assertGreater(ratio, 0.90)
        self.assertEqual("CUBS", res)

    def test_6_plate_recognition(self):
        img = plate_recognition("test_pics/try4.jpg")
        res = plate_to_text(img)
        self.assertEqual("AK 13378", res)

    def test_7_plate_recognition(self):
        img = plate_recognition("test_pics/try5.jpg")
        res = plate_to_text(img)
        self.assertEqual("Y91 7846", res)

    def test_8_plate_recognition(self):
        img = plate_recognition("test_pics/try6.jpg")
        res = plate_to_text(img)
        self.assertEqual("NOPE", res)

    def test_9_plate_recognition(self):
        img = plate_recognition("test_pics/try7.jpg")
        res = plate_to_text(img)
        self.assertEqual("A61 2024", res)

    def test_10_plate_recognition(self):
        img = plate_recognition("test_pics/try8.jpg")
        res = plate_to_text(img)
        self.assertEqual("59 438 L", res)

    def test_11_plate_recognition(self):
        img = plate_recognition("test_pics/try9.jpg")
        res = plate_to_text(img)
        self.assertEqual("AAG 777", res)

    def test_12_plate_recognition(self):
        img = plate_recognition("test_pics/try10.jpg")
        res = plate_to_text(img)
        self.assertEqual("AU 73671", res)

    def test_13_plate_recognition(self):
        img = plate_recognition("test_pics/try11.jpg")
        res = plate_to_text(img)
        self.assertEqual("CC 19084", res)

    def test_14_plate_recognition(self):
        img = plate_recognition("test_pics/try12.jpg")
        res = plate_to_text(img)
        self.assertEqual("AB9 6324", res)

    def test_15_plate_recognition(self):
        img = plate_recognition("test_pics/try13.jpg")
        res = plate_to_text(img)
        self.assertEqual("AN 98903", res)

    def test_16_plate_recognition(self):
        img = plate_recognition("test_pics/try14.jpg")
        res = plate_to_text(img)
        self.assertEqual("AN 98903", res)

    def test_17_plate_recognition(self):
        img = plate_recognition("test_pics/c1.jpg")
        res = plate_to_text(img)
        self.assertEqual("CB 68470", res)

    def test_18_plate_recognition(self):
        img = plate_recognition("test_pics/c2.jpg")
        res = plate_to_text(img)
        self.assertEqual("CB 68470", res)

    def test_19_plate_recognition(self):
        img = plate_recognition("test_pics/c3.jpg")
        res = plate_to_text(img)
        self.assertEqual("AS 73424", res)

    def test_20_plate_recognition(self):
        img = plate_recognition("test_pics/c4.jpg")
        res = plate_to_text(img)
        self.assertEqual("CB 68470", res)

    def test_21_plate_recognition(self):
        img = plate_recognition("test_pics/c5.jpg")
        res = plate_to_text(img)
        self.assertEqual("CB 68470", res)

    def test_22_plate_recognition(self):
        img = plate_recognition("test_pics/c6.jpg")
        res = plate_to_text(img)
        self.assertEqual("CW 87796", res)

    def test_23_plate_recognition(self):
        img = plate_recognition("test_pics/c7.jpg")
        res = plate_to_text(img)
        self.assertEqual("CQ 24435", res)

    def test_24_plate_recognition(self):
        img = plate_recognition("test_pics/c8.jpg")
        res = plate_to_text(img)
        self.assertEqual("H11 4463", res)

    def test_25_plate_recognition(self):
        img = plate_recognition("test_pics/c9.jpg")
        res = plate_to_text(img)
        self.assertEqual("CQ 24435", res)

    def test_26_plate_recognition(self):
        img = plate_recognition("test_pics/c10.jpg")
        res = plate_to_text(img)
        self.assertEqual("CH 25722", res)

    def test_27_plate_recognition(self):
        img = plate_recognition("test_pics/c11.jpg")
        res = plate_to_text(img)
        self.assertEqual("CC 19289", res)

    def test_28_plate_recognition(self):
        img = plate_recognition("test_pics/c12.jpg")
        res = plate_to_text(img)
        self.assertEqual("CV 74753", res)

    def test_29_plate_recognition(self):
        img = plate_recognition("test_pics/c13.jpg")
        res = plate_to_text(img)
        self.assertEqual("BY 23057", res)

    def test_30_plate_recognition(self):
        img = plate_recognition("test_pics/c14.jpg")
        res = plate_to_text(img)
        self.assertEqual("CG 98731", res)