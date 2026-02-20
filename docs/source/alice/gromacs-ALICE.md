# Running GROMACS on ALICE guide
*By Nicole Schmidt-Hebbel [@nicoleyshebbel](https://github.com/nicoleyshebbel)*

---

## 1. GROMACS
GROMACS is an all atom molecular dynamics simulation software. Molecular dynamics (MD) simulations are capable of predicting how every atom in a protein or a system will move over time. Such simulations can showcase a variety of biomolecular processes, such as conformational changes, ligand binding and protein folding. All-atom simulations calculate the trajectory of every atom in the system, making them extremely precise but computationally heavy.

---

## 2. Loading the necessary modules
Your first step is to load the GROMACS module. 

```
module load GROMACS
gmx -h
```

---

## 3. Input files
To set up your GROMACS run, you will need a couple of different files. 
- PDB file containing protein structure
- mdp file which sets parameters of the run. (can be found in tutorials, or custom made)

---

## 4. PDB2GMX
GROMACS does not use PDB files directly. Instead, it uses .gro files. This is the file where the spatial coordinates of your atoms will be stored during your molecular dynamics simulation. It can be read with your favourite visualization tools such as PyMOL or VMD, in the same way as a PDB file.

To transform a PDB file into a .gro file, you use this command:

```
gmx pdb2gmx -f protein.pdb -o protein.gro
```

After you hit enter, you will be prompted to choose a force field.

This step should generate two types of files:
- a topol.top file
- one or more itp files depending on how many chains are present in your PDB file

---

## 5. Setting up the simulation box
```
gmx editconf -f protein.gro -o box.gro -d 1.0 -c -bt cubic
```

---

## 6. Solvating the system
It is time to fill the simulation box with water. The p flag refers to our topology file topol.top, instructing GROMACS to update the topology after the solvation step.

```
gmx solvate -cp box.gro -cs spc216.gro -o solvated.gro -p topol.top
```

---

## 7. Adding ions
GROMACS uses ions to neutralize the charges across the system and to replicate physiological conditions. To add ions, first generate a tpr file.

```
gmx grompp -f ions.mdp -c solvated.gro -p topol.top -o ions.tpr

#Then replace solvent with ions using genion. This command will prompt you to pick a group, typically SOL or Water.

gmx genion -s ions.tpr -o solvated_ions.gro -p topol.top -pname NA -nname CL -neutral -conc 0.15

#When prompted, select the solvent group (commonly SOL or Water, depending on your index groups).
```
---

## 8. Energy minimization
This step ensures there are no steric clashes or inappropriate geometry in the system.

```
gmx grompp -f minimization.mdp -c solvated_ions.gro -r solvated_ions.gro -p topol.top -o minimization.tpr

gmx mdrun -deffnm minimization -v

#The name after deffnm corresponds to the prefix used for outputs from that run. The v flag provides verbose feedback that can help identify errors.
```

---

## 9. Equilibration run, temperature
This equilibration run is an NVT ensemble (canonical ensemble). In this ensemble, the number of particles (N), volume (V), and temperature (T) are conserved. This step is crucial to bring the system to the intended simulation temperature, often 300 K (sometimes 298 K).

```
gmx grompp -f nvt.mdp -c minimization.gro -r minimization.gro -p topol.top -o nvt.tpr

gmx mdrun -deffnm nvt -v
```

---

## 10. Equilibration run, pressure
Once temperature is stabilized, move on to stabilizing pressure and density. This step is conducted under an NPT ensemble, meaning the number of particles (N), pressure (P), and temperature (T) are conserved. This ensemble is also called the isothermal isobaric ensemble and resembles experimental conditions more closely.

```
gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -p topol.top -o npt.tpr

gmx mdrun -deffnm npt -v
```

---

## 11. Production run
After the equilibration steps, the system is ready for the production run. It is recommended to run this step using a Slurm script, since it takes considerably longer than the previous steps.

```
gmx grompp -f md.mdp -c npt.gro -p topol.top -o md.tpr

#To start the production run (interactive example, not recommended for long runs):

gmx mdrun -deffnm md -v

#For ALICE, run the mdrun step inside a submitted Slurm job, using the appropriate resources for your system.
```
