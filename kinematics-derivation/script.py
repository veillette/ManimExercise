"""The four kinematics equations for constant acceleration, derived with algebra only.

Every step uses nothing beyond: the definition of acceleration, the definition of
average velocity, the area of a rectangle and a triangle, and ordinary algebra.
No calculus, no limits.

Scenes:
    Scene1_Hook            the four equations, unexplained
    Scene2_Quantities      the five quantities and what "constant acceleration" means
    Scene3_Equation1       v = v0 + a t          (definition of acceleration)
    Scene4_Equation2       dx = 1/2 (v0 + v) t   (average velocity of a straight line)
    Scene5_Equation3       dx = v0 t + 1/2 a t^2 (substitute, eliminate v)
    Scene6_Equation4       v^2 = v0^2 + 2 a dx   (substitute, eliminate t)
    Scene7_Example         a worked problem, cross-checked
    Scene8_Summary         all four, tagged by the variable each one omits
"""

from manim import *

# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------
BG = "#0E1116"
C_V0 = "#7FB3FF"  # initial velocity
C_V = "#5BD1E8"  # final velocity
C_A = "#FFC857"  # acceleration
C_T = "#C792EA"  # time
C_X = "#5CD48A"  # displacement
C_MUTED = "#8A94A6"  # axes, secondary text
C_HI = "#FF7B72"  # attention, "deficit"

config.background_color = BG

# ----------------------------------------------------------------------------
# The one graph the whole derivation lives on: v0 = 2, a = 1.5, t = 5.
# Scenes 3-5 reuse these so the picture stays continuous.
# ----------------------------------------------------------------------------
V0 = 2.0
ACC = 1.5
TMAX = 5.0
VF = V0 + ACC * TMAX  # 9.5
VAVG = (V0 + VF) / 2  # 5.75


def titled(text):
    """Title bar with a hairline rule underneath."""
    label = Text(text, font_size=32, weight="BOLD").to_edge(UP, buff=0.4)
    rule = Line(
        ORIGIN, RIGHT * (config.frame_width - 2.6), stroke_width=1.5, color=C_MUTED
    )
    rule.next_to(label, DOWN, buff=0.18)
    return VGroup(label, rule)


def result_box(mob, color):
    return SurroundingRectangle(
        mob, color=color, buff=0.26, corner_radius=0.14, stroke_width=2.5
    )


def vt_axes():
    """Velocity-time axes, plus their labels. Returns (axes, labels)."""
    ax = Axes(
        x_range=[0, 6.0, 1],
        y_range=[0, 11.5, 2],
        x_length=5.6,
        y_length=3.9,
        tips=True,
        axis_config={"stroke_width": 2.5, "color": C_MUTED, "include_ticks": False},
    )
    lab_t = MathTex("t", color=C_T, font_size=36)
    lab_t.next_to(ax.x_axis.get_end(), DOWN, buff=0.22)
    lab_v = MathTex("v", color=C_V, font_size=36)
    lab_v.next_to(ax.y_axis.get_end(), LEFT, buff=0.22)
    return ax, VGroup(lab_t, lab_v)


def vt_line(ax, color=C_V, v0=V0, acc=ACC, tmax=TMAX):
    return Line(ax.c2p(0, v0), ax.c2p(tmax, v0 + acc * tmax), color=color, stroke_width=4)


# ============================================================================
class Scene1_Hook(Scene):
    def construct(self):
        # --- stroboscopic motion: equal time steps, growing gaps --------------
        track = Line(LEFT * 6.2, RIGHT * 6.2, color=C_MUTED, stroke_width=2)
        track.shift(DOWN * 1.9)

        steps = 8
        x0, x1 = -6.2, 6.2

        def strobe_point(k):
            frac = (k / steps) ** 2
            return track.get_start() + RIGHT * (x1 - x0) * frac

        ball = Dot(strobe_point(0), radius=0.15, color=C_V)
        note = Text("equal time steps", font_size=22, color=C_MUTED)
        note.next_to(track, DOWN, buff=0.45)

        self.play(Create(track), FadeIn(ball), FadeIn(note), run_time=1.0)

        self.add_subcaption(
            "Equal time steps, but growing gaps. That is constant acceleration.",
            duration=3.4,
        )
        for k in range(1, steps + 1):
            ghost = Dot(ball.get_center(), radius=0.07, color=C_V).set_opacity(0.45)
            self.add(ghost)
            self.play(
                ball.animate.move_to(strobe_point(k)), run_time=0.33, rate_func=linear
            )
        self.wait(0.4)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.7)

        # --- title -----------------------------------------------------------
        title = Text("The Four Kinematics Equations", font_size=52, weight="BOLD")
        subtitle = Text(
            "constant acceleration  ·  derived with algebra alone",
            font_size=26,
            color=C_MUTED,
        )
        head = VGroup(title, subtitle).arrange(DOWN, buff=0.35)

        self.add_subcaption("The four kinematics equations for constant acceleration.", duration=2.4)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.wait(0.6)
        self.play(head.animate.scale(0.62).to_edge(UP, buff=0.45), run_time=0.9)

        # --- the four equations, unexplained ---------------------------------
        eqs = VGroup(
            MathTex(r"v = v_0 + a t", font_size=44),
            MathTex(r"\Delta x = \tfrac{1}{2}\,(v_0 + v)\,t", font_size=44),
            MathTex(r"\Delta x = v_0 t + \tfrac{1}{2} a t^2", font_size=44),
            MathTex(r"v^2 = v_0^2 + 2 a \Delta x", font_size=44),
        )
        eqs.arrange_in_grid(rows=2, cols=2, buff=(2.0, 0.9))
        eqs.move_to(DOWN * 0.35)

        self.add_subcaption(
            "Most classes hand you these four and say: memorize them.", duration=3.0
        )
        self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.25) for e in eqs], lag_ratio=0.25),
                  run_time=2.6)
        self.wait(0.8)

        question = Text("Where do they come from?", font_size=32, color=C_A)
        question.to_edge(DOWN, buff=0.6)
        self.add_subcaption("But where do they come from?", duration=2.2)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=1.0)
        self.wait(1.2)

        rule = Text("No calculus. Just algebra.", font_size=32, color=C_X)
        rule.to_edge(DOWN, buff=0.6)
        self.add_subcaption("We will derive all four using nothing but algebra.", duration=2.6)
        self.play(FadeTransform(question, rule), run_time=1.0)
        self.wait(1.6)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ============================================================================
class Scene2_Quantities(Scene):
    def construct(self):
        head = titled("Five quantities. That is all there is.")
        self.play(FadeIn(head[0]), Create(head[1]), run_time=1.0)

        # --- motion diagram ---------------------------------------------------
        track = Line(LEFT * 4.6, RIGHT * 4.6, color=C_MUTED, stroke_width=2)
        track.shift(UP * 1.35)
        start = Dot(track.get_start(), radius=0.11, color=C_V0)
        end = Dot(track.get_end(), radius=0.11, color=C_V)

        lab_start = MathTex("v_0", color=C_V0, font_size=40).next_to(start, UP, buff=0.3)
        lab_end = MathTex("v", color=C_V, font_size=40).next_to(end, UP, buff=0.3)

        arrow = Arrow(
            track.get_start() + RIGHT * 1.4 + UP * 0.75,
            track.get_start() + RIGHT * 3.4 + UP * 0.75,
            buff=0,
            color=C_A,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.18,
        )
        lab_a = MathTex("a", color=C_A, font_size=40).next_to(arrow, UP, buff=0.12)

        brace = Brace(track, direction=DOWN, color=C_MUTED)
        lab_x = MathTex(r"\Delta x", color=C_X, font_size=40)
        lab_x.next_to(brace, DOWN, buff=0.15)

        self.add_subcaption(
            "An object starts at velocity v-naught and ends at velocity v.", duration=3.0
        )
        self.play(Create(track), FadeIn(start), FadeIn(end), run_time=0.9)
        self.play(Write(lab_start), Write(lab_end), run_time=0.8)
        self.add_subcaption(
            "In between, a steady acceleration a, over an elapsed time t.", duration=2.6
        )
        self.play(GrowArrow(arrow), Write(lab_a), run_time=0.9)
        self.play(GrowFromCenter(brace), Write(lab_x), run_time=0.9)
        self.wait(0.5)

        diagram = VGroup(
            track, start, end, lab_start, lab_end, arrow, lab_a, brace, lab_x
        )
        self.play(diagram.animate.scale(0.8).move_to(UP * 1.55), run_time=0.8)

        # --- the five cards ---------------------------------------------------
        def card(sym, meaning, color):
            s = MathTex(sym, color=color, font_size=46)
            m = Text(meaning, font_size=17, color=C_MUTED)
            box = RoundedRectangle(
                width=2.45,
                height=1.55,
                corner_radius=0.14,
                stroke_color=color,
                stroke_width=2,
                fill_color=color,
                fill_opacity=0.07,
            )
            VGroup(s, m).arrange(DOWN, buff=0.24).move_to(box)
            return VGroup(box, s, m)

        cards = VGroup(
            card("v_0", "initial velocity", C_V0),
            card("v", "final velocity", C_V),
            card("a", "acceleration", C_A),
            card("t", "elapsed time", C_T),
            card(r"\Delta x", "displacement", C_X),
        ).arrange(RIGHT, buff=0.2)
        cards.move_to(DOWN * 0.75)

        self.add_subcaption(
            "Five quantities in total, and every equation links them.", duration=2.8
        )
        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cards], lag_ratio=0.15),
            run_time=2.0,
        )
        self.wait(0.6)

        banner = VGroup(
            Text("Constant acceleration means:", font_size=24, color=C_MUTED),
            Text(
                "the velocity changes by the same amount every second.",
                font_size=26,
                color=C_A,
            ),
        ).arrange(DOWN, buff=0.18)
        banner.to_edge(DOWN, buff=0.45)

        self.add_subcaption(
            "Constant acceleration means the velocity changes by the same amount every second.",
            duration=3.4,
        )
        self.play(FadeIn(banner, shift=UP * 0.2), run_time=1.2)
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ============================================================================
class Scene3_Equation1(Scene):
    def construct(self):
        head = titled("Equation 1  ·  from the definition of acceleration")
        self.play(FadeIn(head[0]), Create(head[1]), run_time=1.0)

        # --- graph on the left ------------------------------------------------
        ax, ax_labels = vt_axes()
        graph = VGroup(ax, ax_labels).scale(0.95).move_to(LEFT * 3.7 + DOWN * 0.75)
        line = vt_line(ax)

        v0_dot = Dot(ax.c2p(0, V0), radius=0.075, color=C_V0)
        v0_lab = MathTex("v_0", color=C_V0, font_size=32).next_to(v0_dot, LEFT, buff=0.18)

        self.play(Create(ax), FadeIn(ax_labels), run_time=1.0)
        self.play(FadeIn(v0_dot), Write(v0_lab), run_time=0.6)
        self.add_subcaption(
            "Because the acceleration never changes, the velocity graph is a straight line.",
            duration=3.0,
        )
        self.play(Create(line), run_time=1.4)

        # slope triangle
        t_a, t_b = 2.2, 4.2
        p_a = ax.c2p(t_a, V0 + ACC * t_a)
        p_b = ax.c2p(t_b, V0 + ACC * t_a)
        p_c = ax.c2p(t_b, V0 + ACC * t_b)
        run = Line(p_a, p_b, color=C_T, stroke_width=3.5)
        rise = Line(p_b, p_c, color=C_A, stroke_width=3.5)
        run_lab = MathTex(r"\Delta t", color=C_T, font_size=30).next_to(run, DOWN, buff=0.12)
        rise_lab = MathTex(r"\Delta v", color=C_A, font_size=30).next_to(rise, RIGHT, buff=0.12)

        self.play(Create(run), Write(run_lab), run_time=0.7)
        self.play(Create(rise), Write(rise_lab), run_time=0.7)
        self.wait(0.4)

        # --- algebra on the right ---------------------------------------------
        s1 = MathTex(r"a = \frac{\Delta v}{\Delta t}", font_size=46)
        s2 = MathTex(r"a = \frac{v - v_0}{t}", font_size=46)
        s3 = MathTex(r"a\,t = v - v_0", font_size=46)
        s4 = MathTex(r"v = v_0 + a t", font_size=50)
        steps = VGroup(s1, s2, s3, s4).arrange(DOWN, buff=0.62, aligned_edge=LEFT)
        steps.move_to(RIGHT * 3.0 + DOWN * 0.55)

        hint2 = Text("clock starts at 0", font_size=18, color=C_MUTED)
        hint3 = Text("×  t", font_size=19, color=C_MUTED)
        hint4 = Text("+  v₀", font_size=19, color=C_MUTED)
        # one common left edge so the annotations line up instead of going ragged
        hint_x = steps.get_right()[0] + 0.4
        for hint, step in ((hint2, s2), (hint3, s3), (hint4, s4)):
            hint.next_to(step, RIGHT, buff=0.4)
            hint.align_to(RIGHT * hint_x, LEFT)

        self.add_subcaption(
            "Acceleration is the change in velocity divided by the change in time.",
            duration=3.0,
        )
        self.play(Write(s1), run_time=1.2)
        self.wait(0.6)

        self.add_subcaption(
            "The velocity changes from v-naught to v, over a time t.", duration=2.8
        )
        self.play(TransformMatchingShapes(s1.copy(), s2), FadeIn(hint2), run_time=1.3)
        self.wait(0.6)

        self.add_subcaption("Multiply both sides by t.", duration=2.0)
        self.play(TransformMatchingShapes(s2.copy(), s3), FadeIn(hint3), run_time=1.2)
        self.wait(0.5)

        self.add_subcaption("Add v-naught to both sides, and there is equation one.",
                            duration=3.0)
        self.play(TransformMatchingShapes(s3.copy(), s4), FadeIn(hint4), run_time=1.2)
        box = result_box(s4, C_V)
        tag = Text("Equation 1", font_size=20, color=C_V).next_to(box, DOWN, buff=0.2)
        self.play(Create(box), FadeIn(tag), run_time=0.9)
        self.wait(2.0)

        # --- y = mx + b ---------------------------------------------------------
        self.play(
            FadeOut(VGroup(s1, s2, s3, hint2, hint3, hint4)),
            VGroup(s4, box, tag).animate.move_to(RIGHT * 3.5 + UP * 0.9),
            run_time=1.0,
        )
        shape = VGroup(
            MathTex(r"y = m x + b", font_size=44, color=C_MUTED),
            Text("intercept  v₀     slope  a", font_size=22, color=C_MUTED),
        ).arrange(DOWN, buff=0.35)
        shape.next_to(VGroup(s4, box, tag), DOWN, buff=0.85)

        self.add_subcaption(
            "Look at its shape: y equals m x plus b. Intercept v-naught, slope a.",
            duration=3.4,
        )
        self.play(FadeIn(shape, shift=UP * 0.2), run_time=1.1)
        self.play(Indicate(v0_lab, color=C_V0, scale_factor=1.5),
                  Indicate(rise_lab, color=C_A, scale_factor=1.5), run_time=1.2)
        self.wait(1.6)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ============================================================================
class Scene4_Equation2(Scene):
    def construct(self):
        head = titled("Equation 2  ·  what a straight line averages to")
        self.play(FadeIn(head[0]), Create(head[1]), run_time=1.0)

        ax, ax_labels = vt_axes()
        graph = VGroup(ax, ax_labels).scale(1.02).move_to(LEFT * 3.4 + DOWN * 0.55)

        self.play(Create(ax), FadeIn(ax_labels), run_time=1.0)

        # --- warm-up: constant velocity ---------------------------------------
        flat = Line(ax.c2p(0, VAVG), ax.c2p(TMAX, VAVG), color=C_MUTED, stroke_width=4)
        rect = Polygon(
            ax.c2p(0, 0), ax.c2p(TMAX, 0), ax.c2p(TMAX, VAVG), ax.c2p(0, VAVG),
            stroke_width=0, fill_color=C_X, fill_opacity=0.28,
        )
        warm = MathTex(r"\Delta x = v\,t", font_size=48)
        warm_note = Text("steady velocity: distance is just a rectangle",
                          font_size=21, color=C_MUTED)
        warm_group = VGroup(warm, warm_note).arrange(DOWN, buff=0.4)
        warm_group.move_to(RIGHT * 3.6 + DOWN * 0.4)

        self.add_subcaption(
            "If the velocity never changed, displacement is simply velocity times time.",
            duration=3.2,
        )
        self.play(Create(flat), FadeIn(rect), run_time=1.0)
        self.play(Write(warm), FadeIn(warm_note), run_time=1.2)
        self.wait(1.4)

        # --- the real case ------------------------------------------------------
        line = vt_line(ax)
        trap = Polygon(
            ax.c2p(0, 0), ax.c2p(TMAX, 0), ax.c2p(TMAX, VF), ax.c2p(0, V0),
            stroke_width=0, fill_color=C_X, fill_opacity=0.28,
        )
        self.add_subcaption(
            "But the velocity does change. So what do we use instead?", duration=2.8
        )
        self.play(
            ReplacementTransform(flat, line),
            ReplacementTransform(rect, trap),
            FadeOut(warm_group),
            run_time=1.4,
        )
        self.wait(0.5)

        # --- average velocity is exact -----------------------------------------
        s1 = MathTex(r"\Delta x = v_{\text{avg}} \cdot t", font_size=48)
        s1_note = Text("exactly true — that is what \"average\" means",
                        font_size=20, color=C_MUTED)
        s1_group = VGroup(s1, s1_note).arrange(DOWN, buff=0.35)
        s1_group.move_to(RIGHT * 3.6 + UP * 1.35)

        self.add_subcaption(
            "Displacement equals average velocity times time. That is not an approximation.",
            duration=3.4,
        )
        self.play(Write(s1), run_time=1.2)
        self.play(FadeIn(s1_note), run_time=0.7)
        self.wait(1.0)

        question = Text("So what is the average of a straight line?",
                         font_size=23, color=C_A)
        question.move_to(RIGHT * 3.6 + DOWN * 0.55)
        self.add_subcaption("So what is the average of a straight line?", duration=2.6)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=1.0)
        self.wait(1.2)

        # --- the symmetry proof --------------------------------------------------
        mid_line = DashedLine(
            ax.c2p(0, VAVG), ax.c2p(TMAX, VAVG), color=C_A, stroke_width=3, dash_length=0.12
        )
        # label sits inside the plot: to the left of the axis it would fall off frame
        mid_lab = MathTex(r"v_{\text{avg}}", color=C_A, font_size=30)
        mid_lab.next_to(ax.c2p(0.35, VAVG), UP, buff=0.12)

        self.play(FadeOut(question), run_time=0.4)
        self.add_subcaption(
            "Try the midpoint of the two end velocities.", duration=2.6
        )
        self.play(Create(mid_line), Write(mid_lab), run_time=1.2)

        tri_deficit = Polygon(
            ax.c2p(0, V0), ax.c2p(0, VAVG), ax.c2p(TMAX / 2, VAVG),
            stroke_color=C_HI, stroke_width=2, fill_color=C_HI, fill_opacity=0.55,
        )
        tri_surplus = Polygon(
            ax.c2p(TMAX / 2, VAVG), ax.c2p(TMAX, VAVG), ax.c2p(TMAX, VF),
            stroke_color=C_X, stroke_width=2, fill_color=C_X, fill_opacity=0.55,
        )
        # a small legend in the empty wedge above the line, so nothing sits on
        # top of the triangles or runs off the left edge of the frame
        def key(txt, color):
            swatch = Square(side_length=0.16, stroke_width=0,
                            fill_color=color, fill_opacity=0.75)
            return VGroup(swatch, Text(txt, font_size=16, color=color)).arrange(
                RIGHT, buff=0.12
            )

        lab_def = key("slower than average", C_HI)
        lab_sur = key("faster than average", C_X)
        legend = VGroup(lab_def, lab_sur).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        legend.next_to(ax.c2p(0.75, 11.2), DR, buff=0.0)

        self.add_subcaption(
            "In the first half the object is slower than that midpoint.", duration=2.6
        )
        self.play(FadeIn(tri_deficit), FadeIn(lab_def), run_time=1.0)
        self.add_subcaption(
            "In the second half it is faster, by exactly the same shape.", duration=2.8
        )
        self.play(FadeIn(tri_surplus), FadeIn(lab_sur), run_time=1.0)
        self.wait(0.8)

        # 180-degree rotation is a point reflection, so it lands exactly on the
        # other triangle even though the axes have different x and y scales.
        mover = tri_surplus.copy()
        self.add(mover)
        self.add_subcaption(
            "Rotate the surplus half a turn and it fills the deficit perfectly.",
            duration=3.2,
        )
        self.play(
            Rotate(mover, angle=PI, about_point=ax.c2p(TMAX / 2, VAVG)),
            run_time=2.0,
        )
        self.play(Flash(ax.c2p(TMAX / 4, (V0 + VAVG) / 2), color=WHITE, line_length=0.2),
                  run_time=0.8)
        self.wait(0.6)

        # spell out the pairing the rotation is showing: it is the whole no-calculus
        # argument, and it is pure algebra -- at time t/2 - s the velocity is
        # v_avg - a*s, and at t/2 + s it is v_avg + a*s, so each pair averages to v_avg
        verdict = VGroup(
            Text("Every moment that is too slow is matched", font_size=21, color=C_A),
            Text("by one that is exactly as much too fast.", font_size=21, color=C_A),
            Text("surplus = deficit", font_size=25, color=C_A),
        ).arrange(DOWN, buff=0.22)
        verdict.move_to(RIGHT * 3.6 + DOWN * 0.85)
        self.add_subcaption(
            "Every moment that is too slow is matched by one exactly as much too fast.",
            duration=3.6,
        )
        self.play(FadeIn(verdict[0]), FadeIn(verdict[1]), run_time=1.0)
        self.wait(1.2)
        self.play(FadeIn(verdict[2]), run_time=0.7)
        self.wait(1.2)
        self.play(FadeOut(mover), FadeOut(tri_deficit), FadeOut(tri_surplus),
                  FadeOut(lab_def), FadeOut(lab_sur), run_time=0.8)

        # --- the result -----------------------------------------------------------
        s2 = MathTex(r"v_{\text{avg}} = \frac{v_0 + v}{2}", font_size=46)
        s3 = MathTex(r"\Delta x = \frac{1}{2}\,(v_0 + v)\,t", font_size=50)
        results = VGroup(s2, s3).arrange(DOWN, buff=0.85)
        results.move_to(RIGHT * 3.6 + DOWN * 1.25)

        self.add_subcaption(
            "So the average velocity is the midpoint of the two ends.", duration=2.8
        )
        self.play(FadeTransform(verdict, s2), run_time=1.2)
        self.wait(0.7)
        self.add_subcaption("Put that back in, and there is equation two.", duration=2.8)
        self.play(TransformMatchingShapes(VGroup(s1.copy(), s2.copy()), s3), run_time=1.5)
        box = result_box(s3, C_X)
        tag = Text("Equation 2", font_size=20, color=C_X).next_to(box, DOWN, buff=0.2)
        self.play(Create(box), FadeIn(tag), run_time=0.9)
        self.wait(1.8)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ============================================================================
class Scene5_Equation3(Scene):
    def construct(self):
        head = titled("Equation 3  ·  substitute, and lose the final velocity")
        self.play(FadeIn(head[0]), Create(head[1]), run_time=1.0)

        # --- what we already have ------------------------------------------------
        known1 = MathTex(r"v = v_0 + a t", font_size=38, color=C_V)
        known2 = MathTex(r"\Delta x = \tfrac{1}{2}(v_0 + v)\,t", font_size=38, color=C_X)
        tag1 = Text("Equation 1", font_size=17, color=C_MUTED)
        tag2 = Text("Equation 2", font_size=17, color=C_MUTED)
        col1 = VGroup(known1, tag1).arrange(DOWN, buff=0.16)
        col2 = VGroup(known2, tag2).arrange(DOWN, buff=0.16)
        banner = VGroup(col1, col2).arrange(RIGHT, buff=1.8)
        banner.next_to(head, DOWN, buff=0.45)

        self.play(FadeIn(banner), run_time=1.0)

        problem = Text(
            "Equation 2 still mentions v. Replace it using Equation 1.",
            font_size=23, color=C_A,
        )
        problem.next_to(banner, DOWN, buff=0.5)
        self.add_subcaption(
            "Equation two still mentions the final velocity. Replace it using equation one.",
            duration=3.6,
        )
        self.play(FadeIn(problem, shift=UP * 0.15), run_time=1.0)
        self.wait(1.4)

        # --- the substitution chain ---------------------------------------------
        chain = VGroup(
            MathTex(r"\Delta x = \tfrac{1}{2}\big(v_0 + (v_0 + a t)\big)\,t", font_size=44),
            MathTex(r"\Delta x = \tfrac{1}{2}\big(2 v_0 + a t\big)\,t", font_size=44),
            MathTex(r"\Delta x = \big(v_0 + \tfrac{1}{2} a t\big)\,t", font_size=44),
            MathTex(r"\Delta x = v_0 t + \tfrac{1}{2} a t^2", font_size=50),
        ).arrange(DOWN, buff=0.5)
        chain.next_to(problem, DOWN, buff=0.55)

        hints = [
            "substitute",
            "collect the two v₀ terms",
            "halve the bracket",
            "distribute the t",
        ]
        captions = [
            "Substitute v-naught plus a t in place of v.",
            "The two v-naught terms collect into two v-naught.",
            "Halve everything inside the bracket.",
            "Distribute the t, and there is equation three.",
        ]

        prev = None
        hint_mobs = VGroup()
        for step, hint_text, cap in zip(chain, hints, captions):
            hint = Text(hint_text, font_size=18, color=C_MUTED)
            hint.next_to(step, RIGHT, buff=0.5)
            hint_mobs.add(hint)
            self.add_subcaption(cap, duration=2.6)
            if prev is None:
                self.play(Write(step), FadeIn(hint), run_time=1.2)
            else:
                self.play(TransformMatchingShapes(prev.copy(), step), FadeIn(hint),
                          run_time=1.3)
            self.wait(0.5)
            prev = step

        final = chain[3]
        box = result_box(final, C_X)
        tag = Text("Equation 3", font_size=20, color=C_X).next_to(box, RIGHT, buff=0.35)
        self.play(Create(box), FadeOut(hint_mobs[3]), run_time=0.7)
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(1.6)

        # --- the geometric reading ------------------------------------------------
        self.play(
            FadeOut(banner), FadeOut(problem),
            FadeOut(hint_mobs[0]), FadeOut(hint_mobs[1]), FadeOut(hint_mobs[2]),
            FadeOut(chain[0]), FadeOut(chain[1]), FadeOut(chain[2]),
            VGroup(final, box, tag).animate.scale(0.85).move_to(RIGHT * 3.5 + UP * 1.6),
            run_time=1.0,
        )

        ax, ax_labels = vt_axes()
        VGroup(ax, ax_labels).scale(0.95).move_to(LEFT * 3.6 + DOWN * 0.55)
        line = vt_line(ax)

        rect = Polygon(
            ax.c2p(0, 0), ax.c2p(TMAX, 0), ax.c2p(TMAX, V0), ax.c2p(0, V0),
            stroke_width=0, fill_color=C_V0, fill_opacity=0.4,
        )
        tri = Polygon(
            ax.c2p(0, V0), ax.c2p(TMAX, V0), ax.c2p(TMAX, VF),
            stroke_width=0, fill_color=C_A, fill_opacity=0.45,
        )

        self.play(Create(ax), FadeIn(ax_labels), Create(line), run_time=1.2)

        piece1 = VGroup(
            MathTex(r"v_0 t", font_size=38, color=C_V0),
            Text("how far you would go\nif you never sped up", font_size=18, color=C_MUTED),
        ).arrange(DOWN, buff=0.2)
        piece2 = VGroup(
            MathTex(r"\tfrac{1}{2} a t^2", font_size=38, color=C_A),
            Text("the extra distance the\nacceleration bought you", font_size=18, color=C_MUTED),
        ).arrange(DOWN, buff=0.2)
        pieces = VGroup(piece1, piece2).arrange(DOWN, buff=0.65)
        pieces.move_to(RIGHT * 3.5 + DOWN * 1.1)

        self.add_subcaption(
            "The rectangle is how far you would go if you never sped up.", duration=3.0
        )
        self.play(FadeIn(rect), FadeIn(piece1), run_time=1.2)
        self.wait(0.8)
        self.add_subcaption(
            "The triangle is the extra distance the acceleration bought you.", duration=3.0
        )
        self.play(FadeIn(tri), FadeIn(piece2), run_time=1.2)
        self.wait(0.8)
        self.add_subcaption(
            "Two terms in the equation, two pieces in the picture.", duration=2.8
        )
        self.play(Indicate(final, color=WHITE, scale_factor=1.08), run_time=1.2)
        self.wait(1.6)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ============================================================================
