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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9c07f01-0f54-356b-9eca-859a02911a64 | -7.7567 | -44.0415 | 2025-10-09 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 3b6ea481-86b6-3396-be1c-ce20f17b1336 | -6.6806 | -46.3184 | 2025-10-09 03:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2afa0e01-87a0-38a8-b016-d22e1a76a2c0 | -8.1993 | -43.3424 | 2025-10-09 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| e28be4a2-ca41-3b32-b20b-a0548347007b | -18.0589 | -44.9632 | 2025-10-09 03:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 00a9d1c5-ce55-3cb5-8777-a6aa8545c732 | -18.0213 | -50.4547 | 2025-10-09 03:10:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ddaa6718-ff04-386d-ab02-cc8dbcd29d07 | -10.5464 | -50.0188 | 2025-10-09 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| b839d5ae-268e-386a-b02d-bb390fdb8bc3 | -6.6808 | -46.2961 | 2025-10-09 03:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 31e7e79b-bbfe-34cf-8c5a-c7fefb9a1b92 | -5.3224 | -43.392 | 2025-10-09 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 7d6ebf68-c5cc-3b9c-a984-aff0473450ab | -8.5587 | -46.2162 | 2025-10-09 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0eb8f0ee-bd28-3706-88fb-6e26279d23b0 | -8.5401 | -46.1957 | 2025-10-09 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| e87057d2-0f2a-3b33-b799-5ac703c71147 | -16.0042 | -50.8147 | 2025-10-09 03:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 6c324de5-e043-3186-82e2-be79ef0d8002 | -14.4334 | -43.9635 | 2025-10-09 03:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7f9587c4-aca1-3c81-b1c6-64747b7b1369 | -6.6806 | -46.3184 | 2025-10-09 03:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f163ec12-8050-363a-8e44-95008011cdaa | -17.6421 | -47.1871 | 2025-10-09 03:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 1034687c-1669-3744-b059-7327c02f84a3 | -17.9227 | -57.4922 | 2025-10-09 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.9 |
| 2f71a9c6-f66f-3e05-9dac-82c1bb4ee76c | -17.6415 | -47.2103 | 2025-10-09 03:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a06b1f78-1072-332b-a98f-f68b7896e1ca | -17.9224 | -57.5128 | 2025-10-09 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 8de3dd76-7737-3385-8d3d-98c4df250ee3 | -8.1993 | -43.3424 | 2025-10-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 4597a373-1953-3e0b-9531-a0701eae455e | -5.34 | -43.5303 | 2025-10-09 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 72c6a0e2-7489-315e-9c56-5f65160f3ccb | -14.4138 | -43.9672 | 2025-10-09 03:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2e8e6124-7181-3371-b999-90331bd5dbdc | -6.6993 | -46.3169 | 2025-10-09 03:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| fba2ca60-963b-397c-8d99-87663f1aa155 | -18.4118 | -45.2394 | 2025-10-09 03:20:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 120.3 |
| a995a450-c802-396a-96c3-069999cb4bbf | -6.6808 | -46.2961 | 2025-10-09 03:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| adec7944-e648-3db6-8d8b-6f154bce6a57 | -6.6995 | -46.2946 | 2025-10-09 03:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 0afdaa4b-3722-33c4-aee9-34431696a454 | -18.0413 | -50.4511 | 2025-10-09 03:20:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a9496724-349a-33d2-bdc7-1b6db5c4c92a | -5.205 | -37.6279 | 2025-10-09 03:28:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 08ac0929-09e0-387c-aaa2-09f6de351b7e | -4.50994 | -38.82477 | 2025-10-09 03:28:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f3f15577-f9c5-37be-9cb1-30b32c261607 | -4.89531 | -42.25338 | 2025-10-09 03:28:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e9deff1f-b3f6-358a-9809-f988aab2142a | -4.00908 | -43.28382 | 2025-10-09 03:28:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6099ab8-a5e6-3647-a2eb-d83f1447a8d8 | -5.96254 | -35.58051 | 2025-10-09 03:28:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 306233bf-d036-36cb-9a30-30ab9a6db862 | -4.01196 | -43.28644 | 2025-10-09 03:28:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0327c002-b869-36a1-98fd-d819013ac5c1 | -4.0082 | -43.28898 | 2025-10-09 03:28:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b99a911b-cc5e-3209-9874-cf9872541491 | -5.6336 | -35.45556 | 2025-10-09 03:28:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e770426-7a43-357f-bccd-272d9e731782 | -4.72789 | -43.35271 | 2025-10-09 03:28:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 13148f6b-5d40-3f48-9710-643b7ed211ee | -3.64533 | -39.37304 | 2025-10-09 03:28:00 | NOAA-21 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eea299fe-1da2-3c0c-9f93-07afc5cb2ae0 | -4.51471 | -37.93103 | 2025-10-09 03:28:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 96b6b908-55f5-3a29-b62c-b505e475beb6 | -4.61084 | -43.15248 | 2025-10-09 03:28:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 646925da-911e-386b-baa0-428b3b04567a | -5.63729 | -35.4561 | 2025-10-09 03:28:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee1890f6-adc2-3d79-b841-80f926d4d3c4 | -3.26055 | -39.42229 | 2025-10-09 03:28:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b1444bd-d4ff-3517-a336-bfc8bd9996bf | -5.13359 | -37.55919 | 2025-10-09 03:28:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 46495a38-3ae5-3fb5-a6e1-3775e6656b80 | -3.3655 | -43.37952 | 2025-10-09 03:28:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2456afd7-063a-303f-b1f6-4169fcb3754d | -3.85924 | -41.53148 | 2025-10-09 03:28:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb16d1ee-bd00-3497-a9cf-2a7a16308b7a | -4.62276 | -43.43397 | 2025-10-09 03:28:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa8921e9-2590-3807-a2c4-3b6a927df793 | -4.88947 | -42.25242 | 2025-10-09 03:28:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e292a7c5-326a-3008-aba5-306a1f5f7e53 | -5.13782 | -37.55988 | 2025-10-09 03:28:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 10f2b018-047a-36f4-8cba-f4dad5233aae | -3.25558 | -39.42152 | 2025-10-09 03:28:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a3c8473c-0ddf-34ff-8d47-9d4dea7e6fb4 | -6.6993 | -46.3169 | 2025-10-09 03:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b4b07228-57b8-311f-bd0a-1c3a29741ef2 | -17.8413 | -57.6459 | 2025-10-09 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 7a8bbd29-f363-3f57-9a61-d59580cf9946 | -14.4138 | -43.9672 | 2025-10-09 03:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 43c578c3-57ef-3f3b-a382-2273ebe33516 | -14.4133 | -43.9911 | 2025-10-09 03:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| af2e8329-10c3-3291-b385-ab69cdcad82b | -6.6995 | -46.2946 | 2025-10-09 03:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 9fe81bb5-5ccd-3a09-b5c6-63583e9785c1 | -8.1993 | -43.3424 | 2025-10-09 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 8cbeeaba-d1bf-39ac-ac32-17db949880b8 | -16.7518 | -43.9645 | 2025-10-09 03:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ca87e8e2-1265-3d5c-a12b-1bc8168ac411 | -9.0829 | -47.9594 | 2025-10-09 03:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| fa639600-4cc8-34ab-8b04-30c927cbb148 | -18.4118 | -45.2394 | 2025-10-09 03:30:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 94a9ff5c-685e-38cf-936a-fa4385e930c3 | -6.6808 | -46.2961 | 2025-10-09 03:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| e3a0f292-fbe7-348e-bad2-9f2714cf843f | -5.04769 | -45.63395 | 2025-10-09 03:30:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bac8a01c-db2d-367b-b444-d74c75800cd8 | -7.76702 | -44.04038 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a55fcd0e-62d3-3af7-913c-d023e09dc558 | -8.41167 | -41.45233 | 2025-10-09 03:30:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 363ccecb-a285-3ce7-a1ca-19b29be0a9dc | -8.5168 | -46.22865 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bc7f2639-5d4f-3340-a7f6-b3bbf2595b59 | -10.82634 | -42.821 | 2025-10-09 03:30:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47fe48df-80cc-31ed-b567-002042249d09 | -8.53337 | -46.20876 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| d8bac274-b384-3717-825b-a429397df993 | -6.65708 | -35.09452 | 2025-10-09 03:30:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6bf1310c-bc27-3e7b-bbcf-25b19ffcc578 | -7.76275 | -44.02901 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0814a2de-871a-3725-b1f3-87c245f1d360 | -7.73351 | -42.41124 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0aa21c26-c2ba-3a4f-94c9-73e2714cb669 | -5.03327 | -43.60902 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ecbd7b87-8bb1-380b-9f73-a1393aa1ed67 | -5.40287 | -40.98635 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0fdbee17-e7bd-32bf-83f8-e026bccc7866 | -8.54916 | -46.21087 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8a8e9995-c648-31f3-86e4-6253b801603d | -5.39755 | -40.98544 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cfebb3e4-9e7b-32c2-a097-0938aa024a88 | -10.03356 | -42.31426 | 2025-10-09 03:30:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 603dfbb5-fb7e-3c39-94e7-6ccaa815f66d | -5.55011 | -41.30288 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 587f4aae-346a-3a19-98a8-d4eec622067a | -8.19928 | -43.34703 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| eb7f67f9-ae94-3004-8d20-34c1db7c758f | -10.93723 | -42.83682 | 2025-10-09 03:30:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70263fe1-e40e-37fd-8504-36473e00f5b1 | -7.76176 | -44.03418 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c4e3d5b5-f1d3-3cd4-a7c7-f5407140c152 | -7.76597 | -44.04593 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9a02d780-8e15-338b-ad32-9ae6c66788ae | -8.20272 | -43.34857 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 97c82de8-5e35-33e0-9678-a47941068ba4 | -8.2019 | -43.35285 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 804725a9-d78b-3a3e-beb6-386e436a99bd | -8.55507 | -44.62554 | 2025-10-09 03:30:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80475a8b-8186-3da5-bba5-6bf675a30c5c | -10.19742 | -44.5529 | 2025-10-09 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1e43dcf-e535-357d-9dec-2279d08511c6 | -7.27673 | -41.97702 | 2025-10-09 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07a7e5bd-c701-3f09-98c7-086b24a42764 | -7.76753 | -44.04686 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 67b7d146-4457-3ecc-a2c8-06efa0b9028f | -8.54664 | -46.22405 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| fa8d02c2-a5de-34fc-8466-bf1612728156 | -8.50924 | -46.22077 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 5e3e89e9-4d89-3ddd-b709-e85960ec6368 | -9.88853 | -36.04742 | 2025-10-09 03:30:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d65a3d48-6bcc-3c21-98cb-26cce21705d4 | -8.62504 | -45.13262 | 2025-10-09 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53847e25-9f31-396e-ac1a-d03fad79b32e | -8.51488 | -46.22884 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 295ff5f6-f72b-3078-9be8-c8f8536eb7ea | -5.40231 | -40.97978 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1a0f1d1a-0dea-37c2-9268-f5db90d6871e | -7.02075 | -42.74844 | 2025-10-09 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0b2aae88-b226-3a3f-9f79-209d45331ea7 | -7.55377 | -35.20774 | 2025-10-09 03:30:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 10d3459e-5078-3c70-8d71-24519f77cd73 | -7.77479 | -44.0423 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e5f853d-c233-3899-82ce-8dc3dfa66724 | -4.9837 | -45.12507 | 2025-10-09 03:30:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c559edf-0139-3435-b1dd-9eb8bb881421 | -8.63051 | -45.13936 | 2025-10-09 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c5dc11a-2007-3563-8b76-fc613af3cda2 | -5.40406 | -40.97931 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f270ff37-5fb7-305b-b780-89cb228b5a66 | -10.03057 | -42.31518 | 2025-10-09 03:30:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ebe3c605-0291-3cf2-bd0b-fb6f5b5907f0 | -5.30773 | -45.37746 | 2025-10-09 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc79de51-bab4-3a3f-9ee5-d30fdb9ee741 | -7.35183 | -43.86412 | 2025-10-09 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b92a988f-3c01-3ac8-8a19-a9d0895c0482 | -8.54606 | -46.21772 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ae33afc2-7bd2-3fe1-8946-6cca21c2ea80 | -7.7607 | -44.03974 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 96382d62-f2a9-3a8c-8c0c-fec85bf69920 | -7.48785 | -43.1135 | 2025-10-09 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9fb5282b-4043-3f2f-adb0-303ba819a995 | -7.67434 | -42.57832 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README10.md)
