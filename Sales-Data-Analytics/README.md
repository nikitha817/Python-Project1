Sales Data Analytics

I put together this sales analysis tool to help you dig into your numbers—not just record sales, but actually understand what’s going on with your products and revenue throughout the year. You’ve got everything you need here: crunch numbers with NumPy, track how things grow (or don’t), figure out what’s actually making money, and spot which months or products are dragging you down. It’s not about just storing data; it’s about using it.

What It Does

- Enter sales for five products, month by month, for a whole year.
- Save your work and pick up later (everything goes in a neat JSON file).
- Pull up reports showing your averages, best and worst numbers, broken down by product.
- Run profit analysis—just punch in your profit per unit and see what’s really paying off.
- Check growth rates: see how each product’s sales are changing each month.
- Find your best and worst months at a glance.
- Normalize your numbers, so you’re not comparing apples to oranges when one product dwarfs the others.
- See your sales by product, by month, or the overall picture—however you like.

Features

- Uses NumPy arrays for fast, easy calculations.
- Save and load, so you’re not re-entering data every time.
- All the stats: averages, totals, highs, lows—you pick.
- Profit tracking: see what actually makes you money (and what doesn’t).
- Growth analysis: clear month-to-month percentage changes.
- Quick normalization: everything shrunk to 0–1 scale for fair comparisons.
- A menu-driven system, so you don’t get lost or stuck.
- Built-in error checks (so things don’t fall apart if there’s a typo or missing data).
- Handles 12 months × 5 products—just enough to be real, not overwhelming.

How to Run

Step 1: Install NumPy
pip install numpy

Step 2: Fire it up
python sales_analytics.py

Step 3: Pick your action
1. Enter new sales data
2. Load saved sales data
3. See sales reports
4. Run profit analysis
5. Check growth analysis
6. Look at monthly sales
7. Normalize your numbers
8. Exit

Sample Workflow

So, here’s what it looks like in practice:

You start up the program. It asks what you want to do? Let’s say you pick 1 (Get Sales Data).

- Enter product 1: Laptop
- Enter product 2: Phone
- Enter product 3: Tablet
- Enter product 4: Monitor
- Enter product 5: Keyboard

Now, month by month, plug in your sales:
- For January: Laptop: 50,000 | Phone: 75,000 | ...
- Keep going for all months and products.

Once you're done, you’ll see something like:
==================================================
                Sales Data Analysis
==================================================
Sales of January: [50000. 75000. 30000. 20000. 15000.]

Yearly Sales of each product:
Laptop: 600,000
Phone: 900,000
Tablet: 360,000
Monitor: 240,000
Keyboard: 180,000

And, when you save, the data lands in sales_data.json.

Features Explained

Sales Report
- See the average monthly sales per product.
- Find your highest and lowest months, overall and by product.
- Drill down into one product or one month.
- Spot top/bottom performers.

Profit Analysis
- Add profit per unit for each product.
- Get monthly and yearly profit tallied up.
- See which product actually made you the most (and least) money.

Growth Analysis
- Check growth rates: (Current month - Previous month) / Previous month × 100.
- Get the average growth for each product.
- Quickly spot products that shot up or tanked.

Monthly Sales Analysis
- See sales broken down by month for each product.
- Catch your best-performing months—or the laggards.

Sales Normalization
- Push everything onto the same 0–1 scale, so comparisons actually mean something.
- It’s all done with min-max scaling: (value - min) / (max - min).

What’s Behind the Scenes

- Work with 12 × 5 NumPy arrays (months × products).
- Slice and dice arrays (sum, mean, max, min, by row or column).
- Use the axis parameter to choose: axis=0 (by product), axis=1 (by month).
- Save and reload using JSON (arrays turn into lists and back).
- Handle hiccups, like missing files or odd input.
- Use broadcasting (think: add arrays up in one shot, even if shapes don’t match).
- Safely handle growth rates (watch out for dividing by zero).
- Normalize, index, grab specific data, or combine everything.

