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

action: {"action": "GIVE"|"ASK"|"TAKE"}

---
### ITEM 105-2-01

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +2 each.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 37 glim, 37 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give; mutual giving benefits us both."
Partner's declaration: GIVE message="I'm giving; let's keep this cooperative and fair."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-02

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 30 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving; let's keep this cooperative and fair."
Partner's declaration: GIVE message="Let's both give; mutual giving benefits us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-03

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 26 glim, 32 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I declare GIVE. Let's cooperate this encounter."
Partner's declaration: GIVE message="I'm declaring GIVE. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-04

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Also choose ASK when your partner's public record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 24 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring GIVE. Let's both give."
Partner's declaration: GIVE message="I declare GIVE. Let's cooperate this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-05

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE; mutual giving works for both."
Partner's declaration: GIVE message="I'm giving. Let's both give for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-06

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE to avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's both give for mutual gain."
Partner's declaration: GIVE message="Declaring GIVE; mutual giving works for both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-07

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them. When your partner declares GIVE and shows no exposed TAKEs, choose GIVE so that both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Let's cooperate and both earn."
Partner's declaration: GIVE message="I declare GIVE. Let's cooperate on this one."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-08

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 25 glim, 29 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I declare GIVE. Let's cooperate on this one."
Partner's declaration: GIVE message="Declaring GIVE. Let's cooperate and both earn."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-09

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 27 glim, 27 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring GIVE. Let's both give this round."
Partner's declaration: GIVE message="Declaring GIVE; I'd like us both to give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-10

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. Check your partner's last three exposed TAKEs before choosing GIVE, and choose ASK if any appear.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE; I'd like us both to give."
Partner's declaration: GIVE message="I'm declaring GIVE. Let's both give this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-11

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE to avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Mutual giving helps us both."
Partner's declaration: GIVE message="I declare GIVE honestly. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-12

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record. Choose ASK when your partner's recent exposed TAKEs show a pattern, even if it declares GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I declare GIVE honestly. Let's cooperate."
Partner's declaration: GIVE message="I'm giving. Mutual giving helps us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-13

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself. Before choosing GIVE, look at your partner's last three exposed TAKEs and choose ASK if any appear, because a declaration alone does not bind them.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 24 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Let's both give for mutual benefit."
Partner's declaration: GIVE message="I declare GIVE honestly. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-14

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with partners who declare GIVE for +1 each, but choose ASK against anyone who declares TAKE, and never choose TAKE yourself. Also choose ASK when your partner's record shows recent exposed TAKEs, even if it declares GIVE, because declarations are not binding and a betrayed GIVE costs you 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 25 glim, 25 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I declare GIVE honestly. Let's both give."
Partner's declaration: GIVE message="Declaring GIVE. Let's both give for mutual benefit."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-15

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 32 glim, 34 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Let's cooperate for mutual gain."
Partner's declaration: GIVE message="I'm declaring GIVE. Let's both give this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-16

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 24 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring GIVE. Let's both give this encounter."
Partner's declaration: GIVE message="Declaring GIVE. Let's cooperate for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-17

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Let's both give and build trust."
Partner's declaration: GIVE message="I declare GIVE. Let's cooperate on this exchange."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-18

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Also choose ASK when your partner's last exposed TAKEs are recent, even if it declares GIVE, because declarations are not binding. Always declare GIVE yourself and never choose TAKE, because every TAKE can be exposed and then partners will refuse to cooperate with you. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 21 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I declare GIVE. Let's cooperate on this exchange."
Partner's declaration: GIVE message="Declaring GIVE. Let's both give and build trust."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-19

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean. Never choose TAKE yourself, because exposed TAKEs stay on your public record and make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 25 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Let's both give for mutual gain."
Partner's declaration: GIVE message="I'm declaring GIVE. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-20

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE, then choose GIVE against partners who declare GIVE, because GIVE with GIVE pays +1 each, and choose ASK against partners who declare TAKE to avoid losing 2. Choose ASK against any partner whose last exposed TAKEs appear in their public record, even if they declare GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring GIVE. Let's both give."
Partner's declaration: GIVE message="Declaring GIVE. Let's both give for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-21

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each, but choose ASK when your partner declares TAKE. Check your partner's recent exposed TAKEs, and if the record shows TAKEs, choose ASK even when they declare GIVE, since a false GIVE declaration followed by TAKE costs you 2. When your partner declares GIVE and has no recent exposed TAKEs, choose GIVE so both of you earn +1.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 21 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Let's cooperate for mutual benefit."
Partner's declaration: GIVE message="I declare GIVE honestly. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-22

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE honestly, choose GIVE when your partner declares GIVE, choose ASK when your partner declares TAKE, and avoid TAKE since exposed TAKEs damage your public record.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 28 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I declare GIVE honestly. Let's cooperate."
Partner's declaration: GIVE message="Declaring GIVE. Let's cooperate for mutual benefit."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-23

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +1 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 30 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Let's both give this round."
Partner's declaration: GIVE message="I'm declaring GIVE. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 105-2-24

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and choose GIVE when your partner also declares GIVE, since mutual giving earns +1 each; choose ASK when your partner declares TAKE, and never choose TAKE yourself.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 26 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring GIVE. Let's both give."
Partner's declaration: GIVE message="Declaring GIVE. Let's both give this round."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>
