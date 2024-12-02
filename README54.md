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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a6f656-5ca4-3631-af01-0ea99d6cbd9a | -2.08436 | -48.5438 | 2024-12-02 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3556a8f1-ebeb-39c1-b8be-784c3f53da4c | -2.90781 | -54.11598 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d97a478-ffbc-3fd8-a024-ffa4e93a3fc3 | 1.10933 | -56.01846 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 65ff404e-abfa-3d46-8c98-e5c856d76f36 | -2.49497 | -47.27005 | 2024-12-02 04:48:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3355b483-5104-371a-8e02-60af3719b494 | -3.09558 | -54.01097 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 963daa60-9057-32ef-bf95-800fc01c7dec | -3.48089 | -50.25394 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36dea965-6bc4-3474-952f-153d333529fc | -2.69318 | -51.87891 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a43224a-0f84-3047-8508-74b597b753b9 | -3.47089 | -52.24776 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ba1dea4-e11e-35b7-a4c9-899ea8544d19 | -0.31393 | -51.77754 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4bd0148-a444-3928-aff8-785ff0c0a50e | -2.11929 | -50.33845 | 2024-12-02 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83a5b56c-f915-393f-9eec-e3cf186199ba | -4.03342 | -51.02337 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ad4329e-8966-3063-b880-fc7a8555df28 | -3.02096 | -54.01949 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ecabed9-a246-3f6a-b5c9-77a979593d82 | -2.59022 | -54.22237 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b5ecde4-e918-3961-9e63-039783e66913 | -1.96128 | -48.38849 | 2024-12-02 04:48:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db1c39d8-9947-3fdf-bc17-328e3cc8f6f0 | -3.02722 | -54.19229 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6977004-663a-3e9b-be55-3bb86c7305e7 | -1.34787 | -51.38277 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d89d4e33-fafe-3f1c-93ce-0c2aa73c61e8 | -3.52526 | -52.16094 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e7071d-0cd9-3e31-8e32-a85bef34a120 | -3.50237 | -53.83532 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f9e2607-b4fc-3fa3-9bc3-4e5446ad1a2e | -2.95834 | -50.57653 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cf3cd4b-1907-374c-932d-e5b4962b8ec9 | -3.17479 | -53.84611 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 358b75fd-3754-3507-82be-491f8030b155 | -1.5709 | -51.19644 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b44ea34-88e7-3fc2-8095-2426485dbeb3 | -0.59641 | -51.68749 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac7f6b18-1f24-3911-9e3e-064d85ace924 | -3.03498 | -50.97871 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4dfd531-b7c4-3aae-a31e-623086680b44 | -2.81983 | -54.07492 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9321a8ca-6fd4-3673-8b2e-f4b5ed0c780e | -3.7255 | -49.94153 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba783589-99db-3f79-8b8b-60c7d6f5d40a | -0.63475 | -53.44035 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24bd05d8-2c1c-39cf-b2a8-b043f897e1c5 | -2.4561 | -52.21915 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c180c686-8853-3db6-9d59-09f844a7fa6f | -3.03754 | -54.04945 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0a30ed4-22a1-3b89-8bcb-d627a0e24237 | -1.28976 | -51.64446 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06d4d3b8-b766-3eda-b583-4dffbedfb286 | -3.13352 | -48.52753 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57fea0f5-6bd9-3e84-9bba-910b0b33ea5c | -4.09762 | -50.72251 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64d4aa3e-67a2-33cb-83da-ce12ef542be5 | -4.27903 | -50.68792 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53cf8547-7396-3738-976b-32d7f800e781 | -1.53322 | -45.84552 | 2024-12-02 04:48:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8bfc5f2-217a-34d3-8cee-dcb6530528d9 | 1.10469 | -56.01545 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 10acecdb-c014-3dd9-81d3-e177bedf7753 | -1.29501 | -51.37125 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09e71a3a-72fa-3340-94f2-1d1a885dd6aa | -3.11997 | -53.99146 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f228b964-0ad3-3bc7-9ed2-de2999b7f3a9 | -3.17912 | -53.64131 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18072cc6-8b5a-32b7-83ee-8a48981e1135 | -0.20513 | -51.54154 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fb4d1b9-6633-3069-9967-692e0a92e37b | -3.81621 | -52.08387 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df14dc89-2c0e-3eab-a948-0a27234138a4 | 1.14328 | -55.96901 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd039345-9a97-311d-818a-51ea0fb73fdf | -4.63261 | -45.45024 | 2024-12-02 04:48:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95b75ad5-f8b5-3d27-998a-ebd398fb8055 | -1.64742 | -53.8192 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24eea84f-0020-3ca3-9dc6-ad328f0c7b5c | -3.11713 | -53.81007 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c17e751-0e88-30f6-9d28-12e8092a4aa6 | -1.39555 | -53.65552 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 906090fa-a855-31a2-9394-60df53f3a1a8 | -2.64716 | -46.77582 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aa661d1-e3f3-379f-8048-f7b3cdde20b6 | -1.58836 | -52.25047 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae2bbdb9-ed25-3572-93c8-e60bca6e2b49 | -3.04267 | -54.062 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67405fe7-54f4-3135-adb9-e415acebb9ad | -1.2566 | -55.90047 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32e3ddab-00eb-3148-910c-429ef5f351f9 | -2.84233 | -54.03497 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34688e38-b186-325c-8f1a-658a395aec59 | -2.97342 | -53.89565 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c78c5246-186a-3dba-a4ba-f8570249287c | -1.23795 | -51.60492 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6757777e-68e2-3e00-83fc-ce84d5134d77 | -3.21839 | -53.63613 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a70eff56-d21e-3b93-a608-4b730f88719a | -2.38973 | -53.88871 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d60cff4-d8a9-3298-b45a-c7071401d363 | -4.91361 | -41.33642 | 2024-12-02 04:48:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7b731927-ffe6-3d15-ad2f-14c63223906c | -3.24699 | -50.77206 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fc4170d-825d-3aeb-828a-10caee4fd3dc | -3.48529 | -46.08635 | 2024-12-02 04:48:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ede1191-84da-3e50-abd4-cbd571d3c318 | -1.38721 | -53.55812 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad8cae29-3197-3af5-b80d-4e1d14b36ab6 | 1.14035 | -55.97681 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff6263c1-d743-34d0-8df4-22774d13cef6 | -3.62671 | -49.85462 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2ab73b6-1439-31bc-a811-5bce496d09ab | -3.84579 | -52.02506 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e0ede1d-b55a-3715-9868-ac4523cd0c78 | -2.04965 | -51.1972 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd4849ec-8095-3e8e-8bf8-eae7b5dc10bb | -3.30277 | -46.40788 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a66d310a-e91e-38d5-824b-2e4fec7e848a | -3.02321 | -54.02766 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 666c9f04-f2f8-36a1-9c90-e7d2da4b547b | -1.58763 | -51.26236 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a71c69a-8070-35b0-95bb-0870bed0f39f | -1.50375 | -51.1469 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40f66865-aa4f-3d55-bc56-f9797015cecb | -3.06055 | -54.05214 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d281a1ff-476a-390f-abc0-e22211056022 | -3.72531 | -51.08245 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7548243-ace3-3915-bd83-562a5ad390cd | -3.4548 | -51.42057 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 454c9f4b-bc90-3526-8ee8-123c966b8d0b | -3.13137 | -54.18922 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a929ea-e508-33f6-b475-b8be2f3e9bf0 | -1.0868 | -53.63576 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e011e2f2-d3aa-3b2d-a6f0-8d71c240a613 | -2.69023 | -48.86155 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99dfc48e-85cd-3d4f-a09f-e1c62233c018 | -2.53151 | -53.98352 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 782a3fa6-70a3-35aa-98ad-94d256988d4f | -3.49044 | -53.82195 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc917b53-b1b9-313f-84e2-edd53a40e33e | -2.19689 | -48.34137 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec149726-44fb-3a94-9e59-54d3eb4d398d | -3.09782 | -54.01911 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92f59f0c-bdf3-37e1-9e7a-2e9a52f894f9 | -2.22397 | -53.23178 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65e4d50f-1d4f-3f85-9a62-b4bbf7aca9c3 | -3.07292 | -54.53772 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28cb8561-2ae0-3381-b023-45b53505d4db | -3.10865 | -54.04025 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22c1701a-e81c-3043-8f9a-1a82b054d1b9 | -1.68318 | -52.50843 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb758594-4beb-3286-86c7-88144448eda5 | -3.92779 | -50.98158 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27ae2963-9775-36a6-bb4e-d2ecee037edb | -3.7629 | -51.34119 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fba2de57-476a-3c82-8d6a-d9540aa692b3 | -3.46172 | -50.26577 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 969ad902-2402-35e6-aea5-89acfae136c9 | -2.79771 | -51.90613 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 889f36be-82d0-3448-a9e9-f486ebca2409 | -1.57151 | -51.21413 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec90e9d6-1da7-3f03-925e-5dbcb83c7d1d | -2.76394 | -54.023 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8921d13e-18ae-3fb5-97d4-bd3676a7cc50 | -2.33734 | -53.92738 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5af2c4cb-a8a5-3c23-9791-13ebd889c611 | -2.82553 | -51.81543 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49c8079a-3ffa-3102-97da-d7defdb46f07 | -3.11152 | -54.04456 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80e4221f-e175-336b-b67e-d48a441d2219 | -2.45696 | -53.70538 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd42f83e-0c2d-3891-94fa-5f0f5ba20429 | -3.02442 | -54.02005 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26dd21f8-287c-3269-810a-a4d2066923fc | -2.57741 | -54.21234 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f34db0-7772-3617-b08f-80da9e16847e | -2.41444 | -54.01382 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 623548df-bf60-3e1e-b96f-253641567432 | 2.42538 | -60.65169 | 2024-12-02 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d73019-9a13-36e3-86ae-a48ff9e3132e | -2.88825 | -54.0148 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d025edd2-4e80-3d09-9436-b8074fbb0c4f | 1.0061 | -59.46925 | 2024-12-02 04:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62316115-27be-35df-90a5-eaf20d7a3e2d | -3.34364 | -51.6537 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7895ff2-4f5f-36de-9034-251060998148 | -3.22181 | -53.63663 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b43ca3f9-f492-37f8-adff-08fd07a5c025 | -2.09006 | -46.31606 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba5434ae-a35d-347e-ad2d-cac95ebe9e2c | -1.35106 | -55.17007 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0088f027-0aa0-33c3-92a3-5c0a811eb245 | -1.65346 | -52.24673 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README55.md)
