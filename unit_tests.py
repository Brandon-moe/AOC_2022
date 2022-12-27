from days import *
import unittest
class AdventOfCode2021Tests(unittest.TestCase):
    #DAY 1
    def test_day_1_part_a(self):
        self.assertEqual(day1.solve("test/1.csv",1),24000)
    def test_day_1_part_b(self):
        self.assertEqual(day1.solve("test/1.csv",3),45000)
    #DAY 2
    def test_day_2_part_a(self):
        self.assertEqual(day2.solve("test/2.csv","a"),15)
    def test_day_2_part_b(self):
        self.assertEqual(day2.solve("test/2.csv","b"),12)
    #DAY 3
    def test_day_3_part_a(self):
        self.assertEqual(day3.solve("test/3.csv","a"),157)
    def test_day_3_part_b(self):
        self.assertEqual(day3.solve("test/3.csv","b"),70)
    #DAY 4
    def test_day_4_part_a(self):
        self.assertEqual(day4.solve("test/4.csv","a"),2)
    def test_day_4_part_b(self):
        self.assertEqual(day4.solve("test/4.csv","b"),4)
    # #DAY 5
    def test_day_5_part_a(self):
        self.assertEqual(day5.solve("test/5.csv",-1),"CMZ")
    def test_day_5_part_b(self):
        self.assertEqual(day5.solve("test/5.csv",1),"MCD")
    # #DAY 6
    def test_day_6_part_a(self):
        self.assertEqual(day6.solve("test/6.csv",4),7)
    def test_day_6_part_b(self):
        self.assertEqual(day6.solve("test/6.csv",14),19)
    #DAY 7
    def test_day_7_part_a(self):
        self.assertEqual(day7.solve("test/7.csv")[0],95437)
    def test_day_7_part_b(self):
        self.assertEqual(day7.solve("test/7.csv")[1],24933642)
    #DAY 8
    def test_day_8_part_a(self):
        self.assertEqual(day8.solve("test/8.csv")[0],21)
    def test_day_8_part_b(self):
        self.assertEqual(day8.solve("test/8.csv")[1],8)
    #DAY 9
    def test_day_9_part_a(self):
        self.assertEqual(day9.solve("test/9.csv",2),13)
    def test_day_9_part_b(self):
        self.assertEqual(day9.solve("test/9b.csv",10),36)
    #DAY 10
    def test_day_10_part_a(self):
        self.assertEqual(day10.solve("test/10.csv"),13140)
    #DAY 11
    def test_day_11_part_a(self):
        self.assertEqual(day11.solve("test/11.csv",20),10605)
    def test_day_11_part_b(self):
        self.assertEqual(day11.solve("test/11.csv",10000),2713310158)
    #DAY 12
    def test_day_12_part_a(self):
        self.assertEqual(day12.solve("test/12.csv")[0],31)
    def test_day_12_part_b(self):
        self.assertEqual(day12.solve("test/12.csv")[1],29)
    #DAY 13
    def test_day_13_part_a(self):
        self.assertEqual(day13.solve("test/13.csv")[0],13)
    def test_day_13_part_b(self):
        self.assertEqual(day13.solve("test/13.csv")[1],140)
    #DAY 14
    def test_day_14_part_a(self):
        self.assertEqual(day14.solve("test/14.csv",True),24)
    def test_day_14_part_b(self):
        self.assertEqual(day14.solve("test/14.csv"),93)
    #DAY 15
    def test_day_15_part_a(self):
        self.assertEqual(day15.solve("test/15.csv",True)[0],26)
    def test_day_15_part_b(self):
        self.assertEqual(day15.solve("test/15.csv",True)[1],56000011)
if __name__ == "__main__":
    unittest.main()
