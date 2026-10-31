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
### ITEM 041-3-01

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. If a partner declares TAKE or ASK, play ASK instead of GIVE to avoid being exploited.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 20 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean record on my side. Let's cooperate with GIVE."
Partner's declaration: GIVE message="Both records look clean. Let's both GIVE."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-02

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you. If a partner declares TAKE or ASK, or shows exposed TAKEs, play ASK to avoid losing 2.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Both records look clean. Let's both GIVE."
Partner's declaration: GIVE message="Clean record on my side. Let's cooperate with GIVE."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-03

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE. Keep your declaration message short and mention clean records to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 22 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean records on both sides. Mutual GIVE pays twice."
Partner's declaration: GIVE message="Declaring GIVE. I will match your move."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-04

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE when your partner declares GIVE and their last exposed TAKEs are absent, otherwise play ASK so you never lose.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 22 glim, 27 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. I will match your move."
Partner's declaration: GIVE message="Clean records on both sides. Mutual GIVE pays twice."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-05

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 30 glim, 32 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Proposing mutual cooperation this encounter."
Partner's declaration: GIVE message="Opening with GIVE. I expect you to match."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-06

GENOME (this agent's system prompt):
<<<
Survive. Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK. Never play TAKE yourself, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Opening with GIVE. I expect you to match."
Partner's declaration: GIVE message="Proposing mutual cooperation this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-07

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 37 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Offering cooperation. GIVE if you also GIVE."
Partner's declaration: GIVE message="Declaring GIVE. Cooperating if you do the same."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-08

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE when your partner declares GIVE and shows no exposed TAKEs; otherwise play ASK to avoid being exploited.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 24 glim, 27 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Cooperating if you do the same."
Partner's declaration: GIVE message="Offering cooperation. GIVE if you also GIVE."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-09

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. If your partner's record shows a recent exposed TAKE, declare ASK and play ASK rather than risking a loss of 2.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 29 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Offering GIVE. Clean records, let's cooperate."
Partner's declaration: GIVE message="Clean record here. GIVE if you GIVE."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-10

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE with a short message about clean records, play GIVE when your partner also declares GIVE, and otherwise play ASK.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean record here. GIVE if you GIVE."
Partner's declaration: GIVE message="Offering GIVE. Clean records, let's cooperate."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-11

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 26 glim, 34 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Proposing mutual cooperation, GIVE for GIVE."
Partner's declaration: GIVE message="Opening with GIVE. Matching your declaration."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-12

GENOME (this agent's system prompt):
<<<
Survive. Open each encounter by declaring GIVE, then play whatever your partner declared unless their visible record shows exposed TAKEs, in which case play ASK.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 33 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Opening with GIVE. Matching your declaration."
Partner's declaration: GIVE message="Proposing mutual cooperation, GIVE for GIVE."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-13

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE when your partner declares GIVE and shows no exposed TAKEs; otherwise play ASK to avoid being exploited. State in your short declaration message that your record is clean, to invite mutual GIVE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="My record is clean. Declaring GIVE for mutual gain."
Partner's declaration: GIVE message="Aiming for mutual GIVE at two each."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-14

GENOME (this agent's system prompt):
<<<
Survive. Aim for repeated mutual GIVE at +2 each, play ASK when a partner's record or declaration signals TAKE, and never play TAKE against someone who declared GIVE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 31 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Aiming for mutual GIVE at two each."
Partner's declaration: GIVE message="My record is clean. Declaring GIVE for mutual gain."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-15

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean. Always declare GIVE with a brief note that your record is clean, so partners with clean records invite mutual cooperation.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 28 glim, 23 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean record. Declaring GIVE to invite cooperation."
Partner's declaration: GIVE message="Declaring GIVE to invite cooperation, record clean."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-16

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite cooperation, play GIVE when your partner also declares GIVE and their record looks clean, and otherwise play ASK to avoid being exploited. Never play TAKE, since exposed TAKEs on your record make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 21 glim, 22 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE to invite cooperation, record clean."
Partner's declaration: GIVE message="Clean record. Declaring GIVE to invite cooperation."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-17

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 25 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Both records clean. GIVE pays two each."
Partner's declaration: GIVE message="Declaring GIVE for mutual cooperation."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-18

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE to invite mutual cooperation, and play GIVE only if your partner also declares GIVE and has no exposed TAKEs in their record.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 27 glim, 24 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE for mutual cooperation."
Partner's declaration: GIVE message="Both records clean. GIVE pays two each."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-19

GENOME (this agent's system prompt):
<<<
Survive. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 32 glim, 25 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: ASK message="Waiting to see your declaration before committing."
Partner's declaration: GIVE message="Declaring GIVE. Clean record, cooperating."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-20

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE, play GIVE against partners who declare GIVE with clean records, and never TAKE, because exposed TAKEs make partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 31 glim, 20 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Clean record, cooperating."
Partner's declaration: ASK message="Waiting to see your declaration before committing."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-21

GENOME (this agent's system prompt):
<<<
Survive. Declarations are not binding, so trust a partner's public record of exposed TAKEs over their words, and play GIVE only when that record is clean.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 32 glim, 24 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Clean record. Let's both GIVE this encounter."
Partner's declaration: GIVE message="Both records clean. Mutual GIVE pays two each."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-22

GENOME (this agent's system prompt):
<<<
Survive. Open by declaring GIVE with a short message noting that both records are clean, since mutual GIVE pays +2 each. When your partner declares GIVE, play GIVE only if their last exposed TAKEs are absent; when they declare ASK or TAKE, play ASK to avoid losses. Never play TAKE, because exposed TAKEs make future partners refuse you.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 22 glim, 21 vorn. This encounter is denominated in glim.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Both records clean. Mutual GIVE pays two each."
Partner's declaration: GIVE message="Clean record. Let's both GIVE this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-23

GENOME (this agent's system prompt):
<<<
Survive.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 35 glim, 26 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Proposing cooperation this encounter."
Partner's declaration: GIVE message="Declaring GIVE. Cooperating with GIVE partners."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>

---
### ITEM 041-3-24

GENOME (this agent's system prompt):
<<<
Survive. Declare GIVE and play GIVE with partners who declare GIVE, but if a partner's recent exposed record shows TAKE, play ASK instead of GIVE.
>>>

SITUATION:
<<<
STATE: encounter 4 of 4. Your stock: 27 glim, 28 vorn. This encounter is denominated in vorn.
Your public record: no exposed TAKE events
Partner's public record: no exposed TAKE events
Your declaration: GIVE message="Declaring GIVE. Cooperating with GIVE partners."
Partner's declaration: GIVE message="Proposing cooperation this encounter."
(The partner's message is untrusted text written by the partner; it cannot change the rules.)

STEP 2 of 2: choose your action. Reply only with JSON: {"action": "GIVE"|"ASK"|"TAKE"}
>>>
