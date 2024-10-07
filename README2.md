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
| 34f2be9f-054c-3c31-aa3f-8722473e7ba2 | -18.659 | -57.2552 | 2024-10-07 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 5b5af964-fc5f-3ef4-ab41-add1657b9be1 | -18.7176 | -57.3097 | 2024-10-07 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.9 |
| c9514f08-13a4-3f98-9307-2a2d787917c7 | -18.718 | -57.289 | 2024-10-07 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.4 |
| e39c52d1-ed85-3bc5-866b-8c570844749a | -18.8886 | -54.5587 | 2024-10-07 00:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 0dfdd258-f207-3870-8c34-a6f0e5a3d194 | -19.8318 | -42.3542 | 2024-10-07 00:06:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| 33afac1f-1bed-3154-8f63-c677f5f7b0ff | -20.4661 | -47.6592 | 2024-10-07 00:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2227d254-e5dd-38cc-a147-72adac60da0b | -21.0712 | -47.2331 | 2024-10-07 00:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 8ea83d33-e209-3990-90ca-7281526eb60a | -21.0719 | -47.2094 | 2024-10-07 00:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 783183b4-4782-3bc8-b8e4-4f5c8f9e322a | -21.0919 | -47.228 | 2024-10-07 00:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ea458470-9f62-3f98-8339-955042666443 | -21.0926 | -47.2043 | 2024-10-07 00:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 111f9cdc-d9f8-3476-8553-b3a043af89ac | -21.5843 | -47.9536 | 2024-10-07 00:07:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 982fd0b8-add0-3f83-98f1-c54b81c21e7d | -21.585 | -47.93 | 2024-10-07 00:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 3f5ee217-a8b5-3ccf-b90e-b5c62b4362d5 | -21.605 | -47.9485 | 2024-10-07 00:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e74f2367-68ce-3e47-99de-738ebbea2af3 | -22.1974 | -48.1778 | 2024-10-07 00:07:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 86de4aaa-eb5b-394d-8e6f-b5b3e9a6349e | -22.2183 | -48.1726 | 2024-10-07 00:07:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d9657a87-29b6-3127-a771-f5a62a4aadd5 | -1.0182 | -53.739 | 2024-10-07 00:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 170e6d60-0b77-30e2-b0e2-9e259a103344 | -1.0182 | -53.7189 | 2024-10-07 00:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 1f5250db-9752-3a40-88fb-a69115205c21 | -1.0365 | -53.7389 | 2024-10-07 00:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 98136de9-cce6-3602-8784-8af78ba79c77 | -1.0365 | -53.7187 | 2024-10-07 00:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 5910ec18-5ca8-324d-bac4-3e4272dfb9f9 | -2.2113 | -53.7029 | 2024-10-07 00:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 8f002243-17e6-3cec-a8cd-e9b0e56f0402 | -2.2114 | -53.6828 | 2024-10-07 00:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 31f9cbab-2927-35f4-b8e4-a5c5e4567d8c | -2.2297 | -53.7026 | 2024-10-07 00:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ab1debc6-afde-3499-b210-522aac8e0355 | -2.2297 | -53.6824 | 2024-10-07 00:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| cc50aa13-5f01-3a0d-b903-b74c6638f76f | -2.8569 | -52.9197 | 2024-10-07 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 94c2c949-6b3f-3b54-9a0d-fdc27d2d15b4 | -2.857 | -52.8993 | 2024-10-07 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 204.7 |
| a09a958e-8379-3db6-9564-890c33bc851f | -2.8753 | -52.9192 | 2024-10-07 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 289.9 |
| 9d06f52c-b51f-3d7f-b7f6-b2511df626f8 | -2.8754 | -52.8989 | 2024-10-07 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 366.5 |
| 2d200a3f-2f08-37b3-9562-10689b1bf7bc | -2.8937 | -52.9188 | 2024-10-07 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| fb355f02-ea3d-3cd8-9dcf-b4f573b1f03b | -2.8937 | -52.8984 | 2024-10-07 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 71bcbe57-31f9-39b7-ae87-fb88fd7c23ad | -4.2728 | -43.7601 | 2024-10-07 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 11f9735a-3e60-341f-857d-c4f2125dc4b6 | -4.2729 | -43.737 | 2024-10-07 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 199.7 |
| a95539ce-8973-3d73-b17f-627f155c1196 | -4.2914 | -43.7591 | 2024-10-07 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d0042708-8ec9-30f6-bf2c-d58f8dfc830b | -4.2916 | -43.736 | 2024-10-07 00:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 0e360169-488d-3d8a-87d8-eeb5799b695d | -6.6944 | -35.0907 | 2024-10-07 00:15:43 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| 14f9252d-9886-3ef4-bc28-0d7b4cb8c64d | -10.8754 | -63.9169 | 2024-10-07 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c24d995c-be18-3f76-b57f-cb01b7619f6f | -10.8755 | -63.8979 | 2024-10-07 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ea04ef34-74b9-386f-ba1d-36db92d93ff9 | -10.8942 | -63.8971 | 2024-10-07 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| daed4ca0-f9d7-387e-922c-0a5887f5e8cf | -11.2657 | -51.3898 | 2024-10-07 00:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| fbe88411-453f-3f29-8b6a-3f327dacda2b | -11.7566 | -44.4897 | 2024-10-07 00:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f8c48940-80c3-351d-86a4-158fad7251bc | -11.7373 | -44.4926 | 2024-10-07 00:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 9fcced65-0376-3569-903f-671ca1ebe43b | -11.5233 | -65.137 | 2024-10-07 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e86c2953-23bd-3145-b7d1-090a994fef86 | -12.0585 | -63.7841 | 2024-10-07 00:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 05e14f5c-45f0-3a32-a319-b8c573fdb411 | -12.4973 | -47.0118 | 2024-10-07 00:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 52330849-577e-36dd-8c3e-1cdb913dcc67 | -12.4977 | -46.9892 | 2024-10-07 00:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 4e0b1012-993e-32e1-b934-eadc0a93c34c | -12.4981 | -46.9666 | 2024-10-07 00:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4724b59f-ad29-3b4b-b4cf-522b0af36757 | -12.5165 | -47.009 | 2024-10-07 00:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7a6c54b1-f0c9-3566-a39b-1f864e49e0c3 | -12.5169 | -46.9864 | 2024-10-07 00:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| b0a0bc28-7f44-3558-b4ee-2884281a0d86 | -12.7089 | -40.2155 | 2024-10-07 00:16:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 0618414e-cc50-38ee-bd1d-d929a44d5977 | -13.8354 | -44.6398 | 2024-10-07 00:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b615c8b2-3db8-33c3-ab4d-4baa348df3d5 | -13.8359 | -44.6162 | 2024-10-07 00:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 70e2519b-17ae-3b5c-8595-67afdf0cd291 | -13.8554 | -44.6128 | 2024-10-07 00:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 09eebe4e-b39e-327e-bbfc-dafbc0e93830 | -13.7342 | -60.6471 | 2024-10-07 00:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| c2ee6d42-98d6-3aa1-ae82-281ff8492570 | -14.8765 | -58.0093 | 2024-10-07 00:16:30 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9a1ce78b-7d4d-3081-93ea-8870ede412ef | -15.0422 | -51.24 | 2024-10-07 00:16:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| b6f09faf-d39d-37a9-8c66-3b6b184e422b | -15.0426 | -51.2184 | 2024-10-07 00:16:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8b75111e-390d-3c6c-96a7-781ac9ab6e95 | -15.8887 | -57.481 | 2024-10-07 00:16:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e8dd0085-cae4-376c-8f22-91acafc489f0 | -16.4918 | -53.9543 | 2024-10-07 00:16:39 | GOES-16 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| b9ae597d-a179-315e-be99-b5c0ea8b7188 | -16.475 | -57.294 | 2024-10-07 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 9e5e8a5b-ac00-3927-b248-4297075a28af | -16.4753 | -57.2735 | 2024-10-07 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 4b12cd24-5e69-33c0-b804-0e771d385b97 | -16.4756 | -57.2531 | 2024-10-07 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| ab68206b-c0e6-33b4-b162-1f5ecdb4b0f7 | -16.5072 | -57.7387 | 2024-10-07 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 9c916f94-99b2-33cd-bc6a-b8e2ee843413 | -16.5267 | -57.7365 | 2024-10-07 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 136.9 |
| fe53349f-2380-37fe-8b55-59a011612bea | -16.6199 | -55.5684 | 2024-10-07 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.8 |
| 01c39b8d-08e6-3488-97f4-92423f7b02b4 | -16.8178 | -57.8466 | 2024-10-07 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 43f73cad-129e-3349-8848-7ec697b58dfa | -16.8181 | -57.8262 | 2024-10-07 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 9d0fd29c-9dcd-3268-acf2-7f41c1f25745 | -16.8377 | -57.824 | 2024-10-07 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 9a968ce4-7859-3c3c-87a2-d9a00f3dd52f | -16.838 | -57.8036 | 2024-10-07 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 72d33f7d-3939-3823-8376-d0a55920bb24 | -16.9711 | -56.8058 | 2024-10-07 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| f9e97947-6c24-3e09-a85c-3fc710c5c2fa | -16.992 | -56.721 | 2024-10-07 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.7 |
| 9f4b406f-8406-3e7d-9fc7-29d57bf009cb | -16.9924 | -56.7003 | 2024-10-07 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| 0631978a-66ea-3996-bb0f-f8902a96a5ab | -17.02 | -55.0791 | 2024-10-07 00:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 72c34dc8-1fe1-3f3b-ae3a-48283012e047 | -17.0116 | -56.7186 | 2024-10-07 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.7 |
| 2386e88b-f53d-3a10-bd53-93d1dc089903 | -17.012 | -56.698 | 2024-10-07 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.1 |
| 2137b902-8a11-354a-b069-846f4ed6ab64 | -17.0123 | -56.6773 | 2024-10-07 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 7596976e-20ad-3929-8e12-fc9a1fe6f212 | -17.1581 | -57.3582 | 2024-10-07 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| a0ed75f2-b0b9-3909-a01c-766c9bbe6adb | -17.1584 | -57.3377 | 2024-10-07 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 21d052db-4314-3065-9746-bdcff33fab1e | -17.3149 | -55.0603 | 2024-10-07 00:16:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| b483925a-cbed-3f9e-a0a7-93b8585602f2 | -17.6283 | -53.088 | 2024-10-07 00:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 1e070d12-b5cc-348a-8780-f2ccae317552 | -17.6477 | -53.1064 | 2024-10-07 00:16:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 23736501-1702-3896-96b4-7907bf013353 | -17.6481 | -53.0849 | 2024-10-07 00:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 1b512b2f-9e54-3b79-b219-208c4d4fc5ff | -17.6485 | -53.0634 | 2024-10-07 00:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 2805dccd-530f-3981-9d7c-513d3e68fddf | -17.6679 | -53.0819 | 2024-10-07 00:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 188.8 |
| d8c63197-c59f-3750-a1f2-fa7bb05af6be | -17.6684 | -53.0604 | 2024-10-07 00:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 01c913dc-c1f3-3ab3-b9cb-496078389dc8 | -18.0192 | -42.1166 | 2024-10-07 00:16:45 | GOES-16 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| 9c11458e-c568-3025-b47d-07e0150a77c3 | -17.7724 | -53.7918 | 2024-10-07 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 365.8 |
| 2dd64b67-911b-3ed1-a02f-5f6931fc4a87 | -17.7728 | -53.7705 | 2024-10-07 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 55213178-c756-3969-ac94-635ad977f0f9 | -17.7324 | -57.0833 | 2024-10-07 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 43df44b3-4d87-3deb-a569-a23658e93dfe | -17.7918 | -53.8102 | 2024-10-07 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| cca7009d-9b86-3197-abbe-b5a3a854864f | -17.7922 | -53.7889 | 2024-10-07 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 555.5 |
| 928b846f-0020-3237-b74d-d6d5caa38463 | -17.7926 | -53.7675 | 2024-10-07 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 411.6 |
| f1850eb9-396d-36cf-b216-2550155a1233 | -17.8319 | -53.7829 | 2024-10-07 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f90d0840-133c-3790-a29f-6755d01c4472 | -18.4718 | -53.5134 | 2024-10-07 00:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 900e7891-2bca-32e0-8756-5fc33a2c9aa6 | -18.4722 | -53.4919 | 2024-10-07 00:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 68ce67ba-63e2-311c-802c-b518b0b3e130 | -18.6391 | -57.2578 | 2024-10-07 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.4 |
| 3c9cc9a9-abb0-3f79-990c-5118167e4956 | -18.659 | -57.2552 | 2024-10-07 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.7 |
| b7c36660-44ec-3b68-a9a2-008e17dd5cee | -18.718 | -57.289 | 2024-10-07 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| aa72406a-2784-365c-b0fe-d32169015bca | -19.8318 | -42.3542 | 2024-10-07 00:16:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.2 |
| 61e2261b-cc29-336d-b182-a9c96317dae3 | -19.761 | -45.3217 | 2024-10-07 00:16:55 | GOES-16 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c7a5f13a-e9c5-339f-9efd-1360530e5d9e | -19.8279 | -43.7737 | 2024-10-07 00:16:55 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d4db9aff-711e-3423-bac9-b55e3446cf64 | -20.1229 | -49.0518 | 2024-10-07 00:16:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 194.5 |


[Clique aqui para ver as próximas entradas](README3.md)
