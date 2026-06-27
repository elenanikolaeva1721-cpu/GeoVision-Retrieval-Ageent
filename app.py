import streamlit as st
from PIL import Image
from agent import GeoVisionAgent
# REMOVED: from google.colab import files <-- This was causing the ModuleNotFoundError

agent = GeoVisionAgent()

st.set_page_config(
    page_title="GeoVision Retrieval Agent",
    page_icon="🛰",
    layout="wide"
)
st.set_page_config(
    page_title="GeoVision Retrieval Agent",
    page_icon="🛰",
    layout="wide"
)

# --- ADD THIS BLOCK TO REMOVE TOP PADDING ---
st.markdown(
    """
    <style>
         /* Target the main content container padding */
         .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
         }
         /* Target the header/gap spacer above the content */
         header {
            visibility: hidden;
         }
    </style>
    """,
    unsafe_allow_html=True
)
# --------------------------------------------

st.title("🌍 GeoVision Retrieval Agent")


st.caption(
    "AI-powered retrieval of similar Earth observation scenes"
)

st.info("""
The agent compares your image with a reference database of Earth observation scenes
and returns the most similar regions.
""")

st.subheader("Analyze a Satellite Scene")

# FIXED: Uncommented and properly assigned the file uploader widget
uploaded = st.file_uploader(
    " ",
    type=["jpg", "jpeg", "png"]
)

with st.sidebar:
    # Quick Note: In newer Streamlit versions, use_container_width is standard
    st.image("GeoVision_banner.jpg", use_container_width=True)
    st.header("How it works")

    st.write(
        """
        1. Upload a satellite image in JPG or PNG format
        2. The agent extracts visual features
        3. Similar Earth observation scenes are retrieved
        4. Results are analyzed and explained
        """
    )
 
# This will now work perfectly because 'uploaded' is defined above!
if uploaded:
    img = Image.open(uploaded)
    img = img.convert("RGB")

    # Display the uploaded image on the left side of the split layout
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Your Uploaded Scene")
        st.image(img, use_container_width=True)

    results = agent.query(img)
    analysis = agent.interpret_results(results)
    
    with col2:
        st.subheader("AI Interpretation")
        st.metric("Most Likely Scene", analysis["prediction"])
        st.metric("Confidence", analysis["confidence"])
        # Format score safely as a string or float depending on your agent's output
        st.metric("Similarity score", f"{analysis['score']:.3f}" if isinstance(analysis['score'], (int, float)) else analysis['score'])
        st.write("**Summary**")
       
    st.subheader("Top Similar Scenes")
    
    # Created 5 columns to match your loop layout beautifully
    cols = st.columns(5)
    for i, r in enumerate(results):
        # Distribute the results evenly across the 5 columns
        with cols[i % 5]:
            st.write(f"**{r['label']}**")
            st.caption(f"Similarity: {r['score']:.3f}")
            st.image(r["path"], use_container_width=True)