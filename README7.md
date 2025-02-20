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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 475513d6-0f04-32f8-b0de-df5048a9a62f | -20.23728 | -46.46569 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18058c35-2efe-39f3-8b86-062566df7308 | -20.21113 | -46.51512 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f965a4cd-644e-3a47-9bbc-9e2f0420233f | -20.20759 | -46.49825 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86d8425f-590d-314b-a166-b6c08a90905d | -20.21571 | -46.52219 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ea229ef-147d-3b5b-adce-663578b7556e | -12.40944 | -63.99656 | 2025-02-20 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a89f02d-9515-386d-bfcf-234ea1bf8536 | -11.94617 | -63.95024 | 2025-02-20 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e75cbc0-48c4-3b73-8297-53a8444c4aa1 | -11.94663 | -63.94862 | 2025-02-20 06:09:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d060dd-ab6a-3129-9c05-acc51a978681 | -20.2363 | -46.4447 | 2025-02-20 11:30:00 | GOES-16 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 2cb6a2f9-8d57-375a-b12e-8692c7622d3c | -20.2363 | -46.4447 | 2025-02-20 11:40:00 | GOES-16 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 159.9 |
| d4e9e55a-d6fb-3a30-a3f6-2a90765b9ac7 | -20.2363 | -46.4447 | 2025-02-20 11:50:00 | GOES-16 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 196.7 |
| c6cea8b3-754a-3cfc-a1a1-a8645f132d4f | -12.8033 | -45.0239 | 2025-02-20 11:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a402180c-7ff8-301f-809d-3b3cdcb83373 | -17.0609 | -45.043 | 2025-02-20 12:00:00 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 100.0 |
| ab96a538-7c94-3aae-8b3d-4d91b4a5c6dc | -20.2363 | -46.4447 | 2025-02-20 12:00:00 | GOES-16 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 5d14d85f-9bdf-3a4e-90cd-5276e4211ebb | -20.2363 | -46.4447 | 2025-02-20 12:10:00 | GOES-16 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 158.4 |
| e907af30-2462-3086-ab7b-e1a36d827b20 | -17.0609 | -45.043 | 2025-02-20 12:10:00 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |
| acd95e4f-ccf3-3e6f-ad42-638e2cff4957 | -20.2363 | -46.4447 | 2025-02-20 12:30:00 | GOES-16 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 8089f715-1199-3e74-965e-0bc64266a67e | -14.47256 | -45.81109 | 2025-02-20 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bdc8901a-5d65-34bf-8420-82f7aa93fcba | -12.82197 | -45.01918 | 2025-02-20 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 14f4083f-6d39-32bf-b65f-7bb1a5a9024a | -14.62227 | -52.40677 | 2025-02-20 12:38:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c335c8b2-23c2-318d-b7b3-4eb1c8e99503 | -12.9483 | -45.60463 | 2025-02-20 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 00e09d17-f5f8-3265-9ba0-b9e02143e079 | -14.44985 | -45.83128 | 2025-02-20 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| db5db035-90b6-359f-a4d6-ed2424deafa2 | -10.54085 | -45.22024 | 2025-02-20 12:38:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a7f9247-8880-3822-a33b-2b4ab490bcc9 | -12.81179 | -45.01793 | 2025-02-20 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 3e071b60-cd01-3995-ab67-d6b5930ec503 | -14.44148 | -45.81855 | 2025-02-20 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0d4df573-e551-3958-9c81-433beee263e2 | -8.85717 | -44.73634 | 2025-02-20 12:38:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0e3ad6b4-c47e-3068-b783-f7aa6cc6dc9e | -14.47407 | -45.79964 | 2025-02-20 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 15045bae-f801-3df4-aa23-a9b633d4c0f0 | -8.53086 | -44.74054 | 2025-02-20 12:38:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 45bb6cec-a68a-32a9-ac62-f05303cf2335 | -14.15026 | -50.2556 | 2025-02-20 12:38:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 586f85dc-70c6-3e16-9001-6a14d9bc189f | -13.43382 | -43.90805 | 2025-02-20 12:38:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ceee8070-b47d-370a-b573-1d6d4cd97216 | -14.45134 | -45.81986 | 2025-02-20 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| fb43c431-05ed-3880-957d-174f7900294b | -8.84736 | -44.73504 | 2025-02-20 12:38:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| dbfe6171-f77c-37fb-845c-f6e0f5b7c9c1 | -12.69804 | -44.94719 | 2025-02-20 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0a881516-57df-3ddc-b3b8-ab5452a82efa | -14.11404 | -45.66785 | 2025-02-20 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b44da3ad-0f14-3031-9a0e-4d1230eedb61 | -10.53151 | -44.66945 | 2025-02-20 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c843582b-f26d-328e-8795-b842158946cb | -11.72501 | -48.81498 | 2025-02-20 12:38:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5dafdbe9-62aa-305c-80ae-5ae8de3f630d | -12.81335 | -45.00589 | 2025-02-20 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 1945eabb-ee47-3668-ad9b-47168e07f71b | -24.77436 | -51.13298 | 2025-02-20 12:40:00 | TERRA_M-T | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 208129a9-f115-396c-895a-cbe76f47469e | -19.52677 | -53.37343 | 2025-02-20 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d5af4d2a-10f8-36b6-a91a-fbedad4b34fb | -19.91416 | -48.06769 | 2025-02-20 12:40:00 | TERRA_M-T | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1352aabc-6c22-3278-bf9b-1e8f0d6eac35 | -19.9865 | -51.27025 | 2025-02-20 12:40:00 | TERRA_M-T | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2f7a6403-9280-3514-bb08-98c0002e410a | -20.3421 | -53.6648 | 2025-02-20 12:40:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8a9bec1e-cdec-3c2f-a0d3-bcbbcb63a6ec | -20.23952 | -46.45451 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8738623b-c6f9-318a-8b0a-558f4b6cae56 | -21.23716 | -45.75598 | 2025-02-20 12:40:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 636409e5-eb72-3a39-a795-c6f3c13757fb | -18.72833 | -46.81311 | 2025-02-20 12:40:00 | TERRA_M-T | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 85782a5f-defc-3831-ab14-5638032072f7 | -21.895 | -45.59233 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| a8d7e402-0934-3e12-b24d-8cacffb4f857 | -20.23079 | -46.44073 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| e06cdbe9-cda9-3702-9c05-49db1f57a267 | -17.05654 | -45.0476 | 2025-02-20 12:40:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 123.2 |
| c3a11845-8ec7-3519-9035-ae05994bad4a | -17.05828 | -45.03357 | 2025-02-20 12:40:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 68fb7dc4-88b3-36c7-b41e-c0a53e6fa878 | -20.3389 | -45.43037 | 2025-02-20 12:40:00 | TERRA_M-T | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| de61d9f1-f259-3dab-96dd-cffed6827d8d | -20.30534 | -46.4951 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d0ef87ff-72e4-331b-b3f9-763c89aa2e87 | -19.98505 | -51.27994 | 2025-02-20 12:40:00 | TERRA_M-T | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 223427a3-cf99-34ef-8adf-6638e650ff53 | -19.90636 | -52.73943 | 2025-02-20 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d50d83b9-02e1-35d3-b7f9-7101f66d9378 | -20.24106 | -46.44191 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 200024ba-77a5-3e75-873a-9bd115798115 | -19.29849 | -52.80615 | 2025-02-20 12:40:00 | TERRA_M-T | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3ac738d8-19c1-3c70-93dd-8c16a75c4e61 | -20.21142 | -46.51495 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a8e563c2-18db-38d5-93ba-1720b7723a10 | -20.22924 | -46.45354 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 0d5ea9c1-a8be-3e01-a1a3-b3e6e23f19e6 | -20.22162 | -46.5162 | 2025-02-20 12:40:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ecf09c58-0caf-39e6-84b5-51588e6d3e7d | -23.02964 | -48.75192 | 2025-02-20 12:40:00 | TERRA_M-T | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a50b9711-c5ff-3ec2-8ae9-41ce4c7660c9 | -30.59349 | -52.76667 | 2025-02-20 12:42:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 5.9 |
| 01896b61-f270-340f-bf3f-ac01d2bdb339 | -30.59498 | -52.75642 | 2025-02-20 12:42:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 20.0 |
| c327e64b-df3a-382e-8c9f-0fa28f243452 | -12.8037 | -45.0006 | 2025-02-20 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e8d7b2c1-e719-36c4-a497-5a991cb82060 | -12.8033 | -45.0239 | 2025-02-20 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4807e3a7-25ed-37c3-94a6-a1a5f17a3190 | -12.8033 | -45.0239 | 2025-02-20 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 915b8a14-ee4d-38e7-9540-65aba38eef39 | -12.8037 | -45.0006 | 2025-02-20 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 74fa689b-0b6d-38ad-8408-46c625f239fa | -12.8037 | -45.0006 | 2025-02-20 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d35c0ff6-dcf9-3391-a6b2-d348aeb0ef31 | -12.8033 | -45.0239 | 2025-02-20 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 619dfa89-1ae4-37c9-be79-58e8ad512f2a | -12.8037 | -45.0006 | 2025-02-20 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 0602c68b-8dca-352a-b7ce-fae12c1232b0 | -12.8033 | -45.0239 | 2025-02-20 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a86e8f92-449f-38d9-92aa-f83c35ac4685 | -12.8037 | -45.0006 | 2025-02-20 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c5c20226-8e04-362a-85fd-7cb62d0f1ea7 | -12.8037 | -45.0006 | 2025-02-20 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 85f387d9-1d55-3c6b-adba-1aee97cb9c65 | -12.8033 | -45.0239 | 2025-02-20 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 94f2639b-0897-31d0-97e8-21817dec063e | -12.8037 | -45.0006 | 2025-02-20 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7d330b4c-f7b4-33a2-925e-075ee731240d | -12.823 | -44.9975 | 2025-02-20 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 981b7415-5c30-3062-8984-669b17f5c656 | -12.8226 | -45.0208 | 2025-02-20 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f501d2d5-e693-3b19-817f-660fa03864cf | -12.8037 | -45.0006 | 2025-02-20 14:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |


