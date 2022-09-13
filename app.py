import streamlit as st
import openai as ai
placeholder = st.empty()
print("** Loading API Key")
ai.api_key="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"
st.title('GPT-3 Cover Letter Generator')
st.header('Cover Letter generator')
def clear_form():
    st.session_state["cname"] = ""
    st.session_state["y_name"] = ""
    st.session_state["role"] = ""
    st.session_state["who"] = ""
    st.session_state["exp"] = ""
    st.session_state["job"] = ""
    st.session_state['passion'] = ""
#st.help(st.form)
with st.form(key="my_form"):
	c_name=st.text_input("Company Name",key="cname")
	y_name=st.text_input('Your Name?',key="y_name")
	role=st.text_input('What role are you applying for?',key="role")
	who=st.text_input('Who are you emailing?',key="who")
	exp=st.text_input('I have experience in..',key="exp")
	job=st.text_input('I am excited about the job because..',key="job")
	passion=st.text_input('I am passionate about..',key='passion')
	submitted = st.form_submit_button("Submit")
	clear = st.form_submit_button(label="Clear Form", on_click=clear_form)
prompt = ("Write a cover letter to " + who + " from " + y_name +" for a " + role + " job at " + c_name +"." + " I have experience in " + exp + " I am excited about the job because " +job + " I am passionate about "+ passion)
if submitted:
	response = ai.Completion.create(engine = "text-davinci-002",prompt=prompt,max_tokens=int("1949"),temperature=0.99,top_p=int("1"),frequency_penalty=0.3,n=1, presence_penalty=0.9)
	text = response['choices'][0]['text']
	#print("Prompt:", prompt)
	print("Response:", text)
	#st.subheader("Cover Letter Prompt")
	#st.write(prompt)
	st.subheader("Auto-Generated Cover Letter")
	st.write(text)	
	







