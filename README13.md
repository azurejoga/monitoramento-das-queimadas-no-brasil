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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fa4676c-5bf5-3d90-a8f7-e807a0437787 | -7.11565 | -44.38264 | 2025-07-19 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0be5e84-63c8-3b64-a198-c2aaac4ca850 | -7.17714 | -44.09102 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db9850a1-30b2-3acc-bedb-fe29e6ae57ae | -7.17878 | -44.10282 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5837a742-1dd8-38e5-8c93-d66a90bd6665 | -8.30844 | -55.10976 | 2025-07-19 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| acf779b2-1e59-3b43-8a20-c65ae90dbdb7 | -3.13687 | -47.01505 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| af419daf-bb9b-3148-b72e-9df33893867e | -9.55662 | -40.59991 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4aad2a0e-840b-3a20-b830-430fa3224902 | -7.29039 | -43.88884 | 2025-07-19 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f52a3651-be5a-36d5-9ef5-2ac25622796b | -7.10169 | -49.93491 | 2025-07-19 04:08:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a157fd92-e60f-3f48-af15-983bf22ce7d1 | -3.9818 | -48.42236 | 2025-07-19 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72bad81b-ec92-3c9d-b93d-99a08469d04c | -7.49243 | -47.5043 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 924d3ed4-128e-3842-bde5-b540a7a94031 | -4.66578 | -41.95596 | 2025-07-19 04:08:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7595d7eb-6830-328c-bc6e-4cd10331b59d | -2.9108 | -48.254 | 2025-07-19 04:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 52d6afc6-b1b6-33a2-ad3f-1b5ed62d1fce | -5.6379 | -43.7175 | 2025-07-19 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 89f3b4aa-b458-3c1d-98f4-62da9538b1fc | -11.7317 | -48.1849 | 2025-07-19 04:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 33a38b47-40d2-35d4-bc0f-250713932850 | -2.9109 | -48.2325 | 2025-07-19 04:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 135cc99c-1a65-38bd-8f0d-d5db81e7222d | -5.6567 | -43.7161 | 2025-07-19 04:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1fc7e5c5-1f89-307d-83cc-bd7394d4e5eb | -18.05585 | -47.94525 | 2025-07-19 04:10:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 847911fd-44c6-3329-8dc5-f3161acdee83 | -17.55025 | -44.24821 | 2025-07-19 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a83bf2c7-c96b-3e64-b3db-37930070478a | -11.33201 | -44.85538 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dee3f55-b281-3235-8b19-70e7106abfdd | -12.97386 | -46.91932 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a7bd01b-6dac-3d0c-b806-b8889cd62bf9 | -11.36059 | -48.72742 | 2025-07-19 04:10:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df4ba578-ae21-35a7-8b39-23db6989bdf2 | -11.72917 | -48.18933 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| b24907d7-7591-368b-b946-caf8c0d03588 | -12.97577 | -46.92233 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e254b97e-1944-3151-9438-9d28922bdbf4 | -12.37188 | -50.33383 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd6fc6b1-9af1-31de-92ad-05c3d90cc6d8 | -10.81974 | -49.28574 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5245e418-0e6d-3044-885c-59179a91219b | -16.27167 | -46.29195 | 2025-07-19 04:10:00 | NOAA-21 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 245cfe3d-c9c1-324e-980b-0918640e2f45 | -17.65456 | -44.21043 | 2025-07-19 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 801df34e-1f4d-348d-a006-f551fb66d2aa | -16.37691 | -43.03974 | 2025-07-19 04:10:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2342eec2-5d86-3ab3-a0af-62a0d2269526 | -14.73516 | -40.98063 | 2025-07-19 04:10:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19d397de-a16c-3dec-a9c4-5f14db428d6d | -12.06781 | -47.35319 | 2025-07-19 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9a5580e-692f-322d-802d-a492e1d59b34 | -12.4249 | -45.36975 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cba0fbd4-e76a-30ce-8d0a-6c8c7f3ca16c | -11.95801 | -47.01905 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 43583a65-f554-31a9-a81c-579523ad3c02 | -12.03403 | -48.76056 | 2025-07-19 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03de601e-c164-39a2-99c4-0c321ee028c6 | -11.96178 | -47.01971 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6ca8062c-f63b-31be-bf00-65c8f573a12e | -12.37264 | -45.72981 | 2025-07-19 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 581d0241-2716-3930-840f-a0683768b133 | -12.03332 | -48.7645 | 2025-07-19 04:10:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c18678f7-7b32-39a7-9b07-f860f1ceaf8f | -16.77588 | -49.38128 | 2025-07-19 04:10:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed520892-e121-38a8-9946-7159736ad9cd | -12.42362 | -45.3775 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 541521f5-99c1-347e-ac38-50d9124b7279 | -16.04084 | -43.72338 | 2025-07-19 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9406859-f122-300b-ac50-de851d71c2b8 | -15.8946 | -43.4605 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| eaf8af41-78cd-3018-b019-d50cfe1e22fc | -14.71726 | -45.06632 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a12b440-d9a7-3d5e-a250-a4c77bbbd79d | -11.48289 | -47.32498 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e91edee7-d90c-3356-bc2d-a7219c13e474 | -12.96271 | -46.91775 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 622554bd-3823-3589-8d67-477c94018ce5 | -11.83068 | -48.20703 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff6813e7-e8bf-396e-9048-a6f026845f26 | -15.92402 | -43.51275 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0064ef95-4e2c-3fec-abe4-f8fa8909c058 | -14.70258 | -45.07137 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f18b1a-1123-3434-96c5-be0a511531f7 | -10.81598 | -49.28689 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17949a5e-34db-33e5-94a8-8ce380d8de85 | -10.76435 | -52.76499 | 2025-07-19 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb572ffd-404c-30ca-a910-96fb487834b1 | -11.7373 | -48.19075 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 35d349d8-3e1d-399e-8b1b-b3bc2dad7587 | -13.05234 | -49.17753 | 2025-07-19 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ce610863-7898-3767-aa82-9998b0345cc4 | -12.37616 | -45.7304 | 2025-07-19 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39225148-b721-39dd-8039-6a04868bdee0 | -10.81893 | -49.29018 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 426bfc9c-fb60-3cdb-b79f-60d6b94c03dc | -11.83345 | -48.21516 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d64903c-223b-30df-bb82-b2dc43ba0c34 | -11.48848 | -47.32346 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e66427d5-5ee1-305a-96ef-9088da3aa6b5 | -16.04471 | -43.72036 | 2025-07-19 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab1a12a1-abbc-3499-9b1b-0faa2a99add1 | -14.81227 | -41.7443 | 2025-07-19 04:10:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ad14fb7e-628b-3a45-80d1-a3271487447e | -10.57213 | -49.12653 | 2025-07-19 04:10:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2dc1cd7-48c1-3542-9ac6-60e8770aca04 | -11.47689 | -47.3214 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b47bb9e-0470-3735-957d-404a2b7e010d | -15.82682 | -45.77698 | 2025-07-19 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed747410-31c4-3281-a7a5-194fef336e19 | -13.61444 | -45.63897 | 2025-07-19 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7d5d5d3-c347-3447-bd73-734ffa1959d6 | -13.0001 | -46.93582 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a36e7bc8-4aa5-35de-a92b-849135a5fb06 | -15.99424 | -49.82362 | 2025-07-19 04:10:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56af302f-0d10-33c1-a189-97670d8d803e | -11.96099 | -47.0244 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fa7cde1f-bc3a-3214-8bcd-f7f25f547d6e | -11.96605 | -45.46657 | 2025-07-19 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0eb33021-51f0-3d7d-975e-8a6467f65789 | -12.67959 | -46.83126 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acbd626f-1e5a-3992-9453-7085154db60f | -15.7 | -48.12976 | 2025-07-19 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80b05408-f24b-3e8a-a0e6-69552359d729 | -17.55356 | -44.24878 | 2025-07-19 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1116e80f-4f64-3208-96b9-e1e6250b6b73 | -11.46678 | -48.15712 | 2025-07-19 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b1083ef-80fd-330c-a563-caf75e80d3c4 | -11.47985 | -47.31939 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9d0b332-3334-3c6f-86e7-b8972563f4d2 | -14.50178 | -43.69454 | 2025-07-19 04:10:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e97a414e-2440-3cf7-bfd5-26fece0c23a0 | -15.85481 | -43.29948 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e867458-f2c2-3072-81e3-02f64305bb02 | -14.70198 | -45.07504 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cfb197c-89c3-3536-a642-a8ebbbd82e1d | -14.74825 | -48.27369 | 2025-07-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18c87fb8-63f2-3dcc-8c13-5f4145c4e9cd | -11.52434 | -48.953 | 2025-07-19 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65a2870e-e1f1-317c-8cd6-091d579adc7b | -17.65327 | -44.45784 | 2025-07-19 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2bbf439-47f3-3743-a1cd-3729f0ad1660 | -12.03752 | -48.76522 | 2025-07-19 04:10:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 830b0d95-4f42-3747-9c22-330621696acc | -11.82874 | -48.21814 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3e4dc7d-65e6-3a6b-8ec7-b65413ec4ed3 | -13.79076 | -48.49915 | 2025-07-19 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b6c21ee-b2e8-360d-911a-8c353f492173 | -11.73793 | -48.18714 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| d42a1654-57cc-3fe5-9ce1-a08d285f4fbd | -14.70655 | -45.06826 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac04fb77-82df-3ccd-a141-04a24594632b | -11.56666 | -47.07793 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e044b83-b51e-3e0d-9e1b-283c60b8243c | -12.46409 | -46.92772 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93b96d1a-dcd1-39b4-877e-b7cbe8443a99 | -14.70715 | -45.06458 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61ab8ae0-d0f3-33dc-a187-04addb2099bc | -13.61098 | -45.63838 | 2025-07-19 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caefc60b-e5eb-34e7-b8c2-5e1a55e65ddc | -13.05306 | -49.17351 | 2025-07-19 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cc5462c4-e16e-3ab2-91b0-0e8b713f4281 | -10.67148 | -49.68232 | 2025-07-19 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f7bf125f-ef4d-3968-b0a7-d387ec9c9e14 | -11.46207 | -48.16 | 2025-07-19 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b5b92203-9852-3f9d-90b8-c3a43fdcd729 | -11.56123 | -47.08673 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c3eeb94-2ae9-3967-a3fa-a6f116d69426 | -15.89846 | -43.45747 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 326a7688-5de7-3a1a-967e-23c7e6a1bb01 | -12.96197 | -46.92216 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4c46b7f4-7771-3574-8296-05c36c1a3f80 | -11.48675 | -47.32568 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6aed824a-6258-3b79-b4e2-029a1da43949 | -14.77675 | -48.29443 | 2025-07-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25c219ec-5752-3d6a-b5c7-056f0646dc88 | -13.97028 | -42.00489 | 2025-07-19 04:10:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0812654f-5ef8-3983-b8d5-7aa2850fb82c | -12.57898 | -44.75277 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 385b76d2-e9a7-389d-a1f5-85a96e134c7d | -12.36885 | -50.33112 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 118515de-5230-37e4-a931-a1b2e8972ad6 | -11.48758 | -47.32077 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8fd4ce17-d20d-3809-9bff-ae4badf5ed17 | -14.20162 | -45.33585 | 2025-07-19 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6687bdb-5d81-369b-a7c5-1dbd9a55c264 | -12.3617 | -50.33701 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80f7c075-cdb1-346b-95f8-754a65042d23 | -14.69616 | -45.05865 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab5c7bc6-8608-3d46-8b34-50adcd9c74c4 | -11.73324 | -48.19004 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |


[Clique aqui para ver as próximas entradas](README14.md)