class Scene6_Equation4(Scene):
    def construct(self):
        head = titled("Equation 4  ·  when you do not know the time")
        self.play(FadeIn(head[0]), Create(head[1]), run_time=1.0)

        motive = VGroup(
            Text("A dropped stone. A car braking to a stop.", font_size=25, color=C_MUTED),
            Text("Sometimes the clock is the one thing you never measured.",
                 font_size=25, color=C_A),
        ).arrange(DOWN, buff=0.25)
        motive.next_to(head, DOWN, buff=0.6)

        self.add_subcaption(
            "Sometimes time is the one thing you do not know.", duration=3.0
        )
        self.play(FadeIn(motive, shift=UP * 0.15), run_time=1.2)
        self.wait(1.6)
        self.play(FadeOut(motive), run_time=0.6)

        # --- solve equation 1 for t ----------------------------------------------
        left = VGroup(
            MathTex(r"v = v_0 + a t", font_size=40, color=C_V),
            MathTex(r"v - v_0 = a t", font_size=40),
            MathTex(r"t = \frac{v - v_0}{a}", font_size=44, color=C_T),
        ).arrange(DOWN, buff=0.55)
        left.move_to(LEFT * 3.9 + UP * 0.9)
        lead = Text("Solve Equation 1 for t:", font_size=22, color=C_MUTED)
        lead.next_to(left, UP, buff=0.4)

        self.add_subcaption("Take equation one and solve it for t.", duration=2.8)
        self.play(FadeIn(lead), Write(left[0]), run_time=1.2)
        self.play(TransformMatchingShapes(left[0].copy(), left[1]), run_time=1.0)
        self.play(TransformMatchingShapes(left[1].copy(), left[2]), run_time=1.0)
        t_box = result_box(left[2], C_T)
        self.play(Create(t_box), run_time=0.6)
        self.wait(1.0)

        # --- substitute into equation 2 --------------------------------------------
        right_lead = Text("Put it into Equation 2:", font_size=22, color=C_MUTED)
        r1 = MathTex(r"\Delta x = \tfrac{1}{2}(v_0 + v)\,t", font_size=40, color=C_X)
        r2 = MathTex(r"\Delta x = \frac{(v_0 + v)(v - v_0)}{2a}", font_size=42)
        right = VGroup(r1, r2).arrange(DOWN, buff=0.6)
        right.move_to(RIGHT * 3.7 + UP * 0.85)
        right_lead.next_to(right, UP, buff=0.4)

        self.add_subcaption("Now put that into equation two.", duration=2.4)
        self.play(FadeIn(right_lead), Write(r1), run_time=1.2)
        self.play(TransformMatchingShapes(VGroup(r1.copy(), left[2].copy()), r2),
                  run_time=1.5)
        self.wait(1.0)

        # --- difference of squares ---------------------------------------------------
        callout_math = MathTex(r"(v_0 + v)(v - v_0) = v^2 - v_0^2", font_size=40, color=C_A)
        callout_note = Text("difference of squares", font_size=20, color=C_MUTED)
        callout = VGroup(callout_math, callout_note).arrange(DOWN, buff=0.2)
        callout.to_edge(DOWN, buff=0.75)
        callout_box = SurroundingRectangle(
            callout, color=C_A, buff=0.3, corner_radius=0.14, stroke_width=2
        )

        self.add_subcaption(
            "Look at that numerator: v plus v-naught, times v minus v-naught.", duration=3.2
        )
        self.play(Circumscribe(r2, color=C_A, buff=0.15), run_time=1.2)
        self.add_subcaption("That is a difference of squares.", duration=2.4)
        self.play(FadeIn(callout), Create(callout_box), run_time=1.2)
        self.wait(1.6)

        # --- finish ---------------------------------------------------------------
        self.play(
            FadeOut(VGroup(left, lead, t_box, right_lead, r1)),
            VGroup(callout, callout_box).animate.scale(0.8).to_edge(UP, buff=1.35),
            r2.animate.move_to(DOWN * 0.35),
            run_time=1.2,
        )

        f1 = MathTex(r"\Delta x = \frac{v^2 - v_0^2}{2a}", font_size=46)
        f2 = MathTex(r"2 a \Delta x = v^2 - v_0^2", font_size=46)
        f3 = MathTex(r"v^2 = v_0^2 + 2 a \Delta x", font_size=54)
        finish = VGroup(f1, f2, f3).arrange(DOWN, buff=0.5)
        finish.move_to(DOWN * 0.9)

        self.add_subcaption("So the numerator collapses to v squared minus v-naught squared.",
                            duration=3.0)
        self.play(TransformMatchingShapes(r2, f1), run_time=1.4)
        self.wait(0.6)
        self.add_subcaption("Multiply both sides by two a.", duration=2.2)
        self.play(TransformMatchingShapes(f1.copy(), f2), run_time=1.2)
        self.wait(0.5)
        self.add_subcaption("Rearrange, and there is equation four.", duration=2.6)
        self.play(TransformMatchingShapes(f2.copy(), f3), run_time=1.2)

        box = result_box(f3, C_V)
        tag = Text("Equation 4", font_size=20, color=C_V).next_to(box, RIGHT, buff=0.35)
        self.play(Create(box), FadeIn(tag), run_time=0.9)
        self.wait(0.8)

        no_t = Text("no t anywhere", font_size=22, color=C_T)
        no_t.next_to(box, LEFT, buff=0.35)
        self.add_subcaption("Notice there is no t in it anywhere.", duration=2.6)
        self.play(FadeIn(no_t, shift=RIGHT * 0.15), run_time=1.0)
        self.wait(1.8)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ============================================================================
