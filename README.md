# Makmur Jaya's Performance Management System

## Balanced Scorecard Dashboard
This repository contains a prototype dashboard aimed at providing insights into various aspects of organizational performance. The dashboard is designed to be compact yet informative, allowing CEOs and executives to monitor key metrics efficiently.

### Features

- **Data Integration:** Utilizes data from multiple sources including customer orders, reviews, employee attrition, and more.
- **Data Cleaning:** Conducts basic data cleaning operations to ensure data integrity.
- **Visualization:** Presents data visualizations such as histograms to illustrate transaction values, order cycle times, review scores, and job satisfaction distributions.
- **Statistical Analysis:** Calculates median values for metrics such as transaction values, order cycle times, review scores, and job satisfaction.

### Datasets
- https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
  - dataset
    - `olist_order_items_dataset.csv` (columns: 'order_item_id' and 'price' for calculating average order value)
    - `olist_order_reviews_dataset.csv` (column: 'review_score' for calculating average review score)
    - `olist_orders_dataset.csv` (columns: 'order_approved_at' and 'order_delivered_customer_date' for calculating order cycle time)
- https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
  - `WA_Fn-UseC_-HR-Employee-Attrition.csv` (column: 'JobSatisfaction' for calculating job satisfaction score)

### Easy Report
https://medium.com/@albarpambagio/enhancing-executive-effectiveness-makmur-jayas-performance-management-system-3066a89c40ca
