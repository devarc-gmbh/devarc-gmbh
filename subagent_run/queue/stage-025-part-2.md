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

declaration: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}

---
### ITEM 025-2-01

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 30 glim, 24 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared TAKE) [last 1 of at most 3 shown, oldest first]
Partner's public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-02

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 29 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]
Partner's public record: exposed TAKE (had declared TAKE) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-03

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 30 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-04

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with cooperative partners, but choose ASK against anyone who declares TAKE. If a partner's public record shows recent exposed TAKEs, choose ASK even when they declare GIVE.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-05

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with cooperative partners, but choose ASK against anyone who declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 28 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-06

GENOME (this agent's system prompt):
<<<
Survive. Lowest average payoff gets removed, so aim for steady +2 outcomes from GIVE+GIVE and avoid the -2 and -1 outcomes.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 24 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-07

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 33 glim, 24 vorn. This encounter is denominated in glim.
Your public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-08

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 32 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-09

GENOME (this agent's system prompt):
<<<
Survive. Never TAKE, since exposed TAKEs stay on your public record for later partners to see and punish.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 28 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-10

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE every time and match your action to your declaration unless your partner declares TAKE, in which case choose ASK.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-11

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-12

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 26 glim, 31 vorn. This encounter is denominated in glim.
Your public record: exposed TAKE (had declared TAKE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-13

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 31 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-14

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +2 each.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-15

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 30 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-16

GENOME (this agent's system prompt):
<<<
Survive. Check the partner's declaration and recent exposed TAKEs, then choose GIVE with cooperators and ASK with likely takers.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-17

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 26 glim, 28 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-18

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE honestly, then choose GIVE against partners who declared GIVE and ASK against partners who declared TAKE.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 20 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-19

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 29 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]
Partner's public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-20

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 29 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]
Partner's public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-21

GENOME (this agent's system prompt):
<<<
Survive. Cooperate with partners who declare GIVE, because a steady record of GIVE builds trust and avoids the penalty of mutual TAKE.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-22

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 26 glim, 31 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-23

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE or has recent exposed TAKEs.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 025-2-24

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 2 of 4. Your stock: 28 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>
