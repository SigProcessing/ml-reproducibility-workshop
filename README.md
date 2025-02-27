# Computational Reproducibility in Machine Learning: A Hands-On Workshop

Welcome to the repository for "Computational Reproducibility in Machine Learning: A Hands-On Workshop." This repository contains files that facilitate the hands-on exercises discussed in the workshop slides, along with the workshop slides and a setup guide for configuring development environments on Windows, macOS, and Linux.

## Workshop Overview

Computational reproducibility, defined as the ability to consistently recreate the results of a computational analysis using the same data, code, and methods, is a cornerstone of reliable and impactful research. This workshop explores the principles of computational reproducibility and demonstrates how to integrate practical tools into research workflows to enhance transparency, reliability, and efficiency.

The first version of this workshop was given at:

**Data Science in Multi-Messenger Astrophysics Program**  
**University of Minnesota**  
**February 25, 2025**

## Reference

This workshop is based on the paper:

[1] J. Shenouda and W. U. Bajwa, “A guide to computational reproducibility in signal processing and machine learning,” *IEEE Signal Processing Magazine*, vol. 40, no. 2, pp. 141–151, Mar. 2023, doi: [10.1109/MSP.2022.3217659](https://doi.org/10.1109/MSP.2022.3217659).  

## Contents

This repository includes:

- **[Pre-Workshop-Setup-Guide.md](./Pre-Workshop-Setup-Guide.md)** (and [PDF version](./Pre-Workshop-Setup-Guide.pdf)): Instructions for setting up the required development environment.
- **[2025-02-25_UMN-Workshop-Slides.pdf](./2025-02-25_UMN-Workshop-Slides.pdf)**: The presentation slides used during the University of Minnesota workshop.
- Files supporting hands-on exercises for Git, refactoring, virtual environments, Docker, and random number generation.

## Directory Structure

Each directory contains files corresponding to a specific topic covered in the workshop:

```text
conda-env-repro-workshop/   # Virtual environments and dependency management  
docker-repro-workshop/      # Containerization using Docker  
git-repro-workshop/         # Version control with Git  
refactoring-repro-workshop/ # Code refactoring techniques  
rng-repro-workshop/         # Random number generation and reproducibility  
2025-02-25_UMN-Workshop-Slides.pdf  # University of Minnesota workshop slides  
Pre-Workshop-Setup-Guide.md  # Setup instructions  
Pre-Workshop-Setup-Guide.pdf # PDF version of setup guide  
README.md                   # This file  
```

### **Git Reproducibility Exercises** (`git-repro-workshop/`)

This directory contains two shell scripts for testing Git-based version control concepts:

- `git-create-initial-files.sh`: Generates an initial set of files to track with Git.
- `git-create-additional-files.sh`: Adds another set of files, allowing users to practice tracking new additions and understanding Git history.

## License

This repository is shared under the *Creative Commons Attribution 4.0 International (CC BY 4.0)* license. You are free to share and adapt the material as long as you provide appropriate credit. For details, see the full license text at: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
