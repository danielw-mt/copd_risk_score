import pandas as pd
from pandas_profiling import ProfileReport
import pyreadstat

df, meta = pyreadstat.read_sav('data.sav', disable_datetime_conversion=True)
# df.to_csv('data_python_conversion.csv', index=False)

# preprocessing
db_columns = ['login', 'grp', 'xsect']
binarized_columns= ['dem05_32', 'dem05_16', 'dem05_8', 'dem05_4', 'dem05_2', 'dem05_1','dem08_128', 'dem08_64', 'dem08_32', 'dem08_16', 'dem08_8', 'dem08_4', 'dem08_2', 'dem08_1', 'fclinra01_8192', 'fclinra01_4096', 'fclinra01_2048',  'fclinra01_1024', 'fclinra01_512', 'fclinra01_256', 'fclinra01_128','fclinra01_64', 'fclinra01_32', 'fclinra01_16', 'fclinra01_8', 'fclinra01_4', 'fclinra01_2','fclinra01_1']
# predicted spirometry values could be useful because they are ~independent of age, weight etc.
unnecessary_spirometry = ['bclinra202b_2', 'bclinra202b_5', 'bclinra202c_2', 'bclinra202c_5', 'bclinra203b_2', 'bclinra203b_5', 'bclinra203c_2', 'bclinra203c_5', 'bclinra204b_2', 'bclinra204b_5', 'bclinra204c_2', 'bclinra204c_5', 'bclinra205b_2', 'bclinra205b_5']
# TODO what is sr_med? 
# TODO what is mc_med?

df = df.drop(db_columns, axis=1)
df = df.drop(binarized_columns, axis=1)
df = df.drop(unnecessary_spirometry, axis=1)

missing_value_threshold = 0.93

# TODO convert inches in height to feet


# rename columns
baseline_patient_info ={
    'bclinpt01': 'bl_pt_height',
    'bclinpt02': 'bl_pt_weight',
    'bclinpt03': 'bl_pt_health_conditions_beside_COPD',
    'bclinpt04': 'bl_pt_high_blood_pressure',
    'bclinpt05': 'bl_pt_chest_pain_angina',
    'bclinpt06': 'bl_pt_coronay_artery_disease',
    'bclinpt07': 'bl_pt_heart_failure_congestive_heart_failure',
    'bclinpt08': 'bl_pt_heart_attack',
    'bclinpt09': 'bl_pt_stroke_transient_ischemic_attack',
    'bclinpt10': 'bl_pt_liver_disease_hepatitis_cirrhosis',
    'bclinpt11': 'bl_pt_kidney_disease',
    'bclinpt12': 'bl_pt_arthritis_rheuma',
    'bclinpt12a': 'bl_pt_osteoarthritis_degenerative_arthritis',
    'bclinpt13': 'bl_pt_migraines_headaches',
    'bclinpt14': 'bl_pt_asthma',
    'bclinpt15': 'bl_pt_diabetes_high_blood_sugar',
    'bclinpt16': 'bl_pt_depression',
    'bclinpt17': 'bl_pt_anxiety',
    'bclinpt18': 'bl_pt_sleep_disorder',
    'bclinpt19': 'bl_pt_cancer',
    'bclinpt20': 'bl_pt_type_of_cancer',
    'bclinpt21': 'bl_pt_length_of_COPD',
    'bclinpt22': 'bl_pt_number_of_exacerbations_last_year',
    'bclinpt23': 'bl_pt_number_of_exacerbations_last_2_months',
    'bclinpt24': 'bl_pt_number_of_hospitalization_due_to_COPD_last_year',
    'bclinpt25': 'bl_pt_number_of_hospitalization_due_to_COPD_last_2_months',
    'bclinpt26': 'bl_pt_emergency_room_visits_due_to_COPD_last_year',
    'bclinpt27': 'bl_pt_emergency_room_visits_due_to_COPD_last_2_months',
    'bclinpt28': 'bl_pt_shortness_of_breath',
    'bclinpt29': 'bl_pt_shortness_of_breath_duration',
    'bclinpt30': 'bl_pt_worse_cough',
    'bclinpt31': 'bl_pt_worse_cough_days',
    'bclinpt32': 'bl_pt_increase_in_sputum_or_mucus',
    'bclinpt33': 'bl_pt_increase_in_sputum_or_mucus_duration',
    'bclinpt34': 'bl_pt_fever',
    'bclinpt35': 'bl_pt_fever_duration',
    'bclinpt36': 'bl_pt_breathing_faster',
    'bclinpt37': 'bl_pt_breathing_faster_duration',
    'bclinpt38': 'bl_pt_wheezing',
    'bclinpt39': 'bl_pt_wheezing_duration',
    'bclinpt40': 'bl_pt_other_symptoms',
    'bclinpt41': 'bl_pt_other_symptoms_comment',
    'bclinpt42': 'bl_pt_other_symptoms_duration',
    'bclinpt43': 'bl_pt_medications',
    'bclinpt44': 'bl_pt_other_antibiotic_comment',
    'bclinpt45': 'bl_pt_other_medication_comment',
}

