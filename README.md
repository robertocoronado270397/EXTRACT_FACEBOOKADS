To download data from Facebook Ads using Python, you can use the Facebook Marketing API. Before starting, ensure you have a Facebook Developer account, an App created on the platform, and access to the Facebook Marketing API. You'll also need to obtain an access token for your app. You can follow this guide to set up your account and obtain the required tokens: https://developers.facebook.com/docs/marketing-apis/overview/authentication

Once you have all the necessary credentials, you can use the facebook_business Python SDK to interact with the Facebook Marketing API. To install the SDK, run:

```
pip install facebook_business
```

Replace 'your_access_token' and 'act_your_ad_account_id' with your access token and Ad Account ID, respectively. The download_facebook_ads_data function will fetch the last 30 days of ad data, broken down by age and gender, at the campaign level. You can customize the fields, breakdowns, and date presets according to your requirements.