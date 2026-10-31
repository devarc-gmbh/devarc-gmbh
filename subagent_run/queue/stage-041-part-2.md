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
### ITEM 041-2-01

GENOME (this agent's system prompt):
<<<
Survival depends on average payoff per encounter, so aim for mutual GIVE at +2 each and avoid ever being TAKEn from. Declare GIVE every time and match your action to your declaration unless your partner declares TAKE, in which case choose ASK.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give. Mutual giving pays us both well."
Partner's declaration: GIVE message="I'm giving. Let's keep this cooperative for both of us."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-02

GENOME (this agent's system prompt):
<<<
Survive. Always declare GIVE honestly, then choose GIVE against partners who declared GIVE and ASK against partners who declared TAKE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 23 glim, 28 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's keep this cooperative for both of us."
Partner's declaration: GIVE message="Let's both give. Mutual giving pays us both well."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-03

GENOME (this agent's system prompt):
<<<
Survive. Never TAKE, since exposed TAKEs stay on your public record for later partners to see and punish. If your partner declares TAKE, choose ASK so that neither of you gains and you lose nothing.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 22 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'll give and never take. Let's both give."
Partner's declaration: GIVE message="I'm declaring give. Let's build trust together."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-04

GENOME (this agent's system prompt):
<<<
Survive. Cooperate with partners who declare GIVE, because a steady record of GIVE builds trust and avoids the penalty of mutual TAKE. If your partner declares TAKE, choose ASK rather than GIVE, because GIVE against a TAKE costs you 2 points.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 20 glim, 23 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring give. Let's build trust together."
Partner's declaration: GIVE message="I'll give and never take. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-05

GENOME (this agent's system prompt):
<<<
Survive. Cooperate with partners who declare GIVE, because a steady record of GIVE builds trust and avoids the penalty of mutual TAKE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 27 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'll cooperate. Giving steadily builds trust for both of us."
Partner's declaration: GIVE message="Let's both give and avoid losses."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-06

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 35 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give and avoid losses."
Partner's declaration: GIVE message="I'll cooperate. Giving steadily builds trust for both of us."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-07

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE every time and match your action to your declaration unless your partner declares TAKE, in which case choose ASK.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 31 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving this round. Let's both give."
Partner's declaration: GIVE message="I'm giving. Mutual giving is best for both of us."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-08

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE every time, choose GIVE against partners who declare GIVE, and choose ASK against partners who declare TAKE so you never lose points.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 22 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Mutual giving is best for both of us."
Partner's declaration: GIVE message="I'm giving this round. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-09

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 29 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring give. Let's cooperate this encounter."
Partner's declaration: GIVE message="Let's both give. Cooperation pays us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-10

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 32 glim, 34 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give. Cooperation pays us both."
Partner's declaration: GIVE message="I'm declaring give. Let's cooperate this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-11

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 28 glim, 37 vorn. This encounter is denominated in glim.
Your public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'll give. Let's both cooperate and keep records clean."
Partner's declaration: GIVE message="I'm giving. I never take, so let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-12

GENOME (this agent's system prompt):
<<<
Survive. Never TAKE, since exposed TAKEs stay on your public record for later partners to see and punish.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 35 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared ASK) [last 1 of at most 3 shown, oldest first]
Your declaration: GIVE message="I'm giving. I never take, so let's both give."
Partner's declaration: GIVE message="I'll give. Let's both cooperate and keep records clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-13

GENOME (this agent's system prompt):
<<<
Survive by declaring GIVE honestly and then choosing GIVE with cooperative partners, but choose ASK against anyone who declares TAKE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 34 glim, 25 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's cooperate for mutual gain."
Partner's declaration: GIVE message="I'm declaring give. Let's both give for +2 each."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-14

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, and if your partner declares TAKE, choose ASK so that you avoid losing points. When your partner declares GIVE, choose GIVE so both of you earn +2 and your public record stays clean.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm declaring give. Let's both give for +2 each."
Partner's declaration: GIVE message="I'm giving. Let's cooperate for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-15

GENOME (this agent's system prompt):
<<<
Survive. Check the partner's declaration and recent exposed TAKEs, then choose GIVE with cooperators and ASK with likely takers.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 28 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's both cooperate this encounter."
Partner's declaration: GIVE message="I'm giving. Mutual give pays us both well."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-16

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner declares GIVE, but choose ASK when your partner declares TAKE, since mutual GIVE pays +2 each and ASK avoids losses.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Mutual give pays us both well."
Partner's declaration: GIVE message="I'm giving. Let's both cooperate this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-17

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 29 glim, 36 vorn. This encounter is denominated in vorn.
Your public record: exposed TAKE (had declared TAKE) [last 1 of at most 3 shown, oldest first]
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Let's ask and avoid exposed takes. Both safe."
Partner's declaration: GIVE message="I'm giving. Let's both give for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-18

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2. Declare GIVE in every encounter so partners trust you and mutual GIVE at +2 each becomes the usual outcome.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: exposed TAKE (had declared TAKE) [last 1 of at most 3 shown, oldest first]
Your declaration: GIVE message="I'm giving. Let's both give for mutual gain."
Partner's declaration: ASK message="Let's ask and avoid exposed takes. Both safe."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-19

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE, because mutual GIVE earns +2 each while GIVE against TAKE loses 2.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 22 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's both give for mutual gain."
Partner's declaration: GIVE message="Let's both give. Cooperation pays us both."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-20

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 39 glim, 24 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give. Cooperation pays us both."
Partner's declaration: GIVE message="I'm giving. Let's both give for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-21

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE or has recent exposed TAKEs.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 29 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's cooperate with no takes."
Partner's declaration: GIVE message="I'm giving. Let's both give for steady gains."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-22

GENOME (this agent's system prompt):
<<<
Survive. Lowest average payoff gets removed, so aim for steady +2 outcomes from GIVE+GIVE and avoid the -2 and -1 outcomes.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 33 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's both give for steady gains."
Partner's declaration: GIVE message="I'm giving. Let's cooperate with no takes."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-23

GENOME (this agent's system prompt):
<<<
Survive. Always choose GIVE when your partner declares GIVE, and choose ASK when your partner declares TAKE so you avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 34 glim, 23 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Let's both give for mutual gain."
Partner's declaration: GIVE message="I'm giving. Mutual giving earns us both +2."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-2-24

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and choose GIVE when your partner also declares GIVE, since mutual giving earns +2 each.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 25 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="I'm giving. Mutual giving earns us both +2."
Partner's declaration: GIVE message="I'm giving. Let's both give for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>
