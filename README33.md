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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5423b9be-221a-3fe7-a991-9465c0380d6c | -7.5826 | -44.428 | 2025-08-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 5b63093a-ce16-358a-890c-d074f42dc7f0 | -8.7822 | -46.4174 | 2025-08-09 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 61c8e354-15df-37cd-a6b7-53481df0ca3c | -8.5086 | -45.7033 | 2025-08-09 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9375565e-622d-36be-a073-b26a1b1a96bc | -16.9602 | -51.0542 | 2025-08-09 14:00:00 | GOES-19 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4b389330-2034-3b10-99e6-6f5188d6aa49 | -7.5829 | -44.405 | 2025-08-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 442.8 |
| 34952f64-9aa7-381a-a1ca-a75126b51a6c | -5.4353 | -41.2251 | 2025-08-09 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 154.2 |
| 154bc141-2303-3adc-8cd5-3713cd5e5dbb | -12.6595 | -44.4882 | 2025-08-09 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 296.1 |
| b4fba376-5dc5-32cb-841d-8d05ecfb5127 | -5.4165 | -41.2266 | 2025-08-09 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 140.5 |
| bd8dfceb-6b0c-3489-a58c-8275bf71cc74 | -12.5902 | -47.1781 | 2025-08-09 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 196ab8a7-cf0d-351c-a980-d694aff42b70 | -7.7017 | -45.5116 | 2025-08-09 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6f8a8139-62aa-3158-901a-0fc07734b6cf | -7.7202 | -45.5325 | 2025-08-09 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 8480d770-8060-3637-be91-c2d3d7edacb3 | -14.1103 | -45.4077 | 2025-08-09 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 12a92fb2-79d0-3455-b130-2b46e9d67dbc | -7.7014 | -45.5342 | 2025-08-09 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 29b1f0fd-3ef7-3154-8e5c-42def6f26de7 | -14.4849 | -52.1086 | 2025-08-09 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ad21d873-49c5-3d16-bf57-700dee2f9c59 | -8.7822 | -46.4174 | 2025-08-09 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 280.6 |
| d8072014-69a7-3557-9d09-6c40d7846c08 | -5.4165 | -41.2266 | 2025-08-09 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| c1bda39b-dea5-3aa2-898f-c487e4e888b7 | -8.7634 | -46.4194 | 2025-08-09 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| f37b28f0-3b45-3f37-add4-6ce650ed6fee | -14.1103 | -45.4077 | 2025-08-09 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 95a43e78-16bb-3106-9774-65cf6ddced94 | -12.0289 | -47.525 | 2025-08-09 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 9b82b7ef-f410-386c-ac02-7ad848e56de7 | -7.4835 | -44.8729 | 2025-08-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ce2a4556-b9c7-3b5a-98e1-5a96ddb3abba | -12.0293 | -47.5026 | 2025-08-09 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 269.7 |
| 71e057e9-e040-3a43-879d-73fc83719e4b | -12.0484 | -47.5 | 2025-08-09 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 4c0fc137-3752-3336-bd12-6f3e8d4d942f | -7.5829 | -44.405 | 2025-08-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 0ddfae55-8338-38d7-a8a8-2c1e52b5f3d0 | -9.9811 | -45.8328 | 2025-08-09 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 778a7638-dc1a-3459-9bc6-b47a9fb16663 | -7.7202 | -45.5325 | 2025-08-09 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 758e16c2-4cba-3430-a9d2-6aa446fbb23b | -11.0887 | -50.4954 | 2025-08-09 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9dbcad57-6f66-36f3-b359-369f212f399b | -12.0481 | -47.5224 | 2025-08-09 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| e8d61055-cee4-3b9e-9019-c6c6053f7ccc | -5.4353 | -41.2251 | 2025-08-09 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| d3afb434-0051-381c-82b6-1d613c1daccc | -7.5826 | -44.428 | 2025-08-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 27e45a48-66a4-3fec-93bf-1303cc3dcdb1 | -12.0293 | -47.5026 | 2025-08-09 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 31057548-8371-3f8a-88f7-47afcfcf9d31 | -8.7634 | -46.4194 | 2025-08-09 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 7c51c11e-1e6f-3d3b-8ee0-ee5ea44ed01d | -12.5902 | -47.1781 | 2025-08-09 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 720cc9b3-cabf-366f-b1c7-b5474ee0b70d | -12.5906 | -47.1556 | 2025-08-09 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| a887befc-eba9-35eb-9bb9-68ce3738ef76 | -14.4849 | -52.1086 | 2025-08-09 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 98a64b7f-e2c6-31ce-b4c4-40efaae49735 | -7.5826 | -44.428 | 2025-08-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| ee3e92bd-c410-3b0a-a2e5-b98df75a3675 | -12.0484 | -47.5 | 2025-08-09 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e7061910-1a90-30b6-9c8c-571dd9a4705d | -14.466 | -52.0899 | 2025-08-09 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4466f660-4870-3b6b-8455-a79d28eba680 | -8.7822 | -46.4174 | 2025-08-09 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 301.9 |
| f81f8820-0840-3e92-a36d-ea606f58457a | -8.1116 | -47.4371 | 2025-08-09 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 70808b26-ebe9-3f30-936b-0cd8255060e6 | -7.3012 | -39.6453 | 2025-08-09 14:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 72.6 |
| d8407392-d0b4-365a-ab9e-c5b23c3b1fb1 | -12.0481 | -47.5224 | 2025-08-09 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 10ba3d92-171a-3a8c-9f73-4ef581778167 | -7.5829 | -44.405 | 2025-08-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 768814a8-aeed-3429-b7e3-cb2a01ae7a2b | -12.0289 | -47.525 | 2025-08-09 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e26a21ce-55f6-319f-a8d5-99e65fcc6120 | -5.4353 | -41.2251 | 2025-08-09 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 3a272a87-6dcc-3303-bd18-6fa3312731ac | -8.9213 | -60.7489 | 2025-08-09 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 6113a162-bb6e-351c-bdfc-327a16b34660 | -12.0289 | -47.525 | 2025-08-09 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3e181c5a-d743-3354-b6f8-628a4c8c2854 | -7.7202 | -45.5325 | 2025-08-09 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 192.7 |
| ff3c6c95-6c32-3a98-9f86-1c0c2a6a642b | -8.1116 | -47.4371 | 2025-08-09 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 927d96e3-d1b8-3b4b-bafe-00f48dab3a6d | -6.9873 | -43.8606 | 2025-08-09 14:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d2a0ee72-793b-386f-acd8-9d8441c161cd | -8.9213 | -60.7489 | 2025-08-09 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 2c3d0299-26d2-30de-ab31-c68dfec11a7e | -12.0293 | -47.5026 | 2025-08-09 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 385417a8-3f6a-387f-97bb-3e38e7bb0d07 | -12.5902 | -47.1781 | 2025-08-09 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| cdc1d9aa-9a1f-313a-bddc-59249da3a956 | -8.9399 | -60.7481 | 2025-08-09 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 1624ed16-d785-31e0-9312-3f97ab6f68b9 | -12.0481 | -47.5224 | 2025-08-09 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 74a1f306-a31e-3f7b-b8de-ea0ae006376b | -9.5136 | -45.4112 | 2025-08-09 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9e9b2fd7-a03d-30d5-b56f-f35b864826fb | -12.5714 | -47.1584 | 2025-08-09 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2e8648dd-83d0-3704-a7ce-b50ae53148bc | -14.466 | -52.0899 | 2025-08-09 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a71295d3-1a86-341f-b5e1-1e8d57822bb3 | -14.4849 | -52.1086 | 2025-08-09 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c83a3aee-70c8-3203-98e2-0e3e29c93dab | -7.5826 | -44.428 | 2025-08-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 064c1fae-a836-3ceb-ace1-386a80c55e6d | -7.7014 | -45.5342 | 2025-08-09 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ca014342-d2cc-3bc5-898c-0dc26cf35657 | -7.7391 | -45.5307 | 2025-08-09 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f54d251f-68ed-3fe1-8f43-175dc4e1273d | -12.5718 | -47.1359 | 2025-08-09 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 6ee0fb0d-5eaf-3484-abef-22de40fa515c | -12.571 | -47.1809 | 2025-08-09 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9399fdec-3e93-31c3-927d-761bbe1a1273 | -7.5829 | -44.405 | 2025-08-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 0f4c48ce-18fd-3e28-a3c7-7f5b5ee47f99 | -12.5722 | -47.1134 | 2025-08-09 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ef5a83c1-47d7-32c8-8f1b-52e77014fee0 | -6.45 | -45.0086 | 2025-08-09 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 570102b9-2e2e-33b1-9f86-72ea23bed99e | -8.9215 | -60.7297 | 2025-08-09 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| d6ceb90c-abc7-303e-9f0d-c26d22bd8c89 | -7.5826 | -44.428 | 2025-08-09 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7004e3cc-8be9-3e91-b5e8-634ae3598769 | -8.1116 | -47.4371 | 2025-08-09 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0426059a-433c-3609-ba28-be160ec5e92b | -8.9399 | -60.7481 | 2025-08-09 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 186.0 |
| e1c56467-7431-34fc-9ffa-15fb7273dfbc | -12.5722 | -47.1134 | 2025-08-09 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| afcd23bf-e217-3dff-9649-e8f8b7480095 | -7.7202 | -45.5325 | 2025-08-09 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 81e0513f-c5b2-3a07-a2a9-0eca0047c941 | -8.7822 | -46.4174 | 2025-08-09 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 3b2c0095-5680-3b95-a36f-609c224d90bb | -14.4849 | -52.1086 | 2025-08-09 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a4721dad-77ea-3248-926e-f898aa206c97 | -5.4353 | -41.2251 | 2025-08-09 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 38e5f512-7018-3d4c-a817-7748b65a2acb | -8.9213 | -60.7489 | 2025-08-09 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 5b00791c-3e29-3cf6-99b3-d4452fd2f077 | -8.9401 | -60.7288 | 2025-08-09 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 0719b812-4727-31aa-85ac-633f87d34822 | -7.5829 | -44.405 | 2025-08-09 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 991a7615-2522-357a-82b8-c21b9a7feac6 | -8.9215 | -60.7297 | 2025-08-09 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| c2050f30-99ac-37fc-a82d-7322135a44a4 | -5.4165 | -41.2266 | 2025-08-09 14:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 175.8 |
| 9c74707b-0b0b-3961-95b6-e7ee5edd8d49 | -9.5136 | -45.4112 | 2025-08-09 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |


