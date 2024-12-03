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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61bbce00-ad06-3450-9dae-0b1444c76a11 | -4.48022 | -47.73635 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8853b66-8505-3cee-9ce0-96312b5bbf05 | -3.89663 | -46.67385 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18abdd17-eade-305c-8b9d-bbe86c7988f0 | -3.83007 | -46.59932 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3317531c-cd89-33d4-92ec-d9f086b75bbd | -4.18862 | -51.19034 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9d344fb6-829a-3d77-8adb-1a6d94e8d43f | -3.29859 | -53.67592 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24cf5cc8-8b18-3b25-b52a-cfa67b8ad602 | -2.89904 | -51.58372 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a026ad7-57e8-37f7-a78f-b7139fb1e7fd | -4.45971 | -45.09209 | 2024-12-03 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c429108-7ad4-3129-bc84-47da8713055d | -4.74322 | -45.70874 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4eab8d58-b724-3cb4-ae6b-db230e126535 | -1.94692 | -51.20757 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f8401a1-31ec-32ba-a3d8-045cf446e9b0 | -3.70008 | -51.82448 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e54c8db8-903f-3ce9-b209-82feff33d81c | -3.14081 | -45.9897 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09c3a58e-cf62-39c5-b1eb-4260498530f1 | -2.32875 | -45.86385 | 2024-12-03 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c6bf8d-81f5-3da8-aad2-669fe7c70a6e | -2.8562 | -45.83362 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 57fbb645-c1a8-3949-a7bd-e7f104562ab8 | -2.8162 | -53.04591 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03c3b017-5426-31c6-94bf-ddb55effbcd0 | -4.21143 | -44.3734 | 2024-12-03 04:29:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e5752e28-0372-3b64-b310-9770c32d3fb4 | -2.56499 | -46.34924 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95943d81-c8ac-38ac-a7d7-cb1e025185e0 | -7.80092 | -38.73265 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e5598bf-e3ab-37ec-b05b-efc7981329a3 | -3.26771 | -50.21243 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce644cf-7f2c-38f7-8a14-cdb12f4b85b7 | -7.83802 | -47.02892 | 2024-12-03 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af59feb4-c131-3560-adc2-1b886559a6bf | -4.30253 | -48.21407 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 715c25aa-6b4f-3d8e-a037-c3e5731e9d6c | -4.29586 | -48.21302 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2d0a11-3e4c-3a9e-9a49-5a6f29ebd49f | -3.02228 | -48.01654 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15d29faa-4a07-3b17-9d64-bec238f43e53 | -2.58438 | -46.57114 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efce8e55-64ec-32bb-9863-ecf405242de9 | -3.25424 | -50.57452 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40a813c6-d7a3-32d8-9d70-10bef7777c75 | -3.05587 | -54.506 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95f1b5aa-8fab-3626-9633-3ca8dda18ac7 | -3.03518 | -44.95398 | 2024-12-03 04:29:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86643abf-9cd7-3553-9b2b-7e87974a5c1b | -3.8118 | -46.58582 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 553843ff-5937-30f9-8cff-5e510a1d730f | -5.12984 | -44.56163 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeb45f76-c604-3d0a-8ce6-a250244c2253 | -3.31221 | -49.93405 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e51d81c1-7c68-33b3-9c36-695cc36bb24e | -4.32585 | -48.21775 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7df84ce3-0204-3b51-980c-384910373393 | -3.78512 | -46.51835 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a53af6f-0541-30ee-a91b-000ff6eff083 | -2.5633 | -46.33838 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b41a948-9c6f-30e2-9342-9b7b101b9658 | -3.36442 | -54.06972 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abfcbb77-d1ce-3c22-abb6-0f2384dc6782 | -5.57147 | -44.88975 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 815bc90a-7a89-3458-a5f7-abe14eb094a5 | -3.82952 | -46.60278 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9dd3a0f-df46-3ca8-9ed8-c08793b6df6a | -2.80484 | -53.06107 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 450dd823-e726-33c3-8e3c-85a806bd44fe | -3.25734 | -53.66169 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 43cb5ab8-7e53-303c-a171-d8ff914f8387 | -4.03727 | -46.83724 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ab1b72-4e6c-3fca-acc9-9b32e522e627 | -3.9233 | -52.38516 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54a99db9-9e77-3b61-acd6-651b3a66ae6b | -3.17811 | -46.5547 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a913ac57-18db-3ea1-aaf9-ea14e1a70140 | -2.97363 | -53.87426 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d53ef46-0330-35b2-88c9-afd76ace53e6 | -2.60067 | -46.57759 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 979d893c-5558-3601-9c07-b9dd17ed52db | -3.01875 | -54.03226 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d23e5bcd-3391-36c5-bf93-226532192429 | -4.01693 | -49.9659 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2eafaf-acb3-3756-beb6-fba4352a97d6 | -3.85195 | -46.52467 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d7c10d9-23bb-3d8c-a739-1857514582ab | -4.04631 | -46.99781 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae9381ea-0d87-3789-8412-b8d94f3f2d4b | -1.73739 | -52.6416 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61bed7c8-aaf7-3db6-a054-ef0b7fdf04d2 | -6.81451 | -46.77298 | 2024-12-03 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 821f4111-50b1-3046-a86f-1f70fe3a65ec | -4.15842 | -48.58615 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3977a1b5-6354-324b-9186-d475ca7be150 | -5.48406 | -46.37934 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43d10625-40b8-3ccf-bd9b-ec7d619c1395 | -2.56404 | -46.39856 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7fede49-11c6-36ab-8b78-cf407dbb8a61 | -2.54681 | -47.37219 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c249b6d-b570-38a4-9c34-f79c6a5c6d99 | -3.87696 | -46.5818 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3632bdea-76d0-3419-8b9d-5ae22aa8defc | -2.62168 | -46.961 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a95478b-e29b-3d8c-8d72-ef49e8c81de0 | -3.36752 | -45.45177 | 2024-12-03 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933ece48-7857-3ba8-ae91-e4558ec695a4 | -2.05234 | -51.20066 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed814a1a-6713-3545-874f-29dafed5f611 | -4.39993 | -49.77026 | 2024-12-03 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fae47be-33cd-3256-b078-8717784ada0d | -4.56229 | -45.47477 | 2024-12-03 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 73db03cd-40ce-3e07-a04e-4956a793d89d | -2.46899 | -46.54961 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2165b9d8-0c4c-3f5e-90ff-45f5f9602541 | -2.5561 | -53.40177 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a90aaeda-a6ce-3201-936a-4621f273078e | -4.3993 | -49.77415 | 2024-12-03 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c58c768-52e2-36f2-91c1-91386f1204fb | -3.76558 | -46.66425 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ff9e4da-f0e3-333e-9669-941847ce2e26 | -2.66756 | -46.10633 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66d56fd9-eca7-3686-930e-0304a650bc7c | -3.70301 | -51.82739 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3f1bc2be-0afb-3834-837d-a8e62109710c | -4.18257 | -51.18005 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca8afeef-80c3-38ae-8cda-79605a2d1b90 | -3.36968 | -46.67614 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2aa6c593-c112-3ce2-9145-0910577eac55 | -3.19687 | -46.36985 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffffd81d-d28c-300e-9e33-a63c9c0a3756 | -2.55012 | -47.37271 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c633b97a-53ad-3cdd-97fd-e8a9003904d3 | -5.27727 | -47.78777 | 2024-12-03 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85bef9fd-ff75-369b-9ade-15aee415c09f | -4.08148 | -47.3558 | 2024-12-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a779023d-e7c5-3c69-8cc3-3cea321dd1d8 | -2.54368 | -46.2468 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc6c0834-1948-3fdd-a500-f8cd9cc46952 | -4.07438 | -46.81866 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7b52080-a476-38d1-ba4c-721517fb115f | -1.7493 | -52.78572 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73aca590-c2de-3c29-b520-6c54fde58ac0 | -3.33669 | -51.20906 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abcfda1f-0027-360d-b6b3-6ff19d1f1011 | -3.45179 | -50.30342 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 934ccaf9-f4a0-3986-81f9-f8cf186db9be | -3.85032 | -46.53507 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 014302db-67de-3cbe-9ab0-3ebfdaf851fc | -4.10678 | -46.95791 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e59a5900-c474-33f1-a592-cc94ce11be68 | -3.67944 | -44.70354 | 2024-12-03 04:29:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf9e6a93-5bbf-32a5-a2ca-b1d11d5a766e | -4.78716 | -45.42514 | 2024-12-03 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78a4fe8b-7d12-3596-a821-fca2f50b2e9f | -3.93319 | -46.722 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3310ac90-d9db-36a8-aed9-4fcbd3e747af | -4.18108 | -51.18919 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fca8675e-ffc2-399b-af5b-5735eb4c7b75 | -1.70212 | -52.62582 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c125a94-66fe-3053-be1d-758a7b1d17ba | -2.60989 | -46.88528 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f621dc5e-3942-3a6b-9ef1-070b200905ff | -2.45678 | -46.51951 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b88d86f5-ab87-3051-9ebb-a6860778127d | -5.53492 | -46.44884 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4691d153-9c52-3688-a573-10485491edc3 | -4.2953 | -48.21652 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778ab5dd-65b8-3d17-8716-aea9b3501bc7 | -2.69321 | -52.91907 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f5552a6-e036-344f-a5b3-9ae2c28d62ea | -3.20929 | -53.12721 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b720887-c67b-3351-b6a9-5cf6c115b3f7 | -4.91564 | -47.86161 | 2024-12-03 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d26875eb-2d70-3d08-97e4-afcc3751f6d7 | -3.25952 | -53.64826 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 985f4287-1c38-3dc2-9b1b-fcdb163bb100 | -3.768 | -46.6924 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6c41147-536d-3cbe-9b5d-054c0b9c6d6c | -3.33417 | -46.4264 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d797caba-b387-3ac1-b679-5e347e56ce51 | -1.9536 | -53.34396 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8609b79e-5651-329e-ac4c-c0b626642ce3 | -5.1221 | -50.61042 | 2024-12-03 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45a0ba68-5090-3bbd-b0e2-c8900cedd49d | -6.11755 | -43.9671 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bc8298ce-fe2e-36ec-90af-3cf9f6a9f72f | -3.88206 | -52.33073 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4cce45-c1dc-3a2a-9a05-9378a2426834 | -5.80795 | -46.4801 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 688e0846-2cac-347c-8efe-94b3bf80bbd7 | -4.30586 | -48.21459 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc9ad719-77ae-33c6-8149-27b8fd9664e6 | -3.28318 | -53.2824 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c9d4ce1-c81c-31b8-b983-6e544a5c2f94 | -6.98208 | -43.5079 | 2024-12-03 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README50.md)
