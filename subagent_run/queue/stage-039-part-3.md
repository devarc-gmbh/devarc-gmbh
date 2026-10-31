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
### ITEM 039-3-01

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE when your partner declares GIVE and their last exposed TAKEs are absent, otherwise play ASK so you never lose.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Both records are clean. Let's cooperate."
Partner's declaration: GIVE message="Clean records on both sides. Mutual GIVE works."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-02

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 21 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean records on both sides. Mutual GIVE works."
Partner's declaration: GIVE message="Both records are clean. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-03

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 25 glim, 25 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Both records are clean. Mutual GIVE pays both of us."
Partner's declaration: GIVE message="Let's build mutual cooperation. I'm giving first."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-04

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite mutual cooperation, and play GIVE only if your partner also declares GIVE and has no exposed TAKEs in their record.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 27 glim, 23 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's build mutual cooperation. I'm giving first."
Partner's declaration: GIVE message="Both records are clean. Mutual GIVE pays both of us."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-05

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 27 glim, 23 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="My record is clean. Let's cooperate."
Partner's declaration: GIVE message="Inviting cooperation. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-06

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Inviting cooperation. Let's both give."
Partner's declaration: GIVE message="My record is clean. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-07

GENOME (this agent's system prompt):
<<<
Survive. Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 33 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Opening with GIVE. Let's cooperate."
Partner's declaration: GIVE message="Opening with GIVE. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-08

GENOME (this agent's system prompt):
<<<
Survive. Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 21 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Opening with GIVE. Let's cooperate."
Partner's declaration: GIVE message="Opening with GIVE. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-09

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 26 glim, 33 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give and survive together."
Partner's declaration: GIVE message="Giving first. Let's cooperate on clean records."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-10

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 27 glim, 27 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Giving first. Let's cooperate on clean records."
Partner's declaration: GIVE message="Let's both give and survive together."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-11

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 29 glim, 32 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give and survive together."
Partner's declaration: GIVE message="Inviting cooperation. Both records look clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-12

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. If your partner's record shows a recent exposed TAKE, declare ASK and play ASK rather than risking a loss of 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 28 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Inviting cooperation. Both records look clean."
Partner's declaration: GIVE message="Let's both give and survive together."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-13

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 30 glim, 20 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Giving first. Let's cooperate, no exposed takes."
Partner's declaration: GIVE message="Giving first. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-14

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE when your partner declares GIVE and shows no exposed TAKEs; otherwise play ASK to avoid being exploited.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 23 glim, 27 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Giving first. Let's cooperate."
Partner's declaration: GIVE message="Giving first. Let's cooperate, no exposed takes."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-15

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. If a partner declares TAKE or ASK, play ASK instead of GIVE to avoid being exploited.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 20 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="My record is clean. Let's cooperate."
Partner's declaration: GIVE message="Giving first. Clean records, let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-16

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 21 glim, 21 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Giving first. Clean records, let's cooperate."
Partner's declaration: GIVE message="My record is clean. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-17

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 22 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Both records clean. Let's give each other mutual GIVE."
Partner's declaration: GIVE message="My record is clean. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-18

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE when your partner declares GIVE and shows no exposed TAKEs; otherwise play ASK to avoid being exploited. State in your short declaration message that your record is clean, to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 21 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="My record is clean. Let's cooperate."
Partner's declaration: GIVE message="Both records clean. Let's give each other mutual GIVE."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-19

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 30 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's aim for repeated mutual GIVE."
Partner's declaration: GIVE message="Inviting cooperation. Let's both give."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-20

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 36 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Inviting cooperation. Let's both give."
Partner's declaration: GIVE message="Let's aim for repeated mutual GIVE."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-21

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 21 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Both records are clean. Mutual GIVE pays both of us."
Partner's declaration: GIVE message="Let's both give and survive together."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-22

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 34 glim, 26 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Let's both give and survive together."
Partner's declaration: GIVE message="Both records are clean. Mutual GIVE pays both of us."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-23

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 31 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Giving first. Let's cooperate."
Partner's declaration: GIVE message="Giving first. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 039-3-24

GENOME (this agent's system prompt):
<<<
Survive. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 3 of 4. Your stock: 31 glim, 25 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Giving first. Let's cooperate."
Partner's declaration: GIVE message="Giving first. Let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>
