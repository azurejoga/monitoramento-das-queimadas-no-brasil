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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 029b99d7-af83-305e-8029-822b337b163d | -9.38731 | -66.52268 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58ad7778-8446-3507-998e-7aa1284603c2 | -11.01468 | -59.23416 | 2026-08-29 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac5ca5df-a3a3-3145-8292-85913969a28c | -8.34742 | -70.85076 | 2026-08-29 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46ac5583-8ea9-3633-a007-0a2032bc34d9 | -7.58689 | -61.33892 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 38d73fca-2b48-3738-8097-5173bc6cf114 | -8.53138 | -55.3576 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b0c9dab-019a-312f-9a55-cae47d6fc38c | -8.53243 | -55.27076 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e197438a-34c2-3a85-b5e7-0b5fbffdd996 | -7.56263 | -61.30785 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f17d53bc-3c55-3599-8cf3-9d03ab39b18f | -8.6079 | -70.2087 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7068a9c7-9f2a-32fd-a374-83a48205df61 | -11.71089 | -54.53724 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eed4d0f-96ef-3f15-bb6f-d5449656e20e | -14.20412 | -52.84193 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2988bfcc-2539-3eb0-8d24-53fd228b5cb5 | -8.53162 | -55.26977 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ecb99b6-0c17-375a-b460-524131f022d5 | -11.19228 | -55.10262 | 2026-08-29 05:38:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c83b1034-bbf1-3f01-bb0f-472efd6393a4 | -8.53648 | -55.35756 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4a01809-933d-3aa7-93f9-9ec6a4303a7b | -9.20811 | -71.8597 | 2026-08-29 05:38:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e4c80b2-b0de-3cd1-8369-66f05d9bd564 | -8.94884 | -62.38085 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adfbeab1-595f-302c-958f-54465e8e2814 | -8.5939 | -54.77303 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2af8a96-cebf-3e60-b86c-b1541f038fa5 | -9.26086 | -57.0811 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a643fc0-3b05-3e40-bce3-f210be325395 | -14.92342 | -56.33532 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99349ca9-708a-3559-b11b-094e94bc8699 | -11.26532 | -54.02714 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e279079-d073-3e48-83ef-1fc368bb7d65 | -11.27329 | -54.03848 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4570f9d2-a0a9-354a-9e82-cbf7785c7ac2 | -10.55679 | -59.61781 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 042b7e52-43d9-3b57-8659-4a75a23ecaef | -9.97133 | -53.93092 | 2026-08-29 05:38:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 06fab718-ce72-3191-8f09-3b997385f6f6 | -8.59164 | -54.79687 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a001ae6-fd42-35cc-8390-546248730783 | -9.86877 | -65.02943 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e341f2ca-c064-30a8-9969-7edcdf5e8273 | -9.30985 | -56.79705 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aadcca90-a8ba-381e-8c53-3c87e56a104e | -9.43575 | -51.6889 | 2026-08-29 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 894f89a3-fd96-3c00-ad31-a490f2cbd4ea | -10.56946 | -59.61588 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed79aeae-7aec-312d-ae02-cf3323f2036a | -11.72324 | -54.52945 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2918d8ec-9047-3edb-ae98-b500130f9403 | -9.30911 | -56.80245 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af6a395-3eea-37d8-ad67-2079d3f094d1 | -11.03044 | -57.2174 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e81d026c-b884-3d44-8057-a0a798528f66 | -14.90773 | -52.61958 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e827358c-2df3-3fcb-91e0-6cf37651b6e1 | -11.71716 | -54.53386 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c11826c-34eb-3a11-8a63-e57141828707 | -8.59848 | -54.78679 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 015d1e2a-55b5-3c41-93d1-229553f762e4 | -11.26913 | -54.04529 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b1be8b1-95db-359e-95c9-02b04bae47a3 | -7.59338 | -61.344 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b39d1626-68c4-3d82-83ae-47ba12820d00 | -8.94835 | -62.40775 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 578280ef-cce6-3b55-a6bc-6ec421fa13dc | -10.75502 | -54.03429 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 423323c9-40c8-3af4-a3a1-60f428ed450d | -9.91523 | -60.43036 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a25c13a-4e62-36ab-a313-8dcdfe032c23 | -10.40755 | -61.19558 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aedf95f-d39a-3645-8811-a12bd3df806f | -14.20471 | -52.83627 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b57c148a-848d-3352-8673-7fbdf11cbf26 | -8.99947 | -65.4517 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12004431-d3ec-3fce-be25-914ec40d9d5c | -8.59705 | -54.7981 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5bf628b-23df-3f18-a056-7f783af8c8d6 | -8.15547 | -64.00343 | 2026-08-29 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee6bf2cf-b129-390f-82d3-2b4eff618b74 | -7.61932 | -61.36433 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 975b847f-96a8-3f0a-b879-1c7ac47c84fe | -7.00656 | -71.65778 | 2026-08-29 05:38:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b5e3df8-d43c-3116-a91e-73abc9d350ac | -7.54821 | -70.00121 | 2026-08-29 05:38:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d6ddd92-67fb-3b08-8920-6616cf38fc93 | -8.94779 | -62.4115 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e91f47d-0179-33a9-9994-5b1bde8db344 | -10.50815 | -64.3081 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 43ceb4ef-bdf6-32c8-8cec-b58360ccc757 | -9.61107 | -55.12223 | 2026-08-29 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9359499a-8db7-3f76-86d1-5ff33e91a2ea | -11.26192 | -54.0322 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd65c761-7c4c-3d4e-8d32-b72ab598869e | -7.99959 | -61.40922 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b846fd7-8f90-3380-b7a6-f5243f173697 | -9.92535 | -60.44152 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6bc43e0-99d5-3373-b4b5-651d0ecf8716 | -8.5989 | -54.77738 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d34e2718-d5cb-3e40-8d83-f352e05f29b0 | -9.00281 | -65.45222 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e9b6c4e-71f4-379d-a9ac-e721b264086c | -8.65946 | -62.84047 | 2026-08-29 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36172b8f-8413-3570-84d5-9e46aa58fbf9 | -14.91803 | -56.33468 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff1186c8-16fe-3a92-90d4-e404aaa01e7b | -8.67919 | -62.84725 | 2026-08-29 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 361b8f4d-ed54-31a9-a146-f444a42c8be9 | -9.43208 | -67.41839 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e955c171-6a7e-3b4c-82ea-def18eabebac | -11.03862 | -57.22957 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 64e73b99-124f-3757-80b0-45c45e0b3baf | -8.59437 | -54.77518 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 141715b8-66a5-3f9e-90da-6e2232d3aa6d | -7.55969 | -61.30328 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 086bed1e-709d-3652-a203-67f587369ee0 | -8.59594 | -54.79944 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bff8e87-c64d-3f77-abd2-55e58b0c86e5 | -9.76151 | -64.97598 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d2bf32b-c97d-36f0-88b6-992aa76a644c | -11.26966 | -54.04104 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35f5a2c6-64b2-31ff-848b-1e1c44141584 | -14.21082 | -52.84208 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 895cff9c-b67e-3fb2-9865-26e57fc300c6 | -10.48663 | -64.49127 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c507568e-6687-3279-9ea9-6535f5078d93 | -11.04003 | -57.21882 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81b3f61b-5219-3249-b242-27a7c27fbf81 | -9.02875 | -70.91608 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd8bc6e5-6216-345a-857e-4287becfc87c | -14.89846 | -52.61982 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 507e111c-70a9-391b-9813-eb84c5a13ddb | -9.43504 | -51.69458 | 2026-08-29 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce216e9c-7abe-3848-93b2-60da1f92d6a3 | -8.65608 | -62.83995 | 2026-08-29 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0757e1f5-914f-3f85-8148-100f290390de | -8.95103 | -63.27214 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 249a5226-0d4e-3a3f-a8be-91b2d81d96a0 | -8.60487 | -54.78039 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc62bd1a-c5fe-3056-9d0e-f00cb97e09ca | -11.27072 | -54.03247 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ba25827-bb83-365c-a549-91117fc4222c | -11.23116 | -54.00932 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7099f6cf-fecc-31bf-995b-ccc07d12fdf6 | -7.84125 | -62.31221 | 2026-08-29 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67e5f5c5-ad3a-3179-818a-87afe604a501 | -10.0949 | -68.13772 | 2026-08-29 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6178abd-e479-3416-bbf7-4e35562a78b1 | -8.53665 | -55.35827 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57e5e879-8644-37f3-bbfa-18aced50113e | -8.24751 | -70.10383 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98d2acf5-2977-3ee9-baf7-4e4a38cf62a8 | -8.59875 | -70.21117 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f827d6e-9bbb-3e8d-be70-a84d917e0393 | -9.16881 | -59.38345 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef113017-4ad8-3744-b81a-c93d9dafae34 | -8.53733 | -55.26727 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7235803-1759-37cc-bece-5bddda86eca4 | -12.78657 | -60.48639 | 2026-08-29 05:38:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d57a2d5b-cd26-3874-be5e-a41822a1e1be | -11.02768 | -57.23847 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 902c64a4-4504-336b-8b04-2c812bd5f35f | -8.95914 | -62.38243 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| babb9190-3679-3d4e-90bf-6a33b4681bf2 | -9.90867 | -60.16002 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5f7c2a2-64c5-3dde-89c2-5a393146c181 | -8.94605 | -63.28233 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 427821a3-1bbf-3ecc-96c7-f03485a4b5b4 | -11.03113 | -57.21208 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0b0f46a0-46a4-3dde-8a97-37aa8236d517 | -8.95291 | -62.40073 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0419d39a-40a7-30cb-a3f2-285438d38a2f | -7.55908 | -61.30731 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f45ce419-28a2-3393-97bf-7b454cd68db3 | -11.71643 | -54.53701 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 926d152e-55d6-3d6f-bd03-077210033f92 | -9.42919 | -67.41376 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e31a80-82fb-3e55-a2c4-cbcc44104fc4 | -7.9995 | -61.4107 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df8242cd-6b0a-3fc0-ac8c-26055202ab3b | -9.59056 | -61.02869 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc08aff4-69d7-3f85-92cd-96bb1fa6bbed | -9.21558 | -51.54068 | 2026-08-29 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbe6ac95-28ec-3f0e-86ab-12007375264d | -10.46899 | -64.49564 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8911dd4f-d73b-354d-ae17-f05d2a6daac0 | -10.485 | -64.50176 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| de2ffaec-0a5c-3d08-8a93-3015d17184b3 | -8.60654 | -70.21664 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| caf4851a-ee50-3564-8af0-ed36a61ce4bd | -9.03999 | -65.42909 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c56ec540-7e81-30ae-babf-7b1ebdfb3c9f | -14.47475 | -58.52509 | 2026-08-29 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README65.md)
