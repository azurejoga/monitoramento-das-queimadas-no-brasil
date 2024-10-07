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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da48b5f4-ef76-37b3-a2e2-d5db47f50bf8 | -16.5267 | -57.7365 | 2024-10-07 07:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 1a33e29c-7bff-3540-9a3f-e0093a0d977e | -17.0316 | -56.6956 | 2024-10-07 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| fe00eaf0-1b70-3942-b71a-5cdad91cbb55 | -17.0123 | -56.6773 | 2024-10-07 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.0 |
| caff393f-9e98-346f-97af-bf783523d123 | -17.012 | -56.698 | 2024-10-07 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 0e7e6c0e-2168-33ca-bfbe-7e3e057a71e2 | -16.9744 | -56.5996 | 2024-10-07 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 32beed38-c2f7-3531-b848-ad11ea5b98b6 | -16.9179 | -57.6926 | 2024-10-07 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 0b2949b5-910e-3fd8-be33-e781e92240f7 | -17.0323 | -56.6543 | 2024-10-07 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 2c35374c-2ae5-30c5-bc9c-e64ab19dbe6d | -17.0319 | -56.6749 | 2024-10-07 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 224.3 |
| 1cd60d4f-1080-32ad-80f7-08330c371260 | -17.1581 | -57.3582 | 2024-10-07 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.2 |
| 340a4e78-a591-3267-af11-c25b37a13d8d | -17.1474 | -56.805 | 2024-10-07 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 736f0c68-9149-3293-8ffa-2cd6664216d8 | -17.178 | -57.3354 | 2024-10-07 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.1 |
| 5f3fc6c6-bf18-385c-ac20-fd4acb943764 | -17.1777 | -57.3559 | 2024-10-07 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 31bf27c3-b0e0-3666-85da-0ae10f2ebf4a | -17.1584 | -57.3377 | 2024-10-07 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.9 |
| a0c4e29c-4a5e-37b7-a7a4-9cb63dfdd1dc | -17.1281 | -56.7868 | 2024-10-07 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 3e3b7c2d-1ee7-313d-8cf3-70b19d01166c | -17.1278 | -56.8074 | 2024-10-07 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.2 |
| 35f75921-2543-3025-ba72-4258df4e7b4b | -17.1274 | -56.828 | 2024-10-07 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 1d8dec4f-d27b-30d8-aba6-2ec05b44f7ef | -17.0982 | -57.4267 | 2024-10-07 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 014fb257-2627-34d7-8f0a-9c64af0a80aa | -20.5848 | -48.5137 | 2024-10-07 07:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 71fb0ba8-7815-3cba-9ed2-6918fa01cb4d | -20.5643 | -48.5183 | 2024-10-07 07:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 71.1 |
| e93f7f8c-e6a4-3f23-a98f-b60335339a56 | -21.5913 | -47.7172 | 2024-10-07 07:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f7d331d6-fa54-37c7-a5f1-38dc0667e54e | -21.5906 | -47.7409 | 2024-10-07 07:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 3eadde1b-a67e-35ad-b5d9-9c0ad9b9e55c | -18.63 | -57.28 | 2024-10-07 08:03:39 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a1618d4d-b297-3fe0-a7ca-1948d8067a4b | -18.62 | -57.2 | 2024-10-07 08:03:39 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c1823691-ffad-3f63-ab5f-954f21c22649 | -18.66 | -57.3 | 2024-10-07 08:03:39 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4542d1d0-6784-3b67-9a1d-32e702d453ec | -18.65 | -57.22 | 2024-10-07 08:03:39 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f6b894a1-62ed-3276-8620-4f64de8ccb9a | -16.5072 | -57.7387 | 2024-10-07 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 4f79f0a0-08a0-33b7-b632-6e200acdf02f | -16.5267 | -57.7365 | 2024-10-07 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 9e585da9-6eaa-3789-83ca-96f9d376d73a | -16.9741 | -56.6202 | 2024-10-07 08:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 3b797c8f-e837-3e3a-80d2-e47b0e068998 | -16.9744 | -56.5996 | 2024-10-07 08:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 8b253be7-cd00-3dac-8f40-bd34cc4b2bd3 | -16.994 | -56.5972 | 2024-10-07 08:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 0a2e8c77-0f99-3b78-bbd9-a88aa6731f78 | -17.012 | -56.698 | 2024-10-07 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 0fd45eb0-a887-3c68-b2a4-91fa879e02cd | -17.0123 | -56.6773 | 2024-10-07 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.2 |
| 8a9a448d-e779-3b68-9411-5cfe5fae16ba | -17.0316 | -56.6956 | 2024-10-07 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| c317785b-a969-3eda-a7a3-47a8c478ee6a | -17.0319 | -56.6749 | 2024-10-07 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 225.6 |
| a2342bac-b33a-3dfc-bea9-e524cbcc6050 | -17.1581 | -57.3582 | 2024-10-07 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 382752a9-c984-3ea8-b110-7c48d926bda8 | -17.0982 | -57.4267 | 2024-10-07 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 1f1f7fb0-96a1-3424-bb0d-ae68842d55d1 | -17.1274 | -56.828 | 2024-10-07 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| fd487de1-2878-3735-91a2-103aaaf316e3 | -17.1278 | -56.8074 | 2024-10-07 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.1 |
| 0ba28847-8af8-3a20-a943-f71aa77d60be | -17.1281 | -56.7868 | 2024-10-07 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| f152f67e-783f-315b-82f2-415072199d4e | -17.1484 | -56.7431 | 2024-10-07 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 60a125a6-c49d-3afd-a635-2a96554187ef | -17.1584 | -57.3377 | 2024-10-07 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 157.4 |
| 3b3a1f58-bfe4-38af-a38e-4dbc68d63e04 | -17.1777 | -57.3559 | 2024-10-07 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| f401f0ff-9f37-370d-960d-cb8a0d61232b | -17.178 | -57.3354 | 2024-10-07 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.0 |
| 49d2cb84-217a-35ca-8bae-cb93f5e4aba8 | -21.5906 | -47.7409 | 2024-10-07 08:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 74eaff19-a5a3-3bb3-9b27-b653d54e2149 | -21.5913 | -47.7172 | 2024-10-07 08:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 89b0bbdc-5fb7-3d12-be90-9008e7a5901c | -21.5698 | -47.746 | 2024-10-07 08:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 447b35e4-a908-3050-b3f2-5d12ba0c10b0 | -16.5072 | -57.7387 | 2024-10-07 08:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| f24747ee-9e95-3584-8401-3bdaf3ae3d5f | -16.5075 | -57.7183 | 2024-10-07 08:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 4c0c450b-b0d3-35cb-8862-6bee7bfc22ca | -16.5267 | -57.7365 | 2024-10-07 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 3e3c6a5e-581e-3709-8aac-5f2cc2a46817 | -16.5749 | -57.1395 | 2024-10-07 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 9966e240-67cd-3259-ad34-fb3eca67a096 | -17.012 | -56.698 | 2024-10-07 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 8062c225-c9b8-3ecb-98ec-53d29d575f6e | -16.9741 | -56.6202 | 2024-10-07 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 719f8dbe-e352-333d-bc23-04986594c48b | -16.9744 | -56.5996 | 2024-10-07 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 54e79124-a98b-32c3-a000-f684f62eec89 | -16.9937 | -56.6178 | 2024-10-07 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| d7b6275c-119b-3f99-a03d-893272fc99b6 | -17.0319 | -56.6749 | 2024-10-07 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 177.1 |
| 9d35a247-2c6b-3263-929b-b08b7352ca3c | -17.0123 | -56.6773 | 2024-10-07 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.4 |
| 90f663fb-715e-398e-a1af-5a033d43f04b | -17.0316 | -56.6956 | 2024-10-07 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 71237025-4cc6-364a-b0cd-8ce4a359a1d6 | -16.994 | -56.5972 | 2024-10-07 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| aae6ec74-a7a9-3cbb-b399-7c6328565b79 | -17.178 | -57.3354 | 2024-10-07 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 155.2 |
| d79013a2-a2a2-3ea5-b0c6-d678267ede0f | -17.1777 | -57.3559 | 2024-10-07 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.8 |
| 09bd1852-1e1e-3223-9593-675fff35aac7 | -17.1584 | -57.3377 | 2024-10-07 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.1 |
| 97b37402-3ec5-3370-965d-55e5e3c7402f | -17.1581 | -57.3582 | 2024-10-07 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| d4cbefd5-0b9d-3b10-b07f-ebaafa006d3f | -17.1278 | -56.8074 | 2024-10-07 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.4 |
| 4aab0c61-9287-3d55-b2db-cd35374ad740 | -17.1281 | -56.7868 | 2024-10-07 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 7265fc66-198c-3e18-9cd4-2952077860fb | -17.1274 | -56.828 | 2024-10-07 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.0 |
| fc1dea5a-70b0-363b-82c9-779fea8ba1f3 | -17.8314 | -53.8043 | 2024-10-07 08:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| bb24ee81-d0b3-3fdd-a081-177c54a39aee | -16.5072 | -57.7387 | 2024-10-07 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 7dd141fe-d83c-383b-ab2b-bb1a66af14ff | -16.5075 | -57.7183 | 2024-10-07 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 167094ff-a460-3c5e-a4ea-731c33714fdc | -16.5267 | -57.7365 | 2024-10-07 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 65975ce0-0a76-3722-ba4b-f5bdbef6b616 | -16.5749 | -57.1395 | 2024-10-07 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 389ad089-f85e-34b0-b74d-a581f2ad8ef6 | -16.7856 | -57.4015 | 2024-10-07 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 7eaa3430-22ee-3d4c-9fcb-34681781e935 | -16.8051 | -57.3993 | 2024-10-07 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| a793a8c8-8fdd-33c5-9c38-7f8d5674b6b7 | -16.8055 | -57.3788 | 2024-10-07 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| d7c91f1a-27e1-35f2-b7ad-6a04dab67528 | -16.8247 | -57.397 | 2024-10-07 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 5e2ace0f-a831-3df2-81b1-6eb820d70dcd | -16.825 | -57.3765 | 2024-10-07 08:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 7f7e4425-5205-386c-8395-1e20e96e3993 | -17.0123 | -56.6773 | 2024-10-07 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 177.7 |
| 01b412d9-ca7f-3892-88f9-b546071f0b0d | -17.0316 | -56.6956 | 2024-10-07 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| eb756cdf-7808-317e-affc-5995f716f2ac | -17.0319 | -56.6749 | 2024-10-07 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.1 |
| 7643282a-06cc-319f-a70d-d5566131f6b4 | -16.9741 | -56.6202 | 2024-10-07 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.0 |
| a4a7a2d9-5643-3417-b27d-8cb5792818cd | -16.9744 | -56.5996 | 2024-10-07 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| ee860d67-191d-3632-8413-8eaf6913b952 | -16.9937 | -56.6178 | 2024-10-07 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 94b068f6-11a9-3e09-a741-080be13174ac | -16.994 | -56.5972 | 2024-10-07 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 2dcb2516-b059-33c5-bc59-91fd76c2ed88 | -17.012 | -56.698 | 2024-10-07 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 1a848ebb-6f25-35ab-b6c1-29fc9dda4444 | -17.1584 | -57.3377 | 2024-10-07 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.4 |
| f889388c-9441-3616-8ce4-a9de5b71dc01 | -17.1274 | -56.828 | 2024-10-07 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| af4f868a-11be-30c9-9a06-ef90ae04ae0c | -17.1278 | -56.8074 | 2024-10-07 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| b96a9988-ed82-3ff4-a9f2-aee7f31238d1 | -17.1581 | -57.3582 | 2024-10-07 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| a8357bcc-1e16-30fb-b0f2-3f4041a2922a | -17.1777 | -57.3559 | 2024-10-07 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 93119e07-3cd5-3007-9aa7-204b86050ce8 | -17.178 | -57.3354 | 2024-10-07 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| f6253e17-8853-3c88-a835-1bec9108e312 | -17.6877 | -53.0788 | 2024-10-07 08:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2327b630-6e3c-32dd-b1e9-545b460120ac | -17.6873 | -53.1003 | 2024-10-07 08:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e41e7bef-b3b1-390d-925f-330d8ddeeb7e | -17.6679 | -53.0819 | 2024-10-07 08:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 72f73733-3623-35ba-a9fe-4ea724673f1c | -17.6675 | -53.1033 | 2024-10-07 08:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 52df08e3-76a3-3da9-8527-886bcc60a767 | -17.8314 | -53.8043 | 2024-10-07 08:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1c98e21b-bbc1-32ca-aa3f-37030a7e5e89 | -16.5072 | -57.7387 | 2024-10-07 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 0fa73f98-cd95-3dc4-ab40-c067dc22572e | -16.5267 | -57.7365 | 2024-10-07 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| e9f1e0f5-af6e-3d83-9537-2e41e64ffbfd | -17.012 | -56.698 | 2024-10-07 08:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 598f8b0b-77b0-3e7f-a7ba-c2f79d92f91f | -16.994 | -56.5972 | 2024-10-07 08:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| d8a183ab-5d56-31b3-926c-dcdfc169d20f | -16.9937 | -56.6178 | 2024-10-07 08:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 3799fef4-5a9d-3d02-87fe-aa375f42ae7b | -16.9744 | -56.5996 | 2024-10-07 08:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |


[Clique aqui para ver as próximas entradas](README146.md)
