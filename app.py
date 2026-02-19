import streamlit as st

# Page config
st.set_page_config(
    page_title="Omaha Performing Arts - AI Concierge Demo",
    page_icon="🎭",
    layout="wide"
)

# Custom CSS for OPA branding
st.markdown("""
    <style>
    .main {
        background-color: #2B1B3D;
    }
    .stApp {
        background-color: #2B1B3D;
    }
    h1, h2, h3, p {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🎭 Omaha Performing Arts")
st.subheader("AI Concierge Demo - Meet Aria")

# Intro text
st.markdown("""
### Your Digital Usher

Aria is an AI-powered concierge designed to help visitors:
- **Discover shows** based on preferences and occasions
- **Get venue information** (parking, accessibility, policies)
- **Receive personalized recommendations** for date nights, families, or specific genres

**Try it out!** Click the chat button in the bottom right corner.

---

**Test Questions:**
- "What shows do you have coming up?"
- "I'm looking for a date night show"
- "Where should I park for the Orpheum Theater?"
- "What's good for families with kids?"
""")

# Embed Voiceflow chatbot
st.components.v1.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <script type="text/javascript">
          (function(d, t) {
              var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
              v.onload = function() {
                window.voiceflow.chat.load({
                  verify: { projectID: '698fc02dd6a662d6c77c4cdb' },
                  url: 'https://general-runtime.voiceflow.com',
                  versionID: 'production',
                  voice: {
                    url: "https://runtime-api.voiceflow.com"
                  }
                });
              }
              v.src = "https://cdn.voiceflow.com/widget-next/bundle.mjs"; 
              v.type = "text/javascript"; 
              s.parentNode.insertBefore(v, s);
          })(document, 'script');
        </script>
    </head>
    <body style="margin:0; padding:0;">
    </body>
    </html>
    """, 
    height=600,
    scrolling=False
)

# Footer
st.markdown("---")
st.markdown("*This is a prototype demonstration. Built with Streamlit & Voiceflow.*")
