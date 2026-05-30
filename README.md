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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1243c23-b966-3e4f-bc77-23102a3a0160 | -11.591 | -47.4496 | 2026-05-30 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5e22784f-bd4e-3299-b715-1eb35747a6dc | -10.7808 | -46.9281 | 2026-05-30 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 36446346-8526-3eb5-90b3-16a950b49e5b | -10.7801 | -46.9729 | 2026-05-30 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 6a864bfb-ea26-3fab-8de4-284e2c873e9a | -11.591 | -47.4496 | 2026-05-30 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 849136e7-8791-3654-a393-b9e0bf82b9a6 | -10.7614 | -46.9529 | 2026-05-30 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 56fb4886-0e4e-3d47-bb9b-45fdcf2ca27e | -10.7804 | -46.9505 | 2026-05-30 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 0199d8a9-80bf-3704-aeaa-cefa359399f6 | -10.7801 | -46.9729 | 2026-05-30 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c49de6a8-ceea-3f5b-a1d8-0da7a235a4d5 | -10.7614 | -46.9529 | 2026-05-30 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 53d092c7-f2aa-3918-8b1c-860fe87b5534 | -10.7804 | -46.9505 | 2026-05-30 00:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 5a173cf2-055a-3229-824b-e7c3821af8ef | -10.761 | -46.9753 | 2026-05-30 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 00f18f97-00b9-3eaf-be27-278c877ad0aa | -10.7614 | -46.9529 | 2026-05-30 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6f810cfb-d8d3-3a04-8d04-41c0155b94fc | -10.7801 | -46.9729 | 2026-05-30 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f5d8e4d5-78ab-3c41-8769-243740ffc4de | -10.7804 | -46.9505 | 2026-05-30 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 4588c340-4031-3229-a895-e00cd4d91bc1 | -20.5733 | -48.9305 | 2026-05-30 00:30:00 | GOES-19 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| ac2e35cd-6546-3685-a664-0c49a931415c | -10.799 | -46.9053 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58a9baba-fc37-3bb9-b950-bb2da3e0d2f2 | -10.8315 | -46.911201 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39445c45-b3cb-36fb-8ac1-d915cd599da7 | -7.3406 | -49.848499 | 2026-05-30 00:31:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5afaf36-f9fe-3586-bd61-9cb9b1aa3038 | -11.5827 | -47.4436 | 2026-05-30 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c952d28-2ac1-3794-84af-09aaefa6e4c0 | -20.9501 | -49.144798 | 2026-05-30 00:31:00 | METOP-B | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4b44c8a-d671-3e04-92f3-3c12dd5f2dcc | -9.9305 | -48.6777 | 2026-05-30 00:31:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f50e236-6cf2-36ca-99f7-3882a4dd5093 | -10.8348 | -46.9245 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43bebdd5-0ec9-340e-9b6e-99da22780b7b | -11.0709 | -55.032001 | 2026-05-30 00:31:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cd57061-f106-39b2-9287-365db88a76a5 | -11.0669 | -54.498402 | 2026-05-30 00:31:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4ba04c8-7694-3192-8bb6-28365242a744 | -8.7252 | -47.8339 | 2026-05-30 00:31:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1270978-3280-3b75-910b-b927da35653a | -8.7222 | -47.821499 | 2026-05-30 00:31:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 721bda94-2f3c-30e2-9d08-b8fbc1cd4933 | -18.4664 | -54.692799 | 2026-05-30 00:31:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f9c177b6-5679-3efb-80a6-bea824215e39 | -10.7667 | -46.941799 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 593c4c43-0ae6-32ff-83d1-497d0e6ffef7 | -6.2713 | -48.558701 | 2026-05-30 00:31:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f37b545-9fe9-3c31-9766-3eb3d37827f0 | -9.8915 | -52.429298 | 2026-05-30 00:31:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd160ce6-de75-351d-9e0a-3ac200276e98 | -11.6254 | -55.171001 | 2026-05-30 00:31:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1daf2a09-37d5-31d0-a08b-fd752678f2cd | -7.3308 | -49.8508 | 2026-05-30 00:31:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba3da731-dfa9-35c3-8558-794ba07ba1d7 | -7.3383 | -49.838699 | 2026-05-30 00:31:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2331dbfa-901c-3aa7-bf91-3a1e5ef5435b | -10.6299 | -48.323502 | 2026-05-30 00:31:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5e1bd4b-9fa1-3901-9e71-4d2e66e1674e | -10.8023 | -46.918598 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22973f65-87fb-37a0-82ca-2ac8d8ced4db | -11.5797 | -47.431702 | 2026-05-30 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3afd2a0-b1f4-3205-8eb8-bd0b47241a7a | -6.2684 | -48.546501 | 2026-05-30 00:31:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b944f60-a9cb-3b50-acb3-3975848feba2 | -20.568701 | -48.925598 | 2026-05-30 00:31:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad02a8a6-dd14-316b-a187-2253e287d66c | -10.757 | -46.944302 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d5654c9-ae82-3f44-b4c0-272e61991e07 | -19.724701 | -54.646099 | 2026-05-30 00:31:00 | METOP-B | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3d62a3aa-a183-3790-b079-13f1d94584c3 | -9.8931 | -52.436501 | 2026-05-30 00:31:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 920e307b-c45a-325b-b09c-d6bcd6393b51 | -10.8412 | -46.908798 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8796fc84-60cd-361f-96cc-27a77849e311 | -18.4681 | -54.701199 | 2026-05-30 00:31:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 171da939-ef06-3321-9bb2-59d9623831a3 | -12.0007 | -47.757 | 2026-05-30 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c63a57d-9ae7-3dea-9164-c5f45ab9300a | -11.627 | -55.178398 | 2026-05-30 00:31:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20fe9d0f-9852-3c84-b994-e3df1f6414a6 | -10.6273 | -48.312599 | 2026-05-30 00:31:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88fe3aaa-7896-3c29-8fd7-62b40d896779 | -10.7603 | -46.9575 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 835f2f7c-d5a6-3f40-83b3-34e00f40f7c4 | -11.5856 | -47.455601 | 2026-05-30 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a202769a-e2c4-3776-bccd-9b611a6e1412 | -11.0725 | -55.039299 | 2026-05-30 00:31:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7b706d0-ef8e-36d0-9cb5-cd9a213e6a42 | -9.9208 | -48.680099 | 2026-05-30 00:31:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f845d406-d615-3bca-9451-c670d8e3cca7 | -5.798 | -45.125198 | 2026-05-30 00:31:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74ca4020-3293-3a0d-ac4d-1f24a9ee8cb5 | -10.7636 | -46.970798 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d063d4c-4c63-3873-8d4b-92c93f0fc7a9 | -10.7733 | -46.9683 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d98da60-a9bf-30d2-baf6-b5eb55da17dd | -7.5035 | -55.000801 | 2026-05-30 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f03e73a-e715-33c0-bb4a-1d6a906f0838 | -11.5925 | -47.441101 | 2026-05-30 00:31:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7373bae1-2023-3546-893f-e0eb01c15530 | -10.77 | -46.955002 | 2026-05-30 00:31:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46fef887-3e12-3b34-ac15-49a22d8b305b | -11.5895 | -47.429199 | 2026-05-30 00:31:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb75d756-ce68-39d4-bbf4-ed652b3d5f9a | -11.9211 | -54.8322 | 2026-05-30 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ac5b11de-c7d5-3fa1-8fb4-9283f5093812 | -11.9022 | -54.834 | 2026-05-30 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 175.7 |
| c6024cc7-dff5-3d86-b17f-cdf07775d127 | -10.7804 | -46.9505 | 2026-05-30 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| fdd49503-d0dd-37d1-8eee-98653a006256 | -11.9024 | -54.8135 | 2026-05-30 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 61e81c36-953d-3f35-88fd-d1b0f52cd5b3 | -10.7801 | -46.9729 | 2026-05-30 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 416ef12b-3da2-39ef-b6e0-31505cbe5445 | -10.8379 | -46.921 | 2026-05-30 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 16fea5a7-43e3-3c1e-ab7c-0cfcdf9110a4 | -10.8375 | -46.9434 | 2026-05-30 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4a70a635-6638-39e9-8a1c-6a4061d038fb | -10.8379 | -46.921 | 2026-05-30 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| e11458b3-df55-3fcd-8e1b-be29dfb17314 | -10.761 | -46.9753 | 2026-05-30 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 09ca0e0e-99c5-3bb1-beec-ca2800c8e0e7 | -10.7801 | -46.9729 | 2026-05-30 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 5e030fd0-7856-3455-b664-d68cc24bf2d1 | -10.761 | -46.9753 | 2026-05-30 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 5d563cf7-7d8f-33d1-bc9e-00b03f5d8c9f | -10.8379 | -46.921 | 2026-05-30 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 3cc209b6-94dc-3509-b091-d834eb2c1267 | -9.4769 | -40.3365 | 2026-05-30 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 483dcac1-6324-35d4-b0c9-ad69dd4243f7 | -10.8375 | -46.9434 | 2026-05-30 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 040a853a-4643-3a1b-bfc5-c8a5cc0dd39d | -9.4956 | -40.3586 | 2026-05-30 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 6c83418f-7634-3b81-887e-54d67dbe7f7a | -9.496 | -40.3337 | 2026-05-30 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 155.4 |
| 7e726464-2cc0-3fe3-9224-2c40e77fd052 | -10.7804 | -46.9505 | 2026-05-30 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| fb9aa460-b9ae-3971-bea1-5df925e5f15b | -10.761 | -46.9753 | 2026-05-30 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 80cc4902-b0ff-3b04-a7eb-f95152a9a52e | -10.7801 | -46.9729 | 2026-05-30 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f153758f-79ea-3d04-baa0-230fb1475490 | -9.4769 | -40.3365 | 2026-05-30 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.9 |
| b19ad0ac-df69-37d9-b037-3f58cfc5f951 | -9.496 | -40.3337 | 2026-05-30 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 787352bb-b989-3e19-87f9-b13025ef7f35 | -9.4956 | -40.3586 | 2026-05-30 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.9 |
| d00bc877-34a9-3c51-8a8a-c49f2bd77631 | -9.4956 | -40.3586 | 2026-05-30 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.7 |
| afa3e1b3-1cbe-3458-aeab-518d3e76390a | -10.8375 | -46.9434 | 2026-05-30 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 12afd4e1-62d1-30bc-988e-c7ee6b733f85 | -10.761 | -46.9753 | 2026-05-30 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 17fda300-7d58-3413-a158-d3ecbba5efa9 | -9.496 | -40.3337 | 2026-05-30 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 59bd2598-aefe-34e4-a094-f6658c79cb53 | -11.9022 | -54.834 | 2026-05-30 01:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e49c96d4-a580-3bdb-a0b4-1282906ecba9 | -10.8379 | -46.921 | 2026-05-30 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| d7c3b2ad-0f45-3e12-ad81-4e9fad988d2c | -9.3455 | -40.2062 | 2026-05-30 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 45f9c417-61e2-35b1-bdea-843740081e00 | -10.8379 | -46.921 | 2026-05-30 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 8b664de0-ffac-331c-a161-15967ac5bd61 | -10.761 | -46.9753 | 2026-05-30 01:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 2637386e-4c35-390a-8757-0870ef0fa22d | -10.7801 | -46.9729 | 2026-05-30 01:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 439dd922-b636-33f3-b51c-9100a50d75c3 | -10.8375 | -46.9434 | 2026-05-30 01:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6de07b4e-299f-3d9a-b4db-d562fc16f179 | -10.8379 | -46.921 | 2026-05-30 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6f4e38ca-cae2-3b17-b93e-8ba08d02fc33 | -10.761 | -46.9753 | 2026-05-30 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 5ae3a150-c17d-33cf-8b7d-71567e0ce3ee | -10.7614 | -46.9529 | 2026-05-30 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7189672a-fee2-3e6f-8b78-1f796d902587 | -10.7804 | -46.9505 | 2026-05-30 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| eb02bd7a-f46f-3f7d-868c-123d71816c43 | -10.7804 | -46.9505 | 2026-05-30 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2867e769-b466-358a-a7b5-54b3aa145abb | -10.761 | -46.9753 | 2026-05-30 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 896d8d19-cad1-3297-9b93-c9bd1bc847d5 | -10.7614 | -46.9529 | 2026-05-30 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 6f36e14d-3718-3494-a4f1-9083dfedb6d5 | -10.7617 | -46.9305 | 2026-05-30 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 99060359-98a8-34ac-bff8-ae276adcff03 | -10.761 | -46.9753 | 2026-05-30 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 10a39038-8e85-3da4-8459-585ca1a702ca | -10.7804 | -46.9505 | 2026-05-30 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 6ba93afa-d2c8-34fb-b097-136ad9140aeb | -10.7614 | -46.9529 | 2026-05-30 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |


[Clique aqui para ver as próximas entradas](README2.md)
