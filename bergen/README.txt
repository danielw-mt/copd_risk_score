READ ME 

Written by Tomas Mikal Eagan 27 february 2022, Bergen, Norway

The datafiles are available as a Stata 17 MP file (.dta) and thus with attached values and value labels, preferable to use if you have access to Stata
And also as a tab-delimited txt file, where labels were exported, not values for most variables (useful for use in for instance R)

Variables in the dataset
sex				- Women & Men
age_cat2		- Age in three categories [in the published paper, we sometimes used age as a continuous variable, then in whole years. That information is not included here in order to maintain full anonymity for participants in the study per current GDPR]
bodycomp		- body composition was assessed with bioelectrical impedance measurements using a Bodystat 1500 to calculate fat mass index (FMI) and fat free mass index (FFMI). Cachexia was defined as having a FFMI < 14 kg/m2 in women and < 17 kg/m2 in men which corresponds to the lower 95% CI in a normal population (19). Similarly, obesity was defined as FMI > 13.5 kg/m2 in women and > 9.3 kg/m2 in men.
smok_habits		- defined as never, ex, or current (daily)
packyrs_10		- Pack years smoked (defined for ex and daily only) where 20 cigarettes/day for one year equals one pack year divided by ten for regression purposes [where a coefficient then equals increased risk (OR) per 10 pack years smoked].
diabetes		- self-reported, and assessed with aid of medical journal by a physician l (knowing for instance all medications used)
statin			- self-reported, and assessed with aid of medical journal by a physician l (knowing for instance all medications used)
ARB_ACE_all		- use of either AII blockers or angiotensin receptor blockers
sign_CACS		- having a calcium score > 100 = "yes", else is "no"
cor_stenosis	- having significant stenosis on CT angiography assessed by one of two experienced cardiology radiologists. Confirmed coronary stenosis was defined as presence of stenosis (lumen reduction > 50%)
COPD_control	- either COPD patient or control without lung disease
gold			- In COPD patients either GOLD stage I/II or stage III/IV
copd_exacerb_cat	- having had a moderate or serious COPD exacerbation the last 12 months or not. Serious = hospitalization, moderate = treatment with systemic antiobiotics and/or steroids	
resp_failure	-	Having arterial blood gass oxygen tension (pO2) < 8 kPa = yes
eosinophilic_COPD	- Having blood eosinophilia defined as ≥0.3*10^9 cells/L = yes
wholelung950	- % lung area of density < 950 Hounsfield units
crp_cat			- C-reactive protein below 5 or 5 and above