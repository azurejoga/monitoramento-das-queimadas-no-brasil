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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00357e9b-17f6-3804-9ca3-33b3cb29c973 | -9.6703 | -68.58786 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 32bade8f-189c-35a3-92ea-4b2b33498f99 | -9.66927 | -68.59319 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ee84c9f-6f2a-33b9-8d1c-3121808cf2b0 | -9.65432 | -68.56883 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c50b2248-adb6-3d31-9e27-93d6b0fec5c7 | -9.65333 | -68.57396 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62ef58ec-d6bd-37cd-a5db-d92dca8a9df7 | -9.64701 | -68.57272 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c64bcc9-472a-3594-b361-a13523c9bbe9 | -9.6351 | -68.66748 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 193ca1f1-9fb2-377c-935a-00ee148cba32 | -9.63407 | -68.67277 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24892921-0bcd-3fd1-8d50-33d4f0e36a66 | -9.62769 | -68.67162 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e10ac470-321b-3d5d-87f2-1fa897e906c0 | -9.5682 | -68.6058 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25853eee-6acb-3164-aa45-c3203ccf1e61 | -9.56644 | -68.60341 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1681f7f7-ea9f-3a52-8e3a-b3687ad88f7e | -9.56186 | -68.60462 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d9dd1f7-793d-38ac-a1c9-397b56243e7d | -9.52254 | -68.7278 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d151f279-925a-311e-8b6d-ffec1f07a5e1 | -9.4781 | -68.57137 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a87dcd4-9503-3646-9e1c-bd99b8eb8f1d | -9.47439 | -68.56973 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a77df858-189a-39d0-820b-a41ea63c05cc | -9.46016 | -68.56214 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4feb09da-9a7a-304f-a72b-a291e0f67f27 | -9.45916 | -68.56733 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7e2bdea-ff4e-3fc4-940b-d3d8d9207250 | -9.40494 | -68.29007 | 2024-10-17 05:06:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd37f22d-49e8-3d02-a557-334ed3b0efd6 | -9.39773 | -68.29391 | 2024-10-17 05:06:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6011110-39b6-359d-b2bc-d5763fb9fede | -9.39676 | -68.29896 | 2024-10-17 05:06:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04594a6e-1097-3130-bdd3-ddcb526bcd73 | -9.38954 | -68.30284 | 2024-10-17 05:06:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2ac1b54-70e5-38cf-ae7e-27f1b4d199a5 | -10.85509 | -68.26622 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bf6daec1-3b79-3fd3-826c-c290521e0427 | -10.8544 | -68.26621 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 06b1d84c-274e-35ab-a062-c83fd38cb5aa | -10.85416 | -68.27084 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82861cfc-dc83-3bac-a7c6-0042cb03d926 | -10.85351 | -68.27083 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cdfda3f8-a760-3353-8a23-0f0920902256 | -10.81875 | -68.35242 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bf6e7ce-c754-3057-a1a8-ab866308a25c | -10.70945 | -68.61546 | 2024-10-17 05:06:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7c84ff4-01b1-3856-89d9-85655ce12863 | -10.54118 | -68.57243 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40584bb3-f9db-379a-b722-91888c1abf2a | -10.47388 | -68.49732 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 567df808-96d9-3494-9b14-12ce4a2bfbb0 | -10.47223 | -68.4969 | 2024-10-17 05:06:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ecf0c51-361e-3b98-8da0-d24b991c511f | -10.63027 | -67.82803 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a552efeb-0c21-35f7-b2ef-a3f4e2ce035d | -10.6257 | -67.72649 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed7606d4-ce70-3f6f-956f-4b18fd9efb50 | -10.62435 | -67.82676 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ec581f4-b0cf-31d6-a578-9f78da635aac | -10.62298 | -67.72063 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 636c38e5-e09e-37e5-9666-dacffc18c06c | -10.62215 | -67.72497 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b93d3d13-727c-38c2-b667-0d46cc9c12af | -10.62064 | -67.72112 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c16b4466-9580-3cb2-bf75-fee4c82c5322 | -10.61978 | -67.72543 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c7927d-2c02-3cf9-a41e-e80012f14371 | -10.58344 | -67.76694 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c57d89a0-c2bf-348d-9fa4-d9abfc3bb247 | -10.58259 | -67.77134 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b782ac40-6281-309c-bec0-405542f001cf | -10.58087 | -67.6851 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 554a7ba5-2f49-36e1-aa4b-a70c69a493cb | -10.57666 | -67.77016 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2e41610-97fb-36c0-9b45-b8023e75d899 | -10.57497 | -67.68396 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00e74444-c986-3f84-8fa5-8beb7c35901e | -10.38783 | -67.89853 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d39baf3-e60c-384e-8453-5658ab150d8b | -10.38693 | -67.9031 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bb538d7-4612-3cc1-8808-dd0d7a55d72d | -10.38543 | -67.89992 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02f85cde-61a7-3f9e-bb52-0064a22428c3 | -10.37202 | -67.94706 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83e74217-8191-3e40-9337-93a2be4d5a6f | -10.37115 | -67.95145 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ded5d6fe-dd6a-3be8-98d6-f141b94801b4 | -10.36998 | -67.94843 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e4c28ca-a529-311e-bb98-594f1089e254 | -10.36913 | -67.95287 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d931ccc6-6919-39d7-b66e-b5942171e371 | -10.36513 | -67.95033 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3244f99-97c4-3ed8-8b8c-f2cfc168dd23 | -10.36423 | -67.95486 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae4fc26e-2199-3ca0-9740-8d1a75cf7e7c | -10.36311 | -67.95177 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3afe672-972f-3fe3-88d1-5a7f0a79b56d | -10.35953 | -68.07371 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92cea361-46e7-34d5-8787-584d92c97da6 | -10.35884 | -67.94148 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 001eabcf-130e-39f9-9a66-2a2cad92d9c0 | -10.35795 | -67.94608 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 269fb663-fe20-3020-a180-3facf9dc7e24 | -10.35621 | -67.95521 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c08dc15-248c-31da-aecb-0bce57e15979 | -10.35399 | -67.94357 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a177eed6-7e46-3046-98a5-e4aa0c51de7c | -10.35347 | -68.07256 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 305e1f17-01a2-36a4-abe4-da99d70d4233 | -10.35308 | -67.94814 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91347c71-05ef-3217-a59e-d1e2dec0bc9e | -10.35218 | -67.95267 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7183b21-9d4c-3d8e-a432-8598443e83c5 | -10.35193 | -67.945 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d52abefe-456c-33b4-95d0-937e9266aaeb | -10.35181 | -67.98596 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4857536b-9b68-32b8-9aa2-abe3b230371e | -10.35128 | -67.95719 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9e52926-cd11-39dd-b4c8-985df53def11 | -10.35106 | -67.94955 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b647ba00-4628-3a4d-bfe9-faa847bfee8d | -10.35091 | -67.9829 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ba6ffc5-84f0-3617-a79a-150bc9c36356 | -10.35089 | -67.99059 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e053eb9-91a5-3a2d-8974-0c538b8a07c9 | -10.35018 | -67.9541 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b26ae4b-a5a7-36f1-9a9d-392fa3296fa9 | -10.35003 | -67.98751 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ed80f11-a3a0-3ecc-b00d-7c5809fef8d5 | -10.34931 | -67.95863 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bbb8839-95a4-3e1c-a259-c45e2ae36fa2 | -10.34914 | -67.99216 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ecc02d74-8dcd-3209-808d-728d6173a8bf | -10.34524 | -67.95611 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5201aa76-4b77-3fe2-8020-9a2f3920e34f | -10.34485 | -67.98949 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 62763fe1-6cab-337d-8fc5-5f2b70ee592d | -10.34416 | -67.953 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f707827-3cef-3732-a89c-63caecfd86ad | -10.34399 | -67.98638 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f41af517-8b47-34a0-8392-147d4fd2e8a8 | -10.3431 | -67.99101 | 2024-10-17 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16776ddf-7798-3fc3-8b97-a70ad736832b | -10.06995 | -68.06124 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e11a45d-97f8-3139-a252-344013fb98e0 | -10.28841 | -68.84206 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4201899-743f-3ee1-9ef0-762dc0833263 | -10.28736 | -68.84728 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b2a412b-3978-3a22-a41f-58a67c80b212 | -10.2863 | -68.85254 | 2024-10-17 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16bf04f9-8e17-35a0-b7f9-97176a7e0dad | -10.20396 | -69.09126 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb1f4c09-b906-3446-b564-bd0a4bf27806 | -8.71764 | -44.02445 | 2024-10-17 05:06:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b9a8196-d114-34f5-ab2c-2faefc38c84f | -8.71832 | -44.01923 | 2024-10-17 05:06:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28889797-4850-3ca1-bfb0-4ba5863ddff5 | -12.22334 | -50.33974 | 2024-10-17 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8c3363ea-1601-311d-8663-5529d555eafa | -12.22274 | -50.34433 | 2024-10-17 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 579554b8-4c59-3d9c-9953-7fec551c7fbc | -12.22213 | -50.34892 | 2024-10-17 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e48ad0d-81d3-3156-82f1-975cbb780fa0 | -12.21165 | -50.32405 | 2024-10-17 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 368adcda-4239-3de9-b955-00d52cded39e | -10.55273 | -51.57824 | 2024-10-17 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 740615de-470d-3f63-abb6-cf24beafe129 | -10.21282 | -51.66019 | 2024-10-17 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aefd52bf-76ed-3d89-9237-b777aaebd619 | -11.58992 | -51.01479 | 2024-10-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ac46885-b044-3408-b632-06d62bd181cd | -11.55543 | -51.3916 | 2024-10-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9d69ac0-76d8-33d6-8fed-050d46835024 | -12.97187 | -52.45656 | 2024-10-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 559e5be1-87c6-314a-9c5f-cb132c107d9a | -12.96861 | -52.45085 | 2024-10-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 483ad14d-feff-36c5-8bbd-96c74e714483 | -12.64139 | -52.44535 | 2024-10-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a4617a6-38f2-3bc4-a09c-39accd2f4c30 | -12.45433 | -52.40909 | 2024-10-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f85195ad-f09a-38cb-878b-564f0e18b87e | -12.45362 | -52.41425 | 2024-10-17 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54459f48-d36b-38b2-9ca4-598f545133d3 | -10.87087 | -52.35829 | 2024-10-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fa8134d-a90d-311f-91ab-3fe0fd59e9f5 | -10.86629 | -52.36269 | 2024-10-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ad99ff7-6f21-3fd1-a6ef-3cda78014109 | -10.85717 | -52.37137 | 2024-10-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b813709-e6c6-30a8-ad53-8842a38c729f | -10.85648 | -52.37624 | 2024-10-17 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c2ffbc6-2b6b-377f-ba69-57ed3be42eb7 | -10.19914 | -52.32117 | 2024-10-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19372c09-c3c2-3a83-87ab-7ed400bf2f7a | -10.19845 | -52.32602 | 2024-10-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README45.md)
