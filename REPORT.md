## Table of Contents

- [Introduction](#introduction)
- [Overview](#overview)

## Introduction

| Name | Student number | Email |
|---|---|---|
| Kehinde Adewusi | 20251105  | 20251105@novaims.unl.pt |
| Pedro Fonseca | xxx  | xxx@novaims.unl.pt |
| Nuno Pinto | yyy  | yyy@novaims.unl.pt |


## Business Objectives

The business objectives of this solution is to predict Telco churn of customers given data gathered in the previous quarter. The cost of new acquisitions is significanly higher than retaining existing customers and the goal is to prevent churn. Given customer data, it is benefial to identify churn.

Additionally, understanding churn characters will help to know where to invest marketing spend to retain the identified classes of customers with high probabilities of churning.

## Assumptions
- Output that matters is a Yes/No 

## Problem Framing
- Supervised learning: We have a labelled dataset.
- Classification problem: with a target i.e. churn or no-churn
- We do not have a continuous flow of data and the data is small enough to fit in memory, so a plain batch learning will be employed.

### Performance measure

TODO:
 - decide on PR-AUC if we find that the dataset is inbalanced, or F1-Score if it's balanced. F1 will inflate for an inbalanced dataset.
 - If we decide to do further classification of customers by risk tier, then ROC-AUC, followed by the decision above.
    - evaluates the quality of probabilities across all thresholds.
    - recall (sensitivity). we want recall to be high ??
    - precision if we are careful about budget
