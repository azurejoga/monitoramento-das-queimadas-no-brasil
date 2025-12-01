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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cef8b43-715f-355b-a279-763291fa7f24 | -4.3876 | -43.3595 | 2025-12-01 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 9d8a0a14-4800-3474-86a2-c068625a305b | -4.3889 | -43.173 | 2025-12-01 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 26e239b1-a1f8-33d2-8ed6-5335f4784312 | -4.3892 | -43.1263 | 2025-12-01 01:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| d35f17d8-7809-3c73-a741-16d90e4e7dbc | -3.7007 | -45.9223 | 2025-12-01 01:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c4cee3f0-431d-3348-85c9-98e0871d7f3c | -4.389 | -43.1497 | 2025-12-01 01:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 290.0 |
| 102d97af-30b9-3a26-aa04-f2f58bde4e72 | -3.6009 | -47.2521 | 2025-12-01 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ea49c42f-99f1-3dc4-b897-78eff95a0b33 | -3.6008 | -47.2739 | 2025-12-01 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 1d01066b-3323-3d63-b585-5cc710f83260 | -3.9243 | -45.8451 | 2025-12-01 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8c3d3940-6ced-3e14-875e-69a16268cb16 | -4.4064 | -43.3351 | 2025-12-01 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4b39a6b3-6a41-3b85-9bcf-7dca8c4c5508 | -3.7195 | -45.8992 | 2025-12-01 01:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 4dd2a1e9-aae2-3037-b776-b776342f1d23 | -3.7007 | -45.9223 | 2025-12-01 01:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 03493e6c-fdce-3cc8-9ee1-18864fd2badf | -4.3889 | -43.173 | 2025-12-01 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 41af8f02-29ba-38ae-b385-bf1f931d2bde | -20.0142 | -57.4484 | 2025-12-01 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 85183bc7-893f-39fb-ad93-33952cc07858 | -3.9428 | -45.8666 | 2025-12-01 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 45ca8157-edce-3fb2-9ba3-ec1d8cc1b093 | -21.8558 | -44.5676 | 2025-12-01 01:20:00 | GOES-19 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.8 |
| 807a0328-700d-34b6-acee-8d13946647d6 | -4.3702 | -43.1741 | 2025-12-01 01:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 71eeb633-edc8-343b-85cd-8eb6c02b9398 | -4.389 | -43.1497 | 2025-12-01 01:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 207.3 |
| f2a5ea3e-9b3a-3e1a-9606-389a7e907c1d | -4.3879 | -43.3129 | 2025-12-01 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 03c8a3a4-adac-36c5-becd-303a5f8904bc | -4.5987 | -45.2035 | 2025-12-01 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e19afaee-5971-3471-980a-c39f1ed88c4c | -4.3703 | -43.1508 | 2025-12-01 01:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 9ab81e8d-6347-3681-a3b7-9f598c909bbc | -3.7009 | -45.9 | 2025-12-01 01:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 3f4f6c28-1d6a-3b3e-a3fe-b6591c8fe7e9 | -3.2174 | -50.139 | 2025-12-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9271eadd-4618-375b-9115-8b904ecd44cd | -4.3876 | -43.3595 | 2025-12-01 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 50ba0848-1bf6-3d9c-a0d1-c3e9fb1082d6 | -21.855 | -44.5925 | 2025-12-01 01:20:00 | GOES-19 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 28d7ebd1-b877-3484-8312-f74c4f3d38ea | -4.3705 | -43.1274 | 2025-12-01 01:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| acf15c86-374c-39ee-857f-cc972d3e9caf | -17.5141 | -57.1925 | 2025-12-01 01:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 6f27a783-8ed6-325d-8933-e6c7e2b1b6d8 | -4.3877 | -43.3362 | 2025-12-01 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| bd6dcff2-88f5-3fb4-b410-60efd2c80261 | -3.9429 | -45.8442 | 2025-12-01 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 90e1916e-b756-31b3-b8c6-1692f8b06128 | -4.389 | -43.1497 | 2025-12-01 01:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 86d5d25f-aabd-3cf4-bde9-f491c18877c0 | -4.3879 | -43.3129 | 2025-12-01 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5c09e62f-d647-3fb9-aa9a-612e15b84439 | -20.0142 | -57.4484 | 2025-12-01 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 2fc1b40f-c073-32eb-9150-be889fa2a897 | -3.2174 | -50.139 | 2025-12-01 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 96ff0de3-8ffc-39fc-afb4-cbb8c85165b8 | -4.3889 | -43.173 | 2025-12-01 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 45d703a4-0966-386c-b0ba-26352c5d220e | -3.7195 | -45.8992 | 2025-12-01 01:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| a0c0fe65-5870-36c0-8847-be642bc1809f | -4.3702 | -43.1741 | 2025-12-01 01:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e0c1bcf6-8953-3990-aa63-917a4b35cf66 | -4.318 | -45.3768 | 2025-12-01 01:30:00 | GOES-19 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c70fe117-95b3-343a-a4db-4a65798e4992 | -4.3703 | -43.1508 | 2025-12-01 01:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 179.4 |
| a3d3c198-cd80-3480-a55f-a5e1d4c0fbd1 | -3.7009 | -45.9 | 2025-12-01 01:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 123.6 |
| bca51d90-81cf-3403-ac24-8eb67b55f10b | -3.7007 | -45.9223 | 2025-12-01 01:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 91649d7f-da4b-3df9-9fdb-348f644cff7f | -4.3877 | -43.3362 | 2025-12-01 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 79f7cf06-3299-3f0a-8dc8-bd7ba0e571a4 | -4.4064 | -43.3351 | 2025-12-01 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 91d8101c-e756-3184-88f4-5762438c2b72 | -4.3889 | -43.173 | 2025-12-01 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| df8b4f32-9197-31fb-aa10-a696b43b307f | -3.6008 | -47.2739 | 2025-12-01 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e18b51db-9ea3-374a-9caf-b0a975d919d5 | -4.3877 | -43.3362 | 2025-12-01 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 73d5882a-404c-3344-b15f-0fa15849b34f | -4.3879 | -43.3129 | 2025-12-01 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b50f1ce5-8c33-30e7-8509-94cd2e43d33f | -3.2174 | -50.139 | 2025-12-01 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3e5194f7-6f79-38c0-b77a-4a2f377910d4 | -3.7195 | -45.8992 | 2025-12-01 01:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 68655774-b26e-3291-a9a4-08d16ccce9e3 | -4.3702 | -43.1741 | 2025-12-01 01:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 3f43fe88-8c6a-3f39-ab78-fc4efcf85627 | -3.7009 | -45.9 | 2025-12-01 01:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 8cbaed55-c4ce-35fb-9092-aab2c64cf4e5 | -2.2534 | -45.6167 | 2025-12-01 01:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 55d027c8-3bae-3c52-bb45-de0f983737f8 | -20.0142 | -57.4484 | 2025-12-01 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 733be000-1d8e-32be-910f-08c7de4a86af | -20.0145 | -57.4275 | 2025-12-01 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| d6ce6107-bac9-3130-ae69-8e1dda053e4f | -4.389 | -43.1497 | 2025-12-01 01:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 233.4 |
| 89f1e631-4dc9-30de-9edb-cbbfdc074db6 | -4.3703 | -43.1508 | 2025-12-01 01:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 232.9 |
| b89f8512-1ea9-3656-849b-07432f1284c4 | -4.4064 | -43.3351 | 2025-12-01 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8b7ffc3e-245d-30fd-88ca-42b45534ac22 | -20.02529 | -57.43436 | 2025-12-01 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.2 |
| e5d692b3-c7dc-3ee9-a27b-70af1cd1fc2a | -20.01678 | -57.44152 | 2025-12-01 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 322be924-9707-36cd-80bd-f19bf8b4ada7 | -20.00954 | -57.43793 | 2025-12-01 01:47:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 031ec555-67ea-3745-a41d-0e8834e5f915 | -21.855 | -44.5925 | 2025-12-01 01:50:00 | GOES-19 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 8b897998-ada1-3b8a-80da-f9a8f2129cd5 | -4.3889 | -43.173 | 2025-12-01 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 972a1a0d-0650-3c24-b84a-86a5e657b3eb | -4.3702 | -43.1741 | 2025-12-01 01:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| a71cfb1d-78c0-3ab4-869b-f3c696e1ac10 | -20.0142 | -57.4484 | 2025-12-01 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| e85ca860-9f07-3466-80f2-17f08980ea97 | -4.3879 | -43.3129 | 2025-12-01 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 42e95071-dafb-38fd-893f-4d3b4dfc6f14 | -3.2174 | -50.139 | 2025-12-01 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1f6e1b64-1768-3d08-8fb9-d1893df2490b | -4.3703 | -43.1508 | 2025-12-01 01:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |
| a745d12e-8488-3b64-8d63-e3f32cede676 | -4.3877 | -43.3362 | 2025-12-01 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| a03c1b04-4790-3ea7-b41b-caa8b40a6d23 | -4.4064 | -43.3351 | 2025-12-01 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b06074da-1ed4-30a5-ac58-4049e718adb3 | -3.7009 | -45.9 | 2025-12-01 01:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 4528572e-98e5-3c8d-879c-7b2590aef56d | -20.0145 | -57.4275 | 2025-12-01 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| fc31090f-e928-3d78-8724-9784d92f0010 | -4.3876 | -43.3595 | 2025-12-01 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 782151dd-a95b-302e-b679-5e3a6d6ad73b | -3.7195 | -45.8992 | 2025-12-01 01:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ad00c1e5-f4e9-34bb-864b-dbe47830ff36 | -3.6009 | -47.2521 | 2025-12-01 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f3f56e9f-ee6b-3e86-9943-71a9a0d64e1e | -3.6008 | -47.2739 | 2025-12-01 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b9f7c3b2-38f0-33ca-b248-88251cdef25e | -21.8558 | -44.5676 | 2025-12-01 01:50:00 | GOES-19 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.1 |
| be86e37e-ef51-39ea-b6ec-9c16ec6a1813 | -3.7007 | -45.9223 | 2025-12-01 01:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0d9c8b88-f8e3-316c-85fd-4ea02f0b6c9c | -4.389 | -43.1497 | 2025-12-01 01:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d485d4c9-400b-308c-914b-df2431f44a99 | -3.7009 | -45.9 | 2025-12-01 02:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| dd325788-9888-365c-a902-e53201daf3a4 | -4.4064 | -43.3351 | 2025-12-01 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d14db926-7cf1-3a7c-841e-58e7c856bcad | -3.2174 | -50.139 | 2025-12-01 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a0fbe6be-75f3-3b8f-a9f5-7a54ca7547ab | -20.0142 | -57.4484 | 2025-12-01 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 73808fdc-771f-3561-a71e-99d8e3903b04 | -21.8558 | -44.5676 | 2025-12-01 02:00:00 | GOES-19 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| acf7db52-1a02-3b2e-b2d9-276752533aca | -4.3702 | -43.1741 | 2025-12-01 02:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 6c11ed98-acbb-3e7b-be65-dcf1ddc7433f | -3.7195 | -45.8992 | 2025-12-01 02:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| fdf7a562-dbcb-3408-9d1e-3d2446d86d7c | -21.855 | -44.5925 | 2025-12-01 02:00:00 | GOES-19 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| 2cdc4c99-e627-389d-be17-f30c9f25e00c | -4.3889 | -43.173 | 2025-12-01 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4ab65510-057a-3b90-be9d-30b45b1c0d92 | -4.3879 | -43.3129 | 2025-12-01 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c7094070-cb99-3c6e-b593-d58a18fc9d18 | -4.389 | -43.1497 | 2025-12-01 02:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 5ebe3f33-b3f4-3020-93df-d37edfbda7eb | -4.3703 | -43.1508 | 2025-12-01 02:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 91bc2bbc-3f37-3954-8009-75c0f787c2dc | -20.0145 | -57.4275 | 2025-12-01 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 9297744a-cb56-31ef-b60c-6b9cc90fc04a | -4.3877 | -43.3362 | 2025-12-01 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 15531b8f-d85a-359e-ae06-c450d40d286e | -3.6008 | -47.2739 | 2025-12-01 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b4f99114-39cc-38f1-aa5e-1146917e5081 | -17.5338 | -57.1901 | 2025-12-01 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 9e928ee0-8c5a-3bf3-8d94-9151444f0e0d | -4.389 | -43.1497 | 2025-12-01 02:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 51d1260d-b329-3e8e-b40e-6b85a2e92b76 | -4.3889 | -43.173 | 2025-12-01 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 805b665d-9418-335d-a69f-a832f2748e7d | -4.3879 | -43.3129 | 2025-12-01 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7b23385e-d731-3385-b7ba-c7610c2d73d8 | -2.2534 | -45.6167 | 2025-12-01 02:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 0bc0807d-e02d-3219-85de-a54d888e3c67 | -4.4064 | -43.3351 | 2025-12-01 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7f729770-cee3-3dea-a016-72ac0d37e90e | -3.7195 | -45.8992 | 2025-12-01 02:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 87bff0b9-41c6-3631-9583-cc5d7ab8621b | -17.5141 | -57.1925 | 2025-12-01 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| bd1b7d25-0ec8-3c0a-a99d-04779af13eb6 | -17.5341 | -57.1695 | 2025-12-01 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |


[Clique aqui para ver as próximas entradas](README6.md)
