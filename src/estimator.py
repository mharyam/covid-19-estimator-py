import math


def get_period_days(period_type, period_days):
    if period_type.lower() == 'days':
      return period_days
    elif period_type.lower() == 'weeks':
      return period_days * 7
    elif period_type.lower() == 'months':
      return period_days * 30
    return "Invalid Period Type"


def available_beds(total_hospital_beds):
    return int(0.35 * (total_hospital_beds))


def estimator(input_data):
    num_of_days = get_period_days(input_data.get('periodType'), input_data.get('timeToElapse'))
    num_of_days = int(num_of_days / 3)
    reportedCases = int(input_data.get('reportedCases'))
    total_hospital_beds = int(input_data.get('totalHospitalBeds'))
    output_data = {}
    impact = {}
    severe_impact = {}

    currently_infected_impact = reportedCases * 10
    infections_by_requested_time_impact = int(currently_infected_impact * math.pow(2, num_of_days))
    severe_cases_by_req_time_impact = int (0.15 * infections_by_requested_time_impact)
    hospital_beds_by_requested_time_impact = int(available_beds(total_hospital_beds) - severe_cases_by_req_time_impact)

    currently_infected_severe_impact = reportedCases * 50
    infections_by_requested_time_severe_impact = int(currently_infected_severe_impact * math.pow(2, num_of_days))
    severe_cases_by_req_time_severe_impact = int(0.15 * infections_by_requested_time_severe_impact)
    hospital_beds_by_requested_time_severe_impact = int(available_beds(total_hospital_beds) - severe_cases_by_req_time_severe_impact)
    
    impact['currentlyInfected'] = currently_infected_impact
    impact['infectionsByRequestedTime'] = infections_by_requested_time_impact
    impact['severeCasesByRequestedTime'] = float(severe_cases_by_req_time_impact)
    impact['hospitalBedsByRequestedTime'] = float(hospital_beds_by_requested_time_impact)
    severe_impact['currentlyInfected'] = currently_infected_severe_impact
    severe_impact['infectionsByRequestedTime'] = infections_by_requested_time_severe_impact
    severe_impact['severeCasesByRequestedTime'] = float(severe_cases_by_req_time_severe_impact)
    severe_impact['hospitalBedsByRequestedTime'] = float(hospital_beds_by_requested_time_severe_impact)

    output_data['data'] = input_data
    output_data['impact'] = impact
    output_data['severeImpact'] = severe_impact
    return output_data