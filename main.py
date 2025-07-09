import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv
import textwrap
import io

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def main():
    st.set_page_config(page_title="X Post Generator", page_icon="✖️", layout="wide")
    
    st.title("✖️ X Post Generator with Gemini")
    st.markdown("Upload an image and get a compelling X (Twitter) post generated for it")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("Settings")
        tone = st.selectbox(
            "Select tone",
            ["Casual", "Professional", "Funny", "Inspirational", "Provocative"],
            index=0
        )
        include_hashtags = st.checkbox("Include hashtags", value=True)
        include_emoji = st.checkbox("Include emoji", value=True)
        max_chars = st.slider("Max characters", 100, 280, 250)
    
    # Main content area
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Upload Your Image")
        uploaded_file = st.file_uploader(
            "Choose an image...", 
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=False,
            label_visibility="collapsed"
        )
        
        # New text input for image description
        image_description = st.text_area(
            "What's in this image? (Optional but recommended)",
            help="Describe what's in the image to help generate a more accurate post",
            height=100
        )
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Generate Post", type="primary"):
                with st.spinner("Generating post..."):
                    try:
                        # Prepare the prompt
                        prompt_parts = [
                            f"Generate a compelling Twitter (X) post for this image in a {tone.lower()} tone.",
                            "The post should be engaging and appropriate for the platform.",
                            f"Maximum {max_chars} characters.",
                            "Include relevant hashtags." if include_hashtags else "Do not include hashtags.",
                            "Use emojis where appropriate." if include_emoji else "Do not use emojis.",
                        ]
                        
                        # Add user description if provided
                        if image_description:
                            prompt_parts.append(f"User provided this description of the image: {image_description}")
                        else:
                            prompt_parts.append("The image shows:")
                        
                        # Generate the content
                        response = model.generate_content(["\n".join(prompt_parts), image])
                        
                        if response.text:
                            # Display the generated post
                            with col2:
                                st.subheader("Generated Post")
                                st.text_area(
                                    "Post Content",
                                    value=response.text,
                                    height=200,
                                    key="generated_post"
                                )
                                
                                # Character count
                                char_count = len(response.text)
                                color = "green" if char_count <= 280 else "red"
                                st.markdown(f"<p style='color:{color}'>Characters: {char_count}/280</p>", 
                                           unsafe_allow_html=True)
                                
                                # Copy button
                                if st.button("Copy to Clipboard"):
                                    st.session_state.generated_post = response.text
                                    st.toast("Post copied to clipboard!", icon="✓")
                                
                                # Download button
                                st.download_button(
                                    label="Download as Text",
                                    data=response.text,
                                    file_name="x_post.txt",
                                    mime="text/plain"
                                )
                                
                                # Regenerate button with current settings
                                if st.button("Regenerate with Same Settings"):
                                    st.rerun()
                        else:
                            st.error("No response generated from Gemini")
                            
                    except Exception as e:
                        st.error(f"Error generating post: {str(e)}")

if __name__ == "__main__":
    main()
