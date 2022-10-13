#from ..pdf_ficha_internamento import fill_pdf_ficha_internamento
from .. import pdf_aih_sus
import datetime
from flask import Response


def data_to_use(establishment_solitc_name='Establishment Solicit Name',establishment_solitc_cnes=1234567,establishment_exec_name='Establshment Exec Name',establishment_exec_cnes=7654321,patient_name='Patient Name',patient_cns=928976954930007,patient_birthday=datetime.datetime.now(),patient_sex='F',patient_mother_name='Patient Mother Name',patient_adress='Patient Adress street neighobourd',patient_adressCity='Patient City',patient_adressCity_ibgeCode=1234567,patient_adressUF='SP',patient_adressCEP=12345678,main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',initial_diagnostic='Patient Initial Diagnostic',principalCid10="A00",procedure_solicited='Procedure Solicited',procedure_code='1234567890', clinic='Clinic Name', internation_carater='Internation Carater', prof_solicitant_document={'CNS':928976954930007},prof_solicitant_name='Profissional Solicit Name', solicitation_datetime=datetime.datetime.now(), autorization_prof_name='Autorization professional name', emission_org_code='OrgCode2022', autorizaton_prof_document={'CPF':28445400070}, autorizaton_datetime=datetime.datetime.now(),hospitalization_autorization_number=1234567890,exam_results='Xray tibia broken',chart_number=1234,patient_ethnicity='Preta', patient_responsible_name='Patient Responsible Name', patient_mother_phonenumber=5613248546, patient_responsible_phonenumber=8564721598, secondary_cid10='A01',cid10_associated_causes='A02',acident_type='work_path', insurance_company_cnpj=37549670000171, insurance_company_ticket_number=123450123456, insurance_company_series='Insurn Series',company_cnpj=37549670000171, company_cnae=5310501, company_cbor=123456, pension_status='not_insured'):
        return pdf_aih_sus.fill_pdf_aih_sus(establishment_solitc_name,establishment_solitc_cnes,establishment_exec_name,establishment_exec_cnes,patient_name,patient_cns,patient_birthday,patient_sex,patient_mother_name,patient_adress,patient_adressCity,patient_adressCity_ibgeCode,patient_adressUF,patient_adressCEP,main_clinical_signs_symptoms,conditions_justify_hospitalization,initial_diagnostic,principalCid10,procedure_solicited,procedure_code, clinic, internation_carater, prof_solicitant_document,prof_solicitant_name, solicitation_datetime, autorization_prof_name, emission_org_code, autorizaton_prof_document, autorizaton_datetime,hospitalization_autorization_number, exam_results,chart_number,patient_ethnicity, patient_responsible_name, patient_mother_phonenumber, patient_responsible_phonenumber,secondary_cid10,cid10_associated_causes,acident_type, insurance_company_cnpj, insurance_company_ticket_number, insurance_company_series,company_cnpj, company_cnae, company_cbor,pension_status)

#Testing Ficha Internamento
def test_with_data_in_function():
    assert type(data_to_use()) != type(Response())

def test_answer_with_all_fields():
    assert type(data_to_use()) != type(Response())

def test_awnser_with_only_required_data():
    assert type(pdf_aih_sus.fill_pdf_aih_sus(
        establishment_solitc_name='Establishment Solicit Name',
        establishment_solitc_cnes=1234567,
        establishment_exec_name='Establshment Exec Name',
        establishment_exec_cnes=7654321,
        patient_name='Patient Name',
        patient_cns=928976954930007,
        patient_birthday=datetime.datetime.now(),
        patient_sex='F',
        patient_mother_name='Patient Mother Name',
        patient_adress='Patient Adress street neighobourd',
        patient_adressCity='Patient City',
        patient_adressCity_ibgeCode=1234567,
        patient_adressUF='SP',
        patient_adressCEP=12345678,
        main_clinical_signs_symptoms="Patient main clinical signs sysmpthoms",
        conditions_justify_hospitalization='Patient Conditions justify hiospitalizaiton',
        initial_diagnostic='Patient Initial Diagnostic',
        principalCid10="A00",
        procedure_solicited='Procedure Solicited',
        procedure_code='1234567890', 
        clinic='Clinic Name', 
        internation_carater='Internation Carater', 
        prof_solicitant_document={'CNS':928976954930007},
        prof_solicitant_name='Profissional Solicit Name', 
        solicitation_datetime=datetime.datetime.now(), 
        autorization_prof_name='Autorization professional name', 
        emission_org_code='OrgCode2022', 
        autorizaton_prof_document={'CPF':28445400070}, 
        autorizaton_datetime=datetime.datetime.now(),
        hospitalization_autorization_number=1234567890
        )) != type(Response())


##############################################################
# ERRORS IN NAMES CAMPS
# establishment_exec_name
# establishment_solitc_name
# patient_name
# patient_mother_name
# prof_solicitant_name
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
    assert data_to_use(establishment_solitc_name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').status == Response(status=400).status

def test_short_establishment_solitcname():    
    assert data_to_use(establishment_solitc_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_solitcname():    
    assert data_to_use(establishment_solitc_name=123124).status == Response(status=400).status

def test_empty_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='').status == Response(status=400).status

def test_with_space_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='  ').status == Response(status=400).status

def test_long_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').status == Response(status=400).status

def test_short_establishment_exec_name():    
    assert data_to_use(establishment_exec_name='bro').status == Response(status=400).status

def test_wrongtype_establishment_exec_name():    
    assert data_to_use(establishment_exec_name=123124).status == Response(status=400).status

def test_empty_patient_name():    
    assert data_to_use(patient_name='').status == Response(status=400).status

def test_with_space_patient_name():    
    assert data_to_use(patient_name='  ').status == Response(status=400).status

def test_long_patient_name():    
    assert data_to_use(patient_name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').status == Response(status=400).status

def test_short_patient_name():    
    assert data_to_use(patient_name='bro').status == Response(status=400).status

def test_wrongtype_patient_name():    
    assert data_to_use(patient_name=123124).status == Response(status=400).status

def test_empty_patient_mother_name():    
    assert data_to_use(patient_mother_name='').status == Response(status=400).status

def test_with_space_patient_mother_name():    
    assert data_to_use(patient_mother_name='  ').status == Response(status=400).status

def test_long_patient_mother_name():    
    assert data_to_use(patient_mother_name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').status == Response(status=400).status

def test_short_patient_mother_name():    
    assert data_to_use(patient_mother_name='bro').status == Response(status=400).status

def test_wrongtype_patient_mother_name():    
    assert data_to_use(patient_mother_name=123124).status == Response(status=400).status
    
def test_empty_prof_solicitant_name():    
    assert data_to_use(prof_solicitant_name='').status == Response(status=400).status

def test_with_space_prof_solicitant_name():    
    assert data_to_use(prof_solicitant_name='  ').status == Response(status=400).status

def test_long_prof_solicitant_name():    
    assert data_to_use(prof_solicitant_name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').status == Response(status=400).status

def test_short_prof_solicitant_name():    
    assert data_to_use(prof_solicitant_name='bro').status == Response(status=400).status

def test_wrongtype_prof_solicitant_name():    
    assert data_to_use(prof_solicitant_name=123124).status == Response(status=400).status

def test_empty_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='').status == Response(status=400).status

def test_with_space_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='  ').status == Response(status=400).status

def test_long_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').status == Response(status=400).status

def test_short_autorization_prof_name():    
    assert data_to_use(autorization_prof_name='bro').status == Response(status=400).status

def test_wrongtype_autorization_prof_name():    
    assert data_to_use(autorization_prof_name=123124).status == Response(status=400).status

def test_empty_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='')) != Response(status=400).status

