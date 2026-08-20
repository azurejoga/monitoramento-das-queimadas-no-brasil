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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99b5dfc8-fe59-36e7-a52f-381aebbd7ba9 | -8.5385 | -54.7798 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e23db13f-9efb-3c66-aee4-45924e973c31 | -11.6838 | -54.559299 | 2026-08-20 00:38:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8fc8f26-a8a3-3436-ad9f-ce4382b53ca9 | -11.4255 | -54.3312 | 2026-08-20 00:38:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3c5695d-bfe1-3e77-b7b0-7da8044cacd1 | -6.8752 | -59.015301 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00766598-9ab6-3e19-b493-c2545ecab8e9 | -7.3447 | -45.808201 | 2026-08-20 00:38:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55ee36d2-7f43-34b4-9d93-1649b4abba34 | -8.575 | -55.300301 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b731110-951f-38cc-a2b0-8f0dfb806fe6 | -6.4194 | -54.933701 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56cff755-19f1-3ba6-8ec8-898467b9626a | -16.506001 | -55.1745 | 2026-08-20 00:38:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 697efaf5-2b85-3fea-8b97-8cb779f73c8c | -9.1215 | -51.1534 | 2026-08-20 00:38:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de1014fd-6750-39d5-8b09-269cce16c4b1 | -9.9817 | -53.927399 | 2026-08-20 00:38:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa680cec-71f7-3194-87ff-7ba15d8def1c | -9.4026 | -60.550598 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4c3c2c6-6a49-376a-88b1-3657b991b74d | -6.699 | -59.101501 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e70fcd4f-5cd0-3528-89b8-fe4bdededf86 | -4.4561 | -55.450001 | 2026-08-20 00:38:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dac61fb0-8002-3a6b-b7b9-d1c5561eaf12 | -5.7948 | -55.7169 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc0c452e-a353-349a-af3c-6acb8361cdce | -2.1542 | -47.488098 | 2026-08-20 00:38:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 404682fb-75ec-35ae-a3de-3cfe555b86cf | -13.6885 | -53.182598 | 2026-08-20 00:38:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cffcf84e-89f1-36f8-bcfb-9e6c673dceed | -6.7049 | -58.942101 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f1c3777-e9da-3d38-ae0c-e6b3911f7a9e | -6.6918 | -58.929298 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff13f4e9-d41f-36a2-8028-b0c10730cd6f | -5.798 | -55.731201 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68bf478e-6385-3f46-896d-dba669e3592e | -6.8356 | -56.443199 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 303a117b-271a-3867-8ed0-3a59b88e6234 | -6.7038 | -59.076698 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09058be4-660b-3ec3-9679-b21ddee371c7 | -6.8654 | -59.017399 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1540cdcb-19bc-3f9a-aa93-e0935e9bcd2d | -9.1205 | -61.584599 | 2026-08-20 00:38:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c50cdba-1b18-3931-823f-d6b3ab4d9078 | -8.572 | -54.656502 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18ce0996-7b7a-3450-bcae-6e2459053f09 | -8.6601 | -54.6362 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cbf8769-ef7e-3adf-be8d-d78801894819 | -6.694 | -59.0788 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0909ca31-a3b3-38a6-a884-5aa69b1ea0f8 | -10.3352 | -57.554298 | 2026-08-20 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 968fc922-7a90-332f-ae9a-a854dbc82050 | -3.9036 | -55.873199 | 2026-08-20 00:38:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a268d32-6908-3b57-a99c-1faed450744e | -3.1076 | -61.205101 | 2026-08-20 00:38:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12f265d1-4092-375a-8ef6-01fe11331d3d | -8.5791 | -54.732101 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e0740bf-f894-326e-a094-0bfa2a1e492c | -13.5825 | -51.673801 | 2026-08-20 00:38:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bddca575-d5be-3bc5-8b88-4d9eb08658c9 | -7.3513 | -45.834301 | 2026-08-20 00:38:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d810140-7efc-3a7b-909e-2bf535b83cf0 | -10.3254 | -57.556499 | 2026-08-20 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db70aac6-6bf4-35ec-b988-9c3aed8ae2e2 | -8.5605 | -54.651501 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d5a6d8-601a-38d0-99b2-100deb01fee9 | -7.342 | -55.678101 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4c42f1d-efdd-316a-87da-52e21f78e246 | -6.6867 | -56.1497 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35326613-f330-305b-b937-94268e46c1f9 | -3.1057 | -61.196499 | 2026-08-20 00:38:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34441e1e-e8c9-3934-9851-accbdbe585b9 | -9.4133 | -60.4091 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d8c5ce8-c714-3262-b91d-1ab659094b99 | -9.2058 | -59.7742 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff40dfc4-f731-3f0f-80ca-856796c14fdb | -10.4585 | -54.655701 | 2026-08-20 00:38:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce8b9e51-6e03-30c8-8130-77d8b2fba1f3 | -9.4211 | -60.397598 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad3e8f61-2f72-3a5c-8633-7ba5a85439f8 | -14.016 | -53.664501 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97277b66-60ba-399e-82f6-bd92bcdf6d9c | -8.5402 | -54.787102 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53ed4667-b266-30ee-be59-8bf461533d1e | -11.2158 | -54.001499 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58d4dafa-2c0a-37dc-b518-8ab69733b86d | -6.9266 | -59.341999 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 128ed589-3736-3bb3-9bec-3a3a99c42be6 | -1.8277 | -54.4963 | 2026-08-20 00:38:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1d070bc-65d0-311b-8508-f78a5677cf11 | -5.803 | -55.7076 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc883733-8499-307d-b18e-535d72dfee75 | -6.7016 | -58.927101 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 061ad4a9-6cc7-3bd6-9331-95c4ec65e5e7 | -18.0179 | -44.6105 | 2026-08-20 00:38:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 540241a4-b8b6-3eb7-a0ba-1d749ae38b9a | -8.2809 | -62.879002 | 2026-08-20 00:38:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f0e0d6e2-d028-3363-8239-71ce65d5552c | -8.5355 | -54.856998 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed38e6f-f9d8-3f85-8494-e7a63c2b4fa0 | -8.5776 | -54.770802 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4501e701-e9e6-35f3-ad40-9a4b4b59c725 | -6.4315 | -52.764999 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3d4a4c5-2362-3e6d-9243-35dd600e2cad | -6.4113 | -54.943298 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31fb6a57-f28d-3788-92f3-b17bf7e6887a | -8.5659 | -54.7197 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c62f55f0-15c0-3d4a-844b-0090900ce80f | -8.5662 | -54.7658 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bdf734e-d82d-358d-a1d2-d2dfd91f53ec | -14.2082 | -52.886299 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2af092ab-c168-3fd2-aa78-d5a52a675445 | -6.3866 | -54.925499 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723d44d3-8ef1-3805-bbf6-39048f9df25b | -4.2752 | -46.5238 | 2026-08-20 00:38:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c1cd002-5b1d-35bc-ae65-90d09d1f9e96 | -6.4281 | -52.706501 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c470ce82-a8bf-36e6-bdaa-9323e78a5ecd | -9.4174 | -60.428001 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db0acd84-1858-36d9-9750-fb5756dc82ab | -6.8372 | -56.450001 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 783e5931-7cfa-3fb6-bcc1-1b1711701993 | -14.1966 | -52.881001 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1344ffd-de67-32c0-ac87-1158bca6954b | -6.0839 | -57.908001 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7cfec8b-a5c8-3904-b402-e0b72885d8ad | -14.2074 | -52.927399 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec404f7d-e59e-385c-a818-2474247d6972 | -6.4401 | -52.713699 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fcbe79e-5b69-3734-b7e1-c132734267d9 | -7.5349 | -55.574902 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff748070-715f-3253-b445-71ea58572f89 | -4.527 | -56.122299 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffb48e6b-608f-3ae2-9acf-f9a8ced0df6b | -6.7071 | -59.091801 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffedd8fc-9b1b-3aef-a881-5903d77cabd2 | -18.548 | -48.279099 | 2026-08-20 00:38:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f55e139e-0dd7-3305-a69e-f7cc7f306b4c | -14.2179 | -52.883999 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 627ca6ca-38af-36da-813a-a251655b44f7 | -11.2382 | -54.820702 | 2026-08-20 00:38:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35f4c7f2-db74-3ed8-8fb1-63f05d84442e | -6.7445 | -59.028099 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbc3d0f4-1dae-34d0-8ffb-69465381e473 | -10.7849 | -50.309101 | 2026-08-20 00:38:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35f168ad-8452-30a9-a271-5a85c515298b | -8.2933 | -62.889999 | 2026-08-20 00:38:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45343bb6-0156-3de0-9f93-1881b7a6b4ad | -9.1189 | -51.142601 | 2026-08-20 00:38:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b1f7025-a983-3ced-b6ae-f3e4b946d758 | -6.4326 | -52.7253 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc802da9-8174-3c3c-b990-065af96b6cd4 | -9.1029 | -60.921299 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14bde6d3-398a-3fde-88b1-1e54d78cbc3c | -6.2487 | -55.403198 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e154f10-55df-3b84-ba52-41927bf49c6b | -2.5527 | -47.2374 | 2026-08-20 00:38:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34ebe373-1972-3e5e-b899-3a7ea6572fc4 | -7.5709 | -55.551899 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89e0d195-2107-3253-9651-fb445482bd57 | -8.5754 | -54.6712 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13002a7a-7f7f-31ae-8605-1c3b893c94bf | -10.2482 | -54.368 | 2026-08-20 00:38:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab01251-6881-33a4-91b6-c8b85ab34bad | -7.7996 | -61.188202 | 2026-08-20 00:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d0fd913-53d4-35e0-9b62-d7b66810e382 | -7.9485 | -44.656502 | 2026-08-20 00:38:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c406c823-492c-3b52-a077-e63563be9a08 | -11.2064 | -55.044102 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 088ef037-c6dc-30cc-add4-1fa95b752724 | 4.3369 | -61.326199 | 2026-08-20 00:38:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 91cc2a12-a6cb-3913-be62-2ff8a33516b4 | -21.7024 | -47.127701 | 2026-08-20 00:38:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e35fbe62-1bc1-35bc-9ca4-f056270e0024 | -1.8335 | -54.477001 | 2026-08-20 00:38:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f35cc1c-6d30-379c-898a-20ae051a0fd5 | -6.8815 | -56.418301 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cae78c3-7100-35a7-9dca-b47fe32bfcc6 | -6.2389 | -55.405399 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20d876ab-236e-3f22-8aaf-e6ce4e5856fb | -21.705601 | -47.140202 | 2026-08-20 00:38:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d61d6cf9-5e2d-3306-9ce4-ce12b168d5ac | -21.864799 | -46.549 | 2026-08-20 00:38:00 | METOP-B | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6dfde392-2d40-3304-aa17-070050869024 | -9.1114 | -60.337002 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 139662f9-8289-319c-a417-8b65bb2a5514 | -14.2197 | -52.891701 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6ba7b78-bdb1-38dd-b673-2cd581bee01d | -6.589 | -58.975399 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10f66a1e-50a0-3cb2-8182-e7d7602aa47b | -14.1772 | -53.0644 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5dfaf62-5a8e-3686-9c00-7a7941973d5d | -8.6652 | -54.658199 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a46631a-4722-33d1-8f18-e1203b2207a0 | -7.3801 | -55.5285 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd3bdcef-4ecc-3493-a956-86f17b409444 | -14.3052 | -52.993 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
