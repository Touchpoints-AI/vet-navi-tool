import streamlit as st
from utils import render_checklist, source_caption

st.set_page_config(page_title="Health Records", page_icon="📋", layout="wide")

st.title("Requesting Your Military Health Records")
st.markdown(
    "Any civilian doctor you see next will ask about your medical history. Your military "
    "treatment records prove what happened while you served. Get copies now, while it's easy."
)

st.markdown("### Why this matters")
st.markdown(
    """
Your Service Treatment Records (STR) cover the medical and dental care you got while on active
duty. VA uses these records to help decide disability claims. Civilian doctors use them to
understand your history. Don't wait until you need them urgently to go looking for them.
"""
)

st.markdown("### Where your records live")
st.markdown(
    """
- **Recent separations:** Your STRs are usually included with your discharge paperwork, or
  available through **milConnect**.
- **Older discharges:** Records may have been transferred to the **National Archives** (NPRC,
  National Personnel Records Center).
- **VA claims:** If you're filing a disability claim, VA can request your records directly as
  part of that process.
"""
)

st.markdown("### How to request your records")
st.markdown(
    """
**Option 1: milConnect (fastest for recent veterans)**
Go to [milConnect](https://milconnect.dmdc.osd.mil/) and log in with your DS Logon or Login.gov
account. Look for the option to download your DD214 and treatment records.

**Option 2: National Archives (for most veterans)**
Use the [National Archives eVetRecs system](https://www.archives.gov/veterans/military-service-records)
to request your Official Military Personnel File, which includes your service treatment records.
You can request online, by mail, or by fax. Have your full name, Social Security number, branch
of service, and dates of service ready.

**Option 3: Through VA**
If you're already working with VA on a claim, ask your VA representative to help pull your
records as part of that process.
"""
)

st.markdown("### What to do once you have them")
st.markdown(
    """
- Keep a digital copy and a printed copy somewhere safe.
- Bring a copy to your first appointment with any new civilian doctor.
- Upload a copy to My HealtheVet if you're able to, so VA providers can see it too.
"""
)

st.divider()

render_checklist(
    "Health Records Checklist",
    [
        "Check milConnect for my DD214 and treatment records",
        "Request my records from the National Archives if milConnect doesn't have them",
        "Confirm I have my Social Security number and service dates ready for the request",
        "Save a digital copy of my records somewhere safe",
        "Print a physical copy to bring to my first civilian appointment",
        "Share a copy with VA or upload it through My HealtheVet",
    ],
    "health_records",
)

source_caption("National Archives (archives.gov/veterans) and milConnect (milconnect.dmdc.osd.mil)")
