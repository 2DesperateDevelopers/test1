from zang import ZangException, Configuration, ConnectorFactory, HttpMethod, TranscriptionStatus
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
import datetime
from zang.domain.enums.transcribe_quality import TranscribeQuality


def outbound_call():

    try:
        configuration = Configuration('AC777c3e328967b139821b44438c8aa3e2', '39355df419f340a5b9bb05e32bf5592a', 'https://api.zang.io/v2')

        connector_factory = ConnectorFactory(configuration)
        calls_connector = connector_factory.callsConnector
        accounts_connector = connector_factory.accountsConnector
        transcriptions_connector = connector_factory.transcriptionsConnector


        account = accounts_connector.viewAccount()
        print('Account Name - ' + account.friendlyName)
        #+919994231238
        call = calls_connector.makeCall(
            to='+919524238952',
            from_='+17142423463',
            url='https://api.zang.io/v2/Accounts/AC777c3e328967b139821b44438c8aa3e2/Agents/DF1b9fc3a7b3dd4e1b8bfd5ed47aed24ed/Xml',
            statusCallback='https://webhook.site/986ee9db-a914-4072-b97c-4d9204fc7632',
            statusCallbackMethod=HttpMethod.GET,

        )

        print(call.sid)



        while True:
            view_call = calls_connector.viewCall(call.sid)
            status = view_call.callStatus
            if status.name == 'COMPLETED' or status.name == 'FAILED'\
                    or status.name == 'BUSY' or status.name == 'NO_ANSWER'\
                    or status.name == 'NO_BALANCE' or status.name == 'REJECTED' \
                    or status.name == 'CANCELED':
                print(str(datetime.datetime.now()) + ' | Call status is - ' + status.name)
                break
            elif status.name == 'IN_PROGRESS' or status.name == 'RINGING':
                print(str(datetime.datetime.now()) + ' | Call status is - ' + status.name)

        print('********************************Call Details************************************')

        print('SID : ' + view_call.sid)
        print('From: ' + view_call.from_)
        print('To: ' + view_call.to)
        print('Duration: ' + str(view_call.duration))
        if view_call.duration != 0:
            print('Start Time : ' + str(view_call.startTime))
            print('End Time : ' + str(view_call.endTime))

        print('********************************Call Details************************************')

    except ZangException as ze:
        print(ze)


if __name__ == '__main__':
    outbound_call()





