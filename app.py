import streamlit as st
import requests

#Interface API - Schnittstelle zum Server

API_URL = "https://kurs-python-fast.onrender.com/items"

def fetch_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    st.error(f"Error fetching items: {response.status_code}")
    return[]

def fetch_item_by_id(item_id):
    response = requests.get(f"{API_URL}/{item_id}")
    if response.status_code == 200:
        return response.json()
    st.error(f"Error fetching item {item_id}: {response.status_code}")
    return None

def create_item(item_data):
    try:
        response = requests.post(API_URL, json=item_data)
        response.raise_for_status()
        st.success("Item created successfully!")
    except requests.exceptions.HTTPError:
        st.error(f"Error creating item: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An unknown error has occurred: {str(e)}")

def update_item(update_id, updated_item):
    response = requests.put(f"{API_URL}/{update_id}", json=updated_item)
    if response.status_code == 200:
        st.success(f"Item {update_id} updated successfully!")
    else:
        st.error(f"Error updating item: {response.status_code} - {response.text}")

def delete_item(item_id):
    response = requests.delete(f"{API_URL}/{delete_item_id}")
    if response.status_code == 200:
        st.success(f"Deleted Item: {delete_item_id} successfully!")
    else:
        st.error(f"Error deleting Item: {response.status_code}")


# Frontend

st.title("Custom Application with BackEnd")

st.subheader("Fetch Items")
if st.button("Fetch all Items"):
    items = fetch_items()
    st.write(items)


st.subheader("Fetch Item by ID")
item_id = st.number_input("Item ID", min_value=1)
if st.button("Fetch Item"):
    item = fetch_item_by_id(item_id)
    st.write(item)


st.subheader("Create Item")
with st.form("create_item_form"):
    new_id = st.number_input("id", min_value=1)
    new_name = st.text_input("name")
    new_description = st.text_input("description")
    new_price = st.number_input("price", min_value=0.0, step=0.5)
    new_available = st.checkbox("Available", value=False)
    create_submit = st.form_submit_button("Create Item")

    if create_submit:
        new_item = {
                "id": new_id,
                "name": new_name,
                "description": new_description,
                "price": new_price,
                "available": create_submit,
        }
        create_item(new_item)



st.subheader("Update Item")
with st.form("update_item_form"):
    update_id = st.number_input("Update id", min_value=1)
    update_name = st.text_input("Update name")
    update_description = st.text_input("Update description")
    update_price = st.number_input("Update price", min_value=0.0, step=0.5)
    update_available = st.checkbox("Update Available", value=False)
    update_submit = st.form_submit_button("Update Item")

    if update_submit:
        updated_item = {
                "id": update_id,
                "name": update_name,
                "description": update_description,
                "price": update_price,
                "available": update_submit,
        }
        update_item(update_id, updated_item)



st.subheader("Delete Item")
delete_item_id = st.number_input("Delte ID", min_value=1)
if st.button("Delete Item"):
    delete_item(delete_item_id)
    