class Scene7_Example(Scene):
    def construct(self):
        head = titled("Choosing one:  find the variable you don't have")
        self.play(FadeIn(head[0]), Create(head[1]), run_time=1.0)

        problem = Text(
            "A car starts from rest and accelerates at 3 m/s² for 5 seconds.\n"
            "How far does it travel?",
            font_size=27,
            line_spacing=0.9,
        )
        problem.next_to(head, DOWN, buff=0.5)
        p_box = SurroundingRectangle(
            problem, color=C_MUTED, buff=0.3, corner_radius=0.14, stroke_width=1.5
        )
        self.add_subcaption(
            "A car starts from rest and accelerates at three metres per second squared "
            "for five seconds.",
            duration=4.0,
        )
        self.play(FadeIn(problem), Create(p_box), run_time=1.4)
        self.wait(1.4)

        knowns = VGroup(
            MathTex(r"v_0 = 0", font_size=34, color=C_V0),
            MathTex(r"a = 3\ \text{m/s}^2", font_size=34, color=C_A),
            MathTex(r"t = 5\ \text{s}", font_size=34, color=C_T),
            MathTex(r"v = \ ?", font_size=34, color=C_V),
            MathTex(r"\Delta x = \ ?", font_size=34, color=C_X),
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        knowns.move_to(LEFT * 4.6 + DOWN * 1.15)

        self.add_subcaption("We know v-naught, a, and t. We want the displacement.",
                            duration=3.0)
        self.play(LaggedStart(*[FadeIn(k, shift=RIGHT * 0.15) for k in knowns],
                              lag_ratio=0.2), run_time=1.8)
        self.wait(0.8)

        rule = Text("We don't know v — so use the equation without v.",
                     font_size=24, color=C_A)
        rule.move_to(RIGHT * 1.55 + DOWN * 0.15)
        self.add_subcaption(
            "We do not know the final velocity, so use the equation that leaves it out.",
            duration=3.4,
        )
        self.play(FadeIn(rule, shift=UP * 0.15), run_time=1.1)
        self.wait(1.2)

        work = VGroup(
            MathTex(r"\Delta x = v_0 t + \tfrac{1}{2} a t^2", font_size=38),
            MathTex(r"\Delta x = (0)(5) + \tfrac{1}{2}(3)(5)^2", font_size=38),
            MathTex(r"\Delta x = 37.5\ \text{m}", font_size=42, color=C_X),
        ).arrange(DOWN, buff=0.42)
        work.move_to(RIGHT * 1.55 + DOWN * 1.75)

        self.add_subcaption("That is equation three. Plug in the numbers.", duration=2.8)
        self.play(Write(work[0]), run_time=1.0)
        self.play(TransformMatchingShapes(work[0].copy(), work[1]), run_time=1.2)
        self.add_subcaption("Thirty-seven and a half metres.", duration=2.4)
        self.play(TransformMatchingShapes(work[1].copy(), work[2]), run_time=1.2)
        ans_box = result_box(work[2], C_X)
        self.play(Create(ans_box), run_time=0.7)
        self.wait(1.4)

        # --- cross-check ------------------------------------------------------------
        self.play(
            FadeOut(VGroup(problem, p_box, rule, work[0], work[1])),
            VGroup(work[2], ans_box).animate.move_to(RIGHT * 1.4 + UP * 1.9),
            knowns.animate.move_to(LEFT * 4.9 + UP * 0.4),
            run_time=1.1,
        )

        check = VGroup(
            Text("Cross-check with two other equations:", font_size=23, color=C_MUTED),
            MathTex(r"v = v_0 + a t = 0 + (3)(5) = 15\ \text{m/s}", font_size=36),
            MathTex(r"\Delta x = \tfrac{1}{2}(v_0 + v)t "
                    r"= \tfrac{1}{2}(0 + 15)(5) = 37.5\ \text{m}", font_size=36),
        ).arrange(DOWN, buff=0.55)
        check.move_to(RIGHT * 1.4 + DOWN * 0.9)

        self.add_subcaption(
            "Equation one gives the final velocity: fifteen metres per second.", duration=3.2
        )
        self.play(FadeIn(check[0]), run_time=0.7)
        self.play(Write(check[1]), run_time=1.6)
        self.wait(0.7)
        self.add_subcaption(
            "Feed that into equation two, and it gives the same displacement.", duration=3.2
        )
        self.play(Write(check[2]), run_time=1.8)
        self.wait(0.6)

        tick = Text("✓  same answer", font_size=28, color=C_X)
        tick.next_to(check, DOWN, buff=0.45)
        self.add_subcaption(
            "They agree, because all four came from the same straight line.", duration=3.2
        )
        self.play(FadeIn(tick, shift=UP * 0.15), run_time=1.0)
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ============================================================================
class Scene8_Summary(Scene):
    def construct(self):
        head = titled("The four equations")
        sub = Text("each one leaves out exactly one of the five quantities",
                    font_size=21, color=C_MUTED)
        sub.next_to(head, DOWN, buff=0.22)
        self.play(FadeIn(head[0]), Create(head[1]), run_time=1.0)
        self.play(FadeIn(sub), run_time=0.6)

        def entry(tex, missing, color, n):
            eq = MathTex(tex, font_size=40)
            box = SurroundingRectangle(
                eq, color=color, buff=0.28, corner_radius=0.14, stroke_width=2.2
            )
            num = Text(f"Equation {n}", font_size=16, color=C_MUTED)
            num.next_to(box, UP, buff=0.14).align_to(box, LEFT)
            tag = VGroup(
                Text("missing:", font_size=17, color=C_MUTED),
                MathTex(missing, font_size=26, color=C_HI),
            ).arrange(RIGHT, buff=0.14)
            tag.next_to(box, DOWN, buff=0.18)
            return VGroup(box, eq, num, tag)

        grid = VGroup(
            entry(r"v = v_0 + a t", r"\Delta x", C_V, 1),
            entry(r"\Delta x = \tfrac{1}{2}(v_0 + v)\,t", "a", C_X, 2),
            entry(r"\Delta x = v_0 t + \tfrac{1}{2} a t^2", "v", C_X, 3),
            entry(r"v^2 = v_0^2 + 2 a \Delta x", "t", C_V, 4),
        ).arrange_in_grid(rows=2, cols=2, buff=(1.5, 1.0))
        grid.move_to(DOWN * 0.35)

        self.add_subcaption(
            "Four equations, and each one leaves out exactly one of the five quantities.",
            duration=4.0,
        )
        self.play(
            LaggedStart(*[FadeIn(g, shift=UP * 0.2) for g in grid], lag_ratio=0.3),
            run_time=3.0,
        )
        self.wait(1.6)

        self.add_subcaption(
            "Find the quantity you neither know nor want, and the equation picks itself.",
            duration=3.6,
        )
        self.play(
            LaggedStart(*[Indicate(g[3], color=C_HI, scale_factor=1.25) for g in grid],
                        lag_ratio=0.2),
            run_time=2.4,
        )
        self.wait(1.2)

        self.play(grid.animate.scale(0.82).shift(UP * 0.35), run_time=0.9)

        closing = VGroup(
            Text("Two ideas did all the work:", font_size=23, color=C_MUTED),
            Text("acceleration is the slope of the line", font_size=23, color=C_A),
            Text("displacement is its average height times the width",
                 font_size=23, color=C_A),
        ).arrange(DOWN, buff=0.18)
        closing.to_edge(DOWN, buff=0.4)

        self.add_subcaption(
            "Two ideas did all the work: acceleration is the slope of the line, and "
            "displacement is its average height times the width.",
            duration=5.0,
        )
        self.play(FadeIn(closing, shift=UP * 0.15), run_time=1.4)
        self.wait(2.4)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)
        self.wait(0.4)
