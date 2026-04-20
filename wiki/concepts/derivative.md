---
title: "Derivative"
title_pt: "Derivada"
type: concept
tags: [mathematics, calculus, rates-of-change]
created: 2026-04-20
updated: 2026-04-20
source_count: 1
sources: [sources/what-is-special-about-eulers-number.md]
---

## Summary

The derivative of a function measures the instantaneous rate of change—how quickly the output changes as the input changes. Mathematically, it is the limit of the change in output divided by change in input as that input change approaches zero. Derivatives are central to calculus and essential for understanding growth, decay, motion, and optimization.

## Resumo

A derivada de uma função mede a taxa instantânea de mudança—quão rapidamente a saída muda conforme a entrada muda. Matematicamente, é o limite da mudança na saída dividida pela mudança na entrada, conforme essa mudança na entrada se aproxima de zero. Derivadas são centrais para o cálculo e essenciais para entender crescimento, decaimento, movimento e otimização.

## Explanation

### Formal Definition

For a function f(t), the derivative at a point t is:

$$\frac{df}{dt} = \lim_{dt \to 0} \frac{f(t + dt) - f(t)}{dt}$$

### Intuitive Meaning

Imagine a function as describing position over time. The derivative tells you the velocity—how fast you're moving at each instant. More generally, the derivative measures sensitivity: how much the output changes in response to a tiny change in input.

### Key Insight for Exponentials

For exponential functions like a^t, the derivative has a special property: it is proportional to the function itself. This is because of the core property of exponents:

$$a^{t+dt} = a^t \cdot a^{dt}$$

This allows us to factor out a^t, making the rate of change depend on the current value. For *e*, this proportionality constant is exactly 1.

## Current State of the Field

- **Fundamental tool:** Derivatives are the backbone of differential equations, optimization, and physics
- **Computational techniques:** Modern numerical methods approximate derivatives to solve complex problems
- **Machine learning:** Gradients (derivatives) are essential to training neural networks via backpropagation

## Key Papers and Sources

- [[sources/what-is-special-about-eulers-number.md]] — Derivation of why d/dt(a^t) is proportional to a^t

## Related Concepts

- [[concepts/euler-number]] — The derivative of e^t equals e^t itself
- [[concepts/exponential-function]] — Key example where derivatives have elegant proportionality
- [[concepts/calculus]] — Core tool of calculus

## Open Questions

- How do derivatives emerge in quantum mechanics, and what does the derivative of a wave function mean physically?