baseline_recorded_info = {
    'bclinra01': 'bl_ra_height',
    'bclinra01b': 'bl_ra_height_date',
    'bclinra02': 'bl_ra_weight',
    'bclinra02b': 'bl_ra_weight_date',
    'bclinra03': 'bl_ra_COPD_type',
    'bclinra202': 'bl_ra_FEV1_1',
    'bclinra203': 'bl_ra_FVC_1',
    'bclinra204': 'bl_ra_PEF_1',
    'bclinra205': 'bl_ra_FEV1_FVC_ratio_1',
    'bclinra201': 'bl_ra_COPD_type_comment',
    'bclinra05': 'bl_ra_spirometry_date',
    'bclinra06': 'bl_ra_COPD_medications',
    'bclinra06a': 'bl_ra_COPD_medications_comment',
    'bclinra07': 'bl_ra_COPD_state_clinician',
    'bclinra08': 'bl_ra_Anthonisen_exacerbation_type',
    'bclinra09': 'bl_ra_sustained_exacerbation_and_medication',
    'bclinra10': 'bl_ra_hospitalization_required',
    'bclinra11': 'bl_ra_COPD_GOLD_stage',
    'bclinra101': 'bl_ra_FEV1_2',
    'bclinra102': 'bl_ra_FVC_2',
    'bclinra103': 'bl_ra_PEF_2',
    'bclinra104': 'bl_ra_FEV1_FVC_ratio_2',
    'bclinra13': 'bl_ra_spirometry_date_2',
    'bclinra14': 'bl_ra_6_minute_walk_score',
    'bclinra15': 'bl_ra_6_minute_walk_score_date',
    'bclinra16': 'bl_ra_patient_group',
    'bclinra17': 'bl_ra_date_enrolled',
}
clinical_follow_up = {
    'bclinra18': 'fl_pt_not_enrolled_reason',
    'bclinra28': 'fl_pt_shortness_of_breath',
    'bclinra29': 'fl_pt_shortness_of_breath_duration',
    'bclinra30': 'fl_pt_worse_cough',
    'bclinra31': 'fl_pt_worse_cough_days',
    'bclinra32': 'fl_pt_increase_in_sputum_or_mucus',
    'bclinra33': 'fl_pt_increase_in_sputum_or_mucus_duration',
    'bclinra34': 'fl_pt_fever',
    'bclinra35': 'fl_pt_fever_duration',
    'bclinra36': 'fl_pt_breathing_faster',
    'bclinra37': 'fl_pt_breathing_faster_duration',
    'bclinra38': 'fl_pt_wheezing',
    'bclinra39': 'fl_pt_wheezing_duration',
    'bclinra40': 'fl_pt_other_symraoms',
    'bclinra41': 'fl_pt_other_symraoms_comment',
    'bclinra42': 'fl_pt_other_symraoms_duration',
    'bclinra43': 'fl_pt_medications',
    'bclinra44': 'fl_pt_other_antibiotic_comment',
    'bclinra45': 'fl_pt_other_medication_comment',
    'fclinicpt03': 'fl_pt_hospitalizations_due_to_COPD_past_3_months',
    'fclinpt04': 'fl_pt_emergency_room_visits_due_to_COPD_past_3_months',
    'clinpt05': 'fl_pt_visit_to_doctor_due_to_COPD_past_3_months',
}

df = df.rename(columns=baseline_patient_info)
df = df.rename(columns=baseline_recorded_info)
df = df.rename(columns=clinical_follow_up)

report = ProfileReport(df, minimal=True)
report.to_file("harvard_report_2.html")