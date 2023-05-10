import matplotlib.pyplot as plt
import pandas as pd
import AvgPriceperCat, ImageRatio, MonthlyRevenueperCat, MonthlySalesperCat, RevenueperPrice, ReviewperCat, SalesperCategory, SalesperPrice, SalesperReview, SellerperCat, SellerperMonthlySales, SellersperPrice

fig = plt.figure(figsize=(20, 20))

plots = [AvgPriceperCat(), ImageRatio(), MonthlyRevenueperCat(), MonthlySalesperCat(),
         RevenueperPrice(), ReviewperCat(), SalesperCategory(), SalesperPrice(),
         SalesperReview(), SellerperCat(), SellerperMonthlySales(), SellersperPrice()]

for i, plot in enumerate(plots, start=1):
    ax = fig.add_subplot(4, 3, i)
    plot.plot(ax)
  
plt.tight_layout()
plt.show()
