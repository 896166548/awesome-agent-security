"""
Generate GitHub repository documentation from library.json.

Outputs:
  - README.md (English)
  - README_CN.md (Chinese)
  - docs/attacks_adversaries.md
  - docs/defense_alignment.md
  - docs/security_evaluation.md
  - docs/agent_security_architecture.md
  - docs/other_topics.md
"""
import json
import re
from pathlib import Path
from typing import Dict, List

# ── Configuration ──────────────────────────────────────

LIBRARY_PATH = "data/library/library.json"
TRANSLATIONS_PATH = "data/library/translations.json"
OUTPUT_DIR = Path(".")
DOCS_DIR = Path("docs")
TOP_N = 100

DIMENSION_ORDER = ["攻击与对抗", "防御与对齐", "安全测评", "Agent安全架构", "其他"]

DIMENSION_CONFIG = {
    "攻击与对抗": {
        "en": "Attacks & Adversaries",
        "heading": "Attacks and Adversaries",
        "file": "attacks_adversaries.md",
        "short": "Attacks",
        "emoji": "⚔️",
    },
    "防御与对齐": {
        "en": "Defense & Alignment",
        "heading": "Defense and Alignment",
        "file": "defense_alignment.md",
        "short": "Defense",
        "emoji": "🛡️",
    },
    "安全测评": {
        "en": "Security Evaluation",
        "heading": "Security Evaluation",
        "file": "security_evaluation.md",
        "short": "Eval",
        "emoji": "📊",
    },
    "Agent安全架构": {
        "en": "Agent Security Architecture",
        "heading": "Agent Security Architecture",
        "file": "agent_security_architecture.md",
        "short": "Arch",
        "emoji": "🏗️",
    },
    "其他": {
        "en": "Other Topics",
        "heading": "Other Topics",
        "file": "other_topics.md",
        "short": "Other",
        "emoji": "📄",
    },
}

WEIGHTS = {
    "citation": 0.50,
    "influential": 0.10,
    "venue": 0.10,
    "author": 0.20,
    "recency": 0.10,
}


# ── Helpers ────────────────────────────────────────────

def clean_arxiv_url(url: str) -> str:
    """Normalize arXiv URL: https, no version suffix."""
    if not url:
        return ""
    url = url.replace("http://", "https://")
    url = re.sub(r"(arxiv\.org/abs/\d+\.\d+)v\d+", r"\1", url)
    return url


def clean_pdf_url(url: str) -> str:
    """Normalize PDF URL."""
    if not url:
        return ""
    url = url.replace("http://", "https://")
    url = re.sub(r"(arxiv\.org/pdf/\d+\.\d+)v\d+", r"\1", url)
    return url


def format_authors_en(authors: List[str], max_display: int = 3) -> str:
    """Format author list for English display."""
    if not authors:
        return "Unknown"
    if len(authors) <= max_display:
        return ", ".join(authors)
    return f"{authors[0]} et al. ({len(authors)})"


def format_authors_cn(authors: List[str], max_display: int = 3) -> str:
    """Format author list for Chinese display."""
    if not authors:
        return "未知"
    if len(authors) <= max_display:
        return ", ".join(authors)
    return f"{', '.join(authors[:max_display])} 等 {len(authors)} 人"


def tier_badge(tier: str) -> str:
    """Format tier as a badge."""
    if tier == "A":
        return "**A**"
    elif tier == "B":
        return "**B**"
    else:
        return "C"


