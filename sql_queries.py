
############ COUNTRY ######################
country_create_table = ("""
CREATE TABLE IF NOT EXISTS country(
       country_code VARCHAR NOT NULL PRIMARY KEY,
       short_name VARCHAR NOT NULL,
       medium_name VARCHAR NOT NULL,
       long_name VARCHAR,
       alpha2_code VARCHAR,
       currency_unit VARCHAR NOT NULL,
       region VARCHAR,
       income_group VARCHAR,
       wb2_code VARCHAR NOT NULL,
       national_account_Base INT,
       Sna_price_valuation VARCHAR,
       system_national_accounts VARCHAR,
       balance_pay_manual VARCHAR,
       system_trade VARCHAR,
       gov_account_concept VARCHAR,
       imf_data VARCHAR,
       latest_pop_census INT,
       latest_industrial_data INT,
       latest_trade_data INT,
       latest_water_with_Data INT
       )
""")


################# COUNTRYNOTES #######################
cnotes_create_table = ("""
CREATE TABLE IF NOT EXISTS country_notes(
       country_code VARCHAR NOT NULL,
       series_code VARCHAR NOT NULL,
       description VARCHAR,
       CONSTRAINT PK_Cnotes PRIMARY KEY (country_code,series_code)
       )
""")

################# FOOTNOTES #######################
fnotes_create_table = ("""
CREATE TABLE IF NOT EXISTS foot_notes(
       country_code VARCHAR NOT NULL,
       series_code VARCHAR NOT NULL,
       year VARCHAR NOT NULL,
       description VARCHAR,
       CONSTRAINT PK_Fnotes PRIMARY KEY (country_code,year)
       )
""")
################# INDICATOR #######################
indicator_create_table = ("""
CREATE TABLE IF NOT EXISTS indicator(
       country_name  VARCHAR NOT NULL,
       country_code VARCHAR NOT NULL,
       indicator_name VARCHAR NOT NULL,
       indicator_code VARCHAR NOT NULL,
       year INT,
       value FLOAT,
       CONSTRAINT PK_indicator PRIMARY KEY (indicator_code,country_code)
       )
""")

################# SERIES #######################

series_create_table = ("""
CREATE TABLE IF NOT EXISTS series(
       series_code VARCHAR NOT NULL PRIMARY KEY,
       topic VARCHAR,
       indicator_name VARCHAR NOT NULL,
       long_definition VARCHAR,
       periodicity VARCHAR,
       source VARCHAR,
       license_type VARCHAR
       ) 
""")


################# SERIESNOTES #######################

snotes_create_table = ("""
CREATE TABLE IF NOT EXISTS series_notes(
       series_code VARCHAR NOT NULL,
       year VARCHAR NOT NULL,
       description VARCHAR,
       CONSTRAINT PK_snotes PRIMARY KEY (year,series_code)
       )
""")



getStruct=("""                            
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = %s;
""")