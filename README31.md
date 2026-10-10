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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b812678-ed74-3439-a0ca-455feb364be3 | -7.18691 | -52.63902 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6baff994-e4ad-3de8-9ce3-e770c4e9fc39 | -7.02615 | -47.65751 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e80d7d0-71aa-35cc-89f0-64ebc4b1edde | -3.2766 | -54.69567 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 280d5799-85ed-34e9-8efb-85b7e2bb7dd7 | -5.32112 | -50.06804 | 2026-10-10 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5971032f-8f64-305f-b142-faffb3029633 | -3.18081 | -50.58117 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c19a0d91-2ba1-3ab7-a7fc-8461eba080d8 | -7.53853 | -45.31985 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 75b8bade-d913-3d46-a39b-115f7dd14f08 | -9.83444 | -44.77997 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6473276f-804a-34cf-83e0-e6e3b04baeed | -7.52764 | -45.31808 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 434745cb-5c93-3b07-b7b8-1bcba08cb468 | -7.22683 | -55.14638 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a71256de-e380-3da3-a982-ce3e0b6709f1 | -4.84351 | -46.77944 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d989030-819e-3bc6-a8cf-3f44631714bf | -6.07896 | -43.9941 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baafb29a-f18c-33ef-801d-0f3cb5636aa0 | -6.08095 | -44.09281 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de52d37c-2afe-342d-b019-b3505918ec54 | -3.34582 | -50.41498 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c5bbac1-723c-36e6-8d71-83acd18481c8 | -5.95941 | -43.90534 | 2026-10-10 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85a08bf7-61a5-35c8-af61-32d3c0ba57a8 | -8.95967 | -47.37708 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1a3f847-978d-3afe-8e3c-f30452e79183 | -3.80435 | -49.93904 | 2026-10-10 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2a3dcf09-a806-3ffd-8da1-06df4871fade | -2.57859 | -48.25018 | 2026-10-10 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 649f697b-db81-3287-8c59-3ee81b5e5aff | -8.55675 | -46.90606 | 2026-10-10 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b931f51f-e222-3146-a9bb-0a7b8555033e | -5.86995 | -53.51523 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 974d7dbc-55c2-39e1-af4c-13f0e35bc9b6 | -6.64931 | -55.33027 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b861b178-8314-3226-9068-cb5206eb06c2 | -7.09715 | -41.75451 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ffc4cc04-d3b7-3af5-bfad-0e6f8dcbb83d | -2.99266 | -53.90395 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bd5b476-6cd3-30c0-9e1c-42cb9ddec112 | -9.29597 | -47.39263 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7809246b-9bb9-334e-b012-c62991e166a2 | -8.95163 | -47.37579 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 633e1a75-b004-35e2-9153-c8465935ce61 | -7.87868 | -49.80705 | 2026-10-10 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f879b53-9528-3122-80c1-2f6193e6fc0a | -9.73765 | -44.79184 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70728fd0-43ef-3def-a28f-a41715a20c83 | -3.26443 | -50.39068 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2b1a73e-5789-380c-bc03-a8250f08be1d | -5.10902 | -46.21886 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c8acbc4-268c-3656-921d-83a1aa424169 | -3.4686 | -50.07617 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b0717d0-7df8-3d88-92a1-5322aaca0b49 | -7.90657 | -54.72021 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 468926e3-6b58-39b9-9176-6b8c1eff0329 | -5.79078 | -53.80656 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09be7882-42f5-3d67-97fa-7dd04d7dcb32 | -9.3156 | -47.37415 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74fcf73a-861b-30b2-af8a-ac7c1a169259 | -5.88382 | -43.41043 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a0237aa-7964-3732-a057-baf7f15e3245 | -6.25358 | -52.86208 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a59c4c7e-489c-3a1f-b3c2-b0d38748271d | -6.81011 | -41.23847 | 2026-10-10 04:08:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14d41607-591d-3120-b54c-fb110a0a40a3 | -3.50054 | -49.94801 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5606118-85b5-345b-a31f-c04406a2e65c | -8.02208 | -43.90765 | 2026-10-10 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f1ea5d2-6428-3f01-bba6-2c4c5cc26ba3 | -3.20857 | -50.54903 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b38923f-4482-367e-9dd4-a607b86e2afb | -8.99272 | -45.88531 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 879e688f-61b0-3999-8443-26ec3eda4c0f | -5.70373 | -53.47982 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 068db45d-485d-3697-b1f0-0dd576d03fd7 | -6.91255 | -45.87457 | 2026-10-10 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c178869c-1a93-3c8c-bbd5-62d4fac09b86 | -2.79354 | -51.40969 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76030a5e-4ae8-35e8-9468-cb0e844bb0cf | -1.64422 | -54.40633 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cd69295-09ce-3202-876b-490590c20b29 | -9.35203 | -46.56678 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb3a37da-ef7b-3567-b868-f1caf704e4e3 | -6.87489 | -45.0412 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3cd8b3b-cc45-3f16-a329-59e6894f243e | -4.11018 | -54.01378 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 545ee1a0-8d36-3576-a7a1-5fbb1d0935e4 | -5.64392 | -44.05761 | 2026-10-10 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dba64d7-c389-3bb2-8bb2-57a365b7b809 | -6.37505 | -55.16035 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94a2ecae-c4ea-3fed-8597-bb459b3a426c | -6.23209 | -43.85002 | 2026-10-10 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8dfc6b9-967b-3c0d-9533-f656e1823bc9 | -2.29953 | -48.54782 | 2026-10-10 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6b37960e-553a-37b0-abc3-95f0f6b5bbd5 | -4.63626 | -50.96336 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 695482d5-5853-3c9d-9da3-7340547dd491 | -3.80542 | -49.93262 | 2026-10-10 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76f4a665-e66f-3a20-b93d-faa18356d36c | -6.13192 | -43.5324 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac4e2bb8-6f55-3df1-9c1d-864fb62b660d | -8.60841 | -41.08768 | 2026-10-10 04:08:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c367ca2b-5e5d-3a7d-b2b4-37dab710241c | -7.39917 | -44.76564 | 2026-10-10 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9538599-5ed5-3fc8-b6e5-87e25130d3b4 | -7.10571 | -46.71895 | 2026-10-10 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b75782b9-0a5c-3059-b034-c572f436c418 | -7.01467 | -47.70024 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 941fe999-9d24-3050-b9ca-0f68149349d9 | -7.00717 | -47.71904 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1c12f0b-320f-39d3-91bc-40731ca6204f | -5.84573 | -44.92632 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd3265b8-eab6-3bf3-aa8b-27661ecf409b | -5.58942 | -47.28342 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 879e1a4e-4381-39cc-8123-6147fdd47229 | -5.49471 | -43.97458 | 2026-10-10 04:08:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d158ca0e-1f04-3270-a2ad-f8b6b4969454 | -3.12399 | -54.17004 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5e27764d-5b3b-31c9-ad5c-282de589934e | -3.11717 | -54.16867 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2e23da8b-0100-3edd-a113-4eb20008c631 | -6.36118 | -55.15804 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17b66610-4a9b-3212-864c-8ec65e88dfc6 | -6.77721 | -48.66849 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1624e1b8-ec67-3feb-88cd-4fe670384057 | -3.54147 | -54.74446 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 270fc066-805c-3dfc-ab45-5a566dd6300a | -3.57422 | -54.6935 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9fd66929-0fd6-39bd-b266-cedfbe51483c | -2.79422 | -51.4056 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b3357b1-a336-339b-94cc-85dff6dab06f | -3.57937 | -54.69459 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e2ca75a0-5cac-3cae-809b-1df891d0a6a2 | -3.20683 | -50.5597 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4301c92e-7a41-3cb8-a8e6-6a0a23870e42 | -4.22379 | -40.78069 | 2026-10-10 04:08:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b4a82ba5-254b-3025-a654-a7295f0d7dcf | -3.31411 | -54.67345 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0945394b-d849-36b4-8623-ddd0df9d9c21 | -5.75024 | -45.12199 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 706d0736-2b82-3dc2-a1b0-42bf1b85a897 | -3.59616 | -54.60015 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 69ead740-73aa-3f6a-a0be-bedf555207aa | -4.13342 | -50.82102 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7a232cb-a84b-38af-9b26-65250b0f336d | -7.00364 | -47.71412 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0b4a6da1-8d70-3ced-adb7-a5f67b15cf63 | -6.21658 | -52.64401 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6135fae0-d50d-3bbc-ae14-281dcfaed536 | -7.03747 | -47.66768 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d49e4ae5-bc83-3063-bfd9-f6f92816a220 | -7.52126 | -48.02229 | 2026-10-10 04:08:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fd4a6506-3bbb-342c-adf4-32957138b0e8 | -3.28095 | -53.87204 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 889eead9-4259-3370-b268-b8fc8d0e9656 | -9.30579 | -47.3834 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5f36ed4-bd79-3c57-a1df-9a20164bed78 | -3.28426 | -53.87015 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 85ec56e2-a17f-3237-9365-f815bc433a08 | -4.39586 | -46.52989 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75391763-ba2b-3922-8934-39a831b3be2c | -3.21922 | -48.81385 | 2026-10-10 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01fee755-a861-31db-9a43-603b74c832a3 | -8.77265 | -49.61263 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa9f5f22-6058-37fc-9fd0-cf0b545a82e3 | -4.22692 | -46.93122 | 2026-10-10 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f68e3f-7525-3257-a9c2-9449ace32fdc | -1.95229 | -54.39942 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5a9685b-1d15-3c35-86dd-131aca30860b | -3.85543 | -51.93896 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4510051f-a43f-3b97-bc14-15b3c8b79252 | -7.06431 | -46.45654 | 2026-10-10 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15b66ffe-7435-36d5-9ae3-e0e44f06ec95 | -7.14545 | -45.01158 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8faa9db7-7d21-333b-afa7-602dc8a7a16e | -3.55127 | -54.68989 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bf1a37b4-7ba1-38d4-afcc-b4167b9e79c5 | -7.52107 | -45.31266 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6608fdc8-899b-377c-b9a4-255543d169e8 | -4.09219 | -53.99821 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ecf7970b-5f0b-3194-91d3-5491c3175519 | -3.19841 | -53.85263 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c113821a-fff7-3b46-bf14-b487fab019b7 | -3.35065 | -50.41927 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1a127b7-c997-3622-a3d6-aa541cc0f637 | -3.58985 | -54.71715 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88ddfa03-802f-3204-abe7-5ee44cefedc7 | -7.03132 | -47.67858 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a19707c-91c7-3109-bb9f-a0a7a8dfd911 | -8.27477 | -46.42738 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96de7b3a-985d-3a57-bea2-510f598cd92b | -7.061 | -40.95648 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d34124d1-82f3-3fc4-8bc2-6b8b63a026ac | -6.13133 | -43.53612 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README32.md)
