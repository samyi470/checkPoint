from django.core.management.base import BaseCommand, CommandError
from checkPointMng.models import Terminal, TerminalThroughput, Airport

import pandas as pd


class Command(BaseCommand):
    help = 'populate database from csv files'

    def handle(self, *args, **options):
        lASAirport = Airport(name='McCarran International Airport', code='LAS')
        lASAirport.save()
        newTerminal = Terminal(name='Terminal1AB', airport=lASAirport)
        newTerminal.save()

        df = pd.read_excel('D:/DjangoProjects/checkPoint/checkPoint/static/terminal_data/terminal_data/LAS_Term 1 - AB.xlsx')
        df['Hour of Day'] = pd.to_datetime(df['Hour of Day'], format='%H:%M').dt.time
        df['Time'] = df['Date'].dt.strftime('%m/%d/%Y').astype('str') + ' ' + df['Hour of Day'].astype('str')
        df['Time'] = pd.to_datetime(df['Time'])

        for index, row in df.iterrows():
            newThroughput = TerminalThroughput(date=row['Time'],
                                               throughput=row['PMIS - Total Customer Throughput (Unadjusted)'],
                                               terminal=newTerminal,
                                               airport=lASAirport)
            newThroughput.save()
            print('currently at', index)
