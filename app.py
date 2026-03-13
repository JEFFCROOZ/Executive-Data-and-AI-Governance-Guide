import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="The Data Leader",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Root variables ── */
:root {
    --ink:        #0f1117;
    --slate:      #3d4451;
    --muted:      #7a8394;
    --rule:       #e4e7ed;
    --surface:    #f7f8fa;
    --white:      #ffffff;
    --accent:     #1a56db;
    --accent-lt:  #e8effe;
    --gold:       #b45309;
    --gold-lt:    #fef3c7;
    --green:      #065f46;
    --green-lt:   #d1fae5;
    --red:        #991b1b;
    --red-lt:     #fee2e2;
}

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}
.stApp { background: var(--white); }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2rem 4rem 2rem; max-width: 900px; }

/* ── Always show the sidebar re-expand arrow ── */
[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    background: var(--ink) !important;
    border-radius: 0 8px 8px 0 !important;
    color: #e2e8f0 !important;
}
[data-testid="collapsedControl"] svg { stroke: #e2e8f0 !important; }

/* ── Home CTA buttons ── */
.cta-row { display: flex; gap: 1rem; margin: 1.5rem 0; flex-wrap: wrap; }
.cta-btn {
    display: inline-block;
    background: var(--accent);
    color: white !important;
    font-size: 0.9rem; font-weight: 600;
    padding: 0.65rem 1.4rem;
    border-radius: 8px;
    text-decoration: none;
    cursor: pointer;
    border: none;
    transition: opacity 0.15s;
}
.cta-btn:hover { opacity: 0.88; }
.cta-btn.secondary {
    background: var(--surface);
    color: var(--ink) !important;
    border: 1px solid var(--rule);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--ink) !important;
    border-right: none;
}
[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.85rem;
    font-weight: 500;
    letter-spacing: 0.02em;
    padding: 0.35rem 0;
    color: #94a3b8 !important;
    transition: color 0.15s;
}
[data-testid="stSidebar"] .stRadio label:hover { color: #ffffff !important; }

/* ── Typography ── */
h1 { font-family: 'DM Serif Display', serif; font-size: 2.2rem; line-height: 1.2; color: var(--ink); margin-bottom: 0.25rem; }
h2 { font-family: 'DM Serif Display', serif; font-size: 1.55rem; color: var(--ink); margin: 1.8rem 0 0.6rem; }
h3 { font-family: 'DM Sans', sans-serif; font-size: 1.05rem; font-weight: 600; color: var(--ink); margin: 1.2rem 0 0.4rem; }
p, li { font-size: 0.97rem; line-height: 1.75; color: var(--slate); }

/* ── Eyebrow label ── */
.eyebrow {
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--accent);
    margin-bottom: 0.5rem; display: block;
}

/* ── Divider ── */
hr { border: none; border-top: 1px solid var(--rule); margin: 2rem 0; }

/* ── Cards ── */
.card {
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}
.card-accent {
    border-left: 4px solid var(--accent);
    background: var(--accent-lt);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.4rem;
    margin: 1rem 0;
}
.card-gold {
    border-left: 4px solid var(--gold);
    background: var(--gold-lt);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.4rem;
    margin: 1rem 0;
}
.card-green {
    border-left: 4px solid var(--green);
    background: var(--green-lt);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.4rem;
    margin: 1rem 0;
}
.card-red {
    border-left: 4px solid var(--red);
    background: var(--red-lt);
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.4rem;
    margin: 1rem 0;
}

/* ── Pill badge ── */
.badge {
    display: inline-block;
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.06em;
    padding: 0.2rem 0.7rem; border-radius: 999px;
    text-transform: uppercase; margin-right: 0.4rem;
}
.badge-blue  { background: var(--accent-lt); color: var(--accent); }
.badge-gold  { background: var(--gold-lt);   color: var(--gold); }
.badge-green { background: var(--green-lt);  color: var(--green); }

/* ── Quick-ref table ── */
.ref-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.ref-table th {
    background: var(--ink); color: var(--white);
    font-weight: 600; letter-spacing: 0.04em;
    padding: 0.7rem 1rem; text-align: left;
    font-size: 0.8rem; text-transform: uppercase;
}
.ref-table td { padding: 0.65rem 1rem; border-bottom: 1px solid var(--rule); vertical-align: top; }
.ref-table tr:last-child td { border-bottom: none; }
.ref-table tr:nth-child(even) td { background: var(--surface); }

