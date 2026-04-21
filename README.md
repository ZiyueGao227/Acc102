# Acc102
Acc102 code,README and reflection report 
Global Firm Distribution and Industry Structure: A WRDS-Based Python Data Story

Project Title
Global Firm Distribution and Industry Structure: A WRDS-Based Python Data Story

Problem and User
This project addresses the core question: **What are the global geographical and industrial concentration patterns of publicly listed firms?**
It transforms raw corporate data from WRDS into intuitive, easy-to-understand insights for non-technical audiences, including:
- Business school students
- Beginner investors
- General readers interested in global market structure

The project solves the pain point of inaccessible raw financial research data by creating simplified visualizations and narrative explanations of firm distribution.

Data
Source: Wharton Research Data Services (WRDS) – Compustat Database (`comp.company` table)
- **Key Variables**:
  - `gvkey`: Unique firm identifier
  - `conm`: Company name
  - `fic`: Country code (geography)
  - `sic`: Standard Industrial Classification code
  - `naics`: North American Industry Classification System code
- Data Scope: Global publicly listed firms (covered by Compustat)

Methods
Data Acquisition: Python connection to WRDS + SQL query extraction
Data Cleaning: Remove duplicates and rows with missing country codes
Descriptive Analysis: Count firms by country and industry
Data Transformation: Aggregate 4-digit SIC codes into 2-digit industry groups
Visualization: Horizontal bar charts for top 10 countries and top 10 industries
Narrative Generation: Auto-generated business interpretations for social media/data story narration

Key Findings
- Clear geographical concentration: A small number of countries host the vast majority of listed firms.
- Obvious industrial concentration: Several 2-digit SIC industries account for a large share of global public firms.
- The distribution pattern directly reflects global capital market and industrial structure characteristics.

How to Run
Install required packages: `wrds`, `pandas`, `matplotlib`
Configure WRDS account credentials in Python environment
Run the main data extraction & cleaning script
Execute analysis and visualization modules
Output charts and automated interpretation text

Limitations and Next Steps
Limitations
- Only descriptive analysis (no causal inference)
- Simplified geographic and industry classification
- Sample limited to Compustat-listed firms (not full global economy)
- No financial performance indicators (assets, revenue, profit)

Next Steps
- Add firm size metrics (assets, sales) and compare by country/industry
- Map country codes to full country names
- Add time-series analysis to track distribution changes over years
- Include financial performance for deeper industry comparison
