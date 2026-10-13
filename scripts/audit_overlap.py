#!/usr/bin/env python3
"""Evaluate geometric crop overlap; it does not establish shared ink or leakage."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import argparse,csv
from qumran_analytics.geometry import intersection_over_union,bbox_intersection

REQUIRED=['train_id','test_id','train_x1','train_y1','train_x2','train_y2',
          'test_x1','test_y1','test_x2','test_y2']

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv', type=Path,required=True)
    args=p.parse_args()
    with args.csv.open(encoding='utf-8-sig',newline='') as f:
        r=csv.DictReader(f)
        if not set(REQUIRED).issubset(r.fieldnames or []):
            p.error('Required columns: '+','.join(REQUIRED))
        rows=list(r)
    if not rows:
        p.error('CSV has no crop pairs')
    print('train_id,test_id,intersection_area,IoU,geometric_overlap')
    for row in rows:
        try:
            a=tuple(float(row['train_'+c]) for c in ('x1','y1','x2','y2'))
            b=tuple(float(row['test_'+c]) for c in ('x1','y1','x2','y2'))
            overlap=bbox_intersection(a,b)
            iou=intersection_over_union(a,b)
        except (ValueError,TypeError,KeyError) as e:
            p.error('Invalid crop coordinates for '+str(row.get('test_id'))+': '+str(e))
        print(f"{row['train_id']},{row['test_id']},{overlap:.2f},{iou:.6f},{overlap>0}")
    print('NOTE: common coordinate space is required; bounding boxes alone cannot show shared ink.',file=sys.stderr)

if __name__=='__main__':
    main()
