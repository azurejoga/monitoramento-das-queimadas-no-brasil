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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83f0f407-4f71-3a50-92a3-96369a6035ad | -6.98888 | -44.00193 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d85cbce-be1a-3e41-96b0-242b54865615 | -9.01812 | -43.97729 | 2025-10-28 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be28c69c-68ed-34cb-84f0-eab3fe570853 | -10.87177 | -44.41351 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41b4a170-0607-3a1e-b146-b2eb27c2761a | -11.23283 | -46.10746 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a002305e-fd17-32aa-9d07-68881794d6ff | -7.97343 | -45.53208 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cd680a8-6afd-3999-90a7-33493322fd89 | -7.96791 | -45.4569 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb9caa47-6209-37a3-982c-2fd12f43c5e6 | -9.4652 | -46.86958 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b64f5d12-92df-38c0-aee9-b1b2568e5dcc | -9.06938 | -45.10356 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c348bfa9-8d9a-378c-a6bd-082660b8ed86 | -11.02911 | -47.80223 | 2025-10-28 04:14:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1717eea8-99e8-323b-b8e0-79df524e28b8 | -10.5666 | -49.80072 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae2a6951-d88e-3b6e-ac90-b1a9d7ed7db7 | -8.19601 | -44.43743 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96b92d2e-ed72-38bb-9b53-0dce1b1875af | -7.97311 | -46.29765 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dfb96c4-bcfe-38de-94b0-6aa1a9a3e454 | -11.1055 | -44.03209 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 815ee31d-6501-356a-abb3-daec439867ea | -8.07957 | -45.95655 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4993ebc7-4b4e-3396-a144-118e8b26ad45 | -8.64125 | -47.7233 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be0ca964-7240-3e9e-abba-726eb90b6cf5 | -12.38358 | -45.8178 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0269cc21-ae34-3e16-88a6-fb51bf17a905 | -7.86269 | -46.39761 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 648b0c5a-b78f-3fbf-a54a-801e15a76d0a | -8.00022 | -46.19747 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a884b2e4-44c9-3c3f-babe-3230c333d35d | -12.53555 | -47.56318 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8aca0be-9933-3668-8515-f9dd9e5a8005 | -7.67782 | -47.41811 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e240afc-f3d2-3503-88ab-0669acc34e54 | -10.09475 | -45.34067 | 2025-10-28 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1607ea32-377e-337e-9b0d-ba4fe42b46a8 | -12.89988 | -43.35601 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39c8a085-1fb6-3fcc-9ef0-c3af39bf6bf3 | -7.81828 | -46.467 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 444cbd19-c2d4-317a-aa99-2f15680218cd | -9.99642 | -48.10438 | 2025-10-28 04:14:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e06bdb69-8e4d-3129-a29a-c9778d477a68 | -12.20405 | -46.50697 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29c22097-5d7a-3b56-bd48-9dfe479facd4 | -8.14685 | -47.02715 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bc5002d-1314-3d0c-8974-3cb9eaf43144 | -10.36294 | -47.16642 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 298a634b-6045-3902-87cd-0f767ddae300 | -7.62021 | -46.69258 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89a1a4cd-0ffa-33fb-83ba-8b3ad4ded229 | -7.00186 | -46.98874 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6d3e7a4-fc7c-3a24-95d1-e812c6ea6bd0 | -8.69909 | -50.80442 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a954ad78-9f5b-35d7-8c01-e0ad21936b84 | -9.87733 | -47.45893 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edf02f39-bdf0-3a5f-a14e-2ed6ad00d29f | -7.53319 | -46.76415 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efca3fce-62fb-3182-824b-fbc3acfd8df6 | -6.28371 | -44.71785 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2597b221-e4d2-37f5-8ff3-978c5a9e2c90 | -10.23605 | -52.14784 | 2025-10-28 04:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd001be6-2502-3ec2-bb3a-0dce32fed326 | -6.98873 | -39.12414 | 2025-10-28 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 31fcb9cd-27c0-3358-aeef-486fa7f344cf | -11.03209 | -47.80714 | 2025-10-28 04:14:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0809c98-6b89-326a-8f8e-474fcdb6e0ce | -7.16053 | -41.19878 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2d81882-fd84-3c28-9c09-bff7fadab115 | -12.92143 | -43.48051 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b94c066d-64b9-3cfe-8427-195151d5fde4 | -7.85331 | -46.38738 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4067a3c9-bf26-327c-8cff-71a569ade3bd | -7.36879 | -42.44572 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4958c22b-c12a-39fc-9d0e-cb2b1eb212a0 | -9.3371 | -47.84298 | 2025-10-28 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4799a863-4a0b-3b1b-bc20-3bfeeea08ecc | -7.96801 | -46.74587 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf43f8a8-494f-3608-8402-00e88cd3a4c5 | -10.23551 | -52.1507 | 2025-10-28 04:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e6f51ee-4ef6-331e-b128-e9be34313f7c | -7.33509 | -42.44405 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 71b36c6c-a6ec-3ee1-a0e1-07fc6f42a7d7 | -7.95361 | -45.50166 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92a3b9ed-3678-39f8-9029-8a025df722f0 | -6.10455 | -44.67788 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3d90ead-dbdb-32cb-8682-dd9a22de57c1 | -12.08208 | -46.39571 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1bfb22a-579f-3de4-b385-0c8127e5c12b | -5.6075 | -47.10349 | 2025-10-28 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71afa79e-590c-31ea-a8d5-f2a7e86d7298 | -8.32105 | -46.16553 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d0a5d9e-d0d7-3627-b7cd-2bccf3fabe77 | -12.2187 | -46.52526 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4716353-7db6-30d1-824c-b714a221e827 | -8.50863 | -44.03422 | 2025-10-28 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a986a934-db0f-3e9f-831b-8ab00e1ce51e | -7.51053 | -46.28395 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 732662b4-28d1-3291-9a48-51b9396a8158 | -10.29591 | -47.182 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d6ec97c-a90c-34a4-8e88-dd556e4fb840 | -7.48034 | -42.95441 | 2025-10-28 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2cb6b4c-8a69-3e9c-bf9e-ed4f89f13385 | -6.55898 | -41.60763 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 170eddae-8dd2-3378-bc92-26cbef55f06d | -6.51802 | -43.94424 | 2025-10-28 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 776fcad2-b256-3be2-be6a-02ed0c9a2eab | -9.97332 | -47.17962 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17026dc8-468e-3b64-b14c-85c3f6bcdfaa | -7.42538 | -41.87941 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0413116-7f7d-39e1-9912-2a91d2b8b88a | -12.47143 | -44.49805 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 015aea47-13f0-3f4b-8908-0e429c13cdd5 | -7.95299 | -45.50548 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| abf6697c-219f-3096-b389-4f7a73b4e93f | -7.83855 | -46.41042 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aee93bfa-f157-3105-b659-64abb0cd7f7b | -5.61102 | -46.53627 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e8961d8-4147-3619-9381-e99861c78467 | -9.7558 | -49.55939 | 2025-10-28 04:14:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41387820-c78f-330b-aefa-d966c7de261c | -9.25479 | -45.60518 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dfcc498-c11d-3c5c-85c9-9aee212745a3 | -6.68715 | -42.03841 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9edc7759-28f0-3c04-b599-f817f88cc30d | -8.29469 | -42.30913 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a54ff909-3679-3843-a60f-6d3c5b071aa2 | -7.93038 | -49.73468 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d949f041-a9b1-3c68-8c54-8e61e728e279 | -7.80834 | -46.48265 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| cbf311e8-76e1-3478-8bd3-4661e5bca13b | -7.60974 | -46.47873 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8993921e-69f8-3b67-ab95-beaaeb9641d8 | -6.62142 | -44.62548 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c39a5407-f3f5-34f4-8022-5a09ee087b89 | -6.44329 | -42.36132 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8311652f-c492-39df-9caa-15fc450865e7 | -5.49185 | -47.75139 | 2025-10-28 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80c74b55-82e2-3405-96fc-8471944cea87 | -7.94673 | -45.50057 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 073c0d78-daee-377e-8dfe-fbd5d7621e0a | -8.89322 | -49.79545 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7d363b1-e4fb-334d-91d4-c649758ca42b | -6.13252 | -42.69471 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e36e7da3-9fc1-30c9-80d2-b7a6cce10b2f | -7.36044 | -47.63939 | 2025-10-28 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1317e7ea-e98e-300b-a554-97427dc5dceb | -7.94865 | -48.02338 | 2025-10-28 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0aebf84-5dce-3a90-b4a5-46c1d35b1e3c | -10.68649 | -44.3579 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c9d45b0-ed68-3db2-9a1f-0e499acb1ba9 | -10.02171 | -47.13504 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c091b746-db15-364c-ae7d-f07ae7f0769d | -7.80971 | -46.47428 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 07195852-635c-3bc4-a5e9-704b5bb79796 | -13.44868 | -44.09771 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a38fa027-2b48-3ca8-b555-80ea2a1b156e | -9.26426 | -45.56829 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a73df5c6-a867-3544-b90c-f21611f70ccb | -5.56625 | -51.01612 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 728daacd-0971-3f12-a74b-5cbfb7ec1abe | -12.62555 | -45.07277 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a84191d-93d7-34db-aa85-2d895df7c216 | -10.43914 | -47.24485 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf787750-614f-3f5d-8db7-0bc5b10367e6 | -5.71892 | -47.47632 | 2025-10-28 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9a39c6e-c622-36c8-b83b-a38d4f2c0020 | -5.25122 | -50.45195 | 2025-10-28 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f18fa517-6213-3d14-a082-757c36bb9c44 | -8.57704 | -47.15149 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4d4a703-6fcf-385f-9ece-ed44dc2ff2fa | -7.9439 | -45.49622 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7e7fdcf-0720-3742-a699-2bd37005e29c | -7.27028 | -44.96809 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d13d8919-8d07-33cc-bdd3-d20dea0583ba | -7.95805 | -45.51791 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7a20e80-783d-3394-ab01-9277639a12f1 | -6.47747 | -46.72566 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5f059d5-b160-396c-ba07-de08c5143f8a | -6.16815 | -46.095 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e2faccd-e4a8-3272-a856-a7bbca6ca5a9 | -9.46377 | -46.87814 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2f003d21-4df5-3d4b-bdc0-90e083be6a2a | -12.05996 | -47.82103 | 2025-10-28 04:14:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10807517-79ea-3b1f-b4c0-195fbc25aebf | -7.6147 | -46.47096 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c2634d89-1e33-36aa-9442-88d3b74437b1 | -10.64578 | -48.01573 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5368b073-6333-3077-a16b-7c33af081d72 | -9.04933 | -46.92921 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34962521-ef85-386c-a0c4-64c9617e0d2e | -7.37512 | -45.0148 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb75a39e-6df9-3a5c-a429-e994f61e6694 | -11.0392 | -47.85493 | 2025-10-28 04:14:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README29.md)
