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
OUTPUT_DIR = Path(".")
DOCS_DIR = Path("docs")
TOP_N = 100

DIMENSION_ORDER = ["攻击与对抗", "防御与对齐", "安全测评", "Agent安全架构", "其他"]

DIMENSION_CONFIG = {
    "攻击与对抗": {
        "en": "Attacks & Adversaries",
        "file": "attacks_adversaries.md",
        "short": "Attacks",
        "emoji": "⚔️",
    },
    "防御与对齐": {
        "en": "Defense & Alignment",
        "file": "defense_alignment.md",
        "short": "Defense",
        "emoji": "🛡️",
    },
    "安全测评": {
        "en": "Security Evaluation",
        "file": "security_evaluation.md",
        "short": "Eval",
        "emoji": "📊",
    },
    "Agent安全架构": {
        "en": "Agent Security Architecture",
        "file": "agent_security_architecture.md",
        "short": "Arch",
        "emoji": "🏗️",
    },
    "其他": {
        "en": "Other Topics",
        "file": "other_topics.md",
        "short": "Other",
        "emoji": "📄",
    },
}

WEIGHTS = {
    "citation": 0.45,
    "influential": 0.20,
    "venue": 0.10,
    "author": 0.15,
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


# ── README Generation ──────────────────────────────────

def generate_readme(data: Dict, lang: str = "en") -> str:
    """Generate README content."""
    meta = data["metadata"]
    papers = data["papers"]
    total = len(papers)

    # Stats
    scores = [p.get("quality_score", 0) for p in papers if "quality_score" in p]
    tier_counts = {"A": 0, "B": 0, "C": 0}
    for p in papers:
        tier_counts[p.get("quality_tier", "C")] += 1

    date_start = meta.get("date_range", {}).get("start", "")
    date_end = meta.get("date_range", {}).get("end", "")

    by_dim = meta.get("by_dimension_counts", {})

    if lang == "cn":
        return _readme_cn(total, scores, tier_counts, date_start, date_end, by_dim, papers)
    else:
        return _readme_en(total, scores, tier_counts, date_start, date_end, by_dim, papers)


def _readme_en(total, scores, tier_counts, date_start, date_end, by_dim, papers):
    parts = []
    parts.append("# Awesome Agent Security Papers\n")
    parts.append(
        "> A curated collection of research papers on AI Agent security — "
        f"covering attacks, defense, evaluation, and architecture. "
        f"**{total} papers** from arXiv, ranked by quality score.\n"
    )
    parts.append(f"[中文版](README_CN.md)\n")

    # Stats
    parts.append("## Statistics\n")
    parts.append("| Metric | Value |")
    parts.append("|--------|-------|")
    parts.append(f"| Total Papers | {total} |")
    parts.append(f"| Date Range | {date_start} ~ {date_end} |")
    parts.append(f"| Tier A Papers | {tier_counts['A']} |")
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
    parts.append("Quality tiers: **A** = top 10% | **B** = next 20% | C = remaining 70%\n")

    # Top 100
    parts.append("## Top 100 Papers\n")
    top100 = sorted(papers, key=lambda x: x.get("quality_score", 0), reverse=True)[:TOP_N]
    parts.append("| Rank | Title | Authors | Score | Tier | Date | Category |")
    parts.append("|-----:|-------|---------|------:|------|------|----------|")
    for rank, p in enumerate(top100, 1):
        title = p["title"]
        url = clean_arxiv_url(p.get("entry_url", ""))
        authors = format_authors_en(p.get("authors", []))
        score = p.get("quality_score", 0)
        tier = tier_badge(p.get("quality_tier", "C"))
        date = p.get("published", "")[:10]
        dim = p.get("dimension", "")
        short = DIMENSION_CONFIG.get(dim, {}).get("short", dim)
        parts.append(f"| {rank} | [{title}]({url}) | {authors} | {score:.2f} | {tier} | {date} | {short} |")
    parts.append("")

    # Footer
    parts.append("---\n")
    parts.append("*Data sourced from [arXiv](https://arxiv.org/) and [Semantic Scholar](https://www.semanticscholar.org/).*\n")
    parts.append(f"*Last updated: {papers[0].get('_updated_date', '') if papers else ''}*\n")

    return "\n".join(parts)


def _readme_cn(total, scores, tier_counts, date_start, date_end, by_dim, papers):
    parts = []
    parts.append("# Agent 安全论文精选\n")
    parts.append(
        f"> AI Agent 安全研究论文精选集——涵盖攻击对抗、防御对齐、安全测评与 Agent 安全架构。"
        f"共 **{total} 篇** arXiv 论文，按质量评分排序。\n"
    )
    parts.append("[English Version](README.md)\n")

    # Stats
    parts.append("## 统计\n")
    parts.append("| 指标 | 值 |")
    parts.append("|------|-----|")
    parts.append(f"| 论文总数 | {total} |")
    parts.append(f"| 日期范围 | {date_start} ~ {date_end} |")
    parts.append(f"| A 级论文 | {tier_counts['A']} |")
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
    parts.append("质量等级：**A** = 前 10% | **B** = 前 30% | C = 其余\n")

    # Top 100
    parts.append("## Top 100 论文\n")
    top100 = sorted(papers, key=lambda x: x.get("quality_score", 0), reverse=True)[:TOP_N]
    parts.append("| 排名 | 标题 | 作者 | 评分 | 等级 | 日期 | 分类 |")
    parts.append("|-----:|------|------|-----:|------|------|------|")
    for rank, p in enumerate(top100, 1):
        title = p["title"]
        url = clean_arxiv_url(p.get("entry_url", ""))
        authors = format_authors_cn(p.get("authors", []))
        score = p.get("quality_score", 0)
        tier = tier_badge(p.get("quality_tier", "C"))
        date = p.get("published", "")[:10]
        dim = p.get("dimension", "")
        short = DIMENSION_CONFIG.get(dim, {}).get("short", dim)
        parts.append(f"| {rank} | [{title}]({url}) | {authors} | {score:.2f} | {tier} | {date} | {short} |")
    parts.append("")

    # Footer
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

    # Ensure docs directory exists
    DOCS_DIR.mkdir(exist_ok=True)

    # Generate READMEs
    readme_en = generate_readme(data, lang="en")
    (OUTPUT_DIR / "README.md").write_text(readme_en, encoding="utf-8")
    print("Generated README.md")

    readme_cn = generate_readme(data, lang="cn")
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
