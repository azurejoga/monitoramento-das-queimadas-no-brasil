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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e74b7dd-465d-39d7-a97e-054ccf7179e2 | -3.81715 | -51.7029 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d857788-3a2e-361c-8035-ff640135ff65 | -4.11368 | -42.91182 | 2025-10-18 04:49:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 777fcebc-ace7-3cfc-8192-4377ceddfdae | -5.3425 | -44.99908 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52351c52-eb9b-3d51-b7be-4ace5a2c2698 | -8.16747 | -43.30279 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0d0f6d8a-ead7-3645-9e96-cb2846acc9f2 | -9.09331 | -47.78943 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 355e9dd1-0026-32e5-9356-8b05ca695686 | -5.631 | -50.03438 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7459e85a-a70d-3dda-89aa-c525bf7e7139 | -2.7316 | -49.3912 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20066908-da07-3035-8cb8-4446f040cd34 | -8.35718 | -46.21349 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cd8dd15-97b2-3796-9792-c3cdbbecd7a6 | -3.79543 | -51.41029 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ad5bd69-1501-3933-be39-223b69b1ca0d | -7.36322 | -44.22921 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f80b1519-c100-3901-8715-d3552e3b1f5d | -3.94261 | -48.08775 | 2025-10-18 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b933a41d-4001-3836-8b48-74545196dff5 | -3.25732 | -51.22322 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c716da5-b103-3871-b9cc-bb21563fc612 | -7.98641 | -44.16191 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6bc6077-3bfe-370f-b81e-e4cb39a3d8ae | -8.33275 | -49.96692 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c904510-84d7-3ea8-836b-1311d537fff3 | -5.01439 | -46.01498 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d43b51d7-056e-39a7-9de4-3c5eb704973f | -2.15576 | -51.95921 | 2025-10-18 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec2e19a2-bf52-301c-88b3-6880c8604634 | -3.77934 | -51.77097 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc214827-53ff-37b2-8a7f-2e9bc034836b | -4.64908 | -47.94926 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6e59fb-55ca-3a0c-98aa-7e9a47c6a550 | -8.39117 | -46.23267 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 295206d5-fb74-3af2-98d9-9c469305ff3c | -6.60991 | -44.21737 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a860a99-4254-39d6-9e2c-144a91aa011f | -2.86956 | -50.72919 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf4e792-fd16-354c-9c8b-9b984e26c4e0 | -2.86569 | -50.73217 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cbd130f-71fd-357b-9389-592a8b6ac606 | -7.05937 | -46.75483 | 2025-10-18 04:49:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c47df3c-c9bf-3256-ab76-46c7c5911342 | -7.5916 | -44.98625 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8e7e746-1470-3e6b-a9b4-44f40317d22a | -6.74415 | -47.37442 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b32ddb32-316f-3a20-a43e-9efc92ed9ca5 | -6.23558 | -44.1547 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca5469cd-b0e6-3a70-8daf-d162d0f9567d | -2.40337 | -49.36201 | 2025-10-18 04:49:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8511a0aa-c6b2-3823-a0f5-009fdd46523f | -3.75314 | -49.03262 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88862e39-3eaa-3010-b898-ef23154efd9c | -8.44097 | -44.17461 | 2025-10-18 04:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f77caa4-48f3-349c-8882-893b6a8f793c | -2.87234 | -50.7332 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03e5f036-1347-3688-ab9d-87c9791fe8b4 | -4.73331 | -46.1585 | 2025-10-18 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bbe5705-576c-3f94-80d6-035ca9dd4b4b | -3.8177 | -51.69946 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29b54507-ecf1-3528-9ecc-a1fbf1ce20cf | -6.35844 | -58.21333 | 2025-10-18 04:49:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f7c6cb1-74c2-359c-91d5-8a9e5464775f | -2.86459 | -50.73915 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10cbf2f6-688d-38b6-aa9e-da827c35f17e | -5.1653 | -45.22155 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d242838-3915-35c6-90ae-eb946dea6f24 | -2.7466 | -49.38575 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d0b5232-a2a8-3c57-90b8-b71a8afd3cc7 | -3.78979 | -51.76907 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5d80f04-eb6b-3d01-8231-f2bca36b0494 | -6.42144 | -44.70479 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2ecef63-451b-317b-b452-53f1720b729e | -8.38606 | -46.2365 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a079206-2af4-3b3d-a815-d8118c401a05 | -7.48906 | -47.03285 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 238c6f04-8c9f-3122-939a-47f7fc625e1a | -8.78605 | -47.93556 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac58080c-a515-359f-aa7d-f502e71def26 | -2.8635 | -50.74612 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1a45190-fe32-3f2c-9d85-209041161e90 | -3.64804 | -45.2653 | 2025-10-18 04:49:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ca5c0f-0eaf-3c86-83aa-f58fb8740eec | -2.39829 | -48.53511 | 2025-10-18 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 06dfcd4a-d812-3417-95ed-e3a211406a66 | -6.84432 | -42.42594 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e139602-bd7f-3170-b3e4-deebe23f75fa | -8.39504 | -46.23776 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45fa887a-7f38-3b34-ac67-3f367d187add | -5.59843 | -46.384 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b686363a-ad88-33d1-a679-e6d7c2787eed | -7.22353 | -45.31652 | 2025-10-18 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46559c51-08e8-3797-9301-184464e1bddf | -8.61444 | -40.20123 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 174c9402-d6c4-344f-a3ef-ddcad75a11d5 | -8.5471 | -50.07947 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aada8032-4500-3b67-bede-a03de374dfd2 | -9.50511 | -47.26518 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e021c443-8123-3d49-9e75-5334380379c0 | -6.3643 | -45.76218 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a90b9d6-91be-39dd-974e-b3e75d098121 | -2.96846 | -49.30994 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06d471ff-519e-3e63-8b6d-a688462f0fd8 | -8.36438 | -46.21238 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bace79c-ce5e-3955-a9c2-925d54a6c938 | -6.23097 | -44.15112 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c975d742-05f2-3df3-b0bf-7b5004dd2ef4 | -2.81247 | -54.38153 | 2025-10-18 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8952375-38c7-3334-a921-e7e725502cfd | -5.59416 | -46.38343 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b61ee099-b12c-34b1-a7d6-b4f86ce48ac1 | -9.03632 | -47.72105 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83075b7b-2bd6-3d42-92d5-a06fb182c32a | -3.84602 | -41.5796 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cdbddd05-2fa7-3ed5-ab4b-f2a87debe70e | -7.14049 | -46.41083 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7147f7ee-f99c-3d97-8540-47c4aa19dc5c | -5.56125 | -46.37034 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef52b2a1-9fb2-366d-896a-e8daca43844a | -5.88634 | -43.92063 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d39e3aa-ae9b-3845-99c3-7599cd8eafc6 | -5.29366 | -47.93491 | 2025-10-18 04:49:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac1a67d4-f9bd-3020-a9e9-33a1713040bf | -6.54632 | -43.91771 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b9d7a97-b120-3d38-88d3-7b7a592f3152 | -6.65146 | -43.67403 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15e06476-a512-3ba4-a606-63f409985354 | -2.87399 | -50.72272 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d77c403-9522-36fc-aaa4-be14d7debaa3 | -7.86652 | -55.37092 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6720194-cd2c-33d2-a608-55ed43c40059 | -3.8593 | -51.90978 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 335316e5-8766-390b-91a4-1e522d0aab65 | -8.16314 | -47.03017 | 2025-10-18 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20a775c0-8cc5-30d1-98ca-2272ce866803 | -7.21608 | -43.81366 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dd45990-407b-3720-8e15-2326fae8161c | -7.32146 | -48.45931 | 2025-10-18 04:49:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b372045-65da-3cf2-a67e-eabb84e5fffb | -8.09563 | -44.10799 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50fb9c99-74c1-3d5e-a6d1-4969089ecf75 | -6.65189 | -43.67098 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a23987f1-6111-3fda-b029-7c596a63455b | -2.89567 | -48.06451 | 2025-10-18 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f209f868-2683-3aa9-8998-a39ea5d43885 | -8.86091 | -49.88939 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc6862d0-102a-3ba0-a9c1-0ad24b6b1d97 | -4.44665 | -43.24121 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd9abd49-b4a3-3149-8fbd-58c34c9d9c92 | -2.42234 | -47.14675 | 2025-10-18 04:49:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 925c45be-851c-30c1-88e0-14a24750810e | -5.25889 | -47.23943 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 38d5fa97-c948-3217-9c4e-adc3c6a3226f | -7.99782 | -45.1546 | 2025-10-18 04:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 454ddc48-4d4c-3a61-8ed1-3d16684975e9 | -2.94986 | -49.33829 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5efcb214-6f9e-3194-b1ae-d7a321c99e2e | -6.23266 | -44.13919 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79b27e45-29ea-3e2d-8e4a-b5b436605d04 | -3.47243 | -49.92215 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc75481d-0c40-3133-a5b1-5e87fbb2ae03 | -5.25437 | -47.24225 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dab37f5-553d-38f3-ba64-f280f93008d4 | -5.15295 | -46.27032 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c19c8070-3432-3760-b46b-5685b74364e3 | -3.2664 | -50.12173 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fd5be6e-1655-36e3-838c-c35baa0d81a6 | -9.75116 | -43.95877 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1183b63e-b98b-358e-9709-bc59e33039b8 | -5.59473 | -46.37955 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bef0f507-576f-3ded-ae41-598fe399accc | -5.28783 | -49.28522 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d80424f-2164-3683-a8ba-13d934341fbd | -9.75564 | -43.9663 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f357aecb-be32-39b9-ae13-afdbd2f737a7 | -7.62443 | -47.83781 | 2025-10-18 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3520a850-1fb8-3cd0-9bbb-44e3ea2bccdf | -8.44657 | -44.17216 | 2025-10-18 04:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1293c55-3916-3543-8e8f-b5cafa2ef593 | -3.6962 | -49.56538 | 2025-10-18 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01a28fa8-6fe7-3456-b8c3-e319917fa1fd | -4.45325 | -43.23249 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ab554dfc-b902-318c-91ff-5c874c3330ab | -8.38545 | -46.2409 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bb394ef-9246-34d7-82a6-29f737b639a4 | -9.72239 | -44.54889 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 110048f4-23ad-3df9-8a62-b36d5697851d | -3.29746 | -50.01131 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 007cf902-6b89-3ef6-8f98-6990979be3fa | -4.2504 | -48.37244 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d319772d-2eda-30c3-9aa6-5104cba86306 | -8.54584 | -44.5786 | 2025-10-18 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53ec8f78-0a43-36e4-9315-b3dcd7b5c661 | -2.33044 | -57.02986 | 2025-10-18 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4148c04e-90ab-3ff7-a7f8-e91d23a262cb | -9.72076 | -44.56115 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README69.md)
