---
title: "Vacuum Expectation Value"
title_pt: "Valor de Expectativa do Vácuo"
type: concept
tags: [quantum-field-theory, higgs-mechanism, symmetry-breaking]
created: 2026-04-20
updated: 2026-04-20
source_count: 1
sources: [sources/higgs-boson-mechanism.md]
---

## Summary

A vacuum expectation value (VEV) is the average value of a quantum field in its ground state (lowest energy state). For most fields in the Standard Model, the VEV is zero—the field oscillates around zero. However, for the Higgs field, the VEV is non-zero (approximately 246 GeV), meaning the Higgs field has a constant, non-zero background value throughout all of space, even in its lowest-energy state. This non-zero VEV is responsible for electroweak symmetry breaking and is the mechanism by which the Higgs field generates mass for all fundamental particles. The concept of VEV is central to understanding why particles have mass at all.

## Resumo

Um valor de expectativa de vácuo (VEV) é o valor médio de um campo quântico em seu estado fundamental (estado de menor energia). Para a maioria dos campos no Modelo Padrão, o VEV é zero—o campo oscila em torno de zero. Porém, para o campo de Higgs, o VEV é não-nulo (aproximadamente 246 GeV), significando que o campo de Higgs tem um valor de fundo constante e não-nulo em todo o espaço, mesmo em seu estado de menor energia. Este VEV não-nulo é responsável pela quebra de simetria eletrofraca e é o mecanismo pelo qual o campo de Higgs gera massa para todas as partículas fundamentais. O conceito de VEV é central para entender por que as partículas têm massa em primeiro lugar.

## Explanation

### Definition and Quantum Field Theory

In quantum field theory, fields are the fundamental objects. A **field value** φ(x,t) is the state of the field at position x and time t. The **vacuum expectation value** is:

**⟨0|φ(x,t)|0⟩ = vev**

where |0⟩ represents the quantum vacuum (ground state) and ⟨⟩ denotes an expectation value (average).

### VEV for Different Fields

**Electromagnetic field**: VEV = 0
- The electromagnetic field oscillates symmetrically around zero
- No preferred direction in space
- Photons remain massless

**Weak (W/Z) boson field**: VEV = 0 (before symmetry breaking)
- At high temperatures (early universe), W and Z bosons are massless and the weak field has VEV = 0
- At low temperatures (today), the weak field couples to the Higgs field's non-zero VEV
- W and Z bosons acquire mass

**Higgs field**: VEV ≠ 0 (today)
- The Higgs field's potential has a minimum at non-zero field value
- The field "rolls down" to this minimum and sits there
- VEV_Higgs ≈ 246 GeV

### Temperature Dependence

The Higgs VEV changes dramatically with temperature:

**Early universe (T > 159.5 GeV/kB ≈ 10¹⁵ K)**:
- Thermal fluctuations dominate
- Higgs potential minimum is at φ = 0
- VEV_Higgs = 0
- Electroweak symmetry is unbroken
- All particles are massless

**Phase transition (T ≈ 159.5 GeV/kB)**:
- As universe cools, Higgs potential changes
- Minimum shifts from φ = 0 to φ = 246 GeV
- Higgs field "rolls" toward new minimum
- Electroweak symmetry breaks spontaneously

**Present day (T ≈ 2.7 K)**:
- Higgs field locked at VEV = 246 GeV
- W and Z bosons, fermions all have mass
- This is the world we observe

### Mass Generation via VEV

The non-zero Higgs VEV generates mass for particles through **Yukawa couplings**:

**For fermions (electrons, quarks)**:
The Higgs field couples to fermions with strength g_f (Yukawa coupling):
**m_fermion = g_f × VEV / √2**

**For vector bosons (W, Z)**:
**m_W = (g_w × VEV) / 2**
**m_Z = (g_w × VEV) / (2cos(θ_W))**

where g_w is the weak coupling and θ_W is the Weinberg angle.

**For the Higgs boson itself**:
The mass of the Higgs boson reflects the curvature of the potential around the VEV:
**m_H² ∝ (second derivative of potential at VEV)**

### Spontaneous Symmetry Breaking

The Higgs field exhibits **spontaneous symmetry breaking**: the field equations are symmetric under certain transformations, but the VEV breaks this symmetry:

1. **Before symmetry breaking** (T high): Field equations are symmetric; any value φ could be the ground state
2. **After symmetry breaking** (T low): Field "chooses" one specific ground state (φ ≈ 246 GeV)
3. **From a symmetry perspective**: By choosing one state, the field breaks the symmetry—yet the underlying equations remain symmetric

This is why it's called *spontaneous*: the symmetry-breaking emerges dynamically, not imposed externally.

## Current State of the Field

### Precision Measurements

- **Higgs VEV measurement**: Constrained to v = 246.2200... GeV by electroweak precision data
- **Electroweak parameters**: The VEV links multiple Standard Model parameters (W mass, weak coupling, electron mass, etc.)
- **Consistency tests**: Different experimental approaches yield consistent values of the VEV

### Beyond the Standard Model

**Open questions**:
- **Is the Higgs VEV fundamental?** Some theories propose it emerges from composite structures
- **Could multiple VEVs exist?** Supersymmetry predicts multiple scalar fields, each with its own VEV
- **Is the VEV value tuned?** The value 246 GeV seems arbitrary; some theories appeal to anthropic reasoning

### Vacuum Stability Implications

The measured Higgs mass (125 GeV) is special: it places the electroweak vacuum in a **metastable state**. This means:
- Current vacuum is not the true minimum of energy
- The field could tunnel to a lower-energy false vacuum
- Tunneling probability is extremely small (~10^(-10000)); the universe is expected to remain in current state for vastly longer than its current age
- Nevertheless, this hints that the Standard Model may not be the complete theory

## Key Papers and Sources

- [[sources/higgs-boson-mechanism.md]] — Detailed discussion of Higgs VEV and electroweak symmetry breaking

## Related Concepts

- [[concepts/higgs-field]] — The field that possesses the non-zero VEV
- [[concepts/higgs-boson]] — The quantum excited state of the Higgs field
- [[concepts/higgs-mechanism]] — Process by which VEV generates mass
- [[concepts/mexican-hat-potential]] — The potential shape underlying VEV formation
- [[concepts/quantum-field-theory]] — Framework in which VEVs are formulated

## Open Questions

- **What determines the value of the Higgs VEV?** Why 246 GeV and not some other value?
- **Are there other non-zero VEVs in nature?** Beyond the Higgs, could other fields have non-zero VEVs?
- **How does gravity couple to the VEV?** The VEV generates mass, but how does mass relate to gravity's source (energy-momentum)?
- **Could the VEV change in extreme environments?** Near singularities or at Planck-scale densities, does the VEV transform?
