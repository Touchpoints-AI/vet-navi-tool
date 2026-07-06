import streamlit as st
from utils import render_checklist, source_caption

st.set_page_config(page_title="My HealtheVet Setup", page_icon="💻", layout="wide")

st.title("My HealtheVet Setup")
st.markdown(
    "My HealtheVet is VA's patient portal. It's where you message your care team, refill "
    "prescriptions, and see your records online. Set it up as soon as you're enrolled."
)

st.markdown("### What you can do with it")
st.markdown(
    """
- Send secure messages to your VA care team
- Refill and track VA prescriptions
- View lab results and appointment info
- View and download parts of your VA health record
- Schedule or request appointments at many VA facilities
"""
)

st.markdown("### Before you start")
st.markdown(
    """
You need to be enrolled in VA health care first, or at least have an application in with VA
(see the **VA Enrollment** page if you haven't done this yet). You'll also need one of the
following to verify your identity:

- A **Login.gov** account
- An **ID.me** account
- A **DS Logon** account (being phased out, but still works for now)
"""
)

st.markdown("### How to register")
st.markdown(
    """
1. Go to [myhealth.va.gov](https://www.myhealth.va.gov/) and select **Create an Account**.
2. Choose Login.gov or ID.me to verify your identity. If you don't have one, you can create it
   during this step. You'll need an email address and a photo ID.
3. Follow the identity verification steps. This confirms you are who you say you are, so keep
   your ID handy.
4. Once verified, your My HealtheVet account links to your VA health record automatically.
5. Log in and look around: set up secure messaging, check for any prescriptions, and see if your
   VA facility offers online appointment requests.
"""
)

st.markdown("### Different account access levels")
st.markdown(
    """
Not everyone gets the same level of access right away. Basic accounts can message their care
team. **Premium accounts**, verified through Login.gov, ID.me, or an in-person visit, get full
access, including viewing your VA medical records online and refilling prescriptions. If you
verify your identity as described above, you should land at Premium automatically.
"""
)

st.divider()

render_checklist(
    "My HealtheVet Setup Checklist",
    [
        "Confirm I'm enrolled in (or have applied for) VA health care",
        "Set up a Login.gov or ID.me account, if I don't already have one",
        "Go to myhealth.va.gov and create my account",
        "Complete identity verification",
        "Log in and confirm I have Premium account access",
        "Set up secure messaging with my VA care team",
        "Check for any prescriptions I can manage online",
    ],
    "mhv_setup",
)

source_caption("U.S. Department of Veterans Affairs, myhealth.va.gov")
