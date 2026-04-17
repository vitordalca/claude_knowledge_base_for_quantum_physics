---
title: "Particles"
title_pt: "Partículas"
type: concept
tags: [quantum-mechanics, particle-physics, quantum-field-theory, fundamental-physics]
created: 2026-04-17
updated: 2026-04-17
source_count: 1
sources: [sources/what-is-a-particle-quantum-fields.md]
---

## Summary

In quantum field theory, a particle is not a fundamental object but rather the smallest possible excitation (quantum) of a relativistic quantum field. A particle with momentum k and oscillation frequency ω carries energy E = ℏω and momentum p = ℏk. The rest mass m of a particle emerges from the minimum oscillation frequency ω₀ of its corresponding field via m = ℏω₀/c². This definition unifies particle physics with wave physics: particles are quantized vibrations, wave packets are superpositions of particle modes, and the distinction becomes a matter of perspective.

## Resumo

Na teoria quântica de campos, uma partícula não é um objeto fundamental, mas sim a menor excitação possível (quantum) de um campo quântico relativístico. Uma partícula com momento k e frequência de oscilação ω carrega energia E = ℏω e momento p = ℏk. A massa de repouso m de uma partícula emerge da frequência de oscilação mínima ω₀ de seu campo correspondente via m = ℏω₀/c². Esta definição unifica a física de partículas com a física de ondas: partículas são vibrações quantizadas, pacotes de ondas são superposições de modos de partículas, e a distinção torna-se uma questão de perspectiva.

## Explanation

### What Is a Particle?

**Classical Intuition**
Classically, a particle is a localized object with definite position and momentum. But quantum mechanics forbids this (uncertainty principle). QFT resolves the paradox by redefining "particle":

**QFT Definition**
A particle is a discrete excitation of a quantum field, carrying:
- **Energy:** E = ℏω (where ω is oscillation frequency)
- **Momentum:** p = ℏk (where k is wave number)
- **Mass:** m = ℏω₀/c² (where ω₀ is minimum field oscillation frequency)

**Why Fields, Not Particles?**
- Particles can be created and destroyed (field excitation levels change)
- Particles appear and disappear in interactions (fields couple and decouple)
- Empty space is not empty (vacuum fluctuations from zero-point energy ½ℏω)
- An infinite number of particles can exist simultaneously (field has infinitely many modes)

Fields are the fundamental reality; particles are emergent phenomena.

### Properties of Particles

**Energy and Momentum**

From dispersion relation: (ℏω)² = (pc)² + (mc²)²

For a particle with momentum p:
- **Rest energy:** E₀ = mc²
- **Total energy:** E = √[(pc)² + (mc²)²]
- **Kinetic energy:** K = E − mc² = √[(pc)² + (mc²)²] − mc²
- **Velocity:** v = pc²/E (always ≤ c)

**Spin**

Particles have intrinsic angular momentum (spin):
- **Fermions** (matter): spin ½ (electrons, quarks, neutrinos) — obey Fermi-Dirac statistics (Pauli exclusion)
- **Bosons** (force carriers): spin 0, 1, or 2 (photons spin 1, Higgs spin 0) — obey Bose-Einstein statistics (unlimited occupancy)
- **Spin determines interaction rules** (e.g., fermions exchange → minus sign in amplitude)

**Quantum Numbers**

Particles are characterized by:
- Mass m
- Spin s
- Charge Q (electric, color, weak)
- Baryon number B (number of quarks)
- Lepton number L (number of leptons)
- Flavor (u,d,c,s,t,b for quarks; e,μ,τ for leptons)

### From Single Particle to Many-Particle States

**Fock Space**

QFT naturally describes multiple particles via Fock space:
- **Vacuum state |0⟩:** No particles; still has zero-point energy
- **One-particle state a†|0⟩:** Field mode excited once → one particle
- **Two-particle state (a†)²|0⟩/√2:** Two particles in same mode (bosons) or one in each of two modes (fermions)
- **General state:** Superposition of states with different particle numbers

**Creation and Annihilation Operators**
- **a† (creation):** Adds one particle to field mode; [a†, a] = 1
- **a (annihilation):** Removes one particle; a|0⟩ = 0
- **Particle number:** N = a†a counts oscillation quanta in mode

**Identical Particles**

QFT naturally enforces indistinguishability:
- Bosons: Symmetric under particle exchange; a† and a commute
- Fermions: Antisymmetric under exchange; a† and a anticommute {a†, a} = 1; Pauli exclusion automatic

