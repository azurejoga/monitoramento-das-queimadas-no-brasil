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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e57c8641-e794-3cc9-9acd-d096c222e164 | -1.12398 | -54.14368 | 2025-09-22 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 256a37ec-d311-31c4-82f5-84306143935b | 1.69116 | -60.98662 | 2025-09-22 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52a5f26e-6a80-35e3-aed5-c558d2147df4 | -3.9481 | -53.39133 | 2025-09-22 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2f9773b-5c60-33ac-9eb5-c4019c6059d0 | -4.57631 | -56.18494 | 2025-09-22 05:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75f465d0-68bf-36de-8759-907e360b4b5f | -3.8993 | -52.1806 | 2025-09-22 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ac982cb-44e6-3480-a4e4-fe85bad752c6 | -3.75831 | -61.19881 | 2025-09-22 05:27:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6b78c63-2a5a-3c2d-a054-0605626f04bb | -1.94332 | -56.59892 | 2025-09-22 05:27:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a31d852-2cc6-3fd1-8caf-bfb9ba3fa7d9 | -5.39798 | -48.63443 | 2025-09-22 05:27:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef1b2c34-4a22-3d3a-a4bc-feff243485eb | -0.94533 | -47.35312 | 2025-09-22 05:27:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43b1e632-ac32-3a50-be0c-ff7ed1075811 | -3.94853 | -53.38838 | 2025-09-22 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5d7e82e-65c4-37b2-8aca-525d5a8e7900 | -3.94897 | -53.38544 | 2025-09-22 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c950fa2-b8e3-3792-8933-547d76b007da | -8.2472 | -71.04977 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1831de71-6504-3fb9-8a2b-e38b25658eb3 | -8.06545 | -70.33745 | 2025-09-22 05:29:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f6ce4d6-8828-32a7-9570-c8f288eb4b6a | -6.85495 | -59.9668 | 2025-09-22 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47e92169-f359-3357-a95e-3ce74649c389 | -7.6642 | -61.12671 | 2025-09-22 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a464b7e3-9443-3a12-9aab-78d2464381a6 | -3.83663 | -65.13402 | 2025-09-22 05:29:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d77eb42a-c36c-3713-b2ac-16f3558c6f97 | -6.34 | -56.19048 | 2025-09-22 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57244011-ffe0-3223-a65a-82db75f55190 | -7.24589 | -72.50898 | 2025-09-22 05:29:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ef79b9b-fced-370c-ae6b-a2a75e8a7b47 | -9.13399 | -65.46732 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1f7f62c-3e30-3d03-bebf-2c262effb1e4 | -9.1163 | -65.50904 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8900740b-01db-3279-97a4-e8a14daad5a4 | -6.54774 | -55.0404 | 2025-09-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ff9b070-938c-3e2f-93cb-bd74af5f6a5c | -9.21549 | -60.8426 | 2025-09-22 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00bd9db1-c75a-3a06-9311-49b376808964 | -8.06615 | -70.33566 | 2025-09-22 05:29:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 77dd9d1f-d265-3f3c-8597-95c618ebd4e7 | -8.69602 | -64.20501 | 2025-09-22 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1483dbff-9913-3e3d-9e4c-ce9cf8aaee32 | -8.20276 | -61.20565 | 2025-09-22 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb38e0c3-ec6b-385b-a1bb-3ba1dcd7acce | -6.85958 | -59.95964 | 2025-09-22 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0dbd7c3-8191-3fff-b880-004ac99eb5a8 | -7.71638 | -55.45078 | 2025-09-22 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e93945a-ee12-31ed-8943-c083ac52545d | -7.24972 | -72.50704 | 2025-09-22 05:29:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ec85389-5819-3fc8-9f36-719af374d457 | -8.77751 | -68.97709 | 2025-09-22 05:29:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1627df49-ebe3-3cba-9609-0e81b1482e66 | -9.12477 | -67.7321 | 2025-09-22 05:29:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e35fd494-050b-3cc9-b1f1-856b0a5bd150 | -6.86764 | -60.00016 | 2025-09-22 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5cbe48a-77b4-3787-a91a-cb8fc917f76b | -9.13145 | -66.00677 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38cd8118-fe53-346e-8d67-4bab6be06df1 | -9.13048 | -65.46674 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30fe580e-af87-3958-aae4-430d1951af14 | -7.66756 | -61.12722 | 2025-09-22 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d0018b28-d1b8-3ec7-a494-c332d9c5f997 | -9.00167 | -63.67695 | 2025-09-22 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05e7e885-be56-3374-a6bd-c485ebdf95cf | -8.63661 | -69.26676 | 2025-09-22 05:29:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b6853ba-d5f1-3d9e-93ad-cea10a50d0ee | -8.96247 | -63.62384 | 2025-09-22 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ec5915b-c14d-309b-af57-a36c0ffd8f38 | -9.1208 | -67.73144 | 2025-09-22 05:29:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbb1949d-001f-3454-acd0-f59d22995606 | -7.24903 | -72.51082 | 2025-09-22 05:29:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 371bafe8-3c29-3f80-a503-1570617d65d4 | -8.6322 | -69.26597 | 2025-09-22 05:29:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6e07563-9d8e-361d-be87-e7fd3f0ec3fd | -9.10265 | -64.00585 | 2025-09-22 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f445d67-03bb-3169-9040-7bbc7d362e74 | -8.52713 | -70.86971 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 832c826b-11d0-3b6c-aaff-e239613951cf | -8.20331 | -61.20204 | 2025-09-22 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c31a104c-f705-3f7b-917c-555fef04442d | -9.11696 | -65.50507 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c89909f4-74db-308c-a40e-fb8069bab108 | -9.10599 | -64.00638 | 2025-09-22 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25ae9b44-b5cb-3203-bfa7-1a7fd480482c | -7.21463 | -60.62327 | 2025-09-22 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b8d570c0-4f4f-3b8f-9d30-cdad3e70efbd | -8.02758 | -70.83275 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499755c6-257d-31f4-a3f2-1340d8991c0a | -6.63101 | -62.93484 | 2025-09-22 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64298cd7-dd3f-3dbd-84dc-e3517f7c81a2 | -8.98628 | -65.4563 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 274a081a-cf85-3b12-9a33-f9e0dab30bc7 | -7.74241 | -61.12366 | 2025-09-22 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15f0d648-8887-3d0e-9df2-9ed63b069274 | -9.10322 | -64.00229 | 2025-09-22 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49ac4516-3ecf-3a87-ba70-1775fd5907ba | -6.6321 | -62.92789 | 2025-09-22 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cb4ea47-39c3-32df-9e90-38e6846d6a63 | -8.74171 | -69.10555 | 2025-09-22 05:29:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26f44813-e999-3158-a260-c870a4959f7e | -7.71571 | -55.45564 | 2025-09-22 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 452979aa-5cd9-32ec-a613-500beff742bf | -5.6532 | -51.4681 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e125ba0-627e-32a8-a462-a87470397368 | -6.43176 | -62.8601 | 2025-09-22 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 700b52a2-e456-3ea6-967f-6e67553ffc9d | -8.82528 | -68.60075 | 2025-09-22 05:29:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb260197-2567-391d-94f7-210696112466 | -6.54646 | -55.0362 | 2025-09-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aac29d5e-95b9-3ee0-8484-b4ef13460f5d | -6.62879 | -62.92737 | 2025-09-22 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56ff4c1f-c5bf-3ba7-8aef-22133af3eaea | -5.65243 | -51.46502 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37cd313a-be91-3014-b547-fc4c245cacd0 | -8.67601 | -63.45539 | 2025-09-22 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e003c9-1d89-3cf8-93e6-6dd440563e3b | -7.59556 | -69.89029 | 2025-09-22 05:29:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfa9d78a-da66-3e03-990a-37dd8d86ef30 | -6.53982 | -55.02914 | 2025-09-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6728e242-cb9e-37ff-ae51-297078e42289 | -8.98692 | -65.45234 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edb7351f-aabb-38ed-b2b4-9d4bb92c2023 | -5.6538 | -51.46386 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87aa3082-d5b6-3238-adc6-9dc61ff2970c | -6.85553 | -59.96297 | 2025-09-22 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96e04e2f-c0bd-373a-8a27-ce0648db88f6 | -9.77174 | -63.37138 | 2025-09-22 05:29:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 948b3f76-acc7-3f9f-920b-a5de23a4786a | -5.65186 | -51.46926 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c910cd4b-a938-32da-94e3-f6fb2ca4b9e7 | -7.66475 | -61.12311 | 2025-09-22 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce0fbee9-e17f-33a3-8dae-18d3fc15e3a6 | -6.59459 | -62.92912 | 2025-09-22 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2ad34fd-bea4-3c97-9bf9-488b0df42c92 | -8.53393 | -70.94546 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca8ff384-2790-3094-96dc-27c2279b1427 | -7.71176 | -55.45013 | 2025-09-22 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b30095fd-40a8-3def-b2ef-39d1d8b39dc7 | -8.0281 | -70.82982 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac75e0b-1ce9-330e-911b-25cc4057a317 | -7.96158 | -71.35395 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d70c093b-df46-3acb-b20a-eef955e64be8 | -5.65829 | -51.46597 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f03367f-13de-3faf-a0c7-d9b8d7f630b1 | -6.63156 | -62.93137 | 2025-09-22 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72533d87-487e-3e4c-b821-77cdc162c00b | -6.54579 | -55.04109 | 2025-09-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b117ec9-644f-32f0-9507-1cec5544beb0 | -9.11345 | -65.50449 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 108da1b2-d403-3c27-8a86-ba159b21f7c5 | -7.21859 | -60.6201 | 2025-09-22 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 672d737c-0c82-3c8c-a898-cdbb10c3d3e4 | -6.59514 | -62.92564 | 2025-09-22 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9616cb97-c0c2-375f-a1e3-548602db87ae | -8.69265 | -64.20448 | 2025-09-22 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2235e76d-a37a-3314-83db-d7fa42a55cb2 | -7.59087 | -69.88947 | 2025-09-22 05:29:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29124f74-b2c2-3990-9ec0-aa8f24af6c64 | -7.66139 | -61.12259 | 2025-09-22 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6ac40d9b-fc2f-3af7-b003-958179757dd1 | -9.27001 | -64.50632 | 2025-09-22 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd10b095-d14d-35f8-8664-43a8568d131b | -5.6526 | -51.47235 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c132183c-d6e7-3186-8c46-f37cd3816681 | -8.02457 | -71.0552 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 341d926e-61f9-34a5-b670-43a443c813b1 | -8.96579 | -63.62437 | 2025-09-22 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 168bcbb2-58bf-3836-b90c-4fb2edbe303d | -8.98277 | -65.45573 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f8f4c87-6288-3140-845e-f9438ffdc3bb | -5.64599 | -51.46838 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ecb95dc-b53b-39f9-a787-3cd7834f26b2 | -8.20668 | -61.20256 | 2025-09-22 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5d0d6db-c1b7-3ffd-ad82-bcbe9032a773 | -8.01955 | -71.05418 | 2025-09-22 05:29:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b0eb844-80dc-3d2e-8cb6-f000793783c2 | -3.86012 | -63.90367 | 2025-09-22 05:29:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96ef4bb9-8985-396e-a03e-831e05ad4835 | -8.57189 | -67.85931 | 2025-09-22 05:29:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e63045df-d8cd-3da7-9483-94750a064af1 | -9.11279 | -65.50846 | 2025-09-22 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 793c3d91-bfb7-3079-a866-0b2046575731 | -8.20613 | -61.20617 | 2025-09-22 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37edc0ea-3622-3108-9d89-f6f819a99431 | -7.70715 | -55.4494 | 2025-09-22 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1007a1f9-fd85-39d3-84d2-1ec995a52c54 | -9.10656 | -64.00282 | 2025-09-22 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f295fb7-31b4-319a-b0e6-d22152371af6 | -7.24656 | -72.50517 | 2025-09-22 05:29:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 957116c1-ab5f-31fe-b89d-0bc0ab527c65 | -5.64733 | -51.46722 | 2025-09-22 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c6b1ac3-90f6-3ddd-ad66-f6f4e57a073e | -3.85952 | -63.90745 | 2025-09-22 05:29:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
