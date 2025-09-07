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
| 8d00548d-47e9-3f5b-91b7-2f0595fa16b7 | -10.3932 | -44.959 | 2025-09-07 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ab721a30-f3c3-324f-a326-cd5c6146f957 | -11.6149 | -47.1563 | 2025-09-07 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4e5a3202-4c30-3e60-8788-57877358c431 | -19.9021 | -41.4455 | 2025-09-07 00:20:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 1dcc3a8d-11ee-3969-b45b-af7ea4cde31b | -9.4309 | -62.3683 | 2025-09-07 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 138.8 |
| ca28b5cd-9e91-37ed-b7fb-6da73627f4f8 | -1.9484 | -56.5868 | 2025-09-07 00:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 21ef74b1-52d5-32d7-85be-a0d5801348d6 | -11.0596 | -54.1755 | 2025-09-07 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d8d0560b-7cce-383c-98ad-ed3adf9beff2 | -5.9901 | -44.1297 | 2025-09-07 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6002dd28-6388-37bb-a2cf-8e32dd235c0c | -6.8282 | -52.7938 | 2025-09-07 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d5777070-169b-3dec-86da-f9a16ca3a982 | -7.7404 | -48.8204 | 2025-09-07 00:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 82.8 |
| cfc703d2-f826-3385-8cde-930a9d95f73f | -6.0088 | -44.1283 | 2025-09-07 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 76837317-fdfc-3b5a-9069-798265103929 | -1.9301 | -56.587 | 2025-09-07 00:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e0a74f9e-53fa-3779-8d45-7682491c5dd1 | -7.7591 | -48.8189 | 2025-09-07 00:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c8562010-be84-3c7a-afed-52da19c321e0 | -10.3741 | -44.9615 | 2025-09-07 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 75dcdaea-aff6-3fb8-bd2c-a5d94c2e54ac | -6.8281 | -52.8143 | 2025-09-07 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f05ba80c-8687-34a6-b92d-a56aff9faaa8 | -13.781 | -52.7688 | 2025-09-07 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| fdbf4cfa-c651-35a6-84c2-d6acba5e4c9f | -15.124 | -48.0627 | 2025-09-07 00:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 4aabfe3d-d1ae-3cbd-b6b6-b9e947616273 | -10.6128 | -44.3284 | 2025-09-07 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e4777981-a4c3-3da9-8121-792b609e35c3 | -11.5958 | -47.1588 | 2025-09-07 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ead0efc9-efad-3c68-95a9-9d187c654e1b | -13.7618 | -52.7711 | 2025-09-07 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 99be5000-51dc-3c21-a725-70d5d1925419 | -15.1235 | -48.0852 | 2025-09-07 00:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ba8fa347-b0eb-388c-904e-0d8ed44d9752 | -9.4311 | -62.3493 | 2025-09-07 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 4713401e-c9c8-3361-bded-200b14cf96eb | -3.581 | -47.5149 | 2025-09-07 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| d4554d7e-f432-3ea1-8c9f-7f235bb8d492 | -17.6785 | -43.5334 | 2025-09-07 00:20:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ed3b5a2c-4b4e-30e8-8c70-80aa68cf79ce | -2.4263 | -49.3161 | 2025-09-07 00:30:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| d5b6879d-9a8e-3d22-a172-679d2f23fa30 | -9.4309 | -62.3683 | 2025-09-07 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 134.6 |
| b73637bc-7d7d-3013-be43-be392fe05546 | -1.9484 | -56.5868 | 2025-09-07 00:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 7baab516-5073-3a00-a25b-e008253a7343 | -11.4272 | -43.6254 | 2025-09-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7c7e2f7b-772b-34c3-a3c8-22a2e48ca058 | -11.408 | -43.6283 | 2025-09-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 518.6 |
| e9af8f0e-3374-334b-8787-12214f0a1243 | -11.3888 | -43.6312 | 2025-09-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 322bd2d2-b92a-3b4e-8edb-93e84dc2b5ac | -13.7618 | -52.7711 | 2025-09-07 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 3f334b6f-1e6a-3dd5-b954-68541eb48d1e | -17.2375 | -46.6921 | 2025-09-07 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 110.3 |
| d701387c-d9de-3f14-984b-5011f1863141 | -7.7591 | -48.8189 | 2025-09-07 00:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 0798bd6e-ca38-3fdf-9827-73e980a41e61 | -17.217 | -46.7194 | 2025-09-07 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8080f53d-07ea-301b-b812-a3a327e53124 | -7.7402 | -48.842 | 2025-09-07 00:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 032e1722-b37c-3d9e-b3d1-1329412d40a3 | -5.9896 | -44.1758 | 2025-09-07 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 77289b2f-ee2a-32fe-902f-728d608df8ca | -9.4495 | -62.3675 | 2025-09-07 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 7b371d36-cf5f-31ff-8447-1badca12aaaf | -22.4278 | -47.4346 | 2025-09-07 00:30:00 | GOES-19 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| f089ed94-45eb-3e30-a77b-8ee86495d009 | -9.4311 | -62.3493 | 2025-09-07 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a3d760e7-f84c-377f-b2b8-08ef28b189d7 | -11.6149 | -47.1563 | 2025-09-07 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 0163ee5e-83bf-3b1a-a97e-a168d6e98c57 | -5.9901 | -44.1297 | 2025-09-07 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f8a56521-1905-3767-affc-7e4ae06a36bb | -7.7589 | -48.8405 | 2025-09-07 00:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5081c4cc-126d-3ecf-88a1-ffb304461d91 | -3.5995 | -47.5142 | 2025-09-07 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| a6c08626-e089-3a59-9eeb-ebddec2943f0 | -3.581 | -47.5149 | 2025-09-07 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 8b0923da-1373-3385-9412-c84863e1e384 | -13.8407 | -46.2598 | 2025-09-07 00:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| da968165-ef62-3a20-a776-b792e9c30c5d | -17.3643 | -42.6284 | 2025-09-07 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 24de26a8-4f7d-331a-b7de-60df4bb5b4e6 | -11.4076 | -43.6519 | 2025-09-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 17eb0d98-6f7c-3908-9b2d-8ff6b9825211 | -10.3741 | -44.9615 | 2025-09-07 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ef8842db-75ea-3c46-b954-62102850b3f9 | -12.7832 | -52.9477 | 2025-09-07 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 3424bdc1-5ab7-384b-8bca-e6abcaa7a694 | -6.8281 | -52.8143 | 2025-09-07 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 543f814f-0ee0-3d91-b133-29607fff7190 | -5.9899 | -44.1528 | 2025-09-07 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 5b070e86-5c91-3f72-9039-7c37de20495b | -17.237 | -46.7154 | 2025-09-07 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 768d4010-57cb-3f23-a1ff-f0c749f06fa6 | -17.3636 | -42.6532 | 2025-09-07 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 16218bac-f70f-3a11-b20f-da2ffe5c2f2c | -6.0088 | -44.1283 | 2025-09-07 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 101aaa29-3144-3f79-a000-243d3859cf79 | -11.4085 | -43.6046 | 2025-09-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6f380975-544b-3807-9e58-23302bf7cd5a | -17.3844 | -42.6235 | 2025-09-07 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 512847ec-c6d0-312e-b941-b45f8bdd3e64 | -7.7404 | -48.8204 | 2025-09-07 00:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ccc6dc57-0944-3464-9838-cf298f17e287 | -6.0086 | -44.1513 | 2025-09-07 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| bab8328b-2436-30c7-b5fc-ee627a215fb4 | -13.8213 | -46.2631 | 2025-09-07 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 06a1368a-cf92-343a-8f68-2191cd290129 | -10.6128 | -44.3284 | 2025-09-07 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 29d8f53a-cf53-356c-9700-abb3ef6319c3 | -17.6785 | -43.5334 | 2025-09-07 00:30:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 0e572b16-0ab5-31a9-a96a-c274657938bb | -6.1944 | -53.2585 | 2025-09-07 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 66a58c1b-6928-31eb-9a46-1873d25d4988 | -11.5958 | -47.1588 | 2025-09-07 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 4808b71d-c01e-3ac7-9329-3377648bb0b5 | -13.8407 | -46.2598 | 2025-09-07 00:40:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 732a4f02-bd02-3daf-855d-9f12140718bc | -11.4772 | -55.563 | 2025-09-07 00:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a72f7fdc-75fe-36ed-a9da-28d45272000e | -6.8281 | -52.8143 | 2025-09-07 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d62704a5-57b7-34d8-a30e-172a285db56a | -9.4309 | -62.3683 | 2025-09-07 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 4f8efa6d-2396-3784-ac6b-624c1bf8501b | -9.4497 | -62.3485 | 2025-09-07 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2a02da1a-35ca-3f71-84e8-d7efd1128692 | -5.9901 | -44.1297 | 2025-09-07 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0abd4d37-8f72-3a48-b20e-b2f02c1a2b14 | -7.7591 | -48.8189 | 2025-09-07 00:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0bcb2024-c8a2-388b-8845-d48f94334dc0 | -11.4085 | -43.6046 | 2025-09-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 249e4d5a-35ad-3eec-9b03-0f324bc3f17b | -7.7404 | -48.8204 | 2025-09-07 00:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 798c06b9-65db-3b32-a435-49ca8dca2f93 | -10.3741 | -44.9615 | 2025-09-07 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 61d70b10-d1a3-3f60-ab3f-a9e50947ca07 | -17.3643 | -42.6284 | 2025-09-07 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 42e913da-74f6-38d3-9e1c-fb18bb1afe84 | -11.3888 | -43.6312 | 2025-09-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 50339388-f561-361a-b9d7-dec3d09f4c5b | -13.781 | -52.7688 | 2025-09-07 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 117198b2-3644-3931-b34f-d89c66821e8e | -11.4268 | -43.649 | 2025-09-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| b37c8f69-feac-3412-90af-17efc61df71c | -9.4495 | -62.3675 | 2025-09-07 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| c4a761a4-358d-3394-badc-93146a5c1ff3 | -3.5995 | -47.5142 | 2025-09-07 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| ed552dc0-46eb-3335-b091-4d8e24cb3f8b | -17.3844 | -42.6235 | 2025-09-07 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e2dc2046-4df1-3c41-a7e5-7266e7420d80 | -9.4311 | -62.3493 | 2025-09-07 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 51089c36-0474-39ca-a9b1-5e9cfec9fe4e | -17.3636 | -42.6532 | 2025-09-07 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| af76b5d5-24fe-354f-9a75-079281bd0b3a | -11.4076 | -43.6519 | 2025-09-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 0a9d6a63-0a65-32e3-b098-797a3a09c749 | -11.408 | -43.6283 | 2025-09-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 335.7 |
| eecf2c85-56a3-34e6-aa7c-b98089a2633e | -17.6785 | -43.5334 | 2025-09-07 00:40:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 9c1034ea-fdf9-3105-94b2-701b7aa4c82a | -11.2194 | -55.0178 | 2025-09-07 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 57429c94-c7e0-305b-805a-515029a269e6 | -11.4272 | -43.6254 | 2025-09-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| ed399e20-7fe1-326c-845a-c1eba16ea77b | -6.0086 | -44.1513 | 2025-09-07 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 681ca55a-3a66-3850-a82a-0ae4ad6af7ef | -5.9899 | -44.1528 | 2025-09-07 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 207.6 |
| c5364490-8658-3898-be34-594060007c4a | -1.9484 | -56.5868 | 2025-09-07 00:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| cb77a363-6569-34e9-963c-c614a5010d8d | -17.237 | -46.7154 | 2025-09-07 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 221cfce3-d04a-3869-b9e4-4b24c9fe2355 | -17.2375 | -46.6921 | 2025-09-07 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 5c271e91-320a-3795-ba84-b9058d2e810f | -3.581 | -47.5149 | 2025-09-07 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 332c3e6d-6878-338c-acf9-6758488e099b | -10.6128 | -44.3284 | 2025-09-07 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b08fe497-7e2b-3bd9-83b0-1af7c7caa135 | -16.9179 | -45.799198 | 2025-09-07 00:45:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2762c026-d050-35fe-b9a3-a6f9fc59ecbc | -7.6994 | -50.340698 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19cd5758-e138-349e-9210-d7c331c990a9 | -10.7297 | -44.3671 | 2025-09-07 00:45:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fea54678-f0f8-3678-8afe-eafc7234f6bc | -17.6702 | -43.5396 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78ee2cd9-474d-300d-8d3a-8b91a5e10d26 | -11.3886 | -43.629902 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5efac2e-9d07-340c-b4dc-0af0205375b9 | -11.4729 | -55.570202 | 2025-09-07 00:45:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b08b981-dc92-37d9-8665-39b800b35ccc | -8.1787 | -50.1371 | 2025-09-07 00:45:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
