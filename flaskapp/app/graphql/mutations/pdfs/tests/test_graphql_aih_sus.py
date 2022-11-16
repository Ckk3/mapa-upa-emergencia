from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import datetime
from flask import Response
from app.env import GRAPHQL_MUTATION_QUERY_URL


global lenght_test
lenght_test = ''
for x in range(0, 1100):
    lenght_test += str(x)

datetime_to_use = datetime.datetime.now().strftime('%d/%m/%Y')

# Select your transport with ag graphql url endpoint
transport = AIOHTTPTransport(url=GRAPHQL_MUTATION_QUERY_URL)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def data_to_use(establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,establishment_exec_name='Establshment Exec Name',establishment_exec_cnes=7654321,patient_name='Patient Name',patient_cns="928976954930007",patient_birthday=datetime_to_use,patient_sex='F',patient_mother_name='Patient Mother Name',patient_adress='Patient Adress street neighobourd',patient_adress_city='Patient City',patient_adress_city_ibge_code='1234567', patient_adress_uf='SP',patient_adress_cep='12345678',main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',initial_diagnostic='Patient Initial Diagnostic',principal_cid_10="A00",procedure_solicited='Procedure Solicited',procedure_code='1234567890', clinic='Clinic Name', internation_carater='Internation Carater', prof_solicitor_document='{cns: "928976954930007", cpf: null, rg: null}',
prof_solicitor_name='Profissional Solicit Name', solicitation_datetime=datetime_to_use, prof_autorization_name='Autorization professional name', emission_org_code='OrgCode2022', autorizaton_prof_document='{cns: null, cpf: "28445400070", rg: null}', autorizaton_datetime=datetime_to_use,hospitalization_autorization_number='1234567890',exam_results='Xray tibia broken',chart_number='1234',patient_ethnicity='Preta', patient_responsible_name='Patient Responsible Name', patient_mother_phonenumber='5613248546', patient_responsible_phonenumber='8564721598', secondary_cid_10='A01',cid_10_associated_causes='A02',acident_type='work_path', insurance_company_cnpj='37549670000171', insurance_company_ticket_number='123450123456', insurance_company_series='Insurn',company_cnpj='37549670000171', company_cnae=5310501, company_cbor=123456, pension_status='not_insured'):

    request_string = """
        mutation{
            generatePdf_AihSus("""

    campos_string = f"""
    establishmentSolitcName: "{establishment_solitc_name}",
    establishmentSolitcCnes: {establishment_solitc_cnes},
    establishmentExecName: "{establishment_exec_name}",
    establishmentExecCnes: {establishment_exec_cnes},
    patientName: "{patient_name}",
    patientCns: "{patient_cns}",
    patientBirthday: "{patient_birthday}",
    patientSex: "{patient_sex}",
    patientMotherName: "{patient_mother_name}",
    patientAdress: "{patient_adress}",
    patientAdressCity: "{patient_adress_city}",
    patientAdressCityIbgeCode: "{patient_adress_city_ibge_code}",
    patientAdressUF: "{patient_adress_uf}",
    patientAdressCEP: "{patient_adress_cep}"
    mainClinicalSignsSymptoms: "{main_clinical_signs_symptoms}",
    conditionsJustifyHospitalization: "{conditions_justify_hospitalization}",
    initialDiagnostic: "{initial_diagnostic}",
    principalCid10: "{principal_cid_10}",
    procedureSolicited: "{procedure_solicited}",
    procedureCode: "{procedure_code}",
    clinic: "{clinic}",
    internationCarater: "{internation_carater}",
    profSolicitorDocument: {prof_solicitor_document},
    profSolicitorName: "{prof_solicitor_name}",
    solicitationDatetime: "{solicitation_datetime}",
    profAutorizationName: "{prof_autorization_name}",
    emissionOrgCode: "{emission_org_code}",
    autorizatonProfDocument: {autorizaton_prof_document}
    autorizatonDatetime: "{autorizaton_datetime}",
    hospitalizationAutorizationNumber: "{hospitalization_autorization_number}",
    examResults: "{exam_results}",
    chartNumber: "{chart_number}",
    patientEthnicity: "{patient_ethnicity}",
    patientResponsibleName: "{patient_responsible_name}",
    patientMotherPhonenumber: "{patient_mother_phonenumber}",
    patientResponsiblePhonenumber: "{patient_responsible_phonenumber}",
    secondaryCid10: "{secondary_cid_10}",
    cid10AssociatedCauses: "{cid_10_associated_causes}",
    acidentType: "{acident_type}",
    insuranceCompanyCnpj: "{insurance_company_cnpj}",
    insuranceCompanyTicketNumber: "{insurance_company_ticket_number}",
    insuranceCompanySeries: "{insurance_company_series}",
    companyCnpj: "{company_cnpj}",
    companyCnae: {company_cnae},
    companyCbor: {company_cbor},
    pensionStatus: "{pension_status}"
    """

    final_string = """
    ){base64Pdf}
    }
    """
    all_string = request_string + campos_string + final_string
    query = gql(all_string)
    try:
        #When some exception is created in grphql he return a error
        client.execute(query)
        return True
    except:
        return False 

#Testing Aih SU
def test_with_data_in_function():
    assert data_to_use() == True

def test_answer_with_all_fields():
    assert data_to_use() == True

def test_awnser_with_only_required_data():
    assert type(pdf_aih_sus.fill_pdf_aih_sus(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        establishment_exec_name='Establshment Exec Name',
        establishment_exec_cnes=7654321,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_birthday=datetime_to_use,
        patient_sex='F',
        patient_mother_name='Patient Mother Name',
        patient_adress='Patient Adress street neighobourd',
        patient_adress_city='Patient City',
        patient_adress_city_ibge_code=1234567,
        patient_adress_uf='SP',
        patient_adress_cep=12345678,
        main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",
        conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',
        initial_diagnostic='Patient Initial Diagnostic',
        principalCid10="A00",
        procedure_solicited='Procedure Solicited',
        procedure_code='1234567890', 
        clinic='Clinic Name', 
        internation_carater='Internation Carater', 
        profSolicitorDocument={'CNS':928976954930007},
        prof_solicitor_name='Profissional Solicit Name', 
        solicitation_datetime=datetime_to_use, 
        autorization_prof_name='Autorization professional name', 
        emission_org_code='OrgCode2022', 
        autorizaton_prof_document={'CPF':28445400070}, 
        autorizaton_datetime=datetime_to_use,
        hospitalization_autorization_number=1234567890
        )) != type(Response())
    

##############################################################
# ERRORS IN NAMES CAMPS
# establishment_exec_name
# establishment_solitc_name
# patient_name
# patient_mother_name
# prof_solicitor_name
# autorization_prof_name
# patient_responsible_name
# !!!!!!! TESTING !!!!!!!
# Name empty
# Name with space
# long name
# short name
# wrong name type

def test_empty_establishment_solitcname():    
    assert data_to_use(establishment_solitc_name='').status == Response(status=400).status

def test_with_space_establishment_solitcname():    
    assert data_to_use(establishment_solitc_name='  ').status == Response(status=400).status

def test_long_establishment_solitcname():    
    assert data_to_use(establishment_solitc_name=lenght_test[:84]).status == Response(status=400).status

def test_short_establishment_solitcname():    
    assert data_to_use(establishment_solitc_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_solitcname():    
    assert data_to_use(establishment_solitc_name=123124).status == Response(status=400).status

def test_empty_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='').status == Response(status=400).status

def test_with_space_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='  ').status == Response(status=400).status

def test_long_establishment_exec_name():    
    assert data_to_use(establishment_exec_name=lenght_test[:84]).status == Response(status=400).status

def test_short_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_exec_name():    
    assert data_to_use(establishment_exec_name=123124).status == Response(status=400).status

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name=lenght_test[:81]).status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_mother_name():    
    assert data_to_use(patient_mother_name='').status == Response(status=400).status

def test_with_space_patient_mother_name():    
    assert data_to_use(patient_mother_name='  ').status == Response(status=400).status

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name=lenght_test[:75]).status == Response(status=400).status

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='bro').status == Response(status=400).status

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124).status == Response(status=400).status
    
def test_empty_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='').status == Response(status=400).status

def test_with_space_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='  ').status == Response(status=400).status

def test_long_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=lenght_test[:51]).status == Response(status=400).status

def test_short_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitor_name():    
    assert data_to_use(prof_solicitor_name=123124).status == Response(status=400).status

def test_empty_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='').status == Response(status=400).status

def test_with_space_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='  ').status == Response(status=400).status

def test_long_autorization_prof_name():    
    assert data_to_use(autorization_prof_name=lenght_test[:52]).status == Response(status=400).status

def test_short_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='bro').status == Response(status=400).status

def test_wrongtype_autorization_prof_name():    
    assert data_to_use(autorization_prof_name=123124).status == Response(status=400).status

def test_empty_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='')) != Response(status=400).status

def test_with_space_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='  ')) != Response(status=400).status

def test_long_patient_responsible_name():    
    assert data_to_use(patient_responsible_name=lenght_test[:72]).status == Response(status=400).status

def test_short_patient_responsible_name():    
    assert data_to_use(patient_responsible_name='bro').status == Response(status=400).status

