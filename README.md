# Muon Lifetime Simulation: Project 1
This repository contains code that simulates the muon lifetime experiment. Details of the experiment can be found [here](https://www.physlab.org/wp-content/uploads/2016/04/Muon_cali.pdf). The repository uses:


*   `matplotlib`
*   `numpy`

## Running the Code:
The detector is not functional yet, so please follow the steps to simulate the Muons. It should give you a exponential histogram.

```<> python python/Muons.py```

Possible Errors: Sometimes Mac/Linux system require importing other files with "python prefix".

Instead of"

```from Generator import Generator```

Use:

```from python.Generator import Generator```

## Physics
Cosmic ray muons are result of decay of pions from high energy collision of incoming cosmic ray with nuclei in the atomosphere. The final result of the simulation must be a histogram with an exponential plot. The exponential curve is actually a combination of two exponential curves for positve and negative muon. This aspects of the experiment will be added in the future. For now we will try to simulate the experiment to obtain the average lifetime of a muon.

The Simulation Must have three main aspects:

## Generator Class
Simulates an event of muon decay from:
*   Muon first entering detector.
*   Random decay time using Exponential Probability
*   Random coordinates on Detector.


## Detector Class

### Currently Broken. Needs A Sorting Class.

The detector class simulates the photomultiplier that detects light from the scintilator medium. Firstly, the detector accepts the coordinates of incoming lepton, the coordinates of the resulting electron, and the measured lifetime. Secondly, the detector creates a animation of using `matplotlib`. Each event of decay is marked by the same color and number.

