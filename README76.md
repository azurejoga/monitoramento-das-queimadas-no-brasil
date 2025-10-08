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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c377b1d3-7fa1-3012-abf3-f7361426afa4 | -12.23803 | -43.78602 | 2025-10-08 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1e884f-068d-3297-af51-ab4264de5627 | -13.75758 | -45.75363 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b50e85a-08d2-34b6-b70c-958a9ee5a150 | -13.36359 | -47.56097 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa4c015-50dc-3cc6-8ac1-b01d1d950d53 | -11.7358 | -50.93571 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8246bc8d-d3eb-36ef-be16-9479102deca4 | -13.06342 | -47.88298 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bde3f05f-1537-3dc9-9282-137a33990d94 | -12.32261 | -50.27351 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea662b63-4f01-396f-9056-75be3b166261 | -11.148 | -54.86518 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72e82391-4176-3297-9721-0ec9bae22a10 | -11.16266 | -54.87265 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e82aaf1e-349a-3fa6-b587-80676421be99 | -17.16552 | -56.60141 | 2025-10-08 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| caafae58-aa4f-362f-890a-f53a950da67e | -11.77794 | -47.56381 | 2025-10-08 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e3dd2e1-078d-3cf4-a79e-0375fd1a1885 | -11.74018 | -50.95089 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0841ee77-7916-3cfe-b6cf-30512697e209 | -12.37617 | -50.3005 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2fc3132-e838-31b8-a7bd-2175921c45c6 | -15.3138 | -46.16333 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 001d6a6b-ea9a-3e2d-8930-c3ca4744f6aa | -15.31286 | -46.1702 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9907b8fc-935f-32ba-91f4-d0ecbcef8a8b | -15.99214 | -50.94958 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5927694-8ea8-36f8-b820-775cefca4894 | -14.38852 | -46.02283 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 079421a3-fe08-3882-89b8-dba6fad73144 | -15.01666 | -47.55994 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bc99fd3-7978-32de-858c-ce7a750eb937 | -15.99795 | -59.54385 | 2025-10-08 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46e3e266-ea1e-3888-9744-92454f5715d9 | -14.67702 | -51.90059 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aeb963fe-9515-32e1-8945-012b859cef89 | -11.13982 | -54.88897 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9350ce3c-8a65-3853-94f6-fd972f31bdf8 | -15.26093 | -46.33976 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74d4f62f-c068-38cd-9e62-872d1d89d197 | -11.68103 | -50.95925 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 835b17ac-5610-329c-8257-3dbdd604ed85 | -13.37158 | -47.55709 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0eedb907-05f4-3722-8f76-c2e8632ebaee | -14.74952 | -47.86144 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c77d8473-cc2c-3295-ab24-77611df615c0 | -12.12174 | -45.13242 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b36fe83-0a89-36ee-b2fa-18f94cfcdab1 | -13.22422 | -47.1774 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 546d1639-3a68-38ed-9050-7abe84bc83ad | -11.98788 | -46.77406 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 742e15c6-fe7f-3d45-a8ad-60d684e0bd8a | -19.52035 | -44.07613 | 2025-10-08 04:40:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6331bd65-2431-3b19-af30-dd306f0b0f15 | -11.3577 | -55.18663 | 2025-10-08 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2962c2ac-dc34-322e-befb-97007b46e598 | -14.38546 | -46.01503 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b8bb656-da71-37f1-b99e-d2beff5c90e8 | -15.49078 | -47.94352 | 2025-10-08 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0981fd05-cb8b-30df-b584-8f04120c1f4a | -18.02716 | -44.94323 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4770a92-35f9-3c72-9461-e91c01f55df5 | -16.88893 | -46.96465 | 2025-10-08 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49f7ad64-d7c7-32a2-865e-feb761921a7c | -12.50807 | -54.7131 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30f34e6f-921a-31ce-89f6-e1c3c9d854a4 | -14.44716 | -48.7876 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b4ac950-9fd2-3dbe-bf43-44c2e67845e5 | -11.69041 | -50.96441 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7266bc63-81ca-3c9f-98a0-75bd7f266d4f | -18.4999 | -43.90387 | 2025-10-08 04:40:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd605fc3-52a1-34c4-bba6-aeaf5c0eb3eb | -18.01748 | -44.94686 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51a7f19b-54df-3605-86d9-fe01d44a9b0f | -15.76675 | -46.25077 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8c5d4e9-4966-32a6-b3d6-90ccc682e5d1 | -17.13478 | -45.78582 | 2025-10-08 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dfb1003-dc34-3fb6-92dc-22479e9761d5 | -17.29833 | -58.06015 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2ef08cb9-f76e-3b35-989a-b52615caf3a9 | -12.16686 | -50.98085 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e066fc9a-f1b7-3f0f-ab81-47f302cd2866 | -16.27556 | -50.98069 | 2025-10-08 04:40:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed15a747-ac72-3cef-a894-327c887b5669 | -11.2842 | -49.98774 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c75fd54-e938-39af-bd5d-f6a7ee858525 | -17.98166 | -44.97599 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c56a565f-05d1-3b0d-9f9c-6ca3cd77f070 | -11.45274 | -50.21237 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa21db14-e9b9-3883-a616-dfd1a1841145 | -11.11483 | -54.04553 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| faa14c7c-b380-3e62-9d37-cd7c4bc4b781 | -14.90767 | -46.82215 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c09ed2a-a8ee-37b9-8cf9-2c38643b09b0 | -11.34006 | -56.20277 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ac53c15-6a90-3132-8025-95493aea1aa7 | -11.42031 | -56.29115 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afb0abd6-28f2-3996-857c-0dbbb8fbc973 | -17.27365 | -58.12085 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 12b07d4d-f4c3-3140-8af9-b33a9ca40a08 | -14.36829 | -47.73527 | 2025-10-08 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2d90c10a-e13b-3292-b4c1-4319003e59b4 | -15.79196 | -46.24709 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b367c68-c083-37a6-96d4-3a5fcd2ef1b5 | -11.71754 | -50.94356 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 68eeac16-133d-35b3-be1c-6fd9d8a5c00f | -11.74613 | -51.48626 | 2025-10-08 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 664c90f6-c2fb-39d0-a901-9b60a9a5e3bd | -18.40416 | -45.21424 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b5bd7a8-5315-36ac-a5fd-d9731bdc24d1 | -11.15576 | -54.86644 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b34420fc-112e-3416-b16b-ca032a1b1833 | -15.32134 | -46.17493 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c2e484f8-18f4-3fb1-9689-1a6755de70d7 | -11.28089 | -49.98721 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15294bbb-486c-3ce4-a2df-d00d1eafc617 | -14.70238 | -48.39942 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81217bc7-1097-31a4-9a85-19c899e40ea5 | -19.46581 | -45.96059 | 2025-10-08 04:40:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d030d938-ace9-3a32-a714-fa6acb55849e | -11.16909 | -54.85862 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e477d2b-6455-3f2a-82fc-01b70f066da2 | -11.73967 | -50.93274 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 402cc656-421d-3ce0-892c-b74910a1ae9c | -19.30772 | -43.16709 | 2025-10-08 04:40:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad7ced6f-2a32-3a29-92f0-bbd6830e36c3 | -13.28413 | -47.15494 | 2025-10-08 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 703fd182-e750-306d-a673-998957ba35bf | -15.77021 | -46.2557 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd8c6fdf-5c3b-3c11-8195-233602bb8284 | -14.36397 | -45.23309 | 2025-10-08 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab7d43b3-3a85-325b-9570-a631d351608d | -18.02099 | -44.31325 | 2025-10-08 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04d8de6a-ea90-3599-8c29-6d1d6d480048 | -14.3647 | -47.73429 | 2025-10-08 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 921765a0-7e09-3feb-a488-785254da841e | -15.4025 | -48.01511 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 210607ab-8701-34e9-b2d5-48d5f21af858 | -13.46728 | -47.71896 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 143dacc2-c7db-3224-b662-88b619883698 | -15.37005 | -47.30338 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 805a6eab-4d5c-33f4-8266-c54613a1b905 | -12.02057 | -45.20886 | 2025-10-08 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5fd2db60-94c4-3874-9037-9087c8678644 | -14.75245 | -47.86365 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 013527a5-9e1f-3335-94fc-cccec990e9fd | -14.44311 | -48.791 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd5fb452-3ca8-3df6-a43c-4122a776128b | -11.33447 | -56.20997 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37951cfb-0eaa-34e8-a71e-a31de31f9fb6 | -14.8261 | -48.4182 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aa01da3-aeb2-3396-90e9-b59af1b3af76 | -11.1803 | -54.88597 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ef183759-8131-3893-a737-31e529ca0109 | -11.94491 | -51.47506 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1efa9b30-8304-3cae-9536-886a43841860 | -15.31416 | -46.16692 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a4f82a8-8da9-3613-8100-70e97e1f433b | -11.37912 | -54.34102 | 2025-10-08 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4d96f2c-1da3-34ed-8184-64d7e47a3e3a | -15.31012 | -46.16636 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00901358-99fa-3632-836f-5e6ab91b3d9c | -18.40527 | -45.20511 | 2025-10-08 04:40:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4a7fb59-a348-3760-b195-2ef625a3734f | -15.60651 | -52.58228 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f618030e-aae2-3716-be63-2b8c2a01394f | -11.44943 | -50.21183 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4165569c-1396-3966-b04b-c239080c4718 | -13.36432 | -47.55598 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30a3a941-d61f-3dc0-aa16-5b3a2894b193 | -11.15274 | -54.86091 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc9a2459-6441-319a-9ac7-23c6aa83e898 | -12.39617 | -51.14129 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c264b90-707c-3f45-a783-fd9223e41b2a | -14.92705 | -46.7954 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fabcd94a-9fbf-3329-83ff-5f55f44241d4 | -11.73855 | -50.93978 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 08491770-e032-3d8c-93f1-02058f31f65c | -13.03169 | -47.90111 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4776546f-6f17-3fd7-a0d2-056dad3b6bae | -14.71299 | -46.07561 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93e12739-2406-32e6-aa37-baad44757a1f | -12.04664 | -47.77795 | 2025-10-08 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a71d12d7-e5e5-3973-9a25-96ad7cebe0ed | -11.70204 | -50.95547 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4c876e06-0614-36e3-8de8-b698b019023e | -12.2503 | -47.86541 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f66782b-a631-39d0-ae6c-317bdd0251e4 | -11.11853 | -54.04617 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 287ab6a7-8afb-3c53-b497-b2ef5baae658 | -10.88542 | -56.07062 | 2025-10-08 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3278283-b42a-3eac-99b8-ca1de38dd4b8 | -13.31264 | -48.03186 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2af7886-b4af-3863-923b-552f5c77bdef | -11.33586 | -56.20197 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69435cd3-3071-3163-885c-dd8640bcb75b | -11.90982 | -55.90339 | 2025-10-08 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README77.md)
