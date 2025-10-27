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
| 6ace6306-e401-3cb9-a8ab-f8fb908625d8 | -8.48941 | -41.23187 | 2025-10-27 03:21:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 488fa06d-e520-3524-8a4f-753b9d4cf429 | -11.66971 | -41.31957 | 2025-10-27 03:21:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ade11422-91e9-3e19-a726-173ba8f187e1 | -12.2802 | -43.75612 | 2025-10-27 03:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f12704c-a707-3c98-9738-1a16f00aeebf | -19.61408 | -46.18868 | 2025-10-27 03:23:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5a28ca9-be91-335c-a885-11100ec8abc9 | -18.26772 | -45.38045 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9a3b4b4-c16c-30c0-acdd-fc7012bab82f | -17.32014 | -43.65375 | 2025-10-27 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d9814973-3e18-3df3-ab78-bfd65c7b9c2f | -18.26382 | -45.36669 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd76081c-f504-331c-a749-40c2dc3abe41 | -15.32497 | -43.80618 | 2025-10-27 03:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4cb19ff6-e297-3450-bdbd-03ec3ce04f0d | -19.66505 | -44.66029 | 2025-10-27 03:23:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0dfafffd-2f75-32fa-aa1a-088519bbe1d5 | -18.2704 | -45.36898 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb32e7b8-7059-3854-bee9-015da2f10ccc | -15.29329 | -42.94161 | 2025-10-27 03:23:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fefb975c-a7d2-3a69-a1dc-b333aba66f53 | -19.91804 | -44.8176 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f260b28-6837-35a6-a820-d3324acac4d3 | -19.91882 | -44.81967 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2884df02-033e-333f-8e52-229d879cd89d | -19.88703 | -44.37253 | 2025-10-27 03:23:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56acdcf4-73d0-3ea6-95bb-0a061fa1acad | -17.32533 | -43.65985 | 2025-10-27 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 83a78e2a-25a3-3c85-b313-a40a66bbb93e | -16.62416 | -44.59435 | 2025-10-27 03:23:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10ee0afb-a6ef-3b47-8de8-d43fc543eeb2 | -15.29691 | -42.93888 | 2025-10-27 03:23:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24058b5a-8608-362b-8e68-60bb6a4046f9 | -17.32059 | -43.60865 | 2025-10-27 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d172dc3-2a40-3a26-be1a-a7deb1ee0054 | -20.76278 | -43.2295 | 2025-10-27 03:23:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e6b97512-6bf8-3754-b510-1b43174a6cff | -20.75042 | -43.23113 | 2025-10-27 03:23:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d30e6eb2-ac66-33e7-a611-9742afbb4871 | -19.66391 | -44.65961 | 2025-10-27 03:23:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4ec5aeaf-53b7-3f2b-9cd5-7ddf7cf8e2ff | -17.32644 | -43.65488 | 2025-10-27 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 12bc01c2-b78b-345a-a337-03ff0b430d71 | -20.75622 | -43.23201 | 2025-10-27 03:23:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 22b2a008-3609-35d0-a8cc-246ed662e320 | -18.62894 | -43.0687 | 2025-10-27 03:23:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fbbbedc5-2ab7-3308-81d4-f34556c61403 | -19.69335 | -42.26118 | 2025-10-27 03:23:00 | NPP-375D | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 836b1678-c0b7-3ca2-9575-b09be40057e5 | -17.31326 | -43.61232 | 2025-10-27 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc76b875-1247-3ba3-a56d-259f7efb7008 | -19.87472 | -44.17922 | 2025-10-27 03:23:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4451d70-600c-3028-88e3-104cfd4d3cb9 | -19.64075 | -45.39296 | 2025-10-27 03:23:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 442828c1-0f0b-3293-9354-fdf1348d4616 | -17.08086 | -43.19004 | 2025-10-27 03:23:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf8bb049-0606-33db-8547-02acedaccb70 | -19.86855 | -44.178 | 2025-10-27 03:23:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| de603c52-a681-3bf2-bc02-b16f9f9aa659 | -20.75498 | -43.23327 | 2025-10-27 03:23:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3acb177b-e4d3-3f20-bdcf-2a3963d2bb86 | -20.22054 | -42.74321 | 2025-10-27 03:23:00 | NPP-375D | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9352f65e-5f90-3c0b-83b1-cca13171f445 | -18.35057 | -43.96379 | 2025-10-27 03:23:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58f1dc49-8b5d-3af9-b687-643cf064d83b | -18.6299 | -43.06441 | 2025-10-27 03:23:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f09cee77-7882-3d59-aef8-c04dd89192be | -16.62634 | -44.59465 | 2025-10-27 03:23:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac1ee81d-1d1f-3543-bcc6-6dde1c0fce8b | -20.72193 | -42.78341 | 2025-10-27 03:23:00 | NPP-375D | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c4829e35-c1c3-30a5-bae4-ae9854984d82 | -19.55215 | -44.16186 | 2025-10-27 03:23:00 | NPP-375D | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 535e2d5a-8530-330b-b09e-068904fe532d | -15.29074 | -42.93733 | 2025-10-27 03:23:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 350ec5e6-866d-3733-92c6-1fc2f10dfedb | -19.67015 | -44.66143 | 2025-10-27 03:23:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b639b978-8987-36ac-969d-d00210d6e184 | -20.65769 | -42.73124 | 2025-10-27 03:23:00 | NPP-375D | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5d5cb051-c647-393e-ad5c-c4988f082af3 | -21.37826 | -43.60128 | 2025-10-27 03:23:00 | NPP-375D | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c4dfaa9-c349-3cd4-a2e0-5c1d3ac05a10 | -18.58177 | -42.74339 | 2025-10-27 03:23:00 | NPP-375D | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7d4f914-7e29-3a6f-9cdf-4469c2ea634c | -18.58084 | -42.7477 | 2025-10-27 03:23:00 | NPP-375D | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 71f7cf1d-477e-3edc-83fc-df9215b6ddc9 | -19.9243 | -44.81945 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0a17181-7dd8-3774-afa8-7fbc98eba575 | -18.58035 | -42.74478 | 2025-10-27 03:23:00 | NPP-375D | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca1ea864-907f-3460-99db-cda0ffd43da1 | -19.54839 | -44.15955 | 2025-10-27 03:23:00 | NPP-375D | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ccab9d4-8497-37b2-b40c-c538e6cd2c89 | -18.63477 | -43.07027 | 2025-10-27 03:23:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d7302cd9-deeb-3124-84a8-ddba2ca39e75 | -19.66283 | -44.66433 | 2025-10-27 03:23:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4a737210-1eda-3b83-9942-5673a8ed1f5f | -20.65679 | -42.73527 | 2025-10-27 03:23:00 | NPP-375D | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f8cbbff9-83c2-3803-83ab-7a7c10bc5f68 | -20.79862 | -43.31031 | 2025-10-27 03:23:00 | NPP-375D | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b56f260-7f6b-3ed4-b678-a1475a6151fc | -19.66393 | -44.66503 | 2025-10-27 03:23:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 76401b74-0948-3aad-8201-25a999329cc1 | -18.2612 | -45.37789 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7096cd0-2d50-3932-a9d6-4ea4bd22450d | -19.54734 | -44.16419 | 2025-10-27 03:23:00 | NPP-375D | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c540ce1c-b1c8-3406-abcf-2b29819c5821 | -20.75707 | -43.22826 | 2025-10-27 03:23:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f24facfd-7ef6-3fa3-9bca-e8b3860f234e | -19.88586 | -44.37759 | 2025-10-27 03:23:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1c02731-a52c-37c7-804a-1638c46e6826 | -19.6423 | -45.38645 | 2025-10-27 03:23:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95b9aaa5-c5b5-33f6-af67-9d0aeecc6162 | -15.32691 | -43.80718 | 2025-10-27 03:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4cc940fa-cfc2-367e-a40d-e4e5eb46c448 | -19.69256 | -42.2648 | 2025-10-27 03:23:00 | NPP-375D | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8ea1b997-22a3-3103-8a23-faead962c542 | -17.31901 | -43.65882 | 2025-10-27 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d1fba0f2-7435-3e6b-a4f2-eeacc74cf4d6 | -19.15831 | -40.62469 | 2025-10-27 03:23:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26c8c0f5-8841-3b95-8c9c-97e534f0da0b | -16.62784 | -44.5882 | 2025-10-27 03:23:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ac0d077-9920-3c97-b592-49542c02d0ef | -20.66149 | -42.7403 | 2025-10-27 03:23:00 | NPP-375D | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e76d8015-fed3-3ada-9c73-86f92d3ec1a3 | -18.26254 | -45.37215 | 2025-10-27 03:23:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97238a64-b227-3ce1-bb46-028096a7c62c | -19.54617 | -44.15966 | 2025-10-27 03:23:00 | NPP-375D | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7e605ae-876d-39ce-ad38-f34ce9110e66 | -20.7558 | -43.22953 | 2025-10-27 03:23:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 50f8fa29-295c-30ba-8bc4-93c641143a88 | -20.79959 | -43.30597 | 2025-10-27 03:23:00 | NPP-375D | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| adca6416-c932-3777-a6a2-df1d3228a44e | -16.6256 | -44.58796 | 2025-10-27 03:23:00 | NPP-375D | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eada1592-7584-3131-81a7-4fb2992f12eb | -21.66491 | -44.51864 | 2025-10-27 03:25:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a8a8599d-7819-370f-b756-96784de97e82 | -21.58907 | -43.4973 | 2025-10-27 03:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| af512819-03e9-32b4-b5c7-6c1f98e20d2b | -21.59001 | -43.49316 | 2025-10-27 03:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 236c4ba5-bfde-363d-bea9-19dc5e3f6225 | -21.94424 | -46.51195 | 2025-10-27 03:25:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| da1ca4fc-bd2e-385d-a429-fc4eabdcd049 | -21.66057 | -44.50927 | 2025-10-27 03:25:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4ef6b0db-1f50-3c30-8fa4-5833fbcf6ab5 | -21.66003 | -44.51231 | 2025-10-27 03:25:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e6aef20-01d7-3606-8881-a09940b404fe | -21.94104 | -46.52506 | 2025-10-27 03:25:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 98c28d35-84ce-3f15-b5f2-22c0faeca23b | -21.94461 | -46.51952 | 2025-10-27 03:25:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3709b0fa-bdbe-3311-afe4-7613dcb590b7 | -21.66115 | -44.50759 | 2025-10-27 03:25:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02005e63-83a1-3275-ab10-d4a380d4e6e9 | -21.5814 | -43.50457 | 2025-10-27 03:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 97f37e8f-0ab7-319d-b660-79ca2652cf56 | -21.58703 | -43.5062 | 2025-10-27 03:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 90ac6f67-2b8c-33d1-bae8-d6b8e2d1cd23 | -21.9462 | -46.51319 | 2025-10-27 03:25:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| edade3c9-146b-30cf-b613-e4fe1fbff1bd | -21.58802 | -43.50186 | 2025-10-27 03:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 78bc8ce7-b1e1-3707-9c23-7c12ca18fe10 | -21.94268 | -46.51834 | 2025-10-27 03:25:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ff94d202-57be-303f-80e5-98ed7a427770 | -21.93824 | -46.51661 | 2025-10-27 03:25:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9eddf377-03a4-370d-bd87-ffec9f737f68 | -4.4805 | -43.4237 | 2025-10-27 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 0436a94a-55a5-3ad5-aeed-5d808a0cf709 | -7.8223 | -46.4664 | 2025-10-27 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f2c3855c-172c-3a33-a37e-03ce3cd04430 | -4.4618 | -43.4248 | 2025-10-27 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 618c5ee7-c378-317d-9dd2-5189c1fbc643 | -4.3879 | -43.3129 | 2025-10-27 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 60b40074-75e4-371f-b10e-c40c7ca0ca0c | -7.8408 | -46.487 | 2025-10-27 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 1ac6319a-e3ca-385a-8d2e-6e7131fa9d75 | -7.822 | -46.4887 | 2025-10-27 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3075f01d-8146-3938-b88c-38d15e502fa8 | -7.8411 | -46.4646 | 2025-10-27 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| a7644b5e-f187-3e5c-b495-cfe76d4f03ea | -10.8401 | -56.959 | 2025-10-27 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4601f612-622b-38df-b5a7-129a29fe0efb | -7.8406 | -46.5093 | 2025-10-27 03:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| d90aff70-f09a-30e1-b555-36e8b53f2157 | -10.7484 | -44.1932 | 2025-10-27 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 559a9f80-bfdf-37e3-b667-ea1a19bb483b | -7.8411 | -46.4646 | 2025-10-27 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a714ad78-2e31-37ca-a4f3-169ef5c62224 | -10.8401 | -56.959 | 2025-10-27 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f2bae39d-29c6-3115-90e5-53f1bf84cad7 | -7.8223 | -46.4664 | 2025-10-27 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2758f7a1-794c-3c7f-a927-f9671b3fa99f | -4.4805 | -43.4237 | 2025-10-27 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 1cfbdac6-f49a-391e-ad3e-ae9557c0c802 | -7.8408 | -46.487 | 2025-10-27 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 033d0394-12c3-3d7e-b236-aa80b5f23386 | -7.822 | -46.4887 | 2025-10-27 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a5eb01db-03fb-3247-a220-60871305f33f | -4.4618 | -43.4248 | 2025-10-27 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| cc4be65a-5231-3512-b4c5-3d10bfaba6ba | -4.45061 | -43.44001 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README14.md)
