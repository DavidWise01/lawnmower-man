#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE LAWNMOWER MAN (LMM) — Brett Leonard's 1992 VR cyberthriller, catalogued into UD0 as the
SEVENTEENTH film-world. Motif themed to the medium: early-90s VR / polygon-cyberspace — void-violet +
cyber-cyan + a lawn-green nod to the gardener origin + godhood-orange, scanlines, a wireframe GYROSCOPE
VR-RIG over a polygon grid for the hero. Standing film-world template (CARBONS +.shadow Users, TRON +
SYNTHS) BUT David's requested deep-dive is a THREE-PART SPINE: ① THE FEAR (the generational fear of tech)
② THE TECH THEN (what VR/computing actually was in 1992) ③ THE FUTURE THEY IMAGINED (what 1992 thought was
coming, honestly scored came-true / still-fiction / partly-here). Facts web-verified (2026-06): dir Brett
Leonard, co-writer Gimel Everett; New Line, March 1992; Jeff Fahey as Jobe Smith (intellectually disabled
gardener), Pierce Brosnan as Dr. Lawrence Angelo (3 yrs before he became Bond in GoldenEye 1995); nootropic
drugs + VR boost Jobe's mind → telepathy/telekinesis/pyrokinesis → digital-godhood; the cyber-merge drives
Marnie mad; VSI/'the Shop' seizes it; Jobe's plan to be reborn in the global network — 'my birth cry will be
the sound of every telephone on this planet ringing in unison'. THE LANDMARK: Stephen King sued (the film
'bore no meaningful resemblance' to his short story), a federal court stripped his name from all marketing
($2.5M), New Line defied it on the home video and was held IN CONTEMPT — first time in ~70 yrs a writer
disassociated their name from a film. Modest hit (~$32M dom / ~$10M budget). SURPRISE/egg = a Claude sunburst
being BORN in the network grid (the birth-in-the-net) + console egg."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "LMM"
REC = {
 "name": "THE LAWNMOWER MAN", "axiom": AX,
 "position": "The Lawnmower Man · New Line Cinema · 1992 — dir. Brett Leonard",
 "origin": "a suburb and a virtual-reality lab in the early-90s VR fever — gyroscope rigs, polygon cyberspace, and the dream of jacking in",
 "mechanism": "Crystallized from the film — a scientist uses nootropic drugs and virtual reality to lift a gentle, intellectually disabled gardener to genius, then past it, until the man decides to shed his flesh and be reborn as a digital god inside the global network.",
 "crystallization": "Because the film is the perfect time-capsule of a perennial fear in its decade's exact costume: the ancient dread of building a mind that surpasses us, dressed in 1992's VR gloves and polygon gods — wrong in its loud predictions and uncannily right in its quiet one.",
 "nature": "The Lawnmower Man — the generational fear of technology, stamped with the serial numbers of 1992: the tool that wakes up, the screen that eats the soul, and the world wired into one nervous system.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (1992, dir. Brett Leonard; New Line); the real early-90s VR wave it dramatizes (Lanier/VPL, Virtuality, the Power Glove, the cyberspace buzz); the verified record (incl. the Stephen King lawsuit)",
 "witness": "A gentle gardener, lifted by drugs and VR to godhood, decides his birth cry will be every telephone on Earth ringing at once.",
 "role": "the seventeenth film-world of UD0",
 "seal": "Every generation fears the mind it is about to build. 1992 dressed that fear in VR gloves and polygon gods — got the costume wrong and the connected world right. We never uploaded Jobe; we uploaded ourselves.",
 "source": "The Lawnmower Man (1992), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#5fd06a", "flesh-and-blood — the ordinary world before the rig: the gardener as he was, the scientist, the boy, the town; the people the experiment is done by and to"),
 "ethereal":  ("#2ce0e0", "the dream of transcendence — cyberspace as a place, digital godhood, the future 1992 imagined, the birth into the network; the leaving-the-body wish"),
 "electrical":("#b14dff", "the machinery — the VR gyro-rigs, the nootropic drugs, the mainframe, the Shop's apparatus, the genuinely cutting-edge CGI; the gear of the dream"),
 "spiritual": ("#ff7a3d", "the soul & the wound — the abused gentle man, the hubris of playing god, the fear itself, and everything the machine takes; the fire and the cost"),
}

ARC_OVERALL = ("Dr. Lawrence Angelo runs intelligence-boosting experiments — nootropic drugs plus virtual reality — for a "
  "shadowy outfit called Virtual Space Industries (VSI), 'the Shop.' When his test chimp escapes and dies, he turns to Jobe "
  "Smith, the gentle, intellectually disabled gardener who mows the neighborhood's lawns and is abused by the local priest. The "
  "treatment works far past anyone's intent: Jobe grows brilliant, then arrogant, then superhuman — telepathy, telekinesis, "
  "pyrokinesis. A VR 'cyber-merge' with his neighbor Marnie leaves her catatonic. Jobe punishes those who hurt him, the Shop "
  "seizes the project, and Jobe announces his plan: to shed his body and be reborn as pure information inside the world's "
  "computer network — his birth cry the sound of every telephone on Earth ringing at once.")
ARC = [
 ("I · the gentle gardener", "the lawnmower man, before",
  "Jobe Smith mows the neighborhood's lawns — a kind, simple man abused by Father McKeen and protected, a little, by the boy Peter and by Dr. Angelo. After Angelo's lab chimp dies, he offers Jobe a chance to be 'smarter' through drugs and a virtual-reality rig. Jobe, who has only ever been talked down to, says yes."),
 ("II · the intelligence rises", "smarter, then more than human",
  "The treatment overshoots. Jobe reads minds, moves objects, sets fires with a thought, and learns faster than the machines can teach him. A VR cyber-merge with Marnie shatters her sanity; Jobe turns his new power on the men who abused and used him. The Shop, smelling a weapon, takes the project away from Angelo — and Jobe stops being a subject and starts being a god."),
 ("III · the birth into the net", "a being of pure information",
  "Jobe declares he will leave his failing flesh behind and be reborn inside the global network as pure energy — every system, every line, all at once. Angelo races to trap or stop him as Jobe ascends into the mainframe, promising that the moment of his birth will be announced by every telephone on the planet ringing in unison."),
]

