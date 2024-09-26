# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2673add-7883-33f0-9b24-e333d63ded77 | -20.59427 | -56.20649 | 2024-09-26 13:12:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e632739d-34be-3558-bc9e-0995f8dbd02c | -20.59289 | -56.21594 | 2024-09-26 13:12:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6ae1c390-3e88-3cfa-a423-f23036d23546 | -21.36844 | -56.2716 | 2024-09-26 13:12:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e71e15a2-b276-3dee-aa95-109967c48af1 | -15.60572 | -56.94371 | 2024-09-26 13:12:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6ec6d30e-8f62-36d0-a80b-36d4d060e192 | -15.60422 | -56.95354 | 2024-09-26 13:12:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 79bea8ed-2eaf-3259-a554-68bd238b1c58 | -15.60261 | -56.96412 | 2024-09-26 13:12:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 83b7d24e-4914-308d-bbfe-28f94cf2e2f4 | -15.59012 | -56.9205 | 2024-09-26 13:12:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d96b1091-6dc8-3873-a6d3-ff960f43e557 | -15.58859 | -56.93048 | 2024-09-26 13:12:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| ebe6a345-45fb-3543-beb3-b0c252970802 | -15.58079 | -56.9189 | 2024-09-26 13:12:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 25de5198-c71f-3250-9774-e81433367532 | -15.57929 | -56.92865 | 2024-09-26 13:12:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b14690f2-c784-3033-b527-ab74a5e33400 | -16.80456 | -57.48497 | 2024-09-26 13:12:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| fc50e9f8-33f4-37e0-a720-9a617f28d558 | -16.79852 | -57.79967 | 2024-09-26 13:12:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| e828481e-62f3-3317-a229-af6d577678d5 | -18.00041 | -44.45316 | 2024-09-26 13:12:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c7ca0833-4484-3d0e-a614-0ba1117798da | -18.00031 | -44.46032 | 2024-09-26 13:12:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0a6ecaa7-bb3a-3159-a989-5d112d0cea79 | -17.98621 | -44.41698 | 2024-09-26 13:12:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ad12f694-1458-37bc-a477-edd1b77c24a0 | -17.98269 | -44.45194 | 2024-09-26 13:12:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 152.5 |
| c1a08a40-a97a-3748-a222-929f7c2ef0f8 | -17.98258 | -44.45915 | 2024-09-26 13:12:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 08c7ee73-ad68-3cc3-863e-738b850946c4 | -17.89456 | -47.03072 | 2024-09-26 13:12:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 1e2f2e18-a00e-3f56-a010-4d1acc4c2194 | -17.89373 | -47.02358 | 2024-09-26 13:12:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ac470331-6894-3ae1-bbb4-58239e74f0fb | -17.87987 | -47.02959 | 2024-09-26 13:12:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3a012316-2ef6-35b2-9c70-66d622784661 | -17.87898 | -47.02292 | 2024-09-26 13:12:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ed169457-ebdb-38ff-bda0-57a3e528ff54 | -19.58363 | -46.85 | 2024-09-26 13:12:00 | TERRA_M-T | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 11c33018-7eea-313e-a215-bd71b3679cd5 | -19.58072 | -46.88092 | 2024-09-26 13:12:00 | TERRA_M-T | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1d892340-ab96-39ce-85dc-ef251ba38114 | -19.56783 | -46.87219 | 2024-09-26 13:12:00 | TERRA_M-T | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d0dbdb66-89b2-35f0-9af3-8f10a5172ba0 | -22.30261 | -48.06962 | 2024-09-26 13:12:00 | TERRA_M-T | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 20.7 |
| e3bf80b8-4c6a-3f52-b609-b8646080c73c | -22.29982 | -48.06296 | 2024-09-26 13:12:00 | TERRA_M-T | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 01d1e9dc-a42c-3415-ac06-80c69edcf92b | -22.01688 | -48.23522 | 2024-09-26 13:12:00 | TERRA_M-T | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3ba46b26-476b-3356-8677-f4ca637cdfb8 | -22.01456 | -48.26103 | 2024-09-26 13:12:00 | TERRA_M-T | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7cbe3549-1f8a-3ec5-abca-475cd12c7c25 | -22.01262 | -48.22972 | 2024-09-26 13:12:00 | TERRA_M-T | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 70.7 |
| dc18eb3e-3ac6-3190-8dcf-7bba3e1e9fe5 | -22.01012 | -48.25568 | 2024-09-26 13:12:00 | TERRA_M-T | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 216d628e-58cf-31aa-bc35-5fdd418990a3 | -21.953 | -48.55546 | 2024-09-26 13:12:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 96582fe5-c83d-3fde-af70-3a6f5fbb113b | -21.93916 | -48.5545 | 2024-09-26 13:12:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 157.7 |
| a583dcdb-ddfe-3f63-87a1-097e47d1176c | -21.93307 | -48.5472 | 2024-09-26 13:12:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 2f9e6cc8-6100-3b3f-922a-a39ba8b3ee8c | -17.63516 | -47.6191 | 2024-09-26 13:12:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c27d790d-0d58-347d-a24a-4d79116c93a6 | -16.95439 | -47.65208 | 2024-09-26 13:12:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a7fc85de-a50d-32c2-920a-593d5d978156 | -16.95185 | -47.67615 | 2024-09-26 13:12:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| fecfda40-ea6d-3610-bb74-af8a89e8fcd0 | -16.94539 | -47.66888 | 2024-09-26 13:12:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 6a815a45-0c81-3644-bfd4-09469c4a83cb | -16.87149 | -47.70939 | 2024-09-26 13:12:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 907b062a-d7a6-3c27-a403-288be290f1a2 | -16.86903 | -47.73236 | 2024-09-26 13:12:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 1d59082b-63e6-3816-89fa-a99e4b23dac5 | -16.85779 | -47.70792 | 2024-09-26 13:12:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 1150ee01-09ee-3782-9c04-bbe33053ef35 | -16.85536 | -47.73078 | 2024-09-26 13:12:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 39.7 |
| af844c3c-e70b-3443-853d-557817befdce | -18.59133 | -48.97788 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 658f28e7-64ef-3c09-b6e3-c65cb682888e | -18.59128 | -48.97126 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 422d7c4b-2950-3c4c-819a-04f79a4cbbea | -18.1148 | -49.04714 | 2024-09-26 13:12:00 | TERRA_M-T | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c7c220fd-5da6-36d9-8a9b-3a96d452ecbf | -18.11263 | -49.06641 | 2024-09-26 13:12:00 | TERRA_M-T | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 660.4 |
| 3125922b-82cc-37f3-9d99-c8392d04beaa | -18.11041 | -49.08611 | 2024-09-26 13:12:00 | TERRA_M-T | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 988e6b80-8779-3ad0-950d-2cd1e0ca8883 | -18.10005 | -49.06536 | 2024-09-26 13:12:00 | TERRA_M-T | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 6ac1c2b7-26d0-3571-aa52-34311af13c3c | -18.94521 | -49.17611 | 2024-09-26 13:12:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| 1ae7d640-2cf2-3997-81e1-a50c49e7de04 | -18.93361 | -49.18138 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.7 |
| e5c049a4-711e-3eb7-b1a3-fe8d0bbb386e | -18.9326 | -49.1748 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.0 |
| 621acd3d-4e02-33f9-947c-197cb7e46fa6 | -18.93043 | -49.19426 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| 89631585-852e-3bd1-8b70-a79fff92e623 | -18.92001 | -49.17344 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| ec6d44ec-61d8-3632-bdf8-ff0aa428248f | -18.91781 | -49.19322 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 5d93517d-186b-369d-95d4-aaae4ffd150a | -18.9074 | -49.1722 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| af286cf4-5a8b-3d27-8b57-32d23315fdad | -18.90521 | -49.19207 | 2024-09-26 13:12:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.4 |
| 40c9f449-f90f-3b2b-8b73-280de3265412 | -18.7185 | -48.13593 | 2024-09-26 13:12:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| 787c85b8-ea2a-3e80-a31a-29ed7d92040f | -18.19986 | -49.10155 | 2024-09-26 13:12:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| 891deef6-dcd5-3030-81b9-01d8f4eeeeae | -20.86493 | -49.57334 | 2024-09-26 13:12:00 | TERRA_M-T | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 5f0e1b6f-d1ac-305a-b7b2-51dfe3b5d9f1 | -20.81519 | -48.92601 | 2024-09-26 13:12:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| ee3067c6-ca91-324a-9196-9d57533c7efe | -20.81298 | -48.94796 | 2024-09-26 13:12:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.8 |
| e966ba9d-006b-3de7-9632-1bbd43242b11 | -21.95063 | -48.58011 | 2024-09-26 13:12:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 346.8 |
| 4a45424c-d1f7-3dac-a723-bd0415193d8e | -21.93685 | -48.57874 | 2024-09-26 13:12:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ecef3851-0ae6-3c05-be13-e6ce34021bd2 | -21.93058 | -48.57163 | 2024-09-26 13:12:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 3ff53896-8940-39c9-bb27-874229d3ba80 | -21.82904 | -48.67673 | 2024-09-26 13:12:00 | TERRA_M-T | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 34ba3e26-ab9c-3dd1-9883-ff6db0378f96 | -22.24952 | -48.66156 | 2024-09-26 13:12:00 | TERRA_M-T | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 180.8 |
| 1fbf798a-c54f-3675-91f9-ed8043542e7b | -22.24729 | -48.68577 | 2024-09-26 13:12:00 | TERRA_M-T | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.0 |
| 68e74dcb-e6df-3df2-9390-387828102c6b | -22.24291 | -48.65384 | 2024-09-26 13:12:00 | TERRA_M-T | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 374.2 |
| 52f060ff-df9d-3b26-aba0-0dd6032dd23a | -22.24047 | -48.6787 | 2024-09-26 13:12:00 | TERRA_M-T | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 538.6 |
| 2c4c7a12-f81b-3ace-94eb-79d4776455a3 | -22.2292 | -48.65199 | 2024-09-26 13:12:00 | TERRA_M-T | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.9 |
| ebb66f2d-e04d-36d8-87c1-ca7883a2d06d | -22.22675 | -48.67719 | 2024-09-26 13:12:00 | TERRA_M-T | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 603.2 |
| d775252e-89bc-372d-9917-cc66c86658ce | -22.21308 | -48.67513 | 2024-09-26 13:12:00 | TERRA_M-T | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.3 |
| 4f4affe3-a07a-3d05-9fda-a2e7098dd801 | -21.06503 | -49.14802 | 2024-09-26 13:12:00 | TERRA_M-T | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 418.8 |
| 103bf118-69cd-379f-ad90-f2bba1f4746b | -21.06288 | -49.16917 | 2024-09-26 13:12:00 | TERRA_M-T | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 506989dc-08a1-38ad-bd50-239de7e9b359 | -21.05376 | -49.14141 | 2024-09-26 13:12:00 | TERRA_M-T | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 253.9 |
| 25bba331-51b4-3edd-9def-90ed38628b19 | -21.052 | -49.14669 | 2024-09-26 13:12:00 | TERRA_M-T | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 357.1 |
| 52647e34-b0a6-3c0b-8c61-1765cecbd38f | -21.05148 | -49.1626 | 2024-09-26 13:12:00 | TERRA_M-T | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 389.4 |
| 92c8d64d-494f-3bf5-92a7-7f75849068b7 | -21.04986 | -49.16798 | 2024-09-26 13:12:00 | TERRA_M-T | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 194.3 |
| 5e96a1e2-1619-3593-b94c-2d656ce7fe39 | -23.16859 | -50.01765 | 2024-09-26 13:12:00 | TERRA_M-T | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| ae44ed60-3fb2-3753-be7b-416e833af9c9 | -16.80825 | -49.31426 | 2024-09-26 13:12:00 | TERRA_M-T | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| aba27812-f6a8-3690-9c7b-54e68a45e4f3 | -18.78991 | -50.11054 | 2024-09-26 13:12:00 | TERRA_M-T | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 6c74eb91-aab8-3e15-a7f6-91dc5178736a | -18.78799 | -50.12737 | 2024-09-26 13:12:00 | TERRA_M-T | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 619efa3e-7bc9-3c9d-a297-c3045cb0cad1 | -20.61498 | -49.97482 | 2024-09-26 13:12:00 | TERRA_M-T | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 80596734-df0a-3de3-b19b-b350eb776a6e | -20.613 | -49.99323 | 2024-09-26 13:12:00 | TERRA_M-T | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 2698a13a-cb5d-3c05-a959-06d8265ea16c | -20.60286 | -49.97332 | 2024-09-26 13:12:00 | TERRA_M-T | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 358.3 |
| 73567ead-c4b6-3f9a-974e-89d7e903b712 | -20.6009 | -49.99165 | 2024-09-26 13:12:00 | TERRA_M-T | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 300.2 |
| a0b54724-e673-3195-90e4-1434357035c5 | -20.59854 | -49.96686 | 2024-09-26 13:12:00 | TERRA_M-T | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b2c9d00a-5a88-37db-9831-2de5142db69e | -20.59646 | -49.98516 | 2024-09-26 13:12:00 | TERRA_M-T | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 1b6285d7-4ba7-39fe-86d4-cebe282b800b | -20.80196 | -50.47398 | 2024-09-26 13:12:00 | TERRA_M-T | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 188.0 |
| e32fd7e8-36ae-37ee-a64d-1813417cb45f | -20.79921 | -50.46292 | 2024-09-26 13:12:00 | TERRA_M-T | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.0 |
| f6517e52-4e08-35fd-bfa9-3466fa924b45 | -20.79741 | -50.47971 | 2024-09-26 13:12:00 | TERRA_M-T | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 173.1 |
| 72d28200-3817-32ff-be84-ac30ae40ba65 | -20.79027 | -50.47239 | 2024-09-26 13:12:00 | TERRA_M-T | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.8 |
| db527960-990c-3138-be04-ab255e6f58cc | -5.8808 | -48.0908 | 2024-09-26 13:15:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 075563b3-0ffa-35b6-90aa-1944df08612c | -6.8024 | -59.3044 | 2024-09-26 13:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 947dd363-85d8-39a9-82fe-b91f07c20f11 | -6.784 | -59.3052 | 2024-09-26 13:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ffc4bd58-0295-30c6-b5f0-e993390a5892 | -6.7908 | -41.2254 | 2024-09-26 13:15:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| e506d9ad-2504-364e-860b-9d81af305473 | -6.949 | -63.1048 | 2024-09-26 13:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b8092b9d-c92e-3731-9c7e-20a6ce376a75 | -6.9306 | -63.1053 | 2024-09-26 13:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 01dcb880-755e-376c-9cb6-0ee693c77844 | -7.2906 | -61.0869 | 2024-09-26 13:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7f4ccacc-02e2-3d04-906c-8a7b09307d75 | -7.3637 | -55.5134 | 2024-09-26 13:15:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| cda1dc93-156d-3eb6-919e-106f868b1b5f | -7.3639 | -55.4935 | 2024-09-26 13:15:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |


[Clique aqui para ver as próximas entradas](README186.md)
