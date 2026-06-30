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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 027ce825-3b6c-3c14-9da2-0c277aa0340d | -17.712 | -46.7798 | 2026-06-30 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 136.7 |
| f330ce85-6e00-3943-ad76-52ff1043965c | -8.9985 | -45.7418 | 2026-06-30 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| c3ea83c6-ab3b-362e-bafb-68ae044b3a61 | -8.9799 | -45.7212 | 2026-06-30 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 8c07b778-e7e1-3e9e-aabc-7b1fb2da7dfd | -8.9989 | -45.7191 | 2026-06-30 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 349.1 |
| cbaa1d8c-c774-3dcc-8a4c-7a33bb005370 | -8.943 | -45.6573 | 2026-06-30 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 2b1906cc-1221-3e90-bc32-d4591dbc299c | -8.9619 | -45.6552 | 2026-06-30 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 446e9061-fa01-3389-933d-28d74a06bf85 | -17.712 | -46.7798 | 2026-06-30 12:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 8cda5309-7128-3f15-8721-841e977951ee | -8.9619 | -45.6552 | 2026-06-30 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 54b28699-f869-3fbc-8957-5af503a3d963 | -8.9799 | -45.7212 | 2026-06-30 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 45f6a302-2b33-3bbd-9d2d-de3716871573 | -17.712 | -46.7798 | 2026-06-30 12:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 224.5 |
| 59c9d6b0-05b2-3823-9863-4eddd360715b | -8.943 | -45.6573 | 2026-06-30 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 6c4b5139-6a86-35a5-b5ff-a5a771dfa3d6 | -8.9985 | -45.7418 | 2026-06-30 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 096ad436-4748-3878-acb8-ec30b6eb6469 | -8.9989 | -45.7191 | 2026-06-30 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 344.4 |
| 7e8753ca-71c2-3dd8-bb5c-de1ac72c253f | -11.9441 | -57.7091 | 2026-06-30 12:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 7a22a2ea-3b55-36c9-9072-0da759e19c1f | -11.9441 | -57.7091 | 2026-06-30 12:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| d64b2915-f15b-3317-82f6-8313ea3c27df | -17.712 | -46.7798 | 2026-06-30 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 204.0 |
| ce2c90cf-80dd-3622-8b88-29dde2c0b612 | -8.9989 | -45.7191 | 2026-06-30 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 289.1 |
| 17115581-d9f1-3888-9708-d79b7a255719 | -8.943 | -45.6573 | 2026-06-30 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 4b643086-1fba-3185-8697-101153ed2681 | -8.9616 | -45.6779 | 2026-06-30 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| e8f541f0-f73c-338e-a844-626b65eeabd7 | -8.9799 | -45.7212 | 2026-06-30 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 324ad7ce-568b-324a-a00c-c0b1cd518c65 | -8.9985 | -45.7418 | 2026-06-30 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 41bb3987-04bb-3cf0-8509-2fccb4355c7d | -8.9619 | -45.6552 | 2026-06-30 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 211.2 |
| b21373ee-1d41-3ae6-ba7e-33f0c15ad69b | -10.91001 | -56.85149 | 2026-06-30 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3e9bb512-8f08-36f2-9640-9c2ff945f41d | -12.44943 | -58.48251 | 2026-06-30 12:46:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 792fea08-9808-3832-97dc-350cab1de4d0 | -12.19831 | -52.87202 | 2026-06-30 12:46:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e7d1efaf-27ac-3a9a-8d38-8b100d70080f | -11.93717 | -57.70169 | 2026-06-30 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 32c75890-2805-3bd8-82ec-ad42f5d0eb50 | -12.21886 | -56.55104 | 2026-06-30 12:46:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8ae90eee-04ee-36d1-87ae-681efc3026eb | -11.89464 | -57.13192 | 2026-06-30 12:46:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8e333bc5-331b-3262-a89f-55a4f2693e72 | -11.93551 | -57.71482 | 2026-06-30 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 4ce0613c-a5b9-3a08-b6bb-6af64be4fa45 | -12.21683 | -56.56726 | 2026-06-30 12:46:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 78900285-0e5f-368d-b010-1ab9d57bf30e | -9.32357 | -58.01989 | 2026-06-30 12:46:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b680248d-09dc-3c27-b072-59d0ba2996cb | -12.44794 | -58.49426 | 2026-06-30 12:46:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| bf3e129f-d89f-31b4-a757-0e7435437a1a | -9.08746 | -59.43018 | 2026-06-30 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8fc3e542-318f-39dd-abea-64f5d3f5ab28 | -11.79668 | -56.98879 | 2026-06-30 12:46:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 1ce78f16-11d1-3b76-a1a3-c680fa746e65 | -10.29897 | -57.13091 | 2026-06-30 12:46:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8a45ff35-7192-3d1f-b99c-46424ecb0c58 | -12.44872 | -58.48806 | 2026-06-30 12:46:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 5a8ad39e-59b8-3260-b5c4-2eeffaf8772c | -11.94604 | -57.71624 | 2026-06-30 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 21503689-08b6-3bce-8cce-72782a1c2a52 | -11.79481 | -57.00343 | 2026-06-30 12:46:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 0977b276-3cb5-311b-b149-796be9df1d60 | -11.94772 | -57.70308 | 2026-06-30 12:46:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| dcf8e46c-f360-3512-af2d-94b7822b5f2b | -9.0888 | -59.42059 | 2026-06-30 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9f28d134-7f16-3939-a3b7-4281e6cb64a2 | -11.89336 | -57.12531 | 2026-06-30 12:46:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 362e8d52-e8ea-3ec0-b1bc-2614e96474a7 | -10.60305 | -53.46153 | 2026-06-30 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 94437b37-43b0-3d15-9fed-7fbcbfe475e7 | -9.60279 | -56.92161 | 2026-06-30 12:46:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1fb6db9f-7661-3d51-84f5-5cdd7185a7db | -18.25214 | -53.84825 | 2026-06-30 12:49:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 04af00ec-82b1-3a1c-a392-76c5113f9a2c | -17.9191 | -52.69764 | 2026-06-30 12:49:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 54d74b9b-fa0c-35d3-aefe-3a4e9e998fec | -14.20496 | -57.42838 | 2026-06-30 12:49:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| a57095f7-e09a-349a-9592-8ce4916f2320 | -15.28413 | -57.40045 | 2026-06-30 12:49:00 | TERRA_M-T | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4051cf6e-d5d6-35f2-b262-570a9299e7ab | -15.22683 | -55.51517 | 2026-06-30 12:49:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4d44d959-5c6f-3862-9344-5e97b8230062 | -17.9151 | -52.69213 | 2026-06-30 12:49:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| e3b2a0d7-9ca0-3b7f-8020-6500687d09a1 | -16.07768 | -58.50108 | 2026-06-30 12:49:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 8615f8ca-e9ff-3451-b511-07ce2dc1e39d | -18.24183 | -53.84055 | 2026-06-30 12:49:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 22938cfb-b1cf-382f-a77e-0e4fab664b9b | -14.20682 | -57.41333 | 2026-06-30 12:49:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 0bd0fdd9-f77a-358d-86b7-5b1da8b570af | -17.91145 | -52.73153 | 2026-06-30 12:49:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 44.9 |
| c52adff6-df1a-37c6-81f3-916b9bc6430c | -17.91569 | -52.73719 | 2026-06-30 12:49:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 77607fda-1e34-38e5-a633-6f8c2b201bf9 | -15.28599 | -57.38477 | 2026-06-30 12:49:00 | TERRA_M-T | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1b583aaa-0237-3ad0-ab04-35fc55ff4783 | -13.26297 | -56.80291 | 2026-06-30 12:49:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 16b00231-cefa-3a43-a3e9-6a9204981f58 | -8.9619 | -45.6552 | 2026-06-30 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 260.4 |
| 15312f09-4043-3c1f-b669-28108d609d5f | -8.9985 | -45.7418 | 2026-06-30 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 272f49b1-733c-364f-be0d-28eb9862edae | -8.9989 | -45.7191 | 2026-06-30 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 842c2110-920a-31bc-bc55-ae4d4a48b28a | -11.9441 | -57.7091 | 2026-06-30 12:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 95f6ddeb-0dc2-31e3-86dd-2b58febd0274 | -8.943 | -45.6573 | 2026-06-30 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 5d64b4c3-db2b-35db-bede-e64966a2f4db | -8.9799 | -45.7212 | 2026-06-30 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 156be538-0e89-34bc-ac43-6947369aae7d | -17.712 | -46.7798 | 2026-06-30 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 300d51b3-c07f-3f50-b99c-d9afe396f49f | -8.9616 | -45.6779 | 2026-06-30 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 54a7fa30-d736-3e41-93f7-020e51e428d9 | -8.9989 | -45.7191 | 2026-06-30 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 8d05d78e-3d9e-379c-a0d1-680bca72929b | -8.9985 | -45.7418 | 2026-06-30 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 96d74823-42d5-3669-888d-dbc3d7c1af07 | -15.29 | -57.3823 | 2026-06-30 13:00:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f90a38ad-e657-366b-a6d1-74f5ccd89ec4 | -8.9616 | -45.6779 | 2026-06-30 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 9316e886-7823-33be-b527-b49208b42ef0 | -8.943 | -45.6573 | 2026-06-30 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 8e162477-2d13-3298-88a8-879bb14b8862 | -8.9799 | -45.7212 | 2026-06-30 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 086fa574-de27-34e5-a5af-632c0fc89593 | -17.7114 | -46.8031 | 2026-06-30 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 97c794ae-424a-346d-9bef-cef6c0ac2933 | -11.9441 | -57.7091 | 2026-06-30 13:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| ae07ab1c-88f2-3ea3-bdca-6329c13957cd | -8.9619 | -45.6552 | 2026-06-30 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 230.0 |
| bf036871-6d30-31d3-9ce1-d17d1e43b3d4 | -17.712 | -46.7798 | 2026-06-30 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 195.9 |
| b09c0c12-0b3c-35f7-b391-016f054c7e04 | -8.943 | -45.6573 | 2026-06-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| cea2cf77-a725-38c9-b083-a18f214d4b01 | -8.9985 | -45.7418 | 2026-06-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 7c18737f-1490-32a3-9aa1-f1bdac2af193 | -15.29 | -57.3823 | 2026-06-30 13:10:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 07cee207-3906-37ee-948d-ad8a07340a54 | -8.9619 | -45.6552 | 2026-06-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 594c2231-0acb-3adf-8a82-a1bf7437e71e | -8.9799 | -45.7212 | 2026-06-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| feb0ecaa-d62e-3a63-bcc2-539a6ac5e40f | -17.712 | -46.7798 | 2026-06-30 13:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 206.5 |
| d455bacb-37ba-39ff-8607-2ceefbd6d9e6 | -8.9989 | -45.7191 | 2026-06-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 228.8 |
| a7fc9abe-8620-389c-8542-f7b70c870705 | -8.9616 | -45.6779 | 2026-06-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 93ae4eb7-5667-3d79-927a-e1e4ae3cfc0d | -11.9441 | -57.7091 | 2026-06-30 13:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 495d08c6-d778-3dcc-a294-0bb661706f50 | -15.29 | -57.3823 | 2026-06-30 13:20:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e1121bb1-2fc7-3db7-bd7c-8393c532df2a | -12.4283 | -58.4048 | 2026-06-30 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7696d2e9-db06-36cc-9eeb-58275530bfbe | -8.9985 | -45.7418 | 2026-06-30 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| ba60a4bb-4e41-306c-886d-67fc45481f66 | -8.9619 | -45.6552 | 2026-06-30 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 9df0c4f8-8286-3069-8acc-782e966f7c53 | -8.9799 | -45.7212 | 2026-06-30 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5ed9f60d-f668-3cda-98ba-68badebc34b7 | -17.712 | -46.7798 | 2026-06-30 13:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 5a0a7f7f-3c3b-36ac-92e7-7c97fb8bfa01 | -8.9989 | -45.7191 | 2026-06-30 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 277912bc-895f-3712-867f-6cc12933bbab | -11.9441 | -57.7091 | 2026-06-30 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| c0a29cbf-3c98-354d-8837-ccd445bf0193 | -8.9616 | -45.6779 | 2026-06-30 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b4118c79-9ceb-3d82-8e08-5126a5dbd731 | -8.943 | -45.6573 | 2026-06-30 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 2e6cf352-808d-323b-8809-05ddce657358 | -8.9619 | -45.6552 | 2026-06-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 219.0 |
| c34f225c-65ab-37b2-afe9-a77d1698d738 | -11.9441 | -57.7091 | 2026-06-30 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 0437f379-28ac-37d0-a886-da1eb803f4a7 | -17.712 | -46.7798 | 2026-06-30 13:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 965aa58c-a32b-38de-b338-4b8f6c3fce07 | -8.943 | -45.6573 | 2026-06-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9c53b128-4d92-35c1-b6da-cb1dc0c30c5d | -15.29 | -57.3823 | 2026-06-30 13:30:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 767b80c6-fd46-3fa4-9b99-6d56c650ee19 | -8.9799 | -45.7212 | 2026-06-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6635b5ce-4ee7-3324-918a-de7e205d2910 | -11.9251 | -57.7106 | 2026-06-30 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |


[Clique aqui para ver as próximas entradas](README21.md)
