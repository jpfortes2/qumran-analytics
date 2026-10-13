#!/usr/bin/env python3
"""Evaluate UTF-8 CSV with columns: htr_line_id,reference,prediction.

Never use the held-out reference to select checkpoints or tune preprocessing.
"""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
import argparse, csv, json
from qumran_analytics.metrics import aggregate, error_counts


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv', required=True, type=Path)
    p.add_argument('--normalization', default='NFD',
                   choices=['NONE', 'NFC', 'NFD', 'NFKC', 'NFKD'])
    p.add_argument('--strip-combining', action='store_true',
                   help='Editorial policy option; off by default')
    p.add_argument('--output', type=Path, help='Optional JSON results')
    args = p.parse_args()
    with args.csv.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if not {'htr_line_id', 'reference', 'prediction'} <= set(reader.fieldnames or []):
            p.error('CSV columns must be htr_line_id,reference,prediction')
        rows = list(reader)
    if not rows:
        p.error('No rows; populate the CSV with legally usable evaluation data')
    if any(not (r['htr_line_id'] or '').strip() for r in rows):
        p.error('Every row needs an htr_line_id')
    seen=set(); details=[]
    for row in rows:
        line_id=row['htr_line_id'].strip()
        if line_id in seen:
            p.error(f'Duplicate htr_line_id: {line_id}')
        seen.add(line_id)
        if row['reference'] is None or row['prediction'] is None:
            p.error('Every row needs reference and prediction fields')
        counts=error_counts(row['reference'], row['prediction'],
                            form=args.normalization,
                            strip_combining=args.strip_combining)
        details.append({'htr_line_id': line_id, **counts})
    payload={'protocol': {'normalization':args.normalization,
                          'strip_combining':args.strip_combining,
                          'word_tokenization':'whitespace'},
             'summary':aggregate(details), 'per_line':details}
    print(json.dumps(payload,ensure_ascii=False,indent=2))
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
