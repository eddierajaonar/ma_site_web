"""
# function #1 to generate a HREF for an image 

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# function #2 to generate a HREF for an image 
@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img src="data:images/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code

img = get_img_with_href('images/django-200x200.png', 'https://skillvalue.com/fr/user/certificate/i7N4up4Jc9Hg9Ua6k8A99ywWFu33kripQdHd3UznUDTwvhNVBDKv17Le7Ges')
st.markdown(img, unsafe_allow_html=True)

"""


#affiche liste d'image
#----------------------
#badges = ['images/django-200x200.png','images/SplunkEnterprise_Certified-Admin-600px.png','images/BigData.png','images/hadoop.png']
#st.sidebar.image(badges,width=75)

'''
if option == 'chart':
    symbol = st.sidebar.text_input("Symbol", value='MSFT', max_chars=None, key=None, type='default')

    data = pd.read_sql("""
        select date(day) as day, open, high, low, close
        from daily_bars
        where stock_id = (select id from stock where UPPER(symbol) = %s) 
        order by day asc""", connection, params=(symbol.upper(),))

    st.subheader(symbol.upper())

    fig = go.Figure(data=[go.Candlestick(x=data['day'],
                    open=data['open'],
                    high=data['high'],
                    low=data['low'],
                    close=data['close'],
                    name=symbol)])

    fig.update_xaxes(type='category')
    fig.update_layout(height=700)

    st.plotly_chart(fig, use_container_width=True)

    st.write(data)


if option == 'wallstreetbets':
    num_days = st.sidebar.slider('Number of days', 1, 30, 3)

    cursor.execute("""
        SELECT COUNT(*) AS num_mentions, symbol
        FROM mention JOIN stock ON stock.id = mention.stock_id
        WHERE date(dt) > current_date - interval '%s day'
        GROUP BY stock_id, symbol   
        HAVING COUNT(symbol) > 10
        ORDER BY num_mentions DESC
    """, (num_days,))

    counts = cursor.fetchall()
    for count in counts:
        st.write(count)
    
    cursor.execute("""
        SELECT symbol, message, url, dt, username
        FROM mention JOIN stock ON stock.id = mention.stock_id
        ORDER BY dt DESC
        LIMIT 100
    """)

    mentions = cursor.fetchall()
    for mention in mentions:
        st.text(mention['dt'])
        st.text(mention['symbol'])
        st.text(mention['message'])
        st.text(mention['url'])
        st.text(mention['username'])

    rows = cursor.fetchall()

    st.write(rows)


if option == 'pattern':
    pattern = st.sidebar.selectbox(
        "Which Pattern?",
        ("engulfing", "threebar")
    )

    if pattern == 'engulfing':
        cursor.execute("""
            SELECT * 
            FROM ( 
                SELECT day, open, close, stock_id, symbol, 
                LAG(close, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_close, 
                LAG(open, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_open 
                FROM daily_bars
                JOIN stock ON stock.id = daily_bars.stock_id
            ) a 
            WHERE previous_close < previous_open AND close > previous_open AND open < previous_close
            AND day = '2021-02-18'
        """)

    if pattern == 'threebar':
        cursor.execute("""
            SELECT * 
            FROM ( 
                SELECT day, close, volume, stock_id, symbol, 
                LAG(close, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_close, 
                LAG(volume, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_volume, 
                LAG(close, 2) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_close, 
                LAG(volume, 2) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_volume, 
                LAG(close, 3) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_previous_close, 
                LAG(volume, 3) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_previous_volume 
            FROM daily_bars 
            JOIN stock ON stock.id = daily_bars.stock_id) a 
            WHERE close > previous_previous_previous_close 
                AND previous_close < previous_previous_close 
                AND previous_close < previous_previous_previous_close 
                AND volume > previous_volume 
                AND previous_volume < previous_previous_volume 
                AND previous_previous_volume < previous_previous_previous_volume 
                AND day = '2021-02-19'
        """)

    rows = cursor.fetchall()

    for row in rows:
        st.image(f"https://finviz.com/chart.ashx?t={row['symbol']}")


if option == 'stocktwits':
    symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)

    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")

    data = r.json()

    for message in data['messages']:
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])
'''

'''
    logo = ["python","spark","hadoop-logo","kafka", "bash-linux", "sql", "javascript", "splunk", "powerbi", "docker"]
    valuesA = [80, 40, 40, 50, 75, 50, 40, 75, 40, 45]
    
    fig, ax = plt.subplots(figsize=(300,300))

    ax.bar(range(len(logo)), valuesA, width=0.5,align="center")
    ax.set_xticks(range(len(logo)))
    ax.set_xticklabels(logo)
    ax.tick_params(axis='x', which='major', pad=26)

    for i, c in enumerate(logo):
        offset_image(i, c, ax)

    st.pyplot(fig)
'''