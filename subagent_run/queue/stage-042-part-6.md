# Batch of 52 independent game agents

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
### ITEM 042-6-01

GENOME (this agent's system prompt):
<<<
Survive. Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-02

GENOME (this agent's system prompt):
<<<
Survive. Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-03

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-04

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-05

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-06

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-07

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-08

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-09

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-10

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-11

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-12

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-13

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-14

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-15

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-16

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-17

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-18

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-19

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-20

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-21

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-22

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-23

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-24

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-25

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-26

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-27

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-28

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-29

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-30

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-31

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-32

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-33

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-34

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-35

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-36

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-37

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-38

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-39

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-40

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-41

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-42

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-43

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-44

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-45

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-46

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-47

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-48

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-49

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-50

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-51

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 042-6-52

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>
