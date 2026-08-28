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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fc9b740-8b4b-3e3c-8521-c82f67884604 | -9.45252 | -60.53163 | 2026-08-28 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b95fce45-fda0-300c-b0a7-0fe49026a3bc | -7.6056 | -61.34796 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33ed09fd-d053-3dbe-921b-77ae36430713 | -9.24027 | -57.07558 | 2026-08-28 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec50ec00-66ef-3ce1-b9c0-6aba709f69f1 | 0.29974 | -60.44929 | 2026-08-28 05:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2455bdce-ff9f-367e-90df-ce807fc780c0 | -10.39136 | -61.23226 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c736fc4e-2b6d-34ee-81df-846c5918fd2b | -7.61249 | -61.33326 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e7665de-edb0-321a-83a0-ebb16b2ccf80 | -10.39022 | -61.2412 | 2026-08-28 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9899c475-96a7-35c0-bcfe-c6aff26ab20f | -10.50262 | -64.51041 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6ba57a48-c9d5-3919-b270-94e12ea6c3d7 | -1.36463 | -54.63126 | 2026-08-28 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9facc29-ebd1-364c-96ff-28f3cddaeea3 | -9.0001 | -65.4321 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5b8c2f3-9ce5-3ac3-9de2-cda6ce21232a | -8.99068 | -65.44442 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5a7b6c0-d83b-35bf-8af1-f80b0f680a8f | -9.20901 | -65.79037 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fbe0cdc-d4f8-38bc-ac7e-942d6f22d6e9 | -8.55139 | -70.60172 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a26741b1-7d02-33ce-a3d9-fa57dda334f3 | -9.17602 | -70.89659 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 250871a1-98f3-3dd1-9caa-6f3b3bf90617 | -6.24508 | -55.47005 | 2026-08-28 05:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed14ce42-2e7f-3cf5-8913-8b1f473c2d8d | -1.36614 | -54.63702 | 2026-08-28 05:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cea9ca5-05b7-332f-9ef7-bc64706f4091 | -6.15589 | -57.79358 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 291ab164-fcf4-3629-a5f9-6d3f386e074d | -9.25314 | -57.07773 | 2026-08-28 05:55:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d16b746-e143-30c8-afa0-2d9eaaa607e9 | -8.15399 | -64.00345 | 2026-08-28 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ead0522e-932c-37dd-a11d-986c92e2763d | -10.33652 | -64.47559 | 2026-08-28 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d555566-a838-37eb-afa6-178d1d171f82 | -7.58722 | -61.33999 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462860f1-a618-3657-a2cd-8dc6723e4aff | -8.27861 | -70.88168 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a97fce60-cf2f-38b3-aad9-ee7f15fd1f83 | -7.58455 | -61.32381 | 2026-08-28 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8423e254-7b3c-3ab5-9e71-df43632a8fc0 | -8.99944 | -65.43659 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e38727fa-79db-35b4-a933-9bbfabea1b63 | -8.39264 | -70.74068 | 2026-08-28 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d83d9c9f-64d3-31aa-a02a-6bf3452f8b87 | -8.60349 | -70.20833 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47f6b55f-7232-3809-9a6e-05f41ca97ba5 | -8.27126 | -70.09311 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abbb6133-1294-376d-8495-af43be338ef8 | -8.99571 | -65.43604 | 2026-08-28 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5504bfb1-a328-3c06-ac50-4e903bc8de56 | -6.75814 | -55.6911 | 2026-08-28 05:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c72feefe-b056-38a0-b411-cd4e44d8a97b | -6.16715 | -57.7998 | 2026-08-28 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 169ef9aa-c0fd-3cd2-8dac-f0db8111118b | -7.71958 | -70.09594 | 2026-08-28 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9a2ceb0-061a-3389-9717-67760f720b30 | -8.2707 | -70.09666 | 2026-08-28 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fee0b7dc-80cb-3628-9307-7f50195c3bb9 | -16.17289 | -58.58197 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a20dc507-0291-3006-b6de-c0606cd9a106 | -16.15206 | -58.59648 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 8406a1e3-0ed7-3aaa-a5aa-fd371c9ac3d3 | -16.1526 | -58.591 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.3 |
| 40cc4846-1b3d-34b6-8695-152ed204e9a2 | -16.16487 | -58.59766 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 739f0e16-2c48-38d4-a0b4-eafaa7f44570 | -16.1601 | -58.58048 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.4 |
| 8a8359ec-115c-3dd5-bd07-77235e5538ee | -16.159 | -58.59163 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 5b3b5b6f-4ff2-36bd-8437-bef1dde3eff3 | -14.89434 | -56.33057 | 2026-08-28 05:57:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eec6e7d4-61f7-31ac-9c89-b43bc5b2d01c | -16.16704 | -58.57578 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| df29279d-ec91-3ddf-a7c5-be6a52b0ba86 | -16.17235 | -58.58744 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5149894c-f09c-3045-8ffa-1aa0bc758ce3 | -16.1665 | -58.58121 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.4 |
| 26624552-0583-3358-a1db-bce977ca4c61 | -16.16065 | -58.57499 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 444d4560-7d99-3126-8a6d-d5a12115eb37 | -16.1654 | -58.59224 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| b20f12f2-1dc7-3626-8002-9d2afce6995c | -12.90033 | -59.90298 | 2026-08-28 05:57:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c85fa6e-34cd-3384-bce9-86bab308e019 | -16.15954 | -58.58615 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.4 |
| 875847f6-ecdf-33e3-820d-77604a9b7003 | -16.15152 | -58.60187 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 9f6e9bed-6e03-34a1-80ba-418b4fd4ee09 | -12.90644 | -59.89979 | 2026-08-28 05:57:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebba22bf-cbae-37da-b64e-7a25f4369e29 | -16.15846 | -58.59705 | 2026-08-28 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| b5ceec0e-b4b4-3c1e-a9af-db5c261a1313 | -12.91866 | -59.89352 | 2026-08-28 05:57:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 321ba0eb-6c79-3c8d-9822-77dcf5b51afa | -10.498 | -64.5193 | 2026-08-28 06:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 93c3358e-55c7-31b2-b86c-5742d1254001 | -6.1657 | -57.7793 | 2026-08-28 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 94fc0e56-f7e5-304c-9189-c48c61bba0cf | -10.9556 | -50.5311 | 2026-08-28 06:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4eef8585-d800-3fe7-89f4-77b71203f568 | -10.5166 | -64.5186 | 2026-08-28 06:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d0c60694-e72f-30cf-a496-6498c5e57156 | -10.9367 | -50.5332 | 2026-08-28 06:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| d91c9ea3-5d08-3f6e-b62f-c7aed050d194 | -7.2659 | -45.8668 | 2026-08-28 06:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| d1710730-95ba-3542-8646-1ddafd05b4c1 | -16.1638 | -58.6053 | 2026-08-28 06:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 268.6 |
| f0c60981-b635-341f-9536-191ae8371a97 | -16.1444 | -58.6073 | 2026-08-28 06:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 1139f13c-cce8-3fe3-bfdc-4b19c62bd0d0 | -10.4981 | -64.5005 | 2026-08-28 06:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 54a294be-1e23-3df2-a958-0cbb1cfb166b | -10.899 | -50.5159 | 2026-08-28 06:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 27816935-8d6b-3fc4-9bb0-54f029abcb25 | -6.1472 | -57.7995 | 2026-08-28 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| d6707d16-6894-36ca-a0a7-e978cc7aa2f5 | -16.1836 | -58.5831 | 2026-08-28 06:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 217.7 |
| f66292a3-b76f-30dd-97b2-458c7ab7592a | -16.1641 | -58.5851 | 2026-08-28 06:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 430.5 |
| a89ee038-254b-3215-9cfd-a4b638d89e43 | -16.1833 | -58.6033 | 2026-08-28 06:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 5adf6f47-157f-36c2-8355-37e8fbc84217 | -6.1656 | -57.7988 | 2026-08-28 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9cd7a341-b521-38dd-9e11-e272c6ebe213 | -10.9177 | -50.5352 | 2026-08-28 06:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| bc9c7c84-1249-30f1-af12-18a36081ed34 | -16.1447 | -58.5871 | 2026-08-28 06:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 01f07aaa-40d6-346b-8092-34c27e3656cd | -6.1657 | -57.7793 | 2026-08-28 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f6fb7d64-d152-3f73-ae90-2a231c85c108 | -10.8028 | -50.6326 | 2026-08-28 06:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 9631565d-7eeb-3903-bf9c-bda9e4909947 | -6.1656 | -57.7988 | 2026-08-28 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| bce9baf7-a84a-34be-ba82-8025e27b2bbd | -16.1641 | -58.5851 | 2026-08-28 06:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 6e12e435-58fa-3416-a90e-8fe04f4e6bf9 | -16.1638 | -58.6053 | 2026-08-28 06:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 0ee6c0a3-b2dc-3037-832f-b4c7c6465fab | -7.2471 | -45.8685 | 2026-08-28 06:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ee08aa5d-f81b-39e7-93c1-f0d2788b9ddd | -10.5166 | -64.5186 | 2026-08-28 06:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0fa12d3b-0a40-354f-a53c-240f3e7aa5d9 | -10.4981 | -64.5005 | 2026-08-28 06:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 49fc42ca-7314-3dc2-8590-03bcc6fa6e40 | -10.498 | -64.5193 | 2026-08-28 06:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4e2617b0-150e-3593-b7b1-2984d20cfe00 | -10.7839 | -50.6346 | 2026-08-28 06:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 0033bb92-c970-3ec6-b0e9-24d57d6604c2 | -10.899 | -50.5159 | 2026-08-28 06:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 7cdcea38-d24e-3568-a8d0-6031e148f1cb | -10.9367 | -50.5332 | 2026-08-28 06:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 4dd76442-5cd0-3d81-a539-22cd519b8ed7 | -16.17 | -58.59 | 2026-08-28 06:15:00 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df3d1463-f208-3a93-9f44-c31c0a59c767 | -7.2471 | -45.8685 | 2026-08-28 06:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| dadbea65-ea64-3dd2-acc9-3f39fde005eb | -10.937 | -50.5118 | 2026-08-28 06:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f7db55da-5b1b-351e-a325-0c6a5f3bc073 | -16.1638 | -58.6053 | 2026-08-28 06:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 39314b5b-5674-3b63-a82c-7face242146e | -10.498 | -64.5193 | 2026-08-28 06:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| de2a087a-f074-38bb-853f-d0716216cb40 | -10.9177 | -50.5352 | 2026-08-28 06:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1bdfd3e9-b5d6-3981-bc54-a90d8f1ed616 | -10.7839 | -50.6346 | 2026-08-28 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7c9a4c19-1a85-38db-bdc8-799438c5a4b2 | -10.5166 | -64.5186 | 2026-08-28 06:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a3707a33-a37e-3487-8953-b3c9a082f6aa | -10.9859 | -51.0807 | 2026-08-28 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 12eb91ff-8c49-38b6-8bc0-4f30b0610705 | -6.1472 | -57.7995 | 2026-08-28 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| d7e12cb8-d4ba-396c-8608-baabfde67f0b | -10.9367 | -50.5332 | 2026-08-28 06:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 98df6498-47af-37b8-8329-3fc10ad400ab | -10.9856 | -51.1019 | 2026-08-28 06:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5249c020-f204-30e6-a24a-32fd5b26a52a | -6.1657 | -57.7793 | 2026-08-28 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| c957bbb3-90e1-301a-94c6-dd0228d2f971 | -6.1656 | -57.7988 | 2026-08-28 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b1f25b38-0aa0-32cd-af68-ffaa9a3a280b | -16.1641 | -58.5851 | 2026-08-28 06:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.1 |
| 5481a11c-6aa2-3ab7-85ba-19ad5775fd9a | -10.4981 | -64.5005 | 2026-08-28 06:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9e4acc93-765e-3161-9c2f-b17d7f4cad2c | -6.1656 | -57.7988 | 2026-08-28 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 43f42a7f-50d9-3406-91d0-43edf56d4252 | -10.7839 | -50.6346 | 2026-08-28 06:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e3040050-9057-3a42-aebb-70729b1177ec | -10.498 | -64.5193 | 2026-08-28 06:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fa4e5e98-609a-3a21-a12b-7e065ba8194f | -10.9367 | -50.5332 | 2026-08-28 06:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c431fbf3-24d4-3783-8617-dffc3d37cefc | -6.1657 | -57.7793 | 2026-08-28 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |


[Clique aqui para ver as próximas entradas](README67.md)
