import streamlit as st

st.set_page_config (layout="wide")

st.write("Azure VM Inventory")

tab_titles = ["VM Inventory", "VM Backup", "VM Monitoring", "VM Patching"]

tab_inv, tab_backup, tab_mon, tab_patching = st.tabs(tab_titles)

with tab_inv:
  col_vm, col_backup, col_mon, col_bau = st.columns(4)

  col_vm.metric("Total VMs", "45", "+3")
  col_backup.metric("Backup Enabled", "42", "-3")
  col_mon.metric("Monitored VMs", "45", "")
  col_bau.metric("BAU VMs", "40", "-5")

  st.write("VM Inventory Data")

  btn_inv = st.button("Get Inventory Data")
  if btn_inv:
    st.balloons()

with tab_backup:
  col_backup_enabled, col_last_backup = st.columns(2)

  col_backup_enabled.metric("Backup Enabled VMs", "42")
  col_last_backup.metric("Last Backup Success", "39", "-3")

  st.write("VM Backup Data")

  btn_backup = st.button("Get Backup Data")
  if btn_backup:
    st.balloons()

with tab_mon:
  col_mon_enabled, col_healthy_hb = st.columns(2)

  col_mon_enabled.metric("Monitoring Enabled VMs", "45")
  col_healthy_hb.metric("Health Heartbeat", "43", "-2")

  st.write("VM Monitoring Data")
  btn_mon = st.button("Get Monitoring Data")
  if btn_mon:
    st.balloons()

with tab_patching:
  col_patching_enabled, col_unpatched_90 = st.columns(2)

  col_patching_enabled.metric("Patching Enabled VMs", "40")
  col_unpatched_90.metric("VM Not Patched for 90 days", "4", "-10%")

  st.write("VM Patching Data")

  btn_patching = st.button("Get Patching Data")  
  if btn_patching:
    st.balloons()

st.write("Dashboard created by Hybrid Platform Team")

