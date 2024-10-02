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

## Dados Diários - Página 201

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 973b5e87-97dd-3564-8998-cb146e30cebb | -16.6326 | -57.1943 | 2024-10-02 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 12e63728-e533-30c2-aed4-166ad45b3362 | -16.6518 | -57.2125 | 2024-10-02 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 352bf063-218e-3ebe-89b4-f18b10fe1ae6 | -16.8894 | -55.8247 | 2024-10-02 08:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 1065508b-1f68-34cf-b22c-1151a8ac808f | -16.8292 | -55.9152 | 2024-10-02 08:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| e4064272-5e0a-361b-a8fc-2cfd6255062d | -16.8295 | -55.8945 | 2024-10-02 08:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 651dbba5-47f3-35f1-9c33-518275615b97 | -16.8695 | -55.848 | 2024-10-02 08:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 5823b004-ed3e-37eb-932b-91c7c833563f | -16.8891 | -55.8455 | 2024-10-02 08:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 127.9 |
| eff6f0d0-71ff-3d7c-bdd2-a66d930507dd | -21.3661 | -55.6807 | 2024-10-02 08:47:05 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 333041d0-7a19-3590-bdde-0e80f221f786 | -10.8942 | -63.8971 | 2024-10-02 08:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 499eb499-edf8-3d9f-bad6-80b2aa66c433 | -11.2565 | -60.6019 | 2024-10-02 08:56:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 96a2e468-93e5-3e58-b8c4-ee53dfcec182 | -12.6484 | -63.1214 | 2024-10-02 08:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9195ff25-ffb2-37b3-a9e1-a3de491d71c6 | -12.8615 | -62.5129 | 2024-10-02 08:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 131.8 |
| e85e1393-1383-3d43-a2ba-b3f21817e75a | -12.8614 | -62.5321 | 2024-10-02 08:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0cf70207-520e-3515-b1b5-9f4f240a65ba | -12.8805 | -62.5117 | 2024-10-02 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 5916afb2-630f-3505-9dc9-fae743ea0cb8 | -12.8803 | -62.531 | 2024-10-02 08:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 130.7 |
| f7c90ad7-5fc3-33fd-87ac-5f4db7f77a17 | -15.5486 | -56.8873 | 2024-10-02 08:56:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6d3bedba-dcf9-3184-be3b-076e8379bdd0 | -16.6322 | -57.2147 | 2024-10-02 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 287.9 |
| bcc35946-6d2a-37ee-9834-f8cdf6129270 | -16.6326 | -57.1943 | 2024-10-02 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| db254961-1f6a-336d-9bc0-00b050e1cad2 | -16.6518 | -57.2125 | 2024-10-02 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 170.0 |
| 123862b0-d5c2-3d5c-89e6-ada8971f048b | -16.6319 | -57.2352 | 2024-10-02 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| ed6461a2-44dd-31a4-b5ec-a8434eede623 | -16.6171 | -58.214 | 2024-10-02 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| bcaec930-42b7-302b-b2ac-7de4fc8afc89 | -16.6168 | -58.2343 | 2024-10-02 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 14d0d4f7-8dbd-38fb-adda-1bc9140159cf | -16.6127 | -57.217 | 2024-10-02 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 6a8a0bc6-52d3-3a5c-b2f4-718e9d18e84f | -16.6124 | -57.2375 | 2024-10-02 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 0c548110-8589-30fc-ae6a-dcba5637943a | -16.5976 | -58.2162 | 2024-10-02 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 265.1 |
| 57e62fa4-1eb6-3ab7-aa27-b327b0c2fe1a | -16.5973 | -58.2365 | 2024-10-02 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 428.5 |
| 0895584b-c086-3e92-88e2-3856db29b06d | -16.578 | -58.2183 | 2024-10-02 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 9a5b32ea-1487-3b7d-9cd2-237061b79559 | -16.5778 | -58.2386 | 2024-10-02 08:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.7 |
| 0b96e313-fca7-31d9-b80f-b9cdb9671201 | -12.6484 | -63.1214 | 2024-10-02 09:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 14ecd41d-e465-33ab-a8d8-f40574598594 | -12.8615 | -62.5129 | 2024-10-02 09:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| c8874e27-e83a-373a-ad30-2d77df388ddf | -12.8614 | -62.5321 | 2024-10-02 09:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7430a8e4-7b81-34ac-aa29-284c55c93e04 | -12.8803 | -62.531 | 2024-10-02 09:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 0162370e-2e78-3ebe-9d58-410d1ccb40c9 | -12.8805 | -62.5117 | 2024-10-02 09:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 139.7 |
| a708d1d5-8c3d-305e-afc7-cd028aca13fd | -12.6484 | -63.1214 | 2024-10-02 09:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| dba058c1-b8e8-3f63-9e35-40d0c2b15c9a | -12.8615 | -62.5129 | 2024-10-02 09:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| f6ebbeff-6696-3d78-b7b1-463bb42f243a | -12.8805 | -62.5117 | 2024-10-02 09:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 3051e599-3328-3a80-bf0c-7902a2905615 | -12.8803 | -62.531 | 2024-10-02 09:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b7c1658e-815e-30a8-b34f-47a499aed1c6 | -13.5572 | -51.1846 | 2024-10-02 09:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 3425cc1d-2318-36aa-a896-f466467b8343 | -13.5569 | -51.2061 | 2024-10-02 09:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 2f664723-8399-328d-a44f-8c1b1137777e | -15.9003 | -50.1537 | 2024-10-02 09:16:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 32d0f345-f47b-31fa-914c-42fd3bfc9c6a | -13.538 | -51.1871 | 2024-10-02 09:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 7adcf3e7-87b9-31d0-93d9-dabee7c86732 | -13.5376 | -51.2085 | 2024-10-02 09:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 923b8f9b-0143-3ff6-a343-1abc62044ef0 | -13.5569 | -51.2061 | 2024-10-02 09:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 423.2 |
| f0d954e4-5cfa-3e46-9e4a-ba409dfcb0a1 | -13.5572 | -51.1846 | 2024-10-02 09:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 328.8 |
| f2be89dd-6768-3d35-b6af-f5caea7db498 | -15.9003 | -50.1537 | 2024-10-02 09:26:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 807636f3-0b56-3fa0-956e-19809d7abb3c | -13.538 | -51.1871 | 2024-10-02 09:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 392.8 |
| 3f5122e2-02e7-3c8b-ba7e-753ac84e7f0e | -13.5376 | -51.2085 | 2024-10-02 09:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 487.4 |
| ca464f9a-dfb3-3361-a5b6-3e4290b09220 | -13.5569 | -51.2061 | 2024-10-02 09:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 428.8 |
| 93fee173-7459-3298-a61d-3b2eb9aecdef | -13.5572 | -51.1846 | 2024-10-02 09:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 868e92bc-fa9b-39e1-aff4-ec1de25f43e5 | -15.9003 | -50.1537 | 2024-10-02 09:36:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 94de08d6-40e5-3c72-9467-0ae3ce78a383 | -16.8891 | -55.8455 | 2024-10-02 09:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 135.6 |
| 6cc5e4b9-bfba-3ac1-a347-43159f975446 | -12.1597 | -50.0501 | 2024-10-02 09:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 50e31649-fc2a-31af-99e5-7fedd88796f0 | -12.1593 | -50.0717 | 2024-10-02 09:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 86363f02-364d-3dc2-82ad-105b33607fdf | -15.9003 | -50.1537 | 2024-10-02 09:46:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 153.7 |
| e69b3862-a152-36de-b66c-e2fed26dc758 | -16.6322 | -57.2147 | 2024-10-02 09:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 201.5 |
| 5e754657-cf54-3cf0-8d9f-18e66fc9b55b | -16.5976 | -58.2162 | 2024-10-02 09:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 238.3 |
| 0bb9e395-ba0d-3ccd-aa87-5c2c2913bd1a | -16.5973 | -58.2365 | 2024-10-02 09:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 364.7 |
| 001a879e-f12b-3dc6-95ee-acdf283975bd | -16.5778 | -58.2386 | 2024-10-02 09:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 916f273f-d7ea-386d-9c16-995f190b417f | -16.7265 | -57.4287 | 2024-10-02 09:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 12c92b25-2f01-37fa-8934-4682cdb793d5 | -12.1597 | -50.0501 | 2024-10-02 09:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 7cae79e4-ed84-3b84-a547-d5ad6e910d9e | -12.1593 | -50.0717 | 2024-10-02 09:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 33d7fcc7-ee82-3b3a-b33d-127e87bd1d5c | -13.538 | -51.1871 | 2024-10-02 09:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 372.5 |
| 02e52e15-f076-31bf-af2c-848b22da2fd0 | -13.5184 | -51.211 | 2024-10-02 09:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 9717b9f7-6bed-31ae-9045-3db89eab9b6d | -13.5373 | -51.23 | 2024-10-02 09:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3ee755cf-9d0a-3f01-8105-619230ea24da | -13.5376 | -51.2085 | 2024-10-02 09:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 601.6 |
| 104c733d-d167-3e85-969f-b26c1d73aa76 | -13.5569 | -51.2061 | 2024-10-02 09:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| fc3054c2-08d2-3795-b34b-c3436358a9c3 | -15.5486 | -56.8873 | 2024-10-02 09:56:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 15b63796-6c82-3cfd-96d2-5c546d8f96d1 | -16.5778 | -58.2386 | 2024-10-02 09:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| e2d7bc12-5cc1-3c42-b814-8a4c30a0585b | -16.5973 | -58.2365 | 2024-10-02 09:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 287.0 |
| 1aa713fe-0c25-33a5-9d72-2c6e971262bc | -16.5976 | -58.2162 | 2024-10-02 09:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 209.4 |
| e7c4d3a0-246b-3eb0-bf93-98f33b2a972e | -16.6322 | -57.2147 | 2024-10-02 09:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 163.7 |
| 24965121-585f-3da4-9723-9dfd14866a40 | -16.7265 | -57.4287 | 2024-10-02 09:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| a95ea88a-eb77-39d0-a219-e66d24b6e94a | -12.1597 | -50.0501 | 2024-10-02 10:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1f048d59-c090-328b-89a1-a9526e26c410 | -12.8803 | -62.531 | 2024-10-02 10:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 114.7 |
| eb51262b-9176-3646-9eb4-62267a78c55e | -12.8805 | -62.5117 | 2024-10-02 10:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 70dfa765-262f-3f8a-9146-aa23caeef5ff | -13.5184 | -51.211 | 2024-10-02 10:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 8f1ff7f7-a5ee-3144-a6d9-477a905347ee | -13.5188 | -51.1896 | 2024-10-02 10:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 1645d575-f16a-361c-9102-c28c13573246 | -13.5376 | -51.2085 | 2024-10-02 10:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 238.9 |
| fba630ad-2426-3a8e-81d0-2eeb2795b284 | -13.538 | -51.1871 | 2024-10-02 10:06:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 6ead1a2d-e7f3-34b5-bef5-02bf8604a31b | -15.5486 | -56.8873 | 2024-10-02 10:06:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0b0abd78-df99-3000-a74e-d7da2805ecd1 | -16.5778 | -58.2386 | 2024-10-02 10:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.9 |
| 753d41fc-0fba-3cd1-a073-7106b4ebe842 | -16.5973 | -58.2365 | 2024-10-02 10:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 242.2 |
| f6d958ab-4355-368a-a7c5-43d871817287 | -16.5976 | -58.2162 | 2024-10-02 10:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 191.8 |
| 96e92211-38f9-308d-afc1-eaa51fb8d4da | -16.6322 | -57.2147 | 2024-10-02 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.2 |
| d9164cdf-6372-3852-abe7-87dcd6ff11b2 | -13.0211 | -51.1456 | 2024-10-02 10:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 264.7 |
| 9176989d-3b98-318b-a183-a2cf489ed4ed | -13.0207 | -51.167 | 2024-10-02 10:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 62fdd879-fd13-36f4-9f96-3aaac5edbeec | -12.8805 | -62.5117 | 2024-10-02 10:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 07112d33-5ede-3a9d-9867-25d7ee281a84 | -12.8803 | -62.531 | 2024-10-02 10:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 5cebe838-cc55-3b70-9834-214ca99b7c56 | -13.2173 | -48.624 | 2024-10-02 10:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b6dd3f73-d573-3506-b57c-8a39588f2d23 | -13.5376 | -51.2085 | 2024-10-02 10:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 44f18c51-98a4-3e6c-a5db-f034595e3f48 | -15.5486 | -56.8873 | 2024-10-02 10:16:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| db2e993f-cd55-371b-9c16-9273a63ea175 | -16.6322 | -57.2147 | 2024-10-02 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| d2782bcf-d17f-3262-aed2-edcc164f6d6d | -16.5976 | -58.2162 | 2024-10-02 10:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 209.6 |
| af9c2130-5ca0-3c63-9032-e248c4603c7a | -16.5973 | -58.2365 | 2024-10-02 10:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 259.7 |
| 04a10c64-f856-394c-b239-d98485c7f599 | -16.5778 | -58.2386 | 2024-10-02 10:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 2dc1edec-7c56-3641-9c46-35f95c38157e | -16.8983 | -57.6949 | 2024-10-02 10:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 0db5978f-45f1-3d1c-be86-c56e30413009 | -22.5502 | -48.1834 | 2024-10-02 10:17:10 | GOES-16 | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 157.3 |
| d8faf392-cdbd-3fef-bbb6-e4704b14ed7e | -22.5293 | -48.1887 | 2024-10-02 10:17:10 | GOES-16 | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 116.5 |
| a6c69d4e-d995-330f-95f7-eccbb18e0867 | -12.1597 | -50.0501 | 2024-10-02 10:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 922264cc-75be-3c97-a66c-8ace28e5baea | -12.8805 | -62.5117 | 2024-10-02 10:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |


[Clique aqui para ver as próximas entradas](README202.md)
