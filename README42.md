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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06c4f59f-bf43-3d20-aaa3-2424830855a5 | -4.5654 | -48.60694 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e609e648-0342-31e3-ab49-31882ec57a36 | -5.59017 | -43.40453 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94dff181-0c75-3351-b6de-97dd3aaa7142 | -9.9771 | -48.01963 | 2025-10-05 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dd54ad7-611a-399e-8203-c6ebe440d5d3 | -7.16098 | -46.08614 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 51826de6-67df-328a-993c-b6386eebbe4a | -6.44368 | -44.15235 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80448e29-3843-3925-be96-c9af59a2e762 | -9.29543 | -45.9902 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d833222b-f293-359d-8bfe-c7ff09bdb5ac | -5.67576 | -42.78119 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c6ec5cb-f335-317f-b54b-37b290ad959d | -6.39928 | -43.06453 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82ede394-71a7-318c-acb5-aaa85d8fd70d | -5.96003 | -43.51841 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c69f7d24-deb6-3fc2-94fd-71ebc50a8d3c | -5.53418 | -42.66217 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62d55c56-4de4-3af4-aa54-8f7a09eceea8 | -9.14763 | -50.06393 | 2025-10-05 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b0ac4c5-6c87-3811-a63c-b0b5f44eb30c | -8.86685 | -46.85241 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab2e6e33-f95d-3d0b-bd36-8b49e4d60ed6 | -9.11905 | -44.40072 | 2025-10-05 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88d81422-991f-3c8c-a83f-371711b19030 | -10.39615 | -45.41763 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 383f2f72-9824-36dc-9828-17d7617b2f99 | -7.4272 | -46.49713 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f9051a4-249e-3213-85b6-6179918f904a | -6.17683 | -43.8347 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eff39ae3-a6ad-3769-923f-51a2e73472c0 | -5.58423 | -49.0344 | 2025-10-05 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf67a81d-a50d-3727-bdb7-16999a27dfe4 | -6.36443 | -41.62162 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba23678e-048f-379a-b2db-d0bab19828c0 | -6.9879 | -47.46625 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c071a45-2c6a-3025-b6ab-a751d54e0df5 | -6.40104 | -43.05413 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1d4ef868-7d2a-371d-a6e4-e9fa85124d52 | -7.58578 | -43.06907 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6c79666a-517d-376f-8bd9-d65cc3a57777 | -6.69913 | -41.95249 | 2025-10-05 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 81fc9e97-3e2d-31a8-b1b0-4042c65dcb30 | -10.64581 | -46.32182 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8c4d1d7-4e38-353a-95d7-74f4c6ad4210 | -6.14614 | -44.64884 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 2c1ac81f-06c4-3234-b68c-3ab5b9ed75cb | -7.77695 | -44.12254 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65f1d2e5-e40d-3269-8f85-2cddf6396eca | -9.29841 | -46.00019 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 543f2404-3cfd-326a-b47d-d7748c6df7de | -5.86442 | -43.55627 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6cbca52-ae31-3cdf-bca0-354d886b27c5 | -7.79931 | -44.54816 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 547e86bf-62e4-302b-bd6d-99f415c7c8a8 | -7.74521 | -42.54419 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9702276c-810d-3ecc-a109-fd1dd6608f52 | -8.55701 | -46.26303 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 93c9cdfe-ddd2-3ff4-b751-a227a45f7fa3 | -5.83171 | -45.81458 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1f14874-2bf7-3556-a081-029d6aae8785 | -6.46408 | -44.58651 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18c4676d-8eb9-307f-89f5-e2557e745d21 | -9.29759 | -46.0048 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7135c25c-0a01-35b2-bf10-3590e0d94f14 | -6.15133 | -44.64518 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 94ad766d-6df8-3613-a675-f700ef42dddb | -8.58128 | -46.32212 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 84b713e4-6285-325a-a9f9-67dab9c8370a | -7.71546 | -46.2641 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63a80de4-cabe-31fa-bacb-fe1cbf57fc91 | -10.64404 | -46.33158 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 18ce0125-969a-3248-a80b-ec6068fae34c | -7.72529 | -42.3853 | 2025-10-05 03:53:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 683627ce-61f8-3a15-8ee1-bb4ac9eacabb | -6.06256 | -42.5326 | 2025-10-05 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 956ff497-068a-3031-99df-ac2cbd776481 | -7.6062 | -43.06717 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f4a18959-5db8-32e6-9a3a-ac6e93b054f5 | -6.12426 | -42.86063 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d9c426cd-c5d9-3679-9210-d776075c2c9c | -6.01918 | -45.41333 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d9e9e40d-33ac-3420-98b1-452d9b75d148 | -10.3954 | -45.39647 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 646d99a6-00cf-3a88-8a30-0189121b9d7e | -8.55636 | -44.63873 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e230ce88-a11c-3c38-9150-a233b7ae192e | -5.88952 | -42.9168 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f87f8b08-41d9-3a68-849d-3fe5add0a386 | -8.85313 | -46.78677 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5266421-3588-3797-a7bd-4b230bb7a2e4 | -10.39688 | -45.41348 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 45317c5c-9748-3a8f-a6e6-dc033239e867 | -5.88572 | -43.70802 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d966e7b5-e90d-3a6f-aee4-39e8fea64849 | -6.55364 | -44.16994 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34938afe-a9e6-37b3-8f21-2f02c7f0fbc5 | -7.70276 | -42.56559 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 04f0bad1-0a65-3c2b-854e-86190af15c64 | -7.12877 | -38.34445 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e4d276f-a729-3d02-8bed-fe5092359caa | -5.99418 | -44.34881 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1804a9b1-32c9-3b16-aad5-9a9c40d7c9a2 | -8.96026 | -44.61245 | 2025-10-05 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ddde422-b2c3-3623-aedb-f56048f87e30 | -9.54146 | -43.03564 | 2025-10-05 03:53:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a5166374-0291-3d47-a04f-90cea3eeaa21 | -6.06852 | -42.6643 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa18c0ba-9f22-36a9-9d32-2bb5888abf3d | -7.14579 | -38.51672 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ba70f01-51d4-3676-a594-4e9d5b6cc72c | -7.77933 | -44.2095 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20f46899-d066-3c3e-9f7d-9ef7492ec2da | -5.40294 | -41.33709 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb9bc47b-79fa-3030-b331-94e00c9a9e18 | -7.79209 | -48.05391 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecc7d742-e88a-3b5f-9a2f-1cc10d43297f | -8.58881 | -46.30746 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| b7f74718-a1fa-3625-acc8-5ffdaed72d90 | -6.63605 | -42.80594 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ada2f88a-482f-3e3e-8ff1-17f630bb42a1 | -8.55727 | -46.26416 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| aba4ad4a-c2be-3784-9aa5-4c1866ced75b | -9.63774 | -40.58337 | 2025-10-05 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 836aa270-1d92-396a-a25f-b1b229c4f549 | -7.47532 | -43.03144 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5384d91b-eb36-36b9-b060-d2fe08dc5e58 | -5.90025 | -44.73823 | 2025-10-05 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd0c8ae5-195a-3382-baa1-79c0d53c691b | -5.29365 | -43.10752 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0db534cb-000a-31d1-878d-80313e4da162 | -5.72438 | -43.84179 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61682465-17ea-350b-a9f9-bc28e74a30a2 | -5.8333 | -42.4537 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2246df8f-cb11-3899-b645-eca8a54e5bc4 | -6.09608 | -43.47927 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23066156-2c65-3eae-8762-cb28fe2bfc4f | -8.54234 | -46.3195 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1d3e2a48-d2ec-3001-b50a-3d1a94e2af4a | -6.10838 | -43.42421 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffb244dd-8a7b-3c4b-af22-acba7a6319af | -7.23839 | -44.89249 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f6712bbd-ac7f-3088-92d9-546701845133 | -10.64227 | -46.34137 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| f668f7ac-453e-3c4f-8bdd-9beac1cdf805 | -9.95657 | -43.77856 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 48a9e831-1aa5-3824-a128-a440de326e7c | -10.2049 | -40.54771 | 2025-10-05 03:53:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| dd2433f7-4a97-32a4-8a27-0e6f41d69b07 | -6.59857 | -44.32189 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62cec370-1b9d-3b67-9318-600515b96905 | -7.69507 | -42.5882 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8481a01d-2a2d-3ec9-9c4a-d649aebb5ef2 | -6.28809 | -43.91985 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e418006-85b9-3047-ad4b-3612212e880a | -6.21319 | -44.07752 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbca9689-d669-3781-b56f-42255c9b00bb | -5.47193 | -42.79259 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2e48c758-8ba7-3a27-839a-74277e2a49cd | -8.86189 | -46.09863 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96151568-eb8b-30a0-98f6-f073b213b6c7 | -8.22979 | -46.81556 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1fe3720f-b4a7-30c2-9eb4-7e4163d88a76 | -8.92606 | -40.70857 | 2025-10-05 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a5cef74-1171-3d20-8ce7-bd4fb6480d3a | -5.83906 | -42.88578 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 25af5bcb-bfe8-387d-bd41-2548aada8ccf | -6.15353 | -44.65901 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d1694ddf-2de6-35ee-a9a6-4f360fa33a80 | -6.71315 | -42.82598 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e9e90766-c722-3022-b647-c2f55c743131 | -5.64627 | -43.91994 | 2025-10-05 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bd024ef1-fdfd-3182-a48e-04699a39c6bc | -10.32874 | -43.7421 | 2025-10-05 03:53:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dcbcf089-45d3-3114-9f34-0efbb9e1621e | -7.47866 | -42.62907 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0a68f31-22d1-3bdf-a4bd-8b3b3eb35b9d | -8.34303 | -49.49873 | 2025-10-05 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e65902b2-2233-34af-82a3-75f945132a58 | -9.25276 | -46.77638 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 536140a0-46e3-3186-9ffe-242b444097f7 | -6.32573 | -41.62863 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fabc2052-53f8-3f1c-80ff-5215322f12e2 | -6.66642 | -42.38116 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a581e132-05c3-330f-8e21-bf67d74f4d83 | -9.95622 | -43.77501 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2099fee-b134-30fd-b056-6bb606177294 | -6.40372 | -47.29432 | 2025-10-05 03:53:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a5a352b-ff73-3fa9-826d-20f9e813eac9 | -6.55432 | -44.16599 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 498b2cc6-596e-3e8e-ad98-07f2466d9a44 | -9.27661 | -45.66829 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35ba25df-3821-362c-8720-197f14f68ada | -3.806 | -51.08023 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79f8aaf0-1366-37b1-a83e-03cd937e1313 | -7.16332 | -46.2126 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df23e0d-985f-3011-a9e5-75b76610453e | -6.24705 | -45.37548 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README43.md)
