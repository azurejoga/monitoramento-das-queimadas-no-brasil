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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 035633cc-401a-3d6e-915a-bea3953777e3 | -11.08968 | -60.64944 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca6b8e4d-e001-3abc-accb-d86abb324ac9 | -11.08913 | -60.65301 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7c83f9a-b0ea-34dd-963d-3718ebc5a592 | -11.08419 | -60.68497 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 706424c3-8a21-3cdf-87ef-dfb8720d3612 | -5.13331 | -60.36435 | 2024-10-08 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff2bacc3-b492-3aa5-b88b-73be754d000e | -7.89965 | -61.52176 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13297862-2a02-3ba7-b447-c7334652ed1d | -7.91569 | -61.54945 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76105732-6269-3946-af20-b45990abe4e9 | -7.89359 | -61.47417 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9857418-56a1-3198-9b6b-9602eee1bcdd | -9.28385 | -62.32388 | 2024-10-08 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 733cd8e6-384f-3cf1-b996-841f9cf92bec | -9.16555 | -61.57386 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c0cdf54-962c-31e2-b3e9-92f8aa4af450 | -9.16168 | -61.57681 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b995ef47-4415-389c-932d-884a4b9de8ec | -9.15948 | -61.5693 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 304c3d38-f567-348b-8ca0-179ec8415cfa | -9.12337 | -61.43156 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e278819-15b4-31bf-896c-7d10d713a9c0 | -9.12283 | -61.43498 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9581a719-0017-3936-9c75-932c281e83f7 | -9.12006 | -61.43103 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9afa00f6-a06c-39c0-8239-82511c8c224b | -9.11952 | -61.43446 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f7b5833-6778-35e2-8c00-2db895030ae9 | -9.11675 | -61.4305 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf2b1360-c03c-3e35-b9f6-ca6fae862892 | -9.09266 | -61.13068 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43110d42-7d5c-3d0c-ae69-2acf58966c77 | -9.00975 | -61.54917 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ec89e92-416d-3391-be00-de2954e38905 | -8.98601 | -61.44166 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efd51a1c-5f3a-3260-afad-0cf741aab306 | -8.98325 | -61.43765 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23f29b40-8212-3003-800f-891f702e2fa0 | -8.84187 | -61.49335 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 684c62f2-dcfc-37f3-9630-5f4fc8e92e5a | -8.22272 | -61.21934 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a49f075f-fb3d-3228-8a96-d2b1ebc1af9b | -8.21445 | -61.20734 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 489ccaf5-74b2-363c-994a-54bf7cf878db | -8.21093 | -61.20733 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a83094-29b6-3baf-b597-2320ec5f7385 | -8.0884 | -61.27297 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4bd6bb3-18d5-3196-ae98-2cb22f32277f | -9.26253 | -62.45662 | 2024-10-08 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd33548-c102-3c1d-a077-f0a4afa969d1 | -9.16279 | -61.56983 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc44a16f-5a8b-3043-b357-336b54598d8d | -9.16224 | -61.57332 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f362ceb4-dd2e-3bf9-a63c-a98daa84515f | -9.11621 | -61.43393 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33f85f2e-e6e2-3daa-b026-21cf3bc7a934 | -9.09156 | -61.13762 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a122234-cf27-3f2a-9e72-c9e9c8d6893b | -9.08935 | -61.13015 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cb6cd7e-bab3-3652-a4f5-01099b81ff22 | -9.0888 | -61.13363 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58b1220b-01a3-32d9-82e7-fbabb0eefb42 | -9.08219 | -61.13258 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ed81a23-3561-3f0c-9d89-4dcbc216c138 | -9.06711 | -61.40114 | 2024-10-08 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb8f79da-b88e-3149-a6e5-5f0abceac682 | -8.21776 | -61.20787 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d769d0e-33b6-3c43-81e7-718e1236aa3c | -8.215 | -61.20388 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5c18ef3-f759-3ba0-96e6-092846beb361 | -8.20763 | -61.20681 | 2024-10-08 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb715b57-19dd-3f91-99ed-3d3d289ffef0 | -10.00431 | -62.70636 | 2024-10-08 05:23:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7061b402-6e58-363f-8e63-38b2f02de880 | -10.00373 | -62.71 | 2024-10-08 05:23:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06986d47-66c3-3b16-a75c-712ec9ccd565 | -9.64579 | -62.42237 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaccc415-328f-3980-991b-ce8cd980433f | -9.47287 | -62.37296 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f58cac18-6797-3f70-a203-017880609006 | -9.4723 | -62.37654 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d221ad3-db9f-3bde-a2dd-db2c9f9350a0 | -9.74382 | -62.33952 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 955d0711-c842-3f39-972c-6d35cc29974e | -9.74104 | -62.33543 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eecefdb9-6260-3648-a2d1-3da70786ad15 | -9.74047 | -62.33899 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 91b12e75-1b80-3ffb-8d1c-2b425175130c | -10.20953 | -61.95395 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6af717d-73e8-33f8-aae3-6bd1928aeeb8 | -10.20621 | -61.95341 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88693468-936a-3d8e-8f59-99c604fd6068 | -10.20566 | -61.95691 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d24118c4-31d8-3a76-a9ab-c58a822366c0 | -10.2051 | -61.96041 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cd6abb6-2a3b-324e-90ee-ca91aa53647b | -10.20454 | -61.96391 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 927263a8-35f1-3bd5-b6e3-4065bdc62944 | -10.20234 | -61.95638 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f8a8dd2-ef6b-32f3-b89c-c15b0bda32d0 | -10.20179 | -61.95988 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a456a41-cf54-3234-a00b-35d159ead03d | -10.20123 | -61.96338 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e86641a3-ea4a-3729-bad3-fb73c6ec5d27 | -10.19791 | -61.96285 | 2024-10-08 05:23:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f261451-329e-377f-8ef6-634ae9c0f44d | -10.13941 | -62.11591 | 2024-10-08 05:23:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eecc88c-1697-379a-9e31-43d24186593a | -10.07647 | -62.50686 | 2024-10-08 05:23:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dcaf634-9efd-3a9f-b5d3-d56c75e5065f | -10.0542 | -62.4596 | 2024-10-08 05:23:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23a2a6e8-8a23-3f57-a0e7-40ce77e66e03 | -9.74438 | -62.33596 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27cd8754-48e8-390d-bf74-76ac1579a19f | -9.64914 | -62.42292 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e1d8115-c25a-3506-a575-0a60aa33d3ca | -9.64636 | -62.4188 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6dd7724-fe35-3ef2-b949-d613b9511a89 | -9.59924 | -62.19901 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a29e3a4-ce2b-3b6f-a5a3-32f043e0b402 | -9.53313 | -62.38279 | 2024-10-08 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c779541a-7604-3906-a36b-91d83a832f6f | -9.53064 | -62.51787 | 2024-10-08 05:23:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1f95a08-fee3-3390-8f5d-21b4dccde49e | -10.65309 | -61.74945 | 2024-10-08 05:23:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b99f2d4-226a-3c16-a527-7f1fa32dfc47 | -11.88663 | -62.76947 | 2024-10-08 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2a20f75-7011-38f5-a5b9-900084e6bf3e | -11.88605 | -62.77306 | 2024-10-08 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c785962-4888-3c46-81f1-ae7bfb4826c3 | -11.77319 | -62.88363 | 2024-10-08 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d40b12-976a-3e0b-aacd-9df8c8c36e0e | -11.76984 | -62.88306 | 2024-10-08 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 066f0d30-9fc7-3947-98c9-b2923c1b7be2 | -11.76649 | -62.88252 | 2024-10-08 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63a4519c-99ea-32fa-a6ef-d401dd42c7ff | -11.67431 | -62.80066 | 2024-10-08 05:23:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0f508329-6d15-3c95-905a-c2f1b93759c1 | -11.48335 | -61.97719 | 2024-10-08 05:23:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee88b746-cb1b-3f46-b56a-576938805579 | -11.48279 | -61.9807 | 2024-10-08 05:23:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee63d081-6658-3d7a-86de-c699be2238a7 | -9.25268 | -63.65727 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3aca9f1-9a51-31b3-accc-efc807a7ad87 | -8.67205 | -63.48112 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be1bc86a-1722-3234-9725-968ec9612bd2 | -8.67141 | -63.48502 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a88b301-6bb9-30f2-948f-072a0b35a9e9 | -8.66856 | -63.48053 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 484a3bda-3d92-343f-81ac-1bc0c6c4e855 | -8.66792 | -63.48444 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de8ce596-042c-317e-a6aa-c80a638d8da4 | -8.22689 | -64.00459 | 2024-10-08 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 721adf05-6305-3af8-bee6-c36510ab8073 | -9.42045 | -63.25642 | 2024-10-08 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb4da964-fc3b-35f9-9c60-f6a08e0bc56b | -9.03083 | -63.23734 | 2024-10-08 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ea6b09a-e9d8-341b-9dd5-297ee60b0afd | -8.77473 | -63.08826 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3642fe7-348a-33ce-b8ff-f38e66759fd8 | -8.64962 | -63.14573 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7327aeea-27b7-36ba-bc80-6d11b8992fc6 | -8.61764 | -63.12486 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfd28af1-26b5-3403-b06a-99c3990d469b | -8.61445 | -63.10098 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9454443-2744-34e4-9dd1-0482b2c6e71c | -8.6142 | -63.12428 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cecc544c-0ff7-3a6a-b489-9a5b3aa24090 | -8.61101 | -63.10042 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25cd24e6-15e4-3151-b342-a176ea597b6b | -8.60757 | -63.09986 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8c12d40-3305-326f-9c50-a4bced00ae8c | -8.60413 | -63.09929 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08fd9aa-2c22-346e-82bc-588890df8186 | -8.58005 | -63.09532 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcd12a5a-10dc-3435-9366-43b8885755be | -8.57661 | -63.09475 | 2024-10-08 05:23:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac19c067-40eb-3857-90b9-573a3330274f | -9.66641 | -63.12666 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28473e0e-115f-3593-a821-9294792d651d | -9.66299 | -63.12609 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce17fa3-a06c-3c63-bd1b-22a56ab6fea0 | -10.44829 | -63.13124 | 2024-10-08 05:23:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77144520-feb5-35ca-a9bb-dc91ef699ab0 | -10.64036 | -64.53606 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03d102fe-9f5d-3abd-8486-093747f4c151 | -10.63677 | -64.53544 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ae6cdee-6d1d-3250-b96d-5322db8a5c8e | -10.61884 | -64.43082 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42b5c557-3779-3e8e-9687-41dfc21bed7f | -10.61528 | -64.43017 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e75d689-9e3a-3cc8-b1de-e5c0e265451a | -10.59739 | -64.51653 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64c8dac5-cb8c-3d82-bbf5-e5edfcd77784 | -10.59674 | -64.52046 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d981e7-e314-3ec2-a980-8d26af2dfef9 | -10.58596 | -64.40791 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README125.md)
