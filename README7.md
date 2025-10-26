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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51f07d52-d3f8-31e7-ace1-571d6b7e50dd | -2.3178 | -48.5932 | 2025-10-26 03:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 1f45bb47-5e7e-3b6e-95b3-476dea579211 | -4.8933 | -43.2349 | 2025-10-26 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ea71e4d8-183c-3d6b-ba38-8e820f5938a2 | -6.4634 | -47.5498 | 2025-10-26 03:30:00 | GOES-19 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| babe0bdf-2e51-3b06-a825-eba3de1287fe | -13.5405 | -43.0077 | 2025-10-26 03:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 2767b6c6-a982-372b-a2f8-607614b74a1a | -4.8931 | -43.2582 | 2025-10-26 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cc7e7463-6d45-3b12-9ee5-a05dcc56e46b | -6.4821 | -47.5485 | 2025-10-26 03:30:00 | GOES-19 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 7ee81fdb-a0b8-3359-9053-6299a5e501c3 | -4.27198 | -40.7014 | 2025-10-26 03:38:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a6aef07-46c8-3ab5-814d-721cb6c7f364 | -4.79324 | -42.77753 | 2025-10-26 03:38:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 708be989-616c-3739-93a7-2f4385a76e34 | -4.63547 | -42.51187 | 2025-10-26 03:38:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c370aa78-9170-33b9-b6b2-6fe3d802a461 | -5.32593 | -35.9333 | 2025-10-26 03:38:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 38.9 |
| a1cd1b8f-88e8-377c-9646-86a62ed9a179 | -5.1629 | -38.08175 | 2025-10-26 03:38:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6df2866-80bd-370f-ae9a-e43b438673cd | -3.67619 | -38.66502 | 2025-10-26 03:38:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00fb0d89-627f-39f4-8681-5fecf1b60b58 | -3.78661 | -43.40911 | 2025-10-26 03:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe9111e9-b435-367e-8c1f-cdafa77816bb | -4.34492 | -38.77281 | 2025-10-26 03:38:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9bb23ff3-9292-337b-9bb2-ad2d08a8644c | -4.26783 | -40.69673 | 2025-10-26 03:38:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67a07b94-2ac0-38d8-894e-04e9643eac60 | -4.68306 | -42.7274 | 2025-10-26 03:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b73aeb2d-304c-32b8-bfb3-dc880d4b402e | -5.65242 | -35.69821 | 2025-10-26 03:38:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fcec4529-3083-3e6b-b990-7ac751e7c09a | -5.32656 | -35.92934 | 2025-10-26 03:38:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 38.9 |
| e2467e1c-4d12-337a-869f-55ef2d6a8b1a | -3.7355 | -42.30243 | 2025-10-26 03:38:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d949c14-a184-32bc-9c26-0c35763dac2e | -4.64029 | -42.5162 | 2025-10-26 03:38:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e91bbc78-827b-36c0-ab79-c371016b9fbe | -5.32529 | -35.93727 | 2025-10-26 03:38:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 47e55cdf-86f3-34bc-931d-5dfb7346bd3c | -3.7342 | -42.29874 | 2025-10-26 03:38:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 90fb1a62-5c46-3a23-9889-0d0422d959b9 | -3.78578 | -43.41166 | 2025-10-26 03:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb844203-759a-3392-babd-289e71f18758 | -4.02639 | -46.07469 | 2025-10-26 03:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ef9266c-d771-307b-b3fc-233e7285dd27 | -3.95905 | -45.42025 | 2025-10-26 03:38:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97d519e6-4f68-325d-9963-d68dd119b4d9 | -5.6518 | -35.70203 | 2025-10-26 03:38:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3f45ea1c-97d6-388a-b62d-1390ae654151 | -5.4691 | -37.85061 | 2025-10-26 03:38:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7464961d-fb31-36ab-816b-c6f9cd3107fa | -4.26861 | -40.69213 | 2025-10-26 03:38:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d8f749f-e5f2-37a1-900b-eb0f4ae91c78 | -5.0067 | -37.83939 | 2025-10-26 03:38:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59232a5d-1312-3cf2-8b88-8700ef9bfe56 | -5.32241 | -35.9327 | 2025-10-26 03:38:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fb36eac3-06da-3e0a-bf3a-1df4a85f665a | -3.44917 | -41.85167 | 2025-10-26 03:38:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 93b5cc90-5f6f-32a5-8407-a3168e06b239 | -4.81165 | -38.66945 | 2025-10-26 03:38:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ffcc3066-65d5-3c0b-b5fc-0094f576c5cf | -4.64087 | -42.51276 | 2025-10-26 03:38:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a090e72f-9df5-32a0-8048-ac90573ce989 | -4.0275 | -46.06856 | 2025-10-26 03:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a190a3bb-5eb1-3f31-bcd7-7b2754db5afd | -4.81227 | -38.66573 | 2025-10-26 03:38:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d5326449-49b0-3b3d-bdb2-ab3bf3e7e7f3 | -5.6559 | -35.69875 | 2025-10-26 03:38:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 28efb0ac-9cda-30c9-90ce-d8616b52f1b0 | -5.64894 | -35.69767 | 2025-10-26 03:38:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d778a2a6-f52e-330e-bef3-18e133766a6a | -3.73363 | -42.30218 | 2025-10-26 03:38:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8acf294-0b1c-3201-a96c-aae166133d8f | -3.96002 | -45.41478 | 2025-10-26 03:38:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12960df3-f2be-3385-b1eb-cd408090a696 | -3.60879 | -42.87843 | 2025-10-26 03:38:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14c1f297-2546-3923-a15b-5af00f62c6cc | -5.58377 | -37.28188 | 2025-10-26 03:38:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75655a05-de98-3be6-ae0e-f81b109e7ead | -4.26717 | -40.70065 | 2025-10-26 03:38:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 35ce8e15-3025-3c17-98dd-fd4c355b2e41 | -3.7361 | -42.29898 | 2025-10-26 03:38:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1be49d81-898c-3435-b8ed-654bc153aaea | -4.79757 | -42.78518 | 2025-10-26 03:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 714d3c3c-70b0-37c5-a3ee-2e3a2d41b669 | -5.32944 | -35.93391 | 2025-10-26 03:38:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 38.9 |
| 637e1836-b3fa-31f1-b809-a1565f07f7a8 | -4.03323 | -46.07573 | 2025-10-26 03:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a864707-115d-3f70-8e0b-48c33591243e | -4.03259 | -46.0761 | 2025-10-26 03:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 65007337-afdb-31fc-bce1-bc334788b611 | -5.16476 | -38.14503 | 2025-10-26 03:38:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e449c399-103a-36de-b3fc-40e07b714119 | -4.59099 | -37.73755 | 2025-10-26 03:38:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4cd94404-7c83-3187-aee3-0652eab42d85 | -4.32239 | -41.79664 | 2025-10-26 03:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d1c16b9-a7d1-3b9a-8af3-c93f51e72451 | -3.78595 | -43.41311 | 2025-10-26 03:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 048448da-64e5-3377-adfe-515bd5cce0a8 | -3.96197 | -45.41541 | 2025-10-26 03:38:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9faaf6e7-4c12-3f12-8f7a-2057342c7755 | -4.68245 | -42.73092 | 2025-10-26 03:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74faf8f9-49c2-3586-a477-e06b90398706 | -4.27264 | -40.69746 | 2025-10-26 03:38:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9d8b8f0-3fb3-32be-926e-4d8f06a24c1a | -4.32344 | -41.79047 | 2025-10-26 03:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9ce9d26-781c-3519-a4ad-67b0530697d8 | -5.00589 | -37.84434 | 2025-10-26 03:38:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fbf4f6cf-6a16-30d4-b88b-c36548845458 | -5.01694 | -37.82585 | 2025-10-26 03:38:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a677d507-6569-3d6d-a3c2-ddbbdede7d0a | -4.00243 | -41.02335 | 2025-10-26 03:38:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 089b3ca9-07c6-370a-8fbe-e0985e9c7f52 | -5.12085 | -40.74785 | 2025-10-26 03:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a64a6794-8d07-3e67-95c1-205c8dab2241 | -4.79874 | -42.77835 | 2025-10-26 03:38:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 98d3b22a-5943-33a1-9e5d-d41f6371693b | -5.32177 | -35.93668 | 2025-10-26 03:38:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 03473684-e950-34d2-8565-49b8360138fd | -4.79815 | -42.78179 | 2025-10-26 03:38:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c19a5296-781e-303e-9d9b-902c53e0fc76 | -4.32292 | -41.79355 | 2025-10-26 03:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60f1a803-b859-303c-91a9-71cb94a50759 | -5.46944 | -37.84888 | 2025-10-26 03:38:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 431887d5-d177-3f1a-b593-15f089c02cba | -3.96104 | -45.42089 | 2025-10-26 03:38:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2ccf11f-83bf-3496-9340-0706cdc45b0a | -2.3178 | -48.5717 | 2025-10-26 03:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| f0675a07-927f-3de8-8923-f4c3a0886efe | -6.7061 | -42.0517 | 2025-10-26 03:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 076d2cd1-6c06-3a50-acb2-c6fd7369790d | -12.1715 | -47.0131 | 2025-10-26 03:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 03d9d0b9-db1a-3e9d-8720-7c7ca99544fe | -5.0994 | -43.1977 | 2025-10-26 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 29b60088-b4a4-3ad5-b1b7-c3900b5ffa4d | -5.1181 | -43.1964 | 2025-10-26 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| cd3c1d40-f375-3241-bc14-5b204d745020 | -13.5405 | -43.0077 | 2025-10-26 03:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 4fe530e5-a092-386c-9ac8-57312e0804c8 | -2.3178 | -48.5932 | 2025-10-26 03:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 1a473c76-5142-34c2-a29b-648d6ec2bff2 | -4.8933 | -43.2349 | 2025-10-26 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 26d17f5b-4ccb-3167-bcab-5f654c0bbe40 | 1.6386 | -55.7258 | 2025-10-26 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 85f3cd65-16b3-3494-9a4d-f6327c36326a | -4.8931 | -43.2582 | 2025-10-26 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 3d23a0c0-4ed2-389b-8896-df8e29b6da01 | -8.07281 | -42.06158 | 2025-10-26 03:40:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3187cd7e-c05e-38d6-b46a-5f393f022078 | -5.91929 | -39.22469 | 2025-10-26 03:40:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e69e7bd1-35e1-3eb4-becd-5f4a54a7d3ef | -4.89661 | -43.25105 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cf188d77-6457-30f7-ac87-ef3a418592b3 | -6.71541 | -42.04497 | 2025-10-26 03:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dfa90090-505c-359f-b1c7-8195fbe3210c | -9.96344 | -43.86393 | 2025-10-26 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffd06fb8-9bb2-3777-bf49-87ae60f4a73b | -6.36266 | -38.37509 | 2025-10-26 03:40:00 | NPP-375D | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 016f8fbb-2955-3d15-a020-ef94c76b5439 | -6.60035 | -42.05836 | 2025-10-26 03:40:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4e5a8b76-865c-3941-90ed-f12764532a63 | -6.87299 | -41.35009 | 2025-10-26 03:40:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dcdc81f3-3cc1-3935-ab72-03848986ede5 | -5.61303 | -42.6664 | 2025-10-26 03:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fe927cb4-3d65-33e5-a874-6d13f57095c7 | -4.89097 | -43.25002 | 2025-10-26 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8f85227d-fb24-33d8-b29f-2d3702afd197 | -7.76899 | -42.92391 | 2025-10-26 03:40:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e8939b1a-46ec-34fa-b05b-e1b40beab4ec | -7.79496 | -43.16056 | 2025-10-26 03:40:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3238c64f-9692-35f4-8500-9e7891d45965 | -7.79462 | -45.39125 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74a1d463-835d-3091-a983-9b9ef6b1a575 | -9.52068 | -40.30547 | 2025-10-26 03:40:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6c9b96f3-9678-38c8-a9aa-e18f2cfb2853 | -7.76838 | -42.9273 | 2025-10-26 03:40:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 914373e9-e900-310a-8bb4-8c9a01ad3f28 | -7.77364 | -42.92825 | 2025-10-26 03:40:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 39a4e454-0592-3f41-95db-3fb0d74ca28d | -11.67989 | -43.93283 | 2025-10-26 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a5b9207-2205-308b-b760-4a95e99644b2 | -10.82992 | -47.62977 | 2025-10-26 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89dc4f1a-b177-3848-a9c7-5a92f24dc175 | -10.42606 | -44.49732 | 2025-10-26 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5af64597-a93c-3675-ac9a-6922b323ab9f | -6.15362 | -43.13265 | 2025-10-26 03:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ccfb9081-5b43-31cf-adda-ce6810541546 | -7.84066 | -46.43739 | 2025-10-26 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f30d586b-a6fe-3ad3-9afe-6fc2226a8e4c | -7.09196 | -39.57548 | 2025-10-26 03:40:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e61bc3e-603e-31d5-ac58-099c4f3562ba | -10.41379 | -45.32198 | 2025-10-26 03:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 660000b8-6656-393f-a416-726ae040a795 | -7.79984 | -45.39732 | 2025-10-26 03:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdea2230-b795-3b01-8b54-b5d850764e78 | -7.04102 | -41.651 | 2025-10-26 03:40:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README8.md)
