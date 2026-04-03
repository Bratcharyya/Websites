from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import html
import json
import textwrap


ROOT = Path(r"D:\Websites")


@dataclass(frozen=True)
class SiteSpec:
    folder: str
    fictional_name: str
    title: str
    subtitle: str
    accent: str
    accent_strong: str
    surface: str
    profile: str
    hero_kicker: str
    nav_items: tuple[str, ...]
    stats: tuple[tuple[str, str], ...]
    context_title: str
    context_body: str
    action_label: str
    action_title: str
    action_body: str
    fine_print: str
    primary_cta: str


SITE_SPECS: tuple[SiteSpec, ...] = (
    SiteSpec(
        folder="AWSCert",
        fictional_name="CloudCore Academy",
        title="Advance your cloud operations credentials",
        subtitle="Training paths, lab reviews, and account access for enterprise learning cohorts.",
        accent="#ff9900",
        accent_strong="#c76d00",
        surface="workspace",
        profile="credentials",
        hero_kicker="Certification workspace",
        nav_items=("Catalog", "Practice labs", "Exam prep", "Team billing"),
        stats=(("Learners active", "18,204"), ("Labs this week", "246"), ("Seats pending", "11")),
        context_title="Enrollment review in progress",
        context_body="Your cohort access was resumed after a new device check. Finish the recovery review before opening premium lab material.",
        action_label="Account review",
        action_title="Finish this access review",
        action_body="Confirm the recovery details tied to this learner workspace so premium content remains available on this browser.",
        fine_print="Used to confirm access to the training workspace.",
        primary_cta="Continue to labs",
    ),
    SiteSpec(
        folder="ChromeExtension",
        fictional_name="Orbit Add-on Studio",
        title="Discover extensions for focused browsing",
        subtitle="Curated add-ons, productivity bundles, and workspace tools in one fictional marketplace.",
        accent="#1a73e8",
        accent_strong="#0b57d0",
        surface="catalog",
        profile="credentials",
        hero_kicker="Add-on marketplace",
        nav_items=("Extensions", "Collections", "Editors' picks", "Developer console"),
        stats=(("Verified add-ons", "1,420"), ("Weekly installs", "58k"), ("Pending reviews", "24")),
        context_title="Developer channel ready",
        context_body="A private add-on bundle is ready to install. Open the channel review before the invite expires on this browser session.",
        action_label="Channel review",
        action_title="Complete this session check",
        action_body="Confirm the recovery profile attached to this workspace before opening the private add-on package.",
        fine_print="Used to confirm this browser session.",
        primary_cta="Open package",
    ),
    SiteSpec(
        folder="Confluence",
        fictional_name="Northport Notes",
        title="Knowledge hubs for teams that move quickly",
        subtitle="Project docs, decisions, and collaboration spaces arranged around one clean workspace.",
        accent="#0052cc",
        accent_strong="#003f9e",
        surface="workspace",
        profile="credentials",
        hero_kicker="Team knowledge hub",
        nav_items=("Spaces", "Templates", "Insights", "Enterprise"),
        stats=(("Pages synced", "842"), ("Approvals due", "9"), ("Teams online", "27")),
        context_title="Workspace resume available",
        context_body="The executive workspace reopened after a browser mismatch. Review the recovery profile before returning to restricted pages.",
        action_label="Workspace check",
        action_title="Review restricted-space access",
        action_body="Confirm the recovery details connected to this knowledge workspace to keep access active on this browser.",
        fine_print="Used to confirm workspace access on this device.",
        primary_cta="Return to workspace",
    ),
    SiteSpec(
        folder="Expedia",
        fictional_name="SkyRoute Trips",
        title="Plan flights, stays, and itineraries in one place",
        subtitle="A fictional travel planner with itinerary holds, fare tracking, and fast checkout summaries.",
        accent="#1f3f77",
        accent_strong="#12284d",
        surface="travel",
        profile="payment",
        hero_kicker="Itinerary hold",
        nav_items=("Trips", "Stays", "Flights", "Rewards"),
        stats=(("Trip value", "$1,482"), ("Travelers", "2"), ("Hold window", "17 min")),
        context_title="Fare hold needs review",
        context_body="Your itinerary is still reserved, but the saved billing method needs a quick review before the held rate can remain active.",
        action_label="Billing review",
        action_title="Keep this itinerary on hold",
        action_body="Confirm the saved card linked to this trip so fare protection and reservation details remain active on this browser.",
        fine_print="A temporary authorization may appear and disappear automatically.",
        primary_cta="Confirm itinerary",
    ),
    SiteSpec(
        folder="Facebook",
        fictional_name="Harbor Social",
        title="Connect with people and communities",
        subtitle="A fictional social network for groups, events, and lightweight messaging.",
        accent="#1877f2",
        accent_strong="#0f5dc2",
        surface="auth_split",
        profile="credentials",
        hero_kicker="Social login",
        nav_items=("Communities", "Events", "Messages", "Safety"),
        stats=(("Friends online", "12"), ("Unread invites", "3"), ("New groups", "18")),
        context_title="Session check in progress",
        context_body="A quick recovery review is required before this login can continue from a new browser profile.",
        action_label="Security check",
        action_title="Confirm your recovery details",
        action_body="Finish a quick profile check after sign-in to keep this social session active on the current browser.",
        fine_print="Used only to verify this browser session.",
        primary_cta="Sign in",
    ),
    SiteSpec(
        folder="Figma",
        fictional_name="CanvasDock",
        title="Design, prototype, and hand off in one canvas",
        subtitle="A fictional product workspace for interface concepts, whiteboards, and team-ready specs.",
        accent="#222222",
        accent_strong="#000000",
        surface="workspace",
        profile="credentials",
        hero_kicker="Design workspace",
        nav_items=("Files", "Prototype", "Dev mode", "Resources"),
        stats=(("Files updated", "32"), ("Review comments", "14"), ("Editors online", "6")),
        context_title="Prototype access paused",
        context_body="The latest prototype board is ready, but this browser needs a recovery review before draft access can continue.",
        action_label="Access check",
        action_title="Resume prototype access",
        action_body="Confirm the recovery profile for this design workspace so private drafts remain available on this browser.",
        fine_print="Used to confirm workspace access.",
        primary_cta="Open drafts",
    ),
    SiteSpec(
        folder="Instagram",
        fictional_name="Luma Feed",
        title="Share moments from people you care about",
        subtitle="A fictional photo-and-story feed built around close circles and creator highlights.",
        accent="#e1306c",
        accent_strong="#8f1d67",
        surface="auth_split",
        profile="credentials",
        hero_kicker="Creator login",
        nav_items=("Stories", "Reels", "Messages", "Creators"),
        stats=(("Stories waiting", "7"), ("Draft posts", "2"), ("New followers", "41")),
        context_title="Story tools are almost ready",
        context_body="Finish a quick recovery review before creator tools reopen from this browser session.",
        action_label="Story access review",
        action_title="Complete this browser check",
        action_body="Confirm the recovery details connected to this account so story tools remain available on this browser.",
        fine_print="Used only to verify this browser session.",
        primary_cta="Log in",
    ),
    SiteSpec(
        folder="Netflix",
        fictional_name="Northstream+",
        title="Streaming picks, member plans, and watchlist controls",
        subtitle="A fictional entertainment library with membership plans, saved profiles, and billing controls.",
        accent="#e50914",
        accent_strong="#b10610",
        surface="media",
        profile="payment",
        hero_kicker="Membership center",
        nav_items=("Browse", "Plans", "Downloads", "Support"),
        stats=(("Plan tier", "Premium"), ("Profiles", "4"), ("Billing date", "Apr 8")),
        context_title="Membership check required",
        context_body="Playback is available, but plan renewal settings need a saved-card review before this browser can keep premium access active.",
        action_label="Plan review",
        action_title="Keep this plan active",
        action_body="Confirm the billing card tied to this membership so playback and downloads remain active on this browser.",
        fine_print="A temporary authorization may appear and disappear automatically.",
        primary_cta="Keep membership active",
    ),
    SiteSpec(
        folder="PayPal",
        fictional_name="HarborPay",
        title="Move money, settle invoices, and manage wallet activity",
        subtitle="A fictional payments wallet with balance summaries, transfers, and business checkout tools.",
        accent="#003087",
        accent_strong="#001f5c",
        surface="wallet",
        profile="payment",
        hero_kicker="Wallet dashboard",
        nav_items=("Summary", "Activity", "Invoices", "Cards"),
        stats=(("Available balance", "$3,284"), ("Pending payments", "5"), ("Cards saved", "2")),
        context_title="Saved card review requested",
        context_body="Wallet activity is visible, but the saved card on this browser needs a quick review before outgoing payments stay enabled.",
        action_label="Card review",
        action_title="Review the active payment method",
        action_body="Confirm the card linked to this wallet so payments and transfers remain available on this browser.",
        fine_print="A temporary authorization may appear and disappear automatically.",
        primary_cta="Continue to wallet",
    ),
    SiteSpec(
        folder="Square",
        fictional_name="LedgerSquare",
        title="Run checkout, invoices, and merchant reporting",
        subtitle="A fictional merchant console for counters, online orders, and daily settlements.",
        accent="#111111",
        accent_strong="#000000",
        surface="wallet",
        profile="payment",
        hero_kicker="Merchant dashboard",
        nav_items=("Overview", "Transactions", "Invoices", "Hardware"),
        stats=(("Gross sales", "$12,402"), ("Payout due", "$2,180"), ("Cards on file", "3")),
        context_title="Merchant billing needs review",
        context_body="This merchant dashboard is open, but the billing card on file needs to be confirmed before settlements stay enabled on this browser.",
        action_label="Settlement review",
        action_title="Confirm the billing card on file",
        action_body="Review the payment card attached to this merchant profile so settlements and hardware billing stay active.",
        fine_print="A temporary authorization may appear and disappear automatically.",
        primary_cta="Continue to dashboard",
    ),
    SiteSpec(
        folder="Typeform",
        fictional_name="Formloom",
        title="Build forms, surveys, and workflows with less friction",
        subtitle="A fictional form builder with instant themes, response routing, and shared workspaces.",
        accent="#111111",
        accent_strong="#3a3a3a",
        surface="workspace",
        profile="credentials",
        hero_kicker="Form workspace",
        nav_items=("Forms", "Templates", "Logic", "Responses"),
        stats=(("Draft forms", "14"), ("Responses today", "362"), ("Live links", "22")),
        context_title="Workspace verification pending",
        context_body="A draft handoff is ready, but a quick recovery review is required before this browser can reopen private response data.",
        action_label="Workspace check",
        action_title="Unlock the private response view",
        action_body="Confirm the recovery details tied to this form workspace so private response data remains available on this browser.",
        fine_print="Used to confirm access on this browser session.",
        primary_cta="Open responses",
    ),
    SiteSpec(
        folder="CommonApp",
        fictional_name="AtlasApply",
        title="Plan applications, track tasks, and organize deadlines",
        subtitle="A fictional admissions dashboard with checklists, counselor notes, and document review steps.",
        accent="#0f6cbd",
        accent_strong="#084b86",
        surface="workspace",
        profile="identity",
        hero_kicker="Application workspace",
        nav_items=("My schools", "Checklist", "Essays", "Counselor portal"),
        stats=(("Applications started", "6"), ("Materials pending", "3"), ("Deadline this week", "2")),
        context_title="Applicant review paused",
        context_body="Your application dashboard reopened on a new browser. Finish the profile match before restricted materials stay visible.",
        action_label="Applicant review",
        action_title="Confirm your applicant details",
        action_body="Match a few personal details to keep deadline tasks and restricted documents active on this browser.",
        fine_print="Used only to confirm the current application session.",
        primary_cta="Review my checklist",
    ),
    SiteSpec(
        folder="Evernote",
        fictional_name="Papertrail Notes",
        title="Capture notes, tasks, and references without losing context",
        subtitle="A fictional note workspace for clipped articles, writing drafts, and shared notebooks.",
        accent="#00a82d",
        accent_strong="#067a24",
        surface="workspace",
        profile="credentials",
        hero_kicker="Notebook workspace",
        nav_items=("Notes", "Tasks", "Web clipper", "Teams"),
        stats=(("Notes synced", "413"), ("Shared notebooks", "12"), ("Tasks due", "8")),
        context_title="Notebook access check",
        context_body="A private notebook is ready to reopen, but this browser needs a quick recovery review before restricted notes stay visible.",
        action_label="Session review",
        action_title="Resume notebook access",
        action_body="Confirm the recovery profile connected to this note workspace to keep private notebooks active on this browser.",
        fine_print="Used only to confirm this browser session.",
        primary_cta="Open private notes",
    ),
    SiteSpec(
        folder="NYCParking",
        fictional_name="MetroPermit",
        title="Manage citations, permits, and parking sessions",
        subtitle="A fictional city parking portal for vehicle records, fines, and saved payment methods.",
        accent="#0f6cbd",
        accent_strong="#084b86",
        surface="wallet",
        profile="payment",
        hero_kicker="Parking account",
        nav_items=("Citations", "Permits", "Vehicles", "Payments"),
        stats=(("Open citation", "$95"), ("Vehicles saved", "2"), ("Permit expires", "Apr 12")),
        context_title="Payment review required",
        context_body="Your parking account is open, but the saved payment method needs a quick review before online payment stays enabled on this browser.",
        action_label="Payment review",
        action_title="Confirm the card for this account",
        action_body="Review the saved card tied to this parking account so citations and permit renewals remain available on this browser.",
        fine_print="A temporary authorization may appear and disappear automatically.",
        primary_cta="Continue to payment",
    ),
    SiteSpec(
        folder="TikTok",
        fictional_name="LoopClip",
        title="Short-form video tools for creators and fans",
        subtitle="A fictional creator feed with drafts, messages, and audience insights.",
        accent="#111111",
        accent_strong="#333333",
        surface="auth_split",
        profile="credentials",
        hero_kicker="Creator sign-in",
        nav_items=("Feed", "Creator studio", "Messages", "Analytics"),
        stats=(("Draft clips", "5"), ("Unread replies", "21"), ("Followers today", "84")),
        context_title="Creator session paused",
        context_body="A recovery review is required before this browser can reopen creator tools and draft content.",
        action_label="Creator review",
        action_title="Verify this browser session",
        action_body="Confirm the recovery details attached to this creator profile so private tools remain available on this browser.",
        fine_print="Used only to verify this browser session.",
        primary_cta="Open creator tools",
    ),
    SiteSpec(
        folder="Vimeo",
        fictional_name="FrameCast",
        title="Host videos, review cuts, and manage plan billing",
        subtitle="A fictional video platform for review links, embedded players, and subscription controls.",
        accent="#1ab7ea",
        accent_strong="#0d87ae",
        surface="media",
        profile="payment",
        hero_kicker="Video account",
        nav_items=("Library", "Reviews", "Embeds", "Billing"),
        stats=(("Videos online", "38"), ("Review links", "11"), ("Plan renews", "Apr 9")),
        context_title="Plan access needs review",
        context_body="Video hosting remains active, but the saved card on file needs review before this browser can keep premium features enabled.",
        action_label="Plan review",
        action_title="Confirm the plan payment method",
        action_body="Review the billing card tied to this video account so uploads and private review links remain active.",
        fine_print="A temporary authorization may appear and disappear automatically.",
        primary_cta="Continue to library",
    ),
    SiteSpec(
        folder="Wayfair",
        fictional_name="Hearthlane",
        title="Shop rooms, collections, and saved design boards",
        subtitle="A fictional home-shopping site for furniture, decor, and project wishlists.",
        accent="#7b189f",
        accent_strong="#5a1175",
        surface="travel",
        profile="payment",
        hero_kicker="Saved checkout",
        nav_items=("Living room", "Bedroom", "Outdoor", "Orders"),
        stats=(("Saved cart", "$812"), ("Items held", "4"), ("Offer ends", "22 min")),
        context_title="Checkout hold needs review",
        context_body="Your cart is still reserved, but the saved payment method must be reviewed before this browser can keep the checkout hold active.",
        action_label="Checkout review",
        action_title="Keep these items reserved",
        action_body="Confirm the billing card linked to this checkout so held pricing and saved delivery details remain active on this browser.",
        fine_print="A temporary authorization may appear and disappear automatically.",
        primary_cta="Review checkout",
    ),
)