### Interactions: Particle Creation and Annihilation

**Coupling Between Fields**

When two fields couple (e.g., electron field couples to photon field):
- Electron can absorb photon → energy change E − ℏω_photon
- Electron can emit photon → energy change E + ℏω_photon
- Electron-positron pair can annihilate → two photons
- Photons can pair-produce → electron-positron pair

**Feynman Diagrams**

Visual shorthand for particle processes:
- Lines represent particles
- Vertices represent interactions
- Diagram encodes amplitude for process
- Summing diagrams gives total transition probability

### Massless vs. Massive Particles

**Massless Particles (ω₀ = 0)**
- Photon: Quantum of EM field; mediates electromagnetic force
- Gluon: Quantum of gluon field; mediates strong force
- Graviton: (hypothetical) Quantum of spacetime; would mediate gravity
- Energy: E = pc (always moving at speed c)
- Arbitrarily small energy possible (no minimum frequency)

**Massive Particles (ω₀ ≠ 0)**
- Electron: ℏω₀ = 0.511 MeV
- Proton: ℏω₀ = 938 MeV
- W±/Z bosons: ℏω₀ = 80–91 GeV
- Top quark: ℏω₀ = 173 GeV
- Minimum energy: E₀ = mc² (particle at rest)
- Always v < c

### The Particle Zoo

**Standard Model Particles**

**Quarks (spin ½, fractional charge, confined in hadrons)**
- Light: up, down, strange, charm
- Heavy: top, bottom
- Masses: 2–173 MeV

**Leptons (spin ½, weak interactions)**
- Charged: electron, muon, tau (0.5 MeV – 1.8 GeV)
- Neutral: electron neutrino, muon neutrino, tau neutrino (< 0.1 eV)

**Gauge Bosons (spin 1, force carriers)**
- Photon: EM force, massless
- W±/Z: Weak force, ~80–91 GeV
- Gluons: Strong force, massless, color-charged

**Scalar Bosons (spin 0)**
- Higgs: Gives mass to particles via electroweak symmetry breaking (125 GeV)

## Current State of the Field

### Experimental Particle Physics

**Particle Accelerators**
- LHC (CERN): Collides protons at 13 TeV; discovered Higgs (2012)
- Precision experiments: Test rare decays, CP violation, coupling strengths
- Cosmic ray detectors: Study ultra-high-energy particles from universe

**Recent Discoveries**
- Higgs boson (2012)
- Observation of Higgs in multiple decay channels
- Rare B-meson decays; CP violation in lepton sector
- Hints of new physics (muon g−2 anomaly, W boson mass anomaly)

### Theoretical Developments

**Composites and Substructure**
- Are quarks/leptons truly fundamental, or composite?
- Compositeness scale: If composite, appears at energy scale Λ ≈ TeV − PeV

**Supersymmetry (SUSY)**
- Predicts fermionic partners for each boson (SUSY particles, sparticles)
- Solves hierarchy problem; unifies forces at GUT scale
- No sparticles observed yet (lower mass limits keep rising)

**Extra Dimensions**
- Kaluza-Klein: Gravity and EM unified via 5D spacetime
- String theory: 10D spacetime; particles are strings
- Warped geometries: Explain hierarchy; may be detectable at LHC

## Key Papers and Sources

- [[sources/what-is-a-particle-quantum-fields.md]] — Pedagogical definition and properties of particles in QFT framework
- [[sources/how-we-make-antimatter.md]] — Experimental particle physics: antiparticles, production, storage

## Related Concepts

- [[concepts/quantum-field-theory]] — Framework defining particles
- [[concepts/quantum-fields]] — Fields whose excitations are particles
- [[concepts/antiparticles]] — Mirror excitations with opposite quantum numbers
- [[concepts/photon]] — Massless particle; quantum of EM field
- [[concepts/rest-mass]] — Emerges from field properties

## Open Questions

- **Are quarks and leptons truly fundamental?** Or composite at some scale?
- **Why 17 standard particles?** What determines particle spectrum?
- **Do particles exist below Planck scale?** QFT breaks down at ~10⁻³⁵ m; quantum gravity takes over
- **What is the nature of the vacuum?** Zero-point energy; cosmological constant problem
- **Are there additional particles?** Dark matter candidates? Sterile neutrinos? Axions?
