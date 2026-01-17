import matplotlib.pyplot as plt
import streamlit as st

def show_dashboard(fields, risk):
    st.subheader("📊 Document Insights")
    st.write("Fraud Risk Level:", risk)

    if fields["Amounts"]:
        plt.figure()
        plt.hist([float(a.replace("₹","")) for a in fields["Amounts"]])
        st.pyplot(plt)
