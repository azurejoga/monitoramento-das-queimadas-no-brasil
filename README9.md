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
| 6cee2331-01a5-3cdc-a0ce-2ae4caae99ac | -3.03828 | -45.35326 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7ce9396-1473-33b6-abce-3b5289924b01 | -1.4521 | -46.87956 | 2025-12-17 04:25:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c44ba1-fce0-3c4b-804d-0d9c9ee9173e | -5.98163 | -44.59248 | 2025-12-17 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 291713dc-ec7f-3cac-95ed-4ff06f0da569 | -2.73392 | -45.30168 | 2025-12-17 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05467a71-bda5-32de-9059-9cd33aa79ab4 | -1.32789 | -45.81367 | 2025-12-17 04:25:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f72ed59d-ef64-3706-a35b-e3fb16d2167d | -3.34403 | -41.79776 | 2025-12-17 04:25:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f251a62b-6825-36ed-93e4-f34cfb5214d4 | -4.32754 | -44.82082 | 2025-12-17 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6404bb5b-2364-336d-9b62-aa8c0732efe5 | -2.77055 | -48.57282 | 2025-12-17 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b48b7dc9-fdcc-3d12-85ae-d7758995e84a | -1.30181 | -47.25412 | 2025-12-17 04:25:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 707b8a81-db7e-32b0-8b7f-7d34b27230c0 | -3.95013 | -40.93613 | 2025-12-17 04:25:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5e91cced-19e3-3164-a953-38ec6f14dddd | -2.49147 | -47.11426 | 2025-12-17 04:25:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fb5a17d-da15-3f10-9d40-0a1f761d3a33 | -5.59365 | -44.88462 | 2025-12-17 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01be060f-191b-3d9f-bdba-05cf17537b98 | -2.93086 | -48.2285 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35886e69-7e74-343f-87e7-4cdc568528d1 | -2.62861 | -45.66565 | 2025-12-17 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcfc017c-a535-31e9-803c-d32d4e5d8c56 | -2.44631 | -49.02818 | 2025-12-17 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60f7aaba-be5c-3fac-bf96-14746b867e7e | -5.3629 | -36.84285 | 2025-12-17 04:25:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65a4f4a1-de7f-325d-98fe-6a60df9d9416 | -2.36634 | -47.6814 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3003da77-1354-38c3-8bb9-909a4e117de9 | -2.30167 | -46.1438 | 2025-12-17 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e240879-21dd-3f8f-9250-7c410d86951d | -2.66724 | -51.64905 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 293817d0-c8d5-36d6-93cc-38e56deeafdb | -2.69797 | -45.70096 | 2025-12-17 04:25:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac038f71-a8cc-39b0-9f59-ccc3f6bcbef8 | -3.65978 | -47.55343 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bef14583-fcc3-3452-8ca0-5c4f7e3f9d2b | -2.94694 | -40.44468 | 2025-12-17 04:25:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cc11e3d-591b-3afe-81ee-166920f78dd9 | -3.18033 | -48.02827 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 437a3d7e-efd1-37da-bba3-8aa8457db35a | -2.61706 | -45.22373 | 2025-12-17 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c079989c-678b-3b0b-a1fc-40a75c86c289 | -3.71197 | -45.12975 | 2025-12-17 04:25:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a63cf724-f15b-3229-bab8-d3d3be55398d | -2.90591 | -45.58966 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7678e3e2-3bc7-354c-b2e8-ae08de7e9605 | -5.47575 | -45.40471 | 2025-12-17 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96dd5789-dbc8-310e-aba1-f7f96710fec8 | -2.43695 | -47.19495 | 2025-12-17 04:25:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4cd2eec5-442c-3511-813e-c5ea24215e3a | -2.8838 | -45.46959 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6aa68ca0-a659-37c1-ab77-7b80315f7c19 | -2.9026 | -45.58914 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3e2400a-389e-338c-9ae4-d1bf5d293ba2 | -3.14871 | -43.01511 | 2025-12-17 04:25:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84c238b1-6dc5-3ce2-ade7-97d68c20c55d | -1.42423 | -46.06303 | 2025-12-17 04:25:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a3cfdec-d2cd-3487-b0de-1145ca0ca584 | -3.11865 | -54.17602 | 2025-12-17 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 201fa9e8-cf5b-3b64-aa67-089dde61f006 | -3.33075 | -45.41676 | 2025-12-17 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94be666-81c0-3aaf-aef9-05bf0416c3fa | -2.90699 | -45.58279 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fedaf9dd-819c-3116-baa4-e0021e21c462 | -2.93817 | -40.10023 | 2025-12-17 04:25:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6aadfc43-790f-3d36-b17c-c2b2c4ce8220 | -3.93018 | -44.88841 | 2025-12-17 04:25:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52a6536d-2866-3ba2-8dfe-93996fb7b635 | -3.14179 | -48.15672 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5e55b61-5937-37e2-a5cc-5b00003c02b1 | -3.02781 | -45.35515 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f3fcb83-5c39-3ba9-a6c1-529cfa81242b | -4.32699 | -44.82434 | 2025-12-17 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7144fd81-8417-376a-ad4d-8a17beae03c0 | -3.84064 | -47.06125 | 2025-12-17 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2139f134-29ec-31dc-b7aa-60847be086ee | -3.03497 | -45.35275 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d422cc98-a9b3-366e-9099-b4f4dc0d8933 | -3.6862 | -52.00793 | 2025-12-17 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c63607c2-9aa5-3204-9463-88a39ded224c | -1.85766 | -45.83679 | 2025-12-17 04:25:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1cd9d556-17d9-31d5-9794-c4484565250f | -3.03166 | -45.35223 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aeba8e49-8d3d-3a67-ba15-065db2574b18 | -3.12375 | -54.17693 | 2025-12-17 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3e58893-1fcb-307d-81a2-d62eaa10557f | -2.04783 | -45.45126 | 2025-12-17 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cb177b61-a790-31c0-b483-3d0a72b1e884 | -2.62487 | -48.05833 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 065ed4c4-078e-358b-9217-8ce85abf413d | -2.79441 | -51.40847 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc385b1-c20f-37e1-ad2c-4a1c31902dde | -2.68007 | -53.07706 | 2025-12-17 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48a0253a-62d1-399d-ab8d-257bca21c270 | -3.84121 | -47.0577 | 2025-12-17 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 750e1848-c0f5-3618-9010-22c78bdc0f83 | -3.65297 | -47.55236 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| deefca6f-e056-3e50-850b-b4670c42eacb | -2.79016 | -51.40777 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c15aed1-aafe-3fab-8b99-69e67bb5ad0b | -2.56753 | -45.32166 | 2025-12-17 04:25:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4770db1e-dac1-37ba-a375-6d267b9c1e6d | -3.68706 | -44.68189 | 2025-12-17 04:25:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 803779be-606a-3598-a6cc-638b0978e981 | -2.80272 | -51.81035 | 2025-12-17 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e9f5904-e14a-32ec-bae8-8b2c3e7facf3 | -3.03551 | -45.3493 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1f07d49-c22d-3615-b6d3-949e0e3569ad | -2.53327 | -48.24608 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c0a37cb-109e-3f39-8a87-91359eae1442 | -3.95412 | -40.93677 | 2025-12-17 04:25:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c79c2077-befe-3c63-891c-05b057b0dd85 | -3.64676 | -46.89256 | 2025-12-17 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ec5ba79-9280-35bb-9639-3cf2b260ab4d | -5.39627 | -46.96075 | 2025-12-17 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6ba8d1a-ade9-33cb-9588-d1a625a75d4d | -3.35915 | -44.56201 | 2025-12-17 04:25:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61311662-40b6-305d-a03a-a87b35a69bbc | -3.12498 | -48.69356 | 2025-12-17 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37158aea-3250-3e63-bdcc-58e1a1aa8b7d | -1.45153 | -46.88318 | 2025-12-17 04:25:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fafabe4-c6d7-3ff6-86e4-9d31966380ef | -3.87431 | -40.45122 | 2025-12-17 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 76dc4393-b13b-3c06-a4ff-e10daa2894c6 | -3.20511 | -43.18691 | 2025-12-17 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61bb0dcf-b784-3deb-8a1d-e49d9b351f53 | -0.93927 | -46.91135 | 2025-12-17 04:25:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ac3c9ae-2529-3c9d-ba97-fe4b462ef2d4 | -2.92735 | -48.22796 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03dc0720-4ea4-3a4f-930f-06c9e8af3dd6 | -3.10768 | -45.08483 | 2025-12-17 04:25:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 03e58e90-3185-3035-9145-9ff07732b8ce | -4.13673 | -46.29206 | 2025-12-17 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 670d3b9c-9a5a-3117-8757-96c8e3a28b98 | -2.44556 | -48.87141 | 2025-12-17 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d4733ac-cbb8-3323-9130-c1db5af59681 | -2.94287 | -40.44405 | 2025-12-17 04:25:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| def95cf3-9585-3b9d-9045-71716fa51800 | -4.34445 | -48.60482 | 2025-12-17 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 54bf4992-97b5-39c6-8a4d-038da9d25bd0 | -3.17337 | -48.02718 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dda59d9-4b93-3ad8-abd6-ba188a75462b | -1.41703 | -46.06547 | 2025-12-17 04:25:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9fbb3231-b939-38d7-a7a2-5e7970e696c5 | -4.35689 | -46.14632 | 2025-12-17 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef676e94-87d9-38e7-b921-81409e5693ec | -4.42669 | -46.2845 | 2025-12-17 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3193f64b-8525-3ae1-ade0-0d9bcb3c8504 | -3.42177 | -43.16709 | 2025-12-17 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bc89b6b7-a29d-3885-b97b-76b8be7517b7 | -3.69056 | -52.00868 | 2025-12-17 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ad5618b-9e4c-3809-ac43-6f6d242850ab | -1.9688 | -45.71304 | 2025-12-17 04:25:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 083275c9-8188-3184-92b4-3f376ed06e19 | -5.58053 | -44.88981 | 2025-12-17 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42cbadd8-d79c-3bbd-8f6e-312182f2f4ca | -2.04453 | -45.45075 | 2025-12-17 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70402bd4-022b-3fb7-9af3-ee68596bb70f | -3.36878 | -49.16239 | 2025-12-17 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84d1416c-0638-3381-b816-c3258a6398a1 | -3.55915 | -44.89172 | 2025-12-17 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65b082ca-0a47-3fe6-8da3-a273ea73b352 | -2.92671 | -48.23189 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aacd221d-13a6-3654-8732-dd0b74e34613 | -2.74683 | -45.1767 | 2025-12-17 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdc3bfeb-7857-379b-a9c9-1b2e2526947c | -2.52974 | -48.24552 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05e4d62f-ce89-34ad-ba33-aa9e105acaae | -2.5007 | -48.04346 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ac724f-66e5-34b2-84f8-ebb00b484e97 | -12.67307 | -46.77435 | 2025-12-17 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca7c96bb-2b95-3997-aa60-8113e38ffcfb | -11.82207 | -43.79599 | 2025-12-17 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 763fb5cb-bb88-35ca-a383-943ce25dfa02 | -11.84697 | -43.73719 | 2025-12-17 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcffafa3-cb2d-3e4e-ad85-d8373e8acd28 | -7.88895 | -46.75348 | 2025-12-17 04:27:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b378827-9962-34d6-a9d1-0983f82e32be | -8.71903 | -50.24097 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84a83e0d-1639-3aa0-a682-742a4fe3aefc | -11.96921 | -44.4973 | 2025-12-17 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bf26147-ac8d-328c-94db-a14ae94d0ed9 | -9.00768 | -45.92299 | 2025-12-17 04:27:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94e37eda-d791-3680-b3db-830bd55c0f9f | -8.7256 | -50.24643 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29c23fb5-0250-3cff-a32d-7427121b911c | -11.71217 | -44.53585 | 2025-12-17 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2769bda0-e439-36e7-b27c-491d392252b8 | -11.84762 | -43.7326 | 2025-12-17 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36e0bf13-bd93-3a46-a28a-798b18ed9466 | -9.00378 | -45.92603 | 2025-12-17 04:27:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f36841e2-4258-3c47-a0d9-a021dc901f7c | -7.88289 | -46.74895 | 2025-12-17 04:27:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README10.md)
