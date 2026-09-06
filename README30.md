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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cefc163-a708-33f2-980e-17b621834cbf | -3.1972 | -61.23139 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 496125f3-42c6-30a6-bb58-3325679d97d2 | -3.21456 | -53.16932 | 2026-09-06 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 434336ca-f968-36bc-b742-224a7d322fb4 | -3.38758 | -59.41523 | 2026-09-06 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55df6fc8-70cc-351b-a0bf-5460fd2fa2f9 | -3.11035 | -60.65149 | 2026-09-06 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e800a920-c1d2-36ec-9b9d-44f764088544 | -3.79169 | -55.87795 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f3e525-110c-3ae8-b3a1-e2628b2a69fb | -3.38313 | -59.41913 | 2026-09-06 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb491b47-f0d8-367f-ac21-d639bd06893c | -2.0412 | -56.42264 | 2026-09-06 05:40:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3cc4dc3-5e84-3c21-8a30-2b83edd07613 | -1.34882 | -60.233 | 2026-09-06 05:40:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abbdbb6c-fb21-355d-a32c-206035784df7 | -1.49604 | -54.82924 | 2026-09-06 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12dd57f4-3f9f-351b-a078-ebb09aafcd0a | -2.86378 | -50.46392 | 2026-09-06 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83faad1a-c96f-3098-834e-7a61282a3e4e | 2.41055 | -60.67043 | 2026-09-06 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e725cb8-fea5-3c37-9ea9-022c16507bc5 | -3.14247 | -60.63602 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3123d025-3004-31da-8760-7dc1ac4ca9c7 | -3.17166 | -61.14738 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8809065b-2039-315a-8504-2e18d3ea920c | 4.19636 | -59.96294 | 2026-09-06 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb16cac9-7ff3-302c-807b-5ddc05562e3b | -3.17567 | -61.14418 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb97e125-1097-303a-9c15-6bdc2f59298f | -1.39279 | -55.1727 | 2026-09-06 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe1dbf64-b1ef-339f-a58a-80ea6254083f | -3.04648 | -61.32201 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05f5bdd2-ed4a-31ab-9475-34042912f987 | -2.45577 | -57.91262 | 2026-09-06 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a8cee2c1-6b38-381e-b237-6139ab5d4dea | -3.17684 | -61.1367 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57bb8792-dca7-32d4-91ca-7f5f478864ff | -2.86293 | -50.46968 | 2026-09-06 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2f552fb-8a16-3446-864b-14685d266383 | -3.41784 | -58.31346 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31e3b94d-f92e-3465-8424-351dd759332e | -3.42185 | -58.31403 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e46f81b5-4a28-35d5-a9ed-77558925ea21 | -3.03062 | -61.24405 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dee03c5-05c6-39dc-8cd4-c6c1a31d8ea9 | -3.16162 | -50.83031 | 2026-09-06 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95e5b8b1-a304-3bb5-8823-a8b38aa99a0f | -3.43975 | -59.25364 | 2026-09-06 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba79f938-ef21-311f-a57b-b3b125c6a175 | -2.58859 | -59.4016 | 2026-09-06 05:40:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8ebb3c9-1577-397d-b129-505277017f16 | -1.39198 | -55.17797 | 2026-09-06 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a069ab91-938b-338e-917f-a1eca0d17d03 | -3.20005 | -61.23563 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b61774c-37a8-3628-be21-6edf7276a288 | -3.23631 | -58.89408 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccd858d8-ec0b-378a-80d3-02495b5199e4 | -3.42239 | -58.31055 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1842e46-e848-325f-a012-682300e8aef5 | -2.97999 | -60.93771 | 2026-09-06 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 237fdfc4-4cda-3b30-b187-70c425fef24c | -3.80996 | -55.88593 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f19437ab-fc33-39b7-89fd-68d7166e3fb1 | -2.58791 | -59.40601 | 2026-09-06 05:40:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 971088b8-48d1-32ac-bc1a-d3a381ed658e | -3.12269 | -57.69293 | 2026-09-06 05:40:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36701315-51f8-3b86-a46f-a9006fda7141 | -3.11854 | -57.6923 | 2026-09-06 05:40:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e580050d-6453-379f-bd59-a59b84eb3403 | -3.14948 | -60.63713 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35ebf257-1c83-315a-985c-b38f24054762 | -3.38383 | -59.41465 | 2026-09-06 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91bfaed7-9f1d-3c3c-8f1c-5e00f7cf567d | -3.41458 | -54.7754 | 2026-09-06 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e772c09a-e00c-38cf-816a-340135196300 | -2.91574 | -60.99414 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b69826e-1807-3d1c-99fa-03ee3487dcfe | -3.07203 | -61.09041 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b364b93e-6512-3831-89c4-d1e4e80287c0 | -3.22023 | -53.17023 | 2026-09-06 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8594119-30fd-33ab-b183-5cca99db9a0c | -3.80842 | -55.89605 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2b3556a-7f35-3d52-8917-9da48994236f | 0.97867 | -59.38223 | 2026-09-06 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b9cd7aa-9855-3683-b8fd-3e0df9942e41 | -2.86962 | -50.47068 | 2026-09-06 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3a7d339-706e-3498-aa44-d70f7efe3e61 | -2.73475 | -60.07172 | 2026-09-06 05:40:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c071d74e-f743-36d3-8da8-74b1276a8f86 | -3.0827 | -61.17993 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 459ab610-6bab-3f5a-b61e-78ebc108f89c | -3.15452 | -59.14602 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2b9a824-ddcf-3718-b752-72b1bf50ed6e | -3.37565 | -59.41796 | 2026-09-06 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85d0aa61-5d02-330b-877e-8da7b0aade26 | 0.97511 | -59.38277 | 2026-09-06 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d45f37fb-a43a-3658-ad02-b84d7abdba01 | -3.79093 | -55.883 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb06bc7b-62c8-301e-b3de-874c33fe3002 | -3.22934 | -58.88812 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa6a6fee-d925-3243-b4c5-b832792136ec | -3.1843 | -61.13403 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6651a5fa-d95c-3fb3-8507-92b0e3048376 | 2.64399 | -60.15247 | 2026-09-06 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d1aa1de-8f6f-3f81-b9e3-f9e169cd8b78 | -3.85942 | -51.04238 | 2026-09-06 05:40:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e032479-a8d5-3ee9-a58d-32784bdf6d52 | -2.45982 | -57.91327 | 2026-09-06 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f14558c0-a4d4-3838-8040-bee1902d9b86 | -3.08664 | -61.51501 | 2026-09-06 05:40:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 020ce8a5-10f7-3117-9753-d3e2a5d4a1ea | -2.46036 | -57.9097 | 2026-09-06 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7f901b81-f318-3d32-b026-e9329b2b5fcb | -2.25151 | -53.76707 | 2026-09-06 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70e4d5f1-1ad6-332d-9bd1-eb3dcbd98a42 | 0.00698 | -60.59121 | 2026-09-06 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4734ed4-0995-3482-8de3-04fa39318bbd | 0.30604 | -60.44331 | 2026-09-06 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c94296ff-13d2-36c1-bccb-99c1a7fc8ab0 | -3.78693 | -55.87722 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32123b2-424f-36cf-86a8-f5d590a7ea04 | -3.07927 | -61.17941 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b075f0c-a8f8-3b7e-9a3f-178475031276 | -3.15507 | -50.82915 | 2026-09-06 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36567b8f-fd17-3310-8e36-c97ee67025c0 | -3.07985 | -61.17569 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96bca1c6-379d-3361-8f40-0a0211385290 | -1.49196 | -54.82302 | 2026-09-06 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78e36ca6-ce89-3bf7-b898-95601b83e8d4 | -2.91859 | -60.99843 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d928bd6b-8c4a-355b-82e5-59290599e552 | -3.37939 | -59.41856 | 2026-09-06 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e99bc89-88f9-32db-aa15-91da540ef601 | -2.97653 | -60.93716 | 2026-09-06 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8818e8d2-0417-3ebe-8a47-6e08149f0527 | -3.18086 | -61.13349 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea294d7e-7937-3421-87ac-5628a03d5c64 | -1.18536 | -53.8284 | 2026-09-06 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf69b37a-529a-3ccf-9673-727b0ab511e8 | -3.38453 | -59.41016 | 2026-09-06 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f56ae44-15be-311c-86f1-903690b4e78e | -3.79569 | -55.88373 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 457da449-edd3-369c-8bac-f6f43a3cf8e7 | -3.81317 | -55.89678 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f4715da-6231-30a5-acb5-43a2bbdaba8c | -2.71104 | -60.17629 | 2026-09-06 05:40:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4aea9014-12f2-33c2-ae5e-2f3f6b2d07f1 | -3.42587 | -58.31462 | 2026-09-06 05:40:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83849ddf-f980-339b-9b2c-606a31f43064 | -3.13776 | -60.64325 | 2026-09-06 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 023a32de-41c5-3a4e-84cd-c7e4e81d38a9 | -3.44027 | -59.25129 | 2026-09-06 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72b832e7-7e87-3e99-9cc7-e02633f0bf08 | -3.14417 | -60.64825 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4822e2a-2a68-390b-9f7f-0d1cfecbf809 | -2.24665 | -53.76286 | 2026-09-06 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 624d30ac-7e03-3437-a4ca-0d2210e719b1 | 0.87104 | -59.68203 | 2026-09-06 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 175fc40d-6c62-39ce-b473-99d196587e94 | -1.39117 | -55.1832 | 2026-09-06 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c1eb481-e6d5-3d1c-98ae-b16a6201d471 | -2.91455 | -61.00166 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e0d43d9-0759-3e6a-af1b-a6d2ddc06ed6 | 4.19914 | -59.95876 | 2026-09-06 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8958c7f5-46ba-3aba-a4f2-af6100071d38 | -3.06916 | -61.08615 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae86b461-cea6-3258-912b-c080b2d1f7d1 | -3.17509 | -61.14792 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92415ebc-b622-312a-862c-3d2aee398cbb | -3.10974 | -60.65537 | 2026-09-06 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 463a8b50-d9c5-311f-b4a4-389f9004cd30 | -2.91918 | -60.99467 | 2026-09-06 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39e22713-8b14-3d75-89e0-93de82b0acc6 | -2.70948 | -59.68474 | 2026-09-06 05:40:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c70f6702-5f4c-3557-a018-ac48c5d51e9d | -2.45524 | -57.91614 | 2026-09-06 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d03da5b8-486a-3059-94aa-d9546a7a7561 | 3.22739 | -60.48818 | 2026-09-06 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 522b9dd7-0c21-355c-963a-71d0fb91dbd7 | -3.81471 | -55.88664 | 2026-09-06 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1c27755-bcd5-3259-91e6-9fc60e1ac1a4 | -1.18581 | -53.82545 | 2026-09-06 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5354a6fb-38d5-3251-ab6d-cb1e41b661fe | -3.77511 | -61.76862 | 2026-09-06 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7258c077-56d9-3b2b-8ea6-d23262cda98e | -5.96904 | -57.69662 | 2026-09-06 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b1cd3d-c5dc-3268-b3b7-7cd23661b297 | -7.78905 | -70.05317 | 2026-09-06 05:42:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8877b823-85b0-3356-bad6-02c20574b9e6 | -6.87879 | -55.61315 | 2026-09-06 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4630e2-f77a-3557-a6c0-8bce2c25ce32 | -5.20306 | -60.02381 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6952f02-4099-3a9a-9469-df28e01e6799 | -5.3393 | -56.02613 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62fa6f2a-18e5-318f-9ec1-e656b96fede6 | -5.13712 | -56.27321 | 2026-09-06 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 43d509f2-714b-31dd-ad22-c95168f8867d | -5.57015 | -60.16233 | 2026-09-06 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README31.md)
