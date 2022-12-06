from modzy import ApiClient
#from modzy._util import file_to_bytes
import sys
import os
import logging
import dotenv
from modzy.error import ResultsError 
from modzy.jobs import Jobs
import pandas as pd
import gradio as gr
import json

client = ApiClient(base_url="https://aienablement.dmidsc.io/api",\
                   api_key="zHLfWr10mW99Dq4SGPPN.twzeGywuin23YXqV5pyB")

file_path = "batch_records_latest1.csv"
class BatchIntentInference:
    def __init__(self):
        pass

    def chunk_csv(self,file):
        file = file.name 
        dataframe_list = []
        for i,chunk in enumerate(pd.read_csv(file,\
                                            chunksize=1)):
            chunk = chunk['Description']
            dataframe_list.append(chunk)
        return dataframe_list



    def modzy_input_format_text(self,dataframe_list):
        sources_list = []
        for i in range(len(dataframe_list)):
            sources = {"review_{}".format(i): {"input.txt": review} for i, review in enumerate(dataframe_list[i])}
            sources_list.append(sources)
        return sources_list



    def get_model_output(self,model_identifier, model_version, data_sources, explain=True):
        """
        Args:
            model_identifier: model identifier (string)
            model_version: model version (string)
            data_sources: dictionary with the appropriate filename --> local file key-value pairs
            explain: boolean variable, defaults to False. If true, model will return explainable result
        """
        job = client.jobs.submit_text(model_identifier, model_version, data_sources, explain = True)
        #result = job.block_until_complete(timeout=None)
        result = client.results.block_until_complete(job,timeout=None)
        return result



    def modzy_output_format_text(self,file):
        consolidated_result = []

        dataframe_list = obj_BatchIntentInference.chunk_csv(file)
        sources_list = obj_BatchIntentInference.modzy_input_format_text(dataframe_list)
        final_result = []   
        for source in sources_list:
            input_text_list = obj_BatchIntentInference.source_list_individual_text(source)
            result = obj_BatchIntentInference.\
                get_model_output("2xevwntkp2","1.0.0",source,explain=True)
            consolidated_result.append(result)
            result_response = result.results
            result_dict = obj_BatchIntentInference.final_result(source,result_response)
            final_result.append(result_dict)

        json_dump = obj_BatchIntentInference.write_json_file(final_result)                   
        return json_dump

    def write_json_file(self,final_result):
        json_dump = json.dumps(final_result,indent=4)
        with open('final_result.json','w') as f:
            f.write(json.dumps(final_result,indent=4))
        return final_result
        

    def source_list_individual_text(self,source_list):
        input_text_list = []
        for key in source_list:
            input_text = source_list[key]['input.txt']
            input_text_list.append(input_text)

        return input_text_list

    def final_result(self,source,result_response):
        final_result = {}
        if len(source) == len(result_response):
            for key_source,value_source in source.items():
                    for key_res,value_res in result_response.items():
                        if key_source.strip() == key_res.strip():
                            input_text = source[key_source]['input.txt']
                            final_result[input_text] = value_res['results.json']['data']['result']

        else:
            print("Error: Length of source and result_response are not equal")
            return ValueError
        return final_result

obj_BatchIntentInference = BatchIntentInference()

#final_response = obj_BatchIntentInference.modzy_output_format_text(file_path)
# json_obj = json.dumps(final_response,indent= 4)
# with open('final_response.txt','w') as f:
#     f.write(json_obj)


inputs = [
    gr.File(label="source_file")
]


test = "test"

def json_manipulation(self,json_obj):
    pass


def intent_gradio(file):
    final_response = obj_BatchIntentInference.modzy_output_format_text(file)
    return final_response

gr.Interface(
    fn = intent_gradio,
    inputs = inputs,
    outputs = "json"
).launch(share=True)