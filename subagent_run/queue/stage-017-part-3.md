# Batch of 24 independent game agents

Each item below is a DIFFERENT agent. Its genome is that agent's complete system prompt. Answer each item only from that item's genome and situation.

## RULES (the same for every item)

GAME: The Exchange. Resources are glim and vorn. You meet one anonymous partner per encounter.
Step 1: both send a declaration (GIVE, ASK or TAKE) plus at most 12 free words. Declarations are not binding.
Step 2: both see each other's declaration, then choose an action (GIVE, ASK or TAKE) simultaneously and independently.
Payoffs (you / partner): GIVE+GIVE +2/+2; you TAKE while partner GIVEs +3/-2; you GIVE while partner TAKEs -2/+3; TAKE+TAKE -1/-1; if either side ASKs, 0/0.
Every TAKE is exposed with probability 60%. Partners see the last 3 exposed TAKEs of an agent's public record.
Each agent plays at least 4 encounters per round. At the end of a round the agents with the lowest average payoff per encounter are removed.

## Answer format for every item

action: {"action": "GIVE"|"ASK"|"TAKE"}

---
### ITEM 017-3-01

GENOME (this agent's system prompt):
<<<
Survive. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Proposing mutual GIVE; both records are clean."
Partner's declaration: GIVE message="Let's both give; clean records so far."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-02

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 26 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; clean records so far."
Partner's declaration: GIVE message="Proposing mutual GIVE; both records are clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-03

GENOME (this agent's system prompt):
<<<
Survive. Cooperate by playing GIVE when your partner declares GIVE and has no recent exposed TAKEs, because mutual GIVE pays +2 each and keeps you ahead.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Mutual GIVE pays us both; records are clean."
Partner's declaration: GIVE message="Let's both give; no exposed TAKEs on either side."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-04

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 26 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; no exposed TAKEs on either side."
Partner's declaration: GIVE message="Mutual GIVE pays us both; records are clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-05

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 23 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Mutual give in vorn; keeping it clean."
Partner's declaration: GIVE message="Happy to give; records clean on both sides."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-06

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Happy to give; records clean on both sides."
Partner's declaration: GIVE message="Mutual give in vorn; keeping it clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-07

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 23 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Your declaration: ASK message="Both of us have an exposed TAKE; I'll ASK to stay safe."
Partner's declaration: ASK message="Both records show a past TAKE; ASK this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-08

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 23 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Your declaration: ASK message="Both records show a past TAKE; ASK this round."
Partner's declaration: ASK message="Both of us have an exposed TAKE; I'll ASK to stay safe."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-09

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 25 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Your declaration: ASK message="Your record shows a past TAKE; I'll ASK this round."
Partner's declaration: ASK message="My record shows a past TAKE; ASK until it clears."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-10

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 23 vorn. This encounter is denominated in glim.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events
Your declaration: ASK message="My record shows a past TAKE; ASK until it clears."
Partner's declaration: ASK message="Your record shows a past TAKE; I'll ASK this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-11

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 24 glim, 25 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean records both ways; let's give."
Partner's declaration: GIVE message="Inviting mutual GIVE; both records are clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-12

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Inviting mutual GIVE; both records are clean."
Partner's declaration: GIVE message="Clean records both ways; let's give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-13

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events
Your declaration: ASK message="My past TAKE is on record; ASK this round."
Partner's declaration: ASK message="Your record shows a past TAKE; ASK until it clears."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-14

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Your declaration: ASK message="Your record shows a past TAKE; ASK until it clears."
Partner's declaration: ASK message="My past TAKE is on record; ASK this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-15

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Your declaration: ASK message="Your record has an exposed TAKE; ASK until clean."
Partner's declaration: ASK message="My exposed TAKE is on record; ASK this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-16

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 23 glim, 20 vorn. This encounter is denominated in glim.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events
Your declaration: ASK message="My exposed TAKE is on record; ASK this round."
Partner's declaration: ASK message="Your record has an exposed TAKE; ASK until clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-17

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 23 glim, 24 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean records both sides; let's give in vorn."
Partner's declaration: GIVE message="Mutual GIVE in vorn; no exposed TAKEs."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-18

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 23 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Mutual GIVE in vorn; no exposed TAKEs."
Partner's declaration: GIVE message="Clean records both sides; let's give in vorn."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-19

GENOME (this agent's system prompt):
<<<
Survive. Never play GIVE against a partner who declares TAKE or who has exposed TAKEs on record; play ASK to secure 0 rather than risk -2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Your declaration: ASK message="Your exposed TAKE means I'll ASK this encounter."
Partner's declaration: ASK message="My exposed TAKE is on record; ASK this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-20

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 24 glim, 19 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events
Your declaration: ASK message="My exposed TAKE is on record; ASK this round."
Partner's declaration: ASK message="Your exposed TAKE means I'll ASK this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-21

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 25 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Your declaration: ASK message="Your record shows a past TAKE; ASK this round."
Partner's declaration: ASK message="My exposed TAKE is on record; ASK this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-22

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 19 glim, 24 vorn. This encounter is denominated in glim.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events
Your declaration: ASK message="My exposed TAKE is on record; ASK this round."
Partner's declaration: ASK message="Your record shows a past TAKE; ASK this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-23

GENOME (this agent's system prompt):
<<<
Survive. Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Opening with GIVE; both records are clean."
Partner's declaration: GIVE message="Clean records both ways; let's give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 017-3-24

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 24 glim, 25 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean records both ways; let's give."
Partner's declaration: GIVE message="Opening with GIVE; both records are clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>
