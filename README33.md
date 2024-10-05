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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b400348-a03f-3f74-9241-55a880ccd943 | -17.1085 | -56.7892 | 2024-10-05 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 8db0febb-48e5-3d30-a060-ead43284155e | -17.0892 | -56.7709 | 2024-10-05 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 269c910c-b478-3468-825e-49a2d5d6d770 | -17.0888 | -56.7915 | 2024-10-05 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 3c980ecb-a49f-35fd-b994-4c230b9b3175 | -17.0695 | -56.7733 | 2024-10-05 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 659d1786-9abe-3768-8013-25163e33f332 | -18.8606 | -43.6084 | 2024-10-05 02:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 6061269e-ea30-32ea-8f04-fa0b8b5a921a | -18.8809 | -43.6032 | 2024-10-05 02:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| 84645507-5de2-312c-9e35-f00764ad7abc | -18.8816 | -43.5785 | 2024-10-05 02:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| a72f65ab-d609-36c1-8af4-6dc570204b91 | -18.6582 | -57.2967 | 2024-10-05 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| dcc0def7-f8bb-32ae-ae62-23e6cb89a22e | -18.6586 | -57.2759 | 2024-10-05 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |
| d3a4e7f8-638c-32b0-a447-f7f4f00a1de6 | -18.6782 | -57.2941 | 2024-10-05 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 1c5d4f41-a2a0-38f6-a86a-ce8338fd8f3f | -18.6785 | -57.2734 | 2024-10-05 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.3 |
| aa7c6da5-0b0f-3652-837a-319070ed3722 | -18.6981 | -57.2915 | 2024-10-05 02:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 5d728e76-f3ed-355c-9860-6b10183081e9 | -19.0944 | -48.2415 | 2024-10-05 02:16:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 14b5b0a8-a0b4-3500-bb71-12d803b2ff0b | -19.1576 | -46.6279 | 2024-10-05 02:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| d6108786-fa12-352a-9aa0-c677aeb25001 | -20.9179 | -49.0145 | 2024-10-05 02:17:01 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| fc9d94b6-c530-3c3e-9f5a-50f0019fbd48 | -20.9385 | -49.0098 | 2024-10-05 02:17:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.3 |
| 3ad768dd-12c4-385a-bec1-dad7c031d50c | -2.9014 | -50.7142 | 2024-10-05 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| f692195f-70f3-3835-903b-e3452f60ac27 | -3.3083 | -50.4719 | 2024-10-05 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 4c0deef2-2846-30e4-b44a-7cda1a1df69f | -3.3084 | -50.451 | 2024-10-05 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| bbadfb58-342e-3832-a816-a9ef71f78c56 | -3.618 | -47.5352 | 2024-10-05 02:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0c2d1de2-9db8-39f7-a4b3-8ea92df87cd2 | -3.6181 | -47.5134 | 2024-10-05 02:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| d272b872-0e76-3bc2-88f9-e063a1382b0d | -4.9451 | -43.7888 | 2024-10-05 02:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3b3f2bb9-54cd-3744-a0d3-127f95e7a0d2 | -4.9452 | -43.7657 | 2024-10-05 02:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| afb403e9-9bbe-373e-be05-7838cb64a609 | -5.8214 | -44.1426 | 2024-10-05 02:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fd75240a-b264-36e2-b50c-5077493a3ba0 | -5.8216 | -44.1196 | 2024-10-05 02:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e265ecac-4cef-3ff7-9b10-6e5a40ae52c3 | -6.9514 | -59.0666 | 2024-10-05 02:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 548d417c-085e-3407-a30d-f36813d87f79 | -6.9515 | -59.0473 | 2024-10-05 02:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bb37b918-7ace-3a14-a57c-dcacd591b290 | -7.5193 | -63.2558 | 2024-10-05 02:25:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9413384a-9975-3ea7-8186-1021f107e3f3 | -8.7652 | -44.8335 | 2024-10-05 02:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 3edce30b-376a-3af3-a42c-6f9478a6c21e | -8.7655 | -44.8106 | 2024-10-05 02:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 5b6db4cf-0404-3c6a-a794-9b024b9d373a | -8.7841 | -44.8315 | 2024-10-05 02:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 72863944-012c-3cf7-930f-514a590209bb | -8.7844 | -44.8085 | 2024-10-05 02:25:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| c1cb22d8-9842-3fe9-b381-865224f52c9b | -8.7584 | -49.9566 | 2024-10-05 02:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 9cb1809b-cfd9-3171-8a5c-8e0c30a2c079 | -8.6716 | -62.0971 | 2024-10-05 02:25:56 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 83c11feb-0b69-3975-b9d9-0f4764ea62f3 | -8.7769 | -49.9763 | 2024-10-05 02:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e2ad0696-0f5d-396d-8a96-5c1bfc193a5e | -8.7772 | -49.955 | 2024-10-05 02:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 2455e09b-5cf0-39ea-b7f2-ddf76232c7b4 | -8.7774 | -49.9336 | 2024-10-05 02:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 917e3b48-4f81-37bb-8e84-e25b1bc4f8d8 | -8.7957 | -49.9747 | 2024-10-05 02:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9bdeaefc-5783-3d33-b000-7221b231347c | -8.7959 | -49.9533 | 2024-10-05 02:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7478d01f-ec81-34d2-b569-d9990e80f615 | -8.9853 | -49.8083 | 2024-10-05 02:25:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d80e6bff-d2c2-35af-b1a0-93f56b809179 | -9.3457 | -51.1125 | 2024-10-05 02:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 76cfb259-8075-34d3-a35a-9a262d415155 | -9.3645 | -51.1109 | 2024-10-05 02:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 1b0285c5-ee21-3492-815a-52eef16fea2a | -9.3647 | -51.0898 | 2024-10-05 02:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| bb9938bc-6452-3307-87fc-b2dd8b2bcce8 | -10.3126 | -50.5554 | 2024-10-05 02:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f6cb3005-a3ba-3bca-b7d4-53c486377137 | -10.3129 | -50.5341 | 2024-10-05 02:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 7bc79432-b267-37de-a36c-e29c9271d327 | -10.3318 | -50.5322 | 2024-10-05 02:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d97f542f-348b-346c-a808-e280c69bbb40 | -10.3315 | -50.5535 | 2024-10-05 02:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4f177d4b-3800-3cf2-90be-e23adefda132 | -10.4424 | -50.7336 | 2024-10-05 02:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 4f22cd28-fe68-3b19-a454-c9c2dc8a7b95 | -11.1155 | -54.2319 | 2024-10-05 02:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b7e95afe-9d4d-365a-8954-9bcabcd1f005 | -11.0966 | -54.2336 | 2024-10-05 02:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 4c8488c9-8a5b-3cb8-a365-4647576499bd | -13.1362 | -51.1313 | 2024-10-05 02:26:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 6372065b-d15c-3ace-8d2f-d9eb56b2ad2a | -13.1358 | -51.1527 | 2024-10-05 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e0111992-459f-30e1-a9a4-451b7920fb69 | -13.117 | -51.1337 | 2024-10-05 02:26:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 68da54c3-fb5e-3daf-a0a0-c598f8097ace | -13.1166 | -51.1551 | 2024-10-05 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 8f2f2623-29d8-3dd9-a35f-d7eb49cad023 | -13.3978 | -61.9376 | 2024-10-05 02:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 62f4dd2e-befe-3da9-b5de-2ef721244745 | -13.3976 | -61.957 | 2024-10-05 02:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 218.9 |
| 7d30c252-30c4-384d-b7e6-9aca32c1f776 | -13.3786 | -61.9582 | 2024-10-05 02:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a849f69e-850a-3d85-ae88-1f7b781e2b41 | -15.5791 | -57.4532 | 2024-10-05 02:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 6e67e4be-9263-37ba-8ec0-265272cebd5e | -15.5788 | -57.4735 | 2024-10-05 02:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0d379c04-8495-39cc-9562-d6c79aac76e1 | -15.5597 | -57.4553 | 2024-10-05 02:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 77e6b7aa-61bf-306a-a213-94aeda542784 | -16.0942 | -50.2323 | 2024-10-05 02:26:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7c2e070e-e775-314e-a341-46610bcd92e3 | -16.5745 | -57.16 | 2024-10-05 02:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 4cc84930-f081-375b-82aa-afdc51ae0d09 | -16.5742 | -57.1805 | 2024-10-05 02:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 3dd77d66-e608-327f-a522-30888faead36 | -16.5544 | -57.2032 | 2024-10-05 02:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 284c820a-1dbe-35a4-a7f9-735118adae2b | -16.554 | -57.2237 | 2024-10-05 02:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.1 |
| 10a3fd04-0e9b-3691-bf76-62613bc46c34 | -16.4155 | -57.3619 | 2024-10-05 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| c837b6b6-015e-3b84-8c00-5fed8e3e2108 | -16.7647 | -57.4856 | 2024-10-05 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 1602e2d2-c30e-3c76-8dc6-3b9122a8fcf8 | -16.6871 | -57.4536 | 2024-10-05 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| c8ecfbdd-75fc-3914-8b3f-1d79398ff8bb | -16.9484 | -47.1877 | 2024-10-05 02:26:40 | GOES-16 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 478b270d-db2f-3c4d-90de-2ff7ccd46c63 | -16.7843 | -57.4834 | 2024-10-05 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 74450ce9-9784-32fa-b1ba-c6222d08c2e4 | -17.1085 | -56.7892 | 2024-10-05 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| dd9ae2b0-83ce-34f7-98ff-4493bc180e24 | -17.0892 | -56.7709 | 2024-10-05 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| e043306e-19e2-34de-b5b5-4158482aaf07 | -17.0888 | -56.7915 | 2024-10-05 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 2079d6a8-da90-3756-892b-f552a2509856 | -17.1235 | -51.7238 | 2024-10-05 02:26:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 793aef4b-b989-3546-b8dd-f396e2d87886 | -18.6525 | -43.1453 | 2024-10-05 02:26:49 | GOES-16 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.0 |
| 8a48080c-cedd-36db-8090-3e29725fc6d8 | -18.6532 | -43.1204 | 2024-10-05 02:26:49 | GOES-16 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.6 |
| e848d918-ca2a-363d-83d0-49d1b2bda486 | -18.8606 | -43.6084 | 2024-10-05 02:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| cee8cbc8-4b07-3f07-bb60-94e0dfcd0731 | -18.8809 | -43.6032 | 2024-10-05 02:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.4 |
| d507ce59-70d6-3d80-9e86-a16435960601 | -18.8816 | -43.5785 | 2024-10-05 02:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.4 |
| 1ddc6fec-e213-3c50-8825-ed0e15839eac | -18.6582 | -57.2967 | 2024-10-05 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 219cbca8-1c8c-3521-9820-cb2700c35706 | -18.6586 | -57.2759 | 2024-10-05 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| c4268c1c-25c3-35f0-b1d4-f39343606c96 | -18.6782 | -57.2941 | 2024-10-05 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 4836ba35-7b0c-3242-a992-1ad4ec91f1d9 | -18.6785 | -57.2734 | 2024-10-05 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.8 |
| a5c29f9e-56f4-309a-813d-f421544e7e4b | -18.6981 | -57.2915 | 2024-10-05 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 1fc2e94a-e865-3435-af0d-6a4d50273b2f | -19.1576 | -46.6279 | 2024-10-05 02:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 57a9276a-1985-362f-bbca-9027a4705438 | -20.9385 | -49.0098 | 2024-10-05 02:27:02 | GOES-16 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| 5065cd75-37ee-384e-a7d5-247f0bd3eb80 | -2.9014 | -50.7142 | 2024-10-05 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 240b92e0-26e8-3749-afae-ea467d8ea0b3 | -3.618 | -47.5352 | 2024-10-05 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 54834f51-59d4-3334-a4e5-9901efcc1de8 | -3.6181 | -47.5134 | 2024-10-05 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| ea5fc7a1-02f7-3d51-8116-cec31bf4b851 | -4.0794 | -47.9502 | 2024-10-05 02:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 04e00cda-e0c2-3e9e-9fe1-0235462549f2 | -4.9451 | -43.7888 | 2024-10-05 02:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e2f7b80e-2c65-38cb-bc33-b6b805cca4fb | -4.9452 | -43.7657 | 2024-10-05 02:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 861e74f2-3943-3027-8dcb-92605738cd02 | -5.8214 | -44.1426 | 2024-10-05 02:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 8b925af1-082c-37df-92c9-3eccae9c205d | -5.8216 | -44.1196 | 2024-10-05 02:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 0d1d8474-9d1e-3b6e-b4e0-5acb8a2de32d | -6.9514 | -59.0666 | 2024-10-05 02:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2d2080de-bdb0-3515-833a-dad31252ebf4 | -7.1346 | -59.3099 | 2024-10-05 02:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e9f7cd33-a2bc-331d-9451-c73cb876fdb3 | -7.153 | -59.3092 | 2024-10-05 02:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 975c506d-b0ba-3c29-95c9-7f8ee515ebfc | -8.7652 | -44.8335 | 2024-10-05 02:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 14ef6ad9-4a3d-34d6-94cd-0a8be971486a | -8.7655 | -44.8106 | 2024-10-05 02:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 11121fc6-8903-38f5-9dab-dceb71e44180 | -8.7841 | -44.8315 | 2024-10-05 02:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |


[Clique aqui para ver as próximas entradas](README34.md)
