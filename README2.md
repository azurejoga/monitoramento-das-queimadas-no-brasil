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
| 927db4b1-507a-3f3e-aabe-aa77363580cc | -18.03876 | -39.92674 | 2025-03-11 03:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 80f528b9-3f21-33ff-a016-c678852da864 | -16.75467 | -47.73525 | 2025-03-11 03:55:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 390cf6bf-9db6-35f1-933d-abf8a416c3c8 | -20.30233 | -41.35579 | 2025-03-11 03:55:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c0e7eb32-63ef-3ddb-bc5f-84d48a4921ad | -14.56948 | -46.72174 | 2025-03-11 03:55:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ebba277d-06bb-3d7c-ab99-430cf1c41a63 | -15.34508 | -43.71383 | 2025-03-11 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af5e27f2-b161-32f6-8ff0-51f27f65fa91 | -20.36722 | -45.35471 | 2025-03-11 03:55:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f4b5a009-f30f-3942-b8d3-09f77191dfdf | -18.9262 | -42.47934 | 2025-03-11 03:55:00 | NOAA-20 | GONZAGA | MINAS GERAIS | Brasil | 3127503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fb528090-3235-3b56-8b6c-b57e0948622b | -16.3482 | -43.69756 | 2025-03-11 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8616e91-d786-3478-aed7-e7ad6ac18466 | -16.6108 | -43.33262 | 2025-03-11 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 142ec08b-44a5-3bd4-b446-93a7bbcb96f1 | -16.61011 | -43.33668 | 2025-03-11 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 574c657b-926f-30e2-9de3-aeb775254626 | -16.67928 | -43.88543 | 2025-03-11 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb0ef1a1-902f-3705-9935-24467c416b70 | -15.91697 | -41.34891 | 2025-03-11 03:55:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4b9a9c28-94ae-384f-ad47-8ffe438faab1 | -17.67495 | -42.74421 | 2025-03-11 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1de34e7-23f7-395c-8d7b-8896fbdc1d96 | -14.9065 | -48.13741 | 2025-03-11 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bac98d4e-09f8-3c45-a689-ff9a7f7b2d83 | -15.67899 | -41.58065 | 2025-03-11 03:55:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42f4873d-1eed-3d37-b8b3-6e8f4e3cec50 | -20.3062 | -41.35272 | 2025-03-11 03:55:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 24e75a3a-779e-38bf-9a14-83736db07714 | -16.18658 | -44.27596 | 2025-03-11 03:55:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74fc3ff6-64e7-30fa-b690-e46844c48c13 | -15.07872 | -48.9465 | 2025-03-11 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b3598f3-b670-3025-a733-7acd329b2c99 | -19.53721 | -44.07818 | 2025-03-11 03:55:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef871b8b-e29a-3bd3-adb6-e41d1b85fc8b | -14.8583 | -45.19483 | 2025-03-11 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 231f17cb-f543-3745-a18f-7b5d81061850 | -19.6911 | -40.54241 | 2025-03-11 03:55:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 47c0bc68-2118-3b36-9ec1-d94bf8469fdf | -15.94315 | -48.1179 | 2025-03-11 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dbfc457-479a-3d32-95d1-f0baf471ffef | -16.58917 | -44.40036 | 2025-03-11 03:55:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edc3ace6-c277-3f1b-9aa2-606cdc4695d4 | -15.94419 | -48.11247 | 2025-03-11 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bd8869a-b06a-307e-bf8e-3244472321a9 | -20.3029 | -41.35213 | 2025-03-11 03:55:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9ee9374c-ce84-3f22-9b85-de14e7c4508f | -17.75141 | -42.89624 | 2025-03-11 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd65ccf6-e661-373a-b1ba-b3ecf9dce426 | -16.33052 | -42.02217 | 2025-03-11 03:55:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 950cd555-e1ab-3cc6-bb77-3c7e49773ffa | -17.09254 | -43.80386 | 2025-03-11 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c18f299-a418-3702-a0e5-d047781867ef | -17.67558 | -42.74038 | 2025-03-11 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| adfb98f7-b7c2-355e-815d-14b449aedfb5 | -15.56748 | -42.68025 | 2025-03-11 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 56eab1fe-2409-3a5a-9ae0-4b68304e90c3 | -18.9256 | -42.48305 | 2025-03-11 03:55:00 | NOAA-20 | GONZAGA | MINAS GERAIS | Brasil | 3127503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43cfe2ee-e7ad-3a39-8415-555eda0cbf35 | -20.30564 | -41.35637 | 2025-03-11 03:55:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1ae27795-2230-3567-90f1-34d7b2c13832 | -14.5651 | -46.72085 | 2025-03-11 03:55:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9978622-21ee-375f-8212-35ba68a7f7cf | -22.65545 | -43.14894 | 2025-03-11 03:57:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53b67adf-6cab-3935-a697-e90de8716dbb | -21.60972 | -48.47588 | 2025-03-11 03:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beec7296-c339-3571-9f29-4adb804657d6 | -21.74055 | -45.8902 | 2025-03-11 03:57:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f227536f-440f-3c5b-b6c4-3143811e6175 | -21.73684 | -45.88945 | 2025-03-11 03:57:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b72591cf-41ab-341f-8bd9-f4d17edf756e | -21.73865 | -45.89252 | 2025-03-11 03:57:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9f4e49e8-5192-36d6-ad15-beb48f6af6c0 | -22.69822 | -43.63087 | 2025-03-11 03:57:00 | NOAA-20 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 64ad6798-aef3-3916-8c3c-de63b9fafe56 | -21.73948 | -45.88783 | 2025-03-11 03:57:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7eb15a08-f304-356d-9db8-675eff41e878 | -26.86885 | -50.67693 | 2025-03-11 03:57:00 | NOAA-20 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e22a105c-5d4c-39fd-b351-b2f7d3dc7fd2 | -23.9846 | -48.91824 | 2025-03-11 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66ba7744-eba5-3c8c-83fe-37a9413ae6e2 | -21.61403 | -48.47684 | 2025-03-11 03:57:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6ea047b-5783-3429-8a9c-0a23b572308a | -2.82898 | -51.77055 | 2025-03-11 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27ce5ad3-e526-3001-ba63-1751ced7bc27 | -2.53228 | -53.95803 | 2025-03-11 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 109eb57b-f5db-3dbd-aaa4-2f9ca840cbcf | -2.53425 | -53.95671 | 2025-03-11 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f64cb4-a941-3150-a990-7bb44749a5c5 | -10.40234 | -47.98562 | 2025-03-11 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ff9ebe9-ff37-3bab-9985-91f68a58293b | -10.39923 | -47.98054 | 2025-03-11 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeda1720-3949-3e7f-b4b9-a2b8521ae962 | -9.92571 | -59.90493 | 2025-03-11 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f2fffa32-0041-3fcb-9abe-c287fc270f79 | -9.98963 | -48.08946 | 2025-03-11 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a74d359-fca4-34ff-8a08-4d3be8563cbb | -10.39857 | -47.98508 | 2025-03-11 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b02599f0-f9c1-3617-87f6-4c21fad1030a | -10.88149 | -54.11095 | 2025-03-11 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03321f38-bdcd-3ac9-a544-fda9d628afa5 | -10.403 | -47.9811 | 2025-03-11 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e793144-44f1-390a-9a84-2e3a1f370f46 | -10.40366 | -47.97653 | 2025-03-11 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8425ad3d-a971-3e44-be0e-5ee1d1793bc5 | -11.57653 | -47.63005 | 2025-03-11 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a014ec2-39de-3711-961a-f34f426f1a16 | -10.35918 | -47.77332 | 2025-03-11 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ec9bc8e-6a86-3e1d-98d2-b8fc7a370063 | -13.04733 | -40.33847 | 2025-03-11 04:46:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b8c3032b-72a3-327f-8c0d-580b3bf2c3b5 | -10.35851 | -47.77814 | 2025-03-11 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8cdbf24-1ad5-3c00-9be9-e031e044faae | -10.40168 | -47.99015 | 2025-03-11 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20e56ddc-678a-382e-a8e2-a37d8163165a | -11.57261 | -47.62949 | 2025-03-11 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5f74bf6-4838-3031-be5f-7f4b508176d8 | -16.67958 | -43.88539 | 2025-03-11 04:49:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51e8d4f9-4330-33d9-97c8-bb2799f5781a | -15.94192 | -48.11363 | 2025-03-11 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d531f82a-4ac1-33eb-b724-04a9eacaba80 | -16.34776 | -43.6971 | 2025-03-11 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7282096-b7d5-3a77-81b4-25d0848d3bbe | -15.94597 | -48.114 | 2025-03-11 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e2fb20b-1794-3e52-8288-6fb232297b0a | -18.18055 | -39.62338 | 2025-03-11 04:49:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| d879da08-e9e8-3414-a7cd-6cd391b01430 | -16.81334 | -49.39175 | 2025-03-11 04:49:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a8a055c-2c32-375f-ae0a-8f9fbc551f1d | -19.73732 | -42.1172 | 2025-03-11 04:49:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e782c9f0-931a-305a-9581-d077c62bbc17 | -15.78882 | -50.35526 | 2025-03-11 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47201af5-14e8-3b01-b1de-3e4ed28cc3cc | -16.75664 | -48.60521 | 2025-03-11 04:49:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cda070d9-8131-3269-adb7-f97619535327 | -16.77722 | -50.64253 | 2025-03-11 04:49:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffa3578e-4db2-371f-a8b8-655faf3eba3a | -18.17624 | -39.62547 | 2025-03-11 04:49:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 390d29b7-40d8-3e87-949d-a1410e9f8412 | -13.94085 | -48.95989 | 2025-03-11 04:49:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23744783-0719-3f67-b6b4-817b86913e1f | -14.19694 | -45.7534 | 2025-03-11 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a63f7c80-2f0a-3a9c-b780-7fa961a4d566 | -14.57122 | -46.72158 | 2025-03-11 04:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2704d92-913b-32aa-a0eb-c055fcf170f8 | -14.56689 | -46.72099 | 2025-03-11 04:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb08be40-902c-3757-b3e5-c8fca96f8078 | -15.56912 | -47.85529 | 2025-03-11 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f178518-b78a-3fc1-ad83-9717a6e91c60 | -14.19235 | -45.75278 | 2025-03-11 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25437425-2efb-36ca-95f0-911cdf3245a5 | -13.89057 | -43.80555 | 2025-03-11 04:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47c29c7a-bd4d-3d28-90c4-3eaa4b4884b8 | -15.07932 | -48.94463 | 2025-03-11 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66f9bddc-6e7e-3cb0-927c-bce171c1b8fa | -15.34667 | -43.71405 | 2025-03-11 04:49:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5704fcd-2b97-399a-9313-e622af4bde27 | -21.17053 | -44.30252 | 2025-03-11 04:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8d171a70-36ec-3b27-b8be-cb3802b3e6e2 | -25.96626 | -52.60356 | 2025-03-11 04:51:00 | NOAA-21 | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fb7a3ff9-907c-3233-8002-83f8002326ce | -21.17088 | -44.29885 | 2025-03-11 04:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c691ccc2-1667-397a-b5bc-f2ca6fb0690b | -20.28796 | -50.97601 | 2025-03-11 04:51:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dd0e84f4-89fd-3482-ad16-ba00d3033e68 | -21.17104 | -44.30102 | 2025-03-11 04:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 20ef3f6e-0b39-3007-b2f8-d22ed22e139b | -20.31255 | -45.58221 | 2025-03-11 04:51:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86353ac9-f726-3d8d-9523-2fe0258b05cb | -28.58553 | -49.44302 | 2025-03-11 04:53:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c62e46e9-9e7b-33cf-b89e-4aa059df33ee | -31.89556 | -51.97324 | 2025-03-11 04:53:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 33390e7e-7e79-3222-96ea-5da1dd1d862d | -31.89284 | -51.97134 | 2025-03-11 04:53:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 043edc49-1be4-3c61-8727-5baeb5d8e589 | -26.97001 | -53.01816 | 2025-03-11 04:53:00 | NOAA-21 | SÃO CARLOS | SANTA CATARINA | Brasil | 4216008 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 27247e33-f645-3426-abe5-1ac21e354690 | -2.04279 | -50.79382 | 2025-03-11 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2818bb84-cae3-3237-b8f3-f8e01ff3e7e8 | -2.5338 | -53.95618 | 2025-03-11 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 497201fa-ef33-3ee3-9e4a-410f66dbe6fb | -11.86401 | -58.05465 | 2025-03-11 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31f24dd6-bd49-3b91-a862-9a3cc4a84667 | -9.92802 | -59.90442 | 2025-03-11 05:12:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95e1d1e3-4aea-3bb5-b349-612a5d10a57d | -14.90526 | -48.13406 | 2025-03-11 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64b3f7bc-9e2f-3761-a7da-01753baeb319 | -9.57959 | -57.39566 | 2025-03-11 05:12:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc235218-fb54-3679-89ab-754170e54f3e | -14.91127 | -48.13497 | 2025-03-11 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12ca77db-07ca-3988-b727-5ff870ea7a50 | -15.94867 | -48.11146 | 2025-03-11 05:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c988df36-be8e-330d-b1b8-53d4cdce4c53 | -15.94201 | -48.11581 | 2025-03-11 05:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22d9173f-5d13-3f4f-99b2-6da27fa56166 | -15.94248 | -48.11138 | 2025-03-11 05:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
