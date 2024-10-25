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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa959601-442f-3a4a-b055-8f516456312c | -4.8423 | -45.0309 | 2024-10-25 00:45:32 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 73aad510-c815-33d1-be1d-1b45cc6dfe50 | -5.6478 | -46.9687 | 2024-10-25 00:45:37 | GOES-16 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 124993ed-5eab-393a-ac5a-2c994b539cbd | -6.5219 | -60.0457 | 2024-10-25 00:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| be2cb39c-9e59-305c-be05-0d6cca78d089 | -6.522 | -60.0266 | 2024-10-25 00:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| e6d2d569-1c85-31b2-b977-f9f4e287ebd2 | -6.6472 | -47.8642 | 2024-10-25 00:45:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 6c0de882-6f79-3d3d-8b0b-e5d9373eba3b | -8.9064 | -48.544 | 2024-10-25 00:45:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ade3b343-2e4f-3430-9fec-cf6fe4dd1e80 | -10.6519 | -47.9207 | 2024-10-25 00:46:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1ea7bbe2-22ff-382a-b13c-bc4a661f65c2 | -11.883 | -56.4152 | 2024-10-25 00:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9178a1af-a33c-37f1-a0aa-b01875bb3718 | -11.8854 | -56.2138 | 2024-10-25 00:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b5df0664-7876-35e0-add6-ad7638dd20ed | -11.902 | -56.4135 | 2024-10-25 00:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 48b96908-4045-3cea-818e-47f94d9f653b | -11.9022 | -56.3934 | 2024-10-25 00:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 4b558fdc-a138-3954-b2fa-34382db9e3c3 | -12.0444 | -63.1547 | 2024-10-25 00:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| cfdff3fe-a394-33f7-9a8b-e310bcc2f1bb | -12.0445 | -63.1356 | 2024-10-25 00:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| cd405e92-a0b4-3dc8-b3b1-f40ec78edb2f | -12.0632 | -63.1537 | 2024-10-25 00:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 86cbc68a-3ba5-3180-882f-d4543dbb67c1 | -12.0634 | -63.1346 | 2024-10-25 00:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d8b6fc69-6ea4-3c2d-a3dc-43cd4333b5cf | -12.3782 | -63.8821 | 2024-10-25 00:46:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| da53c709-568c-3436-aeb1-0a768702e9ed | -12.3783 | -63.863 | 2024-10-25 00:46:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ccb5f6c3-b012-30d4-9a83-a27a69231891 | -12.3971 | -63.8811 | 2024-10-25 00:46:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a2958393-2f94-32ef-826d-09aca681c332 | -12.4589 | -63.1895 | 2024-10-25 00:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c5f0f059-bd92-306b-977c-9d8ccea7f1a7 | -12.4591 | -63.1704 | 2024-10-25 00:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 2529c773-a27a-394d-a5de-d0d8732296bc | -12.478 | -63.1693 | 2024-10-25 00:46:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2a0c701c-2479-367f-91b8-9c0a39c40025 | -12.5356 | -63.051 | 2024-10-25 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 3a98b9f2-fd86-3363-a0cd-1abf090d1dbb | -13.4767 | -61.6411 | 2024-10-25 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9b6c4765-8afc-30b7-847c-a407446d86a8 | -13.4769 | -61.6217 | 2024-10-25 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3159a3d2-6978-3263-89a3-9457aae9bec1 | -13.4957 | -61.6398 | 2024-10-25 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ce3c4467-4e6a-30e1-a22b-3ec143b0f65a | -13.4959 | -61.6203 | 2024-10-25 00:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 14ca9d54-21f2-3960-b7d0-45efadc577bd | -14.1339 | -44.3037 | 2024-10-25 00:46:24 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| ae31b964-e258-3383-b666-760ec5433cd3 | -17.4012 | -39.9669 | 2024-10-25 00:46:41 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 125.5 |
| a06bcc16-ff07-3f7a-b16e-071f65d3ddac | -16.94 | -57.5268 | 2024-10-25 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 2f5d898a-2c85-3812-9d47-82482afdf556 | -16.9596 | -57.5245 | 2024-10-25 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.2 |
| a2af8b53-a952-3bdd-b396-d6c5c0a8a1dd | -16.9792 | -57.5223 | 2024-10-25 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.4 |
| c3811219-7523-3a82-af52-017d49c8a4d4 | -17.0184 | -57.5178 | 2024-10-25 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 081f0388-9e2c-3d06-a565-7d27948859e5 | -17.0381 | -57.5155 | 2024-10-25 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| 10e5aa1b-3299-3199-89cd-b71d4de2ce37 | -17.7671 | -57.3673 | 2024-10-25 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 87760ec5-9639-3c5e-99eb-0b63481f9267 | -17.8038 | -57.5273 | 2024-10-25 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| d4310117-e90f-3788-83a4-ce94c007347e | -17.8042 | -57.5067 | 2024-10-25 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| ab598330-455b-3454-b340-22ace092b632 | -17.8239 | -57.5043 | 2024-10-25 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| bf18d4d3-9146-34bc-9a4f-151bdf0c48ca | -17.8822 | -57.5588 | 2024-10-25 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| d0db38a2-2392-3c93-b808-af1d21645424 | -17.9019 | -57.5564 | 2024-10-25 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| b47231ca-1b4e-30f6-a6d9-e969ed5444f2 | -17.9023 | -57.5359 | 2024-10-25 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 771c3a5e-49f2-3ffc-afa0-d4d09d63da33 | -18.0056 | -57.2555 | 2024-10-25 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| d1fb1b96-615f-3849-8b83-35be6691f1a5 | -18.0059 | -57.2349 | 2024-10-25 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| dbfb3e50-0cb5-3ab8-9832-ee7b554dc6c8 | -18.0254 | -57.253 | 2024-10-25 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 179a5aa7-905e-305a-8540-b838da8d056a | -18.0452 | -57.2506 | 2024-10-25 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 5332caee-3289-3d60-8e08-a2dc6881865e | -18.0844 | -57.2663 | 2024-10-25 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 7ecad51c-2f7d-3a4f-b05e-7a131d296168 | -18.1042 | -57.2638 | 2024-10-25 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 47438eca-69e7-3cab-b4bc-0618017c13e0 | -18.1223 | -57.3647 | 2024-10-25 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 5713c70a-ccfa-338e-ac2d-558287107daf | -18.1226 | -57.344 | 2024-10-25 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| d1f2d551-ba1a-385e-b52f-3ec2e22abc27 | -18.1421 | -57.3622 | 2024-10-25 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 19d1072f-6041-36d6-9170-b6867635c0a8 | -18.1424 | -57.3415 | 2024-10-25 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| 1ab09c3d-f258-3a62-b44c-b75002876121 | -1.0445 | -47.6237 | 2024-10-25 00:55:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 4dfc8d79-2e41-3019-8cff-8abeef4d82b7 | -1.1834 | -53.6771 | 2024-10-25 00:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 690a5bfe-bb48-39ae-b0bc-be8cd5c9eab8 | -1.1834 | -53.6569 | 2024-10-25 00:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6bb77901-6d15-340d-a7d5-b19c8196f632 | -1.1925 | -47.6002 | 2024-10-25 00:55:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 8a629fa0-adc5-3fd2-a04c-295be3b00705 | -1.211 | -47.5999 | 2024-10-25 00:55:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| cd4fc0bd-d79d-39ee-9356-c34df6078763 | -2.6192 | -52.4564 | 2024-10-25 00:55:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 63f80cab-4af7-35b8-9a4a-cb233a6863a3 | -2.6193 | -52.4359 | 2024-10-25 00:55:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| b29e8b7c-1440-3021-8583-7174ebec1331 | -2.6297 | -49.247 | 2024-10-25 00:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bfbd1565-0e85-3c53-a954-940514791d54 | -2.6482 | -49.2465 | 2024-10-25 00:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 09c21889-54ff-3ac5-b880-21778ac0d773 | -2.796 | -49.2636 | 2024-10-25 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 457b33a0-161a-3104-a44a-3a386dd920ae | -2.796 | -49.2424 | 2024-10-25 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| cd7b638e-6654-3b69-9967-4c3a65a49844 | -2.8144 | -49.2631 | 2024-10-25 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| ee9637c3-e29b-3bd2-8f0a-dbca3f63c0fb | -2.8145 | -49.2418 | 2024-10-25 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 672b5d45-0b4b-3160-b6b8-c06ace12ce32 | -2.9578 | -50.4198 | 2024-10-25 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6356077d-8834-3bc9-94c0-d59c4956a228 | -3.1258 | -45.7002 | 2024-10-25 00:55:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 699a6a6c-9eef-3be7-8391-40748017b96f | -3.2553 | -45.807 | 2024-10-25 00:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6c8fbd4b-1a45-3147-a606-e19ad4d4ed7a | -3.3124 | -49.5235 | 2024-10-25 00:55:24 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 92413157-74a9-3876-9125-5ffb7a945471 | -3.9394 | -46.445 | 2024-10-25 00:55:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3f888d55-9235-3783-bb9b-70b94bf4025e | -3.9396 | -46.4229 | 2024-10-25 00:55:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 31ce4d99-4627-39a6-a802-3829d4c4cdc8 | -3.958 | -46.4442 | 2024-10-25 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7d4bbe21-cebf-3e2a-944e-ae6514310def | -3.9581 | -46.422 | 2024-10-25 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| fa9cf816-5cb3-37f0-9f29-0fbb39b1492a | -4.2243 | -48.5482 | 2024-10-25 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3b14222d-be79-3272-831b-6f04701b8fa9 | -4.2429 | -48.5474 | 2024-10-25 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 802389e1-a6ad-3cd5-b3d9-eb2be86321f8 | -4.2441 | -48.332 | 2024-10-25 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 36762ccd-9bc5-38fe-b381-945a127aecff | -4.2626 | -48.3311 | 2024-10-25 00:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4c6ca816-a653-3e1d-b5c6-a76f6306371a | -4.5045 | -48.2117 | 2024-10-25 00:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ec383fca-d5c3-3a4f-a113-8cd0fec4025c | -4.58 | -48.0132 | 2024-10-25 00:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3722035f-a7ba-3cc7-b45f-84bd5effad81 | -4.8421 | -45.0536 | 2024-10-25 00:55:32 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e4785487-d137-3bf6-85e7-3b33c7b7290c | -4.8423 | -45.0309 | 2024-10-25 00:55:32 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ae640365-0df5-3af5-a9b5-a6792ffd8887 | -4.9208 | -49.8378 | 2024-10-25 00:55:33 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b155dd52-3127-34a8-81b6-04dcc3acdb31 | -5.9788 | -45.3621 | 2024-10-25 00:55:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| bdf13b50-3037-3977-a896-7227387ff068 | -6.5219 | -60.0457 | 2024-10-25 00:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| f6cad7ed-12de-3eaa-83f3-08c08a864ec6 | -6.522 | -60.0266 | 2024-10-25 00:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 1c0e2a83-e0e9-3912-9c4f-3734ed87fac6 | -6.5403 | -60.045 | 2024-10-25 00:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b13d1e9c-c623-35bb-92ad-b0cebc5fd8e6 | -6.6472 | -47.8642 | 2024-10-25 00:55:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 345cd601-65a9-3c89-9ff2-bfbda3d82a81 | -8.9064 | -48.544 | 2024-10-25 00:55:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 140fcafe-ab77-372d-9679-bf7b7efc4fe2 | -9.775 | -36.368 | 2024-10-25 00:55:59 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| 06d0f6b9-0ece-36f0-9974-be2c32dad034 | -9.9691 | -36.2802 | 2024-10-25 00:56:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 8866f36a-92c1-347f-bf67-8a5243214c73 | -10.6519 | -47.9207 | 2024-10-25 00:56:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c295c59b-5b3c-3ff2-829e-298bf3e14366 | -11.883 | -56.4152 | 2024-10-25 00:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ccb3e030-06c5-36a1-baf7-d67ee6d5236d | -11.902 | -56.4135 | 2024-10-25 00:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 9fa9bc23-1e47-3722-906e-68caa582c7f3 | -11.9022 | -56.3934 | 2024-10-25 00:56:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e4d15047-5a85-361e-aaee-6933f86ccc66 | -12.0444 | -63.1547 | 2024-10-25 00:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 110.4 |
| e05be037-cbf6-35e2-be40-c55da2f03615 | -12.0445 | -63.1356 | 2024-10-25 00:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 330c58d2-ac2c-35c8-88bf-95fd3119e92b | -12.0632 | -63.1537 | 2024-10-25 00:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 143.5 |
| d2211341-0bb6-3a50-b966-6fdcdc33bc94 | -12.0634 | -63.1346 | 2024-10-25 00:56:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 63959e2a-37cd-3afd-85d2-39504795b91c | -12.3782 | -63.8821 | 2024-10-25 00:56:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 83586bb5-d78c-3b0b-b5e9-c1b1d3181cf9 | -12.3783 | -63.863 | 2024-10-25 00:56:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 73297da9-2522-331f-b5b6-0728377f8953 | -12.3971 | -63.8811 | 2024-10-25 00:56:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 55b90a3b-37ab-3bdb-ae50-bfa4cccfdf64 | -12.4589 | -63.1895 | 2024-10-25 00:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |


[Clique aqui para ver as próximas entradas](README10.md)
