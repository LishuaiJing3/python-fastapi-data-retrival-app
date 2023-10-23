import gradio as gr


def retrieve_data(input1, input2):
    return f"""The {input1}  from  {input2} """

iface = gr.Interface(  
    fn=retrieve_data,  
    inputs=[  
        gr.Textbox(  
            lines=1,  
            placeholder="Start date",  
            label="Start date",  
            default="2023-10-01"  
        ),  
        gr.Textbox(  
            lines=1,  
            placeholder="End date",  
            label="End date",  
            default="2023-10-02"  
        )  
    ],  
   outputs=["text"] 
)  

if __name__ == "__main__":
    iface.launch()