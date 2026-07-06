import streamlit as st
from utils import render_checklist, source_caption

st.set_page_config(page_title="Transition Checklist", page_icon="✅", layout="wide")

st.title("Master Transition Checklist")
st.markdown(
    "Everything from this tool in one place, organized by when you need to do it. Use this page "
    "to track your overall progress, or the individual topic pages for more detail on each step."
)

st.info(
    "Timelines here are general guidance, not hard deadlines. Some benefits do have real "
    "deadlines. Check the linked official sources for anything time-sensitive to your situation."
)

render_checklist(
    "Before Separation",
    [
        "Start gathering my discharge paperwork (DD214) as soon as it's available",
        "Request copies of my Service Treatment Records before I lose easy access",
        "Attend my Transition Assistance Program (TAP) briefings",
        "Check my TRICARE/TAMP coverage timeline so I know when it ends",
        "Look into whether I qualify for the VA's pre-discharge disability claim program",
        "Save key contacts: my VA regional office, TRICARE, and my unit's transition office",
    ],
    "before_sep",
)

st.divider()

render_checklist(
    "Within 30 Days of Separation",
    [
        "Apply for VA health care enrollment",
        "Set up my My HealtheVet account",
        "Confirm my mailing address and contact info are updated with VA and DoD",
        "Save the Veterans Crisis Line number (988, press 1) in my phone",
        "Check my special enrollment period eligibility on HealthCare.gov",
        "Locate my nearest VA medical center and Vet Center",
    ],
    "within_30",
)

st.divider()

render_checklist(
    "Within 90 Days of Separation",
    [
        "Confirm my VA enrollment decision letter and priority group arrived",
        "Schedule my first VA appointment, or my first civilian appointment if using other coverage",
        "Request my full military health records from the National Archives if not done already",
        "Confirm continuous health coverage with no gap (VA, TRICARE, marketplace, or Medicaid)",
        "Follow up on any VA Community Care referral if my local VA has long wait times",
        "Check in on my own mental health, and connect with peer support if it would help",
    ],
    "within_90",
)

st.divider()
st.markdown(
    "For more detail on any of these steps, use the sidebar to go to the specific topic page: "
    "VA Enrollment, My HealtheVet Setup, Health Records, Mental Health, or Civilian Provider Options."
)

source_caption("U.S. Department of Veterans Affairs (va.gov), Transition Assistance Program and health care enrollment guidance")