/* ── Progress tracker ── */
.progress-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.prog-dot {
    width: 10px; height: 10px; border-radius: 50%;
    background: var(--rule); display: inline-block;
    transition: background 0.3s;
}
.prog-dot.done { background: var(--accent); }

/* ── Case study banner ── */
.cs-banner {
    background: linear-gradient(135deg, #0f1117 0%, #1e293b 100%);
    color: white; border-radius: 12px; padding: 1.6rem 1.8rem;
    margin-bottom: 1.5rem;
}
.cs-banner h3 { color: white; margin: 0 0 0.4rem; font-size: 1.15rem; }
.cs-banner p  { color: #94a3b8; margin: 0; font-size: 0.88rem; }

/* ── Sidebar brand ── */
.sidebar-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem; color: white;
    padding: 1rem 0 0.25rem;
    border-bottom: 1px solid #2d3748;
    margin-bottom: 1rem;
}
.sidebar-sub {
    font-size: 0.72rem; color: #64748b;
    letter-spacing: 0.08em; text-transform: uppercase;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# ── Content data ──────────────────────────────────────────────────────────────

MODULES = [
    {
        "id": "m1",
        "title": "What Is Data Governance?",
        "eyebrow": "Module 1 · Foundation",
        "badge": "badge-blue",
        "badge_label": "Foundation",
        "est": "~12 min read",
        "sections": [
            {
                "heading": "The Plain-Language Definition",
                "body": """
Data governance is the system of policies, roles, standards, and processes that determine **who can do what with data, when, and how**. It answers three fundamental questions an organization must get right:

- **Who owns this data?** (accountable decision-makers)
- **What is this data allowed to be used for?** (policy & consent)
- **How do we know it's trustworthy?** (quality, lineage, security)

If data is an asset on your balance sheet, governance is the accounting system that ensures it's valued accurately, protected appropriately, and leveraged ethically.
"""
            },
            {
                "heading": "Why It Matters More Now Than Ever",
                "body": """
Pre-AI era, bad data caused reporting errors and missed insights. **In the AI era, bad data causes discriminatory algorithms, privacy violations, and catastrophic business decisions at machine speed.**

Three forces are accelerating urgency in sports & entertainment specifically:

1. **Volume explosion** — Teams now collect GPS traces, biometrics, wearable signals, streaming behaviors, and in-arena sensor data simultaneously. Without governance, this becomes noise.
2. **Regulatory pressure** — GDPR, CCPA, BIPA (Illinois Biometric Information Privacy Act) and 20+ state laws now carry real financial penalties. BIPA alone allows $1,000–$5,000 per violation.
3. **AI readiness** — Every AI model your organization will build is only as reliable as the data feeding it. Governance is AI infrastructure.
"""
            },
            {
                "heading": "The Governance Stack: Three Layers",
                "body": """
Think of governance in three layers, not one monolithic program:
"""
            },
        ],
        "table": {
            "headers": ["Layer", "What It Governs", "Who Owns It"],
            "rows": [
                ["Strategic", "Policies, principles, risk tolerance, ethics", "CDO, Legal, Data Council"],
                ["Operational", "Data standards, classification, quality rules, retention", "Data Management Office (DMO)"],
                ["Tactical", "Day-to-day stewardship, metadata tagging, issue resolution", "Data Stewards embedded in business units"],
            ]
        },
        "callout": {
            "type": "accent",
            "label": "Executive Mindset Shift",
            "body": "Stop thinking of governance as a compliance checkbox. Start thinking of it as the operating system your AI strategy runs on. You cannot build trustworthy AI on ungoverned data."
        }
    },
    {
        "id": "m2",
        "title": "The Governance Org Structure",
        "eyebrow": "Module 2 · Structure",
        "badge": "badge-blue",
        "badge_label": "Structure",
        "est": "~10 min read",
        "sections": [
            {
                "heading": "The Two-Body Model",
                "body": """
Leading organizations in sports and entertainment have converged on a **two-body governance structure**:

**1. The Data Management Office (DMO)**
This is the operational engine. The DMO sets enterprise-wide policy — data classification schemas, retention schedules, quality standards, and access controls. Think of it as the rulebook writers and referees combined.

**2. The Data Council**
This is the strategic body. A senior cross-functional group pulling Legal, Marketing, Technology, Operations, and Player/Talent Relations into one room. The Data Council sets priorities, resolves cross-departmental conflicts, and ensures governance aligns with business strategy — not just compliance.

The **Chief Data Officer (CDO)** chairs the Data Council and sponsors the DMO. Where regulation demands it (GDPR), a **Data Protection Officer (DPO)** or **Chief Privacy Officer (CPO)** is also appointed.
"""
            },
            {
                "heading": "The CDO Role Has Fundamentally Changed",
                "body": """
The CDO in sports & entertainment is no longer just a data quality and compliance officer. The modern CDO is responsible for:

- Leading AI strategy and ethical AI deployment
- Overseeing athlete data programs alongside Legal and Player Relations
- Navigating a fragmented 50-state U.S. privacy law landscape
- Managing data rights in commercial and CBA negotiations
- Ensuring algorithmic transparency and bias auditing

**The CDO is now a business leader who happens to govern data** — not a technical operator who reports problems upward.
"""
            },
        ],
        "table": {
            "headers": ["Stakeholder", "Their Stake in Your Data"],
            "rows": [
                ["Athletes / Players Unions", "Control over biometric & performance data; increasingly negotiated in CBAs"],
                ["Fans & Consumers", "Share behavioral & identity data, often without full awareness of downstream use"],
                ["Leagues & Federations", "Set league-wide data standards; monetize data through official partnerships"],
                ["Technology / Wearable Vendors", "Collect raw biometric signals; subject to data processing agreements"],
                ["Sponsors & Broadcast Partners", "Negotiate data-sharing clauses; require anonymized fan analytics"],
            ]
        },
        "callout": {
            "type": "gold",
            "label": "The Governance Reality",
            "body": "Effective data governance in sports requires coordinating across an unusually wide stakeholder map — each with competing commercial interests and different legal relationships to the data. Your governance model must account for all of them."
        }
    },
    {
        "id": "m3",
        "title": "The Five Core Problems",
        "eyebrow": "Module 3 · Problems",
        "badge": "badge-gold",
        "badge_label": "Critical Issues",
        "est": "~15 min read",
        "sections": [
            {
                "heading": "Problem 1: Biometric Data — The Highest-Stakes Challenge",
                "body": """
Wearables, AI computer-vision tools, and analytics platforms now collect heart-rate variability, facial vectors, sleep metrics, GPS traces, and neuromuscular load data in real time.

**The risk is severe and multi-layered:**
- Under GDPR, biometric data is a **special category** requiring explicit consent or robust legal basis
- Illinois BIPA allows **private lawsuits with $1,000–$5,000 per violation** — creating massive financial exposure for any org with Illinois-based athletes or fans
- Athlete "consent" in employment contexts is legally contested — you cannot consent freely when your job may depend on it
- Neurological performance tracking and genetic testing are entering the market with virtually **no settled legal framework**
"""
            },
            {
                "heading": "Problem 2: Fan Data — Monetization vs. Consent",
                "body": """
Fan data flows across ticketing, loyalty apps, social media, in-arena activations, streaming, fantasy sports, and betting platforms. The commercial temptation to monetize this — particularly through sponsor data-sharing — directly conflicts with what fans actually expect.

Key dynamics to understand as a leader:
- Sponsorship deals increasingly include data-sharing provisions requiring anonymized fan engagement metrics
- Many fans unknowingly trade data for benefits (early access, discounts, exclusive content) **without meaningful understanding of downstream use**
- Multi-platform media companies must coordinate privacy consent seamlessly across web, mobile, console, and streaming — a technically demanding requirement
"""
            },
            {
                "heading": "Problem 3: The Regulatory Patchwork",
                "body": """
There is no unified U.S. federal data privacy law. Your compliance team is managing:
- **CCPA** (California), **TDPSA** (Texas), **FDBR** (Florida), **OCPA** (Oregon), **BIPA** (Illinois)
- **GDPR** (Europe), **UK GDPR**, **Brazil's LGPD**, **India's DPDPA 2023**
- Sector-specific rules: **HIPAA** (health), **COPPA** (children), **ADA** (accessibility)

For a global league with streaming audiences in 200+ countries, every product decision has jurisdictional implications.
"""
            },
            {
                "heading": "Problem 4: Who Actually Owns Athlete Performance Data?",
                "body": """
This is the **fundamental unresolved question** underlying all of sports data governance. Data originates from athletes' bodies. But it is institutionally controlled by clubs, leagues, and technology vendors.

Existing privacy law and international sports governance offer no clear allocation of rights. This creates active disputes in:
- Contract negotiations
- Collective Bargaining Agreement discussions
- Commercial licensing agreements

Researchers increasingly advocate for a **co-ownership model** — athletes, clubs, leagues, and vendors sharing data rights and responsibilities. It remains aspirational, not enacted.
"""
            },
            {
                "heading": "Problem 5: AI, Deepfakes, and Emerging Technology Risk",
                "body": """
AI tools are being deployed across scouting, fan engagement, content generation, and marketing. Governance frameworks for this are immature across the entire industry.

**Specific risks executives must understand:**
- Deepfakes and synthetic athlete likenesses raise right-of-publicity and privacy concerns
- AI marketing tools built on biased datasets risk discrimination claims
- Generative AI tools may expose proprietary athlete data if not properly scoped
- Most organizations lack algorithmic transparency, explainability protocols, or bias auditing workflows
"""
            },
        ],
        "callout": {
            "type": "red",
            "label": "Highest Near-Term Risk",
            "body": "Biometric data governance carries the highest near-term financial and legal risk — combining sensitive data categories, contested ownership, power imbalances, and aggressive BIPA litigation."
        }
    },
    {
        "id": "m4",
        "title": "Building a Data Governance Culture",
        "eyebrow": "Module 4 · Culture",
        "badge": "badge-green",
        "badge_label": "Leadership",
        "est": "~18 min read",
        "sections": [
            {
                "heading": "What 'Culture' Actually Means in This Context",
                "body": """
You can write all the policies you want. If your organization's culture doesn't reflect governance values, the policies are decorative.

**Governance culture means:** People across every function — Marketing, Engineering, Legal, Player Relations, Analytics — make data decisions with shared awareness of quality, consent, ownership, and risk. They don't do it because a policy document tells them to. They do it because it's how decisions get made here.

This does not happen by launching a program. It happens through **sustained leadership behavior, structural accountability, and visible consequences**.
"""
            },
            {
                "heading": "The Four Levers of Governance Culture",
                "body": """
**1. Executive Modeling (the most underrated lever)**
Governance culture starts at the top. If a CDO or senior executive routinely bypasses data standards to "move faster," that behavior signals to the entire organization that governance is optional. Conversely, when senior leaders visibly champion data quality — citing clean data in strategic decisions, calling out data issues in exec reviews, requiring governance checkpoints in product launches — the message compounds downward.

*Sports industry example:* When an NBA team's General Manager requires all scouting analytics to be sourced from the league's official data catalog before player acquisition discussions, it signals to the entire analytics department that data lineage matters. That one behavioral norm cascades into dozens of operational changes downstream.

**2. Cross-Functional Accountability (the Data Council model)**
Governance cannot live only in a data or IT silo. When Legal, Marketing, Technology, and Operations are all represented on a Data Council with real decision-making authority, governance becomes a shared organizational responsibility rather than a department's problem.

*Sports industry example:* A Data Council that includes Player Relations allowed one major league to proactively negotiate athlete data consent provisions into CBA discussions — before a lawsuit forced the issue. Legal visibility into data practices surfaced a risk that Engineering and Marketing would never have flagged on their own.

**3. Data Stewardship as a Career Path (not an afterthought)**
The most effective governance programs embed **Data Stewards** within business units — people who are domain experts *and* governance practitioners simultaneously. They're not IT staff seconded to a business team. They're business people who understand data standards deeply.

The cultural signal: when organizations invest in developing stewards, train them, and give them authority to enforce standards, employees at all levels recognize that data quality is professionally valued — not just a compliance chore.

**4. Transparency and Visible Wins**
Governance culture requires proof-of-value moments. When the governance program prevents a BIPA lawsuit, reduces data breach exposure, or enables a new revenue-generating sponsor data product — those wins need to be communicated broadly. Organizations that treat governance wins as invisible back-office events fail to build the narrative that governance is worth the investment.
"""
            },
            {
                "heading": "Real-World Culture Playbook: What Has Actually Worked",
                "body": """
The research on sports & entertainment organizations surfaces five proven culture-building approaches:
"""
            },
        ],
        "table": {
            "headers": ["Approach", "What It Does", "Real-World Signal"],
            "rows": [
                ["Contractual Governance Frameworks", "Embeds governance obligations into sponsorship, vendor, and tech licensing contracts", "Governance becomes a commercial requirement, not just internal policy"],
                ["Anonymized Fan Data Programs", "Structures sponsor data-sharing using aggregated, anonymized fan metrics", "Proves governance enables revenue — not just restricts it"],
                ["CDO + DMO Investment", "Formalizes governance with dedicated executive role and operational office", "Signals governance is a strategic function, not a compliance cost"],
                ["GDPR as Global Baseline", "Adopts European consent standards across all markets, even where not legally required", "Builds fan trust globally; reduces patchwork compliance burden"],
                ["CBA Athlete Data Provisions", "Negotiates data rights, consent, and use-limitation directly into player agreements", "Formalizes athlete data sovereignty at the institutional level"],
            ]
        },
        "callout": {
            "type": "green",
            "label": "The Leadership Imperative",
            "body": "Organizations that treat data privacy as a strategic differentiator — not just a legal obligation — are best positioned to build lasting fan trust, protect athlete rights, and unlock the full commercial potential of their data assets."
        }
    },
    {
        "id": "m5",
        "title": "Where the Industry Is Headed",
        "eyebrow": "Module 5 · Future",
        "badge": "badge-gold",
        "badge_label": "Forward-Looking",
        "est": "~10 min read",
        "sections": [
            {
                "heading": "Five Open Frontiers",
                "body": """
The following areas remain actively unresolved — meaning the organizations that move now have a genuine first-mover advantage.
"""
            },
            {
                "heading": "1. Athlete Data Sovereignty",
                "body": """
The co-ownership model — where athletes, clubs, leagues, and vendors share data rights — is gaining traction in legal and academic circles but has not been enacted in any major jurisdiction. Organizations that proactively build co-ownership frameworks will be ahead of the regulatory curve and will build deeper athlete trust.
"""
            },
            {
                "heading": "2. U.S. Federal Privacy Legislation",
                "body": """
Legal experts broadly expect Congress will eventually pass a federal privacy law. When that happens, organizations with mature, GDPR-grade governance programs will adapt quickly. Organizations running patchwork state-by-state compliance will face significant restructuring costs.
"""
            },
            {
                "heading": "3. AI Governance Frameworks",
                "body": """
This is the most urgent near-term frontier. As AI tools proliferate in scouting, content, marketing, and fan engagement, organizations need:
- Algorithmic transparency standards
- Bias auditing workflows
- Data lineage tracking for AI training sets
- AI-specific data retention and deletion policies

The CDO's mandate is actively expanding into AI governance. Most organizations are 2–3 years behind where they need to be.
"""
            },
            {
                "heading": "4. Neurological and Genetic Data",
                "body": """
Brain health and function tracking tools are entering the sports performance market. Several states have already enacted protections for neurological data. Mandatory genetic testing is under consideration by some governing bodies. This is the next category of biometric governance complexity — and the legal frameworks simply do not yet exist.
"""
            },
            {
                "heading": "5. Children's Data in Esports",
                "body": """
Esports has a uniquely high proportion of minor participants. COPPA, GDPR children's provisions, and state laws like New York's Child Data Protection Act (covering minors up to 18) create technically demanding compliance requirements that most platforms have not adequately addressed. Anti-cheating surveillance systems add further complexity.
"""
            },
        ],
        "callout": {
            "type": "accent",
            "label": "Strategic Positioning",
            "body": "The gap between governance leaders and laggards will widen as AI adoption accelerates and regulatory enforcement intensifies. The time to build the foundation is before the regulation forces you to."
        }
    },
]

QUICK_REF = [
    {
        "title": "Governance Vocabulary Cheat Sheet",
        "description": "Key terms to use confidently in executive conversations",
        "icon": "◈",
        "table": {
            "headers": ["Term", "Plain-Language Definition"],
            "rows": [
                ["Data Governance", "The system of policies, roles & processes that control who can do what with data"],
                ["Data Steward", "A business-unit owner responsible for data quality and policy compliance in their domain"],
                ["Data Catalog", "An inventory of all organizational data assets — what exists, where it lives, who owns it"],
                ["Data Lineage", "The documented trail of where data came from, how it was transformed, and where it went"],
                ["CDO", "Chief Data Officer — executive owner of data strategy, governance, and AI readiness"],
                ["DMO", "Data Management Office — operational body that writes and enforces data standards"],
                ["Data Council", "Senior cross-functional body that sets governance strategy and resolves conflicts"],
                ["DPO", "Data Protection Officer — legally required role under GDPR for organizations processing sensitive data"],
                ["GDPR", "EU data privacy regulation — the global gold standard, applies to any org handling EU resident data"],
                ["CCPA", "California Consumer Privacy Act — strongest U.S. state privacy law, often used as a benchmark"],
                ["BIPA", "Illinois Biometric Information Privacy Act — allows private lawsuits, $1–5K per violation"],
                ["Data Classification", "Categorizing data by sensitivity level to determine appropriate access and security controls"],
                ["PII", "Personally Identifiable Information — any data that can identify a specific individual"],
                ["Consent Management", "The system for capturing, storing, and honoring individuals' data use preferences"],
                ["Data Minimization", "Collecting only the data you actually need — a core GDPR principle and governance best practice"],
            ]
        }
    },
    {
        "title": "Regulatory Quick Reference",
        "description": "Know which laws apply and what they require",
        "icon": "⚖",
        "table": {
            "headers": ["Regulation", "Jurisdiction", "What It Covers", "Key Risk"],
            "rows": [
                ["GDPR", "European Union", "All personal data of EU residents", "Up to 4% of global annual revenue"],
                ["CCPA/CPRA", "California", "Consumer data rights & opt-out", "Civil penalties + private right of action"],
                ["BIPA", "Illinois", "Biometric data collection & storage", "$1,000–$5,000 per violation; private lawsuits"],
                ["COPPA", "United States", "Children under 13 online data", "FTC enforcement; up to $51,744/violation"],
                ["HIPAA", "United States", "Health information", "Up to $1.9M per violation category/year"],
                ["LGPD", "Brazil", "Personal data — mirrors GDPR", "Up to 2% of Brazil revenue"],
                ["DPDPA 2023", "India", "Digital personal data", "Up to ₹250 crore (~$30M USD)"],
            ]
        }
    },
    {
        "title": "Governance Maturity Signals",
        "description": "How to assess where your org stands in a conversation",
        "icon": "◎",
        "table": {
            "headers": ["Maturity Level", "What You'll Hear", "What It Means for You"],
            "rows": [
                ["Ad Hoc (Level 1)", "'We handle data issues when they come up'", "No formal governance — highest risk exposure"],
                ["Reactive (Level 2)", "'We have a data team and some policies'", "Governance exists but isn't embedded in operations"],
                ["Defined (Level 3)", "'We have a CDO, DMO, and data standards'", "Structure is in place — execution consistency is the next challenge"],
                ["Managed (Level 4)", "'We measure data quality and track compliance'", "Governance is operational — focus shifts to optimization"],
                ["Optimizing (Level 5)", "'Governance enables our AI and revenue programs'", "Best-in-class — governance is a strategic differentiator"],
            ]
        }
    },
    {
        "title": "The Governance Conversation: What to Ask",
        "description": "Questions that signal executive data literacy",
        "icon": "❓",
        "table": {
            "headers": ["Context", "Question to Ask"],
            "rows": [
                ["New data initiative", "Who is the data owner and what's our legal basis for collecting this?"],
                ["AI/ML project kickoff", "What data are we training on, and has it been governed for this use case?"],
                ["Vendor / tech contract", "What data do they collect, where does it go, and what are our audit rights?"],
                ["Sponsor data deal", "Is the data we're sharing anonymized, and does it comply with our consent framework?"],
                ["Athlete data program", "Do we have explicit consent, or are we relying on employment obligation? Has legal reviewed?"],
                ["Cross-border expansion", "What data transfer mechanisms are in place for this jurisdiction?"],
                ["Data breach / incident", "What was the lineage of the exposed data and what's our notification obligation timeline?"],
                ["Board / investor review", "Can we quantify our data governance maturity and the risk we've mitigated?"],
            ]
        }
    },
]

# ── Sidebar navigation ─────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown('<div class="sidebar-brand">◈ The Data Leader</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Sports & Entertainment Edition</div>', unsafe_allow_html=True)

    # Support CTA buttons on Home jumping to another section
    _nav_options = ["🏠  Home", "📚  Learning Path", "⚡  Quick Reference"]
    if "nav_jump" in st.session_state:
        st.session_state["_nav_radio"] = _nav_options[st.session_state.pop("nav_jump")]

    section = st.radio(
        "",
        _nav_options,
        key="_nav_radio",
        label_visibility="collapsed"
    )

    st.markdown("---")

    if "completed" not in st.session_state:
        st.session_state.completed = set()

    completed_count = len(st.session_state.completed)
    total = len(MODULES)
    st.markdown(f'<p style="font-size:0.75rem; color:#64748b; text-transform:uppercase; letter-spacing:0.08em;">Progress</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:1.1rem; color:#e2e8f0; font-weight:600;">{completed_count} / {total} modules</p>', unsafe_allow_html=True)

    progress_html = '<div class="progress-row">'
    for i in range(total):
        done = f"m{i+1}" in st.session_state.completed
        progress_html += f'<div class="prog-dot {"done" if done else ""}"></div>'
    progress_html += '</div>'
    st.markdown(progress_html, unsafe_allow_html=True)

    if completed_count == total:
        st.markdown('<p style="font-size:0.8rem; color:#22c55e;">✓ All modules complete</p>', unsafe_allow_html=True)

# ── Helper: render a card type ────────────────────────────────────────────────

def render_callout(callout):
    type_map = {"accent": "card-accent", "gold": "card-gold", "green": "card-green", "red": "card-red"}
    cls = type_map.get(callout["type"], "card-accent")
    st.markdown(f"""
    <div class="{cls}">
        <strong style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.08em;">{callout['label']}</strong>
        <p style="margin:0.4rem 0 0; font-size:0.92rem;">{callout['body']}</p>
    </div>
    """, unsafe_allow_html=True)

def render_table(table):
    headers = table["headers"]
    rows = table["rows"]
    html = '<table class="ref-table"><thead><tr>'
    for h in headers:
        html += f'<th>{h}</th>'
    html += '</tr></thead><tbody>'
    for row in rows:
        html += '<tr>'
        for i, cell in enumerate(row):
            weight = 'font-weight:600;' if i == 0 else ''
            html += f'<td style="{weight}">{cell}</td>'
        html += '</tr>'
    html += '</tbody></table>'
    st.markdown(html, unsafe_allow_html=True)

# ── HOME ──────────────────────────────────────────────────────────────────────

if section == "🏠  Home":
    st.markdown('<span class="eyebrow">Sports & Entertainment · Data Governance</span>', unsafe_allow_html=True)
    st.markdown("# The Data Leader")
    st.markdown("### Your executive guide to governing data in the AI era.")
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("""
    <p>This guide is built for one purpose: to help you move from being a successful business leader <em>before</em> data governance mattered at the executive level, to being a leader who shapes how your organization governs, trusts, and monetizes its data assets — with AI on the horizon.</p>

    <p>Everything here is grounded in the sports and entertainment industry. The problems, examples, and vocabulary are specific to your world: athlete biometrics, fan data, sponsorship agreements, CBAs, wearable vendors, and leagues.</p>
    """, unsafe_allow_html=True)

    col_cta1, col_cta2, _ = st.columns([1.6, 1.6, 3])
    with col_cta1:
        if st.button("📚  Start Learning", use_container_width=True, type="primary"):
            st.session_state["nav_jump"] = 1  # Learning Path index
            st.rerun()
    with col_cta2:
        if st.button("⚡  Quick Reference", use_container_width=True):
            st.session_state["nav_jump"] = 2  # Quick Reference index
            st.rerun()

    st.markdown("## What's Inside")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <span class="badge badge-blue">5 Modules</span>
            <h3 style="margin-top:0.8rem;">Learning Path</h3>
            <p>Structured lessons from foundational concepts through culture-building and future frontiers. Read in order or jump to what you need.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <span class="badge badge-gold">4 References</span>
            <h3 style="margin-top:0.8rem;">Quick Reference Cards</h3>
            <p>Vocabulary cheat sheets, regulatory guides, maturity signals, and the right questions to ask in any executive meeting.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Module Overview")
    for mod in MODULES:
        done = mod["id"] in st.session_state.completed
        status = "✓ " if done else ""
        st.markdown(f"""
        <div class="card" style="margin-bottom:0.6rem;">
            <span class="eyebrow">{mod['eyebrow']}</span>
            <strong>{status}{mod['title']}</strong>
            <span style="float:right; font-size:0.8rem; color:var(--muted);">{mod['est']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.8rem; color:var(--muted);">Source: Data Governance & Privacy in Sports and Entertainment, Research Brief, March 2026. Built for personal executive development use only.</p>', unsafe_allow_html=True)

# ── LEARNING PATH ─────────────────────────────────────────────────────────────

elif section == "📚  Learning Path":
    st.markdown('<span class="eyebrow">Learning Path</span>', unsafe_allow_html=True)
    st.markdown("# Modules")
    st.markdown('<hr>', unsafe_allow_html=True)

    module_titles = [f"{m['eyebrow'].split('·')[0].strip()} — {m['title']}" for m in MODULES]
    if "jump_module" in st.session_state:
        st.session_state["_module_select"] = module_titles[st.session_state.pop("jump_module")]

    selected_title = st.selectbox("Select a module", module_titles, key="_module_select", label_visibility="collapsed")
    selected_idx = module_titles.index(selected_title)
    mod = MODULES[selected_idx]

    st.markdown(f'<span class="eyebrow">{mod["eyebrow"]}</span>', unsafe_allow_html=True)
    st.markdown(f'# {mod["title"]}')
    st.markdown(f'<p style="color:var(--muted); font-size:0.85rem;">{mod["est"]}</p>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    for section_data in mod["sections"]:
        st.markdown(f'## {section_data["heading"]}')
        st.markdown(section_data["body"])

    if "table" in mod:
        render_table(mod["table"])

    if "callout" in mod:
        st.markdown("")
        render_callout(mod["callout"])

    st.markdown('<hr>', unsafe_allow_html=True)

    col_a, col_b = st.columns([1, 1])
    with col_a:
        done = mod["id"] in st.session_state.completed
        if not done:
            if st.button("✓ Mark as Complete", key=f"complete_{mod['id']}", use_container_width=True):
                st.session_state.completed.add(mod["id"])
                st.rerun()
        else:
            if st.button("↩ Mark Incomplete", key=f"incomplete_{mod['id']}", use_container_width=True):
                st.session_state.completed.discard(mod["id"])
                st.rerun()

    with col_b:
        if selected_idx < len(MODULES) - 1:
            if st.button(f"Next: {MODULES[selected_idx + 1]['title']} →", use_container_width=True):
                st.session_state["jump_module"] = selected_idx + 1
                st.rerun()

# ── QUICK REFERENCE ──────────────────────────────────────────────────────────

elif section == "⚡  Quick Reference":
    st.markdown('<span class="eyebrow">Quick Reference</span>', unsafe_allow_html=True)
    st.markdown("# Executive Reference Cards")
    st.markdown("Use these before meetings, reviews, or any conversation where data governance will come up.")
    st.markdown('<hr>', unsafe_allow_html=True)

    ref_titles = [f"{r['icon']}  {r['title']}" for r in QUICK_REF]
    selected_ref_title = st.selectbox("Select a reference card", ref_titles, label_visibility="collapsed")
    selected_ref_idx = ref_titles.index(selected_ref_title)
    ref = QUICK_REF[selected_ref_idx]

    st.markdown(f"""
    <div class="cs-banner">
        <h3>{ref['icon']}  {ref['title']}</h3>
        <p>{ref['description']}</p>
    </div>
    """, unsafe_allow_html=True)

    render_table(ref["table"])

    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:0.8rem; color:var(--muted);">These cards are designed for fast recall in executive contexts. Depth is in the Learning Path modules.</p>', unsafe_allow_html=True)