def test_with_space_patient_responsible_name():    
    assert type(data_to_use(patient_responsible_name='  ')) != Response(status=400).status

def test_long_patient_responsible_name():    
    assert data_to_use(patient_responsible_name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa').status == Response(status=400).status

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
#prof_solicitant_document
#autorizaton_prof_document
# wrong type
# invalid cns
# invalid cpf
# wrong option

def test_wrongtype_patient_cns():
    assert data_to_use(patient_cns='451236548').status == Response(status=400).status

def test_invalid_patient_cns():
    assert data_to_use(patient_cns=451236548554).status == Response(status=400).status

def test_wrongtype_prof_solicitant_document():
    assert data_to_use(prof_solicitant_document='451236548554').status == Response(status=400).status

def test_invalidcns_prof_solicitant_document():
    assert data_to_use(prof_solicitant_document={'CNS':284123312123}).status == Response(status=400).status

def test_invalidccpf_prof_solicitant_document():
    assert data_to_use(prof_solicitant_document={'CPF':284123312123}).status == Response(status=400).status

def test_wrongoption_prof_solicitant_document():
    assert data_to_use(prof_solicitant_document={'BBB':284123312123}).status == Response(status=400).status

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

def test_wrongtype_patient_birthday():
    assert data_to_use(patient_birthday='bahabah').status == Response(status=400).status

def test_wrongtype_solicitation_datetime():
    assert data_to_use(solicitation_datetime='bahabah').status == Response(status=400).status

def test_wrongtype_autorizaton_datetime():
    assert data_to_use(autorizaton_datetime='bahabah').status == Response(status=400).status


##################################################################
# TEST MARKABLE OPTIONS
# patient_sex
# acident_type
# pension_status
# patient_adressUF
# test wrong type
# test not exist option
# test all options in Upper Case
# test all options in lower Case

def test_wrongtype_patient_sex():
    assert data_to_use(patient_sex=1231).status == Response(status=400).status

def test_notexistopiton_patient_sex():
    assert data_to_use(patient_sex='G').status == Response(status=400).status

def test_M_option_patient_sex():
    assert type(data_to_use(patient_sex='M')) != type(Response())

def test_M_optionUpper_patient_sex():
    assert type(data_to_use(patient_sex='M')) != type(Response())

def test_M_optionLower_patient_sex():
    assert type(data_to_use(patient_sex='m')) != type(Response())

def test_F_option_patient_sex():
    assert type(data_to_use(patient_sex='M')) != type(Response())

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

def test_wrongtype_patient_adressUF():
    assert data_to_use(patient_adressUF=1231).status == Response(status=400).status

def test_notexistopiton_patient_adressUF():
    assert data_to_use(patient_adressUF='AUYD').status == Response(status=400).status

def test_AC_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AC')) != type(Response())

def test_AC_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ac')) != type(Response())

def test_AL_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AL')) != type(Response())

def test_AL_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='al')) != type(Response())

