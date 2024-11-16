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
| 3d6f0003-a24e-362a-bad7-28261898ca75 | -6.1363 | -42.578 | 2024-11-16 03:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 556ef51e-7e7b-3940-a723-761addd544c7 | -2.1562 | -53.7039 | 2024-11-16 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 169d4b8b-46d5-3ecd-bab3-648360b0ef2e | -17.235 | -57.4516 | 2024-11-16 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.9 |
| 0d814b60-91d6-3be8-8173-5db7889644ea | -17.626 | -57.5692 | 2024-11-16 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 9bb081b4-57cd-3993-8b20-1e43a5c1b9d0 | -16.958 | -57.6269 | 2024-11-16 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 89513e4b-6218-32c4-9b50-437085181204 | -5.6606 | -35.6437 | 2024-11-16 03:20:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 67.7 |
| cbefd8c7-57d4-3e3e-bd0d-0fc2952db221 | -17.2347 | -57.4721 | 2024-11-16 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| bd0c3255-3100-3366-8d62-076911619a41 | -3.2008 | -45.5629 | 2024-11-16 03:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d92ac12b-f342-30f6-aa87-dd7a4b328718 | -3.2009 | -45.5405 | 2024-11-16 03:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6e2da10a-71a0-3a46-a6f3-01603421001f | -17.2547 | -57.4493 | 2024-11-16 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 1740a54b-8126-36d4-b84e-2aac56a8510c | -2.1562 | -53.7039 | 2024-11-16 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7f642fb7-b482-386e-80b9-1c80fe66f678 | -4.9971 | -44.3149 | 2024-11-16 03:30:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c07fbe81-1fbd-3578-9b81-a8cdb58e6221 | -16.9384 | -57.6291 | 2024-11-16 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 2003ab0b-b052-332a-bec9-5789a9d8ed8f | -2.2299 | -53.6018 | 2024-11-16 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4fec42a2-d71e-34fe-9344-76a4bee032b9 | -3.7394 | -45.6523 | 2024-11-16 03:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 354.7 |
| 9aca1dc2-f926-35bd-9a43-aa354b45a38a | -5.6606 | -35.6437 | 2024-11-16 03:30:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 1685537e-b464-3e03-a40d-2f8d9ee132f9 | -2.7801 | -48.5592 | 2024-11-16 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 00bb8431-7999-3557-a9ea-fa5c9aac342c | -17.235 | -57.4516 | 2024-11-16 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| ca7fad3f-8697-3e41-abf4-6e82cbeb0323 | -6.1363 | -42.578 | 2024-11-16 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| cb416fb4-d1a0-396a-9e9e-68d15c98cac6 | -2.5767 | -54.4188 | 2024-11-16 03:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 968b11e2-c104-3720-bd02-029d120b9211 | -5.6796 | -35.6418 | 2024-11-16 03:30:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 125.6 |
| aa01b81c-ca7e-32f4-a343-1f484e59ea64 | -3.7393 | -45.6747 | 2024-11-16 03:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 316746ae-1999-32fd-9de4-beb0a77cf6c9 | -6.0303 | -48.0376 | 2024-11-16 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 3635ac50-a9c9-3a2f-b048-8394e796b9d6 | -3.758 | -45.6514 | 2024-11-16 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 21f27cbb-22ae-3e5c-b476-6326e5850eda | -16.9577 | -57.6473 | 2024-11-16 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| bd7462d2-69da-317b-a722-56264bdf9d20 | -16.958 | -57.6269 | 2024-11-16 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 09584740-2118-376f-8864-8fb5085252be | -3.7208 | -45.6531 | 2024-11-16 03:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 53960011-fdd5-3e90-8eab-243aada1249c | -3.7207 | -45.6755 | 2024-11-16 03:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 073adf4d-1b17-38e9-887a-fa5e7b675c3e | -2.2299 | -53.6219 | 2024-11-16 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d4f6c065-236f-3663-b5a8-a5c448ae6e1f | -3.7395 | -45.6299 | 2024-11-16 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1a7ade92-4e7c-39d7-b02d-f591af5e5c91 | -2.78 | -48.5806 | 2024-11-16 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 4ba3a4b4-4446-3bbd-9f74-9defb84786f7 | -2.7986 | -48.5586 | 2024-11-16 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8bcf666a-329d-3a02-a4cc-992dd40576da | -16.9577 | -57.6473 | 2024-11-16 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 4d145d77-4fab-379d-a24a-2ac6c04fcc46 | -2.1562 | -53.7039 | 2024-11-16 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 3a53ca3a-c63c-3db6-8dcb-6a1f6ffef4a4 | -2.2299 | -53.6219 | 2024-11-16 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c1c8f30e-3031-384a-a324-1c10b695f162 | -3.7395 | -45.6299 | 2024-11-16 03:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 833976a5-5215-3e01-a901-eb476a36d7bb | -2.7801 | -48.5592 | 2024-11-16 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5fcd0f4f-25cb-30dd-b66c-305c8cd187a8 | -3.2009 | -45.5405 | 2024-11-16 03:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 29da5172-3daa-3d85-8e0f-9af40a8af0c1 | -2.78 | -48.5806 | 2024-11-16 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 4af3dffe-b5e5-3e26-aede-3e9e29412815 | -6.0303 | -48.0376 | 2024-11-16 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| a3e56ea6-ecaf-3f40-8bd5-6b8def2b620c | -17.235 | -57.4516 | 2024-11-16 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| e551ccf8-aa62-3be2-961c-05041c42d19f | -3.7393 | -45.6747 | 2024-11-16 03:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 185.0 |
| 4f7ae837-e96d-3113-9038-521e30b42a2a | -3.2008 | -45.5629 | 2024-11-16 03:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9ee9f3fd-0565-32e6-b766-771de855c82f | -3.7208 | -45.6531 | 2024-11-16 03:40:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c65fd1b2-1b6b-35f6-9651-0d0ff45b671d | -3.7394 | -45.6523 | 2024-11-16 03:40:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 399.7 |
| 24daf5e9-dd89-3640-a32e-ed2d07c55cf4 | -4.9971 | -44.3149 | 2024-11-16 03:40:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 38e581fa-56ed-30ea-ac6e-1484a9bc4afd | -16.958 | -57.6269 | 2024-11-16 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 752a4288-aff8-3229-b017-ba9f6672dde1 | -17.626 | -57.5692 | 2024-11-16 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 6b826e82-9335-32b6-a09b-1bc9b32a96b1 | -5.6796 | -35.6418 | 2024-11-16 03:40:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 139.8 |
| c6c33b41-e3c1-3008-bf57-cbbf40cf30a9 | -2.2299 | -53.6018 | 2024-11-16 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d3adfaa5-32f0-32ba-8862-b1c5e7a4f4fc | -17.646 | -57.5463 | 2024-11-16 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 3a214d5c-f4cf-32e2-965e-83dbb320220f | -3.5851 | -50.5255 | 2024-11-16 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7ff72679-0f60-35e6-a396-7efeefed75db | -16.9384 | -57.6291 | 2024-11-16 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| eed8cfef-340f-3626-bf6c-e3c250b25ec0 | -2.5767 | -54.4188 | 2024-11-16 03:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2afaff33-158c-3cf2-9921-ed8540de9180 | -17.2547 | -57.4493 | 2024-11-16 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| b3f9574b-6c3b-3789-a728-79be72a2faa0 | -3.2009 | -45.5405 | 2024-11-16 03:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c4239a51-2d75-37b4-a510-4e1a01c6e1b5 | -3.2008 | -45.5629 | 2024-11-16 03:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1ef646eb-29a5-307a-aea8-06bb20cacbd2 | -2.78 | -48.5806 | 2024-11-16 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 2aac5180-3018-3cbf-bd4a-2a1dc9da2fe7 | -6.0303 | -48.0376 | 2024-11-16 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f64408ab-efc4-32b9-af32-fe30874b1e9d | -2.7615 | -48.5812 | 2024-11-16 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| bf8fa3d4-48c3-3b08-9573-006d4e1fb802 | -2.5767 | -54.4188 | 2024-11-16 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3039b0b4-0a32-3acf-bbf0-f74ad7898b80 | -2.1562 | -53.7039 | 2024-11-16 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8a7c031b-145b-3e25-89fc-a57755dfe999 | -2.2299 | -53.6219 | 2024-11-16 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0047c948-d6ff-3cee-aa6e-2b06f6efb08f | -3.7394 | -45.6523 | 2024-11-16 03:50:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 307.7 |
| 7bfb205a-d0dc-3f8d-a9d8-4c32dc6c0c1c | -2.0271 | -53.9477 | 2024-11-16 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8a9e6a50-cec5-39c2-88d5-4679fe04219f | -3.758 | -45.6514 | 2024-11-16 03:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 226e63f3-db5d-3ceb-834c-887008124a10 | -17.235 | -57.4516 | 2024-11-16 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| c72ee940-11d3-3f32-a25b-fb2904651031 | -17.2547 | -57.4493 | 2024-11-16 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 247bcf4b-d430-3d80-bc0e-fd507e69f24e | -5.6796 | -35.6418 | 2024-11-16 03:50:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 9e9622f9-8d2f-323d-a3de-cb1d3c14eca0 | -3.7393 | -45.6747 | 2024-11-16 03:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 165.3 |
| b9cffb6a-63ac-35b9-8c4d-2f05cb4a234d | -2.2299 | -53.6018 | 2024-11-16 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 891b3af9-4733-3109-9906-4c8e8f5dfbab | -2.7801 | -48.5592 | 2024-11-16 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fcf7148c-a8fa-3e96-8b13-1d1344f564d8 | -3.758 | -45.6514 | 2024-11-16 04:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 73d8b9e0-c6e7-395e-ac67-542faad7a962 | -3.2009 | -45.5405 | 2024-11-16 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8700a475-6330-3493-8c09-99e396df7cd3 | -1.643 | -53.2677 | 2024-11-16 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e7ebffe9-a223-3aec-9abc-d30580b6494b | -2.7801 | -48.5592 | 2024-11-16 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ea2f8637-c453-35e9-aee9-edff946801a4 | -17.2547 | -57.4493 | 2024-11-16 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.5 |
| 65a9b32a-52a9-3132-bd44-7cc1bba34408 | -3.7393 | -45.6747 | 2024-11-16 04:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 6937ad53-3226-38c2-83a8-8f8223b09992 | -3.2008 | -45.5629 | 2024-11-16 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c4f5bb5a-2b69-3522-9311-9bc109e43705 | -5.6796 | -35.6418 | 2024-11-16 04:00:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 76.3 |
| c2648dcf-745b-3463-9124-2b31369aeae7 | -3.7394 | -45.6523 | 2024-11-16 04:00:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 172.2 |
| c2368ab8-52a4-3d0a-a951-92de148106a9 | -6.0303 | -48.0376 | 2024-11-16 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1664f097-3418-3e0b-b604-db6445b746e4 | -2.1562 | -53.7039 | 2024-11-16 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0ddfb5dd-9381-3e01-89b6-a2b05fb44a42 | -17.235 | -57.4516 | 2024-11-16 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.1 |
| 0ea91be6-5ef2-3bd7-8ddb-ea038ed96a13 | -17.5675 | -57.5351 | 2024-11-16 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 5bb86800-c7b3-3e3e-a1cf-a48a625a6b87 | -2.78 | -48.5806 | 2024-11-16 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 558a3f47-89cd-30d7-a113-398581e2b062 | -5.6606 | -35.6437 | 2024-11-16 04:00:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 4bb83a30-5291-32f3-9fed-246ba5800bf6 | -6.44444 | -47.86042 | 2024-11-16 04:01:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a140a1ef-9208-3f17-a32a-5729ddf83f2e | -6.86038 | -38.8882 | 2024-11-16 04:01:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dd7c07f5-a081-3d63-ac66-773ee8cecba6 | -2.34735 | -47.46935 | 2024-11-16 04:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ecc7a415-6571-3621-a643-a6e53061b777 | -5.24185 | -44.91335 | 2024-11-16 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81de7fa1-3d52-32a0-90ec-807b9040af80 | -6.02432 | -48.04237 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 750fb1c0-05ec-363c-8d12-c87b15802177 | -3.74159 | -45.66637 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 316973f6-e3b0-354e-98dc-1e7c89c0cf45 | -1.99549 | -46.57656 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 951f4333-4b05-39a9-817f-aec197b589ee | -5.00765 | -37.53834 | 2024-11-16 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2a5df16e-b2ce-3522-8bea-5bf7a2da63ee | -5.08129 | -42.56594 | 2024-11-16 04:01:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36321939-8aa6-3d5e-b639-cff9819681a7 | -4.2998 | -48.06925 | 2024-11-16 04:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df9a432f-5ed1-3656-a16d-f5db9c0d24dd | -6.24562 | -47.27412 | 2024-11-16 04:01:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df911c64-4092-3f2f-9516-3b3596c737a6 | -5.67526 | -35.65021 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 0ba655f3-4705-342d-a2d1-21590c4ea7d1 | -5.14413 | -37.70285 | 2024-11-16 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |


[Clique aqui para ver as próximas entradas](README16.md)
