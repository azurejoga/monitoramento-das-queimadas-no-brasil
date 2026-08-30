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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0c29737-dc16-35c4-b359-4cc2191857d6 | -10.1538 | -45.6982 | 2026-08-30 16:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| d0ea2ce1-0ba9-366b-8531-c24db22f7de2 | -10.7867 | -45.3433 | 2026-08-30 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 4a92a3d9-35e9-3fd3-b95d-1ba537ce2327 | -14.4477 | -58.4709 | 2026-08-30 16:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 82135098-ae6f-3f4f-8ba4-eed6d609dc81 | -14.2989 | -51.7072 | 2026-08-30 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 41a90d56-d322-3b1d-a957-65a178075914 | -7.546 | -44.3395 | 2026-08-30 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| fbc29001-d962-3e95-a547-ce56d09dd84e | -12.3229 | -50.5892 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f0c882b7-d6ce-3437-9dc1-01ac63fa8939 | -5.871 | -57.7715 | 2026-08-30 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| c9b437d6-2f68-30a1-85da-90075f8eae9a | -11.2302 | -45.0528 | 2026-08-30 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 0abf6cec-e689-3875-a605-e705e94ab5bd | -13.41 | -51.42 | 2026-08-30 16:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f2ccf49-727d-3233-890b-686846cf1833 | -14.77 | -48.75 | 2026-08-30 16:15:00 | MSG-03 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2fe295c1-1041-3df9-8012-9b7085e317f0 | -13.41 | -51.48 | 2026-08-30 16:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51f6c65a-ac27-33a9-bdca-b0119cc9cb4e | -12.1892 | -50.6053 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6e9c506c-5c39-3e6c-bee9-19edad0ecc13 | -10.8249 | -45.3382 | 2026-08-30 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| ecf452fb-808a-30e2-a4a3-c501bfd9aabf | -12.3803 | -50.5823 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3b307717-ea9a-3733-bbda-662fddea2739 | -7.546 | -44.3395 | 2026-08-30 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 94073896-589a-344c-a8c3-baeb54a75473 | -11.1534 | -51.296 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f6dfdaaa-226f-38de-8729-da95eed27991 | -7.5644 | -49.5857 | 2026-08-30 16:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 94ac3600-8579-3c0c-ba40-837b29d96d18 | -10.9859 | -51.0807 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e0e7fefc-8a93-3b8c-bb1f-5fc28d095d79 | -10.967 | -51.0826 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 15f2c8f7-5d44-37b2-94c5-4d007298403b | -5.9636 | -57.6704 | 2026-08-30 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 5da89fb2-896d-33d3-b25b-730da37ad785 | -12.2281 | -50.5578 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d01bd3fb-9520-3f7a-bf4a-59c1c1fcdf0a | -7.9419 | -44.3001 | 2026-08-30 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 560.5 |
| 316c3856-7ede-38cb-a0f6-feaf30fc1816 | -8.4904 | -70.2392 | 2026-08-30 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 210de7c7-1ff1-30a2-9542-288613b7eac4 | -8.6487 | -62.8376 | 2026-08-30 16:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 4472bd93-50b2-3074-87f8-faec1e845bb6 | -11.2446 | -45.3267 | 2026-08-30 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| f0388932-13c3-31c8-a9dd-94dc73068231 | -14.3536 | -51.8918 | 2026-08-30 16:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| eeb38fd1-df03-303e-8981-775d6ff5fb57 | -8.9966 | -60.6109 | 2026-08-30 16:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2385d0d2-5e0f-3410-90a0-f983b0dfc141 | -8.6311 | -66.5287 | 2026-08-30 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1e1ef87d-e796-3cd7-828e-147d7dcb785f | -12.2086 | -50.5815 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 295def4d-bcd5-3892-a9ee-4ea77378010f | -8.5739 | -66.9754 | 2026-08-30 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 75ee3d3f-bca2-39a7-b36b-4b4ffdf6aca3 | -11.1726 | -51.2728 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d5c1adb8-fdf0-34af-b02e-f76ad4eaa3be | -7.9425 | -44.2538 | 2026-08-30 16:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 10d13db9-f976-300e-8bd2-a343f6823c46 | -3.2178 | -61.2362 | 2026-08-30 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e7a8d48d-248c-3b79-92a8-e65cf0ca0ea7 | -10.7644 | -50.6792 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| e287c016-5a47-34bd-82d6-2c25e6780d51 | -14.4477 | -58.4709 | 2026-08-30 16:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| a1eae741-f54c-347f-9d36-25a799b33ce0 | -6.7884 | -55.6635 | 2026-08-30 16:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 2ad80791-dbf8-37a4-9cac-bda3bf63756b | -12.3229 | -50.5892 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| fa39edb6-df11-395f-b203-0acdc9523182 | -11.1939 | -53.9993 | 2026-08-30 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 226c6ea1-0a4e-3e91-a332-caf89f002080 | -8.574 | -66.9569 | 2026-08-30 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| dc0931bc-6fae-3309-b42e-38d73d556c5c | -3.9707 | -60.0258 | 2026-08-30 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 762e6474-b7ea-3cb5-ae9e-fa80e442808a | -9.0429 | -65.4361 | 2026-08-30 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| e538d0f1-e9af-3c4a-99ee-84cfbaff76e4 | -11.1162 | -49.8923 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 5e77dd83-c98c-3fa7-930f-4272546a1f5c | -7.9907 | -46.5177 | 2026-08-30 16:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 5c49dbb6-d02e-3d5d-80ed-3211dd0667e6 | -11.1349 | -49.9117 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 78c49327-b28a-3be8-9b0c-1d679ed0f239 | -7.9611 | -44.275 | 2026-08-30 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 907a2d48-99aa-3345-8632-e79fb06b77eb | -12.3809 | -50.5393 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 3ef67314-9461-32f1-a30a-2b83a0d3d161 | -10.9595 | -50.2529 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c8891b03-149e-31a6-ab72-60987184fcda | -4.1699 | -60.6874 | 2026-08-30 16:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 9e08b075-40d7-39d8-ac36-1778e0f88adc | -13.8381 | -54.0365 | 2026-08-30 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 413946d4-83cc-344f-85e0-fb06541064d4 | -7.1312 | -42.7708 | 2026-08-30 16:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 7cef1161-9d0f-3c0c-9067-256c7e772533 | -12.3427 | -50.544 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 301.7 |
| 79ec96f7-6a21-3463-b919-5d774cb8c1a1 | -13.4191 | -51.4159 | 2026-08-30 16:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 9071276c-2301-3427-8bc4-eb18ad62c0c3 | -7.2562 | -60.6302 | 2026-08-30 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 8765afae-37ea-3271-b447-cd4506ff2224 | -15.3647 | -53.8307 | 2026-08-30 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 339.0 |
| 968f6290-f579-3dca-9fad-fbe0dedb041c | -12.3232 | -50.5678 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 88f23320-ac76-378c-966b-cbbce9d5fd9d | -6.0 | -45.0889 | 2026-08-30 16:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 692e664f-0572-30f9-a968-2e66c22a995d | -9.7374 | -67.8725 | 2026-08-30 16:20:00 | GOES-19 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dbde42e3-9acd-39e9-9a69-49530e76f7ac | -11.1634 | -50.5727 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5e5097b0-3d8f-3ffc-80b4-3f0f523e974d | -10.1348 | -45.7006 | 2026-08-30 16:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 0ce6e30f-a89b-34c1-af2b-796adbbc37b2 | -8.631 | -66.5473 | 2026-08-30 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1695e383-9679-346f-b686-957a340b0da9 | -12.2277 | -50.5792 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 250e2d15-edb3-3e63-bc54-a500a4d12643 | -8.231 | -61.4304 | 2026-08-30 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 447.6 |
| c38a541b-0ecd-3c65-acfc-664d3e4b2bd7 | -10.9935 | -50.5271 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 46b0d5a2-f49f-3bba-9fb1-62d1d8d5fab1 | -12.3424 | -50.5655 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 196.5 |
| bd60f6f3-03f3-3a72-9f4a-72fc73409ef1 | -13.4187 | -51.4372 | 2026-08-30 16:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 307.4 |
| 1840ede3-43ce-36c3-8d05-c984d74ee6cb | -3.1997 | -61.1799 | 2026-08-30 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| bad01bf7-b151-38f1-a674-0e9fed817a12 | -10.9405 | -50.255 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 5d1ad595-18a2-35b1-a5fc-e7ae94e90a99 | -11.6243 | -50.1998 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 607368f4-9237-3f65-8d37-76403bb5b406 | -12.1895 | -50.5838 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 76cc04f5-100e-310f-87a6-cef7fcc40b66 | -10.1538 | -45.6982 | 2026-08-30 16:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 4bdf2514-3c10-3093-b49c-be33717fa681 | -7.9422 | -44.277 | 2026-08-30 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 308.4 |
| 03a10e8e-6559-369f-b718-24072aa6f864 | -9.2262 | -65.8784 | 2026-08-30 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| d853bb58-279b-3d5a-b429-c78622ab4df6 | -12.209 | -50.5601 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 80b3d88f-416a-3ba6-8b46-cf498f0a7704 | -7.5272 | -44.3413 | 2026-08-30 16:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 1e3b08c4-b8af-35e9-bf60-7574568717aa | -7.1121 | -42.7963 | 2026-08-30 16:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 168.5 |
| 989b8d3e-ea95-3d46-8fcf-5ba2aaef3a4a | -6.6541 | -59.4452 | 2026-08-30 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 18431c51-6d56-3fe8-9f98-7619f98b7fbb | -9.908 | -67.0131 | 2026-08-30 16:20:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 108.2 |
| b1448425-fb88-378b-81d7-898e501d8895 | -10.8653 | -50.2203 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 406a6410-7c83-3cc4-bafb-f3d3dd9464c4 | -10.7839 | -50.6346 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4b8d0660-7162-30b4-81c6-62ca5ea627a5 | -4.0574 | -56.2865 | 2026-08-30 16:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 557f76bc-1fbf-3527-a17b-3dec0e76420a | -8.6012 | -70.2192 | 2026-08-30 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 5ecabfc8-30c6-30b5-9f2d-5aea82b08957 | -11.6396 | -50.4553 | 2026-08-30 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| da639943-1daa-3464-b941-97cb37e0a664 | -10.4794 | -64.5012 | 2026-08-30 16:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 355783b7-a905-3fe2-9d77-4a65f89a948a | -10.7647 | -50.6579 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 808b6f09-c6e1-30f2-9030-58ac4f3a7f43 | -6.77 | -55.6445 | 2026-08-30 16:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 809a5908-08d4-3ad8-bfac-2df300717aca | -10.8425 | -50.5005 | 2026-08-30 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| ffbc50d1-d69f-38aa-bd1e-33a89f47c3b0 | -8.5925 | -66.9379 | 2026-08-30 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 745c150c-1725-3c3c-b0f4-0f30e25c6144 | -11.1723 | -51.294 | 2026-08-30 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e3060734-e85d-3eb8-9073-ebc355db190d | -12.1895 | -50.5838 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b1a175fd-c240-3c00-b9ff-991398864c5f | -10.9177 | -50.5352 | 2026-08-30 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 67b984da-1496-392c-9cf1-885c5676a5eb | -11.1723 | -51.294 | 2026-08-30 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 839b23b8-2ea8-3b7e-ab9f-5f618807823d | -11.0054 | -49.6893 | 2026-08-30 16:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 1941cdd6-4049-3869-a12f-104d3a85facb | -7.8228 | -73.4067 | 2026-08-30 16:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 5522e7f7-3084-3041-aded-17bed2c6703b | -10.7647 | -50.6579 | 2026-08-30 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 5477aca1-d386-3d28-a496-359755faf476 | -10.7649 | -50.6366 | 2026-08-30 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9737c481-106b-308a-9c67-d6b821fa57e2 | -10.9559 | -50.5098 | 2026-08-30 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a8cd81a7-d637-3952-b2ce-676f97f37af5 | -11.3622 | -45.1494 | 2026-08-30 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 82845df0-433e-3e25-9a17-b51a9edd7b02 | -12.2086 | -50.5815 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 14dae9f4-71e6-3af9-b360-dd1ae8f4b7fb | -11.6586 | -50.4532 | 2026-08-30 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 62f5d8f3-9370-3405-8924-baf80bac960d | -7.9425 | -44.2538 | 2026-08-30 16:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |


[Clique aqui para ver as próximas entradas](README98.md)
