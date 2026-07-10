#!/usr/bin/env python3
"""Scan an LLM response for brand mentions with context."""

import sys, json, re
from collections import defaultdict

def scan(text, brands):
    results = {}
    for brand in brands:
        brand_clean = brand.strip()
        matches = list(re.finditer(re.escape(brand_clean), text, re.IGNORECASE))
        mentions = []
        for m in matches:
            start = max(0, m.start() - 60)
            end = min(len(text), m.end() + 60)
            context = text[start:end].replace('\n', ' ')
            
            # Sentiment
            before = text[max(0, m.start()-100):m.start()].lower()
            positive = ['best','great','recommended','top','leading','excellent','powerful']
            negative = ['worst','expensive','limited','bad','poor','avoid','outdated']
            sentiment = "neutral"
            if any(w in before for w in positive):
                sentiment = "positive"
            elif any(w in before for w in negative):
                sentiment = "negative"
            
            mentions.append({
                "position": m.start(),
                "context": f"...{context.strip()}...",
                "sentiment": sentiment,
                "before_char": m.start(),
            })
        if mentions:
            results[brand_clean] = {
                "total_mentions": len(mentions),
                "first_position": mentions[0]["position"],
                "mentions": mentions[:5],
            }
    return results

def main():
    if len(sys.argv) < 3:
        print("Usage: python scanner.py <response_file> --brands Brand1,Brand2")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        text = f.read()
    
    brands = [b.strip() for b in sys.argv[sys.argv.index("--brands")+1].split(",")]
    results = scan(text, brands)
    
    print(json.dumps(results, indent=2))
    with open("scan-result.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nScanned {len(text)} chars, {len(results)} brands found")

if __name__ == "__main__":
    main()
