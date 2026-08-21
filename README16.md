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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ec72520-9a7a-3eb2-a6d8-072947ef07a6 | -6.1178 | -59.8877 | 2026-08-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| bfca05d4-e019-3902-a797-5c58c3f6d05c | -13.9367 | -53.859 | 2026-08-21 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 416507f1-519d-3731-8f85-23806e63d920 | -11.1745 | -54.0421 | 2026-08-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| fb62dad2-0030-3485-96f9-6bbd67d7e198 | -8.3903 | -62.6963 | 2026-08-21 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2a33ef69-2598-36f5-b705-9dc4f31a47af | -3.5221 | -48.1896 | 2026-08-21 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f6142c8d-d949-3b40-ba0b-de299a20a3d1 | -18.0285 | -44.6113 | 2026-08-21 01:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 096fd86d-cd61-3859-bc5f-0db708fa99a7 | -11.1558 | -54.0233 | 2026-08-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 32a4acbb-d2bc-3a41-898e-5d2dadb29444 | -18.054 | -44.413 | 2026-08-21 01:00:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b01b96f1-000c-32e7-9ca9-579b7e27c2da | -7.36 | -45.8361 | 2026-08-21 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.1 |
| ead7f9fd-e89f-351b-8e37-047d9f66a6e1 | -6.2155 | -55.6316 | 2026-08-21 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| cb360651-dfbb-3b4b-a5e7-e06ec38a1c75 | -6.1361 | -59.9063 | 2026-08-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 56ed5872-ec8b-3a9c-b5d9-297805277d5f | -7.3603 | -45.8136 | 2026-08-21 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 390.9 |
| c6773357-0d33-384d-8f24-38d11ab3f0f5 | -7.3793 | -45.7894 | 2026-08-21 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 03bc1201-6ab7-3d6c-baba-08d87faf83b1 | -12.5104 | -54.755 | 2026-08-21 01:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3877ab62-b352-3603-a1d0-8d477aa9bfc2 | -10.769 | -50.3376 | 2026-08-21 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3a0a60b0-be22-39fe-afc2-c923ee383b06 | -3.5406 | -48.1889 | 2026-08-21 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 199.0 |
| f78317a3-ab8b-3cbe-83f9-a33d3bcc7440 | -18.1934 | -50.7554 | 2026-08-21 01:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 8f3568c0-b3e1-3bd6-954d-b9adfec2d951 | -6.8593 | -59.0318 | 2026-08-21 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| e6b7c04c-6cfe-3eab-b4f9-d4bc9a38ffae | -10.7693 | -50.3162 | 2026-08-21 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| cd62cb2c-8650-3570-9bca-65f86e4490ed | -6.6938 | -58.942 | 2026-08-21 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 1f89e2cd-5ec5-334c-ac14-18f0fdf83dbd | -10.3148 | -50.3848 | 2026-08-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 46650a83-ca19-3978-a75f-db19b54dadba | -6.6939 | -58.9226 | 2026-08-21 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f733c09a-e210-3972-9d81-14372d133646 | -6.2341 | -55.6109 | 2026-08-21 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 8ec73b07-24ae-3a8e-b4b9-50b05048f196 | -10.7501 | -50.3396 | 2026-08-21 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| df3079ae-4430-3661-a61d-8ca941335ee3 | -13.3926 | -54.3758 | 2026-08-21 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 174.2 |
| ea138246-8c90-3ac8-a9c8-f275a9218f6b | -10.3151 | -50.3634 | 2026-08-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| bb4bcf62-979c-3d3c-8ece-09d4aed018c1 | -13.3923 | -54.3965 | 2026-08-21 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 66fa4fd8-a41d-36f6-a873-33be733be056 | -10.8078 | -50.2693 | 2026-08-21 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 61eaedc1-b4df-3b0c-b269-b0afb2792965 | -10.8075 | -50.2907 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ed81a480-b48d-3f7f-bb72-f154d80a2e36 | -13.3926 | -54.3758 | 2026-08-21 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 0d6d18a6-8be9-379b-badf-b22094ffd7ea | -4.0943 | -42.5097 | 2026-08-21 01:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| dde3d82d-f3cf-3267-9e9e-0ba0b8f9a726 | -10.8078 | -50.2693 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7d1a0cdd-eda8-3327-878e-b2767ccce6b9 | -6.2156 | -55.6118 | 2026-08-21 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| be84a915-b78c-3f20-8af8-86006e0bc211 | -10.7311 | -50.3416 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b2cfed6d-ac96-363f-b22d-cfeecb13a202 | -11.175 | -54.001 | 2026-08-21 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| d0dc4bd2-347b-3a17-b1fd-821d85c6c6d5 | -10.2595 | -50.2838 | 2026-08-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 625453f4-f889-3205-8c23-d2bb1a366dc8 | -11.1558 | -54.0233 | 2026-08-21 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| ee54981c-df1b-37a4-abb0-9c6665c651ea | -18.1934 | -50.7554 | 2026-08-21 01:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0d74b89a-77d7-3caf-91d0-11b1d4e10e79 | -8.1574 | -46.7247 | 2026-08-21 01:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| cebe8608-e36f-31a5-8646-15029305b60b | -10.7504 | -50.3182 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 0ba6f23e-3397-3527-a3af-3e0e2d8d254d | -6.1361 | -59.9063 | 2026-08-21 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ba9ec93e-020f-3f2b-b14e-35b57da0633e | -6.2155 | -55.6316 | 2026-08-21 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1cdf3d08-6cba-36b8-9325-7a5a196f90a8 | -18.2134 | -50.7518 | 2026-08-21 01:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| cbfde984-910e-35b8-bcbb-736060e72d7e | -6.2341 | -55.6109 | 2026-08-21 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| e11f1940-118a-3739-8d77-4a2165bfa166 | -6.1177 | -59.9069 | 2026-08-21 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7953deaa-68a0-348f-bb52-95e99fe8a921 | -10.7501 | -50.3396 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 48fa255a-050a-32b8-b72a-af523dd41e6c | -11.1747 | -54.0216 | 2026-08-21 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 215.0 |
| a7f27679-bdaf-36af-94e6-60a5ba01edff | -10.7886 | -50.2927 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5410b776-9397-3c28-9588-39a07ec8b0b4 | -10.7693 | -50.3162 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ee17068c-bff5-394d-8a83-4139f5ab466f | -11.6719 | -48.3467 | 2026-08-21 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 659c58cc-f557-3c0d-84aa-3a4ea3a6b422 | -6.6939 | -58.9226 | 2026-08-21 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f75e2048-baaf-3101-99c2-a0a0febfd914 | -8.3903 | -62.6963 | 2026-08-21 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| cb901fff-edd4-3897-8d77-80ac62a398f9 | -13.4114 | -54.3944 | 2026-08-21 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 4f3e3f72-2682-3ddd-99ff-c952202f625c | -10.769 | -50.3376 | 2026-08-21 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 21ac75a7-e918-31a8-b3d3-8ef0283d3009 | -8.1572 | -46.747 | 2026-08-21 01:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 83b396d1-d25a-3ac8-b23d-4e101cf7bfa6 | -6.6938 | -58.942 | 2026-08-21 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 81f023b9-9c57-360b-adea-18d3093b2f00 | -13.3923 | -54.3965 | 2026-08-21 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c1b5327f-14e3-3236-9422-ca22de5eda10 | -10.2592 | -50.3051 | 2026-08-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 1e76b0d5-d400-3b49-ad7d-1ce7f882fdf2 | -3.5407 | -48.1673 | 2026-08-21 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| eb84628f-ff21-3f99-bac2-d1b496071152 | -3.5406 | -48.1889 | 2026-08-21 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 200.2 |
| 294c157f-9d2e-3c18-9272-9abc7d2ed4e4 | -13.4117 | -54.3737 | 2026-08-21 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 897a6124-8297-3f56-8981-f0b2b543b1a3 | -10.3148 | -50.3848 | 2026-08-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 13030bce-6901-3021-bdaa-7f37506180f3 | -7.34 | -45.8 | 2026-08-21 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e75de81-f9b4-3771-874b-8a3584f30f48 | -7.37 | -45.85 | 2026-08-21 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1be24dfa-4709-333d-95a9-b03e25a5dc8c | -7.37 | -45.8 | 2026-08-21 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47e82119-d98e-32b5-ac7e-b2da9f158387 | -3.5221 | -48.1896 | 2026-08-21 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ccd5d7eb-6921-3c5a-8856-86f6164dbb0c | -10.8078 | -50.2693 | 2026-08-21 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 36654229-1590-3ab1-9942-76ac67c85d8a | -6.6938 | -58.942 | 2026-08-21 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| f3cab60a-4887-3be0-9ee1-fc3df49da553 | -3.5407 | -48.1673 | 2026-08-21 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 168573ac-021d-3d03-ab3b-59e81a6f9113 | -18.2134 | -50.7518 | 2026-08-21 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d779447c-9432-3ef1-ae71-54eb50089738 | -10.3148 | -50.3848 | 2026-08-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| ccacece1-f6fb-3ddb-ba8f-d767dab43d5e | -10.7501 | -50.3396 | 2026-08-21 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 9303fae4-daa2-326c-9219-f926dd21d6e7 | -6.1177 | -59.9069 | 2026-08-21 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ceff1e6d-61c0-3568-84a5-d4a20908dd8c | -10.2592 | -50.3051 | 2026-08-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 15f7fb21-1fe6-3a84-a9e2-4bfcd88bec5b | -13.4114 | -54.3944 | 2026-08-21 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0d5ef839-8d45-35b4-a418-74fb41dbee79 | -10.7504 | -50.3182 | 2026-08-21 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 4e70d56c-ad04-3763-ab95-d14d03f74f7c | -10.7693 | -50.3162 | 2026-08-21 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6b850319-003c-312e-83dc-48b723ff5d47 | -18.0285 | -44.6113 | 2026-08-21 01:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2ac183ce-6f6a-3a3b-80ad-8fba3108c90d | -10.8075 | -50.2907 | 2026-08-21 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9effd3aa-779e-369f-b263-7a8d0ffac7c4 | -6.2155 | -55.6316 | 2026-08-21 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7843d8e5-0915-376a-817d-29898fe58d9f | -6.1361 | -59.9063 | 2026-08-21 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 05024d93-22a4-313b-b9a2-bba91d4b664b | -11.1745 | -54.0421 | 2026-08-21 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4420b2cf-f2d8-355b-8566-553f82e91c70 | -6.2341 | -55.6109 | 2026-08-21 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 4ae4bef4-99a0-3c48-b013-afd687490518 | -6.6939 | -58.9226 | 2026-08-21 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 95e441e5-81f4-3c1a-84cb-925766a5f0fb | -13.3929 | -54.3551 | 2026-08-21 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 928f83e6-8ed1-344c-b536-0e4009f33160 | -8.3903 | -62.6963 | 2026-08-21 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 85b1a52e-1c33-3163-a3fa-d2b545ba4b6c | -10.3151 | -50.3634 | 2026-08-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 10fda518-6dfb-3f33-8b13-2eebe0ac03e6 | -18.1934 | -50.7554 | 2026-08-21 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e458be6c-2979-31de-9c2f-d4e5d1a1c828 | -9.2071 | -59.771 | 2026-08-21 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b7d424a8-4edc-3aaa-96b8-48053d83c263 | -3.5406 | -48.1889 | 2026-08-21 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 2475e88b-a38c-3b54-8fee-c0aee93dd25c | -11.175 | -54.001 | 2026-08-21 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 5bc9f03a-aec7-307d-b1f6-a4a310391ec5 | -13.3926 | -54.3758 | 2026-08-21 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 241.2 |
| d2e8b045-b600-349d-9a91-b8ed37057bfb | -4.0943 | -42.5097 | 2026-08-21 01:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 13a7733a-8e70-333d-aa92-cb8cede42e94 | -6.2156 | -55.6118 | 2026-08-21 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9522ba19-be40-3248-b4c4-d9d105966cfb | -13.3923 | -54.3965 | 2026-08-21 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 5f1bf40e-a649-389d-9ab6-d08c7f60eca3 | -11.1558 | -54.0233 | 2026-08-21 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 46a06cf7-dbbe-3092-a2a1-bedcb5bfcea6 | 2.5983 | -60.697 | 2026-08-21 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7a6f0d6d-8d82-3739-a3ba-9815b398c549 | -13.4117 | -54.3737 | 2026-08-21 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 9c629f65-b46b-35af-a1e2-50a43c12b4fe | -10.7311 | -50.3416 | 2026-08-21 01:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 925f2947-3e0e-3cee-94ae-ba78af0cef9c | -11.1747 | -54.0216 | 2026-08-21 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 224.4 |


[Clique aqui para ver as próximas entradas](README17.md)
