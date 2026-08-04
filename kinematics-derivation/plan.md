# The Four Kinematics Equations — Derived with Algebra Alone

## Overview
- **Topic**: Deriving the four constant-acceleration kinematics equations without calculus
- **Hook**: Textbooks hand students four equations to memorize. Where do they actually come from — and can you get there with nothing but algebra?
- **Target Audience**: Algebra-based introductory physics. Prerequisites: solving linear equations, area of a rectangle/triangle/trapezoid, difference of squares. **No calculus is used anywhere.**
- **Estimated Length**: ~6 minutes
- **Key Insight**: For constant acceleration the velocity–time graph is a *straight line*. Everything follows from two facts about a straight line: its **slope** is the acceleration, and its **average height** is the midpoint of its endpoints. The rest is algebra.
- **Resolution**: 1080p (final); 480p while iterating
- **Aspect Ratio**: 16:9

## Narrative Arc
We open on an object speeding up, with the four equations flashing by as things to be
memorized. We then throw them away and rebuild them from two honest starting points:
the definition of acceleration, and the definition of average velocity. A straight-line
velocity–time graph turns the second one into a fact we can prove by symmetry — no
calculus, no limits, no areas we can't compute. Substituting one result into another
produces the third equation; eliminating time produces the fourth. By the end the four
equations aren't four facts, they're one picture seen four ways.

## The derivation (mathematical spine)

Definitions used, and nothing else:
- acceleration: `a = Δv / Δt` (constant)
- average velocity: `Δx = v_avg · t` (this is the *definition* of average velocity, exactly true)

1. **Equation 1** — from the definition of acceleration
   `a = (v − v₀)/t`  →  `at = v − v₀`  →  **`v = v₀ + at`**

2. **Equation 2** — from the definition of average velocity
   On a straight-line v–t graph, the average height is the midpoint of the endpoints:
   `v_avg = (v₀ + v)/2`. Proven by symmetry — the triangle of "deficit" before the
   halfway time is congruent (a 180° rotation) to the triangle of "surplus" after it.
   `Δx = v_avg · t`  →  **`Δx = ½(v₀ + v)t`**

3. **Equation 3** — substitute Eq 1 into Eq 2 (eliminate `v`)
   `Δx = ½(v₀ + (v₀ + at))t = ½(2v₀ + at)t`  →  **`Δx = v₀t + ½at²`**
   Confirmed geometrically: rectangle (`v₀t`) + triangle (`½·t·at`).

4. **Equation 4** — substitute Eq 1 into Eq 2 (eliminate `t`)
   `t = (v − v₀)/a`, so `Δx = ½(v₀ + v)(v − v₀)/a`.
   Difference of squares: `(v + v₀)(v − v₀) = v² − v₀²`
   `2aΔx = v² − v₀²`  →  **`v² = v₀² + 2aΔx`**

---

## Scene 1: Hook — Four Equations to Memorize
**Duration**: ~35 s
**Purpose**: Establish constant acceleration visually, present the four equations as an
unexplained list, pose the question.

### Visual Elements
- Stroboscopic dot moving along a horizontal track: equal time steps, growing gaps
- Title card, then a 2×2 grid of the four equations fading in
- Closing question in accent color

### Content
A dot travels along a track, stamped once per equal time interval. The gaps grow — that
*is* constant acceleration. Title appears. The four equations fade in as a block, then
the question: "Where do these come from?" and the constraint: "Algebra only."

### Voiceover
- **Text**: "Equal time steps. Growing gaps. That's constant acceleration — and these are
  the four equations that describe it. Most classes hand them to you and say memorize.
  Let's derive all four instead, using nothing but algebra."
- **Sync Points**: "growing gaps" → strobe stamps; "these are the four" → grid fades in

---

## Scene 2: The Five Quantities
**Duration**: ~35 s
**Purpose**: Fix notation and state precisely what "constant acceleration" means.

