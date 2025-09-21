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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d392daf6-8377-3593-befb-669f020cda0d | -5.5771 | -42.1493 | 2025-09-21 12:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 9cffbbbe-d203-3719-8454-8228e39924f7 | -12.6088 | -45.1244 | 2025-09-21 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 255.0 |
| 693248b8-da01-3739-99df-56da1b759f7a | -15.55785 | -42.66715 | 2025-09-21 12:00:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| cb276fa9-7ed9-3097-915f-07a41542d99b | -9.99934 | -46.24579 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d20c5dee-1acc-3851-bef0-e0e90241a1fe | -12.61169 | -45.10957 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0a86710a-9642-30e1-9773-ffe1e1642aaf | -14.43589 | -47.56955 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 51d96940-261a-36f3-a0b2-ffd2dd416098 | -12.0262 | -42.50023 | 2025-09-21 12:00:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 72362ff6-e7b8-335b-84d3-1746beb5e386 | -15.73339 | -43.0607 | 2025-09-21 12:00:00 | TERRA_M-T | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e21e8dc9-9de7-39fe-ae9d-6e37d9a97b59 | -11.51271 | -43.62494 | 2025-09-21 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dbf2b817-f857-32d8-8cec-0ec39ea6f200 | -10.26336 | -46.07043 | 2025-09-21 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a2019561-9785-31b0-93ae-b64bfb0721fe | -13.90648 | -42.16501 | 2025-09-21 12:00:00 | TERRA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 306f4b51-315a-3cf3-ab70-90a65053e409 | -14.32295 | -47.79035 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 15872e19-4870-3b56-acdf-a69c1984d073 | -14.97515 | -44.41721 | 2025-09-21 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 182a4b7b-a539-31a0-87e1-7e163f5a8981 | -11.49535 | -43.55698 | 2025-09-21 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 94ad4cf0-bbbb-32c7-997c-78638422653d | -13.14371 | -42.02076 | 2025-09-21 12:00:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 8c2d712b-81cb-3da4-912b-8b10f216e7c7 | -13.53846 | -43.009 | 2025-09-21 12:00:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 06f91202-0255-350c-9c4c-89e1a0d62ba2 | -12.37962 | -47.2267 | 2025-09-21 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| a50c69c4-8d3d-3eb2-bbf8-246bc79ff754 | -17.06754 | -43.79134 | 2025-09-21 12:00:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ba7f3842-b670-3219-88c7-bde45cf3d61b | -11.50024 | -43.5857 | 2025-09-21 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 76395fbc-113c-3deb-bdcc-f777e51caa39 | -18.28327 | -44.30958 | 2025-09-21 12:00:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| edc926a0-4d41-3097-b3e7-d67a7efb3459 | -17.07763 | -43.32506 | 2025-09-21 12:00:00 | TERRA_M-T | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| eefc34d4-c066-35f8-84db-2447c7f2b015 | -14.79703 | -42.83699 | 2025-09-21 12:00:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 765b59d8-de1a-33a6-b0ce-60c690f81075 | -10.2958 | -46.11938 | 2025-09-21 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 18330c2f-f536-385e-977b-c53ed9e46fa3 | -17.12722 | -45.92899 | 2025-09-21 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| dc0fa536-a136-33af-8847-4ba10d292df8 | -12.9925 | -42.24657 | 2025-09-21 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 50e60e02-8fc6-3374-97c3-5ae1536c7f03 | -14.97377 | -44.4265 | 2025-09-21 12:00:00 | TERRA_M-T | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2eaddf02-52d7-32a8-a1e8-fa8a0893e781 | -10.04695 | -46.25957 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| c4539b04-9c8b-3979-a0b5-e1fef10f58e8 | -12.43801 | -45.10141 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 4794542e-52ac-312a-bf5c-60d0afcef7c5 | -14.85266 | -45.48208 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4220e19c-4f33-3fbc-9898-f36fb12ddc14 | -12.45098 | -45.11966 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 251334af-b44d-3325-820b-2759e732c2bf | -14.50637 | -43.90385 | 2025-09-21 12:00:00 | TERRA_M-T | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d2d3e353-0f9b-3ed9-a707-979e35712b76 | -14.85114 | -45.49216 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 395d2bca-c256-306d-bf37-46b88b4e252b | -12.49194 | -46.69028 | 2025-09-21 12:00:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0789706b-707c-325f-9353-08ae58a9a556 | -11.94288 | -46.93143 | 2025-09-21 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3206aa8b-30c5-3591-8424-94e911c8975c | -14.31832 | -47.79766 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c8a7795f-8ce5-350a-b4be-06ae1ac3f3e2 | -14.47241 | -46.49429 | 2025-09-21 12:00:00 | TERRA_M-T | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 88884a1e-92ed-3932-9db0-6da21466820a | -12.28981 | -45.28168 | 2025-09-21 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 885f9510-d30c-3f28-be00-1905e21a8626 | -12.54471 | -42.4765 | 2025-09-21 12:00:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3851e519-54aa-33f1-b8f2-2579a01918ed | -11.49401 | -43.56611 | 2025-09-21 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 0c89d2fd-7382-30de-80f4-c1f7f56e6a8b | -10.56639 | -42.58397 | 2025-09-21 12:00:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 27719271-0f6d-3b79-a82e-fd92b534a9e5 | -12.71441 | -46.85358 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 3eb260d4-ffba-3edb-aeb3-7d010065018e | -12.89194 | -46.82991 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 826c73a2-357d-3c29-a6b2-dd1d93cc3374 | -18.72968 | -43.89077 | 2025-09-21 12:00:00 | TERRA_M-T | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 032e5da5-eeb5-3727-a86f-2bb899cc3e99 | -13.04102 | -42.22534 | 2025-09-21 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| ca8ced47-14e9-3302-8599-39aafaeea9c7 | -14.50623 | -45.26952 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7ca5781d-1ce7-35b2-835e-c84299e57628 | -17.12565 | -45.9391 | 2025-09-21 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| f202e16e-969f-32bd-b5e8-fbbc3f2a74d9 | -17.11325 | -45.9578 | 2025-09-21 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b9427cd2-36db-3df9-a60c-a94dbc147a37 | -12.72254 | -46.84801 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6610068f-f841-384c-9025-0d57c6e83b66 | -17.11483 | -45.94768 | 2025-09-21 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3e368101-b9ea-36a4-aed2-87e366983c44 | -12.69549 | -46.83851 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3720e924-10f6-3da0-b22c-882e86644a0e | -12.69746 | -46.82595 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 5f08567a-7f2e-3ab2-843b-afffc257973d | -15.69062 | -43.75283 | 2025-09-21 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 05057761-790b-385a-ae60-8892295c1df3 | -19.81124 | -46.66817 | 2025-09-21 12:00:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 06f00102-b89b-3147-a09a-b2173dc4e853 | -12.43845 | -45.13874 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 8e2b1bdb-0e68-3c17-95a3-c84d77184454 | -13.22669 | -44.0741 | 2025-09-21 12:00:00 | TERRA_M-T | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6a9b216-a193-30f5-86c6-fd846ebc25fd | -12.60084 | -45.11819 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 2f41fed8-69db-3b01-927b-891992bdffd7 | -11.42654 | -43.52183 | 2025-09-21 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 26eac2e9-0e12-3c58-98a6-57026ca76b51 | -17.40145 | -45.52808 | 2025-09-21 12:00:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a3d35185-b031-3ac1-89b7-50835a171bb3 | -16.23087 | -46.65885 | 2025-09-21 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 729ee05e-1f2f-3822-ba71-cd04474af19f | -13.39776 | -42.17901 | 2025-09-21 12:00:00 | TERRA_M-T | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 8fda7449-9a9a-380a-a3fc-a63c06724537 | -14.51951 | -44.8722 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bef3fd67-1281-3d02-a29c-a551c8f8d884 | -12.40502 | -45.00342 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 70665977-ebf2-3be1-b8b7-93fba5c181d0 | -15.55653 | -42.67655 | 2025-09-21 12:00:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 217a8185-2830-332a-8fa4-5ca350f9f100 | -15.8831 | -47.29578 | 2025-09-21 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 73706e4e-620a-3905-9ce8-99986aee8d44 | -13.04232 | -42.21616 | 2025-09-21 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 216106db-da0a-3cd0-809e-3bc67dca82d2 | -13.4384 | -45.89676 | 2025-09-21 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1871f9c8-4aa5-3eb0-9393-3e643feb47ef | -16.63621 | -44.34933 | 2025-09-21 12:00:00 | TERRA_M-T | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6f0c3069-bf9d-34b5-a1f4-f9246dac3088 | -17.53269 | -43.94967 | 2025-09-21 12:00:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7da10357-f6f0-338c-aa3b-1b01030add7c | -12.01734 | -42.49898 | 2025-09-21 12:00:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| bf498bb5-f758-33f2-923e-a26b6da02a8a | -17.70692 | -44.08299 | 2025-09-21 12:00:00 | TERRA_M-T | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8b98d10-5caa-3893-8983-8227ee8b1126 | -14.52095 | -44.86266 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6138cbb5-63b8-3ad5-9f6c-1191a68142d3 | -12.40351 | -45.01343 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b7632016-3575-303b-ad36-08a5c992d9d5 | -14.62396 | -48.26801 | 2025-09-21 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| aebeef7b-b10d-3dec-84e2-086967ea1499 | -13.03209 | -42.22409 | 2025-09-21 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 81.3 |
| b1c5613d-81e7-3b55-bef0-27e1e2f75cbc | -16.00038 | -47.27155 | 2025-09-21 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cfc01872-2182-3813-8147-eb60e57cf7f5 | -12.60236 | -45.10807 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b9f8060b-b202-3fcf-9bfe-71892b6edec7 | -14.86195 | -45.48351 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 67b0510e-0872-3271-8ecb-17c4330fe8e1 | -14.4373 | -46.51657 | 2025-09-21 12:00:00 | TERRA_M-T | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7c9d5f4c-49e2-315d-9740-fda771ccfc09 | -17.07893 | -43.31578 | 2025-09-21 12:00:00 | TERRA_M-T | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8377f4e8-eb97-3470-a986-5961e4bbc982 | -10.01815 | -46.26178 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 7e49b712-4f9a-39c2-beef-481e499d7a66 | -14.50473 | -45.27947 | 2025-09-21 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 0106cdf9-58f4-3377-bdbf-305b772f855f | -16.48368 | -46.56126 | 2025-09-21 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8885d781-0b07-3b58-a00a-f5151fc16dde | -12.01606 | -42.50796 | 2025-09-21 12:00:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| c1113728-e8e1-30eb-a215-c82242d670c9 | -12.61018 | -45.11965 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 0546fafa-6012-3361-857f-3147c8cfa8f3 | -10.03046 | -46.25093 | 2025-09-21 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 05b06413-4e16-3872-b6f8-4e4e6362fa31 | -15.73468 | -43.0515 | 2025-09-21 12:00:00 | TERRA_M-T | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 43058d87-f537-38a4-9a85-eb980d3452fd | -12.70783 | -46.82758 | 2025-09-21 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 70ea888e-9d80-3f7f-817b-4290f0b93b22 | -17.11796 | -45.92751 | 2025-09-21 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cbe60aaa-ab5a-3bb3-b7fd-063811e769bf | -14.13622 | -42.36858 | 2025-09-21 12:00:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6b094117-7f33-39c7-a805-3ecfcf3fb294 | -15.69193 | -43.7437 | 2025-09-21 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 42003a27-8b20-361f-85ef-fd6fe4eca915 | -12.44003 | -45.12849 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7e5e34ce-e948-324e-af3e-40fb226ba406 | -12.19266 | -43.20359 | 2025-09-21 12:00:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9c3997b0-d61b-3a14-82e3-4efcb3e77a9d | -13.03338 | -42.21492 | 2025-09-21 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 294.4 |
| 426e6ad1-50fe-3110-a4b8-a96d0e642485 | -12.36889 | -47.22493 | 2025-09-21 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6fd4df59-7c25-3217-87f1-558a0f2aa0da | -19.80962 | -46.67856 | 2025-09-21 12:00:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6388daff-da45-3f41-b27f-3913da3ae0f3 | -11.48509 | -43.5648 | 2025-09-21 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 79865da2-aabd-3c6b-8334-2526a4b16144 | -12.44162 | -45.11824 | 2025-09-21 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| d27b617f-a44c-341d-87ca-9c2d76c76dd7 | -10.29391 | -46.13159 | 2025-09-21 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 32578c73-af7e-39ce-9380-58d661684ea8 | -10.64664 | -44.48833 | 2025-09-21 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e42376c1-c39d-3f2e-8936-326f9443a818 | -12.10849 | -47.9183 | 2025-09-21 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README49.md)
