"""
Drug Information Program — expandable starter script

Educational use only. Verify medication information against reliable,
current sources. This program is not a substitute for medical advice.
"""

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
        "class": "SSRI (Selective Serotonin Reuptake Inhibitors)",
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
            "Obsessive-Compulsive Disorder (OCD)",
            "Anxiety",
            "Generalized Anxiety Disorder (GAD)",
            "Bulimia Nervosa",
            "Premenstrual Dysphoric Disorder (PMDD)",
            "Panic Disorder"
        ],
        "off_label_uses":[
            "Bipolar Depression"
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
            "Phenelzine",
            "Tranycypromine",
            "Pimozide",
            "Thioridazine"
            "Isocarboxid",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Escitalopram",
            "Citalopram",
            "Sertraline",
            "Paroxetine",
            "Fluvoxamine"

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
        "class": "SSRI (Selective Serotonin Reuptake Inhibitor)",
        "metabolism":[
            "CYP2D6"

        ],
        "interactions":[
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Fluoxetine",
            "Citalopram",
            "Fluvoxamine",
            "Paroxetine",
            "Sertraline"

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
            "Social Anxiety Disorder",
            "Panic Disorder",
            "Premenstrual Dysphoric Disorder (PMDD)"

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
        "class": "SSRI (selective serotonin reuptake inhibitor)",
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
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Tryptophan",
            "MDMA",
            "Escitalopram",
            "Fluoxetine",
            "Fluvoxamine",
            "Sertraline",
            "Paroxetine"
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
        "class": "SSRI (selective serotonin reuptake inhibitors)",
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
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Pimozide",
            "Disulfiram",
            "Fluoxetine",
            "Escitalopram",
            "Citalopram",
            "Fluoxamine",
            "Paroxetine"

        ],
        "conditions": [
            "Depression",
            "Generalized Anxiety Disorder (GAD)",
            "Social Anxiety Disorder",
            "Obsessive-Compulsive Disorder (OCD)",
            "Obsessive-Compulsive Disorder (pediatric)"
            "Panic Disorder",
            "Premenstrual Dysphoric Disorder (PMDD)",
            "Post-Traumatic Stress Disorder (PTSD)"
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
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
        "info":[
            
        ],
        "conditions": [
            "Depression",
            "Major Depressive Disorder"
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
            "Attention deficit-hyperactive disorder (ADHD)",
            "Post-Traumatic Stress Disorder (PTSD)",
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
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "St John's Wort",
            "Tramadol",
            "Duloxetine",
            "Desvenlafaxine",
            "Levomilnacipran",
            "Milnacipran"


        ],
        "half_life": (
            "Immediate release (IR) formulations half life is about 5 hours."
            "ER or Extrended Release formulations have an 11-15 hour half life"
        ),
    },
    "Duloxetine": {
        "brand_names": ["Cymbalta"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry","Neurology","Pain Management"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI))",
        "conditions": [
            "Depression",
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
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Venlafaxine",
            "Desvenlafaxine",
            "Levomilnacipran",
            "Milnacipran"

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
        "brand_names": ["Pristiq"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
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
        "metabolism:": [
            "CYP3A4"

        ],
        "interactions": [
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Venlafaxine",
            "Tramadol",
            "Duloxetine",
            "Levomilnaciprin",
            "Milnacipran"


        ],
        "half_life": (
            "Desvenlafaxine has a half life of about 11 hours. "
        ),
    },
    "Paroxetine": {
        "brand_names": ["Paxil"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "SSRI",
        "conditions": [
            "Major Depressive Disorder",
            "Depression",
            "Generalized Anxiety Disorder (GAD)",
            "Anxiety",
            "Obsessive-Compulsive Disorder (OCD)",
            "Social Anxiety Disorder",
            "Post-Traumatic Stress Disorder (PTSD)",
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
            "doctors may use fluoxetine as a 'bridge' in order to taper off of paroxetine. "

        ],
        "metabolism": [
            "CYP2DR"

        ],
        "interactions": [
            "Pimozide",
            "Linezolid",
            "Thioridazine",
            "Tryptophan",
            "Warfarin",
            "Fluvoxamine",
            "Escitalopram",
            "Citalopram",
            "Fluoxetine",
            "Sertraline",
            

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
        "class": "SSRI (selective serotonin reuptake inhibitors)",
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
            "Fluvoxamine (not to be confused with the other SSRI, Fluoxetine) is an SSRI drug "
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
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Olanzapine",
            "Fluoxetine",
            "Escitalopram",
            "Citalopram",
            "Paroxetine",
            "Sertraline"


        ],
        "half_life": (
            "In young, healthy volunteers, Fluvoxamine had a half life nbetween 13.6 to "
            "15.6 hours. However, in the elderly, the half life ranged from 17.4 to 25.9 hours."
        ),
    },
    "Bupropion": {
        "brand_names": ["Wellbutrin","Wellbutrin XL","Wellbutrin SR","Zyban","Forfivo"],
        "categories": ["Antidepressants"],
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
            "in patients with preexistinf seizure disorders such as epilepsy. The instant release formulation has a greater "
            "risk of seizures as opposed to the extended release formulations. "


        ],
        "interactions": [
            "Isocarboxid",
            "Phenlzine",
            "Tranylcypromine",
            "Selegiline",
            "Metralinedole",
            "Moclobemide",
            "Pirlindole",
            "Carbamazepine"

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
        "brand_names": ["Desryl"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin antagonist and reuptake inhibitors (SARI)",
        "conditions": [
            "Depression",
            "Major Depressive Disorder"
            "Insomnia",
        ],
        "side_effects": [
            "Prolonged erections",
            "Headache",
            "Orthostatic hypotension",
        ],
        "info": [
            "Trazodone is an atypical antidepressant (sometimes classified as a serotonin antagonist and reuptake inhibitor "
            "used primarily for both depression and insomnia. It is often combined with an SSRI, to augment the antidepressant and anxiolytic "
            "benefits while I also reducing certain side effects. While Trazodone is not "
            ""

        ],
        "metabolism": [

        ],
        "interactions": [

        ],

        "half_life": (
            ""
        ),
    },
    "Mirtazapine": {
        "brand_names": ["Remeron"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tetracyclic Antidepressants",
        "conditions": [
            "Depression",
            "Insomnia",
        ],
        "side_effects": [
            "Weight Gain",
            "",
        ],
        "half_life": (
            ""
        ),
        "info": (
            "Mirtazapine is a tetracyclic antidepressant. "
            "The combination of mirtazapine and venlafaxine is known as 'california rocket fuel' due to their synergy"
        )
    },
    "Amitriptyline": {
        "brand_names": ["Elvail"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry","Neurology","Gastroenterology","Rheumatology"],
        "class": "Tricyclic Antidepressants",
        "conditions": [
            "Depression",
            "Generalized Anxiety Disorder (GAD)",

        ],
        "side_effects": [
            "",
            "",
        ],
        "info": [

        ],
        "metabolism": [

        ],
        "half_life": (
            ""
        ),
    },
    "Vortioxetine": {
        "brand_names": ["Trintellix", "Brintellix"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin Modulator or Stimulant (SMS)",

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
        "half_life": (
            ""
        ),
    },
    "Vilazodone": {
        "brand_names": ["Viibryd"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin Partial Agonist and Reuptake Inhibitor (SPARI)",
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
        "half_life": (
            ""
        ),
    },
    "Nefazodone": {
        "brand_names": ["Serzone"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin-Norepinephrine-Dopamine Reuptake Inhibitor (SNDRI)",
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
        "half_life": (
            ""
        ),
    },
    "Levomilnacipran": {
        "brand_names": ["Fetzima"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
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
        "half_life": (
            ""
        ),
    },
    "Milnacipran": {
        "brand_names": ["Ixel","Savella","Milnaneurax"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin Norepinephrine Reuptake Inhibitor (SNRI)",
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
        "half_life": (
            ""
        ),
    },
    "Dextromethorphan-bupropion": {
        "brand_names": ["Auvelity"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin-Norepinephrine-Dopamine Reuptake Inhibitor (SNDRI)",
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
        "half_life": (
            ""
        ),
    },
    "Toludesvenlaxine": {
        "brand_names": ["Ruoxinlin"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Serotonin-Norepinephrine-Dopamine Reuptake Inhibitors (SNDRI)",
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
        "half_life": (
            ""
        ),
    },
    "Reboxetine": {
        "brand_names": ["Edronax"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Norepinephrine Reuptake Inhibitors (NRI)",
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
        "half_life": (
            ""
        ),
    },
    "Teniloxazine": {
        "brand_names": ["Lucelan","Metatone"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Norepinephrine Reuptake Inhibitor (NRI)",
        "info": [
            "Teniloxazine is a Japanese norepinephrine reuptake inhibitor (NRI). "
            "It has mild inhibition of serotonin and dopamine reuptake, and also "
            "acts as a 5-HT2A receptor antagonist. It has antidepressant properties "
            "as well as antihypoxic and anti-amnestic properties, without strong "
            "anticholinergic, sedative or cardiovascular side effects. "
        ],
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
        "half_life": (
            ""
        ),
    },
    "Viloxazine": {
        "brand_names": ["Qelbree","Vivalan"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Norepinephrine Reuptake Inhibitors (NRI)",
        "info": [
            "Viloxazine was originally developed as an antidepressant, and "
            "was marketed as such for almost 30 years. Presently (as of 2026), it is "
            "used for the treatment of Attention-Deficit/Hyperactivity Disorder (ADHD). "
            "It is a Norepinephrine Reuptake Inhibitor (NRI). "
        ],
        "conditions": [
            "Attention-Deficit/Hyperactivity Disorder (ADHD)",
            "Depression"

        ],
        "off_label_uses": [
            "",
            ""
        ],
        "side_effects": [
            "Insomnia",
            "Headache",
            ""
        ],
        "metabolism":[
            "CYP34A"   
        ],
        "interactions": [
            "Phenytoin",
            "Theophylline"
        ],
        "half_life": (
            "Viloxazine has a half life of about 2 to 7 hours."
        ),
    },
    "Atomoxetine": {
        "brand_names": ["Strattera"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Norepinephrine Reuptake Inhibitor (NRI)",
        "conditions": [
            "Attention-Deficit/Hyperactivity Disorder",

        ],
        "off_label_uses": [
            "Generalized Anxiety Disorder",
            "Anxiety"
        ],
        "side_effects": [
            "",
            "",
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
        "class": "Tricyclic Antidepressants",
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
    "Amoxapine": {
        "brand_names": ["Asendin"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressants",
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

        "half_life": (
            ""
        ),
    },
    "Clomipramine": {
        "brand_names": ["Anafril"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressants",
        "conditions": [
            "Obsessive-Compulsive Disorder (OCD)",

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
    "Desipramine": {
        "brand_names": ["Norpramine","Petrofrane"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressants",
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
        "half_life": (
            ""
        ),
    },
    "Dibenzepin": {
        "brand_names": ["Noveril","Victoril"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressants",
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
        "half_life": (
            ""
        ),
    },
    "Dimetacrine": {
        "brand_names": ["Istonil"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressants",
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
        "half_life": (
            ""
        ),
    },
    "Dosulepin": {
        "brand_names": ["Prothiaden"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressants",
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
        "Doxepin": {
        "brand_names": ["Adapin","Sinequan"],
        "categories": ["Antidepressants"],
        "specialties": ["Psychiatry"],
        "class": "Tricyclic Antidepressant",
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
    # TODO: Add more medications here.
}
# Normalize older entries and ensure every medication has editable info sections.
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

def find_drug(question):
    """Find a generic or brand name mentioned in the question."""

    question_lower = question.lower()
    possible_names = []

    for generic_name, info in DRUGS.items():
        possible_names.append((generic_name, generic_name))

        for brand_name in info.get("brand_names", []):
            possible_names.append((brand_name, generic_name))

    # Check longer names first.
    possible_names.sort(key=lambda pair: len(pair[0]), reverse=True)

    for name, generic_name in possible_names:
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


def show_description(generic_name, info):
    """Display a short description for a medication."""
    print(f"\n{generic_name.title()}")

    description = info.get("description") or (
        "No description has been added yet. Add a 'description' field "
        "to this medication's entry in DRUGS."
    )
    print(description)


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

    if not enzymes:
        print("No metabolism information has been added yet.")
        return

    for enzyme in enzymes:
        count = 0
        other_drugs = []

        for other_name, other_info in DRUGS.items():
            if other_name.lower() == generic_name.lower():
                continue

        other_enzymes = other_info.get("metabolism", [])

        if isinstance(other_enzymes, str):
            other_enzymes = [other_enzymes]

        if any(
            enzyme.lower() == other_enzyme.lower()
            for other_enzyme in other_enzymes
        ):
            count += 1 
            other_drugs.append(other_name.title())

    print(f"\nEnzyme:{enzyme}")
    print(
        f"This medication shares {enzyme} with "
        f"{count} other medication(s) in the database."
    )

    if other_drugs:
        print("Other medications listed:")
        for drug in sorted(other_drugs):
            print(f"- {drug}")

    

def answer_question(question, last_drug=None):
    """Answer a focused question and remember the most recently identified drug."""
    generic_name, info = find_drug(question)

    if generic_name is None and last_drug in DRUGS:
        generic_name = last_drug
        info = DRUGS[generic_name]

    if generic_name is None:
        print(
            "\nI couldn't identify a medication. Include a name such as "
            "'Prozac' or 'fluoxetine', or name a medication first and then "
            "ask a follow-up question."
        )
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

    elif any(term in question_lower for term in [
        "tell me about", "full profile", "everything about",
        "give me information", "information about"
    ]):
        show_full_profile(generic_name, info)

    elif question_lower.strip() in {
        generic_name.lower(),
        *[brand.lower() for brand in info.get("brand_names", [])],
    }:
        show_full_profile(generic_name, info)


    else:
        print(f"\nI found {generic_name.title()} in the database.")
        print("Ask about side effects, conditions, class, half-life,")
        print("brand names, specialties, or say 'what is' for a short description.")

    return generic_name


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


def list_drugs_for_condition(condition_name):
    """Search listed approved-condition fields and off-label-use fields."""
    requested = normalize_text(condition_name)
    found = []
    for drug_name, info in DRUGS.items():
        terms = []
        for field in ("conditions", "off_label_uses"):
            values = info.get(field, [])
            if isinstance(values, str):
                values = [values]
            terms.extend(v for v in values if isinstance(v, str) and v.strip())
        if any(requested in normalize_text(term) or normalize_text(term) in requested
               for term in terms):
            found.append((drug_name, info))

    print(f"\nMedications listed for '{condition_name}':")
    if not found:
        print("No matches found in the current database.")
        print("This only searches information entered here; it does not mean no medications treat the condition.")
        return
    for drug_name, info in sorted(found):
        print(f"- {drug_name.title()}")
        print(f"  Class: {info.get('class') or 'Not added'}")
        categories = info.get("categories", [])
        if isinstance(categories, str):
            categories = [categories]
        print(f"  Categories: {', '.join(categories) if categories else 'Not added'}")


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
    print("- list drugs that treat depression")
    print("- list drugs for OCD")
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
        elif normalized.startswith("list category:"):
            list_category(question.split(":", 1)[1])
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
            # e.g. list antidepressants or list antipsychotics
            list_category(question[5:].strip())
        else:
            last_drug = answer_question(question, last_drug)


if __name__ == "__main__":
    main()
