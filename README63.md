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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 171e3d36-1019-3e67-ba8a-d26641502f6b | -9.79734 | -60.17945 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a349715-9716-394c-975b-486c43ad9140 | -9.93565 | -60.52765 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dc6894f-7bd2-39c0-b52a-a861f71c4494 | -8.60863 | -70.21281 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f89e435f-15eb-3cb1-880c-88bdc6f53de2 | -8.94155 | -62.36823 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21b49ea9-4db9-334e-a819-7376247e9a71 | -9.8623 | -64.98893 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bbf0ea4-5b49-3d66-945c-2940e463e811 | -11.34827 | -61.55285 | 2026-08-31 05:36:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcecfb94-827a-3e74-9c6f-0bcf31a888bc | -9.79621 | -60.16447 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b13271a-a821-35a8-946e-ff203a0400b3 | -9.13879 | -60.52979 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fba4828-cfa4-306a-ba4f-b1b4eb765724 | -10.57742 | -57.49986 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c354dc8-5ec4-39e6-ab38-017aecf08c88 | -9.72013 | -64.99932 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89c659bf-8ca8-329e-8b27-4fba0a0e27ca | -9.83636 | -63.01154 | 2026-08-31 05:36:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5695a11-a662-3026-8cf0-d1f19330da1e | -10.74879 | -54.04605 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 02590e5b-dfad-3d3f-9336-7b2c8e507839 | -9.22408 | -59.58063 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13dd1e21-a670-39ca-b05b-fff68e80b9b5 | -9.23091 | -59.58169 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cca6099-8bd2-374f-ab61-3a53f8cbdec2 | -10.74284 | -54.05167 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fcc70ccd-983b-3324-9929-795433d9a6e5 | -9.71078 | -60.75678 | 2026-08-31 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dec6049f-a091-3f6d-96a7-c4018311892b | -8.70619 | -69.97557 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aa0b3b3-d6f9-31ca-acd9-43164ef08bff | -9.03059 | -65.39415 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 430c63fd-6160-33dd-bd63-2f972237a132 | -9.14688 | -61.1025 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff928009-a702-3385-bfb9-3061bcdb25f0 | -9.00413 | -65.43348 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f02ea86-19f9-3385-abc8-b4585741d634 | -10.57468 | -57.50226 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3a8ca95-4006-3235-8418-cc067ff7245b | -9.14411 | -61.09847 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400734c1-7daf-3117-8d00-0058705ebee9 | -10.48867 | -59.60573 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c50961a4-0e71-3cc2-8dc5-13a1c32043a8 | -9.71643 | -64.9987 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 819240da-c1db-3a7c-b30d-021eb738f885 | -9.05492 | -65.41298 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fe88e14-d4ac-3641-85fb-7fa4e4baef9e | -9.02979 | -65.39886 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 095d6217-2d95-3db9-a6b2-f69dc931f8c1 | -11.67807 | -47.61295 | 2026-08-31 05:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7283b2bd-81bc-3b40-ba58-db0613466dd5 | -8.80062 | -62.5041 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95c77f66-51d0-30f5-b5cf-ec61d97c9225 | -11.49307 | -60.58401 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b882c95a-31be-30af-8377-f13335a2ec5a | -11.48725 | -58.51501 | 2026-08-31 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbac926e-a19f-3b5d-bb1b-d51d3330b9f8 | -9.17758 | -59.63377 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b53d5fc2-0fb3-32b5-a2b3-ae1e2abfc528 | -8.80884 | -70.7788 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7fa109fa-69ac-3a15-84a6-72a40216b4f7 | -11.67744 | -47.61867 | 2026-08-31 05:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f3a5038-643d-3506-ab86-f398753985e6 | -9.94177 | -60.51038 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5e9cb5d-f09b-3eb9-83ec-92db87fe66a9 | -8.62879 | -66.53929 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f92b305f-cb17-31a3-99cd-1ffc72a2fc59 | -9.79453 | -60.17531 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc481eda-7672-32dc-83fd-c6594967c37e | -9.88984 | -60.28217 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 389b7ff2-8a17-3caa-9760-7bc4ca521209 | -8.68198 | -62.84796 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0598af8e-7feb-341e-9141-fffa58b002f6 | -8.94828 | -62.36933 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 315519fb-93af-393a-8c7a-c6ffecb2264b | -10.76112 | -50.85533 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1aa7fd7e-6d2f-3c8e-ae67-f7dd5eaf67ab | -10.4841 | -59.61272 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 580247b7-0924-3bd8-9bcb-19a22e32a48b | -10.74326 | -54.05066 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 95de506a-d9ff-3346-a7cc-a3ea69f70bc5 | -9.05714 | -65.4231 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 438351a4-87c4-3161-8ff7-07c186e77f20 | -9.12925 | -65.47271 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 300e0b2e-920e-3e52-8ce3-c46d047f1c69 | -8.80454 | -62.84893 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c7453f-a0e3-3261-951e-babf8f7a2a52 | -11.0334 | -57.23427 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6a4d364-abc2-34db-b40d-1905e74aa7fc | -9.05875 | -65.41364 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7210c00e-8893-3245-9e82-ec43178bbf4b | -9.8932 | -60.28271 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b600da48-7313-39a2-b42d-8a01a33980c9 | -9.93673 | -60.49863 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19978978-4fd3-371e-b244-a601ff3f1d80 | -9.79678 | -60.18306 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2981634d-b5fc-3c6d-a04d-5254a2a26595 | -9.24912 | -60.43123 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99f38f9b-f5e3-3b53-aba2-95b4717ce554 | -8.81444 | -70.7805 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59195bd7-b105-3007-803d-c5a4ad4d7d66 | -11.08037 | -51.50986 | 2026-08-31 05:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b6b6e62-ca37-3562-8d0f-3b54db55a117 | -8.68342 | -62.81791 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bf89275-beb8-30ab-adc2-b332ca0b23ff | -9.72506 | -65.00357 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d138ca10-75b6-3b31-8530-b61680f50388 | -9.90658 | -60.15184 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4692ecd7-4685-343a-ac11-54acd05bda15 | -8.99948 | -65.43755 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a8d08de-c8a9-3f4e-bea1-50ec43aaa858 | -11.03557 | -57.24638 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c30c9bc5-1578-331a-8f8f-49c2f3c74232 | -9.01369 | -65.40092 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f1fe7e3-e681-3f14-b2e9-0eb0f01ee47f | -11.03763 | -57.23163 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4cd1972-9bc0-32f1-a62e-c27f95a4ca6f | -9.71547 | -64.99287 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20dd2f75-aac4-3b66-a002-1537e652a55c | -8.43313 | -70.41573 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e7bee1-5d64-3b6d-962b-6c5d533454dd | -8.9699 | -62.39075 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9a77c4a-fbc6-329a-93fa-dc5a96a59817 | -9.15076 | -61.09953 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7865eafb-297c-3c3e-8b27-8b9068968457 | -9.18975 | -67.78712 | 2026-08-31 05:36:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ede1b93-4e61-33f2-90fa-335d19585363 | -10.7344 | -54.04404 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df53ea3d-3141-3e7f-9a6b-51adc11c74a7 | -9.72136 | -65.00292 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 882a390a-2f04-38bc-8721-5d60a7c45593 | -8.7962 | -62.48857 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db52b446-6c7b-3e7e-8a1d-7c86ba96b0ed | -9.708 | -60.75272 | 2026-08-31 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68984b6b-dafa-31e8-b2e9-254bb6cd6f22 | -8.67514 | -66.5168 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8951de3-4f4c-3dcd-aaf3-2a67fd3a0681 | -8.94434 | -62.37236 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b96d2299-e578-3af0-ac3c-0c5f1b668093 | -9.20819 | -60.87892 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fc4194c-53e4-349a-9f80-25711a77c164 | -9.17702 | -59.63746 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03989570-a254-3e98-9db0-4d706b520bd8 | -9.07408 | -60.41816 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830eca17-d2df-3bec-9320-c2662d61deaf | -10.4203 | -57.22839 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bd6c07e-7b72-3286-aa0a-a2884ee50875 | -8.67451 | -66.5205 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad0f6a8-9f00-3151-b760-a7ee9aa511a1 | -9.79341 | -60.18253 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b60a359-069d-3551-97eb-bb43b42327fa | -11.29357 | -54.03178 | 2026-08-31 05:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90f186af-fc12-3ae3-900a-d334b0398051 | -9.05955 | -65.40891 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2a1f3b3-affb-367c-8adb-c4a3f4682d34 | -8.873 | -66.89935 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e070365-2e3f-3d40-99b4-f1fad5b875c5 | -10.73873 | -54.04568 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9592d7e5-ce20-3be4-ab1f-30f444eec606 | -8.8012 | -62.50049 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8821fb1-51b3-3b3f-a2cf-01aede4e1fce | -8.96873 | -62.39792 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07145823-f9d9-38bb-b2e0-e597bc0f7036 | -7.87472 | -71.78644 | 2026-08-31 05:36:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c43bfe2a-10b0-33cf-a328-fd116e4393e2 | -9.93452 | -60.51289 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96cea1e6-5cfa-3b07-b0e2-4d781b397a13 | -10.57849 | -57.50284 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7164aac-258b-3926-aaee-aac756164771 | -11.48662 | -58.51926 | 2026-08-31 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bcb3d31-a24b-31b9-a5a2-4413f9dece39 | -10.58022 | -63.52658 | 2026-08-31 05:36:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcab44a5-646d-330e-9497-5fcd937c8da2 | -11.03946 | -57.24694 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9b14553-8fa8-36c2-8c2f-0aab0e3157e1 | -8.94376 | -62.37595 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8950092f-f229-39bb-bc2a-5711b3b31e57 | -9.88759 | -60.27444 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e28e7cc7-f50e-30d1-a585-d51eca318f6c | -8.68211 | -66.52567 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5231d040-c07b-3e77-ac79-082e08ccebea | -8.94219 | -62.06508 | 2026-08-31 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5efb021-178b-3ebf-a1c2-8e487432559b | -10.65566 | -65.28529 | 2026-08-31 05:36:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c320ece5-c61b-388c-9289-1a0c2a8e03a9 | -10.74805 | -54.05136 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e6733f09-5754-38d4-80e9-e8c9ae2a25ed | -10.75104 | -54.06359 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78768fd8-ba7d-3dd8-a4ba-d0944b1dffea | -9.0519 | -65.40758 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 509cff0e-1c9c-38d5-9706-7b92f59e8fe1 | -10.49154 | -59.61004 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d1cb72c-59b4-33ba-bbd8-8b46d3cb309b | -13.63854 | -51.83999 | 2026-08-31 05:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de6986c0-b5b4-3673-8a01-312d58426873 | -9.05573 | -65.40824 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README64.md)
