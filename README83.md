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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc70bf2c-42d6-3d6a-a344-95ab5eb8e26e | -15.0196 | -54.88241 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1c0a3fa9-678a-353e-a4e9-6604302326c2 | -14.66213 | -54.92182 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5024b058-b9c2-3b00-98c7-49c7564e3e80 | -14.2832 | -58.52482 | 2025-08-23 06:22:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 68798483-8b09-36d1-bffe-2b12d4898f20 | -15.05412 | -56.39133 | 2025-08-23 06:22:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 316a2cb3-f6a8-35e2-a9e9-a785cefdd1e9 | -14.67684 | -56.61276 | 2025-08-23 06:22:00 | AQUA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6d81134d-fde2-3442-b76d-89310404c2c8 | -14.27916 | -60.38134 | 2025-08-23 06:22:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 8221c496-07fc-3597-8483-e607045941c1 | -14.29555 | -58.51418 | 2025-08-23 06:22:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 40fc996f-d123-317d-8ee9-fa13ba21bc38 | -14.67092 | -54.9232 | 2025-08-23 06:22:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ea02142d-e4a8-3d18-b3af-b3f334093755 | -15.02888 | -56.3804 | 2025-08-23 06:22:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb815b99-74ef-3a49-9081-37681f6ac05b | -15.54551 | -55.01148 | 2025-08-23 06:22:00 | AQUA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 63d1771d-12c6-3385-b38a-959d96f5fce8 | -14.28924 | -60.37009 | 2025-08-23 06:22:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 28b791e4-59bd-3272-a3bf-29cb156269ed | -25.56479 | -51.05696 | 2025-08-23 06:25:00 | AQUA_M-M | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 345bd0ef-84d1-3ca3-96a3-a27b88ed3ad3 | -5.7614 | -57.6002 | 2025-08-23 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 598be7ff-9aa0-3b15-a89f-4c9c092f6ab0 | -9.9493 | -60.1947 | 2025-08-23 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 7f7996ca-d81b-373f-a2de-5b6809d7dc5c | -15.0756 | -48.5181 | 2025-08-23 06:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 39.4 |
| bfd90b55-f4f1-3829-9cd6-1406e70ae698 | -9.9495 | -60.1754 | 2025-08-23 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ce4419c8-496f-396f-93ae-15ff2c06f5da | -20.4042 | -45.592 | 2025-08-23 06:30:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4933ebf8-575f-3340-a027-42009d15e3f2 | -14.2744 | -58.5266 | 2025-08-23 06:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f1347eb2-fcf0-3319-8b9f-a7abf828fc08 | -5.7615 | -57.5807 | 2025-08-23 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 07d8ee98-0063-3ffb-ad98-17f6ae6e9214 | -5.7429 | -57.6009 | 2025-08-23 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c4469043-c7b1-3c11-9132-066ab7c4fb21 | -9.968 | -60.1937 | 2025-08-23 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 92b9a4fb-7211-38c4-a221-ce4a2f75e03f | -7.0164 | -44.6413 | 2025-08-23 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9cf73abb-9e62-37b5-aee6-a78fc9f04f3f | -12.9921 | -45.2252 | 2025-08-23 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 30f2b1aa-fbe5-3719-96f7-b767821a01bd | -20.4035 | -45.6162 | 2025-08-23 06:30:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| bfeef1fe-720c-3c9f-8897-95c95958c0c0 | -5.7431 | -57.5814 | 2025-08-23 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f7ab7ba2-8a1e-3000-9375-ef596ed20674 | -7.73237 | -67.06827 | 2025-08-23 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25d778da-108b-3070-95b8-2f732c2c0880 | -7.73174 | -67.07308 | 2025-08-23 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a080184d-c8e2-344f-ac66-3d46d70d027d | -7.73853 | -67.06917 | 2025-08-23 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f1bfb61-739d-3ecc-b4a7-8478adb7bff4 | -9.56142 | -68.57814 | 2025-08-23 06:33:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34f6293a-8eb8-38f7-92f1-9ccf3a80972e | -7.7262 | -67.06739 | 2025-08-23 06:33:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35482838-c86f-3f13-b1c5-6d70263c0c61 | -5.7429 | -57.6009 | 2025-08-23 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 89682449-418f-34f1-9010-f38cf43c5dfe | -20.4035 | -45.6162 | 2025-08-23 06:40:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| b856eb0c-364d-39f9-9b72-50ab98534e65 | -9.968 | -60.1937 | 2025-08-23 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0cc33827-0ffb-3f40-a89f-94d371420e14 | -5.7431 | -57.5814 | 2025-08-23 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4177330e-b5ff-389b-a50c-ec0d9dbb503b | -9.9493 | -60.1947 | 2025-08-23 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 789158ad-7e22-342f-97f6-d5dbefce7e8a | -5.7615 | -57.5807 | 2025-08-23 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 91da5455-7239-3880-a947-e5e8bcee01eb | -14.2744 | -58.5266 | 2025-08-23 06:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 458d5634-7601-3edd-846f-337b19b55f85 | -20.4042 | -45.592 | 2025-08-23 06:40:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e61f9633-4cab-379f-9798-f1911ebc31b0 | -9.9495 | -60.1754 | 2025-08-23 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 94c42ce1-32db-36d7-afca-9802891821b1 | -12.9921 | -45.2252 | 2025-08-23 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 7915c9d8-526d-37d2-add8-d87ebff06320 | -7.0164 | -44.6413 | 2025-08-23 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8947f015-58c2-37f3-862c-6056780f2a19 | -5.7614 | -57.6002 | 2025-08-23 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d37cbcb0-de42-38ff-b1dc-110698198027 | -14.2744 | -58.5266 | 2025-08-23 06:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 8b9307f3-af79-3bd1-b62f-e1534e6e09ae | -5.7615 | -57.5807 | 2025-08-23 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7023efcc-c318-33a9-9599-6b1a4aee304f | -5.7429 | -57.6009 | 2025-08-23 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 56aff9b3-10a7-36c1-85c9-eec6b6f6a98d | -13.3723 | -47.5115 | 2025-08-23 06:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1c04a9df-b160-35ad-a44e-62580b8e740d | -9.9493 | -60.1947 | 2025-08-23 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 7c818492-45c0-3160-bea2-76db526fe783 | -9.968 | -60.1937 | 2025-08-23 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b15f0d5f-adb8-34de-82af-ce33af3ec6af | -5.7431 | -57.5814 | 2025-08-23 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6caa8499-da29-3562-9186-8feb9d958859 | -17.5785 | -46.5523 | 2025-08-23 06:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 45.0 |
| b2478074-6791-3d20-a49e-5db08baf51d1 | -5.7614 | -57.6002 | 2025-08-23 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 4953fd9d-6f98-3d4b-bf72-93db17628367 | -9.9495 | -60.1754 | 2025-08-23 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 93a50695-6fdc-30df-bf56-8286e028d7d3 | -12.9921 | -45.2252 | 2025-08-23 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 5a1fb706-43df-3faf-83be-89b82daef8d7 | -7.0164 | -44.6413 | 2025-08-23 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f662b41f-4014-3d8f-bed7-16e792027173 | -9.9493 | -60.1947 | 2025-08-23 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 9ddee0fd-d3a7-327e-8613-21f90bd24b94 | -5.7615 | -57.5807 | 2025-08-23 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e3031fc3-47d1-3697-a256-5a9122e52bd7 | -5.7614 | -57.6002 | 2025-08-23 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d0b090c4-1f64-3c47-b5ce-bfdced6f2c7d | -12.9921 | -45.2252 | 2025-08-23 07:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| cc988e57-6d31-3ad3-b173-3670dae022ef | -14.2744 | -58.5266 | 2025-08-23 07:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9dd71c9a-c34c-3fd7-bc45-57b0c0e3d4d6 | -9.9495 | -60.1754 | 2025-08-23 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5786ac82-994f-3567-b9a8-88ab4e38071e | -20.4042 | -45.592 | 2025-08-23 07:00:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 6a817dc3-63e7-3891-b772-5cca944b8b0e | -9.968 | -60.1937 | 2025-08-23 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5cb71c85-ca94-3f99-a252-17223cb3f531 | -5.7431 | -57.5814 | 2025-08-23 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 9f5919bc-43b6-3b8d-a00d-9218deb306f6 | -5.7429 | -57.6009 | 2025-08-23 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| c5d4da28-07ce-3576-98b6-0b6536a750e3 | -14.2747 | -58.5066 | 2025-08-23 07:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| df2b4dc6-aefb-3544-9eaa-61f8fa10082c | -20.4035 | -45.6162 | 2025-08-23 07:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f2d8cb1b-d519-3b11-ae4f-479b02a038e6 | -12.9921 | -45.2252 | 2025-08-23 07:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8194a290-2a51-30b0-8148-a9992b6a02a0 | -9.9495 | -60.1754 | 2025-08-23 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| f8aa7699-1441-3a4b-a175-a496142b5523 | -20.4042 | -45.592 | 2025-08-23 07:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a9959b61-d636-3a2c-a9e4-459e729b11ab | -9.9493 | -60.1947 | 2025-08-23 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 7a968309-f987-3151-90d3-ba1f69c98399 | -5.7429 | -57.6009 | 2025-08-23 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 5640ab92-fdc5-38a9-b052-e1bcb451ab8f | -14.2747 | -58.5066 | 2025-08-23 07:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 2328746f-6b3f-376d-b170-eb8035b50191 | -5.7614 | -57.6002 | 2025-08-23 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f8aca883-749e-339a-941b-9a98fb67095c | -7.0164 | -44.6413 | 2025-08-23 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e8745966-e25c-3401-8149-cd1b13901d99 | -5.7615 | -57.5807 | 2025-08-23 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8a3add6c-a1d3-3b2e-aafe-8df7649ac5a9 | -14.2744 | -58.5266 | 2025-08-23 07:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 9087a0bd-8461-33bd-8d64-fa9c437115b3 | -5.7431 | -57.5814 | 2025-08-23 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 2222139a-da4b-3c7c-b6b0-754e0f706683 | -9.968 | -60.1937 | 2025-08-23 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 82b85e47-1436-3498-8a21-3d834a505994 | -9.9495 | -60.1754 | 2025-08-23 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 20868134-8675-3633-9578-6d660094bff9 | -9.9681 | -60.1743 | 2025-08-23 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 515113e4-09a1-3250-8ea8-7c5f9d007fd8 | -14.2747 | -58.5066 | 2025-08-23 07:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7e23d3d8-842c-3288-8220-691c03b83797 | -14.2744 | -58.5266 | 2025-08-23 07:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 28facdbc-c978-3aa6-a575-fe6de78ba727 | -7.0352 | -44.6396 | 2025-08-23 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9ffeeaa3-2b5b-385b-99ae-9f3116b36452 | -12.9921 | -45.2252 | 2025-08-23 07:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| aa01344e-1081-3c37-ac45-7be669edd87d | -5.7431 | -57.5814 | 2025-08-23 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 15576636-b2e1-3856-b891-c1776cdf343e | -5.7429 | -57.6009 | 2025-08-23 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 20ca4a6d-0d1d-342a-bc70-9abdc9702bfb | -5.7615 | -57.5807 | 2025-08-23 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a904a153-4244-3aac-b98d-cdafc5bbc634 | -9.968 | -60.1937 | 2025-08-23 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a4da2c53-a427-3142-8c3d-00a81ac82cbe | -9.9493 | -60.1947 | 2025-08-23 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7abcf822-d9d5-3ea0-9b35-0da9a3742cbc | -20.4042 | -45.592 | 2025-08-23 07:30:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3995600d-da4f-3376-ab55-600d26d82c81 | -5.7615 | -57.5807 | 2025-08-23 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7d5c8346-1bb0-3847-9b76-a910bcc2f2b9 | -9.9495 | -60.1754 | 2025-08-23 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a9666f38-1f80-3e25-ae15-e93bcf5ddeea | -5.7614 | -57.6002 | 2025-08-23 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 3330b8cd-bcee-3b34-a2e2-99b21b144c0f | -5.7429 | -57.6009 | 2025-08-23 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4479b5d5-2233-39ff-a6d0-4dcb1fd63a51 | -7.0164 | -44.6413 | 2025-08-23 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7867bac7-ca01-37c2-8807-a0d50235eec9 | -12.9921 | -45.2252 | 2025-08-23 07:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| cc5279b5-e774-3a0c-9255-fa0e85d02e69 | -5.7431 | -57.5814 | 2025-08-23 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| e961d006-d82a-3bb5-9114-a603ef22a9ec | -9.9493 | -60.1947 | 2025-08-23 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9e75b3f5-b9b3-382a-b23f-5154e085a12a | -9.968 | -60.1937 | 2025-08-23 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| fcb4a9c8-322b-3d2d-806b-defec05e752b | -14.2747 | -58.5066 | 2025-08-23 07:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |


[Clique aqui para ver as próximas entradas](README84.md)
