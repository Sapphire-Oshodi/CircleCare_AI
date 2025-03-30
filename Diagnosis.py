import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import gdown

def calculate_risk(answers):
    criteria_met = sum(answers[:3]) >= 1, sum(answers[3:6]) >= 1, sum(answers[6:8]) >= 1
    criteria_count = sum(criteria_met)
    
    if criteria_count == 0:
        return "Low Risk", "#4CAF50"
    elif criteria_count == 1:
        return "Moderate Risk", "#FF9800"
    else:
        return "High Risk", "#F44336"

# Set page config
st.set_page_config(page_title="PCOS Self-Assessment", page_icon="🌸", layout="centered")

# Load the trained model for clinical diagnosis
clinical_model_path = "pcos_diagnosis_pipeline.pkl"
if os.path.exists(clinical_model_path):
    clinical_model = joblib.load(clinical_model_path)
else:
    clinical_model = None
    st.error(f"Clinical diagnosis model file '{clinical_model_path}' not found. Please upload the file.")

# Download the trained model for medical imaging diagnosis from Google Drive
@st.cache_resource
def load_trained_model():
    model_path = 'Pcos_Scan_model.h5'
    if not os.path.exists(model_path):
        url = 'https://drive.google.com/uc?id=1UTBOUNtIzhAtCRDzI5D7TnsGMHsY43D-'
        gdown.download(url, model_path, quiet=False)
    return load_model(model_path)

imaging_model = load_trained_model()

