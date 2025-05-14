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
| 16ff4992-d5d3-3d62-bfd6-df0bfc1a6188 | -13.56133 | -52.88687 | 2025-05-14 00:54:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 2cf292ce-cd5f-33f4-a542-399ae538d75c | -12.72754 | -54.97861 | 2025-05-14 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f7a6e664-46ee-3d51-8d19-6b67bdd321a0 | -11.66202 | -54.95729 | 2025-05-14 00:54:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 383a3bdd-484a-39a8-92b0-13304fe33cfc | -13.04783 | -53.72852 | 2025-05-14 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5ec3a404-09f5-3d07-8939-b7abb212913b | -11.78595 | -47.36577 | 2025-05-14 00:54:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9e381fa3-494a-3509-8f6a-907720ca9d17 | -12.15715 | -48.00742 | 2025-05-14 00:54:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5a11c7c0-80a3-387d-a52d-f6f9f7089bb5 | -10.00249 | -47.84074 | 2025-05-14 00:54:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| b99bf142-4534-3861-af82-95caffa6ce66 | -11.63607 | -48.13012 | 2025-05-14 00:54:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5add9f32-eae2-3b39-9788-06cb5f4e8be3 | -11.63119 | -48.12642 | 2025-05-14 00:54:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| bf6a9060-2c81-3764-9728-82627daf1fc0 | -13.0463 | -53.71676 | 2025-05-14 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 062e8dbf-5f31-345b-ab55-d543bf34f801 | -10.00419 | -47.85231 | 2025-05-14 00:54:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d8fbce16-e238-3b20-94f2-259058d05547 | -11.16517 | -48.6833 | 2025-05-14 00:54:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c1cc478e-30d5-302c-ab27-6a911ad45b78 | -11.79768 | -47.3759 | 2025-05-14 00:54:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 89e8ea74-189f-3418-a20a-1df534751ba2 | -13.38782 | -47.51089 | 2025-05-14 00:54:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e9ec7454-6f93-321c-aa4e-755b1222b42f | -13.96653 | -56.79796 | 2025-05-14 00:54:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 1abbe667-243e-323b-a401-eb36b992d6c2 | -13.56952 | -52.87494 | 2025-05-14 00:54:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 474c1682-d151-3700-b1d9-2cb39a650208 | -11.14897 | -48.68186 | 2025-05-14 00:54:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b637db53-27ca-3ba3-a964-9d44c0a19610 | -13.68976 | -47.77015 | 2025-05-14 00:54:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f9059f2b-26c9-342d-bdc8-640846e7c051 | -13.04712 | -53.7229 | 2025-05-14 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 32724727-08e7-37c5-96bb-a84818faf0da | -13.96544 | -56.79267 | 2025-05-14 00:54:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 970f21b2-a813-3fba-8c2f-9f07043825da | -12.68535 | -58.13482 | 2025-05-14 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| b0ff1722-f9d7-37ae-b940-978dcdd4d916 | -11.79595 | -47.36417 | 2025-05-14 00:54:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e54002ce-a99c-3f3f-b159-107fd7f4ebee | -11.78768 | -47.37744 | 2025-05-14 00:54:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0e4891c6-f7d8-333f-8cfe-80d47b2dd0ea | -13.0828 | -52.04778 | 2025-05-14 00:54:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f8f4ef24-ae00-3d44-bb88-97be624b0fab | -13.95367 | -56.79979 | 2025-05-14 00:54:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f02a4066-6d85-32ed-8aff-872642cb18db | -13.96416 | -56.77786 | 2025-05-14 00:54:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0ffe9414-9b0f-3b66-b63d-0867ef09fe92 | -11.63448 | -48.11954 | 2025-05-14 00:54:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e444ce7d-ffa7-399a-8fee-a2e0b9a60394 | -13.06979 | -52.02003 | 2025-05-14 00:54:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 59b4e876-f052-36ea-90e0-ae12fafbea0e | -8.7173 | -50.24408 | 2025-05-14 00:54:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c3676408-e066-3c05-a518-462f8a0b6c1a | -8.7186 | -50.25323 | 2025-05-14 00:54:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8fb5b1a-4337-3527-947a-8fbacc883aa8 | -11.79931 | -44.28448 | 2025-05-14 00:54:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| bd0ce7ff-bbce-3870-b364-83edb0de6af9 | -13.60294 | -47.38533 | 2025-05-14 00:54:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4b73013f-2018-3e97-8f7d-c9d8f07f62cb | -13.9521 | -56.7893 | 2025-05-14 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| af657f6c-da64-3ea2-8ebb-c615809d0a9d | -13.9713 | -56.7874 | 2025-05-14 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| daa8100c-7090-3082-a89e-fedc8f0baac3 | -13.9713 | -56.7874 | 2025-05-14 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 54c2ab25-e1f0-39c3-8420-152ce65dea2c | -13.9521 | -56.7893 | 2025-05-14 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e897c679-7422-341e-9a2e-d4bfa360ff8c | -13.9713 | -56.7874 | 2025-05-14 01:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a5ec556d-7621-38e2-a09b-5ea159003a09 | -13.9521 | -56.7893 | 2025-05-14 01:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 41999665-7620-3e98-b338-6cc4cbaf540b | -13.9713 | -56.7874 | 2025-05-14 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 2ec5f629-ae20-31dc-a9f0-303cbc5e7ee7 | -13.9521 | -56.7893 | 2025-05-14 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| dc84adcb-66f6-3c0d-901c-cd8cfa0cf7e6 | -21.6089 | -56.048698 | 2025-05-14 01:33:00 | METOP-B | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4cda1a49-a2e7-3abb-a3a7-a45442cafc37 | -21.604601 | -56.032799 | 2025-05-14 01:33:00 | METOP-B | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a469a2fb-de49-3ccf-b46f-7d15d5d878b4 | -13.9669 | -56.779499 | 2025-05-14 01:33:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b62a2eea-fe32-39c0-8380-3c0941e76189 | -13.9622 | -56.8013 | 2025-05-14 01:33:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| debfa936-fbc1-3d9b-a6a1-ca49af3423da | -13.9572 | -56.7822 | 2025-05-14 01:33:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52599d52-bf52-3bfc-a91b-b00351b5735c | -9.4773 | -40.3116 | 2025-05-14 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.6 |
| ae482f9b-da8c-3970-a53b-a53f3fa0c291 | -13.9713 | -56.7874 | 2025-05-14 01:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 93d2b2f5-77df-358d-8a29-418e031fe1bf | -13.9521 | -56.7893 | 2025-05-14 01:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| e829c523-e627-3b74-83a4-c1dadd59bd92 | -13.9713 | -56.7874 | 2025-05-14 01:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| d015b8e6-5dcc-3f1f-8261-da820160d6dc | -9.4769 | -40.3365 | 2025-05-14 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.9 |
| ffc5c265-cdb4-37cf-abfe-57f438429d6a | -9.4773 | -40.3116 | 2025-05-14 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 27e4b557-0435-37a0-9f8d-868da66493b0 | -13.9713 | -56.7874 | 2025-05-14 02:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 193fe293-ed8e-304f-95cf-e29b1675e2dc | -9.4773 | -40.3116 | 2025-05-14 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 45.7 |
| 7196afd1-533d-3911-8332-c3b623e81ff0 | -13.9713 | -56.7874 | 2025-05-14 02:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 075b755b-17e9-3aa1-a0ca-6b5034cfd9a9 | -13.9713 | -56.7874 | 2025-05-14 02:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 519bdbfa-4b2f-363c-a3cd-914f47ea2ea1 | -9.4773 | -40.3116 | 2025-05-14 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 4282bba5-9818-33c2-9624-fe5493f1b8f2 | -13.9713 | -56.7874 | 2025-05-14 02:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a9a79c77-2298-3ceb-bb69-3afcbdcbcef4 | -13.9713 | -56.7874 | 2025-05-14 02:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f618cb89-fbc1-3440-8980-bd68b251c329 | -13.9713 | -56.7874 | 2025-05-14 02:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 010ab6d7-cff3-328d-a624-70c5802cdfe1 | -13.9713 | -56.7874 | 2025-05-14 03:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 6aa044db-a283-31e2-833f-9d17f9900499 | -9.75118 | -36.97975 | 2025-05-14 03:04:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 437c7125-b652-3d62-8d19-cb62795a936b | -9.50434 | -36.63493 | 2025-05-14 03:04:00 | NOAA-21 | IGACI | ALAGOAS | Brasil | 2703106 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 455c5a25-f065-3de9-aa7b-91828ee600b8 | -13.9713 | -56.7874 | 2025-05-14 03:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 24d1fb29-890d-3204-ba74-f4c19708e683 | -13.9713 | -56.7874 | 2025-05-14 03:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 7be04d9a-ee04-34e9-b036-a3b67e23fc79 | -6.64644 | -41.99686 | 2025-05-14 03:30:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fc8cce8e-7ceb-3356-b968-647764ec56bd | -4.98241 | -38.59867 | 2025-05-14 03:30:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 32c98588-8d2a-3ceb-8dee-038574e9701c | -7.23281 | -35.59013 | 2025-05-14 03:30:00 | NPP-375D | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 614b693a-6d7f-3f34-bff2-86486e4006be | -6.32707 | -43.74644 | 2025-05-14 03:30:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa07f68b-65a2-3b9c-b4ad-045fdc959caf | -6.34275 | -43.38931 | 2025-05-14 03:30:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fc8c7a4-f097-3e40-8acc-2eb08bbfbc8f | -6.65203 | -41.99794 | 2025-05-14 03:30:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| edb1dd91-9e29-3187-9b94-345b1d5cd644 | -6.3436 | -43.38457 | 2025-05-14 03:30:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4fbc7b0-cdea-3100-ba29-2020f094c056 | -6.6527 | -41.99422 | 2025-05-14 03:30:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 178a97a8-1ec2-34fe-9ee9-5be945fc0b7b | -6.32073 | -43.74561 | 2025-05-14 03:30:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 583ba722-b03b-3f59-af71-2f22b0fb921b | -5.04582 | -37.40571 | 2025-05-14 03:30:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9298d473-638f-3f46-a04f-76ed0bd12052 | -5.04598 | -37.40663 | 2025-05-14 03:30:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ff562db-ad9a-3fdc-8acf-5e2af7569c60 | -9.75364 | -36.9812 | 2025-05-14 03:32:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71e97fc1-0184-3380-823a-a644199079c5 | -11.79693 | -44.27753 | 2025-05-14 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 960e3486-843a-3eb4-b1ca-3e5a2f3ce034 | -8.07373 | -34.97578 | 2025-05-14 03:32:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b71ae49-6f00-3b00-90aa-3dfa92020633 | -12.49572 | -44.50385 | 2025-05-14 03:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd47ad83-6a20-3d0a-8ff2-1f1b70d0dc83 | -11.80372 | -44.27438 | 2025-05-14 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 911777b6-8aa1-3d30-aae0-9aff2a640f54 | -10.6601 | -44.49578 | 2025-05-14 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ee7f39-55ea-33bd-8243-36bce6585c60 | -11.7978 | -44.27316 | 2025-05-14 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 837a889c-cd59-32f1-90c7-84a3c3ed3b53 | -6.97529 | -42.77917 | 2025-05-14 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0632455a-eb9a-3522-8efe-f04cafd5e493 | -8.56551 | -38.05021 | 2025-05-14 03:32:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c781803-94da-3b13-a6f3-11d9dec75d37 | -11.28746 | -41.86401 | 2025-05-14 03:32:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7178a5fd-0f69-36be-bf0b-dc780f4f4611 | -11.79031 | -47.37843 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9a2cbcee-d631-3568-9269-613ce5d1da02 | -10.66077 | -44.49595 | 2025-05-14 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09aae1ea-9812-3b76-9446-f58265a63914 | -11.79023 | -47.3631 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 181a5930-bf2e-30f8-a0eb-3c667292dacd | -6.97382 | -42.78734 | 2025-05-14 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91791688-8cdf-3b7a-8179-8f7872ca970b | -13.04887 | -43.48737 | 2025-05-14 03:32:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1520b26c-45e2-32bc-a0d4-7c4e6a0ac287 | -12.49659 | -44.49942 | 2025-05-14 03:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0836d79-ef08-3a89-8b6a-85ca14995110 | -12.49272 | -44.49803 | 2025-05-14 03:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82a74322-853b-37e7-a8de-fffb55f4cc40 | -11.28687 | -41.86713 | 2025-05-14 03:32:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ffd7785-dc15-357a-aaac-94e0cb586543 | -13.04814 | -43.49105 | 2025-05-14 03:32:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b651c34b-c201-3349-a05c-bc8765b6fd86 | -10.5205 | -36.46867 | 2025-05-14 03:32:00 | NPP-375D | BREJO GRANDE | SERGIPE | Brasil | 2800704 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4605af66-7b32-3b52-9ad2-ee76c40e01f4 | -8.91709 | -37.97197 | 2025-05-14 03:32:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c2a3a2e-3bbc-3443-b92e-7872734ad1b4 | -11.80284 | -44.27878 | 2025-05-14 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a34b8301-cd31-33a7-8b75-0bf9518f764b | -11.78727 | -47.37729 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3ae5a69-d467-3289-b18c-9ea79fed39ff | -11.79585 | -47.37164 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e9f87cf-1db0-3876-a134-99738bb733a3 | -11.79868 | -44.26878 | 2025-05-14 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README3.md)