def test_wrongtype_patient_responsible_name():    
    assert data_to_use(patient_responsible_name=123124).status == Response(status=400).status


####################################################################
# TEST CNES 
# establishment_solitc_cnes
# establishment_exec_cnes
# empty
# wrong type
# invalid cnes

def test_empty_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes='').status == Response(status=400).status

def test_wrongtype_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes='adsadad').status == Response(status=400).status

def test_invalidcnes_establishment_solitc_cnes():
    assert data_to_use(establishment_solitc_cnes=451236548).status == Response(status=400).status

def test_empty_establishment_exec_cnes():
    assert data_to_use(establishment_exec_cnes='').status == Response(status=400).status

def test_wrongtype_establishment_exec_cnes():
    assert data_to_use(establishment_exec_cnes='adsadad').status == Response(status=400).status

def test_invalidcnes_establishment_exec_cnes():
    assert data_to_use(establishment_exec_cnes=451236548).status == Response(status=400).status

#################################################################
#TEST DOCUMENTS CNS AND CPF
#patient_cns
#prof_solicitor_document
#autorizaton_prof_document
# wrong type
# invalid cns
# invalid cpf
# wrong option

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='451236548').status == Response(status=400).status

def test_invalid_patient_cns():
    assert data_to_use(patient_cns=451236548554).status == Response(status=400).status

def test_wrongtype_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document='451236548554').status == Response(status=400).status

def test_invalidcns_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'CNS':284123312123}).status == Response(status=400).status

def test_invalidccpf_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'CPF':284123312123}).status == Response(status=400).status

def test_wrongoption_prof_solicitor_document():
    assert data_to_use(prof_solicitor_document={'BBB':284123312123}).status == Response(status=400).status

def test_wrongtype_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document='451236548554').status == Response(status=400).status

def test_invalidcns_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document={'CNS':284123312123}).status == Response(status=400).status

def test_invalidccpf_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document={'CPF':284123312123}).status == Response(status=400).status

def test_wrongoption_autorizaton_prof_document():
    assert data_to_use(autorizaton_prof_document={'BBB':284123312123}).status == Response(status=400).status



#################################################################
# TEST DATETIMES VARIABLES
# patient_birthday
# solicitation_datetime
# autorizaton_datetime
# test wrong type
# test valid datetime

def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_valid_patient_birthday():
    assert type(data_to_use(patient_birthday=datetime_to_use)) != type(Response())

def test_wrongtype_solicitation_datetime():
    assert data_to_use(solicitation_datetime='bahabah').status == Response(status=400).status

def test_valid_solicitation_datetime():
    assert type(data_to_use(solicitation_datetime=datetime_to_use)) != type(Response())

def test_wrongtype_autorizaton_datetime():
    assert data_to_use(autorizaton_datetime='bahabah').status == Response(status=400).status

def test_valid_autorizaton_datetime():
    assert type(data_to_use(autorizaton_datetime=datetime_to_use)) != type(Response())

##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# acident_type
# pension_status
# patient_adress_uf
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

def test_wrongtype_patient_sex():
    assert data_to_use(patient_sex=1231).status == Response(status=400).status

def test_notexistopiton_patient_sex():
    assert data_to_use(patient_sex='G').status == Response(status=400).status

def test_M_optionUpper_patient_sex():
    assert type(data_to_use(patient_sex='M')) != type(Response())

def test_M_optionLower_patient_sex():
    assert type(data_to_use(patient_sex='m')) != type(Response())

def test_F_optionUpper_patient_sex():
    assert type(data_to_use(patient_sex='F')) != type(Response())

def test_F_optionLower_patient_sex():
    assert type(data_to_use(patient_sex='f')) != type(Response())

def test_wrongtype_acident_type():
    assert data_to_use(acident_type=1231).status == Response(status=400).status

def test_notexistopiton_acident_type():
    assert data_to_use(acident_type='adadsda').status == Response(status=400).status

def test_work_option_acident_type():
    assert type(data_to_use(acident_type='work')) != type(Response())

def test_work_optionUpper_acident_type():
    assert type(data_to_use(acident_type='WORK')) != type(Response())

def test_work_optionLower_acident_type():
    assert type(data_to_use(acident_type='work')) != type(Response())

def test_traffic_option_acident_type():
    assert type(data_to_use(acident_type='traffic')) != type(Response())

def test_traffic_optionUpper_acident_type():
    assert type(data_to_use(acident_type='TRAFFIC')) != type(Response())

def test_traffic_optionLower_acident_type():
    assert type(data_to_use(acident_type='traffic')) != type(Response())

def test_work_path_option_acident_type():
    assert type(data_to_use(acident_type='work_path')) != type(Response())

