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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2d9acc2-6920-30df-b5fb-1c751e479c0b | -9.95767 | -44.94149 | 2025-11-14 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aba4b51d-1564-3df4-971a-9ad6282c7f5c | -12.71912 | -45.42636 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf5aae24-970f-3341-aa1b-4c48307f374f | -11.93537 | -43.94413 | 2025-11-14 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e60739ce-1175-3e4c-8a0c-5167012a5f20 | -3.16988 | -42.97308 | 2025-11-14 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e77d80-b577-3697-a590-519cc62d3726 | -9.67152 | -43.89444 | 2025-11-14 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 04ef0830-6783-3458-8f20-8163d90ffc5f | -12.02387 | -43.7308 | 2025-11-14 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1625da71-0df4-3e52-b9f1-907e6724efa2 | -4.59177 | -44.40104 | 2025-11-14 03:55:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a7ddc2c-d8b8-3b76-a59e-51e849951655 | -2.24148 | -46.07935 | 2025-11-14 03:55:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24db7bcf-4dc8-3583-b725-19fc1caedd60 | -2.11508 | -45.35983 | 2025-11-14 03:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e29a586c-c1dd-3707-b9b4-2e4a864ececf | -3.98941 | -47.18967 | 2025-11-14 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2ae1256-d99b-3100-a37c-0c8ac75757cc | -9.00757 | -44.17379 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93b56458-fbba-3362-ad76-d76c68b3302c | -2.16993 | -48.37191 | 2025-11-14 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7312c7e4-be2e-3edc-8ea2-2d40c6f7c17e | -11.84895 | -49.22456 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a8abf08-ca18-36d5-b3b9-f0e15f8abbf4 | -5.08774 | -40.24011 | 2025-11-14 03:55:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c90d6f4-6050-3ce6-9aa5-4e771749e6a5 | -3.47686 | -45.65046 | 2025-11-14 03:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| abfdf785-a6d8-33fe-abbf-29899aeec439 | -16.29548 | -39.85128 | 2025-11-14 03:55:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d91a3e0-4fd6-3b63-aef0-d5f8e5b9dbe8 | -2.88301 | -45.28639 | 2025-11-14 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3d862858-5ca3-3a5d-a1c3-c83eec062389 | -4.5708 | -41.53812 | 2025-11-14 03:55:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c279405-ae03-381c-b1e4-9506cb57ad7e | -4.04627 | -46.12687 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34103a6a-b496-34b2-9097-880b8a781330 | -11.85512 | -49.22193 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| a5b9a1af-a9ba-3e7c-9e61-9abc1bef04b8 | -2.84073 | -45.4838 | 2025-11-14 03:55:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 5f5b0103-a587-3b0e-9efc-64c1f10c2915 | -3.8177 | -44.25433 | 2025-11-14 03:55:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2de557c8-efbf-30dc-a316-d2f4da8894db | -3.77315 | -47.72946 | 2025-11-14 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 740b0efd-c839-32f9-a245-731775c0a3be | -3.99491 | -47.19029 | 2025-11-14 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03cbc88c-161c-394e-850e-b5d4feb78367 | -13.91963 | -42.88567 | 2025-11-14 03:55:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1e65e87e-9a35-3d95-8b34-9cf7795ac610 | -5.60221 | -37.80919 | 2025-11-14 03:55:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64ff06ee-3212-3ae9-8ae6-9e0e3c1aca78 | -4.40705 | -42.32845 | 2025-11-14 03:55:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0beb422e-ea15-386c-8160-86edf25023f8 | -7.78905 | -49.61505 | 2025-11-14 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9aa0466-0920-3758-b8df-e5c572f32472 | -12.60055 | -48.37115 | 2025-11-14 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b853dcba-a00f-3515-89ea-ca2d3291994d | -4.25646 | -44.59846 | 2025-11-14 03:55:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e16a874-dd08-3be6-b760-39cdf6341a53 | -3.36226 | -48.40231 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2611a531-8e07-35db-b841-b24eb10fd3a0 | -3.48182 | -45.65124 | 2025-11-14 03:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d63fda3f-70f6-3d58-9625-852dcd470008 | -9.11705 | -43.95274 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67da1a21-380d-3b8f-81b1-529f92e33163 | -10.4483 | -47.3383 | 2025-11-14 03:55:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60ebc143-c73e-3628-b353-db3696e7ee00 | -11.85373 | -49.22364 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8a22754a-1f99-3c3e-b67e-69f81de9d49d | -14.66752 | -46.56913 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 53e9a500-ac1b-3703-a68f-df85074478ec | -11.66628 | -48.46289 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1028274d-e8aa-318f-8435-1a0f07a6384d | -8.53524 | -49.5855 | 2025-11-14 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 299d0401-399e-335c-aec6-04c0a971e0b4 | -3.35449 | -48.39489 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f2fcc1e-db62-33a2-9615-8671c2ed834c | -15.26123 | -43.59266 | 2025-11-14 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58b7845c-13e2-3fed-b656-ba0d1b62d833 | -10.74487 | -48.17492 | 2025-11-14 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed8f91a4-e100-37f9-b96c-ebbc58b06b45 | -15.33364 | -47.35809 | 2025-11-14 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff79e8e2-1ac0-3f9a-af96-95e4db38195d | -11.73112 | -48.51917 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f24c2f5a-018e-38f3-b56b-d8bf109b84aa | -12.14494 | -48.02163 | 2025-11-14 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08d7ccd7-4915-340f-aa6a-d75ad9ef2bc8 | -9.11768 | -43.94912 | 2025-11-14 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09be7806-9d6f-32e9-9a7b-f25ef2ae47f6 | -10.73224 | -44.01717 | 2025-11-14 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dc0b6f97-cf07-31d9-97a2-80e9240f76b4 | -4.69727 | -44.37238 | 2025-11-14 03:55:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb9e4d27-d374-34cd-a699-d83659267714 | -10.20558 | -36.58584 | 2025-11-14 03:55:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e23f6e1-6405-346d-a5ba-50325839c7de | -16.47437 | -42.17642 | 2025-11-14 03:55:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8022c5c9-063d-3134-9966-c18702a072b0 | -13.0011 | -43.84136 | 2025-11-14 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 444786e7-255b-330b-abca-14a4d7a2dd70 | -4.30396 | -46.27251 | 2025-11-14 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e55f54c-e455-3ef3-8178-01e11909134e | -3.38327 | -41.15316 | 2025-11-14 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2e66507-cd52-37e5-94ba-fa1252aa9d51 | -14.35189 | -47.89652 | 2025-11-14 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 142ab10a-6831-3a91-9b03-24e13169d038 | -12.69407 | -45.42176 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb76dfb1-951f-3077-9f4b-a6fd87ac73c6 | -16.28879 | -43.82942 | 2025-11-14 03:55:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97dc9a55-bfd7-32e2-96c7-2b6d6d5d2bdc | -2.45367 | -48.82428 | 2025-11-14 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebffd34b-a420-3a8b-8ecc-e1beba7f1711 | -10.08714 | -36.4525 | 2025-11-14 03:55:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 97e475a0-c8dd-3f25-9b5b-f65484230fd4 | -9.85551 | -47.61253 | 2025-11-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a1d875-6bd9-340e-9633-641d35f552ff | -5.16245 | -37.57713 | 2025-11-14 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1e966e2c-7028-39b8-900c-1d4ba36244de | -4.74959 | -41.07983 | 2025-11-14 03:55:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7b43a2a7-1497-3033-8390-392d80fac719 | -10.10742 | -40.89814 | 2025-11-14 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 05df4a9c-960b-344d-97a7-8f876793bbee | -13.77724 | -43.74271 | 2025-11-14 03:55:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d517ae52-435a-3eb9-bc07-73027b9b73fc | -9.98596 | -45.14785 | 2025-11-14 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0210cc83-d939-3e6a-afae-db5805abdeb3 | -4.46036 | -43.91916 | 2025-11-14 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9d76887-ec49-36f0-8690-cf8ec1fc8b3a | -15.31992 | -43.04995 | 2025-11-14 03:55:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 277ff625-9576-3bed-bbf3-9ee31be7dbf7 | -11.7305 | -48.52244 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11786c97-981b-32d6-9c13-4436bb2c064a | -14.70463 | -46.61228 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1e37aadc-dda1-3320-96ab-703ac4b8f96a | -5.47853 | -37.53487 | 2025-11-14 03:55:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a2b1bba-c8e7-3ffc-8b49-261ad7d3c260 | -4.60674 | -43.29855 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 697bb97b-229f-3048-bf0a-c7d591fa3a0b | -3.27767 | -41.44137 | 2025-11-14 03:55:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b74affb6-3721-337b-9758-6c7527e908cf | -2.4719 | -48.22846 | 2025-11-14 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d63d0f25-41b6-3bf6-b0ef-93cc66300980 | -3.36489 | -48.40565 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f042f7be-8ec4-35d8-8b52-53d74caaad62 | -10.70217 | -44.49126 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3c146d0-40e8-36d9-9c84-12981db1ed2e | -4.0407 | -46.12899 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df802e6a-35c9-37ef-a0d2-9b4003becf26 | -3.80355 | -45.03552 | 2025-11-14 03:55:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8e6dda6-941d-3546-8b0f-fa152afe22e6 | -13.7716 | -43.62077 | 2025-11-14 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77922973-644a-308e-8888-50fd0536f238 | -4.28941 | -41.81414 | 2025-11-14 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a4dfbdbb-b259-38a6-93ac-8edd1a00266b | -4.63525 | -43.28008 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30921138-8490-3bda-bf46-0e01c25d9451 | -13.33447 | -43.18789 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 90a6261c-ccb1-391a-ae9c-fc7ec30081e6 | -13.84716 | -46.90348 | 2025-11-14 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a980b4e1-e015-3531-9181-9577e8a4d188 | -11.9345 | -43.94905 | 2025-11-14 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c0ea837-1684-3955-8e68-ccace949074f | -4.13164 | -43.01292 | 2025-11-14 03:55:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92f3ae14-ca70-3fc9-9197-aa172f481b3a | -9.52036 | -40.59498 | 2025-11-14 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fc5892b1-41a5-3ea4-83fe-d4ed10dbf0eb | -4.83668 | -40.81086 | 2025-11-14 03:55:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50772d1f-d91e-3048-b745-2e252f524bfd | -9.14656 | -45.17525 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e228a1d-633a-3525-b52b-e17461e66665 | -11.82131 | -47.78996 | 2025-11-14 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c6aa858a-3848-3b0e-945d-48e873f652f1 | -11.69303 | -44.73936 | 2025-11-14 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31afd15a-44fd-3be2-8c94-e445de857e1f | -10.32083 | -44.27515 | 2025-11-14 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bdc224e-ce7e-3625-b555-9b7c35855b49 | -10.10422 | -46.58479 | 2025-11-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9b4ccd8-2847-3e33-8c70-650ddc1286d1 | -3.47778 | -45.64487 | 2025-11-14 03:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 41802854-4faf-38cd-8043-c87bea41f30f | -4.83612 | -40.8097 | 2025-11-14 03:55:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9c673ae5-20ac-3d41-acf8-03104e184555 | -10.11111 | -47.51191 | 2025-11-14 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54807421-4132-312b-847c-b05137dabf2a | -2.96081 | -48.58426 | 2025-11-14 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bddb477-cbb3-3bfc-a6d2-6c2eee335f15 | -12.69266 | -45.4296 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a42630b9-b2fb-3db6-b542-93c24cbfa1a0 | -2.9421 | -49.36569 | 2025-11-14 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcf73532-99a6-3de3-9447-747e60d9a711 | -16.0344 | -44.9715 | 2025-11-14 03:55:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b28dd68a-a34e-3d2f-a168-9f92f72eb5ff | -3.7718 | -46.00939 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ca80c4-29ab-337a-ab8a-2ff23d2e1314 | -3.16929 | -42.9768 | 2025-11-14 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1bab066-bac5-3f0f-a4b8-d2fca617f502 | -3.39123 | -41.15071 | 2025-11-14 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43bbb686-dd05-3797-975b-d65558a694d6 | -15.161 | -43.6073 | 2025-11-14 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
