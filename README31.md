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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f60267cd-9aaa-3ff3-a8b2-ad9757379e2a | -7.0615 | -59.1779 | 2025-08-11 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9f5038ef-a6a7-3a97-ab40-010c100c952e | -9.0142 | -47.4384 | 2025-08-11 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e791ef31-ba8c-3890-a4b5-48376172e639 | -14.1108 | -45.3844 | 2025-08-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| bbaa2770-9b7f-32ef-b3a8-628c7dba2fbf | -9.864 | -43.5407 | 2025-08-11 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 8de3186c-872d-3b49-a007-d5174a9d5ea8 | -12.6094 | -47.1754 | 2025-08-11 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f18f0561-5da5-3634-a949-084bed5fa241 | -8.995 | -47.4624 | 2025-08-11 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e1af2309-ffa6-3fb3-b460-4cb77602f6ef | -8.5604 | -54.6973 | 2025-08-11 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e553d942-1f6d-3170-a8e9-c474fadf2f4a | -7.3012 | -39.6453 | 2025-08-11 13:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 136.6 |
| da43f837-641b-3c5e-a1d1-3c1b3edec4ab | -3.9961 | -43.2418 | 2025-08-11 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 0660d231-993a-31a4-bd4f-b0227e1e7c52 | -8.9953 | -47.4403 | 2025-08-11 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 10a4d2b6-8f05-3429-bc52-8bc916898100 | -8.579 | -54.696 | 2025-08-11 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5f70f175-846c-3709-b310-4a0305132585 | -11.5241 | -50.554 | 2025-08-11 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 91d0c3b5-b3ad-318a-bc15-6588b73bf84a | -10.625 | -44.7439 | 2025-08-11 13:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6ded14c4-9214-301f-b448-fba82c4f6711 | -15.4216 | -53.9073 | 2025-08-11 13:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 74c5762a-9868-3b37-b7d7-52629656d2b6 | -7.0799 | -59.1964 | 2025-08-11 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c4a3af6c-1291-3185-a004-017add029ec1 | -9.0142 | -47.4384 | 2025-08-11 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 74a1ea13-1f24-301d-94c5-a1e84e153a04 | -15.4407 | -53.9258 | 2025-08-11 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a6f71320-0c4a-3f27-859b-9584c1e3c4cb | -3.1676 | -48.8041 | 2025-08-11 14:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 217e151a-8249-33a0-9709-acb99b8bb33b | -7.6113 | -45.2026 | 2025-08-11 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 936d9be9-937b-3c67-9d19-5f4eb18c984d | -7.0614 | -59.1972 | 2025-08-11 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| cc2e8f64-0871-3f6c-aed3-aee30aeff02a | -15.4216 | -53.9073 | 2025-08-11 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 892e2ead-3e53-3530-910c-9a7e2f10a548 | -8.5604 | -54.6973 | 2025-08-11 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b2cacde7-28f0-3980-8ed4-b9fa2fc45ebd | -9.2232 | -44.5283 | 2025-08-11 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 523f3c5e-b71b-368d-996e-81dd84381033 | -7.08 | -59.1771 | 2025-08-11 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 28de9271-0555-3e98-bd82-9200fc5b8f5b | -14.1108 | -45.3844 | 2025-08-11 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 66e6eb7f-f8d1-3bd4-be3c-20fd26f164e0 | -11.7209 | -50.1026 | 2025-08-11 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c7111754-b72a-33ba-a15e-74d65e56eb13 | -9.864 | -43.5407 | 2025-08-11 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 3c4a27a6-f687-3e89-a759-c843a20e7881 | -8.579 | -54.696 | 2025-08-11 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b304234d-4b35-3475-bbb2-af25e3b23dc6 | -11.9224 | -44.8597 | 2025-08-11 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a9223651-9349-3f78-8a2c-352a88c7aba0 | -9.2042 | -44.5305 | 2025-08-11 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 71055f02-48eb-3dd9-ac25-8d8c4746f1bd | -8.9953 | -47.4403 | 2025-08-11 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| edc083ae-a8c4-36aa-b629-d415a26bcc0a | -7.0615 | -59.1779 | 2025-08-11 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| af7e6983-1787-361a-87b6-2b38e6e11ba3 | -7.0799 | -59.1964 | 2025-08-11 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 32416eba-8710-303d-be2d-e8badac4a4b8 | -8.995 | -47.4624 | 2025-08-11 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 8a31dcc0-d876-3474-96df-c43354f66916 | -7.0613 | -59.2165 | 2025-08-11 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ff36ad4a-b6a6-3307-b907-fa956a270ce1 | -9.0142 | -47.4384 | 2025-08-11 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 752946b1-23c7-3694-998c-5bc42646a2d1 | -3.1676 | -48.8041 | 2025-08-11 14:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ecada316-6ae7-307b-9d27-76a99e1c59d5 | -7.0799 | -59.1964 | 2025-08-11 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 27379e18-3e85-3908-9257-b8c9cdbe0958 | -9.2042 | -44.5305 | 2025-08-11 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| ce567ed1-ca16-36fa-a002-753547363ce6 | -7.0615 | -59.1779 | 2025-08-11 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d04b9861-5381-357d-87cb-4e08da29f3f0 | -15.4216 | -53.9073 | 2025-08-11 14:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 57f05822-7b58-3a8e-9393-375ea11fa0ec | -11.9224 | -44.8597 | 2025-08-11 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8fc6abb4-34dc-3299-b026-d9f4820a36bc | -8.5604 | -54.6973 | 2025-08-11 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| ef29c085-8165-3528-bec0-a3c03e01b6ec | -15.4407 | -53.9258 | 2025-08-11 14:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ecfc44b9-b29c-3563-919e-61e75988f503 | -3.9961 | -43.2418 | 2025-08-11 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1ed819ec-7bf9-3d56-b543-2dedf92e2d30 | -9.2232 | -44.5283 | 2025-08-11 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 36ac1058-8445-324f-a5da-046c710eca57 | -7.08 | -59.1771 | 2025-08-11 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 26ac8b2e-3be5-3bc3-9733-367582ec0832 | -8.579 | -54.696 | 2025-08-11 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 37650aa7-2d93-32ef-ba62-45dcca816f94 | -15.441 | -53.9048 | 2025-08-11 14:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ce235842-ae92-3f4d-9782-d8431d36ab78 | -14.1108 | -45.3844 | 2025-08-11 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| f445d843-7d9c-35ef-941f-ff7f8fe04e66 | -8.995 | -47.4624 | 2025-08-11 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| b97b851b-2ece-37d2-a58f-f18992e08567 | -7.0614 | -59.1972 | 2025-08-11 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 6e764b67-87a3-3429-8ab9-3c6eb8babea6 | -3.1861 | -48.8035 | 2025-08-11 14:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 00b950fb-b15e-39b1-81d7-8a3bfe0cdf9c | -8.9953 | -47.4403 | 2025-08-11 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| e76bc074-a3fe-35c7-b765-569e42ddd4b8 | -8.5605 | -54.6771 | 2025-08-11 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0e6d8dbe-b0d4-3b5a-b455-8a9b46b04795 | -8.995 | -47.4624 | 2025-08-11 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 160.7 |
| abf116b5-c117-35f3-8b09-68febfb1d927 | -9.2042 | -44.5305 | 2025-08-11 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 66302ce0-0e85-3ccc-9b52-3471b569d0f9 | -8.579 | -54.696 | 2025-08-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 78576ec1-ddb5-3a85-b94c-5f31f46c0a2b | -7.0615 | -59.1779 | 2025-08-11 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 80bf218e-caf8-366b-a659-d1b63fd51ed8 | -15.441 | -53.9048 | 2025-08-11 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9d6275ac-f9f1-3dfd-a072-707ebb79c4f0 | -14.1212 | -44.8933 | 2025-08-11 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 6eed7708-618b-3e1e-a15a-5d5f11fa9129 | -8.5605 | -54.6771 | 2025-08-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 95d0fbdd-7da0-3ebc-b43c-fc92580297fa | -14.1108 | -45.3844 | 2025-08-11 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4b3e4048-df68-38ff-a1f6-390c6f11ab95 | -7.0614 | -59.1972 | 2025-08-11 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| fdf4b1e6-656f-382c-befb-fd66f7c93f2f | -7.0799 | -59.1964 | 2025-08-11 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 04a92a3c-32ca-39e2-9cb2-f4f174ae1cc1 | -8.9953 | -47.4403 | 2025-08-11 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 964dc067-4cd8-30e8-970a-44e942f3d84a | -14.1217 | -44.8699 | 2025-08-11 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 204.6 |
| b9ec00e9-695f-3e54-9735-f69e27f70f80 | -9.2232 | -44.5283 | 2025-08-11 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a3982a04-050d-3fce-8bd5-54a1511cb790 | -11.7209 | -50.1026 | 2025-08-11 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 32cd636d-4e23-327c-91fe-c17ce89dc116 | -7.08 | -59.1771 | 2025-08-11 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 63eff237-9228-3d9d-adc8-d38d8e4d2b3d | -7.3012 | -39.6453 | 2025-08-11 14:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 5412f60f-c3fc-3a03-b89e-aac8b9a17dc3 | -8.5792 | -54.6758 | 2025-08-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| fd8f6a73-f733-38ca-b6f5-f846bb57a044 | -7.0613 | -59.2165 | 2025-08-11 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 945939c8-98ab-37e5-91ab-59fe2cb3ebc1 | -15.4407 | -53.9258 | 2025-08-11 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f2306773-373f-3884-95dd-b8ef736a361e | -15.4216 | -53.9073 | 2025-08-11 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a47e6177-6456-3a2f-b362-3fe00fee2570 | -8.5604 | -54.6973 | 2025-08-11 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 7e518684-fe98-3329-af71-8507bd7158d0 | -12.6094 | -47.1754 | 2025-08-11 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c371e797-7e56-3c0a-ad55-8436608bf13a | -9.2232 | -44.5283 | 2025-08-11 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a67c85ff-e8b6-34ca-abd0-f66a388e0fa0 | -8.995 | -47.4624 | 2025-08-11 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 546a455b-f472-3617-a68e-1aa07bc1aee9 | -7.08 | -59.1771 | 2025-08-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 61029ede-a773-3720-b0d7-9d1805726142 | -7.4561 | -43.9786 | 2025-08-11 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 9177eb3f-609d-3446-a1b6-a50de3e440be | -15.4216 | -53.9073 | 2025-08-11 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9c1acdcf-456b-3b89-b61c-a334558349e1 | -8.579 | -54.696 | 2025-08-11 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 6b8a0d5d-fdb9-3bdd-abf4-2b246464b268 | -15.4407 | -53.9258 | 2025-08-11 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f90fcf4c-5f21-3bdc-85ee-ea395b86a48d | -9.2042 | -44.5305 | 2025-08-11 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f87d6e63-2855-3783-a9f8-a01cc781cd7a | -11.7209 | -50.1026 | 2025-08-11 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 2df51411-dd18-315e-9708-f4a072e72aeb | -8.5604 | -54.6973 | 2025-08-11 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 101fac29-056d-327b-adea-193700189534 | -11.9224 | -44.8597 | 2025-08-11 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 49c62917-69d3-328a-89e1-82c60238d263 | -8.9953 | -47.4403 | 2025-08-11 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 02454f59-716a-38c5-9e1b-c370c7dd5248 | -7.0614 | -59.1972 | 2025-08-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 953c9aab-fa02-3e3a-bc04-d2f6393a8467 | -14.1217 | -44.8699 | 2025-08-11 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| d8014c37-7678-3386-afde-6240d81444fe | -7.0613 | -59.2165 | 2025-08-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c6cfd04d-d56e-3d54-9590-3224278b5807 | -15.441 | -53.9048 | 2025-08-11 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ba0c8957-8700-3848-adc5-ac554ee32638 | -11.7558 | -51.6118 | 2025-08-11 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 4c453aba-992c-31d9-b548-e2a47c871d4f | -7.0615 | -59.1779 | 2025-08-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4701bf10-3ddb-32f5-a906-643a811e1b94 | -7.0799 | -59.1964 | 2025-08-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| aef6e756-af01-3b95-bf2c-8f6159da2a40 | -8.5605 | -54.6771 | 2025-08-11 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a165d2be-6bb3-30fd-886f-b2e16a46b0c0 | -8.5792 | -54.6758 | 2025-08-11 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f8aa670a-0aa0-30b6-a3b8-219ebede0003 | -3.9961 | -43.2418 | 2025-08-11 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6dea93ee-532a-311d-b9dc-1ea36b3ffe98 | -7.0797 | -59.2157 | 2025-08-11 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |


[Clique aqui para ver as próximas entradas](README32.md)
