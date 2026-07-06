import streamlit as st
from utils import render_checklist, source_caption

st.set_page_config(page_title="VA Enrollment", page_icon="🏥", layout="wide")

st.title("VA Health Care Enrollment")
st.markdown("Most veterans have to enroll in VA health care. It's not automatic. Here's how it works.")

st.markdown("### Are you eligible?")
st.markdown(
    """
You're generally eligible if you served in the active military, naval, or air service and were
discharged under a condition other than dishonorable. How much of your care VA covers, and what
it costs, depends on your **priority group**, based on things like:

- Disability rating from a service-connected condition
- Combat service, especially recent combat
- Income level
- Whether you received a Purple Heart or certain other awards

You don't need to figure out your priority group yourself. VA assigns it when you apply.
"""
)

st.markdown("### Combat veterans: know your extended window")
st.markdown(
    """
If you served in a combat zone, you get **10 years of free enrollment eligibility** from your
discharge date for conditions related to that service, no proof of service connection needed.
Don't skip enrolling just because you feel fine right now. Enroll while you have this window open.
"""
)

st.markdown("### How to apply")
st.markdown(
    """
You need three things before you start:

- DD214 or other discharge paperwork
- Social Security number (yours, and your dependents' if applying for their benefits too)
- Current insurance information, if you have any

Apply one of these ways:

- **Online:** [Apply for VA health care on VA.gov](https://www.va.gov/health-care/how-to-apply/)
- **By phone:** Call **877-222-8387**, Monday to Friday, 8 a.m. to 8 p.m. ET
- **In person:** Bring your paperwork to your nearest VA medical center
- **By mail:** Fill out [VA Form 10-10EZ](https://www.va.gov/find-forms/about-form-10-10ez/) and mail it in

Applying online is usually fastest. You'll get a confirmation once VA receives your application.
"""
)

st.markdown("### What happens after you apply")
st.markdown(
    """
VA reviews your application and sends you a decision letter. If you're approved, that letter
tells you your priority group and how to schedule your first appointment. If you don't hear back
in a few weeks, call and check on your application status. Don't just wait indefinitely.
"""
)

st.divider()

render_checklist(
    "VA Enrollment Checklist",
    [
        "Locate my DD214 or other discharge paperwork",
        "Gather Social Security numbers for myself and any dependents applying",
        "Gather current health insurance information, if I have any",
        "Apply for VA health care online, by phone, in person, or by mail",
        "Save or write down my confirmation number",
        "Watch for my decision letter with my priority group",
        "Schedule my first VA appointment once approved",
    ],
    "va_enrollment",
)

source_caption("U.S. Department of Veterans Affairs, va.gov/health-care/how-to-apply/")
