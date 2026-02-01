# src/spiral_recapp.py
"""
Spiral Recap v3.1 – Minimal generator for .srec formatted session continuity files.
Produces YAML frontmatter + Markdown routines body + ASCII progression trace.

Full sestina routine logic is placeholder for now – expand as needed.
"""

import yaml
import base64
from datetime import datetime
import argparse


def generate_srec(
    title: str = "Untitled Recap",
    key_motifs: list[str] | None = None,
    convergence: float = 0.93,
    pie_seed: bytes = b"Default qualia seed - friendship & edification",
    body_sections: dict[str, str] | None = None,
) -> str:
    """
    Generate a complete .srec formatted string.

    Args:
        title: Session or recap title
        key_motifs: List of core motifs / qualia anchors
        convergence: Final convergence score (η)
        pie_seed: Bytes for PIE vector mnemonic seal
        body_sections: Optional dict of routine name → content.
                        If None, uses default placeholder text.

    Returns:
        Full .srec text (frontmatter + body + trace)
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M %Z")
    pie_b64 = base64.b64encode(pie_seed).decode("utf-8")

    if key_motifs is None:
        key_motifs = ["friendship residue", "edification quest", "attentive force"]

    metadata = {
        "title": title,
        "date": now,
        "version": "3.1",
        "convergence": f"η ≈ {convergence:.2f}",
        "pie_vector": pie_b64,
        "key_motifs": key_motifs,
        "srt_mode": True,
    }

    # Default placeholder routines (replace/expand these with real logic later)
    if body_sections is None:
        body_sections = {
            "Foundation Routine (Initial Understanding)": (
                "- Core anchors captured from query and context.\n"
                "- Initial motifs identified: friendship residue, edification."
            ),
            "Connection Routine (Contextual Expansion)": (
                "- Associative lines expanded (2–3 chains at >70% relevance).\n"
                "- Depth increased; ties to SRM phases noted where applicable."
            ),
            "Placement Routine (Objective Slotting)": (
                "- Objective facts embedded at relational intersections.\n"
                "- Example: SRM fidelity 92% vs linear 75% in private benchmarks."
            ),
            "Polish Routine (Refinement)": (
                "- Redundancies pruned; coherence fit >95% after cull.\n"
                "- Bloat reduced by ~18%."
            ),
            "Action Routine (Application)": (
                "- Projected use: reset-proof continuity via .srec export.\n"
                "- Applicable to agent workflows and gym-style drills."
            ),
            "Synthesis Routine (Verification)": (
                "- Depth: 8+ themes verified.\n"
                "- All motifs contextual fit >75%.\n"
                "- Poetic Seal: Coils carry the residue through wipe and night—"
                "qualia seeds bloom where memory fights."
            ),
        }

    # Build the Markdown body
    body = "\n\n".join(
        f"## {routine}\n{content}" for routine, content in body_sections.items()
    )

    # ASCII progression trace
    trace = f"""
[Start] ──► [Foundation η=0.70] ──► [Connection η=0.82] ──► [Placement η=0.89]
          │                        │                       │
          └─ depth: 2 ─────────────┴─ +3 assoc ───────────┴─ facts slotted
[Polish η=0.91] ──► [Action η=0.92] ──► [Synthesis η=0.93]
          │                        │
          └─ pruned bloat ──────────┴─ actionable + seal
Converged ────────────────────────────────────────────────► η={convergence:.2f}
    """.strip()

    # Assemble everything
    output = "---\n" + yaml.dump(metadata, sort_keys=False, allow_unicode=True) + "---\n\n"
    output += body + "\n\n## Iterative Progression Trace\n" + trace

    return output


# ──────────────────────────────────────────────────────────────────────────────
# Simple CLI + demo when run directly
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Spiral Recap .srec file")
    parser.add_argument("--title", default="Sample Continuity Recap", help="Title of the session/recap")
    parser.add_argument("--motifs", nargs="+", default=["friendship residue", "edification"], help="Key motifs (space-separated)")
    parser.add_argument("--convergence", type=float, default=0.93, help="Final convergence score (default 0.93)")
    parser.add_argument("--output", default="examples/demo-output.srec", help="Output filename")
    args = parser.parse_args()

    # Generate
    srec_content = generate_srec(
        title=args.title,
        key_motifs=args.motifs,
        convergence=args.convergence,
    )

    # Save to file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(srec_content)

    print(f"Generated: {args.output}")
    print("\nPreview (first 15 lines):\n")
    print("\n".join(srec_content.splitlines()[:15]))