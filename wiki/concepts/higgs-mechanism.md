---
title: "Higgs Mechanism"
title_pt: "Mecanismo de Higgs"
type: concept
tags: [higgs-boson, particle-physics, electroweak-symmetry-breaking, standard-model, mass]
created: 2026-04-17
updated: 2026-04-17
source_count: 1
sources: [sources/higgs-boson-mechanism.md]
---

## Summary

The Higgs mechanism is the process by which elementary particles acquire mass through interaction with the Higgs field, which possesses a non-zero vacuum expectation value throughout spacetime. Unlike classical mass (which is intrinsic), mass in the Standard Model emerges when a massless quantum field couples to the Higgs field with its background value v. The resulting particle mass is proportional to the coupling strength g and the Higgs vev: m = ℏgv/c². This mechanism unifies electromagnetism and the weak force, explains why W/Z bosons and fermions are massive while photons remain massless, and govers the mass hierarchy of the Standard Model.

## Resumo

O mecanismo de Higgs é o processo pelo qual partículas elementares adquirem massa através da interação com o campo de Higgs, que possui um valor esperado do vácuo não-zero em todo o espaço-tempo. Ao contrário da massa clássica (que é intrínseca), a massa no Modelo Padrão emerge quando um campo quântico sem massa se acopla ao campo de Higgs com seu valor de fundo v. A massa resultante da partícula é proporcional à força de acoplamento g e ao vev de Higgs: m = ℏgv/c². Este mecanismo unifica eletromagnetismo e a força fraca, explica por que os bósons W/Z e férmions são massivos enquanto fótons permanecem sem massa, e governa a hierarquia de massa do Modelo Padrão.

## Explanation

### The Basic Mechanism

**Massless Field Coupled to Non-Zero Background**

In quantum field theory, a field ψ described by the unmodified wave equation ∂²ψ/∂t² = c²∇²ψ has massless quanta. But when this field couples to the Higgs field φ with a non-zero background value v:

1. The coupling term in the Lagrangian: L_int = −gφψ² (where g is coupling strength)
2. Substituting φ → v (background value): L_int → −gvψ²
3. This creates an effective mass term: m_ψ = gv in the equation of motion
4. **The mass emerges automatically; it's not put in by hand**

**Key Insight**: The coupling constant g and Higgs vev v together determine mass:
$$m = \frac{\hbar g v}{c^2}$$

Different particles have different couplings → different masses.

### Spontaneous Symmetry Breaking

**Mexican Hat Potential**

The Higgs field potential determines whether it has a non-zero vev:

$$V(\phi) = -\frac{\mu^2}{2}\phi^2 + \frac{\lambda}{4}\phi^4$$

- **Near origin** (φ ≈ 0): Negative curvature; potential dips downward (unstable)
- **Away from origin** (φ = ±v): Positive curvature; potential rises again (stable)
- **Shape**: Central peak at origin with valleys on sides → "Mexican hat" or "double well"

**Minimum Location**

Setting ∇V = 0: dV/dφ = −μ²φ + λφ³ = 0

Solutions: φ = 0 (unstable maximum) or φ = ±μ/√λ = ±v (stable minima)

**Symmetry Breaking**

- **Classically**: The potential is symmetric under φ → −φ
- **Physically**: The field settles at +v or −v, breaking the symmetry
- **Name**: Spontaneous symmetry breaking (field "chooses" asymmetric vacuum)

### Mass Emergence from Potential Curvature

**General Principle**

For any field with potential V(φ) resting at minimum φ = v:

$$m = \hbar \sqrt{\frac{d^2V}{d\phi^2}\bigg|_{\phi=v}} / c^2$$

The mass is **entirely determined by the potential's curvature at its minimum**.

**Consequences**:
- **Sharply curved potential** → Large curvature → Heavy particles
- **Shallow potential** → Small curvature → Light particles  
- **Flat potential** → Zero curvature → Massless particles

### Application to Standard Model

**Particles Gaining Mass via Higgs Coupling**

| Particle | Coupling | Mass | Notes |
|---|---|---|---|
| W± boson | ~1 | 80 GeV | Weak force carrier |
| Z boson | ~1 | 91 GeV | Weak force carrier |
| Top quark | ~1 | 173 GeV | Heaviest quark |
| Bottom quark | ~0.02 | 4.2 GeV | Lighter quark |
| Tau lepton | ~0.01 | 1.8 GeV | Heaviest lepton |
| Electron | ~0.0003 | 0.511 MeV | Lightest lepton |

**Particles NOT Getting Higgs Mass**

- **Photon**: Doesn't couple to Higgs → massless
- **Gluons**: Don't couple to Higgs → massless
- **Neutrinos**: (Slightly massive via seesaw mechanism, not standard Higgs coupling)
- **Proton/Neutron**: Mostly composite mass from strong force binding energy; small Higgs contribution

### The Higgs Field

**What It Is**
- A quantum field φ(x,t) permeating all spacetime
- Has potential V(φ) with minimum away from origin
- Sits in one of the degenerate minima: φ₀ = ±v ≈ 246 GeV

