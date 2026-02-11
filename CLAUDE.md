# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **German children's detective novel** -- "Die Herrenhaus-Detektive, Band 1: Das verbotene Herrenhaus". Target audience: children aged 8-10. Published via Amazon KDP. Part of a planned 3-book series.

The language of all content is **German**. All chapter text, planning documents, and metadata are written in German.

## Repository Structure

```
Kapitel/                          # Chapter files (Markdown)
  Die_Herrenhaus_Detektive_Band1_KapitelX.md
Author_Info.md                    # MASTER REFERENCE -- read before every chapter
Die_Herrenhaus_Detektive_Buchkonzept.md           # Book concept & Amazon strategy
Die_Herrenhaus_Detektive_Band1_Story_Outline.md   # 18-chapter story outline (4 acts)
Die_Herrenhaus_Detektive_Band1_Detaillierte_Szenenplanung.md  # Scene-by-scene plan
Die_Herrenhaus_Detektive_Kapitel_Schreibvorlage.md            # Chapter template/checklist
Schreibstil_Regeln_8_Jahre_Die_Herrenhaus_Detektive.md        # Writing style rules
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
- **Chapter length**: 1,600-1,900 words
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

- **Chapters 1-13**: Complete (~1,600 words each)
- **Chapters 14-18**: Outlined/sketched (~250-300 words each, need expansion to ~1,600 words)
- **4-Act Structure**: Act 1 (Ch 1-4) Setup, Act 2 (Ch 5-9) Investigation, Act 3 (Ch 10-14) Danger, Act 4 (Ch 15-18) Resolution

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
