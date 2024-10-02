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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a179ea92-4a84-3a21-8a72-b09e80ff5c1b | -16.6909 | -57.208 | 2024-10-02 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 6cd56a42-da1b-30e7-a57a-77f9d358fb1d | -16.6868 | -57.4741 | 2024-10-02 04:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 2786869e-b812-3560-9473-758205e536d5 | -16.6322 | -57.2147 | 2024-10-02 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 03ed71a9-d0e9-39e7-abab-d47a69447e22 | -16.8894 | -55.8247 | 2024-10-02 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| f011538e-6957-3386-a432-c98195ce7cfb | -16.8891 | -55.8455 | 2024-10-02 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| 79256070-0e93-3123-86ab-c1d9f40f96df | -16.8698 | -55.8272 | 2024-10-02 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 1b6e3a3a-1084-3956-a62c-79f512d7d0d9 | -16.8695 | -55.848 | 2024-10-02 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 135.4 |
| ae92cc46-9149-303f-82f5-b8025c156e93 | -16.8386 | -57.7628 | 2024-10-02 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.4 |
| 287cde98-7015-3cb2-a425-6cf351d43695 | -16.8295 | -55.8945 | 2024-10-02 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.3 |
| 69241373-fa7c-3ebc-9200-6ff057030c75 | -16.8292 | -55.9152 | 2024-10-02 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 1d56b010-5f37-3f0a-a2a0-675283baa02d | -17.1091 | -56.7479 | 2024-10-02 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.8 |
| a566b854-1717-3325-9977-c3acfc36670d | -17.1088 | -56.7685 | 2024-10-02 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 92f89aee-ddf1-307c-8a52-ba8db7075df8 | -17.0895 | -56.7503 | 2024-10-02 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 5acf4908-a3f7-3fe6-a3c5-e5ffbba5aced | -17.0892 | -56.7709 | 2024-10-02 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 7b46818f-b78d-3b0c-a861-7c6c743fe6fb | -17.0709 | -56.6908 | 2024-10-02 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 1fb98b45-96ae-329d-ae2b-01c90d8a1008 | -17.0705 | -56.7114 | 2024-10-02 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 9dea429a-3690-3719-943d-f1838c4a2bc6 | -17.0695 | -56.7733 | 2024-10-02 04:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 3518912f-a928-32e5-8d61-5f96aff38e0e | -20.5259 | -46.3023 | 2024-10-02 04:06:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1a2040b0-41ff-3e37-a8f7-03547322148b | -20.5053 | -46.3074 | 2024-10-02 04:06:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6541d1b6-bde6-3209-be8c-e5c5b26701a8 | -21.3661 | -55.6807 | 2024-10-02 04:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e3749b7a-e1f1-3048-bb03-58f244748391 | -21.3456 | -55.6841 | 2024-10-02 04:07:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1768b8a6-596c-3cb7-b927-8ba0ba8c5481 | -5.9788 | -45.3621 | 2024-10-02 04:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4a367bc7-241d-326c-92e9-5013a54ddcc9 | -5.9786 | -45.3847 | 2024-10-02 04:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 2b7f20a6-4bb3-31ee-9231-8862f60a1ea7 | -9.9553 | -64.9172 | 2024-10-02 04:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7f2ec8f4-a3c3-37f0-a7a6-d8169cd9a1e5 | -9.9368 | -64.8991 | 2024-10-02 04:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 015fc0ea-da2e-3945-b83b-fc030ed9c597 | -9.9367 | -64.9179 | 2024-10-02 04:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 52c8d6b0-8db9-34cd-a85f-d324f9cef616 | -10.867 | -69.495 | 2024-10-02 04:16:08 | GOES-16 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 777402f1-efa8-3a4f-a68a-85f4505432f2 | -11.6931 | -64.9974 | 2024-10-02 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d93f92bf-9029-3db5-9642-32de02bad15d | -11.6743 | -64.9983 | 2024-10-02 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e5ad373d-4991-3444-a1d4-a0925e78e93c | -11.6742 | -65.0172 | 2024-10-02 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 3e3789e5-24de-329a-bf72-e4f2d1f8a174 | -11.6554 | -65.018 | 2024-10-02 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ef8dd51c-cdbb-3fb3-a4aa-d1b689032cca | -12.6486 | -63.1022 | 2024-10-02 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e369d81c-4225-3b99-85b6-6d9a0a56266b | -12.6484 | -63.1214 | 2024-10-02 04:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 612b945f-1e56-3a25-b26d-cf137dc15302 | -12.8803 | -62.531 | 2024-10-02 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e0043627-c718-3eaf-b952-9e6822d708fa | -12.8614 | -62.5321 | 2024-10-02 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 3e70f290-a36a-35dd-be99-fd8bee74a536 | -12.8612 | -62.5514 | 2024-10-02 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 136.7 |
| b88cb287-a771-3fbe-bc78-7c32577eb2be | -12.8426 | -62.514 | 2024-10-02 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8c8ac16f-79f7-3fc6-bcc4-5a8cd207602a | -12.8424 | -62.5333 | 2024-10-02 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 512a3c88-15e6-3cc2-ab0d-d069df204e65 | -12.8423 | -62.5526 | 2024-10-02 04:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 3b6e3aba-ea98-388b-a458-5d7a43194791 | -13.1122 | -51.4329 | 2024-10-02 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 96ad1c89-4435-385a-a8aa-22a56ddf2913 | -13.0745 | -51.3949 | 2024-10-02 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ec29f068-523f-33fa-b448-3bea23fa9516 | -13.0742 | -51.4163 | 2024-10-02 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 70fa7da5-21a4-3561-b3fd-b7aaf0b17522 | -13.0553 | -51.3973 | 2024-10-02 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e8dce031-c976-3117-a51a-e5c2f66fbd35 | -13.055 | -51.4186 | 2024-10-02 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ed7e9cb3-4ad1-3070-bfb2-887dc0176313 | -13.2173 | -48.624 | 2024-10-02 04:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4a634c35-dc78-3063-a797-eb5014257718 | -15.8936 | -57.155 | 2024-10-02 04:16:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 85912868-730a-3755-a0a6-f5789fd2644d | -15.8933 | -57.1754 | 2024-10-02 04:16:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4e8731eb-f712-3c09-a049-c8dc83b41a86 | -16.6127 | -57.217 | 2024-10-02 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 449c2800-b74a-3376-9bcf-ab2e97bd2c64 | -16.6124 | -57.2375 | 2024-10-02 04:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 4a6ae7c0-d0a3-3b1b-b5af-2c22fb69694b | -16.514 | -57.2896 | 2024-10-02 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 25e14806-1a01-35d7-b4f2-ecdd5b020480 | -16.5137 | -57.31 | 2024-10-02 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 23df5291-02ee-38f0-9c3c-f23c0292b4b2 | -16.4945 | -57.2918 | 2024-10-02 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 93f8c347-0be5-3be1-9689-990a2500d065 | -16.4942 | -57.3122 | 2024-10-02 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| b1d9f3c3-b811-30b5-a53d-adfa2eeabe85 | -16.475 | -57.294 | 2024-10-02 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 0589a5d6-6eba-3af8-8069-b8254874e645 | -16.4746 | -57.3144 | 2024-10-02 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| fdcf6d46-1928-3173-a8f0-0088ac3c621c | -16.8096 | -55.9177 | 2024-10-02 04:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| d56f1791-5e60-3ed6-8cdf-f0993c02c34b | -16.7108 | -57.1852 | 2024-10-02 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| ea22b7f1-f999-37f7-85ff-1f95d3e107b5 | -16.7063 | -57.4718 | 2024-10-02 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 0e318b18-5a5f-3982-8808-1ecff7cd6e2b | -16.6916 | -57.167 | 2024-10-02 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| aaaa09ec-1d7f-38c7-9445-ec4b7c4fa2d1 | -16.6912 | -57.1875 | 2024-10-02 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| a6a5ee65-ed45-37e6-bd10-3417f3bc77de | -16.6868 | -57.4741 | 2024-10-02 04:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 10c11157-3171-3690-8c5a-6058b07cb932 | -16.6322 | -57.2147 | 2024-10-02 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| fbc6feb5-0b9c-32a5-a42e-cfbb08ff025f | -16.8894 | -55.8247 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| ed27f034-049c-330b-9a04-98e4f668dd75 | -16.8891 | -55.8455 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 127.1 |
| c3cea5b1-5cab-3d6a-9fd2-bbe82590bcdd | -16.8698 | -55.8272 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 156.7 |
| b687bc78-b533-345f-8746-cfaf282b0fa1 | -16.8695 | -55.848 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 204.7 |
| d2dbe94e-9a2e-3e33-941c-7d1d3bd19faf | -16.8491 | -55.892 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 67f4fdf8-0029-336a-91c8-7d10c77a7972 | -16.8488 | -55.9128 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 296d85c0-7f22-322a-bd14-d7ab76b6f6b3 | -16.8299 | -55.8737 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| ff7a8148-3d94-3c20-aa9c-aa968cc02fab | -16.8295 | -55.8945 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| bae7b4c6-dab6-3fe4-baf9-917765be178d | -16.8292 | -55.9152 | 2024-10-02 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 1b80104a-0f6f-3ff6-9339-2746a2354eba | -17.0709 | -56.6908 | 2024-10-02 04:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 4a6dc237-02c1-3346-a153-11f877c5668f | -18.3281 | -43.2276 | 2024-10-02 04:16:47 | GOES-16 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.2 |
| 4cfbfe6c-c297-334f-9083-c6afd3d0c004 | -20.5259 | -46.3023 | 2024-10-02 04:16:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| e24c5697-7ee5-3a8f-aebd-447188ce2f44 | -20.5053 | -46.3074 | 2024-10-02 04:16:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| f2144c01-0473-3bf6-9d09-541da774a08f | -21.3661 | -55.6807 | 2024-10-02 04:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 79.1 |
| bd4d54ef-47f6-30a7-845a-e23068d60024 | -21.3456 | -55.6841 | 2024-10-02 04:17:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4a48f27e-04b7-3ce2-86ce-0bbb372bc523 | -22.3929 | -49.2727 | 2024-10-02 04:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.1 |
| b60f3b74-2397-3826-8424-8bdd7f146405 | -22.3922 | -49.2961 | 2024-10-02 04:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 220.3 |
| fcdd2b67-801e-3943-8948-4d6ae57630c2 | -22.372 | -49.2777 | 2024-10-02 04:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 200.2 |
| ba90d28b-d11f-3bbf-933d-d55d4e500655 | -22.3713 | -49.3011 | 2024-10-02 04:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 250.0 |
| 03c2ace1-1d0e-38e8-9cf6-2b867a722530 | -22.3505 | -49.306 | 2024-10-02 04:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| 21027368-542f-39d6-bb3e-ca018f0fd555 | -9.9367 | -64.9179 | 2024-10-02 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c33acb5c-b602-304b-aa0e-e6d3f44e5f7e | -9.9368 | -64.8991 | 2024-10-02 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b694014b-a023-37ea-85fe-415ac4a1b773 | -9.9554 | -64.8984 | 2024-10-02 04:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 6303e21f-fbc6-35e3-9811-9a01a8d12ef1 | -10.8483 | -69.4954 | 2024-10-02 04:26:08 | GOES-16 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 67ec8e77-5947-38e8-8110-d079de58da1f | -10.867 | -69.495 | 2024-10-02 04:26:08 | GOES-16 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 90.8 |
| b509b60d-3ec4-39bf-8f95-4e3022e8d274 | -10.9899 | -63.57 | 2024-10-02 04:26:09 | GOES-16 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 0076e035-a8ad-37ce-9cb5-5d125abdde75 | -11.0087 | -63.5691 | 2024-10-02 04:26:09 | GOES-16 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1d7b7c68-cbef-3112-896e-a42221d6130e | -11.6742 | -65.0172 | 2024-10-02 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e9fe9c9a-4a4c-38e9-aef7-c3b17b4afb15 | -11.6743 | -64.9983 | 2024-10-02 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 162.5 |
| a5533823-6978-3655-982e-04033ceb630c | -11.6931 | -64.9974 | 2024-10-02 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c0068ac9-7900-30ba-9836-1750111ced05 | -12.6484 | -63.1214 | 2024-10-02 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d58fcf84-83ef-3361-a20d-986d220587e9 | -12.6486 | -63.1022 | 2024-10-02 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4611c74a-c79b-3e22-98f3-29e44120712a | -13.055 | -51.4186 | 2024-10-02 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 75c512fe-e593-33aa-8ed8-bc1a347b8dcd | -13.0553 | -51.3973 | 2024-10-02 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 75e6931b-7ea5-3723-bac4-45b0b1c6b330 | -13.1122 | -51.4329 | 2024-10-02 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d03b1bb0-40d8-3832-9d8e-4ffd93896ed1 | -13.1125 | -51.4115 | 2024-10-02 04:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9f7839b4-4179-3d49-889f-2cb4ea7ac4d9 | -14.7787 | -48.7882 | 2024-10-02 04:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 4e2cf3f0-1e6d-395c-82b6-911c869a8824 | -14.7791 | -48.7659 | 2024-10-02 04:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 136.7 |


[Clique aqui para ver as próximas entradas](README81.md)
