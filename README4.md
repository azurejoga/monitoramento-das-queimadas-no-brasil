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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f57a423-fe64-31cb-a862-527e11b7f331 | -7.4074 | -60.0108 | 2025-08-07 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 54bf96c4-aff6-30ad-aef0-5d78cb44ec66 | -8.5211 | -43.3063 | 2025-08-07 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8d8a6217-2197-3553-bf69-237758eb1799 | -8.9028 | -60.7498 | 2025-08-07 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 67e77cb2-315c-3786-8d5b-44030a67bc8e | -10.6441 | -44.7413 | 2025-08-07 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 31861f89-0829-354e-a7ff-2bd9ea2c9057 | -8.9399 | -60.7481 | 2025-08-07 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d4e18b26-fa81-3551-905a-46d999c1654c | -8.9041 | -60.5577 | 2025-08-07 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 47ccb6e6-26e0-3b70-88ed-0af7ffdd9fe5 | -8.9215 | -60.7297 | 2025-08-07 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 75063282-fb7b-3cf3-806a-f9698815fa83 | -7.4074 | -60.0108 | 2025-08-07 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 4482368d-4caf-3f68-b8c8-29127a905006 | -6.5194 | -45.569 | 2025-08-07 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 50e1263d-2b49-345f-b719-049da1a2e498 | -5.8218 | -46.2258 | 2025-08-07 02:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| bf8f757b-9639-37ad-bebe-c7e7a31c827d | -10.6438 | -44.7645 | 2025-08-07 02:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| dc26c0a7-b0ef-37fc-b7c5-02e14fe461e1 | -8.9213 | -60.7489 | 2025-08-07 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 00134a2a-46bb-33c1-8a47-91a477d17cef | -8.9212 | -60.7681 | 2025-08-07 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 77ea9cd1-ebed-31cd-9147-15e202b7afd0 | -5.8218 | -46.2258 | 2025-08-07 02:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 8028573c-0932-3e32-9461-c2724088e4e4 | -8.9041 | -60.5577 | 2025-08-07 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 7b8037de-f622-393f-a31c-2efcf32aafd6 | -11.7508 | -48.1825 | 2025-08-07 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 314f1f52-0490-3d3c-bc32-ca3e61647556 | -9.625 | -40.6122 | 2025-08-07 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 5a76f09e-c372-3857-9ca9-71a88f391787 | -8.5211 | -43.3063 | 2025-08-07 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4968acf6-a49d-3a2c-a2de-30522538d423 | -10.6441 | -44.7413 | 2025-08-07 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 0312ed64-20c5-37fe-9153-56cae305183d | -8.9213 | -60.7489 | 2025-08-07 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 53fba910-7930-3a45-bc43-b3f214b81f61 | -7.4074 | -60.0108 | 2025-08-07 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| be56cd3a-53f5-394a-9f47-8c74f41b73f9 | -9.6254 | -40.5875 | 2025-08-07 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 243b2969-4334-3e47-9b09-fdcd8293e741 | -10.6438 | -44.7645 | 2025-08-07 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 2a9dfcfd-47ac-369f-820f-7c53b5b6dd4e | -8.9215 | -60.7297 | 2025-08-07 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 96764b7c-fb9f-36fb-84cf-26d80f95bd12 | -7.4074 | -60.0108 | 2025-08-07 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| df157b0e-1ccb-318c-82b7-b2cee6725b89 | -11.7508 | -48.1825 | 2025-08-07 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 034a9745-4c93-3422-a249-d541c10b0ca2 | -10.625 | -44.7439 | 2025-08-07 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 7cbf0be6-6895-3dc9-a378-118b31fa5718 | -10.6438 | -44.7645 | 2025-08-07 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 224f8f8d-5922-3b27-aafa-9cde0db362fa | -8.9213 | -60.7489 | 2025-08-07 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 5036d543-5b07-349e-a9e7-87c8692bba9e | -7.389 | -60.0116 | 2025-08-07 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b4175474-812f-345e-bc8d-dece878f9b78 | -8.9041 | -60.5577 | 2025-08-07 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5b7b7144-a4ac-3ea5-874a-936e423886b6 | -10.6441 | -44.7413 | 2025-08-07 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 98245e2d-07ae-3363-b044-1fb21e6880a0 | -8.9212 | -60.7681 | 2025-08-07 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 4b4f3fc4-a388-384b-9e49-16be6804bf66 | -8.9215 | -60.7297 | 2025-08-07 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 1b67c626-2f00-3325-bd24-eef0ae6bf952 | -10.6441 | -44.7413 | 2025-08-07 03:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| db54b6a8-cf69-3d17-a175-44371a9c6689 | -7.4074 | -60.0108 | 2025-08-07 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| fa38b64f-6647-34f6-a97f-3f31d2bb1216 | -10.6438 | -44.7645 | 2025-08-07 03:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 09596eee-d5eb-3011-946f-333f2aa9aa67 | -14.534 | -45.5879 | 2025-08-07 03:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 1575140f-e554-3950-830e-552e1a8f8932 | -8.9213 | -60.7489 | 2025-08-07 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 94d1dd37-f4b7-30ab-adce-0c3a5d55ac61 | -8.9041 | -60.5577 | 2025-08-07 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| e760c1b8-af8f-3d59-974d-dc18f73adda7 | -8.9215 | -60.7297 | 2025-08-07 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d8754633-b9e8-37fa-8d29-f4e185b29447 | -5.8218 | -46.2258 | 2025-08-07 03:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 33f34251-298f-3cb4-a206-d900b8542ece | -10.625 | -44.7439 | 2025-08-07 03:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 69391aba-e1e9-3147-a625-9c0907a31a98 | -8.9212 | -60.7681 | 2025-08-07 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ceb3784b-c426-3fff-afa4-02e754946809 | -14.534 | -45.5879 | 2025-08-07 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 38185d95-bdf5-3afc-9f22-28affe9aed5a | -10.6441 | -44.7413 | 2025-08-07 03:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 131.3 |
| c3bbcd68-ebbe-3ed4-bf0f-b6debd4a8189 | -11.7508 | -48.1825 | 2025-08-07 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| efba931a-5c1d-3b91-871b-ee8526e4b0c5 | -8.9212 | -60.7681 | 2025-08-07 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6050cc81-60af-333f-ab5e-d831aa5193c5 | -10.6247 | -44.767 | 2025-08-07 03:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 752b38d9-ccf7-3224-a8bb-72ab895c03a2 | -8.9041 | -60.5577 | 2025-08-07 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5084d0cd-2b61-323c-9025-5e8515676549 | -8.9215 | -60.7297 | 2025-08-07 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 1b0b934a-4c69-374a-bb79-b385ca1ca62f | -10.6438 | -44.7645 | 2025-08-07 03:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 19267ec0-f5df-3b94-87a4-e83bfc962c4d | -14.5335 | -45.6112 | 2025-08-07 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 244e90b6-5373-33f6-b600-a8a23180a636 | -8.9213 | -60.7489 | 2025-08-07 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 503cb154-c5fe-38dc-bbd0-2cb5cede7271 | -10.625 | -44.7439 | 2025-08-07 03:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 30ced5a3-f518-33d6-9871-76dcc4b8c22a | -7.4074 | -60.0108 | 2025-08-07 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 8ba15f8c-39b9-34b9-87f6-fcc696e92aa4 | -9.55492 | -40.34858 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c3ae180f-fda6-3ff1-8fb2-ace2283fd559 | -9.55775 | -40.34232 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e2bcc286-601f-3a4f-9d86-257183c1664c | -9.5567 | -40.34763 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 194b43a1-9273-36eb-bd2b-90cd934708f3 | -9.56232 | -40.34447 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ced27207-1ee8-3e44-bc3e-afbedb0b3437 | -9.30109 | -40.24109 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 601ccd39-f972-3562-8a81-3fd5d37ab86a | -9.56413 | -40.34352 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 9058372c-85ce-3867-ae41-479b42eb1712 | -9.3611 | -40.3153 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f4ebd93-a06e-34cc-a553-c2f432ea8492 | -8.58637 | -36.17096 | 2025-08-07 03:13:00 | NOAA-21 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 509af1c2-7dbd-34d6-b78c-2b4ab7060661 | -10.27751 | -40.81438 | 2025-08-07 03:13:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ba65178e-0bd7-3fcd-8a75-8eb0c2d02549 | -9.5613 | -40.34982 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e583ca17-b5dc-3cb3-8301-7e96600529e6 | -9.36006 | -40.32061 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65e4e23b-118e-3694-a459-ae9544dab495 | -9.55594 | -40.34323 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| be7bc543-ab00-3532-baec-b3a7cd4a370a | -9.56309 | -40.34885 | 2025-08-07 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 68f969dd-7e4f-3318-9e32-cde7cc6c0db2 | -8.97907 | -40.61983 | 2025-08-07 03:13:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 288a7d84-734d-3b3a-8f2a-70b5285b4e48 | -16.21662 | -40.13771 | 2025-08-07 03:15:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 03ce6abe-c32d-33ba-851f-02deb4624404 | -15.74514 | -43.39103 | 2025-08-07 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1ae8a774-287b-3c90-ba5b-b50967704814 | -18.72821 | -39.86872 | 2025-08-07 03:15:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 16447039-6eed-31d8-a4a0-d67e5102e3a3 | -17.19904 | -44.33118 | 2025-08-07 03:15:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5dc6072-e0ce-3d08-abbf-dfde45cb5c1b | -18.72836 | -39.87201 | 2025-08-07 03:15:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7d669264-bece-3fca-aa81-85995a80ae6c | -18.72906 | -39.86859 | 2025-08-07 03:15:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 20ce57e6-d6ed-3a1a-87fd-faac2d5e285b | -15.93275 | -43.51668 | 2025-08-07 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1857302a-f6ff-3de2-8050-9f1c3fc90dd5 | -18.73347 | -39.86988 | 2025-08-07 03:15:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60d316ca-edf6-35df-be9a-14851bc0bac0 | -17.20062 | -44.32453 | 2025-08-07 03:15:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c652087b-bec9-3882-aa51-1629d8221450 | -18.89546 | -41.00799 | 2025-08-07 03:15:00 | NOAA-21 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 45ab79c6-b2c5-37c1-8901-79471e68ee8e | -17.20223 | -44.32812 | 2025-08-07 03:15:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4664db5-97bb-32c9-9468-2bad938592e0 | -18.72749 | -39.8721 | 2025-08-07 03:15:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6321ac05-5e09-3be4-941a-c04e49f470f3 | -15.77894 | -39.3736 | 2025-08-07 03:15:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6605b6fa-3851-3922-9c25-51e509bcc640 | -22.73696 | -42.96088 | 2025-08-07 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3acbb8b4-3c38-3b4a-bd24-29fdded5cf34 | -22.03654 | -43.21556 | 2025-08-07 03:17:00 | NOAA-21 | COMENDADOR LEVY GASPARIAN | RIO DE JANEIRO | Brasil | 3300951 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14199a3a-d741-3eba-b97e-822c3559e52b | -20.20244 | -41.45685 | 2025-08-07 03:17:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4a39daba-3a6c-3c91-8a1c-f0cbe85d645c | -20.33757 | -41.44492 | 2025-08-07 03:17:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 561978fd-cf20-3641-99e4-085dd8e60692 | -19.93599 | -44.17737 | 2025-08-07 03:17:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2b3fe05a-7984-345b-b8fb-551079a307ae | -8.9041 | -60.5577 | 2025-08-07 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 3a7a9792-661b-3f9a-9494-9e12d13a9b56 | -10.6438 | -44.7645 | 2025-08-07 03:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4cd43731-d940-3600-ae18-f8dd253960ad | -8.9212 | -60.7681 | 2025-08-07 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8bb55ca6-c52f-3393-b45d-0489dbe2c81f | -8.9213 | -60.7489 | 2025-08-07 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 153.2 |
| e504fcdc-0ac9-3522-b67f-2b40585ffdc7 | -10.625 | -44.7439 | 2025-08-07 03:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| cdbed41d-6933-36b1-8a4d-f83987e2ebf4 | -7.4074 | -60.0108 | 2025-08-07 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dedfd088-daa4-310a-b755-cff6d761b231 | -10.4402 | -44.3982 | 2025-08-07 03:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b410af27-70b3-399a-ac05-33e05b52487d | -10.6441 | -44.7413 | 2025-08-07 03:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| cb30dc59-b30a-3f74-9983-9da247bd0fdc | -9.553 | -40.3503 | 2025-08-07 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.8 |
| d6dfdf8a-a56e-340c-bee1-f72ef72b63a2 | -8.9215 | -60.7297 | 2025-08-07 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c3f4e539-887e-3d6c-ab0c-3a5b406e70b1 | -8.9215 | -60.7297 | 2025-08-07 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d46087ce-ac32-369d-b284-977e8d574051 | -8.9213 | -60.7489 | 2025-08-07 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |


[Clique aqui para ver as próximas entradas](README5.md)
