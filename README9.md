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
| 7fc508ca-dd8d-32ac-86cf-5b37fb103fcc | -10.9397 | -43.0593 | 2026-07-05 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 2ce25479-9ac4-3282-8300-cb978c633ce4 | -10.9401 | -43.0355 | 2026-07-05 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| af08a01f-75ad-3cb2-8127-3adaf7e2db30 | -13.2407 | -54.3096 | 2026-07-05 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 971414df-1347-3fa2-8a42-c626152acdab | -13.2404 | -54.3303 | 2026-07-05 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a11edf68-e937-30bd-9712-c05a380491cd | -10.9401 | -43.0355 | 2026-07-05 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a26f3452-7647-35db-bc49-843bfcfc7750 | -13.2407 | -54.3096 | 2026-07-05 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b27dd7be-458e-3b28-b0a8-e4c9d6bddd4c | -10.9401 | -43.0355 | 2026-07-05 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b7a524fe-b7d5-369a-97ad-abe9d4c4bafd | -8.86576 | -62.21584 | 2026-07-05 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9b56b45-bdd4-3e18-bbd8-5a1401263632 | -8.8546 | -62.21409 | 2026-07-05 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bb02b4b7-9425-3e8e-b017-2e877d37a0ca | -8.86527 | -62.21964 | 2026-07-05 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e06c676c-7f94-3803-9ce4-6f156561433a | -9.37609 | -65.77503 | 2026-07-05 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9deaf4d-01bb-345c-9088-c1aee7f889dd | -9.66921 | -67.21386 | 2026-07-05 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5a21827-540a-3b0b-b047-0b7ebddb552d | -8.86067 | -62.21112 | 2026-07-05 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3648fa75-ba15-39f2-be5b-61cbeb27f374 | -8.85509 | -62.21025 | 2026-07-05 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 08685ead-6ef0-3716-8b6e-c95bca4dd56f | -9.36265 | -65.74167 | 2026-07-05 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83d758bf-8dfd-3e0b-bcb0-228d6a8e7b47 | -9.66518 | -67.21329 | 2026-07-05 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0207a23-43e9-32f2-bdb2-ed5ed536c5ed | -11.4525 | -46.5943 | 2026-07-05 06:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 70ababc4-1780-382a-8c4a-39a23396c448 | -10.9401 | -43.0355 | 2026-07-05 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1b01623b-f8bc-3ee3-8ff3-a6a281b5f0c6 | -11.4334 | -46.5969 | 2026-07-05 06:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0eb892f3-60e6-3dc2-a5bf-b5c348da1a51 | -11.08653 | -68.712 | 2026-07-05 06:10:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fe5b5c2-fc1e-3ade-a40c-bb656f994fcf | -10.9401 | -43.0355 | 2026-07-05 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 6f12477b-efad-3298-97d4-4ced60416a00 | -10.9401 | -43.0355 | 2026-07-05 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2a66b726-96be-31ae-8d13-eb35971c87e0 | -10.9401 | -43.0355 | 2026-07-05 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| be5aaa3c-f16c-3947-90ad-8fd9bdc1ab9e | -11.44275 | -46.60342 | 2026-07-05 06:44:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5736c69e-9fac-361e-8df3-415644f9dd03 | -6.93816 | -43.71312 | 2026-07-05 06:44:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 589f2d4d-5151-316d-be92-4b560a803500 | -10.92809 | -43.04928 | 2026-07-05 06:44:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 10835c85-7b68-31df-a0c6-1451cf433f12 | -10.93707 | -43.03393 | 2026-07-05 06:44:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 3d810c66-d85a-33b6-9b79-c8a8daf576ad | -10.93119 | -43.0257 | 2026-07-05 06:44:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b67a1ae9-899e-32c0-a3ba-67558d7db70d | -13.23626 | -54.32469 | 2026-07-05 06:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ae33d2cb-1b57-38f8-b4c7-498ae7b74354 | -13.22627 | -54.32305 | 2026-07-05 06:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 741601be-a5bb-3adf-bd34-9caf2a090cdb | -10.9401 | -43.0355 | 2026-07-05 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 185c3ff8-52ec-3387-a4cf-75f18b50f571 | -10.9401 | -43.0355 | 2026-07-05 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b3e81641-823f-331d-b3de-e78a1ce7704c | -10.9401 | -43.0355 | 2026-07-05 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| fd8b156f-3923-333e-8e93-4fcda178891b | -10.9401 | -43.0355 | 2026-07-05 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e99e4762-e157-3336-b841-bc4a383f4174 | -10.9401 | -43.0355 | 2026-07-05 07:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2012266a-8890-3055-9198-99eeb5a5f9b9 | -10.9401 | -43.0355 | 2026-07-05 08:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| a85b4fa8-2f7d-3305-91a6-84f2a284e24a | -13.2407 | -54.3096 | 2026-07-05 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 006c09b6-226d-3e11-896e-ccbf961d7038 | -8.15296 | -36.5756 | 2026-07-05 11:06:00 | TERRA_M-M | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3f9a3ca3-106b-38f4-82ea-17dfce14cd2f | -11.91949 | -43.39088 | 2026-07-05 11:08:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fa639c51-22c9-31e3-9b86-a8bcb6495eff | -12.54536 | -45.4789 | 2026-07-05 11:08:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| c7c3f0f6-34a8-3723-992d-236788cc5cff | -8.71939 | -54.53967 | 2026-07-05 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| c71666dc-be30-32d5-b9bb-ed1c77a5f821 | -8.71682 | -54.55936 | 2026-07-05 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 765c51be-cae7-37ec-b78b-24e4ee6043a9 | -8.71938 | -54.54642 | 2026-07-05 12:44:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 94f968dd-bda8-3699-afe0-0454559cf75d | -14.14983 | -52.88168 | 2026-07-05 12:46:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c538a4b4-a35e-340b-9007-743f82b112c4 | -11.60286 | -61.53055 | 2026-07-05 12:46:00 | TERRA_M-T | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 359f75a0-1ddd-3cd5-8347-458d56d61387 | -12.50387 | -55.75195 | 2026-07-05 12:46:00 | TERRA_M-T | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1f0b2ca0-9924-30ca-bf92-58ab895e9cab | -14.15233 | -52.90835 | 2026-07-05 12:46:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 0b72f58f-f7d4-32db-abdc-c9095c100278 | -12.5025 | -55.72753 | 2026-07-05 12:46:00 | TERRA_M-T | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ec66a6f5-3d16-35fc-861f-661354abcb1f | -13.24172 | -54.32128 | 2026-07-05 12:46:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ad810c53-40ef-3e37-912a-bbe630f42ac0 | -10.90563 | -56.8528 | 2026-07-05 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 215096f6-3347-3062-842d-f0412f536132 | -12.50603 | -55.73357 | 2026-07-05 12:46:00 | TERRA_M-T | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 16772231-bc1a-3f91-9450-7271f1868c1c | -14.15582 | -52.87554 | 2026-07-05 12:46:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 22432a90-3f92-3910-a403-915b6f3af57b | -13.2404 | -54.3303 | 2026-07-05 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 12707d15-0803-34ee-bc0c-4f08b4099770 | -13.2404 | -54.3303 | 2026-07-05 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| b4614bf0-daff-3dcf-b93d-953a6d9ec803 | -13.2404 | -54.3303 | 2026-07-05 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 1afcdf72-3269-32a3-a7b7-f51c86fb4876 | -13.2407 | -54.3096 | 2026-07-05 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 0fe3dc2a-25fc-3a82-a7a3-c5af392dbc8e | -13.2404 | -54.3303 | 2026-07-05 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ce2344f9-b5e8-3bb7-a68a-8a9874d25b2d | -13.2407 | -54.3096 | 2026-07-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 0c15794d-4130-33a6-b7ef-0e34158bccbb | -13.2404 | -54.3303 | 2026-07-05 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| c9dc3317-be30-3045-a35a-a1f97961def0 | -6.9323 | -43.7264 | 2026-07-05 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b225655c-5a59-3b36-9847-0cb595972c98 | -14.1442 | -52.8926 | 2026-07-05 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f12c056c-9d59-39db-8e7b-c38d6fddf971 | -13.2407 | -54.3096 | 2026-07-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d4f7f818-47a4-3863-a405-6d224b04f6e7 | -12.4977 | -55.7343 | 2026-07-05 14:00:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8d395ff8-2477-3e5e-81f9-53305866b8b5 | -13.2404 | -54.3303 | 2026-07-05 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 5d528e2c-d8d5-39d3-b6ac-271721fd9c76 | -14.1442 | -52.8926 | 2026-07-05 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 255959ad-4619-31a4-81db-7815cf236eeb | -13.2407 | -54.3096 | 2026-07-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 275881b1-dbae-3b35-aa52-b116f81d4fa0 | -13.2404 | -54.3303 | 2026-07-05 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 6963378d-c9b6-3e23-ae6e-d0e90e61268a | -14.1442 | -52.8926 | 2026-07-05 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| dbcf62ea-12fd-3302-a743-486660f00bfb | -12.4977 | -55.7343 | 2026-07-05 14:10:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c2b00d22-24d7-3cc8-9429-6989f639e9a7 | -6.9323 | -43.7264 | 2026-07-05 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7d0e6458-5c46-3330-9a25-af72dade2a1a | -13.2407 | -54.3096 | 2026-07-05 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 85dd9f9c-4f75-39bc-803a-db9a77cbbdf1 | -6.9323 | -43.7264 | 2026-07-05 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6baa3baf-d4be-3357-9ea9-307fa2489d93 | -12.4977 | -55.7343 | 2026-07-05 14:20:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 13fce5cd-3fd1-35cb-a119-7b9fbbe65677 | -13.2404 | -54.3303 | 2026-07-05 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| dc1c292c-caae-3b03-9530-46370806b5d0 | -6.895 | -43.7066 | 2026-07-05 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5d204cc7-26ac-31dd-b447-c2bdd12780fb | -14.1442 | -52.8926 | 2026-07-05 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 68487051-9c02-3f88-8766-5907183ab0c3 | -12.4977 | -55.7343 | 2026-07-05 14:30:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 817f3733-c5de-30d1-bd9c-d757b1bacc81 | -14.1442 | -52.8926 | 2026-07-05 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 5404254b-302d-366b-87f4-c8b80191df26 | -6.9138 | -43.7049 | 2026-07-05 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c131d922-3a6a-3953-aed4-1b5830fe3171 | -6.9323 | -43.7264 | 2026-07-05 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d1f315b4-f648-3718-98e4-e5d14fbc719d | -6.895 | -43.7066 | 2026-07-05 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| af997741-2d1e-308a-8d59-a2fe9a03be42 | -13.2407 | -54.3096 | 2026-07-05 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 04506d08-b81b-359d-be6f-f8700aeb6020 | -13.2404 | -54.3303 | 2026-07-05 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| e7e58092-6a25-36ed-90b6-9edfc53b3f2e | -13.2407 | -54.3096 | 2026-07-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 44393750-2064-326c-b959-ec1c0ae05af4 | -14.1442 | -52.8926 | 2026-07-05 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 41686700-9852-32bf-9336-e3756573c7b0 | -6.9323 | -43.7264 | 2026-07-05 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 35fcb820-6dfa-3567-ba19-6c7e72dd40c2 | -13.2215 | -54.3117 | 2026-07-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d9e031be-eee7-383e-b9f7-1ee5550a155c | -6.895 | -43.7066 | 2026-07-05 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 72c6b019-60c7-317a-a296-3d591f5365d5 | -13.2404 | -54.3303 | 2026-07-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 0d947e36-f771-338d-b47f-4e5160655aa2 | -12.4977 | -55.7343 | 2026-07-05 14:40:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |


