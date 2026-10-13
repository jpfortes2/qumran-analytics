# Methodology — research record

## Manuscript and scope

The study focuses on the *Community Rule* (1QS), using working images organized by manuscript column. The full source-image acquisition procedure, edition attribution, URLs and licenses must be verified against the upstream provider before any imagery is redistributed. No third-party manuscript images are included in this initial repository.

## Image workflow

The historical notebook documents source-image retrieval, column region-of-interest (ROI) selection, visual adjustments and line-level segmentation using image-processing and Kraken-related routines. It also records manual inspection and reconciliation where visual/physical lines cannot safely be mapped one-to-one to a textual reference.

## Text preparation and provenance

The workflow uses line IDs, column IDs, physical crops, audit tables, selected ground-truth versions and checksums. Reference-assisted transcription was used for training material; it must not be described as fully independent paleographic reading. Textual references, including ETCBC-derived resources, are subject to their own conditions of use.

## Experimental partitions

| Partition | Count | Purpose |
|---|---:|---|
| Training (batches 01–05) | 55 | Model adaptation |
| Main validation (batch 06) | 4 | Checkpoint selection / internal evaluation |
| Locked test (batch 07) | 11 | Independent evaluation pending expert ground truth |

The test manifest records one line per column and image SHA-256 digests. Exact duplicates were not observed by manifest hash comparison, but geometric checks flagged **four train–test crop pairings involving three test images** as potentially overlapping. Later attempts to compare ink-pixel overlap were inconclusive because source rectangle coordinates did not match crop dimensions. The existence of shared textual ink remains unresolved.

## Training record

- Hardware: Tesla T4 GPU under Google Colab
- Framework: Kraken 7.1.1
- Initialization: PP-OCRv6-related pretrained weights
- Recorded experiment: FT01_R02
- Training epochs: 30
- Number of training examples: 55
- Main validation examples: 4
- Best checkpoint filename: `checkpoint_13-0.7102.ckpt`
- Converted model filename: `best_0.7102.safetensors`
- The notebook recorded the latter model checksum, but the weights are intentionally not distributed here.

## Preliminary metric interpretation

- Earlier base-model character accuracy: **59.18%**.
- Best recorded fine-tuned validation character accuracy: **71.02%** (selected via the validation split).
- **Difference of descriptive figures:** 11.84 percentage points; **not** yet an independently verified causal improvement or a held-out test result.

To establish a controlled comparison, both models must be evaluated using identical held-out ground truth, transcription policy, Unicode normalization, segmentation, decoding and edit-distance procedures.

## Proposed independent evaluation

For character error rate (CER):

`CER = (substitutions + deletions + insertions) / number_of_reference_characters`

The same definition can be applied to whitespace-tokenized words for WER. Per-line error rates should be published alongside corpus-level (micro-averaged) values; CER can exceed 100% if insertion errors are sufficiently numerous.

The locked test set must not be used for iterative checkpoint selection, manual parameter search or reference-guided correction of test predictions. Expert transcribers should be blinded to model hypotheses, while any prior human inspection of the imagery must be disclosed.
