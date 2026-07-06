import streamlit as st
from utils import render_checklist, source_caption

st.set_page_config(page_title="Civilian Provider Options", page_icon="🩺", layout="wide")

st.title("Civilian Health Coverage Options")
st.markdown(
    "VA isn't your only option, and for some care it isn't even the fastest one. Here's what "
    "else is out there, and when each option makes sense."
)

st.markdown("### TRICARE")
st.markdown(
    """
If you're retiring after 20+ years of service, you likely qualify for **TRICARE**, the
military's health plan for retirees and their families. If you're separating before retirement
eligibility, you may still have **Transitional Assistance Management Program (TAMP)** coverage
for 180 days after separation, or you can buy the **Continued Health Care Benefit Program
(CHCBP)** for up to 36 months as a bridge.

Learn more and check your specific eligibility at [TRICARE.mil](https://www.tricare.mil/).
"""
)

st.markdown("### VA Community Care")
st.markdown(
    """
If you're enrolled in VA health care but the nearest VA facility is too far away, the wait is too
long, or VA doesn't offer the specific care you need, you may qualify to see a civilian
provider with VA paying the bill. This is called **VA Community Care**. Ask your VA care team
if you qualify. You don't arrange this on your own, VA has to authorize it first.

Learn more at [VA Community Care](https://www.va.gov/COMMUNITYCARE/index.asp).
"""
)

st.markdown("### The Health Insurance Marketplace")
st.markdown(
    """
If you don't have TRICARE, VA coverage, or a job that offers insurance, you can buy a private
health plan through the **Health Insurance Marketplace**. Depending on your income, you may
qualify for financial help to lower the monthly cost. Open enrollment happens once a year, but
losing military health coverage qualifies you for a **special enrollment period**, so you don't
have to wait.

Compare plans and check if you qualify for savings at [HealthCare.gov](https://www.healthcare.gov/).
"""
)

st.markdown("### Medicaid")
st.markdown(
    """
Depending on your income and household size, you may qualify for **Medicaid**, free or very
low-cost health coverage run by your state. Rules vary state to state, so check your state's
Medicaid page or apply through [HealthCare.gov](https://www.healthcare.gov/), which will screen
you for Medicaid eligibility as part of the marketplace application.
"""
)

st.markdown("### How to think about it")
st.markdown(
    """
- **Retiring at 20+ years?** Look at TRICARE first.
- **Separating before retirement?** Check if you have TAMP coverage, and enroll in VA health
  care regardless. They can work together.
- **Enrolled in VA but care is hard to access locally?** Ask about VA Community Care.
- **No coverage lined up at all?** Don't go without insurance. Check HealthCare.gov right away,
  since separating from the military qualifies you for a special enrollment window.
"""
)

st.divider()

render_checklist(
    "Civilian Provider Options Checklist",
    [
        "Determine if I qualify for TRICARE (retiree) or TAMP (recent separation)",
        "Check if VA Community Care applies to me and ask my VA team about it",
        "Check my special enrollment eligibility on HealthCare.gov",
        "Compare marketplace plans and check if I qualify for cost savings",
        "Check my state's Medicaid eligibility",
        "Make sure I have some form of health coverage lined up with no gap",
    ],
    "civilian_provider",
)

source_caption("TRICARE (tricare.mil), U.S. Department of Veterans Affairs (va.gov), and HealthCare.gov")
