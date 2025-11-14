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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bbb5085-db0c-345f-a75f-1b6373d74b41 | -2.88357 | -49.47709 | 2025-11-14 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4eab6784-affc-3127-a4d6-09eaf06bf84f | -6.48081 | -43.76243 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0292acab-b26d-364b-9981-86b0ac933880 | -4.77894 | -47.8814 | 2025-11-14 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22ec0a3f-0460-3033-8eb5-90ceb4bbca66 | -5.75327 | -45.10756 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d81d6a9-43ad-3906-a6c9-3efe2bd12c72 | -4.32561 | -48.6382 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8aad5ed-cba5-3a32-8a74-1761e74e7f1d | 1.52965 | -55.65915 | 2025-11-14 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09b6f9d5-ea0c-36d9-98b4-7d395c56a2e1 | -6.06704 | -41.57751 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 73ccb6ed-6cb9-36fb-ad38-b22d666bf549 | -3.01495 | -49.44054 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb6a021f-124d-3c3c-bfc3-5e18f373b2e4 | -1.83142 | -53.80234 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed3377d8-993a-339b-ab5b-04c763803b7d | -2.88412 | -45.29385 | 2025-11-14 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c7244d4-ae3a-3a5a-9d84-bc99342e63f3 | -3.08517 | -49.27621 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b25a3ec9-b890-3cd7-bd57-c7f19bc60481 | -2.52091 | -47.80807 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b63b49a5-e013-3449-956d-4065b84134bf | -4.98829 | -43.88663 | 2025-11-14 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a65f43d4-df1f-3998-a8be-d9f1c640f6d2 | -3.76806 | -47.7277 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eaff2e7-bd6a-351d-b7c1-351bea96ffce | -3.99547 | -47.18767 | 2025-11-14 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73541cd-2290-34a0-a6a1-b1270d1784b9 | -5.31029 | -47.29494 | 2025-11-14 04:44:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92a71b1b-e887-37c7-9b9c-74029082f9b6 | -4.459 | -43.91739 | 2025-11-14 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb7dda00-243c-34aa-a627-cb63c30cf54a | -6.68809 | -47.79956 | 2025-11-14 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a077f96-d316-3470-afb3-66e23f9b6a0e | -4.70541 | -46.44306 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e20bc6b2-1134-3180-9b19-d27dbeb306e6 | -6.47228 | -48.37191 | 2025-11-14 04:44:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0333be-514a-3d5b-9fed-de1279727618 | -7.05502 | -45.06409 | 2025-11-14 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ded6795-d5f7-3914-9c78-77daecbf8e17 | -6.85217 | -46.76294 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 526201d1-e88d-3386-804b-0db75f23761b | -4.8213 | -49.72853 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebe9cef6-9976-352a-b8c2-b2af922fcac2 | -7.45997 | -42.58301 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb0a9a56-458c-3647-b0ce-116a4d4a14b0 | -2.6545 | -47.00194 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c11a5be-c6b0-3d19-bbe2-06fd3076a875 | -5.73962 | -42.7308 | 2025-11-14 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1607dea-6392-3f48-a867-9bdd6194a976 | -5.3623 | -46.29459 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| bc7a65ae-6e3e-340c-9a0b-b1202d33cd15 | -5.54275 | -41.81713 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b8f5e36-1b7f-3951-9d20-a268b70c13e2 | -7.3534 | -43.35956 | 2025-11-14 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fce0275c-63fd-3126-a5cc-a670c91e8502 | -5.75344 | -49.25903 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9763da26-8565-3e7f-84be-d381fcbcd461 | -5.34897 | -46.76209 | 2025-11-14 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab5e16d7-3600-3692-9230-acb8066da67f | -2.8801 | -45.29328 | 2025-11-14 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74678bdb-eec6-3e56-9eb7-ca590b45b417 | -6.06143 | -41.56668 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 153094ee-77a1-39bc-9348-065f97d86b49 | -2.11066 | -45.36698 | 2025-11-14 04:44:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d80806-9cdb-3e31-ad66-a34f4d5631eb | -5.79097 | -43.73831 | 2025-11-14 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b65e420e-e611-374b-833c-0f2d3bca558b | -4.59058 | -44.40245 | 2025-11-14 04:44:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cb58f42-84f0-35f4-910d-b0b288327784 | -5.42074 | -44.81075 | 2025-11-14 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe71b111-da3e-3392-9c2a-8f5e9527b71b | -3.76166 | -47.74358 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e3d1edb-50bb-3971-b4ce-6a01c4052d87 | -4.59558 | -49.62915 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ea6b3b2-edc0-3c3e-a23e-b6544979566c | -2.94262 | -49.36148 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6f8d452d-7b3c-3be8-bade-1f553b33941d | -5.41891 | -43.2644 | 2025-11-14 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b91074e3-7b58-3bf8-8af0-15eb92b2194b | -1.8004 | -52.08622 | 2025-11-14 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d3f9cb2-35f9-359d-8e1e-a84a73c63a07 | -4.42112 | -47.60024 | 2025-11-14 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a45f7b0-042d-3323-8f55-3c015eb992dd | -2.94317 | -49.35799 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6ea27195-6e4d-30ff-8cc3-f00a0cb85c34 | -3.79748 | -51.3712 | 2025-11-14 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed03417c-3aa8-3131-a759-0b55548b5e61 | -3.35234 | -46.86826 | 2025-11-14 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 248abae3-4ea9-3b02-9dd2-fa6558535c1a | -7.05865 | -43.58648 | 2025-11-14 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d472b58-7a26-3b13-a8a0-dc79ed6e0f8e | -3.30407 | -50.10873 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 428120b4-eb58-38fb-ad57-c1b7360675b7 | -3.85316 | -52.29984 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db7bc190-5392-37af-a563-01d794c63b3f | -4.10764 | -50.05482 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1d4adb7-c6ff-3e82-92d2-7ea66479890a | -4.60789 | -43.35374 | 2025-11-14 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99eb8178-5660-39f6-9242-b3f29d15d9f7 | -4.77714 | -46.45134 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1c6976f-8c99-3470-8b73-133d7725b29f | -0.16414 | -50.40843 | 2025-11-14 04:44:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7cdab81-aba2-32bd-be96-45550a6c9333 | -3.62526 | -49.10326 | 2025-11-14 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dba0843a-ff55-34a4-82b1-493063aa3a32 | -6.73695 | -46.06829 | 2025-11-14 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a30a8704-2855-3a3d-bc08-5971814987b6 | -3.90969 | -54.68921 | 2025-11-14 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc8115c6-5b7c-3702-8455-e8bed39d197c | -5.36772 | -46.2852 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e35f670-c5df-3454-8a2f-cc2e4a7288ad | -3.80734 | -43.59867 | 2025-11-14 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca01f92d-6f32-32fe-981e-2ecb1a40aded | -4.92553 | -47.87058 | 2025-11-14 04:44:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bc631ca-32be-3483-be77-4dcd449fe599 | -3.98053 | -44.65293 | 2025-11-14 04:44:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4489d459-1338-3a05-bd3a-856435e8cc15 | -0.86419 | -47.31136 | 2025-11-14 04:44:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ef2eb59-74ed-31d4-a7c6-c58af6e45f68 | -7.00321 | -42.78902 | 2025-11-14 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 93318faf-3def-38dc-b796-7a8d17210f91 | -4.77102 | -45.58567 | 2025-11-14 04:44:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f08e4b66-3025-3c4b-a44c-47628719236c | -4.98243 | -43.88886 | 2025-11-14 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecfdde2d-451a-389b-96d6-989e3a64e11d | -7.15079 | -41.26028 | 2025-11-14 04:44:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 580a2edf-4187-39d8-ab4c-b86abc9125cb | -1.37352 | -52.53207 | 2025-11-14 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8413afdd-abc4-367b-a184-4de03e6ecf8c | -3.80278 | -43.59799 | 2025-11-14 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 1e709a74-5287-3ba2-a0a4-a79b19618533 | -3.0094 | -49.43254 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f819a8c-2ec8-351c-830f-3ec9de3b43b8 | -1.83287 | -53.79341 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41410ee3-faba-3736-aa85-3e0119e1df17 | -5.20613 | -50.63026 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c8d13d1-4870-3dce-964d-a3096e4ec0aa | -6.06736 | -41.56395 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 912dbcea-d4cd-3ab2-82dd-0111388b4a31 | -6.06749 | -41.5742 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 192df18f-c1fd-37c7-b202-70a464e280cd | -5.30005 | -45.07592 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a653764-8842-3d52-84ca-6742f01cde09 | -2.75326 | -49.52756 | 2025-11-14 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18e66738-db1c-32cb-a776-6b8794326289 | -3.43016 | -42.42601 | 2025-11-14 04:44:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3aa37b17-8e3a-3a19-9bb7-01ca9adb450b | -3.98248 | -48.00284 | 2025-11-14 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 436a3669-2595-354a-a15b-023b42cde16c | -6.26898 | -47.70358 | 2025-11-14 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7a387de-3ebb-3ed3-b6a2-5399e4b77eb5 | -6.09563 | -41.61084 | 2025-11-14 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85534e2a-aae5-348d-a362-8408abc04ebb | -5.72703 | -42.36072 | 2025-11-14 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 265d0786-faef-3c23-9282-410bb0f0ff3b | 0.71615 | -51.37133 | 2025-11-14 04:44:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d63d4a3-c091-31da-822d-afc351307235 | -4.46678 | -45.82917 | 2025-11-14 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0665c86-ebb1-3db9-a107-963538095117 | -2.16454 | -48.42793 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d347196-8ef0-36b6-abde-5d59c7e35f8a | -6.72252 | -42.03198 | 2025-11-14 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dd5620f5-c265-3d94-9121-572abee3e5b5 | -3.81646 | -44.25203 | 2025-11-14 04:44:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d14c69f7-00f2-331d-87b7-b0df5999066f | -3.30131 | -50.10478 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20b841bb-4bd5-3699-9575-97114bc9922a | -4.88497 | -49.38749 | 2025-11-14 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa7e4d10-689e-3b58-bf6c-79dc62f5fe96 | -5.5233 | -46.37247 | 2025-11-14 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd670fe4-1399-31b3-901c-78b2e2eb9c4b | -6.42753 | -47.30104 | 2025-11-14 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50cbf1cf-256e-3fde-96ea-7a32db14a006 | -5.59193 | -45.17588 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc5227e4-706b-3c16-94cd-9bed4a690c83 | -3.36059 | -49.51212 | 2025-11-14 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7571a33-e09a-3949-8d70-0a79110709fe | -5.85609 | -47.49178 | 2025-11-14 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e5e2497-6e3e-32ea-ac72-252a12662755 | -5.45978 | -47.10134 | 2025-11-14 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d24e023b-99b3-30e8-ba32-be68d993f436 | -6.8873 | -42.85305 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 6c4b9caa-f304-3957-85b5-0b7fc4d9fa24 | -5.48739 | -47.69907 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6da86cf4-dbd5-3658-a0ca-f7e38a8c1a1e | -4.10309 | -48.01687 | 2025-11-14 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 523e1a45-7b9c-3d1e-bd55-d3763189151a | -4.71774 | -42.94052 | 2025-11-14 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 842ad07d-e0e9-3851-ae49-1e736deb30fb | -4.71519 | -46.44688 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4f8eb120-d657-3a65-a9d1-fff8de7d24b1 | -5.97836 | -42.59764 | 2025-11-14 04:44:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f72cbfdc-5b4d-346e-8b1d-bc07155c3a2c | -4.30232 | -46.27139 | 2025-11-14 04:44:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c6bd5ca-5c1b-3faa-bae2-92d6cb94eecc | -6.57229 | -47.90007 | 2025-11-14 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README44.md)
