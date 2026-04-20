---
title: "Why Don't Real Particles Decay Back to Void? Virtual vs. Real Particles"
title_pt: "Por Que Partículas Reais Não Decaem de Volta ao Vácuo? Partículas Virtuais vs. Reais"
type: output
tags: [quantum-field-theory, virtual-particles, feynman-diagrams, conservation-laws, uncertainty-principle]
created: 2026-04-20
query: "What makes a virtual particle after gathering energy enough to its rest mass to become 'real' not go back to a void state or decay back into void? Is the initial energy that holds that particle into existence?"
---

## Answer / Analysis

The distinction between virtual and real particles is fundamental to understanding why real particles don't "decay back into void." The answer involves the **mass-shell condition**, **energy conservation**, and the **uncertainty principle**.

### Virtual Particles: Off-Shell and Temporary

Virtual particles exist only because of [[concepts/quantum-field-theory#foundational-principles|the uncertainty principle]]:

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

A virtual particle can "borrow" energy ΔE from the vacuum for time Δt ~ ℏ/ΔE. The heavier the particle, the shorter it can exist:

- Electron (0.5 MeV): lifetime ~ 10⁻²¹ seconds
- W boson (80 GeV): lifetime ~ 10⁻²⁵ seconds

Virtual particles must be **reabsorbed (annihilated) within that window** to satisfy energy conservation on average. In Feynman diagram language, they are *internal lines* that connect two real particle interactions—they're not independent entities but bookkeeping in the amplitude calculation.

### Real Particles: On-Shell and Stable

Real particles satisfy the **mass-shell condition** — the energy-momentum relation:

$$E^2 = (pc)^2 + (mc^2)^2$$

They are **"on-shell"**: they can propagate to infinity with definite energy and momentum. Crucially: **this energy came from external input** (a collision, decay, accelerator, etc.).

**Example**: In electron-positron collision producing a real photon:
- Incoming electrons contribute kinetic energy
- This energy is converted into the photon
- The photon is created with definite E and p satisfying E = pc (massless)
- The photon can travel macroscopic distances

### Why Real Particles Don't "Decay Into Void"

A real particle does not spontaneously vanish back into vacuum because:

1. **Energy conservation**: The particle has real energy (E = mc² at minimum, at rest). For it to "disappear," that energy must go somewhere. Total energy in an isolated system is conserved. There is nowhere for the energy to go except into other particles or fields.

2. **Conservation laws**: Real particles can *decay* into other particles if kinematically allowed (e.g., muon → electron + neutrino + antineutrino). But decay into *nothing* violates energy conservation.

3. **Stable particles have no decay modes**: Electrons, protons, photons have no kinematically allowed decay channels, so they're absolutely stable.

### The Key Distinction: Virtual vs. Real

| Aspect | Virtual | Real |
|--------|---------|------|
| **Lifetime** | Brief: Δt ~ ℏ/ΔE (off-shell) | Indefinite (or decays to other allowed channels) |
| **Energy-momentum** | Off-shell: E² ≠ (pc)² + (m²c⁴) | On-shell: E² = (pc)² + (m²c⁴) |
| **Creation** | Quantum fluctuations via uncertainty principle | External energy input (collision, decay) |
| **Propagation** | No; reabsorbed immediately into same interaction | Yes; to macroscopic distances |
| **Feynman diagram** | Internal lines | External lines |

### What "Holds" a Real Particle Into Existence?

The question implies continuous energy input is needed. This is a misconception:

**A particle's existence is its energy-momentum state.** The rest mass m = ℏω₀/c² is a *property of the field*, not something requiring "support."

- When a collision creates a real electron, the **kinetic energy of the collision** is converted into the electron's [[concepts/rest-mass|rest mass + kinetic energy]]
- After creation, the electron continues to exist (it's a stable excitation of the electron field)
- It does **not** need continuous energy input to "stay real"—its mass is intrinsic to the [[concepts/quantum-fields|field structure]]
- The electron only disappears if it decays (e.g., via beta decay in a nucleus, or in an annihilation with a positron)

**Vacuum energy is similarly not "held up"**: The vacuum's zero-point energy (½ℏωm per mode) is the ground state of the field. Real particles are excitations *above* that ground state, but they don't require work to maintain—they're stable states of the underlying quantum fields.

## Sources Consulted

- [[concepts/quantum-field-theory#particles-as-field-quanta|Particles as field quanta; creation and annihilation]]
- [[concepts/particles#interactions-particle-creation-and-annihilation|Interactions between fields; Feynman diagrams]]
- [[concepts/rest-mass|Rest mass emerges from minimum field oscillation frequency]]

## Follow-up Questions

- How does the uncertainty principle distinguish between virtual particles that should contribute to loop diagrams vs. those that don't?
- Why can electron-positron pairs be produced in high-energy collisions but not just "appear" spontaneously in vacuum?
- What determines which decay modes are kinematically allowed for a given particle?
- Does the vacuum fluctuation energy have any measurable consequences beyond virtual particle loops (Casimir effect, Hawking radiation)?
