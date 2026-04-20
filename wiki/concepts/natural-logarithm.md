---
title: "Natural Logarithm"
title_pt: "Logaritmo Natural"
type: concept
tags: [mathematics, calculus, inverse-functions]
created: 2026-04-20
updated: 2026-04-20
source_count: 1
sources: [sources/what-is-special-about-eulers-number.md]
---

## Summary

The natural logarithm, denoted ln(x), is the inverse function of the exponential e^x. It answers the question "e to the what power equals x?" Natural logarithms appear universally in continuous growth models, calculus, and physics, where they provide an elegant way to work with exponential relationships.

## Resumo

O logaritmo natural, denotado ln(x), é a função inversa da exponencial e^x. Ele responde à pergunta "e elevado a qual potência é igual a x?" Os logaritmos naturais aparecem universalmente em modelos de crescimento contínuo, cálculo e física, onde fornecem uma maneira elegante de trabalhar com relações exponenciais.

## Explanation

### Definition

The natural logarithm is defined as:

$$\ln(x) = y \iff e^y = x$$

In other words, ln(x) is the exponent you must apply to *e* to get x.

### Key Properties

- **Logarithm of a product:** ln(ab) = ln(a) + ln(b)
- **Logarithm of a quotient:** ln(a/b) = ln(a) − ln(b)
- **Logarithm of a power:** ln(a^b) = b·ln(a)
- **Special values:** ln(1) = 0, ln(e) = 1

### Connection to Exponential Derivatives

The natural logarithm solves the "mystery constants" problem in exponential derivatives. For any base *a*:

$$\frac{d}{dt}(a^t) = (\ln a) \cdot a^t$$

The proportionality constant is precisely ln(*a*)—the natural log of the base tells you how fast that exponential grows.

### Why "Natural"?

The logarithm is called "natural" because:
1. It uses *e* as the base, which emerges naturally from calculus and continuous growth
2. It appears unavoidably in problems involving rates proportional to current state
3. It has the simplest derivative: d/dx(ln x) = 1/x

## Current State of the Field

- **Data analysis:** Logarithmic scales are standard for handling large ranges (decibels, pH, Richter scale, star magnitudes)
- **Signal processing:** Log-frequency transforms (spectrograms) are crucial tools
- **Information theory:** Shannon entropy uses logarithms; information is measured in "bits" (log₂) or "nats" (ln)
- **Optimization:** Many algorithms use logarithms to convert multiplicative problems into additive ones, simplifying computation

## Key Papers and Sources

- [[sources/what-is-special-about-eulers-number.md]] — How ln(*a*) gives the proportionality constant for base *a* exponentials

## Related Concepts

- [[concepts/euler-number]] — ln(e) = 1 by definition; *e* is the base of the natural logarithm
- [[concepts/exponential-function]] — Natural log is the inverse; undoing exponential growth
- [[concepts/derivative]] — The derivative of ln(x) is 1/x, the simplest logarithmic derivative

## Open Questions

- Why does information theory naturally use logarithms, and what is the deep connection to exponential distributions?
- How do logarithms emerge in quantum phase space and thermodynamic entropy?
