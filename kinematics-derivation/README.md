# The Four Kinematics Equations — an algebra-only derivation

A ~3-minute Manim video that derives all four constant-acceleration kinematics
equations without using calculus, for an algebra-based physics class.

| | Equation | Leaves out |
|---|---|---|
| 1 | `v = v₀ + at` | `Δx` |
| 2 | `Δx = ½(v₀ + v)t` | `a` |
| 3 | `Δx = v₀t + ½at²` | `v` |
| 4 | `v² = v₀² + 2aΔx` | `t` |

## What the derivation assumes

Only two definitions, plus ordinary algebra:

- **acceleration** — `a = Δv / Δt`, and it is constant
- **average velocity** — `Δx = v_avg · t`, which is exactly true by definition

Everything else is derived. In particular, the usual "displacement is the area under
the velocity–time graph" step is replaced by a symmetry argument that an algebra
student can check: because the velocity–time graph is a *straight line*, the amount
the object falls short of the midpoint velocity in the first half of the trip is a
triangle congruent to the amount it exceeds the midpoint velocity in the second half.
Rotate one 180° about the halfway point and it lands exactly on the other, so the
average velocity is `(v₀ + v)/2`. No limits, no integrals.

From there:

- Equation 1 comes straight from the definition of acceleration.
- Equation 2 is `Δx = v_avg · t` with the average filled in.
- Equation 3 is Equation 2 with `v` substituted away using Equation 1.
- Equation 4 is Equation 2 with `t` substituted away using Equation 1, where the
  numerator `(v₀ + v)(v − v₀)` collapses by difference of squares.

Scene 7 works a numeric example and cross-checks it against a second equation, so the
four read as one system rather than four rules to memorize.

## Files

| File | What it is |
|---|---|
| `plan.md` | Scene-by-scene plan: content, visuals, narration, colour palette |
| `script.py` | The Manim Community Edition source, one class per scene |
| `merge_srt.py` | Merges Manim's per-scene `.srt` files into one track for `final.mp4` |
| `concat.txt` | ffmpeg concat list, in scene order |
| `final.mp4` | The stitched video |
| `final.srt` | Subtitles for the stitched video |

## Building it

Requires Manim Community Edition, ffmpeg, and a LaTeX install (`latex` + `dvisvgm`,
plus `standalone`/`amsmath`, e.g. `texlive-latex-base texlive-latex-extra`).

```bash
pip install manim

# preview quality
manim -ql script.py Scene1_Hook Scene2_Quantities Scene3_Equation1 Scene4_Equation2 \
                    Scene5_Equation3 Scene6_Equation4 Scene7_Example Scene8_Summary

# final quality
manim -qh script.py Scene1_Hook Scene2_Quantities Scene3_Equation1 Scene4_Equation2 \
                    Scene5_Equation3 Scene6_Equation4 Scene7_Example Scene8_Summary

# stitch, and build the merged subtitle track
sed -i 's/480p15/1080p60/' concat.txt          # if you rendered at -qh
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
python merge_srt.py --quality 1080p60
```

`concat.txt` as committed points at the `1080p60` output. Point it at `480p15` if you
are only doing preview renders.

## Scenes

1. **Hook** — stroboscopic motion showing equal time steps with growing gaps; the four
   equations appear unexplained.
2. **Five quantities** — `v₀`, `v`, `a`, `t`, `Δx`, and what "constant acceleration"
   actually says.
3. **Equation 1** — from the definition of acceleration; establishes that the
   velocity–time graph is a straight line (`y = mx + b`).
4. **Equation 2** — the average-velocity argument and the 180° rotation proof.
5. **Equation 3** — substitute Equation 1 into Equation 2; read the two terms off the
   graph as a rectangle plus a triangle.
6. **Equation 4** — eliminate `t`; difference of squares.
7. **Worked example** — a car from rest, 3 m/s², 5 s; picking the equation by the
   variable you don't have, then cross-checking.
8. **Summary** — all four, each tagged with the variable it omits.

## Colour convention

`v₀` blue · `v` cyan · `a` amber · `t` violet · `Δx` green. The same colours are used
for the symbols, the graph elements, and the result boxes throughout.
