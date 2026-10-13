# Reproducibility guide

## Publicly runnable components

The repository includes dependency-free Python utilities for edit-distance-based metrics and geometric overlap checks. It also contains unit tests with **synthetic** strings, not the research data.

```bash
python -m unittest discover -s tests -v
python scripts/evaluate_htr.py --csv path/to/your_predictions.csv
python scripts/audit_overlap.py --csv path/to/your_bboxes.csv
```

CSV schemas:

```text
# HTR metrics (UTF-8)
htr_line_id,reference,prediction

# geometric overlap (UTF-8)
train_id,test_id,train_x1,train_y1,train_x2,train_y2,test_x1,test_y1,test_x2,test_y2
```

## Full research reconstruction — requires additional sources

Full reconstruction of FT01_R02 requires the manuscript images/crops, archived ground-truth manifests, original baseline weights and an environment matching the private experimental record. These assets are not distributed here. The included historical research notebook is redacted, lacks outputs and depends on private folder organization. **It is not executable end to end from a fresh checkout.**

For a future formal release, provide: source attribution and licenses; a stable image/crop manifest; full checksums; a fully specified data split and transcription policy; pinned Python/Kraken/Torch dependencies; a training command that matches the validated environment; model provenance; reproducible inference; and a locked independent test evaluation. Avoid publishing test labels before the preregistered comparison is completed.
