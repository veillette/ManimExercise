# ManimExercise

Manim animations for physics teaching.

## Projects

### [`kinematics-derivation/`](kinematics-derivation/)

Derives the four constant-acceleration kinematics equations using algebra only — no
calculus — for an algebra-based physics class.

- `v = v₀ + at`
- `Δx = ½(v₀ + v)t`
- `Δx = v₀t + ½at²`
- `v² = v₀² + 2aΔx`

The step that normally needs calculus (displacement when the velocity is changing) is
handled with a symmetry argument about a straight-line velocity–time graph, which an
algebra student can verify directly. See the
[project README](kinematics-derivation/README.md) for the full derivation and build
instructions.

## Requirements

- [Manim Community Edition](https://www.manim.community/)
- ffmpeg
- A LaTeX installation (`latex` and `dvisvgm`, plus the `standalone` and `amsmath`
  packages)

```bash
pip install manim
```

Each project folder is self-contained: render with `manim -ql script.py <Scene...>`
from inside it, then stitch with the project's `concat.txt`.
