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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5c98455-3425-3588-8e0b-9d1a2874e0a8 | -6.94901 | -58.95519 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7d005f7-558d-34ba-98b8-c00e8683429f | -7.49965 | -55.31279 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4f73c94-a527-35be-9102-418f53d89d0a | -6.93264 | -55.69657 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc817547-1a64-36a8-a6bf-4876821e1dca | -11.03524 | -57.25068 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7ada15e-1b0e-3262-8d63-524683980433 | -9.22367 | -59.76357 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5921d095-3b43-351c-90a3-cff68e476e78 | -6.12144 | -57.6888 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d588e96d-acab-366c-b180-7ccead2f260b | -9.61346 | -55.12612 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce26120a-5d4a-35b1-b809-5c23ecffe454 | -11.29556 | -54.03616 | 2026-08-30 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d0fccdc4-79cc-3a25-8f8e-62511117e90b | -9.71024 | -60.73532 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54357672-e396-3e53-a3c9-20cb039260e3 | -6.77038 | -55.65774 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4958e26c-b214-3eb2-baff-e83d3c33b9ef | -5.87578 | -57.78247 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 0a567d73-01cf-3419-8a5b-b2397d400df0 | -9.40621 | -51.65316 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 279d3b98-fec4-310c-a50b-50a71e6d54d3 | -9.04924 | -65.41985 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9eb7cccc-908b-3957-9cc8-b24d06f5104e | -6.82849 | -59.42162 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0999ca7d-4071-3f57-8ee1-af660d750fbc | -8.95592 | -62.37403 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 404fad59-7034-336c-9507-4b11ff659f6e | -8.25053 | -62.76012 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 643bb83c-cf99-3f80-9516-951fec903ebb | -6.9344 | -58.95995 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cb0e0da-4d08-328a-bf34-529ed7d3dfde | -11.18985 | -55.11099 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af2b0499-f6cb-3e2b-8d06-78201328ec81 | -11.23768 | -54.00641 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 93f9acae-8ab3-34c9-8e57-094bf3d6bf4a | -7.59452 | -61.34766 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ab6d814-c237-30ea-9a4c-7803d2c874a9 | -7.84685 | -62.31969 | 2026-08-30 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caceddaf-b0b0-3a67-9737-95409829904f | -8.24691 | -62.75952 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67eaf797-6a4b-3936-8961-bbc04ecbb398 | -8.61364 | -54.77928 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49e4199f-b819-3fe2-8af6-ec5921dec8aa | -9.60882 | -55.13058 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68c5ee4a-4008-3a53-8553-540e89e86b69 | -5.87688 | -57.77536 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a85a622e-71d4-3d33-9955-c47e5971f28a | -6.1676 | -57.78333 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64794ae-8cc4-3fda-a107-23683b5b2e1a | -6.79175 | -55.66559 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 905bcd1a-5833-3662-acd8-5dfacbb6454a | -5.85927 | -57.55322 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fe668931-bac7-3fa7-82eb-c7a214d600d6 | -6.78955 | -55.67661 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 715a1e5d-77be-3a78-afec-6fd18b87754a | -10.99863 | -50.52291 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32164b71-c6b5-31e1-9fe4-81082d2ba398 | -7.55482 | -61.31069 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ec5edee-5c1a-3de1-b4d3-53a38fd23cda | -7.5159 | -55.33406 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3278daac-a841-3c1e-be99-d76d25c3230e | -7.40328 | -60.58718 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e984f847-5111-348a-b92e-b88b9454e7a1 | -7.57114 | -61.34008 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a09844c2-9f4c-34be-9561-f2dfad0c27f0 | -8.50317 | -55.29941 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5ec505a-0491-30ed-9752-b8fd8f34d444 | -6.95947 | -58.95327 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dbce41e-3ddd-3925-aa40-cd4ac2608063 | -11.20701 | -53.99159 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd970f3e-1d53-39f1-ab70-c55d76bad8b6 | -5.89746 | -57.75307 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2f40707-5679-3a97-af63-4f3e92a559cf | -8.93398 | -67.36843 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12d4ea59-c8f1-39ec-884b-189f74ef5505 | -11.03999 | -57.2179 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd7cd242-1b96-3c21-ade3-2001b6140e48 | -8.63331 | -66.54077 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9da8935-cee3-397a-bb3e-e0bd9410105b | -8.5998 | -70.21396 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23f276f6-a8d8-3b98-b019-87c10288cb52 | -9.89264 | -60.26725 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 004895f8-156d-35ef-8ab7-8d40892e33c3 | -7.12403 | -56.55275 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30a30384-d2d8-3b19-a90f-a663dc0ae68e | -5.47946 | -57.14023 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b84578ff-7ac1-35b8-aeba-0faf9bb3fffe | -9.76751 | -48.16444 | 2026-08-30 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3fad3ff-23c0-3313-8dac-75dafe16d012 | -11.24434 | -54.00955 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d8db693a-edf2-38ec-aa0e-1033b777b98f | -5.98555 | -55.72598 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28f7ece7-89f7-3519-b2fc-546192cf7ded | -8.23214 | -54.95166 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88bd2514-e9ba-3bd6-a092-6cd3c09d4c20 | -8.97554 | -50.80162 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 48cc630a-e0e9-39b5-89f4-11e06542526e | -8.25415 | -62.76072 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 635d04c5-8508-3111-a33b-57f4f4e6c26b | -6.49844 | -53.25641 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 225edef4-6fb2-3e46-a559-682da960c370 | -10.73364 | -54.04463 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34790e8b-e6a6-35e7-bbb7-b9f6f65ebff8 | -11.24 | -54.00899 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ab6b7c4e-60bc-3b99-8f13-b8aec11f7cd4 | -8.17104 | -55.5633 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19fb2a28-f21a-3a5e-9910-ba9af29987b5 | -9.41463 | -56.98666 | 2026-08-30 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 736f0edb-c367-37a8-8a11-5bc7c580fe18 | -5.97324 | -57.67724 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b4f340f-257f-342b-aa48-4c13854ae463 | -7.50522 | -55.32777 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2b00a78-e7a2-3b2c-9a60-ef0151130dcf | -9.41453 | -56.98598 | 2026-08-30 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b858ccd-49c1-3cd6-a787-52e36091c972 | -6.31768 | -54.74358 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 284f4f6a-cbb6-3dc4-aade-073cbf86f03b | -6.26703 | -55.42233 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44fa9bee-b8d0-3e90-8d81-bc41a6b53278 | -8.55593 | -54.78643 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 34b87b89-c85a-32fd-ac01-d54881f4a62d | -9.94093 | -60.5233 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8ca740da-0645-348c-843d-76eafbd3f49d | -6.22602 | -55.6197 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d82e92d3-9cb8-3912-81e0-8de0874d75cf | -6.76369 | -55.65224 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a39a965b-0b64-3475-bfcb-c436e78a87c3 | -6.84686 | -58.97823 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2a9a65a-292b-3aaf-b0a5-8ab509556d99 | -11.03881 | -57.25119 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8938e1da-6793-3d2e-b0b3-9a160fe480c0 | -5.48366 | -57.1404 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d7723413-1b63-3d88-898a-582385dc5752 | -6.88274 | -59.40186 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dca69985-e3c4-3570-8fad-67921cdfaa8a | -9.9107 | -60.15202 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0a51b85-d75f-334f-8f46-a2adf3c6ae2e | -9.07134 | -60.40815 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20318ac4-559d-3058-9dde-274f69dc7419 | -6.08015 | -57.8902 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be385d67-df3a-37fa-b628-0928a453b09c | -6.15912 | -53.48226 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98accd3a-25a8-3bf0-a0a4-9f56c1da4100 | -8.50463 | -55.34386 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd03ce83-f1f9-39ec-a1a7-5d9ef9627442 | -9.93595 | -60.51171 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0becfbb-dd8b-341d-a397-df35411e678c | -8.95527 | -62.37803 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 685cd2c8-37fd-3ec7-b724-da5507b04377 | -6.12286 | -53.55818 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d387bcf-46be-3b94-8a7b-cb759c393880 | -11.15802 | -51.3041 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f42e44d3-8837-3c7c-801d-c9676105c859 | -9.07544 | -64.2504 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d4c430e-8593-33c0-ab7c-3eef2a561445 | -5.87743 | -57.77179 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e647108-1aee-3361-ab6b-ddcbc9808b7c | -9.16154 | -59.50782 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f891274-82b5-36c8-8cec-7903cf5db012 | -11.16245 | -51.31121 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8fc6e7f5-ad03-315e-b691-8b6c80b9baf2 | -6.65003 | -53.1895 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c404fb18-a929-3f28-87ce-94109e557d53 | -6.1715 | -57.78027 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b978b6f-b859-38ea-9a16-72e25b8c9abc | -7.56046 | -61.31923 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 03307a77-c9e3-3bb6-a983-c584fa0eb041 | -7.30099 | -60.61144 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f0d8068-d90a-3474-9eab-a43bfa32b6e5 | -9.93098 | -60.43535 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ad5a3a-ae83-3881-bb06-edd12962d6b2 | -7.00769 | -59.64552 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 068e5d8f-e68b-3985-a662-c1733e0c424a | -8.58793 | -66.95898 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bbe15ea-f3bf-3554-8051-0e04add84b8d | -9.06255 | -65.42242 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75e2aa45-d430-319f-b202-2b818734a7ce | -6.93504 | -55.7058 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de5a50fc-1273-3814-b437-eff285e155b5 | -6.64203 | -53.18422 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a38ca2f3-c566-30cd-8fc1-0e92e9f924cb | -9.25572 | -57.524 | 2026-08-30 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25e1fb25-50e6-39f2-b8bc-a906a5e08448 | -9.241 | -60.4105 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffb21ec1-f8a2-3042-9444-32e8c6c37e9f | -6.94516 | -58.95814 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f996c2e8-3a62-3876-bc4b-d0a33127557d | -7.52236 | -55.31609 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ebf06028-b358-30c2-a644-f1ec577bcb69 | -9.8959 | -64.98753 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6f7e0d3-708d-3fed-bb51-5c72e7e98fb0 | -5.88802 | -57.76979 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b251b77d-1a66-325c-bbde-be556db729d6 | -10.75695 | -54.00182 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a404b32-ee35-33d3-aea4-fd617aa46a4a | -8.90006 | -60.56505 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README58.md)
