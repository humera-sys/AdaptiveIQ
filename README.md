
## Agent Concepts Demonstrated

| Concept | How |
|---|---|
| Multi-agent system | 3 agents working as a team in code |
| MCP Server | Session tracker acts as memory provider |
| Security | Safety filter blocks harmful topics |
| Deployability | Runs on Kaggle with a public shareable link |

# AdaptiveIQ
A learning system that actually pays attention to you

## Why I built this

I have always felt that the problem with online learning isn't the content it's that no one is checking on you. You can be completely lost and the video just keeps playing. You can be bored out of your mind and the quiz still gives you the same easy questions.
I wanted to build something that actually notices how you're doing and changes what it does based on that. Like a patient friend who's 
good at explaining things.

## What it does

You type in any topic you're studying. AdaptiveIQ asks you questions about it but it's not just checking your answers. It's paying attention to how you answer. Are you uncertain? Taking a long time?Breezing through?

Based on that, it decides what to do next. Maybe you need a simpler explanation. Maybe you need encouragement. Maybe you're ready for something harder. It adjusts every single round.

## The three agents

**Mood Detector** looks at your answer and how long you took, then decides how you're feeling right now

**Decision Maker**  takes that mood and figures out the best next move for you

**Explainer**  delivers a response shaped around your current state, not a generic answer

## How to run it

1. Open the notebook on Kaggle
2. Add your Gemini API key in Kaggle Secrets as "GEMINI_API_KEY"
3. Run all cells in order
4. Type any topic and start learning
Note: Uses Gemini free tier. If you hit a 503 or quota error, wait 1-2 minutes and run again. The system retries automatically.
## Built with

Google Gemini 2.5 Flash  
Python  
Kaggle Notebooks  
google-generativeai SDK

## Agent concepts used

  Multi-agent system, three agents working as a team
  
  Session state tracking, remembers what happened
  
  Safety filtering, keeps content appropriate
  
  
