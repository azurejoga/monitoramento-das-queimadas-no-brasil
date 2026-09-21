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
| 4da2edf3-d8d3-330b-a996-5a78aeb86f91 | -16.2962 | -49.9354 | 2026-09-21 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 97860919-f4f0-3848-bf3d-279e405a0318 | -3.6946 | -60.5835 | 2026-09-21 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e8a12f77-a58d-32d5-a11e-b05db92c5a95 | -6.2026 | -57.7778 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 312da32b-16aa-307d-8fd0-4c8e770fffa7 | -11.041 | -54.1567 | 2026-09-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| fa75978b-4671-3ca6-aa94-aa16a66e7a4e | -10.7626 | -50.8069 | 2026-09-21 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f56ded62-a2e7-3f81-82d4-e5a2d4a51624 | -5.7614 | -57.6002 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| a82e55a4-9d1b-3c8e-afb9-d9d9a91d0ab5 | -7.5704 | -57.6766 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| e0e9b16c-7bef-3556-9a1d-92122f3e9a18 | -6.4486 | -59.9717 | 2026-09-21 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 74141d7d-4b4d-3fda-bf6b-5e48dd8d8df0 | -5.2168 | -56.1096 | 2026-09-21 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b92ece65-f91c-3386-bb77-c36b5707de21 | -3.0534 | -61.2767 | 2026-09-21 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 00dce55a-3290-3442-b304-89687c344b0f | -9.5593 | -66.0545 | 2026-09-21 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 446b4258-e662-305e-8a98-0e8c8d7418e9 | -7.5703 | -57.6962 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 4c3bf204-b5b4-3426-bdb4-51707a98656e | -7.5891 | -57.6561 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fb0f037d-c34c-3bec-b59f-7862112e18ba | -11.8017 | -49.7913 | 2026-09-21 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 16d54e8c-ad6b-3226-890b-1a462bc3eb66 | -13.9118 | -48.5669 | 2026-09-21 00:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9b1cc98b-d702-3e5c-b43d-3f08eb9c765a | -3.0716 | -61.2953 | 2026-09-21 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 9b1c7122-bae2-3164-8df8-c97bf34afee0 | -3.0717 | -61.2764 | 2026-09-21 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 4e0a2bab-79e5-3ce3-bc65-b357bddff3af | -6.1668 | -47.3297 | 2026-09-21 00:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9802bce4-535d-302d-b198-b42683654901 | -10.39 | -51.8775 | 2026-09-21 00:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e1336575-ddc1-3e2d-b9db-9558bc5a4d82 | -3.753 | -59.419 | 2026-09-21 00:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5e772709-d574-3fe6-bd8b-eb869b1f7971 | -4.3357 | -55.6659 | 2026-09-21 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0da0c097-5414-34a6-9936-bde7bb515098 | -6.467 | -59.9902 | 2026-09-21 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 983434ee-8264-39f8-9d9c-9b5c23d909b2 | -10.5906 | -57.4936 | 2026-09-21 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 961cf76b-c6c7-3288-8503-fb3ea355bf6f | -6.3195 | -60.0147 | 2026-09-21 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 43910192-b2e7-3fcb-aa33-e5fb050ef29b | -10.7813 | -50.8262 | 2026-09-21 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| bf773f97-6d26-3444-b500-835b3e683c01 | -2.8791 | -57.8184 | 2026-09-21 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d70e8dc6-6227-38fe-9d83-2f15feb9352b | -10.0712 | -50.26 | 2026-09-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 649f915a-5eea-37db-a804-f941478fceef | -9.5594 | -66.0359 | 2026-09-21 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4535c140-9d1a-3820-9890-a3aaecb73b99 | -4.3541 | -55.6653 | 2026-09-21 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 59f99bd0-fe37-3ccc-8d39-dfcece4736d1 | -6.8754 | -63.107 | 2026-09-21 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9a4f7e3d-4e06-31cf-a766-7f2cca5adc28 | -11.8204 | -49.8106 | 2026-09-21 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 636c1c26-a5de-35d6-9871-baec51452c0c | -7.2519 | -55.5994 | 2026-09-21 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 624da0b9-4c6e-32c6-bf44-4ebcde79bc02 | -5.7615 | -57.5807 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 341d8b8e-1eb2-3ec4-bb51-52402ba8eff4 | -10.485 | -50.3674 | 2026-09-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 807e9887-6e71-33a3-b40a-0a3e4c392f05 | -10.7437 | -50.8089 | 2026-09-21 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 3bc7a985-4875-3bec-b6d8-d45a87454af0 | -10.9112 | -53.9635 | 2026-09-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b785816a-8b8f-3517-a00e-a0ad16ccbe7e | -7.5889 | -57.6757 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 3aeee61a-b33a-352d-9a65-ee1d32f7f796 | -16.2967 | -49.9133 | 2026-09-21 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b3e0898f-ca22-349d-92f7-3395d675124a | -10.2173 | -59.403 | 2026-09-21 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 2ae7c29a-b19c-3ab8-bd13-e0ce38f33f3a | -10.4853 | -50.346 | 2026-09-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 61219d94-302e-3015-8a0f-186db8723f50 | -7.5888 | -57.6953 | 2026-09-21 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| e45f9775-7f9f-341d-bae1-8b0dc813dde9 | -10.7064 | -50.7703 | 2026-09-21 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f27cfda8-3393-38bc-bb6f-e9116a64e0ce | -6.7464 | -59.4223 | 2026-09-21 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| bd3c2ef8-c924-3e72-ae54-4c7bdd469d60 | -6.4485 | -59.9909 | 2026-09-21 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8e300ba4-32de-39d9-b2d2-ab442d38889d | -3.0535 | -61.2578 | 2026-09-21 00:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a05b9b58-5c40-3c3d-9447-1501f08d0c09 | -2.8791 | -57.799 | 2026-09-21 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 31cca587-0d0c-3730-b9bf-3ef842aa2996 | -6.467 | -59.9902 | 2026-09-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 6c68bd82-a357-3b8a-a498-18fb431971dd | -7.5891 | -57.6561 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| feac6db6-9826-346c-80bc-0e656d0e0bd7 | -4.3541 | -55.6653 | 2026-09-21 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ecd447e7-bd51-328b-b717-dcf0ae55ccd2 | -6.4485 | -59.9909 | 2026-09-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 522ca9e0-9126-36dc-a549-61f6a0d75297 | -10.0712 | -50.26 | 2026-09-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| d8458a9c-6f93-30d3-bb96-48ef8b354a33 | -5.2168 | -56.1096 | 2026-09-21 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| df68ae3e-3968-36db-b20d-27d543bd0171 | -10.485 | -50.3674 | 2026-09-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 6686e389-8a51-38da-a975-dc7f661781f8 | -6.4671 | -59.9711 | 2026-09-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7f1a3988-e6d9-33a3-93bc-497eb02d98c2 | -10.2173 | -59.403 | 2026-09-21 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9da77c8d-bdc2-378a-8cfe-475b845a1ed6 | -11.8204 | -49.8106 | 2026-09-21 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3708035e-bdc2-327a-bc6c-366c35b68248 | -3.4241 | -59.2535 | 2026-09-21 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 682cb6c2-84bd-3496-888e-498614e9cd95 | -5.7615 | -57.5807 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 501d9bd9-327c-364e-8568-d702f86b252a | -4.3357 | -55.6659 | 2026-09-21 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 00dd0f69-4fa5-3843-b1c1-3083c45431c8 | -3.0717 | -61.2764 | 2026-09-21 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ab6c8320-989b-340f-960d-fac976bc53f7 | -7.2519 | -55.5994 | 2026-09-21 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ecdf7a52-44b6-34af-b1ed-e016eb589a53 | -3.0535 | -61.2578 | 2026-09-21 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 354a8f57-6ed4-32d9-a627-fcfac88a2b45 | -3.0534 | -61.2767 | 2026-09-21 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 40b5feec-b931-3741-b3ff-07d8199e0370 | -11.8017 | -49.7913 | 2026-09-21 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 04a1c0f8-6411-3ef1-b8dc-44e7fed60307 | -9.5593 | -66.0545 | 2026-09-21 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b1409930-cd00-34dd-bc79-56d68d57e433 | -6.7464 | -59.4223 | 2026-09-21 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ceec9f60-e2a1-3550-869a-8e1ff4167df7 | -7.5888 | -57.6953 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 629ca0e2-e575-3677-96d2-9cf6b81c13a4 | -10.7437 | -50.8089 | 2026-09-21 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8697c7d7-a6e6-30df-b942-345b86d2ce5a | -11.041 | -54.1567 | 2026-09-21 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5dec4ee4-f71f-3d20-a212-6876aaeb64f7 | -10.0714 | -50.2387 | 2026-09-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| bbb359b1-2d11-3b9e-a9d2-215bd34553e9 | -9.4757 | -45.4156 | 2026-09-21 00:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c101fb36-8345-399b-8c65-f0549b8107ca | -10.7629 | -50.7857 | 2026-09-21 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9b71e1b2-63fd-3b43-bea6-0ea85a375fb0 | -3.4424 | -59.2531 | 2026-09-21 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e8fece05-b3fe-3d86-8369-5afbc365fe8d | -5.7614 | -57.6002 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 07e45683-0013-388c-928f-19b69db7fb17 | -16.03 | -52.5135 | 2026-09-21 00:50:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| eb5337cb-fd4f-3e68-8c42-62b817cdeb35 | -10.0523 | -50.2619 | 2026-09-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d2b723be-a7b6-353e-8e50-dc106fec16cd | -10.5042 | -50.344 | 2026-09-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b34cb315-2522-3b94-801a-864014e4b236 | -9.4567 | -45.4178 | 2026-09-21 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5c3cd7d8-a3d1-3860-a8de-ad16fd9c6c81 | -11.8014 | -49.8129 | 2026-09-21 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 44d3294a-fd0a-3821-b494-147e68158f60 | -6.8754 | -63.107 | 2026-09-21 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 409fdba8-cba0-3948-87d9-556f37d297e1 | -13.9118 | -48.5669 | 2026-09-21 00:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6f649ca5-6a33-3e3d-a693-2bcbe8fb565c | -6.3195 | -60.0147 | 2026-09-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9e2d50fd-b595-35c7-8477-11a88c5f6e73 | -7.5703 | -57.6962 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 995e3c2d-2585-3d1b-9d23-a775a27c2196 | -2.8791 | -57.8184 | 2026-09-21 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ac2babb7-9178-3c43-bda7-250e1281f729 | -7.5704 | -57.6766 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| a9d69dd7-646a-3e28-a835-1df69ab35592 | -3.424 | -59.2726 | 2026-09-21 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| a8c7201d-ca15-3088-90f4-ce67b9c159b4 | -10.744 | -50.7876 | 2026-09-21 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| d2499fd5-303a-3426-ab7e-70f0a40b4b18 | -6.2026 | -57.7778 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5676af98-4475-37b2-89ac-fb8df98bd2dc | -6.4486 | -59.9717 | 2026-09-21 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8c24b4a9-59e3-3324-a3a7-556d6b1907a6 | -2.8791 | -57.799 | 2026-09-21 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bbacc132-3b13-3965-90c3-9000fe208047 | -9.5594 | -66.0359 | 2026-09-21 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 47c6cab1-5f11-3fd5-bf0e-38b57c8f6409 | -10.4853 | -50.346 | 2026-09-21 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 4d67b9c6-569e-3c19-a799-73077c210827 | -14.8465 | -49.2863 | 2026-09-21 00:50:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c91e24b1-49c4-301e-a09d-6099c0f9fbbd | -3.0717 | -61.2575 | 2026-09-21 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 01b4605c-45b8-3388-b3e3-abafdff9b9da | -10.7626 | -50.8069 | 2026-09-21 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 7258567f-de43-3110-879f-dc8f0347d53a | -7.5889 | -57.6757 | 2026-09-21 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| ab830121-0075-30ee-a490-340d2fb7859f | -6.4671 | -59.9711 | 2026-09-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 40017e00-dc1e-3139-9475-9395d63e2667 | -9.4564 | -45.4406 | 2026-09-21 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4ba1b62e-2029-32a5-8467-549b485ce374 | -7.5704 | -57.6766 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 1bdb0bd1-1eee-38dd-ac5e-d94efe0d2c9f | -5.7615 | -57.5807 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |


[Clique aqui para ver as próximas entradas](README11.md)
