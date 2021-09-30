brady
==============================

Analysis of Brady hotsprings Porotomo data

Data contains the metadata for nodal seismometers and wells, and location of continuous waveforms data from the 238 nodal seismometers. DAS data isn't included yet.

To Try:

1. Fast matched filtering to find additional meqs in the seismometer data.
    - use the catalog of quakes from Berkeley to find templates in the seismometer data
    - run FMF to find other quakes
    - compare to the paper that does it for DAS
2. Once EQTransformer is working, use that to try to find quakes
3. Use templates created from the local seismic database to find more quakes??
4. Cluster the quakes by
    - Correlation
    - the final -1 layer of EQTransformer
5. What about training EQTransformer on the local equake database too? OOr transfer learning/fine tuning?
6. Train VAE on equake data for construction of a representative latent space.