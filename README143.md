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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 614af5e5-044d-3cb0-a13f-b346ec2bed6a | -9.64964 | -67.40037 | 2025-10-05 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca727bed-b89b-3db9-89e9-a581d737ce8c | -11.20953 | -54.98854 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 004bbde6-f78a-3bc2-96e4-c63e2504a15c | -10.46122 | -57.49639 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 705bccdd-dccd-363d-be18-d66fed132d79 | -11.5125 | -60.45381 | 2025-10-05 05:36:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3a5dc0c-5361-3abd-81c1-05ec5581a5ec | -10.54457 | -69.43097 | 2025-10-05 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29234282-b0b2-3c67-b820-48baf995f3a4 | -14.83079 | -54.76844 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5dcf28d-d1ee-324b-88ff-ee51e7ffe300 | -9.81811 | -67.57402 | 2025-10-05 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06d4e5a8-5cd3-3e16-af1f-44c320451d17 | -10.79828 | -69.03744 | 2025-10-05 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae691077-37c6-3459-9669-248475b9473a | -14.58013 | -52.46123 | 2025-10-05 05:36:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cabe385b-71b8-3436-826a-f3f90bc12f28 | -9.8398 | -59.47329 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3a85c2-aa61-39ef-be4c-1d7621961c45 | -10.06979 | -63.52303 | 2025-10-05 05:36:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6513baa7-3f08-3aeb-a050-8d401d7f99df | -9.33927 | -54.52485 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 247125a5-2e62-331a-beb9-20c92fa44dd8 | -14.58076 | -52.45478 | 2025-10-05 05:36:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d2affa1-f14d-38c6-9cc6-4dc839a31d1e | -9.55893 | -67.44597 | 2025-10-05 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 182cbd10-306c-3ac8-b060-a02bbf02323c | -9.45384 | -56.65384 | 2025-10-05 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13740fa5-4bb8-36b7-a0fc-700f23a2d0d0 | -10.06024 | -59.35464 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 804ff416-bec8-3fa9-97c1-b098084e2731 | -14.30494 | -52.92272 | 2025-10-05 05:36:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3887834c-1d3e-32f9-a873-74106c1f5305 | -9.21227 | -60.42571 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cb69d3a-479c-3109-a95d-102173f55d46 | -7.91617 | -71.78124 | 2025-10-05 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7724d3a0-2e9f-32f9-bea7-c768fca05b7c | -12.96983 | -51.04255 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f114ef4-e538-3f0b-bc35-a2605e2eb196 | -9.34434 | -54.52919 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9385656-eaa3-3e03-aa7b-0c5212ebf469 | -11.00064 | -57.04705 | 2025-10-05 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5481b8ee-7498-3512-9aab-c1d804137e77 | -11.83007 | -61.20801 | 2025-10-05 05:36:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62e7ff7a-d3aa-3282-aadf-330277e89aa3 | -13.73912 | -51.31141 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20152f5a-3cbf-366e-b354-bce587df1605 | -11.40407 | -55.17976 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68426689-5283-3a62-8029-9d4c5c783bbf | -9.42582 | -63.69273 | 2025-10-05 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e18b2e1-2743-3299-ab87-e90c259f1445 | -10.46448 | -57.50676 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ae014e0-9aa6-30be-b1b1-4cb438874f14 | -8.78775 | -64.23055 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 041a4fb8-4930-346a-a0d4-75260a3461d0 | -10.4599 | -57.50603 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e79007a-3af2-3280-ade3-b8d55c6325d2 | -9.30963 | -54.53627 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 485e7d89-d57d-3933-904f-96ab0cfe5de3 | -11.87354 | -56.88253 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0422bd6c-df83-3367-82d4-b6aa6c0247da | -12.31797 | -55.13467 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9179bbf-b8f5-3bd4-aa05-3a236a6211d9 | -13.72778 | -51.28151 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| ac7eae3e-fc04-31ae-81e2-10abc8aee098 | -12.32177 | -55.14985 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce136cfe-b6e2-358e-8428-fd33896ac5b4 | -8.42892 | -70.12519 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e079e155-805b-3000-97a5-7cfd9f972874 | -10.83702 | -57.17387 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01d9941c-de99-3aa3-aec1-6ae95a1f9833 | -11.45815 | -51.52108 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6a44aec-9058-3e62-9aa5-354b6ac9609d | -9.9864 | -57.82013 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a336ec1-8b92-3b42-bf86-708b9c1a91ac | -10.1835 | -58.18011 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d40456e-cd32-33ef-bb94-dadf5d8d1a34 | -9.56127 | -63.21021 | 2025-10-05 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6603f03f-be6b-3bb7-8968-b37c288bb157 | -10.83495 | -57.18914 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67fb5255-b719-3a60-8345-dc88c5b1f894 | -9.3453 | -54.5219 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f08ad1cc-cd87-3c79-a2a7-8795438948b9 | -8.42462 | -70.12442 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 651e6347-2158-3439-a097-95e764a9c10e | -10.09975 | -65.03996 | 2025-10-05 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 495475b8-35e9-3053-b8bf-213d20f7d881 | -12.98713 | -51.01535 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca5938f-c07a-34c0-9842-daf2867c5ec8 | -12.30602 | -55.14059 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fc79081-ddfc-3de4-bc48-23a2d243bd56 | -11.45126 | -51.52051 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79226d00-cefa-31bc-a0f0-cc00858c8729 | -9.63825 | -63.24419 | 2025-10-05 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1ee1a6d-89c2-375d-91a7-232077f71676 | -9.1986 | -58.96282 | 2025-10-05 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25154935-00f9-33fc-8174-f81e0b9f7944 | -10.6562 | -58.76013 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0d844c-e418-30a6-91aa-351b1f9e680d | -9.33976 | -54.52114 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 347fd4b2-c61a-3d3c-8814-1db33129d75b | -13.72924 | -51.26723 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| aa937ac9-1dcb-3c29-837a-8088754d5b29 | -7.89187 | -63.01282 | 2025-10-05 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdc66d6a-302e-385f-9f21-fb256da13952 | -12.30734 | -55.12951 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ba0ebaa-e6fb-36ba-be30-394b5b0acb77 | -9.64048 | -54.31493 | 2025-10-05 05:36:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f59816e-60f1-34bd-b59b-4e4f6c466bdb | -11.39948 | -55.17216 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d49b321-f5d0-3494-831d-74c6ec8c1c43 | -9.85109 | -60.27917 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65f7c155-6819-3648-ae46-56cdeacc2cc8 | -9.42933 | -62.30544 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b218c646-5119-3684-9b19-30998d736439 | -9.32671 | -54.53479 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab882273-c5eb-36bc-869b-698d424a32a8 | -10.35702 | -58.45702 | 2025-10-05 05:36:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da547cac-cc26-39b9-b5fd-b1a3eb036938 | -9.47257 | -66.04003 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8659d62c-2955-3e62-8873-893b6f5d8ee5 | -12.31199 | -55.13771 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 630d36ab-ed0b-336f-bcb6-f6687c0a1de7 | -9.12095 | -61.76033 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f99e5ebd-4ce3-3bdc-92a1-de7e36e71f3d | -9.3347 | -54.51669 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef0b86e1-3c6c-3283-880d-a0781d51f288 | -11.39402 | -55.17149 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1efecf4c-7dc9-33cc-9358-c947748ee429 | -9.53898 | -62.89483 | 2025-10-05 05:36:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5cdf6cc-afab-337e-a258-fa2ebec4dfc4 | -9.45454 | -56.64862 | 2025-10-05 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d577382e-11e9-33f0-886e-90f5171502df | -12.32134 | -55.15347 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b83b83f1-a904-30c2-96b6-3b29a3e5248b | -10.46647 | -57.49227 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a9a2149-1c03-3faf-9908-40e7d3df464f | -9.10235 | -61.52781 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79684743-bac6-380c-b5fd-aa640a3c5702 | -12.30984 | -55.15565 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55275bb9-b341-3445-a0dd-f7e2b9dcf23e | -13.72851 | -51.27437 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 6890c458-8bbb-3639-969a-1e184e03b547 | -8.43249 | -70.13008 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62618f38-37b0-3007-9ba2-10ccf26695c7 | -10.10031 | -65.03645 | 2025-10-05 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db49b96f-5822-38df-abcc-2d8a07925c47 | -9.15068 | -59.53513 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2dce63f-d3c7-351e-99a3-efe1c12ee46a | -12.31155 | -55.14135 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef332fc-3dcc-33bb-9a83-36a7bf37d9e9 | -9.33276 | -54.53163 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c72299a-8e71-30fa-911e-02e21b67c129 | -9.56467 | -63.23265 | 2025-10-05 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95b3caea-7722-3c8b-aaaa-2d95f02d444d | -9.90394 | -63.58788 | 2025-10-05 05:36:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2052d0aa-e966-394d-ae75-8c48c61d9509 | -9.37163 | -62.29268 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92127efb-8c88-3fd9-83ea-71f22b573444 | -9.32771 | -54.52713 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe1e8f02-829f-39de-b84c-9e126c2f85e2 | -9.03836 | -61.64347 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f89fd06-ca21-37ac-86f3-04ee1b645db3 | -11.84512 | -63.72054 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3da147b-0bbd-3140-b4c8-97e3b0d3b810 | -9.14322 | -62.36909 | 2025-10-05 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e937ed2e-cbc6-3819-8918-98551a8e259b | -12.30649 | -55.13853 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3738ff7c-5161-3ac1-8168-23300cd1ab45 | -9.16346 | -58.31072 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c8ef815-f2f3-3bcc-86cf-bdf0d32a41a7 | -8.43322 | -70.12595 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 971ea89f-f6ff-3614-b767-f7b63f9398bc | -12.97627 | -51.05053 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9304106a-a979-317a-a913-2533a372a005 | -9.40565 | -56.89443 | 2025-10-05 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c1e61dc-a95d-3812-b902-d1a9077265a7 | -10.45084 | -62.63053 | 2025-10-05 05:36:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f82a95ff-97d6-30e3-9822-8aa9c1f5bec4 | -10.63355 | -69.54515 | 2025-10-05 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5afca73-86eb-3b15-8f5b-83d467ea4d5e | -9.68025 | -67.24071 | 2025-10-05 05:36:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 625fb0ff-c1cc-343f-a145-e632a8269790 | -12.31332 | -55.12655 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 524df9f7-5d2d-3735-a513-15c5f006ff76 | -9.3048 | -59.32401 | 2025-10-05 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef59b5a7-818b-3aec-84df-54d95ae87aeb | -11.39359 | -55.17495 | 2025-10-05 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbd079f5-8f09-3d62-ab04-0a746c87ebfe | -10.18592 | -63.62817 | 2025-10-05 05:36:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5891f4f2-f9ff-3d73-8059-2fd25156eef7 | -9.16484 | -65.48942 | 2025-10-05 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d92a4a16-96f4-387e-bb54-79c1b23e4aaa | -11.45887 | -51.52318 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad8a57ef-dff8-3b3e-b0c3-06a5e2142fa8 | -9.43826 | -64.3699 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52f44ceb-2f59-36d4-b0e1-152b4bd8f0f9 | -8.81372 | -63.45967 | 2025-10-05 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README144.md)
