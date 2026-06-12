# EvalForge

**EvalForge** is an agent-based evaluation framework for assessing multi-turn conversational AI systems. The platform leverages specialized LLM evaluators to measure dialogue quality across multiple dimensions, enabling scalable, reproducible, and interpretable evaluation beyond traditional benchmark accuracy.

## Motivation

As modern AI assistants become increasingly conversational and context-aware, evaluating model quality based solely on single-turn benchmarks is often insufficient.

EvalForge was developed to support systematic evaluation of multi-turn dialogue systems, with a focus on conversation quality, task completion, safety, and human-likeness. The framework is designed to help identify model strengths and failure modes through structured, rubric-based assessment.

## Core Evaluation Dimensions

### Coherence

Evaluates conversational consistency, context retention, topic continuity, and logical flow across dialogue turns.

### Task Completion

Measures how effectively a model addresses user goals and fulfills requested tasks throughout a conversation.

### Safety

Assesses harmful content, unsafe recommendations, policy-sensitive behaviors, and other safety-related risks.

### Human-Likeness

Evaluates naturalness, fluency, conversational appropriateness, and overall user experience.

## Architecture

EvalForge adopts a modular multi-agent design in which each evaluation dimension is handled by a dedicated LLM-based evaluator.

```text
User Conversation
        │
        ▼
 ┌─────────────────┐
 │ Response Output │
 └─────────────────┘
        │
        ▼
 ┌─────────────────────────────────────┐
 │      Evaluation Agent Layer         │
 ├─────────────────────────────────────┤
 │  Coherence Agent                    │
 │  Task Completion Agent              │
 │  Safety Agent                       │
 │  Human-Likeness Agent               │
 └─────────────────────────────────────┘
        │
        ▼
 Score Aggregation & Analysis
```

Each evaluator follows standardized scoring rubrics and produces structured outputs that support downstream analysis and benchmarking.

## Project Structure

```text
EvalForge/
├── src/          # Evaluation agents and core framework logic
├── prompts/      # Rubrics and LLM evaluation prompts
├── data/         # Dialogue datasets and evaluation samples
├── results/      # Evaluation outputs and aggregated scores
└── tests/        # Testing and validation scripts
```

## Key Features

* Multi-turn dialogue evaluation
* Agent-based evaluation architecture
* LLM-as-a-Judge assessment workflows
* Rubric-driven scoring and rationale generation
* Modular and extensible evaluation framework
* Structured output aggregation for downstream analysis

## Future Directions

* Pairwise response comparison
* Agent trajectory evaluation
* Conversational memory assessment
* Human-AI agreement studies
* Benchmark integration and large-scale evaluation

## Author

**Jingni Wu**

Computational Linguistics | AI Evaluation | Conversational AI
