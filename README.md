<div align=center>
  <h1>🔍 LLM Citation Scanner</h1>
  <p><em>Scan LLM responses and tag every brand mention with context: position, sentiment, source URL, confidence. Know exactly where your brand appears in AI answers.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=MIT></a></p>
  <p>by BrandVirality — <strong>SaaS for AI visibility.</strong><br>Author: Jose Zuma</p>
</div>

---

## Quick Start

```bash
pip install requests
python scripts/scanner.py response.txt --brands "BrandVirality,OpenAI,Anthropic"
```

## Features

- Scans any text for brand mentions
- Ranks by position (first mention = highest value)
- Tags sentiment: positive, neutral, negative
- Extracts context window around each mention
- Outputs JSON + terminal report

## Related

- geo-prompts, geo-watch, geo-audit-skill, mcp-geo, geo-prompt-optimizer, awesome-ai-visibility
