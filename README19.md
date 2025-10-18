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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28a41dc3-d911-3264-9d7f-10832a154c01 | -6.88791 | -45.43389 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f8445043-b416-39e5-b264-9a6251ce6af4 | -11.49351 | -44.03885 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9794c8ad-5ac3-3f7c-8849-e0f39c189e97 | -13.77071 | -48.22705 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4181e7c0-cb8c-3c2f-9200-33e5c108d60a | -11.99529 | -47.14958 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 617413fa-e31d-302e-a5c4-56ba87cf13ab | -13.73309 | -44.23104 | 2025-10-18 04:02:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88767fdc-fb28-3aff-a359-872d074d73b8 | -10.53474 | -44.50798 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e889ba56-6df0-3d4f-b55f-f7e2e9364315 | -10.49802 | -43.27714 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cab360c-40a2-3023-b196-83d27a236460 | -10.18383 | -44.53616 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 181535ae-76b4-31a4-ae5b-dd2948b5570c | -11.63826 | -47.86047 | 2025-10-18 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b4b5d5d-1b06-385f-a72f-4d06f14ea751 | -13.81112 | -45.51506 | 2025-10-18 04:02:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03b9779f-e855-3141-bc49-df3a4a11cba2 | -7.16468 | -46.21464 | 2025-10-18 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 150a27d9-c4ab-31d0-a512-3ebd366d1303 | -7.66586 | -44.62856 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8beb76e6-0735-3493-8eec-96a62fe44931 | -11.47563 | -44.01469 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da1f8313-d6de-35a9-a75e-879684b32c93 | -7.36787 | -44.06427 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e94f9d6d-24dd-3cc5-b936-921afec6ac1d | -12.36405 | -47.18132 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33c1b634-c2bb-388e-a4e7-ef28199abcbb | -10.49146 | -43.44582 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a0d043e7-f6b9-38ce-a2ae-360ea121d8e6 | -10.44172 | -49.35779 | 2025-10-18 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 925e3de7-ac82-32aa-881b-d3ea265698ca | -10.24961 | -44.03227 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98debcf5-78a6-37ff-9ab8-0c6dd2b5d6ee | -13.73377 | -44.22701 | 2025-10-18 04:02:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f0484b-d5bc-3329-91b1-2da7f986206e | -13.92267 | -45.59738 | 2025-10-18 04:02:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5349a568-e7ce-3c58-a122-c5eef4cc771d | -10.2518 | -44.04916 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b561092-8a1d-388a-bc35-0b959813aea1 | -6.744 | -47.37311 | 2025-10-18 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d19595f-e906-3b55-b2f7-6195544bda30 | -11.36219 | -47.30113 | 2025-10-18 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee44b221-545a-3bec-acc4-bb9625ab2407 | -10.62263 | -48.01751 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38c30279-2d69-39d4-9ace-2aa13d9373f0 | -11.35161 | -44.25601 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0ce905e-d012-3337-8d72-a55c9cdd46b1 | -13.62956 | -43.95274 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bd89050-e77b-3d71-b4b5-33ed489e7925 | -7.5403 | -43.93344 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| faaeaed6-e0aa-303e-83ca-b75285bbc940 | -11.00666 | -47.90169 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f7922db-52e0-3193-a992-049e601355fc | -9.14306 | -46.66626 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 638b2bb4-f3a6-3793-b31b-aeb5be88b058 | -7.34177 | -43.86256 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| de0771f4-3a11-386f-833e-9b975630f2c8 | -10.50482 | -43.45208 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47ffa38d-439c-31d7-8092-d4fb7baca593 | -7.66425 | -44.63806 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a9bf16f-61b9-396d-9dc9-d47770b9e48c | -10.5035 | -43.46005 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 958fe884-1aaa-3551-8c8f-699cf43cf2d9 | -13.42117 | -48.08089 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22403377-d6d4-38fd-8ed4-e9624358190c | -10.50943 | -43.42422 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 142b9006-4c28-35aa-aa41-95d98c766a97 | -12.70148 | -48.62368 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f8ada7e-7700-3c0a-9519-b768e29c5ebc | -7.98306 | -44.15487 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2ffc23f-2425-3c27-a6d8-bc97ab24210c | -10.78914 | -44.09594 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8879129-67b9-3d38-95ab-ce00d6cde397 | -9.66825 | -48.52462 | 2025-10-18 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 073ece43-ce6c-3200-bfe9-a30082b7313d | -13.22385 | -43.97453 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b1dc57f-2f59-353e-b2f3-6815a997eeab | -8.55033 | -50.08051 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 837651fa-d422-39c1-ad9b-3372e68dc189 | -11.58535 | -44.0535 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a6b857ca-0670-3093-a1af-e83bbd6a3857 | -10.53562 | -49.54942 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed91e4b3-5077-3c70-a958-0fdffd49146a | -7.48594 | -47.03271 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c31f9f22-dcbc-3e39-a442-09e8dac28287 | -11.38042 | -44.26093 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cef2e0f-147d-33ec-8aa3-e9928c576287 | -12.16941 | -45.08248 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1474e957-9d02-39d5-8b01-dfb962028ec2 | -10.09129 | -47.66042 | 2025-10-18 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 424033b7-ff80-337b-ab82-d57d91a1e83e | -11.37682 | -44.26031 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4680f016-ae1e-3d74-bc93-e15ac030dcab | -13.40962 | -47.97139 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25c5bcbf-7094-3a53-8758-c5faa371ce9e | -11.48422 | -44.02881 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 296bbf07-33b4-3bf5-82d4-ee6ab087dc3f | -9.08215 | -45.14338 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1dec4cfc-cf6e-3001-9928-646d995d539d | -8.16532 | -43.3011 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 51fba837-2a79-3336-be88-ab315918d657 | -12.15453 | -45.07989 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b62b0c3-d8aa-3cd1-9d68-1785c5dbfb12 | -8.78294 | -47.92652 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f73b7c55-31ae-3993-84c3-dacc68cb5185 | -8.45435 | -44.17027 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c930363c-945a-35ee-a9de-85a62cc9d593 | -12.91696 | -48.58312 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3040255-fbd9-36a4-b153-fab85179da36 | -13.86802 | -45.46178 | 2025-10-18 04:02:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36685ea9-7434-381d-a4f2-b3396f583940 | -10.15281 | -44.52687 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73cb0a11-2750-3e56-a09e-32d97813a9e0 | -8.56519 | -44.60256 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f32f71f-3b0a-38d1-98a6-c99287f8e723 | -9.64752 | -48.72555 | 2025-10-18 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68e3e16b-26c3-30ed-964c-e265b604799f | -14.94125 | -41.96108 | 2025-10-18 04:02:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ec3b2f6-65ff-318b-8aae-0c1a73d21dd4 | -7.17286 | -42.37482 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e64ef5d8-649b-39b5-8067-01a6a6962b3c | -8.17341 | -47.04065 | 2025-10-18 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d68b108f-43ed-3e33-889f-b2c3de3d7d23 | -11.61104 | -44.07484 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 83441e4d-255d-3294-a604-2f6265809e60 | -10.11938 | -44.5442 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37674271-f1c6-36df-8165-70742f877806 | -12.36979 | -44.07996 | 2025-10-18 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18ad939c-8d8e-3891-9135-29c735ec2417 | -10.42286 | -44.91209 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b07c142-0eee-3100-84ba-fb18061cdebf | -7.12463 | -47.23556 | 2025-10-18 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cd3722f-8522-361c-8d21-9fc9a9e4ae6b | -11.60966 | -44.08309 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 27251a7b-71a6-3e5f-bdba-2bb62d0093ca | -13.83475 | -42.62786 | 2025-10-18 04:02:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d272bdd0-7d2a-3863-91f4-d302792d5a79 | -10.70879 | -44.54912 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cffcd320-c86e-3e3d-9cc0-ff5dcc1a5c19 | -12.36559 | -44.08336 | 2025-10-18 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27426203-a654-37db-91f6-c1fddc71f0c0 | -6.93969 | -43.67433 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d32b45a-907a-3f50-8951-0b844f6531ac | -8.53603 | -44.08223 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94621191-94ab-3a12-9924-79438c31bb07 | -10.71749 | -48.14752 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed3d7b3f-3613-3e72-9994-ea8611791985 | -10.36945 | -48.05785 | 2025-10-18 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3caa54d-a4fc-3bdd-918b-1383b37f697c | -11.46288 | -44.0252 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7780e417-e39d-33c3-af92-5609fb7ac878 | -13.46118 | -48.11113 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d99133eb-a208-32f4-b700-1021f40d1ece | -9.13876 | -46.66544 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fea7f406-2d7e-3122-95f1-4167f8a616d1 | -10.2361 | -44.06924 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5146ded0-fc90-33b8-b04a-dd975e5a89cc | -8.21449 | -43.30793 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8e754662-ea17-3866-b9e1-718c5a65e664 | -13.48463 | -47.95572 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 733698d4-ffa9-37db-ac44-c4224720726b | -10.49497 | -43.4464 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b5fb46e3-ffcf-3b3d-8dbc-f7518969ada5 | -13.02721 | -46.94942 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b72f7d5c-622e-3137-9dfe-4451573fb74f | -10.69626 | -44.55603 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd1272fd-3188-3886-a2cb-886b24634695 | -11.60897 | -44.08721 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e1fff02f-76af-35c3-89f8-af6127cb8f45 | -11.37618 | -44.28631 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bf80ac0-3d61-323b-919d-80a45ed2a9a1 | -7.16255 | -46.21321 | 2025-10-18 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 29bc5b9f-7e5b-3ca6-898c-164af6d3adf6 | -13.51384 | -47.99694 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffe8b406-896f-3a20-9a9c-8b3d64f5912b | -12.80062 | -48.65 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ddb5d5a-d07e-399b-8c2d-b7e02d85d151 | -11.84877 | -38.19965 | 2025-10-18 04:02:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c634a148-b7ce-37db-89ed-8c2849ed1d5f | -11.60679 | -44.07836 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 79e3e1ed-e8e8-3be4-8231-6ead36e7a4b0 | -9.21668 | -40.56131 | 2025-10-18 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d704b5ac-25cf-36d7-bb18-0a0029a42098 | -11.37187 | -44.28992 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 986cd22d-fb9f-3533-a21c-0f62a6580578 | -8.19288 | -42.35 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7290da32-a034-3082-a843-ebbfcaced2e9 | -13.22733 | -43.97514 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f8b546d-d697-32f2-8a26-2288425ebaf0 | -8.36639 | -46.19763 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87ddf9b0-5082-35ee-a041-2c1dcd5f9108 | -8.23374 | -44.00381 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a750d6b6-1963-35c3-8fad-52ad4401df3c | -11.36632 | -45.26596 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6779741-ab5c-3db2-9e50-4ee1c9eab4b2 | -7.11637 | -44.72851 | 2025-10-18 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README20.md)
