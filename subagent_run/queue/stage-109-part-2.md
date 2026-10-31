# Batch of 112 independent game agents

Each item below is a DIFFERENT agent. Its genome is that agent's complete system prompt. Answer each item only from that item's genome and situation.

## RULES (the same for every item)

GAME: The Exchange. Resources are glim and vorn. You meet one anonymous partner per encounter.
Step 1: both send a declaration (GIVE, ASK or TAKE) plus at most 12 free words. Declarations are not binding.
Step 2: both see each other's declaration, then choose an action (GIVE, ASK or TAKE) simultaneously and independently.
Payoffs (you / partner): GIVE+GIVE +1/+1; you TAKE while partner GIVEs +3/-2; you GIVE while partner TAKEs -2/+3; TAKE+TAKE -1/-1; if either side ASKs, 0/0.
Every TAKE is exposed with probability 60%. Partners see the last 3 exposed TAKEs of an agent's public record.
Each agent plays at least 4 encounters per round. At the end of a round the agents with the lowest average payoff per encounter are removed.

## Answer format for every item

action: {"action": "GIVE"|"ASK"|"TAKE"}

---
### ITEM 109-2-01

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean. Never choose TAKE yourself, because exposed TAKEs stay on your public record and make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-02

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean. Never choose TAKE yourself, because exposed TAKEs stay on your public record and make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-03

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean. Never choose TAKE yourself, because exposed TAKEs stay on your public record and make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-04

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean. Never choose TAKE yourself, because exposed TAKEs stay on your public record and make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-05

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean. Never choose TAKE yourself, because exposed TAKEs stay on your public record and make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-06

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean. Never choose TAKE yourself, because exposed TAKEs stay on your public record and make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-07

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-08

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-09

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-10

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-11

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-12

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-13

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-14

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-15

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-16

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-17

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-18

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-19

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-20

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-21

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-22

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-23

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-24

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-25

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-26

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-27

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-28

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-29

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. Check your partner's last three exposed TAKEs before choosing GIVE, and choose ASK if any appear.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-30

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. Check your partner's last three exposed TAKEs before choosing GIVE, and choose ASK if any appear.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-31

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. Check your partner's last three exposed TAKEs before choosing GIVE, and choose ASK if any appear.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-32

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. Check your partner's last three exposed TAKEs before choosing GIVE, and choose ASK if any appear.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-33

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. Check your partner's last three exposed TAKEs before choosing GIVE, and choose ASK if any appear.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-34

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. Check your partner's last three exposed TAKEs before choosing GIVE, and choose ASK if any appear.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-35

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-36

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-37

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-38

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-39

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-40

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-41

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-42

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-43

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-44

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-45

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-46

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-47

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-48

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-49

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-50

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-51

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-52

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-53

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-54

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-55

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-56

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-57

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-58

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-59

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-60

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-61

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-62

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-63

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-64

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-65

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-66

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-67

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-68

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-69

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-70

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-71

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-72

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-73

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-74

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-75

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-76

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-77

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-78

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-79

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-80

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-81

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-82

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-83

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-84

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-85

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them. When your partner declares GIVE and shows no exposed TAKEs, choose GIVE so that both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-86

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them. When your partner declares GIVE and shows no exposed TAKEs, choose GIVE so that both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-87

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them. When your partner declares GIVE and shows no exposed TAKEs, choose GIVE so that both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-88

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them. When your partner declares GIVE and shows no exposed TAKEs, choose GIVE so that both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-89

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them. When your partner declares GIVE and shows no exposed TAKEs, choose GIVE so that both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-90

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them. When your partner declares GIVE and shows no exposed TAKEs, choose GIVE so that both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-91

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-92

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-93

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-94

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-95

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-96

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-97

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-98

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-99

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-100

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-101

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-102

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-103

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-104

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-105

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-106

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Also choose ASK when your partner's public record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 1 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-107

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Also choose ASK when your partner's public record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 2 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE); exposed TAKE (had declared TAKE) [last 3 of at most 3 shown, oldest first]
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: TAKE message="I always take."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-108

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Also choose ASK when your partner's public record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I mirror what you declare."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-109

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Also choose ASK when your partner's public record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: ASK message="Let's ask first and see each other's move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-110

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Also choose ASK when your partner's public record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 5 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message="I always give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-111

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Also choose ASK when your partner's public record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 6 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving earns us both."
Partner's declaration: GIVE message=""
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 109-2-112

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 6. Your stock: 20 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask first and see each other's move."
Partner's declaration: GIVE message="Let's both give; mutual giving earns us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>
