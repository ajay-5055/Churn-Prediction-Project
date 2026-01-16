import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from log_code import setup_logging
logger = setup_logging('ploting')

class PLOT:
    def plots(df):
        try:
            total_customers = len(df)
            grouped = (df.groupby(['gender', 'SeniorCitizen', 'Churn']).size().unstack(fill_value=0))
            x_labels = [(g, s) for g, s in grouped.index]
            x = np.arange(len(x_labels))
            width = 0.35
            churn_no = grouped['No']
            churn_yes = grouped['Yes']
            plt.figure(figsize=(7, 4))
            bars1 = plt.bar(x - width / 2, churn_no, width,
                            label='Churn = No', color='g')
            bars2 = plt.bar(x + width / 2, churn_yes, width,
                            label='Churn = Yes', color='y')
            for bar in bars1:
                value = bar.get_height()
                percent = (value / total_customers) * 100
                plt.text(bar.get_x() + bar.get_width() / 2,value / 2,
                         f"{int(value)}\n{percent:.1f}%",ha='center',
                         va='center', color='white', fontsize=9)
            for bar in bars2:
                value = bar.get_height()
                percent = (value / total_customers) * 100
                plt.text(bar.get_x() + bar.get_width() / 2,value / 2,
                    f"{int(value)}\n{percent:.1f}%",ha='center',
                         va='center', color='white', fontsize=9)
            plt.xticks(x, x_labels)
            plt.xlabel('Gender and Senior Citizen')
            plt.ylabel('Customer Count')
            plt.title('Churn by Gender and Senior Citizen')
            plt.legend(title='Churn')

            plt.text(0.98, 0.95,'Senior Citizen\n0 = Non-Senior\n1 = Senior',
                transform=plt.gca().transAxes,ha='right', va='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.85)
            )

            data = df.groupby(['PhoneService', 'gender', 'SeniorCitizen', 'Churn']).size().unstack(fill_value=0)
            fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
            width = 0.35
            for i, phone in enumerate(['No', 'Yes']):
                temp = data.loc[phone]
                x = np.arange(len(temp))
                axes[i].bar(x - width / 2, temp['No'], width, label='Churn = No')
                axes[i].bar(x + width / 2, temp['Yes'], width, label='Churn = Yes')
                for j in range(len(temp)):
                    axes[i].text(x[j] - width / 2,temp['No'].iloc[j],temp['No'].iloc[j],ha='center', va='bottom', fontsize=8)
                    axes[i].text(x[j] + width / 2,temp['Yes'].iloc[j],temp['Yes'].iloc[j],ha='center', va='bottom', fontsize=8)
                axes[i].set_xticks(x)
                axes[i].set_xticklabels(list(temp.index), rotation=45)
                axes[i].set_title(f'Phone Service = {phone}')
                axes[i].set_xlabel('Gender & SeniorCitizen')
            axes[0].set_ylabel('Number of Customers')
            fig.legend(['Churn = No', 'Churn = Yes'], loc='upper right')
            fig.text(0.01, 0.92,'Senior Citizen\n0 = Non-Senior\n1 = Senior')
            fig.suptitle('Churn Analysis by Phone Service, Gender and Senior Citizen')
            plt.tight_layout()

            fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
            width = 0.35
            for i, churn in enumerate(['No', 'Yes']):
                temp = df[df['Churn'] == churn]
                grouped = (temp.groupby(['MultipleLines', 'gender']).size().unstack(fill_value=0))
                x = np.arange(len(grouped))
                axes[i].bar(x - width / 2, grouped['Male'], width, label='Male')
                axes[i].bar(x + width / 2, grouped['Female'], width, label='Female')
                for j in range(len(grouped)):
                    axes[i].text(x[j] - width / 2, grouped['Male'].iloc[j],grouped['Male'].iloc[j], ha='center', va='bottom', fontsize=8)
                    axes[i].text(x[j] + width / 2, grouped['Female'].iloc[j],grouped['Female'].iloc[j], ha='center', va='bottom', fontsize=8)
                axes[i].set_xticks(x)
                axes[i].set_xticklabels(grouped.index, rotation=20)
                axes[i].set_title(f'Churn = {churn}')
                axes[i].set_xlabel('MultipleLines')
                axes[i].set_ylabel('Number of Customers')
                axes[i].legend(title='Gender')
            fig.suptitle('MultipleLines vs Gender by Churn')
            plt.tight_layout()

            grouped = (df.groupby(['InternetService', 'Sim']).size().unstack(fill_value=0))
            x = np.arange(len(grouped)) 
            width = 0.2 
            plt.figure(figsize=(10, 5))
            plt.bar(x - 1.5 * width, grouped['Airtel'], width, label='Airtel')
            plt.bar(x - 0.5 * width, grouped['Jio'], width, label='Jio')
            plt.bar(x + 0.5 * width, grouped['BSNL'], width, label='BSNL')
            plt.bar(x + 1.5 * width, grouped['Vi'], width, label='Vi')
            for i in range(len(grouped)):
                plt.text(x[i] - 1.5 * width, grouped['Airtel'].iloc[i],grouped['Airtel'].iloc[i], ha='center', va='bottom', fontsize=8)
                plt.text(x[i] - 0.5 * width, grouped['Jio'].iloc[i],grouped['Jio'].iloc[i], ha='center', va='bottom', fontsize=8)
                plt.text(x[i] + 0.5 * width, grouped['BSNL'].iloc[i],grouped['BSNL'].iloc[i], ha='center', va='bottom', fontsize=8)
                plt.text(x[i] + 1.5 * width, grouped['Vi'].iloc[i],grouped['Vi'].iloc[i], ha='center', va='bottom', fontsize=8)
            plt.xticks(x, grouped.index)
            plt.xlabel('Internet Service')
            plt.ylabel('Number of Customers')
            plt.title('Internet Service vs SIM Distribution')
            plt.legend(title='SIM')

            fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
            width = 0.35
            for i, sc in enumerate([0, 1]):
                temp = df[df['SeniorCitizen'] == sc]
                grouped = (temp.groupby(['Sim', 'gender']).size().unstack(fill_value=0))
                x = np.arange(len(grouped))
                axes[i].bar(x - width / 2, grouped['Male'], width, label='Male')
                axes[i].bar(x + width / 2, grouped['Female'], width, label='Female')
                for j in range(len(grouped)):
                    axes[i].text(x[j] - width / 2, grouped['Male'].iloc[j],grouped['Male'].iloc[j], ha='center', va='bottom', fontsize=8)
                    axes[i].text(x[j] + width / 2, grouped['Female'].iloc[j],grouped['Female'].iloc[j], ha='center', va='bottom', fontsize=8)
                axes[i].set_xticks(x)
                axes[i].set_xticklabels(grouped.index)
                axes[i].set_title(f'SeniorCitizen = {sc}')
                axes[i].set_xlabel('SIM')
                axes[i].set_ylabel('Number of Customers')
                axes[i].legend(title='Gender')
            fig.suptitle('SIM vs Gender by Senior Citizen')
            plt.tight_layout()

            service_cols = ['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']
            plt.figure(figsize=(18, 10))
            for i, col in enumerate(service_cols, 1):
                plt.subplot(2, 3, i)
                pct = df[col].value_counts(normalize=True) * 100
                ax = pct.plot(kind='bar', color=['c', 'y', 'k'])
                plt.title(f'{col} Usage (%)')
                plt.xlabel('')
                plt.ylabel('Percentage')
                for container in ax.containers:
                    ax.bar_label(container, fmt='%.1f%%')
            plt.tight_layout()

            for sim in df['Sim'].unique():
                sim_df = df[df['Sim'] == sim]
                fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
                width = 0.35
                for i, churn in enumerate(['No', 'Yes']):
                    temp = sim_df[sim_df['Churn'] == churn]
                    grouped = (temp.groupby(['Contract', 'gender']).size().unstack(fill_value=0))
                    x = np.arange(len(grouped))
                    axes[i].bar(x - width / 2, grouped['Male'], width, label='Male')
                    axes[i].bar(x + width / 2, grouped['Female'], width, label='Female')
                    for j in range(len(grouped)):
                        axes[i].text(x[j] - width / 2, grouped['Male'].iloc[j],grouped['Male'].iloc[j], ha='center', va='bottom', fontsize=8)
                        axes[i].text(x[j] + width / 2, grouped['Female'].iloc[j],grouped['Female'].iloc[j], ha='center', va='bottom', fontsize=8)
                    axes[i].set_xticks(x)
                    axes[i].set_xticklabels(grouped.index, rotation=15)
                    axes[i].set_title(f'Churn = {churn}')
                    axes[i].set_xlabel('Contract')
                    axes[i].set_ylabel('Number of Customers')
                    axes[i].legend(title='Gender')
                fig.suptitle(f'Contract vs Gender by Churn (SIM = {sim})')
                plt.tight_layout()

            fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
            width = 0.35
            for i, churn in enumerate(['No', 'Yes']):
                temp = df[df['Churn'] == churn]
                grouped = (temp.groupby(['PaperlessBilling', 'gender']).size().unstack(fill_value=0))
                x = np.arange(len(grouped))
                axes[i].bar(x - width / 2, grouped['Male'], width, label='Male')
                axes[i].bar(x + width / 2, grouped['Female'], width, label='Female')
                for j in range(len(grouped)):
                    axes[i].text(x[j] - width / 2, grouped['Male'].iloc[j],grouped['Male'].iloc[j], ha='center', va='bottom', fontsize=8)
                    axes[i].text(x[j] + width / 2, grouped['Female'].iloc[j],grouped['Female'].iloc[j], ha='center', va='bottom', fontsize=8)
                axes[i].set_xticks(x)
                axes[i].set_xticklabels(grouped.index)
                axes[i].set_title(f'Churn = {churn}')
                axes[i].set_xlabel('Paperless Billing')
                axes[i].set_ylabel('Number of Customers')
                axes[i].legend(title='Gender')
            fig.suptitle('Paperless Billing vs Gender by Churn')
            plt.tight_layout()

            fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
            width = 0.35
            for i, churn in enumerate(['No', 'Yes']):
                temp = df[df['Churn'] == churn]
                grouped = (temp.groupby(['PaymentMethod', 'gender']).size().unstack(fill_value=0))
                x = np.arange(len(grouped))
                axes[i].bar(x - width / 2, grouped['Male'], width, label='Male')
                axes[i].bar(x + width / 2, grouped['Female'], width, label='Female')
                for j in range(len(grouped)):
                    axes[i].text(x[j] - width / 2, grouped['Male'].iloc[j],grouped['Male'].iloc[j], ha='center', va='bottom', fontsize=8)
                    axes[i].text(x[j] + width / 2, grouped['Female'].iloc[j],grouped['Female'].iloc[j], ha='center', va='bottom', fontsize=8)
                axes[i].set_xticks(x)
                axes[i].set_xticklabels(grouped.index, rotation=30, ha='right')
                axes[i].set_title(f'Churn = {churn}')
                axes[i].set_xlabel('Payment Method')
                axes[i].set_ylabel('Number of Customers')
                axes[i].legend(title='Gender')
            fig.suptitle('Payment Method vs Gender by Churn')
            plt.tight_layout()

            for sim in df['Sim'].unique():
                sim_df = df[df['Sim'] == sim]
                fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
                width = 0.45
                for i, churn in enumerate(['No', 'Yes']):
                    temp = sim_df[sim_df['Churn'] == churn]
                    grouped = (temp.groupby([((temp['tenure'] - 1) // 3 + 1), 'gender']).size().unstack(fill_value=0))
                    x = np.arange(len(grouped))
                    axes[i].bar(x - width / 2, grouped['Male'], width, label='Male')
                    axes[i].bar(x + width / 2, grouped['Female'], width, label='Female')
                    for j in range(len(grouped)):
                        axes[i].text(x[j] - width / 2, grouped['Male'].iloc[j],grouped['Male'].iloc[j], ha='center', va='bottom', fontsize=8)
                        axes[i].text(x[j] + width / 2, grouped['Female'].iloc[j],grouped['Female'].iloc[j], ha='center', va='bottom', fontsize=8)
                    axes[i].set_xticks(x)
                    axes[i].set_xticklabels([int(q) for q in grouped.index]) 
                    axes[i].set_title(f'Churn = {churn}')
                    axes[i].set_xlabel('Tenure (Quarter Number)')
                    axes[i].set_ylabel('Customers')
                    axes[i].legend(title='Gender')
                fig.suptitle(f'Quarterly Tenure Analysis | SIM = {sim}')
                plt.tight_layout()

            charge_bins = [0, 25, 50, 75, 100, 125]
            charge_labels = ['0-25', '26-50', '51-75', '76-100', '101-125']
            fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
            width = 0.2
            for i, churn in enumerate(['No', 'Yes']):
                temp = df[df['Churn'] == churn].copy()
                temp['ChargeGroup'] = pd.cut(temp['MonthlyCharges'],bins=charge_bins,labels=charge_labels)
                grouped = (temp.groupby(['ChargeGroup', 'Sim'], observed=True).size().unstack(fill_value=0))
                x = np.arange(len(grouped))
                axes[i].bar(x - 1.5 * width, grouped['Airtel'], width, label='Airtel')
                axes[i].bar(x - 0.5 * width, grouped['Jio'], width, label='Jio')
                axes[i].bar(x + 0.5 * width, grouped['BSNL'], width, label='BSNL')
                axes[i].bar(x + 1.5 * width, grouped['Vi'], width, label='Vi')
                for j in range(len(grouped)):
                    axes[i].text(x[j] - 1.5 * width, grouped['Airtel'].iloc[j],grouped['Airtel'].iloc[j], ha='center', va='bottom', fontsize=7)
                    axes[i].text(x[j] - 0.5 * width, grouped['Jio'].iloc[j],grouped['Jio'].iloc[j], ha='center', va='bottom', fontsize=7)
                    axes[i].text(x[j] + 0.5 * width, grouped['BSNL'].iloc[j],grouped['BSNL'].iloc[j], ha='center', va='bottom', fontsize=7)
                    axes[i].text(x[j] + 1.5 * width, grouped['Vi'].iloc[j],grouped['Vi'].iloc[j], ha='center', va='bottom', fontsize=7)
                axes[i].set_xticks(x)
                axes[i].set_xticklabels(grouped.index)
                axes[i].set_title(f'Churn = {churn}')
                axes[i].set_xlabel('Monthly Charges Range')
                axes[i].set_ylabel('Number of Customers')
                axes[i].legend(title='SIM')
            fig.suptitle('Monthly Charges vs SIM by Churn')
            plt.tight_layout()

            for sc in [0, 1]:
                sc_df = df[df['SeniorCitizen'] == sc]
                fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
                width = 0.35
                for i, churn in enumerate(['No', 'Yes']):
                    temp = sc_df[sc_df['Churn'] == churn]
                    grouped = (temp.groupby(['Region', 'gender']).size().unstack(fill_value=0))
                    x = np.arange(len(grouped))
                    axes[i].bar(x - width / 2, grouped['Male'], width, label='Male')
                    axes[i].bar(x + width / 2, grouped['Female'], width, label='Female')
                    for j in range(len(grouped)):
                        axes[i].text(x[j] - width / 2, grouped['Male'].iloc[j],grouped['Male'].iloc[j], ha='center', va='bottom', fontsize=8)
                        axes[i].text(x[j] + width / 2, grouped['Female'].iloc[j],grouped['Female'].iloc[j], ha='center', va='bottom', fontsize=8)
                    axes[i].set_xticks(x)
                    axes[i].set_xticklabels(grouped.index)
                    axes[i].set_title(f'Churn = {churn}')
                    axes[i].set_xlabel('Region')
                    axes[i].set_ylabel('Number of Customers')
                    axes[i].legend(title='Gender')
                fig.suptitle(f'Region vs Gender by Churn | SeniorCitizen = {sc}')
                plt.tight_layout()
            plt.show()

        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in line no:{error_line.tb_lineno} due to:{error_msg}')