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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d269106-c86f-30f2-a842-b566f775ba7c | -13.18315 | -47.39404 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e09d41-088b-36e9-96e6-902185bab9f6 | -15.29304 | -49.47971 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2910b251-bf01-37d2-8c38-7959066fae07 | -14.7293 | -46.83134 | 2025-09-28 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b731becc-0e0b-373a-b08a-5a2849539a66 | -15.25776 | -56.82439 | 2025-09-28 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5f4e2db-2346-336e-906d-96dfd4abe500 | -14.83808 | -45.57294 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29aac28c-8d14-3713-8396-3188b3fd2f54 | -19.32599 | -43.81683 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddd00a80-19f7-3fc7-ac3d-6e996a7004c8 | -13.60824 | -48.102 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3eaccec-9a0c-3259-a95f-ffcb054ec78e | -12.65493 | -51.6847 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68d45e78-a02e-321d-9344-cb81fa9e423c | -15.53502 | -47.89761 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f96c6a8-2396-3d8b-90d4-15bb89f77334 | -18.1136 | -42.18724 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a9ed636f-2de0-3324-8f12-8f38dc8605a5 | -13.58345 | -47.30968 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c6df760-3b96-3e19-beb8-2543d2593dd3 | -14.93115 | -47.69983 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55f03290-f80c-3fe6-a856-13834a57cb9d | -13.40005 | -48.151 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d00369e9-e015-30a9-ab48-225e96a244ba | -12.6474 | -51.68328 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cd93bd4-b94e-31b7-ae6d-9297a1975da7 | -15.81281 | -46.04253 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70e75b0c-0f4b-34b9-9a21-4c67732066b8 | -19.93887 | -43.61757 | 2025-09-28 04:27:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 52ebab4d-5cf0-3a58-999f-0fc7a0aabfc8 | -15.53003 | -47.90778 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa5621a6-cf1c-3b20-92c6-cabf59fba3e1 | -15.54428 | -56.29248 | 2025-09-28 04:27:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba25babf-1d28-3a25-8bf3-f3ab3dd2fdf1 | -13.60113 | -47.32719 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9297ce7d-ef8b-3ff8-bacc-b062d2d1f36f | -14.49714 | -48.55558 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b7b884a-d2cf-3060-84b9-10c4a7fcbca5 | -15.28121 | -46.42131 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20a1a9c8-61f0-3e1e-b532-b13ed6077751 | -15.63041 | -46.25861 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4780adad-260a-38cd-816c-d5a23d53c07f | -14.58511 | -48.25978 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61ae430c-2b25-3762-95a2-47bab386263f | -15.21248 | -48.07191 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91f665f3-be02-31cc-a0e4-5f6a333886f9 | -13.78536 | -47.8837 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a9f846f-f134-3ec5-b06d-9d910bd06df2 | -14.44355 | -46.36279 | 2025-09-28 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdff7659-efac-3fac-9106-ad078ed5ac26 | -13.58953 | -47.31432 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b971c341-14ae-3c2e-bbd2-dd97d1415114 | -15.89794 | -46.20054 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2665ee34-372b-3317-91fb-ab02f0361c8c | -19.86911 | -43.80502 | 2025-09-28 04:27:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 13d9d887-2f0a-3afa-99e7-137418710627 | -12.96761 | -47.21041 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22e27747-c61c-3be7-93fe-6a33e626ade4 | -15.8802 | -46.20115 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 321836b8-5a02-3143-816c-5ab84b32b368 | -13.60856 | -47.32109 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 977f9a76-c92d-3984-a440-fb4bffa0dd60 | -13.78424 | -47.89078 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dacd2e68-c921-3c94-9a5b-4de7e0a2c52c | -13.60414 | -47.32756 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1adb7aca-6fde-3c00-b502-49b6bd84e0b0 | -20.2048 | -48.68254 | 2025-09-28 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0f86734f-78c0-324c-b408-e2a072250460 | -14.58349 | -48.24858 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e05b8ef-0d13-3c1c-bf37-742d36299a63 | -13.34339 | -47.3034 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f46d1fb-d994-35ad-ab94-f264bbf6b9d1 | -15.22022 | -48.06589 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3f3c895-b6af-312e-91c9-fcc3b2a3652b | -17.44851 | -50.83818 | 2025-09-28 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 171ab4ed-d576-31c4-8e7f-1329886396e2 | -14.49415 | -48.55527 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9103dd18-92bc-373d-93a8-79ede4a9bd39 | -18.20348 | -53.31933 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 127938bc-62c4-3940-ae4d-4ae95ea2637d | -12.98386 | -49.44086 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93bdcaa5-1215-3d22-9de4-410ac6ccf943 | -12.99067 | -49.4419 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13cb0823-daa4-3451-8703-a402001416f6 | -16.26949 | -51.05339 | 2025-09-28 04:27:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f51d642c-8935-32e4-a92c-f39e349ae447 | -20.40517 | -46.46788 | 2025-09-28 04:27:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fba22bde-9740-3c47-b5c0-3e1b6114654d | -18.19879 | -53.32346 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72ae298c-5082-39cc-acfc-44906043ba2b | -12.98323 | -49.44466 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fcab2b1-a51e-3d69-95dc-7e06406ebf01 | -13.77654 | -47.87498 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a40f35d7-54cc-3f73-9de4-c6d45e054054 | -14.53877 | -48.40162 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 942d3745-1df0-3918-ba47-ad0259685f1b | -13.43726 | -46.51648 | 2025-09-28 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20e6b2db-2ce9-3587-a564-d7386761e55f | -13.60667 | -47.29166 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23af4c76-ecee-315b-b979-64216c3d2753 | -18.19502 | -53.32244 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20c33493-9978-393f-8e2a-9ffa11caa009 | -13.31796 | -47.31381 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94dbd271-463e-3efb-98ab-319c2cad4c0f | -15.20289 | -48.47596 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09f6e511-2c08-33cf-875c-1d06aab1fe98 | -12.96319 | -47.21696 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f7465e2-b7f0-31f2-8a94-0f61143ad9ec | -13.59946 | -47.29422 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f92ad005-de7b-38f8-abfc-f5b5f7f9995c | -15.96582 | -50.87725 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 978a0d0c-66f0-374f-87e2-5c92b792b238 | -18.19972 | -53.31828 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57d6dafa-bb69-36df-ad45-9e4a9012a38c | -12.7649 | -50.49455 | 2025-09-28 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5523e689-8fee-32f8-b889-044079cc0de7 | -13.61162 | -48.08073 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b749b449-eee5-3e98-b28f-7ad546adad4d | -13.59116 | -47.3038 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fb0dca4-97ca-3ec0-85ed-c416332c8522 | -12.9925 | -49.43081 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5b2bca1-e6ee-31f0-ab34-1c539ee80c0a | -13.7897 | -47.92075 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24aa0c8a-cfa6-35ba-a125-0a1ea68c946c | -15.53554 | -47.91604 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1391cff3-2d6a-34d4-a933-7aa6ee447795 | -13.25355 | -48.45065 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d701c252-8e1a-3e29-8a60-8a26b4b30f69 | -15.26339 | -51.48114 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4164e27f-fa87-3461-ab9f-980fab990571 | -13.6376 | -48.06685 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aafaddd3-c701-35c0-b415-ff32c1c3bdb2 | -12.99283 | -49.45007 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a6c5b2b1-c6e9-30d6-ae09-a39df9b50396 | -13.62679 | -47.31316 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cb1884f-1106-38a9-877b-ff93e58ced95 | -15.83935 | -56.40084 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6df13d46-70cd-3cad-a781-d79845f5ab40 | -13.60774 | -48.08373 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4dad32f-212a-3250-8504-c650086c00ac | -13.60831 | -48.08019 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2415c10-9877-30aa-8d1b-a7d753a97511 | -15.03037 | -47.14758 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcb4cdb4-d581-3142-9c1f-11f119a790f9 | -19.5035 | -46.34213 | 2025-09-28 04:27:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 49ac1e9a-2664-3ef3-a587-03c7e405c9d7 | -13.26683 | -48.45292 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c4ec88a-5402-3545-aa80-b54e6530825d | -15.2891 | -49.48273 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a321394-3fc7-3e75-8b6c-97e81dfab8fc | -13.64092 | -48.06739 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd6cc4c4-4524-317e-a9a9-48c52f466fb8 | -14.53433 | -48.40818 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89e23f20-85df-3f42-95d0-49cf724f00b2 | -15.08707 | -48.32872 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fa00865-9c08-31fb-b2c8-f33371da4016 | -18.90635 | -41.1301 | 2025-09-28 04:27:00 | NOAA-20 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 098e3426-c9cf-304e-984d-42a699b9f64e | -15.35061 | -50.13416 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9529cf18-2630-3d98-accd-fde2852a042a | -15.09037 | -48.32928 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f27c32f7-37f2-308e-b40a-ae32e47056e5 | -15.43109 | -48.23554 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2eeeb5e4-7416-3b0b-890f-71f4d2fba8ee | -15.62697 | -46.25808 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99d19b75-22f4-3ec6-8fea-d9c3bebf94d1 | -15.43449 | -48.21418 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6b04785-383d-308f-96ab-6bc2214a3184 | -13.58567 | -47.31731 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 476265fb-371f-3762-9a9d-6b47985657b7 | -13.7156 | -48.34471 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c465154a-667b-3d72-a232-71ea6d152b79 | -15.62217 | -48.35907 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cf90231-e112-3fb3-b39a-06e81c82e4b5 | -13.71503 | -48.34827 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0d4f9240-13c1-3335-ac8f-dce1a39cc7ab | -14.58292 | -48.25214 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f10ddcc-80b1-31d5-b647-71917547fc60 | -13.39723 | -48.16868 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e3424d4-896b-31a1-858a-17739edc81e0 | -15.90252 | -46.21728 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 989a648b-d1dd-314b-8431-b732b050d5c8 | -15.90139 | -46.20108 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17a80ab1-c241-318f-bb14-e7757a4d3bfa | -15.08561 | -49.56612 | 2025-09-28 04:27:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5967a156-5fb3-3e13-98cc-e6a7f108361e | -13.00859 | -49.4605 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 52213947-3061-3680-84e6-7246a261aee6 | -20.4129 | -46.46461 | 2025-09-28 04:27:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf7b0827-a0a0-31d8-ba8c-1e6e06a942b6 | -12.65811 | -51.66602 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 211e132e-8dbe-3bbb-9b6b-bd6b2fd2f820 | -14.3353 | -44.49672 | 2025-09-28 04:27:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b21b2c3-c0d3-3412-908f-6506492e2e0e | -13.62568 | -47.32031 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9befc495-bb77-31ff-8620-9ed9060969c4 | -13.34725 | -47.30043 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README80.md)
