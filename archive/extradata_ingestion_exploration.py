import pandas as pd

# Load the uploaded dataset
df = pd.read_csv("Synthetic Financial Datasets.csv")

# Preview the first few rows
df.head()
import numpy as np
import warnings

# Patch deprecated np.float and np.bool for seaborn compatibility
if not hasattr(np, 'float'):
    np.float = float
    warnings.warn("Patched np.float for compatibility with seaborn.", DeprecationWarning)

if not hasattr(np, 'bool'):
    np.bool = bool
    warnings.warn("Patched np.bool for compatibility with seaborn.", DeprecationWarning)
# 📚 Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ⚙️ System Patch (already done, but repeat to be safe)
import numpy as np
import warnings
if not hasattr(np, 'float'):
    np.float = float
    warnings.warn("Patched np.float for compatibility with seaborn.", DeprecationWarning)

# ✅ Reload dataset (if needed)
df = pd.read_csv("Synthetic Financial Datasets.csv")

# 🔍 1. Check class distribution
sns.countplot(x='isFraud', data=df)
plt.title("Class Distribution - isFraud")
plt.xticks([0, 1], ['Not Fraud', 'Fraud'])
plt.show()

# 🔍 2. Fraud by transaction type
plt.figure(figsize=(10,5))
sns.countplot(x='type', hue='isFraud', data=df, order=df['type'].value_counts().index)
plt.title("Fraud vs. Transaction Type")
plt.xticks(rotation=45)
plt.show()

# 🔍 3. Summary Stats for Fraud vs Non-Fraud
print("Summary for FRAUD:")
display(df[df['isFraud'] == 1].describe())

print("Summary for NON-FRAUD:")
display(df[df['isFraud'] == 0].describe())

# 🔍 4. Correlation heatmap (numerical features)
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
