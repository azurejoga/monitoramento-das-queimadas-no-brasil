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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c65e9854-da74-3e93-b1f2-5fec6e7501bc | -3.6196 | -47.28922 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bbcc182-87ee-370a-a05d-a7c421f24cfa | -3.61897 | -47.29339 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 227ffa13-790b-3b9a-8dbc-4ec5260f94e8 | -3.61834 | -47.29752 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c2ea96f-eeef-3554-9657-3ec9c90aded2 | -3.61772 | -47.30159 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a699cd08-9475-3969-94d5-32ae748c4ab1 | -3.61444 | -47.25046 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8b0f86d-3721-367d-8ac1-35c1e46ae8fb | -3.61146 | -47.24577 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03841ab9-9b92-34e1-a821-54dbc5e55e62 | -3.59973 | -47.29889 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 512eaa45-c185-37a7-a7ce-88e51f829118 | -3.59613 | -47.29837 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e579666-6f47-32b6-b25d-9bfc7558bd87 | -3.59017 | -47.28906 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f35556f3-e29c-3c9a-8136-541ed76693f5 | -3.57503 | -47.3759 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f5577531-d5ca-3020-bb21-a90a28829531 | -3.57439 | -47.37996 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 02750f24-09f2-3c30-ae1e-896bf89cdb88 | -3.57376 | -47.38401 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aab05827-3770-30c9-8d11-b910b870b2fd | -3.57144 | -47.37536 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 6fc1ea86-9271-35df-90e8-d5b318c68014 | -3.57081 | -47.37942 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| bdc612a9-6af1-30b0-82c7-ff59a9261876 | -3.57018 | -47.38347 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7950807-9f93-3406-8d71-f6d97896a4c6 | -3.56786 | -47.37481 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9c7c3554-5816-3b7a-b254-7e186c703fee | -3.56723 | -47.37886 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c7595904-c980-382a-97e6-f611f8af1075 | -3.5666 | -47.38292 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1e88ff53-b883-33a7-93f0-856fb1cc09fc | -3.56365 | -47.37831 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d004a1ad-e0f3-3574-856c-0afd9eea72b1 | -3.56302 | -47.38237 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a9372852-3182-3ca1-808d-e03045ef9efd | -6.42239 | -47.28837 | 2024-10-30 04:44:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ac30977-e246-3bdc-a4f5-bf9ad6379cbb | -6.36192 | -47.9166 | 2024-10-30 04:44:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c72ffcb-3032-3f76-8e4a-593b295d9d86 | -6.167 | -46.95712 | 2024-10-30 04:44:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ee845c6-3d47-3803-9815-e7d5d56055cd | -6.14399 | -47.23867 | 2024-10-30 04:44:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04a333e4-8ed8-3f93-acc6-f6daeb5eb54e | -6.1344 | -46.87047 | 2024-10-30 04:44:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a8ec22d-ad1f-3986-84e9-186aa9c0549f | -6.04759 | -46.60107 | 2024-10-30 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7010a329-72a7-3f22-9d41-aada937c47a2 | -6.04374 | -46.60051 | 2024-10-30 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdce09ad-03ea-3d25-8404-7da9d435f9e4 | -5.73392 | -47.04463 | 2024-10-30 04:44:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f714aeca-0512-3ab1-a6db-566f5bc22c8f | -5.5386 | -46.53324 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc9eaa53-d8d3-3e20-9c69-01bde7673194 | -5.53652 | -46.52999 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be313948-0b0f-3fc5-b71b-75c352ba0c32 | -5.53583 | -46.53473 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61c01846-1081-338e-9e40-fb426c19f6cf | -5.53476 | -46.53267 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3630c40f-3658-3cb3-b9b6-71e609cbf6c3 | -5.50707 | -47.16824 | 2024-10-30 04:44:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eb550ea-e1f6-38b8-a3e2-0e2f7c3f00b0 | -5.37705 | -46.57487 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70dd773a-d3f7-3599-bd1c-bace8a0d6428 | -5.22922 | -46.73891 | 2024-10-30 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04c43219-5758-3a7e-a3e8-310d16a64810 | -7.54239 | -48.30294 | 2024-10-30 04:44:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45bb4f1e-3d36-36fe-b155-f4299ee5e4f2 | -7.54052 | -48.30552 | 2024-10-30 04:44:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 416088b7-aa2a-3c28-99d1-c563ffc7a7f8 | -7.53881 | -48.30244 | 2024-10-30 04:44:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b3b57bf-b3db-3f0a-ac28-390ffad74af8 | -7.53819 | -48.30648 | 2024-10-30 04:44:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8808c6a8-fa60-3c91-a7c4-50713a36f31e | -7.27254 | -47.75405 | 2024-10-30 04:44:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c15ca63-9919-39a2-acde-c0518fa2c162 | -7.04289 | -47.62116 | 2024-10-30 04:44:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11241b71-bee4-304c-a580-d319ff3a1b79 | -6.73993 | -48.17708 | 2024-10-30 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 688c8964-34bd-38aa-9bec-f0299d8f8d49 | -6.6627 | -47.09557 | 2024-10-30 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f769abe7-01d1-3f4f-b25d-25528ed74a2b | -6.55814 | -48.14378 | 2024-10-30 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f97cf2c-dc3e-3ed2-b93b-c237b96881b1 | -7.6685 | -47.32307 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6bd91fd-4648-345e-88ce-31c5c4fb03a4 | -7.66782 | -47.32763 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4eaec652-62c1-3306-9eae-a1cfbcc11bfa | -7.66641 | -47.28547 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f90d5cc-611b-308e-9170-fa7c8e67bb35 | -7.64161 | -47.24397 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9723b313-d397-3486-a798-91a1d10f9e98 | -7.58824 | -47.11462 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfa437de-9711-35a4-9103-c5075b745df8 | -7.58755 | -47.11927 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77b0c7b7-220d-3baf-8416-068a98b5ef38 | -7.58443 | -47.11404 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 077501c3-b561-3fe7-bb2a-2e5f34bd5f20 | -7.58373 | -47.11869 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d3c37ea-310a-3786-85be-7fc8fba2ae20 | -7.58163 | -47.13277 | 2024-10-30 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e28f2964-314a-3e26-bfeb-b872a9873087 | -7.48582 | -47.1545 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e62a131e-8e4a-3a63-b39e-cb34d6432da6 | -7.48202 | -47.15393 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 284c64d4-1ce2-3aab-9236-85eba0836066 | -7.46577 | -47.1846 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8572cd9-5a73-3a56-b434-213795c40bcd | -7.36703 | -47.22889 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f71c49d-fae1-38b1-a806-775dc7144104 | -7.36634 | -47.23346 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d26c0d2-7661-32fd-a829-e2fd06f6bf2b | -7.02768 | -47.25489 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 847f65c7-fdaf-3205-ab9e-b8483095a875 | -7.02394 | -47.25422 | 2024-10-30 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 868bc2af-5625-3173-bd4c-b58d570cd0d2 | -6.88288 | -46.83588 | 2024-10-30 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fff0773-0657-3ac3-a524-670b26af5f7d | -6.88216 | -46.84067 | 2024-10-30 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3599606-d397-370b-a3f8-46048ebdcba8 | -6.87903 | -46.83532 | 2024-10-30 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d33f1001-3271-3740-8726-9112f6e44a7e | -6.81927 | -46.78748 | 2024-10-30 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a125c570-31ba-3aa3-9749-b8faad19396e | -9.03989 | -47.81635 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13d6b9c9-3c93-34d0-9234-9113767aff84 | -9.03615 | -47.81582 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3ab0a25-89ec-3d32-9c43-93d4e15f2313 | -8.87344 | -47.97124 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fc75a00-b08e-3064-977f-2eaf5fc07ee6 | -8.86975 | -47.97064 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f422009-448d-3cb3-aaf7-1ed6aaa74558 | -8.68105 | -47.95787 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 810da92a-7f56-357a-8037-5695c2683b0a | -8.67896 | -47.95504 | 2024-10-30 04:44:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f495be12-f3f3-3e7a-b3e6-727143af3319 | -8.55007 | -47.99562 | 2024-10-30 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b02eb7c7-4bfa-36e0-b390-2254e7783f33 | -8.23305 | -47.67126 | 2024-10-30 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89b2eeb2-74df-393f-8d31-21d960256d5e | -8.05682 | -47.08468 | 2024-10-30 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71410942-5688-3b61-b099-caa6ce7c7f36 | -8.05502 | -47.08743 | 2024-10-30 04:44:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2201ad4f-11b4-3227-b07a-03f53fe98878 | -1.98386 | -48.75451 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c41f82c9-9caf-3375-b001-6da1c57bb73b | -1.60548 | -47.24374 | 2024-10-30 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21e6364a-5aaa-327f-b538-b95998705327 | -1.47994 | -47.33359 | 2024-10-30 04:44:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55441416-2daf-36b6-baa6-8e4e5c81c6b1 | -1.47643 | -47.33304 | 2024-10-30 04:44:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04f85ca7-4641-3875-9d2b-bc7af4f31950 | -2.15526 | -47.90174 | 2024-10-30 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 322ab03a-15d5-3212-a275-821a11e6cbc6 | -2.07413 | -48.21931 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 580d7605-d5c1-3478-bcef-62e8a0d709e9 | -2.07356 | -48.22297 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a93eea16-60be-33f0-b54f-1fc249a6baf7 | -2.02897 | -48.1979 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb4f9ec8-ebd5-3446-b546-51910f8b9a88 | -1.8677 | -47.82496 | 2024-10-30 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f346fde-be65-3450-b688-78170984dd1c | -2.90965 | -48.61395 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 320faf69-fe62-34c8-8f29-bcdce4208f5d | -2.90625 | -48.61343 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cfd863e-dc11-399c-bbba-80bf18e7dc36 | -2.90569 | -48.61704 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c09ea2f-0137-3121-8f79-e20b9cb141be | -2.85688 | -48.46139 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faf4aec2-41a8-3580-a2ce-68460cf026b0 | -2.84724 | -48.45617 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b49b6f9-d874-33c7-b166-3e388d71bca9 | -2.80356 | -48.66824 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b15728ff-7b62-36c6-b6a7-850abd7e8744 | -2.76808 | -48.71793 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d6339c8-8005-38ec-939b-03940c6b6669 | -2.76582 | -48.71023 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac190314-027d-38ba-a87f-4537297e1a2f | -2.76414 | -48.72099 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fc1b173-fc7e-3657-a9a5-c64a7bfb3f36 | -2.76294 | -48.66196 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ec1586c-b37c-3f8c-b706-9e2d8d8cdafd | -2.99123 | -48.06824 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbdba6fc-140c-359b-9932-5f83b882d909 | -2.97791 | -48.78263 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b6dcd2-4f27-3f69-8b5d-4b77b6f495a3 | -2.97735 | -48.78621 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c820bb-7c21-3421-8db7-5e1eaa8f0290 | -2.96819 | -48.05702 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ed0ed91-0266-370d-a34b-6027826e9227 | -2.9676 | -48.06079 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37c2cac3-3830-31c3-9da9-868a04b3c897 | -2.96702 | -48.06455 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be13399f-127c-3db1-b65f-fa7e84614ab3 | -2.96586 | -48.63704 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README75.md)
