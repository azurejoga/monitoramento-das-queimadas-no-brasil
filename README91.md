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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18355fd7-5ea8-31ad-817b-6541e058fc24 | -20.48307 | -47.17511 | 2026-09-24 11:30:00 | TERRA_M-M | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 25de36b2-186d-3b6d-a564-b3a75bae924d | -20.4846 | -47.16507 | 2026-09-24 11:30:00 | TERRA_M-M | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b352ba9-aab9-307a-a5ac-2ac6fdec2f55 | -18.8859 | -47.16599 | 2026-09-24 11:30:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| e17197bd-f84d-3f31-a05a-c64656597fb4 | -19.29392 | -46.97699 | 2026-09-24 11:30:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0dfd8ce-1032-323f-8270-efae5190e9d5 | -18.88432 | -47.17627 | 2026-09-24 11:30:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| dc967f06-29f0-3005-88ee-06e1b764fd47 | -10.9449 | -43.8614 | 2026-09-24 11:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 8dc35c77-7223-3f31-8608-0a293e8bbcb6 | -7.2881 | -45.5494 | 2026-09-24 11:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fcb459ba-5051-3757-b568-590d3538bea3 | -9.2415 | -47.3487 | 2026-09-24 11:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e202c9f6-c1a4-30fa-ba64-6beb7f7444d3 | -10.9449 | -43.8614 | 2026-09-24 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 9d6dfee6-b400-3100-881b-06b9c4e260e8 | -9.2412 | -47.3708 | 2026-09-24 11:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 6d7e93a3-8b07-3d33-8fd2-7b97630d940d | -9.2415 | -47.3487 | 2026-09-24 11:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1e4fe105-e9a4-3687-bbfd-eb4787ac3482 | -10.9453 | -43.8378 | 2026-09-24 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| d866f433-2e99-3ca3-ae77-37d804b7cda8 | -9.2604 | -47.3467 | 2026-09-24 11:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| aab2cb1a-6fec-388d-9778-64fa297260f1 | -10.0924 | -46.0005 | 2026-09-24 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| f1f6c58b-81c6-3b17-a411-c2634f8b5cd7 | -7.2881 | -45.5494 | 2026-09-24 11:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 40d9fd7d-940c-3e0e-84a3-5c7c6ea7d413 | -10.1297 | -46.0412 | 2026-09-24 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 22e36db2-f330-3ef2-9670-5f83d44592a8 | -9.2604 | -47.3467 | 2026-09-24 12:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| d36085a3-54f4-3391-bd18-16899a47678e | -9.2415 | -47.3487 | 2026-09-24 12:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| e405e66c-78a8-33c9-b1c7-a28c59569f48 | -7.2881 | -45.5494 | 2026-09-24 12:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ce7bf0e1-dc99-35f7-af96-36b801bc1aed | -9.5522 | -45.3611 | 2026-09-24 12:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 7f0a61fa-8d1c-3fc6-8ab6-f95eacb19987 | -9.2412 | -47.3708 | 2026-09-24 12:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| a03edab4-12a7-3732-8f9a-1400b0431f22 | -10.9258 | -43.8641 | 2026-09-24 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 54188f3f-69d6-37df-9d49-c8b88735b43a | -10.9453 | -43.8378 | 2026-09-24 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 91c5b3b0-dd38-3d0a-bcd5-457e15f5e95f | -10.9449 | -43.8614 | 2026-09-24 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 11c7cadf-e346-3da7-8e99-6387686b9064 | -10.9453 | -43.8378 | 2026-09-24 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 692b123b-ee1b-37fa-9054-ee9e285e4197 | -10.9449 | -43.8614 | 2026-09-24 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 390.8 |
| 5eb83518-ab0c-3c6e-a039-cd7dd739f153 | -8.7735 | -45.6303 | 2026-09-24 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b9bd0e52-c89d-3995-8c59-cb239c97529c | -8.3761 | -47.3023 | 2026-09-24 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3c7a280c-5668-3adb-883f-491c91fc2c65 | -10.9258 | -43.8641 | 2026-09-24 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 30c61d4b-f3e1-3cd7-a45e-1dbb166d0a48 | -7.2881 | -45.5494 | 2026-09-24 12:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 16f3bfbd-a34a-38d5-9ebb-a5443b9278a0 | -8.7738 | -45.6076 | 2026-09-24 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 209.8 |
| b4eda417-146a-3b3f-9d20-bd8c03b8e8de | -10.9641 | -43.8586 | 2026-09-24 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 0cbe9cb1-a982-3af6-816f-91f3d1789522 | -9.5522 | -45.3611 | 2026-09-24 12:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| cb718ec0-c86d-3edc-9f37-649435006c2a | -10.14 | -50.23 | 2026-09-24 12:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5915b4be-0aa7-3d14-902b-97be955e814f | -10.08 | -50.21 | 2026-09-24 12:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fdb0d44-cf69-3be4-900e-2bf6413566c5 | -10.08 | -50.15 | 2026-09-24 12:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 393e2200-ed70-35d7-b041-5cb05c5ca773 | -10.05 | -50.2 | 2026-09-24 12:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69df1aeb-b702-3dbe-8292-7b929201ae8f | -10.11 | -50.22 | 2026-09-24 12:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70f5736a-9daf-39fa-94c5-ecc3b162893c | -9.2604 | -47.3467 | 2026-09-24 12:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 12c0f540-f68c-33df-8586-a247328e914c | -10.9449 | -43.8614 | 2026-09-24 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 311.1 |
| 7dfc3698-53bf-314e-b33e-1327998e7047 | -10.9258 | -43.8641 | 2026-09-24 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| fee9935e-2dd7-3416-9a15-a9d00cb5b654 | -9.2415 | -47.3487 | 2026-09-24 12:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| a826a54d-fa78-3350-b1d4-7dd50313599f | -8.4307 | -47.4515 | 2026-09-24 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9cd81bde-875e-38b9-bfc3-9b371cf6cda6 | -9.6302 | -43.9219 | 2026-09-24 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 06a690b9-5fb8-3ab8-b81b-5f2efd311aa1 | -9.6111 | -43.9243 | 2026-09-24 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 17f2f7b5-792b-3d34-9517-2635b0175d6a | -10.9453 | -43.8378 | 2026-09-24 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 33c84ac3-3f72-3d4a-a6ca-d8f79c7fc39f | -9.2412 | -47.3708 | 2026-09-24 12:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 216a18bb-7ea8-3f1d-939b-a52dbb93dc31 | -8.9208 | -45.9084 | 2026-09-24 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 4ff35001-fad8-3e55-b8fb-78071820fa43 | -9.5522 | -45.3611 | 2026-09-24 12:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 2c34270f-c5ed-3423-a00a-c1d0d112bbe3 | -9.2412 | -47.3708 | 2026-09-24 12:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 0299b9c6-09ca-309e-8fc6-b4ae06177bc7 | -9.2604 | -47.3467 | 2026-09-24 12:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 3cb25a6a-6de8-3bda-aa5e-9f32448b2b31 | -9.6111 | -43.9243 | 2026-09-24 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| d968249c-8396-398a-a338-eae8e4057e9a | -9.2415 | -47.3487 | 2026-09-24 12:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| a1a77ffe-9383-3dbf-a214-8effafb5aec1 | -8.7735 | -45.6303 | 2026-09-24 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 039d76f9-9de5-334a-8d2c-d8b065bd7f9e | -9.6302 | -43.9219 | 2026-09-24 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 2f0fcf37-1dc9-3c2c-b2cd-816abd6f7aed | -8.7738 | -45.6076 | 2026-09-24 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 53698ea3-ac7c-36a8-9300-3016137efdf7 | -8.7738 | -45.6076 | 2026-09-24 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 5e25b593-7134-3b0d-8637-71a95b75abe0 | -9.2412 | -47.3708 | 2026-09-24 12:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a5959513-4b61-3e0f-9fc2-07df48c14f04 | -8.7735 | -45.6303 | 2026-09-24 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1658d2d5-4e53-342b-87db-5acd982df70c | -9.6302 | -43.9219 | 2026-09-24 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 0c31ec5d-c56f-3853-9e81-e0b137b55177 | -9.2415 | -47.3487 | 2026-09-24 12:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a835c627-8bb9-374d-a799-edc976827e9e | -9.6111 | -43.9243 | 2026-09-24 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 11f397a5-b902-3615-9329-363f0d7ec6b5 | -9.2604 | -47.3467 | 2026-09-24 12:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 1262c7f9-0781-3ce2-8384-22d5dddba38f | -8.3761 | -47.3023 | 2026-09-24 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| cccbcadc-a940-3223-a655-504a0f69a588 | -9.2415 | -47.3487 | 2026-09-24 12:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| e4b2dffd-78ec-3dd5-b585-67b92a0148da | -9.2604 | -47.3467 | 2026-09-24 12:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 48482bcb-42cc-3c2e-84fc-7ae92bcca8a6 | -9.6111 | -43.9243 | 2026-09-24 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 97de7834-f8c8-33c1-b9dd-4d3dcc2332e4 | -10.9449 | -43.8614 | 2026-09-24 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 404.7 |
| 81802690-ef1c-383f-b914-2362eadd5f20 | -11.3246 | -44.0169 | 2026-09-24 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| ed6563a3-88e6-3b00-9365-81578d45cc45 | -8.2529 | -48.2128 | 2026-09-24 12:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7b4a50c8-92f7-34e7-a5f3-ff53cd15dcd3 | -9.6302 | -43.9219 | 2026-09-24 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| d2445002-616e-3cc0-8a94-84b2c5232f74 | -10.9258 | -43.8641 | 2026-09-24 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 3b28ed1f-4981-316b-85b1-ed02a6252f74 | -9.5332 | -45.3633 | 2026-09-24 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 004c83bb-d0c0-30e5-acfe-118b225bb113 | -9.5522 | -45.3611 | 2026-09-24 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| a7424aa7-6151-3336-815b-dba2de9a68a3 | -9.2412 | -47.3708 | 2026-09-24 12:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 02644d2e-6e38-346f-9635-ed017af7dd99 | -11.325 | -43.9934 | 2026-09-24 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 98c83038-7a27-3eee-8bf1-14504aa9e30b | 3.2676 | -59.99062 | 2026-09-24 12:59:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e208a7f9-fe50-3a90-86e5-8e990ea94d50 | -8.3761 | -47.3023 | 2026-09-24 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 05f38bde-31d1-38fe-adf9-bdab083e67f5 | -8.4495 | -47.4497 | 2026-09-24 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5ae6e27c-62a7-3f18-878a-ce349783c9dc | -9.5332 | -45.3633 | 2026-09-24 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7d643cc1-d90e-3f16-9edb-87c0198abd6c | -8.4307 | -47.4515 | 2026-09-24 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ba371ed8-07c5-32aa-8c43-a27ddf581d61 | -9.6302 | -43.9219 | 2026-09-24 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 3a14490f-6a8c-317c-9706-9af741ab8784 | -9.5522 | -45.3611 | 2026-09-24 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f58439ce-67ee-3f93-b796-54728a40a23d | -9.6111 | -43.9243 | 2026-09-24 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 608c9d00-6f88-310e-8728-d2fe194031d5 | -9.2415 | -47.3487 | 2026-09-24 13:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0c091620-f91a-3fc7-bcab-123ef06c48bd | -9.2604 | -47.3467 | 2026-09-24 13:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 6de71eae-f6bf-346b-81f0-cfa376a2e5f6 | -11.3246 | -44.0169 | 2026-09-24 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 6eb96f54-9bfb-3400-9429-5b8085e115ce | -1.82632 | -55.73217 | 2026-09-24 13:01:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 1806b311-f847-3bfa-92f3-dedf70cc396b | -6.01361 | -59.93635 | 2026-09-24 13:01:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| cf5499d1-e1fc-3740-a822-4af0bb367fae | -6.61955 | -59.91406 | 2026-09-24 13:01:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| d3d79996-0127-353b-9df5-68b13c34f950 | -6.44613 | -59.94812 | 2026-09-24 13:01:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 0e731b18-b59c-394f-b006-1a340bc09da3 | -5.59996 | -60.20709 | 2026-09-24 13:01:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 1b4ca994-897d-39c9-9bc7-0ef3be7fb672 | -1.8333 | -55.69662 | 2026-09-24 13:01:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 19497b98-780b-3ebe-bc2f-1d9e57b83fce | -5.60207 | -60.20159 | 2026-09-24 13:01:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f87d8836-d06c-3227-8888-55254cf1e24f | -6.73104 | -59.42674 | 2026-09-24 13:01:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| b2f587d2-47f6-3f98-8dc8-1033db958952 | -6.74522 | -59.42853 | 2026-09-24 13:01:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 109419f2-20d9-3378-b3c6-fa8314c2291c | -6.44035 | -59.95431 | 2026-09-24 13:01:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 26b29628-4915-345d-8d06-41a9b0b74cdc | -6.61661 | -59.93653 | 2026-09-24 13:01:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 3d22a65f-fe58-310a-9cee-826df91e63f0 | -5.60262 | -60.18632 | 2026-09-24 13:01:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 12b0fcad-4781-3aa5-9b54-332a99c7d706 | -7.89235 | -61.17933 | 2026-09-24 13:04:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |


[Clique aqui para ver as próximas entradas](README92.md)
