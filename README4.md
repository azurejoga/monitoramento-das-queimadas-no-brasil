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
| 7bc4d83f-ca8f-370e-a97e-5fa19c47b259 | -11.6798 | -43.4446 | 2026-09-22 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 620faa5f-bc51-3f70-8d9c-142336015949 | -6.467 | -59.9902 | 2026-09-22 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 17221008-1e81-3abc-9515-47bfef5bb739 | -6.4671 | -59.9711 | 2026-09-22 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 33e05e02-24b2-319a-a2f5-063af8d44200 | -7.5889 | -57.6757 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 0a79d902-73db-30a7-83ee-b5173833a5bc | -18.727 | -46.9345 | 2026-09-22 00:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 25b73fba-ad77-34fd-a39a-6e3199db7170 | -7.5704 | -57.6766 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| b5574297-f321-354b-9ea0-f826c5d389fc | -7.5888 | -57.6953 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 745b1e0a-804e-3bd9-afef-6978b4594b47 | -13.2791 | -51.7737 | 2026-09-22 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 69559589-7aef-323d-ac40-87d7eb67a08f | -6.0925 | -57.6847 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8f44db2e-6c2a-3a0d-b83f-6f69a53bd877 | -2.8608 | -57.7994 | 2026-09-22 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 45c1fe2d-4e81-3f40-ade7-d72dd4856a23 | -13.2983 | -51.7713 | 2026-09-22 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 17eb37db-521a-380c-930e-4dfef895ac89 | -2.8791 | -57.799 | 2026-09-22 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a4f1aaa6-186a-3d17-8ef3-e227c4367353 | -5.7756 | -45.0826 | 2026-09-22 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 6cbdf07d-aef1-332d-87c8-0ea51314845b | -6.0549 | -57.8227 | 2026-09-22 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| ea629bd6-eb8f-323e-b5fa-e43782ecedef | -11.3255 | -54.0487 | 2026-09-22 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 44e4618b-9c69-3d03-8458-0745c22a9c55 | -5.7382 | -45.0853 | 2026-09-22 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 7553d7b9-76bd-3069-929d-f3be136a6342 | -3.3492 | -59.867 | 2026-09-22 00:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8072b881-2891-35de-92a5-ab5c3b69ef4c | -5.7567 | -45.1067 | 2026-09-22 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| f9bd694a-7c11-3075-820d-481cfa2b0cdf | -5.9333 | -59.9899 | 2026-09-22 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7173168d-c163-37ac-8614-4990aecf5e0c | -8.8275 | -50.482 | 2026-09-22 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6a39bd4d-454c-344e-9710-c7ebef7e1abe | -7.326 | -55.5953 | 2026-09-22 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| c77437c2-6844-3ea1-8fc3-6f1ed5c5c928 | -11.6793 | -43.4684 | 2026-09-22 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| c50cdf8a-6641-33c7-9f5c-e9283d8b03c9 | -5.8054 | -43.8438 | 2026-09-22 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 58bb2389-6472-34e0-aa67-21cafaf1f293 | -11.3068 | -54.0299 | 2026-09-22 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8d49329f-6893-3903-8040-c85bec1af673 | 1.5284 | -55.9045 | 2026-09-22 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 06ed825f-992e-34bb-beb7-984be9036bd7 | -3.0542 | -54.4081 | 2026-09-22 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1deedf15-1254-39f0-9358-05ab00f340f9 | -6.4485 | -59.9909 | 2026-09-22 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| d9eb8335-d8d4-3a59-8a00-764ef1c329b3 | -9.257 | -46.1873 | 2026-09-22 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| bbe1a59b-f73f-3f57-9845-9794c3d61d80 | -9.2576 | -46.1422 | 2026-09-22 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 569.8 |
| 16df59b5-3ce9-3be6-9968-20066093f7db | -12.9461 | -51.0481 | 2026-09-22 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 7c0981e7-8477-3482-9c4a-65f8f0b9ef23 | -11.7672 | -50.8253 | 2026-09-22 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 43ebfe45-afd8-32aa-af95-fc5bd18b95d7 | 1.5468 | -55.9043 | 2026-09-22 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 4779ee57-35db-357d-91b2-c8750fd7e3cd | -5.7571 | -45.0613 | 2026-09-22 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| c01a3e57-dd9a-33d2-beaa-d50e87198434 | -9.2386 | -46.1443 | 2026-09-22 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 22acfcc2-87cf-32b3-8977-84c754dd8a9c | -18.727 | -46.9345 | 2026-09-22 00:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 634b4971-a331-3b12-b5ff-4a8e33fc144f | -5.7567 | -45.1067 | 2026-09-22 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 3e943085-cd67-310f-9b85-85e998c3ebdd | -6.0928 | -57.6262 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 74e9bc98-23f4-3197-b390-a59f7ce9cb48 | -4.2951 | -49.1234 | 2026-09-22 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 05cc18a9-a182-3ce2-81f4-96572b8b9bdd | -9.2762 | -46.1627 | 2026-09-22 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f44e51d1-ad5c-3675-86d0-b7c3b71d8f37 | -2.4206 | -58.2712 | 2026-09-22 00:50:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 396bbff0-c02c-348d-b3e6-468ac51f23a3 | -11.3257 | -54.0282 | 2026-09-22 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| b9271e9b-f5cc-36f9-afbd-c120720a53fa | -3.0726 | -54.4076 | 2026-09-22 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 38832950-e24d-36e2-96c8-9b5f94f79777 | -12.165 | -47.3948 | 2026-09-22 00:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c9e48844-b102-340f-b715-d7e90b155d7a | -7.5888 | -57.6953 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b50dc3b4-7260-3ee8-93bd-45e613ddae1c | -12.1458 | -47.3974 | 2026-09-22 00:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 9bbc9f5b-60b6-3761-b636-e597e7da6b78 | -5.738 | -45.108 | 2026-09-22 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 34b51cd4-20c5-304b-8e10-b856136a5d0f | -11.7675 | -50.804 | 2026-09-22 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 204130e7-647a-33b7-b244-ff519537adf1 | -12.8056 | -54.0462 | 2026-09-22 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 99f5e94e-62ed-351d-95cd-0d1e822d19ca | -7.5889 | -57.6757 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 0f20da63-29e3-3214-970d-5c98ebbe35fb | -8.7916 | -44.2778 | 2026-09-22 00:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 5f4a3b68-452e-3635-8c3c-1c9b6f7694f7 | -5.8052 | -43.867 | 2026-09-22 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 6ddfd30b-48a4-39f1-9bfa-a3adff76f2d9 | -6.0549 | -57.8227 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0c08eff4-0eeb-3b1f-aa46-4ed77945e870 | -12.8059 | -54.0255 | 2026-09-22 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d9430e57-4961-3c04-bb49-b2fd0d64437e | -11.3255 | -54.0487 | 2026-09-22 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| ec82bf67-0db6-3b59-9bcf-4110b60cd6a6 | -6.0365 | -57.8235 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 10d53d83-0e00-38e7-a468-ae6c6b2131cf | -5.7756 | -45.0826 | 2026-09-22 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f72b3041-9a78-39d3-a4c7-f84d87068eaf | -12.7868 | -54.0275 | 2026-09-22 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 595a5993-93aa-3f9d-8f14-97cda7e2f8a0 | -3.3867 | -59.5223 | 2026-09-22 00:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| e4691135-87ae-3d6d-a833-c56a1327f6bd | -9.2383 | -46.1668 | 2026-09-22 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 236.9 |
| dd3fa63c-fe63-3c0a-8827-4454357998f9 | -5.7382 | -45.0853 | 2026-09-22 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 41887d7d-39d3-354b-9ea5-34843f678d1f | -8.8275 | -50.482 | 2026-09-22 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b6836fbc-95c9-3f7e-9556-c77baf4a5514 | -11.3066 | -54.0505 | 2026-09-22 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c3f0811c-ca4a-3b50-945f-3b1f34d3a2e1 | -7.5704 | -57.6766 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dae6e1bb-1d50-30cb-ae0d-92dcbcf50678 | -5.7864 | -43.8684 | 2026-09-22 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 6818f756-9b2f-3a34-9192-ea2533fd58f4 | -6.571 | -44.1516 | 2026-09-22 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 421af3fd-4ff2-39a6-ab2b-68df1a4f86c1 | -6.5898 | -44.15 | 2026-09-22 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d8001c2c-18c4-3aed-aaad-ab296a8ac6ac | -8.6169 | -54.6328 | 2026-09-22 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e7b3c60a-60e9-35e9-9933-d341070b7043 | -11.6793 | -43.4684 | 2026-09-22 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 512104fd-e186-3e0d-90c8-6ce5e07da293 | -5.7569 | -45.084 | 2026-09-22 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 359.4 |
| c1094ab9-2887-328e-924e-3057737bccfb | -5.9334 | -59.9707 | 2026-09-22 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 71afa151-15bd-33be-a456-50ae1455294c | -5.9333 | -59.9899 | 2026-09-22 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9d9071cc-5de2-316a-a81c-bf0a95b1053f | -9.2573 | -46.1647 | 2026-09-22 00:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 743.5 |
| 51153f2b-a05d-3afd-a3c5-12c258f1e8c4 | -18.7472 | -46.93 | 2026-09-22 00:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 144.8 |
| b65cb2fa-71b2-374a-a075-9a49339f2f84 | -6.1109 | -57.684 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e0b9c796-f1e2-3232-b073-af22af1cc911 | -12.7865 | -54.0482 | 2026-09-22 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3420af53-77b2-3588-b1db-ea13939924e8 | -9.5594 | -66.0359 | 2026-09-22 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| b4928a60-1a38-3dee-bd15-3b184d98bb1b | -6.0925 | -57.6847 | 2026-09-22 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| ef3fb197-5af1-3e69-ba62-91fbbd1b056c | -3.3492 | -59.867 | 2026-09-22 00:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| f7cb8f5f-cfe7-3554-98f6-33b0d576787c | -11.6798 | -43.4446 | 2026-09-22 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 6c79fd41-8b5a-3f15-8892-ca6c2a4f3e92 | -2.8608 | -57.7994 | 2026-09-22 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1c8c0cc6-d2c6-3f13-aa44-34907edfc59e | -6.467 | -59.9902 | 2026-09-22 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 0f4ed185-27f1-3c33-9884-7b264fe8e8cf | -3.1135 | -60.684101 | 2026-09-22 00:57:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e97f090b-a8ea-30f4-ba0a-da67ef411264 | -9.6701 | -54.331001 | 2026-09-22 00:57:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c146e69-4c0b-38cf-9ae0-287be09d8c61 | -2.3966 | -58.274899 | 2026-09-22 00:57:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00a2be5f-f3b7-3f54-911a-2bc0d7dd0f62 | 1.5412 | -55.897099 | 2026-09-22 00:57:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b591e7-2d52-3c52-99d8-f188caa85e55 | -6.1602 | -59.940498 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eee679a5-a35c-338c-ba4b-ea806d9812fa | -10.4111 | -50.350201 | 2026-09-22 00:57:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21dc7167-01d6-3c6f-a20e-46f125090a29 | -7.3258 | -55.587299 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d7b4f2-257a-39cf-96ad-b4f08d24fb4e | -9.5642 | -65.998001 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16047439-ee0a-3f78-b76c-9c5405559444 | -13.2807 | -51.781502 | 2026-09-22 00:57:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2309db23-bc51-39e0-965d-6345fac332d8 | -8.5947 | -54.6133 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a19d7745-dfd2-34ff-9008-6b1b49edbbf8 | -4.9497 | -55.812599 | 2026-09-22 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72319fbf-ee6c-3865-9231-2c10fd7e12a2 | -6.4237 | -59.9655 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9181b406-3bcc-37f9-a2db-91db02d6721c | -3.4899 | -59.176899 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33f7f1bc-b9b2-323c-b87d-29377a31c3aa | -5.4548 | -60.147499 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e758b2c-4d0e-3b8a-911f-4abbc94468e2 | -3.1789 | -61.197498 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca2164c-4890-3af3-b726-b18b57b4dc3b | -4.2524 | -55.429699 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54df327b-7f59-36df-b9ee-fd9f9520cfb0 | -5.8034 | -57.731899 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5bbe3e6-1d9a-3452-8d36-121df5757725 | -3.0708 | -61.266201 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b84874f-38a2-35e9-990e-71f251f2d513 | -3.3663 | -61.296101 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
