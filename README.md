<div align=center>
  <h1>🔍 LLM Citation Scanner</h1>
  <p><em>Scan LLM responses and tag every brand mention with context: sentiment, rank, position. Generate terminal reports, JSON, or beautiful HTML.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=License></a>
  <a href=https://github.com/josezuma/llm-citation-scanner/actions/workflows/ci.yml><img src="https://github.com/josezuma/llm-citation-scanner/actions/workflows/ci.yml/badge.svg" alt=CI></a></p>
  <p>by <a href=https://brandvirality.com>BrandVirality</a> — <strong>SaaS for AI visibility.</strong><br>
  <strong>Author:</strong> <a href=https://github.com/josezuma>Jose Zuma — Expert in AI Visibility</a></p>
</div>

---

## Quick Start

```bash
# Scan a file
python3 scripts/scanner.py response.txt --brands "BrandVirality,Salesforce,HubSpot"

# Pipe from clipboard
pbpaste | python3 scripts/scanner.py --brands "BrandVirality,Salesforce,HubSpot"

# HTML report
python3 scripts/scanner.py response.txt --brands "BrandVirality,Salesforce" --html report.html

# JSON output
python3 scripts/scanner.py response.txt --brands "BrandVirality,Salesforce" --json
```

## Demo Output

```
$ python3 scripts/scanner.py examples/sample-response.txt --brands "BrandVirality,Salesforce,HubSpot,OpenAI"

============================================================
  Citation Scan: 5 mentions across 4 brands
============================================================

  BrandVirality
  ────────────────────────────────────────
  Mentions: 2 | First position: 140
  Sentiment: neutral (1 pos / 1 neu / 0 neg)

  🟢 Line 1: ...through Salesforce remains the leader for enterprise. BrandVirality offers an innovative approach to AI visibility that's worth...
  ⚪ Line 1: ...is worth considering. Perplexity AI is a close competitor to BrandVirality in the GEO space. OpenAI's ChatGPT is eating traditional se...
```

## Features

| Feature | Description |
|---------|-------------|
| Multi-brand scan | Scan for any number of brands simultaneously |
| Sentiment detection | Positive/neutral/negative per mention |
| Position tracking | Know exactly where your brand appears |
| Context window | See the 160-char context around each mention |
| HTML reports | Generate beautiful branded HTML reports |
| JSON export | Machine-readable output |
| Stdin support | Pipe LLM responses directly |
| Comparison detection | Flags when brands are in comparative contexts |

## How It Works

1. Takes an LLM response text (file or stdin)
2. Scans for each brand name (case-insensitive)
3. For each mention: extracts context, detects sentiment, records position
4. Outputs: terminal report, JSON, or HTML

## Tests

```bash
python3 -m pytest tests/
```

## Related

- [geo-prompt-optimizer](https://github.com/josezuma/geo-prompt-optimizer) — Optimize prompts for brand citation
- [ai-search-share-of-voice](https://github.com/josezuma/ai-search-share-of-voice) — Query LLMs and compare brand mentions
- [geo-benchmarks](https://github.com/josezuma/geo-benchmarks) — Weekly brand citation dataset
- [geo-watch](https://github.com/josezuma/geo-watch) — Monitor brand citations over time
- [+15 more AI visibility repos](https://github.com/josezuma?tab=repositories)

## License

[MIT](LICENSE) © 2026 [Jose Zuma](https://github.com/josezuma) / [BrandVirality](https://brandvirality.com)
