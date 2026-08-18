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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19d85d8d-2399-3e08-b5d7-f42bfc17e684 | -6.84627 | -59.00589 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb6ce563-d30c-32d5-8e37-2bf259e30028 | -6.53281 | -43.10972 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74288069-9e8d-3860-80c0-aadf21e56299 | -8.58932 | -50.34417 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 34c9eb5b-b37d-3cee-8022-0b43c93caa56 | -3.68499 | -47.65047 | 2026-08-18 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 53863b7c-4e96-31f3-bc83-f9d9a547f971 | -6.4046 | -54.94579 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5752e3e-a0c7-364e-8c08-fe1c9c0adb06 | -6.70464 | -58.94061 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 710edafc-a200-3376-b02d-8273e1066685 | -8.59593 | -50.34977 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 66b2c672-c15f-3a91-bac5-11b63013920e | -6.69604 | -58.95008 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4971d802-fcb9-392e-a9c1-3ddc757ce390 | -6.95355 | -59.04011 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6196fc29-1b43-3f43-9b1c-ada581e8c922 | -5.1427 | -56.28298 | 2026-08-18 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f97834c-03de-320e-a524-22a65b26f30e | -8.49159 | -48.80596 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42e1c1f5-324f-371c-90ad-1f2d57c37dca | -4.53705 | -42.93118 | 2026-08-18 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d0dc817-3dd0-30c0-a7f1-1ef77e58bc40 | -9.59499 | -45.37364 | 2026-08-18 04:38:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dba9a48-f6cc-3ffc-af77-05f48e63dfb9 | -8.5764 | -54.70864 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9da73cb9-e634-34f4-b728-37925f9eddf6 | -8.36751 | -46.35775 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f805259-db1d-372d-939a-92bb3deeadc5 | -9.28386 | -50.32492 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac87c911-9d13-3a80-a9fb-6a0af6ec4958 | -8.74223 | -45.31663 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bcd42cd-60ed-3c99-8350-5453dc3c1c5e | -4.4903 | -42.55842 | 2026-08-18 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45a65e76-7cea-3652-b372-0821e5ebfc2b | -7.53802 | -46.61889 | 2026-08-18 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4ecdee8-b2a5-36b4-b753-1fac0c32ca02 | -9.76144 | -46.70475 | 2026-08-18 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac4eac44-3ed9-34ab-bf1d-de6def36fa58 | -7.6068 | -60.82865 | 2026-08-18 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bcfc5b3f-f64a-3dd2-b17d-3d2caa56c27f | -6.70563 | -58.94505 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc904cad-7967-3feb-8727-ddd2fb0337b4 | -3.51427 | -48.03224 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0129fea2-e349-382b-92f1-37262e260472 | -6.75653 | -59.17518 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8b7901c-1a7e-35b9-bd18-038b66919f36 | -3.50915 | -48.03562 | 2026-08-18 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc7f8264-8b79-3a22-963c-1a48c735105a | -9.45968 | -51.61957 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 148d4da1-31f4-36b6-beca-bc5c04612447 | -7.45953 | -46.15339 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ea16db9-82cd-3dea-a909-bf4670b330c5 | -6.87062 | -56.42058 | 2026-08-18 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eb48995-b124-3fae-8476-64531e58bf06 | -6.39384 | -54.94696 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2ecf296-39fc-377d-9fa4-bffa3628f998 | -6.67486 | -56.15899 | 2026-08-18 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a1a582d-e8ae-3d12-8a58-e6e01faa4c93 | -6.58678 | -42.23025 | 2026-08-18 04:38:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6cae7711-f1c0-3253-ab33-8e1f66b4ed74 | -8.04304 | -50.10446 | 2026-08-18 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8de0cacf-7a97-38ac-850b-2fbd6a38f6f8 | -6.30852 | -55.71068 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 691b7c7c-1558-3945-86a2-3248cb4c2011 | -6.21041 | -49.10037 | 2026-08-18 04:38:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76d61ed0-deec-38ac-89ae-635232d9a125 | -8.48473 | -48.80481 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a88ad70-8f0d-32d0-84b5-4631c2e87747 | -8.58901 | -54.72208 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 5bb0c75e-2e60-30e9-8cb7-6d27e34170b5 | -5.73634 | -43.27625 | 2026-08-18 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f426992-465e-3bf6-a10d-4c00f3284cbd | -9.42536 | -48.26287 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3efabb00-5a61-3be7-a787-1bdfc51cfa69 | -8.5638 | -54.72281 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 94813a83-20f5-3a99-bd33-f00fde4507c2 | -7.553 | -55.56553 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae8447ca-983e-3ebe-9aa7-24d40e438e28 | -9.15292 | -40.10836 | 2026-08-18 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37f54523-4104-307b-b441-da649e80986c | -7.13426 | -47.51689 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1a641fb-65d1-3890-9c9d-32861d2b0bbb | -6.9516 | -59.028 | 2026-08-18 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 30d1976c-61e1-3fad-9564-89f463718e73 | -14.1824 | -52.9089 | 2026-08-18 04:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 286.8 |
| bbda99e9-2c6b-3b92-9432-55a7a804ef4c | -6.7478 | -59.1716 | 2026-08-18 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 62f1d3e1-564a-3ca7-903c-474eb74f5739 | -14.2014 | -52.9276 | 2026-08-18 04:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| cd891272-921e-3d76-bb46-f9d42960430f | -14.8228 | -46.6419 | 2026-08-18 04:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d1d1d438-177b-3fdc-bd7c-e26f9e42f784 | -6.841 | -59.0132 | 2026-08-18 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4ae5e28f-c407-3542-99c1-64378d2a0f6d | -14.1821 | -52.93 | 2026-08-18 04:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 177.4 |
| e5daa721-a45d-3b3e-932d-fa00d3605a43 | -14.1631 | -52.9113 | 2026-08-18 04:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| fc62e0ed-f223-35d1-85c5-f0dda3a070a7 | -8.4899 | -48.821 | 2026-08-18 04:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c78c593c-6de9-3826-88bc-e476299aa8f6 | -6.748 | -59.1523 | 2026-08-18 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5ca71900-78fe-3af0-9a8b-c2c4407fd86b | -14.1828 | -52.8878 | 2026-08-18 04:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 4f0cf62e-68c8-3f48-a6b7-d2c9dc93a8d2 | -8.604 | -50.3527 | 2026-08-18 04:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 60f789cc-5a2b-3af1-96e3-2ac05a66c4ab | -8.6042 | -50.3315 | 2026-08-18 04:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 4c101f0a-49ce-3ca9-b129-08bff01475a1 | -14.1635 | -52.8902 | 2026-08-18 04:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4abd86dd-05aa-306b-bde0-67b063ec7a7e | -6.8411 | -58.9939 | 2026-08-18 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 48525ac5-6082-3f5d-a402-00cee9eb9d3a | -17.4554 | -47.86395 | 2026-08-18 04:40:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0586e3a-9b7e-37b3-8cbc-0d4793e05073 | -14.22874 | -45.41485 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e182de67-123b-304a-87b6-eae1759c0312 | -14.83731 | -46.64604 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7162835-abcd-3a2d-91ed-cf247054e52d | -11.36035 | -46.39743 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afc183ac-2a31-31ba-8346-34d29df3587d | -17.45597 | -47.86025 | 2026-08-18 04:40:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1ae16aa-d389-379e-932f-e04e8257cec9 | -14.83335 | -46.64913 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae4b2125-4888-3ef1-b0b0-f4100b058be8 | -11.54449 | -46.21836 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6551ee7a-4524-30dc-bac0-58fa9dc2903e | -14.30326 | -47.17499 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4662a70b-a1b1-3fe6-84d1-154cfd0f8fca | -15.63068 | -48.88992 | 2026-08-18 04:40:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8899a6b3-a3ef-3eda-962c-de892a4e7332 | -15.25121 | -56.48757 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 390b19c1-2c7d-317c-b145-620d712b8fa1 | -17.47743 | -48.87284 | 2026-08-18 04:40:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc4b4ab4-5502-348d-9add-e62441aab033 | -13.25069 | -51.65797 | 2026-08-18 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c9ac0e3-9715-33c3-94f0-17af29c79824 | -14.03243 | -53.68484 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5b80bef0-242f-3756-8d26-8ec632d0ff3e | -10.27279 | -50.4239 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7494a248-e77e-3f7d-9051-d9a706afd297 | -12.24629 | -45.87047 | 2026-08-18 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a98fe1e6-c168-3bbd-9683-e6b6d589e09b | -15.38736 | -52.79913 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5b6690a-46e2-3ce1-878a-04586b5ca362 | -11.33921 | -51.12496 | 2026-08-18 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88a1b09b-73a0-341f-afe5-51ea546afdf5 | -15.92905 | -55.54232 | 2026-08-18 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7b38fe9-4dbe-3a44-81fe-cd2846307d93 | -13.50508 | -46.2845 | 2026-08-18 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d709411-5f3c-3091-a27c-09ca06ee9f60 | -13.40976 | -57.0496 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0abc162a-3dd8-3d63-bf34-2e0337d2b2c8 | -8.89835 | -60.55978 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0421cf2e-c4e3-3648-a582-e4b2e9257ea6 | -11.12369 | -47.2682 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d372f17f-8002-32c1-aceb-0c99dc05c40c | -14.17651 | -52.90666 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c3431032-519c-3464-bb28-3d178910f1ff | -14.16388 | -52.90935 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 497596f8-9fc6-35da-97ef-badeda651aa5 | -10.14414 | -54.2742 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54490876-cd41-3762-9e05-f101dfee4b8c | -14.03728 | -53.68173 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6fd66d7e-1f49-3046-9b9c-e1b0a35add6e | -15.01914 | -52.70733 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bed1625f-ff16-3116-9e9e-11ce3a353195 | -14.30271 | -47.17862 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f472e327-5889-3792-a1b1-e863fd7ba454 | -11.52723 | -46.64053 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ae14d1b1-6a01-3dc0-bbeb-2a48983edf11 | -10.93661 | -57.11068 | 2026-08-18 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 92664726-9446-3341-9185-6aad3d6d99f5 | -14.26075 | -51.93353 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ffab168-9deb-3d67-89bf-ef0aa5617560 | -11.71637 | -54.62643 | 2026-08-18 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49ece082-ec9c-3e62-88c5-7f43a49678ff | -11.52666 | -46.62219 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d6ccfd9-6553-3af6-ac83-785a36650e7e | -16.30324 | -53.18783 | 2026-08-18 04:40:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae49efc-7df8-3eb1-869a-ad174937157b | -12.76428 | -48.42636 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd11703c-e57a-38ef-b4c1-501461d2d71c | -14.4988 | -45.6818 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcfe0483-31c5-3443-9361-e7efe7f87b92 | -13.58477 | -51.78264 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc424661-701b-3623-8163-0c4690dcde9b | -13.01882 | -56.58401 | 2026-08-18 04:40:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d46cc9b-df28-3397-8897-aa51f678732a | -11.12938 | -46.4931 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10f78868-ae79-311f-a0a4-11f73062052d | -11.38386 | -46.40112 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 797208ff-d0b8-373f-85d1-23973e7c210d | -17.08676 | -46.60229 | 2026-08-18 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6e7ee2d-e360-342e-8c06-e07cedb4c691 | -14.3596 | -51.92221 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8266213d-fbee-362c-96ba-dac581248b21 | -17.81437 | -50.64797 | 2026-08-18 04:40:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
