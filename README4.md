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
| 2179f0a9-9812-3b65-8648-c104e35ec318 | -10.8165 | -49.229 | 2024-10-15 00:16:35 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c500f13b-9bd6-39c4-8429-dbf0de77e722 | -10.8208 | -49.250599 | 2024-10-15 00:16:35 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2f832d2-fae8-3351-a358-ec330b50a3e6 | -9.5651 | -43.4981 | 2024-10-15 00:16:36 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a2b1e258-ce3d-3351-849a-3a726c865065 | -9.5749 | -43.495998 | 2024-10-15 00:16:36 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| da2e23cd-20f5-339f-95d9-fb3210a6692f | -9.5768 | -43.5047 | 2024-10-15 00:16:36 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0ffca9e0-abf5-3094-af64-b43f7a4a4e00 | -10.1438 | -46.314499 | 2024-10-15 00:16:36 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb2b9cc7-9877-3b94-85db-7c739db7ed12 | -7.5517 | -35.103401 | 2024-10-15 00:16:37 | METOP-C | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70318a7c-3a61-3d79-8e67-29aeb0afb359 | -8.858 | -40.8634 | 2024-10-15 00:16:38 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 3c488a71-a0ea-30f8-a052-85ebb0120988 | -8.8596 | -40.870399 | 2024-10-15 00:16:38 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 24286edf-ef18-3f7d-a1b2-738ce4d4c395 | -8.8612 | -40.877399 | 2024-10-15 00:16:38 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f3266138-e6fd-3341-b7eb-45f8e5f622f7 | -7.4398 | -35.153198 | 2024-10-15 00:16:39 | METOP-C | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9228be23-d45f-3c7e-b8f1-acd0ff16fe24 | -9.4462 | -44.132198 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cdf29a69-13d9-3f26-b4b9-8ebaaec16f05 | -9.4482 | -44.141701 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07fc5022-4f86-3900-abeb-98f5d9768cb9 | -9.4503 | -44.1511 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c7f416db-a330-39f8-a43d-d5d7e5a8156d | -9.4523 | -44.160599 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eaf1feb5-586d-3134-bc91-d0889ef33afe | -9.4544 | -44.170101 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d0566d1e-8048-309f-a977-d9ee1f39d2b8 | -9.4564 | -44.1796 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 737c911b-aff0-3ed6-8bce-7de886e0421d | -9.4447 | -44.172199 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4bd4e74b-3b58-3bb4-81e4-0da658eb3a9c | -9.4467 | -44.181702 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67daf57c-6f25-3266-8986-da0a1f952b59 | -9.4328 | -44.164799 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 379be86f-1314-3430-aa20-35dffcc8a8c1 | -9.4349 | -44.174301 | 2024-10-15 00:16:40 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 85dc014d-d4b4-3261-84cf-f7c55f1242c8 | -10.0241 | -47.308102 | 2024-10-15 00:16:41 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75b45554-ed60-3985-ae19-6a5a238bce0c | -10.0273 | -47.323601 | 2024-10-15 00:16:41 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31a55020-04f6-3068-8775-2cca47212fb4 | -10.0049 | -47.264 | 2024-10-15 00:16:42 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed6856d0-e6fd-361f-b562-41ba4426bec0 | -10.008 | -47.279301 | 2024-10-15 00:16:42 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f958f1da-dbf6-3646-9259-7ed2f2ab0a43 | -10.0112 | -47.294701 | 2024-10-15 00:16:42 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b58dc298-e84e-3286-a602-57a306c67f96 | -10.0144 | -47.310101 | 2024-10-15 00:16:42 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b9c8684-3fe5-3ec4-8999-c28013b18498 | -10.0176 | -47.3256 | 2024-10-15 00:16:42 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81ee8cfc-e0a5-3707-b993-04786317b249 | -10.0502 | -47.633099 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82850722-269f-3ba0-985b-2c3f791bda40 | -10.0535 | -47.649399 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1accf67-2861-3682-89f3-1ebe1b42d951 | -10.0569 | -47.665699 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a07cc4d-1ffd-3c34-9ede-0c394526ccd7 | -10.0602 | -47.682098 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 222faefc-b1ce-3cf1-a372-4cb956f37f45 | -10.0636 | -47.698502 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9efcfcbf-c6a8-3bc7-b2a9-6b82a1548267 | -10.0405 | -47.635101 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47642872-65b3-3c87-87cb-d5c1720c46f8 | -10.0438 | -47.651402 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4acadbb8-2fc0-3db0-9182-f9bf1dd8b9bb | -10.0472 | -47.667702 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6788fa4b-0008-36b9-866a-3d5e796e5d47 | -10.0505 | -47.684101 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 703ce195-ec1f-3ad6-ae07-fa3c2302b37a | -10.0539 | -47.7005 | 2024-10-15 00:16:42 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0371a636-47a5-3e58-a5fa-bd502b04d93f | -9.5018 | -45.828201 | 2024-10-15 00:16:45 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e24f166-6c95-3163-b526-15024677a58f | -9.4745 | -45.796299 | 2024-10-15 00:16:45 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4c98d1e-306f-39f1-a52e-cc7f1537b926 | -9.9355 | -48.113098 | 2024-10-15 00:16:46 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7204611d-39db-3f44-bc98-fae08f303012 | -9.9391 | -48.130699 | 2024-10-15 00:16:46 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 987422cc-e80f-3350-98e5-079b7347b24c | -9.9294 | -48.132702 | 2024-10-15 00:16:46 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 433ad145-67d8-3a05-b4de-013a8fb98e93 | -6.8054 | -42.767799 | 2024-10-15 00:16:49 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5c72cd2-bc15-348b-a6b5-29f66836de5d | -6.8071 | -42.775398 | 2024-10-15 00:16:49 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d491b7d2-0cb2-3828-8976-73f03e962a9d | -7.8674 | -47.735901 | 2024-10-15 00:16:49 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d14a9414-4b63-3786-8a6e-2682307c2224 | -7.8706 | -47.751202 | 2024-10-15 00:16:49 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a01e4324-d3aa-3dde-a068-73f9f0768acc | -8.7125 | -44.0089 | 2024-10-15 00:16:51 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1043283-3f8e-3626-a8de-638b092831f1 | -8.7145 | -44.018002 | 2024-10-15 00:16:51 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3d9dbe-23b6-3318-a38c-1868ce636865 | -9.5214 | -47.774601 | 2024-10-15 00:16:51 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d287db67-57a4-3162-972f-8eac157182d4 | -9.5248 | -47.791 | 2024-10-15 00:16:51 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| daa71e4f-4993-3343-bc06-5606e2e569f5 | -9.5116 | -47.7766 | 2024-10-15 00:16:51 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21346aff-9f24-3d76-8635-922f841a8ae3 | -9.515 | -47.792999 | 2024-10-15 00:16:51 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5b833ce-3740-3bef-989a-f1c22a6ac047 | -6.8959 | -43.959099 | 2024-10-15 00:16:52 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f8ac29e-c025-3817-80ab-1dde49672f0f | -6.8978 | -43.967602 | 2024-10-15 00:16:52 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d4bb6b23-14af-3e5e-8575-3859a8a1943e | -6.6935 | -43.049301 | 2024-10-15 00:16:52 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22d9dd70-cbb7-33e8-847c-e107897d9498 | -7.47 | -46.5895 | 2024-10-15 00:16:52 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66697171-e5bc-3cc9-8558-275bcf5c5b1e | -8.3181 | -42.774399 | 2024-10-15 00:16:53 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 804a8f47-2601-3c52-b4af-551a56296d9f | -6.6824 | -43.6451 | 2024-10-15 00:16:54 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22582939-0f86-3824-b872-08f1afabbb41 | -8.1277 | -42.334 | 2024-10-15 00:16:55 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 527e7174-9282-3b51-baf8-afc454d66a86 | -8.1294 | -42.341499 | 2024-10-15 00:16:55 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95f1f8cf-461b-39f2-9ff7-511fa6ae600b | -8.1311 | -42.348999 | 2024-10-15 00:16:55 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c72a0c5a-1c96-38c0-b26d-d2a0e46c5a4a | -6.8111 | -44.457802 | 2024-10-15 00:16:55 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fac3b912-5f2c-32c2-aec7-971234e1cf9b | -6.8131 | -44.466801 | 2024-10-15 00:16:55 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dfccfc1-fb44-39c6-8d22-c798d6381638 | -6.8033 | -44.468899 | 2024-10-15 00:16:55 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76cf0ed7-ac21-3121-bd48-34c8bbf33341 | -9.1957 | -47.525902 | 2024-10-15 00:16:56 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fd00c6b-8a7f-3f31-b36b-e2e9604d0e0e | -9.1989 | -47.5415 | 2024-10-15 00:16:56 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afd9e7d4-765a-3fd5-8f05-dd344c33c3b6 | -9.186 | -47.528 | 2024-10-15 00:16:56 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8867454a-4cea-3436-95fb-6c97ca8d88db | -9.1892 | -47.543499 | 2024-10-15 00:16:56 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99fb2d24-d00c-38f5-b84d-707ff5dab33c | -6.5956 | -43.855598 | 2024-10-15 00:16:56 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 642e225d-c093-3cd0-9a9f-89ff19aaa64f | -6.5434 | -43.666901 | 2024-10-15 00:16:56 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdf34b74-0bab-310e-8572-030493d92936 | -7.4818 | -48.0765 | 2024-10-15 00:16:57 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 497129a2-2099-37ca-9c41-f496ff6b6f94 | -7.4852 | -48.092499 | 2024-10-15 00:16:57 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb3351b9-e72e-33a0-8d9f-7d34756d68e3 | -9.0983 | -47.643799 | 2024-10-15 00:16:58 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efedbe6a-5a02-35af-af66-f4a80d5660a9 | -9.1016 | -47.659599 | 2024-10-15 00:16:58 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1f435bc-1fae-3a52-b6ab-3c8de12e7ce3 | -9.0825 | -47.7631 | 2024-10-15 00:16:58 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cedaae4-9a7c-3b91-bf14-55418a3f4612 | -9.0858 | -47.779099 | 2024-10-15 00:16:58 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 064baafe-fd36-32f2-a628-641cb66a668b | -6.486 | -43.870701 | 2024-10-15 00:16:58 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ddace12-a496-3b0d-ba1e-4d8d2fd22701 | -6.4762 | -43.872799 | 2024-10-15 00:16:58 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe114467-e4f9-36ad-8245-80ee09991780 | -6.4781 | -43.881199 | 2024-10-15 00:16:58 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea82eb4-5053-3c5e-90a3-59cd4f75af01 | -9.0727 | -47.765099 | 2024-10-15 00:16:59 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e46a8405-a653-3d8d-a2af-f7aeeca418fd | -9.076 | -47.781101 | 2024-10-15 00:16:59 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3afc602b-5402-3961-a440-d7f71fdba704 | -7.0482 | -46.811501 | 2024-10-15 00:16:59 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f3feaf5-add6-344a-aa9d-2923062f976e | -9.1922 | -48.638199 | 2024-10-15 00:17:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d300146b-8344-34a1-9ab5-c63cd11030c6 | -9.196 | -48.6567 | 2024-10-15 00:17:00 | METOP-C | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f13b1ce2-2a52-32e4-86b0-8af1bef370a4 | -6.0663 | -42.410099 | 2024-10-15 00:17:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f86a11f5-49be-347e-a492-bd65ce2289a5 | -9.1765 | -48.8573 | 2024-10-15 00:17:01 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e486b9fa-e005-3423-9d5b-ac13b98a4fc1 | -8.1269 | -43.956799 | 2024-10-15 00:17:01 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df1bf7c3-714f-33c0-af1c-30ae2a781f3c | -8.1288 | -43.965698 | 2024-10-15 00:17:01 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 354e4615-e9a8-318a-b373-09a449f4498d | -9.1725 | -48.8382 | 2024-10-15 00:17:01 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be900429-dd2f-38f8-86e5-4db2265755aa | -6.1873 | -43.406799 | 2024-10-15 00:17:01 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f79a15a3-0386-3642-89a8-820358e1e326 | -6.1891 | -43.4147 | 2024-10-15 00:17:01 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 954cb898-9d5d-38fa-aba5-20f506d16423 | -6.1908 | -43.4226 | 2024-10-15 00:17:01 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b29f7b5-5b0e-3019-bdaf-29ae71d7de11 | -7.5042 | -49.482399 | 2024-10-15 00:17:01 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903e372d-fe9c-3d25-b712-29188270795a | -6.4091 | -44.356998 | 2024-10-15 00:17:01 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b71aae1-97fd-382e-8b64-59207f8207ba | -7.5098 | -49.460499 | 2024-10-15 00:17:01 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d258948-c006-339f-9130-68d86d84990a | -7.5139 | -49.4804 | 2024-10-15 00:17:01 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c14084f-9024-3aa4-b14d-63e4b6e8d594 | -6.3993 | -44.3591 | 2024-10-15 00:17:01 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8a9a5df-7b99-30fa-8ad0-5004421c9b95 | -7.5001 | -49.462502 | 2024-10-15 00:17:01 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6d84b6-509e-37ce-9142-82c8fb3eafdc | -8.2392 | -44.848202 | 2024-10-15 00:17:02 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
