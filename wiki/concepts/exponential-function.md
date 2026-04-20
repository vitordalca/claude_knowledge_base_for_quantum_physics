---
title: "Exponential Function"
title_pt: "Função Exponencial"
type: concept
tags: [mathematics, calculus, growth-models]
created: 2026-04-20
updated: 2026-04-20
source_count: 1
sources: [sources/what-is-special-about-eulers-number.md]
---

## Summary

An exponential function is a function of the form a^t, where a base *a* is raised to a variable power t. Exponential functions model growth and decay where the rate of change is proportional to the current state. The most natural and important exponential base is *e*, where the proportionality constant equals 1, making e^(ct) the canonical form in applications.

## Resumo

Uma função exponencial é uma função da forma a^t, em que uma base *a* é elevada a uma potência variável t. Funções exponenciais modelam crescimento e decaimento em que a taxa de mudança é proporcional ao estado atual. A base exponencial mais natural e importante é *e*, em que a constante de proporcionalidade é 1, tornando e^(ct) a forma canônica nas aplicações.

## Explanation

### Core Property

The defining property of exponentials is that exponents add to give products:

$$a^{s+t} = a^s \cdot a^t$$

This property connects additive changes in the exponent to multiplicative changes in the output, bridging two fundamental operations.

### Proportionality to Derivative

For any base *a*, the derivative is:

$$\frac{d}{dt}(a^t) = (\ln a) \cdot a^t$$

This means the rate of change is proportional to the function itself, with proportionality constant ln(*a*).

### Examples of Bases

- **Base 2:** Growth that doubles each unit time (e.g., a bacteria colony that doubles daily). Proportionality constant: ln(2) ≈ 0.6931
- **Base 3:** Growth that triples each unit time. Proportionality constant: ln(3) ≈ 1.0986
- **Base *e*:** The "perfect" growth rate where proportionality constant is 1, making calculus elegant

### Canonical Form

In applications, exponentials are almost always written as e^(ct) rather than a^t. The constant *c* has direct physical meaning: it is the proportionality constant (growth rate, decay rate, oscillation frequency).

## Current State of the Field

- **Universal in modeling:** Any phenomenon with continuous growth or decay is modeled using exponential functions
- **Population dynamics:** Growth or decline in populations follows e^(rt) where r is the intrinsic growth rate
- **Radioactive decay:** Atoms decay as e^(-λt) where λ is the decay constant
- **Compound interest:** Money grows as e^(rt) where r is the continuous interest rate
- **Wave equations:** Quantum fields and classical waves use e^(ikx - iωt) for spatial-temporal propagation

## Key Papers and Sources

- [[sources/what-is-special-about-eulers-number.md]] — Complete derivation of why exponential derivatives are proportional to themselves

## Related Concepts

- [[concepts/euler-number]] — The most natural base for exponential functions
- [[concepts/natural-logarithm]] — The inverse function; every exponential has a logarithmic inverse
- [[concepts/derivative]] — Why exponential derivatives are proportional to the function

## Open Questions

- In quantum mechanics, why do amplitudes take exponential form (e^(iS/ℏ) in path integrals)?
- How do exponential functions emerge in thermodynamics and statistical mechanics?