def test_work_path_optionUpper_acident_type():
    assert type(data_to_use(acident_type='WORK_PATH')) != type(Response())

def test_work_path_optionLower_acident_type():
    assert type(data_to_use(acident_type='work_path')) != type(Response())

def test_wrongtype_pension_status():
    assert data_to_use(pension_status=1231).status == Response(status=400).status

def test_notexistopiton_pension_status():
    assert data_to_use(pension_status='adadasd').status == Response(status=400).status

def test_worker_option_pension_status():
    assert type(data_to_use(pension_status='worker')) != type(Response())

def test_worker_optionUpper_pension_status():
    assert type(data_to_use(pension_status='WORKER')) != type(Response())

def test_worker_optionLower_pension_status():
    assert type(data_to_use(pension_status='worker')) != type(Response())

def test_employer_option_pension_status():
    assert type(data_to_use(pension_status='employer')) != type(Response())

def test_employer_optionUpper_pension_status():
    assert type(data_to_use(pension_status='EMPLOYER')) != type(Response())

def test_employer_optionLower_pension_status():
    assert type(data_to_use(pension_status='employer')) != type(Response())

def test_autonomous_option_pension_status():
    assert type(data_to_use(pension_status='autonomous')) != type(Response())

def test_autonomous_optionUpper_pension_status():
    assert type(data_to_use(pension_status='AUTONOMOUS')) != type(Response())

def test_autonomous_optionLower_pension_status():
    assert type(data_to_use(pension_status='autonomous')) != type(Response())

def test_unemployed_option_pension_status():
    assert type(data_to_use(pension_status='unemployed')) != type(Response())

def test_unemployed_optionUpper_pension_status():
    assert type(data_to_use(pension_status='UNEMPLOYED')) != type(Response())

def test_unemployed_optionLower_pension_status():
    assert type(data_to_use(pension_status='unemployed')) != type(Response())

def test_retired_option_pension_status():
    assert type(data_to_use(pension_status='retired')) != type(Response())

def test_retired_optionUpper_pension_status():
    assert type(data_to_use(pension_status='RETIRED')) != type(Response())

def test_retired_optionLower_pension_status():
    assert type(data_to_use(pension_status='retired')) != type(Response())

def test_not_insured_option_pension_status():
    assert type(data_to_use(pension_status='not_insured')) != type(Response())

def test_not_insured_optionUpper_pension_status():
    assert type(data_to_use(pension_status='NOT_INSURED')) != type(Response())

def test_not_insured_optionLower_pension_status():
    assert type(data_to_use(pension_status='not_insured')) != type(Response())

def test_wrongtype_patient_adress_uf():
    assert data_to_use(patient_adress_uf=1231).status == Response(status=400).status

def test_notexistopiton_patient_adress_uf():
    assert data_to_use(patient_adress_uf='AUYD').status == Response(status=400).status

def test_AC_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AC')) != type(Response())

def test_AC_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ac')) != type(Response())

def test_AL_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AL')) != type(Response())

def test_AL_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='al')) != type(Response())

def test_AP_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AP')) != type(Response())

def test_AP_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ap')) != type(Response())

def test_AM_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='AM')) != type(Response())

def test_AM_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='am')) != type(Response())

def test_BA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='BA')) != type(Response())

def test_BA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ba')) != type(Response())

def test_CE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='CE')) != type(Response())

def test_CE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ce')) != type(Response())

def test_DF_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='DF')) != type(Response())

def test_DF_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='df')) != type(Response())

def test_ES_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ES')) != type(Response())

def test_ES_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='es')) != type(Response())

def test_GO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='GO')) != type(Response())

def test_GO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='go')) != type(Response())

def test_MA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MA')) != type(Response())

def test_MA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ma')) != type(Response())

def test_MS_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MS')) != type(Response())

def test_MS_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ms')) != type(Response())

def test_MT_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MT')) != type(Response())

def test_MT_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='mt')) != type(Response())

def test_MG_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='MG')) != type(Response())

def test_MG_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='mg')) != type(Response())

def test_PA_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PA')) != type(Response())

def test_PA_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pa')) != type(Response())

def test_PB_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PB')) != type(Response())

def test_PB_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pb')) != type(Response())

def test_PR_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PR')) != type(Response())

def test_PR_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pr')) != type(Response())

def test_PE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PE')) != type(Response())

def test_PE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pe')) != type(Response())

def test_PI_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='PI')) != type(Response())

def test_PI_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='pi')) != type(Response())

def test_RJ_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RJ')) != type(Response())

def test_RJ_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rj')) != type(Response())

def test_RN_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RN')) != type(Response())

def test_RN_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rn')) != type(Response())

def test_RS_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RS')) != type(Response())

