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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 874f8069-4eeb-3d20-abba-ee9d931d83cc | -17.2933 | -57.4857 | 2024-11-12 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 712d8078-e4d7-3e22-99ef-d4b23417239b | -2.7402 | -49.3502 | 2024-11-12 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 87d9003a-937e-3b19-b395-c539c835327d | -17.2737 | -57.488 | 2024-11-12 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| f976c09f-5690-33b0-bf5f-f4e8498a2a4f | -2.9913 | -51.3356 | 2024-11-12 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 4cd22767-303d-38eb-9af5-c08846917d6b | -17.6073 | -57.5099 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 7420b6e2-e8e4-356d-ad9d-d9d11c2c961a | -3.0913 | -54.287 | 2024-11-12 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a50561fd-08de-3100-a1b8-c4bd51337879 | -17.5872 | -57.5328 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| b7b24729-95e6-3b8d-9ddf-c12404f393b8 | -17.6283 | -57.4252 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 7754981d-464b-3b7f-af5c-f3234d07e63d | 1.048 | -60.5986 | 2024-11-12 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fb12d9b8-819e-3cad-b3c0-2c2d9378fbdd | 1.0663 | -60.5985 | 2024-11-12 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 92501404-7896-38d7-836c-c5abf94de78d | -3.0913 | -54.307 | 2024-11-12 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b4dc52fe-6fc4-30f9-a0bd-f811a23e4e8e | -17.6069 | -57.5304 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| a5cdf545-8a1f-325a-8027-59536af67c8c | -17.6477 | -57.4434 | 2024-11-12 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 54497de1-6c92-3cb9-ab87-584291b51db9 | -2.7587 | -49.3497 | 2024-11-12 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 215.9 |
| 8a86b384-bc79-3920-8f20-690a019c953e | 1.0663 | -60.5795 | 2024-11-12 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 9c48d555-d2a9-359d-a1a2-5d48d95d2303 | -3.1097 | -54.2865 | 2024-11-12 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| fb0dbdf1-e169-333b-8228-e70176d27051 | -2.7588 | -49.3285 | 2024-11-12 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 74be8a53-c68e-3475-8cb8-86f66b8eee9c | -2.9982 | -49.5336 | 2024-11-12 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4824ac23-54e2-3244-8ad8-cdea8365564f | -17.274 | -57.4675 | 2024-11-12 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 44e083ad-c178-3435-91d4-0e80cc7cb648 | -17.3126 | -57.5039 | 2024-11-12 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.3 |
| a6921b95-c327-38f9-b0a2-1e0a31522c69 | -4.1941 | -46.185799 | 2024-11-12 00:31:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2eb8945-2c44-381c-803c-1abe6fc4177d | -3.8097 | -47.798698 | 2024-11-12 00:31:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 610e6b2b-8b93-3d7f-9f4d-78eaaf2eb555 | -5.9162 | -42.973 | 2024-11-12 00:31:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e141235e-5569-3aa5-87b4-979eb982ddd5 | -1.6103 | -47.514702 | 2024-11-12 00:31:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 678ca2e0-4897-3139-a2e3-38fbae20facd | -4.0862 | -47.700199 | 2024-11-12 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a2d87a0-3748-3f16-954b-7f11953b1a89 | -3.0854 | -54.297798 | 2024-11-12 00:31:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| debca905-60fe-3dae-a088-c55a03e4d0fb | -2.3654 | -48.5172 | 2024-11-12 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9200883e-7f47-387d-be52-10c45a534e90 | -3.0952 | -54.2957 | 2024-11-12 00:31:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ace13b-153d-3e24-aaaa-1ebe21184c93 | -2.75 | -49.346901 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c94e589-7c9d-37d5-9640-8057870bb92d | -2.5375 | -45.397701 | 2024-11-12 00:31:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 178909d8-7f07-357b-8a71-edfca3521bf0 | -3.9537 | -46.712299 | 2024-11-12 00:31:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33a325ba-45a0-3f3b-9651-f7cba1e68fcc | -4.2097 | -46.884998 | 2024-11-12 00:31:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5ac5c4d-bafe-3a60-932e-0d44f2357ee4 | -2.7789 | -51.747002 | 2024-11-12 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee0462be-1c7e-3b48-9654-9f07b40de35e | -4.0878 | -47.707199 | 2024-11-12 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b83b46d1-9b63-37b6-a670-309e483d3524 | -20.318399 | -48.820202 | 2024-11-12 00:31:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e396aabd-5cb2-384d-8370-7b1298bd9674 | -4.0605 | -43.953499 | 2024-11-12 00:31:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7ff465-36bd-37cb-8215-7872df62d929 | -2.7732 | -50.3111 | 2024-11-12 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cddc0795-ffef-3ba7-a9d9-89090344a1ad | -2.6768 | -48.662701 | 2024-11-12 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98a512bc-139b-3925-91fb-4eb8fb93fd41 | -4.4467 | -44.8181 | 2024-11-12 00:31:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c56b35ef-11db-3fd0-9f86-ee61334f4969 | -5.5172 | -39.098598 | 2024-11-12 00:31:00 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0ceecf6a-7e4d-3f56-aa3c-e99962dbe21a | -5.8831 | -39.673401 | 2024-11-12 00:31:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 56bcf2f7-eb0f-3a68-8b20-c4078022e00a | -5.9304 | -39.4855 | 2024-11-12 00:31:00 | METOP-C | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 980a37bc-1c50-30bb-83f1-9573d8990905 | -5.9272 | -39.4725 | 2024-11-12 00:31:00 | METOP-C | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 29e2ed76-9b2b-3142-aab4-7b1b5c56fcf9 | -2.9025 | -49.247601 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4049be46-3e77-36f1-b24d-aabf57d605e3 | -2.8945 | -49.257599 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7986c570-8bd1-3142-bf70-cdfaef1297b0 | -3.808 | -47.791599 | 2024-11-12 00:31:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d0a6e6-2d43-3a30-be43-e2edb81e5a66 | -2.8927 | -49.249802 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485f195c-177b-371b-be1d-d4cd937f51ba | -2.8154 | -46.651699 | 2024-11-12 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8e38547-c427-38cc-be6f-c90b59492d2d | -2.3146 | -48.429901 | 2024-11-12 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b277a7f1-576a-3f00-be42-9d12a32002ee | -3.5575 | -43.565399 | 2024-11-12 00:31:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 572b3a73-1c4b-3bc2-a45b-dec90b7aa2c6 | -4.1925 | -46.179001 | 2024-11-12 00:31:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cfd6f238-74d7-3b20-8c83-14557bfe8aa4 | -2.9805 | -49.545799 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 910e9d32-47c5-33f7-9d15-ae29d68cbe81 | -2.7679 | -49.334801 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2938568f-e99b-3980-8e3f-b28c15219346 | -2.9512 | -49.098999 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac39af2d-23b6-3d3d-b9a9-8c47109dae1d | -2.526 | -45.392899 | 2024-11-12 00:31:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6a9b6ad-091b-3692-810c-d6a55dcc8c41 | -3.8033 | -48.951302 | 2024-11-12 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986b78a1-168e-3010-984f-89b3e0c8d5f4 | -2.7823 | -49.217201 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8d0a005-1b0a-3078-8cc4-2b3695fae0e6 | -3.6928 | -52.116199 | 2024-11-12 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d27ff0f-61c0-31ae-ac6b-34138c5eb81f | -2.7518 | -49.354698 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f28afe8-64bb-3c68-8982-7dbb6966e772 | -2.9903 | -49.543701 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de2951e-c385-38a7-8bd9-c032ed4da6ae | -6.9716 | -40.0387 | 2024-11-12 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| febfd61a-c048-3eea-a677-7de4e0bddb36 | -2.7581 | -49.337002 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b08dbb70-b67f-3f48-8fc4-33a2a8c8100f | -3.2636 | -48.751202 | 2024-11-12 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f834beb4-f32c-34d4-b0e8-e35fa7f77e9d | -4.8768 | -44.402599 | 2024-11-12 00:31:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd19bd4-bd6e-3222-9381-33997f633894 | -3.4774 | -44.9547 | 2024-11-12 00:31:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 584332d3-c822-3d0b-8ef1-65438373a1c7 | -2.7014 | -49.178398 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04617863-6e0a-3762-b342-37618396f50e | -6.9688 | -40.0271 | 2024-11-12 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| eb39851c-f96f-3ef6-9599-762876e1b716 | -3.4597 | -49.206799 | 2024-11-12 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1917ff4-9405-3a8e-8e7e-aaf295c0fdca | -2.9885 | -49.535599 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a381db5-60fc-3cc6-bbe8-7355e3900b68 | -20.635201 | -48.835999 | 2024-11-12 00:31:00 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8f65d77-efea-38a1-a55d-86c9a6e65c58 | -2.9836 | -51.3339 | 2024-11-12 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 367b5643-b6f8-33fd-9cad-d9ebb06883c4 | -3.0916 | -54.2798 | 2024-11-12 00:31:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce00d4a-f2e3-34a8-abe4-17eb0f39dddb | -16.568701 | -44.063702 | 2024-11-12 00:31:00 | METOP-C | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b2e15a28-130b-39bb-8b3b-446b91684bc8 | -18.3454 | -40.018799 | 2024-11-12 00:31:00 | METOP-C | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36ccb04d-a16b-38a8-b176-17637c1a2da5 | -2.7809 | -50.300301 | 2024-11-12 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08008fe4-8d0b-3ead-b23b-242003a933d8 | -2.7598 | -49.344799 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba804dc6-e0c4-3828-b6ef-3ae4a7756a2b | -2.3162 | -48.437099 | 2024-11-12 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abaef80d-edbb-3604-8475-d971d0f3c2e2 | -2.7841 | -49.224899 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 670230a4-94f5-3944-8dd2-ff2506972ebc | -20.320801 | -48.833 | 2024-11-12 00:31:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4babc4be-4f62-3fa3-b5b1-1296058cf027 | -2.5292 | -45.406898 | 2024-11-12 00:31:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb32cfc1-0b27-3cb4-b83c-e81b39805d30 | -3.8068 | -48.966801 | 2024-11-12 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84eb03bb-bc22-30b4-b0e6-a882ade5f829 | -6.9813 | -40.036301 | 2024-11-12 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3d309cc7-b56a-3db8-ac1c-29a26482a030 | -4.4451 | -44.811001 | 2024-11-12 00:31:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b1eb783-4445-3dbd-8808-dad39668b8a5 | -3.8051 | -48.959099 | 2024-11-12 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d7e485a-36ee-362b-a8a5-d8e1abd527fa | -2.5406 | -47.523899 | 2024-11-12 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e72262-01ef-31d0-8044-8a3906016a3c | -2.9738 | -51.335999 | 2024-11-12 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d17b740-b372-3a76-a447-5734cb089743 | -2.7385 | -49.341301 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae127b4-2bd9-3eb7-9a9a-0be7d482c5f2 | -2.5422 | -47.5308 | 2024-11-12 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03acad60-fcee-3211-b030-09de6b9d00b0 | -16.570299 | -44.070801 | 2024-11-12 00:31:00 | METOP-C | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4322b76b-e724-38c5-bfd7-198ef2b55c06 | -4.8866 | -44.400299 | 2024-11-12 00:31:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7cbb8ca5-2ecb-341f-9029-2f61011966d4 | -3.4579 | -49.198898 | 2024-11-12 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 975a228a-7ae5-3ee7-8880-fe5ab32e3bab | -4.2081 | -46.878101 | 2024-11-12 00:31:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c15610a-f736-3322-858f-cdcce56da70e | -4.4831 | -46.321602 | 2024-11-12 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94d2deaa-34ae-360a-9891-8e4901ef51e3 | -4.7111 | -47.23 | 2024-11-12 00:31:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0243fde7-a3f1-3edc-a049-10b35d06781b | -2.7616 | -49.3526 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04babc8e-951e-3b08-b513-5bfd0575eed9 | -2.9761 | -51.3461 | 2024-11-12 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f106b351-a232-300b-aa2d-d45cee19067d | -2.9859 | -51.344002 | 2024-11-12 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc9fe36-4da1-303c-84cc-8f3a2bdd1a5d | -4.8004 | -45.277401 | 2024-11-12 00:31:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a8d8407-025b-3d7d-ae72-18b20b40f6fd | -2.9787 | -49.537701 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef876f21-7e7f-362f-aaeb-e9f98d7c229a | -4.0623 | -43.961102 | 2024-11-12 00:31:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
