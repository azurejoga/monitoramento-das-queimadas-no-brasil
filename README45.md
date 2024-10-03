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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf087139-0fab-3131-ae5a-c06a4d0a6721 | -9.0073 | -67.525497 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2ee95c1-fefc-3385-bbae-c103854abc66 | -7.1819 | -59.77 | 2024-10-03 01:51:21 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55b39116-cfc3-393b-9914-10291cee1f11 | -7.1858 | -59.785999 | 2024-10-03 01:51:21 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb789d91-ae9c-348f-bef1-28a10a3a6cba | -9.0448 | -67.786697 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f4e2fae-d2b3-31d9-b73e-fbf4043fc298 | -9.0464 | -67.793701 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 601d3343-fbf5-3b85-b316-c15882b51bd9 | -9.0495 | -67.807602 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd56a76a-5df4-38a6-889f-62d152dd2fd1 | -9.0572 | -67.842499 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dff63f1-d4df-3d50-8096-28c0c72a2911 | -9.0588 | -67.849503 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e52a3051-a45d-3a7b-8cfe-c424d22534a8 | -9.0366 | -67.795898 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a709aa88-2ee3-34e9-949f-a1570f5a4ed7 | -9.049 | -67.8517 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a431250-1f12-35be-ab80-3ed239947343 | -9.0505 | -67.858704 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1c09c4-f0d4-3dd9-8593-c687d1c0f5e6 | -9.0521 | -67.865601 | 2024-10-03 01:51:21 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d42454f-e88d-3091-b47a-4244efc0db97 | -9.0113 | -67.7285 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c009c876-edff-33c6-855b-c261e6bc7df3 | -9.0128 | -67.735497 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6da09dab-f0dc-3838-adcf-5a7cb4f74872 | -9.0144 | -67.742401 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a61dc0b8-fd50-3b2a-980a-07ee9b826ee7 | -9.0267 | -67.798103 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c29c016-b3db-3a97-9c46-6dd66a3f0b92 | -9.0283 | -67.805099 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14d4f0a2-d6f0-3332-9d14-74f5944cc6dd | -9.0407 | -67.860901 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6afdda4-1f14-337c-afcb-d616c5f9a07e | -9.0422 | -67.867798 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c7b0504-c4e4-3fee-9e15-a788e1820f84 | -8.9129 | -67.3797 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe00954-ca37-30c9-8be3-ad7c927bf09f | -8.9973 | -67.804703 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c667e21a-8352-31db-9824-8a2367b9e262 | -9.0511 | -68.093803 | 2024-10-03 01:51:22 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 062e6ea9-1c43-3afb-93ba-4e0556e5ad34 | -6.8681 | -59.035 | 2024-10-03 01:51:23 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ddc21385-9c32-322e-b8aa-f71080262131 | -8.6544 | -66.595901 | 2024-10-03 01:51:23 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 765ca680-33fa-3289-bd75-cad860866e31 | -8.656 | -66.602798 | 2024-10-03 01:51:23 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a94a1ca2-b5dc-3205-b82d-d41de30b880b | -8.8314 | -67.383499 | 2024-10-03 01:51:23 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a413c7a-6b2d-39a5-a8eb-07dc86d5d2a9 | -8.833 | -67.390404 | 2024-10-03 01:51:23 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7d1c87b-61bd-3293-85ad-c2965b4b6ed1 | -8.6446 | -66.598198 | 2024-10-03 01:51:23 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff00210-e1f0-35ee-a400-93328bd16428 | -8.6602 | -66.667603 | 2024-10-03 01:51:23 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d722b17e-7305-3ebd-8dd9-c235a817c7ea | -8.6489 | -66.662804 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91b9d4e3-8327-3e97-a249-a98c48c703ae | -8.6504 | -66.6698 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6ad850-5415-3cb4-a054-11a2a5daf041 | -8.652 | -66.676697 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5072a92e-667e-3fb4-a6da-2289bc68cbc5 | -8.6469 | -66.699699 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02c3ef89-503b-3781-a66a-9880b5bf4f37 | -8.6485 | -66.706596 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 037daa88-644f-3cdf-9317-c204b27a8eb8 | -8.6371 | -66.701897 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a41baa03-a959-3875-bc66-da22e3d08e22 | -8.6387 | -66.708801 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c4eb82e-9e38-3ca0-a5b8-b30398b9e12e | -8.6402 | -66.715797 | 2024-10-03 01:51:24 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8d78f53-8122-3c63-8dbe-0d8043499c95 | -8.6664 | -67.014999 | 2024-10-03 01:51:25 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6350dbca-9612-3d49-ba3f-dbeb6cae0fc3 | -8.7755 | -67.6866 | 2024-10-03 01:51:25 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea8c34f1-f609-3311-8d33-e982275069f0 | -8.7657 | -67.688797 | 2024-10-03 01:51:25 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97b0eb01-a429-3fa2-abd4-6d3fb771cce4 | -8.7672 | -67.695702 | 2024-10-03 01:51:25 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cbd197e-a057-34a1-afa5-8d497498e10a | -8.7559 | -67.690903 | 2024-10-03 01:51:26 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0901e050-d5da-374d-8e51-b16869917100 | -8.7574 | -67.6978 | 2024-10-03 01:51:26 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 932b3ed0-3208-3cd1-a2c5-83960d7eda0f | -8.7829 | -68.789497 | 2024-10-03 01:51:29 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d84718b9-987a-3a54-b97e-36b957000d44 | -8.7845 | -68.7967 | 2024-10-03 01:51:29 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e38c3bf-23de-3f20-9751-8417ce515a15 | -8.7827 | -68.835297 | 2024-10-03 01:51:29 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6e92c4c-88a6-334e-8ae8-848411b3d4a6 | -7.6758 | -64.9739 | 2024-10-03 01:51:33 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0943d6c5-ea17-3314-8be0-1ab82ff2e265 | -7.459 | -64.438103 | 2024-10-03 01:51:35 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 711f3b9b-d4b7-3a00-b578-92269a730a46 | -7.4473 | -64.432198 | 2024-10-03 01:51:35 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac29a14-5121-333e-9f63-a3af7904472f | -7.4492 | -64.4403 | 2024-10-03 01:51:35 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50bd3235-df6b-389d-ba1d-dddc1743528a | -7.4625 | -64.675797 | 2024-10-03 01:51:35 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cbc1a13-b9f6-3814-a933-4ff22a378517 | -7.0267 | -63.074001 | 2024-10-03 01:51:36 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e841b5c-d5c6-3ec3-8931-7a17a33e82b5 | -7.029 | -63.083801 | 2024-10-03 01:51:36 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4671c3a4-d906-3a07-9525-4efb7eb1e876 | -7.3787 | -64.669899 | 2024-10-03 01:51:37 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8df7a2f9-bbed-38d6-bda3-269cf9e3b414 | -7.3805 | -64.677902 | 2024-10-03 01:51:37 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b53d3b3-f0b2-3f66-bb34-e5d6c9913024 | -7.291 | -64.647903 | 2024-10-03 01:51:38 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1daa235f-faff-3071-bfac-1b25e1aaa66b | -7.2929 | -64.655899 | 2024-10-03 01:51:38 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26e7d5a4-73fa-3d22-8b17-9c6f3750a1ad | -7.6441 | -67.187401 | 2024-10-03 01:51:42 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20a06f87-6342-3381-85ef-3caf52fa9397 | -7.6456 | -67.194199 | 2024-10-03 01:51:42 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 559c6024-5b50-37e5-a627-ce6ef96b2202 | -7.6343 | -67.189598 | 2024-10-03 01:51:42 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5555efc-8d5f-313b-8bc3-5a7a05ebd537 | -7.6358 | -67.196404 | 2024-10-03 01:51:42 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| caafc55d-6f35-36d6-989b-78d052540fe5 | -7.6374 | -67.2033 | 2024-10-03 01:51:42 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6b3da22-ee07-342a-bf94-9e94c98be619 | -8.1816 | -70.080299 | 2024-10-03 01:51:43 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fea215e6-36cc-3e9b-ae83-54de384de734 | -8.1257 | -70.4841 | 2024-10-03 01:51:46 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 92e0076d-470f-3905-bb6f-55efb8a19f2b | -8.2556 | -71.133797 | 2024-10-03 01:51:46 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ccb94c93-96e5-3b0a-acb6-8ab8ec834b34 | -7.3731 | -67.999603 | 2024-10-03 01:51:49 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57362122-8b2a-3863-97cd-fcef6952e593 | -7.3747 | -68.0065 | 2024-10-03 01:51:49 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b477e4b-6164-3f75-a577-d61186aeaa45 | -7.3762 | -68.013397 | 2024-10-03 01:51:49 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9e3e710-a10c-33a5-8acb-c3238bbeabeb | -7.3633 | -68.001801 | 2024-10-03 01:51:49 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03118fd0-991c-3b2a-a210-a221e850cbf4 | -7.3649 | -68.008698 | 2024-10-03 01:51:49 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b93e811c-f3f2-3c8a-baf6-6ea82b454e37 | -7.3664 | -68.015602 | 2024-10-03 01:51:49 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5cf6b0f-3c12-31f5-8aed-9922d18190e0 | -7.9266 | -71.462402 | 2024-10-03 01:51:52 | METOP-B | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5e962293-63be-3390-a6a0-5357224e2bfd | -7.5304 | -70.3899 | 2024-10-03 01:51:55 | METOP-B | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6edde6eb-d05b-3237-8fee-e1e679a5a8e3 | -7.8821 | -72.787201 | 2024-10-03 01:51:58 | METOP-B | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 40318dad-f141-3090-b2ed-141a4d070aea | -7.4264 | -72.7108 | 2024-10-03 01:52:05 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33be02a4-9ec4-392f-823a-3325bd481b40 | -3.3855 | -42.263 | 2024-10-03 01:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| bc6628d9-a32b-3d7f-814b-aab1439f9118 | -3.404 | -42.2858 | 2024-10-03 01:55:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 75baa246-ac04-334c-aca3-c31d54d33b76 | -3.4042 | -42.2621 | 2024-10-03 01:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a25e0a25-e581-317e-a819-37f7c799716d | -3.4229 | -42.2612 | 2024-10-03 01:55:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 64c7d360-62cd-3339-b1e8-a0d8240f0bca | -4.0949 | -48.4894 | 2024-10-03 01:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ec897391-8381-3371-8f6a-f03ed0923da0 | -4.095 | -48.4679 | 2024-10-03 01:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| f0502456-6eae-3ca0-855a-5da1021d24dd | -4.5375 | -43.304 | 2024-10-03 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 09b34d8b-634c-3540-ac45-0e8608a8718b | -4.58 | -48.0132 | 2024-10-03 01:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c2360dc5-b97c-3726-973e-166d25a1ac72 | -4.9264 | -43.79 | 2024-10-03 01:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 45d26365-6060-3130-bbf3-1e417d7d600e | -4.9265 | -43.7669 | 2024-10-03 01:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| ea289831-b288-37a5-bab7-1a51a01efa06 | -6.8777 | -59.0504 | 2024-10-03 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9e212f90-11f4-344c-b737-c3762c5365c0 | -6.8778 | -59.031 | 2024-10-03 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 166430e7-a476-3c07-836a-ebb28d445fca | -8.8506 | -45.5086 | 2024-10-03 01:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 4aa839a6-ba7b-3ef4-a730-39fc6b20133f | -8.8509 | -45.4859 | 2024-10-03 01:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 0d3e04a1-78ef-3788-ae40-b982b5f8691f | -8.8695 | -45.5066 | 2024-10-03 01:55:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 1e4e982c-e833-3680-bcea-5f569c8cab30 | -8.8926 | -62.3348 | 2024-10-03 01:55:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a8edbb32-bd48-34af-9172-13b0f4000028 | -8.9791 | -67.4099 | 2024-10-03 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 8e468c74-3a0c-3135-ab99-d746d2558b64 | -9.0149 | -67.7423 | 2024-10-03 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7f59362d-f07a-34b8-9aed-3a020bf695b8 | -9.0515 | -67.871 | 2024-10-03 01:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0777eeed-6707-317b-88b7-7de1af6da0c3 | -9.1566 | -61.6758 | 2024-10-03 01:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fb9a16f2-696e-3330-81f5-1ad69883fe5f | -9.1752 | -61.6749 | 2024-10-03 01:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9c5a32aa-b509-3db1-a42b-c4674f9a1962 | -9.3839 | -61.0526 | 2024-10-03 01:56:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ed54a7f0-7a1e-3f18-b063-e7442b02ced5 | -9.4368 | -64.5419 | 2024-10-03 01:56:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9818440d-f555-3b62-afd3-f60090244dd6 | -9.468 | -62.3857 | 2024-10-03 01:56:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 0c3cc8ea-76d4-3d12-a140-53bb4905a3bc | -9.4865 | -62.4039 | 2024-10-03 01:56:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 38.0 |


[Clique aqui para ver as próximas entradas](README46.md)
