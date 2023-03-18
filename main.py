import os
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adreportrun import AdReportRun
from facebook_business.adobjects.adsinsights import AdsInsights

def download_facebook_ads_data(access_token, ad_account_id, date_preset=None, level='campaign'):
    FacebookAdsApi.init(access_token=access_token)
    account = AdAccount(fbid=ad_account_id)
    
    params = {
        'level': level,
        'fields': [
            AdsInsights.Field.campaign_id,
            AdsInsights.Field.campaign_name,
            AdsInsights.Field.adset_id,
            AdsInsights.Field.adset_name,
            AdsInsights.Field.ad_id,
            AdsInsights.Field.ad_name,
            AdsInsights.Field.spend,
            AdsInsights.Field.impressions,
            AdsInsights.Field.clicks,
            AdsInsights.Field.actions,
            AdsInsights.Field.conversions,
        ],
        'breakdowns': [
            AdsInsights.Breakdown.age,
            AdsInsights.Breakdown.gender,
        ],
    }
    
    if date_preset:
        params['date_preset'] = date_preset
    
    data = account.get_insights(params=params)
    
    return data

if __name__ == '__main__':
    access_token = 'your_access_token'
    ad_account_id = 'act_your_ad_account_id'
    
    data = download_facebook_ads_data(access_token, ad_account_id, date_preset='last_30d')
    
    for row in data:
        print(row)
