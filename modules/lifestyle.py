import streamlit as st
import pandas as pd
import numpy as np

# Image paths
MAIN_IMAGE_PATH = "assets/Untitled_design.png"
FOOTER_IMAGE_PATH = "assets/pngwing_25.png"
FAQ_IMAGE_PATH = "assets/image3.jpg"
TRACKING_TOOLS_IMAGE_PATH = "assets/image4.jpg"
MENTAL_HEALTH_PATH = "assets/image5.jpg"
HERBAL_REMEDIES_PATH = "assets/image6.jpg"
TESTING_INFO_PATH = "assets/image7.png"
LIFESTYLE_TIPS_PATH = "assets/image9.jpg"
FOOD_RECOMMENDATIONS_PATH = "assets/image8.jpg"

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

# PCOS-related resources
PCOS_STATISTICS = """
- PCOS affects 5-10% of women of reproductive age worldwide.
- It is one of the leading causes of infertility in women.
- Up to 70% of women with PCOS may have undiagnosed symptoms.
- Women with PCOS are at a higher risk of developing type 2 diabetes, high blood pressure, and heart disease.
"""

LIFESTYLE_TIPS = """
- Include whole grains, lean proteins, and healthy fats.
- Engage in regular physical activity.
- Practice mindfulness and relaxation to manage stress.
"""

NIGERIAN_FOODS = """
- Grilled fish, boiled eggs, lean chicken, beans, and snails.
- Brown rice, unripe plantain, sweet potatoes, and yam in moderation.
- Ugu, bitter leaf, okra, spinach, and garden egg.
- Avocados, groundnuts, coconut oil, and palm kernel oil.
- Watermelon, apples, and oranges.
"""

FOREIGN_FOODS = """
- Grilled salmon, tofu, and boiled eggs.
- Quinoa, whole-grain pasta, and oats.
- Broccoli, kale, and asparagus.
- Almonds, walnuts, and olive oil.
- Blueberries, kiwi, and avocados.
"""

HEALTHY_SNACKS = """
- Nuts and seeds (almonds, walnuts, sunflower seeds)
- Greek yogurt with fresh fruit
- Sliced vegetables with hummus
- Fresh fruit (berries, apples, oranges)
- Dark chocolate (in moderation)
"""

# Tracking Tools Section Content
tracking_tools = [
    {
        "name": "Flo Period Tracker",
        "description": "Tracks menstrual cycles, ovulation, and symptoms. Offers personalized insights.",
        "link": "https://flo.health/",
    },
    {
        "name": "MyFitnessPal",
        "description": "Tracks daily food intake and fitness activities to support healthy habits.",
        "link": "https://www.myfitnesspal.com/",
    },
    {
        "name": "Clue",
        "description": "Tracks menstrual cycles and symptoms, offering predictions about ovulation and periods.",
        "link": "https://helloclue.com/",
    },
    {
        "name": "Fitbit",
        "description": "Monitors physical activity, sleep, and stress, encouraging regular exercise.",
        "link": "https://www.fitbit.com/",
    },
    {
        "name": "Headspace",
        "description": "Provides guided meditations and stress-relief techniques to enhance mental health.",
        "link": "https://www.headspace.com/",
    },
    {
        "name": "Cara Care",
        "description": "Tracks food, symptoms, and digestion to support dietary adjustments.",
        "link": "https://cara.care/",
    },
    {
        "name": "Kindara",
        "description": "Tracks fertility and basal body temperature to provide insights into hormonal health.",
        "link": "https://www.kindara.com/",
    },
    {
        "name": "PCOS Tracker App",
        "description": "Tracks PCOS-specific symptoms, medication, and lifestyle habits.",
        "link": "https://pcostrackerapp.com/",
    },
    {
        "name": "Period Diary",
        "description": "Tracks cycles, moods, and symptoms with visual trend reports.",
        "link": "https://www.perioddiary.com/",
    },
    {
        "name": "Happify",
        "description": "Focuses on emotional health and well-being through interactive activities.",
        "link": "https://www.happify.com/",
    },
]

