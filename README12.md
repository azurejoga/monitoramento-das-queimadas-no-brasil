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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e52dc6-3543-3fbf-bcde-822acc7031b3 | -1.2799 | -53.405201 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d3e754-ec82-3f89-86a1-7da58eec1c2e | -1.2607 | -53.366299 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ecd0d0d-28ef-33d4-8406-98bebb54f6de | -1.263 | -53.376598 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a593e3de-40b4-3a2b-bcbb-450ef454c672 | -1.2654 | -53.386902 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7a5426f-1543-3c3c-a722-d5238b85aae9 | -1.2701 | -53.407398 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e2d6ed8-382d-3a4d-861f-637d90e22ace | -1.2724 | -53.417599 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb0f081-b745-35c7-8c88-960423610a44 | -1.258 | -53.3993 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0875e69d-0b0c-38e2-a80e-699d6169ecc4 | -1.2603 | -53.409599 | 2024-11-03 01:09:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc9545e-8bcc-3d94-83db-a2afad971ce2 | -1.7143 | -55.763302 | 2024-11-03 01:09:51 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa053009-ecb6-30bb-ae24-e3d5d6d301a0 | -1.7161 | -55.771 | 2024-11-03 01:09:51 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eea2429c-82c8-3928-b9d2-b68684019f92 | -1.7045 | -55.765499 | 2024-11-03 01:09:51 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 296bdd8e-8a8d-3095-9f55-95c312467800 | -1.1913 | -53.6479 | 2024-11-03 01:09:51 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08f49e6e-2fcc-3ab4-9bc4-fe24763337d5 | -1.1936 | -53.657902 | 2024-11-03 01:09:51 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5bc7ab-2c41-37ba-b5d8-a69260e96417 | -1.312 | -54.222 | 2024-11-03 01:09:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 584e0467-3471-39d4-ac32-fe8a45d9bb05 | -1.1786 | -53.682098 | 2024-11-03 01:09:52 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1a9ff6-25fa-33a1-a540-aed0bddff3ea | -1.1981 | -53.902901 | 2024-11-03 01:09:52 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c4008f-d9a7-3350-adcb-be710632bb74 | -1.2003 | -53.912498 | 2024-11-03 01:09:52 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61091878-f11f-3f99-9e2d-c5b3468954b5 | -1.5297 | -55.4044 | 2024-11-03 01:09:52 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9de39000-5891-3c87-a21e-5a1f1d34f52c | -1.5315 | -55.4123 | 2024-11-03 01:09:52 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39dc5e51-d599-3e55-bd05-7c427a05cda9 | -0.6694 | -51.678902 | 2024-11-03 01:09:52 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fb3d5ca7-c65f-3d37-b3af-0c6eac97a697 | -0.6725 | -51.692501 | 2024-11-03 01:09:52 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8da34a-5c18-3544-bbeb-e348e350a3e8 | -1.2024 | -54.012001 | 2024-11-03 01:09:52 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5e7883-9413-3c2f-8afd-293793f6e6ba | -1.3368 | -54.601501 | 2024-11-03 01:09:52 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b80a8da6-6620-3963-a5e8-5d438649dca1 | -1.3387 | -54.610199 | 2024-11-03 01:09:52 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 330c4d80-c2d1-3c48-88ee-31a9d88427b2 | -1.1566 | -54.0816 | 2024-11-03 01:09:53 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b717f676-02bb-357a-ab87-bf02ec08bc04 | -1.3231 | -54.632 | 2024-11-03 01:09:53 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6c717df-5958-3fdb-a9cd-001b751f16b7 | -1.3251 | -54.640701 | 2024-11-03 01:09:53 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b0c44b5-d373-3b97-aea4-c577e8f05791 | -1.0867 | -53.640099 | 2024-11-03 01:09:53 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 413e9344-1281-31b9-b07d-dcba3cb5dba3 | -1.089 | -53.650002 | 2024-11-03 01:09:53 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6751cf5-8a0a-3f6a-80c5-26f120f1369b | -1.0769 | -53.6423 | 2024-11-03 01:09:53 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57cf3533-9802-3b63-b3dd-3946c6f1f705 | -1.0792 | -53.652199 | 2024-11-03 01:09:53 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc0658a-f3bf-33f2-be34-7fd6c3d09492 | -1.4693 | -55.5009 | 2024-11-03 01:09:54 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b90be9c4-0767-3ff0-b5b9-4a0d311727a7 | -1.5568 | -55.886299 | 2024-11-03 01:09:54 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d53f6a1-5cd6-39c4-939b-b87960c3bb01 | -1.4507 | -55.782001 | 2024-11-03 01:09:55 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 123554d4-43e6-3fa9-a0e2-a7869f25c3f9 | -1.4525 | -55.7897 | 2024-11-03 01:09:55 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f98352-8954-39dc-bdd3-d7f3ed62c360 | -1.4401 | -56.007401 | 2024-11-03 01:09:56 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13938c3f-6e6d-3a88-95b0-adaaf2a60feb | -1.2659 | -55.693901 | 2024-11-03 01:09:58 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 574cb408-125c-3ba7-9855-37ce6eb398b5 | -1.2544 | -55.688301 | 2024-11-03 01:09:58 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f607d1b-6c19-3cce-8663-a79e6812cff8 | -1.2561 | -55.696098 | 2024-11-03 01:09:58 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbce27d1-cac0-3ac7-8117-8f4f338eae10 | -1.2579 | -55.7038 | 2024-11-03 01:09:58 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b08f79-80a7-3ea3-9580-c0ba6370c79b | -1.2596 | -55.711498 | 2024-11-03 01:09:58 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd42da97-c84d-3ea0-8e74-6abb503260f7 | -1.2137 | -55.8269 | 2024-11-03 01:09:59 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66254237-2665-3e66-8e98-7439807bf08d | 2.5589 | -51.100899 | 2024-11-03 01:10:43 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4524fb5b-ec2d-35ed-8546-13a3ac52b853 | 2.5552 | -51.117599 | 2024-11-03 01:10:43 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 023855c7-1ba7-376c-8e6c-b613ca46fe2b | 2.5687 | -51.103001 | 2024-11-03 01:10:43 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 219ef92f-ee2e-3184-b01d-9cb0f2caccd0 | 0.6807 | -59.8004 | 2024-11-03 01:10:44 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2bbb2241-5ee2-390c-987d-3dd96f6de831 | 1.1241 | -59.434299 | 2024-11-03 01:10:50 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ce37c12e-e797-34d5-81c1-3c3d44a6332b | 1.1339 | -59.436501 | 2024-11-03 01:10:50 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 30c944df-feb0-360c-8c39-6444e04d20dc | 1.1324 | -59.443401 | 2024-11-03 01:10:50 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 730a4954-b514-3066-9616-f496d42cd29b | 1.1189 | -59.548599 | 2024-11-03 01:10:50 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5a4fd7-547c-3c84-930d-7206d736a101 | 1.1174 | -59.5555 | 2024-11-03 01:10:50 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 02a83a29-f023-3431-a4d9-55a7360a8f38 | 1.1996 | -59.966702 | 2024-11-03 01:10:53 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 71cd027e-2526-3c4e-9dd6-8fff0cd44219 | 2.8094 | -60.823101 | 2024-11-03 01:11:22 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b0284ca9-695b-32a5-9798-57c25c23b984 | 2.8078 | -60.830299 | 2024-11-03 01:11:22 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0ccf7d-d1c8-3beb-a949-ed65809476ef | 3.2803 | -61.019199 | 2024-11-03 01:11:31 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a6b947c3-d8ab-3ff0-bd75-7df831b49b49 | -1.2572 | -53.3938 | 2024-11-03 01:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6e7c71f7-b3e7-3380-bd32-1035bf606b5b | -1.2755 | -53.4138 | 2024-11-03 01:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| e15c6bc0-bed3-31f4-99c7-f993a4f39b73 | -1.2755 | -53.3936 | 2024-11-03 01:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 98dd588d-4442-3597-9917-e3a6ff05c674 | -1.2756 | -53.3734 | 2024-11-03 01:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| cf2513f8-8d87-3177-946a-cedc0a821c24 | -2.1746 | -53.6834 | 2024-11-03 01:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 530aebcb-e8a8-3a02-a37e-301097f5147d | -2.2802 | -48.8082 | 2024-11-03 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 17f3a45b-6850-35a2-b1a6-5fea1640bab3 | -2.2986 | -48.8078 | 2024-11-03 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| a5d14a16-844e-327c-9c8a-56aeee23ae78 | -2.6322 | -48.5634 | 2024-11-03 01:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 38476678-252b-30f0-86c7-03e43b6fd645 | -2.6506 | -48.5844 | 2024-11-03 01:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| e8e404a3-7256-34f5-8f63-d27468ae4848 | -2.6507 | -48.5629 | 2024-11-03 01:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f04f309d-569d-3ec9-bef2-348bc5c2ebcd | -2.7033 | -49.33 | 2024-11-03 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 4159a9b0-7353-3d88-b826-271532f538ed | -2.7218 | -49.3295 | 2024-11-03 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 7b2a6e60-58a2-30b0-ab25-93d992c010e7 | -2.5796 | -53.3927 | 2024-11-03 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1f5fc4c7-f776-30a3-aef2-0f360711a7e9 | -2.5797 | -53.3724 | 2024-11-03 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 6d99ab8b-184c-3eaa-b4cb-8e637b5d8c17 | -2.6321 | -48.5849 | 2024-11-03 01:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| a989af0b-4f1c-38c6-b6f8-ed9d8a7b0fd2 | -2.7419 | -54.4353 | 2024-11-03 01:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 8bf4f452-3f95-3b02-9515-1ef0ef3c63da | -2.7419 | -54.4153 | 2024-11-03 01:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 87e9ce5f-2d4f-3d11-b200-14cf0687da5c | -2.7602 | -54.4349 | 2024-11-03 01:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 196.8 |
| 0c61b326-6521-3678-9fd6-47399312a23c | -2.7603 | -54.4149 | 2024-11-03 01:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 8cd70a61-26a5-321f-bfeb-501c8fb6bba3 | -2.7876 | -51.6099 | 2024-11-03 01:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 68f238f3-58ef-3c12-88ab-ca8c45ab378b | -3.0365 | -54.2081 | 2024-11-03 01:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7ffec854-38c1-321c-8f68-6e5aac39ea9d | -3.0397 | -53.2603 | 2024-11-03 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b62413fb-dc86-374b-aea8-9047a9c5416c | -3.055 | -54.1474 | 2024-11-03 01:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| c712f06e-677a-39d9-936f-1c3251f743c8 | -3.0734 | -54.167 | 2024-11-03 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 46123e3e-7281-3597-ba37-d946320a7fa8 | -3.0734 | -54.147 | 2024-11-03 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 0eb9355b-3b73-33bf-95b9-e8040ec1fdef | -3.0918 | -54.1465 | 2024-11-03 01:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4015b73b-df30-364b-b093-b69daf56217c | -3.1213 | -51.1036 | 2024-11-03 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c7f1e882-4fcc-3e88-a5bd-5e9265c9e258 | -3.2047 | -53.4179 | 2024-11-03 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 911452f8-9bfd-3597-b710-e1e0d7f74a2c | -3.2415 | -53.4169 | 2024-11-03 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 96cfb96d-8768-30ac-bb88-dccb163f98fd | -3.2415 | -53.3967 | 2024-11-03 01:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 05708372-9a1b-3d7c-8282-cbbaacb5d644 | -3.2599 | -53.4164 | 2024-11-03 01:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4c6f667d-4971-37e4-872b-7ffd9cdedfe8 | -3.3276 | -50.2825 | 2024-11-03 01:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 06c819b6-a7f8-3536-afba-b09c8f65ce24 | -3.3277 | -50.2615 | 2024-11-03 01:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 8ca6ebf0-b86a-364d-9d95-890a7b0fd0ce | -3.4749 | -50.3826 | 2024-11-03 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| b7e8d99b-0327-3675-b67e-a1f28f2f4bc2 | -3.5466 | -50.8611 | 2024-11-03 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4b7f11da-65d7-3b99-a79e-ccfa27707428 | -3.9474 | -48.3451 | 2024-11-03 01:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f0c5314f-fe8e-3cd7-a255-63ddd5b73de6 | -3.9473 | -48.3666 | 2024-11-03 01:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d8c63d76-3388-3d4a-b9ca-e95020ce915e | -3.967 | -48.15 | 2024-11-03 01:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 050ea21a-717d-3f39-82a0-b37b49ef2768 | -4.4054 | -43.4746 | 2024-11-03 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 215.7 |
| cc760b83-dd62-3d28-b003-4056e04366f3 | -4.4056 | -43.4514 | 2024-11-03 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 268.0 |
| 0e8c68c6-7d55-31e9-b91f-6e02a0a178bf | -4.4058 | -43.4282 | 2024-11-03 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 74be0be1-1e34-3604-bb85-dc7fb17150c5 | -4.4241 | -43.4735 | 2024-11-03 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 12669e3f-d0f8-33cf-b1a3-a4d493481b7d | -4.4243 | -43.4503 | 2024-11-03 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 536adf36-e8ec-3a0b-94a6-3a6ed3d3af12 | -8.7247 | -48.0163 | 2024-11-03 01:15:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 57cbc0ac-93ca-32a3-9965-9d9db68cb076 | -11.2819 | -56.144 | 2024-11-03 01:16:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |


[Clique aqui para ver as próximas entradas](README13.md)
