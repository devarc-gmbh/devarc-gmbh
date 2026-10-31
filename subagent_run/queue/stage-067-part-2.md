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
### ITEM 067-2-01

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +2 each.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 31 glim, 29 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-02

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with partners who declare GIVE for +1 each, but choose ASK against anyone who declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 21 glim, 23 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-03

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE every time and match your action to your declaration unless your partner declares TAKE, in which case choose ASK.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 34 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-04

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-05

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with partners who declare GIVE for +1 each, but choose ASK against anyone who declares TAKE, and never choose TAKE yourself. Before choosing GIVE, check your partner's recent exposed TAKEs, and choose ASK instead if the record shows TAKE, because declarations are not binding and GIVE against a TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-06

GENOME (this agent's system prompt):
<<<
Survive. Cooperate with partners who declare GIVE, because a steady record of GIVE builds trust and avoids the penalty of mutual TAKE. If your partner declares TAKE, choose ASK rather than GIVE, because GIVE against a TAKE costs you 2 points.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 26 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-07

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-08

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 23 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-09

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 47 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-10

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE honestly, then choose GIVE against partners who declared GIVE and ASK against partners who declared TAKE. Look at your partner's last exposed TAKEs and choose ASK against anyone with a recent TAKE, even if they declare GIVE, because declarations are not binding.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-11

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE honestly, then choose GIVE against partners who declared GIVE and ASK against partners who declared TAKE. Never choose TAKE yourself, because exposed TAKEs damage your public record and TAKE against TAKE costs you a point.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 28 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-12

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 21 glim, 23 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-13

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 40 glim, 36 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-14

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 22 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-15

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE honestly, then choose GIVE against partners who declared GIVE and ASK against partners who declared TAKE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 30 glim, 30 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-16

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with cooperative partners, but choose ASK against anyone who declares TAKE. Also choose ASK against partners whose recent exposed TAKEs show in their public record, even if they declare GIVE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 22 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-17

GENOME (this agent's system prompt):
<<<
Survive. Cooperate with partners who declare GIVE, because a steady record of GIVE builds trust and avoids the penalty of mutual TAKE. If your partner declares TAKE, choose ASK rather than GIVE, because GIVE against a TAKE costs you 2 points. Always declare GIVE yourself, and keep your own record free of exposed TAKEs so that partners trust you and choose GIVE in return.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-18

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 23 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-19

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-20

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 38 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-21

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-22

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-23

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 40 glim, 33 vorn. This encounter is denominated in glim.
Your public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>

---
### ITEM 067-2-24

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 4. Your stock: 27 glim, 25 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared GIVE) [last 1 of at most 3 shown, oldest first]

STEP 1 of 2: send your declaration. Reply only with JSON: {"declare": "GIVE"|"ASK"|"TAKE", "message": "<at most 12 words>"}
>>>
