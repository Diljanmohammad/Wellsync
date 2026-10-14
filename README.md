# WellSync Analytics — Lifestyle & Wellbeing Intelligence

WellSync Analytics is a rebranded, deployable edition of the Lifestyle & Wellbeing Analytics project. It explores how everyday activities such as sleep, exercise, social interaction and recovery relate to self-reported stress and wellbeing.

The original raw and cleaned datasets, ETL notebook and hypothesis-analysis notebook remain included. This edition adds portable notebook paths, trained interpretable regression models, a responsive Flask dashboard, JSON APIs and Vercel deployment configuration.

Using Python for data preparation, analysis, and visualisation, the project demonstrates how basic analytics can support **evidence-based decisions** for wellbeing programmes, HR policies, and digital health products.

---

## CI Logo

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

---

## Dataset Content

The project uses a public survey dataset from Kaggle:

* **Dataset name:** Lifestyle and Wellbeing Data
* **Source:** Kaggle (Yash Dalvi)
* **File format:** CSV
* **Approx. size:** ~16k rows, ~20–30 columns

### Key Variable Types

* **Lifestyle / Activity variables** (example names; actual names documented in the Notebook):

  * Sleep duration (hours per night)
  * Exercise / physical activity frequency
  * Daily screen time / device usage
  * Social interaction (frequency/time spent)
  * Work / study hours

* **Outcome variables:**

  * Self-reported stress level
  * Self-reported wellbeing / happiness / life satisfaction score

* **Optional demographics (depending on dataset fields):**

  * Age
  * Gender
  * Region or country

All data is anonymised, with no personally identifiable information.

---

## Business Requirements

The project is framed around a realistic business case:

> Organisations building wellbeing programmes (e.g. HR teams, student services, wellness apps) want to know which lifestyle factors are most strongly associated with stress and wellbeing, so they can prioritise interventions and communication.

From this, the key **business requirements** are:

1. **BR1 – Identify key lifestyle drivers of stress and wellbeing**  
   Determine which activities (sleep, exercise, screen time, social time, work hours) are most strongly associated with lower stress and higher wellbeing.

2. **BR2 – Provide clear, visual insights for non-technical stakeholders**  
   Deliver intuitive visualisations that communicate the relationships between lifestyle habits and wellbeing outcomes for decision-makers who are not data scientists.

3. **BR3 – Build a simple, interpretable predictive prototype**  
   Create a basic model that estimates stress (or wellbeing) from lifestyle variables, to demonstrate how analytics can support evidence-based decisions.

4. **BR4 – Document an end-to-end ETL & analysis workflow**  
   Show a transparent Python-based pipeline for extracting, cleaning, transforming, analysing, and visualising data, designed to be reproducible and extendable.

---

## Hypothesis and How to Validate

### Primary Hypothesis

> **H1:** Individuals who engage in more health-promoting activities (adequate sleep, regular exercise, balanced social interaction, etc.) will report **higher wellbeing** and **lower stress** compared to those with poorer lifestyle habits.

### Secondary Hypotheses

* **H2:** Higher daily **screen time** is associated with **higher stress** and/or **lower wellbeing** scores.  
* **H3:** The combination of **long work/study hours** and **short sleep duration** is associated with **higher stress** than either factor alone.  
* **H4 (planned – future work):** After adjusting for basic demographics (e.g. age and gender), **exercise frequency** may remain an important predictor of **better wellbeing**.  

  * In this submitted version, H4 is **outlined but not implemented**. A multiple regression model with demographic controls is left deliberately as a future extension.

### Validation Approach

The hypotheses are addressed using:

1. **Descriptive analytics**
   * Compare distributions of lifestyle variables and outcome scores.
   * Look for clear trends (e.g. “short sleepers” vs “normal sleepers”).

2. **Correlation analysis**
   * Compute correlations between lifestyle variables and stress/wellbeing outcomes.
   * Check if directions and magnitudes align with H1–H3.

3. **Group comparisons**
   * Create categories (e.g. low/medium/high exercise, short/normal/long sleep).
   * Compare mean stress/wellbeing across groups.

