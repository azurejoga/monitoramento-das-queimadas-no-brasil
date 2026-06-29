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
| 0149bbe4-059f-3e02-ac49-f9ad8f9b6a11 | -12.4654 | -58.481 | 2026-06-29 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8b6d1c43-cd06-3e6c-a141-1c4337b797ff | -8.2907 | -48.1876 | 2026-06-29 12:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ec10f963-0b83-3777-8d9e-a330f27d4072 | -9.0684 | -44.7765 | 2026-06-29 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c8e16dab-cd91-38aa-b8e7-9183d826b748 | -11.9533 | -58.6192 | 2026-06-29 12:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 167.6 |
| f48f79bb-2503-35c4-89cf-2e4686867bcb | -12.4464 | -58.4825 | 2026-06-29 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 6984e90b-9ffa-3673-adfe-c66fa464765e | -11.9535 | -58.5995 | 2026-06-29 12:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 082db7b5-a346-3aff-8b22-8292caa6172a | -8.943 | -45.6573 | 2026-06-29 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 20e1ae74-e70b-3789-ad26-8e6108e8025e | -12.4651 | -58.5009 | 2026-06-29 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 151.8 |
| c940d98f-99fa-334c-a720-16e6ca628ebd | -12.4462 | -58.5023 | 2026-06-29 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 234.6 |
| d6923896-6ed5-3fd7-be23-732c27f55213 | -18.78821 | -57.35764 | 2026-06-29 12:10:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 5e7340dd-3bce-35ae-83d7-eb515b919b21 | -17.70978 | -46.76124 | 2026-06-29 12:10:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 8d036985-4a34-3925-87a7-7bb131451749 | -19.85911 | -46.36377 | 2026-06-29 12:10:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 74bb74dd-f858-3ead-af84-ec352b5e7208 | -18.7779 | -57.3558 | 2026-06-29 12:10:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.1 |
| bc87bb9c-d89f-3666-8404-5a2bf3aa014e | -16.22594 | -53.74594 | 2026-06-29 12:10:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54d4246f-0784-3ae7-ad68-df49da061074 | -17.70767 | -46.78116 | 2026-06-29 12:10:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8ba4ce8f-af2f-3f04-8e11-e01121528166 | -19.86775 | -46.37184 | 2026-06-29 12:10:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 945c2986-a28d-36e1-aa3e-82412131c434 | -17.70635 | -46.77529 | 2026-06-29 12:10:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c5ff9d46-1271-362f-bb9c-d89af84140c3 | -17.71888 | -46.7771 | 2026-06-29 12:10:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9880ad1e-2bf2-3bc6-87c8-e6524e5cbc42 | -16.22457 | -53.75525 | 2026-06-29 12:10:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2abd66f4-b518-33e0-b9d4-dbe0fb6e444a | -11.9535 | -58.5995 | 2026-06-29 12:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8ce53477-7d46-3965-9101-fc8102122a10 | -17.712 | -46.7798 | 2026-06-29 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 18e60a9b-14ff-335c-9006-f53ae4f88c68 | -12.4464 | -58.4825 | 2026-06-29 12:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 26108cef-f3b1-3f4d-bb80-a87d1e433037 | -11.9533 | -58.6192 | 2026-06-29 12:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 180.7 |
| cfa43c2e-bd8e-3d1b-b490-c36cc3d447c4 | -8.943 | -45.6573 | 2026-06-29 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 25241ed4-6980-3945-9ad3-3256d2dfd15e | -12.4651 | -58.5009 | 2026-06-29 12:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 2aab9c0f-b1ea-3e89-a522-2190f6a5154c | -8.2907 | -48.1876 | 2026-06-29 12:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 70dc36eb-06bf-3a1d-a754-0b2a067dd821 | -12.4654 | -58.481 | 2026-06-29 12:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 13031fe0-dcc8-38bc-b3d1-f8efee740e88 | -12.4462 | -58.5023 | 2026-06-29 12:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 288.8 |
| d0efb8c7-d423-3a1b-ae0f-15183ce27dbd | -9.0684 | -44.7765 | 2026-06-29 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| d7bb985b-67a8-3ee6-9ff5-c76d607dc12c | -12.4651 | -58.5009 | 2026-06-29 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 0d09a341-b421-3c3a-9b5c-674b478223b5 | -9.0687 | -44.7535 | 2026-06-29 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 92f4a0e7-8bbf-3226-9121-17e46d7bf102 | -8.943 | -45.6573 | 2026-06-29 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 0e21a679-dcb2-38c6-8611-dfcff90fe399 | -9.0873 | -44.7743 | 2026-06-29 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 74018c78-d93f-3f63-8e55-79cf19bc6051 | -17.712 | -46.7798 | 2026-06-29 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| f4780e18-d409-3208-9d96-9666f41a0c7e | -12.4464 | -58.4825 | 2026-06-29 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 4313bf97-2296-3cec-9260-96b7860fe071 | -11.9535 | -58.5995 | 2026-06-29 12:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 21bf9bb9-6730-36e6-96b9-4efda3b097c4 | -11.9533 | -58.6192 | 2026-06-29 12:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 393fb74a-c66e-3770-9fa2-015586033c3d | -12.5135 | -48.2802 | 2026-06-29 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| f4937218-5e2c-306b-be61-3ef854c56bce | -12.4654 | -58.481 | 2026-06-29 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 7aec8660-c967-3aea-be5c-f6b20c93b86a | -8.2907 | -48.1876 | 2026-06-29 12:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a3f27221-3c6a-383f-a993-d26329393667 | -9.0684 | -44.7765 | 2026-06-29 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 59306677-f1a6-3649-83f4-dc7550708298 | -12.4462 | -58.5023 | 2026-06-29 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 0868f331-c5f0-3686-82ee-5ce98b8b5a9b | -9.0687 | -44.7535 | 2026-06-29 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 30273732-4052-3ead-913f-d1a44c7bc803 | -12.4462 | -58.5023 | 2026-06-29 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 293.2 |
| 06535a0f-953b-330e-9703-623782f6aa86 | -8.2907 | -48.1876 | 2026-06-29 12:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a7fed750-2f3b-3ede-a254-950427d87a2b | -12.4654 | -58.481 | 2026-06-29 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e980de80-1a11-38c7-ab86-9f843a3baeb9 | -11.9533 | -58.6192 | 2026-06-29 12:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 41a059e2-af86-3b82-bc23-9875962f719d | -12.4464 | -58.4825 | 2026-06-29 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 7dfaf44a-edb4-33e2-9332-f81b3f83f815 | -11.9535 | -58.5995 | 2026-06-29 12:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 73080b8c-b27e-322e-aa38-d51cdb5484fd | -12.4651 | -58.5009 | 2026-06-29 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 7dd12aac-186d-3416-870f-24fb7db2bb73 | -9.0684 | -44.7765 | 2026-06-29 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c11c6979-4530-3565-9208-1587120590e0 | -17.712 | -46.7798 | 2026-06-29 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 8ee8bfcd-3478-3e09-86ae-793aa772add4 | -12.5135 | -48.2802 | 2026-06-29 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 37e7b536-8929-33c8-84bb-d7a89b564fc4 | -8.943 | -45.6573 | 2026-06-29 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 65c3d791-33af-3e26-9e5f-a34b2cd0b7b3 | -12.4464 | -58.4825 | 2026-06-29 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 28b7ea89-eb25-3077-bdf1-e89f237041bf | -8.943 | -45.6573 | 2026-06-29 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 046c10a9-d864-3064-b5e6-903e0ce734a8 | -12.4651 | -58.5009 | 2026-06-29 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 58549c78-f920-3d77-b8a1-7299e9d8dcf0 | -12.5135 | -48.2802 | 2026-06-29 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 85860c09-411b-37a7-a3fd-f07805ff4479 | -9.0876 | -44.7513 | 2026-06-29 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 39b417ad-ddca-316f-bd09-08a555b4e170 | -17.7126 | -46.7565 | 2026-06-29 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ec574174-a506-3aa0-954a-1dc01838f98d | -11.9533 | -58.6192 | 2026-06-29 12:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 194.5 |
| a3ef9e8a-12f7-3204-8026-513c4e57ebc5 | -9.0873 | -44.7743 | 2026-06-29 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2a08268b-6568-34b9-9bda-210bef0fa2bf | -17.712 | -46.7798 | 2026-06-29 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 622b6c1f-872a-34fd-b853-afa7e0e096da | -11.9535 | -58.5995 | 2026-06-29 12:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 02adaceb-0ba6-32b9-b1f7-7a083e1facb1 | -9.0684 | -44.7765 | 2026-06-29 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 574ee27c-bc72-300a-8129-ebbed951f182 | -12.4462 | -58.5023 | 2026-06-29 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 357.0 |
| d37a5d62-af5c-390f-b07a-b41f02fb19b7 | -12.4654 | -58.481 | 2026-06-29 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| f73d88c5-5ced-32d9-a0f9-797b13f815d0 | -8.2907 | -48.1876 | 2026-06-29 12:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 096b1498-e5ba-3fad-97dd-96d16f780c97 | -9.0687 | -44.7535 | 2026-06-29 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 88528840-94ca-310d-a033-cbfccc3b289b | -12.4654 | -58.481 | 2026-06-29 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 254570a2-8bd9-333a-9ed7-909d40dda6ac | -11.9533 | -58.6192 | 2026-06-29 13:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 148.0 |
| e7c0bef1-dd09-3b5c-a95d-6a9228f81950 | -17.712 | -46.7798 | 2026-06-29 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 6ca62c78-c56f-3150-9ac4-8ecb7ef71cfe | -8.2907 | -48.1876 | 2026-06-29 13:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 33e902de-ffd2-3152-9987-bb5e657744d6 | -12.4651 | -58.5009 | 2026-06-29 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 1deb50ce-d9bc-33fb-b01b-1050e94619b3 | -8.943 | -45.6573 | 2026-06-29 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| ae0ae8b7-f171-35f2-b215-f7106cfe80fb | -17.7126 | -46.7565 | 2026-06-29 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9ae5423f-6bec-31da-a776-0e14df68ef88 | -12.4462 | -58.5023 | 2026-06-29 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 389.6 |
| ea5f9e63-2002-3b35-bc63-bed43bf7975c | -12.4464 | -58.4825 | 2026-06-29 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 326.6 |
| 5b31b308-0ad7-3b32-adbb-28de1800859e | -12.5135 | -48.2802 | 2026-06-29 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 836d51ed-634d-30a1-b2f4-2312b1541937 | -9.0687 | -44.7535 | 2026-06-29 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| a5901776-a329-3baf-9411-08faf696e980 | -11.9535 | -58.5995 | 2026-06-29 13:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 64eff461-203b-3982-a26f-d27828a4813b | -9.0684 | -44.7765 | 2026-06-29 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| e4cea724-4bfd-359b-91c0-d5fbbaa684bb | -8.2907 | -48.1876 | 2026-06-29 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c4aa7881-32ff-3fc8-9470-1e758e454b45 | -9.0687 | -44.7535 | 2026-06-29 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e51c9064-eb12-3ef9-8fe7-c5fd51bbe02f | -8.943 | -45.6573 | 2026-06-29 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| e8653301-c6b8-35b1-bfd1-985fa62d4b3c | -12.5135 | -48.2802 | 2026-06-29 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| c531f9ab-b592-3529-b222-5bf41dd6c123 | -17.712 | -46.7798 | 2026-06-29 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 425386b2-4a7d-3b5f-91b7-1c36ca121989 | -12.4651 | -58.5009 | 2026-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 203.4 |
| e17b1e86-a81a-35a1-90eb-3e92485fdbf5 | -11.9535 | -58.5995 | 2026-06-29 13:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9eb5f26e-b8d0-3a93-ac1e-8c47e40ae176 | -12.4464 | -58.4825 | 2026-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 333.0 |
| df296fed-ccd4-3772-a948-4699aafa3f8e | -12.4462 | -58.5023 | 2026-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 389.7 |
| 0c4f6c4f-936b-3543-bb56-68b2dfaf4e65 | -12.4654 | -58.481 | 2026-06-29 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 182.3 |
| e5356e24-8575-3d4d-8fc4-434c738c367c | -11.9533 | -58.6192 | 2026-06-29 13:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| edefa3e8-ebdf-3aa2-a3c2-04bb7c677957 | -17.7126 | -46.7565 | 2026-06-29 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 98a66d07-897f-3382-ba0b-87977e169473 | -9.0684 | -44.7765 | 2026-06-29 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| ee708eb5-16ff-3dcd-ae23-4166776d0863 | -12.4462 | -58.5023 | 2026-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 7be0175d-f7c1-3d76-b6d0-1f84e4845c8b | -9.0687 | -44.7535 | 2026-06-29 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 6a603834-cfe0-39e0-bf26-473f401c87e4 | -9.0684 | -44.7765 | 2026-06-29 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 29aaafed-fb92-386c-b7e6-1aeafdef0752 | -8.2907 | -48.1876 | 2026-06-29 13:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5282b0ac-6a3b-3de6-a88a-ad7e912b3e05 | -12.4654 | -58.481 | 2026-06-29 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |


[Clique aqui para ver as próximas entradas](README12.md)