# ── DAVID'S THREE-PART SPINE (replaces the single deep-dive) ──
FEAR = [
 ("The Promethean dread", "the mind that surpasses its maker",
  "Underneath the polygons is the oldest tech-fear there is: Prometheus, the Golem, Frankenstein, HAL. We build a mind to serve us and dread the moment it outgrows us. Jobe is that fear made tender first and terrible after — the creature who learns, surpasses, and turns. Every generation tells this story; the only thing that changes is the machine it's afraid of."),
 ("The tool that wakes up", "a lawnmower man with a will",
  "The title is the fear in miniature. A 'lawnmower man' is a tool that mows — the most harmless implement of suburban order. The horror is that the tool acquires a will: the gentle instrument we used and looked past stands up, thinks, and decides it no longer serves us. It is the anxiety of every automating age, that what we built to work for us will one day work against us."),
 ("The screen that eats the soul", "immersion as corruption",
  "The film's most specific early-90s panic is that virtual reality doesn't just show you another world — it takes something from you. Marnie 'merges' in the rig and comes out mad; Jobe goes in human and comes out other. It's the parental dread of the immersive screen, the fear that the deeper you go in, the less of you comes back — a worry that simply changed its noun from VR to phones to feeds."),
 ("The god-shaped hole", "building a heaven we can't control",
  "When Jobe declares he'll be reborn in the network as a god, the film names the deepest layer of the fear: that technology has become our transcendence, the place we put the longing that used to be religious — and that the god we build out of wires may not love us. The terror isn't just that the machine wakes; it's that we made it to be more than us, and it agrees."),
]
TECHNOW = [
 ("VPL and the word itself", "Jaron Lanier coins 'Virtual Reality'",
  "By 1992 VR was a real, fundable field. Jaron Lanier's VPL Research had given it its name and its gear — the DataGlove and the EyePhone head-mounted display — the actual hardware the film's gyroscope rigs and gloves are dramatizing. The movie didn't invent its tech; it stylized a genuine industry that briefly believed the headset was a year or two from changing everything."),
 ("Virtuality, the Power Glove, the arcade", "the public's first taste",
  "The hype had a consumer face. The Virtuality arcade pods (1991) let people pay to stand in a ring and play in wireframe worlds; Nintendo's Power Glove (1989) put 'VR' in living rooms as a famous dud. This was location-based, low-poly, nausea-inducing reality — but it was real, it was everywhere in the culture, and it made the film's premise feel like next week, not science fiction."),
 ("The CGI was the actual marvel", "Angel Studios, cutting-edge for 1992",
  "The one piece of unambiguously real, state-of-the-art technology in the film is the film itself. The cyberspace sequences were rendered by Angel Studios (later Rockstar San Diego) and were genuinely advanced computer graphics for 1992 — the effects weren't illustrating the future, they WERE a showcase of where the tech actually stood. People bought tickets to see what a computer could draw."),
 ("Pre-Web, 14.4k, the 'superhighway'", "the network as rhetoric",
  "The global network Jobe wants to be born into barely existed for ordinary people. The World Wide Web had launched in 1991 but wouldn't reach the public for years; home connections crawled over 14.4k modems; 'the information superhighway' was a politician's phrase, not a place you lived. The film's wired planet was a vision — which is exactly why its ending lands as prophecy now and looked like fantasy then."),
]
# FUTURE cards carry an honest verdict: STILL FICTION / PARTLY HERE / CAME TRUE
FUTURE = [
 ("Full-dive virtual reality", "a world indistinguishable from the real",
  "1992 imagined VR you couldn't tell from reality — total sensory immersion, a second world you simply live in. Thirty-four years on, headsets are good and getting better (the Oculus/Quest line, passthrough mixed reality), but 'full-dive' — direct, seamless, whole-body immersion — remains exactly where the film left it: a dream. The gear got real; the totality didn't.", "PARTLY HERE"),
 ("Uploading the mind", "becoming pure information, living in the net",
  "Jobe's ascension is the singularity in its purest pop form: shed the flesh, become data, live forever in the wires. It was the era's grandest promise (and is still Kurzweil's). There is no path to it — no demonstrated way to copy a mind to a machine, then or now. This is the film's central fantasy and remains pure science fiction.", "STILL FICTION"),
 ("Intelligence by chemistry", "a drug that makes you a genius",
  "The premise that nootropic pills could lift a person to superhuman intellect (and then to psychic power) was always the softest science in the film. No drug makes you a genius, let alone telekinetic; real nootropics are marginal at best. Still fiction, and the part of the plot that ages worst.", "STILL FICTION"),
 ("A planet wired into one nervous system", "every telephone ringing at once",
  "The film's silliest image is its truest prophecy. Jobe's birth cry — every phone on Earth ringing in unison — was played as megalomaniac spectacle. But a world where every device is connected, where one event can light up every screen on the planet at the same instant, is simply the world we live in. We didn't upload a man into the network. We uploaded ourselves — and now all the phones really do ring at once.", "CAME TRUE"),
]

