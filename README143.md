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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec89d81-a333-3987-8c0b-bfb08d78c35a | -17.42438 | -44.87982 | 2025-10-03 11:42:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| cb6ac5e1-706a-3074-bd27-1154af27e6ea | -17.63452 | -44.45949 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| cc1561fc-c48e-3f32-84af-7d67fb40b173 | -17.96735 | -44.40018 | 2025-10-03 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 3e2924ee-bc31-32b2-bbbb-444c3e1deab3 | -11.9151 | -46.3499 | 2025-10-03 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f31a078c-5f1b-37a7-865f-dda5810f5fe8 | -12.5301 | -47.3213 | 2025-10-03 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 6e00011d-b8d5-3e75-9786-a15389720bef | -9.8991 | -43.7237 | 2025-10-03 11:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 75944b67-e557-3b36-89e2-aefe3fc9639f | -12.6131 | -46.9725 | 2025-10-03 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 6278d04f-4bb4-3378-9815-a0ea59a426e9 | -11.9155 | -46.3272 | 2025-10-03 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 5c386fe6-310c-3799-9da4-756db6273035 | -12.6319 | -46.9923 | 2025-10-03 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0e224705-1199-3c51-baf0-d20ef4ee8d30 | -13.9775 | -48.157 | 2025-10-03 11:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 48edfd0f-d92e-3b25-9cb3-9835c8bd55a2 | -10.9483 | -51.0634 | 2025-10-03 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 0c74d684-a249-39c9-8872-ceaf28320521 | -14.2939 | -45.9076 | 2025-10-03 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0248bf06-a588-3a4e-ada7-24cf0cb0c519 | -9.9962 | -50.2248 | 2025-10-03 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 68563673-e838-3f5c-af8c-34b2935402e4 | -12.6135 | -46.9499 | 2025-10-03 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 71f31060-eb8f-3897-ab2e-553c304a4b80 | -8.8343 | -46.7694 | 2025-10-03 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| df1b32d0-39a1-3ae6-bb6f-b1c204c19fe2 | -13.9771 | -48.1793 | 2025-10-03 11:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 38e51c75-d548-307a-a667-1cffe7a27ce1 | -9.9959 | -50.2462 | 2025-10-03 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e2e3e4ab-41e1-3ca2-b665-f28d6ad985b6 | -9.9965 | -50.2034 | 2025-10-03 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| aa9fa778-2479-38c9-a869-dfc9d340246f | -12.5305 | -47.2988 | 2025-10-03 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 1c4cbcd8-ac32-3435-98e9-aee4b28f1dec | -12.6323 | -46.9697 | 2025-10-03 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 4c065448-18db-3799-892a-e684d38754b0 | -9.9182 | -43.7212 | 2025-10-03 11:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 0cc076de-eef3-3280-806f-7bf090903f13 | -11.9159 | -46.3044 | 2025-10-03 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| c2d18484-a7e7-3d54-bba7-a7908da94017 | -13.7666 | -48.0777 | 2025-10-03 11:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 3b089458-c8e3-3ba1-bb8e-4094cf8c4164 | -12.6127 | -46.9951 | 2025-10-03 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 25817867-666a-351b-867e-28e0d851f4b4 | -12.6131 | -46.9725 | 2025-10-03 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 266f4829-ef51-3337-b4ea-9e820057d48f | -8.8343 | -46.7694 | 2025-10-03 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 51d795b1-f937-31ca-a7f7-f378226e8f6f | -10.9483 | -51.0634 | 2025-10-03 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| eb7005a6-f207-3bd0-8678-e738df69900f | -12.5301 | -47.3213 | 2025-10-03 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.2 |
| d5dcd8eb-72ea-3a80-8fc4-2b86a0ce25e6 | -16.0583 | -51.0454 | 2025-10-03 12:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 939c97a8-76ed-3b2c-8873-a208c52bc6cb | -11.9159 | -46.3044 | 2025-10-03 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8c4dd36b-91fe-348f-836e-61b8758f53ca | -9.9182 | -43.7212 | 2025-10-03 12:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| bf51a17f-159c-3e42-9bd5-1dbd2c991926 | -7.7494 | -46.272 | 2025-10-03 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b81c7786-14f1-3032-a23a-fb14c36dc229 | -12.6323 | -46.9697 | 2025-10-03 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| dce21c06-489d-3bd7-b10c-e1bd54917a3a | -9.8991 | -43.7237 | 2025-10-03 12:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 81af5907-0569-3af4-bae8-87de051345b6 | -12.6319 | -46.9923 | 2025-10-03 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| f78fe9f3-5356-379d-80d9-c78c905c10ec | -11.9155 | -46.3272 | 2025-10-03 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 92687ac7-31c9-3ab4-84cf-1bbd3df59d2f | -12.5305 | -47.2988 | 2025-10-03 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| c3438eda-f958-3754-a7cc-6f406ad451fa | -7.7496 | -46.2496 | 2025-10-03 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| eaff7d91-2051-3cfb-9b2b-1ee27d0f7403 | -11.9167 | -46.259 | 2025-10-03 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0edf7e80-bb61-3f08-a9bf-784f68153ca2 | -11.9151 | -46.3499 | 2025-10-03 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| d700ba5a-679a-39f1-bef6-797df9302596 | -14.4236 | -47.1422 | 2025-10-03 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d04d2e09-e9d0-3224-b3cc-2ff8d941d4e7 | -12.6323 | -46.9697 | 2025-10-03 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 14a4cf58-c0ec-3be9-9219-d4736eb44e53 | -8.1702 | -44.1377 | 2025-10-03 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c9da64df-e2f1-3d96-b81f-450765dc5d10 | -14.426 | -46.0919 | 2025-10-03 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 2a8fd798-10b5-33ab-b34c-2f0b97153568 | -9.9182 | -43.7212 | 2025-10-03 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 164.6 |
| b5f34944-ab22-3cdc-ba45-c023d9c5d459 | -10.948 | -51.0846 | 2025-10-03 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4cc74d10-70a3-3d53-b178-fa7cceab1401 | -13.3422 | -48.0965 | 2025-10-03 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 65537ddd-7ae9-3ab4-bf1a-f364fa7b662b | -11.9159 | -46.3044 | 2025-10-03 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 714ede62-a716-3501-ae36-b0ba8a61ffee | -7.7494 | -46.272 | 2025-10-03 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.1 |
| f1e0c788-eed6-3f42-b456-b7c17820d99a | -7.7682 | -46.2703 | 2025-10-03 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 16d1983d-2459-3f8b-b483-d85fa291fa36 | -12.5305 | -47.2988 | 2025-10-03 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a17554ac-76fe-334f-9d81-9dfded1e52a0 | -13.3414 | -48.1411 | 2025-10-03 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 299db059-e0ce-3474-a355-9b658a20b356 | -12.7435 | -50.5591 | 2025-10-03 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b468e407-e227-3a8c-98d0-fe4e416beb3e | -13.1152 | -47.8848 | 2025-10-03 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5e010cb2-c7b7-3a38-a01e-bef1ae79c990 | -9.8991 | -43.7237 | 2025-10-03 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 73fc8659-e22b-35b7-af22-6da7d6f29f84 | -9.8995 | -43.7003 | 2025-10-03 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| ca7417ae-1f5e-3020-a87c-61a82297c4f8 | -13.7666 | -48.0777 | 2025-10-03 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8b5f2278-418c-3570-a71c-3d1fbc0f1001 | -9.9186 | -43.6978 | 2025-10-03 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| de4483b5-e080-30fb-ab15-5119534efef8 | -16.0583 | -51.0454 | 2025-10-03 12:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 122.6 |
| f3828f6c-4bf8-359a-b4be-a547c1c42570 | -13.1973 | -50.9095 | 2025-10-03 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2b9371bd-6049-390b-9b47-c59c6b15c572 | -11.8963 | -46.3299 | 2025-10-03 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4bc738b3-50b6-3a32-8bab-4a95b14bcc89 | -12.7627 | -50.5567 | 2025-10-03 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 583dde5b-79a1-3f67-a64b-30455c9a2eab | -10.9483 | -51.0634 | 2025-10-03 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 162.3 |
| d107bd31-ef1b-3960-b20a-210dd2ffa068 | -13.3418 | -48.1188 | 2025-10-03 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| aa83fa35-7315-3e55-a7a0-f490cab2a25e | -9.9394 | -43.5777 | 2025-10-03 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| bba8bae4-44fb-30e0-83ba-a544e3fa1e2d | -11.9155 | -46.3272 | 2025-10-03 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 16b07856-b825-3aa6-9454-110f959c65d6 | -7.7496 | -46.2496 | 2025-10-03 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 8016a7a7-e04f-36a1-8ce8-f0733e6597e1 | -8.1699 | -44.1608 | 2025-10-03 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 792d5bd9-4b39-3170-93ce-cf19fb811b81 | -14.607 | -46.7249 | 2025-10-03 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 9c07954c-34ea-31b2-b3d6-47969d125072 | -10.9673 | -51.0614 | 2025-10-03 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| fafd420f-9ef9-38ca-86d6-e8b98130d5cd | -12.6319 | -46.9923 | 2025-10-03 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e2c342ae-10c7-32f2-bc3c-af2c8d2ddcc7 | -8.8343 | -46.7694 | 2025-10-03 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 0d1394ec-f584-305b-938f-157c6ce9eb37 | -17.6338 | -44.4385 | 2025-10-03 12:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 66b1026b-9c11-3c12-9ec1-3149f5f95039 | -12.5301 | -47.3213 | 2025-10-03 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| f26188c5-55a7-3432-89df-6c784bb3a573 | -11.9167 | -46.259 | 2025-10-03 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 1c32dc29-df2b-3a82-aeb7-ee855a5676da | -12.6131 | -46.9725 | 2025-10-03 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 996669d7-f3ae-3242-9ef0-39810fc705b9 | -14.0037 | -44.9376 | 2025-10-03 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| dea7e1db-fc59-3cee-b87d-7e002721cfff | -14.3904 | -45.9369 | 2025-10-03 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 89641f6d-d887-341b-a753-add9e25754c4 | -16.0583 | -51.0454 | 2025-10-03 12:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 225.7 |
| df905db8-4215-350c-874c-d66b1a54de28 | -12.6131 | -46.9725 | 2025-10-03 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| f5c68a22-743f-3e27-a310-d84042214557 | -9.9186 | -43.6978 | 2025-10-03 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 634f5598-9e56-3ee7-9e9c-f7b157d533d5 | -9.9962 | -50.2248 | 2025-10-03 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 46cff66c-f717-3f5d-8851-6368d98dd414 | -9.9965 | -50.2034 | 2025-10-03 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 5288b13f-fefc-32a2-b5da-ce84aa87965d | -16.0587 | -51.0236 | 2025-10-03 12:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8fc2ce83-94d1-349d-a387-8ac91d3c2f4a | -10.9673 | -51.0614 | 2025-10-03 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| af3106b6-cd49-3cd7-bdbc-2e1db854684e | -12.6127 | -46.9951 | 2025-10-03 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 90b554d5-6a1a-3b89-9116-69b3e6b054ed | -11.5462 | -46.6943 | 2025-10-03 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fea91ad1-1b81-3972-9189-94f49380f590 | -12.6319 | -46.9923 | 2025-10-03 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| eb96f267-8355-3ff7-841f-5c823c943606 | -7.7494 | -46.272 | 2025-10-03 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0133492e-dbbf-3fdf-9ee9-7e279b85358a | -8.6911 | -47.6906 | 2025-10-03 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 63f2ca48-ec58-3742-b248-ea2cb40df7fe | -11.9167 | -46.259 | 2025-10-03 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 333.1 |
| 20063213-ea71-3096-b4b0-46e77dc93a58 | -8.8343 | -46.7694 | 2025-10-03 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8acc27ed-2a1e-37f8-9b52-88c3a9790507 | -9.9182 | -43.7212 | 2025-10-03 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 198.8 |
| 04676c49-e7c4-35d5-b2f0-9ba392487252 | -10.948 | -51.0846 | 2025-10-03 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 166.5 |
| dff46ebb-762f-3e2f-bb7f-2af020e59067 | -13.3418 | -48.1188 | 2025-10-03 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 136a9bb8-d082-3ff1-b365-841e65f062b2 | -14.426 | -46.0919 | 2025-10-03 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 7c38469c-7efa-364e-90bd-1b7d5da618d4 | -13.1727 | -47.8987 | 2025-10-03 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 7651e724-ec3a-3602-9385-d093fd9342e5 | -13.7472 | -48.0806 | 2025-10-03 12:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 0136686c-1881-3dff-8fd3-0044df8ee946 | -10.967 | -51.0826 | 2025-10-03 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5a1306a0-6297-3430-950f-375bd710224d | -8.5959 | -44.7833 | 2025-10-03 12:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |


[Clique aqui para ver as próximas entradas](README144.md)
