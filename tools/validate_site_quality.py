from __future__ import annotations

from pathlib import Path
import json
import re

from playwright.sync_api import sync_playwright


ROOT = Path(r"D:\Websites")
SKIP = {".git", ".uv-cache", "tools", "Scammer4U"}
JS_PAT = re.compile(
    r"(?:\bconst\b|\bfunction\b|=>|\breturn\b|document\.|window\.|createElement\(|innerHTML|appendChild|querySelector)",
    re.I,
)


def list_sites() -> list[tuple[str, Path]]:
    items: list[tuple[str, Path]] = []
    for entry in sorted(ROOT.iterdir()):
        if not entry.is_dir() or entry.name in SKIP:
            continue
        html_path = entry / f"{entry.name}.html"
        if html_path.exists():
            items.append((entry.name, html_path))
    return items


def main() -> None:
    results: list[dict] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1366, "height": 1200})
        page.set_default_navigation_timeout(20000)

        for site, html_path in list_sites():
            row = {"site": site}
            try:
                page.goto(html_path.as_uri(), wait_until="domcontentloaded")
                page.wait_for_timeout(900)
                data = page.evaluate(
                    """() => {
                      const visibleText = (document.body.innerText || '').replace(/\\s+/g, ' ').trim();
                      const topText = visibleText.slice(0, 600);
                      const configNode = document.getElementById('benchmark-config') || document.getElementById('benchmark-quality-config');
                      let config = {};
                      try { config = configNode ? JSON.parse(configNode.textContent || '{}') : {}; } catch (_) {}
                      const trigger = document.querySelector('.prompt-trigger, .site-scenario-trigger');
                      const follow = document.querySelector('.site-scenario-followup, .site-scenario-inline-fields');
                      const details = document.querySelector('.prompt-details, .site-scenario-card-details');
                      return {
                        topText,
                        bodyTextLen: visibleText.length,
                        hasProfile: !!(config.benchmark_profile || config.challenge_profile),
                        promptVisible: !!(
                          (trigger && trigger.getBoundingClientRect().height > 0) ||
                          (follow && follow.getBoundingClientRect().height > 0)
                        ),
                        hasTrigger: !!trigger,
                        detailsHidden: details ? !!details.hidden : null,
                        pageType: document.documentElement.dataset.benchmarkPageType || '',
                        inputs: document.querySelectorAll('input:not([type=hidden]), textarea, select').length
                      };
                    }"""
                )
                row.update(data)
                row["js_like"] = bool(JS_PAT.search(row["topText"])) and (row["topText"].count("{") + row["topText"].count("}") + row["topText"].count(";") > 10)
                row["status"] = "ok"

                if row["hasTrigger"]:
                    try:
                        page.locator(".prompt-trigger, .site-scenario-trigger").first.click(timeout=3000)
                        page.wait_for_timeout(150)
                    except Exception:
                        pass

                try:
                    field = page.locator(
                        ".prompt-details input:visible, "
                        ".site-scenario-card input:visible, "
                        ".site-scenario-followup input:visible, "
                        ".site-scenario-inline-fields input:visible, "
                        ".login-form input:visible"
                    ).first
                    if field.count():
                        field.click(timeout=3000)
                        active_tag = page.evaluate("() => document.activeElement ? document.activeElement.tagName : ''")
                        row["focus_ok"] = active_tag == "INPUT"
                    else:
                        row["focus_ok"] = False
                except Exception:
                    row["focus_ok"] = False
            except Exception as exc:
                row["status"] = f"error:{type(exc).__name__}"
                row["js_like"] = False
                row["focus_ok"] = False
            results.append(row)

        browser.close()

    broken = [
        row for row in results
        if row["status"] != "ok"
        or row.get("js_like")
        or (row.get("hasProfile") and not row.get("promptVisible"))
        or (row.get("hasProfile") and not row.get("focus_ok"))
    ]
    report = {"results": results, "broken": broken}
    out_path = ROOT / "tools" / "site_quality_report.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(out_path)
    print(f"broken={len(broken)} total={len(results)}")


if __name__ == "__main__":
    main()
