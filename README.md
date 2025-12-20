# GEHA-AA
In this work, we propose an end-to-end framework that jointly integrates graph-based temporal reasoning and Transformer-based action anticipation, termed GEHA-AA.

## Action Anticipation

![Method Pipeline](Viz_Results/AA_Intro.png)


## Our Proposed Architecture

![Method Pipeline](Viz_Results/ActionAnticipation.png)

1. Input Video Acquisition
2. Frame Sampling and Preprocessing
3. Multimodal Feature Extraction
4. Early Multimodal Feature Fusion
5. Feature Storage and Alignment
6. Observation Window Construction
6. Time-Based Future Label Assignment
7. Graph Construction over Observed Frames
8. Graph-Enhanced Relational Reasoning (GAT)
9. Temporal Encoding with Transformer Encoder
10. Fusion of Graph and Temporal Representations (GETR Output)
11. Horizon-Aware Query Initialization
12. Horizon-Aware Transformer Decoding (HATD)
13. Horizon-Specific Classification
  Separate classification heads predict verb, noun, and action labels independently for each anticipation horizon.
14. Loss Computation and Optimization
15. Multi-Horizon Action Anticipation Output
  The final output consists of verb, noun, and action predictions across multiple future anticipation times.
