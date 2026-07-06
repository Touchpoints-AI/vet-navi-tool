import streamlit as st


def render_checklist(title: str, items: list[str], key_prefix: str) -> None:
    """Render an interactive checklist with a progress bar. Nothing is saved after the browser tab closes."""
    st.subheader(title)

    checked = []
    for i, item in enumerate(items):
        checked.append(st.checkbox(item, key=f"{key_prefix}_{i}"))

    done = sum(checked)
    total = len(items)
    st.progress(done / total if total else 0)
    st.caption(f"{done} of {total} steps checked off. This checklist resets when you close or reload the page, it isn't saved anywhere.")


def source_caption(text: str) -> None:
    st.divider()
    st.caption(f"Source: {text}")
