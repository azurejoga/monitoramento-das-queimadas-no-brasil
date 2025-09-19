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
| b8ce2c28-6357-3ec9-a18b-b3da13aa8087 | -20.5558 | -43.9954 | 2025-09-19 00:00:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| c30318f1-d29e-385e-beb9-91322aea9923 | -9.4007 | -54.6984 | 2025-09-19 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| ea3cf31a-edb5-32b9-8373-c31e38e2f7dd | -9.4194 | -54.697 | 2025-09-19 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c31eb00a-a2da-3079-898c-9f1beda807b0 | -9.4009 | -54.6781 | 2025-09-19 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 196.1 |
| f9bbeb1d-212f-3430-bfb9-1b74b153d45f | -10.6594 | -48.7092 | 2025-09-19 00:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 90f8b9c2-4508-3a6b-88c4-6bdd63afd1c3 | -22.3457 | -46.7406 | 2025-09-19 00:00:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.0 |
| 6db16ef7-b4fd-3639-91a0-d37d6c07b251 | -6.2547 | -43.9009 | 2025-09-19 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8b9bd86d-b862-32f3-a9c4-0e7f3e11ffd2 | -5.6375 | -45.9481 | 2025-09-19 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0eddcfd5-934b-308a-a40a-9bfb210cddba | -10.659 | -48.7311 | 2025-09-19 00:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9795a888-b1e7-367d-9ecb-e467039adeb6 | -17.2163 | -45.9518 | 2025-09-19 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 55e5e822-24d0-3de4-a50c-57e8aae81d94 | -5.356 | -46.1452 | 2025-09-19 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 2304aa3e-7846-3058-a33b-6e93d3d02033 | -7.5708 | -45.4559 | 2025-09-19 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 9ad92b2a-b639-3da1-b541-16b38802d45e | -11.0904 | -41.0771 | 2025-09-19 00:00:00 | GOES-19 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 21f38723-a1aa-31cc-847f-78a28cf9ce65 | -14.2472 | -51.3505 | 2025-09-19 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0b9f0058-f170-3d9e-a957-ef990afa8475 | -6.2732 | -43.9225 | 2025-09-19 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 9cde3c7f-acdb-34c9-8725-ac84f8548fdd | -14.2666 | -51.3479 | 2025-09-19 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| cb8cc3e2-0b09-3ed0-839a-2a04efff7045 | -20.555 | -44.0203 | 2025-09-19 00:00:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.5 |
| cad08fa2-7b00-3f80-8a9a-39a1b73d236d | -7.8439 | -46.2185 | 2025-09-19 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8155725d-0f54-34a2-87fd-cb2773d28a43 | -9.4196 | -54.6767 | 2025-09-19 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 3d6cd166-9e86-369a-ae2a-da075a271ea8 | -6.2544 | -43.9241 | 2025-09-19 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 3fe59a24-b39e-32b4-b31e-972506ba0251 | -6.2734 | -43.8994 | 2025-09-19 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 600e9684-e564-38ca-91fe-5ef7c1c6f64e | -20.5344 | -44.0259 | 2025-09-19 00:00:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| bcd170db-ebfc-3861-8471-d3037f9ae39d | -7.5705 | -45.4786 | 2025-09-19 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8a32e7bd-66a8-3433-9a60-c9b23e27aefb | -14.2662 | -51.3694 | 2025-09-19 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0724d3a0-2221-359d-a11f-79318bc461b7 | -11.0909 | -41.0524 | 2025-09-19 00:00:00 | GOES-19 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 6091ed0e-1238-3386-8963-b42a9d7ae119 | -5.3374 | -46.1464 | 2025-09-19 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| dd0f7b3f-3d7c-30fb-9567-4511d5c06b29 | -22.3449 | -46.7648 | 2025-09-19 00:00:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 2ed7e360-c360-3cd1-815a-2f8a29bef4cc | -17.2169 | -45.9282 | 2025-09-19 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3829345f-7e9b-3e09-8ea1-313e700966aa | -2.9435 | -49.3443 | 2025-09-19 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| b08de84d-376b-3a5d-b2d9-cfdfe83f5a2a | -8.9344 | -46.3119 | 2025-09-19 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 025078b8-cc3c-33b8-8abe-c712d583ea3d | -17.197 | -45.9324 | 2025-09-19 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 23fc1fa6-6639-3c25-a6a5-bf64b11c2c36 | -17.1964 | -45.9559 | 2025-09-19 00:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 5fb63a26-96a2-3a6c-91d9-7d4889c50ae4 | -20.8052 | -47.2273 | 2025-09-19 00:00:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3db3dda0-425d-3197-9357-d1d38565d261 | -8.1381 | -46.771 | 2025-09-19 00:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| f443c9d5-7e1f-3f25-9479-478c10bc2be9 | -5.356 | -46.1452 | 2025-09-19 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 31d26977-eeff-314f-83ff-0e2fda63e803 | -14.2472 | -51.3505 | 2025-09-19 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 65a4384c-0761-3d8e-b8f8-7e1fa1bebd0a | -17.8773 | -40.1468 | 2025-09-19 00:10:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 147.7 |
| 357cf730-8885-3e87-a83d-8e4c44e38380 | -9.193 | -45.3342 | 2025-09-19 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 94e4f90e-188a-38fd-8627-6493f1b374fd | -17.1964 | -45.9559 | 2025-09-19 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 146.4 |
| b547d541-a017-357c-bf47-a977bab3f316 | -17.2163 | -45.9518 | 2025-09-19 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 7d72b89b-29ad-32e7-8d07-cd1bad7545af | -20.8052 | -47.2273 | 2025-09-19 00:10:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 2cf031d8-28ae-3ba5-9875-cbc9b3d19dc7 | -17.857 | -40.1524 | 2025-09-19 00:10:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| c945c8de-9b27-39d5-b7c4-c13a833567e9 | -9.1741 | -45.3364 | 2025-09-19 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 38843b1e-f0dc-338f-8835-8597be45b6b9 | -8.8801 | -46.138 | 2025-09-19 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| a5f5618f-4fee-3b0e-a423-555451e5526e | -17.197 | -45.9324 | 2025-09-19 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 501126a9-ae82-33be-976d-bbdcaad229b2 | -13.8437 | -59.3588 | 2025-09-19 00:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 6cbb6e13-dc08-377e-b9b6-73896fdb2ece | -9.1747 | -45.2907 | 2025-09-19 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 298.0 |
| 6d53bbd6-9ac7-379b-888b-cb2e1cea0d7d | -9.1933 | -45.3114 | 2025-09-19 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1077.2 |
| 44eec8ff-da1d-3f2a-9864-80a8e88074de | -14.2666 | -51.3479 | 2025-09-19 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 53669901-2cf2-334b-9099-2560375a0388 | -9.4009 | -54.6781 | 2025-09-19 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 4bf8af31-c583-31c9-b7ec-5761077cd5cc | -6.2544 | -43.9241 | 2025-09-19 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 61ef2183-0e65-33fc-a90f-11d5cecdff97 | -9.4007 | -54.6984 | 2025-09-19 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| b586a73f-1c5e-3a12-8ef6-5fe332ceed89 | -8.1569 | -46.7693 | 2025-09-19 00:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 94c07d92-038d-3484-b48b-915b730a8f2f | -22.3457 | -46.7406 | 2025-09-19 00:10:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 8b8f26c1-3b3b-308b-b141-7ca9a13c221f | -9.1744 | -45.3135 | 2025-09-19 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 493.3 |
| 7751cb66-38c0-31f5-806a-33780e852da5 | -20.5344 | -44.0259 | 2025-09-19 00:10:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| 3bed9ce2-0dc9-3a0c-aadb-4c8f61bdce6d | -3.7211 | -49.126 | 2025-09-19 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d3abdcfc-1ce9-3abe-b36a-ef72e48f3200 | -5.3374 | -46.1464 | 2025-09-19 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 0fc05a07-4f19-31a3-bf85-4a647b11fc56 | -14.2662 | -51.3694 | 2025-09-19 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 52bda087-cf1b-3adc-ab0c-0e5a9e994213 | -11.0909 | -41.0524 | 2025-09-19 00:10:00 | GOES-19 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 68.5 |
| f72f2754-69c3-3adf-8319-dd74a0712da1 | -7.5705 | -45.4786 | 2025-09-19 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 1934d770-e7de-3748-a31c-40e0490cec67 | -6.2547 | -43.9009 | 2025-09-19 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 0949a74c-b82d-37bf-8589-bcd34c9c1cda | -9.1937 | -45.2886 | 2025-09-19 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 709.3 |
| 0e42d449-202d-3fd2-8150-41e099b8f48f | -7.5708 | -45.4559 | 2025-09-19 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 1e2e28aa-5d6d-3f75-8f6e-11c7cc7b8aed | -14.2469 | -51.372 | 2025-09-19 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 49e14dbc-734c-3056-a083-648be1700b48 | -9.194 | -45.2657 | 2025-09-19 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8f8e3519-abc6-3cca-9d9d-fa98ed748e96 | -9.4196 | -54.6767 | 2025-09-19 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 244f25e8-6cbb-38e0-80ef-a94f2176ce93 | -5.7534 | -43.3835 | 2025-09-19 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 14ac93ca-824c-3eac-8a9f-d98ac878e985 | -2.9435 | -49.3443 | 2025-09-19 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 07501261-043e-379e-a5cc-50281bc88f42 | -5.6375 | -45.9481 | 2025-09-19 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 1f334332-1ea9-3208-8ee3-6f73d01b6d9f | -22.3449 | -46.7648 | 2025-09-19 00:10:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7d285103-120a-3189-9e4c-99e50601d16e | -17.2169 | -45.9282 | 2025-09-19 00:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1434c45a-e4f5-3623-9740-56037b1b903d | -20.7846 | -47.2323 | 2025-09-19 00:10:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 91dd9210-723d-3605-908a-94a5e585f386 | -6.2732 | -43.9225 | 2025-09-19 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 126ff6d6-46a2-3fd9-af2e-3c08c517268d | -20.8052 | -47.2273 | 2025-09-19 00:20:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3bfb58ba-5139-3d3c-99ba-b7ca22bad1f3 | -5.3374 | -46.1464 | 2025-09-19 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 7c7c58d2-3bdf-3046-baf3-86f029dbe27e | -20.7846 | -47.2323 | 2025-09-19 00:20:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e19c3560-a279-3324-b000-d470d4ace4bd | -14.2662 | -51.3694 | 2025-09-19 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| cdf9472f-5287-3767-8c12-9db407f59071 | -14.2469 | -51.372 | 2025-09-19 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ca827332-cf22-3747-94ae-ef413da6c505 | -20.555 | -44.0203 | 2025-09-19 00:20:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 1c945faa-a692-3837-91bc-13bb5a383135 | -14.2472 | -51.3505 | 2025-09-19 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 206ebc1f-e426-3693-892c-12d67c70860c | -6.2547 | -43.9009 | 2025-09-19 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c0e4c4db-f530-395d-b9ae-4c365bc057f9 | -6.2544 | -43.9241 | 2025-09-19 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 0efb893f-040f-34cb-84f1-702b548aefef | -5.356 | -46.1452 | 2025-09-19 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b84d53ae-7b60-3d35-9132-e44dc34b59bf | -20.5344 | -44.0259 | 2025-09-19 00:20:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| af3cf674-4a5a-36f7-b8b0-e429304789b8 | -5.6375 | -45.9481 | 2025-09-19 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 416fe87c-dc00-35b5-877d-98ce44b40d04 | -14.2666 | -51.3479 | 2025-09-19 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a8515eac-5439-3e52-95d0-d383b6057cfd | -2.9435 | -49.3443 | 2025-09-19 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 5d3f42fc-92b5-348f-bd00-e214d24dd927 | -22.3449 | -46.7648 | 2025-09-19 00:20:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a59bfb74-fe00-3b7d-9ef5-3e36dca374c0 | -20.555 | -44.0203 | 2025-09-19 00:30:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 251107ae-ff82-3436-bc9e-5d395816f989 | -20.7846 | -47.2323 | 2025-09-19 00:30:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6d5ee216-35c3-3d15-b2b5-7824b42a6783 | -20.8052 | -47.2273 | 2025-09-19 00:30:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 97.5 |
| a37f0763-45bf-31f4-ad64-8e231333c508 | -14.2469 | -51.372 | 2025-09-19 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 9f9df75a-2a59-3508-a38a-4a3958ba2821 | -9.1747 | -45.2907 | 2025-09-19 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| f78c088d-8436-3cf9-9d83-9d945ee4c87b | -14.2662 | -51.3694 | 2025-09-19 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| b1d99723-f0ed-3016-8539-60ef63381bc1 | -9.1741 | -45.3364 | 2025-09-19 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 709baa0c-15e9-3d9e-856b-64fc1f438a67 | -20.5261 | -42.3816 | 2025-09-19 00:30:00 | GOES-19 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.1 |
| 47a0202c-cba1-3101-bb81-9da460ea9db2 | -20.5344 | -44.0259 | 2025-09-19 00:30:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| 10a8f309-28bd-3375-9f53-34d228bc308b | -6.2547 | -43.9009 | 2025-09-19 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| bbfaa42f-14ee-3118-81b2-9f24d63d82bd | -9.1937 | -45.2886 | 2025-09-19 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 182.7 |


[Clique aqui para ver as próximas entradas](README2.md)
