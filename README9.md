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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd7f3f6c-74e2-38d4-bcaa-4cc1f9c9b067 | -6.8881 | -71.5008 | 2025-09-03 00:30:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 50645b62-2f02-3a5e-beeb-7e93fceb8d9d | -5.6079 | -45.0265 | 2025-09-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 64649b12-c8e6-3c96-867f-7b3da39fe5fb | -6.4402 | -58.138 | 2025-09-03 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 187d90b8-46c3-3e0a-9589-faee8e6cea34 | -11.1033 | -44.6548 | 2025-09-03 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7d5ca704-f370-3267-85ee-b39c2286e3c4 | -9.3394 | -55.2277 | 2025-09-03 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 2c81bd94-c78b-35e7-a694-cd63b5e638f9 | -18.1514 | -51.75 | 2025-09-03 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 9b15f93d-182b-3255-9c8e-b9d2b33f97af | -8.3644 | -48.3116 | 2025-09-03 00:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 835dc4d7-c33b-3835-8b79-2759933b37ea | -5.6081 | -45.0038 | 2025-09-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| a28aed79-e668-332e-b33b-3bde354defba | -4.1604 | -46.7881 | 2025-09-03 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 486b9903-72f6-32ea-9731-5868768b8b23 | -6.4646 | -49.5364 | 2025-09-03 00:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| c8ea3222-f16c-3c7a-9303-c9b9c7da6f0f | -12.6341 | -56.9926 | 2025-09-03 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3007f03a-3f7a-3901-aebb-a2ed2500eaeb | -7.7036 | -48.7587 | 2025-09-03 00:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 152.9 |
| b4ef7ea7-5643-3c11-84a8-5cf30b9397ab | -7.3357 | -59.6484 | 2025-09-03 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 449aaf2e-28ca-378b-b328-8deca4749e59 | -12.8436 | -48.035 | 2025-09-03 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3220b7fe-6d26-3626-90fd-509c4f3f065a | -3.2121 | -47.1138 | 2025-09-03 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 58aa62e6-c512-39d2-8c13-11429f6a5aaf | -9.5231 | -48.8959 | 2025-09-03 00:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 034d45ae-46e7-334e-b172-b0ab07f97b28 | -6.3293 | -58.1814 | 2025-09-03 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 80837a24-53f6-32e3-a137-084da83b9481 | -7.5476 | -61.3437 | 2025-09-03 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 8c1797ed-cb39-3855-afc6-2068f16a1254 | -5.6266 | -45.0252 | 2025-09-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 084b9e85-0963-3034-a007-dcd3496a768c | -12.6339 | -57.0127 | 2025-09-03 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d0955e30-071f-3ac9-8aa5-f0147fcce641 | -7.7224 | -48.7572 | 2025-09-03 00:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 06f225dc-b9c8-3d6c-9509-d16fe49c4273 | -9.5046 | -48.8761 | 2025-09-03 00:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 493d0878-a9df-33e9-af9a-b02c71e214b0 | -3.212 | -47.1357 | 2025-09-03 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 8c3be0a2-9a51-37cc-9804-68bd0d26e47d | -8.3832 | -48.3099 | 2025-09-03 00:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1ed6b5ce-b36e-3eb6-b5e4-3ce9f3ba9dc8 | -17.941 | -47.1718 | 2025-09-03 00:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 5f345904-f566-3f1d-a8c0-d02eead57c35 | -20.8886 | -50.0937 | 2025-09-03 00:30:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| 76b59652-471a-3f61-a25c-d9d92631ad74 | -5.6268 | -45.0025 | 2025-09-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ceaeea3f-441d-33ea-a3cd-99dd3fed8bb0 | -3.2306 | -47.1131 | 2025-09-03 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| b85ba9f0-d46e-3921-82d0-8b84ef88eae6 | -9.5043 | -48.8978 | 2025-09-03 00:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| b20945d3-89eb-3a84-8cd8-06fb6fee5a78 | -6.4462 | -49.5163 | 2025-09-03 00:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e4437eba-adc3-30b3-9354-ae1812d1c579 | -9.1949 | -45.1972 | 2025-09-03 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 263e3f38-58dc-314b-8168-94732799db1e | -6.4648 | -49.5151 | 2025-09-03 00:30:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 6d0b0580-c561-3ffe-9f68-ccb4aa0657fa | -7.7039 | -48.7371 | 2025-09-03 00:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ecc0ec03-39e1-399e-b45c-bc9ff0149381 | -12.4889 | -47.4837 | 2025-09-03 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| bae3e75b-3d44-39a8-b015-6389994e4dbb | -9.176 | -45.1993 | 2025-09-03 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| a3733308-dcd0-391e-b4e7-9a51cb9b8f2f | -3.2305 | -47.135 | 2025-09-03 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| b6739af0-1e0e-3774-97d3-5049fe1e8343 | -10.0932 | -54.7667 | 2025-09-03 00:30:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 5371e537-b3ba-39b5-b66b-7ec0201a4464 | -10.4853 | -50.346 | 2025-09-03 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9f63bb84-f29f-36c9-90b7-9c93e1631daf | -11.1224 | -44.6521 | 2025-09-03 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8b983615-e67a-36f2-aa6f-7477d11c7314 | -9.1949 | -45.1972 | 2025-09-03 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 72dc6071-e9a1-360c-a541-feadd8156f98 | -10.5409 | -50.4256 | 2025-09-03 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b29ccacb-dec9-3822-b82c-511f437d5b4f | -5.6268 | -45.0025 | 2025-09-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 32e1d772-53a9-380a-a1f6-be64248dcdf6 | -7.7039 | -48.7371 | 2025-09-03 00:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 38fdac55-a195-30fe-85f0-ded74384dae2 | -7.5476 | -61.3437 | 2025-09-03 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c9e0ff49-748f-3217-980e-1e017881f785 | -3.2306 | -47.1131 | 2025-09-03 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 159.9 |
| de5f2063-254a-3e7b-bb00-d4d52a56c8cd | -10.0932 | -54.7667 | 2025-09-03 00:40:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 6da2344b-71b8-38c5-a577-0a1ac5561ef6 | -9.3394 | -55.2277 | 2025-09-03 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 55705d7f-f87c-3da2-a8a5-247acb63d16d | -12.4889 | -47.4837 | 2025-09-03 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 5045439b-fd8b-31b5-a479-53363510ea1e | -7.5291 | -61.3444 | 2025-09-03 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 65a2fdec-3ba9-31b1-a637-a339edc90947 | -11.1228 | -44.6288 | 2025-09-03 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 6caca3d9-8540-3b0d-9879-ef4bb50f4e6b | -11.122 | -44.6753 | 2025-09-03 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5a7d2c70-4119-3b53-8d09-b404721bba9b | -12.6341 | -56.9926 | 2025-09-03 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5ec330af-c2d3-354b-bf38-5dd88e138805 | -7.7036 | -48.7587 | 2025-09-03 00:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 4e1d56fa-475a-3064-a082-2baaf7e7499f | -4.1604 | -46.7881 | 2025-09-03 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 5e5947fb-ae16-3218-9c5a-c5b05536e33b | -5.6081 | -45.0038 | 2025-09-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 19c2b680-613f-3bf0-a285-4461483d53dd | -7.7226 | -48.7355 | 2025-09-03 00:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 810bb7af-e51b-3ed5-8580-2a00d8a9c314 | -8.3644 | -48.3116 | 2025-09-03 00:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| d613c8ae-a0d1-3d11-bb26-e647c3a1a97a | -12.6339 | -57.0127 | 2025-09-03 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| b5d3b3a5-0a98-3fdd-a2cb-2d395d97aecf | -8.8842 | -45.822 | 2025-09-03 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e7cc44fb-b038-3028-b85d-94d56eac7012 | -9.5231 | -48.8959 | 2025-09-03 00:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f90e4dfe-c137-3efb-a993-2b8b1413fa5a | -10.4853 | -50.346 | 2025-09-03 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e6252776-420f-3932-a80d-5dcc6ac7c762 | -3.212 | -47.1357 | 2025-09-03 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3779ea17-3909-31bd-8c01-cc1585fd5158 | -11.0393 | -45.0564 | 2025-09-03 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a9351e66-be54-3641-b11d-f6af9c1c6888 | -8.3646 | -48.2899 | 2025-09-03 00:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d065ad88-6e16-33b8-a501-13b0649ed70b | -5.6079 | -45.0265 | 2025-09-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 826defd1-b6e0-3d26-b603-f05f72ec286c | -8.3832 | -48.3099 | 2025-09-03 00:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 98f11cf6-31a7-3c11-bbbf-fa5c498e90ec | -6.4648 | -49.5151 | 2025-09-03 00:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 8ed75365-a026-3c58-9c39-610ace079621 | -7.5477 | -61.3247 | 2025-09-03 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a3a8c1f7-1fc7-30f4-b5d4-9b24df9e5c93 | -11.1224 | -44.6521 | 2025-09-03 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 5af24653-a347-3913-b16a-3a42a9f71495 | -6.112 | -47.2017 | 2025-09-03 00:40:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 0d4f3fdb-27a5-3cc1-bba6-e8c1087456d6 | -6.4646 | -49.5364 | 2025-09-03 00:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 0573e8dd-e27a-317f-98d8-39c058231f0f | -6.1118 | -47.2237 | 2025-09-03 00:40:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b55a78a5-a810-320c-9628-584653c7bd44 | -3.2305 | -47.135 | 2025-09-03 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 217.7 |
| aa703644-597f-3865-9e1b-82b44172860b | -8.3834 | -48.2882 | 2025-09-03 00:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a20c28ec-27af-3f62-a8c6-bf3e40ea24c7 | -11.1033 | -44.6548 | 2025-09-03 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e09f2747-fb4d-379e-98f2-488a71c70590 | -5.6266 | -45.0252 | 2025-09-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d58f4398-8c2a-399f-8fed-c7607adb5ceb | -19.36128 | -49.11184 | 2025-09-03 00:48:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a498d1ac-c049-3217-89ea-6678fe04ce00 | -20.40798 | -45.70148 | 2025-09-03 00:48:00 | TERRA_M-M | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 1766a9bc-43fc-30dd-b3f7-3ff18d0bc1dd | -23.60346 | -49.00462 | 2025-09-03 00:48:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fd467954-73c8-36ec-b355-11eb5a87ddfe | -23.27262 | -52.44671 | 2025-09-03 00:48:00 | TERRA_M-M | SÃO CARLOS DO IVAÍ | PARANÁ | Brasil | 4124608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 43af4a43-876b-3898-b788-f9b0e93a8a1f | -17.92646 | -47.17401 | 2025-09-03 00:48:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3b149c7c-bec5-3fa3-848f-45e99ecf9007 | -18.69114 | -52.7168 | 2025-09-03 00:48:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 96d54e55-fea7-3413-ad39-a23ca680e46a | -17.94562 | -47.23166 | 2025-09-03 00:48:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d9c510b0-02a1-37ea-b8c0-040ded5518af | -18.07546 | -45.99371 | 2025-09-03 00:48:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5a289988-b7c3-37eb-8859-28ebc929dfda | -20.69533 | -46.32399 | 2025-09-03 00:48:00 | TERRA_M-M | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 69d86789-5e33-3922-a7ae-b34086e5be1a | -18.6661 | -49.0879 | 2025-09-03 00:48:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 280ba4b1-76d1-3894-b233-bc21f68271e0 | -18.08162 | -45.96332 | 2025-09-03 00:48:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 647b2954-dba8-3b46-a426-8d3142c82447 | -19.13911 | -47.70203 | 2025-09-03 00:48:00 | TERRA_M-M | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 68c6beea-2a55-3e97-9d85-bfed0ae564ba | -18.17035 | -46.96122 | 2025-09-03 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d409b9c2-783d-37f3-95d9-2eef3dcd26d4 | -22.9922 | -49.91061 | 2025-09-03 00:48:00 | TERRA_M-M | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 3f9b3db5-482c-3b7d-8749-1180c3730e58 | -18.17227 | -46.97353 | 2025-09-03 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9bb969d2-dd21-383e-8da8-e12248572855 | -19.36268 | -49.12146 | 2025-09-03 00:48:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c394787a-2b6d-3bea-970d-76e47885d529 | -18.07313 | -45.97947 | 2025-09-03 00:48:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2c2e8a0f-cb5c-3cf2-938d-03ba525be2b8 | -17.94378 | -47.21975 | 2025-09-03 00:48:00 | TERRA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 321ca75b-1bbc-36f2-928a-a58cd1f7b706 | -23.35316 | -47.1738 | 2025-09-03 00:48:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d2d7eeb6-15e3-3f45-afd8-abf25c6bba93 | -19.13406 | -47.69817 | 2025-09-03 00:48:00 | TERRA_M-M | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 24937d9e-b5a0-34ba-94df-5bb9eba6a3b4 | -25.69338 | -49.89719 | 2025-09-03 00:48:00 | TERRA_M-M | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 198c6133-8075-30c6-baa8-85ac62793f19 | -20.89208 | -50.09654 | 2025-09-03 00:48:00 | TERRA_M-M | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| dfda1efe-1bbb-38b5-a132-2f228eaeb564 | -18.66751 | -49.09756 | 2025-09-03 00:48:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cdea4e46-6fb7-33a0-8769-587f671f520d | -19.13569 | -47.709 | 2025-09-03 00:48:00 | TERRA_M-M | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |


[Clique aqui para ver as próximas entradas](README10.md)
