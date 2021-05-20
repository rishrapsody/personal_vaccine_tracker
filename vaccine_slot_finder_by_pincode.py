import aiohttp
import asyncio
import datetime
import time
import sys
import json
import telegram_send
from dateutil.relativedelta import relativedelta
#import requests




async def vaccine_scan(session, url):
    session_data = 0
    browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
 #   proxies = {"http" : "139.59.1.14:8080", "https" : "139.59.1.14:8080"}
    try:
        async with session.get(url, headers=browser_header) as resp:
            session_data = await resp.json()
#            print(session_data)

            if session_data == 0 or session_data is None:
                pass
            elif (len(session_data['sessions'])) == 0:
                print("No Slots available")
            else:
                if (int(session_data['sessions'][0]['min_age_limit']) == 18):
                    result_dict = {}
                    result_dict['Hostpital Name'] = session_data['sessions'][0]['name']
                    result_dict['Address'] = session_data['sessions'][0]['address']
                    result_dict['Fee Type'] = session_data['sessions'][0]['fee_type']
                    result_dict['Date'] = session_data['sessions'][0]['date']
                    result_dict['Available Capacity'] = session_data['sessions'][0]['available_capacity']
                    result_dict['Vaccine Type'] = session_data['sessions'][0]['vaccine']
                    result_dict['Dose1'] = session_data['sessions'][0]['available_capacity_dose1']
                    result_dict['Dose2'] = session_data['sessions'][0]['available_capacity_dose2']
                    telegram_send.send(messages=[json.dumps(result_dict, indent=4, sort_keys=True)])
                else:
                        print("Slot avaialable but not for 18-45 group")

 #           print(url)
 #           return session_data
    except Exception as e:
        print(e.message)
    except:
#        print(resp.text)
        print("Oops!", sys.exc_info()[0], "occurred.")
#        print(resp.text)


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        pin = '560100'
#        start_date = datetime.date(2021,5,20)
        start_date = datetime.date.today()
#        end_date = datetime.date(2021,9,30)
        end_date = start_date + relativedelta(months=+3)
        delta = datetime.timedelta(days=1)

        while(start_date <= end_date):
#            print(str(start_date.strftime("%d-%m-%Y")))
            date = str(start_date.strftime("%d-%m-%Y"))
            url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}'.format(pin,date)
            tasks.append(asyncio.ensure_future(vaccine_scan(session, url)))
            start_date += delta

        session_data = await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
