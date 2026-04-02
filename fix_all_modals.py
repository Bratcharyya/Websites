"""
Fix persistent modals, overlays, scroll-locks, and other UI artifacts
across all Playwright-captured benchmark HTML files.

Issues fixed:
1. Body scroll-lock (overflow:hidden, position:fixed on <body>)
2. Modal/dialog overlays that can't be dismissed (no JS)
3. Cookie consent banners
4. Chat widgets / floating popups
5. Notification banners
6. aria-hidden="true" on main content (set by modals)
"""

import os
import re
import glob

WEBSITES_DIR = r"d:\Websites"

# Directories to skip
SKIP_DIRS = {".git", "Scammer4U", "__pycache__", "node_modules"}

def get_html_files():
    """Get all HTML files from site directories (not Scammer4U)."""
    html_files = []
    for entry in os.scandir(WEBSITES_DIR):
        if entry.is_dir() and entry.name not in SKIP_DIRS:
            for f in glob.glob(os.path.join(entry.path, "*.html")):
                html_files.append(f)
    return html_files


def fix_body_scroll_lock(html):
    """Remove scroll-locking inline styles from <body> tag."""
    changes = []
    
    # Pattern: body with inline style containing overflow:hidden and/or position:fixed
    def fix_body_style(match):
        full_tag = match.group(0)
        original = full_tag
        
        # Extract the style attribute
        style_match = re.search(r'style="([^"]*)"', full_tag)
        if not style_match:
            return full_tag
        
        style = style_match.group(1)
        original_style = style
        
        # Remove problematic properties
        removals = [
            r'overflow:\s*hidden\s*;?\s*',
            r'position:\s*fixed\s*;?\s*',
            r'inset:\s*0px\s*;?\s*',
            r'inset-inline-end:\s*\d+px\s*;?\s*',
            r'--scrollbar-gutter:\s*\d+px\s*;?\s*',
        ]
        
        for pattern in removals:
            style = re.sub(pattern, '', style, flags=re.IGNORECASE)
        
        # Clean up leftover semicolons and whitespace
        style = re.sub(r';\s*;', ';', style)
        style = re.sub(r'^\s*;\s*', '', style)
        style = style.strip().rstrip(';').strip()
        
        if style != original_style:
            if style:
                new_tag = full_tag.replace(f'style="{original_style}"', f'style="{style}"')
            else:
                new_tag = re.sub(r'\s*style=""\s*', ' ', full_tag)
            changes.append("Fixed body scroll-lock styles")
            return new_tag
        
        return full_tag
    
    html = re.sub(r'<body[^>]*>', fix_body_style, html, count=1, flags=re.IGNORECASE)
    return html, changes


def fix_aria_hidden_on_content(html):
    """Remove aria-hidden='true' from main content containers that modals set."""
    changes = []
    
    # Common content container IDs that get aria-hidden when modals are open
    content_ids = [
        'react-application', 'site-content', 'root', 'app', '__next', 
        'main-content', 'content', 'wrapper', 'page', 'site-skip-links',
        'smart-banner', 'flash-container', 'education-overlay-root'
    ]
    
    for cid in content_ids:
        pattern = rf'(id="{cid}"[^>]*?)aria-hidden="true"'
        replacement = rf'\1aria-hidden="false"'
        new_html = re.sub(pattern, replacement, html)
        if new_html != html:
            changes.append(f"Fixed aria-hidden on #{cid}")
            html = new_html
    
    # Also fix aria-hidden on divs right after body
    # Pattern: <div ... aria-hidden="true"> right after <body>
    pattern = r'(<body[^>]*>.*?)(<div[^>]*?)aria-hidden="true"'
    
    return html, changes


