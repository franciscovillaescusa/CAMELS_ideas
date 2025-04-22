## General Description

CAMELS stands for *Cosmology and Astrophysics with MachinE Learning Simulations*, and it is a collection of more than **15,000 cosmological simulations**: 8,925 hydrodynamic simulations and 6,136 N-body simulations. The hydrodynamic simulations in CAMELS can be classified into three different groups:

- **Generation**: The first/second/third generation follows the evolution of `256³ / 512³ / 1024³` dark matter particles plus `256³ / 512³ / 1024³` initial fluid elements in a periodic cubic box of size `25 / 50 / 100 h⁻¹ Mpc`.

- **Suite**: The simulations can be classified into suites based on the code and subgrid physics model used to run them. CAMELS contains **nine different suites**:

	1. **IllustrisTNG**: Run with the AREPO code using the IllustrisTNG subgrid physics model. *(4,243 simulations)*
	2. **SIMBA**: Run with the GIZMO code using the SIMBA model. *(1,171 simulations)*
	3. **Astrid**: Run with the MP-Gadget code using the ASTRID model. *(2,080 simulations)*
	4. **Magneticum**: Run with the OpenGadget code using the Magneticum model. *(77 simulations)*
	5. **Swift-EAGLE**: Run with the Swift code using the EAGLE model. *(1,052 simulations)*
	6. **Ramses**: Run with the Ramses code. *(296 simulations)*
	7. **CROCODILE**: Run with the Gadget4-Osaka code using the CROCODILE model. *(260 simulations)*
	8. **Obsidian**: Run with the Gizmo code using the Obsidian model. *(27 simulations)*
	9. **Enzo**: Run with the Enzo code. *(6 simulations)*

- **Set**: The CAMELS simulations can be further classified into **six different sets**, depending on how the values of the cosmological and astrophysical parameters and the initial random seed are arranged:

	- **SB (Sobol Sequence)**: At least 128 simulations arranged using a Sobol sequence with `2ⁿ` elements. Each simulation has a unique initial condition seed. Named `SBX` where `X` is the number of dimensions (e.g., `SB28`).

	- **CV (Cosmic Variance)**: 27 simulations sharing the same cosmological and astrophysical parameters, differing only in the initial random seed.

	- **1P (One-Parameter at a time)**: Contains four simulations per parameter plus one fiducial. Each simulation varies only one parameter at a time. Same seed used for all.

	- **LH (Latin-Hypercube)**: 1,000 simulations with parameters arranged using Latin-hypercube sampling. Each simulation has a different initial random seed.

	- **EX (Extreme)**: 4 simulations sharing the same cosmological parameters but different astrophysical configurations:
	  - Fiducial
	  - Very efficient AGN feedback
	  - Very efficient supernova feedback
	  - No feedback

	- **BE (Butterfly Effect)**: 27 simulations (available for IllustrisTNG and SIMBA) sharing the same initial conditions as the 1P set but using different random number sequences during the simulation evolution. This set isolates intrinsic stochasticity in the models.

The initial conditions of all simulations were generated at redshift `z = 127` using 2LPT. For each hydrodynamic simulation, CAMELS also provides an N-body counterpart. Each simulation outputs **91 snapshots**, including key redshifts like `z = 0`. Halos and subhalos are identified using **FoF**, **Subfind**, **Rockstar**, **AHF**, and **CAESAR**, with merger trees from **Sublink** and **Consistent Trees**.

---

## Snapshots

Each CAMELS snapshot includes properties for various simulation particle types:

- **Gas particles** (`PartType0`): Represent the cosmological gas fluid. Stored properties include:
  - Position, velocity, ID, mass
  - Electron number density, neutral hydrogen, metallicity
  - Density, internal energy, star-formation rate, etc.
  - Only in hydrodynamic simulations

- **Dark matter particles** (`PartType1`): Represent the dark matter fluid. Stored properties:
  - Position, velocity, mass, ID
  - Present in all simulations

- **Star particles** (`PartType4`): Represent stars in the simulation. Stored properties:
  - Position, velocity, mass
  - Metallicity, luminosity in photometric bands, ID
  - Only in hydrodynamic simulations

- **Black-hole particles** (`PartType5`): Represent black holes. Stored properties:
  - Position, velocity, mass, ID
  - Only in hydrodynamic simulations

From this data, many derived quantities can be computed — e.g., Lyman-alpha spectra from gas density/temperature/neutral hydrogen, or X-ray luminosities from gas metallicity and temperature.

---

## Galaxy Catalogs

Each snapshot has associated **halo and subhalo catalogs**, capturing galaxy and halo properties:

### Halos

- Position
- Total mass
- Velocity
- Mass of each particle type
- `M200`, `R200`
- Star-formation rate and metallicity

### Subhalos (Galaxies)

Galaxies are identified as subhalos with non-zero stellar mass. Stored properties include:

1. Comoving position  
2. Peculiar velocity  
3. Gas mass (including CGM)  
4. Stellar mass  
5. Black hole mass  
6. Total mass (DM + gas + stars + BH)  
7. Maximum circular velocity:  `V_max = max(√(GM(<R)/R))`  
8. Velocity dispersion  
9. Mass-weighted gas metallicity  
10. Mass-weighted stellar metallicity  
11. Star-formation rate  
12. Spin vector  
13. Stellar half-mass radius  
14. Total mass half-mass radius  
15. Radius where `√(GM(<R_max)/R_max) = V_max`  
16. U-band magnitude  
17. K-band magnitude  
18. g-band magnitude  