4. **Regression modelling**
   * Build a simple linear regression model (including an interaction term for sleep × work hours) to test H3 more formally.
   * Inspect coefficients to see whether signs (positive/negative) match expectations.

In this project, **H1–H3 are implemented and discussed in detail** in the Notebook.  
**H4 remains a clearly documented piece of future work** that would require an extended regression with demographic controls.

Results and conclusions for each implemented hypothesis are summarised in the Notebook and briefly synthesised in this README.

---

## Project Plan

### High-Level Steps

1. **Project definition**
   * Select dataset and domain (lifestyle & wellbeing).
   * Formulate business requirements and hypotheses.

2. **Environment setup**
   * Create project structure and virtual environment in VS Code.
   * Install necessary Python libraries.

3. **ETL pipeline**
   * **Extract:** Load CSV from `dataset/raw/`.  
   * **Transform:** Clean and preprocess data (handle missing values, convert data types, create derived features and categories).  
   * **Load:** Save cleaned dataset to `dataset/clean/` and use it for analysis.

4. **Exploratory Data Analysis (EDA)**
   * Descriptive statistics and initial visualisations of key variables.
   * Check distributions, outliers, and basic relationships.

5. **Hypothesis-driven analysis**
   * Correlation matrix and visualisations mapped directly to H1–H3 and BR1–BR3.
   * Group comparisons and simple statistical summaries.

6. **Modelling**
   * Build a basic linear regression model to predict stress from lifestyle variables (including an interaction for sleep × work hours for H3).
   * Evaluate model performance (e.g. R²) and interpret coefficients.

7. **Dashboard / visual reporting**
   * Create a Notebook-based “dashboard” section with clearly labelled visualisations tied to each business requirement.
   * (Optional extension) Add interactive components with Plotly or Streamlit.

8. **Interpretation, limitations, and recommendations**
   * Summarise findings in clear language.
   * Highlight practical implications for wellbeing programmes.
   * Discuss limitations, ethical considerations, and possible extensions such as H4.

### Data Management

* **Collection:** Dataset downloaded from Kaggle and stored in a dedicated `dataset/raw/` folder.  
* **Processing:** All data cleaning steps are performed in the ETL Notebook and clearly documented.  
* **Storage:** Cleaned data saved into `dataset/clean/` to separate raw vs processed data.  
* **Versioning:** Git commit history is used to track the evolution of the project and changes to the notebooks.

### Methodology Rationale

* A **survey dataset** was chosen because it directly reflects individual lifestyle behaviours and perceived wellbeing, aligning with the project’s goals.
* Descriptive, correlational, and regression analyses offer **interpretable, business-friendly** insights rather than black-box models.
* The methodology maps neatly to the assessment focus on:
  * ETL,  
  * visualisation,  
  * hypothesis testing,  
  * storytelling with data.

---

## Rationale to Map Business Requirements to Data Visualisations

| Business Requirement                                           | Visualisation(s) Used                                              | Rationale                                                                                                                                                                        |
| -------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BR1 – Identify key lifestyle drivers of stress & wellbeing** | Correlation heatmap, boxplots, scatter plots with regression lines | Heatmaps give an at-a-glance overview of relationships. Boxplots and scatter plots show how stress/wellbeing change across lifestyle levels and support the hypotheses visually. |
| **BR2 – Visual insights for non-technical stakeholders**       | Histograms/KDE plots, annotated figures, clear titles and notes    | Distribution plots help people understand the sample (e.g. “most people sleep X hours”). Annotations and plain-language labels make plots accessible.                            |
| **BR3 – Simple predictive prototype**                          | Linear regression summary, coefficient table/plots                 | A simple regression model demonstrates how lifestyle factors can be combined to estimate stress, while remaining interpretable for non-technical stakeholders.                   |
| **BR4 – ETL & workflow documentation**                         | Markdown sections, code comments, diagram-style section headings   | Clear structure and explanation of each step demonstrate the pipeline and make it reusable by technical teams.                                                                   |

