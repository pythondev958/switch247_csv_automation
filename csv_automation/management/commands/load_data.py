      
from django.core.management.base import BaseCommand
import pandas as pd
from sqlalchemy import create_engine
from csv_automation.models import TestRate, RatingPlan

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'

    def add_arguments(self, parser):
        # Positional mandatory arguments
        parser.add_argument('testrates_csv', type=str, help='Path to the testrates CSV file')
        parser.add_argument('ratingplans_csv', type=str, help='Path to the ratingplans CSV file')

    def handle(self, *args, **options):
        testrates_csv = options['testrates_csv']
        ratingplans_csv = options['ratingplans_csv']

        self.stdout.write(self.style.SUCCESS('Starting to load data...'))
        self.insert_data_from_csv(testrates_csv, TestRate)
        self.insert_data_from_csv(ratingplans_csv, RatingPlan)
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
    
    
    def insert_data_from_csv(self, csv_file, model):
        try:
            df = pd.read_csv(csv_file)

        # Apply column renaming based on the model
            if model == TestRate:
                df.rename(columns={
                    '#Id': 'rate_id',  # Rename from '#Id' to 'id'
                    'DestinationId': 'destination_id',
                    'RatesTag': 'rates_tag',
                    'RoundingMethod': 'rounding_method',
                    'RoundingDecimals': 'rounding_decimals',
                    'MaxCost': 'max_cost',
                    'MaxCostStrategy': 'max_cost_strategy'
                }, inplace=True)
            elif model == RatingPlan:
                df.rename(columns={
                    '#Id': 'plan_id',  # Ensure the name is correct as per your model fields
                    'DestinationRatesId': 'destination_rates_id',
                    'TimingTag': 'timing_tag',
                    'Weight': 'weight'
                }, inplace=True)

        # Log renamed columns for debugging
            print("Processing model:", model.__name__)
            print("Renamed DataFrame columns:", df.columns)

            engine = create_engine('postgresql://postgres:admin@localhost:5432/switch247_csv_automation')
            df.to_sql(model._meta.db_table, engine, if_exists='append', index=False)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
    
    
    # def insert_data_from_csv(self, csv_file, model):
    #     try:
    #         df = pd.read_csv(csv_file)
    #     # Explicitly rename columns here to ensure they match your model's fields
    #         df.rename(columns={
    #             '#Id': 'id',  # Rename from '#Id' to 'id' or whatever your model uses
    #             'DestinationId': 'destination_id',
    #             'RatesTag': 'rates_tag',
    #             'RoundingMethod': 'rounding_method',
    #             'RoundingDecimals': 'rounding_decimals',
    #             'MaxCost': 'max_cost',
    #             'MaxCostStrategy': 'max_cost_strategy'
    #         }, inplace=True)

    #     # Check to see if columns are renamed properly
    #         print("Renamed DataFrame columns:", df.columns)

    #         engine = create_engine('postgresql://postgres:admin@localhost:5432/switch247_csv_automation')
    #         df.to_sql(model._meta.db_table, engine, if_exists='append', index=False)
    #     except Exception as e:
    #         self.stdout.write(self.style.ERROR(f'Error: {e}'))

    # def insert_data_from_csv(self, csv_file, model):
    #     try:
    #         df = pd.read_csv(csv_file)
    #         df.columns = df.columns.str.replace(' ', '_')
    #         engine = create_engine('postgresql://postgres:admin@localhost:5432/switch247_csv_automation')
    #         df.to_sql(model._meta.db_table, engine, if_exists='append', index=False)
    #     except Exception as e:
    #         self.stdout.write(self.style.ERROR(f'Error: {e}'))
    
            
            
            
            
            
            
            
            
            
            
            