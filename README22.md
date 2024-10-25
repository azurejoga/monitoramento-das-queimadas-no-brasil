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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ecf439c-150d-3c5a-8b44-97c059e218c3 | -15.26176 | -43.63402 | 2024-10-25 03:23:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 88f34de9-ea55-3890-b06f-2917e8e34026 | -15.2559 | -43.63269 | 2024-10-25 03:23:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 14.7 |
| f35f3c4e-cc60-3084-acd8-3b7e995ba30a | -15.17377 | -41.0019 | 2024-10-25 03:23:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1c247d0-060d-3990-8afe-66a53f422653 | -14.953 | -42.25666 | 2024-10-25 03:23:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a52a1fb4-c102-3b81-9488-fc8b4b30641d | -14.95229 | -42.2602 | 2024-10-25 03:23:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 587b3d25-ecc4-366a-a93d-d0d73c869c5d | -14.48502 | -45.49535 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c5ef4535-fde3-39fd-8095-50ef390a89a5 | -14.48372 | -45.50137 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de24b5a6-d108-30f9-a4db-a9ef8ccbe19b | -14.48281 | -45.48894 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c707a30-3819-3ccc-b33d-b942687cd8f7 | -14.48146 | -45.49498 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 29cdd3a4-a70e-3783-9ecb-38755979d783 | -14.47881 | -45.50692 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21eebd70-60cb-3a4d-bc3f-87adbe9c0ef7 | -14.47839 | -45.4938 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a8d2de1-f089-341a-abc7-35c0989fcfbb | -14.4771 | -45.49978 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe3ab4fc-248e-33d3-b760-611de4379d65 | -14.47581 | -45.50576 | 2024-10-25 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59c34e7d-b909-3bf5-8611-5da8b7610474 | -13.57149 | -43.4352 | 2024-10-25 03:23:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7843c1ed-60f1-32cb-93f5-7681fabe454a | -13.35464 | -43.92772 | 2024-10-25 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b573630d-2c27-38e7-bc04-de6b59ca8254 | -13.3536 | -43.93267 | 2024-10-25 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93133e72-64f3-3797-910d-2d461118bf71 | -22.30216 | -41.88529 | 2024-10-25 03:25:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 59590812-a835-3a17-a746-6d2b9c30c169 | -1.0445 | -47.6237 | 2024-10-25 03:25:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 370804b2-e001-395f-8f72-799d8f0c5a43 | -2.8145 | -49.2418 | 2024-10-25 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8c912e69-ad59-3835-963a-5c2a4d92b6ac | -3.1949 | -46.807 | 2024-10-25 03:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8cbea3d5-914e-38db-b65b-716510b0bcfd | -3.2135 | -46.8063 | 2024-10-25 03:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| e0336c56-9031-3803-b16a-d4c03ef57c43 | -3.2136 | -46.7843 | 2024-10-25 03:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b5a12e17-db0e-349e-be81-1b798405ac2d | -3.958 | -46.4442 | 2024-10-25 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 62cd4044-a271-37c9-9b19-002f762b74d4 | -3.9581 | -46.422 | 2024-10-25 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| f68f6f6f-e1d9-3d64-b8a4-51c5733524e3 | -6.5219 | -60.0457 | 2024-10-25 03:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 775a45f9-ef4b-361f-849d-64bbd83dd938 | -12.3782 | -63.8821 | 2024-10-25 03:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 961f0762-3d64-3b0b-9fd4-16b2db000b2a | -12.3783 | -63.863 | 2024-10-25 03:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0ddd30f7-4b47-386c-b9bd-201b7b7ea4c8 | -12.4589 | -63.1895 | 2024-10-25 03:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1b013bd8-2ca7-3862-bfba-ee1a2893478a | -12.4591 | -63.1704 | 2024-10-25 03:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 132c1e92-cc20-310b-84cb-e55d131b825e | -12.478 | -63.1693 | 2024-10-25 03:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4585f2b5-5911-34b2-a400-a9d98f5c01e2 | -15.6788 | -55.972 | 2024-10-25 03:26:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 0b8d3951-858f-3752-861b-119def6301db | -16.9593 | -57.545 | 2024-10-25 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 4e0d7ae6-b2ac-3fb9-8334-3f187c2bdbde | -16.9596 | -57.5245 | 2024-10-25 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.8 |
| 5eeb049e-5bbe-399e-bf81-331aba7578ca | -16.9792 | -57.5223 | 2024-10-25 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| f0c3e873-502f-33a3-9f72-fddf013b528c | -17.0014 | -57.3561 | 2024-10-25 03:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| bdb69b36-98c6-36db-97dc-821030d1439c | -17.0381 | -57.5155 | 2024-10-25 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| bcbd1d2d-94a8-371c-8794-f7eac60ef598 | -17.2386 | -57.2256 | 2024-10-25 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 84348982-380a-391b-a19b-d7ccd083ceb8 | -17.2537 | -57.5108 | 2024-10-25 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 4e74ec4a-4e42-3030-8b5e-7c97b27ca1ad | -18.0448 | -57.2712 | 2024-10-25 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 15da24b8-84d9-38d4-af44-dc32603fdba9 | -18.0452 | -57.2506 | 2024-10-25 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.8 |
| afb50775-5de4-39c0-9563-a069a32ff699 | -18.0646 | -57.2688 | 2024-10-25 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 56eb41cc-e8f6-3ff0-8e30-9de16f0ef4e1 | -18.065 | -57.2481 | 2024-10-25 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 7e707811-f9de-3678-9085-359972e39e19 | -18.0844 | -57.2663 | 2024-10-25 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 03cd07d0-6229-3700-86c9-64ad33fda4e0 | -18.0847 | -57.2456 | 2024-10-25 03:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| f4d242dd-5628-3425-a262-23e68aebcb6c | -2.8145 | -49.2418 | 2024-10-25 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1c95c385-0b9f-3238-b35c-fbaa7b190f8a | -3.1949 | -46.807 | 2024-10-25 03:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d9734e26-fb38-3f49-aced-eeca834863aa | -3.2135 | -46.8063 | 2024-10-25 03:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 0d45404a-a5c1-3062-a3a8-36fefb48a638 | -3.958 | -46.4442 | 2024-10-25 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 652f0280-df12-3387-88a0-efa16f8583c0 | -3.9581 | -46.422 | 2024-10-25 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 500479b5-e794-38ff-8c8d-a86df149f863 | -4.2429 | -48.5474 | 2024-10-25 03:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 638ec5ab-6ba0-3cf2-85c4-29a1a5eb30f5 | -5.3911 | -48.8969 | 2024-10-25 03:35:36 | GOES-16 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| e59beed6-ddda-38fe-8225-eb88ba7e2599 | -5.9788 | -45.3621 | 2024-10-25 03:35:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| bc322248-054f-3ac2-bffc-0225fe7718ab | -6.5219 | -60.0457 | 2024-10-25 03:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 221cc14d-0c83-3273-9cd4-aab3e954e21a | -12.3782 | -63.8821 | 2024-10-25 03:36:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7382c244-ac31-3346-bd5e-74d883069ba4 | -12.4591 | -63.1704 | 2024-10-25 03:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 28d1e95c-d89f-3e00-8ed2-a9633126b250 | -15.6788 | -55.972 | 2024-10-25 03:36:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| c8836d9a-c5e1-3b43-8731-72003115008f | -16.9596 | -57.5245 | 2024-10-25 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |
| 76ef67f8-10af-35e3-9904-b4e586d950a7 | -16.9792 | -57.5223 | 2024-10-25 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 3f6804b9-1a34-3b7e-b8a7-687ec968a455 | -17.0381 | -57.5155 | 2024-10-25 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| e8b224d5-472e-3ce8-b8c6-4fef9953694f | -17.0786 | -57.429 | 2024-10-25 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 2ba77c4b-ea1e-31d4-8ccf-cb7581de0fc2 | -17.2386 | -57.2256 | 2024-10-25 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| a3658a8c-da4d-302f-94eb-82adc95bb329 | -17.2147 | -57.4949 | 2024-10-25 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 2df206b5-e862-3534-97d0-4332d169f7ee | -17.2537 | -57.5108 | 2024-10-25 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| 20bf0431-35c2-3bc4-bae6-2e2876a99362 | -17.215 | -57.4744 | 2024-10-25 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| cabc93ac-9d1f-37a2-b0e9-2b7a3670e51a | -17.2186 | -57.2485 | 2024-10-25 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| ef7c3354-87a8-3bd6-a9fc-cd7d0c957700 | -17.2383 | -57.2462 | 2024-10-25 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| bf3255ef-274d-3094-9d23-65b77f0c42f2 | -18.3 | -56.2431 | 2024-10-25 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| ea59ac5e-2745-3613-8a2f-3fcd0e258421 | -18.3004 | -56.2222 | 2024-10-25 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 7336a514-3b4c-349c-99a9-53340a624787 | -18.3199 | -56.2404 | 2024-10-25 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 2b5d5c95-e586-3d0b-a25d-44a2d093b972 | -18.3203 | -56.2195 | 2024-10-25 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 1a7efe23-342c-33bf-b662-e937c3fba901 | -18.3398 | -56.2377 | 2024-10-25 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| fafe05c7-da74-31d1-bc9e-b8a5e97412df | -18.3401 | -56.2168 | 2024-10-25 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| a027308b-c147-3c40-943a-34bf560eed60 | -3.2135 | -46.8063 | 2024-10-25 03:45:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 6f28cff7-12b8-3312-ac0c-b4dc1bcb5421 | -3.9581 | -46.422 | 2024-10-25 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5a573c16-65d7-3454-aa99-69a52adafb24 | -6.5219 | -60.0457 | 2024-10-25 03:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 650ca6a6-812d-32c9-8e3a-ce7fc00aa2fd | -12.3782 | -63.8821 | 2024-10-25 03:46:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5d4183d7-bd03-357b-94ec-045898a703de | -12.4589 | -63.1895 | 2024-10-25 03:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 7cfadee7-3718-3194-b95c-f57560d5939d | -12.4591 | -63.1704 | 2024-10-25 03:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c3e44ae7-fdb2-3938-8d77-d41b1c4de76c | -12.478 | -63.1693 | 2024-10-25 03:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 54c8bd5a-5fdc-3a04-bcf3-d49574350d24 | -15.6594 | -55.9742 | 2024-10-25 03:46:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c7990460-d59d-3451-a9f3-ab6ef588653c | -16.94 | -57.5268 | 2024-10-25 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 36d9371b-c5b4-377f-9064-b98d0db0b09d | -16.9596 | -57.5245 | 2024-10-25 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.5 |
| bc62d68f-c808-3a3b-ab6f-2bd293a61443 | -16.9792 | -57.5223 | 2024-10-25 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.1 |
| 8f9b1229-b889-31e8-a4ad-317772e858bc | -17.0381 | -57.5155 | 2024-10-25 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 798b1624-9c35-3713-bb06-30fa3a5569b5 | -17.0586 | -57.4517 | 2024-10-25 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| f82fa54a-c488-3b01-81a7-ab7db3296a2a | -17.219 | -57.228 | 2024-10-25 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 7e872604-3b5c-3cdd-be44-402155afd32f | -17.2537 | -57.5108 | 2024-10-25 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| dbd5e13e-6941-3a65-9772-c490f268d0ac | -17.2386 | -57.2256 | 2024-10-25 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 20f2a55c-d5be-3fca-9cbc-83a4facfaabd | -17.2147 | -57.4949 | 2024-10-25 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 2295a40d-eacc-32c7-abeb-9b0543222253 | -17.215 | -57.4744 | 2024-10-25 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 56df30e5-58ee-3db0-9436-952dfd2c523b | -17.2186 | -57.2485 | 2024-10-25 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 48fba8e3-1436-3074-8e95-e8d892756035 | -18.3199 | -56.2404 | 2024-10-25 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 9c57fae0-abe8-3a61-80ca-4cddde8081ce | -18.3203 | -56.2195 | 2024-10-25 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| c8352a0b-92b0-3d69-9670-bd45baa3cc46 | -3.1949 | -46.807 | 2024-10-25 03:55:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 943caf9b-93d7-32a0-9158-1c2b3850f1b1 | -3.2135 | -46.8063 | 2024-10-25 03:55:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 3d8e4efa-e46e-37fe-937f-60796aa23265 | -4.2429 | -48.5474 | 2024-10-25 03:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5f8e04ab-ff6b-39d6-bcf1-63bd789d5728 | -12.3782 | -63.8821 | 2024-10-25 03:56:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f6cf4bd7-39d7-341f-80d0-3b6bab058ce1 | -12.4589 | -63.1895 | 2024-10-25 03:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 95352854-df27-37b3-b3ed-5c83fb33233e | -12.4591 | -63.1704 | 2024-10-25 03:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d79d898b-4ccf-3f1b-92b0-88594c4ac12c | -12.478 | -63.1693 | 2024-10-25 03:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |


[Clique aqui para ver as próximas entradas](README23.md)
