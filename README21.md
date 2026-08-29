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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd6bc5c-d7f1-30a1-ad96-487138e57142 | -5.8894 | -57.7708 | 2026-08-29 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b949e653-2286-39d0-bbc2-32444015c224 | -7.4952 | -55.3062 | 2026-08-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 974c4ce1-5fec-3f76-9f85-ca39829bee1f | -6.7884 | -55.6635 | 2026-08-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 1f84fcda-7e05-32b2-8e45-fc7859902b3e | -7.5139 | -55.2851 | 2026-08-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7696116e-9cad-3bbd-a4dc-b7026e12db35 | -7.5137 | -55.3051 | 2026-08-29 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| c16672c1-f3ed-3e4d-8380-a0ef1bf5d9a4 | -10.4794 | -64.5012 | 2026-08-29 03:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 749402b0-8cc6-3a80-bd94-e90e229074cc | -5.8895 | -57.7513 | 2026-08-29 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a91001b3-9602-3205-a1bd-7de7bf4a3974 | -11.0443 | -57.2222 | 2026-08-29 03:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 356990fa-41dc-3176-87ff-f0c6739e0553 | -3.73926 | -44.39133 | 2026-08-29 03:53:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c65e68d-8581-3a87-b515-5263191060f2 | -2.72348 | -47.04876 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d222270d-7a62-35ca-972a-8a1aa30ca0c3 | -4.16904 | -42.43497 | 2026-08-29 03:53:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a77c9c0-744f-3f47-b712-009f69365f9c | -1.59176 | -47.35883 | 2026-08-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5885624c-c5f3-3376-bb6f-6cbc6014a946 | -2.71925 | -47.04089 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a02c6ee-2110-3876-8cde-60b4827bd3ff | -2.71647 | -47.04723 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ff7df80-aff2-3a8f-a031-b0d92940a6a0 | -2.72191 | -47.04802 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b40d2d1b-4923-3b98-a951-a02fe76c9df4 | -2.71984 | -47.03736 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 002350c2-2dbc-31b4-a9a6-7b60418c6d62 | -2.49789 | -48.1341 | 2026-08-29 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4649b993-8cdc-3c69-bd1e-f8b75a1163dd | -3.95668 | -44.02708 | 2026-08-29 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eab75ef-6b34-394d-b7b8-febcd397229a | -2.71762 | -47.04013 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aea08a14-e229-312c-9251-242dd61d10f1 | -2.99696 | -48.96038 | 2026-08-29 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb50ea9f-c207-3355-b6a3-1c96bdc44730 | -5.47976 | -37.53484 | 2026-08-29 03:53:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 259175c6-5e5c-3e5e-b01c-56b5036945bd | -2.71865 | -47.04442 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78edd12d-e8ca-35cc-bb6d-f06f7951bbb0 | -3.66528 | -43.39312 | 2026-08-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17d123b4-12ac-354a-9f56-fcf645b9290a | -2.72289 | -47.05227 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d214ea9b-f5b1-3c6b-8628-6418c9b52837 | -2.7223 | -47.05576 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99d64a16-c2da-3688-8d09-6d42e65a511d | -2.98552 | -48.95367 | 2026-08-29 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c1756dc-ec78-3924-85ca-3b95ad9cb1ab | -1.03696 | -47.55565 | 2026-08-29 03:53:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 656a16d5-870e-33de-bcee-472b30a28199 | -1.20587 | -47.76219 | 2026-08-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bff71796-27ee-3c66-a689-db1d01978211 | -4.64312 | -42.43699 | 2026-08-29 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db05079f-b12c-332e-a360-7083cf910892 | -2.72077 | -47.05506 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ed051e7-f95b-3715-8ba0-b92ecaf0ef81 | -2.50376 | -48.13493 | 2026-08-29 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2de41a9-f747-3da8-8403-52915fb9b76c | -3.69977 | -39.58895 | 2026-08-29 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 22ef925b-c8a5-3fe9-aa96-3547d66fba5a | -1.59548 | -47.35562 | 2026-08-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b72d6eb1-d74f-3d2a-aa32-6cb8076717f8 | -2.99164 | -48.95469 | 2026-08-29 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7a5b6e03-81c2-3aad-9c6e-7af64bb7b1f9 | -3.18472 | -48.02005 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3900126c-8815-30ed-b5ed-6b28119e045c | -2.71704 | -47.04367 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a763079-44fb-3b4b-b73d-4c06c1d077b5 | -1.59236 | -47.35505 | 2026-08-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fff17f5-5969-3ad0-bddd-add94bc8fc19 | -2.72527 | -47.03823 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6aefd73f-2f0d-38ad-8a9d-f3576e062b71 | -3.18407 | -48.02399 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a12b044-a5de-36e6-8c9f-447376200b78 | -4.17214 | -42.44046 | 2026-08-29 03:53:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d56c7e06-75c9-3326-9dbc-9f35c289c197 | -1.59486 | -47.35933 | 2026-08-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcba24dc-2f69-328a-a135-203b1fb5db27 | -3.7187 | -45.25492 | 2026-08-29 03:53:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 436b607b-d27f-3873-9f01-192f5ea4aff2 | -2.72134 | -47.05155 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2de02d1e-38bc-3fe5-806f-046fd54be6ec | -2.72305 | -47.04097 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71696300-0d06-3267-ae67-177cc24bfd96 | -3.97303 | -41.51655 | 2026-08-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4055d83-3df6-315a-8e3d-392fc9990738 | -3.69579 | -39.59212 | 2026-08-29 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 256f6430-3670-35ae-92fd-4a392ec43083 | -2.50307 | -48.13907 | 2026-08-29 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b245e640-0b69-3c12-9ef5-07101670c004 | -2.72467 | -47.04175 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88e00af5-17a5-3049-9cac-fa735d281c57 | -2.71805 | -47.04795 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7deb8412-c3e5-3ed0-858f-b8301308b7e3 | -3.35555 | -44.22757 | 2026-08-29 03:53:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c09518b8-a197-366d-8759-7effce60f790 | -2.71819 | -47.03658 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 435b331c-2abe-32d8-ac1d-893752d3d70b | -3.69919 | -39.59263 | 2026-08-29 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5ef777ad-14e1-3d03-a235-9aad87a543b4 | -5.47644 | -37.53433 | 2026-08-29 03:53:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2206827f-27d0-3828-8b2d-7a29622dff62 | -2.72408 | -47.04527 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00042a0d-af21-3984-9e19-a393cf48f801 | -4.16825 | -42.43985 | 2026-08-29 03:53:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| deb6f8e9-fffd-3b4b-a1a8-0bf9fd00882b | -2.72093 | -48.80142 | 2026-08-29 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfb22add-891d-3e03-882a-589b3ff7ba18 | -3.59925 | -43.00836 | 2026-08-29 03:53:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807ddc5b-76c2-3050-a9d8-7bb251386af5 | -3.70091 | -39.58171 | 2026-08-29 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c91c9f14-3f8f-329f-bb3b-69e0ed3be627 | -4.64698 | -42.4376 | 2026-08-29 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bb14c61c-5a59-31d4-bc7d-8e8e2a64b775 | -2.72362 | -47.03745 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d33659c-ef14-3f06-b6f2-de22d1d25125 | -2.72248 | -47.04451 | 2026-08-29 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c3af351-e32e-34bb-8726-5a3fa973cad5 | -3.97232 | -41.52094 | 2026-08-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 68be9223-71d9-3f9a-856c-63c830e82988 | -10.90838 | -46.61227 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ab71213-d1ab-3ba4-9bfe-9acb2997e94d | -6.75842 | -46.13799 | 2026-08-29 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0c409ed-efbc-3ad5-aba9-c6c2a948933a | -11.02635 | -49.68001 | 2026-08-29 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5e45fbe-33a6-33ef-b80f-d5c7bae6237b | -11.4839 | -46.93276 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf337169-5d5c-3917-bd27-6f30c7b7c68d | -7.05619 | -42.18898 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26cf5000-b653-349b-8885-3add2982a531 | -11.62041 | -46.72564 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08784c8d-3bb1-3027-a0f5-627838d3900b | -10.89837 | -46.61681 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 34372d9e-0023-3a65-914d-907201ad9bbd | -6.40502 | -51.67545 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 632049e6-8a21-3d35-bc05-4c3165879aad | -5.60346 | -44.03678 | 2026-08-29 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 739c23da-bb0f-3eed-bfc7-54bffb2e0587 | -10.07322 | -36.26794 | 2026-08-29 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b889eb7-0274-3610-8d18-646a91b95c78 | -6.41198 | -51.67595 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb515528-bd76-3b54-8df3-cb6548ce5d6d | -8.79906 | -50.49533 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63199525-b18c-345c-b3f0-f696d40e2c04 | -11.49051 | -45.09965 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 069de948-3f05-32b4-9a68-3e85fa697543 | -11.37092 | -45.13691 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb2dd6af-24d0-3224-a069-ba3747394680 | -11.36409 | -45.15178 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37525f7e-1842-32f6-b80a-36c99abc3f4b | -6.91739 | -44.95156 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6f19907-6110-372b-acf4-8c8adaf83c92 | -11.2538 | -45.06303 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfa06158-4eae-3926-a326-68754fd2e48b | -9.69231 | -46.5504 | 2026-08-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10379d31-26f8-3831-b399-fdf2cf61499b | -5.60376 | -44.03614 | 2026-08-29 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73bbeca5-492a-35e5-8c3c-cb1f8e998456 | -10.86336 | -44.8055 | 2026-08-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b062a6ea-4b74-397c-9b34-6ffb83e342d7 | -8.66178 | -49.54982 | 2026-08-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38c521fd-d65c-3103-a645-107b9b937f8b | -6.8439 | -42.86726 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5e596954-baf5-3e24-b0a9-5a0d94a466a5 | -9.46387 | -45.63544 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f03e740-fb6d-377a-afb3-008a2a7e2dd5 | -4.36858 | -47.7754 | 2026-08-29 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 310aa2f9-f649-3055-96a8-fb1f27a29e54 | -9.64787 | -48.27046 | 2026-08-29 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aabd02c3-5fbf-3546-b5ba-af74ef360264 | -12.26613 | -43.14243 | 2026-08-29 03:55:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e72f75b0-5351-3cd1-ab50-8257aa804e79 | -3.87418 | -48.04578 | 2026-08-29 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b85d0d83-aca8-353c-af55-c4215581131c | -11.37502 | -45.13785 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c2acc52-e9d1-3634-9b77-9c5fa011fae8 | -7.05691 | -42.18459 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ef75096-f472-31b2-9a46-a1c7bd87a901 | -6.49229 | -49.90373 | 2026-08-29 03:55:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0f8b264-0f3f-3bca-bf43-9e8acc71f85a | -7.07915 | -42.21053 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de3e7e04-520b-35f0-bb0a-168fba7be177 | -7.13113 | -42.77216 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f35ed8d-d0eb-39e8-a4ab-d4547a8e948e | -9.15218 | -49.96868 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dbb83c2-9ec8-35dd-8bfc-9fab3a96fbe6 | -7.0803 | -42.79991 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4899add9-d31b-3226-a9cb-9dacad17311e | -5.59924 | -44.03608 | 2026-08-29 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d41d956-2361-3406-94ce-6513d1c6c8f9 | -8.99484 | -50.79497 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8acbf0d7-9d3a-35b7-b59d-1d5b3250ff38 | -4.2846 | -48.19566 | 2026-08-29 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fb74ce07-b06b-36b2-b397-83527fb74056 | -7.60687 | -47.28467 | 2026-08-29 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README22.md)
