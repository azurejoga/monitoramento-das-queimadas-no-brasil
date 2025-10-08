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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09c7ff7f-09e3-3813-a35c-8a5cd1eece3c | -13.3245 | -48.0101 | 2025-10-08 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 8edfe96f-1b8e-3147-afa4-05338017efcd | -14.2564 | -45.8449 | 2025-10-08 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 82349ea0-b080-3f2f-bc69-7f7c1699e810 | -14.7184 | -46.0636 | 2025-10-08 13:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 148.0 |
| efe011b2-df63-3f77-a3d4-0b7d184a640a | -8.9306 | -46.6033 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 868ee99e-fdab-31be-bd8a-9fdc216a222f | -11.0265 | -50.8854 | 2025-10-08 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2990d55e-3cf7-338f-bf91-89909a1dbc87 | -12.4267 | -45.6136 | 2025-10-08 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| acb1aeb8-468f-38e5-868c-db6406fcc92f | -10.7472 | -46.6409 | 2025-10-08 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0680ac82-344d-3068-864e-96ece65532ad | -13.7364 | -45.68 | 2025-10-08 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 232.1 |
| 6106fb75-16d0-37ee-9f35-0e9c4e515f9a | -13.7918 | -45.809 | 2025-10-08 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| beb4baa3-c07e-353b-be1c-6f736d892a26 | -12.3655 | -50.3049 | 2025-10-08 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 95e589e9-7545-35cf-9500-13b5b7d6ac17 | -8.5016 | -46.2669 | 2025-10-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 426.0 |
| 2474a22f-3d87-3396-a35a-630746d4e109 | -13.3517 | -47.5818 | 2025-10-08 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| bad06b69-b43d-3afe-997f-9e50c3232816 | -13.3211 | -47.1596 | 2025-10-08 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f2e31462-57ae-3aaa-ba02-e407d05943a5 | -10.9106 | -47.1353 | 2025-10-08 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| c515f606-aee1-30b8-8a99-78f8deb29d34 | -11.9331 | -46.4153 | 2025-10-08 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d52f6d66-3958-3574-8b71-89e2f245b069 | -13.7548 | -45.723 | 2025-10-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 500f13f4-5b16-33a6-947f-34c0fdb8cf5f | -13.0009 | -46.7795 | 2025-10-08 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 10dc878a-a6ae-3bf4-8e37-d885e879e87f | -13.3048 | -48.0352 | 2025-10-08 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 40b68b1c-5ce9-3413-9588-21a2f1ee2a9a | -7.7203 | -42.4023 | 2025-10-08 13:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 544e7680-e66d-3208-905f-1e4b6c58b2be | -8.5398 | -46.2181 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| d60bed96-a608-3997-860f-d275a1377fd3 | -14.7179 | -46.0867 | 2025-10-08 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 345.6 |
| f3d3ef8f-98a7-3f4c-9a7c-1790003d2783 | -11.9523 | -46.4126 | 2025-10-08 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 175bd933-7e85-3849-a81e-16a4e5fbd5c3 | -7.8307 | -44.1497 | 2025-10-08 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 03418519-5cea-3cdc-823d-2ea284919cea | -7.7922 | -44.2229 | 2025-10-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 09cb121e-3ade-30f4-aedb-71628e8138f1 | -13.7738 | -45.7429 | 2025-10-08 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 8a302ba2-a8f4-371e-a410-35f0edad8fb7 | -14.7184 | -46.0636 | 2025-10-08 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 175.4 |
| ce6ab224-6164-39fd-b921-b5b3cf6b9677 | -13.2855 | -48.0381 | 2025-10-08 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ce9ebe01-ce6c-37df-8a13-7a2674b0fd4c | -8.4824 | -46.2912 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 4de28015-8c9f-3662-8e42-f96c0bfbde27 | -12.0122 | -45.1929 | 2025-10-08 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| dc050041-1431-3415-85d3-d9df8e5f1acd | -10.0692 | -50.4094 | 2025-10-08 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bd0ad942-a392-3a5f-8f80-5394aad791b6 | -11.2436 | -50.2645 | 2025-10-08 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 59400e9e-b106-37c7-8ca4-43a9ae9ac350 | -11.1482 | -47.7503 | 2025-10-08 13:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 11e5a61f-f06c-39c5-a448-a87f7c227a1b | -10.4245 | -45.3907 | 2025-10-08 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 30d365dc-d490-3f5d-be03-8e675a89a022 | -11.4678 | -43.5011 | 2025-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 67e543a7-7176-3ebf-9a65-b65897fb7671 | -13.7368 | -45.6569 | 2025-10-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 184b9b03-733e-3609-8af9-2428baf0d9be | -11.4682 | -43.4774 | 2025-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 7e2e2abf-37a9-3dfc-813b-895b8c50f45e | -15.321 | -46.1622 | 2025-10-08 13:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| fddc3af7-d23f-3f83-8a97-621585d3fed1 | -7.7924 | -44.1998 | 2025-10-08 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 1840686d-db67-3cbb-b83c-f33645745f4b | -7.7932 | -42.6082 | 2025-10-08 13:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| a800936f-d776-31ea-8b4d-4e6fa50ce6e1 | -12.5109 | -54.714 | 2025-10-08 13:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 227134db-9e1d-3711-a7ab-1eeb1908d605 | -11.487 | -43.4981 | 2025-10-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| bd81ec82-98fe-3290-89b2-f5378a3d47f9 | -8.9005 | -46.0233 | 2025-10-08 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c6a73f22-1a83-3c4d-b2be-873164ffaa6b | -8.5584 | -46.2387 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a87c18cc-46f7-3451-808a-dfe3255cd8c6 | -7.4857 | -43.0655 | 2025-10-08 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 9518d92b-f813-3138-a867-08af3bebd2fd | -12.5107 | -54.7345 | 2025-10-08 13:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 5540b838-8cd6-3744-a1de-dfb43972bb28 | -7.7927 | -44.1767 | 2025-10-08 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 18acf9c8-06a9-3eb0-a8d7-5cd70779b056 | -11.7043 | -46.3794 | 2025-10-08 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 13d22fdf-f365-351c-8cca-be6ce76ed56e | -18.0394 | -44.9438 | 2025-10-08 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d2a6b493-7d73-32e8-8fab-39f22acc4597 | -7.4666 | -43.0909 | 2025-10-08 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| 2647140b-2a4a-3f6e-a29d-ef6f9ce1ebc2 | -11.4153 | -50.2023 | 2025-10-08 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8495a9bc-a89a-3c8c-98b5-92bc2440a648 | -8.9306 | -46.6033 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6934c7c5-038f-3f01-a67d-22f3f56a074d | -8.5395 | -46.2406 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| ba589ef1-681e-33e6-974c-f02f87fede0b | -14.6983 | -46.0902 | 2025-10-08 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c5f0f819-e894-3961-9e12-cc17f9ea04e9 | -8.5207 | -46.2425 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 1e126c5a-d520-366e-8553-c1752909ded3 | -7.4669 | -43.0674 | 2025-10-08 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| f2668ceb-f284-31da-8726-3294500b0ac2 | -13.3706 | -47.6013 | 2025-10-08 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 94b6b39d-200a-36d6-8c10-a8142659a769 | -11.7047 | -46.3567 | 2025-10-08 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 7b212371-4992-3b40-ae02-06cdc508cd20 | -12.4916 | -54.7364 | 2025-10-08 13:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 78d07918-77e1-3e58-a8da-6bf3b4b5bd6e | -8.9121 | -46.5829 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c123e862-9135-3051-b613-3fa924922d58 | -13.3245 | -48.0101 | 2025-10-08 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 76369f32-dbfe-3eb3-bfa0-b6fba1cc54c3 | -7.7392 | -42.4002 | 2025-10-08 13:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| c1193797-db97-3596-850a-96f6519fd0f4 | -17.304 | -58.0566 | 2025-10-08 13:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 66deb463-2f66-3d56-8114-42b31f114245 | -13.3967 | -47.2382 | 2025-10-08 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 0ba83dbb-f65a-31e1-b420-d949e3af26b7 | -13.3018 | -47.1626 | 2025-10-08 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 145.6 |
| a2d8c690-ec71-3ab0-aa81-8b37a230b4d2 | -13.8117 | -45.7826 | 2025-10-08 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 64f104cb-4e73-3874-ab1d-9322e0152c0b | -12.2525 | -47.8728 | 2025-10-08 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 6d3c0178-a6d8-35ed-b210-79137d962c53 | -10.7472 | -46.6409 | 2025-10-08 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 5afe86c4-5318-3d8b-bcbf-eb3442e19c58 | -10.8919 | -47.1153 | 2025-10-08 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8957af5e-ddbf-3bf0-9954-246e0b97f482 | -14.2564 | -45.8449 | 2025-10-08 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 44fd0714-21c9-3734-b551-345935e6afa9 | -9.6795 | -49.9355 | 2025-10-08 13:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| feb42df2-f08a-39c9-bffe-ee5233777db1 | -13.2434 | -47.194 | 2025-10-08 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| dabdf685-7f99-3321-8419-d77448df4db7 | -12.2528 | -47.8505 | 2025-10-08 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ce95c3ec-1185-34e4-973b-621ebc26b36a | -7.5463 | -44.3164 | 2025-10-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 00c93f1c-56b2-3e6e-a918-f110412d2b6b | -9.2096 | -46.9084 | 2025-10-08 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| cc87d5a7-dc16-372f-8a27-8699cd443b5c | -7.777 | -42.3961 | 2025-10-08 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| ce07c3d5-f879-3054-a0a8-d44a3acf3aaf | -11.785 | -45.0421 | 2025-10-08 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9ee0c389-07ca-361d-81f8-5de0d88ba769 | -13.7918 | -45.809 | 2025-10-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 02880aa0-9490-3dde-8ed5-8eb0e2b1a099 | -8.9309 | -46.5809 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 955e8ee6-efaa-3a6b-8579-e82924065160 | -13.2847 | -48.0827 | 2025-10-08 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 0ad51024-80fb-3e1b-999b-445db439211f | -8.1804 | -43.3445 | 2025-10-08 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| 8f0fa810-3ac3-3c0c-9ce7-932ee5e7e742 | -13.7733 | -45.766 | 2025-10-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4f295916-79fa-3b2b-9ce3-f035cf39c2df | -13.3778 | -47.2185 | 2025-10-08 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8467a881-d183-3d61-91af-7bdc42378d45 | -12.0118 | -45.2161 | 2025-10-08 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f4b4d148-ba3b-3ed6-9fc3-6c6350e121c5 | -13.3517 | -47.5818 | 2025-10-08 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 955a117f-bced-3c2b-a97a-09417e41bf3a | -8.1007 | -39.4489 | 2025-10-08 13:40:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 18d59e52-0d60-366e-b198-635de573e46a | -8.6106 | -45.102 | 2025-10-08 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 178.5 |
| e2d4df30-c3f9-3a64-adad-ef2bdf7e19f4 | -13.3774 | -47.2411 | 2025-10-08 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8c606ad8-3e0b-35d9-b119-6b137f6073c1 | -13.3513 | -47.6042 | 2025-10-08 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 3aa6da1e-b614-39ce-831c-68088843c3c6 | -12.5297 | -54.7326 | 2025-10-08 13:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 07e7bb6d-599d-36ec-b206-db9d96dfe96b | -13.7364 | -45.68 | 2025-10-08 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 393.2 |
| b7e21f69-ae4b-380d-8393-05b870826e93 | -10.7468 | -46.6634 | 2025-10-08 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ad8950f5-a387-34b3-9144-c31fce2cbb73 | -14.3889 | -46.0063 | 2025-10-08 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 7847fbb2-e37d-3419-9b25-0fa4491beedb | -9.1899 | -49.9818 | 2025-10-08 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a1b2533f-ff63-3aec-926f-8e757ab50639 | -13.304 | -48.0798 | 2025-10-08 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4a372cd1-0650-3ef6-a02f-873a2abf68bd | -11.1168 | -49.8492 | 2025-10-08 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 501f032f-7a1f-332a-8a1e-1d56f0163ee7 | -11.0982 | -49.8298 | 2025-10-08 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6fd58779-1d83-310a-9d4f-866162b0a2f0 | -12.1833 | -50.9905 | 2025-10-08 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f5a53585-6d3b-3e28-8574-1ce1cd6c1c39 | -8.4636 | -46.2931 | 2025-10-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 891de5b5-1369-3399-bc26-02d4c6e7616f | -14.2559 | -45.8681 | 2025-10-08 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 4c10096a-6d61-3152-bbb9-9c9f43f27ee8 | -8.1807 | -43.321 | 2025-10-08 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |


[Clique aqui para ver as próximas entradas](README106.md)
