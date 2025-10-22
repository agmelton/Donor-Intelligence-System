[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-Online-%231f77b4?style=flat-square&logo=github)](https://agmelton.github.io/donor-intelligence-system/dashboard/)

# Donor Intelligence System

**Donor segmentation, LTV, and churn analytics for nonprofit fundraising**

## Table of contents
- [Overview](#overview)
- [Business context](#business-context)
- [Methodology](#methodology)
- [Key results and insights](#key-results-and-insights)
- [Recommendations](#recommendations)
- [Data dictionary](#data-dictionary)
- [How to view the dashboard](#how-to-view-the-dashboard)


## Overview
A polished, recruiter-ready analysis delivered by Anna Grace Melton. This repository contains data, analysis code, static visuals, and a dashboard that can be published via GitHub Pages.

## Business context
Clear, concise business context relevant to the project.

## Methodology
Analyses were performed using Python (pandas, numpy, matplotlib, seaborn, scikit-learn where used). Visuals are embedded below and in `/dashboard/index.html`.

## Key results and insights

<!-- visuals embedded below -->


## Key results and insights

### Donor retention rate & average donation

<img src="dashboard/../visuals/donor_retention_avgdonation.png" alt="Donor retention rate & average donation" width="700" />

### Donor segment composition

<img src="dashboard/../visuals/donor_segment_pie.png" alt="Donor segment composition" width="700" />

### Donor LTV distribution

<img src="dashboard/../visuals/ltv_distribution.png" alt="Donor LTV distribution" width="700" />

### Donors by donation count

<img src="dashboard/../visuals/donors_by_count.png" alt="Donors by donation count" width="700" />


## Recommendations
- Prioritize monthly sustainer acquisition and targeted re-engagement for high-risk donors.

## Data dictionary
- donors.csv: donor-level aggregated metrics: donor_id, first_donation, last_donation, donation_count, total_donated

## How to view the dashboard
To view the dashboard live, enable GitHub Pages under Settings → Pages → main branch / (root).
