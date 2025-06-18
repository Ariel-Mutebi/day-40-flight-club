import os
import smtplib

SMTP_PORT = 587 # Apparently, my ISP blocked port 25.

class Announcer:
        def __init__(self):
                self._SMTP_SENDER = os.environ.get("SMTP_SENDER")
                self._SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

        def announce(self, mailing_list, historical_price, price, departure_airport, destination_airport, outbound_date, inbound_date, number_of_stops):
                with open("email_template.txt") as email_template:
                        email_body = email_template.read()
                        email_body = email_body.replace("[DEPARTURE_AIRPORT]", departure_airport)
                        email_body = email_body.replace("[DESTINATION_AIRPORT]", destination_airport)
                        email_body = email_body.replace("[HISTORICAL_PRICE]", str(historical_price))
                        email_body = email_body.replace("[PRICE]", str(price))
                        email_body = email_body.replace("[OUTBOUND_DATE]", outbound_date)
                        email_body = email_body.replace("[INBOUND_DATE]", inbound_date)
                        email_body = email_body.replace("[NUMBER_OF_STOPS]", str(number_of_stops))

                with smtplib.SMTP("smtp.gmail.com", SMTP_PORT) as connection:
                        connection.starttls()
                        connection.login(user=self._SMTP_SENDER, password=self._SMTP_PASSWORD)
                        for email_address in mailing_list:
                                connection.sendmail(
                                        from_addr=self._SMTP_SENDER,
                                        to_addrs=email_address,
                                        msg=f"Subject: Affordable Flight Deal Found!\n\n" + email_body
                                )