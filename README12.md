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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c27f879-de30-3fa5-a631-69ea164a4cea | -8.5907 | -51.5955 | 2025-06-23 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| d4bad576-442e-3f7e-a013-9d6a36ea2281 | -11.2702 | -52.4605 | 2025-06-23 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 3d3a31cd-779e-3b3b-bda4-6343060bbe41 | -11.5812 | -44.6554 | 2025-06-23 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| b877374c-c9d5-3c05-98bf-e7d300e13603 | -8.5722 | -51.5761 | 2025-06-23 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f5b3acff-829c-3114-8852-2aa9cf717a9a | -8.051 | -43.1237 | 2025-06-23 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 378fc10a-a33f-3308-84b6-0f57f2cd714c | -8.5911 | -51.5537 | 2025-06-23 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f7bfec48-53d8-3bd7-98b0-704fed1d38a5 | -7.457 | -45.5568 | 2025-06-23 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7b5a7c5a-0dae-33ab-a7e2-90d2280fe395 | -7.4758 | -45.5551 | 2025-06-23 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 166a0b94-16da-3b25-a8be-c0bf807673d1 | -8.5909 | -51.5746 | 2025-06-23 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 322.1 |
| 50c8c7a8-98e9-3e50-ae55-d1ef517ee8db | -8.0703 | -43.0981 | 2025-06-23 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 314.0 |
| 16393462-98fa-34e4-9d36-8bf6cc654caa | -11.2702 | -52.4605 | 2025-06-23 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 5b375f9e-e35b-3319-91d7-155239c33960 | -8.0703 | -43.0981 | 2025-06-23 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 371.6 |
| 168ac7f4-46f8-39b1-9788-17deb1b20ad4 | -8.5722 | -51.5761 | 2025-06-23 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| aeeaba64-a89c-3f22-8e67-b6bd35421132 | -8.051 | -43.1237 | 2025-06-23 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.3 |
| d5a9a887-47e9-37ca-8f8f-ef211ccf9f4d | -8.5911 | -51.5537 | 2025-06-23 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e28efbca-f58a-3d12-b446-447282561b3c | -7.457 | -45.5568 | 2025-06-23 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 5c5d367d-253b-3efa-8a0c-d58eb517d489 | -8.5909 | -51.5746 | 2025-06-23 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 358.1 |
| fd202ff9-7984-38ed-846f-b1cdf3388c20 | -8.5907 | -51.5955 | 2025-06-23 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| e2135a13-acf5-39db-8fd9-3de5e7782669 | -7.4758 | -45.5551 | 2025-06-23 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| d75a7c98-9456-3727-99d9-14ec283037f9 | -8.07 | -43.1216 | 2025-06-23 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 383.0 |
| 87841d1b-662b-300a-99e4-47806a0b9304 | -11.2699 | -52.4814 | 2025-06-23 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4df9c459-1aa5-315a-82b6-095abe709644 | -8.07 | -43.1216 | 2025-06-23 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 339.7 |
| 2f196bef-8c7c-35e9-babc-f586ab947648 | -8.8006 | -45.0128 | 2025-06-23 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4cc83ea3-15c0-3df3-86e7-e7f507b8be35 | -11.2699 | -52.4814 | 2025-06-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| bd58ca30-6cf8-3bd5-bcf7-7506fdb1b7f9 | -7.457 | -45.5568 | 2025-06-23 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 6caca2c8-ea7e-39cd-8819-e1cd04dfdb92 | -8.5722 | -51.5761 | 2025-06-23 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c9c1b2ae-ebcf-3464-be8d-e552b9e8e769 | -8.0703 | -43.0981 | 2025-06-23 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 378.9 |
| d2fc3ca4-23cd-3ce1-b210-07e21f4a5565 | -11.2702 | -52.4605 | 2025-06-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 15901bd0-758b-3f07-9d37-7e31702119ce | -8.5909 | -51.5746 | 2025-06-23 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 306.6 |
| 88b983b0-ad10-3417-8e6c-6ac29f398c76 | -8.5911 | -51.5537 | 2025-06-23 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d899eedb-282c-3993-82ba-b884cc73bb7a | -8.0513 | -43.1001 | 2025-06-23 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| a7e80644-1049-3930-a5c5-04906ecc478a | -8.5907 | -51.5955 | 2025-06-23 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| a20f17f1-b1a3-38a0-8dcf-e5b7f41f4459 | -7.4758 | -45.5551 | 2025-06-23 13:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d15f240b-9659-36b0-9914-ec765029b963 | -17.6708 | -46.8347 | 2025-06-23 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.8 |
| af568d6a-638d-3e7b-908a-bbf9d995945a | -8.5907 | -51.5955 | 2025-06-23 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| dd8cbd4f-63a8-3034-96da-4928a076a51a | -11.2702 | -52.4605 | 2025-06-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 179.3 |
| f42e1226-b25d-3025-9b00-ac4b1a929af7 | -8.5722 | -51.5761 | 2025-06-23 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 30114d46-1e05-3325-9c70-02fa14bd53ec | -8.5909 | -51.5746 | 2025-06-23 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 9b1f8b14-1afe-3691-af9a-28065aa9fc23 | -11.2699 | -52.4814 | 2025-06-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 8614c70f-6520-32d3-a960-386307ca9f3a | -7.457 | -45.5568 | 2025-06-23 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b652efa2-8d98-3d27-b925-565d544c5b0e | -8.5911 | -51.5537 | 2025-06-23 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4dd35cb9-2097-3494-b966-8a0fb0f3718a | -8.5907 | -51.5955 | 2025-06-23 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 59fdb74c-2376-3b8d-97af-a27c24e4f627 | -8.5911 | -51.5537 | 2025-06-23 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 96e42383-2c8c-34cf-804e-9c7530b1a75e | -8.5909 | -51.5746 | 2025-06-23 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 242.4 |
| 46d5c3c3-350e-3811-aa4e-061ab6a15b58 | -8.051 | -43.1237 | 2025-06-23 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.9 |
| 960a5bcc-de77-33c2-8c2d-124e81137b59 | -11.2699 | -52.4814 | 2025-06-23 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b2121dbd-aa39-3fc2-ac95-46f2e643500c | -7.4758 | -45.5551 | 2025-06-23 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e8df1734-2795-347c-9e50-9b63c8d05556 | -8.5907 | -51.5955 | 2025-06-23 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c2e8cfa1-b87e-3cbf-b06e-f12e4b6152e7 | -8.051 | -43.1237 | 2025-06-23 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| c59f70f9-9ac8-335d-b644-4fa964ffe6db | -8.0703 | -43.0981 | 2025-06-23 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 208.2 |
| 7a0b10bf-b055-3e56-96c0-21d7ef2ff65a | -8.8006 | -45.0128 | 2025-06-23 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| cec3c88a-e7c3-3b30-b8d9-c4616ebae9ba | -10.8571 | -53.7631 | 2025-06-23 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4309cbe0-a68b-32f2-8041-eaf6cc2f334e | -5.9522 | -44.1787 | 2025-06-23 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 3d7c1d6c-ba1b-37c1-8f1d-74494c5d7b04 | -11.2699 | -52.4814 | 2025-06-23 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8a50cb1a-def6-358f-8ae7-033fd3c31dfe | -8.0513 | -43.1001 | 2025-06-23 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| 6494bacc-b6bc-3fa1-9e59-b47d0297b857 | -8.5909 | -51.5746 | 2025-06-23 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 213.6 |
| 38d1cb9a-0aa9-3b86-9941-641f826a5b7e | -8.5911 | -51.5537 | 2025-06-23 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 3d2d7769-66d0-3e15-a883-d46ce60259e7 | -8.5911 | -51.5537 | 2025-06-23 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b2c1dfec-613c-3c1b-82c9-2690b9139c80 | -8.3746 | -47.4348 | 2025-06-23 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 852f2bed-ac0b-3b03-b012-3af19e5d9bfc | -11.2699 | -52.4814 | 2025-06-23 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d62e3cf3-0066-3abf-96ca-262e310a9af2 | -7.457 | -45.5568 | 2025-06-23 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 8a1b5345-2d02-3fb4-be51-82568e51f74f | -8.5909 | -51.5746 | 2025-06-23 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 0668a7ed-631e-3172-9913-c5b3430aa56b | -7.4758 | -45.5551 | 2025-06-23 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 6301f8e6-b85e-353f-aaa6-a8361cc29024 | -5.9522 | -44.1787 | 2025-06-23 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 983af4e1-0d8a-3db4-9648-6603ce0731ef | -8.5907 | -51.5955 | 2025-06-23 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 72bb7338-b099-3eea-884a-8ee64c621d44 | -8.0513 | -43.1001 | 2025-06-23 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.7 |
| 44b190b8-2e24-341c-bbeb-718d542dd091 | -10.8571 | -53.7631 | 2025-06-23 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8dfd23f6-d626-3d54-85d7-a02cbd99980b | -8.5907 | -51.5955 | 2025-06-23 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 37211665-0ae2-3af4-b668-83ec82d62275 | -7.457 | -45.5568 | 2025-06-23 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 286bd90f-e797-35db-85f5-3909036023c3 | -10.8571 | -53.7631 | 2025-06-23 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3cc7703d-1bbc-3a4c-a72d-3d5b2adc433f | -8.5911 | -51.5537 | 2025-06-23 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b233fb47-59cb-3cfe-b64f-9c1d261ba4bc | -7.4758 | -45.5551 | 2025-06-23 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f5a04a99-23d2-3418-99c5-c6bdcbb9c1a7 | -8.5909 | -51.5746 | 2025-06-23 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 180.4 |
| ae9bb44c-dee0-3032-abab-1a6629a07e8b | -11.2699 | -52.4814 | 2025-06-23 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| f331891c-5d23-3a3c-a6b6-96efe8cf4159 | -5.9522 | -44.1787 | 2025-06-23 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |


