import streamlit as st
from utils import render_checklist, source_caption

st.set_page_config(page_title="Mental Health", page_icon="🧠", layout="wide")

st.title("Mental Health Resources")

st.error(
    "**If you're in crisis right now, get help immediately.**\n\n"
    "Call or text **988**, then press **1** to reach the Veterans Crisis Line. "
    "You can also chat online at "
    "[veteranscrisisline.net](https://www.veteranscrisisline.net/) or text **838255**.\n\n"
    "This works whether or not you're enrolled in VA care, and whether or not you're a "
    "veteran yourself. It's also there for family and friends who are worried about someone. "
    "It's free, confidential, and available 24/7."
)

st.markdown(
    "Transition is hard on your mental health even when nothing looks wrong on paper. You don't "
    "need a crisis to justify getting support. Here's what's available to you."
)

st.markdown("### VA Mental Health Services")
st.markdown(
    """
- **Any discharge status:** VA offers free confidential mental health services related to
  military sexual trauma (MST) regardless of your discharge status or whether you're enrolled
  in VA health care.
- **Enrolled veterans:** Once you're enrolled in VA health care, you can access therapy,
  medication management, and specialized programs for PTSD, depression, substance use, and more
  through your local VA medical center.
- **Same-day services:** Every VA medical center offers same-day mental health services if
  you need to be seen urgently but it's not a 911 or 988 emergency.
- Learn more at [VA Mental Health](https://www.va.gov/health-care/health-needs-conditions/mental-health/).
"""
)

st.markdown("### Vet Centers: no enrollment required")
st.markdown(
    """
Vet Centers are community-based counseling centers, separate from VA medical centers. They offer
free individual and group counseling for combat veterans, sexual trauma survivors, and their
families, and you don't need to be enrolled in VA health care to use one. Find a location at
[VA Vet Centers](https://www.va.gov/find-locations/?facilityType=vet_center).
"""
)

st.markdown("### Peer support")
st.markdown(
    """
Sometimes the most useful person to talk to is someone who's been through it. Look into:

- **Vet Center peer support:** many Vet Centers have peer specialists on staff who are
  veterans themselves.
- **VA Whole Health peer support:** ask your VA care team about peer support specialists.
- **Give an Hour, Team RWB, and other veteran service organizations:** community-based peer
  networks outside the VA system.
"""
)

st.markdown("### You don't have to wait for a diagnosis")
st.markdown(
    """
You don't need a specific problem or a crisis to reach out. Adjustment struggles, sleep issues,
irritability, relationship strain, all valid reasons to talk to someone. Reaching out early is
easier than waiting until things get worse.
"""
)

st.divider()

render_checklist(
    "Mental Health Checklist",
    [
        "Save the Veterans Crisis Line number (988, press 1) in my phone",
        "Look up my nearest Vet Center location",
        "Ask my VA care team about mental health services, even if I feel fine right now",
        "Look into peer support options near me",
        "Talk to someone, a professional, a peer, or a friend, about how the transition is going",
    ],
    "mental_health",
)

source_caption("Veterans Crisis Line (veteranscrisisline.net) and U.S. Department of Veterans Affairs (va.gov)")