def test_RS_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rs')) != type(Response())

def test_RO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RO')) != type(Response())

def test_RO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='ro')) != type(Response())

def test_RR_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='RR')) != type(Response())

def test_RR_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='rr')) != type(Response())

def test_SC_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SC')) != type(Response())

def test_SC_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='sc')) != type(Response())

def test_SP_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SP')) != type(Response())

def test_SP_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='sp')) != type(Response())

def test_SE_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='SE')) != type(Response())

def test_SE_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='se')) != type(Response())

def test_TO_optionUpper_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='TO')) != type(Response())

def test_TO_optionLower_patient_adress_uf():
    assert type(data_to_use(patient_adress_uf='to')) != type(Response())



####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# patient_adress_city
# patient_adress_city_ibge_code
# patient_adress_uf (already tested in option tests)
# patient_adress_cep
# test wrong type
# test empty value
# test empty space value
# invalid value
# Long value

def test_wrongtype_patient_adress():
    assert data_to_use(patient_adress=1212312).status == Response(status=400).status

def test_empty_value_patient_adress():
    assert data_to_use(patient_adress='').status == Response(status=400).status

def test_empty_space_patient_adress():
    assert data_to_use(patient_adress='  ').status == Response(status=400).status

def test_invalid_value_patient_adress():
    assert data_to_use(patient_adress='111').status == Response(status=400).status

def test_long_value_patient_adress():
    assert data_to_use(patient_adress=lenght_test[:103]).status == Response(status=400).status

def test_wrongtype_patient_adress_city():
    assert data_to_use(patient_adress_city=1212312).status == Response(status=400).status

def test_empty_value_patient_adress_city():
    assert data_to_use(patient_adress_city='').status == Response(status=400).status

def test_empty_space_patient_adress_city():
    assert data_to_use(patient_adress_city='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_city():
    assert data_to_use(patient_adress_city='111').status == Response(status=400).status

def test_long_value_patient_adress_city():
    assert data_to_use(patient_adress_city=lenght_test[:73]).status == Response(status=400).status

def test_wrongtype_patient_adress_city_ibge_code():
    assert data_to_use(patient_adress_city_ibge_code='1212312').status == Response(status=400).status

def test_empty_value_patient_adress_city_ibge_code():
    assert data_to_use(patient_adress_city_ibge_code='').status == Response(status=400).status

def test_empty_space_patient_adress_city_ibge_code():
    assert data_to_use(patient_adress_city_ibge_code='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_city_ibge_code():
    assert data_to_use(patient_adress_city_ibge_code=2411).status == Response(status=400).status

def test_long_value_patient_adress_city_ibge_code():
    assert data_to_use(patient_adress_city_ibge_code=52352352352352352352352352352).status == Response(status=400).status

def test_wrongtype_patient_adress_cep():
    assert data_to_use(patient_adress_cep='1212312').status == Response(status=400).status

def test_empty_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep='').status == Response(status=400).status

def test_empty_space_patient_adress_cep():
    assert data_to_use(patient_adress_cep='  ').status == Response(status=400).status

def test_invalid_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep=2411).status == Response(status=400).status

def test_long_value_patient_adress_cep():
    assert data_to_use(patient_adress_cep=52352352352352352352352352352).status == Response(status=400).status

#############################################################################
# TEST BIG TEXT WITH LINE BRAKES
# main_clinical_signs_symptoms
# conditions_justify_hospitalization
# exam_results
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit


def test_wrong_type_main_clinical_signs_symptoms():
    assert data_to_use(main_clinical_signs_symptoms=131).status == Response(status=400).status

def test_empty_value_main_clinical_signs_symptoms():
    assert data_to_use(main_clinical_signs_symptoms='').status == Response(status=400).status

def test_empty_spaces_main_clinical_signs_symptoms():
    assert data_to_use(main_clinical_signs_symptoms='    ').status == Response(status=400).status

def test_shortText_main_clinical_signs_symptoms():
    assert data_to_use(main_clinical_signs_symptoms='abla').status == Response(status=400).status

def test_more_than_limit_main_clinical_signs_symptoms():
    assert data_to_use(main_clinical_signs_symptoms=lenght_test[:1030]).status == Response(status=400).status

def test_wrong_type_conditions_justify_hospitalization():
    assert data_to_use(conditions_justify_hospitalization=131).status == Response(status=400).status

def test_empty_value_conditions_justify_hospitalization():
    assert data_to_use(conditions_justify_hospitalization='').status == Response(status=400).status

def test_empty_spaces_conditions_justify_hospitalization():
    assert data_to_use(conditions_justify_hospitalization='    ').status == Response(status=400).status

