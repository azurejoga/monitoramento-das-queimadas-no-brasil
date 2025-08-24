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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28d580b7-fc8d-3c48-b677-ef6b9ff8a8b9 | -21.72562 | -46.8182 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8fc901c0-b6f3-32a4-8bed-8b9eea7bcfcc | -21.03627 | -42.5317 | 2025-08-24 03:47:00 | NOAA-20 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 8b9d2270-f5b0-3a97-97b7-a3cebd5c5825 | -21.72697 | -46.81166 | 2025-08-24 03:47:00 | NOAA-20 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e7cc1a84-d249-3a7d-9a0d-9ddace6c4adc | -22.00511 | -44.99937 | 2025-08-24 03:47:00 | NOAA-20 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c2ef7084-dc07-3e0e-892d-df93c6fd778b | -20.08356 | -46.10649 | 2025-08-24 03:47:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d536d4fb-de53-332a-995f-b2a4b10163ec | -20.35043 | -51.69479 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| dadfb2ff-7dd2-3779-92bf-230d77e41125 | -22.28311 | -42.58364 | 2025-08-24 03:47:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2cf31a59-a7ac-3401-ae4c-fa64f60ffa20 | -19.62832 | -43.18521 | 2025-08-24 03:47:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 29873a79-d734-3994-ad51-d60e3704fc7d | -20.08156 | -46.11659 | 2025-08-24 03:47:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 118b79c1-55a7-314d-930e-9213b1192793 | -21.54593 | -44.17401 | 2025-08-24 03:47:00 | NOAA-20 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dd1b73f9-b2d5-3a11-b900-8f719a37ed71 | -23.25268 | -46.62945 | 2025-08-24 03:47:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| ca305ec2-2a7a-3956-89eb-efd4e461e404 | -19.92545 | -44.2175 | 2025-08-24 03:47:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 00daaead-50bd-3931-a0a5-cb7fa0ec9b65 | -23.65106 | -46.29359 | 2025-08-24 03:47:00 | NOAA-20 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 05ce1bbb-1a5c-31c7-9bac-ada1a360cd5e | -22.28284 | -42.58671 | 2025-08-24 03:47:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 006713cc-2385-31fc-b05a-cc51700fd331 | -20.39738 | -41.40082 | 2025-08-24 03:47:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 86072778-78d6-31a9-a8aa-1091b5a2d36c | -20.35305 | -51.68552 | 2025-08-24 03:47:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 18.6 |
| cd211c7c-6862-34c4-85be-51c8f0896832 | -20.11913 | -45.36756 | 2025-08-24 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a5edb1bd-b8fe-344f-a5cd-032c8be24561 | -23.65427 | -46.50197 | 2025-08-24 03:47:00 | NOAA-20 | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d0fe3467-abf8-3cd2-a224-5998a92e24f0 | -19.60669 | -47.60688 | 2025-08-24 03:47:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 934038fa-8049-3ffd-be0f-b676a297905b | -20.08562 | -46.10863 | 2025-08-24 03:47:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb4c4968-6408-3186-9126-c38dd800b4a6 | -23.26264 | -46.62697 | 2025-08-24 03:47:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d1d82eae-2d1e-3d2c-b18d-c229f0c7cf9c | -20.52061 | -42.19868 | 2025-08-24 03:47:00 | NOAA-20 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6c22f9c0-92df-3f99-9574-fb7aeb51b40b | -23.3707 | -46.86215 | 2025-08-24 03:47:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 1f95fe2d-1765-317a-86f4-dcc81b4f34ab | -23.10034 | -45.79913 | 2025-08-24 03:47:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f2985ee1-1290-32f3-a9d4-53096975432b | -20.08685 | -47.76112 | 2025-08-24 03:47:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c60747a7-284b-35f7-af2a-94bd65d671bc | -21.54681 | -44.1735 | 2025-08-24 03:47:00 | NOAA-20 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a3eda1b-d2b0-36e6-aa31-a319ca5b334d | -22.14296 | -43.65798 | 2025-08-24 03:47:00 | NOAA-20 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| ca4d9259-1ca1-3c84-a1be-f3287a452fa2 | -21.27015 | -43.04568 | 2025-08-24 03:47:00 | NOAA-20 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d0858fd0-be99-3711-8beb-59eeb3e046e2 | -20.36708 | -46.74328 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8c86812-bb05-316d-9b52-f21d668eb62b | -20.09198 | -47.76238 | 2025-08-24 03:47:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10ebcbd0-8ecb-37b8-ba28-8a01dc9f09dc | -23.32342 | -47.8481 | 2025-08-24 03:47:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 22c2c09e-9763-3d7a-aa70-7de0646ca733 | -20.36819 | -46.73781 | 2025-08-24 03:47:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f79dd74-1553-3642-895a-448f1f1288a2 | -9.1721 | -59.4823 | 2025-08-24 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 4a68fabc-d6f5-3acf-afdc-77a92c7f1214 | -11.5437 | -51.8454 | 2025-08-24 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| d4ef4377-035a-3b7b-b36a-d7de0bee7104 | -9.2184 | -60.7921 | 2025-08-24 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ffd24fbe-4b53-3ddf-9de6-0945ff8e6b1f | -11.5247 | -51.8474 | 2025-08-24 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 87233b26-2df5-3a50-aa08-beabce326b70 | -14.2941 | -58.4849 | 2025-08-24 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0393162d-028d-3902-ab6d-ffd040a956e3 | -9.0231 | -65.7169 | 2025-08-24 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 26d1213d-dee3-34cb-8fbd-5761853d5a3c | -11.5245 | -51.8685 | 2025-08-24 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5b737ab8-5c27-3ba6-8a72-eca29252ff14 | -20.339 | -51.7062 | 2025-08-24 03:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cbe191fd-0674-3369-b837-673ead9578bf | -5.4364 | -60.1779 | 2025-08-24 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3f7edca1-e4b2-37b4-9aa8-acb73238835d | -9.1722 | -59.4629 | 2025-08-24 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 33364467-1578-3ee5-b555-80af3c9918ac | -14.2939 | -58.5049 | 2025-08-24 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| cdfcd95b-f05f-32d6-ab88-abb483f73cd5 | -9.0046 | -65.6988 | 2025-08-24 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 46a139a8-1bd7-35ab-a799-da569c8278cb | -11.5434 | -51.8665 | 2025-08-24 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 98e5088d-6d95-319f-a588-f9e831b9e7b6 | -8.6131 | -62.5929 | 2025-08-24 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c4ae0c0f-1202-34be-99cb-ff4ad4c5a1b5 | -9.1535 | -59.4834 | 2025-08-24 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 642fa43e-623e-3d09-8be6-4059b91ace35 | -20.3594 | -51.7023 | 2025-08-24 03:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c50bdde1-78af-339c-b01c-1896d205ecb3 | -9.1536 | -59.464 | 2025-08-24 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 218931f2-e941-3354-97ab-11c751d642ce | -9.1998 | -60.793 | 2025-08-24 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| dc6d41d6-4b61-3e38-b139-b7cc12f18aec | -20.3396 | -51.6839 | 2025-08-24 03:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 73.1 |
| fdf4c5e2-0b13-3e21-877e-097b9657c839 | -9.0232 | -65.6982 | 2025-08-24 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 743579ee-1b36-3bc7-91f3-911ddbe712c6 | -20.3599 | -51.68 | 2025-08-24 03:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5b9a210c-ac00-3eb9-ba93-6f9a27375997 | -9.1535 | -59.4834 | 2025-08-24 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 8c38c726-f45f-3dea-9be4-70bbfcc63c0d | -11.5247 | -51.8474 | 2025-08-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1c5ce176-9a5a-3859-a422-f63e0b04932c | -9.1998 | -60.793 | 2025-08-24 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f55fd79c-b223-32d9-96d1-1797ff1af6e1 | -9.1536 | -59.464 | 2025-08-24 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| c433a06b-eccc-330f-baa6-db824d6ed1c4 | -9.1721 | -59.4823 | 2025-08-24 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7dcd3628-fe3e-3651-8123-e4c1039baf94 | -9.0231 | -65.7169 | 2025-08-24 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d1dda737-b262-3cd6-9a06-10e419f341fd | -5.4364 | -60.1779 | 2025-08-24 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 0fcf3eee-30d8-378d-baf1-2bd227915914 | -9.0232 | -65.6982 | 2025-08-24 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| e6fa71f8-65ad-3b93-8895-34a32000f086 | -11.5437 | -51.8454 | 2025-08-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9c4a22e0-6a05-3f6b-b748-44f34759df7a | -8.6131 | -62.5929 | 2025-08-24 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6fff93b0-78d9-395f-ba63-ffd7e1fba127 | -9.0046 | -65.6988 | 2025-08-24 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c1cbcc77-2e63-33ca-93d7-01e23c5181b3 | -11.5434 | -51.8665 | 2025-08-24 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4b7693ba-b4bd-3ccf-8561-b5b292616d67 | -9.1722 | -59.4629 | 2025-08-24 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 31ec03ff-ece8-310e-a224-bac1fa2d8214 | -14.2941 | -58.4849 | 2025-08-24 04:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 33a28e06-952e-390c-a2cc-27e2c455dcc7 | -9.1536 | -59.464 | 2025-08-24 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 3e975f9c-bf28-3048-bfc4-1fad0ffbec09 | -9.0046 | -65.6988 | 2025-08-24 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1797166c-d893-381f-a7fe-97d285cd3894 | -4.9605 | -55.8226 | 2025-08-24 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 284b05e3-6d57-36d7-929e-64ba97e85937 | -9.1535 | -59.4834 | 2025-08-24 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| ee059da6-d836-3208-b707-0159f74e4ead | -9.1998 | -60.793 | 2025-08-24 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 966ce103-be03-3672-873b-e107a1f43815 | -10.4164 | -47.1732 | 2025-08-24 04:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d217c6d2-5a82-3ec0-bac5-afff3d1d5368 | -9.1722 | -59.4629 | 2025-08-24 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 476fe3e9-ce13-3f2f-bfbc-62a5181bb812 | -11.5437 | -51.8454 | 2025-08-24 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.9 |
| f55ff4d5-3e78-3aa8-a7ba-fc2241f3cb3d | -11.5245 | -51.8685 | 2025-08-24 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 41e76a70-5d74-37e7-97dc-3a6277d3457a | -9.1721 | -59.4823 | 2025-08-24 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 56160064-b35a-3685-96e6-ea7cdecb24fc | -11.5247 | -51.8474 | 2025-08-24 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 835c21a9-00d8-3949-9153-fbc5639a6967 | -11.5434 | -51.8665 | 2025-08-24 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| dfa48ddb-6473-3289-b60b-551882f8839c | -8.6131 | -62.5929 | 2025-08-24 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| da3491bf-0a95-3feb-8ac7-db1d21fed07e | -9.0231 | -65.7169 | 2025-08-24 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9a5e7d90-2fbb-334d-9308-893d03b242b6 | -9.0232 | -65.6982 | 2025-08-24 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c171140b-1e54-333a-8469-821b717140f1 | -4.9605 | -55.8226 | 2025-08-24 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d113dcba-6eab-3e3a-83cb-ec9d57e3da32 | -11.5245 | -51.8685 | 2025-08-24 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ef7cbcab-3fa3-37eb-ba2d-2d7b66b175a1 | -9.0046 | -65.6988 | 2025-08-24 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 368a944b-6477-348c-ad4f-2b88a771af98 | -9.1721 | -59.4823 | 2025-08-24 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9dcc48df-93be-38a9-9100-21dd87fd76fb | -9.1998 | -60.793 | 2025-08-24 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 44fc5a3e-a1a5-3b8d-b0aa-f0dc9d5403f3 | -11.5434 | -51.8665 | 2025-08-24 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7f0b2c39-a4af-3e6d-8852-49f0b1aa6fc1 | -10.4164 | -47.1732 | 2025-08-24 04:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 65dd09c4-47a4-3029-bd74-949f1f609980 | -9.1536 | -59.464 | 2025-08-24 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 275cd13c-cd70-39cc-ac04-47704118cd8a | -9.1535 | -59.4834 | 2025-08-24 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 8ef65def-5529-31d8-9b2f-96f530d6e32e | -9.0231 | -65.7169 | 2025-08-24 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| eb287590-d234-32d7-a73b-9156a265bbc2 | -9.0232 | -65.6982 | 2025-08-24 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 994ac464-57b3-38b2-94a2-bef070740f00 | -11.5247 | -51.8474 | 2025-08-24 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| cc1a1008-eb70-3bc0-9d81-09fbd8d79cd3 | -9.1722 | -59.4629 | 2025-08-24 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 1f5e07bb-ed6c-3fd7-8486-0f87ce32b247 | -11.5437 | -51.8454 | 2025-08-24 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| be79a7ad-ac08-3f63-934a-25ec90627baf | -5.7431 | -57.5814 | 2025-08-24 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e746434d-e417-3098-901a-3ae81152e5cf | -10.6131 | -44.3051 | 2025-08-24 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6a23abbc-cc8e-360b-bbb2-10f125971913 | -8.6131 | -62.5929 | 2025-08-24 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b13b394b-f192-3546-b407-af86c9bb843c | -4.9605 | -55.8226 | 2025-08-24 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |


[Clique aqui para ver as próximas entradas](README32.md)
