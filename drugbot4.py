"""
Drug Information Program — expandable starter script

Educational use only. Verify medication information against reliable,
current sources. This program is not a substitute for medical advice.
"""
import requests
import xml.etree.ElementTree as ET
import re


# ------------------------------------------------------------
# 1. MEDICATION DATABASE
# Add more medications by copying the structure of this entry.
# ------------------------------------------------------------

DRUGS = {
    "fluoxetine": {
        "brand_names": ["Prozac","Sarafem","Prozac Weekly"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Selective Serotonin Reuptake Inhibitor (SSRI)",
        "drug_classes": ["SSRI"],
        "info": [
            "Fluoxetine (brand name: Prozac) is an SSRI drug used for "
            "the treatment of various psychiatric disorders. It was the "
            "first SSRI drug to be discovered, and revolutionized the "
            "antidepressant industry. In 2024, there were over 29 million"
            "Prozac prescriptions in the United States."
        ],
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Obsessive-Compulsive Disorder",
            "Anxiety",
            "Generalized Anxiety Disorder",
            "Bulimia Nervosa",
            "Premenstrual Dysphoric Disorder",
            "PMDD",
            "Panic Disorder",
            "OCD"
        ],
        "off_label_uses":[
            "Bipolar Depression",
            "Cataplexy",
            "Social Anxiety Disorder",
            "Binge Eating Disorder"
        ],
        "side_effects": [
            "Hives",
            "Skin rash",
            "Restlessness",
            "Decreased appetite",
            "Diarrhea",
            "Sexual side effects",
            "Fatigue",
            "QT prolongation"

        ],
        "metabolism": [
            "CYP2D6",
            "CYP2C19",
            "CYP2C9",
            "CYP3A4"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Clorgyline",
            "Dronedarone",
            "Isocarboxazid",
            "Levoketoconazole",
            "Levomethadyl",
            "Linezolid",
            "Mavacamten",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Nialamide",
            "Ozanimod",
            "Phenlezine",
            "Pimozide",
            "Piperaquine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"

        ],
        "half_life": (
            "Fluoxetine's half-life varies with duration of use. After "
            "chronic administration it is commonly about 4–6 days; its "
            "active metabolite, norfluoxetine, has a longer half-life."
        ),
        
        
    },
     "escitalopram": {
        "brand_names": ["Lexapro","Cipralex"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SSRI"],
        "class": "Selective Serotonin Reuptake Inhibitor (SSRI)",
        "metabolism":[
            "CYP2D6"

        ],
        "interactions":[
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Pirlindole",
            "Linezolid",
            "Methylene Blue",
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Dronedarone",
            "Levoketoconazole",
            "Lazabemide",
            "Mesoridazine",
            "Metoclopramide",
            "Nialamide",
            "Ozanimod",
            "Piperaquine",
            "Procarbazine"

        ],
        "info": [
            "Escitalopram (brand name Lexapro) is an SSRI drug. It was approved "
            "for use by the FDA in the United States in 2002. It is on the World "
            "Health Organization's (WHO) list of essential medications. In 2023 "
            "it was the second most prescribed antidepressant and fourteenth most commonly "
            "prescribed medication in the United States with over 37 million prescriptions. "
            "It is also the (S)-enantiomer of citalopram, hence the name 'escitalopram'."

        ],
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Anxiety",
            "Generalized Anxiety Disorder (GAD)",
        ],
        "off_label_uses":[
            "Post Traumatic Stress Disorder (PTSD)",
            "Obsessive-Compulsive Disorder (OCD)",
            "OCD",
            "PTSD",
            "Social Anxiety Disorder",
            "Panic Disorder",
            "Premenstrual Dysphoric Disorder (PMDD)",
            "PMDD"

        ],
        "side_effects": [
            "Nausea",
            "QT prolongation"
            "Trouble sleeping",
            "Dry mouth",
            "Sexual side effects",
            "Dizziness",
            "Insomnia",
            "Somnolence"
            
        
        ],
        "half_life": (
            "The elimination half-life is approximately 27 to 32 hours."
        ),
    },
    "Citalopram": {
        "brand_names": ["Celexa"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SSRI"],
        "class": "Selective Serotonin Reuptake Inhibitor (SSRI)",
        "info":[
            "Citalopram (brand name Celexa) is an SSRI drug used to treat various mental health disorders. "
            "While it is normally administrated in pill form, various European countries "
            "give citalopram intravenously (IV) when initiating treatment, followed by oral "
            "administration in continuation. Citalopram also has a higher affinity for H1 anthistamine "
            "receptors than its isomer, escitalopram. "
        ],
        "metabolism": [
            "CYP2C19",
            "CYP3A4",
            "CYP2D6"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Dronedarone",
            "Fluconazole",
            "Isocarboxazid",
            "Levoketoconazole",
            "Linezolid",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Posaconazole",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"
        ],
        "conditions": [
            "Depression",
            "Major Depressive Disorder"
        ],
        "off_label_issues":[
            "Generalized Anxiety Disorder",
            "Panic Disorder",
            "Body Dysmorphic Disorder",
            "Obsessive-Complusive Disorder",
            "Dysthymia",
            "Hot Flashes",
            "Anxiety"

        ],
        "side_effects": [
            "Sexual side effects",
            "Lack of emotion",
            "Fever",
            "Drowsiness",
            "QT prolongation",
        ],
        "half_life": (
            "About 35 hours in healthy adults"
        ),
    },
    "Sertraline": {
        "brand_names": ["Zoloft"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SSRI"],
        "class": "Selective Serotonin Reuptake Inhibitor (SSRI)",
        "info":[
            "Sertraline (brand name Zoloft) is an SSRI drug used to treat various mental disorders. "
            "It was developed by Pfizer in 1991. It is on the World Health Organization's (WHO) "
            "list of essential medications. In 2016 it was the most commonly prescribed "
            "psychotropic medicine in the United States. Sertraline uniquely has relatively "
            "high activity as an inhibitor of dopamine transporter (DAT). "
        ],
        "metabolism": [
            "CYP2D6",
            "CYP2BR"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Disulfiram",
            "Dronedarone",
            "Ensitrelvir",
            "Fluconazole",
            "Furazolidone",
            "Iproniazid",
            "Isocarboxazid",
            "Ketoconazole",
            "Levoketoconazole",
            "Linezolid",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Posaconazole",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Toloxatone",
            "Tranylcypromine",
            "Ziprasidone"
        ],
        "conditions": [
            "Depression",
            "Generalized Anxiety Disorder (GAD)",
            "Social Anxiety Disorder",
            "OCD",
            "PMDD",
            "PTSD",
            "Obsessive-Compulsive Disorder",
            "Obsessive-Compulsive Disorder (pediatric)"
            "Panic Disorder",
            "Premenstrual Dysphoric Disorder",
            "Post-Traumatic Stress Disorder"
        ],
        "off_label_uses": [
            "Premature ejaculation",
            "Anger"
        ],
        "side_effects": [
            "Nausea",
            "Diarrhea",
            "Headache",
            "Insomnia",
            "Sexual side effects",
            "Dry mouth"
        ],
        "half_life": (
            "The elimination half life of Sertraline (Zoloft) is about 26 hours"
        ),
    },
    "Venlafaxine": {
        "brand_names": ["Effexor","Effexor XR"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry","Neurology","Pain Managment"],
        "drug_classes": ["SNRI"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
        "info":[
            
        ],
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Anxiety",
            "Generalized Anxiety Disorder",
            "Panic Disorder",
            "Social Anxiety Disorder",
            "Social Phobia"
        ],
        "off_label_uses": [
            "Diabetic Neuropathy",
            "Migraines",
            "Hot flashes",
            "Attention deficit/hyperactive disorder (ADHD)",
            "Post-Traumatic Stress Disorder (PTSD)",
            "PTSD",
            "ADHD"
            "Narcolepsy"
        ],
        "side_effects": [
            "Loss of appetite",
            "Sweating",
            "Drowsiness",
            "Sexual side effects",
            "Intense withdrawal side effects"
        ],
        "info":[
            "Venlafaxine is a Serotonin Norepinephrine Reuptake Inhibitor (SNRI) "
            "Venlafaxine can cause severe withdrawal symptoms if stopped suddenly. "
            "Doctors sometimes use antidepressants with a longer half-life in order to taper patients off. At high doses, Venlafaxine inhibits "
            "Serotonin, Norepinephrine and Dopamine. Though the inhibition of dopamine is relatively "
            "low. Hence the SNRI categorization as opposed to SNDRI characterization. "
        ],
        "metabolism": [
            "CYP2D6"
        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Dronedarone",
            "Furazoidone",
            "Ipeoniazid",
            "Isocarboxid",
            "Ketoconazole",
            "Levoketoconazole",
            "Linezolid",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Tranylcypromine",
            "Trifluoperazine",
            "Ziprasidone"

        ],
        "half_life": (
            "Immediate release (IR) formulations half life is about 5 hours."
            "ER or Extrended Release formulations have an 11-15 hour half life"
        ),
    },
    "Duloxetine": {
        "brand_names": ["Cymbalta","Irenka"],
        "categories": ["Antidepressants"],
        "drug_classes": ["SNRI"],
        "specialties": ["Psychiatry","Neurology","Pain Management"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Generalized Anxiety Disorder",
            "Anxiety",
            "Neuropathic pain",
            "Fibromyalgia",

        ],
        "off_label_uses": [

        ],
        "side_effects": [
            "Nausea",
            "Dry mouth",
            "Headache",
            "Dizziness",
            "Sexual side effects",
            "Increased sweating"
        ],
        "info": [
            "Duloxetine is an SNRI drug used for the treatment of both mental disorders "
            "and chronic pain. While tricyclic antidepressants, anticonvulsants and opioids "
            "have better efficacy than Duloxetine, Duloxetine remains more tolerable than opioids. "
            "Duloxetine is known to have unpleasant withdrawals from discontinuing medication "
            "It is used for various forms of pain, such as diabetic neuropathy, multiple sclerosis related "
            "neuropathy. It is considered a first line treatment for anxiety. "

        ],
        "interactions": [
            "Bromopride",
            "Isocarboxazid",
            "Linezolid",
            "Mavorixafor",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Thioridazine",
            "Tranylcypromine",
            "Viloxazine"

        ],
        "metabolism": [
            "CYP2D6",
            "CYP1A2"

        ],
        "half_life": (
            "Duloxetine has a half life of approximately 10-12 hours. "
            "Smoking is known to decrease duloxetine concentration."

        ),
    },
    "Desvenlafaxine": {
        "brand_names": ["Pristiq","Khedezla"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SNRI"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"
        ],
        "off_label_uses": [
            "Hot flashes"
        ],
        "side_effects": [
            "Dizziness",
            "Trouble Sleeping",
            "Increased sweating",
            "Constipation",
            "Sexual side effects"
        ],
        "info": [
            "Desvenlafaxine is an SNRI drug used for the treatment of major depressive disorder. "
            "It has similar efficacy to its' parent compound, Venlafaxine (brand name: Effexor). "
            "It is a syhnethetic form of the isolated major active metabolite of Venlafaxine."

        ],
        "metabolism": [
            "CYP3A4"

        ],
        "interactions": [
            "Bromopride",
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "half_life": (
            "Desvenlafaxine has a half life of about 11 hours. "
        ),
    },
    "Paroxetine": {
        "brand_names": ["Paxil","Brisdelle","Pexeva"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SSRI"],
        "class": "Selective Serotonin Reuptake Inhibitor (SSRI)",
        "conditions": [
            "Major Depressive Disorder",
            "Depression",
            "Generalized Anxiety Disorder (GAD)",
            "Anxiety",
            "Obsessive-Compulsive Disorder (OCD)",
            "Social Anxiety Disorder",
            "Post-Traumatic Stress Disorder (PTSD)",
            "PTSD",
            "PMDD",
            "Premenstrual Dysphoric Disorder (PMDD)"

        ],
        "off_label_uses": [
            "Premature ejaculation",
            "Hot flashes",
            "Fibromyalgia",
            "Compulsive Gambling"

        ],
        "info": [
            "Paroxetine is an SSRI drug used for the treatment of various mental "
            "disorders. It is on the World Health Organization's (WHO) list of essential "
            "medications. Paroxetine was the first antidepressant approved for Panic Disorder "
            "in the USA. Paroxetine is known to have severe withdrawal side effects. Ocassionally, "
            "doctors may use fluoxetine as a 'bridge' in order to taper off of paroxetine. It is widely "
            "considered the most potent and powerful of the SSRI drug class. "

        ],
        "metabolism": [
            "CYP2DR"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Colchicine",
            "Dronedarone",
            "Isocarboxazid",
            "Levoketoconazole",
            "Linezolid",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"
        ],
        "side_effects": [
            "Sexual side effects",
            "Loss of appetite",
            "Sweating",
            "Trouble Sleeping",
            "Nausea"
        ],
        "half_life": (
            "Paroxetine has a half life of about 21 hours."
        ),
    },
    "Fluvoxamine": {
        "brand_names": ["Luvox"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SSRI"],
        "class": "Selective Serotonin Reuptake Inhibitors)",
        "conditions": [
            "Obsessive-Compulsive Disorder (OCD)",
            "Major Depressive Disorder",
            "Depression",
            "Obsessive-Compulsive Disorder (pediatric)",
            "Social Anxiety Disorder"
        ],
        "side_effects": [
            "Constipation",
            "GI issues",
            "Headache",
            "Dry mouth",
            "Abdominal pain",
            "Excessive sweating",
            "Insomnia",
            "Sexual side effects"
        ],
        "off_label_uses":[
            "Separation Anxiety Disorder"


        ],
        "info": [
            "Fluvoxamine (not to be confused with another SSRI, Fluoxetine) is an SSRI drug "
            "used primarily for the treatment of Obsessive-Compulsive Disorder. While all SSRIs "
            "in the USA carry a black box warning, Fluvoxamine has significantly less of a suicide risk "
            "in those under 25 than the other antidepressant drugs. It is also more tolerable than the "
            "other SSRIs, especially in relation to cardiovascular complications. "

        ],
        "metabolism": [
            "CYP1A2",
            "CYP3A4",
            "CYP2D6",
            "CYP2C19",
            "CYP2B6"

        ],
        "interactions": [
            "Agomelatine",
            "Alosetron",
            "Astemizole",
            "Bromopride",
            "Cisapride",
            "Colchicine",
            "Eliglustat",
            "Fezolinetant",
            "Isocarboxazid",
            "Levomethadyl",
            "Linezolid",
            "Mavacamten",
            "Mavorixafor",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Procarbazine",
            "Ramelteon",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Terfenadine",
            "Thioridazine",
            "Tizanidine",
            "Tranylcypromine"
        ],
        "half_life": (
            "In young, healthy volunteers, Fluvoxamine had a half life nbetween 13.6 to "
            "15.6 hours. However, in the elderly, the half life ranged from 17.4 to 25.9 hours."
        ),
    },
    "Bupropion": {
        "brand_names": ["Wellbutrin","Wellbutrin XL","Wellbutrin SR","Zyban","Forfivo"],
        "categories": ["Antidepressants"],
        "drug_classes": ["NDRI"],
        "specialties": ["Psychiatry", "Smoking Cessation", "Weight loss"],
        "class": "Norepinephrine Dopamine Reuptake Inhibitor (NDRI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Seasonal Depression",
            "Smoking cessation"
        ],
        "off_label_uses": [
            "Attention-Deficit/Hyperactivity disorder (ADHD)",
            "Weight management"
        ],
        "side_effects": [
            "Seizures",
            "Weight loss",
            "Hypersexuality",
            "Insomnia"
        ],
        "info": [
            "Bupropion is a norepinephrine dopamine reuptake inhibitor (NDRI). It was previously known as "
            "amfebtamone before being renamed. It is used as both a first line medication for treatment of depression "
            "as well as an adjunct to a serotogenic agent such as an SSRI or SNRI. Unlike most antidepressants, "
            "bupropion has a low incidence of sexual side effects, and is even linked to weight loss. It is also more "
            "activating, as opposed to many sedating antidepressants. Making it a great choice for people experiencing "
            "fatigue due to their depression. Bupropion is known the lower the seizure threshold, and therefore contradicted "
            "in patients with preexisting seizure disorders such as epilepsy. The instant release formulation has a greater "
            "risk of seizures as opposed to the extended or sustained release formulations. "


        ],
        "interactions": [
            "Bromopride",
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "metabolism": [
            "CYP2B6",
            "CYP2C19"

        ],
        "half_life": (
            "The half life of bupropion is highly variable. Anywhere from 12 to 30 hours. "
        ),
    },
    "Trazodone": {
        "brand_names": ["Desyrel","Oleptro"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Atypical Antidepressant","SARI"],
        "class": "Serotonin Antagonist and Reuptake Inhibitor (SARI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"
            "Insomnia",
        ],
        "off_label_uses":[
            "Anxiety",
            "Generalized Anxiety Disorder"
        ],
        "side_effects": [
            "Prolonged erections",
            "Headache",
            "Orthostatic hypotension",
            "QT prolongation"
        ],
        "info": [
            "Trazodone is an atypical antidepressant (sometimes classified as a serotonin antagonist and reuptake inhibitor "
            "used primarily for both depression and insomnia. It is often combined with an SSRI, to augment the antidepressant and anxiolytic "
            "benefits while I also reducing certain side effects. While Trazodone is not an SSRI, it does share some properties with SSRIs such as "
            "discontinuation syndrome upon suddenly stopping the drug. It is structurally related to SNDRI/SARI drug nefazodone, as it is a phenylpiperazine "
            "compound. "
            

        ],
        "metabolism": [
            "CYP3A4",
            "CYP2D6",
            "CYP1A2"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Dronedarone",
            "Ensitrelvir",
            "Fluconazole",
            "Isocarboxazid",
            "Ketoconazole",
            "Levoketoconazole",
            "Linezolid",
            "Mesoridazine",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Posaconazole",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Sparfloxacin",
            "Terefenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"

        ],

        "half_life": (
            "Trazodone's half life is around 4 to 14 hours, whereas extended release formulations last 9 to 13 hours. "
        ),
    },
    "Mirtazapine": {
        "brand_names": ["Remeron"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tetracyclic Antidepressants",
        "drug_classes": ["TeCA"],
        "conditions": [
            "Depression",
            "Major Depressive Disorder"
        ],
        "off_label_uses": [
            "Generalized Anxiety Disorder (GAD)",
            "Social Anxiety Disorder",
            "Obsessive-Compulsive Disorder (OCD)",
            "Panic Disorder",
            "Post-Traumatic Stress Disorder",
            "Low Appetite/Underweight",
            "Insomnia",
            "Nausea and Vomiting",
            "Headaches and Migraines",
            "Itching"
        ],
        "side_effects": [
            "Weight Gain",
            "Sleepiness",
            "Dry mouth",
            "Increased appetite",
            "Mania",
            "Hypomania"
        ],
        "metabolism": [
            "CYP2D6",
            "CYP1A2",
            "CYP3A4",
            "CYP3A5"
        ],
        "half_life": (
            ""
        ),
        "info": (
            "Mirtazapine is a tetracyclic antidepressant. It is primarily used for the treatment of Major Depressive disorder. "
            "It has a faster onset of action compared to SSRI medications. Mirtazapine has a high affinity for histamine receptors. "
            "Mirtazapine is known to cause discontinuation syndrome if stopped abruptly. "
            "The combination of mirtazapine and venlafaxine is known as 'california rocket fuel' due to their synergy and efficacy for treatment "
            "resistant depression. "
        )
    },
    "Amitriptyline": {
        "brand_names": ["Elvail"],
        "categories": ["Antidepressants"],
        "drug_classes": ["TCA"],
        "specialties": ["Psychiatry","Neurology","Gastroenterology","Rheumatology"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Neuropathic pain",
            "Migraines",
            "Chronic Tension Headache",
            "Nocturnal enuresis",
            "Fibromyalgia"
        ],
        "off_label_uses": [
            "Irritable Bowel Syndome Diarrhea Predominant (IBS-D)"
            "IBS-D",
            "IIBS"
        ],
        "side_effects": [
            "Dry mouth",
            "Dizziness",
            "Weight gain",
            "Abnormal heart rhythyms",
            "Glaucoma",
            "Increased appetite",
            "Tremor",
            "Constipation",
            "Sexual side effects"
        ],
        "info": [
            "While Amitriptyline is an antidepressant and classified as such, it is rarely used for depression "
            "due to its side effect profile and other drugs being more favorable. It is usually used after other "
            "treatments fail. It is considered very effective for diabetic neuropathy, even being compared to gabapentin "
            "and pregabalin. Low doses have also been shown to improve sleep disturbances, pain and fatigue associated with "
            "fibromyalgia. It is occassionally used for the treatment of diarrhea predominant irritable bowel syndrome (IBS-D). "

        ],
        "metabolism": [
            "CYP2D6",
            "CYP2C19"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Clorgyline",
            "Dronedarone",
            "Furazolidone",
            "Grepafloxacin",
            "Iproniazid",
            "Isocarboxazid",
            "Levoketoconazole",
            "Levomethadyl",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Nialamide",
            "Pargyline",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Toloxatone",
            "Tranylcypromine",
            "Ziprasidone"
        ],
        "half_life": (
            "Amitriptyline's half life is about 21 hours"
        ),
    },
    "Vortioxetine": {
        "brand_names": ["Trintellix", "Brintellix"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SMS","Atypical Antidepressant"],
        "class": "Serotonin Modulator and Stimulant (SMS)",

        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "off_label_uses": [
 
        ],
        "side_effects": [
            "Nausea",
            "Dry mouth",
            "Diarrhea",
            "Constipation",
            "Vomiting",
            "Sexual side effects"
        ],
        "info": [
            "Vortioxetine is a serotonin modulator and stimulator. The mechanism of action "
            "is not fully understood, it is believed to increase serotonin levels, possibly by interacting with certain serotonin receptors."
            "Like many antidepressants, it is contradicted in those taking monoamine oxidase inhibitors. "
            "Vortioxetine may cause less emotional bluting than other antidepressants."

        ],
        "interactions": [

            "Linezolid",
            "Methylene blue",
            "Isocarboxazid",
            "Ozanimod",
            "Rasagiline",
            "Phenelzine",
            "Procarbazine",
            "Safinamide",
            "Selegiline",
            "Mavorixafor",
            "Metoclopramide",
            "Tranylcypromise"


        ],
        "metabolism": [
            "CYP2D6"

        ],
        "half_life": (
            "Vortioxetine has a half life of 66 hours."
        ),
    },
    "Vilazodone": {
        "brand_names": ["Viibryd"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SPARI","Atypical Antidepressant"],
        "class": "Serotonin Partial Agonist and Reuptake Inhibitor (SPARI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",

        ],
        "off_label_uses": [
            "Generalized Anxiety Disorder",
            "Anxiety"
        ],
        "side_effects": [
            "Nausea",
            "Diarrhea",
            "Trouble Sleeping",
            "Acute pancreatitis",
            "Sleep paralysis",
            "Sleep disturbances",
            "Sexual side effects"

        ],
        "info": [
            "Vilazodone is a serotonin modulator and partial agonist. According to multiple studies, "
            "Vilazodone did not meaningfully out perform a placebo in at least 5 studies. In successful "
            "trials, Vilazodone showed a 13 percent greater response than placebo. The FDA admitted in 2011 "
            "that it was unclear if it had any advantages compared to other antidepressant drugs. "

        ],
        "interactions": [
            "Ensitrelvir",
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "metabolism": [
            "CYP3A4",
            "CYP2C19",
            "CYP2D6"

        ],
        "half_life": (
            "Vilazodone has a half life of 25 hours."
        ),
    },
    "Nefazodone": {
        "brand_names": ["Serzone"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SNDRI","Atypical Antidepressant"],
        "class": "Serotonin-Norepinephrine-Dopamine Reuptake Inhibitor (SNDRI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Aggressive Behavior",
            "Anxiety",
            "Generalized Anxiety Disorder",
            "Panic Disorder"

        ],
        "info": [
            "Nefazodone is considered an atypical antidepressant, as it has features of different antidepressant "
            "classes. Some considering it a SARI drug while others consider it an SNDRI. While Nefazodone is not a new drug, "
            "in 2004 it was discontinued in most countries due to liver toxicity. As of 2026, it is available as a generic "
            "drug in the United States. It is a phenylpiperazine compound and is related to the antidepressant Trazodone."

        ],
        "off_label_uses": [
        ],
        "side_effects": [
            "Dry mouth",
            "sleepiness",
            "Nausea",
            "Dizziness",
            "Liver toxicity",
            "orthrostatic hypotension",
            "Jaundice"
        ],
        "interactions": [
            "terfenadine",
            "alprazolam",
            "colchicine",
            "Conivaptan",
            "Dihydroergotamine",
            "Dronedarone",
            "Eplerenone"
            "Eletriptan",
            "astemizole",
            "cisapride",
            "pimozide",
            "carbamazepine",
            "triazolam"
        ],
        "metabolism": [
            "CYP3A4"

        ],
        "half_life": (
            ""
        ),
    },
    "Levomilnacipran": {
        "brand_names": ["Fetzima"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SNRI"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
        "conditions": [
            "Major Depressive Disorder",

        ],
        "info": [
            "Levomilnacipran is an SNRI drug, it is the levorotatory enantiomer of "
            "milnacipran, another SNRI drug. It has a significantly higher potency for inhibiting "
            "norepinephrine reuptake compared to serotonin reuptake. "

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Nausea and vomiting",
            "Constipation",
            "Increased sweating",
            "Tachycardia and palpitations"
        ],
        "interactions": [
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "metabolism": [
            "CYP3A4"

        ],
        "half_life": (
            "About 12 hours"
        ),
    },
    "Milnacipran": {
        "brand_names": ["Ixel","Savella","Milnaneurax"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SNRI"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
        "conditions": [
            "Fibromyalgia",
            "Depression",
            "Major Depressive Disorder"

        ],
        "off_label_uses": [
            "Social Anxiety Disorder"
        ],
        "info": [
            "Milnacipran is an SNRI antidepressant. Unlike most SNRIs, it is only approved in the USA for the treatment "
            "of fibromyalgia. It can be prescribed off label for depression or other neuropathic pain. In France, it is approved "
            "for treatment of depression, but not fibromyalgia. "

        ],
        "interactions": [
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "metabolism": [
            "CYP3A4"
        ],
        "side_effects": [
            "Blurred Vision",
            "Body aches",
            "Fast heartbeat"
            "Cough",
            "Chills",
            "Fever",
            "Increased sweating",
            "Nasal congestion",
            "Fatigue"
        ],
        "half_life": (
            "About 8 hours."
        ),
    },
    "Dextromethorphan-bupropion": {
        "brand_names": ["Auvelity"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SNDRI"],
        "class": "Serotonin-Norepinephrine-Dopamine Reuptake Inhibitor (SNDRI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder (MDD)",
            "Agitation associated with Alzheimer's disease"

        ],
        "info": [
            "Dextromethorphan-bupropion is an antidepressant comprised of the cough suppressant dextromethorphan and "
            "NDRI antidepressant, bupropion. These two drugs together perform better than either drug as monotherapy for depression. "
            "It is known to lower the seizure threshold, and is therefore contradicted in those with seizure disorders, as well as "
            "those with anorexia or bulimia. It is also important to not abruptly discontinue any CNS depressants such as alcohol, "
            "benzodiazepines, or barbituates, as these can also significantly lower the seizure threshold. Dextromethorphan acts as an NMDA receptor antagonist "
            "and a serotonin-norepinephrine reuptake inhibiitor. Unlike many antidepressants, it is not associated with sexual side effects or weight gain. "

        ],
        "off_label_uses": [
            "Smoking withdrawal",
            ""
        ],
        "metabolism": [
            "CYP2D6",
        ],
        "interactions": [
            "Bromopride",
            "Clorgyline",
            "Furazolidone",
            "Iproniazid",
            "Isocarboxazid",
            "Linezolid",
            "Mavorixafor",
            "Methylene Blue",
            "Moclobemide",
            "Nialamide",
            "Ozanimod",
            "Pargyline",
            "Phenelzine",
            "Pimozide",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Toloxatone",
            "Tranylcypromine"

        ],
        "side_effects": [
            "Anxiety",
            "Side pain",
            "Bladder pain",
            "Seizures"
        ],
        "half_life": (
            "About 22 hours"
        ),
    },
    "Toludesvenlafaxine": {
        "brand_names": ["Ruoxinlin"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["SNDRI"],
        "class": "Serotonin-Norepinephrine-Dopamine Reuptake Inhibitors (SNDRI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "info":[
            "Toludesvenlafaxine is an SNDRI drug approved for the treatment of major depression in China. It is under development "
            "for use in other countries such as the United States. It is a prodrug to the SNRI drug desvenlafaxine (Pristiq). However, "
            "unlike desvenlfaxine, Toludesvenlaxine also inhibits dopamine reuptake. Overall it seems to have a more balanced reuptake of "
            "serotonin, norepinephrine and dopamine compared to desvenlafaxine. "
        ],
        "off_label_uses": [
            "Generalized Anxiety Disorder",
            "Anxiety"
        ],
        "side_effects": [
            "",
            "",
        ],
        "half_life": (
            ""
        ),
    },
    "Reboxetine": {
        "brand_names": ["Edronax"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["NRI"],
        "class": "Norepinephrine Reuptake Inhibitors (NRI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder (MDD)",
            ""

        ],
        "info": [
            "Reboxetine is an NRI antidepressant approved for depression. While it is used in many countries, "
            "it is not approved for us in the United States for any condition. Some studies have found Reboxetine "
            "to be no more effective than a placebo for adults with unipolar major depression. Some sources have even "
            "stated that reboxetine is a harmful agent that shouldn't be used."

        ],
        "interactions": [
            "Linezolid",
            "Methylene Blue",
            "ketocanzole",
            "Azithromycin",
            "Itraconazole",
            "Papaverine",
            "Voriconazole",
            "Bosentan"


        ],
        "off_label_uses": [
            "Panic Disorder",
            "Attention Deficit/Hyperactivity Disorder (ADHD)",
            "ADHD"
        ],
        "side_effects": [
            "Insomnia",
            "Dizziness",
            "Dry mouth",
            "Nausea",
            "increased sweating",
            "Headache"
        ],
        "metabolism": [
            "CYP3A4"
            "CYP2D6"
        ],
        "half_life": (
            "Reboxetine has a half life of 13 hours"
        ),
    },
    "Teniloxazine": {
        "brand_names": ["Lucelan","Metatone"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["NRI"],
        "class": "Norepinephrine Reuptake Inhibitor (NRI)",
        "info": [
            "Teniloxazine is a Japanese norepinephrine reuptake inhibitor (NRI). "
            "It has mild inhibition of serotonin and dopamine reuptake, and also "
            "acts as a 5-HT2A receptor antagonist. It has antidepressant properties "
            "as well as antihypoxic and anti-amnestic properties, without strong "
            "anticholinergic, sedative or cardiovascular side effects. It was developed as "
            "an antidepressant, but is presently used for cerebrovascular insufficiency. "
        ],
        "conditions": [
            "Cerebrovascular Insufficiency",
            "Depression",
            "Major Depressive Disorder (MDD)"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "half_life": (
            ""
        ),
    },
    "Viloxazine": {
        "brand_names": ["Qelbree","Vivalan"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["NRI"],
        "class": "Norepinephrine Reuptake Inhibitors (NRI)",
        "info": [
            "Viloxazine was originally developed as an antidepressant, and "
            "was marketed as such for almost 30 years. Presently (as of 2026), it is "
            "used for the treatment of Attention-Deficit/Hyperactivity Disorder (ADHD). "
            "It is a Norepinephrine Reuptake Inhibitor (NRI). It has not been shown to be as effective as  "
            "stimulant drugs such as methylphenidate. "
        ],
        "conditions": [
            "Attention-Deficit/Hyperactivity Disorder (ADHD)",
            "ADHD",
            "Depression",
            "Major Depressive Disorder"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Insomnia",
            "Headache",
            "Drowsiness",
            "Sleepiness"
        ],
        "metabolism":[
            "CYP34A"   
        ],
        "interactions": [
            "Alosetron",
            "Duloxetine",
            "Fezolinetant",
            "Isocarboxazid",
            "Melatonin",
            "Methylene Blue",
            "Mexiletine",
            "Ozanimod"
            "Phenelzine",
            "Pomalidomide",
            "Procarbazine",
            "Ramelteon",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tacrine",
            "Tasimelteon",
            "Theophylline",
            "Tizanidine",
            "Tranylcypromine",
            "Warfarin"
        ],
        "half_life": (
            "Viloxazine has a half life of about 2 to 7 hours."
        ),
    },
    "Atomoxetine": {
        "brand_names": ["Strattera"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["NRI"],
        "class": "Norepinephrine Reuptake Inhibitor (NRI)",
        "conditions": [
            "Attention-Deficit/Hyperactivity Disorder (ADHD)",
            "ADHD"

        ],
        "info": [
            "Atomoxetine is an NRI drug (sometimes called an SNRI: Selective Norepinephrine Reuptake Inhibitor. "
            "It has been found to help various symptoms of ADHD, such as focus, executive dysfunction, working memory "
            "It is considered to be as effective for ADHD as methylphenidate. It can be used with or without a stimulant "
            "drug. Due to low abuse potential, it is ideal for patients with ADHD who have a co-occuring substance abuse disorder. "

        ],
        "off_label_uses": [
            "Generalized Anxiety Disorder (GAD)",
            "Anxiety",
            "Cognitive Disengagement Syndrome",
            "Narcolepsy",
            "Excessive sleepiness",
            "Traumatic Brain Injury",
            "Noctural Enuresis"
        ],
        "interactions": [
            "Isocarboxazid",
            "Linezolid",
            "Mavorixafor",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Procabazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "side_effects": [
            "Sexual side effects",
            "Discouragement",
            "Dizziness",
            "Feeling sad or empty",
            "Irritability",
            "Lack of appetite",
            "Loss of interest or pleasure",
            "Sleepiness",
            "Trouble concentrating",
            "Trouble sleeping"
        ],
        "metabolism":[
            "CYP2D6"
        ],
        "half_life": (
            "Atomoxetine has a half life of about 5 hours"
        ),
    },
    "Amitriptylinoxide": {
        "brand_names": ["Amioxid","Ambivalon","Equilibrin"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [
            "Amitriptylinoxide is both an analogue and metabolite of amitriptyline. "
            "It has similar effects and efficacy as an antidepressant drug. However, it has "
            "a faster onset of action and fewer adverse effects as compared to amitriptyline. "
            "It is also considered a prodrug to amitriptyline and acts similarly in receptor "
            "binding assays. "

        ],
        "metabolism": [
            "CYP2C19",
            "CYP2D6"

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
    "Amoxapine": {
        "brand_names": ["Asendin"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressant (TCA)",
        "drug_classes": ["TCA"],
        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "info": [
            "Amoxapine is a tricyclic antidepressant that is an N-demethylated metabolite of "
            "the antipsychotic drug Loxapine. It is believed to have a faster onset of action "
            "compared to other antidepressants. Some studies suggest improvements could be seen as "
            "early as four to seven days. It has similar properties to atypical antipsychotics. "

        ],
        "interactions": [
            "Bromopride",
            "Clorgyline",
            "Isocarboxazid",
            "Levomethadyl",
            "Linezolid",
            "Methylene Blue",
            "Metoclopramide",
            "Moclobemide",
            "Phenelzine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "off_label_uses": [
            "Schizophrenia",
            ""
        ],
        "side_effects": [
            "Dry mouth",
            "Increased appetite",
            "Constipation",
            "Sedation"
        ],
        "metabolism": [
            "CYP2D6"
        ],

        "half_life": (
            "About 8 to 10 hours"
        ),
    },
    "Clomipramine": {
        "brand_names": ["Anafril"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Obsessive-Compulsive Disorder",
            "OCD"
            "Depression",
            "Major Depressive Disorder"

        ],
        "info": [
            "Clomipramine is a tricyclic antidepressant that is primarily used for Obsessive-Compulsive Disorder (OCD)"
            "It is approved for Major Depressive Disorder in the UK, Japan and Australia. Some studies suggest that Clomipramine "
            "may be more effective for severe depression than other antidepressant drugs. It is a very powerful Serotonin Reuptake "
            "Inhibitor (SRI). It was shown to have a higher affinity for serotonin than fellow tricyclic drugs imapramine, amitriptyline and "
            "dosulepin (dothiepin). It is the most potent serotonin reuptake inhibitor of both the tricyclic class and SSRI class, including "
            "Paroxetine which is widely considered the most powerful SSRI. "

        ],
        "off_label_uses": [
            "Hyperacusis",
            "Panic Disorder",
            "Trichotillomania",
            "Body Dysmorphic Disorder",
            "Chronic pain",
            "Narcolepsy",
            "Premature ejaculation"
        ],
        "metabolism": [
            "CYP2D6"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Dronedarone",
            "Grepafloxacin",
            "Isocarboxazid",
            "Levoketoconazole",
            "Linezolid",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"

        ],
        "side_effects": [
            "Bladder Pain",
            "Bloody or Cloudy Urine",
            "Body aches",
            "Pins and needles feeling",
            "Painful urination",
            "Sneezing",
            "Poor Concentration",
            "Tiredness",
            "Headache",
            "Sexual side effects",
            "Increased sweating",
            "Weakness"
        ],
        "half_life": (
            "Between 19 to 37 hours (averaging to about 32 hours)"
        ),
    },
    "Desipramine": {
        "brand_names": ["Norpramine","Petrofrane"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",

        ],
        "info": [
            "Desipramine is a tricyclic antudepressant that acts as a selective norepinephrine "
            "reuptake inhibitor. It does have weak serotonin reuptake inhibitor properties, as well as alpha1 blocking "
            "and antihistamine and antichloirgenic effects. Since the release of SSRIs, it has no "
            "longer been considered a first line treatment for depression. Some studies have shown that "
            "Desipramine may be helpful for the treatment of ADHD, though these benefits appear to be short term. "
            "It is also a major metabolite of Imapramine and Lofepramine, other tricyclic antidepressant "
            "drugs. "

        ],
        "off_label_uses": [
            "Attention Deficit/Hyperactivity Disorder",
            "ADHD",
            "Functional dyspepsia"
        ],
        "side_effects": [
            "Dry mouth",
            "Constipation",
            "Blurry Vision",
            "Dizziness",
            "Nausea",
            "Drowsiness"
        ],
        "Interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Dronedarone",
            "Furazolidone",
            "Grepafloxacin",
            "Iproniazid",
            "Isocarboxazid",
            "Levoketocanazole",
            "Levomethadyl",
            "Linezolid",
            "Mavixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Moclobemide",
            "Pargyline",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"

        ],
        "metabolism": [
            "CYP2D6"
        ],
        "half_life": (
            "About 12 to 30 hours"
        ),
    },
    "Dibenzepin": {
        "brand_names": ["Noveril","Victoril"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "info": [
            "Dibenzepin is a tricyclic antidepressant used throughout Europe. It is often "
            "compared to other tricyclics as far as efficacy, but a lower propensity for side effects. "
            "It is mostly used for major depressive disorder. It mostly inhibits norepinephrine and is often "
            "called a selective norepinephrine reuptake inhibitor. Unlike other tricyclic antidepressants, it is no "
            "antiagregenic effects nor antiserotogenic or antidopaminergic effects. It is shown to have similar efficacy "
            "to tricyclic antidepressant drug imapramine. "

        ],
        "metabolism": [
            "CYP450",
            "CYP2D6",
            "CYP3A4",
            "CYP1A2",
            "CYP2C19"

        ],

        "off_label_uses": [
            "Neuropathic pain",
            ""
        ],
        "interactions": [
            "Brimonidine",
            "Entacapone",
            "Artemether",
            "Lumefantrine"

        ],
        "side_effects": [
            "Dry mouth",
            "Blurred vision",
            "Constipation",
            "Urinary retention",
            "confusion",
            "Weight gain"
        ],
        "half_life": (
            "About 5 hourss"
        ),
    },
    "Dimetacrine": {
        "brand_names": ["Istonil","Linostil","Istonyl"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "info": [
            "Dimetacrine is a tricyclic antidepressant once used in Japan, but currently still used in Europe. "
            "It was believed to be similar to tricyclic antidepressant drug, Imapramine. However, a double blind clinical "
            "trial showed that Dimetacrine was not as efficacious as Imapramine. It has been shown to cause more weight loss "
            "and abnormal liver tests than Imapramine. "

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Dry mouth",
            "Constipation",
            "Blurred vision",
            "Dizziness and drowsiness",
            "Headache",
            "Nausea",
            "Weight gain",
            "Abnormal liver tests"
        ],
        "metabolism": [
            "CYP2C19",
            "CYP2D6",
            "CYP3A4"
        ],
        "half_life": (
            ""
        ),
    
    },
    "Dosulepin": {
        "brand_names": ["Prothiaden"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Psychogenic facial pain"

        ],
        "info": [
            "Dosulepin (also called dothiepin) is a tricyclic antidepressant that was frequently used in the UK. "
            "It is no longer widely used to high toxicity in overdose, while also not having many benefits that other tricyclic "
            "antidepressants didn't have. It acts as an SNRI (serotonin norepinephrine reuptake inhibitor) and also has antihistamine, antiadregenic, "
            "antiserotonergic, anticholinergic, and sodium channel blocking effects. "
        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Drowsiness",
            "Extrapyramidal symptoms",
            "Tremor",
            "Disorientation",
            "Dizziness",
            "Sweating",
            "Dry mouth",
            "Urinary retention",
            "Hypotension",
            "Arrthymias",
            "Nausea",
            "Vomiting"
        ],
        "metabolism": [
            "CYP219",
            "CYP2D6"
        ],
        "interactions": [

        ],
        "half_life": (
            "About 14.5 to 24 hours"
        ),
    },
        "Doxepin": {
        "brand_names": ["Adapin","Sinequan"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Insomnia"

        ],
        "off_label_uses": [
            "Anxiety",
            "Chronic Uticaria",
            "Generalized Anxiety Disorder",
            "Headache",
            "Neuropathic pain"
        ],
        "side_effects": [
            "Fatigue",
            "Dry mouth",
            "Hypotension",
            "Weight gain",
            "Tinnitus"
        ],
        "info": [
            "Doxepin is a tricyclic antidepressant drug that is available as an oral pill and as a cream. "
            "The cream is to treat atopic dermatitis or lichen simplex chronicus, whereas the pill treats mental "
            "disorders such as depression, anxiety and insomnia. Doses used for insomnia are often far lower than "
            "doses used for depression. Doses below 25mg serve as a pure antihistmine whereas doses from 25mg to 300mg are "
            "defined as antidepressant dosages. It is more activating at high doses as oppsosed to low doses. It is a highly potent "
            "antihistamine with it being its strongest activity, some even considering it the most powerful H1 antagonist available. At "
            "least among the tricyclcic antidepressants. "
        ],
        "metabolism": [
            "CYP2D6",
            "CYP2C19",
            "CYP1A2",
            "CYP2C9",
            "CYP3A4"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Dronedarone",
            "Isocarboxazid",
            "Levoketoconazole",
            "Levomethadyl",
            "Linezolid",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Moclobemide",
            "Ozanidmod",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"

        ],
        "half_life": (
            "Around 17 hours"
        ),
    },
        "Imapramine": {
        "brand_names": ["Tonafril"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Anxiety",
            "Panic Disorder"

        ],
        "off_label_uses": [
            "Post-Traumatic Stress Disorder",
            "PTSD"
        ],
        "side_effects": [
            "Dry mouth",
            "Drowsiness",
            "Dizziness",
            "Rapid heart rate",
            "Urinary retention"
        ],
        "info": [
            "Imapramine is a tricyclic antidepressant which has efficacy similar to MAOI drug Phenelzine. It was "
            "used quite frequently prior to the newer SSRI drugs, which feature less toxicity in overdose and less side effects. "
            "Imapramine remains a very important drug despite this, and is used for many mental health conditions across "
            "a broad age range. "

        ],
        "metabolism": [
            "CYP1A2",
            "CYP2C19",
            "CYP2D6"
        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Furazolidone",
            "Grepafloxacin",
            "Iproniazid",
            "Isocarboxazid",
            "Levoketoconazole",
            "Levomethadyl",
            "Linezolid",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Moclobemide",
            "Pargyline",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"
        ],
        "half_life": (
            "Imapramine has a half life of 20 hours."
        ),
    },
        "Lofepramine": {
        "brand_names": ["Lomont","Gamanil","Tymelyt"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressants",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "off_label_uses": [
            "Fatigue",
            ""
        ],
        "side_effects": [
            "Agitation",
            "Anxiety",
            "Pins and needles feeling",
            "Constipation",
            "Diarrhea",
            "Vomiting"
        ],
        "info": [
            "Lofepramine is a tricyclic antidepressant that is considered to be a thid generation tricyclic antidepressant. "
            "The reasoning is due to it being relatively safe in overdose and having less side effects, It is not available in the United "
            "States, Canada, Australia or New Zealand. But it is available in Ireland, Japan, South Africa and the UK, as well as some "
            "other countries. It is considered to be a prodrug of desipramine. "

        ],
        "metabolism": [
            "CYP2D6",
            "CYP2C19"
            
        ],
        "interactions": [
            "Altretamine",
            "Apraclonidine",
            "Brimonidine",
            "Phenelzine",
            "Tranylcypromine",
            "Isocarboxazid",
            "Moclobemide",
            "Selegiline",
            "Rasagiline"
            

        ],
        "half_life": (
            "5 hours as Lofepramine, 12-24 hours as active metabolites. "
        ),
    },
        "Melitracen": {
        "brand_names": ["Dixeran","Melixeran","Trausabun"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Anxiety",
            "Generalized Anxiety Disorder"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Dry mouth",
            "Drowsiness",
            "Constipation",
            "Dizziness",
            "Weight gain",
            "Increased appetite"

        ],
        "info": [
            "Melitracen is a tricyclic antidepressant that is used for both depression and anxiety. "
            "It is available as both a stand alone medication, and as a combination with flupentixol and Melitracen "
            "(brand name: Deanxit). There is not much information known about Melitracen as far as its pharmacology, "
            "but it is likely similar to the tricyclic drugs imipramine and amitriptyline. However it is shown to have "
            "improved tolerability."

        ],
        "metabolism": [
            "CYP2C19",
            "CYP3A4",
            "CYP2D6"

        ],
        "interactions": [
            "Vemurafenib"

        ],
        "half_life": (
            "Approximately 19 hours."
        ),
    },
        "Nitroxazepine": {
        "brand_names": ["Sintamil"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Nocturnal Enuresis"

        ],
        "off_label_uses": [
            "Anxiety",
            "Generalized anxiety disorder",
            "OCD",
            "Obsessive-Compulsive Disorder",
            "Chronic Neuropathic pain"
        ],
        "side_effects": [
            "Dry Mouth",
            "Constipation",
            "Weight gain",
            "Blurred Vision",
            "Dizziness",
            "Increased heart rate"
        ],
        "info": [
            "Nitroxazepine is a tricyclic antidepressant formulated in India. In addition to depression, "
            "it also treats nocturnal enuresis. It acts as a serotonin norepinephrine reuptake inhibitor, exhibiting "
            "similar side effects to tricyclic antidepressant imapramine, while also having a lower rate of "
            "anticholinergic side effects."

        ],
        "metabolism": [
            "CYP2D6",
            "CYP3A4"

        ],
        "interactions": [
            "Fluoxetine",
            "Paroxetine"

        ],
        "half_life": (
            "Nitroxazepine has a half life of 8 to 15 hours"
        ),
    },
        "Nortriptyline": {
        "brand_names": ["Pamelor","Aventyl"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "Attention-Deficit/Hyperactivity Disorder (ADHD)",
            "Smoking cessation",
            "Neuropathic pain",
            "Anxiety"
        ],
        "side_effects": [
            "Dry mouth",
            "Constipation",
            "Blurry vision",
            "Sleepiness",
            "Low blood pressure with standing",
            "Weakness",
            "Seizures"
        ],
        "info": [
            "Nortriptyline is a tricyclic antidepressant that acts as a strong norepinephrine reuptake inhibitor, with moderate "
            "serotoning reuptake abilities. It also inhibits the activity of histamine and acetylcholine. It is an active metabolite "
            "of amitriptyline. It is thought to have sleep-improving effects due to its antagonism of H1 and 5-HT2A receptors. It has the "
            "highest affinity for the dopamine transporter among the tricyclic antidepressants."

        ],
        "metabolism": [
            "CYP2D6"
        ],
        "interactions": [
            "Bromopride",
            "Dronedarone",
            "Grepafloxacin",
            "Iproniazid",
            "Isocarboxazid",
            "Levomethadyl",
            "Linezolid",
            "Mavorixafor",
            "Methylene Blue",
            "Metoclopramide",
            "Moclobemide",
            "Pargyline",
            "Phenelzine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"
            

        ],
        "half_life": (
            "Nortriptyline has a mean half life of 30 hours, though half lives as short as 18 and as long as 44 "
            "have been reported. "
        ),
    },
        "Noxiptiline": {
        "brand_names": ["Agedal","Elronon","Nogedal"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressant (TCA)",
        "drug_classes": ["TCA"],
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Anxiety",
            "Generalized Anxiety Disorder",
            "Chronic pain"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Dry mouth",
            "Constipation",
            "Urinary retention",
            "Dizziness",
            "Drowsiness",
            "Orthostatic hypotension",
            "Dizziness",
            "Fainting"
        ],
        "info": [
            "Noxiptiline (also called noxiptyline) is a tricyclic antidepressant used to treat depression. It is considered "
            "to be one of the most effective tricyclic antidepressants, even rivaling amitriptyline in clinical efficacy. It acts "
            "as a serotonin norepinephrine reuptake inhibitor. "

        ],
        "metabolism": [
            "CYP450"

        ],
        "interactions": [
            "MAOIs",
        ],
        "half_life": (
            ""
        ),
    },
        "Lisdexamfetamine": {
        "brand_names": ["Vyvanse","Elvanse"],
        "categories": ["Stimulant"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["CNS"],
        "class": "Central Nervous System Stimulant",
        "conditions": [
            "Attention Deficit/Hyperactivity Disorder",
            "ADHD",
            "Binge Eating Disorder"

        ],
        "off_label_uses": [
            "Narcolepsy",
            ""
        ],
        "side_effects": [
            "Constipation",
            "Decreased Appetite",
            "Headache",
            "Nausea",
            "Abdominal pain",
            "Vomiting",
            "Weight loss"
        ],
        "info": [
            "Lisdexamfetamine is a stimulant medication that treats ADHD and Binge Eating Disorder. It is "
            "an inactive prodrug that is converted in the body into dextroamphetamine, which is a pharmacologically "
            "active compound and is responsible for the drug's activity. It was developed with the intention "
            "of providing a long duration effect that is consistent throughout the day, while also lowering the abuse "
            "potential that other stimulants have. "

        ],
        "metabolism": [
            "Hydrolytic Enzymes (Peptidases)"

        ],
        "interactions": [
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Procarbazine",
            "Safinamide",
            "Rasagiline",
            "Selegiline",
            "Tranylcypromise"

        ],
        "half_life": (
            "The half life of lisdexamfetamine is only an hour, but after "
            "the body converts it into dextroamphetamine, it has a half life of about 10-12 hours"
        ),
    },
        "Pipofezine": {
        "brand_names": ["Azafen","Azaphen"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressant (TCA)",
        "drug_classes": ["TCA"],
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Nausea",
            "Vomiting",
            "Dry mouth",
            "Dizziness",
            "Headache",
            "Fatigue",
            "Sleepiness",
            "Fatigue"
        ],
        "info": [
            "Pipofezine is a tricyclic antidepressant approved in Russia for treatment of depression. "
            "While it was introduced in the late 1960s, it is still used today. It is a potent inhibitor of "
            "the reuptake of serotonin. It also has sedative effects which implies it has antihistamine activity. "

        ],
        "metabolism": [
            "CYP2D6",
            "CYP3A4",
            "CYP2C9",
            "CYP2C19"

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
        "Protriptyline": {
        "brand_names": ["Vivactil"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressant (TCA)",
        "drug_classes": ["TCA"],
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
            "Chronic migraine",
            "Anxiety",
            "Generalized Anxiety Disorder",

        ],
        "off_label_uses": [
            "Narcolepsy",
            "Panic Disorder",
            "Attention Deficit/Hyperactivity disorder",
            "ADHD",
            "OCD",
            "Obsessive Compulsive Disorder",
            "Cocaine Dependence",
            "Bipolar Depression",
            "Enuresis",
            "Bulimia nervosa"
        ],
        "side_effects": [
            "Dry mouth",
            "Constipation",
            "Urinary retention",
            "Increased heart rate",
            "sedation",
            "irritability",
            "Decreased coordination"
        ],
        "info": [
            "Protriptyline is a tricyclic antidepressant with energizing properties, which differs "
            "from the other TCAs which tend to be sedating. It is used to treat a myriad of mental disorders "
            "as well as chronic pain conditions or reoccuring headaches and migraines. If used in patients with schizophrenia "
            "or bipolar disorder, psychosis may worsen. It is known to have significant withdrawal symptoms if stopped "
            "suddenly. "

        ],
        "metabolism": [
            "CYP2D6"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Clorgyline",
            "Dronedarone",
            "Grepafloxacin",
            "Isocarboxazid",
            "Levoketoconazole",
            "Levomethadyl",
            "Linezolid",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Moclobemide",
            "Phenelzine",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Safinamide",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"

        ],
        "half_life": (
            "Portriptyline's half life is on average 74 hours"
        ),
    },
        "Trimipramine": {
        "brand_names": ["Surmontil"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TCA"],
        "class": "Tricyclic Antidepressant (TCA)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder",
        ],
        "off_label_uses": [
            "Delusional Depression",
            "Schizoaffective Disorder",
            "Schizophrenia",
            "Insomnia",
            "Anxiety",
            "Generalized Anxiety Disorder"
        ],
        "side_effects": [
            "Sedation",
            "Dry mouth",
            "Blurred vision",
            "Constipation",
            "Urinary retention",
            "Weight gain",
            "Rash",
            "Sexual side effects"
        ],
        "info": [
            "Trimipramine is a unique tricyclic antidepressant with sedative, anxiolytic and weak antipsychotic properties "
            "It is used to treat multiple mental illnesses, and is often described as a 'second generation' TCA due to its weak "
            "monoamine reuptake abilities. It does have anthistamine, antiserotonergic, antiadrenergic, antidopaminergic and anticholinergic properties "
            "similar other medications in its class. "
        ],
        "metabolism": [
            "CYP2C19"
        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Clorgyline",
            "Dronedarone",
            "Furazolidone",
            "Iproniazid",
            "Isocarboxazid",
            "Levoketoconazole",
            "Levomethadyl",
            "Linezolid",
            "Mavorixafor",
            "Mesoridazine",
            "Methylene Blue",
            "Metoclopramide",
            "Moclobemide",
            "Pargyline",
            "Phenelzine",
            "Pimozide",
            "Piperaquine",
            "Potassium Chloride",
            "Potassium Citrate",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Saquinavir",
            "Selegiline",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Tranylcypromine",
            "Ziprasidone"
        ],
        "half_life": (
            "Trimipramine has a half life of 23 to 24 hours"
        ),
    },
        "flupentixol": {
        "brand_names": ["Depixol","Fluanxol"],
        "categories": ["Antipsychotics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Typical Antipsychotic"],
        "class": "Typical Antipsychotic",
        "conditions": [
            "Schizophrenia"

        ],
        "off_label_uses": [
            "Depression",
            "Self harm"
        ],
        "side_effects": [
            "Extrapyramidal side effects",
            "Dry mouth",
            "Constipation",
            "Constipation",
            "Hypersalvation",
            "Nausea",
            "Insomnia",
            "Restlessness",
            "Headache", 
            "Myalgia",
            "Hyperprolactinemia"
        ],
        "info": [
            "Flupentixol is a typical (first generation) antipsychotic that is used as a long-acting "
            "injection given once every two to three weeks. It is used mainly for schizophrenic patients with "
            "poor medication compliance and frequent relapse of illnesses. Though it is also available as a tablet. In "
            "low doses, it can be used as an antidepressant and has evidence of showing a decrease in self harm. "
            "It is combined with the TCA drug Melitracen as the brand 'Deanxit'."
        ],
        "metabolism": [
            "CYP2D6"

        ],
        "interactions": [
            "Lithium",
            "Citalopram"

        ],
        "half_life": (
            "About 35 hours"
        ),
    },
        "tianeptine": {
        "brand_names": ["Stablon","Coaxil"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Atypical Tricyclic Antidepressant",
        "drug_classes": ["TCA","Atypical Antidepressant"],
        "conditions": [
            "Depression",
            "Major Depressive Disorder"

        ],
        "off_label_uses": [
            "Anxiety",
            "Asthma",
            "IBS",
            "Irritable Bowel Syndrome"
        ],
        "side_effects": [
            "Headache",
            "Dizziness",
            "Insomnia",
            "Nightmares",
            "Dry mouth",
            "Constipation",
            "Nausea",
            "Abdominal pain",
            "Euphoria",
            "Severe withdrawal symptoms",
        ],
        "info": [
            "Tianeptine is an atypical tricyclic antidepressant that acts as an atypical agonist of the mu-opioid receptor. "
            "It has both antidepressant and anxiolytic effects, it also modulates glutamate receptors. It is available in "
            "some European and Asian countries. In the United States, it is unregulated and sold under multiple names. It is considered "
            "a recreational drug, even earning itself the name 'gas station heroin'. As of July 2026, the Drug Enforcement Administration (DEA) "
            "announced its intention to make tianeptine a Schedule I controlled substance. Despite this, it has been proven to help combat severe "
            "depressive episodes, even being considered comparable to drugs like amitriptyline or fluoxetine, with even fewer side effects. Studies have "
            "shown tianeptine is useful in the treatment of asthma, ibs, panic disorder and even has anticonvulsant and analgesic properties. "
            "It is considered to have significantly fewer side effects than other tricyclic antidepressant drugs. "

        ],
        "metabolism": [
            "CYP450"
        ],
        "interactions": [
            "Alcohol",
            "Diazepam"

        ],
        "half_life": (
            "2.5 to 3 hours in young adults, and 4 to 9 hours in the elderly."
        ),
    },
        "Maptrotiline": {
        "brand_names": ["Ludiomil"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TeCA"],
        "class": "Tetracyclic Antidepressant (TeCA)",
        "conditions": [
            "Depression",
            "Major depressive disorder",
            "Depression associated agitation",
            "Depression associated anxiety"


        ],
        "off_label_uses": [
            "Panic disorder",
            "Neuropathic Pain",
            "Polyneuropathy",
            "Bipolar depression"
        ],
        "side_effects": [
            "Dizziness",
            "Drowsiness",
            "Somnolence",
            "Fatigue",
            "Dry Mouth",
            "Constipation",
            "Vertigo",
            "Increased appetite"
        ],
        "info": [
            "Maptrotiline is a tetracyclic antidepressant that is chemically similar to the tricyclic antidepressants Nortriptyline and Protriptyline. "
            "It tends to have more distinct anxiolytic effects and is more sedating than protriptyline. Maprotiline is found to have similar efficacy and "
            "tolerability to antidepressant drug moclobemide. It is used to treat all forms of depression and various severities. Some studies have shown that "
            "Maptrotiline may actyally have potent anti-profilerative effects against some cancers, specifically Burkitt lymphoma type cancers. "
        ],
        "metabolism": [
            "CYP2D6"
        ],
        "interactions": [
            "Bromopride",
            "Isocarboxazid",
            "Linezolid",
            "Mavorixafor",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "half_life": (
            "Maptrotiline has a half life between 27 to 58 hours. The average half life is 51 hours."
        ),
    },
        "Mianserin": {
        "brand_names": ["Tolvon"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TeCA"],
        "class": "Tetracyclic Antidepressant (TeCA)",
        "conditions": [
            "Depression",
            "Major depressive disorder",
            "Insomnia"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Constipation",
            "Dry mouth",
            "Drowsiness"
        ],
        "info": [
            "Mianserin is a tetracyclic antidepressant that is structurally related to mirtazapine. It has greater "
            "noradrenergic activity and less 5-HT3 receptor antagonism than mirtazapine. At high doses, it is used to treat "
            "major depressive disorder, at low doses it is used to treat insomnia. "

        ],
        "metabolism": [
            "CYP2D6",
            "CYP3A4",
            "CYP1A2"
        ],
        "interactions": [
            "Apraclonidine",
            "Brimonidine",
            "Sibutramine",
            "Artemether",
            "Lumefantrine"
        ],
        "half_life": (
            "The half life ranges from 21 to 61 hours. No average half life has been reported."
        ),
    },
       "setiptiline": {
        "brand_names": ["Tecipul"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["TeCA"],
        "class": "Tetracyclic Antidepressant (TeCA)",
        "conditions": [
            "Depression"

        ],
        "off_label_uses": [

        ],
        "side_effects": [
            "Drowsiness",
            "Sedation",
            "Dry mouth",
            "Weight gain",
            "Dizziness",
            "Sexual side effects",
            "Constipation",
            "Nausea"
        ],
        "info": [
            "Setiptiline is a Japanese tetracyclic antidepressant drug that is a close analogue of Mianserin and Mirtazapine. "
            "It acts as a norepinephrine reuptake inhibitor, alpha 2 adrenergic antagonist and serotoning receptor antagonist. It is "
            "also an H1 receptor inverse agonist/antihistamine. "

        ],
        "metabolism": [
            "CYP2D6",
            "CYP3A4",
            "CYP1A2"

        ],
        "interactions": [

        ],
        "half_life": (
            "Setiptiline has a half life between 11 to 20 hours."
        ),
    }, 
        "isocarboxazid": {
        "brand_names": ["Marplan"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["MAOI"],
        "class": "Irreversible Monoamine Oxidase Inhibitor (MAOI)",
        "conditions": [
            "Treatment resistant depression",
            "Atypical Depression",
            "Melancholic Depression",
            "Endogenous Depression",
            "Depression"

        ],
        "off_label_uses": [
            "Parkinson's disease",
            "Alzhemier's disease"
        ],
        "side_effects": [
            "insomnia",
            "Dry Mouth",
            "Urinary hesitancy",
            "Carbohydrate cravings "
        ],
        "info": [
            "Isocarboxazid (brand name: Marplan) is an irreversible monoamine oxidase inhibitor (MAOI) drug for the hydrazine "
            "class. It is used as an antidepressant for treatment resistant depression, and is rarely used due to its plethora of "
            "interactions, with both drugs and foods. It is prescribed less often than the other irreversible MAOI drugs (Phenelzine and Tranylcypromine). "
            "This is presumably due to issues of affordability and availability. There is no FDA approved "
            "generic equivalent. "
        ],
        "metabolism": [
            "CYP2D6"

        ],
        "interactions": [
            "Albuterol Sulfate",
            "Alfentanil",
            "Alprazolam",
            "Amineptine",
            "Amitriptyline",
            "Amitriptylinoxide",
            "Amobarbital",
            "Amoxapine",
            "Amphetamine",
            "Anileridine",
            "Apraclonidine",
            "Aprobarbital",
            "Arformoterol Tartrate",
            "Aripiprazole",
            "Armodafinil",
            "Asenapine",
            "Atomoxetine",
            "Baclofen",
            "Barbital",
            "Bemetizide",
            "Bendroflumethiazide",
            "Brimonidine",
            "Bromazepam",
            "Bupivacaine",
            "Buprenorphine",
            "Bupropion",
            "Buspirone",
            "Butalbital",
            "Butorphanol",
            "Calcium Oxyybate",
            "Cannabis",
            "Carbamazepine",
            "Carbidopa",
            "Carbinoxamine",
            "Carisoprodol",
            "Carphenazine",
            "Cetirizine",
            "Chloral Hydrate",
            "Chlordiazepoxide",
            "Chloroprocaine Hydrochloride",
            "Chlorpromazine",
            "Chlorthalidone",
            "Chlorzoxazone",
            "Citalopram",
            "Clobazam",
            "Clomipramine",
            "Clonazepam",
            "Clonidine",
            "Clopamide",
            "Clovoxamine",
            "Clozapine",
            "Cocaine",
            "Codeine",
            "Cyclobenzaprine",
            "Cyclopenthiazide",
            "Cyclothiazide",
            "Cyproheptadine",
            "Daridorexant",
            "Desflurane",
            "Desipramine",
            "Desvenlafaxine",
            "Deutetrabenazine",
            "Dexfenfluramine",
            "Dexmedetomidine",
            "Dexmethylphenidate",
            "Dextroamphetamine",
            "Dextromethorphan",
            "Diacetylmorphine",
            "Diazepam",
            "Diazoxide",
            "Dibenzepin",
            "Dichloralphenazone",
            "Diethylpropion",
            "Difenoxin",
            "Dihydrocodeine",
            "Dipenhydramine",
            "Diphenoxylate",
            "Dobutamine",
            "Dopamine",
            "Dothiepin",
            "Doxepin",
            "Doxylamine",
            "Droperidol",
            "Droxidopa",
            "Duloxetine",
            "Dyclonine Hydrochloride",
            "Enflurane",
            "Entacapone",
            "Ephedrine",
            "Epinephrine",
            "Escitalopram",
            "Esketamine",
            "Estazolam",
            "Eterobarb",
            "Ethchlorvynol",
            "Ethopropazine",
            "Ethylmorphine",
            "Femoxetine",
            "Fenfluramine",
            "Fentanyl",
            "Flibanserin",
            "Fluoxetine",
            "Fluphenazine",
            "Flurazepam",
            "Fluspirilene",
            "Fluticasone Propionate",
            "Fluvoxamine",
            "Formoterol Fumarate",
            "Foscarbidopa",
            "Foslevodopa",
            "Fospropofol",
            "Furazolidone",
            "Gabapentin",
            "Gepirone",
            "Guanadrel",
            "Guanethidine",
            "Halazepam",
            "Haloperidol",
            "Halothane",
            "Hexobarbital",
            "Hydrochlorthiazide",
            "Hydrocodone",
            "Hydroflumethiazide",
            "Hydromorphone",
            "Hydroxyamphetamine",
            "Hydroxytryptophan",
            "Hydroxyzine",
            "Imipramine",
            "Indapamide",
            "Isoflurane",
            "Isometheptene",
            "Isoproterenol",
            "Ketamine",
            "Ketazolam",
            "Ketobemidone",
            "Levalbuterol",
            "Levocetirizine",
            "Levodopa",
            "Levomethadyl",
            "Levomilnacipran",
            "Levorphanol",
            "Lidocaine",
            "Linezolid",
            "Lisdexamfetamine",
            "Lofepramine",
            "Lorazepam",
            "Loxapine",
            "Magnesium Oxybate",
            "Maprotiline",
            "Mazindol",
            "Meclizine",
            "Melitracen",
            "Melperone",
            "Meperidine",
            "Mephentermine",
            "Mephenobarbital",
            "Mepivacaine Hydrochloride",
            "Meprombamate",
            "Meptazinol",
            "Mesoridazine",
            "Metaraminol",
            "Methadone",
            "Methamphetamine",
            "Methdilazine",
            "Methocarbamol",
            "Methohexital",
            "Methotrimperazine",
            "Methoxamine",
            "Methoxyflurane",
            "Methyclothiazide",
            "Methyldopa",
            "Methylene Blue",
            "Methylphenidate",
            "Metolazone",
            "Midazolam",
            "Midodrine",
            "Milnacipran",
            "Mirtazapine",
            "Modafinil",
            "Molindone",
            "Moricizine",
            "Morphine",
            "Nalbuphine",
            "Nefazodone",
            "Nefopam",
            "Nicomorphine",
            "Nitrazepam",
            "Nitrous Oxide",
            "Norepinephrine",
            "Notriptyline",
            "Olanzapine",
            "Opicapone",
            "Opipramol",
            "Opium",
            "Orphenadrine",
            "Oxazepam",
            "Oxycodone",
            "Oxymetazoline Hydrochloride",
            "Oxymorphone",
            "Ozanimod",
            "Papaveretum",
            "Paregoric",
            "Pargyline",
            "Paroxetine",
            "Pentazocrine",
            "Phentobarbital",
            "Perampanel",
            "Perazine",
            "Periciazine",
            "Perphenazine",
            "Perphanzine"
            "Phendimetrazine",
            "Phenelzine"
            "Phenmatrazine",
            "Phenobarbital",
            "Phentermine",
            "Phenylalanine",
            "Phenylephrine",
            "Phenylpropanomine",
            "Pimozide",
            "Piperacetazine",
            "Piritramide",
            "Polythiazide",
            "Potassium Oxybate",
            "Prazepam",
            "Prilocaine HCl",
            "Primidone",
            "Procarbazine",
            "Prochlorperazine",
            "Promazine",
            "Promethazine",
            "Proparacaine HCl",
            "Propofol",
            "Protriptyline",
            "Psuedoephedrine",
            "Quazepam",
            "Quetiapine",
            "Quinethazone",
            "Ramelteon",
            "Rasgiline",
            "Remifentanil",
            "Remimazolam",
            "Remoxipride",
            "Resperine",
            "Rizatriptan",
            "Ropivacaine",
            "Safinamide",
            "Salmeterol Xinafoate",
            "Secobarbital",
            "Selegiline",
            "Serdexmethylphenidate",
            "Sertindole",
            "Sertraline",
            "Sevoflurane",
            "Sibutramine",
            "Sodium Oxybate",
            "Solriamfetol",
            "Sufentanil",
            "Sulpiride",
            "Sumatriptan",
            "Suvorexant",
            "Tapentadol",
            "Temazepam",
            "Terbutaline Sulfate",
            "Tetrabenazine",
            "Tetracaine HCl",
            "Tetrahydrozoline HCl",
            "Thiethylperazine",
            "Thiopental",
            "Thiopropazate",
            "Thioridazine",
            "Tianeptine",
            "Tilidine",
            "Tizanidine",
            "Tolonium Chloride",
            "Topiramate",
            "Tramadol",
            "Tranylcypromine",
            "Trazodone",
            "Triazolam",
            "Trichlormethiazide",
            "Trifluoperazine",
            "Trifluperidol",
            "Trimeprazine",
            "Trimipramine",
            "Tryptophan",
            "Tyrosine",
            "Venlafaxine",
            "Viloxazine",
            "Vortioxetine",
            "Xipamide",
            "Zaleplon",
            "Ziprasidone",
            "Zomitriptan",
            "Zolpidem",
            "Zopiclone",
            "Zotepine"
        ],
        "half_life": (
            "Isocarboxazid has a half life between 1.5 to 4 hours."
        ),
    },
        "amisulpride": {
        "brand_names": ["Solian"],
        "categories": ["Antipsychotics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Atypical Antipsychotic"],
        "class": "Atypical Antipsychotic",
        "conditions": [
            "Schizophrenia",
            "Depression",
            "Dysthymia",
            "Nausea",
            "Vomiting",
            "Acute psychosis"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Extrapyramidal side effects",
            "Hyperprolactinaemia",
            "Weight gain",
            "Insomnia"
        ],
        "info": [
            "Amisulpride is an atypical antipsychotic, chemically considered a benzamide drug. It is "
            "associated with high prolactin, which can cause lactation in both men and women. It has a lower "
            "risk of causing movement related disorders. In the United States, it is only approved for prevention "
            "of postoperative nausea and vomiting. It is considered to be as effacacious as olanzapine, even being considered "
            "a viable treatment option in cases of clozapine-resistant schizophrenia. It was found to be very "
            "helpful in treating dysthymia and is approved for depression in numerous countries."
        ],
        "metabolism": [

        ],
        "interactions": [
            "Citalopram",
            "Bupropion",
            "Clozapine",
            "Sertindole",
            "Ziprasidone",
            "TCAs"

        ],
        "half_life": (
            "Amisulpride has a half life of 12 hours"
        ),
    },
        "Aripiprazole": {
        "brand_names": ["Abilify"],
        "categories": ["Antipsychotic"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Atypical Antipsychotic"],
        "class": "Atypical Antipsychotic",
        "conditions": [
            "Schizophrenia",
            "Bipolar disorder",
            "Autism",
            "Major Depressive Disorder",
            "Depression",
            "Tic disorder",
            "Tourette's"

        ],
        "off_label_uses": [
            "Obsessive-Compulsive Disorder",
            "OCD",

        ],
        "side_effects": [
            "Restlessness",
            "Insomnia",
            "Weight gain",
            "Nausea",
            "Constipation"
        ],
        "info": [
            "Aripiprazole is an atypical antipsychotic that is occassionally referred to as a third generation "
            "antipsychotic. It is used to treat various mental disorders, including certain neurologic disorders like "
            "Tourette syndrome and Autism. It is unique as it is a selective partial agonist at the D2 receptors when levels are low "
            "and reducing when levels are high. It is also a partial agonist at the D3 and D4 receptors, as well as certain serotonin "
            "receptors. "

        ],
        "metabolism": [
            "CYP3A4",
            "CYP2D6"

        ],
        "interactions": [
            "Bepridil",
            "Bromopride",
            "Cisapride",
            "Dronedarone",
            "Ensitrelvir",
            "Fluconazole",
            "Isocarboxazid",
            "Ketoconazole",
            "Levoketoconazole",
            "Mavorixafor",
            "Mesoridazine",
            "Metoclopramide",
            "Pimozide",
            "Piperaquine",
            "Posaconzole",
            "Saquinavir",
            "Sparfloxacin",
            "Terfenadine",
            "Thiorizidazine",
            "Ziprasidone"
            
        ],
        "half_life": (
            "Arirpiprazole has a half life of 75 hours. "
        ),
    },
        "Acepromazine": {
        "brand_names": ["Atravet","Acezine"],
        "categories": ["Antipsychotics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Typical Antipsychotic"],
        "class": "Typical Antipsychotic",
        "conditions": [
            "Nausea (animal)",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [
            "Acepromazine is an antipsychotic drug that was used in the 1950s for human use, "
            "however, today it is almost exclusively used in animals as a sedative and antiemetic. "
            "It is closely related to analogue chlorpromazine, which is still used in humans. "
        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            "Acepromazine has a half life of 3 hours in horses, and 16 hours in canines. "
        ),
    },
     "mixed amphetamine salts": {
        "brand_names": ["Adderall","Adderall XR","Mydayis"],
        "categories": ["Stimulant"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["CNS"],
        "class": "Central Nervous System Stimulant",
        "conditions": [
            "Attention Deficit/Hyperactivity Disorder",
            "ADHD",
            "Narcolepsy"

        ],
        "off_label_uses": [
            "Athletic Performance enhancement",
            "Cognitive Enhancer",
            "Appetite suppressant",

        ],
        "side_effects": [
            "Euphoria",
            "Sex drive changes",
            "Increased wakefulness",
            "Hypertension",
            "Raynaud's phenomenon",
            "Tachycardia",
            "Frequent erections",
            "Abdominal pain",
            "Diarrhea",
            "Nausea"
        ],
        "info": [
            "Mixed amphetamine salts (also known as adderall) typically refers to a combonatination of "
            "dextroamphetamine and levoamphetamine. It is used to treat attention deficit hyperactivity disorder (ADHD) "
            "and Narcolepsy."
            
        ],
        "metabolism": [
            "CYP2D6",
            "DBH",
            "FMO3",
            "XM-ligase",
            "GLYAT"
        ],
        "interactions": [
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Pimozide",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Sibutramine",
            "Tranylcypromine"
        ],
        "half_life": (
            "9 to 11 hours for dextroamphetamine, and 11 to 14 hours for levoamphetamine"
        ),
    },
     "Zolpidem": {
        "brand_names": ["Ambien"],
        "categories": ["Nonbenzodiazepines"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Z-drugs"],
        "class": "Nonbenzodiazepine",
        "conditions": [
            "Insomnia"

        ],
        "off_label_uses": [
            "Brain injury",
            "Parkinson's disease",
            "Comatose state",
            "Vegetative state"
        ],
        "side_effects": [
            "Sleepiness",
            "Headache",
            "Nausea",
            "Diarrhea",
            "Memory problems",
            "Hallucinations",
            "Depression"
        ],
        "info": [
            "Zolpidem is a medication used for short term treatment of sleeping problems. It is only "
            "to be used after CBT for insomnia and after behavioral changed have been made and tried. "
            "It decreases the time to sleep onset by about 15 minutes and at larger doses, helps people stay "
            "asleep longer. Flumazenil can reverse zolpidem's effects during overdose."
        ],
        "metabolism": [
            "CYP3A4",
            "CYP2C9",
            "CYP1A2",
            "CYP2D6",
            "CYP2C19"
        ],
        "interactions": [
            "Calcium Oxybate",
            "Ensitrelvir",
            "Magnesium Oxybate",
            "Potassium Oxybate",
            "Sodium Oxybate"

        ],
        "half_life": (
            "3 hours for immediate release versions, and 3 to 6 hours for "
            "extended release formulations. "
        ),
    },
     "Disulfiram": {
        "brand_names": ["Antabuse"],
        "categories": ["Alcohol-abuse deterrant"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Alcohol-abuse deterrant"],
        "class": "Aldehyde dehydrogenase inhibitor",
        "conditions": [
            "Alcoholism",
            "Alcohol use disorder",
            "AUD"

        ],
        "off_label_uses": [
            "Glioblastoma",
            "Metastatic Breast Cancer",
            "Parasitic Infections",
            "HIV"
        ],
        "side_effects": [
            "Headache",
            "Metallic taste",
            "Sexual side effects"
        ],
        "info": [
            "Disulfiram is a second line treatment for alcoholism, behind acamprosate (Campral) and Naltrexone. "
            "Under normal metabolism, alcohol is broken down in the liver by the enzyme alcohol dehydrogenase to acetaldehyde "
            "dehydrogenase to harmless acetic acid. Disulfiram blocks this reaction at the intermediate stage by blocking acetalehyde "
            "dehydrogenase. This causes the acetaldehyde in the blood to be five to ten times higher than found during metabolism alone. "
            "it causes a person to have severe hangover symptoms as well as immediate negative reaction to alcohol. It does not reduce alcohol cravings "
            "like the other drugs, so compliance is often poor. There is a subdermal implant replaced every 12 weeks that has better results. "
        ],
        "metabolism": [
            "ALDH",
            "TPMT",
            "CYP2E1",
            "DBH",
            "BCHE",
            "CES1",
            "CES2"
        ],
        "interactions": [
            "Amprenavir",
            "Dronabinol",
            "Metronidazole",
            "Paraldehyde",
            "Sertraline"
        ],
        "half_life": (
            "About 7.3 hours"
        ),
    },
     "Benperidol": {
        "brand_names": ["Anquil","Frenactyl"],
        "categories": ["Antipsychotics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Typical Antipsychotic"],
        "class": "Typical Antipsychotic",
        "conditions": [
            "Hypersexuality Syndrome",
            "Antisocial hypersexual behavior",
            "Schizophrenia"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Extrapyramidal symptoms (EPS)",
            "Sleepiness",
            "Dry Mouth",
            "Hyperprolactinemia",
            "Weight gain",
            "High blood sugar"
        ],
        "info": [
            "Benperidol is a typical antipsychotic drug, frequently used to treat antisocial hypersexual "
            "behavior. It is considered one of the most potent neuroleptics available. It is often used as a "
            "parole condition for sex offenders. It is primarily a D2 and D4 antagonist. "
        ],
        "metabolism": [
            "CYP3A4"

        ],
        "interactions": [
            "Levodopa",
            "Epinephrine"
            
        ],
        "half_life": (
            "Benperidol has a half life from 8 to 30 hours"
        ),
    },
     "Donepezil": {
        "brand_names": ["Aricept"],
        "categories": ["anticholinesterase agents"],
        "specialties": ["Psychiatry"],
        "drug_classes": [""],
        "class": "anticholinesterase agents",
        "conditions": [
            "Dementia",
            "Alzheimer's Disease"
        ],
        "off_label_uses": [
            "Lewy body dementia",
            "Traumatic brain injury",
            "Vascular dementia",
            "Dementia associated with Parkinson's Disease",
            "Parkinson's Disease Dementia"
        ],
        "side_effects": [
            "Diarrhea",
            "Nausea",
            "Vomiting",
        ],
        "info": [
            "Donezepil is a medication used to treat Alzheimer's disease, which is a form of dementia. "
            "It has a small benefit in mental function and overall ability to function, however it does not "
            "change the course of the disease. It is available to be taken by mouth and by a transdermal patch. "
    
        ],
        "metabolism": [
            "CYP2D6",
            "CYP3A4"
        
        ],
        "interactions": [
            "Bepridil",
            "Cisapride",
            "Dronedarone",
            "Levoketoconazole",
            "Mesoridazine",
            "Pimozide",
            "Piperaquine",
            "Saquinavir",
            "Sparfloxacin",
            "Terfenadine",
            "Thioridazine",
            "Ziprasidone"

        ],
        "half_life": (
            "Donepezil has a half life around 70 hours, though it is up to 100 in the elderly."
        ),
    },
     "buspirone": {
        "brand_names": ["Buspar"],
        "categories": ["Anxiolytics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Anxiolytic"],
        "class": "Anxiolytic",
        "conditions": [
            "Anxiety",
            "Generalized Anxiety Disorder",
            "GAD"
        ],
        "off_label_uses": [
            "Depression",
            "antidepressant induced sexual dysfunction",
            "hypoactive sexual desire disorder"
        ],
        "side_effects": [
            "Nausea",
            "Headaches",
            "Dizziness",
            "Movement disorders"
        ],
        "info": [
            "Buspirone is an anxiolytic agent that does not produce significant sedation, dependence "
            "or withdrawal symptoms. It's drug mechanism is primarily partial agonism at the postsynaptic serotonin "
            "5-HT1A receptors and full agonism at presynaptic 5-HT1A autoreceptors. This initially reduces "
            "serotogenic neuron firing. It has weak antagonistic effects at multiple dopamine receptors as well as "
            "some alpha receptors. It is used primarily for anxiety, but is occasionally used to augment antidepressants. "
            "It is not associated with sexual side effects, unlike many  psychiatric medications. "
        ],
        "metabolism": [
            "CYP3A4"
        ],
        "interactions": [
            "Ensitrelvir",
            "Isocarboxazid",
            "Levoketoconazole",
            "Linezolid",
            "Phenelzine",
            "Tranylcypromine"
        ],
        "half_life": (
            "About 2.5 hours"
        ),
    },
     "lorazepam": {
        "brand_names": ["Ativan"],
        "categories": ["Anxiolytics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Benzodiazepines"],
        "class": "Benzodiazepines",
        "conditions": [
            "Anxiety",
            "Seizures",
            "Insomnia",
            "Agitation",
            "Catatonia"
        ],
        "off_label_uses": [
            "Alcohol withdrawal",
            ""
        ],
        "side_effects": [
            "weakness",
            "sleepiness",
            "low blood pressure",
            "decreased memory formation",
        ],
        "info": [
            "Lorazepam is a unique drug due to its anxiolytic, sedative, hypnotic, amnesic, anticonvulsant and "
            "muscle relaxant properties. It is a high potency and intermediate acting benzodiazepines. It has recreational "
            "properties and can be a drug of abuse. "
        ],
        "metabolism": [
            "UGT2B4",
            "UGT2B15",
            "UGT2B7",
            "UGT1A7",
            "UGT1A10"
        ],
        "interactions": [
            "Flumazenil",
            "Isocarboxazid"
        ],
        "half_life": (
            "lorazepam has a half line of 10 to 20 hours"
        ),
    },
     "serdexmethylphenidate/dexmethylphenidate": {
        "brand_names": ["Azstarys"],
        "categories": ["Stimulant"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["CNS"],
        "class": "Central Nervous System Stimulant",
        "conditions": [
            "ADHD",
            "Attention Deficit/Hyperactivity Disorder"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "decreased appetite",
            "nausea",
            "indigestion",
            "weight loss",
            "increased heart rate",
        ],
        "info": [
            "Serdexmethylphenidate/dexmethylphenidate is a fixed dose combination medication containing "
            "serdexmethylphenidate, which is a prodrug of dexmethylphenidate. Dexmethylphenidate is a d-threo enantiomer "
            "of racemic methylphenidate, another CNS drug used for treated adhd. It is approved for use in those 6 years "
            "of age and older. "
        ],
        "metabolism": [
            "CES1"
        ],
        "interactions": [
            "Isocarboxazid",
            "Linezolid",
            "Methylene Blue",
            "Ozanimod",
            "Phenelzine",
            "Procarbazine",
            "Rasagiline",
            "Safinamide",
            "Selegiline",
            "Tranylcypromine"

        ],
        "half_life": (
            "the mean terminal elimination halflife of serdexmethylphenidate/dexmethylphenidate is "
            "11.7 hours. "
        ),
    },
     "Chlorprothixene": {
        "brand_names": ["Truxal","Taractan"],
        "categories": ["Antipsychotics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Typical Antipsychotic"],
        "class": "Typical antipsychotic",
        "conditions": [
            "Schizophrenia",
            "Bipolar Disorder",
        ],
        "off_label_uses": [
            "Nausea",
            "Insomnia",
            "Alcohol withdrawal",
            "Opioid withdrawal"
        ],
        "side_effects": [
            "Sedation",
            "Dry mouth",
            "tachycardia",
            "Excessive sweating",
            "Hypotension"
        ],
        "info": [
            "Chlorprothixene is structurally related to another antipsychotic Chlorpromazine (brand name: Thorazine). "
            "Like many typical antipsychotics, it is associated with EPS. However, it is still at a lower rate than other "
            "antipsychotics. This decreased risk occasionally gives it the label of an atypical antipsychotic. Many other drugs "
            "were derived from the creation of Chlorprothixene. Lometraline, Tametraline and Sertrakine were created through "
            "structural modification of Chlorprothixene. "
        ],
        "metabolism": [
            "CYP2D6",
            "CYP3A4",
        ],
        "interactions": [
            "Opioids",
            "Tramadol",
            "TCAs",
            "Anti parkison's drugs"
        ],
        "half_life": (
            "Chlorprothixene has a half life of 8 to 12 hours. "
        ),
    },
     "Fluphenazine": {
        "brand_names": ["Prolixin"],
        "categories": ["Antipsychotics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Typical Antipsychotic"],
        "class": "Typical Antipsychotics",
        "conditions": [
            "Schizophrenia",
        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "EPS",
            "Sleepiness",
            "Depression",
            "Increased weight gain",
        ],
        "info": [
            "Fluphenazine is a typical antipsychotic. It inhibits tubulin polymerizaction, which is something other phenothiazine "
            "derivatives do, including perphenazine, chlorpromazine, trufluoperazine, triflupromazine. It is rarely used in present day due to "
            "the new atypical drugs being more inexpensive, associated with less side effects and just as effective. There are intramuscular injection forms "
            "available. "
        ],
        "metabolism": [
            "CYP2D6",
            "CYP2C9",
            "CYP2E1"
        ],
        "interactions": [
            "Alfuzosin",
            "Amiodarone",
            "Amisulpride",
            "Amitriptyline",
            "Anagrelide",
            "Apomorphine",
            "Aripiprazole",
            "Arsenic Trioxide",
            "Artemether",
            "Asenapine",
            "Astemizole",
            "Atazanavir",
            "Azithromycin",
            "Bedaquiline",
            "Bepridil",
            "Bromopride",
            "Buprenorphine",
            "Buserelin",
            "Calcium Oxybate",
            "Certinib",
            "Chloroquine",
            "Chlorpromazine",
            "Ciprofloxacin",
            "Cisapride",
            "Citalopram",
            "Clarithromycin",
            "Clobazam",
            "Clofazimine",
            "Clomipramine",
            "Clorgyline",
            "Clozapine",
            "Crizotinib",
            "Cyclobenzaprine",
            "Dabrafenib",
            "Dasatinib",
            "Degarelix",
            "Delamanid",
            "Desipramine",
            "Deslorelin",
            "Deutetrabenazine",
            "Disopyramide",
            "Dofetilide",
            "Dolasteron",
            "Domperidone",
            "Donezepil",
            "Doxepin",
            "Dronedarone",
            "Droperidol",
            "Duloxetine",
            "Ebastine",
            "Efavirenz",
            "Encorafenib",
            "Enflurane",
            "Entrectinib",
            "Eribulin",
            "Erythromycin",
            "Escitalopram",
            "Famotidine",
            "Felbamate",
            "Fingolimod",
            "Flecainide",
            "Fluconazole",
            "Fluoxetine",
            "Fluvoxamine",
            "Formoterol",
            "Foscarnet",
            "Fosphenytoin",
            "Galantamine",
            "Gatifloxacin",
            "Gemifloxacin",
            "Glasdegib",
            "Gonadorelin",
            "Goserelin",
            "Granisetron",
            "Halofantrine",
            "Haloperidol",
            "Histerlin",
            "Hydroquinidine",
            "Hydroxychloroquine",
            "Hydroxyzine",
            "Ibuteilide",
            "Iloperidone",
            "Imapramine",
            "Inotuzumab Ozogamicin",
            "Iproniazid",
            "Isocarboxazid",
            "Itraconazole",
            "Ivabradine",
            "Ivosidenib",
            "Ketoconazole",
            "Lapatinib",
            "Leuprolide",
            "Levofloxacin",
            "Levomethadyl",
            "Lofexidine",
            "Lorcaserin",
            "Lumefantrine",
            "Macimorelin",
            "Magnesium oxybate",
            "Mefloquine",
            "Mesoridazine",
            "Methadone",
            "Metoclopramide",
            "Metronidazole",
            "Mifepristone",
            "Mirabegron",
            "Mirtazapine",
            "Mizolastine",
            "Moclobemide",
            "Moxifloxacin",
            "Nafarelin",
            "Nelfinavir",
            "Nialamide",
            "Nilotinib",
            "Norfloxacin",
            "Octreotide",
            "Ofloxacin",
            "Olanzapine",
            "Odansetron",
            "Osilodrostat",
            "Osimertinib",
            "Oxaliplatin",
            "Paliperidone",
            "Panobinostat",
            "Pargyline",
            "Paroxetine",
            "Pasireotide",
            "Pazopanib",
            "Peginterferon Alfa-2b",
            "Pentamidine",
            "Perphenazine",
            "Phenelzine",
            "Pimavanserin",
            "Pimozide",
            "Pindolol",
            "Pipamperone",
            "Piperaquine",
            "Pitolisant",
            "Ponesimod",
            "Posaconazole",
            "Potassium Oxybate",
            "Probucol",
            "Procainamide",
            "Prochlorperazine",
            "Promethazine",
            "Propafenone",
            "Propranolol",
            "Protriptyline",
            "Quetiapine",
            "Quinidine",
            "Quinine",
            "Ranolazine",
            "Ribociclib",
            "Risperidone",
            "Ritonavir",
            "Rolapitant",
            "Saquinavir",
            "Selegiline",
            "Selpercatinib",
            "Sertindole",
            "Sertraline",
            "Sevoflurane",
            "Sodium Oxybate",
            "Sodium Phosphate",
            "Solifenacin",
            "Sorafenib",
            "Sotalol",
            "Sparfloxacin",
            "Sulpiride",
            "Sunitinib",
            "Tacrolimus",
            "Tamoxifen",
            "Telaprevir",
            "Telavancin",
            "Telithromycin",
            "Terfenadine",
            "Tetrabenazine",
            "Thioridazine",
            "Toloxatone",
            "Tolterodine",
            "Toremifene",
            "Tranylcypromine",
            "Trazodone",
            "Triclabendazole",
            "Trimipramine",
            "Triptorelin",
            "Vandetanib",
            "Vardenafil",
            "Vemurafenib",
            "Venlafaxine",
            "Vilanterol",
            "Vinflunine",
            "Voclosporin",
            "Vorinostat",
            "Ziprasidone",
            "Zolmitriptan",
            "Zotepine",
            "Zuclopenthixol",
        ],
        "half_life": (
            "Fluphenazine oral has a half life of 14 to 16 hours. "
        ),
    },
     "Quetiapine": {
        "brand_names": ["Seroquel","Seroquel XR"],
        "categories": ["Antipsychotics"],
        "specialties": ["Psychiatry"],
        "drug_classes": ["Atypical Antipsychotics"],
        "class": "Atypical Antipsychotics",
        "conditions": [
            "Schizophrenia",
            "Bipolar Disorder",
            "Major depressive disorder",
            "Depression"

        ],
        "off_label_uses": [
            "Insomnia",
            "Tourette Syndrome",
            "Tourette's",
            "Anxiety"
        ],
        "side_effects": [
            "Weight gain",
            "Dry mouth",
            "Dizziness",
            "Headache"
        ],
        "info": [

        ],
        "metabolism": [
            "CYP3A4"
        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },

        "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "drug_classes": [""],
        "class": "",
        "conditions": [
            "Depression",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
        "Budesonide-formoterol": {
        "brand_names": ["Symbicort"],
        "categories": ["Inhaler"],
        "specialties": ["Pulmonology"],
        "drug_classes": ["Combination Inhaler"],
        "class": "Combination Inhaler",
        "conditions": [
            "Asthma",
            "Chronic Obstructive Pulmonary Disease (COPD)",
            "Chronic Bronchitis",
            "Emphysema"

        ],
        "off_label_uses": [
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "drug_classes": [""],
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
     "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },

      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
          "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },
      "": {
        "brand_names": [""],
        "categories": [""],
        "specialties": [""],
        "class": "",
        "conditions": [
            "",

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "interactions": [

        ],
        "half_life": (
            ""
        ),
    },


}

DRUGS = {name.strip().lower(): info for name, info in DRUGS.items() if name.strip()}

for _drug_info in DRUGS.values():
    if "off_label_uses" not in _drug_info and "off_label_issues" in _drug_info:
        _drug_info["off_label_uses"] = _drug_info["off_label_issues"]
    _drug_info.pop("off_label_issues", None)
    if "info" not in _drug_info and "Info" in _drug_info:
        _drug_info["info"] = _drug_info["Info"]
    _drug_info.pop("Info", None)
    _drug_info.setdefault("info", [])
    _drug_info.setdefault("off_label_uses", [])
    for _field in ("brand_names", "categories", "specialties", "conditions",
                   "side_effects", "off_label_uses", "info"):
        _value = _drug_info.get(_field, [])
        if isinstance(_value, str):
            _value = [_value] if _value.strip() else []
        _drug_info[_field] = [
            item for item in _value
            if isinstance(item, str) and item.strip()
        ]

SIDE_EFFECTS_NOTE = (
    "Side effects vary from person to person. Not everyone experiences "
    "them, and it is not possible to predict with certainty which effects "
    "a particular person will experience. This program provides general "
    "educational information, not personal medical advice."
)

INTERACTION_WARNING = (
    "WARNING: This list may be incomplete. Always check with a "
    "pharmacist or doctor about potential interactions before "
    "starting, stopping, or combining medications."
)

def lookup_drug_api(drug_name):
    """Search RxNorm for a medication name."""

    url = "https://rxnav.nlm.nih.gov/REST/rxcui.json"

    try:
        response = requests.get(
            url,
            params={"name": drug_name, "search": 2},
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        return data.get("idGroup", {}).get("rxnormId", [])

    except requests.RequestException as error:
        print(f"API request failed: {error}")
        return []


def lookup_dailymed_info(drug_name):
    """Retrieve available drug-label information from DailyMed."""

    search_url = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json"

    try:
        response = requests.get(
            search_url,
            params={"drug_name": drug_name, "pagesize": 5},
            timeout=15
        )
        response.raise_for_status()
        results = response.json().get("data", [])

        if not results:
            return None

        # Use the first matching label for this initial version.
        set_id = results[0].get("setid")

        if not set_id:
            return None

        label_url = (
            "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/"
            + set_id + ".xml"
        )

        response = requests.get(label_url, timeout=15)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        namespace = "{urn:hl7-org:v3}"

        wanted_sections = {
            "indications and usage": "Uses",
            "warnings": "Warnings",
            "warnings and precautions": "Warnings and precautions",
            "adverse reactions": "Side effects and adverse reactions",
            "drug interactions": "Drug interactions",
            "dosage and administration": "Dosage and administration",
        }

        information = {}

        for section in root.iter(namespace + "section"):
            title_element = section.find(namespace + "title")

            if title_element is None:
                continue

            title = " ".join("".join(title_element.itertext()).split())
            title_lower = title.lower()

            for heading, display_name in wanted_sections.items():
                if heading in title_lower and display_name not in information:
                    text_element = section.find(namespace + "text")

                    if text_element is not None:
                        content = " ".join(
                            "".join(text_element.itertext()).split()
                        )

                        if content:
                            information[display_name] = content[:2500]

        return {
            "label_title": results[0].get("title", drug_name),
            "information": information,
            "url": label_url,
        }

    except (requests.RequestException, ET.ParseError, ValueError, KeyError) as error:
        print(f"DailyMed lookup failed: {error}")
        return None


def extract_drug_name(question):
    """Remove common question wording and return the likely drug name."""

    name = question.strip().rstrip("?.! ")

    prefixes = [
        "what is ",
        "what are ",
        "tell me about ",
        "information about ",
        "side effects of ",
        "uses of ",
        "what is the half life of ",
        "what is the half-life of ",
        "how is ",
    ]

    name_lower = name.lower()

    for prefix in prefixes:
        if name_lower.startswith(prefix):
            name = name[len(prefix):].strip()
            break

    # Remove common endings from questions.
    for ending in [" used for", " metabolized by", " processed by"]:
        if name.lower().endswith(ending):
            name = name[:-len(ending)].strip()

    return name

def find_drug(question):
    """Find a generic or brand name mentioned in the question."""

    question_lower = question.lower()
    possible_names = []

    for generic_name, info in DRUGS.items():
        possible_names.append((generic_name, generic_name))

        for brand_name in info.get("brand_names", []):
            if brand_name:
                possible_names.append((brand_name.strip().lower(), generic_name))

    # Check longer names first.
    possible_names.sort(key=lambda pair: len(pair[0]), reverse=True)

    for name, generic_name in possible_names:
        if not name:
            continue
        pattern = r"\b" + re.escape(name.lower()) + r"\b"

        if re.search(pattern, question_lower):
            return generic_name, DRUGS[generic_name]

    return None, None


def show_side_effects(generic_name, info):
    print(f"\nPossible side effects of {generic_name.title()}:")
    effects = info.get("side_effects", [])

    effects = [effect for effect in effects if effect.strip()]
    if effects:
        for effect in effects:
            print(f"- {effect}")
    else:
        print("No side-effect information has been added.")

    print(f"\nNote: {SIDE_EFFECTS_NOTE}")


def show_conditions(generic_name, info):
    print(f"\nConditions listed for {generic_name.title()}:")
    conditions = info.get("conditions", [])

    conditions = [condition for condition in conditions if condition.strip()]
    if conditions:
        for condition in conditions:
            print(f"- {condition}")
    else:
        print("No condition information has been added.")


def show_off_label_uses(generic_name, info):
    print(f"\nOff-label uses listed for {generic_name.title()}:")
    uses = info.get("off_label_uses", [])
    if isinstance(uses, str):
        uses = [uses] if uses.strip() else []
    if uses:
        for use in uses:
            print(f"- {use}")
    else:
        print("No off-label uses have been added yet. Add them to the 'off_label_uses' field.")


def show_class(generic_name, info):
    print(f"\nDrug class of {generic_name.title()}:")
    print(info.get("class") or "Class information has not been added yet.")


def show_half_life(generic_name, info):
    print(f"\nHalf-life of {generic_name.title()}:")
    print(info.get("half_life") or "Half-life information has not been added yet.")


def show_brand_names(generic_name, info):
    print(f"\nBrand names listed for {generic_name.title()}:")
    brand_names = info.get("brand_names", [])

    if brand_names:
        for brand_name in brand_names:
            print(f"- {brand_name}")
    else:
        print("No brand names have been added.")


def show_specialties(generic_name, info):
    print(f"\nSpecialties associated with {generic_name.title()}:")
    specialties = info.get("specialties", [])

    if specialties:
        for specialty in specialties:
            print(f"- {specialty}")
    else:
        print("No specialty information has been added.")


def lookup_drug_api(drug_name):
    """Look up a medication name using the RxNorm API."""

    url = "https://rxnav.nlm.nih.gov/REST/rxcui.json"
    params = {
        "name": drug_name,
        "search": 2
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        drug_ids = data.get("idGroup", {}).get("rxnormId", [])

        if not drug_ids:
            print(f"No RxNorm match found for '{drug_name}'.")
            return None

        print(f"\nRxNorm matches for '{drug_name}':")

        for drug_id in drug_ids[:5]:
            name_url = (
                f"https://rxnav.nlm.nih.gov/REST/rxcui/"
                f"{drug_id}/properties.json"
            )

            name_response = requests.get(name_url, timeout=10)
            name_response.raise_for_status()
            name_data = name_response.json()

            properties = name_data.get("properties", {})
            normalized_name = properties.get("name", "Name unavailable")

            print(f"- {normalized_name} (RxCUI: {drug_id})")

        return drug_ids

    except requests.RequestException as error:
        print(f"API connection error: {error}")
        return None



def show_description(generic_name, info):
    """Display a short description for a medication."""
    print(f"\n{generic_name.title()}")

    description = info.get("description") or (
        "No description has been added yet. Add a 'description' field "
        "to this medication's entry in DRUGS."
    )
    print(description)


def show_drugs_by_class(drug_class):
    class_aliases = {
        "ssri": "ssri",
        "snri": "snri",
        "tca": "tricyclic antidepressant",
        "sndri": "sndri",
        "nri": "nri",
        "ndri": "ndri",
        "sari": "sari",
        "maoi": "maoi",
        "atypical ads": "atypical antidepressant",
        "atypical antidepressant": "atypical antidepressant"
    }

    requested = drug_class.strip().lower()
    requested = class_aliases.get(requested, requested)

    matching_drugs = []

    for drug_name, info in DRUGS.items():
        drug_type = info.get("class", "")

        if isinstance(drug_type, list):
            class_names = drug_type
        elif isinstance(drug_type,str):
            class_names = [drug_type]

        else:
            continue

        for class_name in class_names:
            normalized_class = class_name.lower()
        if requested in {"ssri", "snri", "sndri", "nri", "ndri", "sari"}:
                if f"({requested})" in normalized_class:
                    matching_drugs.append(drug_name)
                    break
                elif requested in normalized_class:
                    matching_drugs.append(drug_name)
                break

    print(f"\nMedications in the class: {drug_class}")

    if matching_drugs:
        print("Medications found:")
        for drug in sorted(set(matching_drugs), key=str.lower):
            print(f"- {drug}")
    else:
        print("No medications found in this class.")
      # normalized_class = drug_type.lower()

        # Match by abbreviation when one is included in parentheses.
       # if requested_class in {"ssri", "snri", "sndri", "nri", "ndri", "sari"}:
        #    if f"({requested_class})" in normalized_class:
        #        matching_drugs.append(drug_name)

        # TCA entries use different singular/plural labels.
      #  elif requested_class == "tricyclic antidepressant":
        #    if "tricyclic antidepressant" in normalized_class:
        #        matching_drugs.append(drug_name)

        # Allow searching by the full class name, too.
       # elif requested_class in normalized_class:
       #     matching_drugs.append(drug_name)

   # print(f"\nMedications in the class: {drug_class}")

   # if matching_drugs:
    #    print("Medications found:")
      #  for drug in sorted(matching_drugs, key=str.lower):
      #      print(f"- {drug}")
   # else:
   #     print("No medications found in this class.")

#def show_drugs_by_class(drug_class):
    #print(f"\nMedications in the class: {drug_class}")

   # class_aliases = {
    #    "ssri": "Selective Serotonin Reuptake Inhibitor (SSRI)",
    #    "snri": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
    #    "tca": "Tricyclic antidepressants",
    #    "sndri": "Serotonin-Norepinephrine-Dopamine Reuptake Inhibitor (SNDRI)",
    #    "nri": "Norepinephrine Reuptake Inhibitor (NRI)"
   #     "ndri":
   # }

   # requested_class = drug_class.strip().lower()

   # requested_class = class_aliases.get(
   #     requested_class, requested_class
  #  )

   # for abbreviation, full_name in class_aliases.items():
    #    if requested_class == abbreviation.lower():
    #        requested_class = full_name.lower()
     #       break

   # matching_drugs = []

   # for drug_name, info in DRUGS.items():
       #     drug_type = info.get("class","")

         #   if isinstance(drug_type,str):
         #       drug_type = [drug_type]

         #   for class_name in drug_type:
            # Compare the main class name, ignoring the abbreviation
            # in parentheses and extra closing parentheses.
        #        normalized_class = class_name.lower().strip()
     #           normalized_class = normalized_class.replace("(", " ")
 #               normalized_class = normalized_class.replace(")", " ")
#                normalized_class = " ".join(normalized_class.split())

        #    if normalized_class.startswith(requested_class):
       #         matching_drugs.append(drug_name)
      #          break
  #  print(f"\nMedications in the class: {drug_class}")

  #  if matching_drugs:
     #   print("Medications found:")
   #     for drug in sorted(matching_drugs):
   #         print(f"- {drug}")
   # else:
   #     print("No medications found in this class.")



            

            #for drug_type_name in drug_type:
            #    if drug_type_name.strip().lower() == requested_class:
            #        matching_drugs.append(drug_name)
            #        break
            #if matching_drugs:
            #    print("Medications found:")
             #   for drug in sorted(matching_drugs):
              #      print(f"- {drug}")
          #  else:
            #    print("No medications found in this class")

    #matching_drugs = []

    #for drug_name, info in DRUGS.items():
    #    drug_type = info.get("class","")

    #    if isinstance(drug_type,str):
        #    drug_type = [drug_type]

        #for drug_type_name in drug_type:
           # if drug_type_name.lower() == drug_class.lower():
          #      matching_drugs.append(drug_name)
          #      break
   # if matching_drugs:
      #  print("Medications found:")
      #  for drug in sorted(matching_drugs):
        #    print(f"- {drug}")
    #se:
       # print("No medications found in this class")

    
def show_info(generic_name, info):
    """Display general notes/information added to a medication entry."""
    print(f"\nGeneral information for {generic_name.title()}:")
    notes = info.get("info", [])
    if isinstance(notes, str):
        notes = [notes] if notes.strip() else []
    if notes:
        for note in notes:
            print(f"- {note}")
    else:
        print("No general information has been added yet. Add notes to the 'info' field.")


def show_full_profile(generic_name, info):
    print(f"\nMedication: {generic_name.title()}")
    show_brand_names(generic_name, info)
    show_specialties(generic_name, info)
    categories = info.get("categories", [])
    if isinstance(categories, str):
        categories = [categories] if categories.strip() else []
    print("Categories: " + (", ".join(categories) if categories else "Not added yet"))
    show_class(generic_name, info)
    show_conditions(generic_name, info)
    show_info(generic_name, info)
    show_off_label_uses(generic_name, info)
    show_side_effects(generic_name, info)
    show_half_life(generic_name, info)
    show_metabolism_enzymes(generic_name, info)
    show_interactions(generic_name, info)

def show_interactions(generic_name, info):
    print(f"\nDrug interactions for {generic_name.title()}:")
    print(INTERACTION_WARNING)

    interactions = info.get("interactions", [])
    interactions = [
        item for item in interactions
        if isinstance(item, str) and item.strip()
    ]

    if interactions:
        for interaction in interactions:
            print(f"- {interaction}")
    else:
        print("No interaction information has been added yet.")

def show_metabolism_enzymes(generic_name, info):
    print(f"\nMetabolism enzymes for {generic_name.title()}:")

    enzymes = info.get("metabolism", [])

    if isinstance(enzymes, str):
        enzymes = [enzymes] if enzymes.strip() else []

    enzymes = [
        e.strip() for e in enzymes
        if isinstance(e,str) and e.strip()
    ]

    if not enzymes:
        print("No metabolism information has been added yet.")
        return

    for enzyme in enzymes:
        other_drugs = []

        for other_name, other_info in DRUGS.items():
            if other_name.lower() == generic_name.lower():
                continue

            other_enzymes = other_info.get("metabolism", [])

            if isinstance(other_enzymes, str):
                other_enzymes = [other_enzymes] if other_enzymes.strip() else []

            other_enzymes = [
                e.strip().lower() for e in other_enzymes
                if isinstance(e,str) and e.strip()
            ]
            if enzyme.lower() in other_enzymes:
                other_drugs.append(other_name.title())

        #if any(
         #   enzyme.strip().lower() == other_enzyme.strip().lower()
         #   for other_enzyme in other_enzymes
          #  if isinstance(other_enzyme,str) and other_enzyme.strip()
        #):
          #  count += 1 
          #  other_drugs.append(other_name.title())

        print(f"\nEnzyme:{enzyme}")
        print(
            f"This medication shares {enzyme} with "
            f"{len(other_drugs)} other medication(s) in the database."
        )

        if other_drugs:
            print("Other medications listed:")
            for drug in sorted(other_drugs):
                print(f"- {drug}")

    

def answer_question(question, last_drug=None):
    """Answer a focused question and remember the most recently identified drug."""
    generic_name, info = find_drug(question)

    if generic_name is None and last_drug in DRUGS:
        question_lower = question.lower()

        follow_up_phrases = [
            "side effects",
            "half life",
            "halife-life",
            "metabolism",
            "metabolized by",
            "interactions",
            "dosage",
            "what is it",
            "tell me more",
            "full profile"
        ]
        if any(phrase in question_lower for phrase in follow_up_phrases):
            generic_name = last_drug
            info = DRUGS[generic_name]

        if generic_name is None:
            possible_name = question.strip().rstrip("?.!")

            rxnorm_ids = lookup_drug_api(possible_name)
            result = lookup_dailymed_info(possible_name)

            if result and result.get("information"):
                print(f"\nDrug label: {result['label_title']}")
                print("Source: DailyMed")
                print(result["url"])

                for heading, details in result["information"].items():
                    print(f"\n--- {heading} ---")
                    print(details)
            elif rxnorm_ids:
                print(f"\nRxNorm recognized '{possible_name}'.")
                print(f"RxNorm ID: {rxnorm_ids[0]}")
                print("No detailed drug information was retrieved.")
            else:
                print(f"\nI couldn't find information for '{possible_name}'.")

        return last_drug

    question_lower = question.lower()

    # Check specific requests before general questions such as "what is".
    if any(term in question_lower for term in [
        "side effect", "side effects", "adverse effect", "adverse effects"
    ]):
        show_side_effects(generic_name, info)

    elif any(term in question_lower for term in [
        "half-life", "half life", "half lives", "half-lives"
    ]):
        show_half_life(generic_name, info)

    elif "off-label" in question_lower or "off label" in question_lower:
        show_off_label_uses(generic_name, info)

    elif any(term in question_lower for term in [
        "general info", "general information", "extra info", "notes about", "info about"
    ]):
        show_info(generic_name, info)

    elif any(term in question_lower for term in [
        "condition", "conditions", "treat", "treated", "used for",
        "indication", "indications"
    ]):
        show_conditions(generic_name, info)

    elif any(term in question_lower for term in [
        "drug class", "what class", "class", "type of drug", "category"
    ]):
        show_class(generic_name, info)

    elif any(term in question_lower for term in [
        "brand", "brand name", "brand names"
    ]):
        show_brand_names(generic_name, info)

    elif any(term in question_lower for term in [
        "specialty", "specialties", "speciality", "specialities"
    ]):
        show_specialties(generic_name, info)

    elif "interaction" in question_lower:
        show_interactions(generic_name, info)

    elif any(term in question_lower for term in [
        "metabolism enzyme",
        "metabolism enzymes",
        "metabolized by",
        "metabolised by",
        "cyp enzyme",
        "cyp enzymes",
        "metabolism"

    ]):
        show_metabolism_enzymes(generic_name, info)

    elif any(term in question_lower for term in ["what is", "what's"]):
        show_info(generic_name, info)
        choice = input(
            "\nWould you like to see the full profile? (yes/no): "
        ).strip().lower()

        if choice in {"yes", "y"}:
            show_full_profile(generic_name, info)
        else:
            print("No problem! Ask me another question.")
    elif generic_name is not None and any(term in question_lower for term in [
        "tell me about", "full profile", "everything about",
        "give me information", "information about"
    ]):
        show_full_profile(generic_name, info)

    elif generic_name is not None and question_lower.strip() in {
        generic_name.lower(),
        *[brand.lower() for brand in info.get("brand_names", [])],
    }:
        show_full_profile(generic_name, info)

    #elif any(term in question_lower for term in[""])
    elif generic_name is None:
        possible_name = question.strip().rstrip("?.! ")

        for prefix in ("what is ", "what's ", "tell me about "):
            if possible_name.lower().startswith(prefix):
                possible_name = possible_name[len(prefix):].strip()
                break

        # Try the medication APIs only if the local database had no match.
        rxnorm_ids = lookup_drug_api(possible_name)
        result = lookup_dailymed_info(possible_name)

        if result and result.get("information"):
            print(f"\nDrug label: {result.get('label_title', possible_name)}")
            print("Source: DailyMed")
            print(result.get("url", ""))

            for heading, details in result["information"].items():
                print(f"\n--- {heading} ---")
                print(details)

        elif rxnorm_ids:
            print(
                f"\nRxNorm recognized '{possible_name}', "
                "but detailed information wasn't retrieved."
            )

        else:
            print(
                f"\nI couldn't retrieve information for '{possible_name}'."
            )

        return last_drug

    #elif generic_name is None:
        #print("\nI couldn't identify that medication in the database.")

    #else:
       #print(f"\nI found {generic_name.title()} in the database.")
       # print("Ask about side effects, conditions, class, half-life,")
       # print("brand names, specialties, or say 'what is' for a short description.")

    return generic_name if generic_name is not None else last_drug


def normalize_text(value):
    """Lowercase text and collapse repeated whitespace."""
    return " ".join(str(value).lower().strip().split())


def list_drugs():
    print("\nMedications in the database:")
    for generic_name in sorted(DRUGS):
        brands = DRUGS[generic_name].get("brand_names", [])
        if brands:
            print(f"- {generic_name.title()} (brand: {', '.join(brands)})")
        else:
            print(f"- {generic_name.title()}")


def list_category(category_name):
    """List drugs by category, tolerating simple singular/plural differences."""
    requested = normalize_text(category_name).rstrip("s")
    print(f"\nMedications in {category_name.strip().title()}:")
    found = False
    for drug_name, info in sorted(DRUGS.items()):
        categories = info.get("categories", [])
        if isinstance(categories, str):
            categories = [categories]
        if any(normalize_text(category).rstrip("s") == requested for category in categories):
            print(f"- {drug_name.title()} ({info.get('class') or 'Class not added yet'})")
            found = True
    if not found:
        print("No medications found in that category. Check the spelling or add the category to your entries.")


def list_drugs_by_class(class_name):
    """List medications by their drug_classes field."""

    aliases = {
        "ssris": "ssri",
        "snris": "snri",
        "tcas": "tca",
        "tecas": "teca",
        "saris": "sari",
        "atypical ads": "atypical antidepressants",
        "atypical aps": "atypical antipsychotic",
        "atypical ap": "atypical antipsychotic",
        "typical aps": "typical antipsychotic",
        "typical ap": "typical antipsychotic",
    }

    requested = normalize_text(class_name)
    requested = aliases.get(requested, requested)

    found = []

    for drug_name, info in DRUGS.items():
        groups = info.get("drug_classes", [])

        if isinstance(groups, str):
            groups = [groups]

        if any(normalize_text(group) == requested for group in groups):
            found.append((drug_name, info))

    print(f"\nMedications in {class_name.upper()}:")

    if not found:
        print("No medications found in this group.")
        print("Check that the medications have a drug_classes entry.")
        return

    for drug_name, info in sorted(found):
        print(f"- {drug_name.title()}")
        print(f"  Class: {info.get('class') or 'Not added'}")


def list_drugs_for_condition(condition_name):
    """Search listed conditions and off-label uses."""
    requested = normalize_text(condition_name)
    found = []

    for drug_name, info in DRUGS.items():
        conditions = info.get("conditions", [])
        off_label_uses = info.get("off_label_uses", [])

        if isinstance(conditions, str):
            conditions = [conditions]

        if isinstance(off_label_uses, str):
            off_label_uses = [off_label_uses]

        condition_match = any(
            requested in normalize_text(term)
            or normalize_text(term) in requested
            for term in conditions
            if isinstance(term, str) and term.strip()
        )

        off_label_match = any(
            requested in normalize_text(term)
            or normalize_text(term) in requested
            for term in off_label_uses
            if isinstance(term, str) and term.strip()
        )


        # Check whether the condition matches
       # condition_match = any(
       #     normalize_text(term) == requested
       #     for term in conditions
       #     if isinstance(term, str) and term.strip()
       #     )
       # off_label_match = any(
       #     normalize_text(term) == requested
       #     for term in off_label_uses
       #     if isinstance(term, str) and term.strip()
#)

        #off_label_match = any(
        #    requested == normalize_text(term)
        #    for term in off_label_uses
        #    if isinstance(term, str) and term.strip()
       # )

        if condition_match or off_label_match:
            found.append((drug_name, info, off_label_match))

    print(f"\nMedications listed for '{condition_name}':")

    if not found:
        print("No matches found in the current database.")
        print(
            "This only searches information entered here; "
            "it does not mean no medications treat the condition."
        )
        return

    for drug_name, info, off_label in sorted(found):
        print(f"- {drug_name.title()}")

        if off_label:
            print("  OFF-LABEL")

        print(f"  Class: {info.get('class') or 'Not added'}")

        categories = info.get("categories", [])
        if isinstance(categories, str):
            categories = [categories]

        print(
            f"  Categories: "
            f"{', '.join(categories) if categories else 'Not added'}"
        )

def list_conditions():
    conditions = set()
    for info in DRUGS.values():
        for field in ("conditions", "off_label_uses"):
            values = info.get(field, [])
            if isinstance(values, str):
                values = [values]
            conditions.update(v.strip() for v in values if isinstance(v, str) and v.strip())
    print("\nConditions and uses in the database:")
    for condition in sorted(conditions, key=str.lower):
        print(f"- {condition}")
    if not conditions:
        print("- None added yet")


def list_specialties():
    specialties = set()
    for info in DRUGS.values():
        specialties.update(v.strip() for v in info.get("specialties", []) if v.strip())
    print("\nSpecialties in the database:")
    for specialty in sorted(specialties, key=str.lower):
        print(f"- {specialty}")
    if not specialties:
        print("- None added yet")


def show_help():
    print("\nCommands you can use:")
    print("- list drugs")
    print("- list antidepressants")
    print("- list category: Antidepressants")
    print("- drugs that treat OCD")
    print("- list conditions")
    print("- list specialties")
    print("- Ask about a drug's side effects, conditions, class, half-life, info, or off-label uses")
    print("- Ask about a specific drug by the brand or generic name")


def main():
    print("=" * 42)
    print("        DRUG INFORMATION PROGRAM")
    print("=" * 42)
    show_help()
    print("Type 'quit' to exit.")
    last_drug = None

    while True:
        question = input("\nWhat would you like to know? ").strip()
        normalized = normalize_text(question)

        if normalized in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not normalized:
            print("Please enter a question.")
            continue
        if normalized in {"help", "commands"}:
            show_help()
        elif normalized in {"list drugs", "show all drugs", "list all drugs"}:
            list_drugs()
        elif normalized == "list conditions":
            list_conditions()
        elif normalized == "list specialties":
            list_specialties()
        
        elif normalized.startswith("list "):
            requested_group = normalize_text(question[5:].strip())

            class_groups = {
                "ssri", "ssris",
                "snri", "snris",
                "tca", "tcas",
                "atypical antipsychotic",
                "atypical antipsychotics",
                "atypical ap", "atypical aps",
                "typical antipsychotic",
                "typical antipsychotics",
                "typical ap", "typical aps",
                "atypical antidepressant",
                "atypical antidepressants"
            }

            if requested_group in class_groups:
                list_drugs_by_class(requested_group)
            else:
                list_category(question[5:].strip())

       # elif normalized.startswith("list"):
         #   list_category(question[5:].strip())
        elif normalized.startswith("list drugs that treat ") or normalized.startswith("tell me all the drugs that treat ") or normalized.startswith("list drugs for ") or normalized.startswith("which drugs treat ") or normalized.startswith("what drugs treat ") or normalized.startswith("medications that treat ") or normalized.startswith("drugs that treat ") or normalized.startswith("which medications treat ") or normalized.startswith("what medications treat ") or normalized.startswith("find drugs for "):
            prefixes = (
                "tell me all the drugs that treat ", "list drugs that treat ",
                "list drugs for ", "which drugs treat ", "what drugs treat ",
                "medications that treat ", "drugs that treat ",
                "which medications treat ", "what medications treat ", "find drugs for "
            )
            condition = normalized
            for prefix in prefixes:
                if condition.startswith(prefix):
                    condition = condition[len(prefix):]
                    break
            list_drugs_for_condition(condition.rstrip("?.! "))

        
        elif normalized.startswith("list "):
            requested = question[5:].strip()
            requested_lower = requested.lower()

            drug_classes = {
                "ssri", "snri", "tca", "sndri", "nri", "ndri", "sari",
                "tricyclic antidepressants",
                "tricyclic antidepressant",
                "selective serotonin reuptake inhibitor (ssri)",
                "serotonin norepinephrine reuptake inhibitor (snri)"
            }

            if requested_lower in drug_classes:
                show_drugs_by_class(requested)
            else:
                list_category(requested)

        else:
            last_drug = answer_question(question, last_drug)



if __name__ == "__main__":
    main()
    
