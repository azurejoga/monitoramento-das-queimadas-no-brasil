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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2917728-581f-3037-8d49-3ae0dad28b8a | -5.41498 | -47.56949 | 2024-12-08 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0377766e-c022-3274-b1e2-117bfe19be83 | -2.23436 | -45.57812 | 2024-12-08 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdc2079a-d0c1-3955-a634-8a82755813d1 | -4.07325 | -46.71127 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4413c181-b5c1-398a-9663-8b34f833fb1a | -5.91068 | -48.02944 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38241431-6a44-365c-8aa2-e4ca5bc3bc63 | -6.68285 | -47.66114 | 2024-12-08 04:36:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 531be423-9eb6-34c9-ba34-a37c18f3ee66 | -4.58509 | -48.01645 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb0b595e-c6e2-3ff0-9049-aee90f8ff476 | -6.29098 | -43.85256 | 2024-12-08 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3842e219-869b-3636-a1f6-0a4b4295a574 | -6.65382 | -47.52871 | 2024-12-08 04:36:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abd0aab4-ee5a-3369-9997-6b927ead02cb | -5.52641 | -46.96057 | 2024-12-08 04:36:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c8d9936-bae5-32f1-9637-fdff74a22bdc | -4.04937 | -46.88642 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 216c8387-9fd6-3cee-8b01-62ec6836fdf1 | -5.76371 | -46.85217 | 2024-12-08 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74f28736-110e-3231-8939-a29ce22240dd | -5.25381 | -37.50588 | 2024-12-08 04:36:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ef1eade0-f4c4-36ce-918f-87fc2975b757 | -1.97223 | -48.43568 | 2024-12-08 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe9a4b1e-9f04-3c5e-8889-e1ea2453c2d2 | -6.65439 | -47.52501 | 2024-12-08 04:36:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8230da5-b759-3a55-a5a8-ad6123b23f39 | -4.584 | -48.02343 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 413b7597-e243-3c8e-acf6-ddb337976213 | -6.42432 | -52.0127 | 2024-12-08 04:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f2428e8-480f-34b5-869e-d9cfdd271f79 | -6.3082 | -47.34079 | 2024-12-08 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa8755a5-930a-3f01-a8ab-34174e0b61d8 | -5.25312 | -37.51085 | 2024-12-08 04:36:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8694852e-91be-3a35-8a5d-09333c0619b1 | -4.77857 | -48.08174 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acb770eb-e691-3273-89fa-21143f73c85e | -4.17274 | -48.61179 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cfec00b-5421-3381-8dc3-2eb806d8853e | -4.58176 | -48.01593 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b400477-88b1-3bd2-8795-361b6f9e0981 | -7.88073 | -44.20208 | 2024-12-08 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51e8b8c1-6e68-37b8-8119-c73585a424cc | -4.04515 | -46.7109 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d927bd1b-4639-3c54-b33d-f412d3cf9e76 | -1.51385 | -52.66824 | 2024-12-08 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f4d392b-9ce4-3270-8fee-d9d089a788a1 | -7.80662 | -46.22866 | 2024-12-08 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d30d08-45b2-35fe-9e4b-4a225dfb28c4 | -6.05084 | -44.04642 | 2024-12-08 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2d759f9-0528-3efc-8773-da6a2d3d5c90 | -6.83168 | -47.3034 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d94c0cef-ee91-38e8-8f2c-c63fe5a3b464 | -4.58121 | -48.01943 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ee33237-d584-3328-a11d-6a681ff0c200 | -7.9872 | -45.79474 | 2024-12-08 04:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64ca6061-9677-3b9a-ae16-7e69d615b655 | -5.42418 | -44.70852 | 2024-12-08 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24df20dd-462d-318c-bb30-c7b59a3f52fa | -7.88018 | -44.20584 | 2024-12-08 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1181c77-47ae-3a02-8b93-a9a2499654a1 | -4.03582 | -46.81617 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 210d448a-c367-34f2-807f-f2948fd938cd | -6.86841 | -47.24733 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed90ec96-2b9a-3b83-adc3-efdb3e19645c | -5.77702 | -42.60152 | 2024-12-08 04:36:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1f40326c-318f-3242-953b-618ec9a4b4c0 | -5.64095 | -46.73547 | 2024-12-08 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dcd63c7-842a-34de-a34f-fce445239b0a | -5.24962 | -37.50605 | 2024-12-08 04:36:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c4a604af-af11-370b-a39e-ea21788116e8 | -4.8923 | -48.04962 | 2024-12-08 04:36:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46b31299-54c7-31f2-9931-f738b5fbf742 | -6.20608 | -46.06252 | 2024-12-08 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df0f6305-239e-3ce5-9329-4018609e6f5e | -5.92073 | -48.03102 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc747c8e-a207-39f8-84de-b9d47a11a13f | -5.92407 | -48.03156 | 2024-12-08 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abe48f0e-4c7d-3e95-b98c-a94c3505409f | -3.92061 | -46.72253 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 172c2e8b-d88f-3aa9-9550-264431751971 | -6.87303 | -47.24023 | 2024-12-08 04:36:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c86e37d3-b1bc-37d9-8866-6a95ebd4463e | -5.64154 | -46.73162 | 2024-12-08 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6597ed58-52dd-368f-9737-a0aed7934a95 | -4.58067 | -48.02291 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ee4da9f-3f98-3ea1-a649-5972b9082588 | -4.0807 | -46.70864 | 2024-12-08 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3de769b6-1ec3-37aa-98f1-98fe44fc89c3 | -5.77033 | -46.55133 | 2024-12-08 04:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f98b2ce-4409-3842-a3e5-d033cd365017 | -5.14374 | -47.50679 | 2024-12-08 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b040b40d-427d-34c1-817c-1fa20bbfad6b | -3.85374 | -40.44755 | 2024-12-08 04:36:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a2d6c7e4-834e-33ad-8c1f-bc052ae42a8a | -5.19513 | -47.74192 | 2024-12-08 04:36:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdcf336b-f824-3627-9f26-e30b0db9c837 | -4.31835 | -49.39094 | 2024-12-08 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db68b5bb-0c30-3c87-af0a-5663d06d8ebb | -5.6496 | -47.52386 | 2024-12-08 04:36:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbd341c9-8cab-37fd-971e-eff4d0be65a5 | -4.58291 | -48.0304 | 2024-12-08 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0acd740b-bd51-3a58-90ba-944a15477668 | -12.53118 | -57.73834 | 2024-12-08 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2882132b-7aa4-390b-8bc6-b9f362662719 | -12.77974 | -54.22049 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edb0d1f9-4b7c-3d89-b179-d6f4ac33f612 | -15.18406 | -43.75365 | 2024-12-08 04:38:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e39edd0f-26cc-3615-8a61-3f33207b0606 | -11.20801 | -53.82212 | 2024-12-08 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0065867-53d0-3293-a30d-36d5e8c29075 | -12.28001 | -49.50044 | 2024-12-08 04:38:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54676306-a161-3eba-ac0e-5b3eaf486f8f | -12.85469 | -51.93151 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e47d600a-19ab-3872-a5fd-2d0e99374050 | -12.40567 | -49.67852 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59283537-e106-3ed2-8aff-971f155ceb5c | -8.05247 | -47.90763 | 2024-12-08 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c2c1283-6bc1-3247-8c0f-897196b82d9a | -12.2457 | -54.29122 | 2024-12-08 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4df39d64-93a0-38c8-8fb8-89849c307eb6 | -13.8927 | -54.62598 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e432215e-99c6-32a8-9a65-549eecdd52d0 | -9.21822 | -49.4845 | 2024-12-08 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccb022bd-5a1b-3d0f-8c8b-2d756f9d11c3 | -12.85804 | -51.93208 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3377b944-b14f-32c6-93dd-c36d26d786b3 | -12.41348 | -49.69446 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12979df0-14bc-3133-9932-17d25e398a01 | -12.78651 | -54.22395 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4a56fff-264f-3093-a537-cc6a10bed168 | -9.22418 | -50.69442 | 2024-12-08 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4bffb33-119a-30fb-b874-37273cdc46e8 | -11.82567 | -57.82376 | 2024-12-08 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3689523c-1ce0-384f-b350-e775665cbf18 | -9.11215 | -49.46746 | 2024-12-08 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93e6d2d6-27a3-38bf-b8d7-32814d1cb5bf | -12.40234 | -49.67799 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e876064d-76d0-36c2-a021-7db868f7dc6d | -12.78727 | -54.21958 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faa5cc6a-724c-3717-9f85-82d948cf3472 | -12.40623 | -49.67494 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0137d45d-164d-3760-adc1-4d873bf1857e | -13.89562 | -54.63107 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 59f0a1c6-a6dc-3b7f-b94f-ce30faf179cc | -12.59347 | -54.38904 | 2024-12-08 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56575047-0caf-3099-b473-6a50b1677424 | -11.15674 | -49.70057 | 2024-12-08 04:38:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfb2b21a-6770-3480-8b98-39c381f10e57 | -9.21545 | -49.48049 | 2024-12-08 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69f08d67-b6d6-31ba-98e0-40de5bcbc3b1 | -12.91054 | -49.68048 | 2024-12-08 04:38:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf207da4-67af-342e-bd20-d532bdd3953f | -12.12187 | -54.29037 | 2024-12-08 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7942e08e-110c-3683-bf6e-6e68e9a8d989 | -12.27051 | -49.49524 | 2024-12-08 04:38:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96d65a0c-b099-37bd-bcac-aeed7c2de8c4 | -8.05019 | -47.8997 | 2024-12-08 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0279d8e6-f470-3566-a5ff-5ebcb3644b1d | -11.75052 | -54.72818 | 2024-12-08 04:38:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42369dca-d791-3237-8187-6d83c30c34d8 | -13.90004 | -54.62735 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8892cd95-2c83-3690-8781-987947c77714 | -11.20071 | -53.8209 | 2024-12-08 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78c4d6ea-dc9f-3aed-bad6-94957f03ea81 | -10.47001 | -51.68182 | 2024-12-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 373b99ce-11fa-3cb2-8cab-daa488108924 | -13.89637 | -54.62664 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac5616b6-6a37-3860-9eff-4da57a269089 | -12.59423 | -54.38459 | 2024-12-08 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 784c6dec-9cab-3e8e-bc81-178b7125f2cc | -12.53711 | -48.32187 | 2024-12-08 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8da91448-1571-33ef-9e75-389bb333ee51 | -7.97267 | -55.05965 | 2024-12-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbd0d1b6-3345-33df-a2ee-12a50c9ed6d5 | -12.4107 | -49.69034 | 2024-12-08 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35dc25e9-c5ce-3eb5-9f9c-e27e2ec9a792 | -12.54001 | -48.32634 | 2024-12-08 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b0926c5-f0d2-3a95-9268-06aeaa30bd4f | -12.85746 | -51.93568 | 2024-12-08 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68676c7f-0fdd-3585-8383-98e4bfb0b47a | -9.21876 | -49.48101 | 2024-12-08 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 177b4f29-f54e-3fc4-9d96-25ebc4316b9a | -12.9072 | -49.67994 | 2024-12-08 04:38:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cee5a4f-77b3-3954-93c9-d6aabd5db024 | -13.15531 | -49.2234 | 2024-12-08 04:38:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5d344ec-1ebe-397d-90dc-644970147233 | -9.16078 | -49.48231 | 2024-12-08 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006a8fec-b5f9-3455-9a3f-ae248979fec5 | -11.72594 | -57.44275 | 2024-12-08 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 184dccb8-81a3-3b6f-9124-bec980f041c5 | -12.77901 | -54.22483 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b91a4109-9d4e-36ec-92dc-123e0919bcaf | -12.27611 | -49.50351 | 2024-12-08 04:38:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 245aa8d4-6e0e-3770-beba-2f0d70f37dbe | -12.84665 | -58.22351 | 2024-12-08 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0ee63da-5120-3034-8f56-0cb2adcaaf48 | -12.77921 | -54.22269 | 2024-12-08 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README10.md)
