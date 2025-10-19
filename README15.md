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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cbd9cec-166e-3cd5-abcf-57409097a840 | -13.90353 | -45.53386 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b331c79d-3623-3704-b0c6-4bad966946b5 | -11.6428 | -44.08839 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b3cbd19-74d4-3f2c-9004-74976947d615 | -12.98692 | -47.26386 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 402624e8-a79d-3743-8409-9d5e60b0fb4b | -12.00001 | -46.7733 | 2025-10-19 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c2c0b17b-750d-3d5c-bd32-1950b17ec635 | -12.32772 | -41.38371 | 2025-10-19 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c527e16a-e58f-3739-a765-5c113d96e533 | -11.99749 | -46.7698 | 2025-10-19 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0b828ed0-e4fb-3cff-ae5f-fa671eaa6219 | -15.0331 | -46.61525 | 2025-10-19 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e167b54f-96b0-32be-925a-9843b035423b | -15.02842 | -46.61105 | 2025-10-19 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51e8446d-1198-38d6-bf2d-7a5e79668d79 | -14.28292 | -42.32791 | 2025-10-19 03:45:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| ea834261-2f54-38a5-90e8-510e8ce8c107 | -12.98451 | -47.28151 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb768a84-8514-3c48-8ebe-b031b87785c8 | -11.60883 | -44.05817 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ffa337e0-8a44-3099-b776-283219619bd6 | -11.60786 | -44.06347 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e4c92d52-644c-35e1-b6a6-3b4d9606f766 | -10.80802 | -43.92689 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ee975c6-cd79-3b61-a84f-f6ab15f72312 | -10.23534 | -44.89272 | 2025-10-19 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5dfe34a4-05a7-3b10-b17c-adfe0c5dfbc6 | -15.25984 | -43.58896 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29e58e14-67c3-3e43-a468-36da31f71cc4 | -12.14422 | -45.07381 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b994903-f90f-3f75-b86c-21dc9ea4a54e | -16.78924 | -42.76398 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 011132bb-0af7-3687-974d-fdbd9b8a00e6 | -9.98341 | -47.05781 | 2025-10-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02c30646-0b60-35cf-8914-fa6080493a60 | -10.97738 | -42.29476 | 2025-10-19 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 40733955-e03c-3b8c-b7e2-dcd52365e875 | -12.15088 | -45.09396 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85ee33a1-9232-32ff-9e37-368de75e228f | -13.024 | -46.95444 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f2f9097-2146-3cf9-8455-811082723e04 | -13.8662 | -45.46214 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1858e89b-c982-3d35-800e-68b0f8c43842 | -16.14415 | -41.15408 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 38f12c52-42c8-3439-8664-28a40e51f95d | -16.14288 | -41.13957 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df1073a7-2bf0-3a31-acec-89cd88c03a6a | -16.82171 | -41.7994 | 2025-10-19 03:45:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9ed55ab1-653f-3ccb-bfbe-049c7ace09f0 | -12.15707 | -45.06128 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2bac2b1-097f-318e-b88b-7fbc04844936 | -12.98621 | -47.27315 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b69a9734-0f1e-3447-b937-74c1bae51d82 | -16.78064 | -42.76566 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4b59c74-a9e4-3afe-bf68-848bbf913ef5 | -12.44348 | -44.74981 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f058cd69-9110-3fbe-80b1-cb9bc96741ab | -10.22623 | -44.05117 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 543f7fc9-1067-37d0-ba3d-faf24371f460 | -12.4538 | -45.43869 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2681a2e6-6fbf-31cd-8a6a-1dee8d4bd560 | -12.45776 | -45.44601 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6959533d-5d45-3b10-aebe-89fff578510d | -10.88854 | -46.08815 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 13f58d2b-2428-3b6a-bb86-ab0f919b69f2 | -16.14865 | -41.15008 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 2da8bcef-6c23-3ea5-b2fc-83304b621caf | -17.08643 | -41.69379 | 2025-10-19 03:45:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0c8b930d-4526-337b-95f6-6be0497973a7 | -10.68257 | -44.54284 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e99a7ec-f90a-3d47-abc0-2658d71180f7 | -15.51932 | -41.67207 | 2025-10-19 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e76dc344-d0e7-3d72-a4f6-43eda0ac37b7 | -10.22853 | -44.0536 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6295bbb0-5dda-3c02-9d5f-28505c154c94 | -16.7562 | -42.77906 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 9dbc1377-0244-39a4-8d78-437d9b8d33da | -16.75555 | -42.78268 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 84397ee6-b342-3fb6-a8f3-118c2821ad1c | -12.93562 | -42.8628 | 2025-10-19 03:45:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 53acde04-f609-30d8-8b88-0cd46bc79fab | -16.77996 | -42.76928 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 21cdc9cb-2b6d-335d-80a8-1013a94986af | -12.99186 | -47.26904 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad9e6bed-03c1-37b8-8d53-5779779cf7a3 | -16.74816 | -42.77765 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bd2b577-421b-3f22-bbd6-8a931351c376 | -13.90293 | -45.53694 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5fa9c39-c808-3877-823b-1b5e891de451 | -16.76023 | -42.77975 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 58.4 |
| b5b5228d-ee7d-3a17-951c-52cc1df8106c | -12.98612 | -47.26793 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3d5b889-516a-3c1a-a96d-903ee90d2dda | -12.44842 | -44.75069 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c5f18fe-d80c-3f5d-8ef5-efd552c0c0b2 | -12.98536 | -47.27733 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14fa03c5-a85a-36de-9e91-8cd1903f2510 | -10.86453 | -43.94319 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d89ecbc-d139-3610-8ac3-da12bce4c29f | -14.38593 | -40.77457 | 2025-10-19 03:45:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 57ec2a28-8f8d-30da-8cc9-0212c8d96660 | -16.73533 | -42.80249 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 186b3a7b-edac-3d83-90ef-a318d3adb8fa | -10.71494 | -44.5353 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c74a0dc8-2b7a-33ab-8be0-46d0742546e7 | -12.16002 | -45.10111 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52cc6e89-b7e0-3554-b0ea-475540d39e60 | -10.53502 | -44.1438 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e65e8669-54e3-3c2d-8542-9c9d02b4f5fe | -10.10116 | -44.55944 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4241ef13-feaf-377b-b61c-31a65ad2669f | -13.40152 | -42.80928 | 2025-10-19 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0b81335f-1f92-34b5-acf9-5035c7dd49bc | -16.7481 | -42.8009 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deaf733b-6537-3827-b287-54415b3c2bfa | -10.68226 | -44.54381 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18daa590-26a7-3406-a05d-0604eb33933f | -16.73943 | -42.77998 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e624ea3-9255-3f73-a2d6-c5b7ad3f3854 | -10.12803 | -44.52678 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c06b4bb2-8790-306a-a7e0-04a2135b74d0 | -12.18601 | -45.10231 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae3cac1-cff3-35f4-8d1e-dd9525eaf0f7 | -11.60309 | -44.06257 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd221e23-299b-3c51-9cf6-702a03001fd3 | -12.19158 | -45.10056 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6dc6afaa-2b35-39f9-9ebf-4eee2b55b491 | -16.75757 | -42.79446 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99773686-08d7-37c7-aa17-8512fbf94a40 | -16.7401 | -42.77628 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d356cc56-dae6-36a3-9d49-a6357de073e0 | -13.71132 | -40.98502 | 2025-10-19 03:45:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd5f0a87-e754-3d63-9f6d-4968a64236fd | -13.90413 | -45.5308 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae1c59b7-15a9-32fe-a21f-2394963b62c2 | -10.92069 | -43.82334 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca621964-85b3-3d4d-9948-0eb31f952ca3 | -11.65248 | -47.31849 | 2025-10-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66a34fb7-df2f-3489-bd63-8c37cba05782 | -10.89207 | -46.06961 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 32b6461c-ff90-34ea-885c-35e694b001e4 | -15.03378 | -46.61186 | 2025-10-19 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 7096a450-b614-325b-afba-36c2ff7c59ff | -10.92144 | -43.82168 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d3d4002-7356-3e8d-94a8-e874899e6298 | -10.72931 | -44.54153 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dd4c1fb-e2c4-3083-841a-e7fc8c6e1f16 | -12.98366 | -47.28567 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0be02f5-db32-3612-8691-1d8ddb1bd631 | -13.89012 | -45.52204 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d16785c6-7e57-32fd-863f-df2a8fca4910 | -16.75824 | -42.79074 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8099749a-4050-37a6-8937-7313c250ccfe | -16.80947 | -41.00697 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1c14cc9b-d0c5-3504-a401-61c740588f28 | -16.7475 | -42.78127 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7a547ba-a5b0-3be6-8cb8-bac884d3e968 | -11.14638 | -47.71148 | 2025-10-19 03:45:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b48db55b-a528-362b-9428-e695ffbd8a61 | -15.01741 | -41.99699 | 2025-10-19 03:45:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f92f964-463a-3a34-8b7b-6dfd46b21268 | -16.75286 | -42.79756 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b79d30-5ee7-3395-905a-87abde32cbf2 | -16.82466 | -40.18077 | 2025-10-19 03:45:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 86b18893-1477-3242-bff1-de1669d94080 | -15.78052 | -41.33895 | 2025-10-19 03:45:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4881f630-045e-3d5d-b616-0c0bc093b602 | -16.80724 | -42.82391 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df7e4f7a-4608-378a-a217-5dc57b5ee31c | -10.58123 | -41.5059 | 2025-10-19 03:45:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 94bb6bdb-6556-37c6-ae7a-a7300b3eb7a6 | -16.74346 | -42.78062 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 355742a2-b8b1-3806-bea8-c748778b7275 | -16.76553 | -42.77332 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f2eee04-0a00-3095-926a-a1c39fa3e18f | -11.99671 | -46.7737 | 2025-10-19 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 43280374-71ca-3bb8-a989-9bf93e4b9881 | -16.76893 | -42.77749 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a27e1bd2-9d81-3721-bf9f-35f8323b9056 | -9.96293 | -45.2816 | 2025-10-19 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e26de392-f198-3558-b7bc-7f45602d1045 | -12.99362 | -47.26606 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b650efd6-a421-3193-9d3a-b12ad4ea7316 | -12.18198 | -45.09585 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4acf2255-f545-3138-8b40-96184b8c0224 | -16.75283 | -42.77475 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 47840900-f80e-3672-b222-ef1489d22244 | -10.55819 | -43.3924 | 2025-10-19 03:45:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 66141ba4-7d8f-3f56-9541-b95907e86ed7 | -14.97998 | -47.08017 | 2025-10-19 03:45:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 174bce69-e4ea-3984-9077-06ed25b835a4 | -14.55212 | -43.50905 | 2025-10-19 03:45:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b909bb4-9806-3a01-a68d-507814392e01 | -13.21463 | -43.15604 | 2025-10-19 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7f6c4622-ff18-39b0-9780-bfa6b5030c8b | -10.36939 | -47.46461 | 2025-10-19 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5cc06291-c7c8-31fa-84a5-22bd7dc1f1fc | -11.41681 | -41.42297 | 2025-10-19 03:45:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README16.md)
