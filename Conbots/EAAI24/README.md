# Mimicking the Maestro: Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition

## Paper Abstract
    Motor skills, especially fine motor skills like handwriting, play an essential role in academic
    pursuits and everyday life. Traditional methods to teach these skills, although effective, can be
    time-consuming and inconsistent. With the rise of advanced technologies like robotics and artificial
    intelligence, there is increasing interest in automating such teaching processes. In this study, we
    examine the potential of a virtual AI teacher in emulating the techniques of human educators for motor
    skill acquisition. We introduce an AI teacher model that captures the distinct characteristics of human
    instructors. Using a reinforcement learning environment tailored to mimic teacher-learner interactions,
    we tested our AI model against four guiding hypotheses, emphasizing improved learner performance, enhanced
    rate of skill acquisition, and reduced variability in learning outcomes. Our findings, validated on synthetic
    learners, revealed significant improvements across all tested hypotheses. Notably, our model showcased
    robustness across different learners and settings and demonstrated adaptability to handwriting. This research
    underscores the potential of integrating Imitation and Reinforcement Learning models with robotics in revolutionizing
    the teaching of critical motor skills.
    
## Repository Description
The contents presented here are part of a contribution presented as a paper at *EAAI-24'*.

The following are included in this repository:

  - `trained_teacher_models/`: 4 trained model files describing 4 virtual teachers, each trained with different teacher-learner connection settings.
  - `environment.py`: A virtual environment for training a learner model on a follow-the-cursor task.
  - `t_sim_environment.py`: Simulated environment created for technical reasons of running two agents (teacher and learner) simultaneously. Can be ignored 
by the user.
  - `main.py`: Main running file to train a virtual learner, with full description of parameters and their meaning.


## Getting Started
To train a virtual teacher model with our environment and trained virtual teacher, one is recommended to walk through the description of arguments under
`main.py` to craft a customized call.

**Usage Example**

Running the following on CLI will result in training a virtual learner model connected to a virtual teacher model with asymmetric stiffness level of type low-high,
and with normal (Gaussian) noise type on the learner target during training. Results will produce 10 files, saved at consecutive steps of the learning process.

```
python main.py -stiffness_type 4 -connected 1 -noise_type normal
```

## Software Requirements
In order to use the repository, you should create a virtualenv or conda environment with the following required packages:

    gym=0.19.0
    numpy>=1.19.2
    opencv-python=4.5.5.64
    pandas>=1.1.5
    stable-baselines=2.10.2
    stable-baselines3=1.3.0

We recommend using **python 3.6**, as it is based on an older stable-baselines version which included gail. the code will not work for **python 2.7**.

## How to cite
Mulian, H., Shlomov, S., Limonad, L., Noccaro, A., & Buscaglione, S. (2024). [Mimicking the Maestro](https://doi.org/10.1609/aaai.v38i21.30369): Exploring the Efficacy of a Virtual AI Teacher in Fine Motor Skill Acquisition. Proceedings of the AAAI Conference on Artificial Intelligence, 38(21), 23224-23231. 
