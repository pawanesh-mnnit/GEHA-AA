# GEHA-AA
In this work, we propose an end-to-end framework that jointly integrates graph-based temporal reasoning and Transformer-based action anticipation, termed GEHA-AA.

## Action Anticipation

![Method Pipeline](Viz_Results/AA_Intro.png)


## Our Proposed Architecture

![Method Pipeline](Viz_Results/ActionAnticipation.png)

1. Multimodal Feature Extraction and Fusion
   RGB frames and optical flow are processed using a pretrained ResNet-50 backbone, and their features are fused at the feature level to obtain a unified multimodal representation for each frame.
2. Observation Window Construction and Label Assignment
   Fixed-length observation windows are constructed from fused features ending at annotated action boundaries, while future verb, noun, and action labels are assigned using time-based anticipation horizons.
3. Graph-Based Relational Modeling
   A dynamic k-nearest-neighbor similarity graph is built over observed frames, and a Graph Attention Network propagates information across semantically related frames to capture non-local relationships.
4. Global Temporal Encoding
  The observed feature sequence is simultaneously processed by a Transformer encoder with positional embeddings to model ordered temporal evolution and long-range dependencies.
5. Graph-Enhanced Temporal Reasoning (GETR)
  Relational features from the graph branch and temporal features from the transformer branch are fused to form a unified graph-enhanced temporal memory of the observed clip.
6. Horizon-Aware Decoding and Prediction
  Learnable horizon queries attend to the fused memory via a Transformer decoder, producing horizon-specific representations that are used to predict future verb, noun, and action labels across multiple anticipation times.
