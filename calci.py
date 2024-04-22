import streamlit as st


st.title("Hello Users 🖐️")

with st.container():
    st.markdown("""
                <marquee style="border-top:2px solid black; border-bottom:2px solid black; color:#1B1464;" direction='left' bgcolor='red' >🤗WELCOME TO STREAMLIT CALCULATOR 🤗</marquee>""",
    unsafe_allow_html=True)
col1,_,col2=st.columns([5,5,19],gap="small")

#with col1:
    #st.image("images/calculator.jpeg",width=200)
    
with col1:
    st.image("images/calculator.jpeg",width=200)
    
def calulation(reslut:float,operation:str,input1:float,input2:float):
    
      return f"{operation} on {input1} and {input2} is {result}"


if "cal"  not in st.session_state:
    st.session_state.cal=[]

with st.sidebar:
    st.subheader("Result Histroy 🤖")
    st.markdown("check the result(s) here")
    for cal in st.session_state.cal:
        with st.chat_message(cal["role"]):
         st.markdown(cal["content"])    

with col2:
    operation = st.selectbox("Select the Operation",["ADDITION","SUBTRACTION","MULTIPLICATION","DIVISION"])

    input1 = st.number_input("Enter the 1st number")
    input2 = st.number_input("Enter the 2nd number")




    if st.button("GO",type="primary"):
        if operation =="ADDITION":
            result = input1+input2
            
        elif operation =="SUBTRACTION":
            result = input1-input2
        elif operation=="MULTIPLICATION":
            result = input1*input2
        elif operation =="DIVISION":
            result = input1/input2
            
        else:
            st.markdown("invalid input")   
            
    #st.markdown(f"#### {calulation(result,operation,input1,input2,)}")    
        with st.chat_message("assistant"):
            response= calulation(result,operation,input1,input2)
            st.success(response)  
        
            
        st.session_state.cal.append({"role":"assistant","content":response})   
                    
with st.container():
    st.markdown("""
                <marquee style="border-top:2px solid black; border-bottom:2px solid black; color:#1B1464;" direction='left' bgcolor='#12CBC4' >NOTE: You can view your results history in the sidebar section </marquee>""",
    unsafe_allow_html=True)
