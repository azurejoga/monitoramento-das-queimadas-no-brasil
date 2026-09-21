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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b18b467f-2802-328e-9749-b4e38c043368 | -11.3422 | -51.3394 | 2026-09-21 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d9049689-a1c2-38c0-a296-db3738da636a | -8.8275 | -50.482 | 2026-09-21 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9d2036af-e203-3eac-8816-92dda10c8fb5 | -8.7911 | -48.7502 | 2026-09-21 00:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 69.9 |
| fd6a972a-a401-3f3a-a694-603c95693b94 | -10.236 | -59.4018 | 2026-09-21 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a7c3454e-11fd-3ff5-b598-49c58ffcac08 | -4.3541 | -55.6653 | 2026-09-21 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2b927978-c630-39bb-9982-9450221e1f18 | -11.0223 | -54.1379 | 2026-09-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 44e51efd-28c2-310d-8ce4-1f666813a853 | -11.0509 | -54.9106 | 2026-09-21 00:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 51cb7253-bf05-399a-baf0-0bc1e8bdbf89 | -11.8204 | -49.8106 | 2026-09-21 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0c778985-5a1b-369c-8911-f3dbad75bb0b | -5.7799 | -57.58 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5665dfb3-32c0-35c8-ba2d-c62ed1d8615a | -9.5593 | -66.0545 | 2026-09-21 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d5a61005-dc6b-3eef-82b2-97ed0db96c77 | -12.6799 | -50.9526 | 2026-09-21 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8404e106-d1a8-3389-b620-a5c9b69ea35b | -11.8014 | -49.8129 | 2026-09-21 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 4e5c6136-8e2c-3b56-bad2-2094a9ffa0b7 | -9.5594 | -66.0359 | 2026-09-21 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| fa4d9b09-edad-3498-907e-80b0b57c65d0 | -7.5704 | -57.6766 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| e052c9c7-02cc-3d9b-84d5-6e88c32ddd28 | -5.7615 | -57.5807 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 75af62c9-fa6f-33fb-9f23-2cf7f4dbe498 | -5.2168 | -56.1096 | 2026-09-21 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 09e023a2-941e-3200-82ae-c74be0ab5439 | -3.3867 | -59.5223 | 2026-09-21 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 73ef5a6a-a402-391d-a517-5359f9f01e10 | -6.8754 | -63.107 | 2026-09-21 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| bb39e113-f4e1-32a4-97cb-4efd74261b82 | -6.4671 | -59.9711 | 2026-09-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 15178cb7-5c51-35d2-b395-b3b420eb6e5d | -7.5889 | -57.6757 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 256.0 |
| f13a4e29-408f-3312-9c72-12ad26f5b47a | -11.8017 | -49.7913 | 2026-09-21 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a1c44fed-dc86-3bd3-adf5-e20007df164d | -10.9112 | -53.9635 | 2026-09-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1bf932ae-8ec3-3820-997d-b7b84282601a | -7.6075 | -57.6747 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7e2d213c-c11f-3395-a6aa-7bc462eca450 | -10.8096 | -50.1407 | 2026-09-21 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2b4db102-3c3e-3c27-93aa-7ef9c5d657c6 | -7.5703 | -57.6962 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| c176da10-9546-397e-808b-031bb97e6c3d | -3.753 | -59.419 | 2026-09-21 00:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f4d0ff2f-fe6a-3d4b-ba52-cf4b52bdd218 | -7.5891 | -57.6561 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7e4e9c06-0c9b-3da4-9978-1b9299b03b3f | -9.5595 | -66.0172 | 2026-09-21 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 49caef6e-5a23-3453-9951-aec0a3d946e8 | -6.467 | -59.9902 | 2026-09-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| dacf07b6-8f9d-32b2-b134-2686cf26f897 | -6.3011 | -60.0154 | 2026-09-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8753fa4d-c10c-328c-aa9a-8cfa8b4f6d24 | -3.0534 | -61.2767 | 2026-09-21 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| b6f3416b-04eb-3d88-a280-e83476ac9db0 | -11.041 | -54.1567 | 2026-09-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c5eb8c77-f5de-3d32-adce-d2330be3f05d | -12.3102 | -50.1826 | 2026-09-21 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 66991cb3-1796-3168-b490-bd21cb1ad85b | -11.6802 | -43.4209 | 2026-09-21 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a91239b1-5832-33cc-891d-c549f5464a7e | -6.7464 | -59.4223 | 2026-09-21 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2ff6fce5-569f-328f-aa2d-64538b7393d0 | -12.3105 | -50.161 | 2026-09-21 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d58b9a4f-76b4-356e-be77-c20322052c67 | -7.5888 | -57.6953 | 2026-09-21 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 950baad5-08ad-3a38-80f1-96718e8e10e5 | -6.4485 | -59.9909 | 2026-09-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2ebb6ae1-ceec-3127-96af-b6f412c380e3 | -3.0535 | -61.2578 | 2026-09-21 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 858d6ee6-2031-33fa-89bc-8fc5059afceb | -3.0717 | -61.2764 | 2026-09-21 00:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 04c09960-4e5b-30da-9e9b-bccacdb61051 | -11.3419 | -51.3606 | 2026-09-21 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 833321b0-46c5-3e58-8e9a-7f312640e9ca | -10.2173 | -59.403 | 2026-09-21 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b08ec9a5-163d-34c5-a172-96e63f41d376 | -11.1372 | -54.0045 | 2026-09-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f2a3e8bc-4f69-31dd-b1a2-24238b5f9ed8 | -6.4486 | -59.9717 | 2026-09-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| eb0ba21f-34e2-3c66-9bc2-cb3389d3322e | -4.3542 | -55.6455 | 2026-09-21 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7ba2425a-c88e-30ed-b922-cf58e3bd8930 | -7.2519 | -55.5994 | 2026-09-21 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c0e2235e-bc17-32ac-9ee4-02212b1cf31c | -5.7615 | -57.5807 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b2f7a084-4d96-36c1-be7b-77b2ca9a3ddc | -10.4661 | -50.3693 | 2026-09-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 087a48cb-e334-3dda-8478-73723e6e7d5a | -7.4283 | -44.7639 | 2026-09-21 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 62253e13-098c-3b98-b2d3-e9a4c62e8bb6 | -11.3419 | -51.3606 | 2026-09-21 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 2883f963-6a02-344b-88b9-5af4c2eccd28 | -7.6075 | -57.6747 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0519565f-fa38-39bc-8fb0-6cbf34c2e53e | -5.7799 | -57.58 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ae0e90ca-a321-3a79-b9d4-89444a6a83c7 | -2.8791 | -57.799 | 2026-09-21 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 3b97e198-cd19-3245-bae2-cf0f6a262fcc | -3.0717 | -61.2764 | 2026-09-21 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 303954ae-463b-3446-90f2-7a15561f6196 | -7.5704 | -57.6766 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| c540f170-5d92-392c-9962-dccc52e976ad | -10.4477 | -50.3285 | 2026-09-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2356a3cb-fb46-365b-9440-020c3e555263 | -10.8096 | -50.1407 | 2026-09-21 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 5ef74220-f942-3c0e-8d5d-3289372067bc | -10.9112 | -53.9635 | 2026-09-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 30aab1b9-d739-3300-ad4e-83404a0b5e44 | -3.0716 | -61.2953 | 2026-09-21 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 73e9527c-44c0-3aef-b609-a7973b75ddf1 | -7.5891 | -57.6561 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c46924ec-c57d-3023-92b7-c870ea157e8e | -7.2519 | -55.5994 | 2026-09-21 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 90d66534-e0d0-394c-b3c9-3671efff6e43 | -10.4475 | -50.3499 | 2026-09-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| e5f2dbd1-d518-396e-89d2-dd87cb082771 | -6.467 | -59.9902 | 2026-09-21 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 28cec678-74d6-30cf-b7ba-1fe702746d60 | -10.4288 | -50.3305 | 2026-09-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9164339b-1838-3035-a320-3c1c98df2bed | -6.4486 | -59.9717 | 2026-09-21 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| df9a9df5-89ca-356d-ba3d-c1d1a228978d | -6.7369 | -55.0874 | 2026-09-21 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ee8fe694-26d4-38d9-a3fc-4c668928d5b1 | -10.4664 | -50.3479 | 2026-09-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 8ef27efa-4bf2-3bcd-b6e0-6e9b917c066f | -11.8014 | -49.8129 | 2026-09-21 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 1bc402f4-e1ed-3db9-99d8-f7a667ac83c3 | -6.7464 | -59.4223 | 2026-09-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 78a2dade-c9a9-3128-9f01-d60a4c235d15 | -6.4671 | -59.9711 | 2026-09-21 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 701a4afc-df3f-37b9-aece-19fafcd6721f | -4.3541 | -55.6653 | 2026-09-21 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2cb7d8fd-ac1a-303f-8513-dd0e237fb8c2 | -8.7726 | -44.28 | 2026-09-21 00:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2ec5203a-f3a5-3b20-ad2d-659db1a8471b | -11.0223 | -54.1379 | 2026-09-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e4f1e240-eceb-3cbf-ad0e-27e11cbfb989 | -6.8754 | -63.107 | 2026-09-21 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c96dc746-edb4-3080-9442-993af9874c00 | -16.03 | -52.5135 | 2026-09-21 00:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e3f990bd-8e59-3ddf-8d52-1ed5f9f9dbcf | -4.3542 | -55.6455 | 2026-09-21 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b78649ed-1631-3abc-89d1-9d93f5a27f1b | -3.0534 | -61.2767 | 2026-09-21 00:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8871a006-8f80-35ea-8d83-a905061204b3 | -11.0509 | -54.9106 | 2026-09-21 00:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f5780ba9-cbb2-3193-92e5-e72120ca0af1 | -7.5703 | -57.6962 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 3c8a91eb-da52-332a-925e-12a147f0dd84 | -5.2168 | -56.1096 | 2026-09-21 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 8b55bc3d-0d8a-39b0-a60b-ce5883060136 | -6.3195 | -60.0147 | 2026-09-21 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 61f360ea-66e1-3709-b290-a29ae2896d1e | -9.5594 | -66.0359 | 2026-09-21 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8cb885b4-bdba-3700-87e3-44f137bd9612 | -4.0944 | -52.1252 | 2026-09-21 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 064b72b1-4643-3d22-b32d-e0290be54c3c | -11.041 | -54.1567 | 2026-09-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4b1104eb-2712-34fb-99bb-17933410c67a | -7.5889 | -57.6757 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 221.6 |
| 64485075-8642-35ab-8a51-cb7224c99578 | -7.5888 | -57.6953 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 7d92f91f-257c-3f67-853c-58024b7402d8 | -9.5593 | -66.0545 | 2026-09-21 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fc7aefb7-09e7-3200-8054-532082f07c02 | -10.2173 | -59.403 | 2026-09-21 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 59f65d31-0789-3814-acd3-1ef71ed9bd91 | -3.753 | -59.419 | 2026-09-21 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| cb2fedf3-2095-380b-8ab1-e6976ad493dc | -6.2026 | -57.7778 | 2026-09-21 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5f1242ef-c752-337f-944d-fc7baa10edde | -10.78 | -50.85 | 2026-09-21 00:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5d9509b-d13a-3ea0-93a2-34f5d358e55a | -10.69 | -50.77 | 2026-09-21 00:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d03ab12f-f0f6-3942-905f-3d8b018f41f0 | -10.72 | -50.78 | 2026-09-21 00:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64a7454c-876a-37ed-ae6c-c55fd83687ce | -10.78 | -50.8 | 2026-09-21 00:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54530d55-7d4f-39cd-9228-3b7a2c13dde7 | -10.75 | -50.79 | 2026-09-21 00:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4bd01f9-b245-30b3-adb7-8da7e9e78c52 | -10.75 | -50.85 | 2026-09-21 00:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d958283-0b8d-3971-be6b-b6d2be284996 | -19.61891 | -48.71401 | 2026-09-21 00:18:00 | TERRA_M-M | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bb2cdcc0-763c-395e-a1da-e282ea75b95a | -17.75756 | -46.99713 | 2026-09-21 00:18:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 074f5e07-7341-33ba-bbd8-a162774adbcf | -17.75544 | -46.99097 | 2026-09-21 00:18:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 947aff85-66f9-34ac-9db5-8639f56c63c8 | -18.72758 | -45.14603 | 2026-09-21 00:18:00 | TERRA_M-M | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |


[Clique aqui para ver as próximas entradas](README2.md)