Each visual in the Notebook is explicitly linked to one or more business requirements in its markdown explanation.

---

## Analysis Techniques Used

### Techniques

* **Descriptive statistics**
  * Mean, median, standard deviation, and distribution checks for key variables.

* **Exploratory Data Analysis (EDA)**
  * Histograms and KDE plots for lifestyle behaviours and wellbeing scores.
  * Boxplots for group comparisons (e.g. sleep categories vs stress).

* **Correlation analysis**
  * Pearson correlation matrix for lifestyle and outcome variables.
  * Heatmap visualisation to summarise relationships at a glance.

* **Group comparisons**
  * Comparisons of mean stress/wellbeing between simple lifestyle groups (e.g. low vs high exercise, short vs longer sleep).

* **Regression modelling**
  * Linear regression predicting stress from lifestyle variables, including an interaction term for work hours × sleep (to test H3).
  * Model coefficients interpreted in plain language.

More advanced hypothesis tests and demographic-adjusted models (e.g. for H4) are described as **future extensions** rather than implemented features in this version.

### Limitations & Alternative Approaches

* The dataset is **cross-sectional**, so causal statements cannot be made; a longitudinal design would be needed for causal inference.
* Self-report data introduces bias; pairing lifestyle logs with objective measures (e.g. wearable data) would strengthen conclusions.
* More advanced models (Random Forest, Gradient Boosting) or regularisation techniques (Lasso/Ridge) could offer better predictive performance but were deprioritised in favour of interpretability for non-technical audiences.
* Limited use of demographic variables means potential confounding effects (e.g. age, gender) are not fully explored; this motivates H4 as future work.

### Use of Generative AI Tools

Generative AI tools (such as Copilot in VS Code and ChatGPT) were used for:

* **Ideation and design thinking**
  * Refining business requirements.
  * Structuring the README and Notebook layout.

* **Code optimisation and patterns**
  * Suggesting idiomatic pandas and plotting patterns.
  * Providing template examples for regression and plotting, which were then adapted and verified.

* **Narrative support**
  * Drafting initial explanations and summaries, later edited by the learner.

All AI-assisted content was reviewed, tested, and, where necessary, modified. AI tools were treated as helpers, not as sources of final, unedited code.

---

## Ethical Considerations

### Data Privacy

* The dataset is anonymised and does not include direct identifiers.
* No attempt was made to re-identify individuals, and analysis focuses on aggregate patterns.

### Bias & Fairness

* The sample may not be demographically representative (e.g. skewed towards certain age groups, countries, or socioeconomic status).
* This can bias the relationships observed, so conclusions are presented cautiously and framed as **pattern insights**, not universal truths.

### Legal & Societal Issues

* The data is used under the terms of its public release on Kaggle, within an educational context.
* Results are not used for any decisions affecting real individuals and are explicitly labelled as exploratory.
* The project avoids prescriptive or moralising claims about “correct” lifestyles and instead focuses on statistically observable associations.

---

## Dashboard Design

Although the primary implementation is a **Jupyter Notebook**, the analysis is structured to function like a simple analytics dashboard, and could be transferred to Plotly Dash or Streamlit.

### Planned Dashboard Pages / Sections

1. **Overview**
   * Project summary, dataset overview.
   * Key high-level statistics (e.g. average sleep, stress, wellbeing).

2. **Lifestyle Distributions**
   * Histograms/KDE plots for sleep, exercise, screen time, social time, work hours.
   * Quick understanding of how the sample actually lives.

3. **Lifestyle vs Stress**
   * Boxplots and scatter plots (with regression lines) exploring:
     * Sleep vs stress
     * Exercise vs stress
     * Screen time vs stress
     * Combined effects (e.g. sleep × work hours for H3)

4. **Lifestyle vs Wellbeing**
   * Similar plots showing lifestyle vs wellbeing/happiness scores.
   * Focus on positive outcomes and protective factors.

5. **Correlation & Modelling**
   * Correlation heatmap between lifestyle variables and outcomes.
   * Simple linear model summary with brief explanation of key predictors.

