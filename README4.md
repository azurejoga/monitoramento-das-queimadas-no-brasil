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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2afe0c28-6c0d-3a45-baea-b8143e8009ce | -16.2562 | -50.9275 | 2025-10-01 00:50:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 42b921e5-8953-3fcf-9a0c-6691df247880 | -13.1777 | -50.9335 | 2025-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3c139204-5fc8-3a40-9569-b496ab61c794 | -10.7291 | -45.3738 | 2025-10-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 221ce7ac-d70f-33c2-b989-dbb7fac204c9 | -8.5081 | -47.2676 | 2025-10-01 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 80e52022-f981-3f75-97bf-95b3b4a557ed | -3.4577 | -50.089 | 2025-10-01 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| e8ec0582-6d7c-3753-a1c4-1db0da0f740e | -15.9234 | -48.1279 | 2025-10-01 00:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8c65e5bb-64a4-37d6-9b7a-333ba8d881f2 | -15.1806 | -49.1011 | 2025-10-01 00:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 0395b0c7-7685-3144-a7a3-ec0ba2f7870c | -21.0365 | -45.6693 | 2025-10-01 00:50:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f38e49dd-4c35-3384-ae4d-e54d0ad06977 | -11.8438 | -44.964 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| e8c7c0c5-d331-3452-89b3-69296bc6a5d0 | -13.3274 | -47.8536 | 2025-10-01 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2fce9400-4f66-3b03-88ec-4409fecd5172 | -11.3858 | -44.8923 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 88f43556-b56b-3f57-81f5-a981bad93a09 | -11.8242 | -44.9901 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 07f3da84-0bbc-33ae-9d34-f1b19e7fdd63 | -13.9818 | -45.0581 | 2025-10-01 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 630f2bdd-25af-3675-bb13-70cf3e9c3384 | -14.9914 | -46.9549 | 2025-10-01 00:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c4bd7847-d835-38b4-b621-0bcef354d07a | -15.9426 | -48.1471 | 2025-10-01 00:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 079b7f04-43a8-3d4c-8af4-e45a543e0a49 | -8.5079 | -47.2897 | 2025-10-01 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 9926392e-0d65-31ce-b348-604843d6e560 | -11.8434 | -44.9872 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 277.3 |
| c502cbea-1c81-34b2-8c5a-a54a5d5a0e60 | -9.3089 | -54.5229 | 2025-10-01 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ca606cb6-8c6c-347f-a655-6b23633c02fe | -5.8657 | -43.3981 | 2025-10-01 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3ee9d639-8acf-3f31-8d6f-8b1fc1311e25 | -10.7478 | -45.3942 | 2025-10-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 35bbc899-394e-3eb8-b570-c9b347156989 | -11.805 | -44.9929 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8bcd0981-6188-3d81-bc58-fddf31946ca0 | -12.8198 | -50.571 | 2025-10-01 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 317.8 |
| 38a33925-a141-341c-91ba-7c7fa7e7f0b8 | -20.6309 | -46.2046 | 2025-10-01 00:50:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8d06d3bf-7a36-3807-a80d-2a2f32d96ee8 | -13.1969 | -50.931 | 2025-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| edd901a0-0ced-39f3-893d-a9e53033e44f | -3.5161 | -49.4528 | 2025-10-01 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d8908458-bc83-399f-9aff-f0809d4eaa1d | -12.839 | -50.5686 | 2025-10-01 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 796ced72-d162-39a2-aa06-1ab8c3a89d40 | -11.8054 | -44.9697 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1b362fc1-2355-3307-ac9b-27bd289fb02b | -15.011 | -46.9515 | 2025-10-01 00:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| a75b9a18-b587-38e9-8b16-440f760e0f24 | -15.9431 | -48.1245 | 2025-10-01 00:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 208ac235-82e3-3c40-b217-79d646e1b7f8 | -5.6361 | -43.9258 | 2025-10-01 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| ce68dfba-b9ee-3e53-a8bf-7c798c191225 | -13.3471 | -47.8284 | 2025-10-01 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4d395acc-ed7d-312a-8dd7-bad656c253d8 | -13.1774 | -50.9549 | 2025-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 657cc419-f8f1-3b09-b8d1-2b5f7f00af78 | -13.6756 | -46.7878 | 2025-10-01 00:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d4303cb8-bc32-3ac1-a444-31cbdb591ed6 | -9.0821 | -48.0252 | 2025-10-01 00:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 52658a83-8286-3aca-8b83-5ab5b4686f48 | -11.1523 | -54.3104 | 2025-10-01 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f3d8414d-840e-35a2-8714-f564085abcba | -10.9773 | -46.5217 | 2025-10-01 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d5d17580-ae9e-300d-81c2-aab59686f45b | -8.559 | -44.7184 | 2025-10-01 00:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 46083d89-9c7f-3446-8ec7-0f177bf82d24 | -11.4049 | -44.8895 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d5820c3e-b2e4-30f6-8939-859634f1965a | -11.8246 | -44.9669 | 2025-10-01 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 282.7 |
| 6d491d6f-4f79-3016-bea7-5e250ef84015 | -12.8394 | -50.5471 | 2025-10-01 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 162.6 |
| c530dd1f-99dc-322b-aa75-33811e8baa11 | -9.2902 | -54.5242 | 2025-10-01 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7a7b3193-10fd-39d9-92e3-c53e06f9183d | -21.0572 | -45.6638 | 2025-10-01 00:50:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 77390690-091a-3cfb-852c-98fabe3e6db0 | -10.7482 | -45.3713 | 2025-10-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| baf872d7-0c84-321d-a919-1c27b8c11017 | -22.5946 | -46.7698 | 2025-10-01 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| c3333ba0-d038-3c9b-8f9b-f9b9ebc3c8ca | -9.9189 | -43.6743 | 2025-10-01 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 2fe2858c-1df9-3efb-a89c-7dc74f744e6b | -9.0821 | -48.0252 | 2025-10-01 01:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 0bb4abd2-28b4-3099-ae85-e15cb6f2c509 | -15.9426 | -48.1471 | 2025-10-01 01:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 31.0 |
| f63a4929-001c-37a1-a03f-99798fc13378 | -14.3524 | -45.8974 | 2025-10-01 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6de6ad33-a18c-3f04-ab76-9ceaf249cacb | -9.4396 | -54.5537 | 2025-10-01 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 7312f937-70aa-34cd-9a8a-8f845aebc764 | -8.5081 | -47.2676 | 2025-10-01 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 8b593daa-8733-370f-b34c-93fd8c54e3d4 | -17.4049 | -47.1431 | 2025-10-01 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 81722ce0-d967-3adc-b454-5bbe8c8554e9 | -11.1523 | -54.3104 | 2025-10-01 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b8784f06-31f9-3dcc-beff-9e62f4df5e54 | -5.6548 | -43.9244 | 2025-10-01 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 623bbf29-f60c-3f3c-9851-ee257dadbc42 | -16.2562 | -50.9275 | 2025-10-01 01:00:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 144.0 |
| c5f10d4a-a29d-3d89-9e88-a2ad43017fb5 | -10.8429 | -45.4044 | 2025-10-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 445fd56f-7c22-3c7c-8d4f-a5ae58fce135 | -16.2366 | -50.9306 | 2025-10-01 01:00:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 846e2595-ccec-37e2-9d2e-b385cf798d6d | -13.3467 | -47.8508 | 2025-10-01 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 44cfbdc8-4af2-3ae1-8b43-c338d78620db | -20.5998 | -45.878 | 2025-10-01 01:00:00 | GOES-19 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 11f22530-dab6-373c-95c0-dd02f075220c | -9.2902 | -54.5242 | 2025-10-01 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 193f932f-5dfe-302f-af4e-23ed0331340d | -3.0827 | -47.0088 | 2025-10-01 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 327c2822-bd45-38fc-80f8-9e0277c948ad | -3.4762 | -50.0883 | 2025-10-01 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 907a118e-07da-3838-8477-eb296cf259fb | -21.0572 | -45.6638 | 2025-10-01 01:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5728c833-75ef-38bf-ade6-e76fb4c2ac8d | -3.1013 | -47.0082 | 2025-10-01 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| ba824c48-280e-3608-9b1a-4215918c4e4d | -13.1966 | -50.9525 | 2025-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 424.3 |
| 509fb670-de7f-3054-a2ab-5cd65791c3b8 | -9.4394 | -54.5739 | 2025-10-01 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| bf4a35d7-fdcc-3db3-9cc7-e0fc57ebe65b | -3.1012 | -47.0301 | 2025-10-01 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 4451a427-88dc-3ba3-a3f2-a16057c4b8b0 | -9.9383 | -43.6483 | 2025-10-01 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 262.0 |
| fa1f30a7-80cb-3a52-9103-3489dc0be6bd | -13.1777 | -50.9335 | 2025-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 274.2 |
| a644acbe-4b6e-37a7-a119-8ac8c2d1f89b | -10.7482 | -45.3713 | 2025-10-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 739837e4-80da-3d62-913e-c69228d829c1 | -13.3471 | -47.8284 | 2025-10-01 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 238f8987-077b-3e6f-a335-de7451ed4fad | -14.3519 | -45.9206 | 2025-10-01 01:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4f75e343-26a4-348a-93e0-08f2c39c914f | -10.7291 | -45.3738 | 2025-10-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 6c2ef47a-64af-3a15-b9c7-cb8e5238152a | -18.71 | -49.1621 | 2025-10-01 01:00:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d5c30260-09b6-3345-ac52-f5532247b284 | -21.0365 | -45.6693 | 2025-10-01 01:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 65bfc6f1-9527-39cd-a070-c7d4a0d7380e | -15.1806 | -49.1011 | 2025-10-01 01:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9fc3b81b-beb8-3f6c-bc70-8c9796462ed3 | -8.5079 | -47.2897 | 2025-10-01 01:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 0c2710c5-4979-3b3e-a2d1-abf481406f48 | -18.7301 | -49.1581 | 2025-10-01 01:00:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c8d9bfa6-daee-399d-9676-d715bf8af163 | -11.3858 | -44.8923 | 2025-10-01 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| aaee4270-91d1-392c-9e2d-1b3429eeda34 | -12.8202 | -50.5495 | 2025-10-01 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 459.5 |
| 99032893-2f0f-36d3-8de6-7da4634cd3b9 | -17.4043 | -47.1662 | 2025-10-01 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 0b02709e-dd9d-313c-97e5-60cf8ae41be6 | -10.9204 | -46.5065 | 2025-10-01 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 65671b0c-ce33-3b07-b7a1-580661c367ba | -9.3089 | -54.5229 | 2025-10-01 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 06d0ca19-4d6b-377d-9763-a0301ab9e6cc | -12.8394 | -50.5471 | 2025-10-01 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 400.1 |
| ac9d8111-0031-3561-9239-89bb791a6bd8 | -12.8198 | -50.571 | 2025-10-01 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 362.1 |
| e74ddad1-e1e4-35fb-9977-f27cc7b2dc53 | -9.938 | -43.6718 | 2025-10-01 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 84fdfdf7-e3ca-3905-80e9-4562e77801a3 | -15.9234 | -48.1279 | 2025-10-01 01:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 35.2 |
| bc0b725c-0dbe-3596-81d2-2b59e25f56ad | -14.9914 | -46.9549 | 2025-10-01 01:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 19fd5924-ff86-3d97-bf93-4d64af031790 | -13.1774 | -50.9549 | 2025-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 377.5 |
| 1edcf513-a1bc-34ca-98eb-c81d055de198 | -13.3274 | -47.8536 | 2025-10-01 01:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 268dcf14-3d90-353d-b691-ee5c924a5382 | -15.9431 | -48.1245 | 2025-10-01 01:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 78621e6c-6b69-3f24-a7ca-61e010aaf638 | -13.1969 | -50.931 | 2025-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 307.6 |
| c89c6a6b-7c3d-3906-9830-617f585ed512 | -12.8756 | -45.2671 | 2025-10-01 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 962de3b9-cb57-301e-8029-24d82a6a802f | -5.6361 | -43.9258 | 2025-10-01 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| bd5ba985-4859-39ff-a81f-57ef76c4fb69 | -12.839 | -50.5686 | 2025-10-01 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 401.4 |
| 77e198f9-4909-32b4-b7e9-af9d1039b551 | -9.9574 | -43.6458 | 2025-10-01 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| dec2b57f-4305-3481-8d7c-2e96d418a9b7 | -9.9186 | -43.6978 | 2025-10-01 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 5f275457-d9b8-30e2-85a8-23ac8e4c277b | -20.6103 | -46.2098 | 2025-10-01 01:00:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c39baa15-a44b-3a97-9ec6-fc7bb27b6b17 | -10.9773 | -46.5217 | 2025-10-01 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 9573d32a-362d-3422-bc41-3873d00393b3 | -20.6309 | -46.2046 | 2025-10-01 01:00:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 18839568-8b0c-38ab-8167-38d080280b04 | -3.4577 | -50.089 | 2025-10-01 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |


[Clique aqui para ver as próximas entradas](README5.md)
