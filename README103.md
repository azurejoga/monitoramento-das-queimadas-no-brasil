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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec54795a-dacb-3fbb-80ec-9b561be6701d | -7.9107 | -55.12604 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 609f2aa4-6ed0-3f12-9a9f-21176aecf160 | -7.91015 | -55.1081 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c087257-d9c8-30a1-bdcd-9326c87fc825 | -7.9096 | -55.11158 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c44a864-ef65-3146-bc0e-ed6593a5bb83 | -7.90076 | -55.16734 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71a3e578-e897-34e4-a375-403d279b4cbb | -7.89966 | -55.15288 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2501da1a-7882-3f1a-a616-dca18ba94423 | -7.89911 | -55.15636 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9155cf0d-2bd4-3ec2-9efd-4c6174c096fe | -7.89855 | -55.15985 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e4c311f-cd9e-38d3-8e3f-dd96357595aa | -7.89413 | -55.1663 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50509259-5c5c-3db0-b08e-e45bcaa69744 | -7.89083 | -55.14433 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 997fda84-0947-3c77-88c2-f4cd953057d2 | -7.88793 | -54.73098 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53920d39-2baf-3595-b476-570ffe17dffb | -7.88752 | -55.14381 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8904c8b4-c187-3c29-bea6-b59fc775f48b | -7.88572 | -54.72354 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7926698a-e096-32c9-820a-bbb13a4745ca | -7.88518 | -54.72699 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 832fca26-f290-32aa-9627-a9c9cf8cb791 | -7.87163 | -55.52245 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 129d1103-19d5-31de-9d3d-b307ae4ba97e | -7.86886 | -55.5184 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15a8bd44-a56a-3790-8912-d6e711eb1f77 | -7.86553 | -55.51788 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfbae6f5-5d33-3b69-98f6-7b4fcd6d47a8 | -7.85827 | -55.54205 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 532ca460-52f7-36ee-adf4-459e3f3b197d | -7.85771 | -55.54559 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b483b3b-ff9f-312c-a5dc-f04bf3f7f937 | -7.85494 | -55.54152 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97298195-3c47-3929-ad15-4777e7af9052 | -7.8516 | -55.54099 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f9c253a-d6d5-3ecb-9fa0-f52da4a5b3f1 | -8.96955 | -55.06102 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ce629ed-2ddc-3b9a-868f-37d90e6205b9 | -8.94971 | -55.03294 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e13732f-6072-3b38-90c7-cc62e4c36f55 | -8.94866 | -55.08615 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c560f6c-3ac2-3c97-bc7a-cbbf7a8cc2cb | -8.94644 | -55.07512 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7280904c-d8a9-3f5e-ab03-0da6b31a8831 | -8.9415 | -55.08502 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f0bc419-5e28-3aad-8d8b-dedca4144ded | -8.94095 | -55.08849 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 976d0a56-f02b-3a56-aaab-aae88d53e6ce | -8.93875 | -55.08102 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c56e4102-1773-35d4-b659-2193683b305f | -8.9382 | -55.0845 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43ca88ed-80dd-3cc8-ae26-8fc0faf42547 | -8.93765 | -55.08797 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4202ce2f-b6a4-3468-80fc-e39ff5c81e7e | -8.52318 | -55.19263 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8934c10-efb9-3062-bed4-8b906e82914d | -8.51931 | -55.19559 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e9a22b03-d9ca-3517-8358-04e657b30530 | -8.51656 | -55.19157 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ec0ea545-ef77-3832-b75a-a57caee0d1c7 | -8.51601 | -55.19506 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05d1a2bb-bdc4-3d1b-9fd0-84de1388dab0 | -8.48696 | -55.03344 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad68aeac-548f-353e-aa64-e8c640a711a5 | -8.45831 | -55.00042 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47d3ae36-9159-380e-875a-068dcca6464d | -8.44718 | -54.83513 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb1f386d-9969-32b5-a940-3fdab5dc69f6 | -8.44334 | -54.83808 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9402550-a3a3-3940-b2d0-745e57ff62a2 | -8.43351 | -54.92178 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b783e62-a8fa-3d8c-9a19-9fe3bf89f300 | -8.43185 | -54.91085 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e7f0d74-f12e-3ab9-b4a3-c0cdd3686e92 | -8.4283 | -54.82144 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 639bdb61-9c08-3f3f-81e7-1ce594298c61 | -8.41704 | -55.02589 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 121fff9a-4885-3433-9522-3a8ef44a7865 | -8.41538 | -55.01495 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c7744d4-a644-3ae5-82ce-361cf2ed5305 | -8.41483 | -55.01842 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02d36ef2-ff36-321e-896b-1d79fc1114dc | -8.41428 | -55.02189 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc069296-515f-36b2-a050-01dd41be3676 | -8.41373 | -55.04676 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b8cac5-754a-3c53-ba18-81794cffea2c | -8.41373 | -55.02537 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f8da031-a37e-3224-b252-a763e45673e7 | -8.41147 | -55.01429 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b12c30c-9ea1-35f8-b270-980ae86d4c6c | -8.41098 | -55.04275 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60cc5010-39fb-3374-9cf9-b865b45bc85c | -8.41092 | -55.01776 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e7ff7dd-8417-3682-9f9d-e7533d1d75aa | -8.40987 | -55.0497 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce25fcc8-f253-3be0-aba0-de22b58bb7fc | -8.40819 | -55.03513 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e471a649-03dc-3320-baec-44d4a6082df9 | -8.40707 | -55.02071 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b8f58d7-1ead-37ba-85e2-d8569bf3ae50 | -8.40601 | -55.07404 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4a3ddc4-2486-35b9-b64d-1f5f3ada5a4e | -8.40213 | -55.0306 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b820fba-14c4-3ac2-a7fc-a65a11e60066 | -8.39828 | -55.03355 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20e636a5-af8d-317a-88f1-88d2cc9b9f0a | -8.39717 | -55.01913 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55a87101-5297-3d3c-baa1-4276aac4a019 | -8.39443 | -55.03651 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8aa5f260-3ae4-36cc-ba30-6b6f73b6793d | -8.39441 | -55.01514 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3197b187-75c9-3db9-98e8-a15120830346 | -8.39435 | -54.95108 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc2868ba-1765-399b-97da-5777dad8eb36 | -8.3911 | -55.01461 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac9dcb4c-69dc-3870-98fe-02d2e3c07fbe | -8.38884 | -54.9431 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56843303-bff3-3809-96f1-c5b8501c346c | -8.38671 | -55.02104 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03ca03f4-ebdf-3c02-b7c3-85a1d84a5d60 | -8.38667 | -54.97832 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2113766-8236-359f-ab2e-659f4da950ce | -8.38665 | -54.95697 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc263285-e67b-37f8-820d-6216a6739e28 | -8.38445 | -54.94951 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0427f30-7cea-3b21-a84a-714b1f6dc01a | -8.38278 | -54.93858 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff89abf6-5b97-3a28-a9e0-7be4d1dd38f3 | -8.38231 | -55.02746 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cb33de0-29fd-3bdb-a8cb-d0236e9c249c | -8.37452 | -54.92661 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ce28572-7dca-3061-860e-e32e3281ce1b | -8.37132 | -55.0756 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44cdcd46-0028-3b54-9916-f514e95b1b7d | -8.36801 | -55.07508 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 757355cb-66ca-3c21-9d50-d01796932819 | -8.36793 | -54.9469 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60865e42-aa8c-371b-b838-1d2866501bee | -8.36739 | -54.95036 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44344c30-be77-3c4a-be02-b1ff54ae60d9 | -8.35919 | -55.04516 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e3e4f4f-dfc6-323d-bdd3-9d3cc9d9ddf3 | -8.35864 | -55.04864 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91fb9fa0-8d9d-386b-b724-8890e27118f5 | -8.35424 | -55.05507 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dab4dc7-8254-3ed9-a44f-816f6b5090bc | -8.35369 | -55.05854 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d501afc0-55e6-3883-a3e6-dcfa9d67276f | -8.35364 | -54.97308 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf46a4c1-0bc6-3c9f-8bd0-274b4725060d | -8.35314 | -55.06202 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9dcb49d-8f17-35ba-a61b-3d3b20ae39e3 | -8.35259 | -55.0655 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58d1cdb5-c956-3389-846f-b5a3cfeebf20 | -8.35204 | -55.06898 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26556e92-432b-35ec-805e-b59f8c7aee3e | -8.35034 | -54.97256 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eb3357c-31c7-3819-9364-7429179b6d67 | -8.34983 | -55.0615 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac7f5ad8-aa3f-3a29-817d-35f80dc562e4 | -8.34979 | -54.97603 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b31ee94a-12ba-368f-b969-78989310e590 | -8.32778 | -55.00814 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f83cd820-1564-319f-a6f1-73399c1c5c16 | -8.32118 | -55.00708 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43cc21fe-3571-3c11-8630-6a217d7c6e08 | -8.32063 | -55.01056 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172e3d0d-9e8f-3a06-a31f-068ce8f12f12 | -8.31898 | -54.99961 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 30446510-72a5-3234-8e73-23f40cf3214d | -8.31843 | -55.00308 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 53c62045-eae7-3dc0-8363-25a3d87819e4 | -8.31788 | -55.00656 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5e20e390-c4ce-35a2-85bb-5f398f3b1d92 | -8.31567 | -54.99909 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d49399c7-5297-344c-887a-ce163a5a57f1 | -8.31512 | -55.00256 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 6fff9eea-5262-353a-9ad7-4ac60c928118 | -8.31457 | -55.00603 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2730b2f1-651a-38c3-8a2c-761754e38e37 | -8.31237 | -54.99857 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81e8f995-109b-348a-a6bb-b20375de8025 | -8.30906 | -54.99804 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9edbe2-faf8-3009-b4b0-52b58d35566a | -8.29394 | -55.39253 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c4d91a4-1d57-32a0-8b48-7ad8dcd11907 | -8.29217 | -54.99469 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7d554ab-b94f-3b8c-8c19-19870509d19d | -8.29162 | -54.99816 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21995826-d1e1-3644-a1c2-a08e99200533 | -8.43931 | -54.83739 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43614acb-63b6-3b69-a9c7-7c2000a77f92 | -8.4305 | -54.82889 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa0312d6-6f8e-372b-8a97-e2880fb8f747 | -8.42666 | -54.83183 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README104.md)
