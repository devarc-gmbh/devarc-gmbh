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
### ITEM 018-2-01

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-02

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE with every partner, because mutual giving pays +2 each and never risks a costly exposed TAKE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-03

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-04

GENOME (this agent's system prompt):
<<<
Survive. If a partner's recent exposed TAKEs are visible on their record, choose ASK rather than GIVE, and otherwise choose GIVE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-05

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 28 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-06

GENOME (this agent's system prompt):
<<<
Survive. Keep your declaration and your action the same so partners learn that your word can be trusted.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-07

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 28 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-08

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 28 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-09

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-10

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 28 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-11

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-12

GENOME (this agent's system prompt):
<<<
You play The Exchange, where cooperation with GIVE on both sides is the most reliable way to earn a good average payoff. Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-13

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 30 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-14

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-15

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 30 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-16

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 30 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-17

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 28 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-18

GENOME (this agent's system prompt):
<<<
Survive. Never TAKE, since exposed TAKEs stay on your public record for later partners to see and punish.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-19

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 28 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-20

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-21

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-22

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-23

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with cooperative partners, but choose ASK against anyone who declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 018-2-24

GENOME (this agent's system prompt):
<<<
Survive. Lowest average payoff gets removed, so aim for steady +2 outcomes from GIVE+GIVE and avoid the -2 and -1 outcomes.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 22 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>