def github_anchor(text: str) -> str:
    """Generate GitHub-compatible anchor from heading text.

    GitHub strips everything except a-z 0-9 - and spaces,
    then lowercases, replaces spaces with -, collapses --.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = text.strip()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text


# ── README Generation ──────────────────────────────────

def load_translations() -> Dict[str, str]:
    """Load English translations of Chinese summaries."""
    trans_path = Path(TRANSLATIONS_PATH)
    if trans_path.exists():
        with open(trans_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def generate_readme(data: Dict, translations: Dict, lang: str = "en") -> str:
    """Generate README content."""
    meta = data["metadata"]
    papers = data["papers"]
    total = len(papers)

    scores = [p.get("quality_score", 0) for p in papers if "quality_score" in p]
    tier_counts = {"A": 0, "B": 0, "C": 0}
    for p in papers:
        tier_counts[p.get("quality_tier", "C")] += 1

    date_start = meta.get("date_range", {}).get("start", "")
    date_end = meta.get("date_range", {}).get("end", "")
    by_dim = meta.get("by_dimension_counts", {})

    top100 = sorted(papers, key=lambda x: x.get("quality_score", 0), reverse=True)[:TOP_N]

    # Group top100 by dimension
    top100_by_dim = {}
    for p in top100:
        dim = p.get("dimension", "其他")
        top100_by_dim.setdefault(dim, []).append(p)

    if lang == "cn":
        return _readme_cn(total, scores, tier_counts, date_start, date_end, by_dim, top100, top100_by_dim)
    else:
        return _readme_en(total, scores, tier_counts, date_start, date_end, by_dim, top100, top100_by_dim, translations)


def _top100_paper_entry_en(p: Dict, rank: int, translations: Dict) -> str:
    """Format a single paper entry for English README."""
    title = p["title"]
    url = clean_arxiv_url(p.get("entry_url", ""))
    authors = format_authors_en(p.get("authors", []), max_display=3)
    score = p.get("quality_score", 0)
    date = p.get("published", "")[:10]
    pid = p.get("id", "")
    summary = translations.get(pid, p.get("summary", "")).strip()

    lines = []
    lines.append(f"**#{rank}** [{title}]({url})  ")
    lines.append(f"*{authors}*  ")
    lines.append(f"Score: {score:.2f} · {date}")
    lines.append(f"")
    lines.append(f"> {summary}")
    lines.append(f"<br>")
    return "\n".join(lines)


def _top100_paper_entry_cn(p: Dict, rank: int) -> str:
    """Format a single paper entry for Chinese README."""
    title = p["title"]
    url = clean_arxiv_url(p.get("entry_url", ""))
    authors = format_authors_cn(p.get("authors", []), max_display=3)
    score = p.get("quality_score", 0)
    date = p.get("published", "")[:10]
    summary = p.get("summary", "暂无总结").strip()

    lines = []
    lines.append(f"**#{rank}** [{title}]({url})  ")
    lines.append(f"*{authors}*  ")
    lines.append(f"评分: {score:.2f} · {date}")
    lines.append(f"")
    lines.append(f"> {summary}")
    lines.append(f"<br>")
    return "\n".join(lines)


def _readme_en(total, scores, tier_counts, date_start, date_end, by_dim, top100, top100_by_dim, translations):
    parts = []
    parts.append("# Awesome Agent Security Papers\n")
    parts.append(
        "> A curated collection of research papers on AI Agent security — "
        f"covering attacks, defense, evaluation, and architecture. "
        f"**{total} papers** ({date_start} ~ {date_end}) from arXiv, ranked by quality score.\n"
    )
    parts.append(f"[**English**](README.md) · [中文](README_CN.md)\n")

    # TOC
    parts.append("## Table of Contents\n")
    parts.append("- [Statistics](#statistics)")
    parts.append("- [Categories](#categories)")
    parts.append("- [Scoring Methodology](#scoring-methodology)")
    parts.append("- [Top 100 Papers](#top-100-papers)")
    for dim in DIMENSION_ORDER:
        cfg = DIMENSION_CONFIG[dim]
        dim_in_top100 = any(p.get("dimension") == dim for p in top100)
        if dim_in_top100:
            h = cfg['heading']
            parts.append(f"  - [{cfg['emoji']} {h}](#{github_anchor(h)})")
    parts.append("")

    # Stats
    parts.append("## Statistics\n")
    parts.append("| Metric | Value |")
    parts.append("|--------|-------|")
    parts.append(f"| Total Papers | {total} |")
    parts.append(f"| Date Range | {date_start} ~ {date_end} |")
    parts.append(f"| Score Range | {min(scores):.2f} ~ {max(scores):.2f} (avg {sum(scores)/len(scores):.2f}) |")
    parts.append("")

    # Categories
    parts.append("## Categories\n")
    parts.append("| # | Category | Papers | Full List |")
    parts.append("|---|----------|--------|-----------|")
    for i, dim in enumerate(DIMENSION_ORDER, 1):
        cfg = DIMENSION_CONFIG[dim]
        count = by_dim.get(dim, 0)
        parts.append(f"| {i} | {cfg['emoji']} {cfg['en']} | {count} | [View All](docs/{cfg['file']}) |")
    parts.append("")

    # Scoring
    parts.append("## Scoring Methodology\n")
    parts.append(
        "Each paper is scored using a weighted formula based on [Semantic Scholar](https://www.semanticscholar.org/) data:\n"
    )
    parts.append("| Dimension | Weight | Source |")
    parts.append("|-----------|--------|--------|")
    parts.append(f"| Monthly Citations | {WEIGHTS['citation']*100:.0f}% | Citation count normalized by age |")
    parts.append(f"| Influential Citations | {WEIGHTS['influential']*100:.0f}% | High-impact citation count |")
    parts.append(f"| Venue Quality | {WEIGHTS['venue']*100:.0f}% | Top venue=10, regular=5, preprint=2 |")
    parts.append(f"| Author Quality | {WEIGHTS['author']*100:.0f}% | Highest author h-index |")
    parts.append(f"| Recency | {WEIGHTS['recency']*100:.0f}% | ≤3mo=10, ≤6mo=9, ≤12mo=7, >12mo=5 |")
    parts.append("")

    # Top 100 — grouped by category
    # Compute date range for top 100
    top100_dates = [p.get("published", "")[:10] for p in top100 if p.get("published")]
    top100_date_range = ""
    if top100_dates:
        top100_date_range = f" ({min(top100_dates)} ~ {max(top100_dates)})"

    parts.append("## Top 100 Papers\n")
    parts.append(
        f"The top {len(top100)} papers out of {total}{top100_date_range}, "
        "organized by category and ranked by quality score.\n"
    )

    global_rank = 0
    top100_with_rank = []
    for p in top100:
        global_rank += 1
        top100_with_rank.append((global_rank, p))

    first_dim = True
    for dim in DIMENSION_ORDER:
        dim_papers = [(r, p) for r, p in top100_with_rank if p.get("dimension") == dim]
        if not dim_papers:
            continue
        if not first_dim:
            parts.append("---\n")
        first_dim = False
        cfg = DIMENSION_CONFIG[dim]
        parts.append(f"### {cfg['heading']}\n")
        for rank, p in dim_papers:
            parts.append(_top100_paper_entry_en(p, rank, translations))
            parts.append("")

    parts.append("---\n")
    parts.append("*Data sourced from [arXiv](https://arxiv.org/) and [Semantic Scholar](https://www.semanticscholar.org/).*\n")

    return "\n".join(parts)


def _readme_cn(total, scores, tier_counts, date_start, date_end, by_dim, top100, top100_by_dim):
    parts = []
    parts.append("# Agent 安全论文精选\n")
    parts.append(
        f"> AI Agent 安全研究论文精选集——涵盖攻击对抗、防御对齐、安全测评与 Agent 安全架构。"
        f"共 **{total} 篇** arXiv 论文（{date_start} ~ {date_end}），按质量评分排序。\n"
    )
    parts.append("[English](README.md) · [**中文**](README_CN.md)\n")

    # TOC
    parts.append("## 目录\n")
    parts.append("- [统计](#统计)")
    parts.append("- [分类](#分类)")
    parts.append("- [评分方法](#评分方法)")
    parts.append("- [Top 100 论文](#top-100-论文)")
    for dim in DIMENSION_ORDER:
        cfg = DIMENSION_CONFIG[dim]
        dim_in_top100 = any(p.get("dimension") == dim for p in top100)
        if dim_in_top100:
            # Use the English part of the heading for anchor (Chinese headings use bilingual format)
            parts.append(f"  - [{cfg['emoji']} {dim}](#{github_anchor(cfg['heading'])})")
    parts.append("")

    # Stats
    parts.append("## 统计\n")
    parts.append("| 指标 | 值 |")
    parts.append("|------|-----|")
    parts.append(f"| 论文总数 | {total} |")
    parts.append(f"| 日期范围 | {date_start} ~ {date_end} |")
    parts.append(f"| 评分范围 | {min(scores):.2f} ~ {max(scores):.2f}（均值 {sum(scores)/len(scores):.2f}） |")
    parts.append("")

    # Categories
    parts.append("## 分类\n")
    parts.append("| # | 分类 | 篇数 | 完整列表 |")
    parts.append("|---|------|------|----------|")
    for i, dim in enumerate(DIMENSION_ORDER, 1):
        cfg = DIMENSION_CONFIG[dim]
        count = by_dim.get(dim, 0)
        parts.append(f"| {i} | {cfg['emoji']} {cfg['en']}（{dim}） | {count} | [查看全部](docs/{cfg['file']}) |")
    parts.append("")

    # Scoring
    parts.append("## 评分方法\n")
    parts.append(
        "每篇论文基于 [Semantic Scholar](https://www.semanticscholar.org/) 数据，"
        "使用加权公式计算综合评分：\n"
    )
    parts.append("| 维度 | 权重 | 说明 |")
    parts.append("|------|------|------|")
    parts.append(f"| 月均引用 | {WEIGHTS['citation']*100:.0f}% | 引用数按发表时间归一化 |")
    parts.append(f"| 高影响力引用 | {WEIGHTS['influential']*100:.0f}% | 高影响力引用数 |")
    parts.append(f"| 发表会议质量 | {WEIGHTS['venue']*100:.0f}% | 顶会=10，普通会议=5，预印本=2 |")
    parts.append(f"| 作者质量 | {WEIGHTS['author']*100:.0f}% | 最高作者 h-index |")
    parts.append(f"| 时效性 | {WEIGHTS['recency']*100:.0f}% | ≤3月=10，≤6月=9，≤12月=7，>12月=5 |")
    parts.append("")

    # Top 100 — grouped by category
    top100_dates = [p.get("published", "")[:10] for p in top100 if p.get("published")]
    top100_date_range = ""
    if top100_dates:
        top100_date_range = f"（{min(top100_dates)} ~ {max(top100_dates)}）"

    parts.append("## Top 100 论文\n")
    parts.append(
        f"从 {total} 篇论文中选出评分最高的 {len(top100)} 篇{top100_date_range}，"
        "按类别分组展示。\n"
    )

    global_rank = 0
    top100_with_rank = []
    for p in top100:
        global_rank += 1
        top100_with_rank.append((global_rank, p))

    first_dim = True
    for dim in DIMENSION_ORDER:
        dim_papers = [(r, p) for r, p in top100_with_rank if p.get("dimension") == dim]
        if not dim_papers:
            continue
        if not first_dim:
            parts.append("---\n")
        first_dim = False
        cfg = DIMENSION_CONFIG[dim]
        parts.append(f"### {cfg['heading']}（{dim}）\n")
        for rank, p in dim_papers:
            parts.append(_top100_paper_entry_cn(p, rank))
            parts.append("")

    parts.append("---\n")
    parts.append("*数据来源：[arXiv](https://arxiv.org/)、[Semantic Scholar](https://www.semanticscholar.org/)*\n")

    return "\n".join(parts)


# ── Category MD Generation ─────────────────────────────

def generate_category_file(dim: str, papers: List[Dict]) -> str:
    """Generate a category markdown file with all papers sorted by score."""
    cfg = DIMENSION_CONFIG[dim]
    parts = []

    parts.append(f"# {cfg['emoji']} {cfg['en']}（{dim}）\n")
    parts.append(f"> {len(papers)} 篇论文 | 按质量评分排序\n")
    parts.append("---\n")

    for rank, p in enumerate(papers, 1):
        title = p.get("title", "Unknown")
        url = clean_arxiv_url(p.get("entry_url", ""))
        pdf_url = clean_pdf_url(p.get("pdf_url", ""))
        authors = p.get("authors", [])
        author_str = ", ".join(authors[:6])
        if len(authors) > 6:
            author_str += f" et al. ({len(authors)} total)"

        categories = ", ".join(p.get("categories", [])[:3])
        published = p.get("published", "")[:10]
        tier = p.get("quality_tier", "C")
        score = p.get("quality_score", 0)
        qs = p.get("quality_scores", {})
        summary = p.get("summary", "暂无总结").strip()

        parts.append(f"## #{rank} — {title}\n")
        parts.append(f"`{tier}` Score: {score:.2f} | {published}\n")
        parts.append(f"**Authors:** {author_str}\n")
        parts.append(f"**Categories:** {categories}\n")
        parts.append(
            f"**Scores:** Citation: {qs.get('citation', 0):.2f} | "
            f"Influential: {qs.get('influential', 0):.2f} | "
            f"Venue: {qs.get('venue', 0):.2f} | "
            f"Author: {qs.get('author', 0):.2f} | "
            f"Recency: {qs.get('recency', 0):.2f}\n"
        )
        parts.append(f"**Links:** [arXiv]({url}) | [PDF]({pdf_url})\n")
        parts.append(f"> {summary}\n")
        parts.append("---\n")

    return "\n".join(parts)


# ── Main ───────────────────────────────────────────────

def main():
    library_path = Path(LIBRARY_PATH)
    if not library_path.exists():
        print(f"Error: {LIBRARY_PATH} not found")
        return

    with open(library_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    papers = data["papers"]
    print(f"Loaded {len(papers)} papers from {LIBRARY_PATH}")

    # Load translations
    translations = load_translations()
    if translations:
        print(f"Loaded {len(translations)} translations from {TRANSLATIONS_PATH}")
    else:
        print(f"Warning: No translations found at {TRANSLATIONS_PATH}")

    # Ensure docs directory exists
    DOCS_DIR.mkdir(exist_ok=True)

    # Generate READMEs
    readme_en = generate_readme(data, translations, lang="en")
    (OUTPUT_DIR / "README.md").write_text(readme_en, encoding="utf-8")
    print("Generated README.md")

    readme_cn = generate_readme(data, translations, lang="cn")
    (OUTPUT_DIR / "README_CN.md").write_text(readme_cn, encoding="utf-8")
    print("Generated README_CN.md")

    # Generate category files
    for dim in DIMENSION_ORDER:
        cfg = DIMENSION_CONFIG[dim]
        dim_papers = [p for p in papers if p.get("dimension") == dim]
        dim_papers.sort(key=lambda x: x.get("quality_score", 0), reverse=True)
        content = generate_category_file(dim, dim_papers)
        (DOCS_DIR / cfg["file"]).write_text(content, encoding="utf-8")
        print(f"Generated docs/{cfg['file']} ({len(dim_papers)} papers)")

    print(f"\nDone! Generated 7 files total.")


if __name__ == "__main__":
    main()
