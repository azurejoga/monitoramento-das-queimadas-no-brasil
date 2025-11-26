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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dda3b396-3a10-364a-8f73-39e790691e99 | -3.02918 | -51.03021 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9a8d3df-8b5b-397e-9e63-f46ceeea1054 | -2.9352 | -48.23232 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f62571db-2988-3757-8c83-118de1a66435 | -4.46277 | -50.79256 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d3f922-31ba-3887-8a9c-669025338019 | -4.65992 | -43.98189 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 1dc83402-c359-38ce-9eef-6ad2e7e44a18 | -3.2413 | -50.59391 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6eca05d-c673-3959-8745-ac4c31bd87d4 | -3.21135 | -50.22161 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52077c26-56b4-3426-9fa1-6e7f8cba1b86 | -4.68078 | -49.37984 | 2025-11-26 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6860dd3a-7c13-3115-9a06-c52eb24aa0b6 | -4.70662 | -43.99556 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b469e035-8d50-3609-9dce-faa0dd08441a | -4.17798 | -43.73381 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9090d64c-b591-36d9-ac25-09b287ff8769 | -2.74137 | -47.13334 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52f39355-ff47-3135-b0a0-a374f8038939 | -2.93101 | -48.22567 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3bdf299-3bcf-35f6-b6e9-dc9067f0d65e | -3.36049 | -49.50557 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46f3824f-6412-399b-a8a6-4bc4a614764e | -4.009 | -46.49978 | 2025-11-26 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5cae26eb-8157-3a0d-a750-09ba2684fe53 | -3.96301 | -49.03652 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d76ad9df-7dc9-37a8-8dea-cd3edd61fc8e | -4.17476 | -43.70734 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2a36f1d7-faab-3a7f-b34c-50cc30806040 | -4.97343 | -50.87457 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7bded56-5516-35ec-9d48-32a3ee7c6099 | -3.07503 | -50.26019 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fda79ee2-5055-3e9d-99cb-f2e08eed4279 | -7.1669 | -44.99607 | 2025-11-26 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 002bef00-2daf-37d9-846d-1e1e39658cf5 | -6.87747 | -47.24353 | 2025-11-26 05:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 845cc6d8-b101-3df4-808b-5933de85732f | -3.02617 | -51.22129 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a2d14d-ad8d-314a-8561-2c78a1dfd438 | -4.16722 | -43.71719 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f1d6908f-7cbf-3a35-a8f4-a37292164406 | -3.02445 | -51.03337 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00390643-1a56-3d53-99dd-9d989bc7be3c | -2.88217 | -51.78275 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75e40b09-e9a9-381d-83fb-34c1f0b775c6 | -3.45673 | -50.53979 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f4775ac-c3f6-35ee-93cd-4bc6849ce0e3 | -4.67525 | -49.38434 | 2025-11-26 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc5bef2c-3835-31f1-aae7-e9af295c6c99 | -4.72101 | -46.45782 | 2025-11-26 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 992a292c-796e-3157-84e6-8a80a0c36482 | -4.17565 | -49.86547 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fccaf509-49d1-3068-b86c-65b63c749654 | -2.57066 | -51.82238 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8382455a-d85d-3024-9c0d-330637a12bcb | -6.76378 | -46.51605 | 2025-11-26 05:10:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 760c1373-51a7-3aa4-ab51-6b45b57b4f0a | -4.66538 | -48.48482 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f082139-4ca2-3ea8-99be-f250a6d2244e | -4.67597 | -49.37925 | 2025-11-26 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6698d7d5-cad9-36fe-a7bb-9464c4952156 | -4.60241 | -44.41032 | 2025-11-26 05:10:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 552e4be5-42c5-3f94-8820-dee4aa7dd721 | -4.17405 | -43.71847 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| af149cdb-e2f9-37a0-a37b-1fd02200dde8 | -2.94111 | -48.22725 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46acfdf1-80de-3e77-80e9-f78e20bf2176 | -5.70451 | -47.06055 | 2025-11-26 05:10:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 714627ac-4664-32ca-af90-b7113e823421 | -4.057 | -54.47502 | 2025-11-26 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adc242e4-1764-33d1-8733-ba42768bd2a9 | -4.72044 | -46.46181 | 2025-11-26 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d148b5f7-16e3-394f-b41e-9944e0bb3bae | -4.10407 | -49.07026 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e3c9665-90fa-31ed-8c6a-8b2f1ee1f180 | -3.39628 | -49.521 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7a65d71-d976-3fb5-a513-6dd52a6b6e6f | -3.32393 | -49.72306 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7436e2b7-1075-33eb-a76f-c557aa0f4249 | -3.22468 | -50.58715 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 526f11a9-8bc5-3c19-9dda-87507d9d2b5d | -5.28989 | -43.64349 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8fc0a15-2291-30c2-abc1-866d3ebaf0f1 | -2.37722 | -48.66528 | 2025-11-26 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 362243be-c07b-382d-98d2-5957f6c12237 | -4.28346 | -47.3093 | 2025-11-26 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b386165-139d-3ce8-b196-cc39e3bf1005 | -2.89011 | -51.80996 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f12fc96a-a0e3-33d2-8224-ac037f120657 | -3.32465 | -49.71838 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 600fff00-b317-373a-8b60-febc23d26b44 | -3.3785 | -50.57617 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36650141-5de7-3e01-aa35-c31742548199 | -3.66564 | -50.16603 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47693f9c-1283-359e-84f3-925302b6dcf8 | -1.35971 | -55.42874 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3975dbc5-5d4e-340c-bfc2-8944048599dc | -2.94068 | -48.23017 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8187144f-d23f-3982-b8d6-d274ee23a866 | -2.74731 | -47.13064 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a611d860-3732-3ac4-8a11-f01a002f4ec2 | -2.60528 | -48.14032 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 933ce13f-ac78-37c2-abb9-2152ed861a51 | -5.33578 | -43.56834 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e04f723b-0977-3617-af80-4f76d33311ab | -2.93058 | -48.2286 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 91cfc0e5-9f2a-33d4-906b-ff09a7ed3761 | -2.92555 | -48.22772 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7798d135-64eb-3516-b21f-aaeec9ecdede | -2.8522 | -50.73685 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4341480-dfd3-3ebe-97a8-e04e82f813ba | -3.53494 | -53.25524 | 2025-11-26 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a50685a9-db34-3fd2-b2c3-5c767b45434a | -2.94213 | -49.36406 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc21dcdd-3654-3d42-9570-c8ece038ec7c | -2.47263 | -47.83051 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2c1eccf-c19a-3153-88f7-67d698d7e989 | -2.88299 | -51.80373 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4b5ed9e-3bc1-32f2-94e1-49446d41a333 | -4.09923 | -49.06942 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05c5a10c-f6d8-32b6-837c-e280f31779ab | -3.09519 | -50.55233 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70868219-4a7a-3f3d-b21a-f61e32091567 | -3.45611 | -50.54398 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b09e403-aaba-30b1-858f-22393cfde6a6 | -3.02074 | -51.14457 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a035fd12-9aa4-3a1c-818d-34625e823f34 | -4.05741 | -48.82261 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e886f2ae-b2b4-3877-8124-04ac0ceb3dd4 | -3.34981 | -49.7719 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b29590f3-46b6-3b87-b4a1-a51ea1d28608 | -4.81393 | -43.82597 | 2025-11-26 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12106c68-d879-31cf-a58a-0ad542b55ea1 | -2.50024 | -47.82232 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50f473c8-914b-32eb-b8aa-7f3157e655df | -3.65851 | -50.48602 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33b327c0-e788-330c-bd1a-b13f8fc9c91e | -2.92511 | -48.23066 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aef40143-c8ff-374a-bb52-4dbb3482d687 | -2.48478 | -47.81985 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6feb0bc6-d78a-3d87-990f-4a14e2e363ac | -4.71665 | -47.15781 | 2025-11-26 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0072ac04-eed6-37e7-b72d-93c8c1659b0e | -4.28511 | -47.29795 | 2025-11-26 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be3b034f-c558-3e0f-bb14-ea36150e4de2 | -4.17428 | -49.87496 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25960180-bb75-3ee0-b837-061df9562f34 | -7.56243 | -45.87486 | 2025-11-26 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb22d6cc-79a7-3ea7-9ca3-5f8365d5e602 | -3.21475 | -50.16904 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 045b90ab-923e-3341-ae95-89c6da0320e8 | -2.87821 | -51.78215 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1f0f619-470e-351f-a5dd-cdb58595f156 | -4.30923 | -50.74154 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81ee7190-ecba-3d69-ba0f-ea5936b3203b | -3.20759 | -50.21655 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7564dd0b-3355-38b5-ac14-8838f845f9b8 | -3.00967 | -51.03616 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f028a59-d4e8-31c5-88fa-95b8afeee4a4 | -3.37077 | -49.258 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60d46bb2-5ad4-3ba2-987a-e8e7faa73519 | -4.28402 | -47.30545 | 2025-11-26 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a31285d-c23c-3629-938c-1f1c11925f7d | -3.4063 | -50.56795 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e325920-ffc6-38fd-b1e1-c3923bac7315 | -4.60164 | -44.41609 | 2025-11-26 05:10:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a6b991-3b9f-3b8a-9dbf-dde54875159b | -1.35361 | -55.42426 | 2025-11-26 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2d93690-ce01-3ff4-9cd8-deb74b962946 | -4.71717 | -47.15419 | 2025-11-26 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9282bc9-38a2-35f8-9a41-da0960149cba | -4.10484 | -49.06497 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e6d6886-2485-3640-bc6a-ca5fd82410b0 | -3.52307 | -53.06296 | 2025-11-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0030bb57-f2d1-30e0-92c6-90bee75328ab | -4.65904 | -43.97691 | 2025-11-26 05:10:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 201dd627-0245-36f7-b5f5-b0f88b5148fa | -3.32922 | -49.71909 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a024a1d-e5e1-38da-a3dc-99bac965fd34 | -6.76439 | -46.5116 | 2025-11-26 05:10:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a478611-7a83-31ad-bdfa-e81a2a8ea337 | -4.9269 | -49.01886 | 2025-11-26 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c1fe534-b703-30ef-af00-a24b085e7374 | -2.92598 | -48.22477 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3da4c15e-56d6-3b0c-bd95-63053aafac26 | -4.82954 | -43.81979 | 2025-11-26 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e1475d2-2329-32d1-a3df-52789f3dafa2 | -3.47523 | -50.79664 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36dc742b-9ad3-3935-bafa-ba4b1964f488 | -4.20704 | -48.5718 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c835cf-bbed-30ef-800b-c1f49be9ad87 | -4.24781 | -48.57048 | 2025-11-26 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c63fae0e-7437-361f-9658-465466b5c98b | -2.87903 | -51.80313 | 2025-11-26 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51408b40-5ace-3d8f-8b7d-1b2f3e101bb2 | -3.17491 | -48.02872 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b46a38ae-cdfc-3d94-9aee-e36b1cffc8d3 | -4.09214 | -50.2042 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README28.md)
