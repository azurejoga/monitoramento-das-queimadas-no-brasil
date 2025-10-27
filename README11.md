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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c947e30-20ef-3930-9e19-d94c24dc4aa0 | -9.4761 | -40.3862 | 2025-10-27 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 748fea69-8e94-3423-bd8a-fec7e8ed7625 | -12.5258 | -47.5678 | 2025-10-27 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fb2aacb6-66cd-3dcd-8079-d7730c04cc6a | -3.5782 | -44.5297 | 2025-10-27 02:20:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ef3bd234-9b0f-3079-892b-0b3aa9d2705d | -4.4479 | -45.4599 | 2025-10-27 02:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 8c395448-2317-3418-980a-8866b2396df7 | -8.0255 | -46.7593 | 2025-10-27 02:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| f8c7da30-069a-3922-9238-ead0b5f6c348 | -10.7484 | -44.1932 | 2025-10-27 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 765ee9ec-5c79-3c7e-8c02-dbba40e9f31d | -4.4805 | -43.4237 | 2025-10-27 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 8863254a-713b-364b-8241-3c6574d6c85d | -4.4665 | -45.4589 | 2025-10-27 02:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| ea1db74a-81d1-31c3-b47a-ee5d325a9f33 | -10.8401 | -56.959 | 2025-10-27 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| c1216104-40f5-32a7-8c0f-562efb97eba1 | -4.4618 | -43.4248 | 2025-10-27 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| ada3d4a1-ae04-3722-aa5f-ce5a6c1b26a6 | -4.4431 | -43.4259 | 2025-10-27 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 43925c3c-1787-38d2-a72b-1db35aacf213 | -4.4807 | -43.4005 | 2025-10-27 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c1fc97cc-b3b0-3be0-be07-30492bf6fa54 | -4.4665 | -45.4589 | 2025-10-27 02:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 0a6f5bad-684d-3a3a-a746-a9f4937cce44 | -10.7676 | -44.1905 | 2025-10-27 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2d8f7117-eaf6-36e4-962a-fc6e6941405c | -8.0255 | -46.7593 | 2025-10-27 02:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 242fba50-8a48-3671-99f1-add266025e15 | -4.4479 | -45.4599 | 2025-10-27 02:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 38a07bce-8241-3c70-bf00-420bb4e69bb8 | -3.5782 | -44.5297 | 2025-10-27 02:30:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 88b3262b-54a4-3dd0-ae27-f3d755740749 | -4.3879 | -43.3129 | 2025-10-27 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 44c345a1-55d5-362d-a90a-7fcb5c6e0ee3 | -9.4761 | -40.3862 | 2025-10-27 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 5c122a0c-732d-3466-a42a-ad8e22c3cce0 | -4.3877 | -43.3362 | 2025-10-27 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 6ae48df1-07bc-343c-9fd1-f50845c0cb5c | -4.4805 | -43.4237 | 2025-10-27 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 45b7edcf-221e-37c4-ae85-e9bbf919ebae | -7.0692 | -46.7541 | 2025-10-27 02:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 660bc425-517d-3188-8d6b-299ff3cd8447 | -10.8401 | -56.959 | 2025-10-27 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 297bf0a4-c882-3cd4-8998-c823a8ada193 | -4.4431 | -43.4259 | 2025-10-27 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 0da126bb-25bf-3137-8124-873836a64a79 | -4.448 | -45.4374 | 2025-10-27 02:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 37e701b0-4503-30d2-8a3a-1bee4adccd41 | -4.4804 | -43.447 | 2025-10-27 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 765f3059-0a0b-31cb-b5fc-5f801ce59bcd | -4.4618 | -43.4248 | 2025-10-27 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3c538d24-daf7-3ccc-8545-65fd2c191898 | -3.5595 | -44.5305 | 2025-10-27 02:30:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| a80b7e3f-9b0a-3ded-8b21-2aad0de2a557 | -10.7484 | -44.1932 | 2025-10-27 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 55143279-55dd-31f2-a504-c81211679007 | -4.4805 | -43.4237 | 2025-10-27 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 22d5d5ae-e013-35b9-9074-77eefcc1ae41 | -7.8596 | -46.4853 | 2025-10-27 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a2a8e5cc-a70c-37da-a27b-8972b1de24d8 | -10.7676 | -44.1905 | 2025-10-27 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 00b75015-4f6b-354b-9191-94edbf56cdc8 | -7.8406 | -46.5093 | 2025-10-27 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 413c6792-6b24-33b6-add5-8a28e33d59a4 | -4.4618 | -43.4248 | 2025-10-27 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3ec8c778-1540-37df-9448-6bc56c34876b | -4.4807 | -43.4005 | 2025-10-27 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| d0398d6d-abdd-3639-92d4-c0c8b3a510f6 | -4.4431 | -43.4259 | 2025-10-27 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 5d767e6f-3b97-3458-b4fb-61ef2f8a4e5d | -4.4479 | -45.4599 | 2025-10-27 02:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e7e84974-54ea-3aa9-a932-198e1884b769 | -7.822 | -46.4887 | 2025-10-27 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 0f4e52ea-9007-3d0d-88c4-cfc911ea35a6 | -10.7484 | -44.1932 | 2025-10-27 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 07d081a5-2b63-37a6-915e-85f3ed2307a1 | -4.4804 | -43.447 | 2025-10-27 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 58900c50-f887-31e5-8890-a916c188117e | -4.3879 | -43.3129 | 2025-10-27 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 11eb9f4f-48de-39f2-a7f2-463de69f8a6c | -7.8408 | -46.487 | 2025-10-27 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 250.4 |
| 75ee8450-8468-3222-b6bc-34f18de59518 | -3.5595 | -44.5305 | 2025-10-27 02:40:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 47c703cf-2a69-3293-9f4d-eff80a6e2a49 | -7.8223 | -46.4664 | 2025-10-27 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 8848d951-d93e-3c89-af74-b12ee6ef8d0b | -7.8411 | -46.4646 | 2025-10-27 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| b4b6dba2-8248-33b9-a28d-7763df523498 | -4.4665 | -45.4589 | 2025-10-27 02:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 0cd925d2-a085-39a8-83db-9e1acae95b7c | -10.8401 | -56.959 | 2025-10-27 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 888f23e6-ca91-39e5-8524-d4ff290fcda3 | -4.3877 | -43.3362 | 2025-10-27 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 38b94710-f30a-3141-983e-6d2b282bbefc | -3.5782 | -44.5297 | 2025-10-27 02:40:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1e46a596-c1f0-38aa-8159-3bc9ae772e55 | -7.0692 | -46.7541 | 2025-10-27 02:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| f9515d12-b4c8-3112-8f95-d360799b017f | -10.7484 | -44.1932 | 2025-10-27 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4e5845d7-6596-3bbd-89e8-6749f0b1e8ea | -4.4431 | -43.4259 | 2025-10-27 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 4f7829d0-553a-32b3-9950-17e792a37eff | -4.4804 | -43.447 | 2025-10-27 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| f3945b4b-ed25-363c-9b1f-e18db86f119e | -10.8401 | -56.959 | 2025-10-27 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5b2ec322-4941-363b-8433-c884e187f662 | -4.4618 | -43.4248 | 2025-10-27 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5335a775-7e85-3635-8319-9b0b527a1185 | -7.822 | -46.4887 | 2025-10-27 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| fa78d42c-166e-3304-abc0-dfc71e29bb00 | -9.9995 | -47.1772 | 2025-10-27 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 9bf48d8b-ee30-3edf-839b-ed21ec1d2822 | -7.8408 | -46.487 | 2025-10-27 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 78ac5b5a-f290-39a8-9f72-3d5b4729df4b | -10.7676 | -44.1905 | 2025-10-27 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 39367491-3b8a-33b2-afd1-dd65fce8e24f | -4.3877 | -43.3362 | 2025-10-27 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 22487055-7084-3416-9dd8-d1b288b0bafd | -9.9806 | -47.1794 | 2025-10-27 02:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 98d4b9b6-2424-3155-802b-4a82a8b59f78 | -3.5782 | -44.5297 | 2025-10-27 02:50:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 025f7edf-98cc-3aa0-808b-35a964a9e260 | -4.3879 | -43.3129 | 2025-10-27 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 7dd06ded-e31e-37c7-8fd0-cc6cb57f90c3 | -4.4805 | -43.4237 | 2025-10-27 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| b5e4726f-5c5d-378c-84b1-4122113fb534 | -4.4479 | -45.4599 | 2025-10-27 02:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 10068db5-ecef-3436-9528-34d2db98cee8 | -4.4807 | -43.4005 | 2025-10-27 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d25fdae1-4a6f-3b11-a7f1-eeeb484b642a | -7.8411 | -46.4646 | 2025-10-27 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| cd908d99-71e7-3d17-add6-f70fc453b78f | -7.8223 | -46.4664 | 2025-10-27 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 1a05e2ac-2819-3782-844d-d0e73d1b0a75 | -4.4618 | -43.4248 | 2025-10-27 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 242d26fc-13f3-327b-ac53-bf6a986b79ac | -3.5782 | -44.5297 | 2025-10-27 03:00:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 7b6cbd2e-8859-37e6-952f-262c9e240bbf | -9.9806 | -47.1794 | 2025-10-27 03:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a1771742-8c0f-3a47-8dbc-5a3156f2fe90 | -8.0255 | -46.7593 | 2025-10-27 03:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 496f34b8-37f6-329c-8913-1911ec514545 | -10.8401 | -56.959 | 2025-10-27 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f06abeb3-3030-3f72-a7c5-79fb276f77ea | -7.8413 | -46.4423 | 2025-10-27 03:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 8eff0954-4c2c-30d6-8491-37adfc3b1aef | -7.8408 | -46.487 | 2025-10-27 03:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 7e553bbc-103e-3289-b181-beb7910d68ef | -4.2415 | -45.6953 | 2025-10-27 03:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 389e0156-048c-3cc4-8888-77cd90da9a8f | -4.3877 | -43.3362 | 2025-10-27 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 07c7616a-cc99-3f88-973e-3412a604ca40 | -14.314 | -54.3138 | 2025-10-27 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ba34a808-34f4-3ece-8965-1ef1a6311195 | -4.3879 | -43.3129 | 2025-10-27 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| d72670eb-8aa8-3f33-8b9b-c3f02a4aecbb | -7.8411 | -46.4646 | 2025-10-27 03:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8ea9d599-1166-3fb0-ba7a-b8f4f64f1842 | -4.4805 | -43.4237 | 2025-10-27 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 5501030a-f7b1-39f9-a01c-24a202d26800 | -9.9995 | -47.1772 | 2025-10-27 03:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 96b96176-fe3e-3bd1-9204-c3b530e40ef1 | -10.7484 | -44.1932 | 2025-10-27 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a377c907-efb8-3ef5-b854-7b47439cd261 | -10.7676 | -44.1905 | 2025-10-27 03:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8af3f2eb-bd35-38cb-aed7-b6483ee5fcba | -3.7287 | -47.6395 | 2025-10-27 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 866fbbd1-ebc5-3759-a44b-6e52be4b1cd4 | -4.4479 | -45.4599 | 2025-10-27 03:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 448218a3-73fc-3cdf-aada-fe57b30061d2 | -3.7101 | -47.6403 | 2025-10-27 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 23a2221e-2d5b-3fa1-8832-31927b2b03f2 | -3.7286 | -47.6613 | 2025-10-27 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 8677d8a4-4f7f-385b-95e4-ee3862f699a4 | -3.7287 | -47.6395 | 2025-10-27 03:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cda6f267-9a06-3be2-be7e-157c3e5016dd | -10.7484 | -44.1932 | 2025-10-27 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fdb793e0-ef52-35c6-ba14-7ac9c956d75f | -7.8223 | -46.4664 | 2025-10-27 03:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 309be02e-0b8c-37dd-94ce-5873caddc157 | -7.8696 | -47.2606 | 2025-10-27 03:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 4d1ae426-db50-394d-bec9-4df9e35d6956 | -4.4618 | -43.4248 | 2025-10-27 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b53e122e-3c07-3b08-aab8-14799022477a | -9.9806 | -47.1794 | 2025-10-27 03:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| d9e46371-91e1-395b-9121-0d43d1d73b91 | -4.2415 | -45.6953 | 2025-10-27 03:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0ae284ce-e58e-3e23-b323-e6edc692bb32 | -7.8408 | -46.487 | 2025-10-27 03:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 699f168a-61c9-362b-b904-cec0f238c5e6 | -4.4804 | -43.447 | 2025-10-27 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f7af8225-83e1-3428-a60b-c203851c791a | -4.4431 | -43.4259 | 2025-10-27 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 8951e909-ca90-3fd9-a26f-06633b4aa8bd | -7.8411 | -46.4646 | 2025-10-27 03:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3e114f5a-90a8-32c6-8fc3-67f5f30d4f6e | -4.4479 | -45.4599 | 2025-10-27 03:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |


[Clique aqui para ver as próximas entradas](README12.md)
