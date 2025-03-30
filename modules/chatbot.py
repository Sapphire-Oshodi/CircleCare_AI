import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage

# Set page configuration as the very first Streamlit command
st.set_page_config(
    page_title="CycleCare AI - Comprehensive PCOS Management",
    layout="wide",
)

# Create three tabs: one for API Key input, one for Chat with Ada, and one for API Request.
tabs = st.tabs(["API Key", "Chat with Ada", "API Request"])

# ---- Tab 1: API Key Input ----
with tabs[0]:
    st.header("Enter Your OpenAI API Key")
    # Use a text input with type password to keep the key hidden
    user_api_key = st.text_input("API Key", type="password", placeholder="sk-...")
    if user_api_key:
        st.session_state["api_key"] = user_api_key
        st.success("API Key saved! Please proceed to the other tabs.")
    else:
        st.warning("Please enter your API key to proceed.")

# Stop further execution if the API key is not provided
if "api_key" not in st.session_state:
    st.stop()

# Retrieve the API key from session state
api_key = st.session_state["api_key"]

# Initialize the language model using the API key provided by the user
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=api_key)

# Define the prompt template for the Chat with Ada functionality
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

# ---- Tab 2: Chat with Ada ----
with tabs[1]:
    st.title("CycleCare AI - Comprehensive PCOS Management")
    st.markdown(
        "<h2 style='color: #070F2B; font-family: Helvetica;'>Your Personalized PCOS Companion</h2>",
        unsafe_allow_html=True,
    )
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
    
    # Initialize session state for storing past chat responses
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    st.subheader("Choose Your Language")
    selected_language = st.selectbox("Choose a language:", list(language_options.keys()))
    
    # Input for user queries
    user_input = st.text_input("💡 Curious about PCOS? Ask Ada!")
    
    if st.button("Submit", key="chat_submit"):
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
                st.session_state.chat_history.append({
                    "question": user_input,
                    "response": response_text,
                    "language": selected_language
                })
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

# ---- Tab 3: Custom API Request ----
with tabs[2]:
    st.title("Custom API Request")
    st.markdown("Enter your custom API request below and press **Submit API Request** to get a response from the model.")
    
    # Use a text area for longer custom input
    api_request = st.text_area("API Request", placeholder="Type your custom API request here...")
    
    if st.button("Submit API Request", key="api_submit"):
        if api_request.strip():
            try:
                with st.spinner("Sending API request..."):
                    custom_response = llm.predict(api_request)
                st.markdown("### API Response:")
                st.markdown(custom_response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter an API request to proceed.")
