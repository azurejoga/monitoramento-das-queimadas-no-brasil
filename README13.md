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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8014268a-631c-3081-b7fb-56c6b6c2569b | -3.49343 | -50.45914 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fb6b603-3c97-3047-803b-211e5ec79d64 | -6.35374 | -46.47109 | 2025-11-04 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d85edd3-6d40-353b-afb5-5fc86d3fe72b | -5.98533 | -41.92247 | 2025-11-04 04:10:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b67594d2-18f7-3568-99bf-192b4a4f6c8f | -7.0861 | -38.82634 | 2025-11-04 04:10:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d6647f1-f7f0-3749-9e0e-3579284b9367 | -5.73875 | -39.45948 | 2025-11-04 04:10:00 | NPP-375D | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 55acb0dd-6f83-389c-b869-9d905d41ceec | -6.32693 | -46.32574 | 2025-11-04 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93d31394-3f33-36da-90fa-5bfbfd198789 | -4.87783 | -49.00413 | 2025-11-04 04:10:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b25e4fe-59fd-3c46-aa85-e4e9384e3290 | -6.0648 | -47.28586 | 2025-11-04 04:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 084348da-bab2-3968-8a04-973fa74a7695 | -1.22011 | -49.15201 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43bba070-d9d2-3219-8b22-a6eee8abd89a | -5.75967 | -45.90073 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23944e3d-76d0-301d-9814-494bb14358bc | -4.91831 | -47.3302 | 2025-11-04 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3358f4fa-d679-3259-8ba7-c62e39dd2c61 | -4.52004 | -45.25254 | 2025-11-04 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e2f8729-451a-3092-8e19-c5077fffad0c | -4.69429 | -45.68213 | 2025-11-04 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6345537f-f88d-37a4-a56c-b8eac1e7aaf0 | -4.46755 | -43.23451 | 2025-11-04 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d554be8b-0d7d-39e1-9cca-c16dd9fca908 | -6.70201 | -39.12176 | 2025-11-04 04:10:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 31809f09-2ca9-326d-ae68-9ce52a2b4bb3 | -6.50383 | -42.06527 | 2025-11-04 04:10:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f2099f14-c0a8-3446-b56f-ad63e70c65ee | -6.13293 | -41.54444 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1efc8300-3d31-373e-8041-09d4cece1588 | -5.62624 | -41.09146 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0dbd6e92-5d1e-38ac-8616-c4c0b784c7d2 | -7.42675 | -40.72042 | 2025-11-04 04:10:00 | NPP-375D | MARCOLÂNDIA | PIAUÍ | Brasil | 2205953 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 39bc7250-41ff-33c6-a60f-be2fe42be4fb | -4.5392 | -40.14992 | 2025-11-04 04:10:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 11e88716-8a6a-30b4-8321-15214f3432df | -4.5797 | -43.34116 | 2025-11-04 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 442ba794-fb2c-3c39-bf88-620aaf45b267 | -5.60359 | -41.10563 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 54bae990-b8a4-36b4-b3f2-9202400ba06f | -6.40221 | -43.06685 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a929605-1578-37c9-8df8-10ea19bb6e82 | -6.10107 | -41.70271 | 2025-11-04 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d7094006-d8c9-3218-a532-034f6add3292 | -5.03405 | -43.61515 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38633661-0fbe-3cff-9943-e671d2ab314f | -3.43319 | -42.54157 | 2025-11-04 04:10:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2c5dbdc-f755-32b7-92dd-d20c1d7dfa54 | -5.37162 | -44.74183 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3f611c05-e31c-375d-8884-0406b886fce1 | -4.38234 | -46.27393 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a2f9b58-0ac1-3d69-8180-d19139fd8d97 | -4.91466 | -47.32526 | 2025-11-04 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fc4f405-997f-3ec1-aaea-3d90769174d3 | -6.40618 | -43.06375 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe46b61f-4957-3382-87f9-7ac51e8bdb30 | -6.46814 | -43.22361 | 2025-11-04 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 50e7dc10-cde8-33ac-874a-b9091de5b97b | -4.9557 | -44.9032 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2263341b-5154-31b9-abdd-7bda33ecedec | -5.83646 | -44.07164 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf265448-ee33-3274-994b-16824e485028 | -5.60275 | -46.26198 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c3fbd54-00a7-3099-ac13-d8dd3f163466 | -3.91901 | -47.6977 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ebd39bff-f802-3c04-8b76-fd666cd18ab6 | -2.98202 | -48.70658 | 2025-11-04 04:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ff151d7-595c-33c8-8c28-e15f52f75926 | -5.92443 | -41.32675 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c1c2473-3f5d-3d0e-ac0b-db6c1b0d3459 | -6.14398 | -44.57928 | 2025-11-04 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25807ca6-9351-3f5f-9046-bddb99275135 | -4.74203 | -46.56696 | 2025-11-04 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02ea9572-cc94-3c55-bb5e-5f8f2baf9f18 | -5.27431 | -48.5053 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88b03149-92c7-3edb-b126-256bedb45ab7 | -5.93385 | -41.33178 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aaffeba2-9fcf-36cc-8e26-5ee047c27404 | -5.92384 | -41.30892 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a43fb63-ab89-3823-a78c-a3cdb92e69b0 | -3.92052 | -47.68845 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ea10bec7-00cd-3b14-a234-8782d21911f9 | -5.12574 | -37.96437 | 2025-11-04 04:10:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44aedbd5-fd7c-3dc4-9de0-007bb95253e3 | -2.62381 | -49.22795 | 2025-11-04 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cc9bdf7-c2bc-39ca-9dfc-6ca53575e089 | -5.92552 | -41.31983 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1468bd2c-7b78-3f87-ac2b-de52e349be49 | -2.12003 | -46.18154 | 2025-11-04 04:10:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5c92d04-0234-3d51-a40b-298a2faa6eb9 | -4.65052 | -46.28881 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 882809d2-235b-325b-a17c-0e9edf31e15a | -6.10164 | -41.74193 | 2025-11-04 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b877467e-078c-3e5a-af01-f081f728c477 | -5.43253 | -44.66182 | 2025-11-04 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccd0cc45-1a3b-39dd-8edb-0a17522d7ad3 | -6.2263 | -37.42209 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c87f9458-3998-36be-a5b5-514358a01783 | -6.40899 | -43.06793 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30c03b19-0380-3420-a027-18c20eb718c1 | -5.30365 | -44.81082 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c1a3877-9d78-32ea-bd39-a97845756143 | -1.21971 | -49.15157 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08e33c51-d80b-38bc-8581-11cc0d68aac7 | -6.16261 | -47.24571 | 2025-11-04 04:10:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7cdc5e9-20c2-30bc-89ff-6e28cddfdd28 | -4.96686 | -44.90516 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 865f5f65-0ab4-361a-af0f-0206f513780b | -4.31425 | -41.44817 | 2025-11-04 04:10:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86fe6c7e-0475-3330-bb5b-8529cedf1ee8 | -3.49828 | -50.4639 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bab38568-ce43-38dc-afcb-d74cdc645697 | -3.54992 | -46.36186 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5b4c783-feed-3e83-bc47-1eb1db470171 | -3.44324 | -53.2625 | 2025-11-04 04:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fc06219-c478-3e06-9af4-15ad0018c749 | -5.52536 | -41.13244 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0a3cba36-164c-3606-948b-ddfa8b393d6b | -5.24 | -44.21568 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c700259-6bd1-38bf-bdf3-49009101b8ba | -5.22056 | -43.75178 | 2025-11-04 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9ff19fb-79e6-3982-9a84-2b75d869f375 | -5.03627 | -43.62344 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5c09a371-5d05-39ed-8ae5-2de8cd364e1a | -4.9349 | -43.41949 | 2025-11-04 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47eb8f74-b71e-30eb-abd0-ad37a58965ef | -3.41289 | -44.4374 | 2025-11-04 04:10:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 847b1ec3-a381-3a06-b9c2-7a19a0f421c8 | -4.61819 | -46.1046 | 2025-11-04 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2fd47c9-76fd-3e1b-8f0f-210f579b2f08 | -4.64992 | -46.29243 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85bec6a8-3f49-3637-8ad6-8490a36dbcaf | -3.50313 | -50.46873 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77edb69-5333-38bf-9523-a4eb1257a365 | -3.44228 | -53.25708 | 2025-11-04 04:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cb043fc-be53-3d76-89a6-f7175cf33185 | -7.30061 | -39.35193 | 2025-11-04 04:10:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5bf1169c-d5e3-3da7-883a-586652cc0c51 | -5.78271 | -43.95849 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a0af0a7-eb85-3474-98d8-4e8b52bc49b7 | -5.61184 | -45.97414 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5d67bbf0-6b7f-3fd6-92ea-8e8da5d0bd0a | -5.23056 | -44.20585 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ace8d1ff-e742-373e-b467-8c45f35c8ec9 | -4.47569 | -43.22808 | 2025-11-04 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 08e551d2-1cc0-37ae-9db7-dd28fb838311 | -4.90954 | -45.09099 | 2025-11-04 04:10:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff6fc001-3163-3d55-9bc6-97bb651369e5 | -3.04529 | -50.27423 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea6f4981-ce6d-36fc-a2e7-c1d052fec995 | -2.49346 | -45.97254 | 2025-11-04 04:10:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 516decc1-04ba-3abe-8577-444e09380195 | -3.6135 | -40.37798 | 2025-11-04 04:10:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 334cc189-ccab-3f87-9f88-1fb7fce61af3 | -6.13902 | -41.54896 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ddf9ca7-c0a5-3039-9efb-9be09150b384 | -3.50249 | -50.47247 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bece2fa-d511-3c56-b2ce-5ed350880ee3 | -5.61827 | -45.97677 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4d4b18da-1d59-377d-9b92-b56f3d043cca | -6.40841 | -43.07157 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab0c1df2-9829-3c54-ae30-82813791cfbb | -6.4056 | -43.06739 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd53c6a9-b017-3162-b703-20d932c3efe0 | -6.13957 | -41.54549 | 2025-11-04 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ea242fb-3e12-3d71-94b9-5433d7f4f7a4 | -4.02161 | -45.46198 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc4cb86a-67da-345b-9a96-619f0e8bb059 | -3.76856 | -52.32571 | 2025-11-04 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15cf66d2-e44c-39ec-9082-c57f195b8d55 | -5.83778 | -44.06363 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5237f1f6-ce8f-3dd5-8955-81ca69e12782 | -3.91523 | -47.69231 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6c72a566-169e-3b3c-aab7-f02cfa24ee9e | -3.69411 | -49.564 | 2025-11-04 04:10:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9fa4d9d-c957-360d-9ed6-20204ab56d76 | -5.98866 | -41.923 | 2025-11-04 04:10:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 909c2d83-8ac9-3e08-a536-8f036456dbb2 | -4.19654 | -45.68877 | 2025-11-04 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 027bcd28-bf9a-3835-88fb-107239e9ff0b | -5.89158 | -42.91937 | 2025-11-04 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d579464d-9129-373e-b840-4e888451c0fc | -5.03242 | -43.61974 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| afcfd65c-62c2-3150-94a0-001422acdeca | -3.92484 | -47.69627 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e147253-1672-349f-b5f9-6ba7fc76e80f | -4.96243 | -45.51594 | 2025-11-04 04:10:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3600cd30-2336-381b-9de3-352115b522a0 | -4.61834 | -46.40684 | 2025-11-04 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5019d6df-617f-3e57-81e5-2c872d61d171 | -6.4118 | -43.07211 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 293786a6-960a-3401-8eef-5451f87b9fc8 | -2.63568 | -54.57316 | 2025-11-04 04:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 392fa715-58a4-331f-bf76-bc5495d3a919 | -2.84295 | -49.83691 | 2025-11-04 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README14.md)