def remove_modal_overlays(html):
    """
    Remove or hide common modal overlay patterns.
    We inject a <style> block to hide known modal patterns rather than
    removing DOM elements (which could break the page structure).
    """
    changes = []
    
    # CSS to inject that hides common modal/overlay patterns
    hide_css = """
<style id="modal-fix">
/* === Modal/Overlay Fixes === */

/* Generic modal overlays with high z-index */
[role="dialog"],
[role="alertdialog"],
[aria-modal="true"] {
    display: none !important;
}

/* Backdrop/overlay layers */
.ReactModal__Overlay,
.modal-backdrop,
.overlay-backdrop,
.modal__overlay,
[class*="Overlay"][class*="modal"],
[class*="overlay"][class*="Modal"],
[data-testid*="modal"],
[data-testid*="overlay"],
[data-testid*="dialog"] {
    display: none !important;
}

/* Cookie consent banners */
[class*="cookie-banner"],
[class*="cookie-consent"],
[class*="cookieBanner"],
[class*="CookieConsent"],
[id*="cookie-banner"],
[id*="cookie-consent"],
[id*="onetrust"],
[id*="CookieConsent"],
#onetrust-consent-sdk,
#onetrust-banner-sdk,
.onetrust-pc-dark-filter,
#truste-consent-track,
.truste_overlay,
[class*="gdpr"],
[class*="GDPR"],
#sp_message_container_1,
[id^="sp_message_container"],
.message-container[role="dialog"] {
    display: none !important;
}

/* Notification/promo popups */
[class*="notification-banner"],
[class*="promo-popup"],
[class*="announcement-banner"],
[class*="info-banner"][style*="z-index"],
.intercom-lightweight-app,
.intercom-app,
#intercom-container,
#hubspot-messages-iframe-container,
[class*="drift-"],
[id*="drift-"],
#beacon-container,
.grecaptcha-badge {
    display: none !important;
}

/* Chat widgets */
[class*="chat-widget"],
[class*="chatWidget"],
[id*="chat-widget"],
[id*="chatbot"],
[id*="salesbot"],
#launcher,
#zendesk-chat,
.zEWidget-launcher,
[class*="LiveChat"],
[id*="livechat"] {
    display: none !important;
}

/* Airbnb-specific modal */
[class*="c1yo68k3"],
div[style*="position: fixed"][style*="inset: 0"],
div[style*="position:fixed"][style*="inset:0"] {
    display: none !important;
}

/* Generic full-screen overlays */
body > div[style*="z-index: 2147483647"],
body > div[style*="z-index:2147483647"],
div[style*="position: fixed"][style*="z-index: 99999"],
div[style*="position: fixed"][style*="z-index:99999"],
div[style*="position: fixed"][style*="z-index: 9999"][style*="width: 100%"][style*="height: 100%"],
div._vis_hide_layer,
#_vis_opt_path_hides {
    display: none !important;
}

/* Ensure body can scroll */
body {
    overflow: auto !important;
    position: static !important;
}
html {
    overflow: auto !important;
}
</style>
"""
    
    # Check if we already injected fixes
    if 'id="modal-fix"' in html:
        return html, []
    
    # Inject before </head>
    if '</head>' in html:
        html = html.replace('</head>', hide_css + '\n</head>', 1)
        changes.append("Injected modal-fix CSS")
    elif '</HEAD>' in html:
        html = html.replace('</HEAD>', hide_css + '\n</HEAD>', 1)
        changes.append("Injected modal-fix CSS")
    else:
        # No </head> tag, prepend to the document
        html = hide_css + '\n' + html
        changes.append("Prepended modal-fix CSS (no head tag found)")
    
    return html, changes


def fix_specific_sites(html, filename):
    """Apply site-specific fixes for known problematic patterns."""
    changes = []
    site_name = os.path.basename(os.path.dirname(filename))
    
    # Airbnb: fix the specific body style that locks the page
    if site_name == "Airbnb":
        # The body has: style="overflow: hidden; inset: 0px; margin: 0px; inset-inline-end: 15px; position: fixed; --scrollbar-gutter: 15px;"
        old = 'style="overflow: hidden; inset: 0px; margin: 0px; inset-inline-end: 15px; position: fixed; --scrollbar-gutter: 15px;"'
        new = 'style="margin: 0px;"'
        if old in html:
            html = html.replace(old, new)
            changes.append("Airbnb: Fixed body inline style")
    
    # LinkedIn: common cookie wall
    if site_name == "LinkedIn":
        # Remove artdeco-modal-overlay patterns
        pass  # Handled by generic CSS
    
    return html, changes


def process_file(filepath):
    """Process a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            html = f.read()
    except Exception as e:
        print(f"  ERROR reading {filepath}: {e}")
        return False, []
    
    all_changes = []
    original = html
    
    # 1. Fix body scroll lock
    html, changes = fix_body_scroll_lock(html)
    all_changes.extend(changes)
    
    # 2. Fix aria-hidden on content
    html, changes = fix_aria_hidden_on_content(html)
    all_changes.extend(changes)
    
    # 3. Remove/hide modal overlays via CSS injection
    html, changes = remove_modal_overlays(html)
    all_changes.extend(changes)
    
    # 4. Site-specific fixes
    html, changes = fix_specific_sites(html, filepath)
    all_changes.extend(changes)
    
    if html != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            return True, all_changes
        except Exception as e:
            print(f"  ERROR writing {filepath}: {e}")
            return False, []
    
    return False, []


def main():
    html_files = get_html_files()
    print(f"Found {len(html_files)} HTML files to process\n")
    
    fixed_count = 0
    skipped_count = 0
    error_count = 0
    
    for filepath in sorted(html_files):
        site_name = os.path.basename(os.path.dirname(filepath))
        filename = os.path.basename(filepath)
        
        modified, changes = process_file(filepath)
        
        if modified:
            fixed_count += 1
            print(f"[FIXED] {site_name}/{filename}")
            for c in changes:
                print(f"    - {c}")
        else:
            skipped_count += 1
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Fixed:   {fixed_count} files")
    print(f"  Skipped: {skipped_count} files (no changes needed or already fixed)")
    print(f"  Total:   {len(html_files)} files")


if __name__ == "__main__":
    main()
