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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea3e356c-24da-3b85-8184-d01c22a4037f | -17.1085 | -56.7892 | 2024-10-05 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| c2af828b-6fec-3692-a1fc-f01fd2c6eb33 | -17.0316 | -56.6956 | 2024-10-05 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 24a00e99-6209-36ec-9821-a7b5389b8125 | -16.9714 | -56.7852 | 2024-10-05 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 158.7 |
| 7ee23f66-1d6e-3613-be55-687e16c03a46 | -17.1771 | -57.3969 | 2024-10-05 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 95516101-b002-3cde-804d-d07b27374dcc | -18.6984 | -57.2708 | 2024-10-05 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| fee32e3c-360f-30b5-bbb0-131a0b84c505 | -18.6586 | -57.2759 | 2024-10-05 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.7 |
| 8c8b977e-ce2a-3930-be34-d9f65956a9f8 | -18.6785 | -57.2734 | 2024-10-05 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.5 |
| b4908006-af3f-33bd-b851-cbb21025b3f3 | -1.17102 | -48.84462 | 2024-10-05 12:34:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9696b212-8b7a-3ad8-a0ac-929b6f65ba99 | -1.16879 | -48.85989 | 2024-10-05 12:34:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 0a399cc6-35b3-3489-9239-0b7a0bbc2cb0 | -3.30864 | -50.45327 | 2024-10-05 12:34:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3671144b-542b-3138-8814-7c2f3ca82f4a | -1.45704 | -46.1815 | 2024-10-05 12:34:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e607f3b0-91cd-3986-985e-1209de7ce4ce | -1.45557 | -46.19156 | 2024-10-05 12:34:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a9f5e3a7-7627-33b0-9c2a-6604f78bd267 | -1.23589 | -46.13187 | 2024-10-05 12:34:00 | TERRA_M-T | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a606c2a5-0402-36e1-9634-485d0fa61e3d | -2.3875 | -46.12203 | 2024-10-05 12:34:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4f238b79-e374-3128-84a4-bcf7a30bfb33 | -2.38606 | -46.13186 | 2024-10-05 12:34:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b91ac0eb-859a-37bc-beda-189dfff75bb1 | -3.61561 | -47.51954 | 2024-10-05 12:34:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 1f29ad4b-e1fb-3c0f-907e-d91066ae5dbf | -4.09083 | -46.87811 | 2024-10-05 12:34:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6f1703f2-cea8-356b-aef5-d753f912e510 | -2.48115 | -48.06401 | 2024-10-05 12:34:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 31b677b0-7883-3216-9b98-f4e31c8b67ac | -3.98877 | -43.02548 | 2024-10-05 12:34:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eb095ba9-4643-3a46-b804-25801e67630c | -3.82821 | -42.26211 | 2024-10-05 12:34:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 7ad12dba-e4a2-3fc3-a1be-e5775cd673bc | -3.82682 | -42.27213 | 2024-10-05 12:34:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 6da287be-8ed1-3392-97dd-f82ad51efd6c | -4.80792 | -43.03152 | 2024-10-05 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| edf25f34-a31b-3798-b5a7-fa086d4cc698 | -4.80655 | -43.041 | 2024-10-05 12:34:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 501fc350-8e2a-30aa-a3f8-5efc92b49ed5 | -4.15084 | -43.05093 | 2024-10-05 12:34:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6d7dd271-b5ef-3ead-810b-583aa0196619 | -3.58417 | -43.72202 | 2024-10-05 12:34:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ff35823-4a2f-3cb7-8b64-cdb3fe14a768 | -3.58288 | -43.73094 | 2024-10-05 12:34:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 725e1ae4-d4b6-3406-92c5-9eeb0971d19d | -3.41996 | -43.1987 | 2024-10-05 12:34:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4511c0bb-9a97-3ee0-8781-4d17112ce42e | -4.6595 | -43.80938 | 2024-10-05 12:34:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 088152b1-9922-33fe-9e4f-9ecd4c51467a | -4.65829 | -43.75412 | 2024-10-05 12:34:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 86f84017-9034-3a68-af08-38254af19441 | -4.657 | -43.76313 | 2024-10-05 12:34:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ad811a34-4e0d-3743-bec0-2cf3082bc5ce | -4.33654 | -43.49047 | 2024-10-05 12:34:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 413dc777-3462-31c1-8375-ae4ac53ad5bf | -4.01254 | -43.24333 | 2024-10-05 12:34:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 3003bd01-52df-3ee1-99ba-18c4a7a92bf3 | -4.01122 | -43.25253 | 2024-10-05 12:34:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| f90e9db4-6471-308a-8a2b-ba83ac31f81a | -3.81047 | -43.1087 | 2024-10-05 12:34:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 59b99d7a-d99a-3760-85c5-757b13933bf7 | -3.99733 | -44.50343 | 2024-10-05 12:34:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1e93768a-b28a-375e-ba58-4f9fcad3f4ad | -3.99605 | -44.51225 | 2024-10-05 12:34:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d90b4120-f544-3e10-bb56-c44e5e4458e2 | -3.39513 | -45.28559 | 2024-10-05 12:34:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9dbbffc0-be9e-3930-a778-90a1d243180f | -3.37726 | -44.83892 | 2024-10-05 12:34:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| eb1eba70-fa85-34ae-aa4b-9e97edc2eebc | -3.36934 | -44.69577 | 2024-10-05 12:34:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 9a9869e2-03b0-3305-9473-c8bcce5290aa | -3.36806 | -44.70462 | 2024-10-05 12:34:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1c06b962-41a9-3fe8-bfa4-ea7f6dea5140 | -4.68183 | -45.88095 | 2024-10-05 12:34:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8355d927-792a-30c5-924d-9db3675faf7c | -4.62815 | -45.61504 | 2024-10-05 12:34:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 987320fe-5c47-3c38-bd93-488ffc8a499d | -4.41414 | -45.37883 | 2024-10-05 12:34:00 | TERRA_M-T | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 61ae1547-2414-3d63-8b1e-ddebb858a75b | -3.79847 | -45.8037 | 2024-10-05 12:34:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| baa69b99-c234-3d44-adbd-25422e880dc6 | -3.7971 | -45.81299 | 2024-10-05 12:34:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6ebabd0a-00b2-31a0-ad58-f99f90cdf0b3 | -6.9699 | -59.0658 | 2024-10-05 12:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 05699229-a844-3388-a728-93d4518c53ae | -6.9514 | -59.0666 | 2024-10-05 12:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 183.8 |
| 524afcd3-f09a-36ee-b3da-a13a6ce52bf6 | -6.9698 | -59.0852 | 2024-10-05 12:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 442fd40f-a043-3637-9439-b19e0798e9f6 | -8.7584 | -49.9566 | 2024-10-05 12:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8c976e02-00ec-3186-95d3-fb799ab63142 | -8.7772 | -49.955 | 2024-10-05 12:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1e0c5d4c-5cfb-31f1-a3b8-2c3c9353c0fd | -8.8714 | -48.3297 | 2024-10-05 12:35:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 638a1727-6ad5-3f3e-9cf2-aa1f5980e920 | -8.8738 | -45.1875 | 2024-10-05 12:35:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ff3d3e99-7536-362a-8a36-f8c9788f1208 | -10.4444 | -50.7162 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 07338a4f-7a25-31e8-a406-d575ea16a7aa | -10.44201 | -50.73111 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 08656731-ee39-3f1c-9392-078b8183b7bb | -11.23362 | -51.18573 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c807f196-bf21-38bb-aa83-1e76685a3246 | -10.24506 | -52.72854 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 5c59a149-3938-340f-a099-82ed99d989a9 | -10.03606 | -53.4634 | 2024-10-05 12:36:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| bf3c01bc-9c37-3b41-888e-0c854a47bcec | -5.90146 | -53.4334 | 2024-10-05 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 58cdca17-b4c3-3c3c-948b-8587936e8865 | -9.44034 | -54.89322 | 2024-10-05 12:36:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f1ca2898-9b09-3bea-9faa-13c6589e2f2e | -4.85561 | -46.52306 | 2024-10-05 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e29ccb67-6bea-3acc-885a-af45cf806c8d | -4.84633 | -46.52181 | 2024-10-05 12:36:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 04be552e-8369-3c2b-b0a2-b506dfad78f9 | -5.99777 | -47.46662 | 2024-10-05 12:36:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d8d0e344-2249-3429-8c74-521c501e005e | -5.38988 | -47.70304 | 2024-10-05 12:36:00 | TERRA_M-T | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d317459c-326a-3020-a232-cca9e0486bbf | -6.92889 | -47.69349 | 2024-10-05 12:36:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4bbcfbfd-b8c4-3d5d-9879-baa2cea2825f | -6.92729 | -47.70406 | 2024-10-05 12:36:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2e4ff46f-1be1-3031-8fa3-d943b7e162fa | -9.32725 | -48.23236 | 2024-10-05 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f0ce6574-6c2c-30fe-b020-58844e674036 | -8.89206 | -48.32222 | 2024-10-05 12:36:00 | TERRA_M-T | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 37180a87-7a36-3350-b4db-2ba8c86ef7ba | -8.88232 | -48.32077 | 2024-10-05 12:36:00 | TERRA_M-T | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 7af4dfb2-fd34-3dc8-a853-2f0946f3de74 | -8.88065 | -48.33171 | 2024-10-05 12:36:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 7793e6b7-2d28-343a-b091-8628c7276130 | -8.8709 | -48.33024 | 2024-10-05 12:36:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 673f62a1-4c99-3818-a5ac-eaa01e332f5d | -8.86282 | -48.31789 | 2024-10-05 12:36:00 | TERRA_M-T | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6862d373-efed-3bfc-811c-dc03318af864 | -8.85308 | -48.31641 | 2024-10-05 12:36:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 32943685-b391-3763-88cb-dacf24d94836 | -8.85141 | -48.32726 | 2024-10-05 12:36:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 37799f08-4bb1-3bbd-a37b-8ea8bf0c571c | -8.61084 | -47.12497 | 2024-10-05 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8e4a0485-92aa-3e96-935c-896d34099597 | -8.60941 | -47.13459 | 2024-10-05 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| c60f6441-0762-3aec-80eb-ad035b8bcca3 | -8.60021 | -47.13326 | 2024-10-05 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7ce967a2-7dc4-3e25-9edd-4e06827b19b8 | -8.49274 | -47.29906 | 2024-10-05 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 3583dfe4-0f3f-3c55-83e0-0a315a352edd | -8.49131 | -47.30868 | 2024-10-05 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 954cd911-8b87-3578-aabb-392ab2261fcb | -10.10678 | -48.82191 | 2024-10-05 12:36:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2fe57a94-8e18-3b76-acb1-6a690fe9834d | -10.69701 | -48.71133 | 2024-10-05 12:36:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4bf2ebe0-560f-37bc-9ff4-32de7b95dcb2 | -11.74536 | -48.35969 | 2024-10-05 12:36:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c0f5e5f9-7653-3d6d-976f-6d3917235432 | -11.72684 | -47.81063 | 2024-10-05 12:36:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d56210a3-7452-39aa-a1d2-48c9a24eb821 | -11.72538 | -47.82032 | 2024-10-05 12:36:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 84104b8a-da3e-38ae-af29-ae6a55008188 | -11.71912 | -47.79951 | 2024-10-05 12:36:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 97a583cd-ce39-372c-b3e5-d6f7b447c6de | -11.71765 | -47.80919 | 2024-10-05 12:36:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| e4b33fdd-67d6-3f0d-9bda-62165c5e5561 | -11.71618 | -47.81889 | 2024-10-05 12:36:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| df99c837-3674-30ea-af7b-539f241afc34 | -11.70846 | -47.80777 | 2024-10-05 12:36:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a9e05a4f-b450-3950-b8ea-0d2297ff75b2 | -11.70699 | -47.81747 | 2024-10-05 12:36:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| b2c23d31-9421-355e-bf4c-d7268dcdc5f4 | -8.77945 | -49.96089 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 509aa4ce-faea-3836-a571-a626a64d7598 | -8.77074 | -49.94523 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| bb960abc-d06a-38e0-a246-bb74cbd2c184 | -8.7685 | -49.95922 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 23fcf6fc-5be5-3fd6-ba6b-4aebd6646a2f | -8.76696 | -49.95282 | 2024-10-05 12:36:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 52a26f0d-4dbf-39b7-83ef-b008643cf65b | -8.65884 | -49.10689 | 2024-10-05 12:36:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| e6f4ff8c-ccde-3cfc-82e2-037f74d3eaf2 | -11.88154 | -50.13776 | 2024-10-05 12:36:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 7a21b70a-2608-3839-893e-b8edc091a3b3 | -10.587 | -39.64173 | 2024-10-05 12:36:00 | TERRA_M-T | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 77888421-740f-3547-965b-562391d8352b | -10.58626 | -39.63612 | 2024-10-05 12:36:00 | TERRA_M-T | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 1d5bc484-c311-3a5b-8480-0f1e6514c360 | -12.99282 | -39.99743 | 2024-10-05 12:36:00 | TERRA_M-T | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 1ed3b6d5-79fe-3859-8db3-274b66126d83 | -7.96213 | -40.27519 | 2024-10-05 12:36:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 0a785d5e-28a5-3046-b2a4-7d78c380c4b4 | -7.95326 | -40.26832 | 2024-10-05 12:36:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 3f0bce90-2a4e-343a-9c1d-e89b1a3b4f50 | -13.21626 | -41.87739 | 2024-10-05 12:36:00 | TERRA_M-T | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |


[Clique aqui para ver as próximas entradas](README159.md)