def test_AP_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AP')) != type(Response())

def test_AP_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ap')) != type(Response())

def test_AM_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='AM')) != type(Response())

def test_AM_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='am')) != type(Response())

def test_BA_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='BA')) != type(Response())

def test_BA_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ba')) != type(Response())

def test_CE_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='CE')) != type(Response())

def test_CE_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ce')) != type(Response())

def test_DF_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='DF')) != type(Response())

def test_DF_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='df')) != type(Response())

def test_ES_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ES')) != type(Response())

def test_ES_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='es')) != type(Response())

def test_GO_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='GO')) != type(Response())

def test_GO_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='go')) != type(Response())

def test_MA_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MA')) != type(Response())

def test_MA_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ma')) != type(Response())

def test_MS_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MS')) != type(Response())

def test_MS_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ms')) != type(Response())

def test_MT_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MT')) != type(Response())

def test_MT_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='mt')) != type(Response())

def test_MG_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='MG')) != type(Response())

def test_MG_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='mg')) != type(Response())

def test_PA_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PA')) != type(Response())

def test_PA_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pa')) != type(Response())

def test_PB_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PB')) != type(Response())

def test_PB_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pb')) != type(Response())

def test_PR_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PR')) != type(Response())

def test_PR_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pr')) != type(Response())

def test_PE_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PE')) != type(Response())

def test_PE_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pe')) != type(Response())

def test_PI_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='PI')) != type(Response())

def test_PI_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='pi')) != type(Response())

def test_RJ_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RJ')) != type(Response())

def test_RJ_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rj')) != type(Response())

def test_RN_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RN')) != type(Response())

def test_RN_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rn')) != type(Response())

def test_RS_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RS')) != type(Response())

def test_RS_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rs')) != type(Response())

def test_RO_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RO')) != type(Response())

def test_RO_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='ro')) != type(Response())

def test_RR_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='RR')) != type(Response())

def test_RR_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='rr')) != type(Response())

def test_SC_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='SC')) != type(Response())

def test_SC_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='sc')) != type(Response())

def test_SP_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='SP')) != type(Response())

def test_SP_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='sp')) != type(Response())

def test_SE_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='SE')) != type(Response())

def test_SE_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='se')) != type(Response())

def test_TO_optionUpper_patient_adressUF():
    assert type(data_to_use(patient_adressUF='TO')) != type(Response())

def test_TO_optionLower_patient_adressUF():
    assert type(data_to_use(patient_adressUF='to')) != type(Response())



####################################################################
# TEST ADRESS VARIABLES
# patient_adress
# patient_adressCity
# patient_adressCity_ibgeCode
# patient_adressUF (already tested in option tests)
# patient_adressCEP
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
    assert data_to_use(patient_adress='98714t926t\ouifhdoaiuhfouiahsdfouhadsufihaosfuhouihisuhfouhasofuhasoiufhaoisufhoaiushfiouahsfpiuhjsapfiadadasdasdadadadadadadqwe4jasfpaosijmfiosanfpioansfiujnsaiofjunaisfnsahjfnu8yaewnofipnkmxpkovjnoiushbfo8auyshfyaufbuasbfuwybeusosadfjh').status == Response(status=400).status

def test_wrongtype_patient_adressCity():
    assert data_to_use(patient_adressCity=1212312).status == Response(status=400).status

