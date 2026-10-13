import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from qumran_analytics.metrics import edit_distance,normalize,error_counts,aggregate
from qumran_analytics.geometry import bbox_intersection,intersection_over_union

class MetricsTest(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance('kitten','sitting'),3)
        self.assertEqual(edit_distance('אבג','אב'),1)
        self.assertEqual(edit_distance('', ''), 0)
    def test_normalization(self):
        self.assertEqual(normalize('\u05e9\u05b8', 'NFD'),normalize('\u05e9\u05b8','NFC',False))
        self.assertEqual(normalize('\u05e9\u05b8', 'NFD',True),'ש')
    def test_metrics(self):
        result=error_counts('אבג דה','אב דה')
        self.assertEqual(result['char_edits'],1)
        self.assertAlmostEqual(result['cer'],1/6)
        self.assertEqual(result['word_edits'],1)
    def test_aggregate_micro(self):
        entries=[error_counts('abc','ab'),error_counts('z','x')]
        self.assertAlmostEqual(aggregate(entries)['CER'],2/4)
    def test_zero_reference(self):
        self.assertIsNone(error_counts('','x')['cer'])
    def test_overlap(self):
        self.assertEqual(bbox_intersection((0,0,2,2),(1,1,3,3)),1)
        self.assertAlmostEqual(intersection_over_union((0,0,2,2),(1,1,3,3)),1/7)
        self.assertEqual(bbox_intersection((0,0,1,1),(1,1,2,2)),0)

if __name__=='__main__':
    unittest.main()
