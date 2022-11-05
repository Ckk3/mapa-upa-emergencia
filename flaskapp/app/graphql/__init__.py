from ariadne import gql, QueryType, load_schema_from_path

# Define type definitions (schema) using file path route
# type_defs = load_schema_from_path("./app/graphql/schema.graphql")

# Define type definitions (schema) using SDL
type_defs = gql(
    """
    type Query {
       places: [Place]
       "Resolver para servir de fixture para models de outra aplicação Django. `model` é a string que deve aparecer no campo model, `table` no momento deve ser um dos: `[ciap, cid10 , procedimento, vias, exame, medicamento]`. Atenção, o campo `fields` está como **String**"
       fixtures(model:String!, table:String!): [Fixture!]
       prescriptions: [String]
       records(cns:String): [MedicalRecord]
    }

    type Mutation {
        "Criação de documento de AIH"
        fillPdfAihSus(
            establishmentSolitcName: String, 
            establishmentSolitcCnes: Int, 
            establishmentExecName: String, 
            establishmentExecCnes: Int, 
            patientName: String, 
            patientCns: Int, 
            patientBirthday: String, 
            "Quais as opções?"
            patientSex: String,             
            patientMotherName: String, 
            patientAdress: String, 
            patientAdressCity: String, 
            patientAdressCityIbgeCode: Int, 
            patientAdressUF: String, 
            patientAdressCEP: Int, 
            mainClinicalSignsSymptoms: String, conditionsJustifyHospitalization: String, 
            initialDiagnostic: String, 
            principalCid10: String, 
            "Não seria solicited procedure?"
            procedureSolicited: String, 
            procedureCode: String, 
            clinic: String, 
            internationCarater: String, 
            "Em graphql não tem entrada dict, como seria?"
            profSolicitorDocument: String, 
            profSolicitorName: String, 
            solicitationDatetime: String, 
            autorizationProfName: String, 
            emissionOrgCode: String, 
            "Em graphql não tem entrada dict, como seria?"
            autorizatonProfDocument: String, 
            autorizatonDatetime: String, hospitalizationAutorizationNumber: Int,
            examResults: String, 
            chartNumber: Int, 
            patientEthnicity: String, 
            patientResponsibleName: String, 
            "Não seria melhor o telefone ser tipo string?"
            patientMotherPhonenumber: Int, 
            patientResponsiblePhonenumber: Int, 
            secondaryCid10: String, 
            cid10AssociatedCauses: String, 
            acidentType: String, 
            insuranceCompanyCnpj: Int, 
            insuranceCompanyTicketNumber: Int, 
            insuranceCompanySeries: String,
            companyCnpj: Int, 
            companyCnae:int=None, 
            company_cbor:int=None, 
            pension_status:str=None
        ){
            base64Pdf: String
        }
    }


    type Place {
       name: String!
       description: String!
       country: String!
    }  

    type Fixture {
        pk: String
        model: String
        fields: String
    }

    type MedicalRecord {
        patient: Patient
        problems: [String]
    }

    type Patient {
        name: String
        cns: Int
    }
   """
)

# Initialize query
query = QueryType()
