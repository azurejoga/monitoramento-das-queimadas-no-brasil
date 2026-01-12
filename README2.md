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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80e6c881-b7a2-3a66-838e-24f59e7b1ba1 | -2.87253 | -45.22508 | 2026-01-12 03:46:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0176011f-4191-3b3b-88b7-5690457ce91e | -2.87841 | -45.22262 | 2026-01-12 03:46:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16ab29ec-85de-3d45-851a-890989206796 | -3.94148 | -38.39332 | 2026-01-12 03:46:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 99e0bb58-6ed7-3524-8291-b8baa19cb594 | -4.60741 | -40.55452 | 2026-01-12 03:46:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2e29a18c-6df0-3cb0-bb1d-9029412fa8a0 | -3.94373 | -38.40134 | 2026-01-12 03:46:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7ba14662-ca96-37ac-8ff5-38a78ebfb62b | -5.9152 | -38.89998 | 2026-01-12 03:49:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc3cf566-dd28-3b7c-87ab-90fcacf40331 | -9.77248 | -36.1219 | 2026-01-12 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1e40a99e-3061-3aa0-9ada-c95bb56ad0de | -6.77505 | -38.55922 | 2026-01-12 03:49:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54a23b6c-0553-35d0-8dd8-2d0ced846a12 | -9.77421 | -36.13341 | 2026-01-12 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d29b99e5-6a1f-3a87-9c2f-c087f118bf62 | -8.65387 | -38.60589 | 2026-01-12 03:49:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6703800c-a9e1-34a7-b5db-3c7ce2ea61eb | -6.77447 | -38.56284 | 2026-01-12 03:49:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2df44db2-bf44-39e6-9ea7-dd201d600840 | -4.68777 | -41.23837 | 2026-01-12 03:49:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 63d154d7-496e-327e-a72d-e54b4ee6331d | -5.49928 | -42.15568 | 2026-01-12 03:49:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7bbd3869-e008-3476-a0d3-81c67a8ba123 | -6.5871 | -35.04314 | 2026-01-12 03:49:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 38b0cd87-eccd-3f89-8c2a-6036a4a9e5fa | -7.99337 | -43.24344 | 2026-01-12 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6028626d-e4fc-3a1d-b0ed-a020a8469a23 | -8.9683 | -38.17139 | 2026-01-12 03:49:00 | NOAA-21 | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c054b864-6d04-3c2d-a4b4-db41eb8edaa4 | -5.91864 | -38.90053 | 2026-01-12 03:49:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd3cba7e-f5d3-32d6-8adc-155b06d51f51 | -6.6483 | -37.37086 | 2026-01-12 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12ff8704-edad-384e-b6bb-cd8d5e6e25fa | -5.49515 | -42.15497 | 2026-01-12 03:49:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 34767dcd-510a-3278-81f1-3ce4351870e1 | -9.3954 | -35.85493 | 2026-01-12 03:49:00 | NOAA-21 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 11b70715-7f23-3223-98ea-66de5e4d57d9 | -7.38524 | -34.84247 | 2026-01-12 03:49:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3c9d165b-0f0a-34d2-8846-a96022d85bc5 | -5.42753 | -37.73009 | 2026-01-12 03:49:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6e3e79d-6018-3c5d-b8f8-25809066f7a3 | -8.99895 | -35.43718 | 2026-01-12 03:49:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 70522707-a68c-39fd-a74c-c4d0315fc8c1 | -6.00762 | -39.52298 | 2026-01-12 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd3257d6-de46-34dd-a9d5-d97940640f81 | -7.81031 | -36.44387 | 2026-01-12 03:49:00 | NOAA-21 | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8350f9f-dc70-3d1c-85eb-62e04e8fb174 | -10.67074 | -39.19139 | 2026-01-12 03:49:00 | NOAA-21 | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e81eb8ca-64cd-36c2-8a8a-3c5b8736c7be | -5.43087 | -37.73062 | 2026-01-12 03:49:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd6c25f3-75ee-3081-8464-027e8f9bb176 | -6.77167 | -38.55869 | 2026-01-12 03:49:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| efc5e52f-827b-373f-af3a-9461ca1db8fb | -5.65477 | -35.45138 | 2026-01-12 03:49:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69f2f86e-9c9c-31f6-9f43-411d29d0ea5d | -9.00238 | -35.4377 | 2026-01-12 03:49:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7e4ec1c8-093a-3821-89cc-09ec37430a8b | -5.49867 | -42.15939 | 2026-01-12 03:49:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f6f97e30-944b-3f8c-9e14-26f842dd16cf | -6.77109 | -38.56232 | 2026-01-12 03:49:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a797644-b733-30e2-a4fc-21a49d61c33c | -6.58425 | -35.0389 | 2026-01-12 03:49:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 465be1a6-0f13-387a-a99e-106b543f2f6b | -9.32037 | -37.31771 | 2026-01-12 03:49:00 | NOAA-21 | POÇO DAS TRINCHEIRAS | ALAGOAS | Brasil | 2707206 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 48cc9f9d-e16f-3216-896c-30465392424b | -7.81362 | -36.44439 | 2026-01-12 03:49:00 | NOAA-21 | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48158438-fe36-36e6-a21b-03ca0ba9d5fe | -7.99764 | -43.24418 | 2026-01-12 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 936b0265-2fe8-3efd-a68e-5c32d3117fad | -6.58766 | -35.03943 | 2026-01-12 03:49:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 41ce863e-2cbe-3e07-bbb8-3a9056c6d1fa | -8.99905 | -35.43743 | 2026-01-12 03:49:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b76d6514-e3b3-3d0d-a022-2cc46cc24481 | -5.49576 | -42.15125 | 2026-01-12 03:49:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ac5c2876-bee3-341f-ae03-ce4e28b73b8c | -5.49989 | -42.15196 | 2026-01-12 03:49:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 189dd3b5-2e9a-3d3f-b7ae-2c6162e5dab1 | -6.05111 | -35.2882 | 2026-01-12 03:49:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 644c3427-e2b1-3957-868b-ed2957e5e6ef | -9.77476 | -36.12975 | 2026-01-12 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 85ee5aa2-b133-38c0-96f5-76f8bf27d5d8 | -6.00698 | -39.52692 | 2026-01-12 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 896a3401-ba09-39d2-be90-0fce710bf506 | -5.65422 | -35.45494 | 2026-01-12 03:49:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8b2c90bd-8b47-366d-b381-0c5e019f5212 | -9.38057 | -36.90889 | 2026-01-12 03:49:00 | NOAA-21 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93aa5733-3894-3b66-8db2-110e2fe2ba20 | -9.10027 | -39.28045 | 2026-01-12 03:49:00 | NOAA-21 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 54250d4c-35b6-3580-ad27-d10630a84e3b | -5.5704 | -37.58004 | 2026-01-12 03:49:00 | NOAA-21 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4f242170-6941-35c3-b9bd-cab130ebf3a0 | -10.07766 | -39.42753 | 2026-01-12 03:49:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 214ec9ac-75ba-3d8c-b4d8-cf3b52f4a922 | -6.58369 | -35.0426 | 2026-01-12 03:49:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e0839f05-aaa1-3bc6-884c-d0f8a5a864ab | -6.97744 | -40.95847 | 2026-01-12 03:49:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92d92949-f1ab-357e-b456-ab6b975544e0 | -5.91653 | -39.99178 | 2026-01-12 03:49:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d9596a26-df59-3bf5-b529-de1eae815839 | -9.77869 | -36.12662 | 2026-01-12 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 460843a5-84d8-31d6-8332-955c618fc663 | -6.64775 | -37.37433 | 2026-01-12 03:49:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e049e11f-2bd9-3e28-8245-3099e1dadb24 | -14.19493 | -39.20314 | 2026-01-12 03:51:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c2d60420-5e03-349a-800b-b7269bbafa3a | -16.31348 | -45.10942 | 2026-01-12 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dfa9158-be01-3caa-b42c-5ff8df120195 | -16.31003 | -45.10461 | 2026-01-12 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 036f300c-7d8b-3cda-99e6-fce08b2fdc21 | -13.86486 | -40.62383 | 2026-01-12 03:51:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1e399351-b036-3de7-8581-2436e76cc8df | -15.51683 | -47.99241 | 2026-01-12 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd7a1e1f-9e75-32ba-8c34-d9878a1d4400 | -12.31372 | -46.92008 | 2026-01-12 03:51:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825adc3b-376f-3493-b5c6-d285dca7f54e | -12.31312 | -46.92317 | 2026-01-12 03:51:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 961c9588-68ae-3a11-ae0f-38c0c9f48f1f | -13.4297 | -43.85049 | 2026-01-12 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f09ade2-075a-3f49-bc20-25d6f22a5fd2 | -17.30177 | -42.67596 | 2026-01-12 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c0ecd9a-e661-34dd-b8c6-a3a68f73a509 | -17.87468 | -44.7191 | 2026-01-12 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63e56a4c-48e1-3f73-a622-b7e02d2fdc5d | -14.43615 | -46.24205 | 2026-01-12 03:51:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63ceebb9-f771-31fd-aedc-c6a86d0d12f1 | -15.51226 | -47.98861 | 2026-01-12 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2050eec5-5182-38d4-bb94-847d23ec85ce | -15.51167 | -47.99155 | 2026-01-12 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac380ffc-ce14-3123-a33e-c7428a05cd2d | -17.30104 | -42.68026 | 2026-01-12 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd630565-3460-3115-95a8-ad715d9f3630 | -17.27734 | -41.25233 | 2026-01-12 03:51:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a272d7c5-ec44-3bf0-89d9-9ded83735e86 | -16.31421 | -45.10544 | 2026-01-12 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6d218f2-8375-30dc-9e86-b32083babcfa | -17.29745 | -42.67963 | 2026-01-12 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc7461b8-6ebd-3f28-b7c2-bfa6bf2980e3 | -14.19106 | -39.20615 | 2026-01-12 03:51:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3836dd7e-a32b-3319-8cdc-c15e88ce730d | -11.88833 | -44.71594 | 2026-01-12 03:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c4aa73a-2079-37b2-90fd-f62bd945f6ef | -12.60069 | -46.53027 | 2026-01-12 03:51:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02facfcd-30f0-36d8-9117-87624f132752 | -13.43376 | -43.85122 | 2026-01-12 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 679a4304-efa8-3718-b95a-419fb29ffb80 | -17.31119 | -44.92902 | 2026-01-12 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5b7ed47-a630-37bd-82d0-ee5565684bfe | -17.27798 | -41.24851 | 2026-01-12 03:51:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d815c305-bd61-326b-ad49-aa4b3e5ac6cc | -15.51623 | -47.99546 | 2026-01-12 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a23b35b-4043-3ca3-89a8-32f2125d269c | -17.75736 | -43.42816 | 2026-01-12 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ba4b497-f383-3522-80d9-60ce52150bc7 | -12.60588 | -43.31532 | 2026-01-12 03:51:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 341a8452-f42c-303b-a32e-afa2e19ca789 | -15.51744 | -47.98935 | 2026-01-12 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fcc7908-7a35-3bde-ab53-27df77af723a | -18.24918 | -42.61925 | 2026-01-12 03:51:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8422c89d-75c4-3f2d-a7bb-5041c5c98e12 | -18.25273 | -42.61987 | 2026-01-12 03:51:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 01646b34-f128-38c5-a9e1-88ad7300ac48 | -22.91905 | -43.64147 | 2026-01-12 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| adb98e9b-46c5-303b-a092-97af1492bb80 | -20.40657 | -42.35633 | 2026-01-12 03:53:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a6277763-8a9c-3362-9a83-d943f171f4de | -22.56819 | -46.98503 | 2026-01-12 03:53:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0328aca-1d62-30fb-8855-ae64f249283c | -23.39126 | -47.00592 | 2026-01-12 03:53:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8b3aaa9f-439f-3953-b2d5-021e3f0383d0 | -21.46035 | -48.68502 | 2026-01-12 03:53:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 996aa540-9e5f-3eb9-aa26-80f84b7b47ea | -21.01381 | -43.98487 | 2026-01-12 03:53:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89535aef-a6b4-306b-9be7-85504ff0cc2a | -20.12169 | -46.85933 | 2026-01-12 03:53:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1617c00f-b7c9-30ee-9f2b-1cbed007f252 | -22.68194 | -45.10731 | 2026-01-12 03:53:00 | NOAA-21 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d7bf74d4-082b-35f5-aad6-1a526b5de027 | -22.19525 | -43.01233 | 2026-01-12 03:53:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 79eee377-f073-325b-bb36-d2ba0459894e | -22.64325 | -43.17497 | 2026-01-12 03:53:00 | NOAA-21 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9d79a498-9126-3645-84a0-ed3ef969f6af | -20.11815 | -46.85412 | 2026-01-12 03:53:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65241221-0672-3ab2-b381-7c9e4fe13d87 | -22.67726 | -45.11142 | 2026-01-12 03:53:00 | NOAA-21 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 185e6e74-898c-389a-b61f-a76224309681 | -23.4064 | -46.42313 | 2026-01-12 03:53:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d035432c-43f1-3cfb-bdbf-a68bd687d110 | -21.01367 | -43.98681 | 2026-01-12 03:53:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6d81dc4d-87e9-3189-9792-bafcb01a939d | -0.09108 | -51.28259 | 2026-01-12 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4997c34-8424-3b5f-a700-f5a800e4cb9d | -0.84756 | -47.57217 | 2026-01-12 04:18:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49235fb4-6c0c-31e3-8bfa-f372fd11a19e | -0.09138 | -51.27946 | 2026-01-12 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65e6e23a-c458-3610-89e7-d04e7ef6669e | -0.09084 | -51.28297 | 2026-01-12 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
