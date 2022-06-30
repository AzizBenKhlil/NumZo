import requests, codecs, os
import json
from multiprocessing.dummy import Pool
import concurrent.futures

def getdata(num):
    url = 'https://api.telnyx.com/v1/phone_number/' + num
    html = requests.get(url).text
    data = json.loads(html)
    return data



def getmail(num):
    try:
        
        teliff = getstrng(num)
        data = getdata(teliff)
        try:
            carrier = data["carrier"]["name"]
            country = data["country_code"]
            nmbr = data["national_format"]
            opera = carrier.encode("utf-8").lower()
            bled = country.encode("utf-8")
            tel = nmbr.encode("utf-8")
        except:
            print(num+' is not a valid number.')
            open('result/valid.txt', 'a').write(num  + '\n')
        else:
            tel_ndhif = getstrng(tel)
            tel_ndhiif = tel_ndhif
            
            if ('ATT'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@txt.att.net'
            elif ('T-Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@tmomail.net'
            elif ('Verizon'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vzwpix.com'
            elif ('Sprint'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@messaging.sprintpcs.com'
            elif ('Accessyou'.lower() in opera) and ('HK' in bled) :
                tel_ndhiif = tel_ndhiif+'@messaging.accessyou.com'
            elif ('Aio Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.aiowireless.net'
            elif ('AirCel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@aircel.co.in'
            elif ('AirFire Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.airfiremobile.com'
            elif ('Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelap.com'
            elif ('Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelkk.com'
            elif ('Alaska Communications'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@msg.acsalaska.com'
            elif ('Aliant Canada'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.wirefree.informe.ca'
            elif ('Alltel (Allied Wireless)'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.alltelwireless.com'
            elif ('Ameritech'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@paging.acswireless.com'
            elif ('Andhra Pradesh AirTel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelap.com'
            elif ('Andhra Pradesh Idea'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@ideacellular.net'
            elif ('Assurance Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vmobl.com'
            elif ('AT&T Enterprise Paging'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@page.att.net'
            elif ('AT&T Mobility'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.att.net'
            elif ('Beeline'.lower() in opera) and ('RU' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.beemail.ru'
            elif ('Bell Mobility'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@txt.bell.ca'
            elif ('BellSouth'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@bellsouth.cl'
            elif ('Bluegrass Cellular'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.myblueworks.com'
            elif ('Bluesky Communications'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@psms.bluesky.as'
            elif ('Boost mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@myboostmobile.com'
            elif ('Bouygues Telecom'.lower() in opera) and ('FR' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.bouyguestelecom.fr'
            elif ('Box Internet Services'.lower() in opera) and ('CH' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.boxis.net'
            elif ('C Spire Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@cspire1.com'
            elif ('CellCom'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@cellcom.quiktxt.com'
            elif ('Cellular South'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@csouth1.com'
            elif ('Centennial Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@cwemail.com'
            elif ('Chariton Valley Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.cvalley.net'
            elif ('Chat Mobility'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mail.msgsender.com'
            elif ('Chennai RPG Cellular'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@rpgmail.net'
            elif ('China Mobile'.lower() in opera) and ('CN' in bled) :
                tel_ndhiif = tel_ndhiif+'@139.com'
            elif ('Cincinnati Bell'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.gocbw.com'
            elif ('Claro'.lower() in opera) and ('BR' in bled) :
                tel_ndhiif = tel_ndhiif+'@clarotorpedo.com.br'
            elif ('Claro'.lower() in opera) and ('CO' in bled) :
                tel_ndhiif = tel_ndhiif+'@iclaro.com.co'
            elif ('Claro'.lower() in opera) and ('NI' in bled) :
                tel_ndhiif = tel_ndhiif+'@ideasclaro-ca.com'
            elif ('Claro'.lower() in opera) and ('PR' in bled) :
                tel_ndhiif = tel_ndhiif+'@vtexto.com'
            elif ('Cleartalk'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.cleartalk.us'
            elif ('Cricket'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.mycricket.com'
            elif ('CSL'.lower() in opera) and ('HK' in bled) :
                tel_ndhiif = tel_ndhiif+'@mgw.mmsc1.hkcsl.com'
            elif ('CTI'.lower() in opera) and ('AR' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.ctimovil.com.ar'
            elif ('Delhi Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('Digicel'.lower() in opera) and ('DM' in bled) :
                tel_ndhiif = tel_ndhiif+'@digitextdm.com'
            elif ('DTC'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.advantagecell.net'
            elif ('Edge Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.edgewireless.com'
            elif ('Element Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@SMS.elementmobile.net'
            elif ('Emtel'.lower() in opera) and ('MU' in bled) :
                tel_ndhiif = tel_ndhiif+'@emtelworld.net'
            elif ('E-Plus'.lower() in opera) and ('DE' in bled) :
                tel_ndhiif = tel_ndhiif+'@smsmail.eplus.de'
            elif ('Esendex'.lower() in opera) and ('ES' in bled) :
                tel_ndhiif = tel_ndhiif+'@esendex.net'
            elif ('Fido'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.fido.ca'
            elif ('Firmensms'.lower() in opera) and ('AT' in bled) :
                tel_ndhiif = tel_ndhiif+'@subdomain.firmensms.at'
            elif ('General Communications Inc.'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mobile.gci.net'
            elif ('Globul'.lower() in opera) and ('BG' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.globul.bg'
            elif ('Goa Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('Goa Idea Cellular'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@ideacellular.net'
            elif ('Golden State Cellular'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@gscsms.com'
            elif ('Greatcall'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vtxt.com'
            elif ('Gujarat Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('Gujarat Celforce / Fascel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@celforce.com'
            elif ('Gujarat Idea Cellular'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@ideacellular.net'
            elif ('Guyana T&T'.lower() in opera) and ('GY' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.cellinkgy.com'
            elif ('Haryana Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('Haryana Escotel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@escotelmobile.com'
            elif ('Hawaiian Telcom'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@hawaii.sprintpcs.com'
            elif ('Himachai Pradesh Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('HSL Mobile'.lower() in opera) and ('GB' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.haysystems.com'
            elif ('ICE'.lower() in opera) and ('CR' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.ice.cr'
            elif ('I-wireless(Sprint PCS)'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@iwirelesshometext.com'
            elif ('I-wireless(T-Mobile)'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'.iws@iwspcs.net'
            elif ('Kajeet'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mobile.kajeet.net'
            elif ('Karnataka Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelkk.com'
            elif ('Kerala Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelkerala.com'
            elif ('Kerala Escotel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@escotelmobile.com'
            elif ('Kolkata Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelkol.com'
            elif ('Koodo Mobile'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@msg.telus.com'
            elif ('LongLines'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@text.longlines.com'
            elif ('Lynx Mobility'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.lynxmobility.com'
            elif ('M1'.lower() in opera) and ('SG' in bled) :
                tel_ndhiif = tel_ndhiif+'@m1.com.sg'
            elif ('Mas Movil'.lower() in opera) and ('PA' in bled) :
                tel_ndhiif = tel_ndhiif+'@cwmovil.com'
            elif ('Madhya Pradesh Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('Maharashtra Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('Maharashtra Idea'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@ideacellular.net'
            elif ('Mediaburst'.lower() in opera) and ('GB' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.mediaburst.co.uk'
            elif ('MetroPCS'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mymetropcs.com'
            elif ('Mobiltel'.lower() in opera) and ('BG' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.mtel.net'
            elif ('Mobitel'.lower() in opera) and ('LK' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.mobitel.lk'
            elif ('Movistar'.lower() in opera) and ('AR' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.movistar.net.ar'
            elif ('Movistar'.lower() in opera) and ('CO' in bled) :
                tel_ndhiif = tel_ndhiif+'@movistar.com.co'
            elif ('Movistar'.lower() in opera) and ('ES' in bled) :
                tel_ndhiif = '0'+tel_ndhiif+'@movistar.net'
            elif ('Movistar'.lower() in opera) and ('UY' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.movistar.com.uy'
            elif ('MTN'.lower() in opera) and ('ZA' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.co.za'
            elif ('MTS Mobility'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@text.mtsmobility.com'
            elif ('Mumbai Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('My-Cool-SMS'.lower() in opera) and ('GB' in bled) :
                tel_ndhiif = tel_ndhiif+'@my-cool-sms.com'
            elif ('Nextech'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.ntwls.net'
            elif ('Nextel'.lower() in opera) and ('AR' in bled) :
                tel_ndhiif = 'TwoWay.11'+tel_ndhiif+'@nextel.net.ar'
            elif ('Nextel'.lower() in opera) and ('MX' in bled) :
                tel_ndhiif = tel_ndhiif+'@msgnextel.com.mx'
            elif ('O2'.lower() in opera) and ('DE' in bled) :
                tel_ndhiif = tel_ndhiif+'@o2online.de'
            elif ('OgVodafone'.lower() in opera) and ('IS' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.is'
            elif ('Orange'.lower() in opera) and ('GB' in bled) :
                tel_ndhiif = tel_ndhiif+'@orange.net'
            elif ('Page Plus Cellular (Verizon)'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vzwpix.com'
            elif ('PC Telecom'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@mobiletxt.ca'
            elif ('Personal'.lower() in opera) and ('AR' in bled) :
                tel_ndhiif = tel_ndhiif+'@alertas.personal.com.ar'
            elif ('Pioneer Cellular'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@zsend.com'
            elif ('Pocket Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.pocket.com'
            elif ('Polkomtel'.lower() in opera) and ('PL' in bled) :
                tel_ndhiif = tel_ndhiif+'@text.plusgsm.pl'
            elif ('Qwest Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@qwestmp.com'
            elif ('Red Pocket Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vtext.com'
            elif ('Siminn'.lower() in opera) and ('IS' in bled) :
                tel_ndhiif = tel_ndhiif+'@box.is'
            elif ('SaskTel'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@pcs.sasktelmobility.com'
            elif ('Sendega'.lower() in opera) and ('NO' in bled) :
                tel_ndhiif = tel_ndhiif+'@sendega.com'
            elif ('Setar Mobile email (Aruba)'.lower() in opera) and ('AW' in bled) :
                tel_ndhiif = tel_ndhiif+'@mas.aw'
            elif ('SFR'.lower() in opera) and ('FR' in bled) :
                tel_ndhiif = tel_ndhiif+'@sfr.fr'
            elif ('Simple Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@smtext.com'
            elif ('SMS Broadcast'.lower() in opera) and ('AU' in bled) :
                tel_ndhiif = tel_ndhiif+'@send.smsbroadcast.com.au'
            elif ('SMS Central'.lower() in opera) and ('AU' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.smscentral.com.au'
            elif ('SMSPUP'.lower() in opera) and ('AU' in bled) :
                tel_ndhiif = tel_ndhiif+'@smspup.com'
            elif ('South Central Communications'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@rinasms.com'
            elif ('Southernlinc'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@page.southernlinc.com'
            elif ('Spikko'.lower() in opera) and ('IL' in bled) :
                tel_ndhiif = tel_ndhiif+'@SpikkoSMS.com'
            elif ('Sprint'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@pm.sprint.com'
            elif ('Sunrise Communications'.lower() in opera) and ('CH' in bled) :
                tel_ndhiif = tel_ndhiif+'@gsm.sunrise.ch'
            elif ('Syringa Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@rinasms.com'
            elif ('Tamil Nadu Aircel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = '9842'+tel_ndhiif+'@airsms.com'
            elif ('Tamil Nadu Airtel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = '919894'+tel_ndhiif+'@airtelmobile.com'
            elif ('Telcel'.lower() in opera) and ('MX' in bled) :
                tel_ndhiif = tel_ndhiif+'@itelcel.com'
            elif ('Tele2'.lower() in opera) and ('SE' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.tele2.se'
            elif ('Telecom'.lower() in opera) and ('NZ' in bled) :
                tel_ndhiif = tel_ndhiif+'@etxt.co.nz'
            elif ('Teleflip'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@teleflip.com'
            elif ('TeletopiaSMS'.lower() in opera) and ('NO' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.teletopiasms.no'
            elif ('Telstra'.lower() in opera) and ('AU' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.tim.telstra.com'
            elif ('Tigo (Formerly Ola)'.lower() in opera) and ('CO' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.tigo.com.co'
            elif ('TIM'.lower() in opera) and ('IT' in bled) :
                tel_ndhiif = tel_ndhiif+'@timnet.com'
            elif ('Ting'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@message.ting.com'
            elif ('T-Mobile (Optus Zoo)'.lower() in opera) and ('AU' in bled) :
                tel_ndhiif = tel_ndhiif+'@optusmobile.com.au'
            elif ('T-Mobile'.lower() in opera) and ('AT' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.t-mobile.at'
            elif ('T-Mobile'.lower() in opera) and ('DE' in bled) :
                tel_ndhiif = tel_ndhiif+'@t-mobile-sms.de'
            elif ('T-Mobile'.lower() in opera) and ('HR' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.t-mobile.hr'
            elif ('T-Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@tmomail.net'
            elif ('TracFone (prepaid)'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mmst5.tracfone.com'
            elif ('Txtlocal'.lower() in opera) and ('GB' in bled) :
                tel_ndhiif = tel_ndhiif+'@txtlocal.co.uk'
            elif ('Unicel'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@utext.com'
            elif ('UniMovil Corporation'.lower() in opera) and ('GB' in bled) :
                tel_ndhiif = tel_ndhiif+'@viawebsms.com'
            elif ('Union Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@union-tel.com'
            elif ('US Cellular'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mms.uscc.net'
            elif ('USA Mobility'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@usamobility.net'
            elif ('UTBox'.lower() in opera) and ('AU' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.utbox.net'
            elif ('Uttar Pradesh West Escotel'.lower() in opera) and ('IN' in bled) :
                tel_ndhiif = tel_ndhiif+'@escotelmobile.com'
            elif ('Verizon Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vzwpix.com'
            elif ('Verizon Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vzwpix.com'
            elif ('Viaero'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@mmsviaero.com'
            elif ('Virgin Mobile'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@vmobile.ca'
            elif ('Virgin Mobile'.lower() in opera) and ('GB' in bled) :
                tel_ndhiif = tel_ndhiif+'@vxtras.com'
            elif ('Virgin Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@vmpix.com'
            elif ('Vivo'.lower() in opera) and ('BR' in bled) :
                tel_ndhiif = tel_ndhiif+'@torpedoemail.com.br'
            elif ('Vodacom'.lower() in opera) and ('ZA' in bled) :
                tel_ndhiif = tel_ndhiif+'@voda.co.za'
            elif ('Vodafone'.lower() in opera) and ('DE' in bled) :
                tel_ndhiif = tel_ndhiif+'@vodafone-sms.de'
            elif ('Vodafone'.lower() in opera) and ('ES' in bled) :
                tel_ndhiif = '0'+tel_ndhiif+'@vodafone.es'
            elif ('Vodafone'.lower() in opera) and ('IT' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.vodafone.it'
            elif ('Vodafone'.lower() in opera) and ('NZ' in bled) :
                tel_ndhiif = tel_ndhiif+'@mtxt.co.nz'
            elif ('Vodafone'.lower() in opera) and ('PT' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.vodafone.'
            elif ('Voyager Mobile'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@text.voyagermobile.com'
            elif ('West Central Wireless'.lower() in opera) and ('US' in bled) :
                tel_ndhiif = tel_ndhiif+'@sms.wcc.net'
            elif ('Wind Mobile'.lower() in opera) and ('CA' in bled) :
                tel_ndhiif = tel_ndhiif+'@txt.windmobile.ca'
            elif ('Esendex'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.xit.net'
            elif ('TellusTalk'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@echoemail.net'
            elif ('T-Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@esms.nu'
            elif ('Rogers Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@gin.nl'
            elif ('Telus Mobility'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mms.rogers.com'
            elif ('Movistar'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mms.telusmobility.com'
            elif ('Globalstar'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@movimensaje.com.ar'
            elif ('Helio'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@msg.globalstarusa.com'
            elif ('Orange'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@myhelio.com'
            elif ('Freebie SMS'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.orange.nl'
            elif ('Plus'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@smssturen.com'
            elif ('Carrier'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@text.plusgsm.pl'
            elif ('ACS Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@paging.acswireless.com'
            elif ('Galaxy Corporation'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'.epage@sendabeep.net'
            elif ('Satellink'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'.pageme@satellink.net'
            elif ('Advantage Communications'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@advantagepaging.com'
            elif ('GTE'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@airmessage.net'
            elif ('PageMart'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@airmessage.net'
            elif ('WebLink Wiereless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@airmessage.net'
            elif ('Andhra Pradesh Airtel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@airtelap.com'
            elif ('Kolkata Airtel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@airtelkol.com'
            elif ('Delhi Aritel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@airtelmail.com'
            elif ('Alltel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@alltelmessage.com'
            elif ('TSR Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@alphame.com'
            elif ('Arch Pagers (PageNet)'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@archwireless.net'
            elif ('Morris Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@beepone.net'
            elif ('Beepwear'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@beepwear.net'
            elif ('Bell South (Blackberry)'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@bellsouthtips.com'
            elif ('Bell South Mobility'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@blsdcs.net'
            elif ('Blue Sky Frog'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@blueskyfrog.com'
            elif ('Swisscom'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.bluewin.ch'
            elif ('BPL mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@bplmobile.com'
            elif ('Goa BPLMobil'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@bplmobile.com'
            elif ('Maharashtra BPL Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@bplmobile.com'
            elif ('Mumbai BPL Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@bplmobile.com'
            elif ('Pondicherry BPL Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@bplmobile.com'
            elif ('Tamil Nadu BPL Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@bplmobile.com'
            elif ('Gujarat Celforce'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@celforce.com'
            elif ('Western Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@cellularonewest.com'
            elif ('Midwest Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@clearlydigital.com'
            elif ('Ameritech Clearpath'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@clearpath.acswireless.com'
            elif ('Comcast'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@comcastpcs.textmsg.com'
            elif ('Cook Paging'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@cookmail.com'
            elif ('Movistar'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@correo.movistar.net'
            elif ('Corr Wireless Communications'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@corrwireless.net'
            elif ('Cellular South'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@csouth1.com'
            elif ('Central Vermont Communications'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@cvcpaging.com'
            elif ('Delhi Hutch'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@delhi.hutch.co.in'
            elif ('AT&T Pocketnet PCS'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@dpcs.mobile.att.net'
            elif ('Skytel Pagers'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@email.skytel.com'
            elif ('Southwestern Bell'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@email.swbw.com'
            elif ('US Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@email.uscc.net'
            elif ('Lauttamus Communication'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@e-page.net'
            elif ('Escotel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@escotelmobile.com'
            elif ('Kerala Escotel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@escotelmobile.com'
            elif ('Uttar Pradesh Escotel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@escotelmobile.com'
            elif ('Fido'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@fido.ca'
            elif ('Microcell'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@fido.ca'
            elif ('Telia Denmark'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@gsm1800.telia.dk'
            elif ('Idea Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@ideacellular.net'
            elif ('Maharashtra Idea Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@ideacellular.net'
            elif ('Inland Cellular Telephone'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@inlandlink.com'
            elif ('Motient'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@isp.com'
            elif ('MiWorld'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@m1.com.sg'
            elif ('Mobileone'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@m1.com.sg'
            elif ('MCI Phone'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mci.com'
            elif ('Alltel PCS'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@message.alltel.com'
            elif ('Bell Atlantic'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@message.bam.com'
            elif ('CenturyTel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@messaging.centurytel.net'
            elif ('Nextel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@messaging.nextel.com'
            elif ('Sprint PCS'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@messaging.sprintpcs.com'
            elif ('Mobility Bermuda'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@ml.bm'
            elif ('O2'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mmail.co.uk'
            elif ('Cincinnati Bell'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobile.att.net'
            elif ('Cellular One'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobile.celloneusa.com'
            elif ('Dobson-Alex Wireless'.lower() in opera) or ('Dobson-Cellular One'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobile.cellularone.com'
            elif ('Dobson Cellular Systems'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobile.dobson.net'
            elif ('Cingular Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobile.mycingular.com'
            elif ('Surewest Communications'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobile.surewest.com'
            elif ('Price Communications'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobilecell1se.com'
            elif ('Mobilecomm'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobilecomm.net'
            elif ('Telenor'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobilpost.no'
            elif ('Mobistar Belgium'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobistar.be'
            elif ('Mobtel Srbija'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mobtel.co.yu'
            elif ('Telefonica Movistar'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@movistar.net'
            elif ('Clearnet'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@msg.clearnet.com'
            elif ('Google Project Fi'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@msg.fi.google.com'
            elif ('Pioneer'.lower() in opera) or ('Enid Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@msg.pioneerenidcellular.com'
            elif ('Telus'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@msg.telus.com'
            elif ('Oskar'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mujoskar.cz'
            elif ('Metrocall 2-way'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@my2way.com'
            elif ('Airtouch Pagers'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@myairmail.com'
            elif ('Verizon Pagers'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@myairmail.com'
            elif ('Boost'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@myboostmobile.com'
            elif ('Cellular One West'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mycellone.com'
            elif ('Metro PCS'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mymetropcs.com'
            elif ('Smart Telecom'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mysmart.mymobile.ph'
            elif ('Sunrise'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@mysunrise.ch'
            elif ('NPI Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@npiwireless.com'
            elif ('Omnipoint'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@omnipoint.com'
            elif ('One Connect Austria'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@onemail.at'
            elif ('OnlineBeep'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@onlinebeep.net'
            elif ('Optus Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@optusmobile.com.au'
            elif ('Orange'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@orange.net'
            elif ('Mumbai Orange'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@orangemail.co.in'
            elif ('Orange Mumbai'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@orangemail.co.in'
            elif ('Pacific Bell'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pacbellpcs.net'
            elif ('Digi-Page'.lower() in opera) or ('Page Kansas'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@page.hit.net'
            elif ('Metrocall'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@page.metrocall.com'
            elif ('Mobilecom PA'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@page.mobilcom.net'
            elif ('Mobilfone'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@page.mobilfone.com'
            elif ('Southern LINC'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@page.southernlinc.com'
            elif ('PageOne NorthWest'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@page1nw.com'
            elif ('PageNet Canada'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pagegate.pagenet.ca'
            elif ('MCI'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pagemci.com'
            elif ('Teletouch'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pageme.teletouch.com'
            elif ('Vessotel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pager.irkutsk.ru'
            elif ('Ameritech Paging'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@paging.acswireless.com'
            elif ('SBC Ameritech Paging'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@paging.acswireless.com'
            elif ('Cellular One PCS'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@paging.cellone-sf.com'
            elif ('Ntelos'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pcs.ntelos.com'
            elif ('Rogers'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pcs.rogers.com'
            elif ('PCS One'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pcsone.net'
            elif ('Cellular One East Coast'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@phone.cellone.net'
            elif ('PageMart Canada'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@pmcl.net'
            elif ('Primco'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@primeco@textmsg.com'
            elif ('Qwest'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@qwestmp.com'
            elif ('RAM Page'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@ram-page.com'
            elif ('Chennai RPG Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@rpgmail.net'
            elif ('Safaricom'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@safaricomsms.com'
            elif ('Satelindo GSM'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@satelindogsm.com'
            elif ('SCS-900'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@scs-900.ru'
            elif ('SFR France'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sfr.fr'
            elif ('BeeLine GSM'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.beemail.ru'
            elif ('Bell South'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.bellsouth.com'
            elif ('Bluegrass Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.bluecell.com'
            elif ('Mobitel Tanzania'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.co.tz'
            elif ('Comviq'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.comviq.se'
            elif ('Edge Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.edgewireless.com'
            elif ('EMT'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.emt.ee'
            elif ('Golden Telecom'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.goldentele.com'
            elif ('P&T Luxembourg'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.luxgsm.lu'
            elif ('Meteor'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.mymeteor.ie'
            elif ('Netcom'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.netcom.no'
            elif ('Dutchtone'.lower() in opera) or ('Orange-NL'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.orange.nl'
            elif ('Primtel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.primtel.ru'
            elif ('Public Service Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.pscel.com'
            elif ('Tele2 Latvia'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.tele2.lv'
            elif ('T-Mobile Austria'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.t-mobile.at'
            elif ('UMC'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.umc.com.ua'
            elif ('Uraltel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.uraltel.ru'
            elif ('Vodafone Italy'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.vodafone.it'
            elif ('West Central Wireless'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sms.wcc.net'
            elif ('Kyivstar'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@smsmail.lmt.lv'
            elif ('LMT'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@smsmail.lmt.lv'
            elif ('Sprint'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@sprintpaging.com'
            elif ('Cellular One South West'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@swmsg.com'
            elif ('Vodafone Japan'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@t.vodafone.ne.jp'
            elif ('T-Mobile Germany'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@t-d1-sms.de'
            elif ('Houston Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@text.houstoncellular.net'
            elif ('Manitoba Telecom Systems'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@text.mtsmobility.com'
            elif ('PlusGSM'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@text.plusgsm.pl'
            elif ('Simple Freedom'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@text.simplefreedom.net'
            elif ('TIM'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@timnet.com'
            elif ('T-Mobile UK'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@t-mobile.uk.net'
            elif ('DT T-Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@t-mobile-sms.de'
            elif ('T-Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@tmomail.net'
            elif ('SunCom'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@tms.suncom.com'
            elif ('Triton'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@tms.suncom.com'
            elif ('AT&T'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@txt.att.net'
            elif ('Bell Canada'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@txt.bellmobility.ca'
            elif ('Bell Mobility'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@txt.bellmobility.ca'
            elif ('US Cellular'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@uscc.textmsg.com'
            elif ('US West'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@uswestdatamail.com'
            elif ('Unicel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@utext.com'
            elif ('Vodafone Spain'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@vodafone.es'
            elif ('Powertel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@voicestream.net'
            elif ('VoiceStream'.lower() in opera) or ('T-Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@voicestream.net'
            elif ('Verizon PCS'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@vtext.com'
            elif ('Virgin Mobile'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@vxtras.com'
            elif ('GCS Paging'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@webpager.us'
            elif ('NBTel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@wirefree.informe.ca'
            elif ('Wyndtell'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'@wyndtell.com'
            elif ('Emtel'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'emtelworld.net'
            elif ('ProPage'.lower() in opera) :
                tel_ndhiif = tel_ndhiif+'page.propage.net'
            else:
                tel_ndhiif = 'Not Found'


            if (tel_ndhif == tel_ndhiif):
                pass
            else:
                print('Valid' + ' | ' + bled + ' | ' + tel_ndhif + ' | ' + tel_ndhiif + ' | '+ opera)
                open('result/valid.txt', 'a').write(bled + ' | ' + tel_ndhif + ' | ' + tel_ndhiif + ' | '+ opera  + '\n')
    except:
        pass

def getstrng(num):
    try:
        if (num[0]=="0") and (len(num)>10):
            num = num.lstrip('0')
        if "+" in num:
            num = num.replace('+', '')
        if "-" in num:
            num = num.replace('-', '')
        if ")" in num:
            num = num.replace(')', '')
        if "(" in num:
            num = num.replace('(', '')
        if "&" in num:
            num = num.replace('&', '')
        if "/" in num:
            num = num.replace('/', '')
        if "=" in num:
            num = num.replace('=', '')
        if " " in num:
            num = num.replace(' ', '')
        if "_" in num:
            num = num.replace('_', '')
        
        return str(num)
    except:
        pass
        

####
try:
	spy =raw_input('Enter Your List :')
	with codecs.open(spy, mode='r', encoding='ascii', errors='ignore') as f:
		ooo = f.read().splitlines()
except IndexError:
	print ('ERROR')
	pass
ooo = list((ooo))
####
try:
    os.mkdir('result')
except:
    pass

def Main():
    try:
        zonum =raw_input('Threads :')
        ThreadPool = Pool(int(zonum))
        Threads = ThreadPool.map(getmail, ooo)
    except:
        pass

if __name__ == '__main__':
	Main()