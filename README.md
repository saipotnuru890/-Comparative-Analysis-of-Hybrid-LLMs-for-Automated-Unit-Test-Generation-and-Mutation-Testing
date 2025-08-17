# Comparative-Analysis-of-Hybrid-LLMs-for-Automated-Unit-Test-Generation-and-Mutation-Testing

##  Overview

This project explores the use of "Hybrid Large Language Models (LLMs)" for "automated unit test generation and mutation testing". Traditional testing tools like EvoSuite (Java) and Pynguin (Python) provide structural coverage but often lack meaningful assertions and edge-case handling. On the other hand, standalone LLMs produce human-readable test cases but suffer from logical flaws and hallucinated assertions.

Our work introduces "Hybrid LLMs" (e.g., LLaMA + Claude ,  GPT-4 + DeepSeek , Gemini + Mistral ) to combine their complementary strengths, improving:

* ✅ Test coverage
* ✅ Assertion correctness
* ✅ Fault detection
* ✅ Edge-case sensitivity

We also integrate "Mutation Testing" (using PIT for Java and MutPy for Python) to evaluate the fault-detection ability of the generated test cases.

##  Key Features

* 🔹 Comparative analysis of "standalone vs. hybrid LLMs" for unit test generation.
* 🔹 Framework for evaluating test cases based on:

  * Mutation Score
  * Fault Detection Rate
  * Test Effectiveness
  * Boundary Value Coverage
  * Redundancy Score
* 🔹 Implementation of MuTAP (Mutation Test case generation using Augmented Prompt) framework.
* 🔹 Case study using the `validate_credit_card()` function with multiple mutants.
* 🔹 Experimental results showing "LLaMA-2 + Claude-3" as the most effective hybrid.

---

##  Project Structure

```
├── src/                  # Source code (functions under test & test cases)
├── tests/                # Generated & manual unit tests
├── results/              # Experimental results, mutation reports & coverage
├── notebooks/            # Experiment workflows / prompt engineering
├── report/               # Final PDF report
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. For mutation testing:

   * **Python**: Install [MutPy](https://github.com/mutpy/mutpy)
   * **Java**: Use [PIT](https://pitest.org/)

---

##  Usage

### Run baseline manual tests:

```bash
pytest tests/manual/
```

### Run LLM-generated tests:

```bash
pytest tests/generated/
```

### Perform mutation testing (Python example):

```bash
mut.py --target src/credit_card.py --unit-test tests/generated/test_credit_card.py
```

### Perform mutation testing (Java example with PIT):

```bash
mvn org.pitest:pitest-maven:mutationCoverage
```

---

##  Results Summary

* Standalone LLMs:

  * LLaMA-2 achieved the highest mutation score (93.33%).
  * Mistral 7B excelled in boundary value coverage (100%).
* Hybrid LLMs:

  * "LLaMA-2 + Claude-3" achieved the best balance:

    * Mutation Score: 95.23%
    * Fault Detection Rate: 96%
    * Test Effectiveness: 97.61%
    * Zero redundancy

 Conclusion: Hybrid LLMs outperform both standalone LLMs and traditional tools, making them a promising approach for "AI-driven software testing".

---
