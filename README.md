# Statistic-Normaltest-in-python
This project demonstrates normality tests (D’Agostino-Pearson and Shapiro-Wilk) for salary and work experience data.  

Results: 
Normal test for salaries:0.18071878885695186
Normal test for work_experience:0.6172165634201328
Shapiro-Wilk test for salaries:0.18071878885695186
Shapiro-Wilk test for work_experience:0.7653602896426936

Conclusions:
The results of both tests showed that the first distribution is normal (p-value > 0.05), while the second deviates from normality (p-value < 0.05).

The D’Agostino-Pearson test returned a p-value > 0.05, so we accept the hypothesis of normality. The Shapiro-Wilk test returned a p-value < 0.05, indicating a deviation from normality. The histogram shows an asymmetric distribution, which makes the Shapiro-Wilk result more reliable.
