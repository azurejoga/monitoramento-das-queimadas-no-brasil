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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d2239c2-3fe0-3f7d-827a-bd7a4c92d527 | -18.30967 | -42.35409 | 2025-10-13 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4fcb795c-d0fd-3180-9c1d-63e3e54e28bc | -18.31639 | -42.25574 | 2025-10-13 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a47b12b9-6e1a-300a-a27f-7da02c9f3766 | -14.29231 | -51.54203 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec8584b5-4d00-345b-82eb-20e3f6397452 | -16.91131 | -43.95586 | 2025-10-13 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b3e48ea-40b9-3ed1-94f7-432d9c4a4317 | -21.10746 | -43.10505 | 2025-10-13 03:57:00 | NOAA-21 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ac14d99d-1f30-3cb2-958b-936d6711f045 | -14.22026 | -51.51694 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b25e27cb-4cbe-3dbd-a156-bec2b145127c | -16.1203 | -53.9836 | 2025-10-13 04:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 72b44e72-35ae-3fd1-96bf-d03d89546083 | -8.4658 | -46.1134 | 2025-10-13 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 824639bb-863b-3d64-aa0e-6f72373ec9b5 | -7.4863 | -44.621 | 2025-10-13 04:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 50cbb237-4336-30a6-be58-29746e2a2589 | -16.1207 | -53.9625 | 2025-10-13 04:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 60a5a7b1-2d28-31b3-9085-a60cd41ef030 | -8.4469 | -46.1153 | 2025-10-13 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 757381ee-38a7-3031-93bb-bcce772c9ef7 | -4.47 | -44.9392 | 2025-10-13 04:00:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8c2af567-bbef-311c-be44-6597297c249f | -7.4861 | -44.6439 | 2025-10-13 04:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 546e1239-d6b0-337d-b121-6e42a11beecc | -8.4655 | -46.1359 | 2025-10-13 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ff0864a3-10de-3b78-a296-e0ecd44a4a3c | -7.5049 | -44.6421 | 2025-10-13 04:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0edb98d1-26ce-3e40-b671-342e9097bcde | -7.5052 | -44.6192 | 2025-10-13 04:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ea6cf3a3-0a1a-339d-8762-53a735b58f1a | -4.4886 | -44.9382 | 2025-10-13 04:10:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| ae34b77b-0a94-3417-bd54-893edf2726e5 | -8.4655 | -46.1359 | 2025-10-13 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 89b39c38-c95f-37fd-b95a-69cd3b11faee | -16.1207 | -53.9625 | 2025-10-13 04:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 07782ad2-7e0c-31c6-b5e5-f88256d2c0a5 | -7.4861 | -44.6439 | 2025-10-13 04:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| fc216f29-7d42-3af6-93d0-b54d89ae2c61 | -4.47 | -44.9392 | 2025-10-13 04:10:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 50eb2de5-6973-3553-95de-633833eb4028 | -7.4863 | -44.621 | 2025-10-13 04:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 185.4 |
| b22cb5b5-112e-32c4-8d7b-bc627b7afc64 | -17.338 | -53.8135 | 2025-10-13 04:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ca3f40dc-15ed-3459-a98a-65bfc2d22aef | -8.4658 | -46.1134 | 2025-10-13 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c55e3c45-063c-30df-9638-2ab7eb2498bd | -7.4866 | -44.598 | 2025-10-13 04:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1653f1ee-d906-3ef6-b55e-a6dd424964bd | -16.1203 | -53.9836 | 2025-10-13 04:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 10a06103-148d-3199-b865-aa32387b43cd | -7.5052 | -44.6192 | 2025-10-13 04:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c8d8fb37-c69a-366c-995a-695e0b63436a | -16.1207 | -53.9625 | 2025-10-13 04:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| edc39f18-502f-3d53-8cf4-c3dc5973197c | -8.4469 | -46.1153 | 2025-10-13 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3c5bb79e-8d7a-3023-9f0d-6fb3bea031f2 | -7.4863 | -44.621 | 2025-10-13 04:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 7e55cebc-896f-3428-95a8-0acf64c08cab | -7.5052 | -44.6192 | 2025-10-13 04:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b1b69ca0-acbc-369b-9005-d0eb7e09f059 | -10.8093 | -43.9744 | 2025-10-13 04:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| aba2793d-2d5b-30c0-a83e-5f679788d61b | -4.47 | -44.9392 | 2025-10-13 04:20:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b66f3fab-01b7-366a-87a8-9535b8705d46 | -5.45562 | -43.39516 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f454c15-2b6b-33eb-9b4b-78039693e7e8 | -5.7433 | -40.76845 | 2025-10-13 04:21:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f81b0a0-8808-378a-a59f-1379505189e0 | -4.48442 | -44.93512 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b1679af-b3ca-3319-83f6-8c50a969051c | -4.28252 | -48.57297 | 2025-10-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9100e1d5-8c08-3956-a0a9-be87a5314b58 | -3.24607 | -50.81537 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72a46729-6d84-38ad-89af-052d4776f242 | -2.534 | -47.80764 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9628df00-035a-32fe-84d1-b3b5b9d7477a | -5.45617 | -43.39161 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc4ed00a-05c5-30d3-84a7-0b5cd37b5e4e | -5.93677 | -43.94324 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 490f1dc5-7233-3aac-b919-8d702ab076cd | -5.31953 | -43.43952 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d915edb6-81d1-3b90-9ab3-b4dd710fb5b7 | -2.91008 | -49.17476 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce326393-f55d-3127-87f1-dea8f42d92a9 | -5.13158 | -42.87835 | 2025-10-13 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47487dc8-2fc3-3a56-81f8-5b3b8651f5f0 | -5.57465 | -45.27594 | 2025-10-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e897103-661b-3c05-b6f5-8cf2f5a50ab8 | -2.87995 | -50.73581 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b0edd87c-372c-3ce1-891b-17192d84f5a8 | -4.66481 | -45.70179 | 2025-10-13 04:21:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb68f16f-92d1-3624-b119-4bc010a1d4ba | -5.83687 | -44.06365 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82052f18-1fdf-31a6-8f3c-2bba77144dab | -5.06778 | -40.46975 | 2025-10-13 04:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a463e03-0a00-35bc-a08a-39b935ba2035 | -4.47598 | -44.93029 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 49dc0b4b-c807-39f8-9b25-a30214425f85 | -5.48271 | -44.66241 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c467c0b-d7e1-3963-b09f-170bbe712ba7 | -6.32764 | -42.77154 | 2025-10-13 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd79b215-bea4-31fc-9ec8-c516fbedcd3b | -4.83396 | -41.48199 | 2025-10-13 04:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4345c8bd-2017-3ae1-a207-d3895c678d88 | -3.72511 | -44.392 | 2025-10-13 04:21:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55ddcf34-a11c-3e9b-8288-5a96a7e0b77a | -5.31125 | -44.24776 | 2025-10-13 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 463065ed-c031-3b9a-bbb5-d6172b87a1e9 | -5.34974 | -43.42247 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3aec4b65-a69c-3c02-baac-d51c879229e4 | -5.62007 | -42.81014 | 2025-10-13 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9bbb4bee-e5e2-389c-9d1c-5ff9b254d2be | -3.72292 | -44.40584 | 2025-10-13 04:21:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 065927e9-3207-395e-b95e-0f0e03853151 | -3.61168 | -48.91518 | 2025-10-13 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb98a97d-26aa-386b-82db-96b74081e873 | -3.92148 | -50.01702 | 2025-10-13 04:21:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c24b18d2-62b2-3e35-9d2e-b307cd064942 | -3.21863 | -50.22054 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adee3a31-c100-3398-b81f-2bfb194831fb | -2.45931 | -49.0322 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd6bbb8c-a245-3853-b05d-7c79ef6601a6 | -3.06673 | -49.4113 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5155eee-cfa4-339a-896e-21a834f20f47 | -4.83037 | -41.48147 | 2025-10-13 04:21:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84c4f461-1521-3db1-a476-4dd6bca87833 | -5.57131 | -45.27541 | 2025-10-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e977b97f-7d4e-3880-9050-3939c069e53d | -3.87271 | -44.12084 | 2025-10-13 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8637cd48-96ba-325d-a0dd-96e5f90e5afa | -6.40411 | -41.9514 | 2025-10-13 04:21:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3ea3b25e-c2c2-3358-82c1-547b6462b191 | -5.91401 | -45.43372 | 2025-10-13 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eecae7a-140b-3003-85b1-419014927976 | -5.73757 | -43.83295 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95afa36a-6ad5-3483-a754-39de50b46a79 | -5.47993 | -44.65842 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85f6ef75-a372-3185-b199-710f15897ad7 | -3.41201 | -51.22932 | 2025-10-13 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f8b1ce7-b6da-3dfe-ad19-7370c6730eff | -2.52717 | -47.80182 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| dc8ad423-dd8d-38d1-80b9-9ccda0f77350 | -2.26501 | -47.85133 | 2025-10-13 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 541640d2-8c32-3389-83fa-ee301a3b9e13 | -5.93335 | -40.88719 | 2025-10-13 04:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ab1d69b0-0da7-364b-882d-32c9f250e19b | -3.44832 | -40.40675 | 2025-10-13 04:21:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8413f99e-6ce0-39a0-99f6-719e2d9f077a | -5.46738 | -43.38607 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d6f9fa4-e9ce-38d4-9a3a-76e75cf56650 | -5.24898 | -45.5931 | 2025-10-13 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 741b0586-c168-33d7-8f84-579ac989be4a | -6.17056 | -42.54036 | 2025-10-13 04:21:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 54c05999-41ef-3ebb-b181-7deee6ae582f | -6.40829 | -41.94789 | 2025-10-13 04:21:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fbc36504-6e36-39f3-9678-4eff5b950f44 | -5.91458 | -45.43021 | 2025-10-13 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71ea7302-a728-3680-8924-a84d849f62d3 | -3.42059 | -44.30532 | 2025-10-13 04:21:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a2691f8-f57c-3b1b-a382-b2b463130a18 | -3.27418 | -50.04616 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97202f0f-ce7c-3d93-8cce-1c8a92ba40ff | -4.4783 | -44.93057 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ce2d0ede-d425-33b7-ba44-84fee727d3c4 | -2.98671 | -50.29092 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7157c8c-38d6-3d87-b40d-9f9bb2271a17 | -5.1056 | -43.20295 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 01fe7aa6-dff8-3629-87d7-28634ee2ba16 | -6.21806 | -42.48549 | 2025-10-13 04:21:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d1666e5-1091-3b24-8779-01f1f3caaeb3 | -6.24215 | -43.00539 | 2025-10-13 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| e83cfdf4-73e0-3a85-93eb-c12f43db519e | -4.47997 | -44.94156 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6db5e046-03df-3146-868e-b838bd0e1e1f | -5.83747 | -42.31199 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| abbc073b-60f5-3c1a-a371-193a530dca2b | -6.22147 | -41.5622 | 2025-10-13 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 618f9691-0e3f-3303-aff2-4edcb2e3286b | -5.94121 | -43.93674 | 2025-10-13 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d47912c-b1bb-300a-898d-00689924f2c3 | -3.61364 | -48.91299 | 2025-10-13 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e151ca42-4950-35f5-9065-6497125d3417 | -4.86846 | -45.91489 | 2025-10-13 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3544cdb-c7b1-3807-9845-9901a514d242 | -6.76505 | -39.07724 | 2025-10-13 04:21:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c5bc0bab-c304-3e96-bba6-97a03758f6c9 | -3.21931 | -50.2164 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ebf5551-e727-3c8f-a58e-c506f7b57199 | -2.88479 | -50.73535 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75c80726-7b9a-3d49-8efa-e6e78103bab1 | -3.27852 | -50.04683 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ab1a5d9-6770-332c-aa20-87322e6c6d40 | -4.47542 | -44.93378 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b140f119-2361-3f2c-aada-dab2bed68fe7 | -3.09444 | -50.37278 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 944e9ad5-c471-314a-bd36-2bbc3e7b35d8 | -5.83813 | -42.44508 | 2025-10-13 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README16.md)
