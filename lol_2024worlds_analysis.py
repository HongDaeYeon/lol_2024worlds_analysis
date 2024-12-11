import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '2024worlds.csv'
data = pd.read_csv(file_path)
data.replace('-', pd.NA, inplace=True)

percentage_columns = ['P%', 'B%', 'P+B%', 'W%', 'CTR%']
for col in percentage_columns:
    data[col] = data[col].str.rstrip('%').astype('float', errors='ignore')
data[percentage_columns] = data[percentage_columns].fillna(0)
if 'GP' in data.columns:
    data['Pick Count'] = (data['P%'] / 100) * data['GP']
    data['Ban Count'] = (data['B%'] / 100) * data['GP']

# Most picked champions
most_picked = data.sort_values(by='P%', ascending=False).head(10)
print("Most picked champions:")
print(most_picked[['Champion', 'P%', 'Pick Count']])

plt.figure(figsize=(10, 6))
sns.barplot(y=most_picked['Champion'], x=most_picked['P%'].astype(float), palette='viridis')
plt.title('Most Picked Champions (Percentage)')
plt.xlabel('Pick Rate (%)')
plt.ylabel('Champion')
plt.show()

# Most banned champions
most_banned = data.sort_values(by='B%', ascending=False).head(10)
print("Most banned champions:")
print(most_banned[['Champion', 'B%', 'Ban Count']])

plt.figure(figsize=(10, 6))
sns.barplot(y=most_banned['Champion'], x=most_banned['B%'].astype(float), palette='magma')
plt.title('Most Banned Champions (Percentage)')
plt.xlabel('Ban Rate (%)')
plt.ylabel('Champion')
plt.show()

# KDA vs Win Rate
data['KDA'] = pd.to_numeric(data['KDA'], errors='coerce')
data['W%'] = data['W%'].str.rstrip('%').astype(float)
data = data.dropna(subset=['KDA', 'W%'])

plt.figure(figsize=(10, 6))
plt.scatter(data['KDA'], data['W%'], alpha=0.7, color='blue', edgecolors='k')
plt.title('KDA vs Win Rate', fontsize=16)
plt.xlabel('KDA', fontsize=12)
plt.ylabel('Win Rate (%)', fontsize=12)
plt.grid(alpha=0.3)
plt.show()

# Top 10 Champions by GD10 and XPD10
data['GD10'] = pd.to_numeric(data['GD10'], errors='coerce')
data['XPD10'] = pd.to_numeric(data['XPD10'], errors='coerce')
data = data.dropna(subset=['GD10', 'XPD10'])

plt.figure(figsize=(14, 8))
selected_champions = data.sort_values('GD10', ascending=False).head(10)
plt.plot(selected_champions['Champion'], selected_champions['GD10'], label='GD10 (Gold Difference at 10)', marker='o')
plt.plot(selected_champions['Champion'], selected_champions['XPD10'], label='XPD10 (XP Difference at 10)', marker='s')
plt.title('Top 10 Champions by GD10 and XPD10', fontsize=16)
plt.xlabel('Champion', fontsize=12)
plt.ylabel('Difference at 10 Minutes', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Gold Share vs Damage Share
data['DMG%'] = data['DMG%'].str.rstrip('%').astype(float)
data['GOLD%'] = data['GOLD%'].str.rstrip('%').astype(float)
data = data.dropna(subset=['DMG%', 'GOLD%'])

plt.figure(figsize=(10, 6))
plt.scatter(data['GOLD%'], data['DMG%'], alpha=0.7, color='green', edgecolors='k')
plt.title('Gold Share vs Damage Share', fontsize=16)
plt.xlabel('Gold Share (%)', fontsize=12)
plt.ylabel('Damage Share (%)', fontsize=12)
plt.grid(alpha=0.3)
plt.show()

# GD10, XPD10, CSD10 vs Win Rate
if data['W%'].dtype != 'object':
    data['W%'] = data['W%'].astype(str)
data['W%'] = data['W%'].str.rstrip('%').astype(float)
data['GD10'] = pd.to_numeric(data['GD10'], errors='coerce')
data['XPD10'] = pd.to_numeric(data['XPD10'], errors='coerce')
data['CSD10'] = pd.to_numeric(data['CSD10'], errors='coerce')
data = data.dropna(subset=['W%', 'GD10', 'XPD10', 'CSD10'])

fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

axes[0].scatter(data['GD10'], data['W%'], alpha=0.7, color='blue', edgecolors='k')
axes[0].set_title('GD10 vs Win Rate')
axes[0].set_xlabel('GD10')
axes[0].set_ylabel('Win Rate (%)')

axes[1].scatter(data['XPD10'], data['W%'], alpha=0.7, color='green', edgecolors='k')
axes[1].set_title('XPD10 vs Win Rate')
axes[1].set_xlabel('XPD10')

axes[2].scatter(data['CSD10'], data['W%'], alpha=0.7, color='purple', edgecolors='k')
axes[2].set_title('CSD10 vs Win Rate')
axes[2].set_xlabel('CSD10')

plt.tight_layout()
plt.show()

# Top 10 Champions by Win Rate(Minimum 5 Games Played)
highest_win_rate = data[data['GP'] > 5].sort_values(by='W%', ascending=False).head(10)
print("Highest win rate champions:")
print(highest_win_rate[['Champion', 'W%', 'GP']])

plt.figure(figsize=(10, 6))
sns.barplot(y=highest_win_rate['Champion'], x=highest_win_rate['W%'].astype(float))
plt.title('Top 10 Champions by Win Rate (Minimum 5 Games Played)')
plt.xlabel('Win Rate (%)')
plt.ylabel('Champion')
plt.show()
