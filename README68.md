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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ee988d2-6ff3-3c95-89a7-75c6776c8c83 | -10.6068 | -55.9169 | 2024-10-09 03:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| b0b2dd5d-fc10-3b04-8d7e-ac04d1a62f0d | -10.8755 | -63.8979 | 2024-10-09 03:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 765054a1-fe82-3768-8a42-5d151f6a8803 | -10.8754 | -63.9169 | 2024-10-09 03:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 4732c516-767f-37d1-88c2-ac6e6cc14f44 | -11.2583 | -60.3885 | 2024-10-09 03:56:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a01c3324-0879-323f-8dfa-62a369f962f2 | -11.2771 | -60.3873 | 2024-10-09 03:56:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9549426a-eae7-39fe-af14-800defa0aaa2 | -11.693 | -65.0163 | 2024-10-09 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 031cc26f-fe5a-3850-a2a2-e861548c0b0c | -11.6931 | -64.9974 | 2024-10-09 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d45b3f15-047f-3527-88ed-bef9cfd70da2 | -11.7117 | -65.0155 | 2024-10-09 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 235.1 |
| b23e820a-5a77-3b40-a5e5-66688e412ff7 | -11.7119 | -64.9966 | 2024-10-09 03:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 10cbba84-4f31-3f81-8b1a-d7245daed064 | -13.3978 | -61.9376 | 2024-10-09 03:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 1ee87ca4-384b-39a9-8985-b459f01503a5 | -13.398 | -61.9182 | 2024-10-09 03:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2162fc4a-5a12-3734-83f0-ddbd8fd4d205 | -13.417 | -61.9169 | 2024-10-09 03:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 66b6181f-a54c-3ed5-803f-4e70cd1ab8bc | -13.9353 | -44.5046 | 2024-10-09 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 577224e3-7e8c-338e-9c77-3e9e80a5fdbb | -13.9348 | -44.5282 | 2024-10-09 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 203.2 |
| 7d07b487-eb5c-3969-9ae9-c42edb88d04d | -13.9343 | -44.5518 | 2024-10-09 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| aa1250bf-76aa-37cb-9330-1ee51196df9c | -13.9158 | -44.5081 | 2024-10-09 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 195.4 |
| ad319ea9-5b0e-3451-a08d-620e99976a3f | -13.9153 | -44.5317 | 2024-10-09 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| cc4d53fb-d618-3f80-89fd-adbdef5f5cd3 | -13.8963 | -44.5116 | 2024-10-09 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b5f8ff8e-f077-3408-bfa8-3ec0db88a149 | -14.0975 | -51.0918 | 2024-10-09 03:56:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 375a934c-64a9-35b7-9387-d8be4f2f5d31 | -16.4184 | -55.9455 | 2024-10-09 03:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| e456602c-2a61-3cbb-ac56-132f92fbe805 | -16.8573 | -57.8218 | 2024-10-09 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| c0d85b4c-f73f-3d23-999c-58738c3cdce7 | -16.8576 | -57.8014 | 2024-10-09 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 01b9e187-0012-32c8-a9ab-fb1dbd08de00 | -16.8898 | -55.8039 | 2024-10-09 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 143.6 |
| f18c48e8-67ed-305b-8592-b662b7af2f71 | -16.8901 | -55.7831 | 2024-10-09 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 117.6 |
| 19011d29-941c-3fa8-a3a2-13df36b52f04 | -16.8768 | -57.8196 | 2024-10-09 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| cd83c71d-fc71-383e-9067-aac9675b4637 | -16.9091 | -55.8222 | 2024-10-09 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 5e6e015e-c867-36b7-92d9-0d6562834f64 | -16.9094 | -55.8014 | 2024-10-09 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 311.1 |
| fa48ada6-504a-303f-98f3-8b2791cdc7c2 | -16.9098 | -55.7806 | 2024-10-09 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 204.9 |
| 338477a3-4877-3b9d-9381-f0232251d44e | -16.929 | -55.7989 | 2024-10-09 03:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 56ef220e-9dcc-359e-9ead-0c841b68b376 | -17.0795 | -57.3674 | 2024-10-09 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 6d379772-07ce-35aa-b90e-6172e6582f99 | -17.0799 | -57.3469 | 2024-10-09 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 7a805335-d08c-3b20-a1d4-afe9660efb37 | -17.0979 | -57.4472 | 2024-10-09 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 998baac5-b16a-3f62-891c-faf866b34a78 | -17.0982 | -57.4267 | 2024-10-09 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| b2fcab39-aea2-392e-bf1d-0054d7d2439c | -17.0995 | -57.3446 | 2024-10-09 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| 1c33cf84-9668-3247-a860-8d4650e982ba | -17.1175 | -57.4449 | 2024-10-09 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| bda12ca5-65f2-30c7-9cd0-c028952bc5fd | -17.1178 | -57.4244 | 2024-10-09 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 5253e908-b78c-3900-8a15-379fc23e9c11 | -17.1188 | -57.3628 | 2024-10-09 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 6c2ea01a-220d-3b0a-b4a9-bc3eb90e2833 | -17.7526 | -53.7948 | 2024-10-09 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 64b96355-b357-3f3c-978a-11670f4e9177 | -18.1589 | -56.3869 | 2024-10-09 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 3b835239-30a0-3d19-816b-fcc0e4e35748 | -18.1394 | -56.3686 | 2024-10-09 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| ef31442e-563f-3b33-ac19-45dd4f3e0bb4 | -18.1391 | -56.3895 | 2024-10-09 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 176.5 |
| 5d77c75f-560a-3bae-9a65-7f4dc2a84401 | -18.1196 | -56.3713 | 2024-10-09 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.8 |
| e7665158-4153-3ac5-be44-e7675297795f | -18.1193 | -56.3921 | 2024-10-09 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.4 |
| a5bba909-d002-300c-a5ef-9c4187b1bb68 | -18.1189 | -56.413 | 2024-10-09 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 0db9f634-7171-3246-935e-2a053b28bdea | -18.5996 | -57.2422 | 2024-10-09 03:56:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 9042e9e4-cc1c-31bf-b951-29203fbbd8ab | -18.5993 | -57.2629 | 2024-10-09 03:56:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 61ce69db-2099-35b5-9f45-a1c4d7cf524d | -18.6597 | -57.2137 | 2024-10-09 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 849406f0-6ed1-37e8-8c50-d2b90cf03629 | -19.8138 | -45.5961 | 2024-10-09 03:56:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f23841da-5e1c-36eb-8cc8-38059b50c164 | -19.8131 | -45.6202 | 2024-10-09 03:56:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 149.7 |
| e043347f-de38-3ed1-9233-40b3dc42d4f1 | -19.7927 | -45.6252 | 2024-10-09 03:56:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 6611013d-2fcc-3969-97b7-e08bec975bc5 | -20.1035 | -55.9434 | 2024-10-09 03:56:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 0ad55238-de99-3c9a-807a-c19f0d4b224b | -20.103 | -55.9647 | 2024-10-09 03:56:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 81b1b8b8-06f7-3812-83e1-f50a3f27fb7e | -20.0828 | -55.9677 | 2024-10-09 03:56:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 97bb41f5-b84e-37ac-8e73-3ddb1a320103 | -20.3557 | -48.7031 | 2024-10-09 03:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 8619567f-c806-3d4c-a087-03557d3db5de | -20.3551 | -48.7262 | 2024-10-09 03:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 380.8 |
| 7f9e0669-bb8d-3ba2-95f7-9c7798156ef0 | -20.3544 | -48.7493 | 2024-10-09 03:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2ac70c86-92c1-3513-b60b-df110e7a4cc7 | -20.3352 | -48.7076 | 2024-10-09 03:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 258.6 |
| 9c19f141-7a5f-38bd-b604-1119b4c6e06b | -20.3346 | -48.7307 | 2024-10-09 03:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 684.4 |
| 704be701-1562-30cd-ad6e-3bf2715bb1a4 | -20.334 | -48.7538 | 2024-10-09 03:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 106.3 |
| a5a9ebd3-c6f6-3a68-a803-71c4ce6c981b | -20.812 | -45.6315 | 2024-10-09 03:57:01 | GOES-16 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e29f3a18-9015-325f-85fb-52f2c2b05d35 | -21.5727 | -46.9659 | 2024-10-09 03:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 91cf0bff-7f6d-33c7-b664-754707d82d36 | -21.572 | -46.9898 | 2024-10-09 03:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 1d841869-d044-3754-b663-bd6aaeda0649 | -22.1578 | -48.1172 | 2024-10-09 03:57:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 525ee4b7-ff79-38bf-815e-f56889bc981c | -22.1369 | -48.1224 | 2024-10-09 03:57:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d59b3002-7259-3287-910c-96970f6aee42 | -21.68 | -47.73 | 2024-10-09 04:03:19 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| beac4f0b-546d-3bb9-808d-180835ab61f3 | -21.68 | -47.79 | 2024-10-09 04:03:19 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c5bbcad0-3655-3da0-98b4-8e90bd292a0c | -21.65 | -47.72 | 2024-10-09 04:03:19 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e9432772-b496-3d61-854f-2ca13fecbd9b | -21.65 | -47.77 | 2024-10-09 04:03:19 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 27cfad7f-e945-3757-933b-c5d07be069d2 | -20.33 | -48.73 | 2024-10-09 04:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0327f724-e199-32c2-9c45-0730228c4d0c | -1.11 | -53.6173 | 2024-10-09 04:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5d061ed7-ad10-30aa-bc55-0b8412e545d1 | -3.9021 | -46.4689 | 2024-10-09 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| dc684864-478f-36c2-aee3-5f3db50fb3dc | -3.9023 | -46.4467 | 2024-10-09 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8f23b9cd-4068-3ca9-a2a9-5d6502ac36a2 | -3.9394 | -46.445 | 2024-10-09 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 441a4e73-8af5-3b48-9eb0-3a94e227acb2 | -6.7799 | -60.036 | 2024-10-09 04:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| eeb8a096-4345-3298-9c36-2b1ec1887543 | -6.7614 | -60.0559 | 2024-10-09 04:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 0669acf6-6d0e-39c4-91c1-2b5a87492ba9 | -6.7798 | -60.0552 | 2024-10-09 04:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 460df633-95c9-3879-b7a2-dd73a5e18854 | -8.4919 | -48.6476 | 2024-10-09 04:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1e6332ec-6ae1-3b3b-b9a1-5f350d05bcc2 | -10.3656 | -64.8262 | 2024-10-09 04:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 147c3b4f-34a9-3999-a312-8628ebfbe3ae | -10.3894 | -61.2502 | 2024-10-09 04:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ccc533f7-f858-3243-b195-efa950c70152 | -10.3842 | -64.8443 | 2024-10-09 04:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 076b79e3-5692-322e-b2e9-8c77c1b51db7 | -10.3843 | -64.8255 | 2024-10-09 04:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a27b47c5-de6e-39a9-8f4f-df2483da5fb1 | -10.4287 | -60.9979 | 2024-10-09 04:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 10556754-b1ae-3319-a434-8408c30382ea | -10.3655 | -64.8451 | 2024-10-09 04:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| aa956d81-ea97-3987-b07b-b0db6043d1ca | -10.6253 | -55.9355 | 2024-10-09 04:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| ed5dc2bf-137c-35cd-804b-88f46c112729 | -10.6256 | -55.9154 | 2024-10-09 04:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6c7b840b-cab5-34cc-901b-bf7ed9d9e15f | -10.6258 | -55.8953 | 2024-10-09 04:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 1ab992c5-6cfe-3184-8097-50bd2f1b43db | -10.6068 | -55.9169 | 2024-10-09 04:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 72272385-0149-3c9e-bb05-d7c3715b0166 | -10.8567 | -63.9177 | 2024-10-09 04:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4a71278c-4c11-357e-b0b8-9b24c1bbdf99 | -10.8754 | -63.9169 | 2024-10-09 04:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e6bd6eaf-b7cc-3b4f-89ed-d22cc9746199 | -10.8755 | -63.8979 | 2024-10-09 04:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2ac49374-dfbd-3f8d-b74b-367660282377 | -11.2583 | -60.3885 | 2024-10-09 04:06:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a40e99bd-9427-3d84-ab0d-202f932b436f | -11.2771 | -60.3873 | 2024-10-09 04:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4b0debaa-b576-39a2-a1cb-f19c08fb768b | -11.6806 | -64.0312 | 2024-10-09 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 41373d4d-3645-3a1d-8356-ee9384b83b09 | -11.693 | -65.0163 | 2024-10-09 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 148.4 |
| c0a087f8-db03-304b-9c94-3cb5b87e342f | -11.7119 | -64.9966 | 2024-10-09 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 150.2 |
| d9c7f9f3-ac25-360b-bbc8-66bb655e6708 | -11.6931 | -64.9974 | 2024-10-09 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 109.9 |
| e191a13f-7bf1-32d3-aaa4-2d3921e6f324 | -11.7117 | -65.0155 | 2024-10-09 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 192.8 |
| 15cb4a11-1d8d-352f-9c1a-8c98e7145899 | -13.2877 | -53.704 | 2024-10-09 04:06:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 709ebe75-4b03-3bd1-a5e8-841c0f53ef3e | -13.3978 | -61.9376 | 2024-10-09 04:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 170abbf7-5225-3ae2-97b3-e0d66c4bf648 | -13.398 | -61.9182 | 2024-10-09 04:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |


[Clique aqui para ver as próximas entradas](README69.md)