### Communicating Insights to Different Audiences

* **Non-technical stakeholders**
  * Clear titles, legends, and annotations.
  * Plain-language explanations under each visual.
  * Focus on “what this means in real life” rather than technical jargon.

* **Technical audiences**
  * Access to full code in the Notebook.
  * Model metrics and assumptions documented.
  * Details of cleaning and feature engineering steps.

---

## Unfixed Bugs

* No critical bugs are known at the time of submission.
* Minor improvements (e.g. further plot styling and additional edge-case checks) are noted as comments in the Notebook and could be addressed in future iterations.

---

## Development Roadmap

### Challenges and Strategies

* **Challenge:** Understanding which variables to prioritise from a relatively wide dataset.  
  **Strategy:** Start with domain intuition (sleep, exercise, screen time) and then use correlations and EDA to refine focus.

* **Challenge:** Balancing technical detail with readability for non-technical users.  
  **Strategy:** Keep the core model simple and invest more in clear visualisations and explanations.

* **Challenge:** Ensuring ETL and visualisation steps are reproducible.  
  **Strategy:** Use a clear folder structure, separation of raw vs clean data, and a consistent Notebook layout.

### Future Enhancements

* Extend the Notebook into a full **interactive dashboard** using Plotly Dash or Streamlit.
* Implement **H4** properly by building a multiple regression model that includes demographic controls (e.g. age, gender) to test whether exercise remains a significant predictor of wellbeing.
* Incorporate **demographic stratification** (e.g. insights per age group).
* Explore **time-based data** (if available in future datasets) to move from cross-sectional to trend analysis.
* Experiment with more advanced models and regularisation to see if predictive performance can be improved without losing interpretability.

---

## Deployment

The notebooks remain the technical analysis deliverable. A new Flask interface exposes the analytics as a deployable dashboard.

### Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

### Deploy on Vercel

1. Push all project files and folders to GitHub.
2. Import that repository from the Vercel dashboard.
3. Keep Framework Preset as **Flask** and Root Directory as `./`.
4. Leave Build Command, Output Directory and environment variables blank.
5. Deploy.

The trained `model/wellsync_models.pkl` file is included, so deployment does not retrain the model.

### API routes

* `GET /api/health`
* `GET /api/insights`
* `POST /api/predict`

### Important model limitation

The stress model has low explanatory power because perceived stress is influenced by many factors absent from this cross-sectional survey. Its result is labelled as an educational estimate rather than a diagnosis. The work-life-balance regression is substantially stronger, but still represents association rather than causation.

---

## Main Data Analysis Libraries

The project uses the following key libraries:

* **pandas**
  * Data loading, cleaning, transformation.
  * Example: handling missing values, creating new derived columns.

* **numpy**
  * Numerical operations and array handling used under the hood with pandas.

* **matplotlib**
  * Base plotting library for fundamental charts and fine-tuning.

* **seaborn**
  * High-level statistical visualisations: histograms, boxplots, scatter plots, correlation heatmaps.

* **scikit-learn**
  * Simple linear regression model and basic performance metrics (e.g. R²).

These libraries are listed in `requirements.txt` and imported in the Notebook with clear usage examples.

---

## Credits

### Content & Data

* **Dataset:**
  * *Lifestyle and Wellbeing Data* – Kaggle dataset by Yash Dalvi.
* **General guidance:**
  * Code Institute course material for Data Analytics and Python for Data Preparation.

### Code & Tutorials

* Official documentation for:
  * pandas
  * seaborn
  * matplotlib
  * scikit-learn
* Occasional reference to community examples (e.g. Stack Overflow) for specific syntax questions such as plot customisation and regression usage, referenced in comments where patterns were adapted.

### Generative AI

* ChatGPT and GitHub Copilot were used to:
  * Refine project structure and README text.
  * Suggest code snippets and patterns, later reviewed and adapted by the learner.

---

## Acknowledgements (Optional)

* Code Institute facilitators, mentors, and peers for feedback and guidance.
* Friends and colleagues who provided informal feedback on the clarity of visualisations and explanations.