Code Structure (Quick Snapshot)

- save_sales_data(products, sales): converts arrays to lists, saves to JSON.
- load_sales_data(): loads JSON, back to arrays.
- get_sales_data(month): prompts for names and sales, gives instant summary.
- report_sales(products, sales): all your stats and details.
- profit_analysis(products, sales): combines sales with profit figures.
- growth_analysis(products, sales): checks month-to-month swings.
- sales_normalization(sales): runs normalization math and shows the results.
- main(): runs the menu and ties everything together.

How Data’s Stored

A simple 12 × 5 matrix (months × products), looking something like:
        Laptop  Phone  Tablet  Monitor  Keyboard
Jan:    [50000, 75000, 30000, 20000, 15000]
Feb:    [52000, 78000, 31000, 21000, 16000]
...
Dec:    [60000, 90000, 40000, 30000, 25000]

Saved in JSON:
{
    "products": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "sales": [
        [50000, 75000, 30000, 20000, 15000],
        [52000, 78000, 31000, 21000, 16000],
        ...
    ]
}

Challenges

- Figuring out NumPy’s axis (row vs column) is a whole thing.
- Entering 60 values by hand: tedious, but it keeps things simple for now.
- Always converting arrays to lists for saving/loading.
- Avoiding errors like dividing by zero when growth stalls.
- Remembering array indices vs months or products as humans think of them.
- Mastering slicing, array math, and broadcasting.
- Rounding results for cleaner, more professional output.

What’s Next?

There’s plenty more this tool could do:
- Friendly data checks (no negative sales!).
- Seasonal analysis (like, do sales always spike in December?).
- Forecasting next month’s numbers.
- Visualization—throw in charts with matplotlib for a better look.
- Export reports to PDFs or Excel sheets.
- Compare quarters (Q1 vs Q2 vs Q3 vs Q4).
- Figure out market share for each product.
- Add moving averages to smooth things out.
- Find relationships between products.
- Import data in bulk, so you’re not mashing numbers in by hand forever.

Why Bother?

This project proves I can:
- Use NumPy for real, not just textbook stuff.
- Handle real, multi-dimensional data and not get lost.
- Actually analyze and make sense of business numbers.
- Deal with saving/loading using JSON.
- Build an interactive program that feels complete.
- Tackle realistic business problems with code that works.

What I Took Away

- Data storage isn’t the finish line; mining insights is what matters.
- NumPy is such a time-saver for calculations.
- Multi-dimensional arrays just make business sense.
- User experience counts—a clear menu is half the battle.
- Business logic—like profit and growth—is what actually drives decisions, not just raw numbers.

This feels more like a piece of actual business software than a class assignment. I’m seeing how real tools start.

A Few Analysis Examples

Sales Report:
Average per product: Laptop: 55,000 | Phone: 82,000 | Tablet: 35,000 | Monitor: 25,000 | Keyboard: 18,000
Best Product: Phone (984,000 total sales)
Worst Product: Keyboard (216,000 total sales)

Profit Analysis:
Profit per unit: [10,000, 15,000, 20,000, 25,000, 30,000]
Total profit:
- Laptop: 5,500,000
- Phone: 12,300,000
- Tablet: 700,000
- Monitor: 625,000
- Keyboard: 5,400,000
Winner: Phone (12,300,000)
Loser: Tablet (700,000)

Growth Analysis:
Growth for Laptop: [0.0, 4.0, 3.85, 2.78, ...] (% changes, month to month)
Growth for Phone: [0.0, 4.0, 2.56, 1.28, ...]
Best growth: Laptop (3.45%)
Lowest: Keyboard (2.15%)

Requirements

- Python 3.6 or newer
- NumPy (pip install numpy)

Next Steps

