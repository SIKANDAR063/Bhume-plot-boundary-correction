#!/usr/bin/env python3
"""
Apply the boundary correction method to all available village bundles
and write predictions.geojson for each.
"""
from pathlib import Path
from bhume import load, write_predictions, score
from bhume.align import correct_village

VILLAGES = [
    'data/34855_vadnerbhairav_chandavad_nashik',
    'data/malatavadi',
]

for vdir in VILLAGES:
    print(f'Processing {vdir}...')
    village = load(vdir)
    preds = correct_village(village)
    out = Path(vdir) / 'predictions.geojson'
    write_predictions(out, preds)
    print(f'Wrote {len(preds)} predictions → {out}')
    if village.example_truths is not None:
        print(score(preds, village))
    print()