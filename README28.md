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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a291d00-b357-3a40-ba2e-c790f91eb5f1 | -2.91361 | -50.41505 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eec2450-f073-3e9c-a43e-be10516ffd66 | -7.09599 | -43.46049 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2c13b12-75af-3d62-895a-270132138878 | -6.3639 | -55.83735 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2783b6f2-9e2c-3528-9af1-295e3a7c0577 | -2.9167 | -50.43022 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b045bdf4-fb1e-3c60-8a48-43e524280d98 | -5.99794 | -47.39032 | 2026-09-16 04:14:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 393e8ecc-e549-3a71-b6d3-4c4e4859f8ca | -8.33254 | -51.31315 | 2026-09-16 04:14:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab04444d-9089-3341-88a8-5498f34f7399 | -9.53701 | -45.42017 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d02991ca-78d6-3c6b-a1dd-f9576cb3362f | -8.80026 | -46.89921 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8349cef-5fda-36dd-8da8-6d458d7fff90 | -7.47313 | -42.10279 | 2026-09-16 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76ba7126-96d5-3a48-9e72-b1a6d6ac0213 | -9.07371 | -42.99651 | 2026-09-16 04:14:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0fd85cd2-f844-3a21-b266-a5b6aa980d43 | -5.90212 | -43.48955 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f942c8a4-ef91-32fe-bc74-d26cdc25b433 | -2.91065 | -50.43281 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b780e277-b249-3869-bd87-266c589e806e | -7.29828 | -42.34872 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ade54ac-24e1-38fc-a87c-c1fac17d70f4 | -10.30789 | -45.27323 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c673cd5-3768-344d-ba00-b27dbcf10601 | -6.27297 | -44.14992 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21cfa8b1-6553-3d0a-aa6a-b0cc213140b8 | -10.33361 | -45.29339 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9694e65-5ca2-3c8c-a22c-56c3f6a61359 | -4.67832 | -42.09483 | 2026-09-16 04:14:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff9792f9-df68-3f68-906f-db2092cdf0ad | -9.57232 | -46.58749 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c530ed0e-3367-397e-a0f1-62eea2b2c78d | -7.46927 | -42.10572 | 2026-09-16 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5ea23a5c-4960-3f50-9712-d4ec52267f0f | -8.05571 | -43.74891 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1d71096-14d5-3a57-980c-7fa60985c8a4 | -2.88939 | -50.42549 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2862cc2c-ce36-347d-970b-41ffbd74f31e | -3.84734 | -51.76917 | 2026-09-16 04:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4f07682-9a35-3cca-9fdf-4fcf159ff9de | -4.28651 | -48.03755 | 2026-09-16 04:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42790b57-7413-327e-8a00-0d1f748e7074 | -6.98903 | -38.14919 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3b4e37f-d83a-31e3-bceb-87a43b2d9ce6 | -4.60164 | -48.51032 | 2026-09-16 04:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51a66529-8393-3869-b4c8-f76b171af335 | -4.46374 | -55.25871 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8880aefa-195b-3393-adf6-b04a425f6f30 | -11.19706 | -42.82419 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 86a021a8-2298-363c-8602-93592304e6bf | -9.10998 | -45.73713 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 011f2f1d-c39e-39b0-8c9e-f9ae3ab78d4f | -4.51324 | -54.96379 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10b55b21-6372-3d3a-b9f3-f77cfd3f08e6 | -7.25668 | -46.16769 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bb17c6b-f9ad-358e-9270-32e88ae5e0d3 | -11.31254 | -42.32817 | 2026-09-16 04:14:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c05b7fa-e8b9-36b0-bd50-ad36e8968cea | -2.90993 | -50.40354 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d588a3d-9e3f-342d-94d2-fb70b79ae3bb | -9.40896 | -47.85262 | 2026-09-16 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5d234a4-c661-3fcb-af86-2974fe07f2e8 | -9.81534 | -48.91418 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1e3650c-0497-37bf-92ff-35f7160d0fb5 | -11.13812 | -40.47797 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| ca4fe806-9c60-3d8d-9fa3-f8c97da0d2e8 | -9.86621 | -49.83555 | 2026-09-16 04:14:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| febad43a-4e0b-310a-82b0-530221a2ba99 | -7.73676 | -44.70945 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce2adc2f-f2a1-3fa0-9ac9-b946d5cbcc52 | -5.61981 | -45.24673 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 71d8777f-7387-3747-bb6c-ae491f1729bd | -9.10705 | -45.73227 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6087019d-e369-34c2-8e52-d03cb484857f | -9.48863 | -45.44593 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69aa2248-c173-39fc-ac50-a95aeca19c1d | -6.94385 | -41.69199 | 2026-09-16 04:14:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eee21297-3f5f-3b2f-ae9e-ad3645d11003 | -7.09832 | -43.53217 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5f121f4-bda9-3cd0-9086-71c22457f76a | -2.86561 | -49.63497 | 2026-09-16 04:14:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9100371d-9e5b-380d-ab72-0fb4cf56fad7 | -6.81629 | -35.15053 | 2026-09-16 04:14:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 929157c8-95d2-3f2f-9dd2-2b5058cf1384 | -6.80695 | -52.48179 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 276750bd-2298-3c3f-805b-cb949bb9336c | -2.89973 | -50.4309 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2cd3ee-b17e-305f-b39c-5600e4fe5e32 | -5.6377 | -51.69619 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 082647b7-bfb1-3005-aeee-8b5fb16e6910 | -5.99722 | -46.62996 | 2026-09-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e12df8b0-d20e-36b4-a403-e732a5da7452 | -9.48716 | -45.4327 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d13c54fe-3d1c-3111-8be3-48ce96a7ba83 | -5.36914 | -50.16686 | 2026-09-16 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fb0173f-a620-3e25-83c5-c900257de8c6 | -6.15828 | -55.70827 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 450988d3-7cbd-3cec-8d3f-32b42c750ca9 | -8.32726 | -51.31214 | 2026-09-16 04:14:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d50d14ce-3d73-3cf1-98fe-0d78f20a64e6 | -9.48647 | -45.43685 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf9ab22a-1011-387c-9c94-1d3e374447d1 | -10.58471 | -47.74947 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa683761-60e2-3683-8c34-732818a142e3 | -7.09127 | -41.76848 | 2026-09-16 04:14:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f9bad02-e181-3964-aed9-5ef8d73d43b8 | -4.33917 | -46.61669 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e6d207b-3905-3a9a-a62e-fa7889018c16 | -8.84084 | -45.86417 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bd28c0d-4420-32b9-ad9c-ddfe94e3bb9c | -10.09767 | -45.61833 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40fc727f-63a5-3e22-8bd4-544871d7d9d2 | -6.66507 | -43.652 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c95bd6-9f25-348b-8583-d3ac5c7c52c0 | -8.47928 | -44.57693 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8a819dd-dfbf-3090-940d-0671f8657d52 | -8.78413 | -45.89278 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 467a1e54-a62d-3b69-b4a1-66cd16f89912 | -9.15927 | -49.99237 | 2026-09-16 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6a6ae90-f3eb-3afc-9eed-90058fa6865a | -6.19172 | -44.03371 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7ab7ec1-eea2-3cf2-9c4f-44b862156a1e | -2.89605 | -50.41932 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94d78ad7-e659-3e17-a2cb-61eda9edb429 | -6.95102 | -41.68958 | 2026-09-16 04:14:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 11101eb7-a540-3b55-90c6-c6412cac4de6 | -5.63472 | -51.67965 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee2c03cf-f169-36d2-9702-c61620491263 | -3.47308 | -54.68938 | 2026-09-16 04:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7c1e9c9-a59a-35f1-9028-ccf1fe97a08c | -8.46197 | -46.87692 | 2026-09-16 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52247c3a-a8fa-31ce-b1fd-36a422a00209 | -9.35404 | -50.08696 | 2026-09-16 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bd4787d-6734-320d-8341-9049994d3cb4 | -7.12204 | -42.08957 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c046f350-4a0a-3cc7-98aa-00882868c1f1 | -6.39703 | -44.05478 | 2026-09-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 342f8e55-d86a-3b49-b5d3-8cca8ccbc9ef | -9.79023 | -46.49065 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 393bed02-fecd-3272-868f-712ab6fe9272 | -7.06344 | -46.74677 | 2026-09-16 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff77e580-1fc1-3a17-9afb-af5b2efb65fc | -11.19982 | -42.82823 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| eff2d041-dbf7-32bf-9b24-1075b82fdec9 | -3.01474 | -51.34078 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fb5ff25b-547e-3974-b17e-74c26805ab30 | -13.75449 | -48.79173 | 2026-09-16 04:17:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0a43acf-41f8-3a47-b043-d279f49afa25 | -11.7892 | -46.59271 | 2026-09-16 04:17:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2954247b-d2d2-39be-99c5-e3c3b7250119 | -10.93229 | -54.08368 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f6e03c3-e3f8-3c64-ab1e-cfbd0b429430 | -13.76252 | -48.81347 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9361465-0bfa-36eb-88cb-861e77c92dd2 | -15.17153 | -43.84731 | 2026-09-16 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd2fdcd-7662-3172-a23b-6b2d5c9344e2 | -15.29356 | -42.7877 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef9fe22c-3a5e-314a-9f9f-7f94b2c949db | -10.88895 | -47.58198 | 2026-09-16 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dab9538-58df-3190-84c4-6ee7c7d40d2d | -17.04385 | -41.29261 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| d35cbafc-c37e-3230-9c8d-d3af681f2f10 | -13.28922 | -51.2713 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 827c6699-f4c6-3a21-9519-30fc3299e5fb | -10.87273 | -50.8217 | 2026-09-16 04:17:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f314a33b-9d3b-3330-859e-fc9c4fad124a | -15.56029 | -42.37495 | 2026-09-16 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0bbc153c-b764-3533-90ac-131337d2ca24 | -15.50272 | -53.84499 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38b71dea-ea5c-3eff-a688-07705087cd70 | -11.55156 | -46.86644 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3df6fa24-558f-367b-82c2-84d419a27814 | -15.49878 | -53.80919 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27b1bcb1-6a97-3a9e-9ea6-3d77c5b343e2 | -12.71138 | -48.28115 | 2026-09-16 04:17:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 394a984c-7362-3b47-abc5-6a6e2417bd73 | -12.15296 | -47.99231 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47f8289d-965c-37f5-b7e2-1a314db726d1 | -18.64896 | -47.28873 | 2026-09-16 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb0cad1-2f79-37d8-b8d8-0902364548e3 | -13.55854 | -43.5249 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d63b333-65dc-37a9-ae1e-3f8f71aa17cb | -12.5323 | -47.10686 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc82b474-e897-379b-bf9f-da50ab88e7f7 | -14.3975 | -44.70822 | 2026-09-16 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe65ab6d-948b-3463-9cea-0aec3876c2fe | -11.31287 | -47.24497 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b12e9d16-364c-398a-b9d9-92612b42fdbb | -13.55275 | -42.41315 | 2026-09-16 04:17:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52916f5b-62d4-399e-8c10-b7cae61d9ab6 | -15.89447 | -40.23087 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3487968f-5a5b-30a6-aecc-44e68a83c0bd | -12.49429 | -41.41377 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e82fa2ad-d96a-346e-a8bb-36df0059b8f3 | -11.21382 | -46.40588 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README29.md)
