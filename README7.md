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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc1bdd3d-f7ad-3ca7-af76-c3a0b4292567 | -2.867 | -45.4182 | 2025-11-11 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 223.4 |
| b0e311ff-f341-33c2-8b92-796733198515 | -2.8669 | -45.4406 | 2025-11-11 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 233.0 |
| fa42cc12-bf9a-3301-98f5-f53625a5aad1 | -4.9223 | -44.3196 | 2025-11-11 01:10:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 828fbba9-019a-39b1-b6ef-2bd948f14a2a | -21.4568 | -48.7989 | 2025-11-11 01:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 51694bb3-7632-370c-a0d4-8321819ddff7 | -2.8484 | -45.4188 | 2025-11-11 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 2b9fb2e7-440c-3787-8a12-91357503cba8 | -2.8854 | -45.44 | 2025-11-11 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 182.7 |
| ec9e5539-ecb6-34c9-99ed-c46f6a33b42e | -2.6626 | -45.4251 | 2025-11-11 01:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 65d0ad47-b220-3a9c-9e23-5cde8e1f187b | -3.974 | -43.7763 | 2025-11-11 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| f09f07ad-fd6a-37b9-a45f-d83091fe7555 | -3.9554 | -43.7773 | 2025-11-11 01:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f7931ed8-3eb2-3e0e-8422-68749d6b6270 | -2.8855 | -45.4175 | 2025-11-11 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 208.4 |
| 6a6edc76-f7bc-3689-aa98-4fe9d592c955 | -2.8483 | -45.4413 | 2025-11-11 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 1d057673-2fab-3fd0-b2ee-7dd555bd7590 | -4.9034 | -44.3437 | 2025-11-11 01:20:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0ac1f4a2-37a5-332a-9535-c6b5b546ac84 | -4.9036 | -44.3208 | 2025-11-11 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 89eba13b-f25b-3940-9e3f-5ab0fe9c4108 | -2.867 | -45.4182 | 2025-11-11 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 260.7 |
| d2009b5e-f5a1-3ef4-b0ee-f609baf9f6fe | -4.9223 | -44.3196 | 2025-11-11 01:20:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 57e5bfdf-c153-3850-8835-30db3e058e60 | -2.8669 | -45.4406 | 2025-11-11 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 223.2 |
| 60cf13b3-d6be-3553-ad5a-525370657509 | -2.8669 | -45.4406 | 2025-11-11 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 0b4bb03f-671c-3eaa-9f33-c403160e4ccd | -4.9223 | -44.3196 | 2025-11-11 01:30:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5ead5ca5-0844-31d4-845f-d19a69904dbd | -2.8854 | -45.44 | 2025-11-11 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 82081521-48fb-3bc6-b8b4-69aec1cbe792 | -2.8855 | -45.4175 | 2025-11-11 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6c7dc659-6b89-3f05-b0b3-76dd103691af | -2.6626 | -45.4251 | 2025-11-11 01:30:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 693e1375-698b-30de-878e-3844ed735123 | -3.9554 | -43.7773 | 2025-11-11 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0029180c-5619-338a-a92f-afa6399fcb2c | -4.9036 | -44.3208 | 2025-11-11 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 43366529-99ec-3e26-a823-728db80f7839 | -2.867 | -45.4182 | 2025-11-11 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 867f450d-2f22-327e-ae46-67acd853269e | -21.961 | -49.9032 | 2025-11-11 01:30:00 | GOES-19 | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 3cc0b196-4d24-36cf-8d99-283d276f7b19 | -3.974 | -43.7763 | 2025-11-11 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 3cb57626-1826-3d84-98fe-ebef178532b1 | -19.742 | -58.0672 | 2025-11-11 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 662c69bd-2d46-332f-97ca-6f2029837c88 | -18.391001 | -54.9786 | 2025-11-11 01:39:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4b3743-c874-340b-82eb-332deffaf595 | -21.434099 | -48.792198 | 2025-11-11 01:39:00 | METOP-C | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e8aaa78d-3fd0-31ee-93f4-761ad794557f | -18.3881 | -54.967201 | 2025-11-11 01:39:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 412c7937-e375-3f62-916f-7756a17cbd23 | -19.7428 | -58.056099 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d2304e6c-292e-36f4-a8db-6b30e0c7f7a3 | -19.7526 | -58.053501 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ba619293-36be-3dd8-9fad-2bab4ca99533 | -19.785999 | -58.019699 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e7ecffff-1501-3dc1-8cf3-b9f4d87996fb | -21.9396 | -49.891201 | 2025-11-11 01:39:00 | METOP-C | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| efdc27f3-ba47-3ded-8e81-c5bb44b5ae33 | -19.733101 | -58.058601 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed5e62f0-e86b-30c3-a0b8-bb61787451aa | -18.477699 | -53.384102 | 2025-11-11 01:39:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 34076f32-7e93-3dfd-89d9-6b6b6ca7c99a | -18.4718 | -53.4011 | 2025-11-11 01:39:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2aa464cc-209a-3905-82f0-84b01e6fc854 | -21.936001 | -49.915001 | 2025-11-11 01:39:00 | METOP-C | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc7f3450-7f09-33bf-9bea-ce6007c54f12 | -19.8092 | -58.030499 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4d420558-2903-3034-a4ca-872367b27c6c | -18.468 | -53.386902 | 2025-11-11 01:39:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| df8b8e92-59c7-3e30-982d-2b7f67b2f787 | -19.753099 | -58.0116 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a93f784f-7f03-3605-b616-34265ac5cc3a | -21.945499 | -49.9119 | 2025-11-11 01:39:00 | METOP-C | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d536d18-19d9-3299-ad55-fd828e5d9673 | -19.7349 | -58.066399 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 47683476-7c4f-32a0-afc5-0028f70ab10d | -19.8074 | -58.022598 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7903e37f-62b1-37dd-a4ef-cae7878f5406 | -19.731199 | -58.050701 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3c281adb-5955-3271-98ac-802fcc4d8a98 | -26.604601 | -53.154598 | 2025-11-11 01:39:00 | METOP-C | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8b66ef5-84be-36af-933d-b176bb366f62 | -19.7409 | -58.048199 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 69c9c7d5-bd57-337e-8e19-1f98fcbc537c | -19.7647 | -58.016899 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 005a5b87-ab3a-38d4-83cc-9f1d7539991b | -19.7549 | -58.019402 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0e445e18-4c16-30d6-bbc8-a0fdabf8b3aa | -19.7446 | -58.0639 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4cf8668c-f087-36f7-9de1-1fe8bab72e4c | -19.787901 | -58.027599 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9381089a-e977-3ee6-b51f-74a0d49c16ea | -19.7507 | -58.045601 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af7f742e-47cc-3c2f-ab0e-6917b3ed8bd3 | -19.797701 | -58.025101 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 274109e8-b1cd-3511-a3cb-42d634f7e6c6 | -19.762899 | -58.009102 | 2025-11-11 01:39:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5d202f8e-83ca-3e9a-8053-b1e1a5652df7 | -21.930099 | -49.894299 | 2025-11-11 01:39:00 | METOP-C | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c3f83ff-3998-3667-a021-f3f405c8f0d5 | -4.7204 | -46.4497 | 2025-11-11 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 28c8819f-cd5b-3492-97bc-9ee00337615d | -3.974 | -43.7763 | 2025-11-11 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b0cc35be-91da-39ba-aac9-681d63585089 | -2.8855 | -45.4175 | 2025-11-11 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 300e87fb-d0ff-3ef1-8832-9a65a3abfdff | -2.6626 | -45.4251 | 2025-11-11 01:40:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| bba74e0f-8e00-3008-8b05-60bd7f2c23b4 | -2.867 | -45.4182 | 2025-11-11 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 95456ac5-1804-3028-a2a8-89bb274bee94 | -3.9554 | -43.7773 | 2025-11-11 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| d681a778-6ecb-33f6-ad02-6c189b2d258a | -19.742 | -58.0672 | 2025-11-11 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| c600ae7d-4764-3efd-87f4-1e931b420998 | -19.73901 | -58.04501 | 2025-11-11 01:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.7 |
| c3c922ab-44be-3c30-972a-5ab8a99114d3 | -19.74267 | -58.06858 | 2025-11-11 01:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 820c5b11-9d52-35e0-a433-f521281d8608 | -19.74472 | -58.07498 | 2025-11-11 01:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| cb14d6b9-3b10-34e4-9450-0efd46158bd1 | -5.4241 | -44.6524 | 2025-11-11 01:50:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 7af62e21-d171-31ec-a54d-4ffa7dfa3401 | -4.9036 | -44.3208 | 2025-11-11 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6dd69dc6-4a01-3757-9356-aced9fa360b7 | -4.7204 | -46.4497 | 2025-11-11 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 2c930b08-8cd5-34b1-a0af-f1deff5f170d | -3.9554 | -43.7773 | 2025-11-11 01:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 54850666-5f82-3e72-be0c-f1ec300b2e9e | -3.974 | -43.7763 | 2025-11-11 01:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 44a01673-f419-39a7-a179-37abb14b3f8e | -2.867 | -45.4182 | 2025-11-11 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 19ea1194-ec2d-381a-9bcc-2e744a3ce9b0 | -5.6436 | -41.0629 | 2025-11-11 01:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 31e93d9e-c809-3934-b3e6-5534fa4688f9 | -2.8855 | -45.4175 | 2025-11-11 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 02dbdbe2-10d3-36f9-8158-0c0d69820347 | -19.742 | -58.0672 | 2025-11-11 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| ed309294-d91b-3138-bd60-f567195b5601 | -2.8669 | -45.4406 | 2025-11-11 01:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1f800ee1-83aa-30d9-a205-49db4a841b47 | -19.7424 | -58.0465 | 2025-11-11 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| d39542b2-e8b7-337e-b53d-bda7afe165f3 | -3.974 | -43.7763 | 2025-11-11 02:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a9b59b99-7f26-3c4c-b576-db7fffae8e1b | -19.742 | -58.0672 | 2025-11-11 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| aa18d6d3-623b-3eb3-a3bc-02f58d1c0f5e | -4.9036 | -44.3208 | 2025-11-11 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 37656fb7-d680-3a73-a45f-9f69a33f91a2 | -4.7204 | -46.4497 | 2025-11-11 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 40afe9ab-305e-33ba-8ad6-f370169c1141 | -2.867 | -45.4182 | 2025-11-11 02:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d0032bdc-2500-32c5-9b36-045e78bef4c9 | -3.9554 | -43.7773 | 2025-11-11 02:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 6d49033d-bb27-3e68-9cb6-d75adf5bf56a | -9.6295 | -40.3392 | 2025-11-11 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.4 |
| e28f6cec-7a38-3147-9e8c-e028bb1c8823 | -2.8669 | -45.4406 | 2025-11-11 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 0c82c844-01de-3d6b-b6d4-bb9ba1ff77bf | -2.8855 | -45.4175 | 2025-11-11 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 23c34e0f-7f93-3231-9328-043e4269039a | -2.6626 | -45.4251 | 2025-11-11 02:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 96fd09d0-f299-3223-a5a7-b2eb7412b325 | -2.867 | -45.4182 | 2025-11-11 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 945c6809-967b-3394-b95f-5c549fce41d8 | -2.8669 | -45.4406 | 2025-11-11 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 8d5e1044-2cc0-354d-be20-ca34e4a9507d | -2.867 | -45.4182 | 2025-11-11 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 41.4 |
| cb3d83ce-3e37-34a4-9f73-58b7ec918449 | -4.7204 | -46.4497 | 2025-11-11 02:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 400fc4e2-0328-3b07-b9a1-d7f25bf4ec93 | -5.4241 | -44.6524 | 2025-11-11 02:40:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b76442bd-14d3-3e0c-9d53-aeb0fd10a72a | -18.4026 | -54.9913 | 2025-11-11 02:50:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 1f9b94ae-9a05-3e91-b83f-5e3f6a815f0f | -4.7204 | -46.4497 | 2025-11-11 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d585ffbf-8345-3e54-a7f5-e9b08da4d1f6 | -5.4241 | -44.6524 | 2025-11-11 02:50:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ff16d49e-c41d-3f68-8248-92ce149c12f9 | -19.742 | -58.0672 | 2025-11-11 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 67d93656-9470-3ee6-b303-94f1f3d0ffa3 | -18.4026 | -54.9913 | 2025-11-11 03:00:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 5c589152-4af8-323a-9d8e-da2c32c9eef6 | -5.4241 | -44.6524 | 2025-11-11 03:00:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 404c8b84-824a-3b64-8dc1-c4e354cedfe0 | -4.7204 | -46.4497 | 2025-11-11 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ee324672-26a8-3668-a429-d10017d8dda2 | -5.6436 | -41.0629 | 2025-11-11 03:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| d91e072a-a0b9-37c3-9532-3cb4e1c411de | -4.7391 | -46.4487 | 2025-11-11 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 44.9 |


[Clique aqui para ver as próximas entradas](README8.md)