def test_shortText_conditions_justify_hospitalization():
    assert data_to_use(conditions_justify_hospitalization='abla').status == Response(status=400).status

def test_more_than_limit_conditions_justify_hospitalization():
    assert data_to_use(conditions_justify_hospitalization=lenght_test[:410]).status == Response(status=400).status

def test_wrong_type_exam_results():
    assert data_to_use(exam_results=131).status == Response(status=400).status

def test_empty_value_exam_results():
    assert type(data_to_use(exam_results='')) != type(Response())

def test_empty_spaces_exam_results():
    assert type(data_to_use(exam_results='    ')) != type(Response())

def test_shortText_exam_results():
    assert data_to_use(exam_results='abla').status == Response(status=400).status

def test_more_than_limit_exam_results():
    assert data_to_use(exam_results=lenght_test[:410]).status == Response(status=400).status


#############################################################################
# NORMAL TEXT VARIABLES THAT CANNOT BE NULL
# initial_diagnostic
# principal_cid_10
# procedure_solicited
# procedure_code
# clinic
# internation_carater
# emission_org_code
# test wrong type
# test empty value
# test empty spaces 
# test short text
# test more than limit

def test_wrong_type_initial_diagnostic():
    assert data_to_use(initial_diagnostic=131).status == Response(status=400).status

def test_empty_value_initial_diagnostic():
    assert data_to_use(initial_diagnostic='').status == Response(status=400).status

def test_empty_spaces_initial_diagnostic():
    assert data_to_use(initial_diagnostic='    ').status == Response(status=400).status

def test_shortText_initial_diagnostic():
    assert data_to_use(initial_diagnostic='abla').status == Response(status=400).status

def test_more_than_limit_initial_diagnostic():
    assert data_to_use(initial_diagnostic=lenght_test[:46]).status == Response(status=400).status

def test_wrong_type_principal_cid_10():
    assert data_to_use(principal_cid_10=131).status == Response(status=400).status

def test_empty_value_principal_cid_10():
    assert data_to_use(principal_cid_10='').status == Response(status=400).status

def test_empty_spaces_principal_cid_10():
    assert data_to_use(principal_cid_10='    ').status == Response(status=400).status

def test_shortText_principal_cid_10():
    assert data_to_use(principal_cid_10='ab').status == Response(status=400).status

def test_more_than_limit_principal_cid_10():
    assert data_to_use(principal_cid_10=lenght_test[:6]).status == Response(status=400).status

def test_wrong_type_procedure_solicited():
    assert data_to_use(procedure_solicited=131).status == Response(status=400).status

def test_empty_value_procedure_solicited():
    assert data_to_use(procedure_solicited='').status == Response(status=400).status

def test_empty_spaces_procedure_solicited():
    assert data_to_use(procedure_solicited='    ').status == Response(status=400).status

def test_shortText_procedure_solicited():
    assert data_to_use(procedure_solicited='ab11').status == Response(status=400).status

def test_more_than_limit_procedure_solicited():
    assert data_to_use(procedure_solicited=lenght_test[:70]).status == Response(status=400).status

def test_wrong_type_procedure_code():
    assert data_to_use(procedure_code=131).status == Response(status=400).status

def test_empty_value_procedure_code():
    assert data_to_use(procedure_code='').status == Response(status=400).status

def test_empty_spaces_procedure_code():
    assert data_to_use(procedure_code='    ').status == Response(status=400).status

def test_shortText_procedure_code():
    assert data_to_use(procedure_code='ab11').status == Response(status=400).status

def test_more_than_limit_procedure_code():
    assert data_to_use(procedure_code=lenght_test[:12]).status == Response(status=400).status

def test_wrong_type_clinic():
    assert data_to_use(clinic=131).status == Response(status=400).status

def test_empty_value_clinic():
    assert data_to_use(clinic='').status == Response(status=400).status

def test_empty_spaces_clinic():
    assert data_to_use(clinic='    ').status == Response(status=400).status

def test_shortText_clinic():
    assert data_to_use(clinic='ab11').status == Response(status=400).status

def test_more_than_limit_clinic():
    assert data_to_use(clinic=lenght_test[:20]).status == Response(status=400).status

def test_wrong_type_internation_carater():
    assert data_to_use(internation_carater=131).status == Response(status=400).status

def test_empty_value_internation_carater():
    assert data_to_use(internation_carater='').status == Response(status=400).status

def test_empty_spaces_internation_carater():
    assert data_to_use(internation_carater='    ').status == Response(status=400).status

def test_shortText_internation_carater():
    assert data_to_use(internation_carater='ab11').status == Response(status=400).status

def test_more_than_limit_internation_carater():
    assert data_to_use(internation_carater=lenght_test[:20]).status == Response(status=400).status