def test_empty_value_patient_adressCity():
    assert data_to_use(patient_adressCity='').status == Response(status=400).status

def test_empty_space_patient_adressCity():
    assert data_to_use(patient_adressCity='  ').status == Response(status=400).status

def test_invalid_value_patient_adressCity():
    assert data_to_use(patient_adressCity='111').status == Response(status=400).status

def test_long_value_patient_adressCity():
    assert data_to_use(patient_adressCity='98714t926t\ouifhdoaiuhfouiahsdfouhadsufihaosfuhouihisuhfouhasofuhasoiufhaoisufhoaiushfiouahsfpiuhjsapfiadadasdasdadadadadadadqwe4jasfpaosijmfiosanfpioansfiujnsaiofjunaisfnsahjfnu8yaewnofipnkmxpkovjnoiushbfo8auyshfyaufbuasbfuwybeusosadfjh').status == Response(status=400).status

def test_wrongtype_patient_adressCity_ibgeCode():
    assert data_to_use(patient_adressCity_ibgeCode='1212312').status == Response(status=400).status

def test_empty_value_patient_adressCity_ibgeCode():
    assert data_to_use(patient_adressCity_ibgeCode='').status == Response(status=400).status

def test_empty_space_patient_adressCity_ibgeCode():
    assert data_to_use(patient_adressCity_ibgeCode='  ').status == Response(status=400).status

def test_invalid_value_patient_adressCity_ibgeCode():
    assert data_to_use(patient_adressCity_ibgeCode=2411).status == Response(status=400).status

def test_long_value_patient_adressCity_ibgeCode():
    assert data_to_use(patient_adressCity_ibgeCode=52352352352352352352352352352).status == Response(status=400).status

def test_wrongtype_patient_adressCEP():
    assert data_to_use(patient_adressCEP='1212312').status == Response(status=400).status

def test_empty_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP='').status == Response(status=400).status

def test_empty_space_patient_adressCEP():
    assert data_to_use(patient_adressCEP='  ').status == Response(status=400).status

def test_invalid_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP=2411).status == Response(status=400).status

def test_long_value_patient_adressCEP():
    assert data_to_use(patient_adressCEP=52352352352352352352352352352).status == Response(status=400).status

#############################################################################



def test_wrong_birthdaydatetimeType():    
    assert data_to_use(patient_birthday='aygduiaydg').status == Response(status=400).status

def test_wrong_patientnametype():    
    assert data_to_use(patient_name=123124124124).status == Response(status=400).status

def test_wrong_sexType():
    assert data_to_use(patient_sex=12347).status == Response(status=400).status

def test_wrong_sexOption():
    assert data_to_use(patient_sex='G').status == Response(status=400).status

def test_wrong_sexOptionExtend():    
    assert data_to_use(patient_sex='Female').status == Response(status=400).status

def test_wrong_pateintmothernameType():    
    assert data_to_use(patient_mother_name=12313).status == Response(status=400).status

def test_wrong_solicitantdocument_type():
    assert data_to_use(prof_solicitant_document=654658).status == Response(status=400).status

def test_invalid_document_option():
    assert data_to_use(prof_solicitant_document={'AAAA':928976954930007}).status == Response(status=400).status

def test_solicitdoc_invalid_CPF():
    assert data_to_use(prof_solicitant_document={'CPF':12345678955}).status == Response(status=400).status

def test_atiorizationdoc_invalid_CPF():

    assert data_to_use(autorizaton_prof_document={'CPF':55568421956}).status == Response(status=400).status

def test_patientinvalidCNS():
    assert data_to_use(patient_cns=2222213565489689).status == Response(status=400).status

def test_solicitDoc_invalidCNS():
    assert data_to_use(prof_solicitant_document={'CNS':5641654864983}).status == Response(status=400).status

def test_autorization_invalidCNS():
    assert data_to_use(prof_solicitant_document={'CNS':5641654864983}).status == Response(status=400).status

def test_wrong_patientadressType():
    assert data_to_use(patient_adress=13123124124).status == Response(status=400).status

def test_wrong_patientResponsiblePhonenumberType():
    assert data_to_use(patient_responsible_phonenumber='8564721598').status == Response(status=400).status

def test_wrong_patientMotherPhonenumberType():
    assert data_to_use(patient_mother_phonenumber='5613248546').status == Response(status=400).status 

def test_wrong_patientadresscityType():
    assert data_to_use(patient_adressCity=1231241241).status == Response(status=400).status

def test_wrong_adressCEPtype():
    assert data_to_use(patient_adressCEP='12345678').status == Response(status=400).status

def test_invalid_patient_adressCEP():
    assert data_to_use(patient_adressCEP=12345671238).status == Response(status=400).status
