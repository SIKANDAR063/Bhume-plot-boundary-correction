gpt link ->https://chatgpt.com/share/6a2edcce-6b20-83e8-8f37-13380056278c
claude chat link -> https://claude.ai/share/1c0b17aa-5c2c-49de-8289-ab8969fcc3e5
deepseek chat link -> https://chat.deepseek.com/share/9nt0fniikvajvfl4z1


# 🗺️ BhuMe Engineering 

> **"For each land plot, decide whether the official boundary can be nudged onto the real field, and if so, where it should go."**

---

# Overview

This repository contains my solution to the **BhuMe Boundary Alignment Challenge**.

The objective is to correct spatial drift between official cadastral land boundaries and the actual field boundaries visible in satellite imagery.

Historical land records in Maharashtra were originally surveyed using traditional field-survey methods and later georeferenced onto modern satellite imagery. Because the original maps were never tied to GPS coordinates, many plot boundaries are shifted by several meters from their true position on the ground.

The goal of this project is to:

1. Detect positional drift.
2. Correct boundaries whenever sufficient evidence exists.
3. Estimate confidence for every correction.
4. Avoid modifying plots that are already correct.
5. Flag uncertain plots instead of forcing incorrect corrections.

The solution focuses on:

* Accuracy
* Confidence calibration
* Restraint
* Generalization to unseen villages

rather than simply maximizing performance on the public example truths.

---

# Problem Understanding

Each village contains:

### Official Plot Boundaries

Stored in:

```text
input.geojson
```

These boundaries originate from historical cadastral maps.

---

### Satellite Imagery

Stored in:

```text
imagery.tif
```

This serves as the primary visual reference for identifying actual field boundaries.

---

### Boundary Hints

Stored in:

```text
boundaries.tif
```

These are automatically generated field-edge detections.

Important:

* Helpful as guidance
* Not always accurate
* Can contain noise
* Must not be blindly trusted

---

### Example Truths

Stored in:

```text
example_truths.geojson
```

These are manually corrected plots used as trusted control points.

---

# Solution Architecture

The pipeline consists of five stages.

---

## Stage 1 — Control Point Analysis

The provided example truths are treated as trusted reference plots.

For each example truth:

1. Locate the corresponding official plot.
2. Compute centroid displacement.
3. Measure:

```text
dx = x displacement
dy = y displacement
```

These shifts represent how much the cadastral map has drifted locally.

---

## Stage 2 — Spatial Drift Estimation

The village does not drift uniformly.

Plots near each other tend to experience similar displacement.

To estimate correction for unseen plots:

1. Calculate distance to nearby control plots.
2. Weight nearby truths more heavily.
3. Predict local displacement.

This creates a smooth village-wide correction field.

---

## Stage 3 — Local Boundary Refinement

After applying the estimated shift:

1. Extract a raster patch around the plot.
2. Sample boundary points.
3. Compare the plot outline against detected field edges.
4. Search within a small neighborhood.

The search attempts to improve alignment while avoiding unrealistic corrections.

Only small local adjustments are allowed.

This prevents catastrophic failures.

---

## Stage 4 — Validation

Every correction is validated before acceptance.

Validation includes:

### Boundary Quality

How well the corrected boundary aligns with detected field edges.

---

### Area Consistency

The corrected geometry should remain consistent with:

```text
recorded_area_sqm
pot_kharaba
```

Large area discrepancies are treated as suspicious.

---

### Shift Magnitude

Very large corrections are considered low-confidence.

---

### Evidence Strength

Weak visual evidence results in lower confidence.

---

## Stage 5 — Confidence Calibration

Producing a boundary is not enough.

The system must also estimate:

> "How likely is this correction to be correct?"

Confidence is computed using:

### Alignment Quality

Better edge alignment → higher confidence.

---

### Control Point Support

Plots near trusted examples receive higher confidence.

---

### Area Agreement

Boundaries consistent with land records receive higher confidence.