If I kept going, I’d add:
- Dashboards and graphs (matplotlib, plotly)
- A web interface (Flask or Django)
- Hook up a database for big teams or historical data
- Real-time dashboards that update as sales come in
- Maybe even toss in machine learning for predictions
- Turn it into a mobile app

Honestly, companies rely on tools like this for real decisions. Data analysis isn’t just theory—it’s how businesses stay sharp.

Next up: add visuals or forecasting. That’s where the fun begins.Sales Data Analytics

Here’s a tool I built so you can actually dive into your sales numbers. It’s not just about dumping data somewhere—it's about wrapping your head around what’s selling, where the money’s coming from, and which months or products are slowing you down. I tried to make this really practical: crunch numbers with NumPy, track growth, see what’s profitable, and instantly spot red flags.

So, what can you do with it?

- Enter sales for up to five products, month by month, for the entire year.
- Save everything to a tidy JSON file so you can take a break (and not lose your work).
- Pull up reports with averages, highs, lows, and details by product.
- Plug in profits per unit and see where the money really piles up.
- Track how each product’s sales change every month.
- Instantly spot your best and worst months.
- Normalize your numbers—makes comparisons fair when one product is way bigger than the rest.
- View your data by product, by month, or zoomed out for the big picture.

Features at a Glance

- Fast calculations with NumPy arrays.
- Save and load data whenever you want.
- Get all the stats: averages, totals, peaks, dips—whatever you need.
- Profit analysis: see what products are boosting you (and which are dead weight).
- Growth tracking with clear month-to-month changes.
- Quick normalization (everything between 0 and 1 for real comparisons).
- Simple menu—no getting lost.
- Catches typos or missing data so things don’t fall apart.
- Handles up to 12 months and 5 products—enough to be real, but not overwhelming.

Getting Started

Step 1: Install NumPy
pip install numpy

Step 2: Run the program
python sales_analytics.py

Step 3: Pick what you want to do:
1. Enter new sales data
2. Load saved sales data
3. See sales reports
4. Run profit analysis
5. Check growth analysis
6. Look at monthly sales
7. Normalize your numbers
8. Exit

Typical Workflow

Fire up the program. It’ll ask what you want to do. Let’s say you start with entering sales data.

- Name your products: maybe Laptop, Phone, Tablet, Monitor, Keyboard.
- For each month, plug in sales numbers: January—Laptop: 50,000, Phone: 75,000, and so on.

When you finish, you’ll get an overview like this:
==================================================
Sales Data Analysis
==================================================
Sales for January: [50000. 75000. 30000. 20000. 15000.]

Yearly Sales by Product:
Laptop: 600,000
Phone: 900,000
Tablet: 360,000
Monitor: 240,000
Keyboard: 180,000

Hit save, and your data lands in sales_data.json.

Features Explained

Sales Report
- Average monthly sales for each product.
- Find your strongest and weakest months, both overall and by product.
- Zoom in on any product or month.
- Instantly spot top and bottom performers.

Profit Analysis
- Enter profit per unit for each product.
- See total profit—monthly and yearly.
- Find out which product really pays the bills, and which one isn't worth the trouble.

Growth Analysis
- Monthly growth rates: (Current - Previous) / Previous × 100.
- Average growth by product.
- Quickly see which products are surging (or tanking).

Monthly Sales
- View breakdowns by month for each product.
- Catch your best and worst sales periods in seconds.

Sales Normalization
- Everything gets put on a 0–1 scale, so big and small products actually compare.
- Uses min-max scaling.

Behind the Curtain

- Uses a 12 × 5 NumPy array for months and products.
- Fast operations (sum, mean, max, min) by month or by product.
- Explicit axis control—axis=0 for products, axis=1 for months.
- Saves and loads using JSON, flipping between arrays and lists.
- Handles common headaches: missing files, weird input, dividing by zero on growth rates.
- Broadcasting lets you quickly add or combine arrays.
- Normalization, specific lookups, and slicing all supported.

Code Nutshell

