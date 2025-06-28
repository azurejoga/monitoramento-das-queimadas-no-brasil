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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e36fb655-bbbc-3b61-92e8-6135c95de30b | -10.8382 | -53.7648 | 2025-06-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e1b809ab-7602-36cb-a8b3-b39711e5c86d | -10.8385 | -53.7442 | 2025-06-28 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6e464fc8-4bad-3a90-a382-b2b91a59d38d | -6.892 | -43.9851 | 2025-06-28 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| d3f5388f-9ed4-3ccc-b09c-13a5aac1b606 | -8.5722 | -51.5761 | 2025-06-28 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fb0b7200-6b5a-3607-8d21-976068cf7c5d | -7.2219 | -43.0682 | 2025-06-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 244.6 |
| 29f09491-0d89-39c1-9cca-1a440a7d6355 | -9.1393 | -49.4941 | 2025-06-28 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8e39565d-7407-34ad-af83-8995b9c360e0 | -11.2664 | -52.7527 | 2025-06-28 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 368.3 |
| 0230c355-92d2-3e30-8590-16f30ef46fa5 | -9.1205 | -49.4958 | 2025-06-28 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 243.4 |
| 041b9f63-6ba3-3791-8d1b-49a6d96c712e | -6.9108 | -43.9834 | 2025-06-28 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 189.1 |
| f089a189-7330-3730-a7f1-efafcb5fbceb | -11.0646 | -55.3555 | 2025-06-28 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6ac870ed-1c55-3a09-946e-e1455f9d425e | -11.2666 | -52.7318 | 2025-06-28 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| d55b7e4c-33eb-396b-8aa7-529ed719a19f | -11.2661 | -52.7735 | 2025-06-28 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| fcd03143-4288-36b9-ac81-a62d026a25a2 | -9.7041 | -56.1843 | 2025-06-28 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 20029472-b667-3911-8c92-4dde2e96faa9 | -12.2527 | -46.754 | 2025-06-28 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 84607a7f-8bd6-3e6f-bbbe-599d422aefa5 | -4.5429 | -48.0151 | 2025-06-28 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 51985abc-2911-3dbc-b6b8-a0a9ce91729d | -11.0266 | -55.3789 | 2025-06-28 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| adfefa02-6884-33f7-bf27-a83506d77b6d | -7.2405 | -43.0899 | 2025-06-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| f13ef80e-c04d-3fe9-aa44-b0aa1e9a117e | -7.2217 | -43.0917 | 2025-06-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 234.4 |
| 566a2eee-0733-3c16-b55b-7845e14437a8 | -9.1208 | -49.4743 | 2025-06-28 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 188.7 |
| b6d61e84-a386-3c52-b10e-21647e113978 | -11.0457 | -55.3571 | 2025-06-28 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 199.6 |
| 7e2159b7-8095-36c5-a0fe-5ad000877df7 | -11.2853 | -52.7508 | 2025-06-28 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 210.3 |
| bce4c0b3-9874-3106-b294-4318156cec1d | -11.0455 | -55.3773 | 2025-06-28 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 597.1 |
| 3fd31d8d-8ada-3ec8-98e8-de955c886e27 | -11.0644 | -55.3757 | 2025-06-28 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 223.9 |
| fa876bb9-0f1b-37a0-b4b6-a69a31514cd2 | -11.5779 | -52.115 | 2025-06-28 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| dec574c6-9bc6-34f0-b5f7-499e92ce5930 | -11.0453 | -55.3976 | 2025-06-28 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 98fc7453-73a7-345a-8cd4-40717d77bec8 | -9.7228 | -56.183 | 2025-06-28 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| a6cf4044-f44d-39d0-9399-0a5230ce4684 | -12.2523 | -46.7766 | 2025-06-28 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 53842e96-190f-3eba-acc4-aef8f2facfb3 | -9.1017 | -49.4976 | 2025-06-28 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| da17363b-b872-34ea-8006-76c6936b1b70 | -7.2028 | -43.0936 | 2025-06-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 9d2962c2-b7cb-30ad-9ee7-d531cd567817 | -12.2715 | -46.7739 | 2025-06-28 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8ff5c275-8296-3ace-9a81-03f7a5a2c39c | -9.102 | -49.4761 | 2025-06-28 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| d5417f39-37de-37a6-b0e7-e2181c0053ed | -11.2856 | -52.7299 | 2025-06-28 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 54d7051a-5439-39bf-8ac4-5c0e96810039 | -7.2408 | -43.0664 | 2025-06-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| f0ecb908-f14c-3071-a611-fd6016b59f9f | -7.2031 | -43.0701 | 2025-06-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.3 |
| d3d18309-ab87-3373-b304-d121158ae197 | -6.8922 | -43.9619 | 2025-06-28 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c0b901ba-b7b6-3bde-aa9d-e4d02fb025ce | -6.9416 | -42.8834 | 2025-06-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| e42c6586-e497-3150-a398-fed421135848 | -4.5427 | -48.0367 | 2025-06-28 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 56c3738f-8fe9-3edd-897e-90cc42f4c075 | -6.911 | -43.9602 | 2025-06-28 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b8a3f9ef-5102-3a2b-9338-11bc7f819a22 | -12.2719 | -46.7513 | 2025-06-28 00:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| ea961731-d2bd-38c1-b05f-69e756e87cfb | -7.2217 | -43.0917 | 2025-06-28 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 272.8 |
| 73c20df7-78ad-3813-90c7-3822f92ea799 | -10.8385 | -53.7442 | 2025-06-28 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 08b84559-dbbe-33b5-8795-f798ab34293c | -6.9105 | -44.0065 | 2025-06-28 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d1007fb4-715c-30f5-812a-49c5c31cbea4 | -9.1205 | -49.4958 | 2025-06-28 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 348.6 |
| 5ff4b53a-ae9c-3996-a179-e13845fe8f0b | -7.2028 | -43.0936 | 2025-06-28 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 59afc428-9994-3569-bb6a-ce68e88612fa | -6.911 | -43.9602 | 2025-06-28 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| c6c8fc1e-6b50-3d78-87e9-99264c20eaa8 | -12.2523 | -46.7766 | 2025-06-28 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a9654995-c1aa-3911-ada2-9ffe6d39e825 | -9.1017 | -49.4976 | 2025-06-28 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9cc2b12b-eb88-301c-b45a-37c1c42c3050 | -11.2661 | -52.7735 | 2025-06-28 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 56d8c7fe-a1ef-3d59-a369-33d2d6b7d012 | -12.2527 | -46.754 | 2025-06-28 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 33946e1e-e159-3594-a5c9-055a833bf135 | -11.2856 | -52.7299 | 2025-06-28 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ac84cdae-6887-32ec-bea5-1e49f36f4f35 | -9.102 | -49.4761 | 2025-06-28 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 6db9fb93-f7d8-391c-a391-117335a5fe90 | -11.2664 | -52.7527 | 2025-06-28 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 216.6 |
| db0147e4-bc49-3068-b1d4-e7cd867f9451 | -11.2853 | -52.7508 | 2025-06-28 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 222.9 |
| ddaef963-1a58-3a64-9277-48dcc0af571f | -10.8382 | -53.7648 | 2025-06-28 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 68ea7843-8114-30c3-9d7e-b54658157bb2 | -8.5722 | -51.5761 | 2025-06-28 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 384886f1-db59-3842-a4ef-fbdaf2a90701 | -4.5427 | -48.0367 | 2025-06-28 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| be226bbb-4358-3abd-9a78-0ff224db0ebd | -6.8922 | -43.9619 | 2025-06-28 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 230b2413-ee94-3d68-9d28-e1f01654ea96 | -9.1208 | -49.4743 | 2025-06-28 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 6f2d7b9a-f472-3dd9-a288-7656ed8f7001 | -6.9108 | -43.9834 | 2025-06-28 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 267.7 |
| c899bf55-7e50-32c1-aa3e-1cb656d2ea9f | -6.892 | -43.9851 | 2025-06-28 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0683edae-46c1-37f4-a1af-f310f4d7e37d | -11.2666 | -52.7318 | 2025-06-28 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b3ec6a96-7b6a-35f5-a7eb-1e10812ab59d | -7.2219 | -43.0682 | 2025-06-28 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 311.3 |
| 8f94c948-6e65-34b1-9ac8-838785d04f52 | -11.285 | -52.7716 | 2025-06-28 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| cbf71e6c-b5a1-3d8b-8b27-5cb75c34939d | -4.5429 | -48.0151 | 2025-06-28 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 6d18a813-0abf-3afc-aa6c-c61b822501bc | -7.2031 | -43.0701 | 2025-06-28 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 10f9276f-e41e-31aa-9c4f-214cc5cf045b | -6.9388 | -42.8745 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 939e2195-ed6c-33dd-9327-40852b3eb856 | -7.2131 | -43.086899 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ae9d8d7-cffb-33ff-a13d-4948e0c51b03 | -11.2573 | -52.701698 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8923a640-10b3-34bd-ab05-19bae04fbf14 | -7.5426 | -45.827099 | 2025-06-28 00:10:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30f666c9-712a-311d-b7a1-03b86f99c750 | -4.5422 | -48.0144 | 2025-06-28 00:10:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a85c07d7-cf78-3feb-b993-9e756974fe9a | -6.9064 | -43.9683 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a34043a9-149f-3d24-b771-da1e94ef672c | -7.2051 | -43.188702 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67233800-fbc2-3c28-86f0-d6342755228f | -6.4449 | -44.572201 | 2025-06-28 00:10:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0f43b8-7201-3b46-899f-2d2669c73418 | -13.9397 | -43.2332 | 2025-06-28 00:10:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7ed107de-1d85-3ba9-9e1a-7db43d009031 | -6.2289 | -44.525398 | 2025-06-28 00:10:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fee52dec-bbb1-365a-bcca-538f4e16c17e | -12.2634 | -46.77 | 2025-06-28 00:10:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1af3e9-8147-35b9-a853-7a868512c0bf | -11.2669 | -52.699902 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b245e439-064b-3e05-a4a1-f49dd0b3c67b | -6.8966 | -43.970501 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d10f624-43b5-345c-878c-a4744b62f729 | -12.0171 | -47.763302 | 2025-06-28 00:10:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 413b7ffc-c93b-36f7-ab5d-c871067089a7 | -7.2245 | -43.091999 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82ea4c4a-fa4d-3ed3-aa7c-4da324b68b41 | -5.0418 | -38.535999 | 2025-06-28 00:10:00 | METOP-C | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 790f3edd-7f3e-3280-9358-1561afc9ab54 | -8.0342 | -47.6315 | 2025-06-28 00:10:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59b3f6b4-7599-37ea-af47-024381fd870f | -6.8984 | -43.978298 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e55b3e32-cc34-3b5a-9b31-ca3d3e48ba47 | -6.9019 | -43.9939 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48387c17-3bc9-353e-a6b8-c7baf06c56a2 | -13.9434 | -43.250599 | 2025-06-28 00:10:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1114fed7-1211-35d8-b1d8-2ed10b08fadc | -11.5438 | -43.244701 | 2025-06-28 00:10:00 | METOP-C | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 034b4396-0476-3415-8e1c-a686dc29474b | -6.9551 | -42.901001 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f4a1d1d-fb73-3790-991a-22827e77dd81 | -7.1848 | -45.316799 | 2025-06-28 00:10:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8df4d9-ea41-316f-8827-cd73436abb19 | -9.1144 | -49.487499 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac55a6b-3d53-36b9-956e-f03116e20724 | -7.1868 | -45.326 | 2025-06-28 00:10:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c09b9914-677a-3e1a-b322-96f6b5b2091d | -11.8373 | -43.798 | 2025-06-28 00:10:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6dcd9d10-4367-35b1-a541-23d25dbe0917 | -10.5346 | -42.529099 | 2025-06-28 00:10:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b6e1e611-957f-3d17-953d-009cb1f2b6a6 | -6.9001 | -43.986099 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9e9e0730-2aeb-3b4b-8a2d-139f375f7808 | -8.037 | -47.644699 | 2025-06-28 00:10:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4726e0-acb1-3ecd-a0f3-e4fbb8e50905 | -7.5405 | -45.8172 | 2025-06-28 00:10:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25e4e2a4-7344-3b99-b5db-18ba5a69e88c | -11.5702 | -52.087002 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23d9f3b2-cf4f-3377-ba33-db8470c7ce20 | -9.1107 | -49.4692 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92c31c6a-d408-321a-a7ed-fa59e8a536e3 | -13.9416 | -43.241901 | 2025-06-28 00:10:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7311cd4f-f50b-3ca6-98e6-3b65d87cb191 | -12.2509 | -46.758701 | 2025-06-28 00:10:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6271158-d3de-3ea4-973f-c852a19e94fa | -5.8629 | -46.484001 | 2025-06-28 00:10:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
