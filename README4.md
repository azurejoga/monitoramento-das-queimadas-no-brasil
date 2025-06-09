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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d1dadac-2153-37cd-8d95-68f064369787 | -14.25117 | -52.46744 | 2025-06-09 04:08:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6d1102d-60b4-3a68-ba72-cfd3bebc7d83 | -18.05833 | -39.91431 | 2025-06-09 04:08:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1011e75b-09d6-32ce-8844-83b2c3565f31 | -17.77628 | -42.80886 | 2025-06-09 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce13eee4-a039-3cbf-a711-df2a836bf242 | -10.25474 | -46.91253 | 2025-06-09 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37ac24e9-c8fc-3cdc-badc-3d92ee34201a | -14.23395 | -45.47477 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b18a988e-9741-3ab7-90ae-185c77bc38fa | -16.37551 | -48.03294 | 2025-06-09 04:08:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c2e62e2-c284-3a56-8855-a698673a1277 | -13.55638 | -44.19698 | 2025-06-09 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e25b9f56-93c3-3402-a595-31f5d6393517 | -17.59575 | -43.19577 | 2025-06-09 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccc18970-c472-32e6-8693-553ee9945f3d | -14.24923 | -45.48944 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebccef41-da50-3729-8e66-88186bdde2cb | -10.74245 | -52.5092 | 2025-06-09 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5fac6e7-89e6-3c17-8ab5-328218c6272d | -10.84756 | -53.77443 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d11f5e4-61cc-3c7d-be90-06886b827e60 | -17.77684 | -42.80515 | 2025-06-09 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbac350b-ac46-31a2-84e4-21f7a08e4079 | -13.01766 | -47.8664 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e63577d-efc3-3e2c-9c3a-b89c39e12f07 | -10.2459 | -46.91348 | 2025-06-09 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b9c193d-e96e-3021-90f4-4e8b857f129f | -10.74403 | -52.50916 | 2025-06-09 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d8d0407-0680-31dc-beae-3ad2419ddbab | -10.27691 | -46.99322 | 2025-06-09 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b856d23-1058-3646-97e4-f867a738bd49 | -15.09079 | -44.81484 | 2025-06-09 04:08:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6211d247-7cc2-33c0-9a99-4558e809f942 | -13.48797 | -44.13788 | 2025-06-09 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5273b935-1afd-3597-9236-2127273ff5d3 | -13.01462 | -47.86044 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 422669c2-c5a8-344b-9d5d-e181e93c2d71 | -17.67828 | -42.73977 | 2025-06-09 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9451c61d-1786-37aa-9fe8-6a81bf4b450c | -13.01856 | -47.86116 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82687d40-2655-328e-8b34-aaed014a8c04 | -10.5115 | -44.89336 | 2025-06-09 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff9d29c8-5bb4-349b-80d1-38ac1d8bdf41 | -14.24299 | -45.48433 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67062ae0-d7eb-3675-a6b9-89315a1277aa | -11.78164 | -54.78138 | 2025-06-09 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b0ff1db-159d-3abd-ad12-4a13fbc060af | -10.8406 | -53.778 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 78f337ba-740d-3a14-b00d-03a1da1cf78f | -10.26821 | -46.99697 | 2025-06-09 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e06572b-4941-30f2-b9da-089e9b3c1b7c | -12.27543 | -44.60494 | 2025-06-09 04:08:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abdb8712-f9e8-3851-8b01-aead068fa412 | -15.83663 | -42.5947 | 2025-06-09 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2950de5b-5636-3951-9f4f-6452d6d5321b | -14.24988 | -45.48557 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d152c11d-9032-326f-903a-f032343d065e | -11.37526 | -39.07178 | 2025-06-09 04:08:00 | NOAA-20 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 640c919b-c918-34c8-a742-9fbab9e0ed95 | -11.05618 | -44.27099 | 2025-06-09 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ddd12ae-56da-31df-87c0-e157b40cccfc | -10.25559 | -46.90764 | 2025-06-09 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6ce6d99-a64d-3acf-b1e9-75fbcd409e0a | -10.24611 | -46.91603 | 2025-06-09 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62a08a10-29d6-37d6-8a45-6091390a72bb | -10.83966 | -53.78274 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca8658c0-ac73-3eb8-b39a-de6df42c1566 | -12.54807 | -45.42329 | 2025-06-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a235e78-3bac-30ad-b1b7-2d0d2e66f351 | -13.01696 | -47.86256 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53cc763d-149b-37a5-9389-5670806754b1 | -13.01997 | -47.86855 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1be83209-270c-38dd-864e-5fafbd1d0419 | -13.02091 | -47.86329 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b50cbe21-b05b-39b4-aa13-d21858a0bc1e | -14.23739 | -45.47538 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e90706f-e5a6-3dd1-ac41-20b20f0a1a65 | -12.54589 | -45.41478 | 2025-06-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34253f19-5aed-314f-92ab-a908ca6db474 | -10.31341 | -47.01511 | 2025-06-09 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97dc556e-28ee-3af6-87aa-52e06f85cf15 | -17.38563 | -42.65897 | 2025-06-09 04:08:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b826c9c-2bcb-31c5-a72b-4f3486ccef4f | -14.24643 | -45.48495 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6f91d2f-cd59-3d03-91e7-c5fec8265c31 | -10.04679 | -49.19813 | 2025-06-09 04:08:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f804f43f-fd1c-37f0-9365-2ff8ab1b8f2b | -15.51956 | -42.62179 | 2025-06-09 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5506845e-489e-3251-931d-da4399755060 | -10.84568 | -53.78389 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d567354b-0c8e-3b81-aefb-ad1dfdf28de3 | -17.09463 | -43.80416 | 2025-06-09 04:08:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29f9022c-8f77-34e3-9f75-f994d9e9d7be | -12.54873 | -45.41935 | 2025-06-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27b27eb0-185a-3b9b-b8d7-e8ec65c3f06e | -14.24515 | -45.49269 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ce620f6-e6bb-3836-be39-008c5854fcb2 | -13.50523 | -47.86198 | 2025-06-09 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f70724a3-e6cc-3d2c-86dc-20d65efa7983 | -13.5092 | -47.86239 | 2025-06-09 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e968c6f7-a25d-3d64-876b-7fa4b44564ea | -10.85169 | -53.78515 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a47fb6ec-ff30-37f7-a6b3-92d99cbada40 | -14.93263 | -42.28978 | 2025-06-09 04:08:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 121e9d03-3a55-33ae-bf18-173c7394d0ad | -13.01207 | -47.86709 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2833d4a-5c1b-3be7-b178-34c59161f588 | -14.25053 | -52.47067 | 2025-06-09 04:08:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4340883b-6bb2-3d1c-b5a1-66b579994f41 | -14.24083 | -45.47599 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95d1aa68-cd9a-364c-af1a-2258cdea1351 | -14.93653 | -42.28665 | 2025-06-09 04:08:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8398ec4-7224-3691-88e7-d6dac590087c | -13.93816 | -47.20974 | 2025-06-09 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0de2fb9-59b0-3367-a2f2-fcca528225ea | -14.23955 | -45.48373 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc4105bc-9aed-3ab4-8167-2da02fe05abd | -15.83887 | -42.5947 | 2025-06-09 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1386647f-fbc1-3743-9889-4d7363f35dd8 | -13.01371 | -47.86567 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4a993e4-d9ff-3f1a-8817-cdb14e38d5f6 | -10.73844 | -52.50817 | 2025-06-09 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b27262fe-a6fb-3e0e-94a0-3fa4f790f110 | -12.55156 | -45.42392 | 2025-06-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37855c10-d885-3a2d-8bac-3039ab378f7a | -16.68167 | -43.88266 | 2025-06-09 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f95b7970-a11e-3b4e-b7f7-9bed2b57d6f2 | -10.64665 | -44.4804 | 2025-06-09 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45f795ab-a658-3ea1-a02f-f9c5256f6613 | -10.85262 | -53.78043 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04fc0c26-1ae5-3a76-868e-fed2111271f0 | -15.09415 | -44.81542 | 2025-06-09 04:08:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 059e2748-489f-3dc4-93c7-3316def6290d | -11.37226 | -39.07325 | 2025-06-09 04:08:00 | NOAA-20 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae981410-d63c-3032-8c2d-427b0e4f931b | -10.26429 | -46.99636 | 2025-06-09 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f22fd3e-e715-3b9d-8439-d539416f162e | -10.27213 | -46.99759 | 2025-06-09 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d07792f-27a3-3331-a970-c03185a2d4b9 | -10.74333 | -52.5129 | 2025-06-09 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fa0dbc8-dfde-339e-8ed4-31079182ff78 | -14.24235 | -45.4882 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7bbd8a5-8252-3c31-a67d-33bc5573ee5e | -14.2361 | -45.48311 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59660a09-6d69-3832-be9a-922d28fdf905 | -17.389 | -42.65952 | 2025-06-09 04:08:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 304d2aad-72c7-3730-aefa-a3686b1945af | -16.58254 | -49.26103 | 2025-06-09 04:08:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a05d1e7a-54e1-3a71-8b5b-1ff85227cb12 | -13.07514 | -49.57676 | 2025-06-09 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9400b9f8-af90-3e07-b42d-44a47e20b341 | -9.91906 | -49.83358 | 2025-06-09 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b4332b5-d9f2-350c-bfa1-844de8667c67 | -17.77964 | -42.80942 | 2025-06-09 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14080f89-00ea-306a-b3ae-477776a6e45b | -12.54523 | -45.41873 | 2025-06-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c096b65a-913e-3e25-87de-b61c14e8b6d0 | -15.841 | -50.8889 | 2025-06-09 04:08:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5097f798-d47a-3345-be02-7bd72033cd38 | -10.64322 | -44.47982 | 2025-06-09 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5fd5aec-b4d7-363c-8c62-46259204e3e6 | -13.01301 | -47.86185 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c0ce359-a1d2-37e1-b1ce-c1ce5f6f5d80 | -10.85076 | -53.78982 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d89d460-1a60-35dd-95d3-476ecb15f38c | -10.26909 | -46.9919 | 2025-06-09 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ba51ab1-0322-3a0c-b258-ef8c4920e02f | -14.23804 | -45.47152 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2af2b09c-4d92-32d7-af1c-8e90c4a345c9 | -10.25 | -46.91673 | 2025-06-09 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6a6300b-26f9-369c-9cbf-79b1d7ca81c6 | -14.2333 | -45.47865 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f65f7b6f-f73b-3e0d-91a8-93ff875cf51b | -14.24363 | -45.48047 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49b03720-af79-3b2b-813a-19b3c5f1ecfb | -10.64261 | -44.48359 | 2025-06-09 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 437679c5-f33f-3871-bc8d-eb89d493e8a3 | -12.68853 | -45.05815 | 2025-06-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23594a52-f1ff-3bca-b305-683743482276 | -15.07833 | -48.94526 | 2025-06-09 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26bcb98a-ecec-3314-bef9-5f4d5cd76f09 | -12.54174 | -45.41811 | 2025-06-09 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47db0cc9-6fe8-3b6e-a8cc-65624d244783 | -13.00976 | -47.86495 | 2025-06-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7cd8c40-054e-322c-8d75-af0b10953201 | -14.23675 | -45.47924 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fac58cec-6e44-3a20-882e-4e7a58da429a | -12.98295 | -46.749 | 2025-06-09 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08862a19-fe36-3b7c-b870-bc64322aad70 | -14.24019 | -45.47986 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 356fe010-1f88-3b31-9e4b-61a857eb892e | -11.91257 | -54.82903 | 2025-06-09 04:08:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 121025b9-3d85-3366-ad04-2c218909e92e | -10.84663 | -53.77911 | 2025-06-09 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1174aca5-2b7d-349a-a2d8-4351d4f7e9ce | -18.05703 | -39.91661 | 2025-06-09 04:08:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 14ed4bc0-c5ca-3d59-9b22-220e2fcc858f | -14.24579 | -45.48882 | 2025-06-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
