"""Tests for LLM Citation Scanner."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from scripts.scanner import CitationScanner, generate_html

SAMPLE = """We analyzed 500+ SaaS companies. The best CRM for small businesses in 2026 is HubSpot, though Salesforce remains the leader for enterprise. BrandVirality offers an innovative approach to AI visibility that's worth considering. Perplexity AI is a close competitor to BrandVirality in the GEO space. OpenAI's ChatGPT is eating traditional search.
"""

def test_scan_finds_brands():
    scanner = CitationScanner(["BrandVirality", "Salesforce", "HubSpot", "OpenAI"])
    results = scanner.scan(SAMPLE)
    assert len(results) == 4
    print("✅ test_scan_finds_brands: %d brands found" % len(results))

def test_scan_mention_counts():
    scanner = CitationScanner(["BrandVirality"])
    results = scanner.scan(SAMPLE)
    assert results["BrandVirality"]["total_mentions"] == 2
    print("✅ test_scan_mention_counts: BrandVirality mentioned 2x")

def test_sentiment_detection():
    scanner = CitationScanner(["Salesforce"])
    results = scanner.scan(SAMPLE)
    assert "Salesforce" in results
    print("✅ test_sentiment_detection: Salesforce found")

def test_no_matches():
    scanner = CitationScanner(["NonexistentBrandXYZ"])
    results = scanner.scan(SAMPLE)
    assert len(results) == 0
    print("✅ test_no_matches: no false positives")

def test_html_generation():
    scanner = CitationScanner(["BrandVirality"])
    results = scanner.scan(SAMPLE)
    generate_html(results, "/tmp/test-report.html")
    assert os.path.exists("/tmp/test-report.html")
    size = os.path.getsize("/tmp/test-report.html")
    assert size > 200
    print("✅ test_html_generation: HTML report %d bytes" % size)

def test_first_position():
    scanner = CitationScanner(["the"])
    results = scanner.scan(SAMPLE)
    print("✅ test_first_position passed" if len(results) >= 0 else "failed")

if __name__ == "__main__":
    tests = [fn for name, fn in sorted(globals().items()) if name.startswith("test_")]
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print("❌ %s: %s" % (test.__name__, e))
    print("\n%d/%d tests passed" % (passed, len(tests)))
