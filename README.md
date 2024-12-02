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
| c1f8e416-fcd0-3df4-bac0-14fde9fffe1c | -3.1454 | -45.4753 | 2024-12-02 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 194.5 |
| 236b40dd-ceea-3081-a0fe-407501e0c940 | -4.5932 | -43.3471 | 2024-12-02 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6abb1ec2-8861-3cb1-afb6-f08c1507654d | -5.1367 | -43.2185 | 2024-12-02 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 265e03c8-d483-38ca-b9ca-46aeab657516 | -2.9824 | -53.8879 | 2024-12-02 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 806785e7-54e6-31f5-8edd-9399bbe4d782 | -2.5612 | -53.4133 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 49d8b068-9136-3301-a8d6-be584b816887 | -12.2494 | -63.4497 | 2024-12-02 00:00:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| dd840a11-cafb-3a67-808a-358d0a9daa54 | -3.4755 | -50.2566 | 2024-12-02 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 40ebd6e9-7f67-3b5c-81cf-61ed980266bc | -2.1605 | -45.6415 | 2024-12-02 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d6c8bf69-1c34-3f7b-903b-e78cb0647031 | -5.118 | -43.2198 | 2024-12-02 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a0c69a92-197e-3b02-b8c1-b3c75e61f800 | -3.1453 | -45.4978 | 2024-12-02 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 186.0 |
| 4b7cfba2-52e7-3b0b-a9fa-d4d25fe026ab | -2.8012 | -53.0633 | 2024-12-02 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2582e6fb-fb59-3026-9027-7bf0b62c4135 | -3.2591 | -53.6186 | 2024-12-02 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 18b28526-450d-3ebb-a080-790b28d9afe4 | -3.4955 | -46.0871 | 2024-12-02 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5cfb4042-86a7-3aea-98ea-b84efd8be24c | -3.7248 | -52.2819 | 2024-12-02 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8ef5a581-5855-3503-9c62-398aa9945008 | -4.7765 | -46.4244 | 2024-12-02 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b75068b6-8284-328f-b0c8-40a2d065c1c1 | -2.5428 | -53.4137 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 4a656e12-1533-3b11-a41c-dfbdd404e29e | -2.0263 | -54.3088 | 2024-12-02 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| e328834a-98af-37a6-94ad-76138b33241d | -3.237 | -45.763 | 2024-12-02 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d71b7728-8222-3dba-ae04-bca920e0672c | -3.2184 | -45.7637 | 2024-12-02 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 128.0 |
| ba5239ac-6dbe-3e85-81db-49168330e5dc | -3.7084 | -51.8301 | 2024-12-02 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 29354acb-c910-393d-ba5d-6cb6ec7e2a6f | -2.6348 | -53.3712 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 63b0bb2f-ca10-377f-8b5a-f206d0fa2d10 | -3.2775 | -53.6181 | 2024-12-02 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ea68d6c9-201f-3ce6-a3e4-8a430f1150b0 | -3.3848 | -49.8596 | 2024-12-02 00:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| aef8cdfa-5b57-33de-8e72-ae08e8f3a8c0 | -2.9871 | -52.5086 | 2024-12-02 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9b649ba9-0a5f-3945-ba00-f747c8129082 | -3.4017 | -50.2171 | 2024-12-02 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f41a0905-2a0f-39e0-9996-f81f07065dd4 | -2.8013 | -53.043 | 2024-12-02 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 597b0125-a07a-3c09-8b11-8e6de4c1b728 | -2.5428 | -53.3935 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0c55a4bb-6cdf-31be-b770-c0a62eaa8d9a | -4.8174 | -48.6272 | 2024-12-02 00:00:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7938aa1f-9e5a-3eee-aba9-b68753964e57 | -5.1369 | -43.1951 | 2024-12-02 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 8b01fe5d-96cd-3867-9831-67394ef0798f | -4.9085 | -41.3371 | 2024-12-02 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 26ae20f2-5772-3afe-bee6-5c092eeb39df | -3.4201 | -50.2375 | 2024-12-02 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 47d72f92-52d0-3c4f-b8f6-50d7adcac15e | -2.5612 | -53.3931 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 09bec173-af7d-31d5-856c-d14bf820f57f | -6.086 | -48.0557 | 2024-12-02 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 218.6 |
| a8d16e24-dcd2-3e19-9977-515c46a5ae7d | -3.4769 | -46.0879 | 2024-12-02 00:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 804455dd-7d47-3dc3-9157-7dabddc4a557 | -3.4017 | -50.2381 | 2024-12-02 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| e0885b28-8643-376a-81c4-68c0cfe6af45 | -5.1181 | -43.1964 | 2024-12-02 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ba942699-0b10-3835-a712-915a90574e78 | -3.259 | -53.6388 | 2024-12-02 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 88823a7a-ebad-3179-af19-606308fbdf9c | -3.2774 | -53.6383 | 2024-12-02 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| cd30693b-63fa-3639-8913-153acfbc8f5a | -2.5796 | -53.3927 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f0777450-8cff-3eaa-a5df-8c81d5c37fc7 | -3.7522 | -54.5093 | 2024-12-02 00:00:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 5ae98a24-9e0d-3a33-a22e-21d0026f14b3 | -10.0107 | -36.1108 | 2024-12-02 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 184.5 |
| 851191bd-ded0-3fce-a70a-71304ff7a785 | -10.0112 | -36.0836 | 2024-12-02 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 212.1 |
| 663e0f2d-c287-3e8b-84fc-9ac572c8f750 | -10.6674 | -44.4835 | 2024-12-02 00:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a38ca701-2cf4-3de4-ab1e-9471dde6fa53 | -3.3462 | -50.2399 | 2024-12-02 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 3e621565-2472-3ab9-9693-f70b14e77953 | -2.1604 | -45.6639 | 2024-12-02 00:00:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 71faa48f-68dd-3ccc-bcbf-d836bf3aa3c9 | -2.8197 | -53.0425 | 2024-12-02 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| da5c156a-d856-3989-b6ec-6739f1e0ecfd | -1.0735 | -53.4562 | 2024-12-02 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6b1e0ae0-4a02-3928-967a-56a8dfeb3305 | -6.0862 | -48.0339 | 2024-12-02 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| f41d933c-e236-3dfd-9224-b95d1371c100 | -2.2667 | -53.6011 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| edcf7ba0-5418-3152-92d4-dc55ba4715e0 | -2.6349 | -53.351 | 2024-12-02 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| b038d690-0e5a-3509-8a5d-10b840768c66 | -2.8196 | -53.0629 | 2024-12-02 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| e9cd7b84-3407-39cd-b3c8-b6bf0bff0cb1 | -12.2493 | -63.4688 | 2024-12-02 00:00:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 40e89bf2-4f6d-346d-969a-290083f33cf6 | -4.5745 | -43.3483 | 2024-12-02 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| cf2f26ff-e1c9-332b-a0f1-eee8cc80f5f9 | -6.0674 | -48.0569 | 2024-12-02 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a0fab3d5-728c-34f3-acde-19f7c9c389bd | -2.2901 | -45.7498 | 2024-12-02 00:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a1df07e0-dd01-3f92-beb8-4c33845cd8c1 | -4.267 | -50.8551 | 2024-12-02 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 00deaa56-64cd-3cbf-b419-4e46a2b9c5ef | -2.55 | -53.4 | 2024-12-02 00:00:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfc4f493-48fb-3e5a-b0d4-87c3f6d54338 | -4.8174 | -48.6272 | 2024-12-02 00:10:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0bc168e1-2163-3ca5-b6c5-e3149a7f7b43 | -3.371 | -53.2107 | 2024-12-02 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a26d92f7-d971-3483-96f4-df66084d3f08 | -3.7522 | -54.5093 | 2024-12-02 00:10:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| f0a69cfb-e77e-315e-94ac-4378cb0fb1e1 | -2.9208 | -45.8417 | 2024-12-02 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 39c60235-93d0-37a4-ad03-a715e02b8286 | -2.5428 | -53.4137 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| fe7e1189-2582-3184-aa01-0b3c01f8e82a | -6.0862 | -48.0339 | 2024-12-02 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 1d0b7405-1cff-34f0-8fb1-e1db82a2cdae | -4.7765 | -46.4244 | 2024-12-02 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2922f06e-e893-3261-bc29-67ca45adf91a | -3.1454 | -45.4753 | 2024-12-02 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 138.4 |
| f0064dae-77c0-3227-a082-0494500deadd | -2.5428 | -53.3935 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 978959ff-f71e-3526-b6dc-6582850a52c5 | -6.0676 | -48.0352 | 2024-12-02 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0aa53622-5c02-3b5a-ac41-1a37585155d4 | -3.4769 | -46.0879 | 2024-12-02 00:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 10b036e1-a485-3bf5-a549-87c32fd174e2 | -2.9824 | -53.8879 | 2024-12-02 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 88589f1c-393b-37b6-9828-c402e8fbee0c | -2.0263 | -54.3088 | 2024-12-02 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 805477ce-032f-35cf-8cb5-e2dfe9752016 | -2.9394 | -45.8411 | 2024-12-02 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5ca24695-1623-3410-9dd6-65855a13644f | -2.9209 | -45.8194 | 2024-12-02 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2c49cca6-6864-31fe-bf63-24c941afeb74 | -3.7248 | -52.2819 | 2024-12-02 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 05e81273-44a0-399c-b55f-d97ddd117358 | -1.0735 | -53.4562 | 2024-12-02 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| bf1744c0-3c98-35e5-955e-1d1ebbcfadbe | -5.1181 | -43.1964 | 2024-12-02 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f98bdd9e-562a-3f70-8110-f5fdf277f23d | -12.2493 | -63.4688 | 2024-12-02 00:10:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b362bf60-079b-398d-8e73-bc27fdda059d | -4.5743 | -43.3716 | 2024-12-02 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6168e04b-a8eb-343a-8f57-9523dc3889d4 | -3.4755 | -50.2566 | 2024-12-02 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 33703537-3e38-3713-a7fa-bfa0f5828bfb | -2.5612 | -53.3931 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 4ccd9cbb-eb35-3b3f-8cf6-c386bf197a7e | -3.4017 | -50.2171 | 2024-12-02 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fe48742c-91de-3e9b-aad0-c5f4ab16274e | -2.9871 | -52.5086 | 2024-12-02 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| cb1a7443-f543-3f21-a5ac-dc3b0d943bad | -3.4017 | -50.2381 | 2024-12-02 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 5a5e9244-3d5d-3ba7-8488-c6ec73b5ce0a | -5.1369 | -43.1951 | 2024-12-02 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| dd9e0b63-8947-33ea-861f-c3ffd653dabc | -3.3018 | -52.0694 | 2024-12-02 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f52eb0d0-1c64-3b58-bcdd-14601de7c795 | -4.267 | -50.8551 | 2024-12-02 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 62e17c63-4d54-398e-8bed-9ee01b49e526 | -2.8196 | -53.0629 | 2024-12-02 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| bd453989-c411-37cc-ab37-f3f16e163d9b | -3.4955 | -46.0871 | 2024-12-02 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1f95220e-f574-3fa8-8a95-82f2f191f7ee | -2.5612 | -53.4133 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| e87ccb3c-8c75-3ea0-83d5-02a041c95e44 | -6.0674 | -48.0569 | 2024-12-02 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| b22bf627-0ab9-3c40-b1f0-772041aec766 | -2.5795 | -53.4129 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2ab1d182-da78-3958-aad4-f4011332a19c | -2.8013 | -53.043 | 2024-12-02 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 61b89f3c-46a6-3874-9d05-957e31d8ce85 | -5.118 | -43.2198 | 2024-12-02 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 388dd358-ec05-3e16-82f3-d803beed1497 | -2.6348 | -53.3712 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 72fe87e8-8b64-34c6-b6ee-22286571e22e | -2.6533 | -53.3506 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c8e1ebe0-8745-3244-87f7-65b82c342de0 | -2.5796 | -53.3927 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 12357663-f78f-328f-b5eb-542ee2388cf6 | -5.1367 | -43.2185 | 2024-12-02 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 0d474e19-8844-33d2-858e-58dcbcae7694 | -3.1453 | -45.4978 | 2024-12-02 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 2293d386-a970-32e3-a138-554f1f264a6d | -3.0055 | -52.5081 | 2024-12-02 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 14b0ff9b-0fd9-37b2-be5f-7620015de9f9 | -2.6349 | -53.351 | 2024-12-02 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 27066912-b8ba-3ae3-bd81-f25a2d6af810 | -4.5745 | -43.3483 | 2024-12-02 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |


[Clique aqui para ver as próximas entradas](README2.md)