---

### Shift Magnitude

Small corrections are generally more reliable than large corrections.

---

# Restraint Strategy

A major requirement of the challenge is restraint.

The system intentionally avoids unnecessary corrections.

Plots may be flagged when:

* Evidence is weak
* Multiple interpretations exist
* The official boundary already appears correct
* Confidence falls below acceptable thresholds

This reduces over-correction and improves robustness.

---

# Repository Structure

```text
bhume-starter-kit/
│
├── bhume/
│   ├── __init__.py
│   ├── align.py
│   ├── baseline.py
│   ├── geo.py
│   ├── io.py
│   └── score.py
│
├── data/
│   ├── vadnerbhairav/
│   │   ├── input.geojson
│   │   ├── imagery.tif
│   │   ├── boundaries.tif
│   │   ├── example_truths.geojson
│   │   └── predictions.geojson
│   │
│   └── malatavadi/
│       ├── input.geojson
│       ├── imagery.tif
│       ├── boundaries.tif
│       ├── example_truths.geojson
│       └── predictions.geojson
│
├── run_all.py
├── quickstart.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Installation (From Scratch)

## Step 1 — Clone Repository

```bash
git clone <your-repository-url>
cd bhume-starter-kit
```

---

## Step 2 — Install UV

macOS / Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

---

## Step 3 — Install Dependencies

```bash
uv sync
```

This command:

* Creates a virtual environment
* Installs Python 3.12
* Installs all project dependencies
* Locks versions using uv.lock

---

## Step 4 — Add Village Data

Place downloaded village bundles inside:

```text
data/
```

Example:

```text
data/
├── 34855_vadnerbhairav_chandavad_nashik/
│   ├── input.geojson
│   ├── imagery.tif
│   ├── boundaries.tif
│   └── example_truths.geojson
│
└── malatavadi/
    ├── input.geojson
    ├── imagery.tif
    ├── boundaries.tif
    └── example_truths.geojson
```

---

# Running the Pipeline

## Run All Villages

```bash
uv run run_all.py
```

---

## Run Quickstart Demo

```bash
uv run quickstart.py data/34855_vadnerbhairav_chandavad_nashik
```

---

## Generate Predictions

After execution:

```text
data/<village>/predictions.geojson
```

will be created automatically.

---

# Example Output

```text
Processing data/34855_vadnerbhairav_chandavad_nashik...

Wrote 2457 predictions

coverage:
2457 corrected

accuracy:
median IoU pred = 0.74
official = 0.61

improvement = +0.13

calibration:
Spearman(conf,IoU)=0.42
```

---

# Output Format

Each prediction contains:

```json
{
  "plot_number": "123",
  "status": "corrected",
  "confidence": 0.84,
  "method_note": "boundary alignment",
  "geometry": {...}
}
```

---

# Dependencies

| Library                | Purpose                             |
| ---------------------- | ----------------------------------- |
| geopandas              | GeoJSON processing                  |
| rasterio               | GeoTIFF reading                     |
| shapely                | Geometry operations                 |
| numpy                  | Numerical computation               |
| scipy                  | Statistical analysis                |
| pillow                 | Image utilities                     |
| opencv-python-headless | Edge detection and Chamfer matching |

---

# Limitations

Current assumptions:

* Example truths represent local drift accurately.
* Satellite imagery quality is sufficient.
* Boundary hints contain useful signal.
* Large shape deformations are avoided.

---

# Future Improvements

Potential improvements include:

* Local affine transformations
* Multi-scale edge matching
* Learned confidence models
* Plot-neighborhood consistency checks
* Graph-based boundary refinement

---

# Conclusion

This solution prioritizes:

* Reliable correction
* Confidence calibration
* Restraint
* Explainability
* Generalization

The objective is not simply to maximize IoU on a small validation set but to produce a trustworthy correction pipeline that scales to unseen villages and provides realistic confidence estimates for every prediction.
