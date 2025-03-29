import streamlit as st

# Image paths
COMMUNITY_SUPPORT_IMAGE_PATH = "assets\image2.jpg"

# Community & Support groups
SUPPORT_GROUPS = """
### Local PCOS Support Groups You Can Join in Nigeria

- **Cysters Advocate**: [Join WhatsApp Group](https://chat.whatsapp.com/F9mezTC19kFFajwjGneSGb)  
- **That.PCOS.Chick**: [Follow on Instagram](https://www.instagram.com/that.pcos.chick?igsh=MXNqdWQ5cW9ybXI2cQ==)  
- **PCOS Conquerors**: [Follow on Instagram](https://www.instagram.com/pcosconquerors?igsh=cnphY3l0eWdicDBp)  
- **The Fit Priest** (aka Selema ‘That’ PCOS Babe): [Follow on Instagram](https://www.instagram.com/thefitpriest?igsh=bHY0YjFodGd5dXoz) 
- **PCOS Awareness Association**: [Visit Official Website](https://www.pcosaa.org/)
"""

# Define the Streamlit app
def main():
    st.set_page_config(
        page_title="CycleCare AI - Community & Support",
        layout="wide",
    )

    # Community & Support Section
    st.subheader("Community & Support")
    st.image(COMMUNITY_SUPPORT_IMAGE_PATH, width=600, caption="Connecting the PCOS Community")
    st.markdown(SUPPORT_GROUPS, unsafe_allow_html=True)

    st.markdown("### Monitoring and Follow-Up")
    st.markdown("Regular monitoring and follow-up tests are crucial for managing PCOS effectively. Your healthcare provider will determine the appropriate tests and frequency based on your individual needs.")
    st.markdown("Always consult with a healthcare professional to determine the appropriate tests for your specific situation.")

if __name__ == "__main__":
    main()