### Visual Elements
- Motion diagram: start marker (`v₀`), end marker (`v`), brace for `Δx`, arrow for `a`
- Row of five colour-coded cards: `v₀`, `v`, `a`, `t`, `Δx`
- Definition banner

### Content
Every one of the four equations relates the same five quantities. Each equation leaves
exactly one of them out — that turns out to be how you choose which to use. Constant
acceleration means the velocity changes by the same amount every second.

### Voiceover
- **Text**: "Five quantities: starting velocity, ending velocity, acceleration, elapsed
  time, and displacement. Constant acceleration means the velocity changes by the same
  amount every second — no more, no less."

---

## Scene 3: Equation 1 — From the Definition of Acceleration
**Duration**: ~55 s
**Purpose**: Derive `v = v₀ + at` and establish the straight-line v–t graph.

### Visual Elements
- Left: velocity–time axes, straight line from `v₀`, slope triangle showing `Δv` and `Δt`
- Right: four-line algebra stack, each line revealed in turn, final line boxed

### Content
Acceleration is the rate the velocity changes: `a = Δv/Δt`. Start the clock at zero and
that's `a = (v − v₀)/t`. Multiply through by `t`, add `v₀`, done. Note the shape: it's
`y = mx + b`. The velocity–time graph of constant acceleration is a straight line with
intercept `v₀` and slope `a`. That single fact carries the rest of the video.

### Voiceover
- **Text**: "Acceleration is change in velocity divided by change in time. Multiply both
  sides by t. Add v-naught to both sides. Equation one. And look at its shape — y equals
  m x plus b. The velocity–time graph is a straight line."

### Technical Notes
- Shared graph constants `v₀ = 2`, `a = 1.5`, `t_max = 5` reused in scenes 3–5

---

## Scene 4: Equation 2 — The Average Velocity Trick
**Duration**: ~75 s
**Purpose**: Derive `Δx = ½(v₀ + v)t`, the step that would otherwise need calculus.

### Visual Elements
- Constant-velocity case first: flat line, rectangle area `Δx = vt`
- Then the sloped line and the trapezoid
- Dashed line at `v_avg`, midpoint crossing at `t/2`
- Two congruent triangles (deficit red, surplus green), one rotated 180° onto the other

### Content
For steady velocity, `Δx = vt`. When velocity changes, `Δx = v_avg·t` is *still* exactly
true — that's what average velocity means. The only question is what the average is.
For a straight line, it's the midpoint of the endpoints, and we can prove it: the amount
the object falls short of `v_avg` in the first half is a triangle, the amount it exceeds
`v_avg` in the second half is a congruent triangle — rotate one 180° about the midpoint
and it lands exactly on the other. Surplus cancels deficit.

### Voiceover
- **Text**: "Displacement equals average velocity times time — that's not an
  approximation, that's what average means. And for a straight line, the average is just
  the midpoint of the two ends. Watch: rotate the surplus triangle half a turn, and it
  fills the deficit exactly. Every moment that is too slow is matched by one exactly as
  much too fast."
- **Sync Points**: "rotate the surplus" → 180° rotation animation

### Technical Notes
- The 180° rotation is a point reflection, so it is exact even though the axes have
  different x and y scales
- The rotation is a picture of a purely algebraic pairing: at time `t/2 − s` the
  velocity is `v_avg − a·s` and at `t/2 + s` it is `v_avg + a·s`, so every symmetric
  pair of moments averages to `v_avg` exactly. Stating that in words on screen is what
  keeps the "no calculus" claim honest rather than hand-waved

---

## Scene 5: Equation 3 — Substitute and Expand
**Duration**: ~60 s
**Purpose**: Derive `Δx = v₀t + ½at²` and interpret it geometrically.

### Visual Elements
- Equations 1 and 2 side by side at the top
- Substitution chain, with the substituted `v` highlighted
- Graph split into rectangle (`v₀t`) + triangle (`½at²`), each labelled with its meaning

