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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d753b621-f9e5-3986-ad83-82b6527588f2 | -3.67569 | -39.57827 | 2025-08-14 04:19:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2fff07e4-770d-3e8d-9d56-19e49e45a054 | -2.48842 | -47.57294 | 2025-08-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac4647f4-d67f-3ff5-99e3-ca66489d90a6 | -3.99271 | -43.23906 | 2025-08-14 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb84ac53-bd93-3f21-ab5d-36a78aa2bef8 | -5.16 | -39.50208 | 2025-08-14 04:19:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a7c11f9-c669-38e4-a125-28b6dcc26a89 | -4.4071 | -47.62898 | 2025-08-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de9f01c7-0550-351b-9176-c293661fcf6e | -8.73149 | -44.00794 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43085067-34cd-378f-a814-35fb56361b2b | -4.60756 | -45.6134 | 2025-08-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55e42936-47ef-3314-addf-952a4cdd16ff | -3.89644 | -41.03637 | 2025-08-14 04:19:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9686c712-de3c-3bcc-a748-3a6d32f07660 | -8.26272 | -45.05998 | 2025-08-14 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 125f4713-5326-380f-9d70-15d94c818ae6 | -7.94395 | -46.8423 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b29f7da3-ce57-3573-a2e6-97d5f424d914 | -2.36894 | -51.90546 | 2025-08-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bfa1c2ee-f294-3739-b756-6c4d80af35b9 | -6.12731 | -44.71096 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69686243-776c-3930-b696-0bc6791eff08 | -2.36665 | -51.90742 | 2025-08-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 98962fad-e0c9-3007-8093-b3a54eb85a3b | -2.91237 | -48.29922 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 13d9ab47-1414-3d27-9f37-031e67ad55b3 | -2.90537 | -48.24508 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca2d6327-ac70-3af2-b98d-d6fcd10a13f7 | -2.48911 | -47.5686 | 2025-08-14 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8f260534-b45e-340c-b8c1-9b7b8ba851e4 | -5.98741 | -44.14711 | 2025-08-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1ea35ff-bd0e-3e30-845f-b3b7b6a6648d | -8.7455 | -44.00644 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb3d3b7f-3146-39ee-b167-81a323b4d285 | -6.10772 | -44.61958 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 954a11ea-414e-3333-b5cc-321e515a2622 | -4.06528 | -47.98239 | 2025-08-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d2702af-b1d6-366d-95c7-e63d203c0342 | -8.25941 | -45.05946 | 2025-08-14 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a8c74af-0753-3de4-a0ee-e2c0ad1e26fd | -6.55322 | -44.46702 | 2025-08-14 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a414c0b-a5ca-3d46-8414-662d2b789176 | -7.93204 | -46.85162 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfa43b30-1e45-3503-8514-1281f2b4bf08 | -7.07722 | -44.94277 | 2025-08-14 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e11a2384-be75-36dd-a9d0-1aaeafe14961 | -4.22706 | -47.21568 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 63ffff02-a062-3ab6-824c-e562afd58269 | -8.74609 | -44.02497 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ce8cc16-8d7c-3bc6-b9b3-b1e94a3ad465 | -5.75994 | -46.66634 | 2025-08-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f73b9cce-8ab3-3158-899c-9c6a77b33a28 | -5.88596 | -43.92409 | 2025-08-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aa293b1-78c0-3a9e-81b2-58d8b092e79c | -3.82172 | -41.5564 | 2025-08-14 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 690c2874-cf57-3332-b1f3-0a9e778be5b7 | -7.94792 | -46.83919 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70b9d6af-e305-3c0a-ab5a-ac3868a7aed2 | -6.73207 | -44.27784 | 2025-08-14 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09f25a3f-5f49-31ef-9390-612eff190b11 | -3.88558 | -41.03461 | 2025-08-14 04:19:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8d00653-b251-389c-ab7f-c10ae1d8cf23 | -3.43603 | -49.04618 | 2025-08-14 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c07a6aac-0f5a-37ad-867c-eab1fe2102d5 | -3.43547 | -49.04963 | 2025-08-14 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 395f4ca2-1960-389d-93b9-80002f626387 | -3.67181 | -39.58025 | 2025-08-14 04:19:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1fea86da-d375-30b9-ad0f-deded60c0ce9 | -8.52021 | -43.30282 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50672d59-7085-3509-9501-dae2ee24b09a | -3.82232 | -41.55242 | 2025-08-14 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4a107b90-a221-39c1-8e52-07ecb79c29e1 | -3.99872 | -47.1492 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ba58b80-d68a-317e-a7bf-e1a12716513e | -3.43149 | -49.04899 | 2025-08-14 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 155c06ec-a665-34e4-93e5-876ec545644a | -7.95131 | -46.83975 | 2025-08-14 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d033556d-3ae1-3451-aa44-43ba86eb0a25 | -8.52194 | -43.2915 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ddc9162-8473-3e90-883e-53a7f0f25b17 | -6.94669 | -44.56075 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2685cde8-8f78-31a5-84b9-180d03929e5b | -4.22641 | -47.21968 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a70cc0cc-0e83-33f8-ba99-24ba8b7cc912 | -4.11189 | -48.72651 | 2025-08-14 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 591db31a-cffc-3fe7-9149-7d02e2bd1509 | -3.37155 | -43.36509 | 2025-08-14 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e855d87c-6411-3f1f-b67e-284a4464e7e5 | -5.89568 | -57.74352 | 2025-08-14 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fd5c40b6-ee75-3ab7-8466-d5687bb9d1f0 | -8.5202 | -43.32592 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 64df3c37-22a6-36dc-82af-3ee9388358ff | -8.73656 | -44.01977 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04229556-d819-3f17-905f-2210bfdb617d | -7.13262 | -41.84288 | 2025-08-14 04:19:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3caa9f5-f914-3a86-8b8a-78cdaacc8f6d | -6.18395 | -43.31255 | 2025-08-14 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1f5ee17-4fe4-3647-9f58-cd1ed3ee7b84 | -8.74439 | -44.01364 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5142d397-3102-37a1-af87-9990e61ff5ec | -3.81992 | -41.5683 | 2025-08-14 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c95267ef-a21a-39d9-958f-e54387442424 | -2.91301 | -48.24626 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1f686b4-705b-37c8-9ff8-94865ce3771d | -2.90471 | -48.29804 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1828da57-cfe8-36fc-84ac-ee4217d8ad05 | -8.74554 | -44.02856 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61c61f41-35df-37d8-8727-ce2e0ba6c52b | -4.60081 | -43.31125 | 2025-08-14 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13356335-52c3-3f02-a4ea-34a72169b8b9 | -5.98024 | -44.14954 | 2025-08-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2c093b3-1459-39bd-8262-caa310429df5 | -6.68278 | -46.7128 | 2025-08-14 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 065489a1-f2bd-3e3d-b887-728e622f55ed | -5.37847 | -36.84987 | 2025-08-14 04:19:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f2c4b524-6e0b-305d-955b-3d5f2f630b5e | -4.29679 | -48.06062 | 2025-08-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80a114ee-14a7-3667-a022-566788c412b2 | -6.73539 | -44.27834 | 2025-08-14 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45401c00-1d18-3c2f-87c4-e707fff576ca | -5.89367 | -57.74234 | 2025-08-14 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f6896b2-b2c3-37db-a134-b49f7fc7c492 | -6.61516 | -43.88999 | 2025-08-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6f3e138-2e70-3e99-9006-b464498cd2b6 | -5.88695 | -57.74096 | 2025-08-14 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f0d649db-78e5-3d9e-be13-74911d8eb79d | -8.74775 | -44.01417 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe66e87-9c61-3a01-8ea9-c76f407967f7 | -5.79426 | -43.61464 | 2025-08-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 17e14424-66f7-39fb-9337-3ed3ad1066a8 | -6.55216 | -44.01325 | 2025-08-14 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c1411e4-da16-3b97-980f-dec77e666617 | -7.25578 | -46.05539 | 2025-08-14 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27dfb91b-0604-35de-a004-cfdd54d92479 | -4.14451 | -38.27237 | 2025-08-14 04:19:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 10fd8a8b-eb71-306c-a194-6e593a0e8a20 | -8.25611 | -45.05894 | 2025-08-14 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 50481b5a-9697-3203-8d70-deb4c320385b | -2.91162 | -48.30392 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 059f80ab-d9ec-3cca-8956-10a1b924c137 | -5.68311 | -43.65199 | 2025-08-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3638ca2-cbdd-3382-830b-dca02379c009 | -7.06247 | -44.36147 | 2025-08-14 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b98cabda-297f-30a8-8004-798ed5f2141d | -6.94391 | -44.55675 | 2025-08-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8edaddaf-2db2-35c6-901d-43131234d584 | -5.88264 | -43.92355 | 2025-08-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79b5442d-c313-31ff-ac4a-0ef69a807f35 | -4.72582 | -38.39708 | 2025-08-14 04:19:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7f477082-4ed6-35d6-8e4a-c00b25e2b69d | -6.53449 | -56.20208 | 2025-08-14 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f82a3b53-6d02-3e1b-b6ec-e8c55f23018d | -4.06598 | -47.97805 | 2025-08-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41a205c0-6682-3cd7-857f-e4570045e585 | -2.37157 | -51.90823 | 2025-08-14 04:19:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0ac6a96d-109e-32ff-a79c-a8a2859a6949 | -4.77258 | -45.32337 | 2025-08-14 04:19:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0d055cd-7285-39ae-b34f-8a0593a6ac41 | -3.88699 | -42.55607 | 2025-08-14 04:19:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 447bafe7-142d-3766-b125-c808dc877c05 | -8.52821 | -43.31945 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e68614f1-e3c3-39ac-9572-94b231906c12 | -8.23295 | -46.24446 | 2025-08-14 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07175a13-87f3-336c-938f-7eedb7d9bfc0 | -6.55376 | -44.46355 | 2025-08-14 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f0677d-f6b3-3a2f-8405-4f6a9fbba243 | -8.74498 | -44.03217 | 2025-08-14 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f2d61db-194d-3d36-808d-2ba02da6e103 | -6.45068 | -44.55698 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20248ff2-2620-372f-8496-8b1ec8b5f723 | -6.35638 | -43.65111 | 2025-08-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 040b7c79-3d49-3e7f-bdcf-ccf3aa4b6940 | -6.99843 | -45.61965 | 2025-08-14 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 070a0592-d6a3-3842-9df2-6e2c5ee75d6d | -8.52363 | -43.32645 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ddb3a88e-7832-3b4f-8ce7-fb12b4bb5359 | -6.10147 | -44.72462 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c7d45e8-7265-3726-9672-3a586b04a7bc | -3.44001 | -49.04681 | 2025-08-14 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 166effe9-a81d-337a-a2a3-b81490a3c9ec | -6.12785 | -44.70752 | 2025-08-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5df15b8-d6ba-3634-a00e-66bfa9f6c9af | -2.90854 | -48.29864 | 2025-08-14 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cab4b0cd-12ac-336b-a180-3db0dd72e657 | -4.26077 | -46.6651 | 2025-08-14 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 385c5380-47fe-343d-9300-2853fd1bd471 | -4.22386 | -47.21606 | 2025-08-14 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c040046b-82c8-3815-a8f5-4bf210586f6b | -5.8821 | -43.92704 | 2025-08-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0079fb32-1690-3347-9822-ead9a7fec3af | -8.5242 | -43.32269 | 2025-08-14 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a4f5592-5b8a-3163-a5ad-f79139c8d671 | -4.35163 | -40.81897 | 2025-08-14 04:19:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0bdafd8-0dd5-3027-bb98-0e20327d3ca5 | -3.43205 | -49.04554 | 2025-08-14 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7b4493d-f5a5-326f-a14a-8080ad119dd9 | -3.82052 | -41.56434 | 2025-08-14 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README13.md)
