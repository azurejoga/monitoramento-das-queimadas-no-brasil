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
| bbbb3640-bb64-3f97-bb4c-05e19aa629df | -8.31223 | -48.05251 | 2025-05-06 00:35:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 612c223d-d642-345c-9c81-c43bae7e6594 | -5.1626 | -45.11001 | 2025-05-06 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| a871028c-2430-3f6c-af32-5046aacc2edf | -6.78871 | -47.59659 | 2025-05-06 00:35:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 86725383-f095-3e73-b769-f76393e3723b | -6.6865 | -42.1252 | 2025-05-06 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| faa44e48-8fa7-3f79-894b-2ff69ef8a0f5 | -14.2257 | -45.4571 | 2025-05-06 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 6c715ba1-3641-3b4c-a18a-b2477f79c7f5 | -6.7053 | -42.1234 | 2025-05-06 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| aa3ec573-14a4-3d4f-b5c4-169a663a99cf | -6.7053 | -42.1234 | 2025-05-06 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 492dd228-4f4a-34af-a5ed-1b651c2b9267 | -14.2257 | -45.4571 | 2025-05-06 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 9fb44f81-abdd-31d3-b9f7-7900a5fbc9cd | -21.3692 | -48.609402 | 2025-05-06 00:58:00 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9dc4b01c-19b7-3ffc-bae2-8088b95d134e | -20.064699 | -49.3591 | 2025-05-06 00:58:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b984f2b3-c74e-3054-ac44-24011099123f | -21.372601 | -48.622501 | 2025-05-06 00:58:00 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c83c8be5-f6f1-3f99-bdec-caa348894644 | -20.061501 | -49.346699 | 2025-05-06 00:58:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b2d68071-7b23-308c-a419-2b35900ea759 | -23.2684 | -55.350899 | 2025-05-06 00:58:00 | METOP-B | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bcba2e9-2131-3c8f-8722-0e71ba83d7b0 | -14.2363 | -45.455799 | 2025-05-06 00:58:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4bbec6c6-acd4-387f-b514-f236acb11cb9 | -12.5578 | -57.7472 | 2025-05-06 00:58:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3dda3aa7-98ae-36ef-af28-063efa608c9a | -21.7311 | -56.099602 | 2025-05-06 00:58:00 | METOP-B | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 81a97eac-e3d1-32c3-851b-c411466338d1 | -23.6099 | -48.993198 | 2025-05-06 00:58:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b095186f-104b-3b12-b4af-d8b2e8f97081 | -14.2267 | -45.458599 | 2025-05-06 00:58:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87dd4e97-8a18-3268-8e23-c8ca308b954b | -23.6129 | -49.004799 | 2025-05-06 00:58:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b835cf5e-7b0a-3607-86ba-6d921981e4bb | -20.067801 | -49.371498 | 2025-05-06 00:58:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a5054b4f-20fd-343e-83de-24696fef274c | -21.732599 | -56.107101 | 2025-05-06 00:58:00 | METOP-B | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a60f166f-8615-346b-8624-94abb1dbe136 | -21.384501 | -50.1078 | 2025-05-06 00:58:00 | METOP-B | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1360324-8e2c-3553-907e-a61488769e65 | -23.2668 | -55.343399 | 2025-05-06 00:58:00 | METOP-B | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 180084dd-d83f-33b8-9244-1b16b4de0aa9 | -23.6003 | -48.996101 | 2025-05-06 00:58:00 | METOP-B | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c236e70f-2a31-322e-a0b3-82c4ef2a477f | -14.2257 | -45.4571 | 2025-05-06 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f45d54ae-e16b-324d-8a2e-3c850d8749df | -6.7053 | -42.1234 | 2025-05-06 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 880988e3-9229-3c91-b253-d47d75e0007e | -14.2257 | -45.4571 | 2025-05-06 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ed23cb81-ccc7-3f6d-ac67-c1e24205788b | -6.7053 | -42.1234 | 2025-05-06 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 2c6d278a-e912-35be-ac5d-3a65985f22fc | -19.7459 | -48.0086 | 2025-05-06 01:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 204.9 |
| b22d7cb1-2050-3b69-bd5c-cb471300b208 | -19.7662 | -48.0041 | 2025-05-06 01:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c8536a8e-3ea7-3a56-ac30-c07af62614c0 | -6.7053 | -42.1234 | 2025-05-06 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| effe78fd-d653-3fb8-a10e-9d6a47d4476d | -19.7452 | -48.0318 | 2025-05-06 01:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 7934a2c3-2438-3b45-8b27-15d531a95fb5 | -14.2257 | -45.4571 | 2025-05-06 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 39742c95-a766-3a67-bd93-1cf8e05de546 | -14.2257 | -45.4571 | 2025-05-06 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1f565c33-c374-3cf1-bfec-cb61310ad5f5 | -14.2257 | -45.4571 | 2025-05-06 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 6fdb9914-8303-3866-9103-fb5cd9ac9207 | -21.735001 | -56.105801 | 2025-05-06 01:49:00 | METOP-C | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6d9c31db-c396-3afd-ab40-e7626e53e61e | -14.2257 | -45.4571 | 2025-05-06 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 871bb55f-af78-3345-94ca-58d3c1322dd8 | -6.7053 | -42.1234 | 2025-05-06 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| cb0b22e1-6222-3887-9a55-3ce0dd3bc15d | -14.2257 | -45.4571 | 2025-05-06 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ad213b1a-dc41-3b51-b669-389498673cd5 | -6.7053 | -42.1234 | 2025-05-06 02:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 9a997c51-b825-304d-83f1-f13a5e2f5cc5 | -6.7053 | -42.1234 | 2025-05-06 02:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 104a0e6f-4fe2-305c-9c95-fd87b241e812 | -14.2257 | -45.4571 | 2025-05-06 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b4dc25c6-0f62-37e9-bcf1-f59d4fce5a4f | -6.7053 | -42.1234 | 2025-05-06 02:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| a9a71512-c85f-3305-a8b8-2e322eff176b | -14.2257 | -45.4571 | 2025-05-06 02:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0ed5b289-d84b-370f-9406-d1e638947345 | -6.7053 | -42.1234 | 2025-05-06 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| f358f52c-d161-3cb4-ab1a-adbc9387b374 | -7.23249 | -35.58751 | 2025-05-06 03:02:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 199b638d-29fd-36bd-9132-ef6079f30059 | -7.23335 | -35.58715 | 2025-05-06 03:02:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5083346f-51b4-34eb-ac8f-e470de2cacfa | -7.23181 | -35.59121 | 2025-05-06 03:02:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfce4de4-f606-3a09-ba7a-1216fcd2ce3b | -7.23269 | -35.59087 | 2025-05-06 03:02:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00b97f0b-ea0e-3458-b32f-5bf25bdd1717 | -10.82219 | -37.16862 | 2025-05-06 03:04:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64a3fc76-821f-364d-aca0-9126b1670799 | -21.1788 | -43.98426 | 2025-05-06 03:08:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2f6a0512-4c81-3996-90b4-9116c586ab64 | -6.7053 | -42.1234 | 2025-05-06 03:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| d2da4a7c-6b3b-325a-9f64-1aaca9c5899e | -6.96914 | -42.80209 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3d1a136f-121b-363e-bfac-c2a1b23b67e8 | -8.86472 | -37.78707 | 2025-05-06 03:53:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e895a832-d58d-336b-a6c3-54887b42f445 | -6.95065 | -42.79417 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| afd5cbf8-c9df-3ffd-a0ed-21cff58fae30 | -7.55358 | -45.87141 | 2025-05-06 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ceb465f-964c-32b6-9e11-258b39c7a051 | -8.07287 | -34.97663 | 2025-05-06 03:53:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f9c2310-a3fc-302d-ab10-73bbe3c719c6 | -8.07898 | -43.13365 | 2025-05-06 03:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| bf448f43-39ae-35e8-9ba7-e4174f14c3f1 | -6.69598 | -42.13292 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 43.2 |
| c2ed8506-bb9f-3841-a60e-968fe0b5c2d4 | -8.07124 | -43.13237 | 2025-05-06 03:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2afad3d5-17de-3458-a3dd-2aa8df2cf627 | -7.55487 | -45.83604 | 2025-05-06 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af9b239c-0146-3837-8d9d-a264b7e06cbf | -6.97073 | -42.79252 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 582c68e7-45f8-3e69-8391-fa04949438fe | -6.70341 | -42.13415 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0c3a4d37-d168-34b1-b6c7-182035849a07 | -8.07595 | -43.1281 | 2025-05-06 03:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| fd5748d8-0a90-3cf8-a022-1cba52d7522e | -6.96993 | -42.7973 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2a0ceff8-baa6-310c-ac08-928eba98e473 | -6.96368 | -42.81113 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11568f46-070c-31af-b508-bfabdf5793b5 | -6.71277 | -47.59459 | 2025-05-06 03:53:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deb3570a-6f65-3f21-b789-d0e3eab78879 | -6.96528 | -42.80149 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5147160d-a5fe-3fd2-be92-e3efa1e4de27 | -6.69453 | -42.12997 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| a09d6eee-3a68-3b6e-a20e-60dd22b9c3a9 | -6.70044 | -42.12907 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9373efd1-638b-34b3-b89d-40f9c2ae557d | -6.96448 | -42.8063 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c140b395-130c-3718-82cd-5da0830a5801 | -8.8603 | -37.79365 | 2025-05-06 03:53:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 174fa9ab-2c08-3791-9f7f-7af3aa27956c | -6.70197 | -42.1312 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 31.5 |
| ccc09b89-3381-3e2a-82ab-164118ff2288 | -6.78747 | -47.59653 | 2025-05-06 03:53:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2ac9bda-680f-3544-9c63-e9c40cea87d3 | -3.26282 | -42.55351 | 2025-05-06 03:53:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c83c48f-b9c3-383a-8f41-9ff1321d4b0a | -7.23427 | -35.5882 | 2025-05-06 03:53:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5d382219-f033-394c-89d0-14d5fa599004 | -4.12237 | -46.67911 | 2025-05-06 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3da9012-1417-31de-a1e1-627af02dcd2d | -6.78805 | -47.59326 | 2025-05-06 03:53:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b57adaeb-3ca5-3726-a797-6a56fcf834b7 | -6.96607 | -42.7967 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0d518be0-2fce-3442-a410-7d79905460a6 | -6.95146 | -42.78937 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 299293c5-0d10-3c51-a9f7-56e09336e40b | -7.5587 | -45.8417 | 2025-05-06 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e85c34e9-db6d-3a01-af00-520060fd853d | -5.16276 | -45.10426 | 2025-05-06 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 53dadf8a-4831-3bba-8cfc-363f2293ccf2 | -6.70416 | -42.12968 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce68fa60-0e65-3885-a069-1095db47e140 | -6.69753 | -42.13505 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 13d955f6-59fc-3de2-961e-763723d60cec | -3.2603 | -42.55342 | 2025-05-06 03:53:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b9321fc-d50e-3dac-bb6a-b7f513ae845f | -6.70125 | -42.13567 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| e6170776-71a8-34b6-924d-250b53600750 | -4.1229 | -46.67599 | 2025-05-06 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a13ea4e-42d5-3709-b97b-299c7bffd7da | -7.55956 | -45.83675 | 2025-05-06 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f013bfdc-20f5-30bf-a67c-292173bdff42 | -7.55271 | -45.87644 | 2025-05-06 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6d16370-a928-3b7e-aa83-bc9a3d3c9425 | -6.96834 | -42.80691 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b119ca93-cb99-30fd-8d07-6b2eafbce759 | -8.07511 | -43.13301 | 2025-05-06 03:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 2bc62717-d008-3f32-b4cb-1469a02a34d4 | -6.71756 | -47.59862 | 2025-05-06 03:53:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 082342e6-d914-3427-b3d6-e0d9741a1a77 | -6.9553 | -42.79003 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 17b77cce-17ca-3f67-9e13-fbe008c36de2 | -5.16194 | -45.10906 | 2025-05-06 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 23cea136-1f8b-309f-931d-8697dff69269 | -6.23062 | -36.52354 | 2025-05-06 03:53:00 | NOAA-21 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e12a2e0-54c5-323c-9fac-9e7627fcb4ae | -6.69825 | -42.13058 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| f1a99be5-5894-35c3-8825-9a07868bd226 | -6.95611 | -42.78522 | 2025-05-06 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d900684b-08c8-3854-b334-6e38f1ff1f56 | -6.6997 | -42.13353 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 43.2 |
| ce952bd5-39dd-39cf-b1d3-4d0f7965d60f | -6.69381 | -42.13444 | 2025-05-06 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 603d0cef-4b5b-3b07-b845-9d009de75a86 | -8.20247 | -48.98853 | 2025-05-06 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README3.md)
