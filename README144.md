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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 955bb5de-4250-36df-88e0-db0d5222f893 | -17.20452 | -43.53894 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ea74e30e-cd23-30eb-9eea-3edc486844f3 | -16.05804 | -39.85025 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 9b61357e-2975-348a-850c-df7c789464c7 | -19.49367 | -44.92487 | 2026-10-07 15:58:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d72e82c2-9f2e-34d7-9bfc-29aea15e52b1 | -14.92935 | -41.10252 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3889e496-5ae5-3c51-95d1-c1d529a889d2 | -15.72374 | -43.27531 | 2026-10-07 15:58:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3d4fa6df-ea5f-3665-9803-ec224027329d | -14.323 | -40.52027 | 2026-10-07 15:58:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0818a25d-424d-3501-b3bb-b9e080ffc902 | -14.1526 | -42.18435 | 2026-10-07 15:58:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| d706b299-1b39-377a-9c60-6b11d69a99bf | -17.02196 | -41.03055 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b10b6fd8-90df-33b0-8ddf-4003ac00fef7 | -17.5264 | -45.46946 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b2df7560-46b7-397f-84b2-51fa8d0257cf | -16.00529 | -44.10331 | 2026-10-07 15:58:00 | NOAA-21 | PATIS | MINAS GERAIS | Brasil | 3147956 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 510a6320-202a-30f4-ba92-a95daca95613 | -14.41287 | -41.33889 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 310.7 |
| b50397f9-cc0b-3ab0-bee2-f6f802543a0c | -15.63665 | -41.69908 | 2026-10-07 15:58:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.8 |
| ef592802-a57b-369c-8b3a-1d058167863c | -15.63614 | -41.69506 | 2026-10-07 15:58:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| c329192b-047c-30f3-9a4e-e568e5a3a2f4 | -16.143 | -43.5225 | 2026-10-07 15:58:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 2ae6afb1-aa8f-3ea4-843e-7290c951d7da | -15.96793 | -40.70502 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 6090dfe4-2bd8-3926-bd6e-1ba6315a53ae | -18.04652 | -44.58181 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2b810bc9-164e-3b4b-9077-3720340eed01 | -18.04728 | -44.58878 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 68d29dc0-65ec-3b48-ada7-68068f7b3882 | -18.54815 | -44.01337 | 2026-10-07 15:58:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d48b70cb-c395-32aa-90e2-c200f552c476 | -16.04674 | -39.85178 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| dbaa16e8-a5a1-3f1e-9b3a-4e6ec679bcdc | -16.85485 | -40.58952 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b0ccdf6e-492e-3842-8d7a-7f8d24d57a2d | -15.53677 | -41.24183 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| bbda95f6-ba7d-34d4-a7f5-003f9ae75ee0 | -17.01392 | -45.90435 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c9527d22-df85-34bb-bda2-75d1c584087f | -14.96609 | -40.28113 | 2026-10-07 15:58:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 98250e5f-a3a2-3a27-a9c3-3d75209d4902 | -15.53724 | -41.24548 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 6e2d5db4-6a25-366f-ac1f-aec5652d5a45 | -15.94846 | -40.26445 | 2026-10-07 15:58:00 | NOAA-21 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 256816a0-d50b-349b-b039-67faedc3b5d0 | -16.20452 | -42.26195 | 2026-10-07 15:58:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a3321b97-c2b8-330d-bc64-4ccc9806e876 | -14.39294 | -41.37466 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 129.2 |
| e808ff51-fddc-3a28-8bf1-31c301c9fec4 | -15.55086 | -41.4771 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0af98788-2a66-3159-8e1e-3e1e838b7f43 | -15.11327 | -43.62638 | 2026-10-07 15:58:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 5734be5e-e64a-3d03-ab59-2e4720f61270 | -16.47297 | -41.81554 | 2026-10-07 15:58:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e9a8e46b-8841-3f32-881b-6f9b9a194e7a | -18.04096 | -44.57955 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 262272b3-c28a-3dbd-a4ac-a7638adf200c | -14.88648 | -42.36487 | 2026-10-07 15:58:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 44a0ed10-99ae-3a27-ac90-b2ab1c2ed99c | -15.81232 | -43.93903 | 2026-10-07 15:58:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5f820e04-b7f7-35c2-948c-d25fb880c2d9 | -18.9983 | -39.80174 | 2026-10-07 15:58:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 12aee17e-c3aa-33ab-a6ce-6a15bcfb9055 | -19.01623 | -39.87815 | 2026-10-07 15:58:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f3801248-4aab-3226-8e0a-070b7b91b72e | -16.05742 | -39.84563 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 1565c7da-96b1-3f18-babb-916ad406af5b | -15.21263 | -41.49103 | 2026-10-07 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| cf2fc7fa-a125-314b-8da8-367229175e9c | -17.13214 | -40.91864 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 80431430-ff77-3d70-b8b6-86d1ea77fb11 | -14.75283 | -41.82325 | 2026-10-07 15:58:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b821160b-efb0-3b76-b0bc-e04d5c3e4c38 | -18.0354 | -44.57731 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5a8579fe-2653-3cc3-9eb9-a71120e0f81e | -17.02651 | -45.91509 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c9c1dfd4-7e17-3ad0-a33e-063163b6ec13 | -14.43248 | -41.1297 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 33f8edb2-393d-3858-9d3c-b684fa66ba75 | -16.85151 | -40.59504 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| c6fab1ec-a973-311c-b3c4-6e5c20571915 | -14.35976 | -41.27666 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 104.8 |
| eb2a297e-759e-3b0e-aea4-f4ab16acfee7 | -16.00408 | -44.1043 | 2026-10-07 15:58:00 | NOAA-21 | PATIS | MINAS GERAIS | Brasil | 3147956 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a6e25d90-d848-3696-906b-d5ed677d55c6 | -16.85883 | -40.58899 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.9 |
| 48a9323e-9be3-379a-951a-a16ccb8283e7 | -15.99899 | -38.9227 | 2026-10-07 15:58:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 7edd34da-3b01-3df1-9ef6-58ad917b8e44 | -16.05556 | -39.86026 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 09753d0f-c116-3764-acfb-8e6ae11ce5de | -16.24339 | -41.79872 | 2026-10-07 15:58:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 34379ab9-d5e8-3736-b0ed-71fb9b960bbc | -16.89956 | -40.88019 | 2026-10-07 15:58:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 20f827c3-ab92-3f75-b2ab-c0f29e498be6 | -16.03789 | -41.33587 | 2026-10-07 15:58:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 71f4af51-2b66-3adb-ba60-82828f73689d | -15.9672 | -40.69954 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 67987fe8-87ec-3c93-b131-ae98fb63eafc | -16.05114 | -39.85594 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 6fe83049-df59-31bd-9f56-34b2fffecf79 | -14.90651 | -48.7642 | 2026-10-07 15:58:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 06f15e4b-37e7-377e-94d6-8b811ba80071 | -14.40935 | -41.72882 | 2026-10-07 15:58:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 45c51fd9-e761-36cd-a82f-2b64bb3f5138 | -15.39202 | -41.70283 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.3 |
| e8840a93-2166-317d-bab1-963ba4b67753 | -18.18207 | -42.34697 | 2026-10-07 15:58:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 5319946f-c433-35b5-b74b-d1a3b03afa8e | -15.54674 | -41.47767 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 02a57aba-4d4b-329b-8a0f-f26772ce3cbd | -14.58058 | -40.73821 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 656d5501-61ef-377b-8391-64ebb1283d79 | -15.11067 | -48.50497 | 2026-10-07 15:58:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ae7f1b7-9aba-3831-8efe-21defe242f79 | -15.89597 | -44.5249 | 2026-10-07 15:58:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff6bf585-ff33-3a08-8541-49e082524187 | -16.0549 | -39.85543 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| b1fc55f5-8bb5-3a43-89d3-c1d99972adda | -14.43744 | -42.28844 | 2026-10-07 15:58:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| afb95b62-dcff-35b7-8991-2339e40446ec | -15.66825 | -39.70296 | 2026-10-07 15:58:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 926dbedd-a989-3f8c-be6f-8ee8f67a75c1 | -16.05051 | -39.85127 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 103dad99-b98c-3c2f-9fcf-760d42fe13d4 | -14.79178 | -41.96262 | 2026-10-07 15:58:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a4f4320e-c973-3d42-84d8-fc2870b100c8 | -14.67445 | -40.80949 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 4c5718bd-1e1e-356a-9101-504a712c9e05 | -16.85577 | -40.58579 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 772fd0c4-81f4-32b0-b808-8cf5353d0029 | -18.38573 | -40.31712 | 2026-10-07 15:58:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 4dcb27de-0d85-39bb-a5eb-6580cd31665c | -16.84846 | -40.59165 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| cf0fdeda-37bc-3669-9e86-7efcd407b4e2 | -16.20402 | -42.26151 | 2026-10-07 15:58:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c41104ab-e197-3b31-b2b4-0a16ff8f92db | -16.45414 | -41.06004 | 2026-10-07 15:58:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| cabf4a8e-db93-3f2e-9332-9e04fa791ca1 | -14.21486 | -42.75572 | 2026-10-07 15:58:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a63d9dad-2163-3fc5-92ff-5275f5489547 | -16.13761 | -43.5177 | 2026-10-07 15:58:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ea15974e-2c25-3dd9-b375-e4f8b03b4aaa | -17.02736 | -45.92306 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 205.6 |
| b9c916f0-58ad-3d1f-8a24-9857896c6864 | -17.79199 | -44.44455 | 2026-10-07 15:58:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab113d12-345a-3d96-8034-10f7ef4b2c8d | -14.75113 | -41.82287 | 2026-10-07 15:58:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 10890b87-2952-3429-bf2e-7567857cdd90 | -16.9325 | -42.10636 | 2026-10-07 15:58:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 6aa01f6c-dd54-37d7-9c2b-68570da1189f | -14.36172 | -40.37987 | 2026-10-07 15:58:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 11c1756b-cdec-3493-a75b-cd9d05c6743c | -15.39754 | -46.1159 | 2026-10-07 15:58:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 27022740-9931-3c7b-80ef-f9d8ee076353 | -17.14747 | -43.85279 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34ae130d-dfa7-3b43-9ec7-717956fe45eb | -14.21461 | -42.75394 | 2026-10-07 15:58:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f733a44e-d59e-3364-8a2e-5bf34eddcc48 | -15.39569 | -41.69826 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.3 |
| 623ff8c3-4d9a-3fbe-bace-dddcf0d1012b | -15.69411 | -41.05283 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ef8bb962-8069-33ba-be91-6868b0db809e | -14.79442 | -47.13219 | 2026-10-07 15:58:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bbf17a8f-be86-3e7a-a87d-df2c01406956 | -14.38842 | -41.37151 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 2789729f-4baf-37ba-ba8d-84682bf77d3b | -15.4652 | -41.20304 | 2026-10-07 15:58:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3ed11083-7dc1-3601-a6ad-99a141e8e7e8 | -15.44915 | -43.95762 | 2026-10-07 15:58:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 364805ea-ac8d-3c87-9f76-b96c46cc4d38 | -14.94177 | -45.45393 | 2026-10-07 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b8f983e2-cbea-32f6-b74e-30c46577aed6 | -14.35321 | -41.36162 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 79d7b56f-6ddc-3b92-8519-03dad9e36ea0 | -17.20567 | -40.80928 | 2026-10-07 15:58:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 0cd7a1c5-608a-3d92-b659-0fe944c90d4b | -14.4108 | -41.72783 | 2026-10-07 15:58:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5a4ee539-5f1b-3b25-9be1-905bf449f467 | -16.86922 | -45.22404 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 72d4c675-6e1d-3bc7-b22f-89443c8054b5 | -17.76755 | -42.70467 | 2026-10-07 15:58:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d91ddb90-9d83-365b-b7e5-68e8fc76ca02 | -17.01925 | -41.03906 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 215aafd6-b519-371b-affa-ef5dec6c17e6 | -14.80037 | -47.13157 | 2026-10-07 15:58:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 333b51f8-adaf-35d7-90cf-c7d10d193a17 | -15.96329 | -40.70035 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 1e2cbe42-e26c-34d2-ae24-ff1818f2bc49 | -18.04024 | -44.57299 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c7832d6a-0a77-306b-9791-42cd2c705590 | -16.19018 | -44.56673 | 2026-10-07 15:58:00 | NOAA-21 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 32.3 |
| e27a4753-a030-3cec-a2e4-8e0d424a0f0c | -18.54659 | -44.01429 | 2026-10-07 15:58:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README145.md)
