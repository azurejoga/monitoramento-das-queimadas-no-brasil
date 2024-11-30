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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10fd5e06-d6b3-3299-9ed1-623d39465514 | 0.97912 | -50.25626 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8de0d8d1-cefb-3297-a9ea-4e4c8ddcaaa6 | -1.07385 | -62.64669 | 2024-11-30 05:27:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f7e4010-5207-394a-a93b-a16399904eac | -3.09128 | -51.4085 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25343b45-6a73-393b-a34c-82edae5bb356 | -2.58442 | -53.98714 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e8e377e-0d1a-3936-9a1d-27a9081c5bf7 | -1.5002 | -54.95248 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dd6202ed-2a4d-3524-b893-2de8cfa89e56 | -3.2909 | -53.28159 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8195fc2-22e7-365e-80fd-3ea69410c8d7 | -0.95808 | -51.65907 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b29049ca-dfa1-3609-84fa-1bb07c0dba90 | -1.43236 | -55.24674 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96dde326-33c0-32b2-b56a-37efc0061874 | -0.96335 | -51.71638 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01b8254f-4370-3794-8e51-39d3ddb1ebcb | -2.37938 | -47.88137 | 2024-11-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d4b4b701-9cb1-37cf-b114-53dafec89630 | -1.77322 | -52.95141 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4a501db-261b-3cb4-babb-3174b3741996 | -3.59609 | -50.37449 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeae68c4-0769-3f45-8a4f-397d10c4228f | -2.97225 | -53.29153 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c248a9b6-eba7-3bef-a9b6-cc6fb4bffb79 | -3.3028 | -53.83564 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 67acf5c7-4f9e-3707-8cbe-d605e54d703b | -3.09704 | -50.36496 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87aeba51-0993-36da-86bc-340a037f3ec0 | -1.16379 | -53.7778 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3441250d-c735-3019-b491-4fafee525b42 | -2.58909 | -53.98785 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b87948c-8353-3e10-b379-074624383f25 | -3.3001 | -50.38013 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a0a10ca-b673-3e1f-9819-c958ea7ab281 | -3.42649 | -53.89137 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e778607-0950-3b9b-a937-59c67629eeee | -3.07085 | -50.33347 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e65e81ac-03ba-3e6f-8590-17fac75e1047 | -3.1024 | -50.37035 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be2c7885-6461-312f-968a-a8402b452e23 | 0.93538 | -50.74428 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33fd7df2-9b80-33de-86cf-05fae48c3976 | -1.07154 | -53.63429 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0da5f9b8-39f8-3c33-8036-1e25ec92b4f9 | -1.15326 | -51.69874 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e8e603e-12c3-355f-8f3b-7467ec85fbf5 | -4.1926 | -50.68509 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| effb3825-fca6-3112-bcea-1fbd98f6715a | -1.35393 | -55.64226 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c5f72a5-1953-335d-85b3-d4c7cdf79dac | -2.4434 | -53.62572 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcbe042a-f141-3817-9b87-c628219e8560 | -3.42245 | -53.88571 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f1a688c-a84c-3114-a1cf-4b946e57f96d | -1.05625 | -53.21874 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1e5fd11-7635-38cf-93fb-0f932b942944 | -1.64687 | -53.8664 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 91535247-0377-3ca8-b437-b3d8edcf6060 | -1.72148 | -52.48392 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 705522cf-6210-3daa-86c9-6e021f763562 | -1.06106 | -53.21952 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36a43dae-24ad-3958-8119-75b1baae858f | -1.26988 | -54.55433 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4818c59d-c600-3f7a-89ed-f89291f68684 | -3.0985 | -54.02409 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25314221-77c2-36ea-9cbd-a5f70b860c95 | -2.62448 | -51.77435 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00e01565-1021-3c3b-bf92-7435706ef3c5 | -2.04369 | -54.70214 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1804ab7f-830d-3f83-93f5-cca4d91641c9 | -1.15275 | -51.70213 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeb2979f-d820-38d1-8d96-a9d9dc2369c5 | -1.3155 | -51.73484 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d675a50-252d-341d-bd91-2f04efe6f0eb | -3.33477 | -53.36149 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84ec884c-b464-3d6a-8164-06037290b319 | -3.05881 | -50.33154 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e297562f-39f7-3d45-adb9-d6419fb8232a | -1.66244 | -52.40879 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 815a961a-2ad8-3545-8776-6fe073193255 | -1.62515 | -53.88394 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548c06ea-045b-3c75-9674-75ad586e80bf | -0.26583 | -51.64842 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38a6601c-ff0b-3ec6-b494-f66c75b8d295 | -2.97593 | -53.89573 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2c42c3d-e4de-320b-b8d8-eb271185d89b | -3.24945 | -50.61568 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9956ec74-da32-3148-b731-4c2efda459ac | -1.59963 | -52.2906 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34166aa2-5168-3095-95f6-0c2d445a60d7 | -2.82201 | -54.0312 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a50cd5b-9e01-3d8f-bdde-de9c7fe5549f | -1.61677 | -53.33221 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 257e2b46-c46e-3c76-be39-6441f127a157 | -1.3242 | -54.63939 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b7ccc92-63fa-3eff-a654-4f12865a5a18 | -3.52275 | -62.77064 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b29667eb-9505-3a76-b188-25994766add4 | -2.92121 | -54.26768 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97c51f03-557d-3f4d-9752-50e4fd111382 | -3.09769 | -50.3605 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe205a06-b2af-3811-ae40-41344d7225e9 | -3.25349 | -53.86909 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fbb0cc3-7a86-3f70-9672-072bfd2ddc00 | -1.45211 | -47.71158 | 2024-11-30 05:27:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b970440f-d4b2-3a2f-855a-a88855a45d69 | -3.21697 | -54.17484 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 347ad5c4-3263-3d7b-808d-b6df4eddfb4d | -0.96286 | -51.64785 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff268d5f-badf-35ff-873d-00410db4ec96 | -3.95498 | -50.1928 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4a36522-ad7b-3cd5-9230-80362db1cfa4 | -1.53955 | -55.86854 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d6e2b36-fb3e-3c2e-aa69-12abbc03ca66 | -2.92516 | -52.68832 | 2024-11-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebb696ee-077d-349e-a2d4-ea14ebfbcf83 | -3.75436 | -49.94301 | 2024-11-30 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e76b9de7-d7d4-347a-87d7-7b3b88b6fcfd | 1.10283 | -59.58669 | 2024-11-30 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 366931ec-d812-3e58-96c3-d2ac190fd96b | -2.74997 | -60.23473 | 2024-11-30 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 419ed262-0302-32b2-8da4-eb1aa8425115 | -3.25813 | -53.64062 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d49b2818-8618-3b2b-aabe-f03f7e60c662 | -3.25735 | -53.64592 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17fd19cf-4b3c-3801-87e1-59980d0c5744 | -2.41406 | -56.4374 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 44acda17-7c65-32e4-8a4b-d5a9f61b63bd | -2.2372 | -53.62851 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8f1779c-104f-37bf-b0e4-017ffe1c336b | 1.30796 | -60.41444 | 2024-11-30 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2566716b-5467-3a9f-939e-eb53275ad27e | -2.92234 | -54.26554 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e92a6e72-5a7c-3773-b639-88bd98f05d0d | -3.30419 | -50.27831 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de2d64d5-2bf7-3cf7-beb9-a78029fd9226 | -3.45744 | -54.57029 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 340d08e3-3ec5-3c11-ad53-16c11a4ffb4d | -3.3996 | -53.03288 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2921aa23-5835-34f7-a557-aa0ecc909449 | -1.83121 | -54.5309 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 016d48e7-2f71-3c24-b242-5185dafd483d | -3.09542 | -54.29736 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac067f1-b188-3d10-9499-3a01a231f2da | -1.18634 | -51.76898 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c2ba089-c56d-3a7d-8624-def1dbcff0c1 | -2.95763 | -51.69714 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bc43fe8-f9d3-3045-9b9d-b9ba42076a80 | -3.96058 | -48.09903 | 2024-11-30 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f39cba98-fa73-3be5-909b-55d2cbd16798 | -3.34409 | -50.75192 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86f23fca-34f7-3819-a542-c13af56ee418 | -1.78441 | -52.74392 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90608694-8d04-3a11-ad61-99d314f1fda0 | -1.70182 | -52.44049 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0f3baf1-09d5-375e-82d7-087020ae6384 | -1.52999 | -52.66785 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 237a184e-afe2-3aec-a4cc-e00835efc675 | 0.98193 | -50.13026 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 905657c0-2bd7-3058-8f6f-716308f844a0 | -1.44325 | -55.20464 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fdb1252-700a-3a64-8dc5-d68771eeed56 | -3.30224 | -51.06606 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6b96b2c-3e75-3104-936f-afe32073816a | -4.05568 | -49.06224 | 2024-11-30 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f471f02a-4eb2-3aa8-9166-f4942a7eb22a | -3.40437 | -50.65997 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 877e94a2-934a-33ae-8fec-5a968f964178 | -3.18916 | -54.32715 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7569d6f2-2c3d-32fc-9daa-b0bc6b74e05c | -2.9839 | -53.90022 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c556467-e121-3929-b59a-275dfd682595 | -3.21157 | -54.17898 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7c61f3ec-75eb-34e4-b597-67e7181f9e44 | -2.21685 | -53.76014 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5b868a8-da7e-3a62-b2ea-510fc0664de3 | 1.8932 | -55.71942 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e92a9077-3271-33ef-b827-61845d3be957 | -1.58393 | -53.84238 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dfb6ede-57c8-3520-bb57-00680c501f9c | -1.1634 | -53.5682 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a3ac294-b708-371b-a874-ab93bc4ed366 | -3.30164 | -51.06998 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85a4e965-4fc0-3529-908b-a9401d067791 | -1.61798 | -52.35496 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4bc8eeb-d0f0-3f4d-a8ac-98eddaae0b88 | -2.73142 | -54.1361 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e45dfee1-fb75-3630-bbf3-d3b08a978885 | -3.76269 | -50.18114 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2515060b-7e30-329a-8ac9-f5a68701a702 | -1.26092 | -54.55413 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da7cee81-eb8d-34af-b2e9-54c602887fa0 | 0.88425 | -51.98214 | 2024-11-30 05:27:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5144c772-f66e-3478-b99e-353767286284 | -2.80367 | -53.04678 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35e388b8-06e7-3cf8-a58f-62de047b253d | -3.4423 | -59.28733 | 2024-11-30 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README128.md)
