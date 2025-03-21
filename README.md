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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a99152-eaba-33da-83c5-3a966d6da62e | -19.444 | -54.7708 | 2025-03-21 00:00:00 | GOES-16 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 40.2 |
| b6255811-20a8-362f-97d5-5d726576f0fa | -30.7106 | -54.1727 | 2025-03-21 00:00:00 | GOES-16 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 73.2 |
| 787c4ed6-a240-338a-9cd4-383bf15a49e9 | -11.8921 | -40.956699 | 2025-03-21 00:06:00 | METOP-B | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e8318248-2172-32ab-a73f-a025d8f8990b | -11.8942 | -40.965302 | 2025-03-21 00:06:00 | METOP-B | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 783f8436-940b-3842-8ac2-8fe422034866 | -21.1884 | -48.783401 | 2025-03-21 00:06:00 | METOP-B | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6a356d34-92ad-3159-b3e9-0417ffb4cb92 | -11.4868 | -40.0308 | 2025-03-21 00:06:00 | METOP-B | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fda0ca8a-63a4-377a-8045-37d49b4b2066 | -13.67 | -52.1343 | 2025-03-21 00:58:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df4993e2-6c54-3d84-938b-92ba41f13094 | -20.917999 | -56.5312 | 2025-03-21 00:58:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 692e990b-f605-307e-8e53-1ad31fc12aa3 | -19.434099 | -54.778099 | 2025-03-21 00:58:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e1f9a930-c01a-3445-8591-15e585ae55d4 | -19.424299 | -54.780201 | 2025-03-21 00:58:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eaef9864-a4ae-3531-9c14-703fe8178d60 | -13.6766 | -52.118 | 2025-03-21 00:58:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98896165-2638-3c7a-a025-0d771a8150cc | -13.6782 | -52.125 | 2025-03-21 00:58:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a1657ab-07d5-3db3-b394-31dfe414157c | -20.9203 | -56.5439 | 2025-03-21 00:58:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dd89fe46-249a-332b-b85f-fa0869bfb9d2 | -19.432199 | -54.768501 | 2025-03-21 00:58:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f710e74b-a858-3534-aa7c-8c5e2ffacc49 | -13.6798 | -52.132 | 2025-03-21 00:58:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88fbf5d7-af60-3a11-80e5-4ecaff7c401a | -30.7097 | -54.168598 | 2025-03-21 00:58:00 | METOP-C | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 693dc534-a798-325e-b647-93cd717359af | -13.6684 | -52.1273 | 2025-03-21 00:58:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92739f15-01b9-3ef3-9dd6-559677927722 | -19.436001 | -54.787601 | 2025-03-21 00:58:00 | METOP-C | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2a9ec315-174f-3fea-8141-f7aad7c3dd87 | -23.7526 | -55.415298 | 2025-03-21 00:58:00 | METOP-C | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93d3b0cb-1721-39da-a966-447206707fc6 | -27.850201 | -50.174301 | 2025-03-21 00:58:00 | METOP-C | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc644c79-f6f0-3ebc-90e7-02157f241d8f | -23.7624 | -55.4133 | 2025-03-21 00:58:00 | METOP-C | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57d14ae9-223d-3ee6-b992-d9dcb186cbec | -19.444 | -54.7708 | 2025-03-21 01:10:00 | GOES-16 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 3b146688-6b4f-379b-b3b8-b36ce15669df | -13.6761 | -52.1274 | 2025-03-21 01:10:00 | GOES-16 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2a342be3-ef27-3a1e-81d2-06a45cb2f856 | -30.7087 | -54.17602 | 2025-03-21 01:15:00 | TERRA_M-M | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 10.8 |
| f80f7e03-7a8d-3e99-9a5f-55f0940c2d98 | -30.71013 | -54.18768 | 2025-03-21 01:15:00 | TERRA_M-M | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 28.6 |
| 52530f5e-d53f-3eac-92ed-ac47f48beb96 | -27.85193 | -50.18227 | 2025-03-21 01:15:00 | TERRA_M-M | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 9758b7d2-dd97-39cd-9cf8-ed58111b739a | -30.43858 | -53.48352 | 2025-03-21 01:15:00 | TERRA_M-M | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| c6385571-67be-3632-86dd-0a468b6ee948 | -30.73029 | -54.19588 | 2025-03-21 01:15:00 | TERRA_M-M | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 9.8 |
| 11b63495-194f-3837-bdb9-41aa3b9d4972 | -30.71806 | -54.17436 | 2025-03-21 01:15:00 | TERRA_M-M | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 6.3 |
| 525474c8-272f-3993-8afe-8ab1e8341f13 | -19.43722 | -54.78098 | 2025-03-21 01:17:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| cead1291-8ef6-373b-b7c5-07251362a187 | -19.42964 | -54.79173 | 2025-03-21 01:17:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e2d8d595-638d-3844-9e6d-1faa05e37328 | -20.93012 | -56.54945 | 2025-03-21 01:17:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7257dc8b-ef3f-3eaf-b51e-7446cb4abbac | -19.43851 | -54.79035 | 2025-03-21 01:17:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c22dfadf-adb0-384f-ae54-b5202c252dd1 | -20.92067 | -56.55075 | 2025-03-21 01:17:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a42fd997-ba2e-344b-8f54-7862e180cda4 | -20.91932 | -56.54007 | 2025-03-21 01:17:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0ecdc76d-bea4-36aa-8aad-84ca23ff8ed2 | -23.75884 | -55.43215 | 2025-03-21 01:17:00 | TERRA_M-M | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 426b441c-3126-31eb-a3c1-8bac8763ef60 | -19.42835 | -54.78236 | 2025-03-21 01:17:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d45cce43-ff75-391c-903b-f8c75b262b48 | -22.94073 | -51.09841 | 2025-03-21 01:17:00 | TERRA_M-M | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c88fef56-1ccf-3bf2-907e-4350e462a79a | -21.11787 | -55.66518 | 2025-03-21 01:17:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ee1408fc-1d5c-3bf2-928e-b6f5bd900639 | -13.6761 | -52.1274 | 2025-03-21 01:20:00 | GOES-16 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 404c480b-efed-3b63-ac57-8c6c685efd66 | -18.0022 | -54.00968 | 2025-03-21 01:20:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c9926ad-eff9-3b73-8826-3eb8a768869c | -12.94164 | -55.94165 | 2025-03-21 01:20:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a41bd1eb-aa3b-3d9b-99a3-155fee01d6cb | -15.59554 | -57.3335 | 2025-03-21 01:20:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2de95245-a4a0-3ca6-9260-944ee5d34237 | -13.67845 | -52.13194 | 2025-03-21 01:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9cce638e-a96b-35ed-a785-5301e07a989d | -13.6682 | -52.13368 | 2025-03-21 01:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4740c054-c72f-3c26-9dc6-827a2411d2aa | -11.95425 | -55.91864 | 2025-03-21 01:20:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d3bf7c9-8603-380a-be64-be033bd11ca2 | -6.92782 | -35.13408 | 2025-03-21 03:15:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| bfa4498c-a8b0-3498-8b91-b73e856620b2 | -6.92349 | -35.13334 | 2025-03-21 03:15:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| b997a25c-64e6-35f2-972e-3cd6f7ec6838 | -6.92711 | -35.13824 | 2025-03-21 03:15:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 89873657-7074-3616-9eda-f71a00045780 | -6.92279 | -35.13749 | 2025-03-21 03:15:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 47acba16-d24a-34c9-b616-6e45457cd546 | -8.86983 | -36.43387 | 2025-03-21 03:17:00 | NOAA-21 | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aea81a24-6d0c-3c65-9381-74fac9ed95fb | -8.39321 | -35.0255 | 2025-03-21 03:17:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3db7e68c-844e-3c26-bfe2-4ab017422fe0 | -8.38902 | -35.02476 | 2025-03-21 03:17:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b056816a-15ac-3957-9f21-afa944a7e248 | -15.79951 | -42.03601 | 2025-03-21 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 74a958b0-b1d5-303f-a120-cc981255b708 | -17.46837 | -39.24382 | 2025-03-21 03:19:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 01b90758-18d4-3568-ba02-047b179bc4c3 | -18.11861 | -39.68628 | 2025-03-21 03:19:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 133941b8-aeec-38ef-9fa3-7228d65826c8 | -19.83396 | -40.11237 | 2025-03-21 03:19:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 522aa21f-1379-36ad-b45f-da6b1853308e | -18.11999 | -39.6837 | 2025-03-21 03:19:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ea1870d3-3543-3bd4-bbfb-86ebd6d6b2a6 | -17.46365 | -39.24285 | 2025-03-21 03:19:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e1c6886c-93aa-33a3-9e2c-e4f6a7da79c9 | -13.35924 | -41.3413 | 2025-03-21 03:19:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e685638c-6c81-3b60-9ee1-170019f7cc47 | -15.80046 | -42.03155 | 2025-03-21 03:19:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 57c31169-e81b-3258-a365-efc518a7cc1c | -20.12735 | -46.78954 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c4b6dee0-1958-3ad6-95db-fb1438746232 | -20.11851 | -46.76571 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 53d7d9d1-043a-3144-88ff-bb7bf8a6c36f | -20.20727 | -46.67606 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05ce7bbf-6aac-3dd0-978e-9d3a604502ee | -20.11835 | -46.77675 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 83919f6f-9320-3e89-93ba-e6d34180b908 | -20.12199 | -46.78134 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40a93e3c-5498-3730-ba78-a8f05a806e20 | -20.12391 | -46.7737 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0979cbfa-c2bd-3421-a750-dc7c2fbb1a95 | -20.13098 | -46.77504 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d6abf95-5f8a-3af8-b560-73422367d6d8 | -20.11663 | -46.77316 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2235005a-e8ca-3433-826a-8337f31065d9 | -20.12021 | -46.7691 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 15785763-36d9-334c-a536-53fd78b349e0 | -20.13084 | -46.7862 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3caf29b3-8568-3537-95f1-a355758df43f | -20.1255 | -46.77776 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b982de2b-b037-3939-96bb-8277809f9985 | -20.11274 | -46.76941 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb2aad65-a119-31f7-a99d-848e2dc9aca0 | -20.12915 | -46.78237 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be1f83f8-c34a-309b-83e5-283df3d98d57 | -20.21334 | -46.68123 | 2025-03-21 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 455734bd-0066-34d6-bb8e-795f7d7a3043 | -2.92984 | -39.98148 | 2025-03-21 03:40:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68de3edb-d4b9-3407-b7cb-fcfb9762d614 | -8.39204 | -35.0257 | 2025-03-21 03:42:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6053f965-49b8-309b-af9a-c5c1876d3835 | -6.9268 | -35.13691 | 2025-03-21 03:42:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c7a558b1-047f-3ff3-ab4a-642f057357fb | -8.67445 | -36.24018 | 2025-03-21 03:42:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a1688525-edba-3377-acc4-733b866780f1 | -6.92735 | -35.13344 | 2025-03-21 03:42:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 45a1f49c-1b12-32fb-a3c4-ab20fe44c62a | -8.87038 | -36.43391 | 2025-03-21 03:42:00 | NPP-375D | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 84519d4f-eba3-3274-b89e-c9270da05dff | -8.38916 | -35.02551 | 2025-03-21 03:42:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ba5b8e78-07f4-3a0a-bcfa-7f0522a68bb8 | -8.8791 | -36.52938 | 2025-03-21 03:42:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 098e5372-6745-3214-9034-10b08d7ec933 | -7.21875 | -35.79257 | 2025-03-21 03:42:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1925e5db-31e1-3f1e-83ab-acf4f3f947e8 | -9.11515 | -40.61827 | 2025-03-21 03:42:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b7c1086-2044-341c-9bac-4b73fa329350 | -9.11575 | -40.6148 | 2025-03-21 03:42:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 188e9bcb-34b0-3fd4-9738-eb06e037a1a9 | -8.87372 | -36.43443 | 2025-03-21 03:42:00 | NPP-375D | SÃO JOÃO | PERNAMBUCO | Brasil | 2613206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e1faa08-9416-3418-ae02-e18ba41502a2 | -6.92403 | -35.13292 | 2025-03-21 03:42:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2d7dd61c-a133-387a-bc4d-f4d18e86a3f2 | -6.92348 | -35.13639 | 2025-03-21 03:42:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 296a7fe4-5453-3926-8b4f-02523a929a79 | -10.36655 | -38.27422 | 2025-03-21 03:45:00 | NPP-375D | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c7007e80-44c9-3e63-b0f6-75993050d1cd | -12.78467 | -45.40157 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d31ed6bc-9a1b-3c09-8440-a109460d5fc2 | -12.04747 | -40.47612 | 2025-03-21 03:45:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ecbc96d-b24f-3fc5-9bdc-15b202def092 | -15.80361 | -42.02842 | 2025-03-21 03:45:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 70eb22f9-de48-334f-a1bf-62f07ca48959 | -13.3598 | -41.34146 | 2025-03-21 03:45:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 77fb3133-cbbb-313e-8e80-9dfead9a8fe5 | -10.52734 | -37.34153 | 2025-03-21 03:45:00 | NPP-375D | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2449e032-2334-3070-a61a-253331ddbdc8 | -12.77792 | -45.40403 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9a86555-d113-3d6a-a891-680b7a5f5da7 | -10.24464 | -40.51315 | 2025-03-21 03:45:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1da32e50-bfd2-3057-8f53-8e0279356e56 | -16.13611 | -42.32877 | 2025-03-21 03:45:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cbc9bb1e-1412-3fba-8a64-da1e383668f3 | -12.05078 | -40.47416 | 2025-03-21 03:45:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 59f7cb0e-850a-3350-8bef-4738cac9ed5a | -12.78981 | -45.40266 | 2025-03-21 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README2.md)
