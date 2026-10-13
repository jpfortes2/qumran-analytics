# Limitations and open scientific issues

**This is an exploratory report, not a published benchmark.**

1. **Sample size.** Four lines form the primary validation sample, too small for confident external generalization claims. Eleven lines are reserved for testing, also small.
2. **Potential leakage.** Four crop pairings involving three test lines have possible geometric intersections with training crops. Image-coordinate/pixel-level resolution is still required.
3. **Assisted ground truth.** Training references were developed with editorial textual assistance; orthographic reconciliation must not be conflated with independent paleographic verification.
4. **Model-selection bias.** The 71.02% figure is the best checkpoint chosen from internal validation, so it cannot serve as an unbiased estimate of test accuracy.
5. **Protocol comparability.** The earlier 59.18% base-model value and later 71.02% checkpoint value should not be overinterpreted as a controlled comparison until evaluated on the same sealed protocol.
6. **Preprocessing and normalization.** Unicode normalization (including Hebrew combining marks), reading order and crop boundary policy can change the measured CER and WER.
7. **Toolchain conflicts.** The historical runtime recorded Kraken 7.1.1 while also installing `safetensors==0.8.0`, although Kraken 7.1.1 declared a `safetensors~=0.7.0` requirement. Reproduction needs a tested, pinned environment; the public release does not claim environment-level reproducibility of model training.
8. **Data-access and licenses.** Manuscript images, derived crops, reference transcriptions, trained weights and held-out test labels require separate rights and distribution review.
9. **Notebook execution order.** The historical research notebook includes repeated setup, failed/revised procedures and destructive file operations. It is an audit record, not a run-all tutorial.

## Claims not warranted yet

Do **not** describe the model as having 71.02% accuracy on unseen test images, claim professional paleographic validation has been completed, or claim the original dataset can be freely redistributed.
