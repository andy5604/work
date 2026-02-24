from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# Colors (corporate-blue palette)
BG       = RGBColor(0x0a, 0x16, 0x28)
SURFACE  = RGBColor(0x11, 0x20, 0x40)
FG       = RGBColor(0xe8, 0xee, 0xf7)
FG_MUTED = RGBColor(0x94, 0xa3, 0xb8)
ACCENT   = RGBColor(0xf5, 0x9e, 0x0b)
GREEN    = RGBColor(0x4a, 0xde, 0x80)
RED      = RGBColor(0xf8, 0x71, 0x71)

W = Inches(13.33)
H = Inches(7.5)

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H

BLANK = prs.slide_layouts[6]  # completely blank


def add_slide():
    return prs.slides.add_slide(BLANK)


def bg(slide, color=BG):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def txbox(slide, text, x, y, w, h,
          size=18, bold=False, color=FG, align=PP_ALIGN.LEFT,
          italic=False, wrap=True):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    run.font.name = "Calibri"
    return tb


def heading(slide, text, y=Inches(0.4), size=32):
    txbox(slide, text, Inches(0.7), y, Inches(11.9), Inches(0.9),
          size=size, bold=True, color=ACCENT)


def badge(slide, text, y=Inches(0.2)):
    tb = slide.shapes.add_textbox(Inches(0.7), y, Inches(4), Inches(0.4))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = f"  {text}  "
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.color.rgb = BG
    run.font.name = "Calibri"
    # background rect behind it
    from pptx.util import Pt as Pt2
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(0.7), y, Inches(len(text) * 0.085 + 0.3), Inches(0.35)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT
    shape.line.fill.background()
    tf2 = shape.text_frame
    tf2.paragraphs[0].alignment = PP_ALIGN.CENTER
    r2 = tf2.paragraphs[0].add_run()
    r2.text = text.upper()
    r2.font.size = Pt(9)
    r2.font.bold = True
    r2.font.color.rgb = BG
    r2.font.name = "Calibri"