def test_wrong_type_emission_org_code():
    assert data_to_use(emission_org_code=131).status == Response(status=400).status

def test_empty_value_emission_org_code():
    assert data_to_use(emission_org_code='').status == Response(status=400).status

def test_empty_spaces_emission_org_code():
    assert data_to_use(emission_org_code='    ').status == Response(status=400).status

def test_shortText_emission_org_code():
    assert data_to_use(emission_org_code='a').status == Response(status=400).status

def test_more_than_limit_emission_org_code():
    assert data_to_use(emission_org_code=lenght_test[:20]).status == Response(status=400).status




#################################################################################
# TEST INT VARIABLES CAN/CANNOT BE NULL
# hospitalization_autorization_number
# chart_number
# patient_mother_phonenumber
# patient_responsible_phonenumber
# insurance_company_ticket_number
# company_cnae
# company_cbor
# !!!!! TESTING
# wrong type
# test empty value
# test empty space
# short value
# long value  

def test_wrong_type_hospitalization_autorization_number():
    assert data_to_use(hospitalization_autorization_number='131').status == Response(status=400).status

def test_empty_value_hospitalization_autorization_number():
    assert data_to_use(hospitalization_autorization_number='').status == Response(status=400).status

def test_empty_spaces_hospitalization_autorization_number():
    assert data_to_use(hospitalization_autorization_number='    ').status == Response(status=400).status

def test_longValue_hospitalization_autorization_number():
    assert data_to_use(hospitalization_autorization_number=int(lenght_test[:20])).status == Response(status=400).status

def test_wrong_type_chart_number():
    assert data_to_use(chart_number='131').status == Response(status=400).status

def test_empty_value_chart_number():
    assert type(data_to_use(chart_number=None)) != type(Response())

def test_empty_spaces_chart_number():
    assert data_to_use(chart_number='    ').status == Response(status=400).status

def test_longValue_chart_number():
    assert data_to_use(chart_number=int(lenght_test[:23])).status == Response(status=400).status

def test_shortValue_chart_number():
    assert data_to_use(chart_number='a').status == Response(status=400).status

def test_wrong_type_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber='131').status == Response(status=400).status

def test_empty_value_patient_mother_phonenumber():
    assert type(data_to_use(patient_mother_phonenumber=None)) != type(Response())

def test_empty_spaces_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber='    ').status == Response(status=400).status

def test_longValue_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber=int(lenght_test[:14])).status == Response(status=400).status

def test_shortValue_patient_mother_phonenumber():
    assert data_to_use(patient_mother_phonenumber=1234567).status == Response(status=400).status

def test_wrong_type_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber='131').status == Response(status=400).status

def test_empty_value_patient_responsible_phonenumber():
    assert type(data_to_use(patient_responsible_phonenumber=None)) != type(Response())

def test_empty_spaces_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber='    ').status == Response(status=400).status

def test_longValue_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber=int(lenght_test[:14])).status == Response(status=400).status

def test_shortValue_patient_responsible_phonenumber():
    assert data_to_use(patient_responsible_phonenumber=1234567).status == Response(status=400).status

def test_wrong_type_insurance_company_ticket_number():
    assert data_to_use(insurance_company_ticket_number='131').status == Response(status=400).status

def test_empty_value_insurance_company_ticket_number():
    assert type(data_to_use(insurance_company_ticket_number=None)) != type(Response())

def test_empty_spaces_insurance_company_ticket_number():
    assert data_to_use(insurance_company_ticket_number='    ').status == Response(status=400).status

def test_longValue_insurance_company_ticket_number():
    assert data_to_use(insurance_company_ticket_number=int(lenght_test[:18])).status == Response(status=400).status

def test_shortValue_insurance_company_ticket_number():
    assert type(data_to_use(insurance_company_ticket_number=12)) != type(Response(status=400))

def test_wrong_type_company_cnae():
    assert data_to_use(company_cnae='131').status == Response(status=400).status

def test_empty_value_company_cnae():
    assert type(data_to_use(company_cnae=None)) != type(Response())

def test_empty_spaces_company_cnae():
    assert data_to_use(company_cnae='    ').status == Response(status=400).status

def test_longValue_company_cnae():
    assert data_to_use(company_cnae=int(lenght_test[:9])).status == Response(status=400).status

def test_shortValue_company_cnae():
    assert data_to_use(company_cnae=12312).status == Response(status=400).status

def test_wrong_type_company_cbor():
    assert data_to_use(company_cbor='131').status == Response(status=400).status

def test_empty_value_company_cbor():
    assert type(data_to_use(company_cbor=None)) != type(Response())

def test_empty_spaces_company_cbor():
    assert data_to_use(company_cbor='    ').status == Response(status=400).status

