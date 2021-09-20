import streamlit as st

st.title('My first Streamlit app')

a = 12.34
st.write(a)

st.write("Some text here")

st.markdown('Text can be **bold** and _italic_.')

st.markdown('Text can be **bold** and _italic_.')

st.markdown(r'''Raw strings can be very useful: we can
- create
- bullet
- lists

and other Markdown things like horizontal lines

---
''')

st.markdown(r'''
$$
i\hbar\frac{\partial}{\partial t} \Psi(x,t) = \left [ - \frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x,t)\right ] \Psi(x,t)
$$
''')

#display mode
st.markdown(r'''
$
i\hbar\frac{\partial}{\partial t} \Psi(x,t) = \left [ - \frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x,t)\right ] \Psi(x,t)
$
''')

#code is just a wrapper around markdown

st.markdown(r'''
```c
int main() {
  return 0;
}
```
''')


# dynamic content

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')

# conditional value displayed if checked
if st.checkbox('Tick me to see'):
  st.write(42)

# conditional dropdowns
selection = st.selectbox('Choose an option', ["Nothing here", "or here", "but something here"])

if selection == "but something here":
  st.write("You found me!")
else:
  st.write("Try again")

# sliders displaying value
int_val = st.slider("Pick an integer", min_value=1, max_value=10, value=5)
st.write(int_val)

#floating point sliders
float_val = st.slider("Pick a float", min_value=1.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")
st.write(float_val)


#create a sidebar
st.sidebar.write("Adding text to the sidebar...")
