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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1597997f-c182-3a3f-b71b-619d80928b8a | -20.4035 | -45.6162 | 2025-08-23 07:40:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9398e6a6-15cf-367d-be08-ff22bc99f3ab | -7.0164 | -44.6413 | 2025-08-23 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6b0f673a-5d8f-31b2-8d5c-1f7018fd1412 | -9.9495 | -60.1754 | 2025-08-23 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c8105dec-ea2d-36b7-9943-0572fe6d8571 | -20.4042 | -45.592 | 2025-08-23 07:40:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| dfae3f5f-db0f-33cf-8788-c2b1ddc47abe | -5.7615 | -57.5807 | 2025-08-23 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cbba16fd-20a9-3882-8e16-455317ab89d4 | -5.7429 | -57.6009 | 2025-08-23 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| faeafdf2-ed36-3cce-8a76-6678869c3418 | -5.7431 | -57.5814 | 2025-08-23 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0c5188ce-7840-30b3-b1cd-d1a8c23a6bb9 | -12.9921 | -45.2252 | 2025-08-23 07:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ba10512a-c347-31e2-a3d8-d2558a8e364e | -5.7614 | -57.6002 | 2025-08-23 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 79946e70-0143-3b7c-a90f-43a8c65f4505 | -9.9493 | -60.1947 | 2025-08-23 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 4bd5ab56-4398-37b5-9248-2e088ae863da | -12.9921 | -45.2252 | 2025-08-23 07:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a596c627-be68-34d7-b078-27a75d46aa15 | -5.7614 | -57.6002 | 2025-08-23 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e665882e-4828-30e9-83ea-83e423d016e7 | -9.9495 | -60.1754 | 2025-08-23 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d3a7c2ca-fe35-3d42-bbbf-a32eca319115 | -7.0164 | -44.6413 | 2025-08-23 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9a700744-f052-3c4b-8cc9-7eaa5b261044 | -20.4042 | -45.592 | 2025-08-23 07:50:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e8beeabf-3c51-3713-b9ef-cee3e36f8d29 | -23.8764 | -47.3552 | 2025-08-23 07:50:00 | GOES-19 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| b24e80a8-38bf-3f6f-9ae6-46b5111457f5 | -5.7615 | -57.5807 | 2025-08-23 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9d7a52cd-a584-34b5-94b1-ee7fc18feeb6 | -20.4035 | -45.6162 | 2025-08-23 07:50:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 8256a30f-5924-30ac-a5b1-b88fb5b58640 | -5.7431 | -57.5814 | 2025-08-23 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 44cc4082-05eb-31cc-b77c-d2d16c7ac268 | -5.7429 | -57.6009 | 2025-08-23 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ac511dc5-177e-3d8a-afd4-6dc33a63c531 | -9.9493 | -60.1947 | 2025-08-23 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3e530dc5-e552-3524-a8c4-76b3aebf04d7 | -9.9495 | -60.1754 | 2025-08-23 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8163f9d1-ba9c-3f16-891b-146ca2aa8323 | -9.9493 | -60.1947 | 2025-08-23 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c2f8a722-e285-3cae-be1e-d1ad3345864e | -5.7615 | -57.5807 | 2025-08-23 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 4c32f11e-4478-38dd-9d3f-469f57e609e1 | -5.7431 | -57.5814 | 2025-08-23 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9a71208f-6704-388a-8412-8a21681fb04e | -5.7429 | -57.6009 | 2025-08-23 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 2d894e83-19b1-3416-bda2-4b0ce8239d21 | -12.9921 | -45.2252 | 2025-08-23 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 130df9f7-19df-3f59-bb46-3e467a5d80b8 | -17.0483 | -47.1451 | 2025-08-23 08:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8bb219e4-b0a5-3377-9a3e-6664b8af738a | -20.4042 | -45.592 | 2025-08-23 08:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| b1c8dd95-54b6-3c07-a381-a4e88068a153 | -12.9921 | -45.2252 | 2025-08-23 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| f87dd8a5-4f26-35b8-90d5-874a6443e91d | -9.968 | -60.1937 | 2025-08-23 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c14140da-5feb-3fb6-8c3c-8e8804c25090 | -5.7615 | -57.5807 | 2025-08-23 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b9064559-ec7e-3b4f-988b-45632020e541 | -5.7429 | -57.6009 | 2025-08-23 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f3e2abdc-8ec4-3f16-8da1-5aa4c1c00280 | -20.4035 | -45.6162 | 2025-08-23 08:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| ffa8b10a-687f-3891-9e0f-6a143d9b67e6 | -5.7431 | -57.5814 | 2025-08-23 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4e4f915f-c7ca-3a63-8971-0f541e672efe | -9.9493 | -60.1947 | 2025-08-23 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| de009a2d-8ab4-3c8d-bdc6-eaa39cefa4f7 | -7.0164 | -44.6413 | 2025-08-23 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 684035e6-1e02-3bcf-a389-e6b2009d2a81 | -5.7614 | -57.6002 | 2025-08-23 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| dbd41d19-a49a-3ca9-8b81-dd2ee7e9bede | -14.2744 | -58.5266 | 2025-08-23 08:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 13b071bb-5936-3a62-ac80-8fc6851c0302 | -9.9493 | -60.1947 | 2025-08-23 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d2fdba71-72b6-3a19-bc04-815da7404533 | -5.7431 | -57.5814 | 2025-08-23 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 18e4e9b5-a123-3bca-840c-68a085f7ad30 | -7.0352 | -44.6396 | 2025-08-23 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0f4fa196-ceed-3328-943a-de8c4b53b3d8 | -20.4035 | -45.6162 | 2025-08-23 08:20:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ddf8a37b-fa7e-35d4-8961-ce4d6de0f7c9 | -9.968 | -60.1937 | 2025-08-23 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d167939f-117d-30b7-adfa-a7e7aba90c7d | -5.7429 | -57.6009 | 2025-08-23 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 62516962-8960-3c9b-a6a5-7720699055f8 | -14.2747 | -58.5066 | 2025-08-23 08:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| f9bf2323-3d04-3c9d-a0f8-01aebeab5732 | -12.9921 | -45.2252 | 2025-08-23 08:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 0cc62d64-a18f-31cb-9844-dcf2db7a5790 | -20.4042 | -45.592 | 2025-08-23 08:20:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 6d041d23-f47f-3847-a7cb-4d2ea6a7d94f | -14.2744 | -58.5266 | 2025-08-23 08:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 44153549-c266-320c-9a8c-52b58891da19 | -5.7429 | -57.6009 | 2025-08-23 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e4b027cb-af88-3399-be08-9413954dfbb1 | -20.4042 | -45.592 | 2025-08-23 08:30:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1b78119c-f8cd-36b7-8a19-ef638f719c65 | -20.4035 | -45.6162 | 2025-08-23 08:30:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4330f882-1486-3f12-a8c0-1f75fe196cff | -14.2744 | -58.5266 | 2025-08-23 08:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1e40d89d-29bd-3c0d-b59c-5a958e264378 | -9.9493 | -60.1947 | 2025-08-23 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4327f730-19b7-3a62-9289-5fc78dfb42eb | -14.2936 | -58.5249 | 2025-08-23 08:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 8de710b7-9592-36ba-98dc-96c78f3129d9 | -14.2747 | -58.5066 | 2025-08-23 08:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 68cc91ca-8097-3e6e-9ff4-852e96810162 | -5.7615 | -57.5807 | 2025-08-23 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e1adb29a-9757-3cdd-b515-037fde3019a3 | -9.9495 | -60.1754 | 2025-08-23 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b1fdf201-c41b-3193-b7c3-08aa3a6ce220 | -12.9921 | -45.2252 | 2025-08-23 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| f220f58f-a4c8-3b2b-85a3-d278a70da8d5 | -5.7431 | -57.5814 | 2025-08-23 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 81abb089-6ccb-3391-97b5-8a43ba2f67f2 | -5.7431 | -57.5814 | 2025-08-23 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8d7cbecf-bd1b-3d71-9d1b-73f2e52081fc | -5.7614 | -57.6002 | 2025-08-23 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ead329c8-c04c-39b4-8ca2-3c95faab15a3 | -9.9493 | -60.1947 | 2025-08-23 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 798537d2-ac7d-3a23-9197-8e163f1ef4a7 | -5.7429 | -57.6009 | 2025-08-23 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| da58c8b8-5240-3c60-90d6-e4261696c768 | -20.4035 | -45.6162 | 2025-08-23 08:40:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 8c2a378e-251c-37cd-8195-32e85112d5ec | -14.2744 | -58.5266 | 2025-08-23 08:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 87379408-f633-3097-89c1-fbdcf0b13d20 | -20.4042 | -45.592 | 2025-08-23 08:40:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 12a77cad-3a49-3412-b314-a84df7fe7528 | -5.7615 | -57.5807 | 2025-08-23 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f651bde4-c5e3-3cb7-baff-e8054f72e949 | -9.9493 | -60.1947 | 2025-08-23 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 390a16bc-e194-35a8-b9d0-8363324c05f8 | -5.7429 | -57.6009 | 2025-08-23 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| d45e5f76-53a9-30ab-a7ed-285283db3bdd | -14.2744 | -58.5266 | 2025-08-23 08:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 99e58c72-cc82-3038-9aeb-cb65fdf8883e | -5.7431 | -57.5814 | 2025-08-23 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 509c50bc-fd3b-3d0a-b31f-56108cc5a702 | -14.2936 | -58.5249 | 2025-08-23 09:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f7c96d75-788d-32e8-95be-daecaa848e3c | -9.9493 | -60.1947 | 2025-08-23 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b66ac166-36c2-3163-bb69-b1272f54955c | -5.7429 | -57.6009 | 2025-08-23 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 8181f29d-b86b-372b-b4b5-ae27bbec1e00 | -5.7431 | -57.5814 | 2025-08-23 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| edef1333-f71e-37be-910b-c801a13718d8 | -5.7614 | -57.6002 | 2025-08-23 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 46fcb729-fd5d-3f05-87a9-c4c2f6b8bfeb | -5.7615 | -57.5807 | 2025-08-23 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3c3fc064-3b3d-363d-8ea4-8c164f201441 | -14.2744 | -58.5266 | 2025-08-23 09:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| dd5908be-1866-38b4-90cf-8ba3221613c4 | -5.7614 | -57.6002 | 2025-08-23 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0ee349a7-6da9-369f-a59d-e0511dbf4849 | -9.9493 | -60.1947 | 2025-08-23 09:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d8c8833d-34fe-3dca-a731-ed5c42e646d4 | -5.7431 | -57.5814 | 2025-08-23 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 77843aa6-d32e-3b44-aeee-85f37352ffc7 | -14.2744 | -58.5266 | 2025-08-23 09:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| a02c35e6-bc6f-3a80-80ad-d0b261785e40 | -5.7429 | -57.6009 | 2025-08-23 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0abd1c47-321d-31a9-a973-4b043e5b2424 | -14.2936 | -58.5249 | 2025-08-23 09:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 7a30f982-f902-3d5d-b36b-8b8805d6d99c | -5.7615 | -57.5807 | 2025-08-23 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fdedd075-3f76-3ce3-93dc-c831dd4cc6f0 | -9.9493 | -60.1947 | 2025-08-23 09:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 3fdf378a-6323-3e94-b721-6eb26bdc78a2 | -9.9493 | -60.1947 | 2025-08-23 09:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ee0ddc76-6f52-33db-aa0f-3ac8d6f0ae1c | -5.7429 | -57.6009 | 2025-08-23 10:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c688658b-5f6e-38c3-8795-cfe764e5a603 | -5.7431 | -57.5814 | 2025-08-23 10:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 088161ce-dd04-3c5c-aaff-d1eff031c5d3 | -5.7431 | -57.5814 | 2025-08-23 10:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e0a4d345-e46b-3b37-81a3-13e297fa2dd2 | -5.7431 | -57.5814 | 2025-08-23 10:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| ac32cf6a-a31c-3948-adae-32476b0bef2e | -7.0164 | -44.6413 | 2025-08-23 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3e036881-a1f9-3441-bec4-d8889ae98576 | -14.0842 | -43.9103 | 2025-08-23 11:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 290466e5-79b5-3201-9e0d-f6ce424d03c2 | -7.0352 | -44.6396 | 2025-08-23 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d9b6db3a-8766-3939-909e-61bb8810987f | -5.7429 | -57.6009 | 2025-08-23 11:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 47ddeec2-c06c-332c-9046-ee76ce0e4a6b | -7.0164 | -44.6413 | 2025-08-23 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| cc464a1e-b68e-3623-bd87-1f0d009e3b9e | -5.7431 | -57.5814 | 2025-08-23 11:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| b897b56e-fb27-3607-b86f-d9d82ce2b9f8 | -5.7431 | -57.5814 | 2025-08-23 11:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| ba833ce8-a620-31a3-801b-88e9c2053fd6 | -14.0842 | -43.9103 | 2025-08-23 11:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |


[Clique aqui para ver as próximas entradas](README85.md)
