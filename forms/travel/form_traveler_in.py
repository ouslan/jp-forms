from sqlmodel import Field, SQLModel, Session
from typing import Optional
import datetime

class TravelerTable(SQLModel, table=True):
    # Section 1: Traveler Information
    id: Optional[int] = Field(default=None, primary_key=True)
    time: datetime = Field(default_factory=datetime.now)
    status_id: int = Field(int, foreign_key="statustable.id")
    age: int
    gender_id: int = Field(int, foreign_key="gendertable.id")
    racial_origin_id: int = Field(int, foreign_key="racialorigintable.id")
    hispanic_id: int = Field(int, foreign_key="hispanictable.id")
    education_id: int = Field(int, foreign_key="educationtable.id")
    travel_companion_id: int = Field(int, foreign_key="travelcompaniontable.id")
    traveler_number: int
    destination_id: int = Field(int, foreign_key="destinationtable.id") # TODO: get data ISO date from the Linux library
    lodging_id: int = Field(int, foreign_key="lodgingtable.id")
    state_id: int = Field(int, foreign_key="statetable.id")
    city: ...
    principal_purpose_id: ...
    activity_id: ...
    travel_stay: int
    expense_est: int # WARNING: It is important to specify the currency is this in local currency or in USD or in the traveler's currency?
    spend_category_id: ... # NOTE: this needs more documentation to understand. wdym by category? How is this a interval variable 1-6. What is 1 and what is 6?

class StatusTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class GenderTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class RacialOriginTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class HispanicTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class EducationTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class TravelCompanionTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class DestinationTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    iso_code: str

class LodgingTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class PrincipalPurposeTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class ActivityTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

class SpendCategoryTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

def create_trade(engine):
    # add static status data
    status_1 = StatusTable(id=1, name="guest")
    status_2 = StatusTable(id=2, name="resident")

    # Add static gender data
    gender_1 = GenderTable(id=1, name="female")
    gender_2 = GenderTable(id=2, name="male")
    gender_3 = GenderTable(id=3, name="transgender")
    gender_4 = GenderTable(id=4, name="gender_fluid")
    gender_5 = GenderTable(id=98, name="other")
    gender_6 = GenderTable(id=99, name="no_response")

    # Add static racial origin data
    racial_origin_1 = RacialOriginTable(id=1, name="white")
    racial_origin_2 = RacialOriginTable(id=2, name="black")
    racial_origin_3 = RacialOriginTable(id=3, name="afroamerican")
    racial_origin_4 = RacialOriginTable(id=4, name="native_american")
    racial_origin_5 = RacialOriginTable(id=5, name="asian")
    racial_origin_6 = RacialOriginTable(id=6, name="mediterranean")
    racial_origin_7 = RacialOriginTable(id=98, name="other")
    racial_origin_8 = RacialOriginTable(id=99, name="no_response")

    # Add static hispanic data
    hispanic_1 = HispanicTable(id=1, name="puerto_rico")
    hispanic_2 = HispanicTable(id=2, name="dominican_republican")
    hispanic_3 = HispanicTable(id=3, name="cuba")
    hispanic_4 = HispanicTable(id=4, name="colombia")
    hispanic_5 = HispanicTable(id=5, name="mexico")
    hispanic_6 = HispanicTable(id=6, name="latam")
    hispanic_7 = HispanicTable(id=7, name="no")
    hispanic_8 = HispanicTable(id=98, name="other")
    hispanic_9 = HispanicTable(id=99, name="no_response")

    # Add static education data
    education_1 = EducationTable(id=1, name="no_primary")
    education_2 = EducationTable(id=2, name="primary")
    education_3 = EducationTable(id=3, name="secondary")
    education_4 = EducationTable(id=4, name="technical")
    education_5 = EducationTable(id=5, name="bachelor")
    education_6 = EducationTable(id=6, name="postgraduate")

    # Add static travel companion data
    travel_companion_1 = TravelCompanionTable(id=1, name="alone")
    travel_companion_2 = TravelCompanionTable(id=2, name="friends")
    travel_companion_3 = TravelCompanionTable(id=3, name="family")
    travel_companion_4 = TravelCompanionTable(id=4, name="group")

    # Add static lodging data
    lodging_1 = LodgingTable(id=1, name="hotel")
    lodging_2 = LodgingTable(id=2, name="airbnb")
    lodging_3 = LodgingTable(id=3, name="family_friends_house")
    lodging_4 = LodgingTable(id=4, name="own_house")
    lodging_5 = LodgingTable(id=99, name="other")

    with Session(engine) as session:
        session.add_all([status_1, status_2])

        session.add_all([
            gender_1, gender_2,
            gender_3, gender_4,
            gender_5, gender_6])

        session.add_all([
            racial_origin_1, racial_origin_2,
            racial_origin_3, racial_origin_4,
            racial_origin_5, racial_origin_6,
            racial_origin_7, racial_origin_8])

        session.add_all([
            hispanic_1, hispanic_2,
            hispanic_3, hispanic_4,
            hispanic_5, hispanic_6,
            hispanic_7, hispanic_8,
            hispanic_9])

        session.add_all([
            education_1, education_2,
            education_3, education_4,
            education_5, education_6])

        session.add_all([
            travel_companion_1, travel_companion_2,
            travel_companion_3, travel_companion_4])
        
        session.add_all([
            lodging_1, lodging_2,
            lodging_3, lodging_4,
            lodging_5])

        session.commit()
