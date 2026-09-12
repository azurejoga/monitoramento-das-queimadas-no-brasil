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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f491390b-4d7e-329e-acdd-402a2a29cdec | -7.2571 | -46.6941 | 2026-09-12 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ef4037fb-21ab-34f9-9f6e-c6a59d64c163 | -11.3727 | -46.8074 | 2026-09-12 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 0b732719-94f3-3dbf-b85b-985d456a6fd0 | -11.3723 | -46.8299 | 2026-09-12 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 3ebef64f-9a21-3754-af5a-b6e8a614d3ad | -8.5415 | -54.7187 | 2026-09-12 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| f356ea1c-fe7d-3b6b-bf17-e5ed481159ee | -2.9394 | -50.4203 | 2026-09-12 12:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 436f1d99-0a80-3372-a8f2-67fb99d588ee | -2.9395 | -50.3994 | 2026-09-12 12:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 65918303-025b-3cbd-a478-310c00be5978 | -11.3723 | -46.8299 | 2026-09-12 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 173.3 |
| baeba269-fcaa-3f96-94e5-8e96e672e9bd | -2.9394 | -50.4203 | 2026-09-12 12:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f7657331-d2e7-3efb-9a36-6a4af53eef01 | -2.9579 | -50.3988 | 2026-09-12 12:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 9d52d893-30b8-333d-8b36-5ce964c737a1 | -6.708 | -45.4409 | 2026-09-12 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9c8eb186-31ca-3255-be84-64f165062df5 | -12.1388 | -48.9672 | 2026-09-12 12:40:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| e67e86c6-5b55-3296-9768-73ecad9e353d | -7.6008 | -46.1288 | 2026-09-12 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5fcceed0-99f1-3695-b9af-c0660d237ecd | -10.2933 | -45.2702 | 2026-09-12 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| f85e2139-7a29-33cf-a0b6-e34a4ad71f30 | -7.2147 | -43.7001 | 2026-09-12 12:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 3ac76273-bc5f-327e-b903-1263d7541f5d | -2.9395 | -50.3994 | 2026-09-12 12:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| de1a22d1-a2ee-3e63-8814-827d0281d05a | -11.3727 | -46.8074 | 2026-09-12 12:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 650053db-9bfd-3315-a660-b3aa9e4a1290 | -13.3192 | -51.6626 | 2026-09-12 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8ed01875-104f-38e4-bfbb-725e65cb80de | -8.5415 | -54.7187 | 2026-09-12 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 350ade21-d665-3514-906a-944c83110c24 | -10.2929 | -45.2932 | 2026-09-12 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ad9877f5-05d9-3d9b-8b68-a64bd1e6c041 | -7.2571 | -46.6941 | 2026-09-12 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5879407c-db12-3595-84a8-18364e551e8e | -7.0164 | -44.6413 | 2026-09-12 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 523eddf6-b044-3ca1-a3cd-59d78a71dd30 | -11.3727 | -46.8074 | 2026-09-12 12:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6e4d3c94-5fac-349b-9eb6-5f940a786de0 | -6.8752 | -47.4533 | 2026-09-12 12:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 07e92cbf-7bf2-3ce8-902c-e455addddb62 | -6.8755 | -47.4313 | 2026-09-12 12:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 151.7 |
| ba6b278d-233e-3d50-877d-cdf746431511 | -10.9491 | -48.3474 | 2026-09-12 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c15039f0-ffc6-3b99-8543-331318473f71 | -8.043 | -43.7565 | 2026-09-12 12:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 6b64ab4f-1e3f-394f-9cd1-1c584f107d4d | -2.9395 | -50.3994 | 2026-09-12 12:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 1a90cb6f-b5e8-34bf-82df-a33b8a7c0ad1 | -5.7754 | -45.1053 | 2026-09-12 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 45ac6818-bf3c-3e88-81f8-4427ba5eeef8 | -7.0166 | -44.6184 | 2026-09-12 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 5ab239cd-a71c-36f2-a811-8590c310e0da | -8.5415 | -54.7187 | 2026-09-12 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 220.7 |
| f85b1740-df01-3217-99c4-df1d8bc19c32 | -6.708 | -45.4409 | 2026-09-12 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 42bd84e3-bcc5-30a2-b3df-71418d1ca095 | -10.5664 | -51.356 | 2026-09-12 12:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 38c9d3dd-6c89-3f45-be39-1fc44db37ec6 | -13.3192 | -51.6626 | 2026-09-12 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 40924151-242f-3f63-b8df-131e32b76129 | -11.3723 | -46.8299 | 2026-09-12 12:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 5eba0c3d-4ba5-3aac-8da3-0ab63f699032 | -7.6692 | -46.7251 | 2026-09-12 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a6f82fba-b44d-3b9b-9144-dc949e4e2d4d | -8.5229 | -54.72 | 2026-09-12 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 4f825e86-879f-390b-b688-7cfa39e912fb | -12.1388 | -48.9672 | 2026-09-12 12:50:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 851be2bb-14dc-3ad3-a6ca-1db00d0e92eb | -12.0906 | -47.2709 | 2026-09-12 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 9b021bce-de6b-314a-9874-0a7790f633ed | -8.043 | -43.7565 | 2026-09-12 13:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 228.7 |
| f2ba5114-885f-3712-8b45-b7fa91afde9a | -8.5415 | -54.7187 | 2026-09-12 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| d382e0ee-2e4d-3c30-878d-8365cc8c3789 | -8.002 | -44.0163 | 2026-09-12 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e116ac3f-06d5-33b6-8c2c-b58ce61b2cd5 | -10.2926 | -45.3161 | 2026-09-12 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b05f9167-f7a7-35f5-bbb1-196ac3a4daa3 | -10.0622 | -45.4819 | 2026-09-12 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 670aef48-6a8c-3bff-adfb-102ec792b7c1 | -10.0625 | -45.4591 | 2026-09-12 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| db2c4be4-0401-3f07-b0bf-076e16307cf5 | -7.2571 | -46.6941 | 2026-09-12 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6e998410-5323-3af2-bdbf-c351788efb19 | -10.9495 | -48.3255 | 2026-09-12 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 817e7a18-1e56-36e6-8703-1e2dbd46a1b1 | -11.3723 | -46.8299 | 2026-09-12 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 512d1c08-855a-3f51-bd33-83fba9416027 | -10.2206 | -50.373 | 2026-09-12 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 1b133123-a8cc-31dc-8d0e-14c3a617a66c | -7.0164 | -44.6413 | 2026-09-12 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 31542da5-9a86-3c43-911e-f7d5ee113554 | -10.3472 | -48.022 | 2026-09-12 13:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ed2c9f5a-6aff-36ab-a13f-9d8747891979 | -7.1716 | -45.92 | 2026-09-12 13:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| df3fe090-813f-39b3-af18-4b7e762b77b1 | -12.1388 | -48.9672 | 2026-09-12 13:00:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 5981ac61-844b-3395-afeb-230d5f2234f2 | -10.2933 | -45.2702 | 2026-09-12 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0585ef1f-8213-3985-95aa-6aa6fe64082d | -8.0427 | -43.7798 | 2026-09-12 13:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 6b6b18fb-54b5-36e6-854b-57901932d5c7 | -10.9491 | -48.3474 | 2026-09-12 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 4ff5566e-ddc2-38fc-bc36-e24623f12668 | -7.6692 | -46.7251 | 2026-09-12 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| ebc2b701-63b4-374d-a474-3fb52eccd4bf | -7.6008 | -46.1288 | 2026-09-12 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 452890b0-34ac-38bc-bab7-f226153385e6 | -7.2147 | -43.7001 | 2026-09-12 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| db3f4dfc-3b49-312e-ab82-a9a218d64d67 | -11.3727 | -46.8074 | 2026-09-12 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 43e69c52-1918-35f8-8269-6d2f9e67e687 | -5.7756 | -45.0826 | 2026-09-12 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d90f2c82-942b-39d6-a547-2709de01ab14 | -7.1901 | -45.9408 | 2026-09-12 13:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 3c13858b-a207-384a-826e-d6d3c283343a | -12.1391 | -48.9453 | 2026-09-12 13:00:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8b301996-f98b-3d16-bf40-60456cad9e6c | -7.1903 | -45.9183 | 2026-09-12 13:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b31d4218-d699-3ad5-bc84-e29dbb7f27d9 | -8.5229 | -54.72 | 2026-09-12 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 05334b7c-05b3-3700-bba5-41e58eb6d2e3 | -10.2929 | -45.2932 | 2026-09-12 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f795f7c4-a92d-3280-806f-b48221cacb34 | -7.1713 | -45.9424 | 2026-09-12 13:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 91c00352-f5a8-3181-9010-59e4e66238ae | -6.8567 | -47.4328 | 2026-09-12 13:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 82b546cf-7e62-3b7b-a3d1-35fbd0be33d0 | -10.5664 | -51.356 | 2026-09-12 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| c2fd7ea7-2eba-34ca-b464-87a2cf9b0368 | -12.0906 | -47.2709 | 2026-09-12 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 21a23292-ecf3-3381-a248-2bf3cfcf50b1 | -7.0166 | -44.6184 | 2026-09-12 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 289.4 |
| 4ec0bc0f-106f-3f01-b2ee-7bc3744491b6 | -10.2171 | -45.2799 | 2026-09-12 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 074c5633-579c-3687-8455-b5edd2bc6839 | -7.2147 | -43.7001 | 2026-09-12 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 375.1 |
| 2542ffb0-8aaf-304f-a4da-43eb2551e75f | -10.2933 | -45.2702 | 2026-09-12 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 4603acfd-58c0-37d0-9d9d-66611b793480 | -11.3723 | -46.8299 | 2026-09-12 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 8d0fbf88-a3c6-324e-b99b-8172f7293469 | -11.3513 | -45.7922 | 2026-09-12 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 2e4b8bb1-2b39-3af5-a944-b2fc5f21c6c5 | -7.0164 | -44.6413 | 2026-09-12 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 9d927237-3e4b-38b5-9d18-c8bfefc0d0e3 | -12.1388 | -48.9672 | 2026-09-12 13:10:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| de1e9d5c-189a-3f52-8dfb-49c19a118ad2 | -7.6692 | -46.7251 | 2026-09-12 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 4e64b31f-12dc-36b4-a5e4-de02eb2d57d0 | -11.8193 | -46.3633 | 2026-09-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| cf8f1e0a-d4e3-374d-872c-439ab4d4dec2 | -8.5415 | -54.7187 | 2026-09-12 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 6b4d1730-f10f-3c43-8919-2328183b8e73 | -10.2929 | -45.2932 | 2026-09-12 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 1b67ac76-39e4-32e5-944a-787554efb9af | -11.372 | -46.8524 | 2026-09-12 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b7958543-a89d-3d4c-970b-385a0eea55c6 | -5.7756 | -45.0826 | 2026-09-12 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a2ba9077-5c8d-383a-9946-4dbf45423a00 | -7.0166 | -44.6184 | 2026-09-12 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 358.4 |
| c0be3e1a-b6cd-32e5-a073-3e2a9b3a015e | -10.9491 | -48.3474 | 2026-09-12 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 3a197d2b-4956-3d02-b190-b9cee06f3c0b | -7.6008 | -46.1288 | 2026-09-12 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 564f28de-3aeb-3870-8acd-50e500789c32 | -10.9495 | -48.3255 | 2026-09-12 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2f796e58-4d3c-34b3-8134-cd3162396f8e | -12.5969 | -53.9854 | 2026-09-12 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 730bd790-935a-3319-a01c-ed15c7996d77 | -8.043 | -43.7565 | 2026-09-12 13:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 634d8bca-f4d3-3a11-baed-adba6759cb86 | -10.2206 | -50.373 | 2026-09-12 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f856f944-7fd0-3696-91cf-7d1bfbfb3861 | -13.3192 | -51.6626 | 2026-09-12 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9783d2fe-7e27-3b34-9638-87ba5a85260b | -7.2571 | -46.6941 | 2026-09-12 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b8292d0f-7be7-3e8c-976b-315e2a69b706 | -10.5664 | -51.356 | 2026-09-12 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 1e1de30d-bffc-3438-97c9-eb294e879de3 | -8.5229 | -54.72 | 2026-09-12 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 46dea9b0-5216-3011-851a-7717c0609690 | -11.3727 | -46.8074 | 2026-09-12 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| bf40636e-27b1-340e-b473-9f4281f52333 | -7.0164 | -44.6413 | 2026-09-12 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 246.4 |
| 902b8b98-756a-35ec-b055-fddeef3268fc | -11.3731 | -46.7849 | 2026-09-12 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| a43d3749-2a80-319b-8e13-0f22acccfe18 | -11.7997 | -46.3887 | 2026-09-12 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 4dfa2047-c941-3ba6-8f6f-312f833aed74 | -7.6692 | -46.7251 | 2026-09-12 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 94182964-3a2f-3b21-acf7-28b71857bb82 | -7.0166 | -44.6184 | 2026-09-12 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 386.3 |


[Clique aqui para ver as próximas entradas](README59.md)
