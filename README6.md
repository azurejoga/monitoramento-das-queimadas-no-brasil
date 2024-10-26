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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06b22ff0-2e50-38ab-94a2-7743248c764d | -7.5978 | -47.0802 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18015bec-bcbc-3393-a36b-02eb66fba2aa | -7.5864 | -47.075401 | 2024-10-26 00:34:06 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f554e5df-8f27-3eb9-9e4b-f1eaf6a720e6 | -7.583 | -47.105701 | 2024-10-26 00:34:07 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c39434e4-e696-3f29-9f42-c5830caf7e56 | -7.4713 | -46.705601 | 2024-10-26 00:34:07 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a497a0c-7c82-35e2-9ffd-e293befe0520 | -7.4729 | -46.712799 | 2024-10-26 00:34:07 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f85550bd-76af-3fa2-b894-2d281a7c771f | -7.4386 | -46.743198 | 2024-10-26 00:34:08 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35cddf8d-fdeb-36d5-bd0c-391cab500d98 | -7.271 | -46.055698 | 2024-10-26 00:34:08 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a924dd10-fbe8-3af3-9c56-2e1f47f019be | -7.2594 | -46.0504 | 2024-10-26 00:34:08 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b523b967-5201-3a7c-b5b6-b5e763f12385 | -7.445 | -46.906799 | 2024-10-26 00:34:08 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17131005-a97c-3052-883a-c20430b274af | -7.9873 | -49.3694 | 2024-10-26 00:34:08 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5556c937-f69c-3e42-9006-f1f98a857972 | -6.6618 | -43.571201 | 2024-10-26 00:34:08 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63bc4d51-35ea-354e-80e7-9ff5ba713813 | -6.8074 | -44.455898 | 2024-10-26 00:34:09 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b0d7434-db2a-311d-8662-8fb3f44f23ad | -6.8095 | -44.464901 | 2024-10-26 00:34:09 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e812750-d58e-30d1-9338-1ce201638b1e | -7.4737 | -47.3512 | 2024-10-26 00:34:09 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10eb3724-4939-3dbe-9263-6257b9a0630d | -7.9836 | -49.6786 | 2024-10-26 00:34:09 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aefdf1b8-265f-3f68-bdd7-dbff4ab4594f | -7.9852 | -49.685799 | 2024-10-26 00:34:09 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a77016c-0a4a-380b-a9bf-268bab5932fa | -7.9868 | -49.6931 | 2024-10-26 00:34:09 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d15c73-7d4b-373c-8e2b-fac23d124d1a | -6.632 | -43.663799 | 2024-10-26 00:34:09 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14337d2b-beaf-3149-8e6d-a0002ad3842f | -6.6344 | -43.673801 | 2024-10-26 00:34:09 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a3fdfd8-3349-3c0f-a6b2-22b9c695b9d8 | -6.6993 | -43.949799 | 2024-10-26 00:34:09 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90d1fd74-4bcb-3af5-8c46-6142f2b5c328 | -6.6895 | -43.952 | 2024-10-26 00:34:09 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1904c6bc-f1d9-3bf4-86c4-912a139ae9ce | -7.9722 | -49.673599 | 2024-10-26 00:34:10 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5314a28-ceb1-393c-80f1-0af107a75fd1 | -7.9738 | -49.680801 | 2024-10-26 00:34:10 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd17001c-d47d-33df-b9e8-1ecb2f119f5f | -7.9754 | -49.688 | 2024-10-26 00:34:10 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f0ca363-09f9-3381-899a-4d7c72c44eab | -7.3583 | -46.978802 | 2024-10-26 00:34:10 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86adc0af-1cf6-3d1c-a014-934803f6c5bc | -7.3599 | -46.985901 | 2024-10-26 00:34:10 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c19dd9e0-a435-3373-aa15-7b7c5c571a4a | -7.4392 | -47.381001 | 2024-10-26 00:34:10 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc3f0e0-ab61-361b-92b8-ded0f8caa541 | -7.4133 | -47.357498 | 2024-10-26 00:34:10 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e45660a-6725-3561-90ca-43751c54034d | -7.1656 | -46.315601 | 2024-10-26 00:34:10 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4800eebc-9a76-3176-a39c-14778a9faecb | -7.1673 | -46.323002 | 2024-10-26 00:34:10 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81e313b9-da06-3e00-b255-29ac15c8fe3d | -7.169 | -46.330399 | 2024-10-26 00:34:10 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a53f730-fbb1-3be5-b72c-6465682c3a67 | -7.1136 | -46.3587 | 2024-10-26 00:34:11 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4468a777-9d6f-3b3e-b3da-27663589b799 | -7.1153 | -46.366001 | 2024-10-26 00:34:11 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b17407c3-09d1-36cc-a36c-bafa5455ea83 | -6.4386 | -43.237 | 2024-10-26 00:34:11 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0799708-0041-3fce-b3a0-309a96dfbd19 | -6.4411 | -43.247799 | 2024-10-26 00:34:11 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8331eae4-90f9-366d-967d-0b02f1abbf68 | -6.7085 | -44.694698 | 2024-10-26 00:34:12 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa8be144-fd62-3798-9603-3600bd3d95df | -6.9204 | -45.6087 | 2024-10-26 00:34:12 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78f72978-3a64-381f-ab17-42e818b53405 | -6.9223 | -45.6166 | 2024-10-26 00:34:12 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 271cd075-b87c-3bb1-85d7-7220af53fdaf | -7.1159 | -46.458698 | 2024-10-26 00:34:12 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b867b54-9242-360b-849b-9c37b3b64490 | -7.7234 | -49.524799 | 2024-10-26 00:34:13 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21b45c78-10ba-361c-8bf6-af5a364eedac | -7.725 | -49.532001 | 2024-10-26 00:34:13 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 237bcddd-aea2-33f3-8915-f382ec30d7c0 | -7.7266 | -49.539101 | 2024-10-26 00:34:13 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72c622af-556f-3369-afac-86c989b7a4d5 | -6.8703 | -45.883099 | 2024-10-26 00:34:14 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d6f6bea-6f6c-3372-bf31-b853ea3f2ee6 | -6.8587 | -45.877602 | 2024-10-26 00:34:14 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc68f86f-c6c0-3392-8791-9bb7750f1236 | -6.8605 | -45.8853 | 2024-10-26 00:34:14 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff203dc7-0c98-3a9c-96a5-dfe6ec0af9f8 | -6.8623 | -45.893002 | 2024-10-26 00:34:14 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b48e69fc-03cc-3770-979a-0ee5487d1824 | -6.8489 | -45.879902 | 2024-10-26 00:34:14 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 730d1438-5bbb-38f8-b2e7-27a42cbe099f | -7.0333 | -46.6842 | 2024-10-26 00:34:14 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4236d9d-4b5b-3574-8e24-5195e509adc8 | -7.035 | -46.691399 | 2024-10-26 00:34:14 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ae8036d-b94d-3edc-855f-d7fc2d64affe | -7.0645 | -46.866001 | 2024-10-26 00:34:14 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6742321-3a14-3c64-a890-17242602ee81 | -7.0661 | -46.873199 | 2024-10-26 00:34:14 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f495ac72-3c75-3165-bdd3-0ff57dc54130 | -7.5585 | -49.5238 | 2024-10-26 00:34:16 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac928e06-35a4-3c36-8085-676189ef9b0a | -7.1443 | -47.854801 | 2024-10-26 00:34:16 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d7a0392-4c2f-3caa-9469-e87a1b6f52b1 | -7.1459 | -47.861698 | 2024-10-26 00:34:16 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 600641c9-d458-3149-8226-0d92ec49e7c9 | -5.6476 | -41.8144 | 2024-10-26 00:34:18 | METOP-B | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a068b04a-2d76-3956-8a39-dd3a54aa6bbd | -7.0143 | -47.963501 | 2024-10-26 00:34:19 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 767c6af5-42f8-378a-a352-979dde546619 | -7.298 | -49.277199 | 2024-10-26 00:34:19 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df26e89-7c43-390e-b573-54425e8ddfb1 | -7.2882 | -49.2794 | 2024-10-26 00:34:19 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f02fe976-7b34-387e-883d-39caba50bb05 | -7.2898 | -49.2864 | 2024-10-26 00:34:19 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8364c413-ad17-3ff9-9a9c-4bcd53bfb020 | -7.044 | -48.3246 | 2024-10-26 00:34:20 | METOP-B | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a018a5d-a7ff-3790-b306-722418c3c4b4 | -7.1203 | -49.1259 | 2024-10-26 00:34:21 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b84886f2-261e-30b6-9255-0c1e48b0e246 | -7.1183 | -49.1628 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c2d956b3-ceea-31a1-8587-56f1ffa06c0a | -7.1198 | -49.1698 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6f392c94-d2f2-3993-9bf8-ba920192572e | -7.0976 | -49.116299 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cf743761-18ca-31cf-bd72-4d68d3c36468 | -7.0991 | -49.123199 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab74737-3803-3828-8e93-c223e2d83180 | -7.1007 | -49.130199 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e69e268d-a5fd-378f-8dda-ae44f1490df3 | -7.1023 | -49.137199 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| db2fe525-e773-386b-86bf-2a5ed6ecb1bb | -7.1085 | -49.165001 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4f4fb933-346f-393f-9139-88785b5b430a | -7.1302 | -49.262901 | 2024-10-26 00:34:22 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dca1864b-e31b-3e7e-93c4-21b6aa9058d7 | -7.1318 | -49.269901 | 2024-10-26 00:34:22 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72cdf5b2-5e73-3d96-bbc4-5a11a334f290 | -7.0893 | -49.125401 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 82c95348-8353-3165-b801-c5263d56641d | -7.0908 | -49.132401 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ff963303-ab85-3bb7-95d5-f00cae11a2eb | -7.0924 | -49.1394 | 2024-10-26 00:34:22 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f4493b84-c63f-3540-9160-818d3dec2bfe | -6.8444 | -48.2612 | 2024-10-26 00:34:23 | METOP-B | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee4f3ee-e4f9-39bd-ae91-5ab573c5f57e | -7.0336 | -49.152401 | 2024-10-26 00:34:23 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1b3819-2584-3d5e-a63c-6c46efc82985 | -7.0351 | -49.159302 | 2024-10-26 00:34:23 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ba2f35c1-591c-3f3f-a011-c56c99f994e8 | -6.4629 | -46.715 | 2024-10-26 00:34:23 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 034968ab-ee20-3ada-a214-350698a0c5af | -7.029 | -49.270599 | 2024-10-26 00:34:23 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62811bc9-e1ee-3226-bd17-c2d1410149fd | -7.0306 | -49.277599 | 2024-10-26 00:34:23 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7640c38d-30f4-3bed-ad6c-858febdd60b5 | -6.5122 | -47.0214 | 2024-10-26 00:34:24 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7defc28-dc5a-3364-a027-6703f5e48140 | -6.5139 | -47.0285 | 2024-10-26 00:34:24 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c664a827-2200-3c88-b937-2fc24295bbc4 | -5.0417 | -40.871601 | 2024-10-26 00:34:24 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a041566a-f92c-3559-834f-123e6cb9bb40 | -5.0456 | -40.887798 | 2024-10-26 00:34:24 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fb8d5d2c-92d6-3106-be97-158423908eb6 | -5.7012 | -44.353802 | 2024-10-26 00:34:27 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed1dcf8-d676-3cf8-a167-2a064f485299 | -5.7034 | -44.3633 | 2024-10-26 00:34:27 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6afe20e8-4626-33bf-add9-71006ce878f4 | -6.4485 | -47.648399 | 2024-10-26 00:34:27 | METOP-B | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c46bdd9b-20b6-3eba-a009-8e9593d1be5b | -6.3754 | -47.371799 | 2024-10-26 00:34:27 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73adaf10-c7f0-3c93-b394-3fb3a596e136 | -6.6848 | -48.743599 | 2024-10-26 00:34:27 | METOP-B | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 622c6c72-4765-3698-aef2-13412c8d305d | -6.2858 | -47.340401 | 2024-10-26 00:34:28 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1afaf1ff-d693-31bb-819a-2b759d135c86 | -6.2805 | -47.817101 | 2024-10-26 00:34:30 | METOP-B | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be1222b7-4b4c-3dce-a50e-12037320509d | -6.282 | -47.824001 | 2024-10-26 00:34:30 | METOP-B | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a10c4270-ba13-3c90-b5b7-491c65546ce4 | -4.9112 | -41.960201 | 2024-10-26 00:34:30 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6920b6a-5250-3bc7-87a7-5d41a71fdd4b | -4.9145 | -41.9739 | 2024-10-26 00:34:30 | METOP-B | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 004914dc-015d-30cc-bc6b-e28a7010cd0e | -6.11 | -47.202099 | 2024-10-26 00:34:31 | METOP-B | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82facd14-97db-3431-b9de-10cba6a2eaa2 | -6.0986 | -47.197201 | 2024-10-26 00:34:31 | METOP-B | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abe01cee-70c7-37d4-964c-4023045af082 | -6.1002 | -47.2043 | 2024-10-26 00:34:31 | METOP-B | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc3b7eb-b9b5-3c34-ae5f-75ebd880d4ae | -5.8369 | -46.232498 | 2024-10-26 00:34:32 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8a2ae9d-b853-3194-9ec5-d93f24025bfe | -5.8387 | -46.240101 | 2024-10-26 00:34:32 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4fedb98-3757-3af5-ad38-df5d6f8248b3 | -5.569 | -45.2934 | 2024-10-26 00:34:32 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd835ea5-7117-3de6-8768-d5257c70542b | -5.571 | -45.3018 | 2024-10-26 00:34:32 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