# Custom CSS for styling
st.markdown("""
    <style>
        body {background-color: #f5f5f5; font-family: Arial, sans-serif;}
        .stButton>button {background-color: #6200ea; color: white; padding: 10px 20px; font-size: 18px; border-radius: 8px;}
        .stRadio > label {font-size: 18px;}
        .result-box {border-radius: 10px; padding: 20px; text-align: center; font-size: 20px; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# Sidebar with logo and navigation
st.sidebar.image("Cycleec.png")
options = st.sidebar.radio(
    "Choose a section:",
    [
        "Symptom Tracker",
        "Clinical Diagnosis",
        "🩺 Medical Imaging Diagnosis"
    ]
)

# Symptom Tracker section
if options == "Symptom Tracker":
    st.header("🌸 PCOS Self-Assessment Quiz 🌸")
    image_path = "Young Person Engaging With Telemedicine App In Healthcare Setting.png"
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.error(f"Image file '{image_path}' not found. Please upload the file.")
    st.markdown("""
    Welcome to the **PCOS Symptoms and Diagnosis Tool**! 
    This tool is designed for both patients and healthcare professionals to assess the likelihood of PCOS.
    Please answer the questions carefully. Your privacy is respected, and the data is not saved.
    """)
    
    st.sidebar.image("hal-gatewood-OgvqXGL7XO4-unsplash.jpg")

    questions = [
        # Ovulatory dysfunction
        ("Do you have irregular or missed periods (fewer than 9 per year)?", "Irregular periods are a common sign of ovulatory dysfunction."),
        ("Have you gone more than 35 days without a period?", "Long cycles may indicate hormonal imbalances."),
        ("Do you often experience very light or very heavy periods?", "Extreme variations in period flow can be a sign of ovulatory issues."),
        # Hyperandrogenism
        ("Do you have excessive hair growth on your face, chest, or back?", "Hirsutism is a key indicator of high androgen levels."),
        ("Have you noticed persistent acne or very oily skin?", "High androgen levels can cause persistent acne and oiliness."),
        ("Do you experience significant hair thinning or hair loss on your scalp?", "Male-pattern baldness or thinning hair may suggest hormonal imbalance."),
        # Polycystic Ovaries
        ("Have you been diagnosed with polycystic ovaries on an ultrasound?", "Polycystic ovaries are a diagnostic factor for PCOS."),
        ("Have you ever been diagnosed with ovarian cysts?", "Ovarian cysts can contribute to PCOS symptoms."),
        # Additional symptoms
        ("Do you have unexplained weight gain or difficulty losing weight?", "Insulin resistance can lead to weight gain in PCOS."),
        ("Do you feel unusually fatigued or low on energy?", "Hormonal imbalances can cause fatigue."),
        ("Do you have darkened patches of skin (e.g., on your neck, armpits, or groin)?", "Acanthosis nigricans is often linked to insulin resistance.")
    ]

    answers = []
    st.markdown("### Answer the following questions")
    with st.form("pcos_quiz"):
        for question, explanation in questions:
            response = st.radio(f"**{question}**\n*{explanation}*", ["No", "Yes"], index=0, horizontal=True)
            answers.append(1 if response == "Yes" else 0)
        submit = st.form_submit_button("Submit Assessment")

    if submit:
        risk_level, color = calculate_risk(answers)
        st.markdown(f"""
            <div class='result-box' style='background-color:{color}; color: white;'>
                Your Risk Level: {risk_level}
            </div>
        """, unsafe_allow_html=True)
        st.write("The Rotterdam Criteria require at least 2 out of 3 factors (Irregular periods, Hyperandrogenism, Polycystic ovaries) to diagnose PCOS. If you are at moderate or high risk, consider consulting a healthcare professional for further evaluation.")

# Clinical Diagnosis section
elif options == "Clinical Diagnosis":
    st.sidebar.image("doctor.webp")
    st.title("🌸 PCOS Diagnosis Tool")
    st.header("🩺 Healthcare Provider Section")
    image_path = "testalize-me-9xHsWmh3m_4-unsplash.jpg"
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.error(f"Image file '{image_path}' not found. Please upload the file.")
    st.write("This section allows healthcare providers to input patient details and receive a PCOS likelihood assessment. Please fill out the following information carefully.")

    if clinical_model is None:
        st.error("Clinical diagnosis model is not available. Please upload the 'pcos_diagnosis_pipeline.pkl' file.")
    else:
        # Section 1: General Information
        st.header("📋 General Information")
        patient_name = st.text_input("Patient's Name")
        patient_age = st.slider("Patient's Age", min_value=10, max_value=90, value=25, step=1)
        additional_notes = st.text_area("Additional Notes (Optional)")

        # Section 2: Ovulatory Dysfunction
        st.header("📅 Ovulatory Dysfunction")
        menstrual_cycle_length = st.selectbox(
            "Average Menstrual Cycle Length",
            [
                "Less than 25 days", 
                "25–34 days", 
                "35–60 days", 
                "More than 60 days", 
                "Totally variable (changes frequently)"
            ]
        )

        # Section 3: Hyperandrogenism
        st.header("🌿 Hyperandrogenism")
        excess_hair_growth = st.radio(
            "Tendency to grow dark, coarse hair?",
            ["Yes", "No"], 
            index=1
        )

        # Section 4: Ultrasound Findings
        st.header("🔬 Ultrasound Findings")
        st.write("If the patient has undergone an ultrasound, please provide the following details:")

        follicle_count = st.number_input(
            "Number of follicles seen in ultrasound", min_value=0, step=1, format="%d"
        )
        ovarian_volume = st.number_input(
            "Volume of ovaries (in cm³)", min_value=0.0, step=0.1, format="%.1f"
        )
        stroma_endometrial_status = st.radio(
            "Was there a mention of increased stroma or abnormal endometrial thickness?",
            options=["Yes", "No", "Not Sure"]
        )
        ultrasound_findings = st.multiselect(
            "Findings mentioned in ultrasound report:",
            options=[
                "A big womb", "A tilted womb", "Fibroids", "Polyps",
                "Swollen tubes", "Ovarian cysts", "Endometriosis",
                "Adenomyosis", "Adhesions", "Thickening of the lining of the womb", "None of the above"
            ]
        )

        # Section 5: Obesity
        st.header("⚖️ Obesity")
        st.write("Calculate BMI:")
        weight = st.number_input("Weight (kg):", min_value=20.0, max_value=200.0, step=0.1)
        height = st.number_input("Height (cm):", min_value=100.0, max_value=250.0, step=0.1)
        if weight and height:
            bmi = round(weight / ((height / 100) ** 2), 2)
            st.write(f"Calculated BMI: {bmi}")
        else:
            bmi = None

        # Section 6: Hormonal and Other Measurements
        st.header("🧪 Hormonal and Other Measurements")
        fasting_glucose = st.number_input("Fasting Glucose Level (mg/dL)")
        fasting_insulin = st.number_input("Fasting Insulin Level (µIU/mL)")
        lh_fsh_ratio = st.number_input("LH/FSH Ratio")
        amh = st.number_input("AMH (Anti-Müllerian Hormone) Level (ng/mL)")
        dheas = st.number_input("DHEAS (Dehydroepiandrosterone sulfate) Level (µg/dL)")
        prolactin = st.number_input("Prolactin Level (ng/mL)")
        tsh = st.number_input("TSH (Thyroid Stimulating Hormone) Level (mIU/L)")
        free_testosterone = st.number_input("Free Testosterone Level (pg/mL)")
        blood_sugar = st.number_input("Random Blood Sugar Level (mg/dL)")
        score = st.slider("Symptom Severity (1 to 10)", 1, 10)

        # Predict button
        if st.button("Predict PCOS Likelihood"):
            try:
                # Prepare the input data for the model
                input_data = pd.DataFrame([{
                    "Age": patient_age,
                    "BMI": bmi,
                    "FastingGlucose": fasting_glucose,
                    "FastingInsulin": fasting_insulin,
                    "LH_FSH_Ratio": lh_fsh_ratio,
                    "AMH": amh,
                    "DHEAS": dheas,
                    "Prolactin": prolactin,
                    "TSH": tsh,
                    "FreeTestosterone": free_testosterone,
                    "BloodSugar": blood_sugar,
                    "Score": score
                }])
                
                # Make the prediction
                probabilities = clinical_model.predict_proba(input_data)[0]
                likelihood = probabilities[1] * 100

                # Display the results
                if likelihood > 50:
                    diagnosis = "PCOS Likely"
                    st.success(f"Prediction for {patient_name or 'the patient'}: {diagnosis}")
                    st.write(f"PCOS Likelihood: {likelihood:.2f}%")
                    st.info("Based on the provided information, it is likely that the patient has PCOS. Please consult with a healthcare provider for further evaluation and confirmation.")
                else:
                    diagnosis = "PCOS Unlikely"
                    st.success(f"Prediction for {patient_name or 'the patient'}: {diagnosis}")
                    st.write(f"PCOS Likelihood: {likelihood:.2f}%")
                    st.info("Based on the provided information, it is unlikely that the patient has PCOS. Please consult with a healthcare provider for further evaluation if symptoms persist.")
                
                if additional_notes:
                    st.info(f"Additional Notes Provided: {additional_notes}")
            except ValueError as e:
                st.error(f"An error occurred: {e}. Please ensure all fields are correctly filled.")

# Medical Imaging Diagnosis section
elif options == "🩺 Medical Imaging Diagnosis":
    st.title("Welcome to the Medical Imaging Diagnosis PCOS Dashboard")
    st.image("pngwing.com (25).png")
    st.write("This app provides insights into the medical imaging analysis.")
    st.write("Upload an ultrasound image to classify it as **Infected** or **Noninfected**.")
    
    threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.5, 0.01)
    user_name = st.text_input("Enter your name:", value="Patient")
    uploaded_file = st.file_uploader("Upload an Ultrasound Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image")

        # Preprocess image
        img = img.resize((256, 256))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make predictions
        if imaging_model:
            yhat = imaging_model.predict(img_array)
            confidence = round(yhat[0][0] * 100, 1)  # Confidence rounded to 1 decimal

            # Classification
            result = "Noninfected" if yhat[0][0] >= threshold else "Infected"

            # Display results
            st.write(f"### **Result:** {result}")
            st.write(f"**Prediction Confidence:** {confidence}%")

            if result == "Noninfected":
                st.success("The ultrasound image is classified as **Noninfected**.")
                st.markdown("""
                **Clinical Insights**:
                - Normal ovarian size (<10 cm³).
                - Fewer than 12 follicles, evenly distributed.
                - Homogeneous ovarian stroma.
                - No cystic patterns detected.
                """)
            else:
                st.error("The ultrasound image is classified as **Infected**.")
                st.markdown("""
                **Clinical Insights**:
                - Increased ovarian size (>10 cm³).
                - Presence of 12+ follicles (2-9 mm) arranged peripherally.
                - "String of pearls" appearance observed.
                - Increased stromal echogenicity.
                - Potential thickened endometrium.
                """)

            # Option to download or save the result
            result_text = f"Result: {result}\nPrediction Confidence: {confidence}%"
            if result == "Noninfected":
                insights = """
                    - Normal ovarian size (<10 cm³).
                    - Fewer than 12 follicles, evenly distributed.
                    - Homogeneous ovarian stroma.
                    - No cystic patterns detected.
                """
            else:
                insights = """
                    - Increased ovarian size (>10 cm³).
                    - Presence of 12+ follicles (2-9 mm) arranged peripherally.
                    - "String of pearls" appearance observed.
                    - Increased stromal echogenicity.
                    - Potential thickened endometrium.
                """
            
            result_text += f"\n\nClinical Insights:\n{insights.strip()}"

            st.download_button(
                label="Download Result",
                data=result_text,
                file_name=f"{user_name}_PCOS_Result.txt",
                mime="text/plain",
            )

            if st.button("Save Result"):
                with open(f"{user_name}_PCOS_Result.txt", "w") as file:
                    file.write(result_text)
                st.success("Result saved successfully.")

# Footer note
st.markdown("""
**Disclaimer:** This tool is for informational purposes only and is not a substitute for professional medical advice. Please consult a healthcare provider for a definitive diagnosis.
""")