def test_longValue_company_cbor():
    assert data_to_use(company_cbor=int(lenght_test[:9])).status == Response(status=400).status

def test_shortValue_company_cbor():
    assert data_to_use(company_cbor=12542).status == Response(status=400).status


##############################################################################
# TEST CNPJ VARIABLES
# insurance_company_cnpj
# company_cnpj
# test wrong type
# test invalid cnpj
# test valid cpnj

def test_wrong_type_insurance_company_cnpj():
    assert data_to_use(insurance_company_cnpj='131').status == Response(status=400).status

def test_invalidCNPJ_insurance_company_cnpj():
    assert data_to_use(insurance_company_cnpj=527415297419524).status == Response(status=400).status

def test_validCNPJ_insurance_company_cnpj():
    assert type(data_to_use(insurance_company_cnpj=37549670000171)) != type(Response())

def test_wrong_type_company_cnpj():
    assert data_to_use(company_cnpj='131').status == Response(status=400).status

def test_invalidCNPJ_company_cnpj():
    assert data_to_use(company_cnpj=527415297419524).status == Response(status=400).status

def test_validCNPJ_company_cnpj():
    assert type(data_to_use(company_cnpj=37549670000171)) != type(Response())


##############################################################################
# TEST STRING THAT CAN BE NULL
# patient_ethnicity
# patient_responsible_name
# secondary_cid_10
# cid_10_associated_causes
# insurance_company_series
# test wront type
# test empty value
# test empty spaces
# test long values
# test short values

def test_wrong_type_patient_ethnicity():
    assert data_to_use(patient_ethnicity=123).status == Response(status=400).status

def test_empty_value_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity=None)) != type(Response())

def test_empty_spaces_patient_ethnicity():
    assert type(data_to_use(patient_ethnicity='    ')) != type(Response())

def test_longValue_patient_ethnicity():
    assert data_to_use(patient_ethnicity=lenght_test[:15]).status == Response(status=400).status

def test_shortValue_patient_ethnicity():
    assert data_to_use(patient_ethnicity='aaa').status == Response(status=400).status

def test_wrong_type_patient_responsible_name():
    assert data_to_use(patient_responsible_name=123).status == Response(status=400).status

def test_empty_value_patient_responsible_name():
    assert type(data_to_use(patient_responsible_name=None)) != type(Response())

def test_empty_spaces_patient_responsible_name():
    assert type(data_to_use(patient_responsible_name='    ')) != type(Response())

def test_longValue_patient_responsible_name():
    assert data_to_use(patient_responsible_name=lenght_test[:72]).status == Response(status=400).status

def test_shortValue_patient_responsible_name():
    assert data_to_use(patient_responsible_name='aaa').status == Response(status=400).status

def test_wrong_type_secondary_cid_10():
    assert data_to_use(secondary_cid_10=123).status == Response(status=400).status

def test_empty_value_secondary_cid_10():
    assert type(data_to_use(secondary_cid_10=None)) != type(Response())

def test_empty_spaces_secondary_cid_10():
    assert type(data_to_use(secondary_cid_10='    ')) != type(Response())

def test_longValue_secondary_cid_10():
    assert data_to_use(secondary_cid_10=lenght_test[:6]).status == Response(status=400).status

def test_shortValue_secondary_cid_10():
    assert data_to_use(secondary_cid_10='aa').status == Response(status=400).status

def test_wrong_type_secondary_cid_10():
    assert data_to_use(secondary_cid_10=123).status == Response(status=400).status

def test_empty_value_cid_10_associated_causes():
    assert type(data_to_use(cid_10_associated_causes=None)) != type(Response())

def test_empty_spaces_cid_10_associated_causes():
    assert type(data_to_use(cid_10_associated_causes='    ')) != type(Response())

def test_longValue_cid_10_associated_causes():
    assert data_to_use(cid_10_associated_causes=lenght_test[:6]).status == Response(status=400).status

def test_shortValue_cid_10_associated_causes():
    assert data_to_use(cid_10_associated_causes='aa').status == Response(status=400).status

def test_wrong_type_insurance_company_series():
    assert data_to_use(insurance_company_series=123).status == Response(status=400).status

def test_empty_value_insurance_company_series():
    assert type(data_to_use(insurance_company_series=None)) != type(Response())

def test_empty_spaces_insurance_company_series():
    assert type(data_to_use(insurance_company_series='    ')) != type(Response())

def test_longValue_insurance_company_series():
    assert data_to_use(insurance_company_series=lenght_test[:12]).status == Response(status=400).status

def test_shortValue_insurance_company_series():
    assert type(data_to_use(insurance_company_series='123')) != type(Response())


