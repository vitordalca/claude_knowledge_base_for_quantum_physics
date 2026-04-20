---
title: "Euler's Number (e)"
title_pt: "Número de Euler (e)"
type: concept
tags: [mathematics, calculus, exponential-functions, constants]
created: 2026-04-20
updated: 2026-04-20
source_count: 1
sources: [sources/what-is-special-about-eulers-number.md]
---

## Summary

Euler's number *e* ≈ 2.71828... is the unique mathematical constant defined as the base of exponential growth where the derivative of e^t equals e^t itself. This makes *e* the natural choice for modeling continuous growth processes and is fundamental to calculus, differential equations, and quantum mechanics.

## Resumo

O número de Euler *e* ≈ 2,71828... é a constante matemática única definida como a base do crescimento exponencial em que a derivada de e^t é igual a e^t. Isso torna *e* a escolha natural para modelar processos de crescimento contínuo e é fundamental para cálculo, equações diferenciais e mecânica quântica.

## Explanation

### Definition

*e* is the unique base *a* such that:

$$\frac{d}{dt}(a^t) = a^t$$

For any other base, the proportionality constant is different. For base 2, d/dt(2^t) = 0.6931 × 2^t = ln(2) × 2^t. The constant *e* is special because its proportionality constant equals 1.

### Why It Emerges

When analyzing continuous growth—like a population that doubles every day—we observe that the instantaneous rate of change is proportional to the current state. The proportionality constant depends on how fast the system grows relative to a standard unit time. *e* is simply the growth rate that naturally arises when we define the proportionality constant to be exactly 1.

### Connection to Other Bases

Any exponential base *a* can be rewritten in terms of *e*:

$$a^t = e^{(\ln a) \cdot t}$$

The proportionality constant for base *a* is always ln(*a*). This explains why the "mystery constants" (0.6931 for base 2, 1.0986 for base 3, etc.) are precisely the natural logarithms of those bases.

## Current State of the Field

- **Ubiquity:** *e* appears in virtually all continuous growth models, differential equations, and quantum mechanical systems
- **Standard notation:** In applied mathematics and physics, exponentials are almost always written as e^(ct) rather than a^t, where the constant *c* has direct physical meaning (growth rate, decay rate, oscillation frequency)
- **Computational use:** Logarithmic scales and natural logs are standard tools in data analysis, signal processing, and scientific computing

## Key Papers and Sources

- [[sources/what-is-special-about-eulers-number.md]] — 3Blue1Brown explanation of why *e* is the natural base for exponential functions

## Related Concepts

- [[concepts/derivative]] — The property d/dt(e^t) = e^t is what makes *e* special
- [[concepts/exponential-function]] — *e* is the most natural base for exponential functions
- [[concepts/natural-logarithm]] — The inverse function; ln(e) = 1 by definition
- [[concepts/calculus]] — *e* is central to differential and integral calculus

## Open Questions

- Why does continuous growth in nature so often follow exponential patterns proportional to e^(ct)?
- How does the emergence of *e* in quantum mechanics relate to the fundamental nature of probabilistic amplitudes?
