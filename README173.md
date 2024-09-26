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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 213a9a46-f451-3e8b-973f-dbf195bc123b | -9.1216 | -61.3526 | 2024-09-26 07:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| eb9a5db7-a9ae-3784-8ad0-b13058dddd05 | -11.2036 | -54.7548 | 2024-09-26 07:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 4db73d16-7073-3c9a-bbc0-d484987f5f7f | -11.2034 | -54.7752 | 2024-09-26 07:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 3ef0e52e-d1fe-33cf-949d-aba8d63b97b4 | -11.2031 | -54.7956 | 2024-09-26 07:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2a868cfd-b56d-348d-9329-aaefea509647 | -11.26 | -65.2801 | 2024-09-26 07:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 22be420a-4331-3d09-96e3-5877f5c8a9c0 | -11.2599 | -65.299 | 2024-09-26 07:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7f843920-ed3f-3b4c-b66b-279a87e90c91 | -12.9043 | -51.2667 | 2024-09-26 07:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| f50f2c16-0209-341f-b8e7-2f3aab07f13a | -12.904 | -51.288 | 2024-09-26 07:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5e54f5cc-b20d-37aa-927c-b4b59b3eeaed | -12.8852 | -51.269 | 2024-09-26 07:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| ecab8e7f-3404-33b8-82bf-1357849ab6c3 | -12.8848 | -51.2904 | 2024-09-26 07:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2667f812-290f-38f6-a06c-df018a3c688e | -12.866 | -51.2714 | 2024-09-26 07:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 501cc370-3d7a-348d-b135-f8d2f8ac7858 | -16.8234 | -57.4789 | 2024-09-26 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 4fd2f961-4205-3617-8f36-46b6fb90b636 | -16.8231 | -57.4994 | 2024-09-26 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 4cdda18e-ad0a-3846-a041-7e89c9dd6a97 | -16.8039 | -57.4811 | 2024-09-26 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| cf053fe1-7305-3021-8ad5-0fa74e462f7f | -16.8036 | -57.5016 | 2024-09-26 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 30806581-591b-3795-b08a-6a0fad7abdf5 | -21.9374 | -48.5688 | 2024-09-26 07:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 38008899-3bf9-30ed-bcc6-c2356d765382 | -7.2905 | -61.106 | 2024-09-26 07:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 48126973-00c7-3b20-83b7-8cf2a308f2d0 | -8.1394 | -61.2817 | 2024-09-26 07:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 248b4f65-702e-399a-8cd7-00fad7616de5 | -8.4156 | -70.7535 | 2024-09-26 07:35:55 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 022d8d9f-bc2c-3c3b-a4ff-67ae72c996a5 | -9.1216 | -61.3526 | 2024-09-26 07:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 83fcd4eb-3d2a-338c-a5ab-38a41bea2310 | -9.1217 | -61.3334 | 2024-09-26 07:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d85a64bc-43a3-39c6-92ed-fd081d1663c4 | -11.26 | -65.2801 | 2024-09-26 07:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| cfdc5a17-5eba-379a-a02b-7f3333a4f338 | -12.8848 | -51.2904 | 2024-09-26 07:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 4a56b7f0-fa02-33a3-aedd-49b0ed1b6f4b | -12.8852 | -51.269 | 2024-09-26 07:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c96b6f4a-5ec1-3bb0-a0bc-07bc3e8036f1 | -16.8036 | -57.5016 | 2024-09-26 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| f6bbad6f-ce4c-31de-9f08-c63c934909d5 | -16.8039 | -57.4811 | 2024-09-26 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| b92eb21d-6a3e-3c45-b566-5beee9bbf734 | -16.8231 | -57.4994 | 2024-09-26 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 4c862062-41d2-335a-9c8f-117b9f567198 | -16.8234 | -57.4789 | 2024-09-26 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 09e38c6f-adfa-31ea-acd5-042fe6d9408e | -17.0991 | -56.1711 | 2024-09-26 07:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| b4a4e1d8-6ad2-324d-889b-7ed4fc8eb023 | -17.0995 | -56.1504 | 2024-09-26 07:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 79479299-6e62-30ec-bd1c-37f7c4be2777 | -17.1188 | -56.1686 | 2024-09-26 07:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 619f33db-ad0d-3d8f-980a-15ae67520d05 | -20.6074 | -51.5209 | 2024-09-26 07:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.9 |
| da53d1c1-b21e-360b-a1d2-3978e091200d | -21.9374 | -48.5688 | 2024-09-26 07:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 50578ad4-8cda-3497-aa29-2158a2d2c661 | -9.1217 | -61.3334 | 2024-09-26 07:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| fb1343a8-e079-359f-a90c-2bc85d6dab94 | -9.1216 | -61.3526 | 2024-09-26 07:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ecfe2989-ac2f-3137-92a5-5c2ecf49b10c | -11.2036 | -54.7548 | 2024-09-26 07:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1cd35bed-bceb-38c0-8080-fef66af22027 | -11.2034 | -54.7752 | 2024-09-26 07:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| aa4df659-35a7-35bd-b282-290288d395aa | -11.26 | -65.2801 | 2024-09-26 07:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8ce392b9-87f3-3913-85c5-c196fcab40c5 | -11.2599 | -65.299 | 2024-09-26 07:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 6945d9a8-b499-3c81-ac6e-da8c309f2bde | -12.8852 | -51.269 | 2024-09-26 07:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1a05f018-9a80-370e-8168-20059b348ea7 | -12.8848 | -51.2904 | 2024-09-26 07:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f2c9f5d8-9436-3f71-92ad-a84c599fb8bf | -16.8234 | -57.4789 | 2024-09-26 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 9dc4c0dd-c452-39cc-8d27-2ecc6f5c069d | -16.8231 | -57.4994 | 2024-09-26 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 8dc2d1d6-65ac-32bb-b0c8-dd5ed97b0a14 | -16.8039 | -57.4811 | 2024-09-26 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 3e365da3-ed37-3385-a253-34a59179677c | -20.6074 | -51.5209 | 2024-09-26 07:47:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| ce66103c-96a2-36c2-b97e-2150ecb5af4f | -20.608 | -51.4986 | 2024-09-26 07:47:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.4 |
| 3c9d6454-94a6-3923-8c87-93832e2c6d91 | -6.9306 | -63.1053 | 2024-09-26 07:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 9b768814-be5f-342b-b022-6daddbf01d75 | -7.2905 | -61.106 | 2024-09-26 07:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| cb3f7ffe-15a4-3b79-ab6a-028e5deaba01 | -7.2906 | -61.0869 | 2024-09-26 07:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 4c556bbd-e553-3858-a09b-47e0bb02f1b0 | -8.1394 | -61.2817 | 2024-09-26 07:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 0ddc76e3-e7e3-3314-9335-c2d61dabc84d | -9.1216 | -61.3526 | 2024-09-26 07:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 858bc0fb-2a9c-30c7-a904-677c8a121780 | -9.1217 | -61.3334 | 2024-09-26 07:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 13cd27af-6aeb-3e8c-b082-1496fc10e8dd | -11.2034 | -54.7752 | 2024-09-26 07:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 89d9b346-9a3c-3d79-844b-9c5f5e7dd83f | -11.2036 | -54.7548 | 2024-09-26 07:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ce21d177-9369-35c1-890a-81d31b58bc88 | -11.26 | -65.2801 | 2024-09-26 07:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b8316d20-b16f-3f84-89c5-8a534320dd25 | -11.616 | -60.3463 | 2024-09-26 07:56:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b8c21548-52bb-3fe5-95e6-448e2fb41897 | -16.1185 | -51.9651 | 2024-09-26 07:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 83162f7b-2fe3-3ae7-be8f-41ce29163f27 | -16.118 | -51.9867 | 2024-09-26 07:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| ad3108d8-52eb-3588-b80c-757e6e8b0e55 | -16.0985 | -51.9896 | 2024-09-26 07:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 917fd2e8-1b55-3373-b148-a1a8bac4d6fa | -20.608 | -51.4986 | 2024-09-26 07:57:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 281.0 |
| 4ab72b89-77d4-305f-aa4e-658f0f4d6964 | -20.6074 | -51.5209 | 2024-09-26 07:57:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 247.6 |
| 690ddf45-bc89-3ad1-8a88-a7001e4e6578 | -20.5876 | -51.5026 | 2024-09-26 07:57:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| b5f89145-ee73-3ef7-a9f1-68f2bf4dc9d3 | -20.587 | -51.5249 | 2024-09-26 07:57:01 | GOES-16 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| 165d5074-1a15-30c2-8a88-48874ca5997b | -21.9374 | -48.5688 | 2024-09-26 07:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 36112b8c-5bb9-3de2-87a4-7e67c66afb78 | -10.01 | -53.48 | 2024-09-26 08:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee1e4a02-0158-3ed9-9346-1d32e2f11d24 | -10.04 | -53.42 | 2024-09-26 08:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9394beaa-5423-3b3f-a7aa-ba217e223b11 | -10.04 | -53.48 | 2024-09-26 08:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac8b5129-5d50-3402-858d-cfbfebfe5caa | -10.04 | -53.55 | 2024-09-26 08:04:29 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84d4604f-e4e2-32b9-857b-0037c70371aa | -6.949 | -63.1048 | 2024-09-26 08:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 11fc42ce-c2ee-350b-a4d2-ce3c4f2d71b8 | -7.2905 | -61.106 | 2024-09-26 08:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| f5b71414-71bb-3841-af5c-4257c9b9888c | -8.4156 | -70.7535 | 2024-09-26 08:05:55 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 4ebaf1f3-9d8e-30a3-8f78-614c612de0d6 | -9.1217 | -61.3334 | 2024-09-26 08:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 361dd0af-399a-3989-b143-78a3d5e55059 | -9.1216 | -61.3526 | 2024-09-26 08:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9c0d9963-a67a-32fa-97a3-f6ea3ddb0ab6 | -11.2036 | -54.7548 | 2024-09-26 08:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 58fded2c-fdcc-339a-9091-aba309fab887 | -11.2034 | -54.7752 | 2024-09-26 08:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 26f9afd9-b0da-33bd-952a-07a662612bde | -11.2223 | -54.7735 | 2024-09-26 08:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| bb3d7284-6396-32a6-bc41-fc4711746b46 | -11.2599 | -65.299 | 2024-09-26 08:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 700ab5e3-14a9-30e3-975f-2384d9ef4de2 | -11.26 | -65.2801 | 2024-09-26 08:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 89f136ed-4422-3100-a2eb-d516e6b49fcd | -11.2788 | -65.2793 | 2024-09-26 08:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 12bd0f00-1013-3bfe-9319-81e2ce3d9da7 | -11.5972 | -60.3475 | 2024-09-26 08:06:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 40235f3f-cccc-373b-8392-2a5c596e969d | -16.118 | -51.9867 | 2024-09-26 08:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e06ab083-98b6-31af-a624-46ea594c0954 | -16.0985 | -51.9896 | 2024-09-26 08:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 04d9ff92-2033-33fb-a344-8d565fca39ca | -16.8036 | -57.5016 | 2024-09-26 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| de93093b-5ef8-3e89-855e-ca25312bdf6d | -16.8039 | -57.4811 | 2024-09-26 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| a015bd3c-f19a-3b3f-834c-bb67ea68557b | -16.8231 | -57.4994 | 2024-09-26 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| c843b132-4255-327c-941d-f3d54545f70c | -16.8234 | -57.4789 | 2024-09-26 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| c9680cf3-1ec0-34c3-8649-f6a47d544c8e | -20.6074 | -51.5209 | 2024-09-26 08:07:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 6e68ee9c-589d-3976-b3f7-56ddfda5cbb1 | -20.608 | -51.4986 | 2024-09-26 08:07:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.8 |
| ac7dfdab-bf50-3e2e-92e6-20ce322f3a93 | -21.9374 | -48.5688 | 2024-09-26 08:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 5071a010-9b27-305e-9358-45faf26492cc | -6.9306 | -63.1053 | 2024-09-26 08:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 393f4216-8261-3072-a5f9-96109b3bed01 | -7.2905 | -61.106 | 2024-09-26 08:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 836ac6be-cbbc-3369-bfe9-a8b6f38c810d | -9.1217 | -61.3334 | 2024-09-26 08:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 5d7ffebc-ad54-3219-851c-139b0fa6e930 | -9.1216 | -61.3526 | 2024-09-26 08:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 52d36e51-c348-32b1-a320-5c97f5e7941a | -11.2034 | -54.7752 | 2024-09-26 08:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 1ec7d720-4cee-3cab-88f3-d78ea78570ef | -11.2223 | -54.7735 | 2024-09-26 08:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5a8cb613-9063-35be-972e-4d8744011da3 | -11.2599 | -65.299 | 2024-09-26 08:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6508f7c7-aff2-3417-b5ca-f8143d60a2dc | -11.26 | -65.2801 | 2024-09-26 08:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ca1310e8-3162-33a6-8822-1c2a258271d4 | -11.2788 | -65.2793 | 2024-09-26 08:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| b1fa28e4-8147-34e6-ad08-bb3b3840aed2 | -11.5972 | -60.3475 | 2024-09-26 08:16:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 9424f665-5503-3274-9913-6e73cb8b5016 | -14.8824 | -51.4992 | 2024-09-26 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |


[Clique aqui para ver as próximas entradas](README174.md)
