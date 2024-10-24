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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4785d5ae-b3de-3dd8-ada7-e73c06cb042a | -2.57925 | -54.01818 | 2024-10-24 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 87e1f54d-145b-3422-96f4-95a20335919f | -2.56953 | -54.01956 | 2024-10-24 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 22aa033f-8b77-3e24-856f-322f5fee647a | -2.49501 | -54.14498 | 2024-10-24 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 09f67f75-8cfe-3fcb-b4ad-9934f4012987 | -2.49353 | -54.13435 | 2024-10-24 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 05aab4f0-e454-3010-b98f-5eef2d1e4789 | -2.48551 | -55.72635 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c911125b-4bae-333a-bd2f-6927fb54d981 | -2.48422 | -55.71721 | 2024-10-24 01:26:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fe018932-dfa4-3a58-80c0-62a43bdb4015 | -2.25148 | -56.81683 | 2024-10-24 01:26:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 282dc23e-6bde-3c44-ae13-f434d774102f | -2.21659 | -51.67261 | 2024-10-24 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c2ef1d21-c45b-3847-ad1e-e997f490e15c | -2.10747 | -56.5895 | 2024-10-24 01:26:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0ca8c5e0-fca9-3d20-8f91-07f19cc398e8 | -1.4971 | -54.18059 | 2024-10-24 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 2d1a9da2-01d9-3da2-9995-3219fe1e7c80 | -1.7256 | -55.76215 | 2024-10-24 01:26:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 13febe82-9508-3f87-9357-5ed998aa4f43 | -1.60018 | -53.31036 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 7191bdcd-5512-3e8e-927a-4d5538785480 | -1.58984 | -53.31185 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 111df300-a0e8-388f-90d6-036a2f52e6f0 | -1.5881 | -53.2997 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4975fbe4-015d-3bf5-8b64-d6254e6bcd06 | -1.57949 | -53.31331 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 03b69435-c00d-387e-a633-cbcc1a0ace94 | -1.54161 | -55.89978 | 2024-10-24 01:26:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a35a9847-622d-3143-a010-5071068c425c | -1.51898 | -51.9353 | 2024-10-24 01:26:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9bd7ec3-d4e5-3c99-8e5b-d33df7bfdd67 | -1.49859 | -54.19138 | 2024-10-24 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 1342631e-bc19-3b09-8552-c3c76a9ca5e1 | -1.48884 | -54.19277 | 2024-10-24 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 434605a5-7707-3046-bb1c-20df1ff0da10 | -1.48734 | -54.18192 | 2024-10-24 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8afed7f9-7f64-3df3-aa62-659d95f54c57 | -1.16735 | -53.50409 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 888dc8ed-ffd2-3aa5-8d86-a378c848f265 | -1.07821 | -53.6701 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 963475e7-85db-327a-9787-54beb17c4693 | -1.06806 | -53.67163 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6f0d28ef-7d22-3614-af99-7598d302a1c1 | -1.06638 | -53.6599 | 2024-10-24 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f33e66dd-9d17-3cb3-94a8-923fed3761cc | -10.1969 | -53.8822 | 2024-10-24 01:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6219d3aa-fbac-3d71-868d-70de9fdc02c6 | -10.1971 | -53.8617 | 2024-10-24 01:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 77853c73-4daf-3e05-b5ba-0e4d14a4478a | -12.6914 | -43.8484 | 2024-10-24 01:26:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 206130a4-4c9f-39a7-911a-d72639db11e5 | -12.6918 | -43.8247 | 2024-10-24 01:26:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b68b79fe-680a-3395-a013-d4506bd259e1 | -13.7417 | -54.0682 | 2024-10-24 01:26:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 81b9ada8-5260-3905-8bb0-a479aec10937 | -13.742 | -54.0475 | 2024-10-24 01:26:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 4dbb8677-ca83-3bbf-856d-daf7fcb7c53b | -13.7609 | -54.0661 | 2024-10-24 01:26:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| dd5d634b-2af3-35ae-9efc-778b56897190 | -13.7612 | -54.0453 | 2024-10-24 01:26:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| d2db2371-76cb-3c72-9099-9106781de2c1 | -14.9145 | -45.1224 | 2024-10-24 01:26:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1741ab6d-d0a4-391d-98e9-bd128857c99d | -16.9596 | -57.5245 | 2024-10-24 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 21d054d2-48dd-30ee-b1d5-94239de4705f | -17.2383 | -57.2462 | 2024-10-24 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 060d92f9-f254-352a-a3c0-03792139e1b5 | -17.7062 | -57.4774 | 2024-10-24 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 3f40741c-e6fd-3b55-a176-d9e7a418d9a2 | -17.7637 | -57.5732 | 2024-10-24 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| e0a09e46-45e7-3981-be4d-86d38025b07c | -17.765 | -57.4909 | 2024-10-24 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 729194fc-7e95-3a27-b9d2-7fe57e73027a | -17.7831 | -57.5914 | 2024-10-24 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 9672f8ae-dc89-35c6-bb58-cf5edb4597f3 | -17.7834 | -57.5708 | 2024-10-24 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 0cf35d16-e497-360c-af2d-3073fb373609 | -17.7841 | -57.5296 | 2024-10-24 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| dc490574-1456-3875-9d32-85b9fda70baf | -17.7844 | -57.5091 | 2024-10-24 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| f3b5dcdc-16ea-37c7-98fb-7725c9580e99 | -18.0639 | -57.3101 | 2024-10-24 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| a8e220bd-46f6-31a9-b33f-c9721fc1e8fa | -18.0834 | -57.3283 | 2024-10-24 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| dfb1e645-e6c1-3359-8f30-e99a89410ab8 | -18.0837 | -57.3076 | 2024-10-24 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.1 |
| 2f0c1b39-cd56-3947-930f-a2828ec7a48f | -18.0841 | -57.287 | 2024-10-24 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 82f6ef39-a4a8-3ba8-a9d0-b11bbe072021 | -23.816 | -55.2713 | 2024-10-24 01:27:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 581b29d3-2e76-3e9b-aa44-f80f94430231 | 1.79397 | -50.47074 | 2024-10-24 01:28:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1a5fd378-1391-3676-a83e-9edaeb020495 | 1.55909 | -55.6665 | 2024-10-24 01:28:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| decc28e8-fcbd-3503-b8b3-8ba44036fb02 | 0.12134 | -62.55434 | 2024-10-24 01:28:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c25a65b4-7b4d-3115-a992-44d29d7de902 | -1.4945 | -54.1962 | 2024-10-24 01:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| c85882aa-d344-32c8-88e7-66b59ea42245 | -1.4945 | -54.1761 | 2024-10-24 01:35:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ad1ed153-88a4-36db-9379-761fa5430d50 | -1.5878 | -53.3292 | 2024-10-24 01:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1da897f9-ebc3-3908-82c1-9721b3a221cd | -1.5878 | -53.3089 | 2024-10-24 01:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 00055a48-ed73-391c-a6af-e1b431dc0c78 | -1.6062 | -53.3087 | 2024-10-24 01:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 92b82bc5-946c-3c9e-86f3-9ee5b63c952e | -2.9578 | -50.4198 | 2024-10-24 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c53b845c-c160-3ec0-b775-5d9dadfb6c8e | -2.9763 | -50.4193 | 2024-10-24 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 84e0225b-d279-3599-9632-396203c77aaf | -3.0745 | -53.8252 | 2024-10-24 01:35:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 62d0195e-b58e-3f8c-97c5-87d675f91b90 | -3.1101 | -54.1661 | 2024-10-24 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d4f683cd-8bee-34c0-960b-0db8a9227a1d | -3.1102 | -54.146 | 2024-10-24 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 68928eb1-c55c-32ca-9345-3a4294086792 | -3.1606 | -50.4766 | 2024-10-24 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2176a454-6755-3b8b-914e-5c5864f91541 | -3.1607 | -50.4556 | 2024-10-24 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3797374f-2f53-3d49-b550-f2e6479a0b22 | -3.7066 | -41.6997 | 2024-10-24 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 5804f58a-ebb8-37ba-898c-ddf37c61ea7d | -3.7068 | -41.6758 | 2024-10-24 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 6613886a-7a5a-3692-9397-5dae9b245e59 | -3.7254 | -41.6987 | 2024-10-24 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 6e4e6114-b920-3190-8e2b-ba653f459f4d | -3.7255 | -41.6748 | 2024-10-24 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 674e2d0f-4bd4-3f3c-8cf2-1131afb15cba | -3.6612 | -54.2715 | 2024-10-24 01:35:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6f55931a-6ca7-3660-908c-90422b3bf45a | -3.9396 | -46.4229 | 2024-10-24 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 324eaee5-c8f4-3c5b-afce-1db07ea3081a | -4.758 | -46.4033 | 2024-10-24 01:35:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 57dbb5d1-c37c-320a-8ce8-8eeccbca06c1 | -5.4373 | -47.6833 | 2024-10-24 01:35:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| f97d8152-660c-3388-af88-532cefe6adc4 | -5.4559 | -47.6822 | 2024-10-24 01:35:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c77c2b4b-2f63-3247-a2ad-2fa276dd4dc0 | -6.7427 | -40.4735 | 2024-10-24 01:35:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| c8fd2c90-cb13-3bb2-bd11-34b7ee82896b | -6.9461 | -40.8447 | 2024-10-24 01:35:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 1e97a2f9-de3f-3cbb-b894-4580285c7d83 | -6.7666 | -59.1129 | 2024-10-24 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| fd22ddff-361e-3921-8655-eed4471e8428 | -7.481 | -63.5577 | 2024-10-24 01:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 03faa9de-2edf-3e62-a6fd-41819b03a5bb | -10.1969 | -53.8822 | 2024-10-24 01:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1306664e-25e8-3eda-bdc8-bee74652cb2f | -10.1971 | -53.8617 | 2024-10-24 01:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c9a2ed51-c6d1-346b-b99e-1f7d79b5d506 | -12.6914 | -43.8484 | 2024-10-24 01:36:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| dc1020fa-007e-3583-a891-9521b0e0c27d | -13.7417 | -54.0682 | 2024-10-24 01:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ea1a5e1a-8540-3787-909e-e5df5a60ea74 | -13.742 | -54.0475 | 2024-10-24 01:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 10437fa5-8759-3d67-8bf1-8d1aa9adb6c1 | -13.7609 | -54.0661 | 2024-10-24 01:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1357f45e-98e4-3641-96a9-0503587d0372 | -13.7612 | -54.0453 | 2024-10-24 01:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4667734d-66e4-3d08-b25f-a63562896082 | -14.9145 | -45.1224 | 2024-10-24 01:36:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a0c09ce3-7860-393b-8874-7dc6eb51743f | -16.9596 | -57.5245 | 2024-10-24 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| 61d858df-67bd-34ae-bef9-ffa2abc40ba3 | -17.0011 | -57.3766 | 2024-10-24 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 88b047a9-b42f-329b-bd60-4e28cfdb28db | -17.238 | -57.2668 | 2024-10-24 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| e01be14b-43c5-3f60-b1df-1670fd34c428 | -17.2383 | -57.2462 | 2024-10-24 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 5b535500-0c2d-3846-8cff-b3299b5c1d2a | -17.2579 | -57.2439 | 2024-10-24 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 8c780420-ee1d-3043-94a6-45f66c697bea | -17.7062 | -57.4774 | 2024-10-24 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| a94ab075-189a-33c0-9adb-3daa6346813c | -17.7637 | -57.5732 | 2024-10-24 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 0a246b17-b4c3-3be1-8339-a54585ea6cb0 | -17.7831 | -57.5914 | 2024-10-24 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| f32d3218-817d-3def-b78e-690e0344dce4 | -17.7834 | -57.5708 | 2024-10-24 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| f20cf9a8-35ec-3893-bb6a-e88a3ebcf435 | -17.7841 | -57.5296 | 2024-10-24 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 2b8af80d-efa1-3f59-8e4d-442a145d28cc | -17.7844 | -57.5091 | 2024-10-24 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 2495e739-b049-3adb-a675-d92f79f5f8ed | -18.0639 | -57.3101 | 2024-10-24 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 032268bc-09bc-3693-a169-d79660f52e49 | -18.0837 | -57.3076 | 2024-10-24 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 6707ef70-6fb7-38ce-869c-df4e30b5cf92 | -19.548 | -56.6143 | 2024-10-24 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 635310b5-b33a-3dde-96c3-770c0ab36c5e | -19.5681 | -56.6114 | 2024-10-24 01:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 120.3 |
| eb30bdf8-1c0b-3313-abd0-32ed0a5aadcf | -23.816 | -55.2713 | 2024-10-24 01:37:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 59aea410-4716-305b-9f5f-f7a519577d57 | 4.8312 | -60.138 | 2024-10-24 01:44:38 | GOES-16 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 33.7 |


[Clique aqui para ver as próximas entradas](README12.md)
