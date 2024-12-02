from data import CountyDemographics

#Part 1
#the function iterates each county in the counties list and adds the population from 2014 to get the total
#input: A list of CountyDemographics objects with a dictionary population with a '2014 Population' key
#output: The sum of the 2014 populations of all counties in the list
def population_total(counties: list[CountyDemographics]) -> int:
    total_population = 0
    for county in counties:
        total_population += county.population['2014 Population']
    return total_population


#Part 2
#the function iterates through the counties list, check if each county's state matches the given state abbreviation (s_abbre)
#If they match, the county is added to the result list
#input: A list of CountyDemographics objects and A string representing the state abbreviation
#output:A list of CountyDemographics objects
def filter_by_state(counties: list[CountyDemographics], s_abbre: str) -> list[CountyDemographics]:
    list_of_county = []
    for county in counties:
        if county.state == s_abbre:
            list_of_county.append(county)
    return list_of_county


#Part 3
#The function calculates the total population for the given education level
#input: A list of CountyDemographics objects where each contains the population data and education level percentages
#output: A string (such as "Bachelor's Degree or Higher")
def population_by_education(counties: list[CountyDemographics], education: str) -> float:
    total_population = 0.0
    for county in counties:
        if education in county.education:
            percentage = county.education[education]
            total_population += county.population['2014 Population'] * (percentage / 100)
    return total_population


#The function calculates the total population of a specified ethnicity across a list of counties
#input: A list of CountyDemographics objects that contain population and ethnicity data for each county and
#A string representing the specific ethnicity
#output: A float, the sum of the populations of the specified ethnicity
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_population = 0.0
    for county in counties:
        if ethnicity in county.ethnicities:
            percentage = county.ethnicities[ethnicity]
            total_population += county.population['2014 Population'] * (percentage / 100)
    return total_population


#The function calculates the total population living below the poverty level across a list of counties
#input: A list of CountyDemographics objects that contains demographic and income data for a county
#output: A float, the total population of all counties living below the poverty level
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_below_poverty = 0.0
    for county in counties:
        poverty_percentage = county.income.get('Persons Below Poverty Level', 0)
        population_2014 = county.population.get('2014 Population', 0)
        total_below_poverty += population_2014 * (poverty_percentage / 100)
    return total_below_poverty


#Part 4
#It calculates the percent of the population with a specific level of education across a list of counties
#input: A list of CountyDemographics objects
#output: A string, the education level to calculate the percent
def percent_by_education(counties: list[CountyDemographics], education: str) -> float:
    total_population = 0.0
    total_sub_population = 0.0
    for county in counties:
        total_population += county.population['2014 Population']
        total_sub_population += population_by_education([county], education)
    if total_population == 0:
        return 0.0
    return (total_sub_population / total_population) * 100


#It calculates the percent of the total population across a list of counties that belongs to a specific ethnicity
#input: A list of CountyDemographics objects
#output: A float, the percent of the total population across all counties that belongs to the specified ethnicity
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_population = 0.0
    total_ethnicity_population = 0.0
    for county in counties:
        if ethnicity in county.ethnicities:
            ethnicity_percentage = county.ethnicities[ethnicity]
            population_2014 = county.population['2014 Population']
            total_ethnicity_population += population_2014 * (ethnicity_percentage / 100)
        total_population += county.population['2014 Population']
    if total_population == 0:
        return 0.0
    percentage = (total_ethnicity_population / total_population) * 100
    return percentage


#It calculates the percent of the total population of a list of counties that is living below the poverty level.
#input: : A list of CountyDemographics objects
#output: A float,the percent of the total population living below the poverty level across all the counties
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population_below_poverty = 0.0
    total_population = 0.0
    for county in counties:
        population_2014 = county.population.get('2014 Population')
        poverty_percentage = county.income.get('Persons Below Poverty Level')
        total_population_below_poverty += population_2014 * (poverty_percentage / 100)
        total_population += population_2014
    if total_population == 0:
        return 0.0
    return (total_population_below_poverty / total_population) * 100


#Part 5
#It returns a list of counties where the percent of people with a specified level of education is greater than a given threshold
#input: A list of CountyDemographics objects, a string (the education level key), a float (the percentage threshold)
#output: A list of CountyDemographics objects where the percent of people with the specified education
# level is greater than the provided threshold
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
    CountyDemographics]:
    result = []
    for county in counties:
        if education_key in county.education:
            if county.education[education_key] > threshold:
                result.append(county)
    return result


#It returns a list of counties where the percent of people with a specified level of education is less than a given threshold
#input: A list of CountyDemographics objects, a string(the education level key), a float(the percentage threshold)
#output: A list of CountyDemographics objects where the percent of people with the specified
#education level is less than the provided threshold
def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
    CountyDemographics]:
    result = []
    for county in counties:
        if education_key in county.education:
            if county.education[education_key] < threshold:
                result.append(county)
    return result


#It returns a list of counties where the percent of a specified ethnicity is greater than a given threshold
#input: A list of CountyDemographics objects, a string (ethnicity key), a float (the percentage threshold)
#output: A list of CountyDemographics objects where the percent of the specified ethnicity is greater than the provided threshold
def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[
    CountyDemographics]:
    result = []
    for county in counties:
        if ethnicity_key in county.ethnicities:
            if county.ethnicities[ethnicity_key] > threshold:
                result.append(county)
    return result


#It returns a list of counties where the percent of a specified ethnicity is less than a given threshold
#input: A list of CountyDemographics objects, a string(the ethnicity), a float(the percentage threshold)
#output: A list of CountyDemographics objects where the percent of the specified ethnicity is less than the given threshold
def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[
    CountyDemographics]:
    result = []
    for county in counties:
        if ethnicity_key in county.ethnicities:
            if county.ethnicities[ethnicity_key] < threshold:
                result.append(county)
    return result


#It returns a list of counties where the percent of people living below the poverty level is greater than a given threshold
#input: A list of CountyDemographics objects and a float, the poverty level percentage threshold
#output: A list of CountyDemographics objects, percent of people living below the poverty level is greater than the given threshold
def below_poverty_level_greater_than(counties: list, threshold: float) -> list:
    result = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            result.append(county)
    return result


#It returns a list of counties where the percent of people living below the poverty level is less than a given threshold
#input: A list of CountyDemographics objects and a float, the poverty level percentage threshold
#output: A list of CountyDemographics objects
# (the percent of people living below the poverty level is less than the given threshold)
def below_poverty_level_less_than(counties: list, threshold: float) -> list:
    result = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            result.append(county)
    return result