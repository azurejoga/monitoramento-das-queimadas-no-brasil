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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 550c2c8e-ae1c-38c3-8a21-36d436177e14 | -11.32827 | -46.02596 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4463ba5c-e370-3841-98cc-ba7a168e8389 | -6.40715 | -49.93369 | 2026-08-31 16:50:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 015ff497-873c-3292-a591-810861f05007 | -5.45422 | -42.65577 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 59e8e4a3-2831-3720-8cfa-b36e810f99d6 | -11.93427 | -45.07159 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 40f70b0d-fec9-392d-873a-3891cc145a40 | -11.71797 | -47.64312 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 83a37e63-97a0-3f71-be63-6a17ead71090 | -10.83922 | -50.64708 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f6aeafcd-1cc5-3498-ae02-e0bba7246390 | -7.71548 | -57.31611 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2fc20ee6-de4c-3e01-b827-c72a65ef415b | -9.78028 | -46.60836 | 2026-08-31 16:50:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| eaaa1e75-b3e8-3a38-89d6-5aa07c10850d | -11.5245 | -45.49559 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4a2f5458-fe6c-395e-bf15-c2c528a43c7b | -11.93915 | -45.07917 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 231a0568-4da0-3474-acd5-27d9b58cc41d | -10.11733 | -50.32004 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 243e0001-2759-3bc9-9c93-5d66d95ae8a0 | -7.09753 | -45.79874 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 07ca3f68-bf66-318b-8b0d-2c8a0b382a75 | -8.08828 | -45.48217 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cd04f93d-2f4e-3a62-93c9-665cb944c68c | -5.41322 | -42.89368 | 2026-08-31 16:50:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| e177a497-feea-31bd-8724-f855f56c9128 | -8.3764 | -45.76106 | 2026-08-31 16:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8ee81223-4cf8-33f0-85f4-0cf5337654fa | -7.60574 | -44.99945 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00834ed6-acc4-3a55-8d40-24dfedc826d1 | -12.09897 | -47.1425 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6b38c9ad-0769-3a77-a7c4-156b6dcc0e71 | -11.089 | -51.5361 | 2026-08-31 16:50:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 13ba41bb-9b3b-3537-a870-63803ba5851b | -11.19826 | -46.11242 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 03921fad-86a7-3e67-92cf-481c1601cf6b | -12.9006 | -45.83807 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 91ea8661-83cf-3ad4-bd09-40fc2bbbace5 | -8.92689 | -45.04065 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c7a3704a-3540-38d4-a1e6-004c18621dc5 | -12.09956 | -44.99423 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ecaaf93a-a877-34ba-be7a-ce2bbea8fab3 | -8.88218 | -46.02631 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 06fde2c7-bc02-3922-89c7-e6c271c5e379 | -11.24427 | -51.26179 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d0c078bb-b77a-3a6f-a50f-ca5bb83b24ed | -9.48005 | -57.01822 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 384e1d77-dcd8-354e-8fb5-f907922fc70d | -11.22672 | -45.15257 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cda43b4d-ae82-3a0b-8b63-28f56026ba46 | -9.60937 | -47.61592 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35a597d7-43a1-34ae-8554-dfc3eb2a8938 | -10.46484 | -46.54993 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c4e1c6a8-8aa5-341b-8350-6281f545b4ff | -8.38316 | -44.98857 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 30d84be0-4062-3234-95bb-0ec3fe29ebc9 | -12.14013 | -47.23371 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3cff6c3f-51de-3449-b63d-c73c3da6b71b | -12.09867 | -45.01134 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 257.0 |
| a6cda89c-1ef4-3488-9c7f-7048e8bdbfc9 | -11.04409 | -49.67708 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 615c4c48-f467-33be-9ce2-a777a3c633ee | -7.74839 | -62.31094 | 2026-08-31 16:50:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a05eca88-220d-3447-90a3-769a20206dd4 | -6.84388 | -41.6883 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 4b0661e3-62c7-3a99-b178-093ed0451839 | -9.43228 | -37.82875 | 2026-08-31 16:50:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e9e943c8-37e5-3345-849a-87e14a86206f | -5.57784 | -42.32857 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 81996447-5263-3f05-acf1-8f72b41a9db3 | -5.17714 | -42.88574 | 2026-08-31 16:50:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c32e7dae-55e3-39f9-8004-41e06d620ce5 | -7.04514 | -55.46624 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bc5da933-2586-3f80-9ab7-eb90a062bf29 | -10.10429 | -50.30269 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9565642f-496e-3e25-843d-e3bcff4b7f14 | -8.04027 | -61.73288 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 79949265-6acb-38b4-9bda-96a369df692d | -11.35262 | -45.23712 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| ad24f3c9-e5a5-3148-9dfc-7bba6c021630 | -11.85235 | -46.76165 | 2026-08-31 16:50:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82d4b4bf-4b81-374c-9ef3-c707b6da3185 | -10.98934 | -49.68163 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8c181df8-cfce-3003-9a99-cbdaee0daaae | -7.98835 | -44.33373 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2e675c18-1122-3305-85b5-76fbd9264539 | -11.19453 | -46.11005 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 6ae07a4d-0234-3216-ba06-151fdd6588f7 | -10.96567 | -48.40526 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 6d8fdb44-929c-35d6-a005-b5ff5591118d | -8.87057 | -47.08335 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d9625827-af6e-39e3-86c1-d0bcac78ae01 | -7.92751 | -44.99813 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 157a7506-77a5-3c67-b291-56c7db2fc53b | -6.93615 | -42.71862 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| adde2bae-ab88-3be2-acf7-6af169248428 | -9.15855 | -59.5295 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 1d113e62-cfd4-32d9-9d09-c60c0addcb2d | -7.48612 | -55.28631 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e0230b2d-faf1-322e-97bc-0745c51d3b2d | -9.79896 | -60.16153 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 50efb0a2-6322-31db-8ece-2e0e5134453c | -5.80087 | -43.64538 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2857867d-9645-34e4-b5fc-74a97e2b3c5e | -9.60066 | -45.40414 | 2026-08-31 16:50:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ffa72f4-98d3-367b-92e2-2c62e2707c4c | -11.21486 | -45.32537 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6faf644b-0e6c-3e7c-b38b-589b1a5417a5 | -6.3992 | -45.43178 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a401dbc1-d4b5-3d0a-811a-c02eb1c9f646 | -7.41876 | -44.24522 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 65c77872-eaea-3364-9d68-35ada8d1ae63 | -6.67929 | -52.85044 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c17ca837-0bc4-3591-8c4f-4d94e7072b28 | -6.75957 | -52.91916 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 914d4412-124c-34fe-9607-26639cd44821 | -11.71358 | -47.63661 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2e7e6e18-03a8-3abc-a4db-7deaf883384b | -10.85639 | -45.32585 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 13f067d5-4b7e-372a-9924-e4b5319f8ab5 | -11.78692 | -47.6715 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 467c7ef1-4185-3eeb-8e47-cd08e52f1f00 | -9.65833 | -46.05778 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9531d0c2-607d-3c6f-9d69-94d278d10907 | -13.46339 | -51.40466 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3fb455de-29b5-337b-9331-34f58f09c954 | -13.46402 | -51.40926 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c6db2899-3331-36b8-ab28-9e3373028f8e | -12.0967 | -44.99912 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 8fdc6c16-c543-3a50-b4e1-fd74e9f4643b | -14.01233 | -54.08105 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ac8b07ee-b87c-38d0-a15c-1b87b54b4dfd | -11.70649 | -47.61253 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 05dcd4e2-77f1-3272-9442-2b51eb5aaa86 | -10.45115 | -46.52935 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 69e15de4-6bb6-3fd1-9536-336371bffd51 | -9.20633 | -51.56672 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9cade8b2-c020-323f-805e-9ec1e99a0238 | -8.9173 | -44.16965 | 2026-08-31 16:50:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f4dbf85d-d68b-3751-a749-f810d81b03d7 | -5.18753 | -42.8932 | 2026-08-31 16:50:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 506ee747-ee73-3cd9-9263-c86c45586089 | -11.24896 | -45.13209 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eabe1e46-55c2-3625-98a8-4a54d828c9fa | -8.96975 | -62.39462 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 38491024-af52-3b1d-9c7d-427bf865cab9 | -12.1083 | -45.02592 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fc1e67b1-1463-3928-9e91-19468a2df84b | -5.48179 | -44.1013 | 2026-08-31 16:50:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b6350754-c2e1-36a9-a365-3fff0d0ebe2b | -8.76465 | -46.46154 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| effd7da6-6ea3-3302-9423-43033d1d2b40 | -10.93215 | -40.08329 | 2026-08-31 16:50:00 | NOAA-20 | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 68b29ea0-0ea1-339e-b827-2d8919feeed1 | -8.90305 | -57.25852 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 936df4c6-36b1-31f3-b2e1-a470c8905d64 | -10.39098 | -48.23985 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 5cf4d573-7765-3b20-9404-38c5e3d81126 | -11.21579 | -46.09048 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0eb3860b-33f6-346a-a3e0-535ef1e550d9 | -10.35273 | -49.97068 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ae6e4038-22a5-3beb-9953-b87731686a26 | -11.62721 | -49.40737 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 204c7486-e675-395b-8c8c-8e924641d0d8 | -11.91525 | -45.04452 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d481c897-9fd1-32be-b24e-fb91cca7bf66 | -11.32196 | -45.20481 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 55a61b17-624e-369a-a9b4-880cb19fcef8 | -7.10047 | -45.79393 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 6a2d2620-99dd-3590-bb8c-c11c1fd4714b | -11.21318 | -45.09163 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 48914ba3-77fd-3a07-9f4c-07d3cac104a2 | -14.12087 | -52.80704 | 2026-08-31 16:50:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 68dd2efd-50f2-38af-9e9d-eee268ead652 | -10.83884 | -45.98903 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8a58bb39-792f-3fe4-8c81-142b13fa790d | -7.08695 | -42.83234 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 137cc8dd-5d5b-3957-93e2-802e2596c29d | -11.71635 | -47.63257 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 881290dd-c4d3-3fc3-bf12-73fae9adef6a | -10.1566 | -45.70192 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 606d5e44-4e69-30d9-8847-09ba5a722256 | -9.84002 | -47.8339 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 70e64568-1963-3325-9ebc-1cd05feb4e57 | -9.16286 | -59.51522 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 941ec07b-b59e-3b0b-8807-0cf187da969a | -11.67723 | -47.62077 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 169f94ce-bc62-3ee2-a931-b439cc037721 | -6.39549 | -45.43242 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6103339f-0746-3946-9db0-eaca93dc50b4 | -11.63058 | -49.40687 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| beb717f8-8a35-3c86-b913-de1f7645ecc4 | -9.60052 | -47.60288 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7656ed38-b51a-3b69-82f9-4a8bcc00cc8f | -7.52816 | -60.48184 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2983f6a5-eeef-3e1d-b77b-ab4636067f4d | -12.10452 | -45.00557 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README164.md)
