import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
sns.set_style('whitegrid')
PRIMARY="#1f77b4"; SECONDARY="#ff7f0e"; NEUTRAL="#7f7f7f"
df = pd.read_csv('data/donors.csv', parse_dates=['first_donation','last_donation'])
# retention over time (simulated quarters)
quarters = ['Q3 20','Q4 20','Q1 21','Q2 21','Q3 21','Q4 21','Q1 22','Q2 22','Q3 22']
repeat_rate = [56,57.2,58.5,59.1,60.8,61.5,63.2,64.8,66]
avg_donation = [195,202,208,215,223,228,238,252,265]
plt.figure(figsize=(9,4))
plt.plot(quarters, repeat_rate, marker='o', color=PRIMARY)
plt.plot(quarters, avg_donation, marker='o', color=SECONDARY)
plt.title('Donor retention rate & avg donation')
plt.savefig('visuals/donor_retention_avgdonation.png', dpi=300, bbox_inches='tight')

# donor segment composition pie (additional)
labels = ['Monthly Sustainers (34%)','Annual Givers (30%)','Event Participants (17%)','Major Donors (14%)','One-time (5%)']
sizes = [34,30,17,14,5]
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.0f%%', textprops=fontsize )
plt.title('Donor segment composition (Oct 2022)')
plt.savefig('visuals/donor_segment_pie.png', dpi=300, bbox_inches='tight')

# additional: LTV distribution
plt.figure(figsize=(8,4))
sns.histplot(df['total_donated'], bins=40, kde=True, color=PRIMARY)
plt.title('Donor total donated distribution (LTV)')
plt.xlabel('Total donated ($)')
plt.savefig('visuals/ltv_distribution.png', dpi=300, bbox_inches='tight')
# additional2: donors by donation_count
plt.figure(figsize=(6,4))
df['donation_count'].value_counts().sort_index().plot(kind='bar', color=PRIMARY)
plt.title('Donors by donation count')
plt.xlabel('Donation count')
plt.savefig('visuals/donors_by_count.png', dpi=300, bbox_inches='tight')
