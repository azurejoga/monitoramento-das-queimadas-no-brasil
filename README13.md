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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 867dbfad-63de-3efa-8f4a-33554a4cb50c | -10.5757 | -64.0248 | 2024-10-05 00:46:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| f1e323ed-ba61-3bf3-a8e2-9882a87683c4 | -10.5943 | -64.024 | 2024-10-05 00:46:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4761184d-6431-3cbb-84d7-19e04767db05 | -10.5945 | -64.0051 | 2024-10-05 00:46:07 | GOES-16 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c378c929-fa62-3c1f-a34f-aa87c47fd5ce | -11.0966 | -54.2336 | 2024-10-05 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a4c06aaf-feec-3d97-aabd-2f1f77fc469c | -11.1155 | -54.2319 | 2024-10-05 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 21856401-24b2-34ca-9d35-05db67cd888c | -13.1543 | -51.1931 | 2024-10-05 00:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 91f77c80-59ba-3dd6-ad85-38de5224e683 | -13.3786 | -61.9582 | 2024-10-05 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 66e01eae-e0e1-389b-a843-a85960c2889c | -13.3976 | -61.957 | 2024-10-05 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 370.6 |
| 9dd9a89b-d687-3cc3-9d73-c7b82982551c | -13.3978 | -61.9376 | 2024-10-05 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 446b2622-5aa2-3385-a2d1-707a09919d7d | -14.5556 | -49.2868 | 2024-10-05 00:46:28 | GOES-16 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 53dd813c-78c4-351a-bc62-7c32c115cff5 | -14.565 | -48.7995 | 2024-10-05 00:46:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 472503f7-23e8-3570-aa53-ccfe4984a440 | -15.5597 | -57.4553 | 2024-10-05 00:46:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| dcc3c37b-788b-309b-8d89-7d453528a5de | -15.5791 | -57.4532 | 2024-10-05 00:46:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 70cab070-de35-3bd9-9d8d-913b73195a1a | -15.7151 | -57.4184 | 2024-10-05 00:46:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 18ddc694-de75-3dae-a575-0101afae9c69 | -15.7346 | -57.4164 | 2024-10-05 00:46:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a9dbd55f-2db0-336f-bd9e-730969240c20 | -16.4155 | -57.3619 | 2024-10-05 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 1d161ea3-e2d6-3b83-a547-a5cb52ccd54f | -16.554 | -57.2237 | 2024-10-05 00:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.4 |
| 6a856a22-7e52-3793-8e12-19d11c6f0b23 | -16.5742 | -57.1805 | 2024-10-05 00:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 170.7 |
| 7816bc75-8d30-36c4-8360-83bf090205f6 | -16.5745 | -57.16 | 2024-10-05 00:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 167.4 |
| faf2caee-f489-30c4-ae95-34b1fa3a40c2 | -16.6594 | -55.5427 | 2024-10-05 00:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 6ad430ac-f698-3e85-9062-08c634bd1fa3 | -16.6598 | -55.5219 | 2024-10-05 00:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 01dbfd2e-dfe6-36ed-9018-b796b552011c | -16.6871 | -57.4536 | 2024-10-05 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 307c2de9-7391-3c55-bb9b-2d17cf0d77e7 | -16.7452 | -57.4878 | 2024-10-05 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 932f9491-340e-3982-8e82-7e8588910172 | -16.7647 | -57.4856 | 2024-10-05 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.9 |
| 27ce5a27-a71a-3dfc-afb0-920378e96bd9 | -16.7843 | -57.4834 | 2024-10-05 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 7d9880bc-f6af-3e09-815a-f32474542f47 | -16.8238 | -57.4584 | 2024-10-05 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 52ed3d8e-e7b3-3a75-a5bb-83019e203f87 | -17.1381 | -57.381 | 2024-10-05 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| d34375be-e8a5-3f2e-b95c-cc20b6a856d7 | -17.0888 | -56.7915 | 2024-10-05 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 5b1391c7-68cd-3a3d-86c9-c2278f747ef3 | -17.0892 | -56.7709 | 2024-10-05 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.6 |
| 361f4f3c-e92b-32bd-a271-0c8983057634 | -17.1085 | -56.7892 | 2024-10-05 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 93f193ef-bedd-3d30-b8cd-b77ee69d7898 | -17.1178 | -57.4244 | 2024-10-05 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 168.7 |
| 87352f3c-37ad-3f27-9ae4-392cac2dd9b8 | -17.1182 | -57.4039 | 2024-10-05 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 227.2 |
| 3a6f5d42-c9c4-3cfb-9667-c91cd481c3ac | -17.1185 | -57.3834 | 2024-10-05 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 20dcbffe-21cc-34e4-b832-32eb9e8a9ee8 | -17.1375 | -57.4221 | 2024-10-05 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 157.6 |
| e04be25b-cda6-3057-8c1c-a1a942f97a52 | -17.1378 | -57.4016 | 2024-10-05 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 221.5 |
| 3dfd076b-8576-3318-91d8-0dd3657bd0c1 | -18.2786 | -54.2261 | 2024-10-05 00:46:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ad414be8-e0cf-353e-9faa-9deaf2164c10 | -18.2985 | -54.2231 | 2024-10-05 00:46:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 7c11ffd3-f4c2-3f12-ac08-b9e4f0e3735e | -18.299 | -54.2018 | 2024-10-05 00:46:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9da7e4b1-dc87-3b01-afec-36c75e99be6e | -18.4867 | -52.8009 | 2024-10-05 00:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3e8cf7e8-46a8-34c0-8deb-6523235e82a9 | -18.4872 | -52.7792 | 2024-10-05 00:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7fe87d41-4380-3804-bff2-30951e74fa03 | -18.6582 | -57.2967 | 2024-10-05 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 7bb926c0-a939-3baf-8c6e-a81b9ec91250 | -18.6586 | -57.2759 | 2024-10-05 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.7 |
| bdf0fa69-00b5-3ad5-9b77-2026464427b8 | -18.6782 | -57.2941 | 2024-10-05 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| d3bc8874-9d5b-3ffa-a8d9-5d117ce89695 | -18.6785 | -57.2734 | 2024-10-05 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.4 |
| 4ac71cf8-5835-34dd-b4cc-a2566290c10a | -19.0156 | -43.15 | 2024-10-05 00:46:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| b842a672-2048-38fb-bee6-f18bb8f51668 | -18.6981 | -57.2915 | 2024-10-05 00:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 47032bfc-21ab-364b-a17a-8ca934702548 | -20.5904 | -51.3907 | 2024-10-05 00:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| c237fe90-ef2b-3fb8-93ef-4a240f70df85 | -20.7901 | -47.7465 | 2024-10-05 00:47:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9eb8ca41-5160-3503-abb6-bc4fea9143e3 | -21.8086 | -48.7392 | 2024-10-05 00:47:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 124.3 |
| c0fc58e1-9386-3b20-83d7-8a123bee23b5 | -1.1942 | -46.5935 | 2024-10-05 00:55:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8fafd9d1-a346-372d-bdf1-bb13cb70a682 | -2.9014 | -50.7142 | 2024-10-05 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| a49a3e3d-0cf9-3447-889c-e30885bf0472 | -2.8829 | -50.7147 | 2024-10-05 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7296ecb2-1c72-30b9-8e1a-f40959b4630d | -3.1432 | -50.2254 | 2024-10-05 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| ea7ecd79-0bc1-363b-97c3-ffeba6f333be | -3.239 | -49.3986 | 2024-10-05 00:55:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9daac447-189e-3fba-9e32-e7800cc71339 | -3.3127 | -49.4599 | 2024-10-05 00:55:25 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 6d883698-74b1-383f-a431-4525ae67d8e5 | -3.5994 | -47.5359 | 2024-10-05 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 03ed7db1-8e7f-3383-bff5-7b78be2a5f0c | -3.5995 | -47.5142 | 2024-10-05 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| b66990d9-e511-36ba-91fe-0c6f40b70446 | -3.618 | -47.5352 | 2024-10-05 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 8f340466-48de-3092-b9e1-19a43967130d | -3.6181 | -47.5134 | 2024-10-05 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 188.5 |
| acb3c331-d3a1-3ffc-bb88-cae869d983db | -4.0148 | -43.2408 | 2024-10-05 00:55:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 311285b5-5882-3ff6-b90f-7444e8923280 | -4.0794 | -47.9502 | 2024-10-05 00:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 188.6 |
| fbd799ef-bdce-3143-81e0-950410cab8f5 | -4.7851 | -50.8117 | 2024-10-05 00:55:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f0d76b0c-2d7a-3fa7-a99c-1c7283def47a | -4.8036 | -50.8108 | 2024-10-05 00:55:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f8f78999-ff7b-3d7b-a87c-66f98207018e | -4.9452 | -43.7657 | 2024-10-05 00:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 449fe9b7-55e4-3bbd-aa3e-7ccf248c7fda | -5.3911 | -46.4322 | 2024-10-05 00:55:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0aa55386-1994-397d-a96a-d94ef5e53520 | -5.8214 | -44.1426 | 2024-10-05 00:55:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| ea14be82-cf8a-38d5-97c7-cca3d5c00d8c | -5.8216 | -44.1196 | 2024-10-05 00:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| c2264ab0-4012-35c7-90c7-5c30a2722bc5 | -7.0233 | -59.3918 | 2024-10-05 00:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6fc6a4e6-5836-3c61-9dcc-82ec3a4adccd | -7.1346 | -59.3099 | 2024-10-05 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a6657f18-bcab-3e25-a0d0-0f65fa68be08 | -7.153 | -59.3092 | 2024-10-05 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| fce6145c-e597-3b32-81c2-4b75b5af4393 | -7.494 | -35.2323 | 2024-10-05 00:55:48 | GOES-16 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 6bf0a091-8d24-385b-a66b-b69d68344fd5 | -7.7362 | -49.2297 | 2024-10-05 00:55:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 3f5a412c-15df-303e-b53b-133127c13718 | -7.7364 | -49.2082 | 2024-10-05 00:55:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 84053ec6-0703-30a4-8a8c-bb59a26d463f | -7.7549 | -49.2282 | 2024-10-05 00:55:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| e5cfdb65-089a-3616-9b88-6c086d534b6b | -7.7551 | -49.2067 | 2024-10-05 00:55:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 109.5 |
| a14d9982-0480-34f2-ac3f-1344d452ca63 | -7.8979 | -61.4631 | 2024-10-05 00:55:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3f805d27-e427-3183-b4f0-c83e7ee5ed95 | -8.6555 | -49.1083 | 2024-10-05 00:55:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 156.6 |
| aa01ced4-5b9b-3925-9fe5-73fe77157eee | -8.6558 | -49.0868 | 2024-10-05 00:55:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 51cfdcf5-0caf-3029-aafa-a5cdabb89858 | -8.7769 | -49.9763 | 2024-10-05 00:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1f933986-3c92-36a1-83b7-00744dc7c5e1 | -8.7772 | -49.955 | 2024-10-05 00:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d7c23b5d-31f8-3de3-870f-cafb7d96fc64 | -8.7957 | -49.9747 | 2024-10-05 00:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1981408b-78fd-3d42-8c88-412a42146ba9 | -8.7959 | -49.9533 | 2024-10-05 00:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 47ec7cee-b027-3f4f-81b1-2a1dba77ac63 | -8.9853 | -49.8083 | 2024-10-05 00:55:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e0621dc3-d20f-327c-91cd-c61872005802 | -10.1801 | -36.3232 | 2024-10-05 00:56:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.9 |
| 65a10cf7-a345-310f-94d0-77a97738c527 | -10.1994 | -36.3197 | 2024-10-05 00:56:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 110.2 |
| 9bc5a4cc-ef70-3fa9-9640-1e7e215fab0d | -10.4424 | -50.7336 | 2024-10-05 00:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 915d682c-7fe7-3948-8600-e7e99f287377 | -10.7542 | -46.1894 | 2024-10-05 00:56:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 6b45b1fe-776b-3800-8758-a97880b9e2b2 | -10.5757 | -64.0248 | 2024-10-05 00:56:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 538b6f15-f7f7-3f05-97fc-277f3bafb65c | -10.5942 | -64.043 | 2024-10-05 00:56:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ed182da3-5f1c-3894-a8bc-23180b12d1b4 | -10.5943 | -64.024 | 2024-10-05 00:56:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8780437d-27ba-371c-8fad-4054e554e06d | -10.5945 | -64.0051 | 2024-10-05 00:56:07 | GOES-16 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| dfdcd604-f913-3ec0-881b-1f005ab9603d | -11.0966 | -54.2336 | 2024-10-05 00:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3c383cbf-fa0f-37a9-b30f-226a8b0db073 | -11.1155 | -54.2319 | 2024-10-05 00:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 26abadbf-8737-3050-8eb4-5d98260eb3ad | -11.1158 | -54.2114 | 2024-10-05 00:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ede7969d-042c-3de5-b11f-b04f4de5450f | -12.7623 | -50.5782 | 2024-10-05 00:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 42b760bd-0fe2-3f33-b21f-84659499c077 | -12.7627 | -50.5567 | 2024-10-05 00:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c64fa8ab-527c-3d70-8725-b1595abbe4f8 | -12.7815 | -50.5758 | 2024-10-05 00:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c0185750-aa13-3e47-bc31-2ff37e580b04 | -12.7819 | -50.5543 | 2024-10-05 00:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 2dc0e14c-aefd-3ba7-8130-4cd8d7f4d7de | -12.8202 | -50.5495 | 2024-10-05 00:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 17125d42-21f2-3a66-9244-b9fb2b0bdd2e | -13.1543 | -51.1931 | 2024-10-05 00:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |


[Clique aqui para ver as próximas entradas](README14.md)
