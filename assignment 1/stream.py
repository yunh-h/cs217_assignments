import streamlit as st
from notes import NoteBook

if 'notebook' not in st.session_state:
    st.session_state.notebook = NoteBook()

nb = st.session_state.notebook

st.title('Note App')

# Add Note Section
st.header('Add a note')
name = st.text_input('Name')
content = st.text_area('Content')

if st.button('Add'):
    if name and content:
        success = nb.add(name, content)

        if success:
            st.success('Note added')
        else:
            st.error('Fail to add note')
    else:
        st.error('Please provide both name and content')

# Sidebar for Search Notes
st.sidebar.header('Search Notes')
term = st.sidebar.text_input('Search term')

if st.sidebar.button('Search'):
    if term:
        results = nb.find(term)
        st.session_state.search_results = results

        if results:
            st.sidebar.write(f'Search Results for "{term}":')
            
            for note in results:
                st.sidebar.write(f'- {note}')
        else:
            st.sidebar.warning(f'No notes found for "{term}"')
    else:
        st.sidebar.error('Please provide a search term')

# Show Notes
st.header('All Notes')
all_notes = nb.list_notes()

if all_notes:
    selected_note = st.selectbox('Select a note', all_notes)
    st.write(f'Content of "{selected_note}":')
    st.write(nb.get(selected_note))
else:
    st.write('No notes available')

    
