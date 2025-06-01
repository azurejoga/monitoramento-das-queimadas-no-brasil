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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e20760d-588c-317c-b65f-d5337217cf0d | -8.1433 | -46.484798 | 2025-06-01 00:20:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e52d101-55d2-3ec8-8ee2-7e13e0d4e1a3 | -4.4885 | -48.8592 | 2025-06-01 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f351edaa-e1de-3e62-9877-9cbdd3e361b4 | -8.1337 | -49.585499 | 2025-06-01 00:20:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6289d66-fe16-364f-9b77-644d7f2ee874 | -12.1284 | -54.570702 | 2025-06-01 00:20:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d7711fa-f0d5-331f-8767-83c83bdd7e2a | -15.0585 | -43.863701 | 2025-06-01 00:20:00 | METOP-B | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 90c7b4ad-8830-32ee-952b-56bfd8459b0d | -14.6923 | -45.0793 | 2025-06-01 00:20:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 035ce3f2-34b9-3ab1-8d57-7d5d53e7360d | -12.7235 | -54.961899 | 2025-06-01 00:20:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eed8c569-3333-3569-8dfc-bdda6c907023 | -9.1348 | -47.573399 | 2025-06-01 00:20:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bf37049-31ac-3b37-b075-4901d8914184 | -13.6426 | -52.175301 | 2025-06-01 00:20:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bf1de5d-9cd4-33f0-bea8-44d44ce4536c | -13.0938 | -45.266499 | 2025-06-01 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1b6ebb2-3e4d-32f4-8b70-0fb518fbe777 | -9.049 | -47.015598 | 2025-06-01 00:20:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce128e93-a464-3f28-923c-b38be9a834ba | -10.1313 | -47.194199 | 2025-06-01 00:20:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b13168bb-5262-30bd-9ecf-cd434e5e0ea9 | -6.2705 | -44.1996 | 2025-06-01 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ddfd441f-f120-3f6b-8459-5835025b1088 | -7.2211 | -43.1388 | 2025-06-01 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| d1b28173-e8f1-3993-9bf6-c9778be6d471 | -10.2268 | -47.1733 | 2025-06-01 00:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0fe83ddd-44aa-3ed8-9640-227c1620f03f | -6.2705 | -44.1996 | 2025-06-01 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fe397331-a806-39d6-83ce-fe85068de012 | -6.2705 | -44.1996 | 2025-06-01 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9d988778-46ca-32a8-9c78-3e5a2605b61a | -6.2705 | -44.1996 | 2025-06-01 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a5fa167f-f2f4-39de-ad34-22ed585700a7 | -10.8318 | -56.960098 | 2025-06-01 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3042c3e-2ca5-3a81-a7c8-f69b741b6dbd | -8.6805 | -46.646301 | 2025-06-01 01:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 101841de-4543-3ec5-9d01-cd8df66e7f5d | -10.1441 | -52.1381 | 2025-06-01 01:11:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6afb35e-d56e-3b9e-9a14-f44b4610becb | -10.1462 | -52.146599 | 2025-06-01 01:11:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7703b28-c337-3aa3-921d-2842bc56ee29 | -11.0809 | -54.774799 | 2025-06-01 01:11:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a8706e9-3e2d-3a49-a1d4-4edcbba0d52d | -11.0793 | -54.767799 | 2025-06-01 01:11:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18211e81-5a70-3b67-8c1b-dbc73cdccd12 | -9.9354 | -59.905998 | 2025-06-01 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b237b8cb-3bde-3bc7-838f-cd19e423b164 | -9.6103 | -50.061798 | 2025-06-01 01:11:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6639361f-975f-3400-888f-5f7dde9ba857 | -11.0825 | -54.781799 | 2025-06-01 01:11:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6565eb17-7406-329b-93b8-60073fa97dd3 | -11.0923 | -54.779499 | 2025-06-01 01:11:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7457253-abc9-3777-98e0-76fd4bd339dd | -6.2791 | -44.212299 | 2025-06-01 01:11:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d69e8da-e191-3586-829a-9c4dfe33699d | -10.1539 | -52.135799 | 2025-06-01 01:11:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf924e4-28f2-3c8c-a190-268cb0040d7c | -10.8286 | -56.945499 | 2025-06-01 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f420f434-dbcd-3b95-bb91-ad1ea461438d | -10.296 | -57.1409 | 2025-06-01 01:11:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 112b031a-f50d-3a86-b91a-4ede7128c914 | -10.827 | -56.938301 | 2025-06-01 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d7d3f16-3061-3b6d-9120-850b81e72e6c | -11.0891 | -54.765499 | 2025-06-01 01:11:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87743bbd-3807-3eb5-ae75-b67fc469ca47 | -9.9334 | -59.8964 | 2025-06-01 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b661ffc-c02e-3956-85bf-a191695dab1d | -10.8302 | -56.952801 | 2025-06-01 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7816d272-4560-3f95-9ce1-bbb7bbf3799e | -11.0907 | -54.772499 | 2025-06-01 01:11:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adb1600d-c7ec-350d-905b-4771fa3e1c8f | -14.68476 | -52.69083 | 2025-06-01 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 0ee36284-e5fb-3d16-bf90-4822a33fab4f | -14.68621 | -52.69704 | 2025-06-01 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f2c45c8d-19bc-3fab-b010-b6682a46ff03 | -14.68438 | -52.68489 | 2025-06-01 01:15:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c2add8f2-713a-36eb-9186-ba383bc8b318 | -12.72288 | -54.96699 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 249082fe-850c-30c9-ab0e-8c33cfe5af89 | -11.45603 | -55.00936 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f2a0d442-bbc9-38f7-9b47-1d2f013248cb | -12.52893 | -57.18888 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8aa7422f-99cc-318e-a882-d88ab52565f0 | -10.47187 | -47.94179 | 2025-06-01 01:17:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| ff14fe16-2a56-343d-8c3b-25d8957b2b66 | -10.29384 | -57.14693 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 95e4ebc4-9ce0-3835-a0f7-8f021ad654ba | -11.44539 | -55.00094 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e33d87cd-0734-3a0c-834e-f53702cd3033 | -11.42966 | -55.00921 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e20d74bf-d74a-3618-b169-2b06c3586c26 | -11.57103 | -47.46386 | 2025-06-01 01:17:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 4d28afb7-0c6c-3ae5-b7a3-1b445547cf56 | -10.47775 | -47.94597 | 2025-06-01 01:17:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d48e3df1-bba2-35cb-aa98-917591d656fe | -11.14139 | -53.93179 | 2025-06-01 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 661530fc-0284-36f2-89f8-f2242bcfefc3 | -11.07213 | -54.77815 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5b823cd2-72dd-35f5-bac4-8433e92df717 | -13.10566 | -52.29163 | 2025-06-01 01:17:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2244776c-2941-370e-b302-d5632b8d408b | -10.82738 | -56.94199 | 2025-06-01 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 00cf3f07-76a9-3c6c-879e-5d6bdf19f8ee | -12.12352 | -54.59372 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 15182639-c08b-31bd-9976-d06112ff8252 | -11.44684 | -55.01076 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 84b3318c-ea0a-3ece-abc5-f77841fbe9c4 | -10.61608 | -57.61042 | 2025-06-01 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3e31495-6701-3c0c-8141-8fdfeec9f980 | -11.07999 | -54.76661 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f51e429b-de8c-35de-823f-85c85bde359f | -10.47754 | -47.97386 | 2025-06-01 01:17:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a5c39c65-e81a-3089-920d-4766bdfa623b | -12.71547 | -54.97403 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f1b0b7f3-84c2-3777-bfb7-12afbbdd6ff7 | -14.02123 | -55.14256 | 2025-06-01 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 77e60c71-b6a5-339c-8a3f-3d3e5dab04e4 | -11.90403 | -54.78893 | 2025-06-01 01:17:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bda79cb4-37b6-375d-8e22-41eaadd46b40 | -11.57932 | -47.45497 | 2025-06-01 01:17:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 60f4ed0c-d769-37db-9027-b4db234be483 | -12.0871 | -54.58447 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2cb76a4b-6ebe-352f-b4db-85d7edd09170 | -13.64156 | -52.17852 | 2025-06-01 01:17:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fae6b464-1e8c-33b1-b9e9-22a96e3548e6 | -11.42826 | -54.9994 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b27668af-dddc-3510-b7f6-14c6de46d90a | -10.46212 | -47.94889 | 2025-06-01 01:17:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 97f3e15c-0530-3978-9a4a-d89418bab634 | -10.82985 | -56.95983 | 2025-06-01 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 81881612-f26e-31a0-a19f-ba7494bbfb68 | -9.9283 | -59.90902 | 2025-06-01 01:17:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| bd7fb655-868c-3c52-a96d-deb210bc70b4 | -12.12501 | -54.60378 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| d06c8402-1a6f-31d0-b83e-fa1fc52e5e97 | -12.22981 | -54.29863 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6a26ff58-4443-3ddf-bd7a-75602d3e60a9 | -12.52769 | -57.17982 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 91bd39dd-aabc-399b-a4cd-fc405ddfad2e | -13.95389 | -54.49061 | 2025-06-01 01:17:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f6af5998-c6ae-3b5d-87a1-fd9222cedbe7 | -12.08563 | -54.57441 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e89cfd43-3910-3292-a381-e0912de91857 | -9.39632 | -56.01103 | 2025-06-01 01:17:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2b345f60-cb5e-3047-8daa-707d1423856a | -11.08295 | -54.78691 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 29646c72-409e-3ef0-9eaa-7ce53b409f95 | -11.08147 | -54.77675 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| e0416ba9-1fde-3f02-91c2-19b4be134b26 | -10.82862 | -56.95091 | 2025-06-01 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2dc75295-5a19-3ebb-8167-14a5047ff16a | -9.9269 | -59.89821 | 2025-06-01 01:17:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a76012fe-1d8a-347b-ba91-9e02e44e01c4 | -11.4362 | -55.00234 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 824b974d-c7e5-3b4a-a850-badb776086bb | -11.70887 | -56.45963 | 2025-06-01 01:17:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89698244-8108-3007-a483-40773ee3c468 | -10.2926 | -57.13803 | 2025-06-01 01:17:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ffead155-cb06-3246-87e6-28a4391b8863 | -10.14265 | -52.13839 | 2025-06-01 01:17:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| c8bb724d-ef55-303c-b53a-b2784437f138 | -11.92247 | -54.41836 | 2025-06-01 01:17:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f9fa6888-b919-37b5-8c5b-8eb8ec88c3a0 | -11.14304 | -53.9429 | 2025-06-01 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 98603422-bfeb-3dc3-8b86-b6798ebf6a8f | -11.43764 | -55.01214 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 933fda5c-e674-356a-9b8d-6cb4f8ba57a0 | -11.42254 | -55.09025 | 2025-06-01 01:17:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3061e599-fe12-378d-a75b-4d914bb8748b | -12.72429 | -54.97662 | 2025-06-01 01:17:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2e915790-6641-39bf-ae6f-ad9f2b812846 | -6.2705 | -44.1996 | 2025-06-01 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 68628188-0350-37f4-8cae-e81d91f2fbed | -6.2705 | -44.1996 | 2025-06-01 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ea8b3a5d-be32-3d00-9636-a43505840772 | -9.9329 | -59.9053 | 2025-06-01 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 3e634e4f-70c4-3d21-96d7-45362ee80611 | -9.9329 | -59.9053 | 2025-06-01 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| bf76f3dd-20e7-327d-8c5e-b8131c0e8d72 | -6.2705 | -44.1996 | 2025-06-01 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a1e72ff7-025c-30ee-b304-e1c0df03de4b | -9.4964 | -40.3088 | 2025-06-01 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.6 |
| f7dea65a-08d4-3f42-8af1-bef804702032 | -7.22072 | -43.13044 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dc1484d4-56b3-311d-b7b2-918e71c7416b | -9.33472 | -40.29357 | 2025-06-01 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3d5b12af-cd31-3d70-ad38-6d5934a04bbe | -8.073 | -34.97727 | 2025-06-01 03:15:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ee5d42ec-8cf0-37bb-830f-77fef69d5955 | -9.29616 | -38.27325 | 2025-06-01 03:15:00 | NOAA-20 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8064c64b-7230-36b6-8a00-449610e5368a | -11.79948 | -41.19432 | 2025-06-01 03:15:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 0264737c-553b-3297-a4e0-ac7866315d4f | -9.33271 | -40.29337 | 2025-06-01 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d31f72d1-e215-34ba-b542-8801f15ad96b | -7.21351 | -43.12917 | 2025-06-01 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README3.md)
