# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **German children's detective novel series** -- "Die Herrenhaus-Detektive". Target audience: children aged 8-10. Published via Amazon KDP. 5-book series planned, each with a **Linear** (classic) and **Interaktiv** (branching/choose-your-own-adventure) version.

The language of all content is **German**. All chapter text, planning documents, and metadata are written in German.

## Repository Structure

```
Author_Info.md                           # MASTER REFERENCE -- read before every chapter

_Gemeinsam/                              # Shared across all books
  Buchkonzept.md                         # Book concept & Amazon strategy
  Schreibstil_Regeln.md                  # Writing style rules (age 8+)
  Kapitel_Schreibvorlage.md              # Chapter template/checklist
  Illustrationen_Prompts.md              # Illustration generation prompts
  Referenzbilder/                        # Reference images

Band_1/                                  # Band 1: Das verbotene Herrenhaus
  Linear/                                # Classic linear story
    Kapitel/                             # 19 chapter markdown files
    Story_Outline.md                     # 18-chapter story outline (4 acts)
    Detaillierte_Szenenplanung.md        # Scene-by-scene plan
    Manuskript.docx                      # Compiled manuscript
    create_manuscript.py                 # Script to compile chapters
  Interaktiv/                            # Branching/choose-your-own-adventure
    Abschnitte/                          # ~96 section files
    Illustrationen/                      # 15 illustrations
    Abschnitt_Map.md                     # Section connection map
    create_manuscript_interaktiv.py      # Script to compile sections
  Cover/                                 # Linear/, Interaktiv/, _Archiv/
  Publishing/                            # KPF/, Kindle_Creator/

Band_2/                                  # Band 2: Das Geheimnis des Brunnens
  Linear/                                # Same structure as Band 1
  Interaktiv/                            # (future)
  Cover/
  Publishing/

Band_3/ ... Band_5/                      # Prepared for future books
```

## Critical Workflow

1. **Before writing or editing ANY chapter**, read [Author_Info.md](Author_Info.md) in full. It contains the continuity tracker (timeline, found items, what the children know, open questions) that MUST be respected.
2. **After completing a chapter**, update the continuity tracker in Author_Info.md with new events, items found, and knowledge gained.
3. **Git commit message format**: `Kapitel X erweitert (~XXXX Woerter)` -- include approximate word count.

## Writing Rules (Non-Negotiable)

- **Sentence length**: 8-12 words (max 15)
- **Paragraphs**: 3-5 lines, lots of whitespace
- **Dialog**: minimum 40-50% of each chapter
- **Perspective**: Third person (Er-Perspektive), always close to Jonas
- **Vocabulary**: Concrete words only. No foreign/abstract words. "seltsam" not "mysterioes", "beobachten" not "observieren"
- **Emotions**: Always physical ("Sein Herz klopfte schneller") never abstract ("Er spuerte ein seltsames Gefuehl")
- **No passive voice**
- **Chapter length**: 1,200-1,400 words (Band 2), 1,600-1,900 words (Band 1)
- **Cliffhanger at end of every chapter** -- mandatory, no exceptions
- **Pacing**: Something must happen every 1-2 pages (new info, question, obstacle, surprise)
- **Next chapter resolves previous cliffhanger immediately** -- no time skips

## Characters

- **Jonas (10)**: POV character. New to village Eichenhain. Curious, observant, asks questions. Mediates between Mila and Ben.
- **Mila (10)**: The brave one. Pushes forward. Impatient. Says "Quatsch", "Jetzt oder nie". Crosses arms, rolls eyes.
- **Ben (10)**: Anxious/skeptic. Wears red cap. Comic relief. Warns, whispers, nervous. BUT must also have surprising brave/clever moments (especially Chapter 13). Not just scared -- also funny and smart.
- **Dynamic**: Jonas asks, Mila pushes, Ben brakes. Mila and Ben bicker (lovingly). All three are a team.

## Chapter Checklist

Every chapter must contain:
- Opening scene with movement (straight into action)
- At least 40% dialog
- At least 1 new clue or discovery
- 1 mini-obstacle (fear, argument, false trail, locked door)
- Clear physical emotional reactions
- 1 mini-decision by the children
- Cliffhanger ending (mandatory!)
- Ben has at least 1 funny or scared moment

## Project Status

### Band 1 (Linear)
- **Chapters 1-18**: Complete (~1,600 words each)
- **4-Act Structure**: Act 1 (Ch 1-4) Setup, Act 2 (Ch 5-9) Investigation, Act 3 (Ch 10-14) Danger, Act 4 (Ch 15-18) Resolution

### Band 1 (Interaktiv)
- Complete (~96 Abschnitte with branching paths)

### Band 2 (Linear)
- **Chapters 1-19**: Complete (~1,200-1,400 words each)

### Band 3-5
- Planned, not yet started

## Common Mistakes to Avoid

- Long descriptions without dialog or action
- Sentences over 15 words
- Abstract/difficult vocabulary
- Subtle emotions instead of clear physical reactions
- Passive constructions
- Chapters without cliffhangers
- Ben being ONLY scared (he must also be clever/funny)
- Mila being ONLY tough (she can be uncertain sometimes)
- Too many side characters at once
