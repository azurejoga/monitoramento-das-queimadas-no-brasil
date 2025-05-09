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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64f0defd-2f64-3eaf-bcb7-d67b864ee306 | -23.6121 | -49.0181 | 2025-05-09 13:10:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 2a8f9f20-e5a2-3e19-98d3-492d929d4320 | -10.9736 | -44.4177 | 2025-05-09 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| cb0904c2-edd1-3c98-8c40-07642d5dff7a | -6.9615 | -42.7872 | 2025-05-09 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| d7757544-c5cf-3688-b027-6580dce5bed5 | -10.9736 | -44.4177 | 2025-05-09 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 593a412d-21ac-3b34-9b24-9cf8e6d8c7bc | -10.4724 | -49.8979 | 2025-05-09 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 7f691c3c-ea86-3999-adca-496589faf53c | -23.6121 | -49.0181 | 2025-05-09 13:20:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 139.0 |
| f79a2d1e-5fe5-3970-9cfa-dd1d0dad6ea1 | -7.6344 | -46.4834 | 2025-05-09 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 89e643cc-ca0e-37cf-8536-57b8740a0e7b | -7.6156 | -46.4851 | 2025-05-09 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f2ba7642-f2d5-3f42-bbee-1925023ef95d | -10.9736 | -44.4177 | 2025-05-09 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b3358809-dc8f-32ed-b097-2f878892ee4c | -6.9375 | -43.2596 | 2025-05-09 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| f0e72794-e997-3928-aa41-114b975bd06f | -11.3855 | -49.6459 | 2025-05-09 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 5eac11df-7d7d-3b86-bdbe-65a606e44eb6 | -10.8318 | -49.9023 | 2025-05-09 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 63b0c0a6-a925-3921-a93f-ef9032ef06c2 | -7.6344 | -46.4834 | 2025-05-09 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ad9b5a0a-5fbc-3b46-b723-e0fa8f90c687 | -10.9733 | -44.441 | 2025-05-09 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 364.3 |
| 7b50aa3b-f18e-362e-904c-a9a305dea3c8 | -10.8129 | -49.9043 | 2025-05-09 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 698a7174-7f6c-383b-a15e-c657d6ab122b | -7.6156 | -46.4851 | 2025-05-09 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e288d108-d4fb-38d2-bb58-5f771250fb1f | -23.6121 | -49.0181 | 2025-05-09 13:30:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 145.7 |
| fd0bf151-2144-3f2d-8dde-d3c1541da6da | -11.4046 | -49.6437 | 2025-05-09 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 2178421b-9c86-3331-8df4-abd5dd39f743 | -6.9615 | -42.7872 | 2025-05-09 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| ffc97362-4ab4-3d10-9590-5f1facbaa333 | -10.8129 | -49.9043 | 2025-05-09 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 428cb8f2-217b-385e-bea7-58c9b6909391 | -14.6414 | -45.1263 | 2025-05-09 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 6abb4e02-cebb-3318-ad08-5197a2bd4ff2 | -7.6344 | -46.4834 | 2025-05-09 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 7c479879-2f19-3496-ace7-baabe586c4f7 | -11.4046 | -49.6437 | 2025-05-09 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| ae3cc809-1101-3deb-be3e-26b1f9d52537 | -7.6156 | -46.4851 | 2025-05-09 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 49491485-1ca8-3d34-b8e5-2a937675f7b9 | -23.6121 | -49.0181 | 2025-05-09 13:40:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 10997461-9989-3fc4-8493-06ac6d3a9c98 | -11.3855 | -49.6459 | 2025-05-09 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 210.8 |
| ca52f261-58a2-3ba2-90c3-3c3bb857301f | -23.6121 | -49.0181 | 2025-05-09 13:50:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 2d2e1cc2-1d98-3bee-923f-af70f77c404a | -7.6156 | -46.4851 | 2025-05-09 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 222fc58c-f943-3073-bf94-415d4c553a2c | -10.9736 | -44.4177 | 2025-05-09 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 4ef43fd2-e74c-3e64-be6a-077507ef58df | -10.8318 | -49.9023 | 2025-05-09 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 227.7 |
| 6a0c61ea-b09c-371e-b8b8-de4d89c9b9b2 | -7.6344 | -46.4834 | 2025-05-09 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 121b7e30-da28-3e64-8cbe-6d7d45582060 | -11.8221 | -49.7023 | 2025-05-09 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5741bda7-bfff-39dc-a883-9a75e1290e7c | -14.6414 | -45.1263 | 2025-05-09 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 8bf5a5c9-3ade-3593-86af-0dbf83bb818a | -10.8129 | -49.9043 | 2025-05-09 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 50d46201-5d57-3de8-a07d-1eb0b7c60ecd | -7.6156 | -46.4851 | 2025-05-09 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 043782d0-e52e-31b9-b91e-bc9cdc2396a9 | -10.9736 | -44.4177 | 2025-05-09 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8dc01088-c7a4-302a-b4e1-05ad76178408 | -12.6339 | -54.0642 | 2025-05-09 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a50c4b56-0ece-3ba4-bb0f-fe5f6586eac4 | -14.6414 | -45.1263 | 2025-05-09 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 399f098f-3a0e-3ee2-9d48-63c021c53329 | -6.9615 | -42.7872 | 2025-05-09 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 15994951-39a2-3fb5-9371-5dca936a928e | -23.6121 | -49.0181 | 2025-05-09 14:00:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 360fa9b7-7431-3f98-bf66-ce3f23e74e5b | -10.8318 | -49.9023 | 2025-05-09 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 1928d85a-af67-3c3b-9018-e98c307d1d92 | -7.6344 | -46.4834 | 2025-05-09 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| dfa1e478-18ef-31f5-a13c-8a010c0df3c2 | -10.8129 | -49.9043 | 2025-05-09 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 780ca098-2749-3a1e-984e-5b28522e8db6 | -23.6121 | -49.0181 | 2025-05-09 14:10:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 110.6 |
| cb39010a-90cd-3c33-a2b0-1e647df024e0 | -8.07 | -43.1216 | 2025-05-09 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 6e7c87f5-0159-35e3-aac6-ed28003a9b01 | -10.8318 | -49.9023 | 2025-05-09 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 08d8ae95-dcc2-3d41-a2f6-2d7e6e8263a2 | -12.6339 | -54.0642 | 2025-05-09 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f95daa4d-71f4-332f-b87b-a87c77646e5e | -11.9557 | -49.6862 | 2025-05-09 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0174fcbc-0a64-3a5f-a83a-71d07be76dd4 | -10.8129 | -49.9043 | 2025-05-09 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 7432b036-13ef-3c76-bf73-fe04687d28eb | -10.9736 | -44.4177 | 2025-05-09 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a1d06cc1-3bd2-3a61-89c6-07d968e96314 | -7.6344 | -46.4834 | 2025-05-09 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b7c56193-304e-3726-b155-0a2385134d23 | -7.6156 | -46.4851 | 2025-05-09 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 04b811ba-ee12-3ea7-baef-9c5a3133da04 | -8.07 | -43.1216 | 2025-05-09 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 3f47ad25-9063-3565-aa28-b95fc4079092 | -10.9736 | -44.4177 | 2025-05-09 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 520fcc13-8b5e-3d15-a959-2b1ba70956f1 | -7.6156 | -46.4851 | 2025-05-09 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 61bec7d6-6533-3816-b7f1-75492896a1ea | -14.6414 | -45.1263 | 2025-05-09 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 685600f5-f726-36fa-bcd0-0b64789e456d | -12.6339 | -54.0642 | 2025-05-09 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 44564506-deeb-3f09-8483-0b57dab10bd5 | -8.07 | -43.1216 | 2025-05-09 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 13a870ac-5038-39ad-8412-d4540b92b262 | -7.6156 | -46.4851 | 2025-05-09 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b6317777-2d65-3530-80b4-e504dbb312cf | -23.6121 | -49.0181 | 2025-05-09 14:30:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a305c026-1970-3f66-937f-f89a924a28d2 | -18.2636 | -53.0096 | 2025-05-09 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 9444c64d-cd8f-3d59-9565-10be4d36ee3d | -12.653 | -54.0622 | 2025-05-09 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 04f92288-554f-3254-b26b-3c30ef2c37fc | -18.284 | -52.9848 | 2025-05-09 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f4fe8414-0c80-3eeb-8082-474f36e6574d | -12.6339 | -54.0642 | 2025-05-09 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 3b5c670c-8382-3272-8507-4004c2eb96e9 | -18.2836 | -53.0064 | 2025-05-09 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0f77eab0-1825-3f11-9adc-ffc5b5ad9500 | -11.9557 | -49.6862 | 2025-05-09 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9c838d7a-66f9-3b3f-a9d2-4e30392a48ba | -10.5502 | -49.7392 | 2025-05-09 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 05158256-76ab-3b7c-8502-cca33425c760 | -10.5692 | -49.7372 | 2025-05-09 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 6daca3ec-46e2-3b95-87f0-3b275a1671e9 | -12.653 | -54.0622 | 2025-05-09 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 16153d3e-f1a9-3a6d-b7e3-d05a03174518 | -13.3752 | -54.2538 | 2025-05-09 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2ef38d1c-019f-35ae-a953-1f02b210ce13 | -6.9615 | -42.7872 | 2025-05-09 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 4c91107b-05bd-3d3d-9ca5-f8cc00eaa7fc | -12.6339 | -54.0642 | 2025-05-09 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 0efe8a4a-9660-3fa2-ad28-a021b358dcb3 | -8.07 | -43.1216 | 2025-05-09 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |


