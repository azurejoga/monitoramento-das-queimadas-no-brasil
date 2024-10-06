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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc5166eb-b2b6-306f-8b0d-0185999fa70c | -17.812 | -53.7859 | 2024-10-06 06:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ad30f844-92b9-393c-8456-cc0c31dac3ef | -18.6387 | -57.2785 | 2024-10-06 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| def78bb1-ec71-3191-8640-ff7289176185 | -18.6391 | -57.2578 | 2024-10-06 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 64379bdf-56ea-3f5b-84bd-cb4a7c6d96ee | -18.6586 | -57.2759 | 2024-10-06 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 9cf26146-6430-3310-9a22-1071db152cb3 | -18.659 | -57.2552 | 2024-10-06 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| a403f94f-fa30-364d-a6d1-6feae38a4b07 | -20.4508 | -51.2846 | 2024-10-06 06:57:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 32490213-7342-3eac-b027-5e5b8d55b303 | -17.02 | -55.06 | 2024-10-06 07:03:48 | MSG-03 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5d14b46f-1bb1-3a35-9716-19cb0235d5df | -10.45 | -50.7 | 2024-10-06 07:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f096cd61-cdb7-3694-95b5-025b32769cae | -10.45 | -50.76 | 2024-10-06 07:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7f29af4-aeed-32cb-a4da-6a2e35e77617 | -10.42 | -50.69 | 2024-10-06 07:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac7339b-823c-3b2e-92df-879b4902d964 | -10.42 | -50.75 | 2024-10-06 07:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bfd2e930-9867-3ae8-9f0c-4d36c05f79dd | -13.3976 | -61.957 | 2024-10-06 07:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 54f28d84-fe71-3230-bf69-bfbe675aa5cf | -16.8241 | -57.438 | 2024-10-06 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 1e0a47f3-705b-3f81-9ec7-1d0b25f14077 | -16.8238 | -57.4584 | 2024-10-06 07:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| a019a797-aace-39a3-b133-f9ce49159b3d | -17.012 | -56.698 | 2024-10-06 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 705da55b-2f92-3faa-946d-c28ba0f23602 | -17.0116 | -56.7186 | 2024-10-06 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 258680cf-a0e2-3f8f-a172-0ecabf4373c3 | -17.0985 | -57.4062 | 2024-10-06 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 40644df3-cc06-38b1-a8ca-31d153ffe39c | -17.0989 | -57.3857 | 2024-10-06 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 1f7ef051-efc3-3f28-8f72-1c219b2c3b2a | -17.1185 | -57.3834 | 2024-10-06 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 65c74ce6-da5f-3350-b3a3-99e2663293ca | -17.1375 | -57.4221 | 2024-10-06 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 894eb832-b0f9-388d-97fc-b214659c9e00 | -17.1182 | -57.4039 | 2024-10-06 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| b726f03c-51f2-32f9-bd47-e829a0739f44 | -17.812 | -53.7859 | 2024-10-06 07:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 150845e8-2c50-3730-87cb-d625bb247e8b | -18.6586 | -57.2759 | 2024-10-06 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 4e006999-7d99-31fb-8d1c-ac1da7a597d9 | -18.659 | -57.2552 | 2024-10-06 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 574b18f8-4308-3558-8142-2299ad948609 | -18.6387 | -57.2785 | 2024-10-06 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 50aafb95-980a-3e39-b588-4db00fcd32bc | -18.6391 | -57.2578 | 2024-10-06 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 08136c6d-513a-383d-9fb0-1d63fc460943 | -20.4508 | -51.2846 | 2024-10-06 07:07:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| 313a2c12-a373-366a-9404-87b4676d34d8 | -13.3976 | -61.957 | 2024-10-06 07:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ee6a60d3-6b95-320f-ac69-b2265d11e13b | -16.8238 | -57.4584 | 2024-10-06 07:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 951e2841-8156-3c90-975d-115f6b56bf30 | -17.0003 | -55.0817 | 2024-10-06 07:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e1d32404-2789-3486-b592-4b7b1882270b | -17.0007 | -55.0607 | 2024-10-06 07:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 6df2bb1e-358d-3bda-bf29-ce96ba02fb3c | -17.02 | -55.0791 | 2024-10-06 07:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 66907e92-0ea4-36b0-a6a8-158acd587909 | -17.0203 | -55.0581 | 2024-10-06 07:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 15045834-6474-3b02-8c56-ae5cc92ffbb9 | -17.0207 | -55.0371 | 2024-10-06 07:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 6211b93f-2dac-3ff0-a3e5-9a6151b19ffb | -17.0116 | -56.7186 | 2024-10-06 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| ad024c28-26ee-3cab-8cf2-c8d9da2dbdc1 | -17.012 | -56.698 | 2024-10-06 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 4dd2f62a-5636-34de-959a-daa5ed1b4e6a | -17.0985 | -57.4062 | 2024-10-06 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| be5ec9c8-83be-3989-a36f-fbf56b852dfd | -17.0989 | -57.3857 | 2024-10-06 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 34c9254b-3203-3d5a-8e19-e822517a570e | -17.1182 | -57.4039 | 2024-10-06 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| edf96986-fe47-3223-b6d7-6dbf95f1f219 | -17.1185 | -57.3834 | 2024-10-06 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| d5043171-31d2-3563-9b8b-b04d3b6e39ac | -17.812 | -53.7859 | 2024-10-06 07:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c425f4a8-7aee-3062-9e4e-3d959de95f65 | -18.6387 | -57.2785 | 2024-10-06 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| d5c892da-0bbc-3cc9-930a-83c58db72bf7 | -18.6391 | -57.2578 | 2024-10-06 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| c785396d-bff4-333a-b4e0-d679d5a219fd | -20.4508 | -51.2846 | 2024-10-06 07:17:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 6386f0a0-2946-3556-b0a2-a626f535ca20 | -20.4712 | -51.2806 | 2024-10-06 07:17:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.0 |
| 222ae985-c829-3e15-8503-406049dacfb2 | -13.3976 | -61.957 | 2024-10-06 07:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 72e243c8-03aa-3f67-800c-a81652d888b0 | -16.8238 | -57.4584 | 2024-10-06 07:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 25350f5f-50cb-3eed-a749-788e57b24cf8 | -17.0007 | -55.0607 | 2024-10-06 07:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b57db024-0907-36f5-8bdd-b22b91bf6fcc | -17.02 | -55.0791 | 2024-10-06 07:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8b400b2c-a778-369f-9398-061a55382663 | -17.0203 | -55.0581 | 2024-10-06 07:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 68f2b611-2d99-3399-85b4-62b635e1b4b2 | -17.0207 | -55.0371 | 2024-10-06 07:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| bb39148e-f8fd-3182-a835-40eb2e095cde | -17.0116 | -56.7186 | 2024-10-06 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| ee263a10-9b02-3abd-8035-33a8cfbeb9cb | -17.0985 | -57.4062 | 2024-10-06 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 6e7e5cf3-b198-36c5-a1f0-9b7641ee4254 | -17.0989 | -57.3857 | 2024-10-06 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 42037d03-2def-381d-b3ed-876ba8fe7d91 | -17.1182 | -57.4039 | 2024-10-06 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| d2c4059c-1dc8-33a2-adfa-30a7440d85eb | -17.1185 | -57.3834 | 2024-10-06 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| eef41163-791a-30c5-a864-5572626410f1 | -17.812 | -53.7859 | 2024-10-06 07:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ede70874-36f8-3a4d-a740-138d0fbcfbc2 | -18.6387 | -57.2785 | 2024-10-06 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 14931f31-3ba5-316b-a128-1d10b210bbfd | -18.6391 | -57.2578 | 2024-10-06 07:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 8b184137-af70-39c7-b809-7017a3746cc4 | -20.4508 | -51.2846 | 2024-10-06 07:27:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| 7c5c5f55-a40f-38bc-950e-40bb887ead70 | -7.48082 | -72.69097 | 2024-10-06 07:29:00 | AQUA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 112c0c39-64b0-34c4-8d9b-11f9a015d910 | -12.6726 | -54.0189 | 2024-10-06 07:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 49b698a1-12d0-3b08-9fb8-d7b5c20a6b5e | -12.6535 | -54.0208 | 2024-10-06 07:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 2aaaf281-bc37-3241-afb5-6df04ea6fd7c | -12.6532 | -54.0415 | 2024-10-06 07:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e10cf318-a0d8-3a10-98fd-824ee7a397b6 | -13.3786 | -61.9582 | 2024-10-06 07:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e5f5bc6e-5b82-33d8-bd3c-cba9c678f328 | -13.3976 | -61.957 | 2024-10-06 07:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7722e35d-c469-36c4-994e-92907c0677e5 | -16.3959 | -57.3641 | 2024-10-06 07:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 14a955f6-2e27-3d19-ba54-3099bd389ae4 | -16.3764 | -57.3663 | 2024-10-06 07:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 4b036ad9-76a0-3ebb-8008-e9f2a61f9f32 | -17.0116 | -56.7186 | 2024-10-06 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| afdbe838-3f22-3de3-b460-67191f28af09 | -17.0203 | -55.0581 | 2024-10-06 07:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ed498046-2210-3625-96e3-8e278d0dcbdc | -17.0007 | -55.0607 | 2024-10-06 07:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 207f81e1-19ee-311a-bd0c-ab6298203214 | -17.1182 | -57.4039 | 2024-10-06 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 53539808-304a-3314-8cb4-62417423c99f | -17.0989 | -57.3857 | 2024-10-06 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| ca8bca9d-a301-31b1-8016-25ea0377edf1 | -17.0985 | -57.4062 | 2024-10-06 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| dd3da523-d200-3f50-a7d4-628e0bcbe570 | -17.1185 | -57.3834 | 2024-10-06 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 53a2a471-04e2-3a34-8bb6-9806ca6256fe | -18.659 | -57.2552 | 2024-10-06 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 2ded4aad-450b-3507-854d-65103eeee755 | -18.6391 | -57.2578 | 2024-10-06 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 6e5803b7-b997-3bbf-b90b-68a00294ea0a | -18.6387 | -57.2785 | 2024-10-06 07:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 6b5345bf-27bb-3229-889c-7e4c7e584dfe | -12.6535 | -54.0208 | 2024-10-06 07:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| b0cb1813-5d20-31a9-b0a1-9ed9735ea8ab | -12.6532 | -54.0415 | 2024-10-06 07:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 71facd34-11ca-3606-8457-c4a34e3f9df8 | -12.6283 | -53.1108 | 2024-10-06 07:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b75d0d7e-e7c0-30ad-91b5-4683709d72ab | -12.6089 | -53.1338 | 2024-10-06 07:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 48e172d6-f207-389c-9980-9b2e2699c7bc | -12.6726 | -54.0189 | 2024-10-06 07:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 77991832-7d13-30b5-b8f4-564829845acf | -13.3786 | -61.9582 | 2024-10-06 07:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 707ad0bd-faba-356c-bc9f-c08bb1c38f4c | -16.3761 | -57.3867 | 2024-10-06 07:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |
| b5191fa1-a465-3230-8ca0-fdb7dc912085 | -16.3764 | -57.3663 | 2024-10-06 07:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 190.0 |
| 17327535-44a6-3d4c-bf66-febe0c0ecead | -16.3956 | -57.3845 | 2024-10-06 07:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 3d760a2b-7ce1-3447-b588-9965b93c3cb9 | -16.3959 | -57.3641 | 2024-10-06 07:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.2 |
| d23f2a1d-9e1e-3e70-86aa-4931bfc319a4 | -17.0007 | -55.0607 | 2024-10-06 07:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 11f9d883-4da9-3c73-8876-d0844e67806c | -17.02 | -55.0791 | 2024-10-06 07:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 6135531a-c4b0-34b3-b74c-74cf67807e29 | -17.0203 | -55.0581 | 2024-10-06 07:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 3023b208-a089-3192-a593-66afe10e105f | -17.0207 | -55.0371 | 2024-10-06 07:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 984547a3-1cf6-31fd-b2f8-b78872a63437 | -17.0116 | -56.7186 | 2024-10-06 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 9d328587-1461-3b07-a302-7f3fa297c320 | -17.1188 | -57.3628 | 2024-10-06 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| db0b1f2a-2528-3903-a4f4-1fd7d94133fb | -17.0985 | -57.4062 | 2024-10-06 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 854655bb-d721-3aa7-ba02-6185423eaa4f | -17.0989 | -57.3857 | 2024-10-06 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 637fd842-911a-30e6-b3e0-7f15ee214828 | -17.1182 | -57.4039 | 2024-10-06 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 79d6026b-5642-3d5c-bd41-1786e632e74f | -17.1185 | -57.3834 | 2024-10-06 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.4 |
| b19974aa-0c34-3d0b-9fc4-ea49ce8d1a5c | -18.659 | -57.2552 | 2024-10-06 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| f50bdc07-97fb-3e92-95f2-f6600ef71bec | -18.6586 | -57.2759 | 2024-10-06 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |


[Clique aqui para ver as próximas entradas](README157.md)
