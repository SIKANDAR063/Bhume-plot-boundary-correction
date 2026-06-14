gpt link ->https://chatgpt.com/share/6a2edcce-6b20-83e8-8f37-13380056278c
claude chat link -> https://claude.ai/share/1c0b17aa-5c2c-49de-8289-ab8969fcc3e5
deepseek chat link -> https://chat.deepseek.com/share/9nt0fniikvajvfl4z1

# LLM Usage Transcript – Bhume Plot Boundary Correction

## Session 1 – Understanding the Problem

### My Prompt

I have a take-home assignment involving correcting misaligned plot boundaries in GeoJSON files.

Input:

* input.geojson (predicted plot boundaries)
* truths.geojson (ground truth plots)

I need to align the predicted boundaries to the ground truth and maximize IoU.

Help me understand:

1. What exactly is polygon alignment?
2. How is IoU calculated?
3. What strategies can be used to improve alignment?

### AI Response Summary

* Explained polygon alignment concepts.
* Explained Intersection over Union (IoU).
* Suggested translation, scaling, rotation, centroid matching, and nearest-neighbor approaches.
* Recommended testing multiple alignment strategies and comparing IoU scores.

### Outcome

Used AI to understand the problem before writing any code.

---

## Session 2 – GeoJSON Processing

### My Prompt

How do I read a GeoJSON file in Python and iterate through all polygon features?

I need to:

* Load GeoJSON
* Extract coordinates
* Process each polygon
* Save corrected polygons back to a new GeoJSON

### AI Response Summary

* Suggested using json and GeoJSON-compatible structures.
* Explained FeatureCollection format.
* Demonstrated reading and writing GeoJSON.
* Explained polygon coordinate extraction.

### Outcome

Implemented GeoJSON loading and output generation.

---

## Session 3 – Designing Alignment Logic

### My Prompt

I have two polygons:

* Predicted polygon
* Ground truth polygon

How can I shift the predicted polygon so it better matches the ground truth?

### AI Response Summary

Suggested:

* Centroid calculation
* Translation vector
* Coordinate shifting
* Recalculation of polygon positions
* Evaluating alignment using IoU

### Outcome

Implemented centroid-based alignment approach.

---

## Session 4 – Improving IoU

### My Prompt

My alignment works but IoU is still low.

What techniques can improve polygon overlap further?

### AI Response Summary

Suggested:

* Rotation search
* Scale adjustments
* Iterative optimization
* Bounding-box matching
* Vertex-level refinement

### Outcome

Tested additional refinement approaches and evaluated improvements.

---

## Session 5 – Debugging

### My Prompt

I am getting errors while processing GeoJSON files.

Error:
[paste error message]

Help me debug this issue.

### AI Response Summary

* Identified parsing issues.
* Explained coordinate format requirements.
* Suggested validation checks.
* Recommended handling malformed features safely.

### Outcome

Fixed GeoJSON processing bugs.

---

## Session 6 – Documentation

### My Prompt

Help me write a professional README for this take-home assignment.

Include:

* Problem statement
* Approach
* Assumptions
* Results
* How to run

### AI Response Summary

Generated README structure and documentation suggestions.

### Outcome

Used AI assistance to improve project documentation.

---

## Overall AI Usage

I used LLMs as an engineering assistant to:

* Understand the problem requirements
* Learn polygon alignment concepts
* Understand IoU evaluation
* Design alignment strategies
* Debug implementation issues
* Improve documentation

All final design decisions, testing, code integration, and validation were performed manually.





