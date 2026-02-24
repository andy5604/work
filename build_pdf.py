from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus.flowables import KeepTogether, PageBreak

PAGE = landscape(A4)
W, H = PAGE

# Colors
BG       = colors.HexColor("#0a1628")
SURFACE  = colors.HexColor("#112040")
FG       = colors.HexColor("#e8eef7")
FG_MUTED = colors.HexColor("#94a3b8")
ACCENT   = colors.HexColor("#f59e0b")
GREEN    = colors.HexColor("#4ade80")
RED      = colors.HexColor("#f87171")
WHITE    = colors.white

def style(name, size=12, color=FG, bold=False, align=TA_LEFT, leading=None, space_before=0, space_after=4):
    return ParagraphStyle(
        name,
        fontSize=size,
        textColor=color,
        fontName="Helvetica-Bold" if bold else "Helvetica",
        alignment=align,
        leading=leading or size * 1.4,
        spaceBefore=space_before,
        spaceAfter=space_after,
        wordWrap='CJK',
    )

S_TITLE    = style("title",    size=36, color=ACCENT, bold=True, align=TA_CENTER, leading=42)
S_SUBTITLE = style("subtitle", size=16, color=FG_MUTED, align=TA_CENTER)
S_META     = style("meta",     size=11, color=FG_MUTED, align=TA_CENTER)
S_H2       = style("h2",       size=22, color=ACCENT, bold=True, leading=28, space_before=4, space_after=8)
S_H3       = style("h3",       size=10, color=FG_MUTED, bold=True, space_before=6, space_after=4)
S_BODY     = style("body",     size=12, color=FG, leading=17)
S_SMALL    = style("small",    size=11, color=FG, leading=16)
S_QUOTE    = style("quote",    size=11, color=FG_MUTED, leading=16)
S_BADGE    = style("badge",    size=9,  color=BG, bold=True, align=TA_CENTER)
S_CENTER   = style("center",   size=12, color=FG, align=TA_CENTER)
S_GREEN    = style("green",    size=13, color=GREEN, bold=True)
S_RED      = style("red",      size=13, color=RED,   bold=True)

def bullet(text, s=S_SMALL):
    return Paragraph(f"<bullet>\u2022</bullet> {text}", s)

def callout_table(text, width=None):
    w = width or (W - 2*inch)
    p = Paragraph(text, S_QUOTE)
    t = Table([[p]], colWidths=[w - 0.3*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), SURFACE),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING",(0,0), (-1,-1), 10),
        ("TOPPADDING",  (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
        ("LINEAFTER",   (0,0), (0,-1), 0, WHITE),  # placeholder
    ]))
    # accent left border via outer table
    inner = Table([[" ", t]], colWidths=[0.08*inch, w - 0.08*inch])
    inner.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (0,-1), ACCENT),
        ("BACKGROUND",  (1,0), (1,-1), SURFACE),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING",(0,0), (-1,-1), 0),
        ("TOPPADDING",  (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
        ("VALIGN",      (0,0), (-1,-1), "TOP"),
    ]))
    return inner

