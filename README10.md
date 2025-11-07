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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93e85faa-bd40-3f7f-aa6f-bd7565787a90 | -5.11482 | -45.88248 | 2025-11-07 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c13faf6-ca23-360e-adff-5fe14e8e65bd | -7.9315 | -55.01426 | 2025-11-07 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 613ff88f-6544-3542-b1c1-318ed1e4a79a | -5.76313 | -40.82663 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f22c283-f750-3667-b442-2c653740fb72 | -5.63138 | -43.91784 | 2025-11-07 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbdec65b-9969-311a-af1f-c557d5feb0d7 | -4.49977 | -45.14037 | 2025-11-07 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d3a35c4-a573-370b-b90c-17dda93eafb6 | -7.1417 | -40.45829 | 2025-11-07 04:25:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e1312a2e-1b02-38e9-a456-b8e5321cc2e3 | -3.3547 | -53.21869 | 2025-11-07 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a5fd220f-eb5b-30fb-b95a-76e466688ac0 | -4.40091 | -46.44185 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ad20ff6-0f4e-3286-9777-5e90132c725c | -6.65309 | -44.48899 | 2025-11-07 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2ecf4c1-f7ca-3da5-8c53-44f280b10f3d | -8.59012 | -39.42348 | 2025-11-07 04:25:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f82a27d1-c7a9-3a42-a6aa-c480a1b3111f | -7.0796 | -41.57939 | 2025-11-07 04:25:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b4e0fcf-9516-37cf-883c-4b43972319d4 | -3.61584 | -52.12053 | 2025-11-07 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efe2b3be-b626-349a-9d93-424e0c9623b1 | -4.97537 | -42.68488 | 2025-11-07 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 850309c0-55ce-3b28-ab0c-57d475f96059 | -5.57297 | -47.10219 | 2025-11-07 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51b16947-9e0b-303c-9dd4-d20f5a0731ec | -5.77091 | -40.80222 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dee60ec9-fa48-3238-b21f-c062f5c304a2 | -6.58906 | -35.25721 | 2025-11-07 04:25:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 68b4b253-9729-3526-a791-7495e705401c | -7.62887 | -39.73636 | 2025-11-07 04:25:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9100c1f3-93fb-3f7f-af6f-2472f6e5cb72 | 2.56545 | -50.97957 | 2025-11-07 04:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69c2db68-dd01-32a9-a52d-fbba341063b2 | -5.55967 | -45.45512 | 2025-11-07 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99cbb931-37e6-3f15-bf14-e138e0481155 | -6.5619 | -44.25387 | 2025-11-07 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b19e527-3d00-380b-b103-4c4371a80570 | -7.08584 | -43.76647 | 2025-11-07 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e16b1585-bb3c-3b49-a15d-987a3da32874 | -5.08561 | -44.80458 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15fa4a84-0e7b-3db6-868b-d56239467d2f | -3.41977 | -52.64828 | 2025-11-07 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8da38df8-99a7-3974-b6b6-04f6dcd5aff4 | -7.71752 | -47.1845 | 2025-11-07 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8741f4d4-f7c1-3371-9c4f-be7472326b27 | -7.18857 | -39.67033 | 2025-11-07 04:25:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0864b6cb-5fbb-331c-8a1f-b71dc77e4aad | -8.87266 | -48.0295 | 2025-11-07 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ccc9917-01f8-30dc-a502-db09daa368d5 | -4.64902 | -46.87254 | 2025-11-07 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aef067de-365d-3086-8848-88138256e8fe | -4.44957 | -46.43514 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 875d31a8-e1e4-32ed-bccf-822c0fc54cb7 | -5.77191 | -40.79547 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ea6efc7e-f6ca-3c15-ba76-ebac210424e5 | -6.70067 | -39.97355 | 2025-11-07 04:25:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 269a1711-0e2d-39de-88f6-20d69d6ddda9 | -4.98943 | -43.87114 | 2025-11-07 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6aaf478f-c865-30a6-9007-f364e9ac4914 | -5.26937 | -47.16686 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ef633e2-4146-36a7-a6d9-846fd018e9e9 | -6.3284 | -41.7001 | 2025-11-07 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12a9507b-5b64-3fa1-bb8b-e572fb0626dc | -4.45289 | -46.43565 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9e012ea6-8004-3868-9ab3-8704a1ae3da9 | -6.65038 | -43.60726 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0714a20e-6c47-3f3e-b90a-b7e8d26e536b | -6.70127 | -39.96934 | 2025-11-07 04:25:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6245e2e7-1dc0-308c-8f0c-51fb524fd983 | -5.77141 | -40.79887 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1172874e-7f1e-3fd4-be60-568c03f43cd8 | -5.7741 | -40.83625 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ff73747-424c-37c5-b66e-d476276517e3 | -5.26659 | -47.16276 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9cc2dbd8-7793-3798-9421-d97df4e5396d | -8.07663 | -46.82797 | 2025-11-07 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cdbc3f1-88e1-3ddc-b1b9-f8c93fee4d89 | -4.57731 | -46.40228 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c37b3f92-e997-3e87-b92e-0ef10368a3df | -4.44902 | -46.43864 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2c9eebd-07f2-3383-b515-716217d8927e | -6.51284 | -38.73453 | 2025-11-07 04:25:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6382d4a7-70f7-368d-9f00-791e62cecd6d | -4.5908 | -45.99378 | 2025-11-07 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cfb4be4-acea-317b-ab24-426d3632ddca | -4.94095 | -47.45855 | 2025-11-07 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04043aad-8aa0-3b08-80a0-cce65a37cbb4 | -5.76661 | -40.83104 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| edd854ae-d4dd-32fe-b810-2773f9f38025 | -6.56534 | -44.02563 | 2025-11-07 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb052f4a-09a0-3f7d-9f49-b960db16be25 | -4.86764 | -48.00716 | 2025-11-07 04:25:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32556f33-c981-31bc-889a-a0da88c6f174 | -9.4426 | -59.20517 | 2025-11-07 04:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b06196c0-e2df-37fc-9f3f-e5f3361e5c42 | -3.34806 | -53.22866 | 2025-11-07 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c469a201-2626-32ac-ae26-33ad184bc321 | -4.41139 | -45.62011 | 2025-11-07 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06365eb3-04fa-3016-aa6a-5282f05869e3 | -6.57851 | -44.03151 | 2025-11-07 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08868c11-b2f1-34d9-9cd8-45f9c8332fc2 | -8.80257 | -47.93717 | 2025-11-07 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2cb0cf1-616b-3820-a5a3-5111b07c125b | -6.96409 | -46.22176 | 2025-11-07 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36970ad9-ea5c-315e-b6d5-28107a00b3bd | -17.02973 | -46.75918 | 2025-11-07 04:27:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c10ea354-d9ff-3936-8e62-2e692d2354e5 | -15.6583 | -49.37822 | 2025-11-07 04:27:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30fcd947-582a-3099-b00c-ec47c0abb1c1 | -18.21401 | -50.94359 | 2025-11-07 04:27:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afb7fe1d-f7d7-341d-ae65-d3107b8a6380 | -19.54631 | -44.1689 | 2025-11-07 04:27:00 | NOAA-21 | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bed8f5a-7f27-38fc-9116-c4ae8cdd32f0 | -16.01241 | -49.22927 | 2025-11-07 04:27:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a15979b-667a-3177-8122-81aa51923cbf | -19.37537 | -44.79965 | 2025-11-07 04:27:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1cf1b45-b17e-3a23-9055-c5dabe851d66 | -14.57558 | -52.87408 | 2025-11-07 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c8b49cb-8ded-3e2a-9422-99c2a908b947 | -19.36829 | -48.61267 | 2025-11-07 04:27:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 981be032-31ca-3f04-ac6d-cb5bd08efca7 | -15.0949 | -48.77355 | 2025-11-07 04:27:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a29d833-42c3-3638-a329-5d706a4033cc | -16.33206 | -45.61629 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccffd426-9202-3651-a09e-e36aee0c3064 | -12.53439 | -48.71117 | 2025-11-07 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a789c425-39f6-3e58-8c7f-8ad30ed02f5a | -15.7553 | -48.55812 | 2025-11-07 04:27:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 249a822f-a753-33a6-8315-f18ea7e47730 | -16.32149 | -45.61463 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7dfc8bb-6590-3b33-8151-eb159338aa25 | -16.27985 | -46.667 | 2025-11-07 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03c2fbc1-299e-3f1d-a53b-af5a631dceb3 | -16.34264 | -45.61793 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7957bd94-0f0f-3ce3-861f-9dc29a909d0f | -19.10009 | -44.25245 | 2025-11-07 04:27:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b800276-cb5b-3fb5-ac32-a0244c801983 | -18.97465 | -50.0262 | 2025-11-07 04:27:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3df15d2a-687a-3c08-9887-5ea4582cfe15 | -15.09924 | -48.78907 | 2025-11-07 04:27:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79be36fa-1f6b-31f4-925c-2ab90d43b3a4 | -13.26969 | -46.04015 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1618cff5-941b-35b8-a35f-eba0af52e6b9 | -18.50106 | -48.76802 | 2025-11-07 04:27:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd7dc8ca-5b9b-3a2b-911a-87627d489479 | -18.51609 | -44.01418 | 2025-11-07 04:27:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6642934f-aaa2-3305-ba06-f658be44b8ed | -16.27623 | -45.60334 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dada83e-80b3-3d65-a1da-4f6d0e5c9e47 | -17.21464 | -47.65392 | 2025-11-07 04:27:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7ea4ce8-7772-3721-8848-b5ee521c5d35 | -18.98404 | -50.03168 | 2025-11-07 04:27:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24da9991-af1e-3f09-9390-ba9d9a7d148d | -14.80043 | -48.80541 | 2025-11-07 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05157e5-4122-3329-8d48-fc76c6134c3a | -16.55419 | -49.393 | 2025-11-07 04:27:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57b2d3e8-2208-3b5e-ba47-d30c71ecb653 | -13.28438 | -46.05764 | 2025-11-07 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 465a1c1e-b07a-3a24-889e-359d993f37af | -16.31091 | -45.61296 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aa10736-e2b4-312f-8790-341ae931da0c | -19.087 | -44.26098 | 2025-11-07 04:27:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c4b0fa1-fca2-3d7f-a8d2-4487a80e6c77 | -18.33064 | -47.27288 | 2025-11-07 04:27:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bb54a36-2686-34b1-81e7-6e195dc7d51a | -16.60272 | -51.27166 | 2025-11-07 04:27:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17db2fa2-2515-354e-a0df-7b2ce1884b77 | -18.21189 | -43.92109 | 2025-11-07 04:27:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f9666ca-1f0a-39ae-a7f7-df137b215432 | -18.09919 | -50.25838 | 2025-11-07 04:27:00 | NOAA-21 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f844c515-511c-304b-a051-6548c538b196 | -15.90992 | -50.39767 | 2025-11-07 04:27:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 997bf5d6-d98e-31b7-90e0-2b436312d737 | -16.9263 | -46.55896 | 2025-11-07 04:27:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0811769-d230-37e4-9acc-01a57e90fefe | -17.53315 | -45.31752 | 2025-11-07 04:27:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd9a109a-bf1a-3a7a-9d4c-93a161d66308 | -16.32854 | -45.61573 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d253272e-238a-39a4-9e93-887befeae146 | -18.54379 | -50.90642 | 2025-11-07 04:27:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb0f5c0e-7ef1-3fe9-abba-91ec4a8ba090 | -16.30033 | -45.6113 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f69c5d7-78fc-3c52-929b-c8beb41bc646 | -19.84377 | -44.89906 | 2025-11-07 04:27:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd3c1b13-2f3f-31c4-a872-1c47dd1ee6f0 | -16.33559 | -45.61684 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3284c90d-e6cc-302c-aaf1-8e8e3dfc6d73 | -14.63046 | -52.45555 | 2025-11-07 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91688ede-6729-3d43-9e06-3d60f3ea5543 | -18.97405 | -50.02988 | 2025-11-07 04:27:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dbbf0b7-095c-3945-84b2-8957added18a | -16.30738 | -45.6124 | 2025-11-07 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec608fb1-f6d8-34b4-9e6b-05c808779501 | -13.22156 | -44.55564 | 2025-11-07 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0825da03-53dd-39aa-a176-36a1c392720f | -18.98464 | -50.028 | 2025-11-07 04:27:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
