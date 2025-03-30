import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage


# Debug: Check what st.secrets contains
st.write("Loaded secrets:", st.secrets)

# Fetch API key solely from Streamlit secrets
openai_api_key = st.secrets["openai"].get("api_key")
if not openai_api_key:
    st.error("API key not found in st.secrets. Please add it to your secrets.toml.")
    st.stop()  # Stop execution if key is missing

# Initialize the language model using the API key from secrets
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_api_key)

# Define the prompt template
prompt_template = ChatPromptTemplate.from_template(
    """
    You are Ada, a helpful health and lifestyle coach specializing in nutrition, exercise, and stress management for PCOS.
    Use the context below to answer user queries. If the context is insufficient, provide general advice.
    Please answer in {lang}.

    Context:
    {context}

    Question: {input}
    """
)

# Define language options for translation
language_options = {
    "English": "English",
    "Yoruba": "Yoruba",
    "Igbo": "Igbo",
    "Hausa": "Hausa"
}

def main():
    st.set_page_config(
        page_title="CycleCare AI - Comprehensive PCOS Management",
        layout="wide",
    )
    
    st.title("CycleCare AI - Comprehensive PCOS Management")
    st.markdown(
        "<h2 style='color: #070F2B; font-family: Helvetica;'>Your Personalized PCOS Companion</h2>",
        unsafe_allow_html=True,
    )

    # Directly display the Ask Ada section without a sidebar or menu
    st.subheader("Ask Ada - Your PCOS Companion")
    
    # Display the main image at the top
    try:
        st.image("./assets/Untitled_design.png", width=800)
    except FileNotFoundError:
        st.warning("Main image not found. Please check the path.")
    
    st.markdown(
        "<h2 style='color: #070F2B; font-family: Helvetica;'>Hi, I'm Ada, your PCOS Expert!</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='font-size: 16px; font-family: Arial; color: #070F2B;'>"
        "I'm here to guide you in understanding and managing PCOS effectively. "
        "Whether it's about symptoms, treatments, lifestyle changes, or anything else, feel free to ask your questions. "
        "Together, we can navigate the journey to better health and well-being."
        "</p>",
        unsafe_allow_html=True,
    )

    # Initialize session state for storing past responses
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Language selection for translation
    st.subheader("Choose Your Language")
    selected_language = st.selectbox("Choose a language:", list(language_options.keys()))
    
    # Input for user queries
    user_input = st.text_input("💡 Curious about PCOS? Ask Ada!")
    
    if st.button("Submit"):
        if user_input.strip():
            context = "PCOS-specific health advice, including nutrition, exercise, and stress management."
            formatted_prompt = prompt_template.format(
                context=context,
                input=user_input,
                lang=language_options[selected_language]
            )
            try:
                with st.spinner("Ada is thinking..."):
                    response_text = llm.predict(formatted_prompt)
                    
                    # Save the question and response to chat history
                    st.session_state.chat_history.append({
                        "question": user_input,
                        "response": response_text,
                        "language": selected_language
                    })
                    
                    # Display the current response
                    st.markdown(f"### Ada's Response ({selected_language}):\n\n{response_text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a question to receive advice.")

    # Display past responses
    if st.session_state.chat_history:
        st.subheader("Past Conversations")
        for i, chat in enumerate(st.session_state.chat_history):
            st.markdown(f"**Q{i+1}:** {chat['question']}")
            st.markdown(f"**Ada's Response ({chat['language']}):** {chat['response']}")
            st.markdown("---")

if __name__ == "__main__":
    main()
