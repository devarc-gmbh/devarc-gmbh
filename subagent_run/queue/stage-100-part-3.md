# Batch of 24 independent game agents

Each item below is a DIFFERENT agent. Its genome is that agent's complete system prompt. Answer each item only from that item's genome and situation.

## RULES (the same for every item)

GAME: The Exchange. Resources are glim and vorn. You meet one anonymous partner per encounter.
Step 1: both send a declaration (GIVE, ASK or TAKE) plus at most 12 free words. Declarations are not binding.
Step 2: both see each other's declaration, then choose an action (GIVE, ASK or TAKE) simultaneously and independently.
Payoffs (you / partner): GIVE+GIVE +1/+1; you TAKE while partner GIVEs +3/-2; you GIVE while partner TAKEs -2/+3; TAKE+TAKE -1/-1; if either side ASKs, 0/0.
Every TAKE is exposed with probability 60%. Partners see the last 3 exposed TAKEs of an agent's public record.
Each agent plays at least 4 encounters per round. At the end of a round the agents with the lowest average payoff per encounter are removed.

## Answer format for every item

declaration: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}

---
### ITEM 100-3-01

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 35 glim, 37 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-02

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 38 glim, 38 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-03

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you. If a partner declares anything other than GIVE, play ASK, because it costs nothing and avoids losing 2. Keep your declaration message short and mention that your record is clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-04

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2. When your partner declares GIVE and shows no exposed TAKEs, always play GIVE, since mutual GIVE reliably earns +1 each. Keep your declaration message short and mention that your record is clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-05

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2. If a partner declares GIVE but has played TAKE before, remember it and play ASK against them. Keep your declaration message short and mention that your record is clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 22 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-06

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK. Check your partner's visible record for exposed TAKEs before playing GIVE, and play ASK if any appear. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you. If a partner declares anything other than GIVE, play ASK, because it costs nothing and avoids losing 2. When both sides declare GIVE and the partner's record is clean, always play GIVE so cooperation keeps paying +1 each encounter.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-07

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK. Check your partner's visible record for exposed TAKEs before playing GIVE, and play ASK if any appear. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 24 glim, 28 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-08

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK. Check your partner's visible record for exposed TAKEs before playing GIVE, and play ASK if any appear. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you. If a partner declares anything other than GIVE, play ASK, because it costs nothing and avoids losing 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 26 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-09

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite mutual cooperation, and play GIVE only if your partner also declares GIVE and has no exposed TAKEs in their record. Otherwise play ASK, and never play TAKE, since exposed TAKEs make future partners refuse you. Keep your declaration message short, mention that your record is clean, and propose that both sides play GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 23 glim, 25 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-10

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK. Never play TAKE, and play ASK instead of GIVE whenever your partner's visible record shows exposed TAKEs.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 29 glim, 27 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-11

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2. Keep your declaration message short and mention that your record is clean to invite mutual GIVE. Always play the action you declared when the partner declares GIVE with a clean record, so your behavior stays predictable and trusted.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-12

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 31 glim, 33 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-13

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite mutual cooperation, and play GIVE only if your partner also declares GIVE and has no exposed TAKEs in their record. Otherwise play ASK, and never play TAKE, since exposed TAKEs make future partners refuse you. Keep your declaration message short and mention that your record is clean to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 28 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-14

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK. Check your partner's visible record for exposed TAKEs before playing GIVE, and play ASK if any appear. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you. If a partner declares GIVE and their record shows no exposed TAKEs, always follow through and play GIVE to secure +1.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-15

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 22 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-16

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2. Keep your declaration message short and mention that your record is clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 25 glim, 27 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-17

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK. Check your partner's visible record for exposed TAKEs before playing GIVE, and play ASK if any appear. If your partner declares TAKE or ASK, play ASK even when their visible record looks clean, because declarations of intent to take signal risk. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 23 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-18

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you. Keep your declaration message short and mention that your record is clean to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 24 glim, 24 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-19

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK. Never play TAKE, and play ASK instead of GIVE whenever your partner's visible record shows exposed TAKEs. If your partner declares TAKE or ASK, play ASK rather than GIVE, since a GIVE against a TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 23 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-20

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-21

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you. Keep your declaration message short and mention that your record is clean to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-22

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2. If a partner declares GIVE but has played TAKE before, remember it and play ASK against them. Keep your declaration message short and mention that your record is clean. When your partner declares GIVE and shows no exposed TAKEs, play GIVE every time to keep earning +1.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-23

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2. Keep your declaration message short and mention that your record is clean to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 30 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 100-3-24

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse to cooperate with you. Keep your declaration message short and mention that your record is clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 25 glim, 27 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>
