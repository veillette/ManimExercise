"""Merge the per-scene .srt files Manim emits into one subtitle track for final.mp4.

Manim writes one .srt per scene, each starting at 00:00. Stitching the videos with
ffmpeg concat does not touch them, so each scene's captions have to be pushed forward
by the total duration of everything before it.

Usage (from the project folder):
    python merge_srt.py --quality 1080p60
    python merge_srt.py --quality 480p15 --out final.srt
"""

from __future__ import annotations

import argparse
import pathlib
import re
import subprocess

SCENES = [
    "Scene1_Hook",
    "Scene2_Quantities",
    "Scene3_Equation1",
    "Scene4_Equation2",
    "Scene5_Equation3",
    "Scene6_Equation4",
    "Scene7_Example",
    "Scene8_Summary",
]

TIMING = re.compile(
    r"(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})"
)


def duration(path: pathlib.Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def stamp(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def parse(seconds: tuple[str, ...]) -> float:
    h, m, s, ms = (int(x) for x in seconds)
    return h * 3600 + m * 60 + s + ms / 1000


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quality", default="1080p60",
                    help="media/videos/script/<quality> directory to read from")
    ap.add_argument("--out", default="final.srt")
    args = ap.parse_args()

    src = pathlib.Path("media/videos/script") / args.quality
    blocks: list[str] = []
    offset = 0.0
    index = 1

    for name in SCENES:
        video = src / f"{name}.mp4"
        subs = src / f"{name}.srt"
        if not video.exists():
            raise SystemExit(f"missing {video} — render that scene first")

        if subs.exists():
            for chunk in re.split(r"\n\s*\n", subs.read_text().strip()):
                lines = chunk.strip().splitlines()
                if len(lines) < 3:
                    continue
                match = TIMING.match(lines[1])
                if match is None:
                    continue
                start = parse(match.groups()[:4]) + offset
                end = parse(match.groups()[4:]) + offset
                body = "\n".join(lines[2:])
                blocks.append(f"{index}\n{stamp(start)} --> {stamp(end)}\n{body}")
                index += 1

        offset += duration(video)

    pathlib.Path(args.out).write_text("\n\n".join(blocks) + "\n")
    print(f"wrote {args.out}: {len(blocks)} captions over {offset:.1f}s")


if __name__ == "__main__":
    main()