def rect(slide, x, y, w, h, fill=SURFACE, line=None):
    shape = slide.shapes.add_shape(1, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line:
        shape.line.color.rgb = line
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    return shape


def accent_bar(slide, x, y, h=Inches(0.8)):
    """Left accent bar for callout."""
    shape = slide.shapes.add_shape(1, x, y, Inches(0.07), h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT
    shape.line.fill.background()


def callout(slide, text, x, y, w, h):
    rect(slide, x, y, w, h, fill=SURFACE)
    accent_bar(slide, x, y, h)
    txbox(slide, text, x + Inches(0.2), y + Inches(0.1),
          w - Inches(0.25), h - Inches(0.2),
          size=13, color=FG_MUTED, italic=True)


def bullet_list(slide, items, x, y, w, h, size=14, marker_color=ACCENT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.space_before = Pt(4)
        run = p.add_run()
        run.text = f"• {item}"
        run.font.size = Pt(size)
        run.font.color.rgb = FG
        run.font.name = "Calibri"


def two_col_header(slide, left_title, right_title, y=Inches(1.5)):
    txbox(slide, left_title,  Inches(0.7),  y, Inches(5.7), Inches(0.4),
          size=11, bold=True, color=FG_MUTED)
    txbox(slide, right_title, Inches(7.0),  y, Inches(5.7), Inches(0.4),
          size=11, bold=True, color=FG_MUTED)


# ─────────────────────────────────────────────────────────────
# SLIDE 1 — Title
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
txbox(s, "SlackFirst Golden Demo", Inches(0.7), Inches(1.8), Inches(11.9), Inches(1.4),
      size=44, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
txbox(s, "Wrap-Up & Learnings — Dreamforce 2026 Vision",
      Inches(0.7), Inches(3.1), Inches(11.9), Inches(0.7),
      size=20, color=FG_MUTED, align=PP_ALIGN.CENTER)
txbox(s, "Salesforce Slack Design & Cross-Cloud Teams · Oct–Nov 2025",
      Inches(0.7), Inches(3.85), Inches(11.9), Inches(0.5),
      size=13, color=FG_MUTED, align=PP_ALIGN.CENTER)
tags = ["Sales Cloud", "Marketing Cloud", "Service Cloud", "AgentForce", "Agentic OS"]
tag_x = Inches(2.5)
for t in tags:
    w = Inches(len(t) * 0.1 + 0.4)
    shape = s.shapes.add_shape(1, tag_x, Inches(4.7), w, Inches(0.35))
    shape.fill.solid(); shape.fill.fore_color.rgb = SURFACE
    shape.line.color.rgb = ACCENT; shape.line.width = Pt(1)
    tf2 = shape.text_frame; tf2.paragraphs[0].alignment = PP_ALIGN.CENTER
    r2 = tf2.paragraphs[0].add_run(); r2.text = t
    r2.font.size = Pt(10); r2.font.color.rgb = ACCENT; r2.font.name = "Calibri"
    tag_x += w + Inches(0.15)

# ─────────────────────────────────────────────────────────────
# SLIDE 2 — What Is the Golden Demo?
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
heading(s, "What Is the Golden Demo?")
two_col_header(s, "ORIGIN", "THE VISION")
txbox(s, "Requested directly by Marc Benioff after seeing three separate SlackFirst demos at the Hawaii offsite. He wanted a single unified vision projecting 12–18 months ahead to Dreamforce 2026.",
      Inches(0.7), Inches(1.9), Inches(5.7), Inches(2.2), size=14, color=FG)
txbox(s, "Slack as the Agentic OS for the enterprise — AgentForce, Slack, and third-party agents connected in a single cross-cloud story, all rooted in user research.",
      Inches(7.0), Inches(1.9), Inches(5.7), Inches(2.2), size=14, color=FG)
callout(s, "Safe harbor: This is an exploratory prototype. Nothing featured is on the product roadmap (yet) or representative of final UI.",
        Inches(0.7), Inches(4.4), Inches(11.9), Inches(0.85))

# ─────────────────────────────────────────────────────────────
# SLIDE 3 — Agenda
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
heading(s, "Today's Agenda")
cards = [
    ("Part 1 · By Cloud",    ["SlackFirst Sales", "SlackFirst Marketing", "SlackFirst Service"]),
    ("Part 2 · Capabilities",["Platform primitives", "Agentic OS big rocks"]),
    ("Part 3 · Process",     ["Research & learnings", "What's next"]),
]
cx = Inches(0.7)
for title, items in cards:
    rect(s, cx, Inches(1.6), Inches(3.8), Inches(3.8), fill=SURFACE)
    txbox(s, title, cx + Inches(0.2), Inches(1.7), Inches(3.4), Inches(0.5),
          size=14, bold=True, color=ACCENT)
    bullet_list(s, items, cx + Inches(0.2), Inches(2.3), Inches(3.4), Inches(2.8), size=13)
    cx += Inches(4.1)

# ─────────────────────────────────────────────────────────────
# SLIDE 4 — Sales Overview
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
badge(s, "Sales Cloud")
heading(s, "SlackFirst Sales", y=Inches(0.65))
txbox(s, "Follow an Account Executive working a deal to close — using AI to automate updates, gather quotes, get approvals, and turn meetings into action.",
      Inches(0.7), Inches(1.45), Inches(11.9), Inches(0.7), size=14, color=FG_MUTED)
two_col_header(s, "KEY CAPABILITIES", "CORE INSIGHT", y=Inches(2.15))
bullet_list(s, [
    "Slack Voice Mode for seamless communication",
    "Rich agent interactions & recommendations",
    "Ambient Intelligence + meeting recaps",
    "Approvals with AI context",
    "Tableau metrics integration",
], Inches(0.7), Inches(2.5), Inches(5.7), Inches(3.2), size=13)
callout(s, '"Speed is everything for sellers. The more we smartly automate — updating Salesforce, gathering quotes, getting approvals — the more they can focus on closing."',
        Inches(7.0), Inches(2.5), Inches(5.7), Inches(1.6))

# ─────────────────────────────────────────────────────────────
# SLIDE 5 — Sales Quotes
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
badge(s, "Sales Cloud · Research Voices")
heading(s, "What Sellers Actually Need", y=Inches(0.65))
callout(s, '"One of my biggest gripes is updating Salesforce hygiene. In a perfect world: \'Push all opportunities with close dates in the next 7 days out by two weeks.\' That would be the biggest use case."',
        Inches(0.7), Inches(1.5), Inches(11.9), Inches(1.3))
callout(s, '"Can it create the opportunity Slack channel and pull the meeting together? Otherwise it\'s 20 min of finding time on people\'s calendars."',
        Inches(0.7), Inches(2.95), Inches(11.9), Inches(1.1))
callout(s, '"A meeting can have 10–12 different tasks... it doesn\'t trigger actions or next steps. [This AI solution] would make the process more agile for the whole team."',
        Inches(0.7), Inches(4.2), Inches(11.9), Inches(1.1))

# ─────────────────────────────────────────────────────────────
# SLIDE 6 — Marketing Overview
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
badge(s, "Marketing Cloud")
heading(s, "SlackFirst Marketing", y=Inches(0.65))
txbox(s, "Follow a marketing manager through campaign brief creation and launch — eliminating scattered knowledge, misaligned stakeholders, and siloed data.",
      Inches(0.7), Inches(1.45), Inches(11.9), Inches(0.7), size=14, color=FG_MUTED)
two_col_header(s, "KEY CAPABILITIES", "CORE INSIGHT", y=Inches(2.15))
bullet_list(s, [
    "Agentic Deep Research for market insights",
    "Agentic Campaign Creation with AI",
    "Integrated Analytics in Slack workflows",
    "Seamless Handoff to Salesforce",
    "Multi-player Agent Experience",
], Inches(0.7), Inches(2.5), Inches(5.7), Inches(3.2), size=13)
callout(s, '"Updating all the different documents, spreadsheets, trackers — everybody has to review that, and then there are 500 variations. It\'s just a lot of tactical work."',
        Inches(7.0), Inches(2.5), Inches(5.7), Inches(1.6))

# ─────────────────────────────────────────────────────────────
# SLIDE 7 — Marketing Quotes
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
badge(s, "Marketing Cloud · Research Voices")
heading(s, "What Marketers Actually Need", y=Inches(0.65))
callout(s, '"The things that take up the most time are creating the brief and getting approvals."',
        Inches(0.7), Inches(1.5), Inches(11.9), Inches(1.0))
callout(s, '"If there\'s a way that it\'s not just a screenshot — and there was an easy way to prompt Slack to go pull something from Tableau and put it in the chat so we could both reference it, that\'d be cool."',
        Inches(0.7), Inches(2.65), Inches(11.9), Inches(1.2))
callout(s, '"I want to see how many customers received a specific campaign... it\'s hard to keep track and I wish the data was more self-serve."',
        Inches(0.7), Inches(4.0), Inches(11.9), Inches(1.1))

# ─────────────────────────────────────────────────────────────
# SLIDE 8 — Service Overview
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
badge(s, "Service Cloud")
heading(s, "SlackFirst Service", y=Inches(0.65))
txbox(s, "Follow a Service Rep through a customer call — starting a swarm, finding experts, and resolving a case while supervisors monitor service quality in real time.",
      Inches(0.7), Inches(1.45), Inches(11.9), Inches(0.7), size=14, color=FG_MUTED)
two_col_header(s, "KEY CAPABILITIES", "CORE INSIGHT", y=Inches(2.15))
bullet_list(s, [
    "Ask Anything for instant information access",
    "Ambient Intelligence during customer calls",
    "In-swarm Expert Finder",
    "Service Supervisor workflow integration",
    "Agentic knowledge updates",
], Inches(0.7), Inches(2.5), Inches(5.7), Inches(3.2), size=13)
callout(s, '"There\'s a lot of noise in escalation channels. Just summarizing — \'here were 3 incidents, here\'s what you need to know\' — while cutting out all the back and forth."',
        Inches(7.0), Inches(2.5), Inches(5.7), Inches(1.6))

# ─────────────────────────────────────────────────────────────
# SLIDE 9 — Service Quotes
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
badge(s, "Service Cloud · Research Voices")
heading(s, "What Service Teams Actually Need", y=Inches(0.65))
callout(s, '"If during a call, AI is able to pull from a knowledge base... someone\'s asking about shipping time frames and it\'s just not on the top of your head. It would be nice to have something pull that in."',
        Inches(0.7), Inches(1.5), Inches(11.9), Inches(1.2))
callout(s, '"That\'s always a struggle — making sure things are moving along and that someone didn\'t miss something, or that a lot of attention is being given to something low-priority."',
        Inches(0.7), Inches(2.85), Inches(11.9), Inches(1.1))
callout(s, '"\'Why did this number drop?\' — Getting that answer quickly is usually very important."',
        Inches(0.7), Inches(4.1), Inches(11.9), Inches(0.9))

# ─────────────────────────────────────────────────────────────
# SLIDE 10 — Platform Primitives
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
heading(s, "Platform Capabilities & Primitives")
txbox(s, "Native Slack capabilities woven throughout all three cloud vignettes",
      Inches(0.7), Inches(1.35), Inches(11.9), Inches(0.4), size=13, color=FG_MUTED)
two_col_header(s, "STARTING NOW", "AGENTIC OS BIG ROCKS", y=Inches(1.75))
bullet_list(s, [
    "Today View — Focused place to start your day",
    "Task Management — Central agent/task/to-do hub",
    "Approvals — Salesforce notifications & workflow",
    "Email — Downmarket composition",
    "Meetings + Calendar — Slack ↔ Salesforce sync",
    "Rich Agentic Interactivity — CRM updates & record creation",
], Inches(0.7), Inches(2.1), Inches(5.7), Inches(4.0), size=13)
bullet_list(s, [
    "Agent Orchestration — Single interface for multiple AI agents",
    "Ambient Intelligence — Real-time listening, transcription, action items",
    "Agent & AppExchange — Marketplace for agents & workflows",
], Inches(7.0), Inches(2.1), Inches(5.7), Inches(3.0), size=13)

# ─────────────────────────────────────────────────────────────
# SLIDE 11 — Research Learnings
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
heading(s, "Broad Research Themes & Learnings")
items = [
    "Lean into SlackFirst advantages. Deep context, everything in one place, immediate action.",
    "Think holistically about use cases. Meetings are high-leverage: before, during, and after. Solve the 'work of work.'",
    "Ambient AI felt novel. Make behavior configurable — show when AI is listening; allow hiding when screen-sharing.",
    "Build trust over time. Start with humans in the loop; give tools for feedback and configuration.",
    "Noise & channel sprawl reduce Slack's value. Be thoughtful about when channels/notifications are created.",
]
y = Inches(1.5)
for item in items:
    callout(s, item, Inches(0.7), y, Inches(11.9), Inches(0.9))
    y += Inches(1.0)

# ─────────────────────────────────────────────────────────────
# SLIDE 12 — What It Is / Isn't
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
heading(s, "What the Golden Demo Is (and Isn't)")
txbox(s, "What It Is  ✓", Inches(0.7), Inches(1.5), Inches(5.7), Inches(0.45),
      size=15, bold=True, color=GREEN)
txbox(s, "What It's Not  ✕", Inches(7.0), Inches(1.5), Inches(5.7), Inches(0.45),
      size=15, bold=True, color=RED)
bullet_list(s, [
    "Forward-looking Figma prototype for DF2026",
    "Conversational, agentic-first, AI-powered",
    "AgentForce + Slack + 3rd-party agents cross-cloud",
    "Slack as the Agentic OS — three distinct vignettes",
    "Rooted in real user research",
], Inches(0.7), Inches(2.0), Inches(5.7), Inches(4.0), size=13)
bullet_list(s, [
    "Not a locked commitment or product roadmap",
    "Not replacing Solutions CoE Golden Demos",
    "Not focused on complex document creation",
    "Not just product walkthroughs",
], Inches(7.0), Inches(2.0), Inches(5.7), Inches(3.5), size=13)

# fix red bullets
for shape in s.shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            for run in para.runs:
                if run.text.startswith("• Not"):
                    run.font.color.rgb = RED

# ─────────────────────────────────────────────────────────────
# SLIDE 13 — What's Next
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
heading(s, "What's Next")
two_col_header(s, "SOCIALIZING WITH SALESFORCE", "GET INVOLVED", y=Inches(1.5))
bullet_list(s, [
    "Service Cloud integration for contact centers",
    "ITSM evolution within Slack",
    "Cloud-specific SlackFirst app vision consultations",
    "V2MOM development for joint SlackFirst FY27 program",
], Inches(0.7), Inches(1.9), Inches(5.7), Inches(3.0), size=14)
bullet_list(s, [
    "#temp-slack-first-golden-demo — Primary channel",
    "#golden-demo-research-sessions — Research",
    "Golden Demo Dream Team doc for stakeholders",
], Inches(7.0), Inches(1.9), Inches(5.7), Inches(2.5), size=14)
callout(s, "Questions? Reach out in the project channels or connect with the Slack Design & Cross-Cloud teams directly.",
        Inches(7.0), Inches(4.5), Inches(5.7), Inches(1.0))

# ─────────────────────────────────────────────────────────────
# SLIDE 14 — Thank You
# ─────────────────────────────────────────────────────────────
s = add_slide(); bg(s)
txbox(s, "Thank You", Inches(0.7), Inches(1.8), Inches(11.9), Inches(1.4),
      size=52, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
txbox(s, "Slack as the Agentic OS for the Enterprise",
      Inches(0.7), Inches(3.1), Inches(11.9), Inches(0.7),
      size=20, color=FG_MUTED, align=PP_ALIGN.CENTER)
txbox(s, "Questions & Discussion",
      Inches(0.7), Inches(4.0), Inches(11.9), Inches(0.5),
      size=14, color=FG_MUTED, align=PP_ALIGN.CENTER)
tags2 = ["Sales Cloud", "Marketing Cloud", "Service Cloud", "Data Cloud", "AgentForce", "Tableau"]
tx = Inches(1.3)
for t in tags2:
    w = Inches(len(t) * 0.1 + 0.4)
    shape = s.shapes.add_shape(1, tx, Inches(5.0), w, Inches(0.35))
    shape.fill.solid(); shape.fill.fore_color.rgb = SURFACE
    shape.line.color.rgb = ACCENT; shape.line.width = Pt(1)
    tf2 = shape.text_frame; tf2.paragraphs[0].alignment = PP_ALIGN.CENTER
    r2 = tf2.paragraphs[0].add_run(); r2.text = t
    r2.font.size = Pt(10); r2.font.color.rgb = ACCENT; r2.font.name = "Calibri"
    tx += w + Inches(0.15)

prs.save("/home/user/work/SlackFirst_Golden_Demo.pptx")
print("Saved: SlackFirst_Golden_Demo.pptx")
