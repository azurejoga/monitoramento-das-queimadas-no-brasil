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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e97305f-c6bd-3747-a214-ab8b3ac99681 | -16.8768 | -57.8196 | 2024-10-09 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 4485d50d-3a78-31d6-bdea-724a0137c761 | -16.8772 | -57.7992 | 2024-10-09 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| b98caf4a-fac4-3265-a11e-d244de71ac1e | -17.1588 | -56.1222 | 2024-10-09 03:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 33bf0fa2-8660-3a1c-9582-631487f9d1c0 | -18.1189 | -56.413 | 2024-10-09 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.5 |
| b9925cad-ffa6-3023-97ff-069e8d90c291 | -18.1193 | -56.3921 | 2024-10-09 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 2e93e9a7-dcbb-388f-af36-45d76155871e | -18.1391 | -56.3895 | 2024-10-09 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| af5a4b3a-5095-36e2-8b45-db4bcd242f4c | -18.5993 | -57.2629 | 2024-10-09 03:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| e75c2e6d-3381-38d8-ba64-e1ec9abea83e | -18.5996 | -57.2422 | 2024-10-09 03:36:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 2267dfae-d904-31d3-be72-92a109017dab | -20.103 | -55.9647 | 2024-10-09 03:36:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 5d2bccd2-4e74-3606-b6af-a1f2e07dec51 | -20.1035 | -55.9434 | 2024-10-09 03:36:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 70d36bb0-b555-34a8-9e39-db84e5446ac3 | -20.3309 | -48.8693 | 2024-10-09 03:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 042e2d2e-ae2e-3363-b9bd-1476b8116708 | -20.3346 | -48.7307 | 2024-10-09 03:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 168.3 |
| ff31c18b-5480-3d5c-8ede-b84892d724fd | -20.3352 | -48.7076 | 2024-10-09 03:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 98.5 |
| adca1048-4b7c-3053-ba93-3306e89f7368 | -20.3513 | -48.8648 | 2024-10-09 03:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 22e7fc14-7dd5-3c40-8eab-a5c24e9e0a44 | -20.3551 | -48.7262 | 2024-10-09 03:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 7f8f5132-724a-32ad-8375-c9be9a9acd8d | -21.572 | -46.9898 | 2024-10-09 03:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4b3b316f-59f6-3ee5-b434-d3ff2362a052 | -21.5727 | -46.9659 | 2024-10-09 03:37:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 5900fc0d-ffdf-34a7-bbda-9fcb21ceeccf | -21.6114 | -47.7357 | 2024-10-09 03:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 105.4 |
| f855179f-327f-30e9-a861-e1805a36c14c | -22.1585 | -48.0936 | 2024-10-09 03:37:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 13b96160-e752-3935-bf5f-73037d0e1807 | -1.11 | -53.6173 | 2024-10-09 03:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| dbeb45fa-2183-36f0-bcd4-bd6fff6bc7ea | -3.9021 | -46.4689 | 2024-10-09 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3f2531d9-7e3f-3dfb-a81a-5612bdec196e | -3.9208 | -46.4459 | 2024-10-09 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1e2e7cf7-91e8-316f-8b70-3313f22ee22e | -3.9393 | -46.4672 | 2024-10-09 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 267e448d-19a0-314d-815a-a98f0293827e | -3.9394 | -46.445 | 2024-10-09 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 81d04e5a-0bc1-3001-98fd-6910e1bfed22 | -6.7614 | -60.0559 | 2024-10-09 03:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 9133d24a-b407-3092-bb33-e33b46a6c713 | -6.7615 | -60.0367 | 2024-10-09 03:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| d285dabf-1a8e-3953-98e3-7ebe0b45c38e | -6.7798 | -60.0552 | 2024-10-09 03:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 5310ab3e-57c2-371f-b4fd-02e851507255 | -8.4919 | -48.6476 | 2024-10-09 03:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 88361791-db82-3ab1-b755-6aa1a4ceeee2 | -10.3655 | -64.8451 | 2024-10-09 03:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f679cedd-d1cb-37d6-b943-75396429d61b | -10.3656 | -64.8262 | 2024-10-09 03:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ccc8ae59-eb66-3a4e-931a-f68bdf1784dc | -10.3894 | -61.2502 | 2024-10-09 03:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| dcb58c5a-61a0-3d9c-9e82-98597ef1c812 | -10.3842 | -64.8443 | 2024-10-09 03:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b4e3f549-51a6-3424-96a2-8b07eb11b594 | -10.3843 | -64.8255 | 2024-10-09 03:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 281b3ab1-1add-33c5-b0bd-cd66914b501c | -10.4287 | -60.9979 | 2024-10-09 03:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| be84f81e-aa02-3315-86e4-b5a4d4624645 | -10.6253 | -55.9355 | 2024-10-09 03:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f9d533ab-f01d-30e3-96d5-0b59f992309d | -10.6256 | -55.9154 | 2024-10-09 03:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c10f4ba3-d8ec-32d2-bc46-b6f4c12a4849 | -10.6258 | -55.8953 | 2024-10-09 03:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1fe49b10-f892-395c-a390-82868b15c083 | -10.8754 | -63.9169 | 2024-10-09 03:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 540000f5-26d7-31a2-a1c6-49a0b2163672 | -10.8755 | -63.8979 | 2024-10-09 03:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b9288e59-6a09-3a6e-bd3a-ab04fd32fd17 | -11.2582 | -60.4079 | 2024-10-09 03:46:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9d363ffb-6f9f-30f5-9842-62611657055f | -11.2583 | -60.3885 | 2024-10-09 03:46:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9c411909-b85a-3de1-930a-4fcd6c31b0e7 | -11.2771 | -60.3873 | 2024-10-09 03:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e86d4a6a-bb8a-3a61-8153-ac0e87d717d6 | -11.693 | -65.0163 | 2024-10-09 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 0b6ea6ff-f401-3ad6-bbce-256f52c964a8 | -11.6931 | -64.9974 | 2024-10-09 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c460a8f7-bb21-3879-8e67-d0fff369a7f7 | -11.7117 | -65.0155 | 2024-10-09 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 221.8 |
| 1063594d-9ccd-363f-a5e1-f4fecdce7594 | -11.7119 | -64.9966 | 2024-10-09 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 85990cd3-5bd5-35a0-8893-a5fa124a14c8 | -13.8369 | -44.5691 | 2024-10-09 03:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0a129440-3eaa-31ec-acba-2ea1d906aa5e | -13.3978 | -61.9376 | 2024-10-09 03:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 01b802e9-81a3-3025-a190-c2152162e4f1 | -13.398 | -61.9182 | 2024-10-09 03:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3d6c83a5-2ad7-32e9-b4a6-c15c2a46c8fd | -13.417 | -61.9169 | 2024-10-09 03:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1dd3763c-a85e-3158-b8bb-e9fd7d5cffa7 | -13.9158 | -44.5081 | 2024-10-09 03:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 202ff2f7-2252-35a6-b8eb-a4ea8e07a0c5 | -14.0975 | -51.0918 | 2024-10-09 03:46:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 1c0cd019-fe09-373d-9390-77387d889f2c | -16.4184 | -55.9455 | 2024-10-09 03:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 72ed42ad-5ac6-3d58-8588-91327ace3ac2 | -16.7846 | -57.4629 | 2024-10-09 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| b1cb6758-fe98-328e-b6f7-9c71bd7a3ddd | -16.8573 | -57.8218 | 2024-10-09 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 86f8d52f-21e7-3b64-8741-b0a0d6266bcd | -16.8576 | -57.8014 | 2024-10-09 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| eb11b2a1-66a4-342a-a7a9-f196cb41f5ce | -16.8768 | -57.8196 | 2024-10-09 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| bdaf9c39-dbd3-3757-b998-a2360c02189a | -16.8772 | -57.7992 | 2024-10-09 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 922d43ca-521d-3618-a8a8-2ddc210c5925 | -17.1467 | -56.8463 | 2024-10-09 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| e9b6551b-3a3a-3597-a4bc-81fe461ea9a9 | -17.1271 | -56.8486 | 2024-10-09 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 3491a6dd-48a7-3334-a7b0-5d3adb6e4ce8 | -18.1189 | -56.413 | 2024-10-09 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| f64b19e5-62cc-3d47-8d42-c2fe3e9837dc | -18.1193 | -56.3921 | 2024-10-09 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.5 |
| 9e82387a-7571-376f-95d7-c33130a491e9 | -18.1196 | -56.3713 | 2024-10-09 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 422a659c-9462-3695-a266-f9578980a76d | -18.1391 | -56.3895 | 2024-10-09 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| ff44cb94-829a-34de-bc74-0de47336a4a9 | -18.1394 | -56.3686 | 2024-10-09 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 23d76923-d9d4-3020-89d1-499cb8e8b8a9 | -18.5993 | -57.2629 | 2024-10-09 03:46:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 1e0951df-a838-3452-b5f8-3697291f461d | -18.5996 | -57.2422 | 2024-10-09 03:46:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 4c2e39bd-0ac4-3c95-a9c8-af6b8c4b7fca | -19.7927 | -45.6252 | 2024-10-09 03:46:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 7eb46f97-23d2-323d-907f-175acc9fb5c4 | -19.8131 | -45.6202 | 2024-10-09 03:46:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 0ff261a1-cdaa-316a-b22f-380cf62c724b | -20.103 | -55.9647 | 2024-10-09 03:46:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 3a939392-5eb1-3af6-a168-19c00a0a71f2 | -20.1035 | -55.9434 | 2024-10-09 03:46:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 4a1cfdc3-7920-3eb2-aa95-a0b41734dc1d | -20.3142 | -48.7353 | 2024-10-09 03:46:58 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 5f34aa68-ec58-34ed-bbb9-51af759b0287 | -20.334 | -48.7538 | 2024-10-09 03:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 35642b94-a00a-36d2-8cae-75723120aa5d | -20.3346 | -48.7307 | 2024-10-09 03:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 613.7 |
| 8c1f87f4-565a-3ff0-bd2e-ab3c664870aa | -20.3352 | -48.7076 | 2024-10-09 03:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 250bc883-4b93-37a3-beaf-48ed9dc32e15 | -20.3551 | -48.7262 | 2024-10-09 03:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 363.1 |
| 3c969855-aa83-3a8e-8a8b-2fc07323c118 | -20.3557 | -48.7031 | 2024-10-09 03:46:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 6886fb4e-530c-388c-9dce-3a64385bcd5a | -21.572 | -46.9898 | 2024-10-09 03:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c5c978fa-33fd-3558-a057-0e1eaec37406 | -21.5727 | -46.9659 | 2024-10-09 03:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e581f13a-39b0-3f13-b213-9441453e2a39 | -21.5928 | -46.9845 | 2024-10-09 03:47:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 67.9 |
| ab28aa5e-e114-3886-b3d9-951487f34ca1 | -21.6114 | -47.7357 | 2024-10-09 03:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 02d89ea1-0bc2-374b-be3f-c24f702a6dd5 | -1.11 | -53.6173 | 2024-10-09 03:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 3bb6dc2a-08b6-3ea1-86ef-c71bd99fd437 | -3.9394 | -46.445 | 2024-10-09 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6b78b289-d58e-3f20-b169-0d73e6173014 | -3.9393 | -46.4672 | 2024-10-09 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| d7113ba7-279b-3d0c-a8fd-a254040d306f | -3.9023 | -46.4467 | 2024-10-09 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9fb350f6-8b0c-3eaa-96e4-995ae444e1d8 | -3.9021 | -46.4689 | 2024-10-09 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| bbdb2504-6314-3d0e-b18c-1ea2219ba142 | -6.7799 | -60.036 | 2024-10-09 03:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 5b163f62-1ff3-3bf0-a85b-d10fa23f10f5 | -6.7798 | -60.0552 | 2024-10-09 03:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 4bf1fbe7-78dd-3512-a636-3aa405b4e986 | -6.7614 | -60.0559 | 2024-10-09 03:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 7d8f1efc-99d0-3890-9b7f-2dcdde6ebd10 | -6.7613 | -60.0751 | 2024-10-09 03:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c384aabc-72c6-3924-91e0-77e0755b66e5 | -8.4919 | -48.6476 | 2024-10-09 03:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 3b94cb78-bf9c-30ee-9560-5ba1e8c0b030 | -10.4287 | -60.9979 | 2024-10-09 03:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 391634c7-8d7b-3e74-9d9c-7e0eb5dd8376 | -10.3843 | -64.8255 | 2024-10-09 03:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c0024b67-0fe3-3483-9fd1-3d2c57950755 | -10.3842 | -64.8443 | 2024-10-09 03:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1c9af3be-9d8f-3804-b7f4-5f9aca54e653 | -10.3894 | -61.2502 | 2024-10-09 03:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 34a9b44d-ff55-3115-9962-ca8ff683c1d3 | -10.3656 | -64.8262 | 2024-10-09 03:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4cda11cb-2408-3787-aaf6-afcfdd63d59f | -10.3655 | -64.8451 | 2024-10-09 03:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 058645f0-3120-3da6-b9bc-ed0af08b1eb8 | -10.6258 | -55.8953 | 2024-10-09 03:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 04317598-5424-3bcb-ac87-be4cc6c1186b | -10.6256 | -55.9154 | 2024-10-09 03:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 4956bb05-8424-3352-ace2-744fc0150af6 | -10.6253 | -55.9355 | 2024-10-09 03:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |


[Clique aqui para ver as próximas entradas](README68.md)
