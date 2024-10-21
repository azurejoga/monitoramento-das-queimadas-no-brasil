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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdf16f26-00c8-37a3-8ddd-ccd835414d50 | 1.0579 | -51.127399 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c3e16168-20f5-3d75-8ca4-88a7b1fa224c | 1.0564 | -51.134201 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed74875-575b-3f96-9cb3-861d42d2c929 | 1.0533 | -51.1478 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 51df141c-9922-3b49-b83d-722bf58ca095 | 1.0518 | -51.154598 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0edef00b-db1a-3193-9007-06c6fb467392 | 1.0503 | -51.1614 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6986aa6a-dda2-3b49-87c8-fdd017ae5725 | 1.0487 | -51.168201 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6d11ab3f-83a4-3635-8201-766d022f0214 | 1.0472 | -51.174999 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2cad9926-cfec-3a55-a9bc-b7c31b2d78c8 | 1.057 | -51.1772 | 2024-10-21 00:40:48 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a9e441db-606e-37d9-ab16-26a872a94a4e | 1.8712 | -50.491402 | 2024-10-21 00:40:59 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c0ec3a78-4e71-3dc2-9eaa-4293c6cb0863 | 1.8614 | -50.489201 | 2024-10-21 00:40:59 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 18398092-e99d-388c-8d89-e63ef95bcd0b | 1.8728 | -50.484501 | 2024-10-21 00:40:59 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 697bbbbc-0fca-3d3b-8262-f7005caa3b60 | 2.1441 | -50.652599 | 2024-10-21 00:41:04 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d4a9c2f8-bbfe-3d3d-8b84-0c5aa4fbe08e | 2.1426 | -50.659401 | 2024-10-21 00:41:04 | METOP-B | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 56629988-8650-3f67-ab91-48e97d62b181 | -1.2018 | -53.6366 | 2024-10-21 00:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| af4a15e8-cf59-365d-9df6-c88ab69d69c1 | -1.9395 | -52.1016 | 2024-10-21 00:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 771df26c-a45f-333e-942e-ac960c16b3e4 | -2.2199 | -50.4594 | 2024-10-21 00:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1c01808e-5688-3b1e-8bc6-cd683c7488fc | -2.2671 | -47.0775 | 2024-10-21 00:45:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 252c4943-be9f-3ef1-ba22-e50025f569e9 | -2.4824 | -49.1233 | 2024-10-21 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 4b1e20c1-e011-3b16-8f41-d2a7374da875 | -2.4824 | -49.102 | 2024-10-21 00:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| af731f5a-22cb-3665-b787-24514b048df3 | -2.7885 | -51.3618 | 2024-10-21 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 94439dd4-9d2c-373d-b5da-3747814c5392 | -2.8069 | -51.3613 | 2024-10-21 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4fd12bb2-a327-30a6-8baa-f6a322678066 | -2.8482 | -45.4637 | 2024-10-21 00:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 67ff00f4-2f89-3778-98bb-139dc01b8acb | -2.8372 | -53.3261 | 2024-10-21 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b8a90987-fad5-3340-a70b-55bf3689f9fe | -2.8667 | -45.4855 | 2024-10-21 00:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 24683d0f-1746-3520-999d-490d4212271e | -2.8668 | -45.4631 | 2024-10-21 00:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 8fd34254-85d5-374d-9b15-587847c44368 | -2.8556 | -53.3256 | 2024-10-21 00:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1d2cc555-cafd-361d-90bf-d42c89c4518a | -2.8864 | -45.215 | 2024-10-21 00:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8c94ab89-f284-3c19-a229-e07bf812c6a5 | -2.8865 | -45.1924 | 2024-10-21 00:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4475e1fc-b558-387f-8058-713e9f1c83e8 | -2.905 | -45.2143 | 2024-10-21 00:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 132.5 |
| fbcb30e4-10eb-36c4-8b50-daf6ba010d8f | -2.9051 | -45.1918 | 2024-10-21 00:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 4f138fc3-6886-37e1-b403-4cb8b7a85669 | -2.9236 | -45.2136 | 2024-10-21 00:45:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8e16f86d-13b6-3af0-a4d2-c52a236d58e6 | -2.9674 | -47.9931 | 2024-10-21 00:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5b200c6d-7edf-31c4-938a-257f5833b1b5 | -2.9852 | -53.0587 | 2024-10-21 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 08bc94e1-c748-3b30-8479-6d4445240200 | -2.9853 | -53.0384 | 2024-10-21 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1bf605c9-7d8d-38ce-b3f4-21a634b17559 | -3.0036 | -53.0583 | 2024-10-21 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d16c1064-2848-3ae4-a186-953c2005f5a4 | -3.0037 | -53.038 | 2024-10-21 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2182d435-cf06-33ef-8795-d3386d44c31c | -3.0581 | -53.2395 | 2024-10-21 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6be7362c-6be6-3082-b241-28a2ab4dce94 | -3.1138 | -53.1163 | 2024-10-21 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c0a79eca-4599-33c9-8c1a-1f325754ef20 | -3.1962 | -50.8099 | 2024-10-21 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 182b471b-607e-3066-8b54-e7f6e3f33d35 | -3.1963 | -50.789 | 2024-10-21 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 44bda44a-e365-3dea-b3ab-50695bc5ee1b | -3.2146 | -50.8093 | 2024-10-21 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 606c6d37-c025-389f-a072-d54584c718e0 | -3.2147 | -50.7884 | 2024-10-21 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 4dea5922-8877-3c97-8fc2-0a6c20ee3c84 | -3.7752 | -53.4012 | 2024-10-21 00:45:28 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fde067ce-5035-3d4a-b11a-12a9212a1519 | -4.8477 | -46.8847 | 2024-10-21 00:45:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f31fbefd-81d6-3a38-a075-5b20e6121c63 | -4.911 | -45.8374 | 2024-10-21 00:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 282d1063-35e2-31cc-9b00-a576508cfe23 | -5.6624 | -35.481 | 2024-10-21 00:45:37 | GOES-16 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 141834a7-d4c8-3f76-8712-756801262480 | -5.6627 | -35.4538 | 2024-10-21 00:45:37 | GOES-16 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 65.2 |
| b3c2041c-7320-39cb-b9f2-364133c1866c | -5.4904 | -50.5882 | 2024-10-21 00:45:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6602a6df-d369-30ab-af6a-d93bf84de0a0 | -5.6707 | -46.4363 | 2024-10-21 00:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 36ab07d4-6094-3a21-8e2f-624cb6e54d92 | -5.6709 | -46.414 | 2024-10-21 00:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 22d39f70-1bd2-300e-9274-06a3de1c5307 | -5.6894 | -46.435 | 2024-10-21 00:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 9fd71052-b4d8-3488-8f75-01251468b0bf | -5.6896 | -46.4128 | 2024-10-21 00:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 50a14227-f66c-3410-a307-dec582eb4c23 | -5.7081 | -46.4338 | 2024-10-21 00:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 155fa54c-e91c-34c3-adbc-be8e3e9ede79 | -9.3718 | -66.4891 | 2024-10-21 00:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 851dd804-3ec1-3a94-a2f4-61c5ad31ca5b | -9.7704 | -64.7174 | 2024-10-21 00:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| bb517da4-adfa-3e9f-9c48-0a2db9a83a6f | -10.1918 | -36.7236 | 2024-10-21 00:46:03 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 316e0c27-d8df-306f-ba1d-eb36a3a85e4b | -10.1923 | -36.6968 | 2024-10-21 00:46:03 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 69.7 |
| bc8c5ab5-fd47-306b-994a-1bcfe20a820b | -12.4778 | -63.1885 | 2024-10-21 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0e4899ea-4ffb-33ad-b440-3eaae57778a2 | -12.5147 | -63.3014 | 2024-10-21 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f9ebd1e4-1ef5-3660-9e02-d1d612afd4f8 | -12.5357 | -63.0319 | 2024-10-21 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7fc12f6b-779a-384d-844f-3bce18626cae | -17.6871 | -57.4387 | 2024-10-21 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 799e1fc7-2b20-3ddc-8ca3-2eb42353baf3 | -17.6875 | -57.4181 | 2024-10-21 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.4 |
| a54272a6-f75d-3825-850a-e6375bd7be6c | -17.7065 | -57.4569 | 2024-10-21 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 1ba3f9c2-73e9-39dc-b49d-111b53a65bbd | -17.7259 | -57.4751 | 2024-10-21 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| aaeeb7bb-10aa-39a9-9c16-70061996b36e | -17.7262 | -57.4545 | 2024-10-21 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 158.5 |
| eb3ab909-348e-3c24-8cb8-c4b79c02d6c8 | -18.263 | -56.1021 | 2024-10-21 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 0d1f08b0-752e-3df8-a8e0-1b09db2e3cc0 | -18.2828 | -56.0994 | 2024-10-21 00:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 213.0 |
| 4d4f7253-920f-357d-8342-b3caee593a85 | -18.2832 | -56.0785 | 2024-10-21 00:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 51a2eaf6-32e6-3aac-b9b0-e0b031a45dc2 | -1.2018 | -53.6366 | 2024-10-21 00:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 36e4a71f-2cbb-3082-9bbc-1b5070faebf2 | -1.9395 | -52.1016 | 2024-10-21 00:55:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 22c3a1f5-a91f-33fe-9083-55561b7bd052 | -2.2199 | -50.4594 | 2024-10-21 00:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9fc5b4d3-47ef-39a2-b060-895d7920509d | -2.2671 | -47.0775 | 2024-10-21 00:55:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 46c507d9-e051-3dfa-b1a7-0b081ea9089d | -2.464 | -49.1024 | 2024-10-21 00:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 28ac6888-445f-3687-a472-f5e9a0ce6be1 | -2.4824 | -49.1233 | 2024-10-21 00:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0e9aa306-48d0-3a4c-9b65-aa7293988e8f | -2.4824 | -49.102 | 2024-10-21 00:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 5491d63d-38f1-3c71-aeaa-5605ab0d1bf5 | -2.7773 | -49.3067 | 2024-10-21 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 58e162c6-1df9-3018-99f2-7185396d91de | -2.7885 | -51.3618 | 2024-10-21 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0e6af5a8-ad3f-3176-979c-4f55585e7122 | -2.8069 | -51.3613 | 2024-10-21 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ab92ba4f-4fc9-3fbd-b2c7-13dd513d0ce0 | -2.8482 | -45.4637 | 2024-10-21 00:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 489351e4-e6be-36c8-a18e-1d2953945c1a | -2.8372 | -53.3261 | 2024-10-21 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dd8bfa2b-8ce2-3bc8-8b74-5d2edd759c26 | -2.8667 | -45.4855 | 2024-10-21 00:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| dfc90e0e-797f-3c52-b2dd-7da7dbb19c3a | -2.8668 | -45.4631 | 2024-10-21 00:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e96cc873-6ee5-325e-b376-fd32087873bd | -2.8556 | -53.3256 | 2024-10-21 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a4bc982d-a478-3b1f-9186-b77561da23a8 | -2.8864 | -45.215 | 2024-10-21 00:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2d32c0b7-7fc0-313d-aa99-5a71b8d0aa74 | -2.8865 | -45.1924 | 2024-10-21 00:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 67d2fd6c-a55b-3d74-9ccc-51a6e2460acf | -2.905 | -45.2143 | 2024-10-21 00:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 133.6 |
| c83ce986-b6b2-38cd-bc12-d2f5f7c0dd4a | -2.9051 | -45.1918 | 2024-10-21 00:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b6febdca-af89-3cc9-882b-f574192e4543 | -2.9236 | -45.2136 | 2024-10-21 00:55:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 18686a2f-7d15-3b37-b63b-b3b568245c01 | -2.9674 | -47.9931 | 2024-10-21 00:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| eddd6a0b-c244-3bc2-be78-76544e89d5ac | -2.9852 | -53.0587 | 2024-10-21 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 68a04801-62e7-3f5a-9efa-1ebb5f8d05ff | -2.9853 | -53.0384 | 2024-10-21 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 14f11cd9-f488-3ab4-ac3b-ed55e6c5ba1a | -3.0036 | -53.0583 | 2024-10-21 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1e56c8a8-3018-3e62-b6f1-39e1c6629cbe | -3.0037 | -53.038 | 2024-10-21 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f75b74de-a600-3701-aad0-f6a1fdb0ff81 | -3.0581 | -53.2395 | 2024-10-21 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ec33bdea-2437-3f0c-a3b8-88576519f944 | -3.0765 | -53.239 | 2024-10-21 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9db75059-e52c-338d-84f9-3595e9913ebb | -3.1138 | -53.1163 | 2024-10-21 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ee1a5312-88af-3d62-a38a-1dfc288e2b1a | -3.1962 | -50.8099 | 2024-10-21 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 3a1882b8-edc7-39b5-9cc0-fd0082f838a8 | -3.1963 | -50.789 | 2024-10-21 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a27f4104-22d2-3246-9688-5959ee443f1c | -3.2146 | -50.8093 | 2024-10-21 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a6698d32-f1da-3095-8343-a48e15c6e096 | -3.2147 | -50.7884 | 2024-10-21 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |


[Clique aqui para ver as próximas entradas](README9.md)
