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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2878fd6-a87b-345e-bf7a-90dd43a7ff3a | -2.25399 | -53.74384 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c8a51d8a-6001-309f-af97-d7cfbbb4f8f9 | -2.70558 | -53.18076 | 2024-11-27 06:01:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07095791-8745-3bbf-a993-328d941b79a6 | -2.25253 | -53.62516 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 736654cc-f2a2-3930-893a-2aef6ad5ba54 | -3.31414 | -53.74854 | 2024-11-27 06:01:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0c55dea8-6cee-3ab8-9055-8073ff8ccb3c | -3.05104 | -48.515 | 2024-11-27 06:01:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 47eef164-912e-397d-8558-934c98d776c1 | -2.93762 | -54.79451 | 2024-11-27 06:01:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ae6f7858-c924-39de-b51e-7460f78b5ff6 | -2.6083 | -53.96894 | 2024-11-27 06:01:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 63f07157-5153-3491-9243-6d4eb0345f0f | -2.8347 | -54.1125 | 2024-11-27 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4ea63934-52b0-3054-aa2a-939e80d25d90 | -3.6973 | -50.2277 | 2024-11-27 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bba1d13f-a669-3066-a039-59c4ef3b951f | -3.0949 | -53.2588 | 2024-11-27 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 26339c7b-46ef-35f2-9dc3-ed1ad1563bc3 | -4.2114 | -50.899 | 2024-11-27 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 17dbfa42-3ea0-3de8-9019-89a69bdbc9d9 | -3.1133 | -53.2583 | 2024-11-27 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| cd8a8a6a-6d30-3f47-87d6-0d82ba834c9f | -3.9674 | -48.0851 | 2024-11-27 06:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| bc5d206d-86fc-3345-9812-b807cd7cff7d | -2.8346 | -54.1326 | 2024-11-27 06:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| daa96e61-aa80-379e-81dd-4337950f9837 | -5.9975 | -45.3607 | 2024-11-27 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 322fcc78-1ce3-355e-acdd-2723ae1cc659 | -3.1691 | -48.4394 | 2024-11-27 06:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 61aace4b-2a96-3718-a2d4-ca6e260b45a1 | -5.9788 | -45.3621 | 2024-11-27 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3e848234-f4d9-36a6-96c9-49c301e63a33 | -3.6043 | -50.3571 | 2024-11-27 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 78b30585-1cf9-32a3-90a7-8b5a2e52c80b | -3.0949 | -53.2385 | 2024-11-27 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 909cd2ce-df42-3abb-be38-87a7c6731911 | -4.2299 | -50.8983 | 2024-11-27 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| afbad5c5-b370-33b4-8a04-d22ceeeb3cd8 | -2.961 | -45.1672 | 2024-11-27 06:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 6e52ea19-ce8f-31ad-91f2-57c0175d1df2 | -3.1691 | -48.4394 | 2024-11-27 06:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f5530938-1ee7-3d5b-8d3b-c85a2db4aeaf | -2.8347 | -54.1125 | 2024-11-27 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a47c192d-dc5c-3f37-a3bf-342b28463ff5 | -2.8346 | -54.1326 | 2024-11-27 06:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 31bfc9ff-aead-3104-96c9-d699abcd9fc4 | -5.9975 | -45.3607 | 2024-11-27 06:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 8cbc1265-df4b-3e25-bbc7-08abb86ebcb9 | -4.2299 | -50.8983 | 2024-11-27 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 24dd05f4-e852-3e0b-ad80-95e346bd953c | -4.2115 | -50.8782 | 2024-11-27 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 63f02723-337e-3f10-8f62-01d4cd2faac1 | -4.23 | -50.8774 | 2024-11-27 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| bbf96e46-53ed-3023-bd77-854112d0e9c0 | -3.1133 | -53.2583 | 2024-11-27 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 23d8f952-a6e5-35a2-8630-5e5ecff2fb81 | -4.2114 | -50.899 | 2024-11-27 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| b1b1ce9d-7a91-370f-9de5-b816eb749fdf | -3.6043 | -50.3571 | 2024-11-27 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 5cde395f-cf0b-346e-9f39-127f9bc0c0fb | -2.9424 | -45.1679 | 2024-11-27 06:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| eeb91843-df84-31b2-aa1c-4841cae05b7a | -3.0949 | -53.2385 | 2024-11-27 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b41b2c10-8cbf-3b59-afb9-e48075ec3942 | -3.0949 | -53.2588 | 2024-11-27 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 0cc1354c-888d-3970-a8fd-a58f277074f5 | -5.9788 | -45.3621 | 2024-11-27 06:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7e799750-c933-367e-8be8-b64bb3088840 | -2.9424 | -45.1679 | 2024-11-27 06:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a1923931-c45f-3df9-a69d-95dcc4f64f26 | -4.2299 | -50.8983 | 2024-11-27 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 9f6170fa-4213-3332-867a-959d93312c44 | -5.9975 | -45.3607 | 2024-11-27 06:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 3981cafb-28b0-35a0-a7d7-dddfc55e6748 | -3.0949 | -53.2588 | 2024-11-27 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 88574381-0d1a-377d-9d27-ffe5ac73df73 | -2.9611 | -45.1446 | 2024-11-27 06:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 749844c6-fbb8-37a8-b559-7d175c96b73d | -3.2208 | -45.27 | 2024-11-27 06:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4ae5e010-e857-3341-8c89-585b4bdf7687 | -4.23 | -50.8774 | 2024-11-27 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| c627ac8e-c81c-3590-be49-414dc02c172c | -3.2022 | -45.2707 | 2024-11-27 06:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 81817154-22f1-3fb8-9f93-c2147fca5dd8 | -4.2114 | -50.899 | 2024-11-27 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| cc467f61-ff87-3145-b95b-47ce99c8980c | -3.6043 | -50.3571 | 2024-11-27 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 088fadc9-7486-30a3-b245-326defd77d50 | -2.961 | -45.1672 | 2024-11-27 06:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 4910add4-1b8f-344e-9626-4318a6ec3f21 | -3.1133 | -53.2583 | 2024-11-27 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| cb3050f9-b989-3868-8bbb-371ca6f150ac | -2.8346 | -54.1326 | 2024-11-27 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| b7217565-70e0-3346-9bc8-cbc311870e61 | -4.2115 | -50.8782 | 2024-11-27 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 95983d2f-f21a-38ac-9573-68ea589e9275 | -5.9788 | -45.3621 | 2024-11-27 06:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ebb6a151-d8a3-3fe9-9d19-a2c5789eced3 | -3.1691 | -48.4394 | 2024-11-27 06:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9980063d-0af4-307e-ac30-2d21072edfed | -2.8347 | -54.1125 | 2024-11-27 06:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 541a9c81-e613-3501-81b2-011bfd5a32bc | -4.2114 | -50.899 | 2024-11-27 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 6600f923-25d0-3926-9618-74d78ff74a09 | -3.6973 | -50.2277 | 2024-11-27 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a46f72ec-0dd1-388f-a594-88b790c8af5b | -6.5631 | -51.1126 | 2024-11-27 06:40:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 317e9e2c-f825-3472-baf7-d8b445510d59 | -4.2115 | -50.8782 | 2024-11-27 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| e59075df-45d1-3b8a-bc26-8483ae87e425 | -5.9788 | -45.3621 | 2024-11-27 06:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9a9db331-70ea-36ae-8b7d-52d346033b86 | -4.23 | -50.8774 | 2024-11-27 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 095ad0ed-253a-35ad-b227-018e3749a320 | -3.0949 | -53.2588 | 2024-11-27 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| a0d5d3a6-c182-3b82-b6cc-98b5c79c6791 | -3.1133 | -53.2583 | 2024-11-27 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ad9155bf-ca7a-3da1-a15c-f991ae9a0acf | -3.6043 | -50.3571 | 2024-11-27 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 4a1abaaf-2277-3724-9ad1-0ae21f4c2b9e | -3.1691 | -48.4394 | 2024-11-27 06:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e8d6520f-4ab8-3244-adc9-0bc8e4c02d33 | -4.2299 | -50.8983 | 2024-11-27 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 8ffeda57-0723-3639-8073-e57145d96605 | -2.8347 | -54.1125 | 2024-11-27 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 3c2f4bea-c750-39f8-8d04-0203c537952c | -3.6043 | -50.3571 | 2024-11-27 06:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c61e192c-48f1-305e-821b-51dd5ca36652 | -4.2115 | -50.8782 | 2024-11-27 06:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 56c5e223-7560-3480-9d54-16a1a48d25c7 | -4.2114 | -50.899 | 2024-11-27 06:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| e569b40e-67ac-3db4-9c96-820911876aba | -3.1691 | -48.4394 | 2024-11-27 06:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5e9279d4-9b1f-3ed8-9ab2-ddb8478d817e | -5.9975 | -45.3607 | 2024-11-27 06:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 9d164d16-9ed3-3759-a784-117d97a0a5bb | -2.8347 | -54.1125 | 2024-11-27 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 22f22743-95e2-3568-affd-a9863a60eaaf | -4.23 | -50.8774 | 2024-11-27 06:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 013d2112-b1a8-33e9-9fee-e47e19634a49 | -4.2299 | -50.8983 | 2024-11-27 06:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 1b944653-ed72-3d3c-9036-4e297ab3a880 | -3.1133 | -53.2583 | 2024-11-27 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1575d66f-ba8a-39fa-8cb0-3fdb15d4a140 | -2.8346 | -54.1326 | 2024-11-27 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| a96bee82-fab0-3a5f-8b0b-b4383445a0cf | -3.0949 | -53.2385 | 2024-11-27 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 38f28aad-5ac3-36b8-94f2-29d0fddaed6e | -3.6973 | -50.2277 | 2024-11-27 06:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| aaccc407-5b3e-3237-8f0b-793810d0b797 | -5.9788 | -45.3621 | 2024-11-27 06:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b5de3962-c65c-3777-bb77-34bf2bff49e9 | -3.0949 | -53.2588 | 2024-11-27 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 5e42cb15-720f-3044-a3cc-533f9526dd50 | -3.6973 | -50.2277 | 2024-11-27 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6da09f8a-eb68-35b0-8f70-a185dd0e9f83 | -3.0949 | -53.2588 | 2024-11-27 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fc312b08-3e69-311f-9c10-a47aca05a7f0 | -2.8347 | -54.1125 | 2024-11-27 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 03756121-9937-3eb3-be3c-eacd3d90f45e | -3.1133 | -53.2583 | 2024-11-27 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 79314e37-2e4e-304b-a1ed-e8cc7eb39d4e | -3.1691 | -48.4394 | 2024-11-27 07:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7da12bca-5649-3b67-82d2-27b412534b8a | -4.23 | -50.8774 | 2024-11-27 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 263.1 |
| 1874a0c6-f5c5-359a-a9bb-f31104ab9075 | -4.2299 | -50.8983 | 2024-11-27 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 265.5 |
| 5c5a434c-3bb4-3c0c-bd99-2dcb2b13fc46 | -2.8346 | -54.1326 | 2024-11-27 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| d9f22774-6b1a-3ce2-a17c-ae6a56da8dae | -4.2115 | -50.8782 | 2024-11-27 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 3ed11f21-5b71-32d6-8dea-26f7f7ee9407 | -3.6043 | -50.3571 | 2024-11-27 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2e7dc29d-d329-3643-8ab8-4f33c243aabf | -4.2114 | -50.899 | 2024-11-27 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 07f01d8e-23ca-3bd2-9a91-788449ef7667 | -3.5858 | -50.3577 | 2024-11-27 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2c91df75-65b1-3e8e-9301-356618049fb1 | -4.23 | -50.91 | 2024-11-27 07:00:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e37d713c-94cd-31e2-9a6d-4d70cade95fe | -4.23 | -50.86 | 2024-11-27 07:00:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 881c264f-a2d6-3b59-9810-079a36f46705 | -3.0949 | -53.2385 | 2024-11-27 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 0ac48833-4338-3943-b861-93149080f28f | -3.6043 | -50.3571 | 2024-11-27 07:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9a1d76d9-b1cf-3916-ad58-a2ed07f4e08d | -4.2115 | -50.8782 | 2024-11-27 07:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 11fed046-44cf-316b-9ab0-9c6ec07c131f | -2.5956 | -54.2181 | 2024-11-27 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 96bff96c-61dc-36b7-8ef3-295438be7e4e | -2.8347 | -54.1125 | 2024-11-27 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 32f176b8-6556-34dc-b8c3-2bd5b4e17966 | -3.1133 | -53.2583 | 2024-11-27 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0a653b29-0c24-3da3-9e47-18e88efa728d | -2.7798 | -54.0334 | 2024-11-27 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 617dedb5-8704-3b36-83a3-ade64e671ccb | -3.0949 | -53.2588 | 2024-11-27 07:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |


[Clique aqui para ver as próximas entradas](README82.md)
