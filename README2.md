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
| f8c3cad6-f3bd-3c12-98d1-dbaaff4993b8 | 2.5252 | -60.717 | 2026-02-19 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 5d559bbb-2db9-326a-afaf-f752286fcb9e | 0.9389 | -60.2578 | 2026-02-19 02:40:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 488703ad-e030-392f-8512-fdd589ac44be | 2.6905 | -60.2401 | 2026-02-19 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 01f24677-26e1-3ab1-b3b2-7f553af6b0c1 | 2.6905 | -60.2401 | 2026-02-19 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 1ed39db1-bed0-3275-9458-d816c370ebf0 | 2.5252 | -60.717 | 2026-02-19 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 790cec50-5f2e-3317-9e09-fb71d3d597a9 | 2.5435 | -60.7167 | 2026-02-19 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0e24e627-03a5-317c-b90a-a8a551d9cda7 | 2.6905 | -60.2401 | 2026-02-19 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 094dce73-4fe4-37e8-9535-92db2f90067c | 2.5252 | -60.717 | 2026-02-19 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 026ea81d-2406-3f0d-aedc-cea340507c38 | 2.5435 | -60.7167 | 2026-02-19 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a077d828-b2d7-3553-adb8-8a91ee00a54c | 2.5252 | -60.717 | 2026-02-19 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 79093966-b11d-31e6-ab9a-c7b9b87852e8 | 2.5252 | -60.7359 | 2026-02-19 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e9957c42-cb22-3213-b736-d6c54aa71c9a | 2.6905 | -60.2401 | 2026-02-19 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| f4d9ba72-407a-371f-b871-258e729a8d17 | 2.5434 | -60.7357 | 2026-02-19 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9a678333-13eb-3dc8-8fc0-8b3faadefd67 | 2.5435 | -60.7167 | 2026-02-19 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| dfb0ab42-1d6f-31cf-b98c-9a81274a71dc | 2.6907 | -60.164 | 2026-02-19 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 86c552d0-9b68-31f1-8b33-f95194318193 | 2.5434 | -60.7357 | 2026-02-19 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c760ebb2-5db2-39ad-9d4b-0c93c86182ac | 2.6905 | -60.2401 | 2026-02-19 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f7110d37-bc5b-316f-9fa3-ee43fb577fb8 | 2.5435 | -60.7167 | 2026-02-19 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7b128afa-0fb8-3435-9467-4fc312bc7d45 | 2.5252 | -60.717 | 2026-02-19 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 224187bf-7b5a-3c3d-98b9-5b69b630d571 | 2.7088 | -60.2398 | 2026-02-19 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f9ba2e16-cc7d-3c60-9dbe-2fac0700c9bc | 2.6905 | -60.2401 | 2026-02-19 03:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 630223b9-b888-3a1b-ba9f-f37160d3d863 | -5.59588 | -35.39474 | 2026-02-19 03:36:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0000e368-8c79-3e2a-acb3-2d114b07c978 | -12.24503 | -44.23614 | 2026-02-19 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1dec7c4-20a4-3232-9847-8d511f60c120 | -12.07734 | -43.52552 | 2026-02-19 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a54da2be-8290-3792-91b6-6e1c8128b033 | -8.54034 | -35.85985 | 2026-02-19 03:38:00 | NOAA-21 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32763671-739f-3f49-9dbd-b2c1dd07c0ef | -12.98675 | -41.18789 | 2026-02-19 03:38:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c9a1fd7b-832a-33ab-bf0a-b02c88dd4f94 | -11.88497 | -45.28956 | 2026-02-19 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4f83f83-c55f-3309-a8de-af757c5899cf | -12.16444 | -46.67502 | 2026-02-19 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f46c64d-fff4-3483-81ef-cfeba2f60deb | -12.24567 | -44.23289 | 2026-02-19 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74023c64-64d9-35c4-b235-c916745aaa13 | -12.08171 | -43.52988 | 2026-02-19 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa707ed3-3a8b-3430-a99d-d2be856cc196 | -11.89141 | -45.28658 | 2026-02-19 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab943e8e-89fb-32dc-888b-3e228d888b9b | -12.07674 | -43.52871 | 2026-02-19 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4873479-b6fc-3518-9a0d-3be1da6641e4 | -12.20341 | -39.32687 | 2026-02-19 03:38:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7287d4b2-8ccd-373b-a656-e58b289267b9 | -7.01193 | -35.00604 | 2026-02-19 03:38:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6f980b9-0973-3f2f-a5eb-c2e7db949c78 | -12.15862 | -46.67331 | 2026-02-19 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e98d7b11-9ac1-3fe4-a897-49af3f8650fc | -12.16472 | -46.67464 | 2026-02-19 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1c35a54-d297-3033-a464-0952c190c45c | 2.6907 | -60.164 | 2026-02-19 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 28a82963-2a4f-359e-b3b8-29fcf9fe6466 | 2.6905 | -60.2401 | 2026-02-19 03:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4dec1de3-edb1-3698-a2b5-834ddd8a12df | -20.04577 | -41.34765 | 2026-02-19 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a678bdc7-02db-3139-821b-245d18871f7b | -12.80879 | -44.82497 | 2026-02-19 03:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d76ea106-35da-3835-9dab-e5ab3623c7d4 | -15.85256 | -43.50535 | 2026-02-19 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c87e955c-67de-3dc4-a69e-70a4e2d3f853 | -13.26648 | -43.93501 | 2026-02-19 03:40:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 333d5a9c-1961-30d0-a2fc-ef646aa56dcc | -15.8596 | -43.50851 | 2026-02-19 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00d39ca6-d520-359e-ba05-71e1f16058e9 | -18.35152 | -39.79707 | 2026-02-19 03:40:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c2b826ca-c8dc-3cfc-bce3-4fbc5b4fd5d9 | -15.96469 | -38.93377 | 2026-02-19 03:40:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 385f7306-60f9-3d73-8163-86080f8be242 | -13.82784 | -42.42348 | 2026-02-19 03:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6db018b5-8ed0-30c2-918e-30547431cb49 | -15.91011 | -41.7309 | 2026-02-19 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42e4df21-6002-3358-b577-25985e19cdd9 | -15.85622 | -43.51147 | 2026-02-19 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25b29943-eda1-3cbc-a607-513002669281 | -13.38064 | -41.32352 | 2026-02-19 03:40:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2edc17d-a508-3b69-a8ca-aed62b120f0f | -16.45797 | -39.15215 | 2026-02-19 03:40:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4590671f-3d52-3b66-bb5d-9c3e76b1ef75 | -14.23311 | -45.42025 | 2026-02-19 03:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e207a90-e7cf-3772-9150-f8c4935666aa | -15.85492 | -43.50755 | 2026-02-19 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3dc495d2-00e5-347d-85c4-502133a27d4d | -15.67406 | -39.80013 | 2026-02-19 03:40:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5b795ce3-f50b-3557-aed8-fbc28fe0e76d | -13.41108 | -43.75029 | 2026-02-19 03:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc0882b-de08-3e57-b257-def8ec65b8d4 | -12.80341 | -44.82392 | 2026-02-19 03:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a0788b6-b454-33c7-ae43-91459865064a | -14.22768 | -45.41903 | 2026-02-19 03:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f83d6a1c-69ad-3b0d-9ab8-662e158ff4df | -13.82331 | -42.42269 | 2026-02-19 03:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2825acb2-47be-33ec-82c1-e61616af56c3 | -15.85723 | -43.50631 | 2026-02-19 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c7fecee-892b-3b2a-9c55-421f0752b090 | -15.95758 | -38.93248 | 2026-02-19 03:40:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5bf40684-d679-315b-a302-fafb260ac420 | -13.26727 | -43.93702 | 2026-02-19 03:40:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 709683f6-fc26-32d9-861f-1d1e63cc92e8 | -12.8081 | -44.82851 | 2026-02-19 03:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c36b976d-a6e7-3474-bc5e-ca95b60d014f | -14.23383 | -45.41665 | 2026-02-19 03:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66e05fe3-5b07-3ae6-a6aa-e5d80660fec3 | -13.26589 | -43.93802 | 2026-02-19 03:40:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0334482c-8b40-3eac-ab50-d8a18ee78837 | -15.91426 | -41.73175 | 2026-02-19 03:40:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 643cd1a2-5e10-3aae-9899-de8f9c640db5 | -18.53011 | -39.77044 | 2026-02-19 03:40:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e2efcc7-5a0d-388c-8d31-dcc3c6cfdea4 | -20.02985 | -47.18719 | 2026-02-19 03:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad792770-26af-34f3-aa78-abc2979b7fd3 | 2.7088 | -60.2398 | 2026-02-19 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8dbfb793-62af-3d8c-8280-8e5dc78b83fc | 2.6905 | -60.2401 | 2026-02-19 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9c34e88e-9fd0-353c-9b0c-9e94c53a7cf1 | 2.6905 | -60.2401 | 2026-02-19 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d67f3e15-a681-3cb0-9dc2-5f514c010d87 | 2.7088 | -60.2398 | 2026-02-19 04:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0264b8d0-ef95-36cc-a2bc-d750296f5eea | -5.05216 | -37.4136 | 2026-02-19 04:06:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5806e3cc-0d43-3e07-b77a-789116c61a16 | -5.32535 | -35.93047 | 2026-02-19 04:06:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 313a6ced-fdc6-3b82-b64e-58c7a4be1767 | -12.81104 | -44.82553 | 2026-02-19 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bcc82da-03fa-341d-b650-7dba43a3bdfd | -11.88421 | -45.28626 | 2026-02-19 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11eb2982-6df3-3b85-b934-a18b9aeeaa7b | -12.80956 | -44.83418 | 2026-02-19 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c10dbd7-77a0-361e-9415-f06155fc864c | -11.88341 | -45.29097 | 2026-02-19 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 569fefb2-5df1-3001-a34f-1988c556dafc | -12.49572 | -43.65034 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f7cb470-8a1a-303f-b311-8d157b54b439 | -8.54029 | -35.85864 | 2026-02-19 04:08:00 | NPP-375D | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4b41136-b1c4-3b8b-aa6a-96740410ea3f | -12.48877 | -43.64914 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e56f1c0-552d-3173-9414-9e26c7d52404 | -12.16001 | -46.67025 | 2026-02-19 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cde8ce30-caed-39da-bf63-07eedde2546f | -13.37949 | -41.32121 | 2026-02-19 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 66b46e7c-e744-33ff-96b8-491a1ab221f4 | -12.24264 | -44.23426 | 2026-02-19 04:08:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cec03523-d202-38ae-a39c-fc865afd4118 | -8.53919 | -35.86008 | 2026-02-19 04:08:00 | NPP-375D | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| abbe10f3-d370-3e07-935e-1ecb7b7dce89 | -12.15935 | -46.67396 | 2026-02-19 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05a4ac2d-37a7-3e7b-ba17-d7bd59bef989 | -12.16344 | -46.67474 | 2026-02-19 04:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e53059c1-5dc9-30d4-948a-9abf266f2a67 | -12.98792 | -41.18828 | 2026-02-19 04:08:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 06f41294-8282-35b7-999e-10bdb7148e80 | -11.89179 | -45.28756 | 2026-02-19 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3893e9d0-4093-344b-a86c-069f02b5cf93 | -12.19908 | -47.97395 | 2026-02-19 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37fdd925-cb09-3843-8ae6-70f645a1df20 | -12.03459 | -49.87481 | 2026-02-19 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70f3f7d8-fe17-3814-bdc7-50fa0283434f | -12.80011 | -44.82359 | 2026-02-19 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb068292-2c60-3221-8582-70614f950f50 | -12.48466 | -43.65242 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fab66061-e00f-3708-b1da-2ab8387021d6 | -12.4916 | -43.65363 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e503bcc-0fe5-3917-a697-b21e1513b68d | -9.17111 | -40.93579 | 2026-02-19 04:08:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4c5f9e1-2a7b-3ae7-b7a5-ea9d8513e906 | -12.03966 | -49.87583 | 2026-02-19 04:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52a182af-a182-3a61-8fb9-2906b5eda041 | -12.8103 | -44.82985 | 2026-02-19 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ccddba5-1b49-3edd-9b29-6a3a34da9540 | -12.4853 | -43.64854 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e8d7dd1-5c64-39eb-92e7-82eaac4f1a25 | -12.79937 | -44.82791 | 2026-02-19 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b66d88c-2253-30cd-9a60-87194f5e410d | -12.24334 | -44.23016 | 2026-02-19 04:08:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba97cccb-af5e-389b-b5d8-fef3e5c18bad | -12.49508 | -43.65423 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45eee891-172f-3465-94c9-a590c2b651c2 | -12.48595 | -43.64466 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
