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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 351c40fb-3299-3d0a-b63a-e86fdc0a7d97 | -10.77543 | -50.63631 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98c9fecb-d8ff-3536-81a1-d9e08fd14f26 | -9.0516 | -65.43845 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c4fde20-8f61-3f26-8fbe-e807b4b02423 | -10.91541 | -50.52975 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6e9536e5-64a9-3ab2-88a9-b13473616da0 | -10.94584 | -50.5385 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bdd44f09-7943-3929-a6bb-5e5f3c5f2dfc | -14.8654 | -52.60174 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46c4c490-4d6c-332e-952a-5189dbb6cbe8 | -11.23115 | -54.00871 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5cd0ac1d-3d57-39e7-bc96-52c5a25dad0b | -11.65091 | -46.73861 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18874078-93b7-33d4-889a-e670261f3fb9 | -11.74315 | -54.51881 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5128138-471b-3d43-afde-bc583d5597b8 | -14.1714 | -52.82492 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5eaef807-e8f6-323f-84a5-99031a73b073 | -11.82498 | -47.21471 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec16f1bd-9697-3091-ae88-46e9be728dec | -10.76294 | -54.04497 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a239ded-ff08-390d-bc8e-6d6e2cec57be | -11.76139 | -54.51748 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237364d6-b191-38e8-8dfb-2ca54f643bbb | -13.41674 | -51.79178 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cb5791b-2654-3d27-982c-43b2db36e1c1 | -10.79834 | -54.00406 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 220bb302-e041-32bc-bf69-d215f7054ea5 | -11.33969 | -48.38362 | 2026-08-28 05:12:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cf24574-2745-3dd7-a67b-2b6b5e70d1ab | -12.91777 | -59.88327 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59478bac-ee81-3068-8657-796df1795fba | -13.58615 | -45.77564 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1139f6cb-091b-3a3a-8e0f-e8620f932ebc | -12.69027 | -48.4309 | 2026-08-28 05:12:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a884b78-9a92-3e18-a26f-e3deb0eb380c | -13.47503 | -57.04287 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4653ecc8-4de8-3c5f-b09c-e85cc059f7ef | -11.83301 | -47.21204 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf1f81f2-efa7-3597-aae6-497eaeeedf60 | -14.93989 | -52.60021 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a373f944-e330-3b47-985c-96ceef3bd1ae | -9.05102 | -65.4416 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee3139ca-14b9-3d49-b657-f3f8c7c3357b | -10.3871 | -61.24356 | 2026-08-28 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c60146a1-da41-33f7-a685-469c0615c13e | -14.40727 | -52.5875 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f8c7bfb-3f38-31db-ab4f-7d37c6513143 | -13.42891 | -54.0148 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a41ae5b7-2c05-35af-b942-89ebbe2e9bbc | -11.16457 | -51.22303 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fdad196-6e21-3180-8d57-53688ccc54fb | -10.75704 | -54.03564 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1e8f14ee-44e9-3748-ab15-7920ff91b1c7 | -11.22583 | -53.99515 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0438f0c-bd2b-3388-a09f-82f5aa148a1b | -11.21865 | -53.99406 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 909cdd40-2da2-32c6-bdc9-ae23bbbb3807 | -13.4717 | -57.04234 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a0e0c43-8ca0-35c7-b26c-2132efedb043 | -10.7547 | -54.02684 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f83e853-6c71-3121-8c38-29c925331527 | -14.88632 | -52.60107 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| afd6cb07-cf36-300e-9bbb-b98842776818 | -15.31623 | -52.75848 | 2026-08-28 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7aa716c-f68e-3a2b-8e67-a132f6f013b2 | -12.9123 | -59.89445 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f65d50b9-6398-3fd2-a37c-6d4d2d5ed487 | -14.85832 | -52.62307 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c847dac-9e7a-3b5e-98b8-b3e9ab1533c4 | -11.22878 | -54.01117 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fde7c15e-cae3-3a6b-bafb-bd1370aff956 | -8.99786 | -65.43349 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 384d8c86-c319-30a8-b7ef-fa951df3cb7c | -11.64417 | -46.74552 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb8dd538-d29e-33c8-9b0e-99b3c7d693cf | -10.4235 | -62.99824 | 2026-08-28 05:12:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cd85de6-6c0a-3eba-9a5a-909d04c2b6b7 | -12.26364 | -50.58917 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9c3c81e-fccb-3aa0-96e3-0fdf61b742c1 | -11.69259 | -54.59288 | 2026-08-28 05:12:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8d8d699-0b60-3e7f-a42a-4e65b9a23400 | -10.83633 | -50.52066 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a6868dc-cc07-387d-8a08-c31c07b47d53 | -14.11282 | -44.38687 | 2026-08-28 05:12:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d8ad41f-02c6-345c-a89e-ba5ad41e3429 | -12.25973 | -50.58397 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7e4340f-b774-3b34-b7ac-820aa4e1b722 | -11.72372 | -54.52819 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c3b6cbdf-9c7e-3136-b314-da3d3d21c639 | -14.90659 | -52.59989 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c231fc7-ef30-3262-b236-bbfa4e77760d | -11.81849 | -47.22122 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8717add0-4095-333e-80f4-d1d4a5ade671 | -13.40338 | -51.41436 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9db9a7a6-64d2-3670-b2a3-961ce460e2bd | -11.72135 | -54.54424 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30003758-339c-38bb-a652-2830afc2f310 | -14.42253 | -52.59711 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62d694e5-c69b-3a36-86e2-8522ef4092ea | -10.78861 | -50.63818 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25f1dcfa-c17f-3798-a4b0-959e720b9581 | -12.76098 | -44.26893 | 2026-08-28 05:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97b419cc-c0e6-3a26-8e01-d670307d3473 | -14.87675 | -52.64027 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ba6360a-8323-33b1-b95e-bc8efb30cb42 | -13.42098 | -51.79226 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96048f88-ddbe-387c-a78c-4edac21ecff8 | -14.86082 | -52.60478 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31bc9121-6832-3130-b28a-f9e551a92778 | -10.75347 | -54.03508 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e6ac836c-e434-3ead-91be-038008ea74dc | -14.89796 | -52.60217 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eb30734-f95e-3368-ab77-c7dc33a3e143 | -8.59797 | -70.22058 | 2026-08-28 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7b7e004-b8e9-3b2c-b86d-a5c2a1020260 | -11.81894 | -47.21748 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| e412eefb-34f0-320c-bc10-66da2eecdd9a | -9.8406 | -60.27526 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d81e821c-a6e4-3929-9f8e-f4fe907fefd7 | -10.501 | -64.51276 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 19b03229-af20-30d3-95db-c3a6f62c5b17 | -11.22939 | -54.007 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cb19b1a-642e-388c-ab42-a7be987e885e | -11.23359 | -54.00335 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbce7aec-9e3a-3fca-9847-e8ebc69b5e67 | -11.22521 | -53.99934 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 211bf8e9-b4e8-337c-a7c7-c6fdfcd42595 | -9.87212 | -60.26714 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed7735e6-9dad-32c5-ace9-f82882b7e689 | -12.43441 | -43.42059 | 2026-08-28 05:12:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c0c202c4-6426-3802-b7af-5c07cfd2751f | -11.21342 | -51.24089 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9a0c4ee7-51fc-3ead-ad6e-a0d6d869b171 | -11.64563 | -46.73379 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cf481a0-f35a-3091-99f7-f008462e9db0 | -10.79883 | -54.01538 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb31230b-3388-30d4-8030-078d562cf401 | -11.28084 | -54.03188 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d98e9a3b-b804-31d8-b928-edc3a02c89c3 | -9.8809 | -60.25974 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6541739-acf7-3d1a-af2c-9e1a24f16430 | -12.24071 | -50.57383 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c0f3330-0603-37cf-af25-c4509b7ce88e | -8.99673 | -65.43979 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db60d565-3728-32d6-8454-0b7308b79b13 | -14.87407 | -52.59929 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcad40c2-7fb9-39b1-9d2a-6cec9d8070e1 | -15.8169 | -48.0947 | 2026-08-28 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98f9c64e-bdcd-376a-a900-04edcfc651ea | -15.76587 | -56.45226 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01ef5eba-0701-319a-8162-3b9ac5f6ccef | -14.86342 | -52.61627 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d7d58f4-3d26-33c6-81af-7e43558126c5 | -11.73133 | -54.54986 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5e9cb0a-b371-3c88-a2b8-47e0bcec5c4d | -12.25914 | -50.58855 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dafa925d-33f9-3edb-8358-46bb3d7edfce | -11.72079 | -54.52364 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53598130-a49b-3dbe-9eef-bd3fe617cd82 | -11.76078 | -54.52151 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d761da6-eff0-3600-8e71-0c53baff7e3f | -14.8764 | -52.6396 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc2ce407-62e9-3d44-beb8-bd964443710c | -11.29223 | -54.02932 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 74f8d883-5c71-3418-a1ed-76fcd59714cd | -12.28105 | -50.59625 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dbbefd8-b01f-3e0d-8f5d-774721441e12 | -11.76616 | -44.92001 | 2026-08-28 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae013893-7eb4-3d90-b407-af6b8200f439 | -11.19856 | -55.09533 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be5863c-2bf4-368e-afff-fb7265081ad8 | -14.93024 | -52.60997 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb9771a5-2be5-35f6-8961-8b8e890985c5 | -11.64619 | -46.72932 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8bff9ce-74c8-3429-93e0-2a6cbf9f4b17 | -13.40394 | -51.41016 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8fd3028f-aec0-3821-93a3-1a11ef15dc54 | -11.75433 | -54.51642 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d4e3cd4-42c5-3bea-944d-bafc45dcc012 | -14.41948 | -52.58915 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98cf0e27-a4ac-3418-9842-099bb7bf9529 | -14.59663 | -53.1554 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fc28d3c-5edc-3a40-847a-cc0d21bd39c0 | -13.47891 | -57.03985 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5501194-a908-3450-bb49-cd8e9317fed6 | -14.89319 | -56.3252 | 2026-08-28 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86fca97d-6672-3794-a262-a8eba9b48242 | -11.22943 | -53.99569 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4541bdd4-5c00-3c1c-8d12-aa9091c076f5 | -11.73783 | -54.53031 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c6c2647-193b-3ed9-a4ca-6f73b84661c9 | -11.22999 | -54.00283 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6eb596f-5669-3525-ab81-37c0199d8151 | -13.4814 | -57.04404 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a718671-1c5c-300d-a911-c876ec4c7a6b | -11.73137 | -54.52522 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7c9adc4-ff7e-3c02-93d4-f503c7dc6f98 | -10.75286 | -54.0392 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README59.md)
