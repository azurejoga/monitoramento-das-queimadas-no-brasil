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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd391022-6f02-3c30-be91-a57e75f369b3 | -3.6065 | -59.4413 | 2026-09-22 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b765b564-95d1-3b14-8c86-665ffedfb331 | -3.0358 | -54.4085 | 2026-09-22 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e7b78908-b5a5-3d9b-a6cc-30f768080ca8 | -6.1178 | -59.8877 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 42d816fe-2a7f-3532-8162-9728c6cc7eab | -5.9333 | -53.5362 | 2026-09-22 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a8f686df-ff50-3a88-8362-9defb45058ef | -6.8985 | -41.6976 | 2026-09-22 15:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 151.7 |
| 72d1c4b0-3567-3d0a-8486-942eec699a34 | 3.7498 | -60.4684 | 2026-09-22 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a02c26ac-d57f-39af-b766-3cdb9c44e3bb | 1.8395 | -56.0582 | 2026-09-22 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 270f99cb-52f7-3281-b435-bd06c8e6f117 | -3.3493 | -59.8479 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 55eae8d2-e54a-3710-9a49-16b2401c138f | -12.0833 | -50.0594 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 17468f26-fe52-3f43-a924-159e206cd1c9 | -3.1719 | -57.832 | 2026-09-22 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 408cd0ef-91a6-37c6-9c46-781fa835987a | -6.8573 | -43.71 | 2026-09-22 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9cb7e691-b4af-3857-866c-9705c014c729 | -3.2817 | -57.8685 | 2026-09-22 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| ed6e8d75-d827-36c5-83cc-5231cc1ed60d | -2.9525 | -57.72 | 2026-09-22 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 2578cbb2-77ec-38cf-8d76-1718d933885b | -11.1367 | -51.1284 | 2026-09-22 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 506485b9-fc9d-3aa2-857e-1c4429cf10ca | 3.9716 | -59.7393 | 2026-09-22 15:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 49922baa-62ac-31eb-8138-ddbff87944aa | -3.132 | -59.029 | 2026-09-22 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1e63c44f-c8a6-3261-aad6-5ad5daaaae4e | -3.4186 | -61.3084 | 2026-09-22 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6eacae6a-0dab-3569-bd0d-de996fbd8a7f | -10.379 | -54.3979 | 2026-09-22 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6e63d57f-a867-30ca-a22e-d3d3ab8dd1d6 | -6.2018 | -47.5902 | 2026-09-22 15:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 0aedf781-c68f-3dd2-afb2-f0bb0dc9eb9d | -5.8241 | -43.8424 | 2026-09-22 15:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 20cde8cf-f3ab-3770-9aac-818ebfed0c58 | -3.2211 | -53.9623 | 2026-09-22 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 225b5aa0-642b-3560-80a1-779ddd93425f | -12.1027 | -50.0355 | 2026-09-22 15:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 930d96de-936f-32cd-9183-354cccd82775 | -12.6608 | -50.9549 | 2026-09-22 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| e7fee48f-2624-38f2-8bc5-160fd11785c9 | -3.3493 | -59.8288 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5596e069-be96-3225-b60d-5e19e3a81690 | -3.7547 | -58.8622 | 2026-09-22 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 55d9269a-2afb-3e6a-9b02-00ced4bc5464 | -3.2818 | -57.8491 | 2026-09-22 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 92daedce-3b77-366d-b8c6-3055b754403a | -7.2673 | -44.043 | 2026-09-22 15:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 7d78bfdc-9e5d-37f9-817b-e867ec146ed9 | -12.3481 | -50.1994 | 2026-09-22 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 6f851ec2-8c76-3abc-a1d9-0c51ae18838d | -3.3 | -57.8681 | 2026-09-22 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 047ab19e-05e1-3bf0-a89b-72314ed564da | -8.3764 | -47.2802 | 2026-09-22 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c8653744-1983-3607-b8ce-5bebb4b12273 | -5.9148 | -53.5372 | 2026-09-22 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0e41462c-f2f7-38c5-894a-c11aac7ac34c | -6.6767 | -58.7105 | 2026-09-22 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 2c93be35-44ec-3831-b24d-7c53cba48b8d | -7.5548 | -48.6843 | 2026-09-22 15:00:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 3fce4e22-623a-32e3-8005-e373e5119020 | -3.331 | -59.8483 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 5f7c5c5a-0348-355d-805a-de57c0267347 | -14.1258 | -45.5904 | 2026-09-22 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 272.4 |
| 825d6912-6daa-31d9-b139-164904de203b | -9.2468 | -57.1686 | 2026-09-22 15:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 47dfe862-00f5-3817-ac26-609eb7db8802 | -7.785 | -44.8212 | 2026-09-22 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 8dc4d5f8-78cb-3dc7-961a-2cf86b5de147 | -12.283 | -50.7011 | 2026-09-22 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| a094629c-29e1-318b-a334-f9d66cd9e51d | -12.6796 | -50.974 | 2026-09-22 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ac4c5c17-d969-3ede-a424-ce36ba58089c | 3.859 | -60.6371 | 2026-09-22 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 13e62979-b060-38d5-a98f-af4ae7de49bc | -12.4182 | -45.0385 | 2026-09-22 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 05dc3450-d3c1-36eb-964d-21a5282a1d6a | -11.4349 | -45.3689 | 2026-09-22 15:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 206.0 |
| f7068b10-8bfc-3bbd-8e17-cd3dcd29f332 | -3.6449 | -58.8647 | 2026-09-22 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f832ebe4-f5dd-36b4-8135-aff4aefc417f | -2.9906 | -57.2137 | 2026-09-22 15:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 75cebd31-9ad0-3360-abc3-3a94524411df | -5.8239 | -43.8656 | 2026-09-22 15:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 6e8eb9fa-6989-380f-b43f-79ec1b01a020 | -11.1337 | -49.9978 | 2026-09-22 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5a63c67c-0fd0-366a-bbac-7e7a1a73b19c | 3.859 | -60.6561 | 2026-09-22 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 593cda52-98a5-30c4-8aa0-e0d9ff4f522d | -6.9681 | -47.5119 | 2026-09-22 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 531adedd-9455-3295-a8e0-519944e55349 | -11.118 | -54.0268 | 2026-09-22 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ba226e47-9324-314b-a001-edd9dd117407 | -6.1111 | -57.6645 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 304.4 |
| f13ab845-552c-3c6b-91a7-798d2c3a7e84 | -3.1901 | -57.8704 | 2026-09-22 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 54bbb4e5-a5a2-3c4f-9d1f-10292071bf71 | -10.2632 | -50.0055 | 2026-09-22 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 1f87e3cf-723b-3895-8733-227e0f7dafc7 | -3.2955 | -59.4476 | 2026-09-22 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5d28eac5-0614-3c65-b4b2-55d7572ceb52 | -3.2183 | -61.0472 | 2026-09-22 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 57a5d7ea-afcb-3ca4-a09c-ac114b35da69 | -10.4536 | -51.325 | 2026-09-22 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| ff8ef1c8-9773-34d3-adff-5358b01328c0 | -8.7919 | -44.2546 | 2026-09-22 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 40cb6570-65fa-337b-b70e-2166cf101252 | -2.5492 | -58.0179 | 2026-09-22 15:00:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 1a6c4d63-ce49-33b7-b09a-132259605fbd | -6.9228 | -42.8852 | 2026-09-22 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 42503aef-cebf-3d17-8826-e7273bd6699f | -6.4301 | -59.9916 | 2026-09-22 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| e1305bdf-29ca-348a-b5e9-6c19aaa88a32 | -6.9225 | -42.9088 | 2026-09-22 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 5504b44e-ac49-3ca8-a98a-eb44628e15bc | -6.295 | -57.735 | 2026-09-22 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| f6f26011-b66e-376d-83f2-9043399a202e | -6.7464 | -59.4223 | 2026-09-22 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b62bb33c-b950-3563-a9ee-a24e016baad9 | -3.3134 | -59.6003 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d11dfade-cd4c-363e-b629-27efd217e9f4 | -4.0925 | -62.0874 | 2026-09-22 15:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 4b1b16bc-9995-316e-9f6a-74d3c2d23df7 | -10.6889 | -50.6658 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b361040d-a663-3f02-b098-bc7822f13c16 | -6.3195 | -60.0147 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 75986930-fb1e-3eed-9648-6f701f31c9fd | -10.3732 | -50.2508 | 2026-09-22 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 031d7982-0991-30a4-8a0d-ed744df16949 | -3.4634 | -58.329 | 2026-09-22 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 17f901db-53a2-3b2e-a752-9abb289d1d99 | -3.2955 | -59.4476 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c8a590d7-67cd-314b-9243-6202b00706e0 | -12.9081 | -51.0314 | 2026-09-22 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2491f738-b24d-3ac6-8dae-a23dfb6fd9a3 | -5.9333 | -59.9899 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 8cb351fe-5e68-3251-aa6a-fbe2f3a069e3 | -11.3817 | -44.0319 | 2026-09-22 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 250.0 |
| ebf0d76e-75de-3e1e-b47c-37731afb7d23 | -1.4301 | -49.0168 | 2026-09-22 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5b531451-7672-3fdd-826c-9b12c1233a2d | -3.478 | -59.597 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 78c3f895-40e1-3c6e-9d5c-b9274b64d361 | 3.0563 | -60.0629 | 2026-09-22 15:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2d109729-53ee-3b25-8fb1-adb4c39fe38a | -1.9484 | -56.5868 | 2026-09-22 15:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6603cada-0992-33bf-988d-4f59d2b7ccbf | -3.0717 | -61.2764 | 2026-09-22 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f6e29144-78a3-370d-ad88-99b5320d5fb0 | -8.845 | -45.9391 | 2026-09-22 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c0a61200-8525-3632-87cd-c819bb2432a3 | -12.3478 | -50.221 | 2026-09-22 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 548ed0ba-6dce-317b-85be-3db4efd01c75 | -6.8985 | -41.6976 | 2026-09-22 15:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| ab71f836-d35a-3a9a-873b-ed0993fb5d60 | -7.0029 | -49.7551 | 2026-09-22 15:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| a4f9bbad-dc70-39a3-806a-5bc3b8eee522 | -6.3013 | -59.9771 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 683a514a-36cc-3f60-b498-7b5ebbfab47c | -3.3493 | -59.8479 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 115b7d1b-4208-3797-befd-44406556dc34 | -6.4484 | -60.0101 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 9cdf4747-a496-34d6-9366-913ab8d5eeac | -11.4527 | -50.2409 | 2026-09-22 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| aba8359f-8a77-393c-b1aa-8f951ba952e4 | -10.379 | -54.3979 | 2026-09-22 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| afe18c2b-8c72-3e9a-b2cd-82996bd4be41 | -5.8678 | -45.2346 | 2026-09-22 15:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 57535c08-eacc-3f39-8c08-b14e219ef142 | -9.2468 | -57.1686 | 2026-09-22 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 3fa5c9d6-cc27-3fdc-8899-254183afe122 | -8.7706 | -45.8567 | 2026-09-22 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| f338bcc5-a9ae-317d-a3b6-7106a5d4ef71 | -10.7437 | -50.8089 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 30f21086-f5fa-3bcb-8031-69bc5b5f4a53 | -9.5595 | -66.0172 | 2026-09-22 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 91fc1d7e-7e94-3cee-8f22-7e62f162412f | -12.2834 | -50.6797 | 2026-09-22 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9f213183-72d2-3cf9-a400-cc5751728b5d | -11.44 | -47.3579 | 2026-09-22 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 83734bdf-289c-3d0d-99e4-7663548aa5ee | -6.1111 | -57.6645 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 230.8 |
| 8b89d25e-7839-314d-b15b-405c0c8a9c1d | -14.1258 | -45.5904 | 2026-09-22 15:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 76f1a341-4d3d-378b-9f0c-1f1ddbc1e55e | -3.0352 | -61.2581 | 2026-09-22 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 694ebbb5-167b-3c07-895e-5298390e527b | -3.405 | -59.522 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 247.3 |
| a778b0a5-5016-3483-b27e-4db1a1020ce6 | -3.8279 | -58.899 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9ffcbcca-9680-38df-84dc-779b37c40ec5 | -6.7354 | -55.3074 | 2026-09-22 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 657ecce9-5682-3bb7-b089-9361ef39d340 | -10.1372 | -45.541 | 2026-09-22 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |


[Clique aqui para ver as próximas entradas](README147.md)