- save_sales_data(products, sales): turns arrays into lists, saves to JSON.
- load_sales_data(): grabs data from file, converts back to arrays.
- get_sales_data(month): asks for names and numbers, spits out a summary.
- report_sales(products, sales): rolls up all the key stats.
- profit_analysis(products, sales): ties sales data to profit per unit.
- growth_analysis(products, sales): checks month-to-month swings.
- sales_normalization(sales): normalizes and displays data.
- main(): ties everything together and runs the menu.

How It Stores Data

Just a basic 12 × 5 grid:
        Laptop  Phone  Tablet  Monitor  Keyboard
Jan:    [50000, 75000, 30000, 20000, 15000]
Feb:    [52000, 78000, 31000, 21000, 16000]
...
Dec:    [60000, 90000, 40000, 30000, 25000]

Saved as JSON:
{
    "products": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "sales": [
        [50000, 75000, 30000, 20000, 15000],
        [52000, 78000, 31000, 21000, 16000],
        ...
    ]
}

What Gets Tricky

- Figuring out NumPy’s axis stuff (row vs column).
- Tediously entering all 60 values—but it keeps things simple for now.
- Flipping arrays to lists to save, then back to arrays when loading.
- Not crashing when someone divides by zero on stalled sales.
- Remembering that months and products in arrays aren’t always how humans think.
- Slicing, math, and broadcasting—easy to trip up.
- Rounding numbers so everything looks clean.

What’s Next?

There’s a ton more to add:
- Smarter checks (no negative sales).
- Seasonal trends (think: December spikes).
- Month-ahead forecasts.
- Graphs and charts with matplotlib.
- Export to PDF or Excel.
- Quarter-to-quarter comparisons.
- See each product’s market share.
- Add moving averages for smoother trends.
- Check for relationships between products.
- Import big batches of data instead of punching numbers in by hand.

Why I Did This

Here’s why this matters:
- NumPy is for much more than homework—it handles real business numbers.
- Managing multi-dimensional data gets much easier.
- Business analysis means finding answers, not just storing more data.
- Saving data with JSON actually works in the wild.
- Built a menu-driven program that anyone can use.
- Wrangled code into a tool that solves real-world business problems.

What I Learned

- Storing numbers isn’t enough—insights are what actually count.
- NumPy saves a lot of time.
- Multi-dimensional arrays just make sense for business data.
- User experience is a big deal—keep menus clear, keep people moving.
- Profit and growth matter way more than just “biggest sales.”

This feels more like actual business software, not just a project. I can see how real tools get started.

Some Example Analyses

Sales Report:
Average per product: Laptop: 55,000 | Phone: 82,000 | Tablet: 35,000 | Monitor: 25,000 | Keyboard: 18,000
Best Product: Phone (984,000 total sales)
Worst Product: Keyboard (216,000 total sales)

Profit Analysis:
Profit per unit: [10,000, 15,000, 20,000, 25,000, 30,000]
Total profit:
- Laptop: 5,500,000
- Phone: 12,300,000
- Tablet: 700,000
- Monitor: 625,000
- Keyboard: 5,400,000
Biggest Winner: Phone (12,300,000)
Biggest Loser: Tablet (700,000)

Growth Analysis:
Growth for Laptop: [0.0, 4.0, 3.85, 2.78, ...] (% change, month to month)
Growth for Phone: [0.0, 4.0, 2.56, 1.28, ...]
Top Growth: Laptop (3.45%)
Lowest: Keyboard (2.15%)

Requirements

- Python 3.6+
- NumPy (pip install numpy)

If I kept going, here’s what I’d add:
- Dashboards and graphs (matplotlib, plotly)
- A web app (Flask, Django)
- Database integration for bigger teams or old records
- Real-time dashboards as sales roll in
- Maybe machine learning for predictions
- A mobile version

Real businesses make decisions off tools like this every day. This isn’t just practice; it’s how companies actually stay on top.

Next up: visuals or forecasting—now that’s the fun part.