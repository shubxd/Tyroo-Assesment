import pandas as pd
import os
from django.core.management.base import BaseCommand

from products.models import Brand, Categories, Product



class Command(BaseCommand):

    cwd = os.getcwd()

    def handle(self, *args, **kwargs):
        brand_df = pd.read_csv(self.cwd+"/data_csv/brands.csv")
        categories_df = pd.read_csv(self.cwd+"/data_csv/categories.csv")
        products_df = pd.read_csv(self.cwd+"/data_csv/products.csv")

        for i in brand_df['name']:
            Brand.objects.create(name = i)
        
        for i in range(len(categories_df)):
            Categories.objects.create(
                **{
                    "name": categories_df.loc[i,'name'],
                    "type": categories_df.loc[i,'type'],
                }
            )
        products_df['brand'] = products_df.brand.apply(lambda x: Brand.objects.get(id=x))
        products_df['type'] = products_df.type.apply(lambda x: Categories.objects.get(id=x))
        
        for i in range(len(products_df)):
            Product.objects.create(
                **{
                    "name": products_df.loc[i, 'name'],
                    "brand": products_df.loc[i, 'brand'],
                    "price": products_df.loc[i, 'price'],
                    "description": products_df.loc[i, 'description'],
                    "type": products_df.loc[i, 'type'],
                    "stock": products_df.loc[i, 'stock'],
                }
            )



