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

## Dados Diários - Página 329

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd151403-39b4-32e6-bfe0-14a516709f3e | -11.08072 | -45.77985 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4349ae58-aea1-3694-9e2c-888c3431befd | -6.84701 | -39.55691 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 554681cd-3886-3bed-a08a-8fc7459b7a38 | -19.84963 | -51.54366 | 2026-10-08 16:37:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e2efbb24-eff4-37ae-8978-ae0bc6303460 | -8.07715 | -55.29007 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 300cee2e-b2c4-3152-9474-c0d731543d94 | -8.95827 | -47.57177 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d2b0d8c-b39f-3407-bd47-906517c961b9 | -11.00561 | -47.97504 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ebe6f91c-075e-3462-a0cf-3ec2b64a8a49 | -11.1361 | -46.12676 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 515e920b-17c5-3a62-8751-5c4ade041eda | -8.52473 | -46.91534 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 430c0cc8-fe37-353d-b845-44f864cbf525 | -9.85639 | -47.85711 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 37b3ae95-1ca7-30c2-b588-c6c618407730 | -9.51809 | -45.60629 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3d583353-1785-36a6-92b7-02d9798ee8ee | -13.02549 | -48.51923 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 168f3631-0d26-39a0-b184-5aa9bf7a4cf0 | -11.58428 | -43.68426 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 69c458a4-6e2b-3501-8481-1cb2475406f0 | -11.13664 | -46.13036 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 16fc4efe-db05-3777-9338-bda853c843f4 | -12.78137 | -44.86861 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e490fbd8-30d6-3d0b-af21-5dc3aaacc954 | -11.27322 | -45.21305 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 507b1e83-0d5a-3b25-95d7-91815c223aa4 | -11.63498 | -43.70185 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e337db5e-5e5e-3eaa-a88d-1aff2ffd66ff | -7.15093 | -45.61454 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c3346a93-1e62-3bb6-8516-8af53c88f849 | -7.11481 | -42.54053 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| dd38da27-a6f8-39e5-8e9c-3ebbb0e0f7c6 | -18.15051 | -44.64744 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd72c853-b28d-3315-a98f-b8c1ec89d00b | -9.77891 | -47.81939 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 772ec3de-1a37-3435-a3c7-9531d6b70989 | -9.4584 | -44.61806 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 55accba1-e6b7-3a8b-bf57-b7c10cc784d1 | -6.9697 | -43.8953 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 68f176f9-2987-3e59-b074-19d428db77c1 | -10.34076 | -47.76286 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f7daceea-1104-382b-ae8c-99cbae1d4404 | -6.16339 | -39.43167 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| b92d4f28-5b56-3cda-ae56-57f7a5596307 | -7.75252 | -54.95271 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5bf3e937-a644-346a-9893-6a5bfbd4bb2d | -12.30743 | -47.05788 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8c847a95-146a-39f1-ab92-39ca37097219 | -11.22046 | -44.86593 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4fb79754-0d5f-311f-85a6-1d2356021278 | -11.21107 | -44.87099 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c767b58b-2506-30e6-abd3-84a02678d5f1 | -11.07806 | -44.03085 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 5c2fa3b8-1237-3ce9-8d5f-860d09ee8702 | -7.21327 | -44.28498 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d688da2b-0564-3a06-909c-be86ec70f58d | -12.8333 | -44.62888 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| fc0a2d57-f03a-3c9e-a4d7-6560f919ed73 | -9.01466 | -45.13065 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9062c20c-02fe-3765-a98d-ebf4f69770f1 | -13.19974 | -47.88366 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2891e31e-cc49-337e-9ed5-177b1d814ea7 | -11.21438 | -44.87047 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bbc1d8a3-7398-3417-871b-c6502b17719d | -6.52826 | -45.4049 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 80f67c8e-58d7-3471-9a14-9209cf11facc | -11.86616 | -43.55673 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| f91c2918-020e-3620-8863-76c147ef2814 | -12.0194 | -43.44657 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| a740d9df-cfe4-38be-8743-08924fe70056 | -12.83607 | -44.62484 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f837143d-548c-3f7f-97ff-986c2c5c6a80 | -10.2522 | -49.66755 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 66e32253-d16c-385a-845d-ef54ae688f53 | -8.97983 | -45.92796 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fa436bb5-236b-3701-8ceb-bdcb83327b8f | -8.51048 | -54.61637 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 70347168-ed1e-3321-b28b-72542e5f822f | -6.06734 | -44.10724 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| cecf4ae8-70e1-366e-9f2e-d36d125df27d | -13.70327 | -49.10481 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8473d4be-5fa8-3387-8815-fd390c2c464f | -9.14117 | -45.82763 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 62f678dc-39b4-3a59-b3d7-b750676eed61 | -7.34253 | -45.29217 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| da4fd607-2715-346c-9dec-7223eb9bbd75 | -18.14235 | -41.62455 | 2026-10-08 16:37:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fcb342a6-d303-3315-86ff-e855b4ac46c7 | -14.65934 | -51.46658 | 2026-10-08 16:37:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f5be9ba9-22fb-3f37-afc1-de38e18c3256 | -5.24708 | -37.57812 | 2026-10-08 16:37:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 53c28573-8e52-3fe6-a606-a2ad58393c1c | -6.51234 | -46.09856 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a914897-7816-3f60-bd87-2cfa827ae09f | -19.07821 | -48.64959 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b319fb2b-64d1-38ff-be3e-38b537c6c4cf | -6.41226 | -44.95812 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d4dc9b2-38e0-3309-9493-447da3d70223 | -7.89382 | -55.0074 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| abc3f2f6-c9c4-346a-8b38-e2f70ad3faff | -9.76014 | -44.79126 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f0ce4d12-da7b-3326-8d76-35be06eb60f6 | -11.01517 | -45.43508 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 33e4e08f-27c6-3c14-bd92-c8c36c3ce63e | -7.90397 | -54.71392 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 91da013e-d148-3792-9f06-3728ddbbd0a3 | -6.93317 | -43.66238 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| fd8cca60-b7db-31fc-8fab-57384fafe752 | -7.81965 | -38.85795 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 2f52ef20-1d94-3f50-86a5-f4d6f6253ecf | -6.86479 | -44.90295 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd43a56f-36fb-3052-ab28-3d5345c92a9d | -10.86367 | -45.55624 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f449f68c-663c-3729-a081-27ea027e4c25 | -5.98608 | -40.92619 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| cc3e7e07-65bf-3261-9d65-3d4cde4fc9ce | -7.48189 | -44.41501 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 11ce2502-0b19-361a-b23b-5f825521eb67 | -11.07685 | -45.77679 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4bed811c-403c-3b45-a5a8-7c2410614581 | -8.60736 | -45.64049 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 543495eb-52b4-3b7e-91c1-bf45512d07b6 | -7.40338 | -44.45341 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9b938584-1ebe-30fb-9a85-dcd6f45cfda6 | -11.08028 | -44.02321 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5e7fcd20-89f7-3a35-90f2-67ba83240bc0 | -18.73473 | -51.12693 | 2026-10-08 16:37:00 | NOAA-20 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d24f1d73-2897-36c8-ada1-a1efab4d2acc | -5.74351 | -41.7178 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| bd6d5ec8-84fb-378d-9240-9f642fdc8cdb | -18.98776 | -46.9475 | 2026-10-08 16:37:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1216c780-3652-38ca-89be-770327277aec | -7.05749 | -44.32473 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d53e3646-4bbd-3ecc-a81b-547c0bb8f0ac | -7.18912 | -44.30723 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f6c015b5-cb68-3abe-9da5-6f770b1a33ec | -9.88225 | -44.8574 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| bc22a60c-cf78-3860-a5cc-2ead0f55cd38 | -6.45286 | -42.80101 | 2026-10-08 16:37:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 74ca66ef-ba40-3c15-aa77-87a5b6256ec8 | -6.98194 | -45.13239 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1ca978a3-46c7-3742-ad64-0ad70ebc53b4 | -6.60175 | -44.84467 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b75cbed4-2fd5-3bff-81d3-69b3f20027ab | -11.14108 | -46.13708 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 8cf3d46e-ec3e-30ec-bcd2-fc4227a1e96f | -7.53973 | -42.08451 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 07fe6b2a-1634-3fc7-a78e-87327ef8ae6c | -8.94968 | -45.12652 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 89acef06-254b-3521-94a4-b422a5ba8687 | -6.60178 | -37.88774 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 00ad3168-3713-3d69-8610-93d116e2b92e | -8.19252 | -46.37502 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a804de9c-a66a-3664-864e-36242d15f704 | -7.88792 | -55.00457 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a62135ca-cedf-31bd-9f36-df4ed5be862d | -12.17922 | -44.81152 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8a71479d-0a42-3126-a9af-1ceffb61016d | -8.59754 | -44.86837 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7324ac59-949c-3170-8d89-44c563c12e3e | -18.30513 | -42.26575 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3d2dfcb3-b2ed-3a81-97a3-14ee2dd4cd78 | -12.16093 | -44.71358 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 10f0ecd7-fd1e-357e-bce7-571c94e19b8d | -8.20607 | -46.4198 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| f2cdbbf5-c467-342b-bdb6-870460e2b906 | -6.05321 | -42.59771 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| a0a851be-976b-3b55-88ad-bec3d9460195 | -6.44277 | -45.93328 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| dbaf89ca-5609-3358-a254-1670446efff6 | -18.82448 | -47.14225 | 2026-10-08 16:37:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 845b1bbb-b1cf-32a9-b087-86cd5d82d7df | -7.56771 | -46.68646 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 684e1490-0dba-352d-a6b5-d18098f297c2 | -18.69247 | -44.36482 | 2026-10-08 16:37:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0a20acd6-fa18-3ba0-a55c-7dde47a01c4d | -7.19244 | -44.26236 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0a67733a-8c44-32c6-bf8d-f672036549b6 | -6.14869 | -38.33733 | 2026-10-08 16:37:00 | NOAA-20 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 12.8 |
| aff80bc9-dd74-39f6-a44b-fb1c6ce5f3c4 | -11.11438 | -45.69037 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c8e584a7-0669-3905-b19f-c0c26241f8cb | -11.97546 | -39.04839 | 2026-10-08 16:37:00 | NOAA-20 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 140cbf0b-c148-324e-8e86-8813369aee9b | -7.16859 | -47.79122 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 37be9632-c661-3e0a-a65b-4f801bb1de1b | -10.90419 | -45.53195 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a57f0309-8016-36f9-a60f-9e3c0442f11b | -9.39753 | -45.88667 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0f9efb3a-1be1-39ac-be8f-125b6f140cd2 | -8.54943 | -46.91899 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1cc5f3fb-6166-32df-b7f4-733da2f44df7 | -5.96482 | -43.90075 | 2026-10-08 16:37:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 5dd6a027-20b2-311c-89d1-4002a420a902 | -11.83648 | -48.10389 | 2026-10-08 16:37:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README330.md)