def two_col(left_items, right_items, left_title="", right_title="", col_w=None):
    cw = col_w or ((W - 2*inch - 0.4*inch) / 2)
    left_cell = []
    if left_title:
        left_cell.append(Paragraph(left_title, S_H3))
    left_cell.extend(left_items)
    right_cell = []
    if right_title:
        right_cell.append(Paragraph(right_title, S_H3))
    right_cell.extend(right_items)
    t = Table([[left_cell, right_cell]], colWidths=[cw, cw])
    t.setStyle(TableStyle([
        ("VALIGN",      (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING",(0,0), (-1,-1), 6),
        ("TOPPADDING",  (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    return t

def badge_para(text):
    t = Table([[Paragraph(text.upper(), S_BADGE)]], colWidths=[2.2*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), ACCENT),
        ("TOPPADDING",  (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING",(0,0), (-1,-1), 8),
    ]))
    return t

def section_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # progress bar (accent line at top)
    canvas.restoreState()

# Build story
story = []

def slide_break():
    story.append(PageBreak())

# ── SLIDE 1: Title ──────────────────────────────────────────
story += [
    Spacer(1, 1.2*inch),
    badge_para("Internal · Oct–Nov 2025"),
    Spacer(1, 0.2*inch),
    Paragraph("SlackFirst Golden Demo", S_TITLE),
    Spacer(1, 0.15*inch),
    Paragraph("Wrap-Up &amp; Learnings — Dreamforce 2026 Vision", S_SUBTITLE),
    Spacer(1, 0.1*inch),
    Paragraph("Salesforce Slack Design &amp; Cross-Cloud Teams", S_META),
    Spacer(1, 0.3*inch),
    Paragraph("Sales Cloud  ·  Marketing Cloud  ·  Service Cloud  ·  AgentForce  ·  Agentic OS", S_META),
]
slide_break()

# ── SLIDE 2: What Is It ─────────────────────────────────────
story += [
    Paragraph("What Is the Golden Demo?", S_H2),
    Spacer(1, 0.1*inch),
    two_col(
        [Paragraph("Requested directly by <b>Marc Benioff</b> after seeing three separate SlackFirst demos at the Hawaii offsite. He wanted a single unified vision projecting <b>12–18 months ahead</b> to Dreamforce 2026.", S_SMALL)],
        [Paragraph("<b>Slack as the Agentic OS for the enterprise</b> — AgentForce, Slack, and third-party agents connected in a single cross-cloud story, all rooted in user research.", S_SMALL)],
        left_title="ORIGIN", right_title="THE VISION",
    ),
    Spacer(1, 0.2*inch),
    callout_table("<i>Safe harbor: This is an exploratory prototype. Nothing featured is on the product roadmap (yet) or representative of final UI.</i>"),
]
slide_break()

# ── SLIDE 3: Agenda ─────────────────────────────────────────
story += [
    Paragraph("Today's Agenda", S_H2),
    Spacer(1, 0.15*inch),
]
cw = (W - 2*inch - 0.4*inch) / 3
def card(title, items):
    cell = [Paragraph(title, style("ct", size=12, color=ACCENT, bold=True))]
    for i in items:
        cell.append(bullet(i, S_SMALL))
    t = Table([[cell]], colWidths=[cw - 0.2*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), SURFACE),
        ("TOPPADDING",  (0,0), (-1,-1), 10),
        ("BOTTOMPADDING",(0,0),(-1,-1),10),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING",(0,0), (-1,-1), 10),
    ]))
    return t
agenda = Table([[
    card("Part 1 · By Cloud",     ["SlackFirst Sales", "SlackFirst Marketing", "SlackFirst Service"]),
    card("Part 2 · Capabilities", ["Platform primitives", "Agentic OS big rocks"]),
    card("Part 3 · Process",      ["Research & learnings", "What's next"]),
]], colWidths=[cw, cw, cw])
agenda.setStyle(TableStyle([
    ("VALIGN",      (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING",(0,0), (-1,-1), 8),
    ("TOPPADDING",  (0,0), (-1,-1), 0),
    ("BOTTOMPADDING",(0,0),(-1,-1),0),
]))
story.append(agenda)
slide_break()

# ── SLIDE 4: Sales Overview ─────────────────────────────────
story += [
    badge_para("Sales Cloud"),
    Spacer(1, 0.1*inch),
    Paragraph("SlackFirst Sales", S_H2),
    Paragraph("Follow an Account Executive working a deal to close — using AI to automate updates, gather quotes, get approvals, and turn meetings into action.", S_SMALL),
    Spacer(1, 0.15*inch),
    two_col(
        [Paragraph("KEY CAPABILITIES", S_H3),
         bullet("Slack Voice Mode for seamless communication"),
         bullet("Rich agent interactions &amp; recommendations"),
         bullet("Ambient Intelligence + meeting recaps"),
         bullet("Approvals with AI context"),
         bullet("Tableau metrics integration")],
        [Paragraph("CORE INSIGHT", S_H3),
         callout_table('"Speed is everything for sellers. The more we smartly automate — updating Salesforce, gathering quotes, getting approvals — the more they can focus on <b>closing</b>."',
                       width=(W - 2*inch - 0.4*inch)/2)],
    ),
]
slide_break()

# ── SLIDE 5: Sales Quotes ───────────────────────────────────
story += [
    badge_para("Sales Cloud · Research Voices"),
    Spacer(1, 0.1*inch),
    Paragraph("What Sellers Actually Need", S_H2),
    callout_table('"One of my biggest gripes is updating Salesforce hygiene. In a perfect world: <b>\'Push all opportunities with close dates in the next 7 days out by two weeks.\'</b> That would be the biggest use case."'),
    Spacer(1, 0.1*inch),
    callout_table('"Can it create the opportunity Slack channel and pull the meeting together? <b>Otherwise it\'s 20 min of finding time on people\'s calendars.</b>"'),
    Spacer(1, 0.1*inch),
    callout_table('"A meeting can have 10–12 different tasks... <b>it doesn\'t trigger actions or next steps.</b> [This AI solution] would make the process more agile for the whole team."'),
]
slide_break()

# ── SLIDE 6: Marketing Overview ────────────────────────────
story += [
    badge_para("Marketing Cloud"),
    Spacer(1, 0.1*inch),
    Paragraph("SlackFirst Marketing", S_H2),
    Paragraph("Follow a marketing manager through campaign brief creation and launch — eliminating scattered knowledge, misaligned stakeholders, and siloed data.", S_SMALL),
    Spacer(1, 0.15*inch),
    two_col(
        [Paragraph("KEY CAPABILITIES", S_H3),
         bullet("Agentic Deep Research for market insights"),
         bullet("Agentic Campaign Creation with AI"),
         bullet("Integrated Analytics in Slack workflows"),
         bullet("Seamless Handoff to Salesforce"),
         bullet("Multi-player Agent Experience")],
        [Paragraph("CORE INSIGHT", S_H3),
         callout_table('"Updating all the different documents, spreadsheets, trackers — everybody has to review that, and then there are <b>500 variations.</b> It\'s just a lot of tactical work."',
                       width=(W - 2*inch - 0.4*inch)/2)],
    ),
]
slide_break()

# ── SLIDE 7: Marketing Quotes ───────────────────────────────
story += [
    badge_para("Marketing Cloud · Research Voices"),
    Spacer(1, 0.1*inch),
    Paragraph("What Marketers Actually Need", S_H2),
    callout_table('"The things that take up the most time are <b>creating the brief and getting approvals.</b>"'),
    Spacer(1, 0.1*inch),
    callout_table('"If there\'s a way that it\'s not just a screenshot — and there was an easy way to <b>prompt Slack to go pull something from Tableau and put it in the chat</b> so we could both reference it, that\'d be cool."'),
    Spacer(1, 0.1*inch),
    callout_table('"I want to see how many customers received a specific campaign... <b>it\'s hard to keep track and I wish the data was more self-serve.</b>"'),
]
slide_break()

# ── SLIDE 8: Service Overview ───────────────────────────────
story += [
    badge_para("Service Cloud"),
    Spacer(1, 0.1*inch),
    Paragraph("SlackFirst Service", S_H2),
    Paragraph("Follow a Service Rep through a customer call — starting a swarm, finding experts, and resolving a case while supervisors monitor quality in real time.", S_SMALL),
    Spacer(1, 0.15*inch),
    two_col(
        [Paragraph("KEY CAPABILITIES", S_H3),
         bullet("Ask Anything for instant information access"),
         bullet("Ambient Intelligence during customer calls"),
         bullet("In-swarm Expert Finder"),
         bullet("Service Supervisor workflow integration"),
         bullet("Agentic knowledge updates")],
        [Paragraph("CORE INSIGHT", S_H3),
         callout_table('"There\'s a lot of noise in escalation channels. Just summarizing — <b>\'here were 3 incidents, here\'s what you need to know\'</b> — while cutting out all the back and forth."',
                       width=(W - 2*inch - 0.4*inch)/2)],
    ),
]
slide_break()

# ── SLIDE 9: Service Quotes ─────────────────────────────────
story += [
    badge_para("Service Cloud · Research Voices"),
    Spacer(1, 0.1*inch),
    Paragraph("What Service Teams Actually Need", S_H2),
    callout_table('"If during a call, AI is able to pull from a knowledge base... someone\'s asking about shipping time frames and <b>it\'s just not on the top of your head.</b> It would be nice to have something pull that in."'),
    Spacer(1, 0.1*inch),
    callout_table('"That\'s always a struggle — making sure things are moving along and that someone <b>didn\'t miss something, or that a lot of attention is being given to something low-priority.</b>"'),
    Spacer(1, 0.1*inch),
    callout_table('"\'Why did this number drop?\' — <b>Getting that answer quickly is usually very important.</b>"'),
]
slide_break()

# ── SLIDE 10: Platform Primitives ──────────────────────────
story += [
    Paragraph("Platform Capabilities &amp; Primitives", S_H2),
    Paragraph("Native Slack capabilities woven throughout all three cloud vignettes", S_SMALL),
    Spacer(1, 0.15*inch),
    two_col(
        [Paragraph("STARTING NOW", S_H3),
         bullet("<b>Today View</b> — Focused place to start your day"),
         bullet("<b>Task Management</b> — Central agent/task/to-do hub"),
         bullet("<b>Approvals</b> — Salesforce notifications &amp; workflow"),
         bullet("<b>Email</b> — Downmarket composition"),
         bullet("<b>Meetings + Calendar</b> — Slack ↔ Salesforce sync"),
         bullet("<b>Rich Agentic Interactivity</b> — CRM updates &amp; record creation")],
        [Paragraph("AGENTIC OS BIG ROCKS", S_H3),
         bullet("<b>Agent Orchestration</b> — Single interface for multiple AI agents"),
         bullet("<b>Ambient Intelligence</b> — Real-time listening, transcription, action items"),
         bullet("<b>Agent &amp; AppExchange</b> — Marketplace for agents &amp; workflows")],
    ),
]
slide_break()

# ── SLIDE 11: Research Learnings ───────────────────────────
story += [
    Paragraph("Broad Research Themes &amp; Learnings", S_H2),
    callout_table("<b>Lean into SlackFirst advantages.</b> Deep context, everything in one place, immediate action — these are Slack's native strengths."),
    Spacer(1, 0.08*inch),
    callout_table("<b>Think holistically about use cases.</b> Meetings are high-leverage: before, during, and after. Seamless end-to-end solves the 'work of work.'"),
    Spacer(1, 0.08*inch),
    callout_table("<b>Ambient AI felt novel.</b> Make behavior configurable — show when AI is listening; allow hiding when screen-sharing with customers."),
    Spacer(1, 0.08*inch),
    callout_table("<b>Build trust over time.</b> Users are skeptical from prior AI experiences. Start with humans in the loop; give tools for feedback and configuration."),
    Spacer(1, 0.08*inch),
    callout_table("<b>Noise &amp; channel sprawl reduce Slack's value.</b> Be thoughtful about when channels/notifications are created — smartly archive when appropriate."),
]
slide_break()

# ── SLIDE 12: What It Is / Isn't ───────────────────────────
story += [
    Paragraph("What the Golden Demo Is (and Isn't)", S_H2),
    Spacer(1, 0.1*inch),
    two_col(
        [Paragraph("What It Is  ✓", S_GREEN),
         Spacer(1, 0.05*inch),
         bullet("Forward-looking Figma prototype for Dreamforce 2026"),
         bullet("Conversational, agentic-first, AI-powered"),
         bullet("AgentForce + Slack + 3rd-party agents cross-cloud"),
         bullet("Slack as the Agentic OS — three distinct vignettes"),
         bullet("Rooted in real user research")],
        [Paragraph("What It's Not  ✕", S_RED),
         Spacer(1, 0.05*inch),
         bullet("Not a locked commitment or product roadmap"),
         bullet("Not replacing Solutions CoE Golden Demos"),
         bullet("Not focused on complex document creation"),
         bullet("Not just product walkthroughs")],
    ),
]
slide_break()

# ── SLIDE 13: What's Next ───────────────────────────────────
story += [
    Paragraph("What's Next", S_H2),
    Spacer(1, 0.1*inch),
    two_col(
        [Paragraph("SOCIALIZING WITH SALESFORCE", S_H3),
         bullet("Service Cloud integration for contact centers"),
         bullet("ITSM evolution within Slack"),
         bullet("Cloud-specific SlackFirst app vision consultations"),
         bullet("V2MOM development for joint SlackFirst FY27 program")],
        [Paragraph("GET INVOLVED", S_H3),
         bullet("<b>#temp-slack-first-golden-demo</b> — Primary channel"),
         bullet("<b>#golden-demo-research-sessions</b> — Research"),
         bullet("Golden Demo Dream Team doc for stakeholders"),
         Spacer(1, 0.1*inch),
         callout_table("Questions? Reach out in the project channels or connect with the Slack Design &amp; Cross-Cloud teams.",
                       width=(W - 2*inch - 0.4*inch)/2)],
    ),
]
slide_break()

# ── SLIDE 14: Thank You ─────────────────────────────────────
story += [
    Spacer(1, 1.0*inch),
    Paragraph("Thank You", S_TITLE),
    Spacer(1, 0.2*inch),
    Paragraph("Slack as the Agentic OS for the Enterprise", S_SUBTITLE),
    Spacer(1, 0.15*inch),
    Paragraph("Questions &amp; Discussion", S_META),
    Spacer(1, 0.3*inch),
    Paragraph("Sales Cloud  ·  Marketing Cloud  ·  Service Cloud  ·  Data Cloud  ·  AgentForce  ·  Tableau", S_META),
]

# ── Build PDF ───────────────────────────────────────────────
doc = SimpleDocTemplate(
    "/home/user/work/SlackFirst_Golden_Demo.pdf",
    pagesize=PAGE,
    leftMargin=inch, rightMargin=inch,
    topMargin=0.6*inch, bottomMargin=0.5*inch,
)

def draw_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # top accent line
    canvas.setFillColor(ACCENT)
    canvas.rect(0, H - 3, W, 3, fill=1, stroke=0)
    # page number
    page_num = doc.page
    canvas.setFillColor(FG_MUTED)
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(W - 0.4*inch, 0.25*inch, f"{page_num} / 14")
    canvas.restoreState()

doc.build(story, onFirstPage=draw_bg, onLaterPages=draw_bg)
print("Saved: SlackFirst_Golden_Demo.pdf")
