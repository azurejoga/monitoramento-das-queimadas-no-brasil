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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e439944-fb63-34d3-9f65-8e02b5f60543 | -13.1747 | -47.7869 | 2025-10-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 0331e06b-2a3c-3adf-86c2-e4b10393b8aa | -11.825 | -44.9437 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 291.0 |
| 50a73202-8a1b-3655-b7ee-82f3df442425 | -11.8478 | -48.0816 | 2025-10-01 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| eb9b2c8b-35dc-3c68-a01f-59d4b63c1506 | -12.481 | -50.2476 | 2025-10-01 13:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 464.3 |
| e81f80ed-77aa-3b14-a5cd-d28b8717bcdf | -9.938 | -43.6718 | 2025-10-01 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 5b89a049-3583-3f73-940b-a31762b2c3d7 | -6.9427 | -41.1373 | 2025-10-01 13:10:00 | GOES-19 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| b252b551-6b62-3972-9810-87daacd186bb | -14.9733 | -46.8896 | 2025-10-01 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2790a43f-2565-3231-bef3-a3fa7c4132f8 | -8.5081 | -47.2676 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ff0cd797-3076-359a-a022-9e6aa8712577 | -8.8926 | -46.6296 | 2025-10-01 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 507.7 |
| 9e0aabd6-f931-30af-a9e3-7d0bf15e44d6 | -7.5559 | -46.8017 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ea347f2c-65f5-3b86-b1db-36e8205f2ad8 | -12.4813 | -50.2261 | 2025-10-01 13:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 253.2 |
| 2bd373cf-8bf0-3dc1-9a95-ecf60fd25e6f | -7.5749 | -46.7778 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 192.7 |
| d38562a6-c9d4-33b9-bb59-60801fdc347a | -13.6707 | -48.0476 | 2025-10-01 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 73869470-5fb3-3db3-806f-95b01f176683 | -8.6908 | -47.7126 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| e2f52778-773b-3f1c-b0e7-d0c6da48d246 | -11.9063 | -48.0076 | 2025-10-01 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 052563e6-1d57-3560-87df-1aa8d1b57ed2 | -10.1084 | -50.299 | 2025-10-01 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 770a64a5-5b90-3324-883d-ef8db971c277 | -7.4249 | -41.8601 | 2025-10-01 13:10:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 8826cc25-e825-3eae-939a-ee6b2200c006 | -8.483 | -47.7983 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| bf1c8a04-970c-3b7a-a174-4da083eee671 | -9.4115 | -47.3308 | 2025-10-01 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0e139982-053c-34a8-bfc2-e462af32b059 | -7.5561 | -46.7795 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| b5507929-b82b-3918-858f-c841dd19106e | -9.1248 | -47.6256 | 2025-10-01 13:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 828a615a-0448-3e7a-ae2c-5eb67da43325 | -8.672 | -47.7144 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7a87ba84-37be-30e6-a911-1f4a05c49733 | -12.2341 | -47.8309 | 2025-10-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bddbc1ac-b25a-3eb6-aa4f-b213419d3ad2 | -11.8254 | -44.9205 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 025c075a-18ce-3de4-80d7-c6b464b085a1 | -9.9186 | -43.6978 | 2025-10-01 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| b6fe43b8-39e9-3758-957b-956fc922702e | -7.1148 | -47.8068 | 2025-10-01 13:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 900a957a-87c0-3742-95d3-180c3e3ac693 | -7.8882 | -47.281 | 2025-10-01 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 08cbd8f6-ecb1-3d39-8d3a-b4601e599893 | -9.4557 | -45.4862 | 2025-10-01 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 664361ad-95ff-3eeb-a93a-b93f7c4becbd | -7.8738 | -45.2684 | 2025-10-01 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5d282719-8cef-361d-9078-b384812a23f0 | -8.8929 | -46.6072 | 2025-10-01 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 10a7447b-17ad-39da-83ee-343e8f70268e | -13.7868 | -48.03 | 2025-10-01 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8685cf61-2503-3519-a54a-3d6d0b4f7e38 | -13.0119 | -45.1988 | 2025-10-01 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 298.1 |
| e72d9408-e2fb-309e-9dad-036086ad0d97 | -9.9193 | -43.6508 | 2025-10-01 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 0a9f98c8-3893-3bdb-8118-81b73bdef8ce | -8.5267 | -47.2879 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 3216e97b-c57b-347c-92c0-d9a140509016 | -8.2105 | -47.0084 | 2025-10-01 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ecf94578-d358-367c-b15a-98970518bc1d | -9.9189 | -43.6743 | 2025-10-01 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 267.8 |
| d05fd96a-9ca7-331a-be46-b27550a65ae4 | -7.8405 | -48.2053 | 2025-10-01 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| ffdbad98-a760-3b4c-b700-3e5d54a9a476 | -9.9376 | -43.6953 | 2025-10-01 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| b232fcbc-81b6-3973-ac80-a6d0428a4471 | -8.9115 | -46.6276 | 2025-10-01 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 428.1 |
| 3f1247d1-0882-3b7d-b2ba-fb0ad4cbde2e | -13.3203 | -47.2048 | 2025-10-01 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 119.7 |
| d814143b-c1e9-31fc-901d-af96ecf1793b | -10.0906 | -50.2154 | 2025-10-01 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 90c3ae73-aba9-328b-a333-f519ad55a14e | -11.9411 | -47.0675 | 2025-10-01 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| bd9158ff-8b81-3e84-b4e9-f25dbe2ff71f | -9.4644 | -47.6124 | 2025-10-01 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 8bac6d98-d5cf-32bd-91f1-c2b70525623d | -11.7797 | -47.5806 | 2025-10-01 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 76a80e1a-2ae7-3d1a-a2be-0a2fe832d921 | -11.6126 | -45.0443 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 66bc2d39-29ec-3def-ac32-95bccccdbc30 | -12.2536 | -47.806 | 2025-10-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 394.1 |
| 20b86d86-3f23-31c3-9298-f0ab931399ca | -8.4833 | -47.7763 | 2025-10-01 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f71d0f9f-27ac-3f37-beac-44f065002088 | -13.7691 | -47.9435 | 2025-10-01 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1ce15575-eeae-3e4a-9b29-e2498a20020d | -9.6441 | -45.5552 | 2025-10-01 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 166.0 |
| f649d416-2868-39ab-ad89-d36d0c8d899d | -9.1434 | -47.6457 | 2025-10-01 13:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 88c72390-5225-39f8-9ae1-d03b34a47114 | -11.8622 | -45.0075 | 2025-10-01 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 7a0f3d56-0573-3348-83b6-a94f3af9e80a | -6.5546 | -43.9221 | 2025-10-01 13:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 17383b89-d8e8-35ec-adf3-77bdf77964d8 | -9.9391 | -43.6012 | 2025-10-01 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e1890ae2-e34d-3fcd-b9b1-6a6e45a724a5 | -6.943 | -41.113 | 2025-10-01 13:10:00 | GOES-19 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 3069c90a-26a2-33c9-9024-86be426ce2ad | -11.829 | -48.0619 | 2025-10-01 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ee79574f-a051-3139-892b-483117eb08fd | -11.6126 | -45.0443 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| f85135ae-f17d-32ab-b5f0-78a043c5a642 | -9.4458 | -47.5923 | 2025-10-01 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 1aa80942-3143-3fbc-8aaa-d77bd522be2a | -14.9079 | -47.2193 | 2025-10-01 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3f56eb6a-689b-3426-98eb-f6134560aed7 | -13.3203 | -47.2048 | 2025-10-01 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 54bfa4f7-3c8d-3216-9269-e623ca0098d6 | -10.0909 | -50.194 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b029e643-0881-3d07-9004-eab6a73b859f | -14.1732 | -46.1124 | 2025-10-01 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 06a8589d-3fe6-35cc-b911-beef7aa45b63 | -8.163 | -46.2554 | 2025-10-01 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 540d0d8f-7528-317d-8d5b-de59eb76adcb | -9.1889 | -48.5166 | 2025-10-01 13:20:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1e3a78d2-673a-320b-a41c-859c98a1357a | -8.5404 | -44.6975 | 2025-10-01 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| abcc9ff7-b607-33b7-9cbb-f38e09d6a354 | -13.3278 | -47.8313 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 06d53df1-5e9b-3f04-b73f-c23fc9a85633 | -5.9555 | -45.8812 | 2025-10-01 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 265.5 |
| a9b542b8-dd14-3055-a237-ef05ea93849c | -11.4592 | -45.0664 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 80883c52-536c-32c8-b5c8-b8c2535328f0 | -8.6911 | -47.6906 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 246c8f80-272b-39c6-bfd4-a3922256b46b | -7.5561 | -46.7795 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 202.4 |
| e30aa9ac-1972-35b1-8d26-0257671d6bb2 | -14.8026 | -45.7713 | 2025-10-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 95837145-1496-313d-b0da-8d9de1d95e8b | -7.1148 | -47.8068 | 2025-10-01 13:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e3822499-07c4-3495-9ddb-450991e501ae | -16.0221 | -50.8989 | 2025-10-01 13:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0024b00f-0e21-31f8-8512-22a8174c9b01 | -7.5746 | -46.8 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 219242ac-60da-36dd-95b6-b0a5fefdfd02 | -10.0712 | -50.26 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a40019bd-a672-3833-9ff2-a86593c7b838 | -13.3414 | -48.1411 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 57e8f8cc-9ccc-32fe-8e73-c54379ce08bf | -11.825 | -44.9437 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 4a3425da-435e-3c56-a368-6a031df748f6 | -13.816 | -47.5107 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f29d0c08-ec2c-3608-87ce-ec74a362f365 | -12.4622 | -50.2284 | 2025-10-01 13:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 198.3 |
| ca8a7ab2-c53a-3fd6-ba9f-1762cd67851f | -10.8433 | -45.3815 | 2025-10-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| ca1758ee-c422-35d7-8ab0-8b52f99b428f | -7.5749 | -46.7778 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 5219c57f-5263-3a39-8aa1-6aacda6e8d80 | -15.9388 | -43.2979 | 2025-10-01 13:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 373.6 |
| 4431e996-22b6-3ea3-ba7b-8cc3708a7c89 | -10.1092 | -50.2349 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c8b2b3e8-a0bd-3d3c-a507-52720f976b3e | -14.7965 | -46.9658 | 2025-10-01 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 920c35dd-9bac-3b37-90c0-7d3b59843ab0 | -13.2969 | -50.6821 | 2025-10-01 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 3838972a-a9a0-3f21-a014-2c17c4ee534d | -8.5587 | -44.7414 | 2025-10-01 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 466b4b7b-e717-3e0f-bb03-b2311273c667 | -9.9376 | -43.6953 | 2025-10-01 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 1fe4fc90-afc7-32ee-bfd2-aae1a9ee9850 | -13.7695 | -47.9211 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0432aa32-021a-3599-9711-314a8fec1f18 | -13.0119 | -45.1988 | 2025-10-01 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 78946853-62f8-3307-bb67-23231ab50007 | -10.1084 | -50.299 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 161.3 |
| df7daad4-d6d8-3013-b0c5-15abde8360b0 | -12.7002 | -48.5637 | 2025-10-01 13:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 52e7913f-49e6-3220-895b-926fa50afcb9 | -8.483 | -47.7983 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 215.0 |
| cfa8e1b3-9827-3168-b4c5-bedbc41fa550 | -8.672 | -47.7144 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6bcb6fa4-76ca-397a-82e7-9e5572c6bdb1 | -12.2344 | -47.8086 | 2025-10-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| a77728bd-d174-3faf-b92b-6fee3104da1e | -11.46 | -45.0202 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 7794d6e4-fcac-3cc2-9646-faf661659969 | -9.9189 | -43.6743 | 2025-10-01 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 351.9 |
| 35404e64-0973-3f0e-bf85-35d27dd5f29a | -7.5559 | -46.8017 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0ae0f802-2071-3f0d-a046-6cdb79ec068d | -7.8882 | -47.281 | 2025-10-01 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 04272a23-c303-368f-a296-9eca8376f0e9 | -11.1178 | -49.7845 | 2025-10-01 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c40a75eb-bc25-3447-afa5-c6b864ab2ed2 | -10.0903 | -50.2368 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e230bbcc-3f5f-315d-9a0e-d690207b0ff2 | -8.5079 | -47.2897 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |


[Clique aqui para ver as próximas entradas](README153.md)
