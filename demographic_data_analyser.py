import pandas as pd

def calculate_demographic_data(print_data = True):
    df = pd.read_csv("adult.data.csv", usecols = [0,1,3,6,8,9,12,13,14], na_values = ['?']).dropna()
    # print(df.columns.tolist() )

    race_count = df['race'].value_counts()
    average_age_men = df[ df['sex'] == 'Male' ]['age'].mean().round(1)
    percentage_bachelors = ( df['education'].value_counts().loc['Bachelors']/len(df) *100 ).round(1)

    edu_mask = [ df['education'].isin(['Bachelors', 'Masters', 'Doctorate']), ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) ]
    higher_education_rich = round( len(df[ (edu_mask[0])  & (df['salary'] == '>50K') ]) / len(df[ edu_mask[0] ]) *100 , 1)
    lower_education_rich = round( len(df[ (edu_mask[1])  & (df['salary'] == '>50K') ]) / len(df[ edu_mask[1] ]) *100 , 1)

    min_work_hours = df['hours-per-week'].dropna().min()
    num_min_workers = len(df[ df['hours-per-week'] == min_work_hours ] )
    rich_percentage = round( len(df[ (df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K') ] ) / num_min_workers*100 , 1)

    country_count = df['native-country'].value_counts()
    high_salary_count = df[ df['salary'] == '>50K' ]['native-country'].value_counts()
    ratio = high_salary_count / country_count
    highest_earning_country , highest_earning_country_percentage = ratio.idxmax() , ( ratio.max()*100 ).round(1)

    top_IN_occupation = df[ (df['native-country'] == 'India') & (df['salary'] == '>50K') ]['occupation'].mode().iloc[0]


# tests
calculate_demographic_data()
