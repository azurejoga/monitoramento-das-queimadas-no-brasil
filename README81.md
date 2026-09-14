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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5548b764-98ea-31a8-9cab-fc0eae6fa6e4 | -10.9506 | -57.1895 | 2026-09-14 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4d0dc2fa-3e68-390e-bae4-9576b60c642b | -10.6413 | -46.1133 | 2026-09-14 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 807c3b07-92d0-37e0-8551-e971d58986fd | -3.66375 | -40.5711 | 2026-09-14 15:31:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1d878619-ce31-3b79-846f-2992396b37ad | -3.72694 | -38.8049 | 2026-09-14 15:31:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1cdbfa07-4bfa-38bd-9b84-69867457b134 | -3.24264 | -39.77877 | 2026-09-14 15:31:00 | NPP-375 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 885c2d9e-7537-364d-99ee-e29c62695c97 | -3.44735 | -39.15036 | 2026-09-14 15:31:00 | NPP-375 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e37bc358-4428-317d-b702-b43ce530bbfa | -3.65075 | -41.07878 | 2026-09-14 15:31:00 | NPP-375 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 73791a88-7754-3152-aaf6-c22ec6a0a5de | -3.78501 | -40.77982 | 2026-09-14 15:31:00 | NPP-375 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 14ffad32-772c-3a14-97e2-55017782eb09 | -4.06114 | -38.49417 | 2026-09-14 15:31:00 | NPP-375 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 366b40f1-1076-3474-8509-c1fe3e0f51f6 | -3.65452 | -41.0799 | 2026-09-14 15:31:00 | NPP-375 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 5888930a-88c3-3bce-8f8d-dc95107659d5 | -4.06181 | -38.49882 | 2026-09-14 15:31:00 | NPP-375 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 380e5e0c-0d6b-327b-8f72-e2f86603a09a | -3.14084 | -40.80163 | 2026-09-14 15:31:00 | NPP-375 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1a249fdd-74dd-3336-99d1-356bcf9d6cbb | -3.22423 | -40.11391 | 2026-09-14 15:31:00 | NPP-375 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 0a8cd2d9-12e0-3d34-aa40-3e050abc14c5 | -3.66315 | -40.57549 | 2026-09-14 15:31:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1518a8e9-2565-3c7c-b3bc-7dfd22006e99 | -3.14243 | -40.80317 | 2026-09-14 15:31:00 | NPP-375 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3d02d2a6-bff8-3b4b-a298-b3fb7dc1b861 | -10.7015 | -54.1663 | 2026-09-14 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a183daa4-c362-3773-b055-b63b185ccb8d | -3.1697 | -58.6437 | 2026-09-14 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 6bf72a58-bdb1-3d1c-846c-b52ae10f36a2 | -8.4112 | -54.7073 | 2026-09-14 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c7e3c517-bc07-3754-81b2-e9f7a2dc5998 | -13.5719 | -51.4605 | 2026-09-14 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a496dbeb-0456-322b-b6e8-a54c9df3ee7e | -10.7715 | -46.3001 | 2026-09-14 15:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 1acd6e97-e42b-3976-bf09-23180a4a8ff5 | -3.3493 | -59.8288 | 2026-09-14 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 7be61035-ada9-3ea1-afa9-15b605c2f487 | -3.3137 | -59.4664 | 2026-09-14 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 04c8fd71-1c2d-3975-a449-6b54d6987e91 | -4.1334 | -60.6692 | 2026-09-14 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 064da033-ce0c-3ed9-b076-e5dabe34da0f | -3.3494 | -59.8097 | 2026-09-14 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 4154e4e9-b9bd-325c-a3ec-2591c6afcb13 | -9.4392 | -48.0984 | 2026-09-14 15:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 1106d99c-911d-3fde-b3c4-3e869daf2800 | -3.3677 | -59.8094 | 2026-09-14 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d6aaab19-5ee9-3c68-bec4-ec86686f77ac | -12.1093 | -50.8499 | 2026-09-14 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e849ae7c-3b4e-3f45-82c5-28d36332ce50 | -9.3755 | -50.1779 | 2026-09-14 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| fbbdee26-bfd0-33e4-9d20-6ee478c0b601 | -13.5526 | -51.4629 | 2026-09-14 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 165.8 |
| e436c96d-9efc-3844-b860-29484d5739d5 | -10.7719 | -46.2775 | 2026-09-14 15:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2ebda9a7-2adc-3cea-932d-6fb459b969aa | -11.8365 | -50.0028 | 2026-09-14 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.9 |
| c1f418fa-4097-309c-bddd-9fe5485d7c2b | -3.3359 | -58.1191 | 2026-09-14 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 6aa79f96-dd08-3fb9-8bbd-286833f04efc | -3.1815 | -61.1424 | 2026-09-14 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7c4566d2-72fc-3dc1-b3ce-f533c03d3baf | -9.3753 | -50.1992 | 2026-09-14 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 0a1e91e5-92b4-373b-8a53-ff8b4a13f2db | -3.4279 | -57.9816 | 2026-09-14 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 74f38a87-165a-365f-8404-f1c12c5cb743 | -6.2916 | -55.2895 | 2026-09-14 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ab9ed0d2-557f-3270-9803-2209c3d2c9e5 | -11.4905 | -50.2581 | 2026-09-14 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8c55908c-8f3f-3a57-9cf8-045de9333333 | -9.3948 | -50.1334 | 2026-09-14 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b793351d-3c3d-30b0-b954-b32c5de3051d | -12.1265 | -44.199 | 2026-09-14 15:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| c890f186-8f27-350c-a485-de19988b6db6 | -3.4058 | -59.2347 | 2026-09-14 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7030bf29-763f-32b2-810e-6e8246274484 | -3.7181 | -58.8823 | 2026-09-14 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2a585228-fda9-3c82-90da-594f0fbde4de | -3.1462 | -60.6317 | 2026-09-14 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5ca15c9f-fa80-3b4c-a984-4ec8a8ba34df | -13.3185 | -51.7051 | 2026-09-14 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ba230ad7-1c37-3334-8e3f-ba6741db39d6 | -2.6601 | -57.5507 | 2026-09-14 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 91175608-280b-3169-ba00-78331ec7a8e6 | -8.5417 | -54.6985 | 2026-09-14 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| efb932dd-e9ae-375b-b35b-58d353488587 | -3.1096 | -60.6512 | 2026-09-14 15:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bc60a85a-2532-3125-af5e-757d19625af2 | -10.7909 | -46.2751 | 2026-09-14 15:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 218.3 |
| ce26921a-5144-33ba-ad9c-5ac988189078 | -9.68 | -54.8393 | 2026-09-14 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 53ecf943-a676-3150-a9f4-6660b679b897 | -10.5667 | -51.3349 | 2026-09-14 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2a175b60-9290-3381-a6ad-03724fc69aa3 | -3.1514 | -58.644 | 2026-09-14 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 41376836-86b5-3b3f-83ef-e503f973ddd6 | -11.383 | -43.9614 | 2026-09-14 15:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 5f5e1554-eaf7-30cc-b990-e1bb5f1e5e6a | -11.8362 | -50.0244 | 2026-09-14 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 0487a3c2-195a-3ba7-9484-3eaf04dbd02e | -3.5894 | -59.0581 | 2026-09-14 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| b2aed02a-2c81-3714-b1d6-ce2869d0f745 | -1.861 | -54.4315 | 2026-09-14 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 41e9ad22-d13d-36c2-b0b3-66c920f7c5da | -7.7636 | -46.6722 | 2026-09-14 15:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 2ead457f-5a9b-3311-a194-c63fd7a4e69b | -10.5484 | -51.2945 | 2026-09-14 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1dbf8713-21b1-32fe-a199-3ddb0765c8af | -3.3138 | -59.4472 | 2026-09-14 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8c640a55-57eb-33d7-bc6d-45c9f6aaadb0 | -6.5781 | -45.3158 | 2026-09-14 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c671dff7-40d5-3494-b21e-af5bc8ea0920 | -3.4632 | -58.4062 | 2026-09-14 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| bb83eba2-b220-31c2-bfb9-420a34320179 | -5.221 | -49.3125 | 2026-09-14 15:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 66c5dca3-c90f-337d-b407-1b844d4e4ff4 | -11.5095 | -50.2559 | 2026-09-14 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| fb864bee-df7c-30c7-9865-91c2685407e6 | -11.4908 | -50.2366 | 2026-09-14 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0eef07c5-448f-3739-95a5-99335ccceb59 | -3.7181 | -58.863 | 2026-09-14 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 621fe024-cb18-3dc4-adba-3e0b8f4f83b9 | -6.2917 | -55.2695 | 2026-09-14 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e2e1db3d-2d07-35e5-be63-56986be1d605 | -3.6077 | -59.0577 | 2026-09-14 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 349e2100-1fe2-3a65-af4c-5cd6e98614f0 | -9.376 | -50.1352 | 2026-09-14 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8a6e0f3d-c138-3e5b-8ddd-cdc480709d46 | -9.1711 | -49.9835 | 2026-09-14 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 80870a81-648c-38cb-b675-cc1321824b48 | -3.3306 | -54.1805 | 2026-09-14 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ffbac780-3ac0-304b-8a11-f5c04a8b7788 | -1.7133 | -54.9521 | 2026-09-14 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| bec469e4-7593-34ea-a719-266b64cb9bc8 | -10.2926 | -45.3161 | 2026-09-14 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5756f180-8d8f-3e2f-be1a-a16f495ba47b | -10.312 | -45.2907 | 2026-09-14 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 365.2 |
| b326fb78-88ec-33f4-b301-f5863a89a2ea | -10.0293 | -52.12 | 2026-09-14 15:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b977935b-3372-3aaf-8a48-46403d21a907 | -2.6601 | -57.5702 | 2026-09-14 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2b6c6164-2f53-382b-83b1-508957176a05 | -9.0417 | -49.8031 | 2026-09-14 15:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| d9458ad4-6e8c-37e2-91e4-8568b2995eb2 | -17.74946 | -42.71133 | 2026-09-14 15:44:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| 5a4d4652-604d-32db-a250-af9680ae479d | -17.75619 | -42.71524 | 2026-09-14 15:44:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| 65884cc5-b87c-310f-92fc-9842b76e950a | -17.48947 | -39.70517 | 2026-09-14 15:44:00 | NOAA-20 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| da0e7869-5910-35fb-acb5-4a86b1a2ff13 | -17.7504 | -42.72125 | 2026-09-14 15:44:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| fdbfc5de-4f7b-3b1c-8a38-ce3304c42543 | -17.75668 | -42.72038 | 2026-09-14 15:44:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| b1e0cc62-8700-3897-a91a-291c8f0262ff | -17.59727 | -44.33428 | 2026-09-14 15:44:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2c4fcd4b-c99b-33bf-9347-7cc26906b750 | -17.69444 | -41.83607 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 154.7 |
| 5d048a7e-86ea-3601-b1ed-40bca29a8086 | -17.79189 | -42.56153 | 2026-09-14 15:44:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bd4574fb-70f2-343e-bd0a-4aae7c96856e | -17.69226 | -41.84203 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 6af6f1d9-9302-3f3e-b76f-a1ccfd3e73de | -18.5274 | -40.23624 | 2026-09-14 15:44:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 20e34cf8-0d1f-3795-ac29-b69ae661084d | -18.10482 | -40.30701 | 2026-09-14 15:44:00 | NOAA-20 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 5ad39475-920e-3e72-9399-22b4de140602 | -17.59778 | -44.34053 | 2026-09-14 15:44:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 16e91aab-094d-36ba-a899-123370f25652 | -17.69542 | -41.84566 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.9 |
| 76fe9670-4c29-37ea-a11d-c85fbbb35a0c | -18.09036 | -42.38071 | 2026-09-14 15:44:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 9e7f43bb-6070-36d9-a56c-bb215974ae43 | -17.69495 | -41.84102 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.9 |
| 1f6d8552-33b7-37ba-ad7d-e2db2df0074f | -17.54062 | -40.9567 | 2026-09-14 15:44:00 | NOAA-20 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| e746fe76-5fe0-34cc-abcf-929bfdb68c13 | -18.48005 | -42.85846 | 2026-09-14 15:44:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a036abcf-b61f-3895-b546-88965d083d5c | -18.30951 | -41.67302 | 2026-09-14 15:44:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6a360585-d0bf-3222-b83d-bcf6d4beedbd | -18.0889 | -42.37802 | 2026-09-14 15:44:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| fc18a7ea-2798-3ec7-a31b-a82ed9929b1f | -17.48822 | -39.70702 | 2026-09-14 15:44:00 | NOAA-20 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 1d349b8d-6662-389e-b2eb-c547de05303b | -17.6918 | -41.83716 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.3 |
| efc89f05-5b84-3f41-b948-9bb18eb3d273 | -18.08939 | -42.38338 | 2026-09-14 15:44:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| ffa7f97b-5372-3624-b44d-935546ea23e2 | -17.74993 | -42.71628 | 2026-09-14 15:44:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| 7c84f30b-931b-3e73-847a-4168da31906f | -17.70083 | -41.83953 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.9 |
| 88c893d0-74fc-39d4-bcd1-f53a1b32d592 | -17.69772 | -41.83595 | 2026-09-14 15:44:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.3 |
| ffae8355-4b5e-300f-bfe1-71d87ee8a5d7 | -18.18111 | -42.03609 | 2026-09-14 15:44:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README82.md)
