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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a637d137-7119-3e46-9909-4a55e8261def | -10.9506 | -57.1895 | 2026-09-14 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8a530c02-73a3-3a67-b320-9658f672a52a | -6.6768 | -58.6911 | 2026-09-14 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 268.4 |
| f3e6147e-662a-3863-be40-12382cdd33b8 | -15.5567 | -48.8176 | 2026-09-14 15:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b142502c-f11c-3e0e-a75f-cd1019dd60d4 | -8.6001 | -44.4609 | 2026-09-14 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| bf6af100-e6b5-3886-b7fc-47406be50035 | -11.3352 | -46.7674 | 2026-09-14 15:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6e049215-03ff-35e5-bd62-5f0f39372b1c | -10.9301 | -48.3497 | 2026-09-14 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 93a1ca10-aff7-35d5-b208-bee1ec5d0468 | -5.2023 | -49.3348 | 2026-09-14 15:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 46eae19b-3801-3479-88f2-6df2790b2f50 | -2.8839 | -50.4428 | 2026-09-14 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| cc6afd78-5a42-3602-a4f4-cb2bc8480f6e | -10.5667 | -51.3349 | 2026-09-14 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 7db3643e-70e3-3bc7-9974-1b23d2c20016 | -8.043 | -43.7565 | 2026-09-14 15:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 050b9a9c-9017-3cfd-be9e-9060728714de | -10.7906 | -46.2977 | 2026-09-14 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a3ee6853-33b4-3cdc-953c-e144bdb20758 | -3.1696 | -58.6629 | 2026-09-14 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f868bfbf-27b5-3fc1-b6ce-1d67f4dd3d6c | -3.5893 | -59.0773 | 2026-09-14 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 2763b8db-9d15-3dab-a02b-cfd572d0e228 | -3.4632 | -58.4062 | 2026-09-14 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a79ce752-a96f-38d5-bf6e-a917a14420fb | -12.1265 | -44.199 | 2026-09-14 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 71bf6cbb-d920-3ee8-bda8-84315724400e | -10.2206 | -50.373 | 2026-09-14 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5b5ee0de-3f04-3d53-a31e-4eedb99b6466 | -10.7722 | -46.2549 | 2026-09-14 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 444.7 |
| 662aaf5a-769b-37d0-a86f-0587b1bbb4b3 | -6.8445 | -55.581 | 2026-09-14 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e947697d-d434-3e68-908c-43200fea0dc2 | -13.3055 | -51.3235 | 2026-09-14 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| db8af157-1fe2-33be-9bef-c7ab831e3012 | -13.3059 | -51.3022 | 2026-09-14 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 176.0 |
| de0cb393-6201-3ee4-b8f6-3bf266465097 | -3.4089 | -58.2142 | 2026-09-14 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 269.8 |
| 3e91bae7-892d-3ef9-ba21-4b6fe02d7b0d | -3.1697 | -58.6437 | 2026-09-14 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| cecd440e-7d92-3858-b66b-fceab60510d6 | -14.4936 | -41.3771 | 2026-09-14 15:00:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 27ae2b83-b175-3ee2-8493-43ee01bfd742 | -10.7271 | -50.6405 | 2026-09-14 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| b71135fb-3a9f-387e-9cca-3e73874f2901 | -3.5894 | -59.0581 | 2026-09-14 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 60c7fe6e-3a60-3ee4-adb3-9e25e0b87c3f | -3.4272 | -58.1945 | 2026-09-14 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 05a832e2-bf8a-3cd4-adac-a9844e1d18a3 | -13.5523 | -51.4843 | 2026-09-14 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 540b8901-a800-3c90-9d60-6db60f3ec8dd | -11.8365 | -50.0028 | 2026-09-14 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 40871820-e3b4-3142-8475-d81c3841a6e7 | -3.7181 | -58.8823 | 2026-09-14 15:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ae86d956-6baf-3227-b464-d73334d96d9c | -3.3493 | -59.8288 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 1394000a-34a7-37a9-a943-835e7b8aafc3 | -3.4279 | -57.9816 | 2026-09-14 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 77c795a0-c878-37be-bbf3-29ffbefa08cd | -10.5484 | -51.2945 | 2026-09-14 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| e9af4048-61ff-3a4b-a389-7a73d27c99cb | -6.6512 | -43.6587 | 2026-09-14 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 9087367d-11bc-3c37-b445-0c037448a161 | -12.5329 | -47.1639 | 2026-09-14 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 5a621b2e-010d-33ce-8d3e-95a79b65d9d4 | -10.7909 | -46.2751 | 2026-09-14 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 6597b521-9aac-316f-b69e-bcaefd9439ca | -5.4546 | -60.2155 | 2026-09-14 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 3514f8de-2523-3f74-bd6b-f6fda1c3c885 | -10.7726 | -46.2322 | 2026-09-14 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 387.4 |
| 6e64f570-80b6-31f0-8141-f73696db5890 | -13.2933 | -41.0016 | 2026-09-14 15:00:00 | GOES-19 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 104.4 |
| aecaf071-8d2c-3b70-b848-485234262586 | -10.7839 | -50.6346 | 2026-09-14 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 943a28a2-57e7-367f-9071-d6513633e6ed | -3.3306 | -54.1805 | 2026-09-14 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 7885ac72-4611-35a8-9553-7ce8371288a0 | -12.3919 | -44.391 | 2026-09-14 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 0f2ae865-124e-34ea-b926-6a2b6aebefc5 | -6.2856 | -42.6834 | 2026-09-14 15:00:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 17182d0f-7278-380a-a59d-1c149700afbf | -3.3677 | -59.8094 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ca999f28-af78-3959-bc73-426ee049d963 | -1.7316 | -54.9518 | 2026-09-14 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f2aa06fc-28b4-33e8-b6a7-c8a0a5d2b1ca | -4.1151 | -60.6696 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ca84bc63-a0e3-3eb1-8499-129fd667d636 | -10.7842 | -50.6133 | 2026-09-14 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 5ef55c44-0961-3781-8776-eca376419c69 | -7.1048 | -41.7971 | 2026-09-14 15:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 222.7 |
| 3629265f-3591-3005-bcb1-739ddf2aac3b | -4.115 | -60.6886 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 7269ddc1-d4d0-3284-99fa-1c33d04abfac | -15.5768 | -48.792 | 2026-09-14 15:00:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3d6a110e-2e6c-3467-8792-bb8b82957004 | -10.8031 | -50.6113 | 2026-09-14 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9767cc47-33ba-3e2b-9dac-bce4eb90df5e | -6.67 | -43.657 | 2026-09-14 15:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| fefffbee-41df-33f2-9ab3-6356d8a0a36f | -9.6086 | -46.7311 | 2026-09-14 15:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 478a35a0-573d-3d95-b48b-de06f0d9a49f | -10.2922 | -45.339 | 2026-09-14 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 327666ab-cf59-303c-805d-0951922ee328 | -8.5417 | -54.6985 | 2026-09-14 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| de7fa3a6-3a71-360f-81f4-af85f1b6632e | -3.3141 | -59.3515 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 50733d6b-1a67-3743-9063-7583669d15fe | -3.4278 | -58.0009 | 2026-09-14 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| bd10a8d2-3826-35d0-bd40-b30d5a3ff023 | -11.2565 | -50.6904 | 2026-09-14 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| de50382f-0f4f-3b37-9afa-738f12505c14 | -10.6827 | -54.1679 | 2026-09-14 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 74bb7d7f-f14e-3164-9e97-41d10be92fb5 | -6.8446 | -55.5611 | 2026-09-14 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| c320fab1-2e61-3a12-bd33-33c3df13ce64 | -3.3139 | -59.3898 | 2026-09-14 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d124145f-2ee8-35a4-a707-5afe20f7c7c6 | -15.5572 | -48.7953 | 2026-09-14 15:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 781b46a4-79b8-3818-a468-76237ee573b1 | -10.312 | -45.2907 | 2026-09-14 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 06c7a92b-12c4-3008-8a6d-f0cff427e0e8 | -8.5415 | -54.7187 | 2026-09-14 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1f8eed4b-ca0d-33fc-823f-9de73344eddf | -10.7715 | -46.3001 | 2026-09-14 15:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 08201342-3366-3917-8005-019c84d5cb60 | -10.7276 | -50.5979 | 2026-09-14 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8cdf90fb-91db-36b4-94d2-b927e83a4bd1 | -9.4325 | -50.1299 | 2026-09-14 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 240.2 |
| ba414151-4842-3b58-8667-7bd4f13195cb | -8.5415 | -54.7187 | 2026-09-14 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 619a04ce-3b0a-3b90-aaef-24df7487dc2e | -12.177 | -48.9623 | 2026-09-14 15:10:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| df673981-5c1a-34b3-91c3-632df14ef51e | -4.115 | -60.6886 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 100e9b23-133c-3b0f-8ec1-b9d1f1f97c1b | -8.5809 | -44.486 | 2026-09-14 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 491e97d7-2ec9-351e-a7c1-1d80f867bcc8 | -12.1265 | -44.199 | 2026-09-14 15:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9c131664-c2d6-3034-8899-f0ae8512c126 | -15.038 | -48.4573 | 2026-09-14 15:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 182f7786-76a9-322f-8c3d-16b2c5186a5c | -2.6601 | -57.5507 | 2026-09-14 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 9b62feea-1363-3b7b-a48d-3a13e8dc4dbc | -14.4936 | -41.3771 | 2026-09-14 15:10:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 7fb2c68d-b490-3f21-a2ae-0f09e280b859 | -10.7839 | -50.6346 | 2026-09-14 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ed18f5f0-10bb-377d-b1f7-f6dc52b62b0a | -3.8957 | -60.5984 | 2026-09-14 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b0d18a54-b27a-3058-9ae5-8b211653f705 | -7.1048 | -41.7971 | 2026-09-14 15:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 156.1 |
| d17b4b0d-8af8-32e2-b09f-5f7f0db5475e | -9.7036 | -54.371 | 2026-09-14 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 5cf577bc-7cba-3514-9447-0e5b40c64fd7 | -8.6194 | -44.4357 | 2026-09-14 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 64624324-c585-375e-994e-934c2f4c76b4 | -5.8507 | -52.0878 | 2026-09-14 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9eb4524c-a075-3737-be0c-f914e2471ffd | -3.1697 | -58.6437 | 2026-09-14 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 2211b585-58a6-3594-9da7-1b6180fad52f | -6.1108 | -57.7035 | 2026-09-14 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| c4228a9c-437f-3e1d-a9b4-f3a0e825a150 | -8.4112 | -54.7073 | 2026-09-14 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 12fb6695-2027-3829-9736-1fdb3bffa5aa | -6.3436 | -55.8243 | 2026-09-14 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 17242781-eee1-3a87-a937-94301961a7cf | -2.6602 | -57.5313 | 2026-09-14 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 91b3a131-93a0-3e8e-a773-46aed981e93b | -10.2922 | -45.339 | 2026-09-14 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c3fab957-c6f8-372c-a0c5-f7eeb069ff55 | -10.7722 | -46.2549 | 2026-09-14 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| ec37d8db-0d3d-32cc-8463-8b7035429255 | -4.1151 | -60.6696 | 2026-09-14 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0ef1b11e-b445-31ae-9cb4-0a74a6b01a16 | -6.9182 | -55.637 | 2026-09-14 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 610aa0db-8d99-32ed-9a6e-5f2a7fe1cc3c | -6.0925 | -57.6847 | 2026-09-14 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 113a6586-fa06-3fb7-bf98-1cbe4704ce4a | -3.7181 | -58.8823 | 2026-09-14 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 993e4134-f567-3112-a4b9-736a332ad92b | -13.5526 | -51.4629 | 2026-09-14 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 225.3 |
| 2125d54c-4ff9-330d-921f-6eaed619f534 | -15.5768 | -48.792 | 2026-09-14 15:10:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 8b55d914-5bb8-38d4-8058-ad3d09cf11e2 | -10.5484 | -51.2945 | 2026-09-14 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 458a0525-61f4-3002-a423-12b62c229b5e | -10.6958 | -47.5175 | 2026-09-14 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 69a21c92-b5cf-3f99-8665-ed7b5d5786a6 | -12.4901 | -41.4012 | 2026-09-14 15:10:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 66294e26-3415-36a5-b8da-e299ff4f099b | -6.1045 | -55.6566 | 2026-09-14 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c62f0a5e-83b1-3521-9ca2-02544d02acfe | -2.8841 | -50.4009 | 2026-09-14 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c8bedabd-1014-365e-a97c-184a89f4a5ed | -10.5667 | -51.3349 | 2026-09-14 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 558739c3-6d36-33ff-8493-46da5bb17d8f | -10.9506 | -57.1895 | 2026-09-14 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |


[Clique aqui para ver as próximas entradas](README78.md)
