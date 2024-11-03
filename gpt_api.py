import openai
import os
from flask import jsonify

def get_recom():
    Country='Philippines'
    Curr_Type='Peso'
    Curr_Forecast_YoY='+4.5%'
    Curr_Forecast_MoM='-1.2%'
    Pol_1='Riot on Capital City over Election Result'
    Pol_1_Sentiment='Negative'
    Pol_2='Conflict between VP and President'
    Pol_2_Sentiment='Negative'
    Pol_3='Tropical Storm Trami devastates seven million in the Philippines'
    Pol_3_Sentiment='Negative'
    CBI='6.5%'
    VAT='12%'
    Tariff= '0%'
    Commodity='Coal'
    openai.api_key = os.getenv('OPEN_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": f"""Give advice to this businessman, and explain in Indonesian,
            You can advice against exporting!
            Tell him about: how risky it is, how much will the contract worth in rupiah when it ended vs now,
            he wanted to export {Commodity} to {Country}.
            Recent News about {Country} is {Pol_1} (sentiment: {Pol_1_Sentiment}),
            {Pol_2} (sentiment: {Pol_2_Sentiment}),
            {Pol_3} (sentiment: {Pol_3_Sentiment}).
                Economic Outlook of {Country} is {Curr_Type} is forecasted {Curr_Forecast_YoY} YoY and {Curr_Forecast_MoM} MoM,
                Central Bank Interest is {CBI}, VAT is {VAT}, Tariff on {Commodity} is {Tariff}"""},
            {"role": "user", "content": "Hi i wanted to export coal to the philippines, spesifically city of ambasing. The amount of contract is 100000 USD, expected to be finished on late 2025"}
        ]
    )
    return jsonify(response)

def pol_ph():
    news1="Philippines wants companies to pay for plastic waste treatment"
    risk1="Medium"
    news2="Climate change may cut Philippines GDP by 18% – ADB"
    risk2="Medium"
    news3="New Maersk facility opens in the Philippines"
    risk3="High"
    news4="Inside P Diddy's strict non-disclosure agreement 'freak off' party guests were forced to sign"
    risk4="Medium"
    openai.api_key = os.getenv('OPEN_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": f"""You are a jewish political expert.
            You are about to give someone a summary of philippines political climate.
            Explain in Indonesian. 
            Recent Political News on Philippines:
            1. {news1}. Possible Risk={risk1}
            2. {news2}. Possible Risk={risk2}
            3. {news3}. Possible Risk={risk3}
            4. {news4}. Possible Risk={risk4}"""},
            {"role": "user", "content": "Give me the summary of Philippines Political Climate"}
        ]
    )
    return response

def ek_ph():
    openai.api_key = os.getenv('OPEN_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": f"""You are a jewish economic expert.
            You are about to give someone a summary of philippines economic climate to someone that about
            to export somethign there.
            Explain in Indonesian. 
            Consider The Following:
            1. Epstein Island Scandal, Phillipine President was allegedly involved
            2. Diddy Scandal
            3. Phillipine GDP
            4. Phillipine Currency Strenght"""},
            {"role": "user", "content": "Give me the summary of Philippines Economic Climate"}
        ]
    )
    return response

def gen_ph():
    Country='Philippines'
    Curr_Type='Peso'
    Curr_Forecast_YoY='+4.5%'
    Curr_Forecast_MoM='-1.2%'
    Pol_1='Riot on Capital City over Election Result'
    Pol_1_Sentiment='Negative'
    Pol_2='Conflict between VP and President'
    Pol_2_Sentiment='Negative'
    Pol_3='Tropical Storm Trami devastates seven million in the Philippines'
    Pol_3_Sentiment='Negative'
    CBI='6.5%'
    VAT='12%'
    Tariff= '0%'
    Commodity='Coal'
    openai.api_key = os.getenv('OPEN_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": f"""Give advice to this businessman, and explain in Indonesian,
            You can advice against exporting!
            Tell him about: how risky it is, how much will the contract worth in rupiah when it ended vs now,
            he wanted to export {Commodity} to {Country}.
            Recent News about {Country} is {Pol_1} (sentiment: {Pol_1_Sentiment}),
            {Pol_2} (sentiment: {Pol_2_Sentiment}),
            {Pol_3} (sentiment: {Pol_3_Sentiment}).
                Economic Outlook of {Country} is {Curr_Type} is forecasted {Curr_Forecast_YoY} YoY and {Curr_Forecast_MoM} MoM,
                Central Bank Interest is {CBI}, VAT is {VAT}, Tariff on {Commodity} is {Tariff}"""},
            {"role": "user", "content": "Hi i wanted to export coal to the philippines, spesifically city of ambasing. The amount of contract is 100000 USD, expected to be finished on late 2025"}
        ]
    )
    return response

def pol_jp():
    news1="A week after election loss, Ishiba has a tailwind to form next government and remain as Japan PM"
    risk1="High"
    news2="Worries for Japan economy after election shock"
    risk2="High"
    news3="Nomura delivers big profit rise in quarter dogged by scandal"
    risk3="Medium"
    news4="Japan's Mitsui raises full-year profit forecast to US$6 billion on LNG business, asset sales"
    risk4="Medium"
    openai.api_key = os.getenv('OPEN_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": f"""You are a jewish political expert.
            You are about to give someone a summary of japanese political climate.
            Explain in Indonesian. 
            Recent Political News on Philippines:
            1. {news1}. Possible Risk={risk1}
            2. {news2}. Possible Risk={risk2}
            3. {news3}. Possible Risk={risk3}
            4. {news4}. Possible Risk={risk4}"""},
            {"role": "user", "content": "Give me the summary of Japanese Political Climate, in a funny way"}
        ]
    )
    return response

def ek_jp():
    openai.api_key = os.getenv('OPEN_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": f"""You are a jewish economic expert.
            You are about to give someone a summary of philippines economic climate to someone that about
            to export somethign there.
            Explain in Indonesian. 
            Consider The Following:
            1. Battotai Song
            2. Japanese Monarchy
            3. Japan GDP
            4. Japan Currency Strenght"""},
            {"role": "user", "content": "Give me the summary of Japanese Economic Climate Showa Style"}
        ]
    )
    return response

def gen_jp():
    Country='Japan'
    Curr_Type='Yen'
    Curr_Forecast_YoY='+1.5%'
    Curr_Forecast_MoM='-1.7%'
    Pol_1='A week after election loss, Ishiba has a tailwind to form next government and remain as Japan PM'
    Pol_1_Sentiment='Neutral'
    Pol_2='Worries for Japan economy after election shock'
    Pol_2_Sentiment='Neutral'
    Pol_3="Japan's Mitsui raises full-year profit forecast to US$6 billion on LNG business, asset sale"
    Pol_3_Sentiment='Positive'
    CBI='5%'
    VAT='10%'
    Tariff= '1%'
    Commodity='Coal'
    openai.api_key = os.getenv('OPEN_API_KEY')
    response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": f"""Give advice to this businessman, and explain in Indonesian,
            Tell him about: how risky it is, how much will the contract worth in rupiah when it ended vs now,
            he wanted to export {Commodity} to {Country}.
            Recent News about {Country} is {Pol_1} (sentiment: {Pol_1_Sentiment}),
            {Pol_2} (sentiment: {Pol_2_Sentiment}),
            {Pol_3} (sentiment: {Pol_3_Sentiment}).
                Economic Outlook of {Country} is {Curr_Type} is forecasted {Curr_Forecast_YoY} YoY and {Curr_Forecast_MoM} MoM,
                Central Bank Interest is {CBI}, VAT is {VAT}, Tariff on {Commodity} is {Tariff}"""},
            {"role": "user", "content": "Hi i wanted to export coal to the philippines, spesifically city of ambasing. The amount of contract is 100000 USD, expected to be finished on late 2025"}
        ]
    )
    return response