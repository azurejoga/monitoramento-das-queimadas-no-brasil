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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66fdf8b4-8c5b-3a68-94b3-ae64fd398544 | -2.95021 | -41.74541 | 2025-12-01 04:04:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4613e32-8bfd-37a5-b871-6dff63b3d019 | -2.25061 | -45.61369 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 514e9727-b3cf-3d3e-9caa-fd114c6c4e43 | -4.39231 | -43.33268 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| f8c46363-2e15-394a-bb22-945472cbbda2 | -3.7135 | -45.90824 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4a9dbb68-00f6-3377-96cc-08075d222334 | -2.24541 | -45.6174 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f10e0381-937f-307f-b662-c1b9b749968d | -3.58216 | -50.27845 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca2a3da8-7ac8-3b3d-9b58-deb6201f46af | -4.3105 | -45.37386 | 2025-12-01 04:04:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f9ac293-373c-3f5d-a56f-7cb7408ae75e | -5.75444 | -40.81646 | 2025-12-01 04:04:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 015d220b-c10b-33b1-8abd-4ae56c6f2135 | -2.60238 | -49.26474 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73a8a440-b26d-3537-8e7b-c958997eda97 | -4.38104 | -43.15888 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 072e20aa-60a9-3524-9e77-05733504d79a | -4.36617 | -43.15645 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d88ec5ae-3de6-3f47-bce0-5e707aa361f4 | -6.98445 | -37.62629 | 2025-12-01 04:04:00 | NPP-375D | CONDADO | PARAÍBA | Brasil | 2504504 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2e5a8bc-2e32-3be6-80b4-c08d37ff4334 | -2.7969 | -45.23156 | 2025-12-01 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38aab1de-1fb7-3bad-99ac-fe9311b74797 | -3.21674 | -50.13597 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30bb6c93-7bda-3493-8cfc-f73a3ad34b43 | -5.48714 | -40.92958 | 2025-12-01 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31339360-fc24-3513-89b2-880625002158 | -3.7427 | -46.00954 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c422fdc-0f87-3c78-b412-625f64a21f3d | -2.64116 | -48.54618 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9544cf52-e521-3c77-a8f2-2a28fc5116fc | -2.64603 | -48.55059 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c39a5d1f-90ae-3145-8015-8fea78a80cb5 | -3.73819 | -46.00878 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 073d7efb-7a33-3939-b54c-1fe96d7be279 | -3.58548 | -40.43348 | 2025-12-01 04:04:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| faa37b2b-ca0b-395a-988e-b05a8f4715a6 | -4.39982 | -43.3339 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee5d0aca-8f00-30ba-b8b0-e0692891d6f2 | -2.9207 | -48.22692 | 2025-12-01 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56110691-a2f7-3a46-bdd3-caa7434369cb | -3.71134 | -45.90857 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| bdc27527-a2f8-3a27-b101-312c0f15d925 | -4.38708 | -43.34108 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a67f6c8-8919-3a9a-b471-ce1994e8f6e3 | -3.70457 | -45.90658 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b6fb4f12-2b8b-310c-8d44-8a0f7eb0bd6f | -2.64662 | -48.54712 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce5c3d25-0366-3640-a9cf-a4ee79a1b24f | -5.33489 | -43.57 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc3f0d5c-7d5a-3e44-b471-8811eb4f439e | -3.70979 | -45.90294 | 2025-12-01 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9f6660a6-e4ed-3999-b077-373791c5aca2 | -4.3762 | -43.15167 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8285ffee-6fd6-38a9-8568-6c9afcfa22f0 | -2.48604 | -44.15448 | 2025-12-01 04:04:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1403c6a-d4a5-3009-9411-01a7362609ef | -3.58292 | -50.274 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55c2754d-210e-35b2-b94d-d91a334f09eb | -2.60879 | -49.26173 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff062d91-b206-3655-a319-890c5e059b32 | -2.64411 | -50.00308 | 2025-12-01 04:04:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012dc2d8-a7ee-3144-8e01-9e1c5377ca60 | -4.37473 | -43.16051 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b51bf679-ce4d-3c00-9dc6-b0adc01304c0 | -1.24724 | -46.30399 | 2025-12-01 04:04:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b7cda86-6ed6-374f-a3c2-d6a6cf56edf7 | -4.36989 | -43.15705 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4e1eaf22-8056-3885-84b8-ab8fb3698c24 | -4.13086 | -43.72828 | 2025-12-01 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0bd49b9-7452-38c0-9102-1d8d017b05ec | -2.65012 | -50.00407 | 2025-12-01 04:04:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 402c83fe-e320-36fc-a590-551b753e0dbd | -3.39181 | -50.25297 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0bf1d167-4a33-336d-84c0-08526d1f467c | -4.38289 | -43.15731 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 63da9a73-37ff-329e-9c6d-dfc7460f4b6c | -3.2346 | -50.66928 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0f5a067-95db-3bcc-931e-c2c0e52e3ced | -3.43267 | -39.04488 | 2025-12-01 04:04:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13bbad59-7c38-33a4-b3a2-03545dc597a3 | -2.44322 | -47.07813 | 2025-12-01 04:04:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 995b96c1-a5da-323b-966d-76c4b4f9371b | -2.84955 | -45.62372 | 2025-12-01 04:04:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08144c22-01eb-3b4b-8161-3fe2b22bd17b | -2.24749 | -45.61569 | 2025-12-01 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc9a7651-6113-30dd-bc73-a5bcb6d9adfe | -3.75636 | -42.95979 | 2025-12-01 04:04:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dda56b2-73ae-3409-831f-5268f585ab7b | -2.9407 | -40.09893 | 2025-12-01 04:04:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 240d2675-8241-3eb0-ab9d-007c518b262c | -3.85151 | -40.9772 | 2025-12-01 04:04:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8498dfbf-dcdd-3469-b122-fe43648a4af9 | -4.37844 | -43.16112 | 2025-12-01 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 270e6ae6-ac56-3296-b29c-e62069446b44 | -3.44625 | -50.16211 | 2025-12-01 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c66190-c3a8-320c-8977-6c4ac5c57b56 | -5.3304 | -43.57386 | 2025-12-01 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfdd0977-b7cf-3e42-baf1-683752a2caf6 | -3.21147 | -50.13053 | 2025-12-01 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4909803-3a93-304c-a3a8-1bf4d327f6ac | -3.21648 | -41.568 | 2025-12-01 04:04:00 | NPP-375D | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 59f2417e-56f9-3fe7-884c-8ca2235b5cd8 | -4.3893 | -43.32758 | 2025-12-01 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3db9b39e-833a-3af9-9484-9407e724bbe5 | -5.52248 | -42.60351 | 2025-12-01 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f5df953e-7d6a-35c9-9f03-800896963ea1 | -2.63631 | -48.54173 | 2025-12-01 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd7a3646-9b72-32b6-9e75-581048a6d69d | -4.44404 | -42.97052 | 2025-12-01 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39a257d8-cd1c-3b9e-b2ac-67d7e029c7d8 | -2.92896 | -42.16357 | 2025-12-01 04:04:00 | NPP-375D | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c74797ca-b3f2-3e59-8b79-923328b06dbb | -3.63366 | -42.34834 | 2025-12-01 04:04:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 35039bf6-351d-33c8-878c-ffbb462e7efd | -2.60785 | -49.26354 | 2025-12-01 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89bb22b6-445b-3c02-b38f-f384dcb79482 | -3.93904 | -45.85074 | 2025-12-01 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a2975c9c-923a-36ab-bd72-7d12a4ed6a37 | -6.3534 | -43.97924 | 2025-12-01 04:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ec7c181-052d-3bd9-a68b-2b6c88ba06ed | -6.3572 | -43.97984 | 2025-12-01 04:06:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b9aad36-5a97-36dc-8c0f-d5f23d638bee | -7.09558 | -39.33716 | 2025-12-01 04:06:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d80ddd1d-a286-3cc5-945c-ded6f844e324 | -6.31214 | -43.80983 | 2025-12-01 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 89deb053-e913-3713-9459-da7b18ecc156 | -8.16909 | -43.21335 | 2025-12-01 04:06:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3292c1de-d2f2-3c86-b71b-edec8ddea906 | -10.13039 | -36.33871 | 2025-12-01 04:06:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0c1b2a26-a633-3ada-afdb-f3d351ef7096 | -6.99288 | -38.69541 | 2025-12-01 04:06:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2c25fedd-8325-3dc1-86d6-e585ae2df619 | -10.62877 | -40.51722 | 2025-12-01 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 90396b6b-6137-32e9-ade0-31e417dd167d | -9.87659 | -40.56915 | 2025-12-01 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2896474a-5e1a-3063-88e9-0e1d24dd497c | -6.3114 | -43.81432 | 2025-12-01 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c9043e9c-29d3-3d68-b964-244ac1daa726 | -6.3159 | -43.81045 | 2025-12-01 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7bfc66f2-5c02-3aeb-8c16-55277e95387a | -9.87604 | -40.57265 | 2025-12-01 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 93275f69-d7da-3a5d-812b-44f79c0ebc38 | -9.38342 | -40.62672 | 2025-12-01 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2d140339-aee0-3b9e-91c0-e63d38de4bed | -6.30462 | -43.8086 | 2025-12-01 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a1633a7-4f17-3bb8-8a35-6c1ea8c0279c | -6.99345 | -38.69179 | 2025-12-01 04:06:00 | NPP-375D | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f65e7678-0fad-3268-8d74-eec43641efb4 | -8.69827 | -39.47147 | 2025-12-01 04:06:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 82f6bfb8-d10a-321f-a522-ec6f2cf1321a | -6.96195 | -39.1362 | 2025-12-01 04:06:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b84d911b-0aad-3685-b644-27a35395dbbd | -6.31517 | -43.81494 | 2025-12-01 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0652d5df-d824-39e7-90a4-dcb985d2ee7e | -6.55789 | -44.00431 | 2025-12-01 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01ce89d8-f3af-3ffb-bb2c-53ce124f41ef | -6.30086 | -43.80799 | 2025-12-01 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 506788cb-03cc-3d56-bad7-58568e86e294 | -17.75319 | -47.29162 | 2025-12-01 04:08:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c8a0644-ac61-3e50-ae3b-38e815035eeb | -13.48385 | -46.70292 | 2025-12-01 04:08:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2834addc-5e84-3966-89e8-8fb37ec7edbd | -13.03627 | -40.05129 | 2025-12-01 04:08:00 | NPP-375D | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ebc4b16f-441b-3ede-a5a8-9b65f9e66eb3 | -17.00378 | -39.77514 | 2025-12-01 04:08:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d64148fc-0b3a-33b8-942f-cdc1693bec42 | -18.14629 | -47.14347 | 2025-12-01 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3c48107-7f29-3d13-9ae2-1941d339a85e | -19.21775 | -45.8036 | 2025-12-01 04:08:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59aa8029-d31d-34c2-b844-07b63515499d | -16.14119 | -41.09583 | 2025-12-01 04:08:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 37ce5f97-4be0-32b3-acd6-e8e820c91de7 | -18.34176 | -52.97273 | 2025-12-01 04:08:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2273b92-0974-34ee-8c76-f48ff9436bda | -16.4448 | -47.42672 | 2025-12-01 04:08:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba9fd9b7-73b9-3c3d-aba5-c349cb14965f | -15.27092 | -43.1776 | 2025-12-01 04:08:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d04f6df-7a4d-37ad-b153-e6fad9f0d381 | -12.01266 | -49.26553 | 2025-12-01 04:08:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d963a97-41b4-36e0-9356-65e4028acd51 | -12.00779 | -49.26454 | 2025-12-01 04:08:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b366e8a-89fd-38b2-a7b2-30faacdb9409 | -13.4693 | -44.54869 | 2025-12-01 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b6cd1dd-fc2e-3a23-b5da-0f9526c86d09 | -19.82909 | -42.4528 | 2025-12-01 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8f96139c-018a-310b-98dd-bb3ffff27a9c | -18.33547 | -52.97522 | 2025-12-01 04:08:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af9a29f6-5ce6-36c7-8225-fcd1f74bd1dd | -13.47983 | -46.70217 | 2025-12-01 04:08:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72f56146-29cc-316a-bae3-91405d02e3c8 | -15.39159 | -39.36843 | 2025-12-01 04:08:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9c492871-b28f-32fc-b89e-c5f93fd40926 | -14.04962 | -42.64983 | 2025-12-01 04:08:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e958c61c-495b-31c9-a054-d298d7f5f7bc | -19.21864 | -45.8056 | 2025-12-01 04:08:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
