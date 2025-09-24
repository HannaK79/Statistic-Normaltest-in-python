import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import normaltest, shapiro

salaries = [3000, 3200, 3500, 3700, 3100, 4000, 3300, 4500, 2900, 4200, 3400, 3100,
            2950, 3600, 3800, 5000, 3700, 5200, 4700, 5500, 4300, 6000, 3100, 2800,
            5000, 3200, 4100, 3900, 4500, 3000]
work_experience = [5.9, 4.9, 5.6, 7.3, 4.8, 4.8, 7.7, 6.6, 3.2, 6.3, 3.9, 3.9, 5.5,
                   3.9, 7.3, 6.7, 5.3, 2.9, 6.6, 5.1, 4.6, 4.6, 5.6, 8.5, 3.7, 4.4,
                   6.4, 4.5, 5.5, 3.6]
# Normaltest Д'Агостіно-Пірсона
_, p_value_salaries = normaltest(salaries)
_, p_value_work_experience = normaltest(work_experience)

# Shapiro-Wilk test
_, p_value_shapiro_salaries = shapiro(salaries)
_, p_value_shapiro_work_experience = shapiro(work_experience)

print(f"Normal test for salaries:{p_value_salaries}")
print(f"Normal test for work_experience:{p_value_work_experience}")


print(f"Shapiro-Wilk test for salaries:{p_value_salaries}")
print(f"Shapiro-Wilk test for work_experience:{p_value_shapiro_work_experience}")