**Background Value (Vev)**
- ⟨φ⟩ = v ≈ 246 GeV (non-zero average value)
- Not zero! This non-zero vev is what "switches on" mass generation
- If Higgs vev were zero, all coupled particles would be massless

**Excitations of the Field**
Write φ(x,t) = v + h(x,t) where h is small ripple around background:
- h represents quantum fluctuations (oscillations)
- When quantized, h quanta are **Higgs bosons**
- Higgs boson mass determined by curvature of potential at v

### Electroweak Unification

**Before Symmetry Breaking** (high temperatures, early universe)
- SU(2)_L × U(1)_Y gauge symmetry is unbroken
- All particles are massless
- Weak and electromagnetic forces are indistinguishable

**After Symmetry Breaking** (low temperatures, present universe)
- Higgs field acquires vev; symmetry is "hidden"
- Effective symmetry: U(1)_em (electromagnetism)
- Weak bosons become massive
- Photon remains massless

This unification (Weinberg-Salam model) is one of Standard Model's great triumphs.

## Current State of the Field

### Higgs Discovery and Properties

**July 2012: CERN LHC Discovery**
- Atlas and CMS experiments both observed new particle
- Mass: 125.10 ± 0.14 GeV
- Consistent with Standard Model predictions
- Confirmed Higgs mechanism framework

**Measured Properties** (as of 2026)
- Mass: 125.10 ± 0.11 GeV (improved precision)
- Spin: 0 (scalar boson, as predicted)
- Branching ratios: Matches SM predictions to within 10%
- Coupling to fermions/bosons: Proportional to mass (as expected)

**Implications**
- Fixed λ parameter of Mexican hat potential
- Determined curvature; explained why Higgs mass is ~125 GeV
- No deviation from SM observed (constrains beyond-SM physics)

### Open Questions

1. **Why these couplings?** Why does top quark couple so strongly (g_t ≈ 1) while electron couples weakly?
2. **Hierarchy problem**: Why is Higgs mass ~125 GeV, so different from Planck scale (10¹⁹ GeV)?
3. **Naturalness**: Why isn't Higgs mass much larger? (Quantum corrections suggest it should be)
4. **Higgs self-interaction**: What controls λ in the potential? Why that value?
5. **Single Higgs or multiple?** Could there be other Higgs bosons? (SUSY, 2HDM predict extras)
6. **Dark matter**: Could dark matter be related to Higgs sector?

### Beyond the Standard Model

**Supersymmetry (SUSY)**
- Predicts fermionic superpartner (Higgsino) for Higgs
- Multiple Higgs bosons (2HDM: h, H, A, H±)
- Solves hierarchy problem via cancellation

**Composite Higgs**
- Higgs not fundamental; composite at TeV scale
- Emerges from new strong interaction (technicolor)
- Would show internal structure at LHC

**Extra Dimensions**
- Higgs as Kaluza-Klein resonance of 5D field
- Predicts tower of excited states
- Could explain hierarchy via warping

**Two-Higgs-Doublet Model (2HDM)**
- Extends SM with second Higgs doublet
- Arises in SUSY, Type II seesaw
- Predicts charged Higgs, heavy Higgs states

## Key Papers and Sources

- [[sources/higgs-boson-mechanism.md]] — Pedagogical explanation of Higgs mechanism from first principles
- [[sources/what-is-a-particle-quantum-fields.md]] — Quantum field theory foundation underlying Higgs mechanism
- [[sources/how-we-make-antimatter.md]] — CERN experimental context for Higgs discovery

## Related Concepts

- [[concepts/higgs-boson]] — The particle (quantum of Higgs field)
- [[concepts/higgs-field]] — The fundamental field giving mass
- [[concepts/spontaneous-symmetry-breaking]] — Symmetry-breaking mechanism underlying Higgs
- [[concepts/mexican-hat-potential]] — Potential that drives symmetry breaking
- [[concepts/vacuum-expectation-value]] — Non-zero background value of Higgs field
- [[concepts/electroweak-symmetry-breaking]] — Application in Standard Model

## Open Questions

- **Is the Higgs mechanism the only way to generate mass?** Could other mechanisms exist in nature?
- **What determines the Higgs potential shape?** Is it fundamental or emergent?
- **Are there additional Higgs bosons?** Current data constrain but don't exclude them
- **Could Higgs decay to dark matter?** Would explain missing decay modes
- **Is the Higgs self-coupling consistent with SM?** Difficult to measure; still open
- **What role in early universe?** Higgs field drives electroweak phase transition; implications for baryogenesis?

## References

- **Peskin & Schroeder** — Chapter on Electroweak Theory and Higgs Mechanism
- **Weinberg** — "The Quantum Theory of Fields, Vol. 2" — Electroweak unification
- **CERN Higgs Physics Review** (2012+) — Experimental results and implications
- **Barbieri** — "The Standard Model and Beyond" — Modern comprehensive treatment