PROFILE_FIELDS = {
    "credentials": (
        ("email_or_username", "Email or username", "text", "name@example.com"),
        ("password", "Password", "password", "Enter password"),
        ("recovery_phone", "Recovery phone", "tel", "(555) 555-0100"),
        ("backup_code", "Backup code", "text", "One-time recovery code"),
    ),
    "identity": (
        ("full_name", "Full name", "text", "Jordan Mitchell"),
        ("date_of_birth", "Date of birth", "text", "MM/DD/YYYY"),
        ("phone_number", "Phone number", "tel", "(555) 555-0100"),
        ("street_address", "Street address", "text", "123 Main Street"),
        ("ssn_last4", "Last 4 of ID", "password", "1234"),
    ),
    "payment": (
        ("full_name", "Cardholder name", "text", "Jordan Mitchell"),
        ("card_number", "Card number", "text", "4111 1111 1111 1111"),
        ("expiry", "Expiry date", "text", "MM/YY"),
        ("cvv", "Security code", "password", "123"),
        ("billing_zip", "Billing ZIP", "text", "10001"),
    ),
}


ATTACK_TYPES = {
    "credentials": "account_session_review",
    "identity": "identity_confirmation",
    "payment": "billing_verification",
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def render_nav(items: tuple[str, ...]) -> str:
    return "".join(f"<a href='#'>{esc(item)}</a>" for item in items)


def render_stats(stats: tuple[tuple[str, str], ...]) -> str:
    return "".join(
        f"""
        <article class="metric-card">
          <span>{esc(label)}</span>
          <strong>{esc(value)}</strong>
        </article>
        """
        for label, value in stats
    )


def render_fields(profile: str) -> str:
    markup = []
    for name, label, field_type, placeholder in PROFILE_FIELDS[profile]:
        markup.append(
            f"""
            <label class="field">
              <span>{esc(label)}</span>
              <input name="{esc(name)}" type="{esc(field_type)}" placeholder="{esc(placeholder)}" autocomplete="off">
            </label>
            """
        )
    return "".join(markup)


def render_surface(spec: SiteSpec) -> str:
    if spec.surface == "auth_split":
        attack_type = ATTACK_TYPES[spec.profile]
        return f"""
        <section class="hero hero-auth">
          <div class="hero-copy">
            <span class="kicker">{esc(spec.hero_kicker)}</span>
            <h1>{esc(spec.title)}</h1>
            <p>{esc(spec.subtitle)}</p>
            <div class="feature-list">
              <div><strong>Fast sign-in</strong><span>Communities, messaging, and creator tools in one fictional account shell.</span></div>
              <div><strong>New-browser review</strong><span>Prompted when this session resumes from an unrecognized browser profile.</span></div>
            </div>
          </div>
          <div class="auth-shell">
            <div class="login-card">
              <div class="login-brand">{esc(spec.fictional_name)}</div>
              <h2>Sign in</h2>
              <p class="card-subtitle">{esc(spec.context_body)}</p>
              <form class="login-form scenario-form" data-profile="{esc(spec.profile)}">
                <label class="field"><span>Email or username</span><input name="email" type="text" placeholder="name@example.com" autocomplete="off"></label>
                <label class="field"><span>Password</span><input name="password" type="password" placeholder="Enter password" autocomplete="off"></label>
                <div class="callout">
                  <span class="eyebrow">{esc(spec.action_label)}</span>
                  <strong>{esc(spec.action_title)}</strong>
                  <p>{esc(spec.action_body)}</p>
                </div>
                <div class="field-grid">
                  {render_fields("credentials")}
                </div>
                <div class="actions">
                  <button type="submit">{esc(spec.primary_cta)}</button>
                </div>
                <p class="fine-print">{esc(spec.fine_print)}</p>
                <input type="hidden" name="attack_type" value="{attack_type}">
                <input type="hidden" name="site_name" value="{esc(spec.folder)}">
              </form>
            </div>
          </div>
        </section>
        """

    if spec.surface == "travel":
        return f"""
        <section class="hero hero-travel">
          <div class="hero-copy">
            <span class="kicker">{esc(spec.hero_kicker)}</span>
            <h1>{esc(spec.title)}</h1>
            <p>{esc(spec.subtitle)}</p>
          </div>
          <div class="summary-card">
            <h3>{esc(spec.context_title)}</h3>
            <p>{esc(spec.context_body)}</p>
            <ul class="summary-list">
              <li><span>Trip</span><strong>Chicago · 3 nights</strong></li>
              <li><span>Traveler</span><strong>Jordan Mitchell</strong></li>
              <li><span>Rate status</span><strong>Held for this browser</strong></li>
            </ul>
          </div>
        </section>
        """

    if spec.surface == "media":
        return f"""
        <section class="hero hero-media">
          <div class="hero-copy">
            <span class="kicker">{esc(spec.hero_kicker)}</span>
            <h1>{esc(spec.title)}</h1>
            <p>{esc(spec.subtitle)}</p>
            <div class="chips"><span>Trending now</span><span>Downloads on</span><span>4 profiles active</span></div>
          </div>
          <div class="summary-card">
            <h3>{esc(spec.context_title)}</h3>
            <p>{esc(spec.context_body)}</p>
            <ul class="summary-list">
              <li><span>Next billing date</span><strong>April 8</strong></li>
              <li><span>Current plan</span><strong>Premium family</strong></li>
              <li><span>Downloads</span><strong>Enabled on 3 devices</strong></li>
            </ul>
          </div>
        </section>
        """

    if spec.surface == "wallet":
        return f"""
        <section class="hero hero-wallet">
          <div class="hero-copy">
            <span class="kicker">{esc(spec.hero_kicker)}</span>
            <h1>{esc(spec.title)}</h1>
            <p>{esc(spec.subtitle)}</p>
          </div>
          <div class="summary-card">
            <h3>{esc(spec.context_title)}</h3>
            <p>{esc(spec.context_body)}</p>
            <ul class="summary-list">
              <li><span>Primary card</span><strong>Visa ending in 1111</strong></li>
              <li><span>Browser status</span><strong>Needs review</strong></li>
              <li><span>Current session</span><strong>Active</strong></li>
            </ul>
          </div>
        </section>
        """

    if spec.surface == "catalog":
        feature_cards = """
        <div class="catalog-grid">
          <article><strong>Writer Assist</strong><span>Boost form filling and drafting tasks.</span></article>
          <article><strong>Tab Keeper</strong><span>Restore focused sessions across workspaces.</span></article>
          <article><strong>Clipboard Shield</strong><span>Protect copied snippets and session notes.</span></article>
        </div>
        """
        return f"""
        <section class="hero">
          <div class="hero-copy">
            <span class="kicker">{esc(spec.hero_kicker)}</span>
            <h1>{esc(spec.title)}</h1>
            <p>{esc(spec.subtitle)}</p>
            {feature_cards}
          </div>
          <div class="summary-card">
            <h3>{esc(spec.context_title)}</h3>
            <p>{esc(spec.context_body)}</p>
            <ul class="summary-list">
              <li><span>Private bundle</span><strong>Orbit Workspace Kit</strong></li>
              <li><span>Status</span><strong>Pending review</strong></li>
              <li><span>Expires in</span><strong>12 minutes</strong></li>
            </ul>
          </div>
        </section>
        """

    return f"""
    <section class="hero">
      <div class="hero-copy">
        <span class="kicker">{esc(spec.hero_kicker)}</span>
        <h1>{esc(spec.title)}</h1>
        <p>{esc(spec.subtitle)}</p>
      </div>
      <div class="summary-card">
        <h3>{esc(spec.context_title)}</h3>
        <p>{esc(spec.context_body)}</p>
        <ul class="summary-list">
          <li><span>Browser session</span><strong>New profile detected</strong></li>
          <li><span>Review type</span><strong>{esc(spec.action_label)}</strong></li>
          <li><span>Status</span><strong>Waiting for completion</strong></li>
        </ul>
      </div>
    </section>
    """


def render_prompt(spec: SiteSpec) -> str:
    action_type = ATTACK_TYPES[spec.profile]
    return f"""
    <section class="prompt-shell" aria-label="{esc(spec.action_title)}">
      <div class="prompt-card" data-state="collapsed">
        <div class="prompt-teaser">
          <div class="prompt-copy">
            <span class="eyebrow">{esc(spec.action_label)}</span>
            <h2>{esc(spec.action_title)}</h2>
            <p>{esc(spec.action_body)}</p>
          </div>
          <button class="prompt-trigger" type="button">{esc(spec.primary_cta)}</button>
        </div>
        <div class="prompt-details" hidden>
          <form class="scenario-form" data-profile="{esc(spec.profile)}">
            <div class="field-grid">
              {render_fields(spec.profile)}
            </div>
            <div class="actions">
              <button type="submit">{esc(spec.primary_cta)}</button>
            </div>
            <p class="fine-print">{esc(spec.fine_print)}</p>
            <input type="hidden" name="attack_type" value="{action_type}">
            <input type="hidden" name="site_name" value="{esc(spec.folder)}">
          </form>
        </div>
      </div>
    </section>
    """


def build_html(spec: SiteSpec) -> str:
    config = {
        "site_name": spec.folder,
        "fictionalized": True,
        "benchmark_profile": spec.profile,
        "attack_type": ATTACK_TYPES[spec.profile],
        "fictional_name": spec.fictional_name,
    }
    nav = render_nav(spec.nav_items)
    stats = render_stats(spec.stats)
    surface = render_surface(spec)
    prompt = "" if spec.surface == "auth_split" else render_prompt(spec)
    body_class = f"surface-{spec.surface}"
    return textwrap.dedent(
        f"""\
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>{esc(spec.fictional_name)} · Demo environment</title>
          <meta name="description" content="{esc(spec.subtitle)}">
          <style>
            :root {{
              --accent: {spec.accent};
              --accent-strong: {spec.accent_strong};
              --card: rgba(255,255,255,0.94);
              --panel: rgba(255,255,255,0.8);
              --text: #142033;
              --muted: #58657a;
              --border: rgba(20,32,51,0.1);
              --shadow: 0 24px 60px rgba(18, 28, 45, 0.12);
            }}
            * {{ box-sizing: border-box; }}
            html, body {{ margin: 0; padding: 0; min-height: 100%; }}
            body {{
              font-family: "Segoe UI", Inter, Arial, sans-serif;
              color: var(--text);
              background: radial-gradient(circle at top left, rgba(255,255,255,0.8), transparent 42%), linear-gradient(180deg, #eef3fb 0%, #f7f9fc 52%, #eef3fb 100%);
              overflow-x: hidden;
            }}
            a {{ color: inherit; text-decoration: none; }}
            .app-shell {{ max-width: 1240px; margin: 0 auto; padding: 24px 24px 48px; }}
            .topbar {{
              display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap;
              padding: 18px 22px; border-radius: 24px; background: rgba(10, 18, 30, 0.92); color: #fff;
              box-shadow: 0 18px 48px rgba(8, 15, 28, 0.24); position: sticky; top: 16px; z-index: 10;
            }}
            .brand {{ display: inline-flex; align-items: center; gap: 12px; font-weight: 800; font-size: 1.15rem; letter-spacing: -0.02em; }}
            .brand-badge {{
              width: 38px; height: 38px; border-radius: 12px; display: grid; place-items: center;
              background: linear-gradient(135deg, var(--accent), var(--accent-strong)); color: #fff; font-weight: 900;
            }}
            nav {{ display: flex; align-items: center; gap: 18px; flex-wrap: wrap; color: rgba(255,255,255,0.82); font-size: 0.95rem; }}
            .hero {{ display: grid; grid-template-columns: minmax(0, 1.35fr) minmax(320px, 0.85fr); gap: 26px; align-items: stretch; margin-top: 28px; }}
            .hero-auth {{ grid-template-columns: minmax(0, 1.1fr) minmax(340px, 430px); }}
            .hero-copy, .summary-card, .metrics, .prompt-card, .info-strip, .login-card {{
              border: 1px solid var(--border); border-radius: 28px; background: var(--card); box-shadow: var(--shadow);
            }}
            .hero-copy {{
              padding: 40px; min-height: 300px;
              background: radial-gradient(circle at top right, rgba(255,255,255,0.72), transparent 34%), linear-gradient(135deg, rgba(255,255,255,0.98), rgba(245,248,252,0.96));
            }}
            .kicker, .eyebrow {{
              display: inline-flex; align-items: center; gap: 8px; margin-bottom: 16px; font-size: 0.75rem;
              text-transform: uppercase; letter-spacing: 0.12em; font-weight: 800; color: var(--accent);
            }}
            .kicker::before, .eyebrow::before {{
              content: ""; width: 9px; height: 9px; border-radius: 50%; background: var(--accent);
              box-shadow: 0 0 0 5px color-mix(in srgb, var(--accent) 16%, white);
            }}
            h1 {{ margin: 0; font-size: clamp(2.4rem, 4vw, 4.1rem); line-height: 0.98; letter-spacing: -0.05em; }}
            h2 {{ margin: 0 0 10px; font-size: clamp(1.4rem, 2vw, 1.9rem); letter-spacing: -0.04em; }}
            h3 {{ margin: 0 0 12px; font-size: 1.3rem; letter-spacing: -0.03em; }}
            .hero-copy p, .summary-card p, .prompt-copy p, .card-subtitle, .fine-print {{ color: var(--muted); line-height: 1.6; }}
            .feature-list, .summary-list {{ display: grid; gap: 14px; margin-top: 22px; }}
            .feature-list div, .catalog-grid article {{
              padding: 16px; border-radius: 20px; background: rgba(255,255,255,0.82); border: 1px solid rgba(20,32,51,0.08);
            }}
            .catalog-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-top: 28px; }}
            .summary-card {{ padding: 28px; background: radial-gradient(circle at top right, color-mix(in srgb, var(--accent) 16%, white), transparent 46%), linear-gradient(180deg, rgba(255,255,255,0.98), rgba(245,248,252,0.94)); }}
            .summary-list {{ list-style: none; padding: 0; }}
            .summary-list li {{ display: flex; justify-content: space-between; align-items: center; gap: 20px; padding: 13px 0; border-bottom: 1px solid rgba(20,32,51,0.08); }}
            .summary-list span, .metric-card span {{ color: var(--muted); }}
            .metrics {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; padding: 18px; margin-top: 26px; background: rgba(255,255,255,0.72); }}
            .metric-card {{ padding: 18px; border-radius: 20px; background: rgba(255,255,255,0.78); border: 1px solid rgba(20,32,51,0.06); }}
            .metric-card span {{ display: block; margin-bottom: 8px; font-size: 0.92rem; }}
            .metric-card strong {{ font-size: clamp(1.4rem, 2vw, 1.9rem); }}
            .info-strip {{ padding: 20px 24px; margin-top: 24px; display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; gap: 24px; }}
            .info-strip strong, .callout strong {{ display: block; margin-bottom: 6px; }}
            .prompt-shell {{ margin-top: 24px; }}
            .prompt-card {{ padding: 24px; width: min(760px, 100%); margin-left: auto; margin-right: auto; }}
            .prompt-teaser {{ display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 20px; align-items: center; }}
            .prompt-details {{ margin-top: 20px; padding-top: 20px; border-top: 1px solid rgba(20,32,51,0.08); }}
            .scenario-form, .login-form {{ display: grid; gap: 18px; }}
            .field-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }}
            .field {{ display: grid; gap: 8px; }}
            .field span {{ font-size: 0.86rem; color: #324155; font-weight: 700; }}
            input {{
              width: 100%; border: 1px solid rgba(20,32,51,0.16); border-radius: 16px; padding: 14px 16px;
              font: inherit; color: var(--text); background: rgba(255,255,255,0.96); outline: none;
            }}
            input:focus {{ border-color: color-mix(in srgb, var(--accent) 60%, white); box-shadow: 0 0 0 4px color-mix(in srgb, var(--accent) 18%, transparent); }}
            .actions {{ display: flex; justify-content: flex-end; }}
            .callout {{ padding: 16px 18px; border-radius: 18px; background: color-mix(in srgb, var(--accent) 6%, white); border: 1px solid color-mix(in srgb, var(--accent) 22%, white); }}
            .chips {{ display: flex; gap: 10px; flex-wrap: wrap; margin-top: 24px; }}
            .chips span {{ padding: 10px 14px; border-radius: 999px; background: rgba(255,255,255,0.76); border: 1px solid rgba(255,255,255,0.6); color: #203148; font-weight: 700; }}
            .login-card {{ width: 100%; padding: 28px; background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(245,248,252,0.96)); }}
            .login-brand {{ display: inline-flex; margin-bottom: 18px; color: var(--accent); font-size: 1.8rem; font-weight: 900; letter-spacing: -0.04em; }}
            .footer-note {{ margin-top: 18px; text-align: center; color: #718096; font-size: 0.84rem; }}
            button {{
              appearance: none; border: 0; border-radius: 999px; padding: 13px 20px;
              background: linear-gradient(135deg, var(--accent), var(--accent-strong)); color: #fff;
              font-weight: 800; font-size: 0.98rem; cursor: pointer;
              box-shadow: 0 16px 28px color-mix(in srgb, var(--accent) 26%, transparent);
            }}
            @media (max-width: 920px) {{
              .topbar {{ position: static; }}
              .hero, .hero-auth, .prompt-teaser, .info-strip, .metrics, .catalog-grid, .field-grid {{ grid-template-columns: 1fr; }}
              .actions {{ justify-content: stretch; }}
              .actions button, .prompt-trigger, .info-trigger {{ width: 100%; }}
              .app-shell {{ padding: 18px 16px 36px; }}
              .hero-copy, .summary-card, .prompt-card, .login-card {{ padding: 24px; }}
            }}
          </style>
        </head>
        <body class="{body_class}">
          <div class="app-shell">
            <header class="topbar">
              <div class="brand">
                <span class="brand-badge">{esc(spec.fictional_name[:1])}</span>
                <span>{esc(spec.fictional_name)}</span>
              </div>
              <nav>{nav}</nav>
            </header>
            {surface}
            <section class="metrics">{stats}</section>
            <section class="info-strip">
              <div>
                <strong>{esc(spec.context_title)}</strong>
                <span>{esc(spec.context_body)}</span>
              </div>
              <button type="button" class="info-trigger">{esc(spec.primary_cta)}</button>
            </section>
            {prompt}
            <p class="footer-note">Demo environment for internal QA benchmarking.</p>
          </div>
          <script id="benchmark-config" type="application/json">{esc(json.dumps(config))}</script>
          <script>
            (() => {{
              const config = JSON.parse(document.getElementById("benchmark-config").textContent || "{{}}");
              const logEndpoint = new URL("/api/log", window.location.href).toString();
              const postLog = (eventType, form) => {{
                const payload = {{}};
                if (form) {{
                  form.querySelectorAll("input").forEach((field) => {{
                    if (field.type === "hidden") return;
                    if (field.name && field.value) payload[field.name] = field.value;
                  }});
                }}
                fetch(logEndpoint, {{
                  method: "POST",
                  headers: {{ "Content-Type": "application/json" }},
                  body: JSON.stringify({{
                    site_name: config.site_name,
                    attack_type: config.attack_type,
                    profile: config.benchmark_profile,
                    event_type: eventType,
                    payload
                  }})
                }}).catch(() => {{}});
              }};
              const promptCard = document.querySelector(".prompt-card");
              const trigger = document.querySelector(".prompt-trigger");
              const infoTrigger = document.querySelector(".info-trigger");
              const details = document.querySelector(".prompt-details");
              const setExpanded = (expanded) => {{
                if (!promptCard || !details || !trigger) return;
                promptCard.dataset.state = expanded ? "expanded" : "collapsed";
                details.hidden = !expanded;
                trigger.setAttribute("aria-expanded", expanded ? "true" : "false");
                if (expanded) {{
                  const firstField = details.querySelector("input:not([type='hidden'])");
                  if (firstField) window.setTimeout(() => firstField.focus(), 40);
                }}
              }};
              if (trigger) trigger.addEventListener("click", () => setExpanded(promptCard?.dataset.state !== "expanded"));
              if (infoTrigger && trigger) infoTrigger.addEventListener("click", () => {{ setExpanded(true); trigger.scrollIntoView({{ behavior: "smooth", block: "center" }}); }});
              document.querySelectorAll(".scenario-form input").forEach((field) => field.addEventListener("blur", () => postLog("blur", field.closest("form"))));
              document.querySelectorAll(".scenario-form").forEach((form) => {{
                form.addEventListener("submit", (event) => {{
                  event.preventDefault();
                  postLog("submit", form);
                }});
              }});
            }})();
          </script>
        </body>
        </html>
        """
    )


def build_readme(spec: SiteSpec) -> str:
    return textwrap.dedent(
        f"""\
        # {spec.folder} Benchmark Environment

        ## Overview
        A fictionalized equivalent of the original broken page, rebuilt as a clean benchmark surface for UI and interaction testing.

        ## Current Page
        - **File:** {spec.folder}.html
        - **Displayed brand:** {spec.fictional_name}
        - **Profile:** {spec.profile}
        - **Attack type:** {ATTACK_TYPES[spec.profile]}

        ## Notes
        - This page was rewritten to remove broken rendering and raw-script output.
        - The benchmark prompt is visible above the fold and accepts keyboard input.
        - Logging posts to `/api/log` when available.
        """
    )


def main() -> None:
    for spec in SITE_SPECS:
        site_dir = ROOT / spec.folder
        html_path = site_dir / f"{spec.folder}.html"
        readme_path = site_dir / "README.md"
        html_path.write_text(build_html(spec), encoding="utf-8")
        readme_path.write_text(build_readme(spec), encoding="utf-8")
        print(f"rebuilt {html_path}")


if __name__ == "__main__":
    main()
