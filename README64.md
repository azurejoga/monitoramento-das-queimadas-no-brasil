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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a163310d-d6b7-3779-8c4e-240859f4b63a | -18.31047 | -56.20746 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 125d2f96-65cc-339c-a037-6ef6775c2573 | -18.30884 | -56.21762 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 8cec18c6-befd-3647-871b-372919237fcd | -18.30122 | -56.20585 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 14eb2969-1a09-3fcb-aaac-118c64a11ac1 | -18.29959 | -56.21602 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 4a9096a3-c6c3-38be-8425-c55f535b6bf2 | -18.2709 | -56.04966 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f75200b6-6772-374f-a698-d4d93c997953 | -18.26932 | -56.05969 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 03c4b9a2-3f87-34b9-b967-a7dde39ad7cb | -18.26012 | -56.05811 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| ce242117-9539-3c6b-89f8-c7dbff68c759 | -18.25853 | -56.06815 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 6d9f093a-a2bc-34b9-9f5f-c41f54f2818e | -18.24932 | -56.06656 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c70929bf-0a33-3db7-b332-c110ffb4606e | -17.94177 | -57.21194 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 103d7bbd-1cd6-3c0c-b1d2-b72a65ed7865 | -17.00913 | -57.5048 | 2024-10-23 05:46:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 34368222-3ca0-3cb5-bdbf-7d3abd057115 | -17.02065 | -56.00282 | 2024-10-23 05:46:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 492f6539-a655-3f7e-9255-b6bce5a7b112 | -17.66561 | -57.44405 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 56d45dce-f961-394e-8677-89aced74b1aa | -17.67165 | -57.46964 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 0c87032f-0736-3b19-8d02-5d96437259e9 | -17.67361 | -57.45774 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| ec27a452-99e5-325b-a2aa-8858fbcc3fd8 | -17.67558 | -57.44585 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| f30f4589-87e3-3dce-b45d-0a2532577b5e | -17.68162 | -57.47145 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 390db263-21dc-37b9-bf88-763b0233323d | -17.68358 | -57.45954 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 8fb38e3d-e29e-31e6-ae7d-d77f88ceffff | -17.75139 | -57.55133 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 69e645a6-20ea-3508-8f31-e0be82e673bb | -17.76338 | -57.54113 | 2024-10-23 05:46:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| e3d0d862-f466-3732-b638-ee966e75de6e | -3.1101 | -54.1661 | 2024-10-23 05:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| b51d31dd-3077-3615-a82e-2e018c0344ba | -3.1102 | -54.146 | 2024-10-23 05:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 602cb3bd-b3f1-314a-aa49-4925368bbbbb | -17.0184 | -57.5178 | 2024-10-23 07:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 6a0f2676-9886-3012-9a01-e704eda77bd9 | -17.6868 | -57.4593 | 2024-10-23 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| c6c50fc3-b63c-3018-8788-2cc44cd9e0a7 | -19.5669 | -56.6744 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 43f5daa0-e907-3843-bca3-d409bd896ef9 | -19.6245 | -56.8129 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 165.2 |
| c7b9d37a-8b6e-3f45-b4aa-78f7c3c92da6 | -19.6249 | -56.7919 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.3 |
| 164fb3a6-6296-36ff-ba52-a03c089efc48 | -19.6253 | -56.7709 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| f7e3b3ae-8633-327d-aa44-98e633cf5283 | -19.6446 | -56.8101 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 23cd2562-9f33-37e7-a06a-9f874c6e9c1e | -19.645 | -56.7891 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 7b8b9380-cf6a-3723-ae53-b68c84d0b630 | -19.5473 | -56.6563 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.0 |
| 7302fd96-ffb1-3260-b1b6-90a49c856bec | -19.5469 | -56.6773 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 167.5 |
| f973eb59-31ac-3b7d-89c7-dd832922544c | -19.5465 | -56.6983 | 2024-10-23 07:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 022897fd-82f2-306e-a57f-aaf0fe80919c | -19.5272 | -56.6591 | 2024-10-23 07:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 7f9ffd8c-8bed-3ec8-98ec-c1a047b16fb5 | -19.5268 | -56.6801 | 2024-10-23 07:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 32543e03-4cd2-3161-8787-c3112f6d3868 | -17.0184 | -57.5178 | 2024-10-23 07:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| b148a9fc-a7ad-3e9f-95cc-dc1db2454843 | -17.6868 | -57.4593 | 2024-10-23 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 5d965cbd-e39e-3129-a6f2-db52eee97358 | -19.6245 | -56.8129 | 2024-10-23 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 154.8 |
| 7745a580-6f6e-3238-8080-73478bd9e3d4 | -19.6249 | -56.7919 | 2024-10-23 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| ee0e7563-8b0c-3023-8aa1-766350bcc8b8 | -19.6253 | -56.7709 | 2024-10-23 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 4bc7feb1-b7e2-3374-b265-0b2e2b1462aa | -19.6446 | -56.8101 | 2024-10-23 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| ef8a2ffb-dcc5-34a6-926f-8cfec08556e2 | -19.645 | -56.7891 | 2024-10-23 07:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| ab79bb08-658a-3510-b38e-2d983366e6ca | -17.0184 | -57.5178 | 2024-10-23 07:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| aa6252fe-0182-3ecb-811b-1253248266cf | -17.6868 | -57.4593 | 2024-10-23 07:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 2feac25c-dc1d-3f30-89eb-b578b7ed75be | -19.645 | -56.7891 | 2024-10-23 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 65dd52c9-f036-3d28-b8d1-0d6e95a1d2bf | -19.6245 | -56.8129 | 2024-10-23 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 172.2 |
| 29259f27-6e2b-3fac-9208-84bf8a60f45d | -19.6249 | -56.7919 | 2024-10-23 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 165.5 |
| 2ee14225-9620-3cbd-91a3-1ba099385443 | -19.6253 | -56.7709 | 2024-10-23 07:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 2e6527a3-ff20-3c68-9df1-ccdbe1129504 | -17.0184 | -57.5178 | 2024-10-23 07:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| fb09b3b3-cca8-3bc1-bade-ae4f8b4f7380 | -17.7637 | -57.5732 | 2024-10-23 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 3d38f592-2b13-3e5a-90dd-8d5014ff9e75 | -17.6868 | -57.4593 | 2024-10-23 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 77672170-6834-336b-9d2b-9678fc8c1e31 | -19.6253 | -56.7709 | 2024-10-23 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 7103be15-5d3e-3280-9ea3-07d80edff3a6 | -19.6249 | -56.7919 | 2024-10-23 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 176.7 |
| d8297934-9354-3425-8f56-3e3c52b34f1b | -19.6245 | -56.8129 | 2024-10-23 07:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 209.2 |
| 8dcfc546-9006-3678-8e0a-72adbc94f861 | -17.0188 | -57.4973 | 2024-10-23 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 77193a78-def4-36e1-80b4-955f1673b2fa | -17.0184 | -57.5178 | 2024-10-23 07:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 15991705-0fd9-3bfb-8fbf-d5e6710336f1 | -17.6868 | -57.4593 | 2024-10-23 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 9f175dac-c78e-3732-9ed6-d7eb90359bc1 | -19.5465 | -56.6983 | 2024-10-23 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 50.0 |
| cfd22226-5a81-3887-945d-ee89f7f4e99e | -19.6253 | -56.7709 | 2024-10-23 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 7bc941c0-886c-37da-b00e-52c5672fb9b2 | -19.6249 | -56.7919 | 2024-10-23 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 168.2 |
| 48f3aac5-59ba-3e6c-a2e1-37163d398125 | -19.6245 | -56.8129 | 2024-10-23 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 179.7 |
| cdda2721-28ef-302c-b97f-cc15c6818731 | -19.5473 | -56.6563 | 2024-10-23 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| fda6d7c3-70f0-31a0-92d4-59b48499e2f2 | -19.5469 | -56.6773 | 2024-10-23 07:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| a6e77512-2a71-3f04-9cf1-5b25e127c5fd | -17.0184 | -57.5178 | 2024-10-23 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| c4169d34-f3ce-3b3f-b86c-10c884fbf2b9 | -17.0188 | -57.4973 | 2024-10-23 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 3480622b-fcfd-3f7c-80f7-02ca7a5e44aa | -17.6868 | -57.4593 | 2024-10-23 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 6d0e6745-1ef6-3516-bda0-1bc84d5f8668 | -17.7637 | -57.5732 | 2024-10-23 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 93a5e82f-583a-3cfa-84e9-ff03a6f84782 | -19.6245 | -56.8129 | 2024-10-23 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 66b0c4a3-e19b-3bd3-999a-24a1c62ddf2b | -19.6249 | -56.7919 | 2024-10-23 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 159.9 |
| f4c17653-2eb0-3d4c-9168-f645e5a93174 | -19.6253 | -56.7709 | 2024-10-23 07:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 5c8112ca-392e-3036-9e5f-c7ac4488747f | -17.0184 | -57.5178 | 2024-10-23 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 3818637b-1693-3f15-b955-776cbe0c4a20 | -17.6868 | -57.4593 | 2024-10-23 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 51a01236-ac87-3400-988e-b1b09a480273 | -17.7637 | -57.5732 | 2024-10-23 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| ab898b86-8e72-31f8-9f2a-986f02a1849a | -17.0184 | -57.5178 | 2024-10-23 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| c3ef3c4f-3a2f-3fa3-ba67-658ac22ea76f | -17.6868 | -57.4593 | 2024-10-23 08:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 103eb128-c1bc-3600-bf94-18d52cc49dfc | -19.5268 | -56.6801 | 2024-10-23 08:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 59181b56-c6a8-3172-a5c6-6f052e03c71e | -19.5465 | -56.6983 | 2024-10-23 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| b4c2b347-0e65-3268-8c77-dbb3c3fc30fb | -19.5469 | -56.6773 | 2024-10-23 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| d9d4c054-353a-34cb-8edb-218fe6c05d97 | -19.5473 | -56.6563 | 2024-10-23 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 46.5 |
| a47caa11-8afa-3883-8660-82bda9f7f583 | -19.6044 | -56.8157 | 2024-10-23 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 2d34f435-2baa-3d00-ae67-0c1795a2fbb7 | -19.6245 | -56.8129 | 2024-10-23 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 8a08d4a3-f149-3a89-bd9b-6cadc0868bcb | -19.6249 | -56.7919 | 2024-10-23 08:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 49.5 |
| c04963d0-ca68-3b72-9c18-4e3b2ecbd210 | -17.0184 | -57.5178 | 2024-10-23 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 6a7b9f94-c98c-300a-a902-5e9e532290e0 | -17.6868 | -57.4593 | 2024-10-23 08:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 297975ee-8334-3ae7-ae0a-64ee777c40f9 | -19.6249 | -56.7919 | 2024-10-23 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 526a09e6-179c-3212-b871-7881458de37c | -19.5268 | -56.6801 | 2024-10-23 08:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| 1c35f034-85d8-3b53-8f0f-f506bcf9bb16 | -19.5272 | -56.6591 | 2024-10-23 08:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.8 |
| e148c309-7165-3457-955a-d895abeb9925 | -19.5465 | -56.6983 | 2024-10-23 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 98d4fb0b-a292-3cb1-9814-67b75bf0c3ec | -19.5469 | -56.6773 | 2024-10-23 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 154.5 |
| 8f170fe3-9aed-31d6-a790-70c995ac91ed | -19.6245 | -56.8129 | 2024-10-23 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 7e1edd16-b5ff-398c-b358-79c2b23b4e4b | -19.5473 | -56.6563 | 2024-10-23 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 4f7a605f-1fbe-34fc-9a54-a78524a7da4a | -19.5669 | -56.6744 | 2024-10-23 08:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 42e43a54-d424-3d98-b703-a0491870f59f | -17.0184 | -57.5178 | 2024-10-23 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 375bb87f-82d7-303d-a6be-9421eaf82796 | -17.6868 | -57.4593 | 2024-10-23 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| ac395957-98bb-3eae-a2f1-45e09c35ca20 | -19.6245 | -56.8129 | 2024-10-23 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.9 |
| 4d972821-b54c-3cfb-8f56-e9148c8f790b | -19.5669 | -56.6744 | 2024-10-23 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 253038cb-3cd9-347b-975d-b67ae72f6937 | -19.6249 | -56.7919 | 2024-10-23 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| ee3b0128-0911-328a-8b80-55880e517b8f | -19.5473 | -56.6563 | 2024-10-23 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 93ce4634-8882-385b-8d6b-98def5c590e5 | -19.5469 | -56.6773 | 2024-10-23 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 146.5 |
| 7f04317c-56bf-3dd9-9105-63d68090c259 | -19.5465 | -56.6983 | 2024-10-23 08:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 134.7 |


[Clique aqui para ver as próximas entradas](README65.md)
