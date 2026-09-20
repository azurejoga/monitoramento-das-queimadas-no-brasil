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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dcc72ca-a327-39f4-93ac-93873bbb293e | -9.00145 | -45.00136 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e17bd08-747c-38f7-88ce-090f23e1e86e | -5.41428 | -44.2744 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ef2b499-a039-30c6-aafb-b4180696f46a | -7.48887 | -46.70861 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a97fe7f-49a8-3724-bf04-50e7a11ea57e | -9.2835 | -48.19536 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e712cbe-de78-336c-9ac6-ecea72211a58 | -9.77202 | -46.0749 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a9d62bb-2ed7-3cb3-b052-c54876453631 | -9.23967 | -46.22552 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 546bd86e-4870-3a81-b472-d4b14a569921 | -7.74495 | -46.74194 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ada1b808-c666-3d0c-b78b-f7d8380a1c25 | -7.5917 | -43.44335 | 2026-09-20 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21cdea4f-5a2e-300b-be18-c64d39a2e520 | -11.66232 | -43.41734 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6e28d030-182c-37f4-823e-778cf7e9a93c | -7.36125 | -44.86966 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7116a011-d6ab-3934-8712-0a76fd819795 | -8.0508 | -46.28477 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b0e63a35-670b-3400-918f-5ae6c58325e9 | -8.68385 | -45.42427 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa244759-7beb-3392-89a0-d37c9ba1927b | -11.80041 | -46.85302 | 2026-09-20 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44ba7d9c-cc31-3559-bfd8-850130263325 | -9.25732 | -46.19057 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86b1aef5-e9b0-3a56-8074-155b3321225f | -5.838 | -53.5357 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0e2044c-bcd4-30d5-b1a8-75223a83fe98 | -10.82774 | -50.9322 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f08af10b-0076-3446-be25-680a9a3d03cf | -8.18321 | -54.7566 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3393d1c3-2ef7-3b4d-bc93-96572f0099bb | -9.02685 | -48.78016 | 2026-09-20 04:19:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f32fb8f-07de-3731-8244-459fa556c6d6 | -5.40349 | -44.2727 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de5d0702-7741-35a3-bd1c-1a833856e403 | -11.09389 | -48.28971 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 574648bb-29fc-3885-ad5d-ddc86311f314 | -7.82824 | -45.27052 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6dc939d-9ec5-3410-b92f-4a7754dc0bf7 | -4.81246 | -45.77401 | 2026-09-20 04:19:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 004a6f8f-3561-3b52-acd0-f4fa832c0117 | -5.28498 | -49.34246 | 2026-09-20 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c661528b-c95c-3264-a22e-e01cded43ca3 | -11.49249 | -47.79044 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 462470ed-84a9-366b-9430-84225b0bdaca | -5.26334 | -44.48597 | 2026-09-20 04:19:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25bd6bfc-bd84-3588-bd04-e373e9def6ae | -9.79227 | -48.32309 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1005f02c-0b4d-39b0-a875-c945dc5af15d | -6.65198 | -47.73649 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8adbaafa-24bb-3b06-8154-0f65bc373802 | -7.44568 | -44.74205 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 799aceb3-95b8-31d0-a9f8-ec2ee6ca993b | -7.427 | -44.74337 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f08114c3-f36e-3f84-b751-358a54e260b0 | -2.81555 | -54.71583 | 2026-09-20 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c9ef040-3a2e-3521-9bba-186e0833a507 | -7.53648 | -45.4333 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 920f2323-66fa-3925-a9b4-ac3a0845788b | -5.848 | -53.55374 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f5aacdc-5f3b-387e-8daf-8f8d2de4766a | -5.80132 | -43.76391 | 2026-09-20 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23214b8b-3c9d-3f53-bbf2-6a48aa2c8da6 | -8.77257 | -48.73306 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b48a2b2-ef22-3b77-92f7-68608f758102 | -6.3113 | -41.75663 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 076011e0-3722-323a-a6b2-dd5fca6a6f7d | -11.06476 | -44.68579 | 2026-09-20 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3c87480-1711-3b51-8c04-57080f557a33 | -6.6569 | -47.47029 | 2026-09-20 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d6801a9-31ef-3f3b-9aad-4e6235d7ba70 | -9.71807 | -47.22398 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e41d433d-0373-326c-84dd-d10c329e71ca | -7.05951 | -47.5396 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5d1ed2f-148e-3c9d-8706-9b33c9f893e4 | -11.63851 | -47.76598 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f8cc73c-eab8-3cf2-9fa2-6ef8f88ef534 | -8.44568 | -43.86143 | 2026-09-20 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d77365e5-97ba-3d36-a1c6-15d03ce266a7 | -5.31496 | -45.24595 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc08b9fd-111b-36e9-a8e1-8deb38b5477d | -10.40557 | -48.92496 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 428313c5-2544-39d2-83ce-414494d8a312 | -5.36093 | -44.32189 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b7bc8ae-100e-3c61-bf40-0cc8b4ef4d9a | -10.49095 | -46.2831 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 764a6157-f877-37d2-a705-efc63ef8bf8c | -7.49691 | -46.70994 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 394352ff-ce38-33ef-8c5a-27f83bb88921 | -8.05306 | -46.29506 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6fe34601-141b-3432-8b5c-bc1019c92092 | -7.29956 | -46.74351 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d3f497a-e7d9-3400-8496-700feaa5d48a | -4.17874 | -49.4072 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6b64e59-63e5-3c7f-bf94-9d5b3c02b16e | -7.54831 | -45.38518 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa8a0cb2-a9de-3e00-b9bf-cae8b001d8a1 | -10.39176 | -48.89997 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1921b10-b50f-38d8-b7e8-31464ae2ca93 | -5.83734 | -47.79269 | 2026-09-20 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ea8a13d-b38d-33b1-9723-ddb080390fed | -6.22643 | -44.69118 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f81ab285-c447-3a20-8e8d-6aa2b2b032a4 | -10.19477 | -44.14791 | 2026-09-20 04:19:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a51c70ce-c4a7-3c02-80e6-6874734c68e7 | -9.04348 | -48.76453 | 2026-09-20 04:19:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 747babac-f5ff-3ad8-bf92-b4cf20f3ec79 | -4.07455 | -52.11814 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6306fd55-c60e-38ea-b301-5a175f94589d | -10.29223 | -50.20959 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d15ecebd-a1fb-3ed3-be60-9bf0e212f68d | -5.67165 | -45.30566 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f13ef632-bbec-3c71-aefd-d7abb61772ef | -3.39478 | -54.06818 | 2026-09-20 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 095d8445-5c7d-3267-912f-79572f7c5c64 | -7.30356 | -46.74443 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0d75c72-a878-3650-9c65-e5000de9f607 | -8.60829 | -47.31076 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74ef4b53-6828-3b1b-807e-90f98794deff | -6.39956 | -43.18958 | 2026-09-20 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae6841ad-bcea-3960-8269-678e7be53deb | -6.40365 | -43.74622 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3274f2fe-7fc8-32dd-8839-569cf79843fd | -8.42746 | -45.86189 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b46b262-699f-343f-8fda-888f25d246ec | -11.23709 | -48.38452 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ab05f0a-697d-3f35-8e4e-41b459107888 | -5.85451 | -53.55467 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a694635a-9201-3c49-be1d-4a025ce26657 | -6.56154 | -42.55789 | 2026-09-20 04:19:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b7759564-c042-3335-a9ba-958f525c9c02 | -5.84841 | -53.51563 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2311040-ff8d-3f49-b3bf-2aecc0acd6b2 | -7.16898 | -47.45438 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ade1ee4-ac38-3751-96eb-4ff01ecffbeb | -9.71941 | -47.26409 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54533ace-8e3a-30a4-9b6e-159f0b9114ae | -8.17407 | -54.77944 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47cff0ec-917b-3068-bf09-730e07b3cc38 | -8.7628 | -48.6729 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 22.6 |
| aaf8d130-d2f8-3bc8-8ae2-99c18a6e6ad9 | -10.4061 | -48.36336 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7467d4be-44a6-37b0-a1d3-91db657431d2 | -7.30946 | -42.26612 | 2026-09-20 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3ea945c-9daa-3ded-84f6-ec7feee17f41 | -5.83292 | -47.7919 | 2026-09-20 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22938718-e2e0-37f0-89ce-4210b210990b | -11.04001 | -48.30018 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9d780ff-871b-3894-97f4-2f4100baa41c | -5.84083 | -53.55984 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2de0139e-ca29-3e60-92fa-75d2d84a6945 | -11.43061 | -45.41801 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58271192-b350-399e-9085-147186fca64f | -8.75178 | -48.65655 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f44690b4-562a-3875-b70a-6a13b6b1c83c | -11.44124 | -45.41986 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f006a564-779e-34b1-aeca-3bc255d94d87 | -8.47422 | -45.09235 | 2026-09-20 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c3fe704-5c3a-3e7c-95e4-6534f6bfdd50 | -9.2773 | -48.24632 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5caa79eb-3151-35e3-9849-17786b788aed | -5.83609 | -53.54591 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89009489-b2f1-371b-ac25-2c325e614b18 | -7.77177 | -44.05266 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fff73888-7e49-3101-babb-a6b828cb6873 | -5.53267 | -45.67649 | 2026-09-20 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8da02cbf-df21-3888-8eaa-bdc738f78f58 | -7.49569 | -46.71698 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 153e1c17-edc3-3807-978e-88b8b4127e7f | -8.75872 | -48.6557 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 453d0337-655c-3240-a49f-48e2f3ae1fc8 | -10.39696 | -48.89644 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63f34f9a-cd41-36be-8788-fd0ba554bcd6 | -7.03755 | -43.6909 | 2026-09-20 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b04b04cb-7f7f-3502-8f93-6abf3fb5c63e | -7.53397 | -45.88579 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| edd32eb8-c003-3ad9-9553-2922613c4bbd | -5.84198 | -53.51439 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6106c44a-9cfc-3373-8367-3e4f986b7d27 | -7.7661 | -44.83787 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56877359-a664-3516-865f-3225d76fd569 | -8.76525 | -48.65864 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1cbc35d-2678-35f6-9a82-6d60e4af9df2 | -3.55488 | -50.29527 | 2026-09-20 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 448e86b8-0416-3a56-8a4f-20ce6bcb2c00 | -11.02119 | -48.33258 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5c787c8-f203-3e51-a667-d7c948c603b6 | -7.09514 | -42.08158 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9e673b84-0208-340c-a75a-a7f8d86f77a2 | -7.75925 | -44.87954 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 952a54a3-133b-383b-8bf0-b41445b6e7ec | -9.17201 | -46.48275 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca0d1539-7b5b-309c-a1ce-9330c1a0e7cc | -5.72622 | -53.45473 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c59f5983-4554-32ba-8733-edfab5425a20 | -5.86712 | -51.5668 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README28.md)
