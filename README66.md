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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71f34a91-5fe4-3e24-bf8d-c830c4fbe637 | -2.89251 | -54.0133 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac575d86-6ec3-3f37-80d7-88ccc8f12408 | -1.72459 | -52.71033 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62ce4851-d493-311a-aab5-7362237fcd48 | -1.28759 | -54.54323 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47e219fe-21c5-3b2f-b819-45ed2c877828 | -1.67635 | -53.20756 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1e9b1c4-8959-321c-bd98-2f7ff9e6a9b9 | -1.62538 | -53.31649 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e210d89-568b-3253-91f7-c9915b179402 | -1.25962 | -51.75805 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d3fdf315-d550-3572-9f7e-a6f53bac835e | -1.39338 | -55.1936 | 2024-11-23 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b726db51-7b8a-3543-acf8-bbd5ab411b98 | -1.72905 | -52.7187 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 094b96ef-9a44-3cbe-babe-384561ebf172 | -1.75095 | -52.38702 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19aa6e05-a629-340f-86c5-81197f3dc627 | -1.67152 | -52.65922 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b8a554c8-4a38-367c-beb7-2f4ed6041b87 | -1.2254 | -53.68613 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70fc8c34-2f0a-38bd-b3b9-639e0db6b674 | -1.20872 | -51.94972 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be4b9176-fab6-3182-a86b-d727561efe41 | -1.77721 | -53.61371 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38c32373-7330-3ab2-9248-fe3b106a5c21 | -2.62257 | -51.79096 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8421bc45-401a-321d-a921-026512585cef | -3.23408 | -54.23183 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ce1cb20-4158-3090-a48a-5f579809ea5a | -3.23292 | -54.09914 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5dd96eee-6bd4-3d28-b6b4-55adbe50e0f3 | -0.93944 | -52.41749 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a77bf08-cf98-30ea-a764-bf9e2c289a24 | -1.24112 | -51.74254 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88dc007e-b96c-3787-a2a2-cbcebc9b2b74 | -3.75035 | -50.00789 | 2024-11-23 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b1ec4339-2093-3e3f-957e-bdf9a1f67cf6 | -1.10958 | -53.39207 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f9e5589-aedb-3b07-9b66-cd57383e7014 | -3.75037 | -50.01389 | 2024-11-23 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c95d0ba-8c1e-3a5b-8dac-5e766a283c27 | -1.7853 | -53.63158 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11e99da0-fd47-32d9-85b9-1127f0f53dd4 | -1.56006 | -53.52835 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed9de923-37e5-3423-82c4-6b10cabff31b | -1.73021 | -52.7112 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbaeec5e-97c0-38ad-99bd-0bf858b9e7fa | -3.25498 | -54.23678 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 639d905b-43ad-31d1-b7b0-b3b1940f9fd2 | -1.73524 | -52.71581 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5d25b40-7a2c-3bca-9cbb-79b7a70d5bf4 | -1.12984 | -53.40211 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f3fdb39-7c5d-3e21-a1fe-0019789fd165 | -1.55955 | -53.53165 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b1ddc26-3391-372a-9d6d-d8e4c235aac3 | -3.23026 | -53.93757 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa83cee-f8f4-394b-a917-24d36ad505bb | -0.93884 | -52.42128 | 2024-11-23 05:33:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8b7b7ad-fdf7-3134-b0f3-39aa8ff3735f | -3.23247 | -54.10216 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826bfa09-09b0-343d-9cbc-f305535cee65 | -1.25693 | -51.75816 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4a03384d-f386-3e3d-925d-1a7b4cf6bc6d | -3.00177 | -51.55029 | 2024-11-23 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8983205e-a9ef-3377-8876-0cf1e6cab590 | -3.26853 | -53.8273 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3209b04b-e18c-3989-a69c-26348a592b0d | -3.26957 | -53.82038 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c9174a6-7a79-3f8c-8782-13e8fa10f0e5 | -2.4543 | -53.70121 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9609f68f-d4ea-3448-9a79-fd0db17ffc6c | -1.6259 | -53.31306 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e814eb51-81ef-3cb7-9c2e-0906a8388ac8 | -1.12544 | -53.40491 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ab876f1-386c-321e-85c6-262cba7023c0 | -1.6019 | -52.5864 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78967441-ae3e-3259-ba79-bc5c15dd6550 | -3.22543 | -53.93365 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fadae3db-54a4-38b8-83a7-722fe248be7c | -2.76771 | -54.06379 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ea20039-768a-37e9-9b9d-c772ddb75e42 | -1.44322 | -53.39465 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd2bd3bd-7789-3878-a5d6-8454e6732059 | -3.31546 | -53.28875 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f126d58-d41f-3c8c-b4ac-513ec272b000 | -1.20934 | -53.68631 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 255e7c78-84a1-3e85-8b0b-56891d77ab32 | -3.50443 | -53.80289 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce7e0db4-27c8-36d0-912e-4cbc6d11e8d8 | -1.52661 | -51.56041 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b9c596d-f0a9-3e98-9fc1-5594c2ab34e2 | -1.22329 | -51.73981 | 2024-11-23 05:33:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98675288-649c-3ace-b79c-d8f82ebbf696 | -1.76629 | -52.70132 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 929378ee-f3c0-3e28-a7a7-a44723ee1fc2 | -3.32435 | -54.09261 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd9b06ab-d0c3-31ce-9f61-5a2a24ef737d | -1.72285 | -52.72158 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c009400a-1d8e-3e15-872e-49448800f3be | -1.62051 | -53.31228 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afd3c2a9-fbed-396f-a06e-54d025be980a | -2.1935 | -53.65244 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b17cc4-a284-3569-999b-3673df92074f | -3.50796 | -53.81643 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ac3af85-dbc5-3adf-a62c-7f68b9362967 | -3.74944 | -50.01406 | 2024-11-23 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c7588941-9500-3336-8cab-92df545c96b5 | -3.08942 | -53.26017 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b1b0ae6-40b4-3336-9df5-92e049c059c7 | -3.06315 | -53.28643 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 515fd750-709b-3451-9b88-7d8359212660 | -1.22587 | -53.68308 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c765c92f-eb94-30f8-9ad3-d91621bbb3b3 | -1.72227 | -52.72532 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd443c1-fee2-3cf2-8e58-cbddccb712c7 | -1.39633 | -54.50209 | 2024-11-23 05:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ef3e41b2-87dd-37b0-8cc3-85db4963a6b3 | -3.25545 | -54.2336 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d80656a-1814-34a2-8918-ceb9bc6b2255 | -1.66277 | -52.70078 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eda5ccf3-fc02-39c2-a3af-a0caa227f52e | -1.44582 | -53.39442 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2ea3c88-3fff-3d43-85af-2ce9ed44f9e1 | -1.65879 | -52.70347 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1e5a757-b352-3378-a520-3d552296dfd2 | -2.20594 | -53.67783 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35fc08d7-4b3b-39a4-8aac-a87b58348097 | -1.11872 | -53.40369 | 2024-11-23 05:33:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49486665-2ace-3177-8b7b-88a3457a5009 | -3.12377 | -53.10427 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6147a311-9f61-3028-b2dc-8ad1f0440140 | -2.85622 | -53.96856 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1867754-0d5e-3145-8e2c-75b4c825087c | -3.25653 | -53.26995 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94909027-fe0e-3e54-9ec6-ca6e4b2081a9 | -2.82089 | -54.02991 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4dcfe76-6044-3a7f-911a-4d4625ffaf41 | -2.77293 | -54.06458 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73eb383c-fef0-3077-a161-fc1b6b0ced49 | -3.2484 | -50.67031 | 2024-11-23 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4289911-aa96-3288-8cc4-eb75dd4ce050 | -1.62724 | -52.60979 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8bc312-43f2-3b0d-80e4-e6c28ee51d04 | -3.06608 | -53.22623 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c78914f2-42f1-39ec-824b-5cd5d583e8d0 | -3.25163 | -54.22336 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa4cd00e-cefd-3d8a-b2c2-cd2036963b2e | -3.50812 | -53.80045 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb0024cd-7faa-3c4a-9120-e05ff368ddb2 | -3.06312 | -53.28555 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e56080d-75ea-3be8-a0cb-127341ec51a3 | -1.61711 | -52.60044 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c98d3bf-bf66-3652-82a5-1b16cced838e | -3.50395 | -53.80622 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bf68c17-005f-34b8-b146-04f9e72f0761 | -3.30005 | -53.85417 | 2024-11-23 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 398104c6-7292-3f9f-b451-c550a6a470e3 | -1.7782 | -53.6072 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51d1e7b0-72e5-33bb-80f3-79384bf99432 | -3.25598 | -53.27359 | 2024-11-23 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 051df3d2-a8b3-3745-ba32-2129b6641796 | -1.72343 | -52.71783 | 2024-11-23 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d5345b1-6934-3af0-a86d-a6a82a064bb6 | -2.86147 | -53.96939 | 2024-11-23 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 331391c2-148a-3b94-a610-31128715c107 | -3.24445 | -54.23348 | 2024-11-23 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97f69008-1edd-3e17-a6f9-78cdd2f530c6 | -12.30191 | -64.45027 | 2024-11-23 05:35:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb09ab2f-e09a-3c3c-8b8e-f9d05cc8ff24 | -12.29192 | -64.44866 | 2024-11-23 05:35:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f6ab861-9a04-3341-b19e-da0d1579300c | -1.6809 | -52.6578 | 2024-11-23 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 92bd540a-2698-3e0c-9618-d3362a6d9263 | -1.6075 | -52.5977 | 2024-11-23 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| af057c23-c27e-3b6a-97f5-891292afe9c6 | -3.2569 | -54.2226 | 2024-11-23 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| fd741cf8-2d4c-3073-a5dd-8dab6d4e4498 | -4.6085 | -46.5002 | 2024-11-23 05:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ab592a6d-fc02-3dba-8e4f-909b0e63d0f8 | -3.719 | -42.7417 | 2024-11-23 05:40:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 8a4e4894-0e60-39e7-997a-7d4234a43d83 | -1.7359 | -52.7181 | 2024-11-23 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7cb0f126-82ae-332d-a2e3-3f15547846d7 | -4.5403 | -42.9066 | 2024-11-23 05:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c5931985-4854-35dc-b682-0e27044df969 | -3.2386 | -54.223 | 2024-11-23 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 27953585-7c9b-30ba-8ff1-be2d63cf5a75 | -2.8166 | -54.0326 | 2024-11-23 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 2a9e0b77-302f-3e2a-a103-44b86ded9f8b | -3.2385 | -54.2431 | 2024-11-23 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 60433b15-17f2-3410-83a5-2c22b81f99d0 | -4.2605 | -48.697 | 2024-11-23 05:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| de88c34d-7af7-340a-9053-d43eeee615fc | -3.2569 | -54.2426 | 2024-11-23 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c38ccd35-e89d-34bd-aa44-474df8deb077 | -4.5403 | -42.9066 | 2024-11-23 05:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ce742514-4f98-31b9-b8ce-19d67961bee5 | -1.7359 | -52.7181 | 2024-11-23 05:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |


[Clique aqui para ver as próximas entradas](README67.md)