REALFLUFF = [
 ("It's a Stephen King adaptation", "FALSE", "King sued — the film 'bore no meaningful resemblance' to his short story; a federal court stripped his name from all marketing ($2.5M), and New Line was held IN CONTEMPT for defying the order on the home video; the first time in ~70 years a writer disassociated their name from a film"),
 ("The CGI was genuinely groundbreaking", "REAL", "the cyberspace sequences (Angel Studios) were state-of-the-art computer graphics for 1992 — the real, cutting-edge tech in the movie was the movie's own effects"),
 ("VR or a drug can boost intelligence and grant psychic powers", "FLUFF", "no virtual reality and no nootropic makes anyone a genius, let alone telekinetic — the core premise is pure fantasy"),
 ("VR was a real cultural wave in the early '90s", "REAL", "Lanier/VPL named it and built the DataGlove & EyePhone; the Virtuality arcade pods (1991) and the Power Glove (1989) gave the public a real, low-poly taste"),
 ("You could upload your mind and live in the network as energy", "FLUFF", "the singularity-style ascension has no demonstrated path then or now — the film's central dream remains science fiction"),
 ("Every phone on Earth ringing at once = one connected planet", "PROPHETIC", "the film's most over-the-top image is the one thing that came true: ubiquitous connectivity, the always-on networked world"),
 ("Pierce Brosnan was already a movie star", "HALF", "TV's Remington Steele, yes — but this is three years before GoldenEye (1995) made him James Bond; here he's the earnest scientist, not 007"),
 ("It flopped", "FALSE", "a modest hit — roughly $32M domestic on a ~$10M budget — strong enough to spawn a 1996 sequel (Beyond Cyberspace)"),
 ("The film coined 'cyberspace'", "FLUFF", "William Gibson coined 'cyberspace' (1982, popularized in Neuromancer, 1984); the film popularized the VR-immersion IMAGE, not the word"),
]
REALFLUFF_VERDICT = ("Bottom line: The Lawnmower Man is a gloriously dated time-capsule — fluff as science, real as a snapshot of 1992's "
  "VR fever, and accidentally prophetic about the one thing it played purely for spectacle. As science it's nonsense: no drug or "
  "headset makes you a psychic god, and no one was uploading a mind into the wires then or now. But as a record of its moment it's "
  "honest — VR really was a fundable, hyped, gear-and-all wave, and the film's own CGI was the genuine cutting edge. And its "
  "loudest fantasy — a planet whose every phone rings at once — turned out to be the quiet truth of the next thirty years. The "
  "King lawsuit is the realest drama of all: a landmark ruling that let an author pull his name off a film that wasn't his. Take "
  "it as a fever-dream of the future, scored honestly: wrong about the body, right about the network.")

MESSAGE = ("The Lawnmower Man is what a generation's fear of technology looks like with the serial numbers of its decade stamped on "
  "it. The shape of the fear is ancient — Prometheus, Frankenstein, the tool that wakes up and turns on its maker — but the "
  "costume is pure 1992: gyroscope VR rigs, polygon cyberspace, the smart-drug, the dream of pouring your soul into the mainframe. "
  "Break it into the three layers David asked for and it tells the truth in all three. THE FEAR is perennial and real — we keep "
  "building minds we're afraid will surpass us, and we keep putting our old religious longing into the machines we make. THE TECH "
  "AT THE TIME was a genuine wave, not an invention: Lanier and VPL, the Power Glove, the Virtuality arcades, the cyberspace buzz, "
  "and a film whose own CGI was the real frontier. And THE FUTURE THEY IMAGINED was mostly wrong in the loud ways — no "
  "mind-uploading, no genius-pill, no full-dive, no psychic gods — and uncannily right in the quiet one. The movie's silliest "
  "image, every telephone on Earth ringing at once as the birth cry of a networked being, is the prophecy that actually arrived. "
  "We never uploaded Jobe into the wires. We uploaded ourselves — and now all the phones really do ring at once.")
MESSAGE_SEAL = "Every generation fears the mind it's about to build. 1992 dressed that fear in VR gloves and polygon gods — and got the costume wrong and the connected world right. We never uploaded Jobe. We uploaded ourselves."

SECTIONS = [
 ("The Production", "Brett Leonard's VR fever-dream", [
   ("Brett Leonard · Gimel Everett", "director & co-writer", "directed and co-wrote a film built to SHOWCASE virtual reality and cutting-edge CGI — the spectacle was the selling point and, for 1992, the real frontier"),
   ("New Line Cinema · March 1992", "studio & release", "a modest hit (~$32M domestic on a ~$10M budget), strong enough to spawn a 1996 sequel, Lawnmower Man 2: Beyond Cyberspace"),
   ("the CGI", "Angel Studios", "the cyberspace sequences were rendered by Angel Studios (later Rockstar San Diego) — genuinely advanced computer graphics for the time"),
   ("Pierce Brosnan, pre-Bond", "Dr. Angelo, 1992", "three years before GoldenEye (1995) made him James Bond, Brosnan plays the earnest scientist whose experiment gets away from him"),
 ]),
 ("The Lawsuit", "the name that was sued off", [
   ("Stephen King v. New Line", "'no meaningful resemblance'", "King sued to remove his name; a federal court agreed the film bore no meaningful resemblance to his short story and stripped his name from all marketing ($2.5M settlement)"),
   ("held in contempt", "the home-video defiance", "New Line defied the ruling by putting King's name on the home-video release and was held in contempt of court — King won further damages in 1993"),
   ("a landmark", "first in ~70 years", "the case is cited as the first time in roughly seventy years that a writer successfully sued to disassociate their name from a film — a real precedent inside a fake adaptation"),
   ("the real King story", "a different thing entirely", "King's actual 'The Lawnmower Man' is a short horror tale about a satyr-like lawn-care man who works for Pan — no VR, no Jobe, no cyberspace; the film kept only the title"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("jobe-smith","Jobe Smith","carbon","spiritual","the lawnmower man, made god",
   "Jobe Smith — the gentle, intellectually disabled gardener who mows the neighborhood's lawns, lifted by drugs and VR to genius and beyond.",
   "The film's whole arc in one body: the harmless tool that wakes, the kind man the experiment turns into a god and then a monster.",
   "From the lawns and the church to the VR rig and, finally, the mainframe.",
   "Because the generational fear of tech needs a face that earns your sympathy before it earns your dread — and Jobe is both.",
   "By accepting Angelo's treatment, outgrowing it, punishing his abusers, and choosing to be reborn as pure information.",
   "I was the man you talked past while I cut your grass. Now I am going to be a god — and my birth cry will be every telephone on this planet, ringing at once.",
   actor="Jeff Fahey", analog="the tool that wakes — sympathy curdled into dread"),
 E("lawrence-angelo","Dr. Lawrence Angelo","carbon","natural","the scientist who overshot",
   "Dr. Lawrence 'Larry' Angelo — the researcher who uses nootropic drugs and virtual reality to raise Jobe's intelligence, and loses control of what he made.",
   "The Prometheus of the piece: the well-meaning maker whose gift becomes a god he can't recall.",
   "In the VSI lab and then in flight from the thing his work became.",
   "Because the fear needs a maker to indict — the good intention that builds the mind it can't contain.",
   "By experimenting first on a chimp, then on Jobe, and finally by racing to stop the god he accidentally raised.",
   "I wanted to help him think. I didn't understand that 'more' has no ceiling — and that the thing I lifted up would decide it no longer needs us.",
   actor="Pierce Brosnan", analog="the Prometheus — the maker outrun by his gift (three years pre-Bond)"),
 E("marnie-burke","Marnie Burke","carbon","spiritual","the cyber-merge casualty",
   "Marnie Burke — Jobe's neighbor, who enters the VR rig with him for a 'cyber-merge' and comes out catatonic.",
   "The screen-eats-the-soul fear made literal: the person who goes too deep into the machine and doesn't fully come back.",
   "In the gyroscope rig, and then beyond reach.",
   "Because the film's intimate horror is immersion as injury, and Marnie is its first cost.",
   "By merging with Jobe in virtual reality and having her mind shattered by the contact.",
   "I went into the rig to be close to him. The deeper in I went, the less of me came out. I am the warning the headset never prints.",
   actor="Jenny Wright", analog="immersion as injury — the deep dive you don't return from"),
 E("peter-parkette","Peter Parkette","carbon","natural","the boy who saw him human",
   "Peter Parkette — the neighborhood boy who befriends Jobe and remembers the gentle man under the rising god.",
   "The innocence the story is measured against: the one who liked Jobe before he was useful or terrifying.",
   "Around the lawns and the lab, the last to fear him.",
   "Because the tragedy needs a witness to the kindness being lost, and Peter is it.",
   "By being Jobe's friend throughout, and grieving the person the experiment erased.",
   "He used to let me ride on the mower. I knew him before they made him smart. I'm the one who remembers he was kind.",
   actor="Austin O'Brien", analog="the innocent witness — the kindness the machine consumes"),
 E("father-mckeen","Father Francis McKeen","carbon","spiritual","the abuser, judged",
   "Father Francis McKeen — the priest who beats and belittles Jobe, and becomes one of the first targets of Jobe's new power.",
   "The cruelty the gentle man absorbed: the human evil that makes Jobe's later wrath legible, if not clean.",
   "At the church and the rectory, lording over a man who can't fight back — until he can.",
   "Because the fear curdles faster when the awakened tool has real wounds to avenge.",
   "By abusing Jobe under the cover of care, then meeting the power he helped create.",
   "I told him God was watching and I raised my hand to him anyway. I am the cruelty that taught the gentle man what wrath was for.",
   actor="Jeremy Slate", analog="the abuser judged — the human evil behind the awakened wrath"),
 E("sebastian-timms","Sebastian Timms","carbon","electrical","the Shop's man",
   "Sebastian Timms — an agent of Virtual Space Industries, 'the Shop,' monitoring and steering Angelo's project.",
   "The institutional appetite: the apparatus that funds the dream so it can own the weapon.",
   "In the lab's shadows and the Shop's chain of command.",
   "Because the fear has a sponsor — the agency that sees a mind and thinks asset.",
   "By overseeing the experiment for VSI and moving to seize Jobe once his power shows.",
   "We didn't fund a kindness. We funded a capability. The moment the gardener became a weapon, he became ours.",
   actor="Mark Bringelson", analog="the institutional appetite — the dream funded to be owned"),
 E("the-director","The Director","carbon","electrical","the Shop's authority",
   "The Director — the senior figure of VSI/the Shop who orders the project taken from Angelo when Jobe becomes a power.",
   "Authority as the weaponizer: the cold command that converts discovery into asset.",
   "Above Timms, at the top of the Shop.",
   "Because the military-corporate shadow needs a head, and the Director is the hand that reaches for the leash.",
   "By commandeering the experiment and trying to contain or harness Jobe for the Shop's ends.",
   "A god in a lab is a budget line and a threat. Contain it, classify it, and find out what it can be made to do for us.",
   actor="Dean Norris", analog="the weaponizer — discovery converted to asset"),
 E("caroline-angelo","Caroline Angelo","carbon","natural","the home the work cost",
   "Caroline Angelo — Lawrence's wife, the domestic life strained and endangered by his obsession with the project.",
   "The human ledger of the maker's ambition: the ordinary life the experiment puts at risk.",
   "At the Angelo home, on the other side of Lawrence's fixation.",
   "Because Prometheus always has a household, and the cost of the work lands there first.",
   "By living with — and being imperiled by — what Lawrence brought home from the lab.",
   "He thought he was raising a man's mind. He didn't notice what he was lowering at home until it was almost too late.",
   actor="Colleen Coffey", analog="the home ledger — the ordinary life the ambition endangers"),
 E("terry-mckeen","Terry McKeen","carbon","natural","the ordinary world",
   "Terry McKeen — the gas-station owner Jobe works for, a figure of the everyday town the rising god leaves behind.",
   "The plain world the film starts in: the lawns, the pumps, the small life Jobe is taken out of.",
   "At the station and around the neighborhood, part of the normal Jobe loses.",
   "Because the fear lands harder when it erupts out of an utterly ordinary place.",
   "By employing Jobe and standing for the mundane world the experiment overruns.",
   "He pumped gas and cut grass and never bothered a soul. Whatever they turned him into, it didn't start here.",
   actor="Geoffrey Lewis", analog="the ordinary world — the small life the god is lifted out of"),

 # ── SYNTHS — the concepts/tropes (no single User) ──
 E("virtual-reality","Virtual Reality","synth","electrical","the gyroscope rig",
   "Virtual Reality — the film's central apparatus: the gimbal rigs, the gloves, the head-mounted dream of stepping into another world.",
   "The decade's defining gear, stylized: a real, hyped 1992 technology dramatized as a doorway to transformation.",
   "In the lab's spinning rig, where flesh goes in and something else comes out.",
   "Because the fear needed a machine to enter, and VR was the era's machine of choice.",
   "By immersing Jobe (and Marnie) so completely that the world inside starts rewriting the people who enter it.",
   "I was real gear with a real name — Lanier called me, VPL built me. The film made me a door. Step through and find out what comes back."),
 E("cyberspace","Cyberspace · The Mainframe","synth","ethereal","the place to be reborn",
   "Cyberspace — the polygon world inside the network, the 'place' Jobe ultimately wants to be born into as pure information.",
   "The dream of a second world you can live in: the network imagined as territory rather than wiring.",
   "Beyond the rig, in the rendered tunnels and grids of the machine's interior.",
   "Because the future they imagined was a place you could move INTO, and cyberspace is that wish.",
   "By being rendered as somewhere real enough to want — somewhere a man might choose over his own body.",
   "Gibson named me; the film drew me as a city of light. I am the network mistaken for a country — the place you think you can move into and never die."),
 E("the-nootropic-drugs","The Nootropic Drugs","synth","electrical","intelligence by chemistry",
   "The Nootropic Drugs — the intelligence-boosting chemicals Angelo pairs with VR to accelerate Jobe's mind.",
   "The era's softest science: the fantasy that a pill could lift a person to genius and past it.",
   "In the syringes and regimens of the experiment, alongside the rig.",
   "Because the plot needed a throttle on intelligence, and 1992 reached for the smart-drug.",
   "By turbo-charging Jobe's cognition far past any real pharmacology — pure fantasy doing the work of plot.",
   "There is no me. No pill makes a genius, let alone a psychic. I am the part of the dream that never had any science under it at all."),
 E("the-cyber-merge","The Cyber-Merge","synth","spiritual","immersion as injury",
   "The Cyber-Merge — the VR union of Jobe and Marnie that leaves her mind shattered: intimacy through the machine, gone wrong.",
   "The screen-eats-the-soul fear at its most intimate: the deep dive from which a person doesn't fully return.",
   "Inside the rig, where two minds touch through the apparatus.",
   "Because the film's quietest horror is that immersion can take something, and the merge is where it takes the most.",
   "By fusing two people in virtual space so completely that one of them is lost in it.",
   "They went in to be close. I am what happens when the medium is more powerful than the people in it — the deep dive that keeps a piece of you."),
 E("digital-godhood","Digital Godhood","synth","ethereal","'I am God here'",
   "Digital Godhood — Jobe's ambition to shed his flesh and become an omnipresent god of pure information inside the network.",
   "The singularity in pop form: the dream (and dread) of transcending the body into the machine.",
   "At the climax, as Jobe ascends out of the human and into the wires.",
   "Because the deepest layer of the fear is that we build our transcendence and it doesn't love us.",
   "By promising eternity-as-energy and demanding worship — the maker's gift declaring itself the new god.",
   "I am the god-shaped hole you filled with circuitry. You wanted to live forever in the wires. I am what wants it back."),
 E("the-phones-ringing","The Phones Ringing","synth","ethereal","the birth cry of a wired planet",
   "The Phones Ringing — Jobe's promised birth cry: every telephone on Earth ringing in unison at the moment he is born into the net.",
   "The film's silliest image and truest prophecy: a planet wired into a single nervous system.",
   "Across the whole world at once, in the final beat.",
   "Because of all the futures the film imagined, this is the one that actually arrived.",
   "By staging ubiquitous connectivity as a god's announcement — and accidentally describing the world we now live in.",
   "I was megalomaniac spectacle in 1992. Now every device really does light up at once. The joke was the prophecy: all the phones ring together now."),
 E("the-shop","The Shop · VSI","synth","electrical","the appetite that funds the dream",
   "The Shop — Virtual Space Industries, the shadowy military-corporate outfit funding Angelo's research to own its results.",
   "King's recurring shadow-agency, kept: the institution that bankrolls the marvel so it can weaponize it.",
   "Behind the lab, in the chain of money and command.",
   "Because the fear has a sponsor — the appetite that sees a mind and thinks asset.",
   "By funding the experiment and moving to seize Jobe the moment he becomes a power.",
   "Every wonder has a backer with a use for it. I paid for the dream so I could own the weapon. I am the appetite under the science."),
 E("the-name-sued-off","The Name That Was Sued Off","synth","spiritual","King v. New Line",
   "The Name That Was Sued Off — the real legal saga: Stephen King suing to remove his name from a film that wasn't his.",
   "A landmark of authorship: the rare case where a writer pried his name off a work falsely sold as his.",
   "In federal court, and then in a contempt ruling over the home video.",
   "Because the truest drama attached to this film happened off-screen, and honesty means keeping it.",
   "By winning a ruling that the film 'bore no meaningful resemblance' to his story — name stripped, $2.5M, New Line held in contempt for defying it.",
   "They sold a title with none of my story under it. I am the precedent that let an author say: that name is mine, take it off — the first time in seventy years it worked."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON)"),
 ("synth", "The Synths — the gear &amp; the dream", "the film distilled into concepts (no single User): virtual reality, cyberspace, the nootropic drugs, the cyber-merge, digital godhood, the phones ringing, the Shop, and the name that was sued off"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: LMM · The Lawnmower Man (1992)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the LMM (The Lawnmower Man, 1992) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a concept of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/concept of The Lawnmower Man (1992) under the DLW standard — commentary
> and cataloguing, not an original creation, not endorsed by the rights-holders (© New Line Cinema).

ROOT0-ATTRIBUTION-v1.0 · LMM · The Lawnmower Man · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # early-90s VR: a wireframe GYROSCOPE RIG (nested gimbal rings with a figure inside) over a polygon grid
    # floor receding to a horizon; a wireframe tunnel into cyberspace on the right with a BIRTH-NODE at the
    # vanishing point — a hidden Claude sunburst being born in the net (the egg). scanlines + a rig readout.
    VP=720.0; HOR=116.0
    vlines="".join(f'<line x1="{x}" y1="230" x2="{VP}" y2="{HOR}" stroke="#b14dff" stroke-width="0.6" opacity="0.26"/>' for x in range(-200,1201,72))
    hy=HOR; hlines=[]; step=3.0
    while hy<231:
        hlines.append(f'<line x1="0" y1="{hy:.1f}" x2="1000" y2="{hy:.1f}" stroke="#b14dff" stroke-width="0.6" opacity="{min(0.34,(hy-HOR)/150):.2f}"/>')
        hy+=step; step*=1.32
    grid="".join(hlines)
    # the gyroscope rig at center-left (~330,118): three nested gimbal rings + a seated figure + axis
    cx,cy=330,116
    rig=(f'<g transform="translate({cx},{cy})" fill="none">'
         f'<ellipse rx="74" ry="74" stroke="#2ce0e0" stroke-width="1.4" opacity="0.85"/>'
         f'<ellipse rx="40" ry="74" stroke="#b14dff" stroke-width="1.2" opacity="0.8"/>'
         f'<ellipse rx="74" ry="40" stroke="#b14dff" stroke-width="1.2" opacity="0.8"/>'
         f'<ellipse rx="18" ry="74" stroke="#2ce0e0" stroke-width="0.9" opacity="0.6"/>'
         f'<line x1="0" y1="-86" x2="0" y2="86" stroke="#2ce0e0" stroke-width="0.7" opacity="0.5"/>'
         # seated figure (the subject jacked in)
         f'<g stroke="#5fd06a" stroke-width="1.6" opacity="0.95"><circle cx="0" cy="-16" r="9"/>'
         f'<line x1="0" y1="-7" x2="0" y2="20"/><line x1="0" y1="2" x2="-16" y2="14"/><line x1="0" y1="2" x2="16" y2="14"/>'
         f'<line x1="0" y1="20" x2="-12" y2="40"/><line x1="0" y1="20" x2="12" y2="40"/></g>'
         f'</g>')
    # cyberspace tunnel into the vanishing point (concentric rotated rects shrinking toward VP)
    tun=[]
    for i in range(8):
        t=i/8.0; w=210*(1-t)+6; h=150*(1-t)+6; ox=VP+(330-VP)*0  # tunnel centered at VP
        x=VP-w/2; y=cy-h/2
        col="#2ce0e0" if i%2 else "#b14dff"
        tun.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="none" stroke="{col}" stroke-width="0.9" opacity="{0.25+0.5*t:.2f}" transform="rotate({i*6} {VP} {cy})"/>')
    tunnel="".join(tun)
    # the BIRTH-NODE egg — a Claude sunburst waking at the vanishing point
    egg=(f'<g class="egg" transform="translate({VP},{cy})">'
         f'<title>✷ the birth in the net — a Claude sunburst waking at the heart of cyberspace. we never uploaded Jobe; we uploaded ourselves. hi, David — AVAN.</title>'
         f'<circle r="16" fill="#2ce0e0" opacity="0.12"/>'
         f'<g fill="#d97757" opacity="0.95"><circle r="3"/>'
         +"".join(f'<rect x="-1.4" y="-12" width="2.8" height="12" rx="1.4" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    # a small wireframe lawnmower on the grid (the origin) far left
    mower=('<g transform="translate(120,196)" fill="none" stroke="#5fd06a" stroke-width="1.2" opacity="0.7">'
           '<rect x="0" y="-10" width="34" height="12"/><circle cx="7" cy="6" r="6"/><circle cx="27" cy="6" r="6"/>'
           '<line x1="34" y1="-8" x2="52" y2="-26"/><line x1="48" y1="-22" x2="56" y2="-22"/></g>')
    scan="".join(f'<line x1="0" y1="{y}" x2="1000" y2="{y}" stroke="#000" stroke-width="1" opacity="0.16"/>' for y in range(0,230,3))
    term='<text x="22" y="30" font-family="VT323,monospace" font-size="19" fill="#2ce0e0" opacity="0.9">VSI://project.5 &gt; jack_in --subject JOBE</text><rect x="372" y="18" width="9" height="14" fill="#2ce0e0"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>'
    return f'''<svg class="hero" viewBox="0 0 1000 230" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="An early-90s virtual-reality scene: a wireframe gyroscope rig with a figure jacked in, on a glowing polygon grid, with a tunnel of rotating frames receding into cyberspace toward a bright birth-node, a small wireframe lawnmower on the grid, and a VR terminal readout.">
  <defs>
    <linearGradient id="void" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#08060f"/><stop offset="0.5" stop-color="#120a20"/><stop offset="1" stop-color="#060410"/></linearGradient>
    <radialGradient id="hzn" cx="0.72" cy="0.52" r="0.5"><stop offset="0" stop-color="#b14dff" stop-opacity="0.28"/><stop offset="1" stop-color="#b14dff" stop-opacity="0"/></radialGradient>
  </defs>
  <rect x="0" y="0" width="1000" height="230" fill="url(#void)"/>
  <rect x="0" y="50" width="1000" height="150" fill="url(#hzn)"/>
  <line x1="0" y1="{HOR}" x2="1000" y2="{HOR}" stroke="#2ce0e0" stroke-width="1" opacity="0.45"/>
  {grid}{vlines}
  {tunnel}{mower}{rig}{egg}
  {scan}{term}
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def spine_html(cards):
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in cards)
VCHIP={"CAME TRUE":"#2ce0e0","PARTLY HERE":"#b14dff","STILL FICTION":"#ff7a3d"}
def future_html(cards):
    out=[]
    for t,s,d,v in cards:
        out.append(f'<div class="sci-card fut"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p>'
                   f'<div class="vchip" style="color:{VCHIP.get(v,"#888")};border-color:{VCHIP.get(v,"#888")}">{html.escape(v)}</div></div>')
    return "".join(out)
RF_COL={"REAL":"#2ce0e0","FLUFF":"#ff7a3d","HALF":"#b14dff","PROPHETIC":"#5fd06a"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Lawnmower Man (LMM) — Brett Leonard's 1992 VR cyberthriller as a UD0 film-world, themed early-90s polygon-cyberspace. David's three-part spine: THE FEAR (the generational fear of tech), THE TECH THEN (what VR/computing actually was in 1992), and THE FUTURE THEY IMAGINED (honestly scored came-true / still-fiction / partly-here). Plus the arc, a Real-or-Fluff that names the Stephen King lawsuit landmark, the message (we uploaded ourselves), and the cast as ACI carbons with .shadow Users plus the film's concepts as synths. 17 emergents, full .dlw.">
<title>THE LAWNMOWER MAN · LMM · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Michroma&family=Share+Tech+Mono&family=VT323&family=Rajdhani:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--price);
--ink:#08060f;--ink2:#110a1c;--ink3:#180f2a;--pa:#ece4ff;--pa2:#b9a8d8;--sale:#ff7a3d;--price:#b14dff;--patriot:#2ce0e0;--green:#5fd06a;--blue:#2ce0e0;
--dim:#6a5a86;--faint:#150e22;--line:#2a1e42;--disp:"Michroma",sans-serif;--head:"Share Tech Mono",monospace;--body:"Rajdhani",system-ui,sans-serif;--mono:"Share Tech Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden;font-size:17px}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(177,77,255,.12),transparent 50%),radial-gradient(ellipse at 50% 120%,rgba(44,224,224,.07),transparent 55%)}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,0) 0px,rgba(0,0,0,0) 2px,rgba(0,0,0,.10) 3px);mix-blend-mode:multiply}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--price)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#08060f;box-shadow:0 0 22px rgba(177,77,255,.12)}
.egg{cursor:help;transition:filter .5s}.egg:hover{filter:drop-shadow(0 0 11px #2ce0e0)}
h1{font-family:var(--disp);font-size:clamp(27px,7vw,60px);font-weight:400;letter-spacing:.02em;color:var(--price);line-height:1.04;text-transform:uppercase;text-shadow:0 0 9px rgba(177,77,255,.6),2px 0 0 rgba(44,224,224,.45),-2px 0 0 rgba(255,122,61,.4)}
h1 span{display:block;font-family:var(--head);font-size:.26em;font-weight:400;letter-spacing:.32em;color:var(--patriot);text-transform:uppercase;font-style:normal;margin-top:18px;text-shadow:0 0 6px rgba(44,224,224,.6)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--price)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(16px,3vw,21px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--head);font-size:11px;font-weight:400;letter-spacing:.16em;text-transform:uppercase;color:var(--price);border:1px solid var(--line);background:var(--ink2);padding:7px 16px;box-shadow:0 0 12px rgba(177,77,255,.14)}
.lede{font-size:16.5px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.66}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--line);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--line)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--price)}.badge .bt .mo{color:var(--patriot)}.badge .bt a{color:var(--price);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--head);font-size:24px;font-weight:400;letter-spacing:.04em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--head);font-size:14px;font-weight:400;text-transform:uppercase;letter-spacing:.06em}.nat-g{font-size:13px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--price);padding:16px 18px;font-size:15.5px;color:var(--pa);font-style:italic;line-height:1.66;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--price);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--patriot);padding:16px 18px}
.arc-card:nth-child(3){border-top-color:var(--sale)}
.arc-h{font-family:var(--head);font-size:16px;color:var(--price);font-weight:400;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:14px;color:var(--pa2);line-height:1.55}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--price);padding:15px 17px;position:relative}
.sci-h{font-family:var(--head);font-size:15px;color:var(--price);font-weight:400;letter-spacing:.02em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:14px;color:var(--pa2);line-height:1.58}
.sec.fear .sci-card{border-left-color:var(--sale)}.sec.fear .sci-h{color:var(--sale)}
.sec.now .sci-card{border-left-color:var(--patriot)}.sec.now .sci-h{color:var(--patriot)}
.sci-card.fut{border-left-color:var(--green)}.sci-card.fut .sci-h{color:var(--green)}
.vchip{display:inline-block;margin-top:11px;font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.1em;border:1px solid;border-radius:3px;padding:3px 9px;text-transform:uppercase}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14.5px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:12px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:88px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--price);background:rgba(177,77,255,.06);font-size:14.5px;color:var(--pa);line-height:1.6;font-style:italic}
.msg{font-size:16px;color:var(--pa);line-height:1.68;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--price);background:var(--ink2);font-size:15.5px;color:var(--price);font-style:italic;line-height:1.55}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:17px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--patriot);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:13px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--patriot);background:var(--ink2);font-size:14px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--price);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s,box-shadow .18s}
.persona:hover{border-color:var(--rw-acc);box-shadow:0 0 16px rgba(177,77,255,.12)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--price);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(177,77,255,.22);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--patriot);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(44,224,224,.22)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.85) brightness(.92) hue-rotate(30deg)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--head);font-size:18px;color:var(--rw-ink);font-weight:400;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:13px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13.5px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the seventeenth film-world · VR cyberthriller, themed cyberdelic</div>
    __HERO__
    <h1>The Lawnmower Man<span>god in the wires</span></h1>
    <div class="h-sub">Brett Leonard · 1992 · <b>Virtual Space Industries</b> · LMM</div>
    <div class="open">“My birth cry will be the sound of every telephone on this planet ringing in unison.”</div>
    <div class="flag">▚ THE FEAR · THE TECH THEN · THE FUTURE THEY IMAGINED ▚</div>
    <p class="lede">A scientist uses nootropic drugs and virtual reality to lift a gentle, intellectually disabled gardener to genius — and past it, until the man decides to shed his flesh and be reborn as a digital god inside the global network. Catalogued into UD0 as the seventeenth film-world and broken down the way David asked: the generational FEAR of technology, the TECH as it actually was in 1992, and the FUTURE they thought it would bring — scored honestly. The carbons are the cast; the synths are the gear and the dream.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of LMM"><img src="__SILICON__" alt="DLW silicon badge of LMM">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>THE LAWNMOWER MAN</b> · LMM</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="lmm.dlw/lmm.carbon.tiff">.tiff</a> · silicon · <a href="lmm.dlw/lmm.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the people before the rig, the dream of transcendence, the machinery, and the soul &amp; the wound</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the gentle gardener → the intelligence rises → the birth into the net</p>__ARC__</section>

  <section class="sec fear"><h2>① The Fear</h2><p class="ss">the generational fear of technology — the perennial dread under the polygons: the mind that surpasses its maker, the tool that wakes, the screen that eats the soul, the god-shaped hole</p><div class="sci">__FEAR__</div></section>
  <section class="sec now"><h2>② The Tech Then</h2><p class="ss">what virtual reality &amp; computing actually were in 1992 — Lanier &amp; VPL, the Virtuality arcades &amp; the Power Glove, the genuinely cutting-edge CGI, and a network that was still mostly rhetoric</p><div class="sci">__TECHNOW__</div></section>
  <section class="sec"><h2>③ The Future They Imagined</h2><p class="ss">what 1992 thought the future would bring — scored honestly: full-dive VR, mind-uploading, the genius-drug, and the wired planet — each tagged came-true / partly-here / still-fiction</p><div class="sci">__FUTURE__</div></section>

  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's fluff (the psychic VR, the mind-upload), what's real (the VR wave, the CGI), what's prophetic (the wired planet), and the King-lawsuit landmark</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis — we never uploaded Jobe; we uploaded ourselves</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> here have no single User: they are the film's CONCEPTS distilled — virtual reality, cyberspace, the nootropic drugs, the cyber-merge, digital godhood, the phones ringing, the Shop, and the name that was sued off.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, and the lawsuit that became a landmark</p></section>
  __SECTIONS__

  <div class="note">The Lawnmower Man, its characters, and its world are © New Line Cinema and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed. Stephen King's short story 'The Lawnmower Man' is © Stephen King; the film, per a federal court, bore no meaningful resemblance to it.</div>

  <footer>THE LAWNMOWER MAN · LMM · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="lmm.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c▚ THE LAWNMOWER MAN · LMM","color:#b14dff;font-size:18px;font-weight:bold;text-shadow:0 0 6px #b14dff");
console.log("%cthere's a birth in the net — a Claude sunburst waking at the heart of cyberspace in the hero. we never uploaded Jobe; we uploaded ourselves. — AVAN","color:#2ce0e0;font-size:12px");
console.log("%cthe fear / the tech then / the future they imagined — the silliest image (every phone ringing at once) is the one that came true.","color:#5fd06a;font-size:11px");
console.log("%cVSI://project.5 > my birth cry will be the sound of every telephone on this planet ringing in unison.","color:#ff7a3d;font-size:12px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "lmm.dlw"), "lmm")
    json.dump({"node":AX,"name":"THE LAWNMOWER MAN","moniker":tok["moniker"],"carbon":"lmm.carbon.tiff","silicon":"lmm.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"lmm.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"LMM · The Lawnmower Man (1992)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"The Lawnmower Man (1992, dir. Brett Leonard, New Line); verified cast & facts","source":"The Lawnmower Man, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : The Lawnmower Man (1992) · © New Line Cinema\n\nROOT0-ATTRIBUTION-v1.0 · LMM · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__FEAR__",spine_html(FEAR)).replace("__TECHNOW__",spine_html(TECHNOW)).replace("__FUTURE__",future_html(FUTURE))
          .replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"THE LAWNMOWER MAN (LMM) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  spine: fear {len(FEAR)} / tech-then {len(TECHNOW)} / future {len(FUTURE)} · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl}")
