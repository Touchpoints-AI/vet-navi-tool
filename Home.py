import streamlit as st

st.set_page_config(
    page_title="Veteran Health Resource Navigation Tool",
    page_icon="🎖️",
    layout="wide",
)

st.title("Veteran Health Resource Navigation Tool")

st.markdown(
    """
You just left the military. The Military Health System took care of you before. Now you have to
take care of this yourself. That's what this tool is for.

This isn't an official VA or DoD product. It walks you through the real steps you need to take.
"""
)

st.info(
    "This tool does not collect any information. It doesn't log you in, store your data, or "
    "submit anything on your behalf. Every checklist here resets when you close the tab. "
    "It's just a guide, you still take the actions yourself on the official sites it links to."
)

st.markdown("### What you'll find here")

st.markdown(
    """
Use the sidebar on the left to move between pages. Here's what each one covers:

1. **VA Enrollment**: Check if you're eligible for VA health care and how to enroll.
2. **My HealtheVet Setup**: Set up your VA patient portal account.
3. **Health Records**: Request your military service treatment records.
4. **Mental Health**: Crisis line, VA mental health services, and peer support.
5. **Civilian Provider Options**: TRICARE, VA community care, the marketplace, and Medicaid.
6. **Transition Checklist**: Every step in this tool, organized by when you need to do it.
"""
)

st.markdown("### How to use this tool")

st.markdown(
    """
- Work through the pages in order if you're just getting started. Jump straight to what you need
  if you already know.
- Check off items as you complete them. Your progress is not saved, so this is a working tool for
  one sitting, or print/screenshot a page if you want a record.
- Every page links to the official government source for that step. This tool explains it,
  the official site is where you actually do it.
- If something changes on the official side, the official site is always right, not this tool.
"""
)

st.warning(
    "If you're in crisis right now, don't wait to read the rest of this. Go to the "
    "**Mental Health** page in the sidebar, or call or text **988** and press **1**."
)

st.divider()
st.caption("Source: U.S. Department of Veterans Affairs (va.gov). Not an official VA or DoD product.")
