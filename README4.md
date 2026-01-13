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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d552df9-dc98-3e53-afb4-a299c6072b9f | -2.86569 | -45.24096 | 2026-01-13 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4990b884-52f2-36e8-b200-0aee9bc4b329 | -3.29975 | -42.53172 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 445c84ce-74fe-38df-bbc8-d55d3e9ad9e0 | -5.1913 | -37.69545 | 2026-01-13 03:59:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b481bf5-6411-382a-acac-fadc0f05541d | -3.55221 | -43.65807 | 2026-01-13 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 557cd46f-8080-3722-b4cd-681d2624fc73 | -7.39362 | -35.21245 | 2026-01-13 03:59:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 38238c8e-b970-3321-a4b4-199ba94e9056 | -5.92671 | -43.32737 | 2026-01-13 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 504a3e51-67dd-373e-b75c-9b2c1e054137 | -4.2015 | -39.56607 | 2026-01-13 03:59:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38d00ded-67d9-3ab9-8e66-75e4371be95f | -2.4224 | -44.9594 | 2026-01-13 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbec7ac6-1061-3e0b-a03d-9964739937a8 | -5.24774 | -39.68537 | 2026-01-13 03:59:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4850940b-4c13-367e-9c84-83a4406fe48e | -3.6002 | -41.86529 | 2026-01-13 03:59:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1a2d1fe-4102-32f8-9ac8-1a1b68a0131e | -4.92124 | -43.42627 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f56e03d2-a177-3809-b73e-c0e026d47dc0 | -2.92632 | -40.60023 | 2026-01-13 03:59:00 | NPP-375D | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1908c4f-1be4-3270-956e-0fe9b7bc015e | -4.42289 | -43.09998 | 2026-01-13 03:59:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cc1d6215-9004-3ff6-9e39-c5d82a0852fd | -5.10578 | -39.46422 | 2026-01-13 03:59:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7bd79c09-0585-3de2-bc91-7d83efca87d0 | -5.16154 | -36.58954 | 2026-01-13 03:59:00 | NPP-375D | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 0e302596-1f89-3e40-9ed4-52310f70a57b | -3.55044 | -43.65066 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af050b51-aa02-3dbe-847c-7a2e9a3c61d9 | -5.49482 | -42.15844 | 2026-01-13 03:59:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6aff8598-eb82-3d9c-8e34-5d5120f44b39 | -4.42636 | -43.1042 | 2026-01-13 03:59:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e9894aaa-71dd-30eb-8a11-8735d0e4b6cf | -8.50974 | -37.0836 | 2026-01-13 03:59:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63d6d9d0-90f7-382e-867a-910a7815bfa1 | -7.52822 | -37.02766 | 2026-01-13 03:59:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 344b4397-566a-3641-b4af-81563212ad72 | -5.92613 | -43.33086 | 2026-01-13 03:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fabb11eb-a9c1-3130-9b45-fd3c4abfa673 | -5.41727 | -38.16851 | 2026-01-13 03:59:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3ca27cca-6fce-3c7a-b00f-fe43ab78e536 | -5.09996 | -43.22578 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| e0068b8f-5a37-3280-8dff-424d09b84f3b | -3.54794 | -43.65738 | 2026-01-13 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dc7c649-b4dc-3d33-9d04-31bb10553385 | -5.5361 | -43.67859 | 2026-01-13 03:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cabddc5b-05e8-3e21-b141-30565c96e532 | -5.92729 | -43.3239 | 2026-01-13 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a72f3b2-7ee9-38ec-b65a-f61015a6508d | -3.30132 | -42.53533 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 72450ad4-d619-3c8c-9095-8372fe5ffc71 | -5.09476 | -43.23214 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| acaea9c2-d728-364c-8d12-a51903111a63 | -4.41824 | -43.10286 | 2026-01-13 03:59:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 62e780f3-5582-3b5d-a4b3-dc50670fc58a | -2.42158 | -44.96446 | 2026-01-13 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 963c6811-cdc4-30d9-af41-956d4b84ae68 | -3.30204 | -42.54258 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f13f8f4a-d6cd-3b01-9f2c-e961af9373ef | -5.09416 | -43.23576 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0527d43e-599c-3a3c-844a-5499f3e6d0a8 | -4.90685 | -38.72059 | 2026-01-13 03:59:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c112aa6-5e76-3ba5-8019-d47cec3f382a | -5.10636 | -39.46065 | 2026-01-13 03:59:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| aba60dbe-748a-3388-bd4e-938aabdd085f | -8.10878 | -38.28291 | 2026-01-13 03:59:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3f38fb9-e2f3-35ef-81fa-335ba47e30fe | -5.24592 | -37.50017 | 2026-01-13 03:59:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e873046-42c8-3247-8126-d2b50f182c85 | -7.81025 | -36.4435 | 2026-01-13 03:59:00 | NPP-375D | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e4602f9-b1a5-3c45-8a3e-9be4ad1e691e | -2.95824 | -40.46888 | 2026-01-13 03:59:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 50bc96ad-fc29-32f9-b653-815df10a0f75 | -3.30051 | -42.54046 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d71ff39e-60ef-30c5-8556-1c1237059463 | -2.8757 | -45.2336 | 2026-01-13 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 754e16dd-9cd8-32a2-892e-000ab5ccefd5 | -3.54981 | -43.65461 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca92023-2854-3c85-8ee1-03728a2b5f7f | -8.37286 | -35.38806 | 2026-01-13 03:59:00 | NPP-375D | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 634981ca-2f9b-376f-b0f9-9ee62c7d24ea | -3.53574 | -43.66036 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96c6f003-b5f3-367d-8831-54bbce78b4c0 | -3.28924 | -42.54577 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2171a4aa-8e84-3238-8d9c-ccce520b3501 | -3.55353 | -43.65021 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa3e0ac-8003-312c-bc56-d05f3edce087 | -5.49556 | -42.15391 | 2026-01-13 03:59:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 03839b55-7460-3df9-a9f1-ce88be507028 | -7.53128 | -37.0274 | 2026-01-13 03:59:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 91d0bc42-af8c-36d6-8ee6-3af11fad80e0 | -6.10656 | -35.26323 | 2026-01-13 03:59:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 885f44e6-8d39-3acd-bdc2-ac057f421cf8 | -2.87263 | -45.22247 | 2026-01-13 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5142cac-fc55-3fec-abb0-1834106865e6 | -3.29291 | -42.43501 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db40a107-9d90-3394-9bbc-105e91a6e4f0 | -6.22053 | -38.31349 | 2026-01-13 03:59:00 | NPP-375D | ÁGUA NOVA | RIO GRANDE DO NORTE | Brasil | 2400406 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8706a3ad-d6d1-32b1-b809-dee400efa19c | -5.93015 | -43.33154 | 2026-01-13 03:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07b9a761-860e-3016-a6dc-2c56efb64f13 | -5.09939 | -43.22929 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| a7fc1f5c-9fe5-3498-bc92-32c1f126f0b3 | -9.09951 | -35.49662 | 2026-01-13 03:59:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a5834a5-26cd-3e13-947b-84dd2203e078 | -5.0988 | -43.23288 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| a6ea9b13-17e1-31dd-8b3b-aa797e0fb9f6 | -3.55287 | -43.65414 | 2026-01-13 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a21cc8b-5a41-3123-a149-9c28a94b352c | -5.11031 | -39.45762 | 2026-01-13 03:59:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c9875495-0f35-31de-a77d-08d0b065424c | -4.73311 | -45.79269 | 2026-01-13 03:59:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e1598b-5b5b-3dd0-b2e9-a700384e46d2 | -4.74051 | -40.82717 | 2026-01-13 03:59:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0224dd37-e381-364a-9a8d-bdde49232610 | -3.54427 | -43.66181 | 2026-01-13 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fba76d58-8d17-3f39-a35b-886aafff8fd8 | -2.42634 | -44.96524 | 2026-01-13 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64f3c189-8972-3640-b182-1213a507f5af | -3.29891 | -42.53682 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 34105a82-8c2d-36b4-a3b2-ce467f575335 | -2.42716 | -44.96017 | 2026-01-13 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1fdd4f13-950d-30d7-9ac8-263cc7f7bc66 | -4.95447 | -43.6926 | 2026-01-13 03:59:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09649fac-b633-339d-a7c1-1b0bf8b84c7e | -5.72812 | -41.27559 | 2026-01-13 03:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65a21d96-1455-3732-96fb-54b0825184c9 | -6.74459 | -37.98578 | 2026-01-13 03:59:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69d145a3-84fc-3ad5-963d-8fa72b6aa8f6 | -6.10293 | -35.26266 | 2026-01-13 03:59:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7c6d61e-9971-38ea-8b43-c2f0cc6fc751 | -2.9461 | -40.38517 | 2026-01-13 03:59:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9b8e129-fc2b-3110-a207-bd96cb72a251 | -5.18069 | -40.14882 | 2026-01-13 03:59:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d673412-7ece-33fc-82e7-ecd780b05490 | -6.47996 | -42.94024 | 2026-01-13 03:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86d95396-bb62-32d7-bfb8-8b109a6965f8 | -2.01749 | -46.64532 | 2026-01-13 03:59:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5411b98-7a92-3f5b-b11c-6ee4f30e62b2 | -6.74405 | -37.98928 | 2026-01-13 03:59:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5cde104b-b693-3e29-9192-d45bd98b1b67 | -3.28692 | -42.54877 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 454c6646-c9a3-325d-8faa-57b7f36161cf | -3.53146 | -43.65971 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 355b1739-ba74-3df9-9e64-fefdefd27d29 | -3.30289 | -42.53746 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad9f98b5-4d36-3a3b-80b8-8aab8e5d559a | -3.30449 | -42.54111 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 914c13c0-bbfb-3589-bd5c-aaa1e7e2ac14 | -5.52901 | -42.85321 | 2026-01-13 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b5cea06-61f7-30f0-b246-aaf2e7a1c809 | -3.60326 | -41.87055 | 2026-01-13 03:59:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 887ddd90-b685-3915-9f6f-d6c14f22d566 | -6.21666 | -38.31644 | 2026-01-13 03:59:00 | NPP-375D | ÁGUA NOVA | RIO GRANDE DO NORTE | Brasil | 2400406 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3ae994d6-d84f-31a7-8709-040d2590b151 | -3.5134 | -40.35862 | 2026-01-13 03:59:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c7804e3b-677a-3e44-9b6f-d7905bde3567 | -5.10343 | -43.23005 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 2fde6a63-55cc-35a8-afec-8349a451b441 | -3.54918 | -43.65855 | 2026-01-13 03:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c333fb2-fff6-3fba-ae0a-127d860966f3 | -4.48319 | -38.59635 | 2026-01-13 03:59:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62ac3a64-5ae7-3086-ad51-1b63cd59fd52 | -5.28798 | -43.5657 | 2026-01-13 03:59:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6eb330e8-c2bb-3ebc-bb11-1b0f8c824582 | -4.63055 | -43.61396 | 2026-01-13 03:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cadb239-a3fa-374c-bdcb-9186d672098e | -3.55418 | -43.6463 | 2026-01-13 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da947179-bfac-373d-ad7d-70c4e684c1aa | -4.7322 | -45.79799 | 2026-01-13 03:59:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ea71e2-c72f-31d6-8025-e236d677d46a | -5.15124 | -40.96287 | 2026-01-13 03:59:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a02dc2e8-2559-31d2-b111-ec7a3bab4b17 | -5.24342 | -37.36318 | 2026-01-13 03:59:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91651d6c-d04e-3b8f-b12d-e43c864bf59d | -5.09535 | -43.22854 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3508dc6f-be8f-3615-a2b0-2c97ff7f019d | -5.09593 | -43.22504 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| f788a965-13e2-3e52-b5f9-015890ae24e2 | -5.10747 | -43.2308 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7afb5741-2f1d-3139-bb65-91087ffc1f57 | -5.6275 | -43.25511 | 2026-01-13 03:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70e5869b-f081-399f-99d3-9179c4985a7e | -5.09821 | -43.23647 | 2026-01-13 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| e0983e83-86bd-3a68-8c8d-49102bb2aefe | -7.53163 | -37.02818 | 2026-01-13 03:59:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa4e52a1-9de2-3c40-86a1-931bc43d334b | -2.87744 | -45.22325 | 2026-01-13 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2386acf4-0bd5-35af-ac6f-070b3a0d1c76 | -4.42695 | -43.10064 | 2026-01-13 03:59:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ca4c5b46-e091-3a8a-8b4c-045dfa5fff33 | -2.87176 | -45.22764 | 2026-01-13 03:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7ce708c-0d64-33e9-a955-4b3be5a78b91 | -3.29734 | -42.53469 | 2026-01-13 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 63e3131c-ce1d-35bf-ab32-0d70107dbb51 | -3.70978 | -41.6885 | 2026-01-13 03:59:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
