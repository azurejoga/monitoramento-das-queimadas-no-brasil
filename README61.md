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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 334176f6-c1fd-3e89-b12d-5a2b4e16c4b6 | -10.8942 | -63.8971 | 2024-10-03 03:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 962b80bf-7e8d-3151-a9e1-0c2bc11be32f | -11.6744 | -64.9793 | 2024-10-03 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 7480e680-2ac8-3eb4-874b-92fb4fbd6ead | -11.6931 | -64.9974 | 2024-10-03 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8519cbea-40d2-30b8-b172-b5c60012bd99 | -11.6932 | -64.9785 | 2024-10-03 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3e576baa-dd2f-3165-96d9-53e5335b6799 | -11.6743 | -64.9983 | 2024-10-03 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 19a86924-240f-3e7b-bfee-dedebcb70800 | -12.4038 | -63.0009 | 2024-10-03 03:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 1acf6f39-1db9-385b-87e4-f93bed989143 | -12.404 | -62.9817 | 2024-10-03 03:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 945a4f3d-4a31-3b89-854a-8db8c0482396 | -12.6295 | -63.1225 | 2024-10-03 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a9070930-c986-339c-857c-c00c181b1f88 | -12.6484 | -63.1214 | 2024-10-03 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 499de9c4-9822-3d74-a819-36161c314051 | -12.8808 | -62.4731 | 2024-10-03 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cfbdcdb3-0b35-32c5-998f-18789e8de0ef | -12.881 | -62.4538 | 2024-10-03 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7c063386-acc7-320a-a2b4-4eb5c2c0dce8 | -12.8994 | -62.5106 | 2024-10-03 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 7ea2f1c0-ea53-3f3d-83d5-4595d513f7af | -12.8996 | -62.4913 | 2024-10-03 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 153.0 |
| f6ee1540-ba68-3184-ab0f-b81e22bcf9e0 | -12.8998 | -62.472 | 2024-10-03 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 144.9 |
| e28d0d8a-4965-3d4b-a2b5-8f93cabfbdcf | -12.8999 | -62.4527 | 2024-10-03 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 58f4f78b-3c5e-3a45-a357-358f6955ecbc | -12.9741 | -62.6409 | 2024-10-03 03:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 030ffdc4-93a4-3dc6-b543-bcd00bfa70f6 | -15.7417 | -48.3842 | 2024-10-03 03:26:34 | GOES-16 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 6fbfc25d-30c8-3f97-b336-3d18735182be | -16.5783 | -58.198 | 2024-10-03 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| edad66df-a85f-39a6-ba47-7a9b37bef41d | -16.578 | -58.2183 | 2024-10-03 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| a46f38d4-1f0f-3a9f-8f38-24fb65515531 | -16.5588 | -58.2001 | 2024-10-03 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.4 |
| e042c4c7-1059-32e5-b052-706cdf11152b | -16.5585 | -58.2204 | 2024-10-03 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 155.9 |
| ec0c92a8-5056-3e31-9788-90987cb39d01 | -16.5582 | -58.2407 | 2024-10-03 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| c8218a4e-7efe-37eb-b29e-7e87031781d3 | -16.779 | -57.8306 | 2024-10-03 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| b90b05db-5a59-3f21-8cff-878efbd46176 | -16.8983 | -57.6949 | 2024-10-03 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 7a100ba8-eb34-3ee9-8459-496d8da09f3d | -16.9179 | -57.6926 | 2024-10-03 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 8d31a411-2b2f-38a1-b725-0b8dbc1719e8 | -16.9176 | -57.7131 | 2024-10-03 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 5000a7bc-8cf6-3a1d-9c43-c3ade93d2460 | -19.0344 | -43.1944 | 2024-10-03 03:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.8 |
| db18c081-749f-3d9b-a992-cd7f784f84b1 | -21.306 | -47.6227 | 2024-10-03 03:27:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0d08e734-9bab-3e0f-acfd-a990ec2d7e32 | -2.92505 | -41.469 | 2024-10-03 03:32:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7c68e055-b113-3fc0-88ac-ebd3ce97dd6c | -2.91984 | -41.46818 | 2024-10-03 03:32:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cb0a5874-c199-3275-9458-fefc788fc6eb | -3.40928 | -42.32408 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 415e4e8b-1274-3821-a8f0-f4717db11383 | -3.40908 | -42.29122 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7832f3cc-0ac8-3ba7-b85e-ddaaad795492 | -3.40888 | -42.33182 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc3abcaf-a31e-3abb-a784-4be91a3472b3 | -3.40869 | -42.32765 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 56b9297f-de49-372e-aa08-c39136625b06 | -3.40851 | -42.29471 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35ac199b-b367-3d46-8781-fae0d8ac7b43 | -3.40824 | -42.26244 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7ff0985-ff28-3b09-b757-8ee0081aaccf | -3.40811 | -42.33118 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54741573-da66-3e2e-b075-e07dac7e5d0f | -3.40794 | -42.29817 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 389465b3-1e76-3b6b-8ac6-4ef5b6db246b | -3.40754 | -42.33464 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8849bf63-5c1f-3f4c-ab2b-a5895885b525 | -3.40707 | -42.26947 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 9595c9a2-c041-341f-9b1d-4ab0434f494b | -3.4065 | -42.27291 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 82a97048-07eb-3512-b301-84c2dac71924 | -3.40538 | -42.27969 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 269.4 |
| 0f80dd81-2cba-3c9f-972b-64138b09965d | -3.40501 | -42.31593 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 509cd41e-c217-32f3-ab8b-8b9033b0d1fe | -3.40443 | -42.31942 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a705cc9-6c85-33b5-a7db-5682e0b4ff21 | -3.40422 | -42.28672 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| affc9eeb-af9d-3793-bf76-c75bf7bdf29f | -3.40364 | -42.29023 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 44354a52-05e7-37b4-a761-925af9d93c83 | -3.40306 | -42.29374 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0f94e4a-bb54-328b-b6b2-ddb596c5a4be | -3.4028 | -42.26151 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aa4aecb-3187-3efb-a6d8-0fd4f291a434 | -3.40266 | -42.33018 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8949ac1a-32d4-3f03-b2f7-1022d110029e | -3.40249 | -42.29719 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d403a223-59dc-3073-843f-de5a51ab1e9f | -3.40209 | -42.33365 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a081b878-0dcb-32c9-904b-3cbdaa8b1b09 | -3.40192 | -42.30064 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d60a01d-d1ac-32b3-9bac-4893aebab0b4 | -3.40164 | -42.26846 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 5ba8ccfa-09cb-3737-b52b-18d19d42f489 | -3.40107 | -42.2719 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 3879c82a-0c12-324d-b3ec-ff8087096e83 | -3.40016 | -42.31129 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b39e865-0dd1-3800-9e1a-d02b477a4753 | -3.39995 | -42.27866 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 269.4 |
| f6c3f581-f248-303e-a3ea-330d6edfac83 | -3.39958 | -42.31483 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d48698b-625b-3a8e-9760-c06b57b18257 | -3.39937 | -42.28217 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3a94ae74-f309-3d9a-9b5d-b9fdb9fba5d4 | -3.39879 | -42.28571 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5e5140c2-de0b-3003-b9e5-49b75a7af534 | -3.3982 | -42.28925 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6328f677-c51b-3da3-be80-d91d4d92e943 | -3.39762 | -42.29276 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 75f41ae5-6508-376f-beb9-f00ff0324bcc | -3.39704 | -42.29627 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe6ec8ad-c3eb-3893-b597-6f5d9a943ee0 | -3.39647 | -42.29971 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d730873-f6ab-3c45-97aa-2a0128495889 | -3.39566 | -42.2708 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8a19709-639f-3574-8dc3-68e9b0c26248 | -3.39509 | -42.27422 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 16e9a00c-b205-3617-8b3f-7edc1186d0e6 | -3.39452 | -42.27765 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 286a520c-71bb-3e9f-be48-ee3cb6aeb361 | -3.39394 | -42.28115 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8b8625ea-7ded-3751-afa7-458a592c37ac | -3.39335 | -42.2847 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6d11bd40-afbc-3ad6-b720-1075369db1c6 | -3.39276 | -42.28826 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7530e91-7b11-3422-96c8-5d6008a0408b | -3.39217 | -42.29177 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 053107bf-4bed-307e-b978-7f72f3319e75 | -3.39022 | -42.26982 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 006e54b7-5ac4-3465-972b-59db1a04153e | -3.38966 | -42.2732 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec8d06ed-7e1a-3089-b188-25d5dfd237f1 | -3.38909 | -42.27664 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f6ca4a1-e38b-3898-aa4c-80a9e1107c97 | -3.38851 | -42.28012 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6d4b178a-6341-3eff-a74b-a293d66141ca | -3.38479 | -42.26881 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cc69335-e6b6-3cd0-be07-0bf4f59bcc10 | -3.38422 | -42.27224 | 2024-10-03 03:34:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4bc4405-411a-3fd1-8653-9c0b8d42ff5c | -3.38365 | -42.27568 | 2024-10-03 03:34:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a6e7aa2-b471-31b6-998c-2c32895bf82a | -10.12809 | -37.23254 | 2024-10-03 03:34:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4475d364-5489-3f8a-8c34-47ac22141b78 | -10.12751 | -37.23151 | 2024-10-03 03:34:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6d7720ee-ade5-35a9-96c2-f252a6ed7239 | -10.08476 | -36.48171 | 2024-10-03 03:34:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| aa437908-e001-32a1-8fa6-ca97295b9ac1 | -8.43185 | -46.2994 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8ea196c-8639-3ee7-8c04-b597d35dbf8d | -8.42988 | -46.30962 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cf50878-b221-37c0-a4a0-ee0879be4977 | -8.42563 | -46.29746 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61a81d4e-a8f6-3b7c-a70c-113469da6ec4 | -8.42557 | -46.85089 | 2024-10-03 03:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48a2299f-1aba-3817-86f6-b15015675743 | -8.42535 | -46.29831 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6674cb9b-f781-3eeb-b596-74a30e3c4b60 | -8.42465 | -46.3027 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a80a8445-c7f0-3ef1-8d75-15ab37bcfc6f | -8.42444 | -46.85667 | 2024-10-03 03:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 368aabcb-be97-32ba-9aa0-be997b7ba16b | -8.42435 | -46.30351 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0658cfbe-aa1f-3f6f-be86-ee1bd37c5920 | -8.42374 | -46.3076 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 420a51dc-a0f8-3de0-8e96-d3e2e5e00c5a | -8.42342 | -46.30834 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b41b23ca-71cc-3d8c-b734-1e8b13c5d710 | -8.41631 | -46.31153 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1168938-26bc-3e41-9e78-e9e430d3c615 | -8.41594 | -46.31236 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4beca39a-165a-3709-9eb9-9738f1a08d8c | -8.41533 | -46.31678 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8700cfb-0213-311b-93dd-07c61fad7f8d | -7.90555 | -46.42698 | 2024-10-03 03:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92810088-3cca-3387-8e09-09cbe93014ed | -7.8506 | -46.25729 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04a73a7a-3700-3ea5-8ee3-6f1ab1d137f6 | -7.84957 | -46.26281 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41dc960b-c721-398b-b6af-33b1d2238d8a | -7.84949 | -46.25997 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5f55b06-f64c-3228-9db5-923b78534ebf | -7.74207 | -46.15799 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53c1d92c-f946-326b-8662-406f82825381 | -7.74089 | -46.16427 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d406e610-c99b-3e93-a300-61307c3ff943 | -7.73669 | -46.15092 | 2024-10-03 03:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README62.md)
