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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a66221f9-acb2-3e9b-afea-93be132ebabd | -3.4225 | -44.389999 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbe58788-3d81-3043-b51f-de19588a830b | -4.1726 | -45.620201 | 2024-11-20 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12a364f9-79fe-3e05-a2b5-9cc805df588c | -2.8895 | -53.031601 | 2024-11-20 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8c8d727-ec0b-3d97-9e7e-2e14f577c2a6 | -4.5399 | -48.016701 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8675cd6f-ddf9-3dfd-a2d2-390c86db9734 | -7.6109 | -43.679501 | 2024-11-20 00:09:00 | METOP-B | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b69751f2-0fea-3f44-9ebb-7a39a1888eca | -11.0509 | -41.610901 | 2024-11-20 00:09:00 | METOP-B | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 580fd3fe-6170-3ceb-b2e4-bda54712195f | -2.9426 | -48.317402 | 2024-11-20 00:09:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53277961-1fe9-3a5f-b27f-55e3457f1d92 | -9.157 | -44.709202 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 379a64ec-f4b3-33f0-a51b-5b701130582e | -0.9286 | -51.7015 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 506f3308-f5be-34de-b65f-f35f62c25535 | -3.569 | -43.623901 | 2024-11-20 00:09:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29e54ef4-a42f-39cd-9d71-e1eb95d0bb9a | -2.5089 | -45.000301 | 2024-11-20 00:09:00 | METOP-B | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb94d6a3-49a4-3fa3-80fc-221cba651555 | -3.5674 | -43.617001 | 2024-11-20 00:09:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 829037fe-9269-304c-8ff4-68ca728b528f | -12.26 | -43.523201 | 2024-11-20 00:09:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 383cb229-9920-3976-97c7-778ce2b69a27 | -3.5788 | -43.6217 | 2024-11-20 00:09:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2b6d924-d282-3588-8596-9e687da711b1 | -3.1054 | -49.143299 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffb0f46-0e63-34b0-a797-571ebdb3c41e | -0.2873 | -51.5383 | 2024-11-20 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 31fbccdb-5457-3658-afed-6f8530c051cb | -4.1682 | -45.5195 | 2024-11-20 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 234.5 |
| 3a70ad15-1047-330c-bb5e-570d16e0375b | -11.1106 | -54.6408 | 2024-11-20 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0326a6c5-6e15-3ca3-b5d0-c505260546db | -4.0671 | -46.8586 | 2024-11-20 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| cbe79b94-d9e6-36c5-8291-f873a133034a | -3.3131 | -45.4013 | 2024-11-20 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 144.5 |
| f7d5e0eb-e60e-3766-9e72-b345894d27d6 | -3.3024 | -43.8314 | 2024-11-20 00:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ed9c4b14-a21c-350a-8eeb-b561306a3c18 | -3.3088 | -50.3671 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 05b60fb1-1fb8-32dd-93e0-c5de75361435 | -2.9115 | -53.0809 | 2024-11-20 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a8e54db1-109a-3f6d-b129-92c875b32d20 | -11.1109 | -54.6204 | 2024-11-20 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9951f775-332a-350c-9642-72bb08195e41 | -2.9968 | -45.4584 | 2024-11-20 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 134.1 |
| c54f54fa-de89-3f40-a56d-f72790034c4b | -9.6598 | -36.361 | 2024-11-20 00:10:00 | GOES-16 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.0 |
| df528f6f-63e6-30c1-9a63-fe17cff2d75a | -4.5614 | -48.0141 | 2024-11-20 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 367ad225-dc75-3ef9-b9e3-1b3554fb7868 | -4.1868 | -45.5186 | 2024-11-20 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d154222d-70f6-3974-bdf3-d76cf71c1f7d | -2.6213 | -51.7791 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1ff1e38f-7938-3105-941b-ee6a9a064913 | -4.5429 | -48.0151 | 2024-11-20 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c44c6d1f-5fcd-3a76-bea0-bb1cc7304b90 | -3.3026 | -43.8083 | 2024-11-20 00:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 645ae261-49eb-3df7-bb31-41ca8bf51736 | -15.3025 | -56.5268 | 2024-11-20 00:10:00 | GOES-16 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 7ec3a4fc-2a48-30e8-af75-d58a1394359f | -2.75 | -51.8377 | 2024-11-20 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8452a555-9d43-3496-b72c-aa18af8335ad | -4.0672 | -46.8366 | 2024-11-20 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7c694268-108c-3ebc-91c2-52a28cade327 | -3.0109 | -51.0236 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b5c02957-a72a-31c6-af44-ec0e8c77f00c | -4.1594 | -43.9739 | 2024-11-20 00:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 14a04610-5674-34aa-b719-3a481e6099ee | -2.7501 | -51.8171 | 2024-11-20 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4d7cf098-9475-38bb-ba45-7a42f77cf9e0 | -4.459 | -46.5966 | 2024-11-20 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9252b1d8-58ac-3fe6-9d65-aec0b1509320 | -4.5616 | -47.9925 | 2024-11-20 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 2c17affb-b0c4-37a4-b85a-9727575b2cf3 | -2.9969 | -45.436 | 2024-11-20 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 362.6 |
| 845dbf98-8b7e-35a9-880e-3092d5d70123 | -2.9117 | -53.0403 | 2024-11-20 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d3772be7-d59d-35af-8e08-1d2be1d5be94 | -3.3212 | -43.8075 | 2024-11-20 00:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 53abd020-2f34-3b5f-95b9-8519c7a445a9 | -14.3409 | -51.5092 | 2024-11-20 00:10:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 20f0240a-cfde-3e19-a3cd-e061c6b5cb9e | -2.9116 | -53.0606 | 2024-11-20 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 0c001d1e-f70c-3d93-a4b6-9f01ff4d1432 | -3.0155 | -45.4353 | 2024-11-20 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 625a3d0e-b4cf-3a0e-b5a7-a6342e98f458 | -3.0355 | -49.4476 | 2024-11-20 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9a99bb91-3cf4-30a1-9515-bc76e1a65f17 | -2.6212 | -51.7997 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 115d094b-fe4f-32f9-b508-dded0f7c0fff | -4.1497 | -45.498 | 2024-11-20 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 4c6850ae-2752-3187-a94e-5a9648cbca16 | -16.8816 | -57.5131 | 2024-11-20 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 6aa45242-9ade-37bd-8f3c-37c4406f68f4 | -4.2528 | -53.6684 | 2024-11-20 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 8a94c317-53cd-3678-95c0-31883ee20cfc | -3.1477 | -49.1251 | 2024-11-20 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| f2c78cd7-8933-37e5-b5b0-7f59ef761ae4 | -3.3211 | -43.8306 | 2024-11-20 00:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 171.2 |
| f8153adf-481f-32f5-9f02-86c5ce1c8f75 | -3.1291 | -49.147 | 2024-11-20 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4395ddae-ac99-3465-9858-564233838375 | -4.1861 | -45.6308 | 2024-11-20 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 6d62dc4f-aec9-31bc-844d-99e84cf1e572 | -14.3413 | -51.4878 | 2024-11-20 00:10:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| d4f11383-756d-36d0-b9f8-ea9b874bd725 | -4.1683 | -45.4971 | 2024-11-20 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 203.9 |
| c6d01bfc-bf9b-3d42-bf62-fac8ea0d154f | -2.6028 | -51.8001 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ffde0ad8-5d9c-3ac8-b3ed-8d3111dbff83 | -2.6212 | -51.8203 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5cacec0c-0930-3824-9587-ced8a8d89b7f | -3.011 | -51.0028 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| b9d8ac88-c2a2-33f7-8e2b-1f8dff0af5ea | -3.7858 | -44.0622 | 2024-11-20 00:10:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| a5407d7e-6a59-3726-a810-94635f8d1bc6 | -4.1495 | -45.5205 | 2024-11-20 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 23a17ce2-938e-36e8-b886-fe21e53d5c1e | -3.8205 | -47.8096 | 2024-11-20 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fa622600-bd22-3763-bda4-90ff76758f42 | -0.947 | -51.724 | 2024-11-20 00:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1d5c6511-ebea-3630-8d3f-3ce19d053bad | -3.802 | -47.8104 | 2024-11-20 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 977fc64e-0135-3ca5-a9bb-ad53d9ef3987 | -2.7217 | -49.3508 | 2024-11-20 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 388fc8e1-496f-31fd-9127-f6a2ccdf5b51 | -3.1292 | -49.1257 | 2024-11-20 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 3c8794b7-8d77-3e9e-8bd0-4d675a7d919a | -3.2708 | -50.6196 | 2024-11-20 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 35def491-3c94-39f7-ad62-48555cd6ed55 | -1.4524 | -47.1166 | 2024-11-20 00:10:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| d6d76497-f239-3fd5-8cc3-117e5eed1273 | -5.4015 | -45.1313 | 2024-11-20 00:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4127d040-c769-3ec8-9616-869207ee7a08 | -4.4592 | -46.5745 | 2024-11-20 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 54d41ecb-a2fe-35ce-914b-d853bbe8a00f | -4.4405 | -46.5754 | 2024-11-20 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 039db0f2-756f-3f55-92cc-e32b8edf5489 | -3.313 | -45.4238 | 2024-11-20 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 4a861658-6042-3e45-ad5a-9d826e7e6913 | -4.4404 | -46.5975 | 2024-11-20 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| dfe19702-d22a-3956-94d1-68ec4cdda332 | -3.2014 | -54.3243 | 2024-11-20 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| a8b97989-ff89-3cbf-9ce0-c5a84359bb35 | -4.4592 | -46.5745 | 2024-11-20 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f15692fc-bdcb-32d2-9334-1c6dbda5ac08 | -11.1106 | -54.6408 | 2024-11-20 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 616d824a-f5eb-319d-9497-244c6b3936d8 | -0.9654 | -51.7238 | 2024-11-20 00:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fee057fd-790a-34a8-bb4a-ec4bb145ef71 | -3.3088 | -50.3671 | 2024-11-20 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 99e41702-4cdf-3c89-b9e3-50a7dc52196f | -3.8205 | -47.8096 | 2024-11-20 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 95ad7bf7-21ca-3c3e-a28a-2cfcb6d87d55 | -11.092 | -54.6221 | 2024-11-20 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a6642138-c541-32d2-b58b-a70fac0bbf45 | -3.8021 | -47.7887 | 2024-11-20 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 156c83bd-b01b-3379-94bd-f220d3fcf1b8 | -3.2014 | -54.3243 | 2024-11-20 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| c342c02e-a632-3514-952f-1ad686d1a8d7 | -4.5614 | -48.0141 | 2024-11-20 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 49e40d19-c06a-372e-a531-729508e2dfb7 | -3.1292 | -49.1257 | 2024-11-20 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 86e8ab21-5f02-353c-8158-3919db4a1cee | -4.4404 | -46.5975 | 2024-11-20 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 0fca0863-66bd-3168-964c-7cbc13e31565 | -4.2528 | -53.6684 | 2024-11-20 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a484e841-2749-3733-8c90-f2e5a67b6ae9 | -4.58 | -48.0132 | 2024-11-20 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 49498f58-0cf7-3849-a6d8-162d0ec5c41d | -4.5429 | -48.0151 | 2024-11-20 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 87abecbe-0242-3a54-ac9d-328b0e4030b0 | -4.0672 | -46.8366 | 2024-11-20 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e0494c89-878d-320b-8dc1-4cf07988ed58 | -3.8206 | -47.7879 | 2024-11-20 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 9f2a8558-4138-30df-bf97-a33a6b8cbdc8 | -15.3025 | -56.5268 | 2024-11-20 00:20:00 | GOES-16 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ee67122a-f453-3fea-8d23-7daf873b2edf | -2.9116 | -53.0606 | 2024-11-20 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| dffec32c-c7c7-3488-bad8-f31078db8cef | -2.831 | -45.1267 | 2024-11-20 00:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 100f17ab-2ffc-3220-baad-d7f7cd0a91b2 | -9.6598 | -36.361 | 2024-11-20 00:20:00 | GOES-16 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| ff520457-830a-3b71-916c-284a0228c09e | -2.4204 | -45.6343 | 2024-11-20 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 89fa97a9-6501-3ffb-8a9f-60a4e3c7e3f2 | -3.011 | -51.0028 | 2024-11-20 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b85e8d74-5ab6-35d8-93c4-95f49e258fc0 | -4.1683 | -45.4971 | 2024-11-20 00:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 11741e81-e57a-36e5-9694-3414d8fdf698 | -4.1594 | -43.9739 | 2024-11-20 00:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 07e01cb0-20ab-3b7d-b350-17aeb21c7df9 | -3.0155 | -45.4353 | 2024-11-20 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 518b63e3-44b3-3a65-bc3d-9d896c62debb | -3.1477 | -49.1251 | 2024-11-20 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |


[Clique aqui para ver as próximas entradas](README8.md)
