import openai
import os

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

