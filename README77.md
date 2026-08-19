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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a87748e-f71a-3058-aaa1-ac70e165bf5d | -11.8721 | -50.1708 | 2026-08-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| be08221c-5133-352a-95a4-af7822dd03ab | -11.8717 | -50.1923 | 2026-08-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| c255684c-c53b-320f-a900-3490eaa0c5f0 | -14.1432 | -52.9558 | 2026-08-19 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| acddcb0e-a49d-3b9a-9500-b26fda2a381c | -6.3909 | -51.7475 | 2026-08-19 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 224ce3db-9d17-3829-8bb6-cb4b7eb3c3b0 | -5.9274 | -49.2505 | 2026-08-19 14:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 264e35d8-590a-3f20-9a1a-a8922bfdd672 | -11.8911 | -50.1686 | 2026-08-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| c2532e8f-d08d-3bd8-944c-f8cb633ea25e | -9.7537 | -43.2962 | 2026-08-19 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 119.8 |
| 05950bb7-98ad-3070-a6ca-0b0f43d6b776 | -5.4319 | -48.3996 | 2026-08-19 14:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8a148f7c-54c7-3994-9021-7019e17eb4c1 | -10.8072 | -50.3121 | 2026-08-19 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 038bad4b-3cca-3ec0-bc90-13efc268ae11 | -14.2213 | -52.883 | 2026-08-19 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 8c6e1d87-b6f1-3638-a995-2a09c5f7d99e | -13.5858 | -51.7781 | 2026-08-19 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 50bf66a5-c4d5-3101-bff5-5b804475952e | -6.7123 | -58.9412 | 2026-08-19 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 34fcd957-c5e6-38ec-a83a-bcbd35f04cdb | -14.47 | -51.8551 | 2026-08-19 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 79fca6bd-c183-3c4c-81c3-5f823c30f104 | -6.073 | -45.2873 | 2026-08-19 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 69ac3731-d765-3355-b8db-bb4fbe79082f | -6.0179 | -57.8437 | 2026-08-19 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 37ac3fbc-2175-342b-a953-5857adcd7492 | -14.221 | -52.9041 | 2026-08-19 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 234.8 |
| b84402cf-066a-3b01-8c26-5aba28af5902 | -9.7393 | -46.8504 | 2026-08-19 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 53b879ff-025e-3e12-b6ed-0f73e8718642 | -11.9319 | -49.9914 | 2026-08-19 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 72ec4399-74e9-3b83-8eb8-2749f165b84f | -15.4388 | -52.9148 | 2026-08-19 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4e7f3254-c35e-3a18-870b-851823b7dc89 | -6.0912 | -57.9187 | 2026-08-19 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| ffc10439-a87e-3da2-9075-5479ae9f5190 | -5.4317 | -48.4212 | 2026-08-19 14:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| bd13e7e2-0b3f-35a1-bac9-2c99ec3bdb1a | -5.9274 | -49.2505 | 2026-08-19 14:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a167dcb1-0cff-3d50-81f6-0d981c81cd14 | -8.1042 | -51.654 | 2026-08-19 14:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 995335db-261a-3409-84f4-c6be4005a40a | -6.0728 | -57.9194 | 2026-08-19 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c528cbec-1727-3532-affe-f0138fb2869a | -13.2996 | -51.6862 | 2026-08-19 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e7e544cf-9230-36ef-83d3-4e2cbb2f5e2c | -8.503 | -54.8625 | 2026-08-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 842a31f4-90f0-34ee-b03a-fb474aadbcfc | -6.9581 | -52.8065 | 2026-08-19 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f2dae374-039b-3cc7-a976-06e423196d2d | -6.0913 | -57.8992 | 2026-08-19 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fa7ac6f3-93c6-3688-8958-0a50aa445082 | -11.1936 | -54.0199 | 2026-08-19 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| cff8ef55-94d4-3a06-840d-a3d1db970548 | -9.4366 | -48.2955 | 2026-08-19 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 0e5374ce-5589-33ea-b375-7b8db0414775 | -9.7393 | -46.8504 | 2026-08-19 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f849c8ef-b247-3daf-a177-1d0bb966dd20 | -14.3734 | -58.2778 | 2026-08-19 14:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 37934d72-2e59-3d04-b6a2-f3f01bc0cf4f | -11.1178 | -47.2654 | 2026-08-19 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 181bfa58-0a44-34d6-aac0-8ecf17200e77 | -14.1625 | -52.9534 | 2026-08-19 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 35aa7865-acce-3846-b261-014fedac30bd | -14.3906 | -53.1354 | 2026-08-19 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| cf478664-b221-3a29-b77f-7daacc138b95 | -9.7533 | -43.3199 | 2026-08-19 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 342.3 |
| d24ec2f1-0f8f-30c1-81f3-81f341767baa | -7.5487 | -55.5829 | 2026-08-19 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| effa4142-19bb-3778-990d-0ee4857f6da8 | -14.2952 | -51.9208 | 2026-08-19 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e2502f26-2f59-3cc5-8948-5454999fb59a | -8.5783 | -54.7768 | 2026-08-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 664574ce-de3f-3424-928d-b7db5530e7fe | -13.2805 | -51.6886 | 2026-08-19 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| d798a7bd-a02e-39f5-bafe-76076010651d | -11.9319 | -49.9914 | 2026-08-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 9def8ca2-f7bd-3ab3-9839-27a0250cd6c7 | -7.5301 | -55.5839 | 2026-08-19 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 343564ce-d4aa-3e3e-9560-d22d7760b578 | -6.254 | -55.391 | 2026-08-19 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 592edae9-6620-3b23-a08b-255afc7a2944 | -6.3909 | -51.7475 | 2026-08-19 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| e9547ccb-fb59-3443-9c2a-e9bbbcc0a81e | -11.6002 | -50.5454 | 2026-08-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| aec5385b-0905-3e78-90c8-0e8b04737dc2 | -8.5596 | -54.778 | 2026-08-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a8b5e1e8-8161-3664-a473-750845e69349 | -11.9961 | -53.4475 | 2026-08-19 14:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| a9b61b01-a425-3688-a368-665d4dc5af30 | -11.2189 | -55.0585 | 2026-08-19 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| f353a549-389c-3eda-a747-d3de430d61db | -14.1432 | -52.9558 | 2026-08-19 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 564bbda7-14aa-3fbc-baf0-c65c597d425d | -10.8075 | -50.2907 | 2026-08-19 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 598cdd47-9808-3a39-9351-e4bf97c6e33b | -7.9149 | -61.7288 | 2026-08-19 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 942dd5c6-104e-3ed3-86d2-794331cfd4bf | -9.7537 | -43.2962 | 2026-08-19 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 170.5 |
| 1f834205-f496-3a11-9bfd-ac8d4b07e0ff | -5.9994 | -57.8639 | 2026-08-19 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7d5c5127-386d-33bd-830c-71f7690c4aed | -8.5971 | -54.7553 | 2026-08-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fd5aef9b-b6fd-386b-a9df-eca63cb373a2 | -10.8072 | -50.3121 | 2026-08-19 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| db25f23c-38bc-3092-b86b-c3b0d14b2ca8 | -5.4317 | -48.4212 | 2026-08-19 14:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a7403d1b-b019-3613-bf5c-24a62fe39b4b | -11.0984 | -47.2901 | 2026-08-19 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 47b98817-6f8a-3804-908f-b6aaef60de15 | -20.5778 | -45.9314 | 2026-08-19 14:40:00 | GOES-19 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 690cbd63-28f2-354b-b717-523e37cd4878 | -14.2763 | -51.902 | 2026-08-19 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 589374bd-a571-3c4c-a053-9c3450cb88ac | -13.5858 | -51.7781 | 2026-08-19 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 8f98d631-b171-344d-8dc0-076301c35b5a | -14.4892 | -52.9968 | 2026-08-19 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 42056565-bf84-3759-9455-38573978532e | -10.7687 | -50.359 | 2026-08-19 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| f40da7a8-39bc-3610-858a-5974d7d918ad | -5.9272 | -49.2719 | 2026-08-19 14:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 70899a7b-8ab3-3a31-a15d-afb6c46e734f | -6.3971 | -46.6292 | 2026-08-19 14:40:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 05b63ef3-8948-3de7-a8c0-bafb620316d7 | -6.0366 | -57.804 | 2026-08-19 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2479fd70-48e6-3448-93a1-64517e43e95c | -7.6171 | -49.9226 | 2026-08-19 14:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 178a1792-6aff-38e8-96c1-e81ec30dc5d7 | -11.8721 | -50.1708 | 2026-08-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b1b68ec3-9459-31a5-b6dd-987e5f01e26f | -5.4319 | -48.3996 | 2026-08-19 14:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |


