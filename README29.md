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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57b78211-c3dd-3e5c-825c-203848b027d0 | -11.63106 | -46.54969 | 2026-08-21 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4270ad47-851f-3457-b0b7-63cc066a3531 | -13.44059 | -51.81347 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0e4d5c6-d27b-336f-a216-2e990baa5d7c | -13.39297 | -54.38446 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7e1c4f75-6da9-3d33-865f-665731e6e3dc | -9.01416 | -40.99425 | 2026-08-21 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48b0a949-017e-3452-b012-9fe1643f0061 | -11.0061 | -45.21578 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62d8a148-0494-392a-b0c2-c610c9a9b039 | -12.84662 | -48.44589 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 794bdb7d-25f0-30f6-ab41-eb97694ffc74 | -10.72809 | -44.78507 | 2026-08-21 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b92c471c-39b4-37a1-8428-414637179aa0 | -14.45856 | -45.61577 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba54f177-6723-300d-a3f8-413a2d0c176f | -13.39248 | -54.36984 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4e3d992e-a32a-326f-b69e-e0e0e015f9c5 | -14.90291 | -44.80754 | 2026-08-21 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c69dce16-3c87-34d7-a468-29255feaff5d | -14.30759 | -51.8945 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0edf18ce-e66f-31d3-a93b-c8ac4ca4e170 | -22.66066 | -42.80554 | 2026-08-21 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0514b4d-d3e2-3975-9978-831d58f5d225 | -14.24322 | -52.14128 | 2026-08-21 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 094e9115-2fad-337b-ac49-f7b6036cddd9 | -18.87131 | -42.0275 | 2026-08-21 04:04:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7dd05996-0398-30a9-9198-85270ecb5b02 | -21.57767 | -43.47997 | 2026-08-21 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b5edf308-f01e-3a1a-aa99-3f82d430a156 | -20.25966 | -46.73394 | 2026-08-21 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11f4d82e-6911-3371-a7c3-2bc1753deef8 | -17.97286 | -44.42729 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6c2482c-0d34-36d3-bb2b-77065c6d4db6 | -19.85949 | -41.08608 | 2026-08-21 04:04:00 | NOAA-20 | LARANJA DA TERRA | ESPÍRITO SANTO | Brasil | 3203163 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2f1e960c-7e25-35f7-b39b-bf762838d396 | -20.28267 | -46.74148 | 2026-08-21 04:04:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4da1286-bfad-342d-b76a-c9d24c771d67 | -18.98218 | -47.03398 | 2026-08-21 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeece1e4-3f5e-3533-856b-b38bc3347fa1 | -18.87677 | -42.03597 | 2026-08-21 04:04:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 099e9d7c-8cf3-3939-859e-f766ab121ab8 | -20.83163 | -44.19227 | 2026-08-21 04:04:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 09369a26-c435-33fe-8550-46c6834af59d | -19.66307 | -46.04442 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 18ae0242-3d80-3668-bba1-89d989c45d71 | -14.30065 | -51.8311 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 334bbb65-3a4e-360d-b9ba-61c892d127c7 | -14.32886 | -51.9133 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6d81377-0bd0-37ab-a899-81c2775df3b9 | -15.7602 | -47.7714 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76e8c25f-c964-388f-b394-6396ee11999c | -16.21202 | -43.50028 | 2026-08-21 04:04:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8b8d8a4-9706-3c6a-951e-4c8ff3e614bf | -15.71281 | -47.79331 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 004d5c39-6c14-3506-96a6-2742fbf62310 | -21.57494 | -43.47553 | 2026-08-21 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 09514bdb-4d41-315d-84ff-c92ce4c65612 | -20.78288 | -45.09834 | 2026-08-21 04:04:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a26d3035-646a-3ad1-93e1-44abd5df5d5d | -18.02707 | -44.61246 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46136ce9-d05d-3c3c-ba33-d858d0668450 | -13.93403 | -53.85691 | 2026-08-21 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b6dbb2f8-c45d-3eab-919b-a3d6a77f60aa | -22.38187 | -43.01999 | 2026-08-21 04:04:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 895ad222-35f4-3aa4-8612-6134a6ae7740 | -18.65783 | -43.58765 | 2026-08-21 04:04:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 84f8129f-ca2f-3c59-a4e7-d923ead07445 | -19.85185 | -43.87655 | 2026-08-21 04:04:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| fc598613-f5a0-3807-bff5-ba344b6247f7 | -20.96633 | -44.61202 | 2026-08-21 04:04:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a3c6910c-c328-3410-884d-5b00101c6d4a | -18.65625 | -43.17964 | 2026-08-21 04:04:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ec1189bd-a371-3a97-aa14-3ac2bd475b87 | -22.17678 | -48.73112 | 2026-08-21 04:04:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d4e7bf1f-d19a-3269-9288-6cb360b769ab | -17.33335 | -43.62878 | 2026-08-21 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c97f79a-7cdb-32a6-a343-a3d5ba9ae428 | -16.04893 | -52.17492 | 2026-08-21 04:04:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bb4febb-5f51-3052-8a03-1d681789bc4b | -14.34478 | -51.89748 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f83a3ff-2bda-3ae6-99c2-eaf81489dfff | -21.88522 | -41.47552 | 2026-08-21 04:04:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| bab7165a-0b9b-3193-9245-e884c316b159 | -18.02784 | -44.60809 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf4bfb5c-b308-3ae2-8195-528a1f4f0f94 | -17.95234 | -44.39641 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bba7693f-19ed-3897-91b9-5a94400b8d15 | -18.87463 | -42.02808 | 2026-08-21 04:04:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 33847ecc-25b2-342a-b8ad-8067416475b8 | -18.97812 | -47.03308 | 2026-08-21 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 858bbd7b-d704-38e7-abf3-d5411120a95c | -15.01268 | -52.67391 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02c0f62c-3630-374b-bae7-b38cc8097501 | -19.67156 | -46.04102 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5dcf4ba9-3659-39ea-aa97-48c3a15aa9b6 | -14.99906 | -52.67647 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00a56bf0-670e-3edd-946c-8d00bfce67c1 | -21.3657 | -44.13019 | 2026-08-21 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 003988d6-efdd-3341-86b2-852c8b0be1e9 | -21.10677 | -43.81429 | 2026-08-21 04:04:00 | NOAA-20 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4aae8d18-3abd-310c-9fad-28a2e73bc1c9 | -21.11017 | -43.81494 | 2026-08-21 04:04:00 | NOAA-20 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66d8b9ee-f829-346f-801e-31969933570e | -14.24222 | -52.14611 | 2026-08-21 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcc69b7b-00da-3295-8984-6777273b2cf5 | -14.31363 | -51.89574 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| b084963f-e4ca-37df-b4eb-26a42b2a7738 | -14.20365 | -52.88351 | 2026-08-21 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91437ca9-93f1-32bd-8807-43efaad24578 | -14.43785 | -51.8192 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6682b6bd-578a-305a-aa21-c7b74619e7f7 | -18.27312 | -43.32824 | 2026-08-21 04:04:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e701f768-f664-3e9b-9f17-6fe71b41563e | -18.87559 | -42.04329 | 2026-08-21 04:04:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 97853138-4fb3-3ea0-a70c-7ea1bfc03bb4 | -20.20222 | -41.56412 | 2026-08-21 04:04:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a1c0d72-6d44-342c-9700-369267052321 | -18.02499 | -44.60303 | 2026-08-21 04:04:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f6c4a7a-1f5d-3fa3-a441-62cf8f97a3d3 | -20.65913 | -46.19715 | 2026-08-21 04:04:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c992f0ba-533e-32dd-852a-f835adfb69af | -17.63325 | -42.32397 | 2026-08-21 04:04:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 64f23571-83ee-3102-9bac-daf2630f71b5 | -14.31066 | -51.9098 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 72d24e30-4bf0-3e5d-9637-c825fc159a4b | -19.67447 | -46.04673 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0be209a-1cc5-3778-a146-1787d1bd0a27 | -18.11317 | -43.73673 | 2026-08-21 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41745d9e-f428-3d13-a941-992cc511047a | -18.03574 | -46.46627 | 2026-08-21 04:04:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61cd4c1e-fd60-3611-9ad8-759078dffa9f | -19.8606 | -45.5291 | 2026-08-21 04:04:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 58ff4c04-6d39-33f9-bf60-3699b39b80d5 | -17.94877 | -44.39572 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2aee3fe2-6ea9-3123-a710-4cea1b273176 | -20.31169 | -47.21545 | 2026-08-21 04:04:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d825ccf2-9d81-3146-923d-bd614e67ef7a | -15.60164 | -46.5764 | 2026-08-21 04:04:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a046ebc-932b-3498-86e6-50c00c8fbb6b | -19.25617 | -44.37693 | 2026-08-21 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 040d0977-484e-3754-9b41-2fda03de8e5e | -18.88122 | -41.09012 | 2026-08-21 04:04:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c2694f7-b022-36f7-995e-63599554a09f | -17.33056 | -43.62404 | 2026-08-21 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc4312cb-8579-3dfc-874e-d2ac43959356 | -14.57116 | -52.9952 | 2026-08-21 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abcd43d3-6aba-3f12-b033-cf2c27c97836 | -13.94694 | -53.86606 | 2026-08-21 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da0b9763-089a-32fc-b813-8f42b3d59f90 | -14.99786 | -52.68201 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f62b106d-ff99-3b39-921f-fa3878bbe732 | -14.31672 | -51.911 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed827cca-804a-349e-8870-1803a590cd77 | -19.66509 | -46.05503 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61d6431a-ebf8-3763-96da-e9384f9d2f22 | -20.83094 | -44.19626 | 2026-08-21 04:04:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3f69a3e4-b1d8-3e75-b1d1-07cb71325d83 | -20.63773 | -41.20629 | 2026-08-21 04:04:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e698714-f4bd-3766-911c-1b6e998d7999 | -20.48386 | -43.40555 | 2026-08-21 04:04:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9b0ee0b1-b617-32f4-a1f6-9e29e920bca8 | -18.02991 | -44.6175 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6703c340-c820-3ec2-b034-105d56307dae | -20.62968 | -43.55872 | 2026-08-21 04:04:00 | NOAA-20 | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7f925298-7663-3390-885b-6b6f198c00cd | -20.04622 | -45.62482 | 2026-08-21 04:04:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c8e0fce-dcd5-3376-a919-57b9a8ba37f0 | -16.53397 | -41.24451 | 2026-08-21 04:04:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d65fdabc-483d-3806-ab56-5f46798261c4 | -20.29056 | -46.72081 | 2026-08-21 04:04:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c4348c1-4b50-3d17-a71a-4374bd257a05 | -22.38127 | -43.0237 | 2026-08-21 04:04:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 99d8a380-e71e-3d63-9f82-afea765db49e | -14.3056 | -51.90388 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02ac2a73-a93f-34d9-b304-8da0abc3eb4c | -17.82579 | -44.30669 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ee55b45-18dc-3869-b451-939f6cc127bd | -19.84263 | -43.16021 | 2026-08-21 04:04:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d8baaa93-9915-3e44-8002-09c74499ad09 | -14.99279 | -52.67527 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afa5bd68-f157-3fb1-96d7-e59e9b60311a | -15.00288 | -52.68902 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a76978b7-2eea-308d-b65b-c3684826eca4 | -19.93672 | -43.62778 | 2026-08-21 04:04:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04666926-156d-316c-82ca-c573084516f4 | -18.03173 | -46.46552 | 2026-08-21 04:04:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3be023ba-bdab-376b-860d-d2da526f4c5a | -16.7261 | -47.68937 | 2026-08-21 04:04:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e938efdf-9694-3e8e-8dcd-cc1dfac08fb6 | -22.15718 | -46.65707 | 2026-08-21 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 14f1a0c0-d8af-3efe-a489-b6b3d438a6d7 | -20.41942 | -41.58619 | 2026-08-21 04:04:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d8313394-f30d-3885-b236-d5868871429d | -15.00411 | -52.68333 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bfa5a8af-0521-3407-a287-b6e34f84172a | -18.12008 | -43.73824 | 2026-08-21 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df50d2ae-d2ec-3917-a9b4-ee5a2627a08c | -20.43777 | -46.49271 | 2026-08-21 04:04:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README30.md)
