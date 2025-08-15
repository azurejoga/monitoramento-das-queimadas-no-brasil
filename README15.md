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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4e4aa68-5359-368f-a342-6ca51757b026 | -9.5477 | -63.584 | 2025-08-15 02:00:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff2b1f24-e7c2-35c1-a53a-2509cb88f4ab | -8.1172 | -61.1964 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba9b3c79-c1c2-3a0f-b352-2911f8f9b35e | -7.6094 | -63.513 | 2025-08-15 02:00:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe001e8-ece4-38af-9fc1-c10e11321856 | -7.6045 | -63.492802 | 2025-08-15 02:00:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3c2700-cb3b-3268-9cc5-58507ebc2ecd | -5.4576 | -60.140598 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6858663f-8c24-3f63-8383-6f2538c64c66 | -6.0825 | -59.967701 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d63283a-6b1a-3f9a-9e7d-cd3153daa407 | -7.8138 | -61.345501 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3fb79f-f957-3f3f-92a4-5c7f999fc4f9 | -13.0672 | -57.131001 | 2025-08-15 02:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 581b1073-433e-3543-8672-616da2dc75b6 | -6.0779 | -59.949299 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0da6f1-1725-358b-8c74-52de51728545 | -7.0899 | -59.2295 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6d0f156-45a9-316e-922b-d69889c2e4a4 | -7.3284 | -60.634399 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3ae057-06e2-379e-b544-a9a64ba25566 | -6.9588 | -60.018101 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b837c11-6552-3581-b0dc-0787dfc446ca | -5.4621 | -60.158901 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc637e0d-44b3-3472-a5f1-bdd4f8cacad8 | -6.6801 | -58.826801 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d10cff5b-f811-3e1a-931e-17a031d280d1 | -6.107 | -59.9422 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a80f9e93-914e-3d5e-af90-b13e6f0138d0 | -9.3878 | -60.540798 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a12bf215-3c7f-3360-8ab8-e7d8fd4d7822 | -7.309 | -60.639198 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40a3cf7f-f461-3dae-b166-94ab8d9ff18c | -6.9544 | -60.0005 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f4e1c37-5008-3fce-84ed-db30e2de997b | -7.5473 | -61.3521 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 064081db-a3cb-354f-b0fa-6f4e9f06d21a | -7.5644 | -61.4216 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0ebdd73-e9ff-37a0-a479-a54307b97f88 | -9.5177 | -60.523602 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8528813e-9c55-3620-a696-e6484cc2a25b | -7.3187 | -60.636799 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 021b47eb-877e-3352-9154-36328161f9ad | -9.2051 | -59.654202 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf5cdfdc-ebf5-3639-b038-fc395c381521 | -10.364 | -64.446503 | 2025-08-15 02:00:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 74165813-94f9-3cc8-b662-0438013b5931 | -9.1857 | -59.6591 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2577b49f-6913-39a5-999a-a9ef2e1b7193 | -7.4349 | -60.029202 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71163a82-44cc-3dfa-ba54-0333427e0d95 | -8.5643 | -63.9202 | 2025-08-15 02:00:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d898388-68d0-3524-9cc4-45093ce016aa | -9.3915 | -60.555599 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f53afa4-d5ff-3dd6-aee8-effa52ccb370 | -5.453 | -60.122299 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc3937a-c47a-3df6-b1dd-3c7e129bba73 | -9.1654 | -59.700802 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7aa5712-2f7b-37d2-b215-cceca347e5b9 | -6.0729 | -59.9701 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bb69737-771f-3e2d-9a24-b5ad05756345 | -9.6368 | -63.097599 | 2025-08-15 02:00:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e76bf44-db54-39a5-b364-44109639e2ec | -7.9582 | -61.7644 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24407d65-dd03-3738-a40a-d830c4cf4934 | -5.4672 | -60.138199 | 2025-08-15 02:00:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d43accf5-068e-3afa-8bf3-16260ee8cfd7 | -8.4056 | -70.434196 | 2025-08-15 02:00:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3f749696-8b8b-3628-aab2-82d03f6d38c2 | -6.9456 | -59.554901 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 078e7cef-3611-3dc1-88ac-e6491ef7ae60 | -6.4815 | -62.943901 | 2025-08-15 02:00:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37e48cfb-609f-34f6-945c-448bcbe98bad | -6.9491 | -60.0205 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 444a2643-b219-3ea7-8f39-318d8e1a004f | -6.9447 | -60.002899 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4653de00-7006-3abe-9ae2-9eb728e24fac | -8.1207 | -61.210499 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64084e3f-960a-3eab-b5d6-515dbeced653 | -6.7242 | -58.8386 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69c78d91-2ce9-3d5c-a0d2-f89471612c15 | -11.3648 | -55.4244 | 2025-08-15 02:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1e78dc9-1037-3a65-9873-ac3909b2fc8c | -7.5971 | -63.505299 | 2025-08-15 02:00:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9661612-daba-3b04-ac04-b7b16b524aed | -6.905 | -59.1479 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbabdff-22a2-344a-8acf-2ae85f925f48 | -6.665 | -58.807701 | 2025-08-15 02:00:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 929bf630-0d89-3980-a174-2b9437ef3a18 | -13.127 | -57.161201 | 2025-08-15 02:00:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68a644fa-156e-35d2-baf9-ad8adb8b2c45 | -9.2191 | -59.6689 | 2025-08-15 02:00:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f7defa0-84b6-3571-9991-38fccf91eb97 | -7.9485 | -61.7668 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f41e7d8-47e0-3091-9fd8-4f754affd84e | -8.5621 | -63.9109 | 2025-08-15 02:00:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca89a97-30b4-3570-8d86-0ff709e851d6 | -6.936 | -59.557301 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| face1e85-4129-38a1-87b6-c091e758056a | -10.473 | -61.327801 | 2025-08-15 02:00:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9922471-6ef9-3d7c-8d95-c3e7387ced16 | -7.2861 | -64.709602 | 2025-08-15 02:00:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2866061f-b569-3ce5-b3c2-84970643993c | -9.5043 | -60.511299 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d25f596d-973b-3aa4-9941-72f431448fd5 | -9.4983 | -60.5285 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0483926-54ad-3de1-885c-9af234d27573 | -8.1138 | -61.1824 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89cb11b6-978b-3d5b-a436-6ac179ccd1fa | -7.5404 | -61.324001 | 2025-08-15 02:00:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0ed7554-0ac1-37a7-ad24-0bef1e3f2355 | -7.6118 | -63.523102 | 2025-08-15 02:00:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19d119e9-6082-3bda-a76b-dfdd1524b7eb | -7.3051 | -60.623402 | 2025-08-15 02:00:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d3e6e91-dcea-3b51-8ae3-626765def688 | -9.3975 | -60.538399 | 2025-08-15 02:00:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8f94fba-237f-38a4-a35b-183a8a25f432 | -9.5454 | -63.5746 | 2025-08-15 02:00:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5683e183-b259-37e4-9318-d455d4087439 | -7.5292 | -61.3254 | 2025-08-15 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f9777506-b729-3079-ac71-d68c7bd18e03 | -9.1706 | -59.6762 | 2025-08-15 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| bbd1d40f-5ad3-3c24-b538-00bf63cfc07e | -7.0797 | -59.2157 | 2025-08-15 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 997c565f-3cc9-3d7f-83c7-341d90f3aa7d | -6.9303 | -59.5305 | 2025-08-15 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 00705973-a0cf-3389-819e-9ff0d9df4ef0 | -6.9302 | -59.5497 | 2025-08-15 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e4b663f7-a0f4-3bce-ba3a-951fe3ba70a3 | -5.455 | -60.1391 | 2025-08-15 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 58125da5-dfd0-397f-bebc-f4bc4eb38d70 | -9.1708 | -59.6568 | 2025-08-15 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 9edbfd4f-5338-36c6-9e88-9cadcb271aea | -6.0807 | -59.9465 | 2025-08-15 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d0bb8eba-49ec-3adb-9455-1c0e30479389 | -9.152 | -59.6772 | 2025-08-15 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d681226b-9dee-3f8d-bf59-68d129d8ad3f | -5.762 | -46.6741 | 2025-08-15 02:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7207aaec-6189-3fb7-9afe-ab8bbda65e41 | -9.1892 | -59.6752 | 2025-08-15 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 01012a3e-5fbf-3e9d-933d-2fac7a2e6f06 | -11.3657 | -55.4107 | 2025-08-15 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 659f5037-734e-3ddd-8413-78dc4aed0895 | -9.5179 | -60.5461 | 2025-08-15 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 37099357-f1c0-37e7-8301-a9b28e2ef866 | -7.0247 | -47.4636 | 2025-08-15 02:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| b3f3299a-f581-3300-ab3e-4ce35a529743 | -9.4994 | -60.5278 | 2025-08-15 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 2f82f231-fe61-3c43-932c-909577ebafa4 | -11.3466 | -55.4326 | 2025-08-15 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 45d4a759-0934-3c5d-9cbb-e4a2d748b4d9 | -11.3653 | -55.4512 | 2025-08-15 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 6f3c2208-d1e8-3a52-bb0b-52f917dc02d0 | -9.518 | -60.5268 | 2025-08-15 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 132c66b9-70c4-3472-bbc8-da3fa942c1aa | -6.946 | -60.0104 | 2025-08-15 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| d32f7a49-68b7-30f7-b89a-031163eb5097 | -9.1894 | -59.6558 | 2025-08-15 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 816a412a-5e49-3568-be6f-35e8a95a07e5 | -9.4992 | -60.547 | 2025-08-15 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 6e8226fd-4a90-36a9-b4bc-ebfd0220db71 | -16.3153 | -52.9201 | 2025-08-15 02:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 25f5996b-0445-30f3-831a-78fa2f6fd72a | -11.3468 | -55.4124 | 2025-08-15 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 204.1 |
| 9b4ae705-f8db-3af2-ab39-b1f238f0026a | -11.3655 | -55.431 | 2025-08-15 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 213.0 |
| b7174659-069e-36bc-8ec5-612e5302fd7e | -7.5291 | -61.3444 | 2025-08-15 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e93da9ee-ebbf-3c22-9301-c43bbb9287d6 | -6.9461 | -59.9912 | 2025-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3a9f8f18-8ffc-3888-93fa-54de70f092a0 | -7.5919 | -63.4978 | 2025-08-15 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 759012f2-f16e-36af-8230-41011b6d9cdf | -9.5147 | -40.3558 | 2025-08-15 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.4 |
| ecf3d0d2-2221-346a-bb70-9e79d4a993f1 | -11.3657 | -55.4107 | 2025-08-15 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3b1d1945-7799-3cba-8705-94518f6f4415 | -9.5179 | -60.5461 | 2025-08-15 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 082629f7-b6bb-39ff-8c91-6b08b7942610 | -6.9302 | -59.5497 | 2025-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 27b7b326-0ede-323b-b3e6-2d6d311d441c | -6.946 | -60.0104 | 2025-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 8724d226-aac9-33e3-a83b-e41700ffdb24 | -6.9303 | -59.5305 | 2025-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 101b25f5-0e84-31c1-841b-bf87050a4a9e | -11.3468 | -55.4124 | 2025-08-15 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 9af578bb-23bb-3780-9bd2-792dc7c72db4 | -16.3153 | -52.9201 | 2025-08-15 02:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b066d21c-54ad-3a41-81e1-b72506c8a97f | -11.3655 | -55.431 | 2025-08-15 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 150.2 |
| fa35a817-7b49-3196-a7e5-3e05f4c2711b | -9.1706 | -59.6762 | 2025-08-15 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2bff3540-c1f0-3e19-9e3c-676d0eb24056 | -11.3466 | -55.4326 | 2025-08-15 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 165.3 |
| baf26dd2-e6eb-3c01-be90-a810c66156c7 | -5.455 | -60.1391 | 2025-08-15 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 091418a4-a600-30ab-b83a-fd5c9d2975d5 | -9.152 | -59.6772 | 2025-08-15 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |


[Clique aqui para ver as próximas entradas](README16.md)
