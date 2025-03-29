import streamlit as st

# Image path
TELEMEDICINE_PATH = "assets\image10.jpg"

# Trusted Gynecologists Directory
GYNECOLOGISTS_BY_STATE = {
    "Lagos State": [
        {"name": "Dr. Nkem", "hospital": "Kings Hospital"},
        {"name": "Dr. Sa'eedah Badmus", "hospital": "Madaniyah Women's Specialist Hospital"},
        {"name": "Dr. Kingsley Obodo", "hospital": "St. Ives Hospital"},
        {"name": "Dr. Umeh", "hospital": "Encee Medical Centre"},
        {"name": "Prof. Bose Afolabi", "hospital": "Breast & Gynecologist Center"},
        {"name": "Dr. Ajayi", "hospital": "Lagoon Hospital"},
        {"name": "Dr. Nwokoma", "hospital": "Kalon Specialist Hospital"},
        {"name": "Dr. Omishakin", "hospital": "PF Medical Centre"},
        {"name": "Dr. Prasad", "hospital": "Vedic Life Care"},
        {"name": "Dr. Tosin Korede", "hospital": "Standard Life Care Hospital"},
        {"name": "Dr. Kolawole", "hospital": "LASUTH"},
        {"name": "Dr. Stephen Amalokwu", "hospital": "St. Stephen Medical Center"},
        {"name": "Dr. Akinola", "hospital": "Royan Hospital"},
        {"name": "Dr. Olanrewaju", "hospital": "Mother and Child Hospitals"},
        {"name": "Dr. Adeleke Kaka", "hospital": "Fad Specialist Hospital"},
    ],
    "Rivers State": [
        {"name": "Dr. Grace Amadi", "hospital": "Rivers State University Teaching Hospital"},
        {"name": "Dr. Chike Uzoma", "hospital": "Braithwaite Memorial Specialist Hospital"},
        {"name": "Dr. Adaobi Nwokedi", "hospital": "Hope Women’s Medical Centre"},
        {"name": "Dr. Bright Akpan", "hospital": "Fertility Care Specialist Clinic"},
        {"name": "Dr. Chinedu Obi", "hospital": "Lifespring Women’s Specialist Hospital"},
    ],
    "Kaduna State": [
        {"name": "Dr. Ibrahim Abdullahi", "hospital": "Ahmadu Bello University Teaching Hospital"},
        {"name": "Dr. Sani Mustapha", "hospital": "Kaduna State Specialist Hospital"},
        {"name": "Dr. Amina Suleiman", "hospital": "Hope Women’s Care Centre"},
        {"name": "Dr. Yusuf Bala", "hospital": "Fertility and Women’s Clinic"},
        {"name": "Dr. Halima Mohammed", "hospital": "Lifespring Women’s Medical Centre"},
    ],
    "Imo State": [
        {"name": "Dr. Kelvin Obiano", "hospital": "Imo State University Teaching Hospital"},
        {"name": "Dr. Chidimma Okoro", "hospital": "Federal Medical Centre"},
        {"name": "Dr. Nnenna Ugochukwu", "hospital": "Hope Fertility and Women’s Centre"},
        {"name": "Dr. Chinonye Eze", "hospital": "Lifespring Women’s Specialist Hospital"},
        {"name": "Dr. Emmanuel Ibekwe", "hospital": "Divine Grace Women’s Clinic"},
    ],
    "Kano State": [
        {"name": "Dr. Abdullahi Garba", "hospital": "Kano State Teaching Hospital"},
        {"name": "Dr. Aminu Sani", "hospital": "Murtala Mohammed Specialist Hospital"},
        {"name": "Dr. Hauwa Yusuf", "hospital": "Fertility and Women’s Care Centre"},
        {"name": "Dr. Bashir Usman", "hospital": "Hope Women’s Specialist Hospital"},
        {"name": "Dr. Zainab Abubakar", "hospital": "Lifespring Medical Centre"},
    ],
    "Oyo State": [
        {"name": "Dr. Kehinde Kupolati", "hospital": "Iye Hospital"},
        {"name": "Dr. Samuel Akindele", "hospital": "Adeoyo Maternity Hospital"},
        {"name": "Dr. Tolulope Adekunle", "hospital": "UCH Ibadan"},
        {"name": "Dr. Oladimeji Ojo", "hospital": "Baptist Medical Centre"},
        {"name": "Dr. Akintunde Adebayo", "hospital": "Wellcare Hospitals"},
    ],
    "Abuja (FCT)": [
        {"name": "Dr. Ifeanyi Osineme", "hospital": "Green Pastures Specialist Hospital"},
        {"name": "Dr. Ibrahim Olowu", "hospital": "Cedarcrest Hospitals"},
        {"name": "Dr. Chinelo Adaji", "hospital": "Federal Medical Centre"},
        {"name": "Dr. Chioma Obasi", "hospital": "National Hospital"},
        {"name": "Dr. Andrew Ibe", "hospital": "National Hospital Abuja"},
    ],
    "Ekiti State": [
        {"name": "Dr. Funmi Aluko", "hospital": "Healing Touch Hospital"},
        {"name": "Dr. Tunde Ogunlana", "hospital": "Ekiti State University Teaching Hospital"},
        {"name": "Dr. Femi Ajayi", "hospital": "God's Care Specialist Hospital"},
        {"name": "Dr. Biodun Ojo", "hospital": "Hope Alive Hospital"},
        {"name": "Dr. Mercy Adigun", "hospital": "Specialist Women's Clinic"},
    ],
    "Cross River State": [
        {"name": "Dr. Nathan Akpan", "hospital": "University of Calabar Teaching Hospital"},
        {"name": "Dr. Iniobong Effiong", "hospital": "Fountain of Hope Specialist Clinic"},
        {"name": "Dr. Chinedu Okoro", "hospital": "Calabar Women's Medical Centre"},
        {"name": "Dr. Blessing Ita", "hospital": "Divine Grace Women’s Clinic"},
        {"name": "Dr. Victor Bassey", "hospital": "Hope and Care Fertility Centre"},
    ],
    "Akwa Ibom State": [
        {"name": "Dr. Blessing Okoro", "hospital": "University of Uyo Teaching Hospital"},
        {"name": "Dr. Sunday Umoh", "hospital": "Fertility and Women’s Care Centre"},
        {"name": "Dr. Iniobong Akpan", "hospital": "Hope Women’s Specialist Hospital"},
        {"name": "Dr. Eno Ekong", "hospital": "Lifespring Medical Centre"},
        {"name": "Dr. Emmanuel Essien", "hospital": "Divine Grace Women’s Clinic"},
    ],
}

# Define the Streamlit app
def main():
    st.set_page_config(
        page_title="CycleCare AI - Telemedicine",
        layout="wide",
    )

    st.subheader("Telemedicine")
    
    try:
        st.image(TELEMEDICINE_PATH, width=500)
    except FileNotFoundError:
        st.warning("Telemedicine image not found. Please check the path.")

    # Move Telemedicine Options to the sidebar
    st.sidebar.header("Telemedicine Options")
    sub_option = st.sidebar.radio(
        "Choose an option:", ["Gynecologists Directory", "Laboratories", "Pharmacies", "PCOS Drugs"]
    )

    if sub_option == "Gynecologists Directory":
        selected_state = st.selectbox("Select a state:", list(GYNECOLOGISTS_BY_STATE.keys()))
        doctors = GYNECOLOGISTS_BY_STATE.get(selected_state, [])
        st.write(f"### Trusted Gynecologists in {selected_state}:")
        for doctor in doctors:
            st.write(f"- **{doctor['name']}** at {doctor['hospital']}")
    
    elif sub_option == "Laboratories":
        st.write("### Laboratories in Nigeria")
        st.write("""
        - **Synlab Nigeria**: Synlab offers a range of diagnostic tests and has multiple locations across Nigeria. [Visit Synlab](https://www.synlab.com.ng/)
        - **Clina-Lancet Laboratories**: Provides comprehensive diagnostic services and laboratory tests. [Visit Clina-Lancet](https://www.lancet.com.ng/)
        - **Union Diagnostic and Clinical Services Plc**: Offers diagnostic and clinical laboratory services. [Visit Union Diagnostic](https://www.uniondiagnostic.com.ng/)
        - **PathCare Laboratories**: Specializes in pathology and laboratory medicine. [Visit PathCare](https://www.pathcarenigeria.com/)
        - **Medbury Medical Services**: Provides various medical and laboratory services. [Visit Medbury](https://www.medburyltd.com/)
        """)

    elif sub_option == "Pharmacies":
        st.write("### Pharmacies in Nigeria")
        st.write("""
        - **HealthPlus Pharmacy**: One of Nigeria's leading pharmacy chains. [Visit HealthPlus](https://www.healthplus.com.ng/)
        - **MedPlus Pharmacy**: Offers a wide range of pharmaceutical products and services. [Visit MedPlus](https://www.medplusnig.com/)
        - **Mopheth Pharmacy**: Provides pharmacy services and health consultations. [Visit Mopheth](https://www.mophethgroup.com/)
        - **Jumia Pharmacy**: Online pharmacy service providing a variety of medications. [Visit Jumia Pharmacy](https://www.jumia.com.ng/pharmacy/)
        - **NetPharmacy**: Online pharmacy offering prescription and over-the-counter medications. [Visit NetPharmacy](https://www.netpharmacy.com.ng/)
        """)

    elif sub_option == "PCOS Drugs":
        st.write("### PCOS Drugs")
        st.write("""
        - **Metformin**: Commonly prescribed to manage insulin resistance in women with PCOS.
        - **Clomiphene Citrate**: Used to stimulate ovulation in women who have difficulty becoming pregnant due to PCOS.
        - **Letrozole**: Another medication used to induce ovulation.
        - **Spironolactone**: Helps manage symptoms like acne and excessive hair growth.
        - **Oral Contraceptives**: Used to regulate menstrual cycles and manage hormone levels.
        - **Eflornithine**: Topical cream used to reduce facial hair growth.
        - **Gonadotropins**: Injectable hormones used to stimulate ovulation.
        """)

if __name__ == "__main__":
    main()