### Content
Equation 2 still contains `v`. Replace it using Equation 1 and simplify: two `v₀` terms
collect, the `t` distributes. The two terms of the answer are exactly the two pieces of
the graph: the rectangle is how far you'd go if you never sped up, the triangle is the
extra distance the acceleration bought you.

### Voiceover
- **Text**: "Equation two still mentions the final velocity. Swap it out using equation
  one. Collect the v-naughts, distribute the t — equation three. And the two terms are
  the two pieces of the picture: rectangle plus triangle."

---

## Scene 6: Equation 4 — Eliminate the Clock
**Duration**: ~65 s
**Purpose**: Derive `v² = v₀² + 2aΔx`.

### Visual Elements
- Framing question: "What if you don't know `t`?"
- Algebra chain, with the difference-of-squares step given its own highlighted callout
- Final boxed result

### Content
Sometimes the time is exactly what you don't have — a dropped stone, a braking car with
skid marks. Solve Equation 1 for `t` and substitute into Equation 2. The numerator is
`(v + v₀)(v − v₀)` — difference of squares — which collapses to `v² − v₀²`. Multiply up
by `2a` and rearrange.

### Voiceover
- **Text**: "Sometimes time is the one thing you don't know. Solve equation one for t,
  substitute, and watch the numerator: v plus v-naught times v minus v-naught. Difference
  of squares. Multiply both sides by two a, rearrange, and there's equation four —
  the only one with no t in it anywhere."

---

## Scene 7: Using Them — A Worked Example
**Duration**: ~55 s
**Purpose**: Show the "missing variable" selection strategy and confirm consistency.

### Visual Elements
- Problem statement card
- Known/unknown list
- Two equations applied, answers boxed
- A green check where two routes agree

### Content
A car starts from rest and accelerates at 3 m/s² for 5 seconds. We know `v₀`, `a`, `t`;
we don't know `v`. Pick the equation missing `v`: `Δx = v₀t + ½at² = 37.5 m`. Then
Equation 1 gives `v = 15 m/s`. Check it with Equation 2: `½(0 + 15)(5) = 37.5 m`. Same
answer — the four equations are one system, not four unrelated rules.

### Voiceover
- **Text**: "From rest, three metres per second squared, five seconds. We don't know the
  final velocity, so use the equation that doesn't contain it. Thirty-seven and a half
  metres. Cross-check with a different equation — same number. They agree because they
  all came from the same straight line."

---

## Scene 8: The Four, Together
**Duration**: ~45 s
**Purpose**: Consolidate; give the practical selection rule; close the arc.

### Visual Elements
- 2×2 grid of the four boxed equations, each tagged with the variable it omits
- Closing line

### Content
Four equations, each missing exactly one of the five quantities. Identify what you have
and what you're missing, and the equation picks itself. And all four came from two
sentences: acceleration is the slope of the line, and displacement is the average height
times the width.

### Voiceover
- **Text**: "Four equations, four missing variables. Find the one you neither know nor
  want, and use the equation without it. Two ideas, one straight line, and algebra did
  the rest."

---

## Transitions & Flow
Scenes 3–6 all reuse the same velocity–time graph geometry (`v₀ = 2`, `a = 1.5`,
`t = 5`), so the picture is continuous across the derivation even as the algebra
changes. Each derived equation is boxed in its own colour when it appears and returns
in that same colour in Scene 8.

## Shared Elements
- The velocity–time straight line — recurring in scenes 3, 4, 5
- Result boxes: every derived equation gets a rounded box in its accent colour
- Colour-coded symbols established in Scene 2 and used throughout

## Colour Palette
- Background: `#0E1116` — near-black slate
- `v₀` initial velocity: `#7FB3FF` (soft blue)
- `v` final velocity: `#5BD1E8` (cyan)
- `a` acceleration: `#FFC857` (amber)
- `t` time: `#C792EA` (violet)
- `Δx` displacement: `#5CD48A` (green)
- Muted / axes / secondary text: `#8A94A6`
- Attention / deficit: `#FF7B72` (coral)
