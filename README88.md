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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c4fcf48-0d32-3622-8d05-42f16595fae7 | -12.7082 | -48.0984 | 2025-08-23 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 6a3bc71a-0866-39d2-ae4c-be435fd74d33 | -7.0352 | -44.6396 | 2025-08-23 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2a420cf2-ab9a-3b19-8cf5-90602aedd1d0 | -9.1533 | -59.5027 | 2025-08-23 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3998fddc-1775-3d30-afe6-c07aac4288bd | -10.6201 | -50.1609 | 2025-08-23 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 544a0f26-c61a-39ee-817a-7f5aaa6612a2 | -5.7614 | -57.6002 | 2025-08-23 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 60cd3edf-bb07-3b2a-b587-138837b626aa | -6.5856 | -44.564 | 2025-08-23 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 7679c535-e229-3c3f-88f1-4119d2148b85 | -12.9921 | -45.2252 | 2025-08-23 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| dc0e0f4b-0b4f-3275-a382-cefd207d434f | -6.6044 | -44.5624 | 2025-08-23 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3e16f9dd-2b4c-3346-ad0f-707b59632a3a | -7.0164 | -44.6413 | 2025-08-23 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| fb83e4f9-d7c4-3374-9e1c-57a67d16b685 | -5.7615 | -57.5807 | 2025-08-23 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 16cb17cd-45fb-30a8-9dac-da8c0f8337ed | -12.7078 | -48.1206 | 2025-08-23 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 36a2b113-b3f8-3e8d-bb80-3caf676f1bfc | -14.6899 | -54.912 | 2025-08-23 12:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9f89932a-2afe-39ab-8f4d-6f0c3757741b | -6.1229 | -43.9578 | 2025-08-23 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 68aa85cc-6f30-3f29-9d93-6d5f7d045ca9 | -5.7429 | -57.6009 | 2025-08-23 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| d7c852d0-ac0e-3add-ae04-8134c2870d17 | -5.7431 | -57.5814 | 2025-08-23 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| aaa3722e-cd9e-3e50-ba39-aaccc4105e12 | -12.5418 | -45.6189 | 2025-08-23 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3a926002-1e2b-3e80-8af1-4ae440021cbf | -7.6296 | -45.2464 | 2025-08-23 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 5b83e3be-ef76-3749-b0e3-d6ee08962355 | -7.6296 | -45.2464 | 2025-08-23 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b142080d-b5f6-39a1-b421-4017da2529f4 | -6.1416 | -43.9563 | 2025-08-23 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 217d6bcf-af80-3886-b54c-dcd5c194d5ed | -12.5418 | -45.6189 | 2025-08-23 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f18b5802-f061-3056-8743-5f3072d533e1 | -5.7614 | -57.6002 | 2025-08-23 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f0b5c445-f6b0-3fb1-a372-948ecc58108d | -6.6044 | -44.5624 | 2025-08-23 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0c963525-e934-3feb-99c6-bfeb1a007c30 | -14.6899 | -54.912 | 2025-08-23 13:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7b096c2a-8426-334c-8430-d127093b70a7 | -5.7431 | -57.5814 | 2025-08-23 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 61bb6482-fb0e-3d9e-8eeb-3bb51928e223 | -6.1229 | -43.9578 | 2025-08-23 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 536dc883-f149-3d6e-a5b4-4df7a42083b7 | -10.6201 | -50.1609 | 2025-08-23 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 08a83786-dc4d-3f10-bf3a-f11e51a00e3c | -7.0352 | -44.6396 | 2025-08-23 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e2bd7942-d64c-3bde-a1a9-2c1946a706bf | -5.9062 | -45.1185 | 2025-08-23 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0642425b-816d-30fa-b174-c5f967c9f734 | -5.7429 | -57.6009 | 2025-08-23 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| fc59e25f-7c0d-362d-b8ad-c686e0d4fc0c | -14.6706 | -54.9142 | 2025-08-23 13:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| f091f84b-b22b-34ae-a529-864f15e14ce1 | -5.7615 | -57.5807 | 2025-08-23 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| da1a8f4e-1d5d-38ec-b092-656e8833dea8 | -10.6393 | -50.1375 | 2025-08-23 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 50434119-cb5b-3228-aea0-7fff9e63bf92 | -6.5856 | -44.564 | 2025-08-23 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 289c7a32-70ea-3a4d-85e4-078d5974b280 | -12.9921 | -45.2252 | 2025-08-23 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 24cc79ee-110d-39f5-bbac-3943d7c04ee5 | -7.0164 | -44.6413 | 2025-08-23 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d108dd72-2533-315d-ae6b-4b83bcaaa812 | -6.1416 | -43.9563 | 2025-08-23 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8b95b0fe-7083-38a2-9283-bd0228ac3390 | -5.7431 | -57.5814 | 2025-08-23 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| a87bcde8-80f2-3484-b04e-3ca51ae5a295 | -5.7615 | -57.5807 | 2025-08-23 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a0b1a31e-8d11-381b-b5bb-779133d8c7d9 | -5.7614 | -57.6002 | 2025-08-23 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| db867c94-01bc-3c2f-9e50-058baaa6aa6b | -5.7429 | -57.6009 | 2025-08-23 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| f06c73a7-5523-36c5-ba24-c7652f1084fb | -8.9579 | -40.6311 | 2025-08-23 13:10:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 85c7a0a9-dfd3-3e0e-b253-29b22ae6f98f | -6.6044 | -44.5624 | 2025-08-23 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 8ac8cf8d-388d-34b8-92b3-d124b3b766bf | -9.1533 | -59.5027 | 2025-08-23 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 299.7 |
| a23e5010-4748-3679-a9f9-dc55c3af6202 | -12.5418 | -45.6189 | 2025-08-23 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| af23832d-e3aa-3117-b0dc-8329682db3db | -14.6899 | -54.912 | 2025-08-23 13:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 433fbd13-2174-3b4d-9811-2c899f38105a | -6.5856 | -44.564 | 2025-08-23 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| d64de555-1c89-398c-b51c-493000c19d35 | -2.0431 | -47.6935 | 2025-08-23 13:10:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a36cf174-b44a-3ce7-b160-f32588f48eb8 | -7.0164 | -44.6413 | 2025-08-23 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 1419f422-937e-3da9-929a-3d77edfbcd28 | -14.8098 | -45.4451 | 2025-08-23 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 5e555085-7c4b-379f-b476-808e0406dbba | -14.6902 | -54.8913 | 2025-08-23 13:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 020dbedc-05ec-34e3-aa52-60b791e7dbc1 | -7.6296 | -45.2464 | 2025-08-23 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 56eaa7ec-0bc4-3818-80e8-278939034c05 | -7.0352 | -44.6396 | 2025-08-23 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 65128942-9726-3afa-bfd2-4785bdf41c13 | -10.6201 | -50.1609 | 2025-08-23 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| bf98484f-f617-321b-b878-732b26bec4cd | -10.639 | -50.1589 | 2025-08-23 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f48c83dc-79e3-3637-91be-165f85543370 | -5.7614 | -57.6002 | 2025-08-23 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 820cab33-bb15-38bb-991d-12b94b50f940 | -6.1416 | -43.9563 | 2025-08-23 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 6aabdfbb-0670-33ed-919b-7a3c03c25ea6 | -6.0972 | -44.6947 | 2025-08-23 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| db491a6a-2694-3754-9c9f-16295cd0c4de | -15.0183 | -54.8942 | 2025-08-23 13:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 62cd22e2-79b4-3a99-b79f-681bb3e46038 | -6.1229 | -43.9578 | 2025-08-23 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 1c8ff92a-cac9-359f-985c-1b9c22a71244 | -12.1872 | -47.2128 | 2025-08-23 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4ca420c2-5d04-3646-ad9f-a1c6e41bb8a9 | -10.6393 | -50.1375 | 2025-08-23 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 319ad8ad-e7a8-36a8-ae6f-8675074439d2 | -5.7429 | -57.6009 | 2025-08-23 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b945f62d-ecd5-3517-888d-cac9ce1b2db8 | -12.1949 | -50.2397 | 2025-08-23 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 797e6b34-98d4-355e-8cce-696ea3baa387 | -5.7615 | -57.5807 | 2025-08-23 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 5b365edd-f59a-3fce-88d6-40e99b7f4f78 | -6.5856 | -44.564 | 2025-08-23 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| d228bff8-7588-3a9c-ab44-bd7670f39c6f | -6.389 | -45.5116 | 2025-08-23 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b2e2e00a-2418-39ec-b99a-2fc8ac4de07f | -10.6201 | -50.1609 | 2025-08-23 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 9a73258a-f289-3b14-b94e-80923e52c411 | -7.0352 | -44.6396 | 2025-08-23 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cb73fbec-e83a-3a4f-9186-3fd82b3c8faa | -9.1533 | -59.5027 | 2025-08-23 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 320.4 |
| b41fddaa-3708-3543-8ec0-0623108221db | -7.0164 | -44.6413 | 2025-08-23 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| cc54b22f-4e88-35eb-a513-5905b206cdb1 | -6.37 | -45.5356 | 2025-08-23 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 536c5d08-ab6f-3c5f-a4fb-ff9b891077a7 | -10.4784 | -46.831 | 2025-08-23 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 3bf798d8-b1c8-32ce-be9a-d35dd4684eb5 | -5.7431 | -57.5814 | 2025-08-23 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 87dd273b-3e87-320b-add1-8f9e5fb2296c | -6.6044 | -44.5624 | 2025-08-23 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d01f04c3-ad8e-300c-8899-7a6d40fab27e | -6.3698 | -45.5582 | 2025-08-23 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| c380fc97-83e2-3454-a973-a3e67e3bd053 | -14.7526 | -45.3857 | 2025-08-23 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c3e2e7fc-e4e2-3192-9926-d0f53edf26a7 | -6.3887 | -45.5342 | 2025-08-23 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 809d941a-125a-3e12-a7c2-e7ed51ead357 | -7.6296 | -45.2464 | 2025-08-23 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 396bc174-702a-3bc9-8da2-5c4d00cfd9ff | -12.5418 | -45.6189 | 2025-08-23 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 0472d139-7a44-3f51-a40f-971f9159ca61 | -14.6899 | -54.912 | 2025-08-23 13:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 99a2c9ef-71d6-3c57-8271-a8be98a39379 | -7.0352 | -44.6396 | 2025-08-23 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b769c000-1a44-3083-869f-319aee30b39e | -5.7614 | -57.6002 | 2025-08-23 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c84ce0bd-bf2d-3d48-bb40-de6760ca5102 | -5.7429 | -57.6009 | 2025-08-23 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| bb9fb63e-96c1-3e5c-8e01-454ac17559ba | -6.0972 | -44.6947 | 2025-08-23 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9d253417-0af0-3983-880b-28f28a43e9da | -15.034 | -56.3928 | 2025-08-23 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 4b15fcbb-4bb0-3723-936e-3c90a6353f6b | -8.527 | -48.8609 | 2025-08-23 13:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 83.9 |
| cf2904a4-8e4c-349b-8cd0-cdb017de190e | -6.5578 | -45.4757 | 2025-08-23 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5d34dd90-6cf6-361f-86a1-d6d4e02133ca | -5.7431 | -57.5814 | 2025-08-23 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 2f5a99ea-618f-3539-899d-6e6c61cd78ce | -6.9837 | -44.1847 | 2025-08-23 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f551d590-da77-3ad9-aae9-4c9edc90de34 | -11.1204 | -44.7681 | 2025-08-23 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3dd9e568-effb-35f6-ad29-44b89e89684f | -6.3887 | -45.5342 | 2025-08-23 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 75000d6f-87c5-32f7-972a-428655d10c14 | -14.7892 | -45.4954 | 2025-08-23 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| efa05cdd-bd91-3164-9f31-c6fd81c18913 | -12.9921 | -45.2252 | 2025-08-23 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 65dda32f-c1a3-30b2-8b2c-b0e3f48cad5c | -5.8309 | -45.1693 | 2025-08-23 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 3057c7e3-14f1-3f04-bb5a-47b1d89279d5 | -6.5856 | -44.564 | 2025-08-23 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 1b744601-bf26-3309-96ac-96908e0cdff0 | -6.37 | -45.5356 | 2025-08-23 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 4d89859d-199d-3cba-94a4-e331e7cd9668 | -6.3698 | -45.5582 | 2025-08-23 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| f9fc3de5-fc22-38d5-9abc-17b590b93b40 | -7.5206 | -44.9151 | 2025-08-23 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0bbd8320-6df3-3fba-a9be-49aafe1d1df5 | -7.0164 | -44.6413 | 2025-08-23 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 328ea00c-9fda-3d21-a965-702b72a58a7a | -5.7615 | -57.5807 | 2025-08-23 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |


[Clique aqui para ver as próximas entradas](README89.md)