# Define the Streamlit app
def main():
    st.set_page_config(
        page_title="CycleCare AI - Comprehensive PCOS Management",
        layout="wide",
    )

    # Sidebar for navigation
    st.sidebar.header("Menu")
    main_menu = st.sidebar.radio(
        "Choose a section:",
        [
            "Home",
            "Food Recommendations",
            "Lifestyle Tips",
            "Testing Information",
            "Herbal and Natural Remedies",
            "Mental Health Resources",
            "Tracking Tools",
            "FAQs",
        ]
    )

    # Home Section
    if main_menu == "Home":
        st.markdown(
            "<h1 style='color: #070F2B; text-align: center; font-family: Helvetica;'>CysterCare - Your PCOS Support Companion</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h4 style='color: #C14600; text-align: center; font-family: Trebuchet MS;'>Empowering Women with Knowledge and Support</h4>",
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        try:
            st.image(MAIN_IMAGE_PATH, use_container_width=True)
        except FileNotFoundError:
            st.warning("Main image not found. Please check the path.")


    # Food Recommendations Section
    elif main_menu == "Food Recommendations":
        st.subheader("Food Recommendations")
        
        try:
            st.image(FOOD_RECOMMENDATIONS_PATH, use_container_width=True)
        except FileNotFoundError:
            st.warning("Food recommendations image not found. Please check the path.")

        with st.expander("Local Food Recommendations"):
            st.markdown("""
            - **Proteins**:
                - Grilled fish
                - Boiled eggs
                - Lean chicken
                - Beans
                - Snails

            - **Carbohydrates**:
                - Brown rice
                - Unripe plantain
                - Sweet potatoes
                - Yam (in moderation)

            - **Vegetables**:
                - Ugu (pumpkin leaves)
                - Bitter leaf
                - Okra
                - Spinach
                - Garden egg

            - **Healthy Fats**:
                - Avocados
                - Groundnuts (peanuts)
                - Coconut oil
                - Palm kernel oil

            - **Fruits**:
                - Watermelon
                - Apples
                - Oranges
            """)

        with st.expander("International Food Recommendations"):
            st.markdown("""
            - **Proteins**:
                - Grilled salmon
                - Tofu
                - Boiled eggs

            - **Carbohydrates**:
                - Quinoa
                - Whole-grain pasta
                - Oats

            - **Vegetables**:
                - Broccoli
                - Kale
                - Asparagus

            - **Healthy Fats**:
                - Almonds
                - Walnuts
                - Olive oil

            - **Fruits**:
                - Blueberries
                - Kiwi
                - Avocados
            """)

        with st.expander("Healthy Snacks"):
            st.markdown("""
            - Nuts and seeds (almonds, walnuts, sunflower seeds)
            - Greek yogurt with fresh fruit
            - Sliced vegetables with hummus
            - Fresh fruit (berries, apples, oranges)
            - Dark chocolate (in moderation)
            """)

    # Lifestyle Tips Section
    elif main_menu == "Lifestyle Tips":
        st.subheader("Lifestyle Tips")

        try:
            st.image(LIFESTYLE_TIPS_PATH, use_container_width=True)
        except FileNotFoundError:
            st.warning("Lifestyle tips image not found. Please check the path.")

        with st.expander("General Lifestyle Tips"):
            st.markdown("""
            - **Diet and Nutrition**:
                - Focus on a balanced diet that includes:
                    - Whole grains: Brown rice, quinoa, whole oats, and whole-grain bread.
                    - Lean proteins: Chicken, fish, tofu, and legumes.
                    - Healthy fats: Avocados, nuts, seeds, and olive oil.
                - Avoid processed foods, sugary drinks, and excessive carbohydrates.
                - Consider a low glycemic index (GI) diet to help manage insulin levels.

            - **Exercise and Physical Activity**:
                - Aim for at least 30 minutes of moderate exercise most days of the week.
                - Include a mix of cardio exercises (like walking, swimming, or cycling) and strength training.
                - Yoga and Pilates can also help improve flexibility, reduce stress, and support hormone balance.

            - **Stress Management**:
                - Practice mindfulness and relaxation techniques such as meditation, deep breathing exercises, or progressive muscle relaxation.
                - Engage in activities that you enjoy and that help you relax, such as reading, gardening, or listening to music.
                - Ensure you get adequate sleep, aiming for 7-9 hours per night.

            - **Regular Health Check-ups**:
                - Schedule regular visits with your healthcare provider to monitor your condition.
                - Keep track of your symptoms, menstrual cycles, and any changes in your health.
            """)

    # Herbal and Natural Remedies Section
    elif main_menu == "Herbal and Natural Remedies":
        st.subheader("Herbal and Natural Remedies")
        try:
            st.image(HERBAL_REMEDIES_PATH, use_container_width=True, caption="Herbal and Natural Remedies")
        except FileNotFoundError:
            st.warning("Herbal remedies image not found. Please check the path.")

        st.markdown(
            """
            ### Herbal and Natural Remedies for PCOS

            Managing PCOS often includes exploring various herbal and natural remedies. These remedies can help alleviate symptoms and improve overall health.

            #### In Nigeria
            - **Bitter Leaf (Vernonia amygdalina)**: Known for its anti-inflammatory and antioxidant properties, bitter leaf can help reduce PCOS symptoms.
            - **Scent Leaf (Ocimum gratissimum)**: This herb is used in traditional Nigerian medicine to support reproductive health and balance hormones.
            - **Moringa (Moringa oleifera)**: Rich in vitamins and minerals, moringa can help balance hormones, reduce inflammation, and improve overall health.
            - **Turmeric (Curcuma longa)**: Turmeric's anti-inflammatory properties can help manage PCOS symptoms and improve insulin resistance.

             #### Internationally
            - **Spearmint Tea**: Drinking spearmint tea regularly can help reduce androgen levels, which may improve symptoms like hirsutism.
            - **Cinnamon (Cinnamomum verum)**: Cinnamon can help regulate menstrual cycles and improve insulin sensitivity in women with PCOS.
            - **Ashwagandha (Withania somnifera)**: Known as an adaptogen, ashwagandha can help manage stress, which is crucial for balancing hormones.
            - **Saw Palmetto (Serenoa repens)**: This herb can help reduce androgen levels and improve symptoms like acne and hair loss.

            #### Lifestyle Tips
            - **Maintain a Healthy Diet**: Focus on whole foods, including plenty of fruits, vegetables, lean proteins, and whole grains.
            - **Regular Exercise**: Engage in regular physical activity to help manage weight, improve insulin sensitivity, and reduce stress.
            - **Stress Management**: Practice mindfulness, yoga, or meditation to manage stress levels, which can have a positive impact on PCOS symptoms.

                        Consult with a healthcare professional before starting any herbal or natural remedies to ensure they are safe and appropriate for you.
            """
        )

    # Testing Information Section
    elif main_menu == "Testing Information":
        render_testing_info()

    # Tracking Tools Section
    elif main_menu == "Tracking Tools":
        st.subheader("Tracking Tools for PCOS")
        st.image(TRACKING_TOOLS_IMAGE_PATH, use_container_width=True, caption="Tracking Tools")
        for tool in tracking_tools:
            with st.expander(f"**{tool['name']}**"):
                st.write(tool["description"])
                st.markdown(f"[Learn More]({tool['link']})")

    # FAQs Section
    elif main_menu == "FAQs":
        st.subheader("FAQs")
        st.image(FAQ_IMAGE_PATH, use_container_width=True, caption="Frequently Asked Questions")
        
        # Frequently Asked Questions as dropdowns
        with st.expander("**1. How does CycleCare AI support PCOS management?**"):
            st.write(
                """
                CycleCare AI offers a holistic approach by providing tools such as symptom trackers, 
                personalized meal plans, tailored fitness programs, stress management techniques, 
                and access to telemedicine services. Additionally, the supportive community fosters 
                24/7 motivation and shared experiences.
                """
            )

        with st.expander("**2. Can I consult with healthcare professionals through CycleCare AI?**"):
            st.write(
                """
                Yes! CycleCare AI integrates telemedicine services, enabling users to consult with 
                certified healthcare professionals, including gynecologists, endocrinologists, 
                nutritionists, and fitness coaches. Personalized wellness plans are crafted to suit 
                your individual needs.
                """
            )

        with st.expander("**3. Is CycleCare AI only for women with PCOS?**"):
            st.write(
                """
                No, while CycleCare AI is designed for individuals managing PCOS, the platform is 
                beneficial for anyone seeking to improve their hormonal health, nutrition, fitness, 
                and overall well-being through expert advice and community support.
                """
            )

        with st.expander("**4. What kind of community support does CycleCare AI provide?**"):
            st.write(
                """
                CycleCare AI connects users with an engaging community where women share experiences, 
                offer peer support, and access educational resources. The community forums and support 
                groups provide a safe space for motivation, encouragement, and learning.
                """
            )

        with st.expander("**5. Does CycleCare AI include mental health support?**"):
            st.write(
                """
                Yes, CycleCare AI recognizes the importance of mental health in managing PCOS and 
                overall wellness. We provide access to mental health professionals who specialize in 
                hormonal health, stress management, and emotional well-being.
                """
            )

        # Support Groups Section
        with st.expander("**6. Are there any local PCOS support groups I can join?**"):
            st.markdown(SUPPORT_GROUPS, unsafe_allow_html=True)

    # Mental Health Resources Section
    elif main_menu == "Mental Health Resources":
        st.subheader("Mental Health Resources")
        try:
            st.image(MENTAL_HEALTH_PATH, use_container_width=True, caption="Mental Health Resources")
        except FileNotFoundError:
            st.warning("Mental health image not found. Please check the path.")

        st.markdown("### Mental Health and PCOS")
        st.markdown("Managing PCOS can be overwhelming, and it's important to take care of your mental health. Here are some resources and tips to help.")

        with st.expander("1. Mindfulness and Meditation"):
            st.markdown("""
            - **Headspace**: Offers guided meditations and mindfulness exercises to help reduce stress and improve mental clarity. [Visit Headspace](https://www.headspace.com/)
            - **Calm**: Provides meditation sessions, sleep stories, and relaxation techniques. [Visit Calm](https://www.calm.com/)
            """)

        with st.expander("2. Therapy and Counseling"):
            st.markdown("""
            - **BetterHelp**: Connects you with licensed therapists for online counseling sessions. [Visit BetterHelp](https://www.betterhelp.com/)
            - **Talkspace**: Offers online therapy with licensed therapists through text, audio, and video messages. [Visit Talkspace](https://www.talkspace.com/)
            """)

        with st.expander("3. Support Groups"):
            st.markdown("""
            Joining a support group can provide a sense of community and help you connect with others who understand what you're going through.

            - **PCOS Challenge**: Offers support groups, workshops, and educational resources for women with PCOS. [Visit PCOS Challenge](https://www.pcoschallenge.org/)
            - **SoulCysters**: An online forum where women with PCOS can share their experiences and support each other. [Visit SoulCysters](http://www.soulcysters.net/)
            """)

        with st.expander("4. Lifestyle and Self-Care"):
            st.markdown("""
            - **Exercise Regularly**: Physical activity can help reduce stress and improve mood. Aim for at least 30 minutes of moderate exercise most days of the week.
            - **Healthy Diet**: Eating a balanced diet with plenty of fruits, vegetables, lean proteins, and whole grains can support overall health and well-being.
            - **Sleep Well**: Aim for 7-9 hours of sleep each night to help your body recover and manage stress better.
            """)

        with st.expander("5. Educational Resources"):
            st.markdown("""
            - **PCOS Awareness Association**: Provides information on PCOS and mental health, along with resources to help manage symptoms. [Visit PCOS Awareness Association](https://www.pcosaa.org/)
            """)

# Define the testing information section
def render_testing_info():
    st.subheader("Testing Information")
    try:
        st.image(TESTING_INFO_PATH, use_container_width=True, caption="Testing Information for PCOS")
    except FileNotFoundError:
        st.warning("Testing information image not found. Please check the path.")

    st.markdown("### Testing Information for PCOS")
    st.markdown("Getting an accurate diagnosis and managing PCOS effectively often requires a range of medical tests. Here are some common tests for PCOS:")

    with st.expander("1. Blood Tests"):
        st.markdown("""
        - **Hormone Levels**: Tests to measure levels of androgens (male hormones) like testosterone, luteinizing hormone (LH), follicle-stimulating hormone (FSH), and estradiol.
        - **Glucose Tolerance Test**: Measures how your body processes glucose to check for insulin resistance or diabetes.
        - **Lipid Profile**: Measures cholesterol and triglyceride levels to assess heart disease risk.
        - **Thyroid Function Tests**: Checks for thyroid disorders, which can cause symptoms similar to PCOS.
        """)

    with st.expander("2. Ultrasound"):
        st.markdown("""
        - **Transvaginal Ultrasound**: Uses sound waves to create images of your ovaries and the thickness of the lining of your uterus.
        """)

    with st.expander("3. Physical Examination"):
        st.markdown("""
        - **Pelvic Exam**: A healthcare provider may perform a pelvic exam to check for any abnormalities in the reproductive organs.
        """)

    with st.expander("4. Other Tests"):
        st.markdown("""
        - **Endometrial Biopsy**: In some cases, a biopsy of the endometrial lining may be recommended to rule out endometrial cancer.
        - **Sleep Study**: If symptoms of sleep apnea are present, a sleep study may be recommended.
        """)

    st.markdown("### Monitoring and Follow-Up")
    st.markdown("Regular monitoring and follow-up tests are crucial for managing PCOS effectively. Your healthcare provider will determine the appropriate tests and frequency based on your individual needs.")
    st.markdown("Always consult with a healthcare professional to determine the appropriate tests for your specific situation.")

if __name__ == "__main__":
    main()