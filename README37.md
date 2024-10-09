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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8bfd641-96dd-3407-bb16-d99f5cd03dab | -17.146999 | -57.4119 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac67d69d-6445-37e6-b42d-5ed6ec97b438 | -17.148701 | -57.419399 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d5dafd50-b796-39d6-afc5-ab8fb79b3978 | -17.1504 | -57.426998 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ed6859b-a529-3a8e-94bb-b390e5ab782d | -17.1521 | -57.434502 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7836ef94-23a1-35fe-bf65-33bf382dabd6 | -17.1539 | -57.442001 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f4131bb-78a2-338f-b000-d2699657a8e7 | -17.1217 | -57.346298 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5b7ad00-9538-30ea-87ee-7e54bfd37e88 | -17.1234 | -57.353802 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ab678a0-fa25-31bd-8fbd-9f1d2885a6c8 | -17.125099 | -57.361401 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97a7eb9f-37b4-361f-8cca-a2fd9baf6483 | -17.133801 | -57.3992 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71313e44-51e2-37f8-866a-aad0bae8b5e3 | -17.1355 | -57.4067 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55d2b9df-f219-36d9-a5de-1ff6b6ce3c7a | -17.137199 | -57.414299 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99c7672f-6c3e-363f-a55f-59385a24d5b3 | -17.138901 | -57.421799 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a17cb808-904e-350a-b939-9d96e72daba6 | -17.140699 | -57.429401 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3dbe48f-a8a4-31ee-bc5c-20fd1ff321f9 | -17.142401 | -57.436901 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d1ac323-337e-35d9-a9af-2bdcddbc6964 | -17.1441 | -57.444401 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 20f69a7b-96f8-3b05-a98d-e889c14cf064 | -17.1101 | -57.341099 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4da99ff7-de03-311b-b6dd-142abe3bd8f0 | -17.1119 | -57.348701 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13d548b7-8762-367d-aa61-94f147d41a5b | -17.1136 | -57.356201 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa6f843d-62e1-3ebd-9805-5076f25cafa7 | -17.115299 | -57.3638 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fcf43192-1d03-3705-ac6f-63c9e84246de | -17.124001 | -57.4016 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b8a2d61-78ae-3c95-8952-2a39269c160d | -17.1257 | -57.4091 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fcdf60a-1cab-3493-8c36-9f868f833e66 | -17.127399 | -57.416698 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 957673da-e623-3e68-a9f1-402ac9284169 | -17.129101 | -57.424198 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98d69bbc-77ec-347c-805e-cfd128224b60 | -17.130899 | -57.431801 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 740ace26-cb73-38d5-9712-fdbd5ffe771e | -17.132601 | -57.439301 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2cdb407-96ee-34d5-9ab2-d7e75a2ababd | -17.1343 | -57.4468 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a05d99d-df45-37ce-a799-e911c8cc449f | -17.136 | -57.454399 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a66fa05-1dd8-39d5-9d59-a3bec0ef17ab | -16.961 | -56.739201 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b31daf1b-b1e1-3a97-80fe-6e7601a10631 | -17.114201 | -57.403999 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a67b6ee-5719-334a-94d1-a57c2284e9fe | -17.1159 | -57.411499 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aad14bcd-1224-3e6a-8dcf-804b59733bbb | -17.117599 | -57.419102 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 102a9939-707e-3151-9a8f-e459f3f190f9 | -17.119301 | -57.426601 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8d29649-fab3-3152-ac38-580f395babd8 | -17.121099 | -57.4342 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7bba03a2-346c-35a7-9dc9-5329bb74afc7 | -17.122801 | -57.4417 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fdb9257e-e59f-36a7-af4f-9d67e6abe97c | -17.1245 | -57.4492 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f3d35e4-b37c-3deb-bb5e-842c4073a33e | -16.9512 | -56.7416 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf31f3d3-fbd5-394d-800a-6a269af9936f | -16.952999 | -56.749599 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81d6d719-072f-3a7f-981f-7953ddd53b3e | -16.954901 | -56.7575 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2a7a4c0-a751-3882-b841-abafcd2d5ab7 | -16.956699 | -56.7654 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b6c8a73-1dae-34cd-b6c6-48d4f5769563 | -16.958599 | -56.773399 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ba02d9d-7b62-33da-a2ed-5a8c1acb739f | -16.9604 | -56.7813 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8b59b6d-22ed-3213-a83d-c9097c1b97d0 | -16.9622 | -56.7892 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1695327f-63d1-3555-8390-25c1daaa37e1 | -16.9641 | -56.7971 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 467a0b13-bd7a-3f5c-ab2c-faac930c8068 | -17.1045 | -57.406399 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5eb21026-581a-38d5-8fac-49a79baf61d9 | -17.106199 | -57.413898 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c4aa335-d0e9-37e7-83d4-84ed081bbb28 | -17.107901 | -57.421501 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a31f280-ccd8-3fd3-8c57-0bb5db2be63f | -17.1096 | -57.429001 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d564b55c-9355-351f-8b3b-e3edf3d56c20 | -17.111401 | -57.4366 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8a0b0da-ba90-314b-8458-7413ff2efbfa | -17.1131 | -57.444099 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ceaef23d-b378-39f3-ac1c-8b71175f20cf | -17.114799 | -57.451599 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fd6db70a-8522-3878-8f90-cf76b593a6d7 | -16.9452 | -56.759899 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6132a426-bb9f-30c9-9467-eb304aa930e0 | -16.947001 | -56.767799 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2b30b17-c51c-3027-a4cc-a54fc99c355b | -16.948799 | -56.775799 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45ca399f-566a-3f0c-a206-45cdf9c03c75 | -16.950701 | -56.783699 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6f069c9-39f8-3ffb-8966-e74ce6a69a70 | -17.0947 | -57.408798 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a195dc39-315b-35b4-83d1-6a2ce25ebb07 | -17.096399 | -57.416302 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a456705-e397-3084-8f8c-053d24cbdf81 | -17.098101 | -57.423901 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92565a5e-b6c0-3091-ac64-efbfe7f5c687 | -17.0998 | -57.4314 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a49e21c-eeab-3a24-9d5a-e36779012641 | -17.101601 | -57.438999 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa724621-b64f-348d-8f4e-e0dc3fc87032 | -17.1033 | -57.446499 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03f6fb4e-2652-39d2-a0a4-8cb0cc2e5325 | -16.9354 | -56.762402 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f244a0f-c4aa-3097-baf8-dd450bcac98b | -16.937201 | -56.770302 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71208170-8225-3f58-b5a7-5999a4164429 | -16.9391 | -56.778301 | 2024-10-09 01:24:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 248bb4a1-4890-3d3f-95d4-727c2121b703 | -17.0849 | -57.411201 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 993d64eb-e839-3234-a9cb-1bdb062121ae | -17.086599 | -57.418701 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c3bfa90c-5e9d-3ddb-99e0-7d23f62b041d | -17.088301 | -57.4263 | 2024-10-09 01:24:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acaba424-b9d7-3ad9-83e1-e99eb87f0762 | -16.8913 | -56.7061 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0cf81fbc-8804-3707-9cf7-ef6b30e07640 | -16.6971 | -55.922699 | 2024-10-09 01:24:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91e7e61a-7c79-3973-bb2e-fbef343da878 | -16.875999 | -56.6847 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b04947d1-8574-3f16-aacc-f871648c07d8 | -16.877899 | -56.692699 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bba97315-520a-3c20-a6f9-3f8974d4fe7b | -16.879801 | -56.700699 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe9ed762-63f8-34d1-9020-6c495fae1d35 | -16.881599 | -56.708599 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d171041f-53de-3db2-9ee5-86de8c5224f0 | -16.883499 | -56.716599 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f657d7be-ef2a-3539-93d4-ca1a94d19898 | -16.8853 | -56.724499 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b9618b0-d170-3cc5-97b2-2925517b1bb6 | -16.868099 | -56.695099 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc4ee8e9-2c94-34ec-a9c2-e6333c57490c | -16.870001 | -56.703098 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40372c6b-060c-3026-95cc-f1c19cd51752 | -16.871799 | -56.710999 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2d616b1-5325-31d2-9f17-5432a2d075db | -16.873699 | -56.719002 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 27700dc0-701e-332b-9692-e13620b43bfb | -16.8755 | -56.726898 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 136295c0-6c3d-3baa-ad62-1c6c5e517535 | -16.589701 | -55.558102 | 2024-10-09 01:24:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2dbd0e05-12bf-33b9-9f6e-300068c55805 | -16.5919 | -55.567001 | 2024-10-09 01:24:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2ea99f9-5861-31a4-8b32-ffc2e1f50937 | -16.863899 | -56.7215 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ee5c034-c468-31d4-a13b-47711f34bcb9 | -16.8657 | -56.729401 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28ac04a6-ad52-33ec-a716-53425d429610 | -16.867599 | -56.7374 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41ca061b-3e86-3164-b5a2-1ce4903da49f | -16.8449 | -56.683998 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6c70b33-c404-34af-8cd2-3d21092f7044 | -16.846701 | -56.692001 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75fc793a-55ff-30fa-b92e-012ee232ca29 | -16.8486 | -56.700001 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9213f6ae-7803-3981-aef4-6145e68e5df5 | -16.856001 | -56.7318 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1cebfd1a-756b-3098-b909-c048beb996c2 | -16.857901 | -56.739799 | 2024-10-09 01:24:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9eaeec77-d838-3e70-892c-decc04cbcb3e | -16.6458 | -55.880699 | 2024-10-09 01:24:56 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1714c7e6-e730-3142-9b4d-18f482df0cfd | -16.6479 | -55.8894 | 2024-10-09 01:24:56 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ef5d928-656a-350b-97e8-a8f56a99c9c3 | -16.8351 | -56.686501 | 2024-10-09 01:24:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a443020c-dd7e-3664-9ff9-2e32d6860d86 | -16.836901 | -56.6945 | 2024-10-09 01:24:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45ca9d47-4e12-3c4f-9532-44a782b3aefd | -16.842501 | -56.718399 | 2024-10-09 01:24:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40a4a8a0-7d76-366f-9c32-5772b28f0951 | -16.8444 | -56.726398 | 2024-10-09 01:24:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f85ae318-51a7-34fb-8846-d81e01db17c5 | -16.846201 | -56.734299 | 2024-10-09 01:24:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0c63493-54f7-3c3d-b1e1-602513831e49 | -16.636 | -55.883202 | 2024-10-09 01:24:56 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d216f55a-879e-3045-8124-07efe4483900 | -16.832701 | -56.720798 | 2024-10-09 01:24:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dde3d4c7-8d71-37ac-822d-123bbb07d22e | -16.8346 | -56.728802 | 2024-10-09 01:24:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ff9d2239-b4fc-3c4d-8461-f1cf6920b716 | -16.7728 | -56.685101 | 2024-10-09 01:24:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README38.md)
