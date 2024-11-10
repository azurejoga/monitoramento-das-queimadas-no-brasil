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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 049a1029-d107-3e26-b29f-fdf80addfed8 | -5.561 | -43.9544 | 2024-11-10 14:10:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| cee89b14-1286-3e46-806d-c2622ca0424f | -6.0096 | -46.1011 | 2024-11-10 14:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d44e20f5-c006-3ad2-b6bd-afc75cf647f0 | -5.15 | -41.6323 | 2024-11-10 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 3e870ee5-4901-3c5e-ae17-7d3a14866dda | -2.2876 | -46.483 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 300f844a-7e8e-3774-b27e-8a346c03be3d | -1.1672 | -52.0918 | 2024-11-10 14:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 456ed02f-7c19-3727-8b6b-35489295e9f5 | -3.9486 | -48.1291 | 2024-11-10 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| eb6137b8-40e5-335c-a64e-3f45d300fdf4 | -3.2521 | -46.4739 | 2024-11-10 14:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 16a42a62-5f08-3c6a-955b-14d817981ffa | -2.0656 | -46.3339 | 2024-11-10 14:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| d15221ff-aace-3e50-a021-3d1ec4cd95b0 | -2.3075 | -46.0836 | 2024-11-10 14:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 43aa88d6-d642-31dd-b296-c44e86c615ff | -2.455 | -46.3235 | 2024-11-10 14:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 27186292-da1e-36d5-990b-c380175c71d9 | -5.9101 | -42.6676 | 2024-11-10 14:10:00 | GOES-16 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 4942f644-1cf3-3a42-a0c9-2ee864737c7b | -1.7691 | -46.2963 | 2024-11-10 14:10:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 60044a18-317a-3060-a6df-e3db0d6989b1 | -8.7562 | -44.0965 | 2024-11-10 14:10:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 24cbd62f-4ed7-3487-9dd3-619eeef396ef | -1.5116 | -54.9944 | 2024-11-10 14:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 2625593c-e66d-36e9-8599-9d2bf4ae5238 | -2.0478 | -46.0903 | 2024-11-10 14:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c46c3997-fda9-3e5d-a6eb-d88b3c8de138 | -1.2352 | -56.1633 | 2024-11-10 14:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 80946d74-2e79-3eef-a884-aab66b74b3a2 | -8.7565 | -44.0733 | 2024-11-10 14:10:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b582a21a-6196-39c9-9d17-e5f4876eb55e | -3.272 | -42.528 | 2024-11-10 14:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 03cbf90f-eaff-3abd-be6d-434550b354e8 | -2.418 | -46.3024 | 2024-11-10 14:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| dde4564f-36ee-328b-bad8-e5238a45bb0f | -3.6701 | -44.7303 | 2024-11-10 14:10:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 139de706-1ae6-3cab-924c-865366d92ff6 | -4.5548 | -43.4889 | 2024-11-10 14:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4c170beb-df1d-38a1-a056-8ebbca466a3a | -3.8185 | -44.8369 | 2024-11-10 14:10:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e02b4dc4-221a-3b73-af0d-90a7e3be92b3 | -2.0293 | -46.0908 | 2024-11-10 14:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6ffe6934-5eac-3eae-91b2-151933c2d97a | -4.3978 | -41.9226 | 2024-11-10 14:10:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 25732c36-40af-3c1d-a1eb-b1aa1bd85af3 | -2.0954 | -48.8125 | 2024-11-10 14:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 866b98d9-98e7-3ca4-acfa-efdfe2354e50 | -5.7475 | -41.9927 | 2024-11-10 14:10:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 37f6303d-e4d1-342c-bb3f-66f07053f003 | -5.1126 | -41.611 | 2024-11-10 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 644c1d62-d3d1-34ff-97bb-2c58aac52bd4 | -3.7853 | -47.4629 | 2024-11-10 14:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 0953d349-6265-30f8-8e55-ae631d9ba557 | -5.5629 | -41.6486 | 2024-11-10 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 293b411a-fa09-3a0c-b820-0e7d94812c1c | -3.3909 | -44.72 | 2024-11-10 14:10:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 91d144c2-333d-3846-adbd-c7fff0a2bcc9 | -3.9671 | -48.1283 | 2024-11-10 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 48c0db6d-935f-3d2a-83b5-33d57aa71c4e | -16.679 | -55.5402 | 2024-11-10 14:10:00 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| c6e92f8c-2cd1-3ca9-8d8b-3073fe72fbd7 | -0.7284 | -49.4496 | 2024-11-10 14:10:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 188ad3cc-7d17-3e1a-947d-844d3cffc581 | -3.9483 | -48.1724 | 2024-11-10 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ce54538c-1dbf-3613-b5a1-8af62ac496a7 | -5.4689 | -41.656 | 2024-11-10 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 5c6be91c-cba5-3315-ac8d-7dc98220b113 | -23.9095 | -54.0606 | 2024-11-10 14:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 4ba36e6e-c8d7-3447-84e3-a9e013cde89b | -3.2721 | -42.5044 | 2024-11-10 14:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e572e77c-0371-3fc4-ba42-efe8c5b1ed6a | -5.4501 | -41.6575 | 2024-11-10 14:10:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| a7204bd1-72d7-3e7d-8180-38d3de44e840 | -1.4057 | -52.3553 | 2024-11-10 14:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0d48381b-a2e9-3cd9-a5e1-92c3f8f3429e | -2.4377 | -45.991 | 2024-11-10 14:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 38313d2c-5f46-36a2-8ba7-5982bda6ec61 | -2.4377 | -45.9687 | 2024-11-10 14:10:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3537f3f5-e9ad-3800-9b54-a7be89a7aa5e | -1.4009 | -55.4518 | 2024-11-10 14:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| afbfd83b-266e-31fc-81b5-1466e06cd026 | -3.9669 | -48.1716 | 2024-11-10 14:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 9f94ad9a-069a-3b82-ac7b-8b7b3d59eada | -17.2933 | -57.4857 | 2024-11-10 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 184.8 |
| 726ca27a-79a7-342c-ae28-a0f145f2b787 | -3.2533 | -42.5288 | 2024-11-10 14:10:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 79458c9f-9707-378a-9e4b-402adf2c63f7 | -3.8196 | -44.655 | 2024-11-10 14:20:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| def8c926-06c4-3ac8-85e4-1fd85193ff3f | -23.9095 | -54.0606 | 2024-11-10 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 101.6 |
| 7a79816c-ae28-33f5-8236-01753518c1ab | -0.3585 | -51.8921 | 2024-11-10 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ad3324d8-757a-3a83-bac5-105ec09817b5 | -2.1766 | -46.4196 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a979896d-45dd-3967-8a08-ce6039ea3952 | -5.7867 | -45.9603 | 2024-11-10 14:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 99f00aaa-0075-322a-8155-cfe95e7cb441 | -2.3443 | -46.1492 | 2024-11-10 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9ccec945-ff2d-3da4-92f6-7f3eed5f174d | -2.6388 | -46.7597 | 2024-11-10 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| fcc4e4e0-781d-32c9-93f2-3653c862a747 | -5.2996 | -46.2156 | 2024-11-10 14:20:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5eeee317-3d0a-3b36-88f6-c04f59bc969a | -2.1932 | -53.6226 | 2024-11-10 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1f7b5393-c767-30cf-a254-8bb2ee146db6 | -17.2933 | -57.4857 | 2024-11-10 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 204.7 |
| 5255870b-53cd-3089-8ee9-1c94d96620b8 | -5.9099 | -42.6912 | 2024-11-10 14:20:00 | GOES-16 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 31e95f95-16a4-3f7e-8491-1836c0146091 | -6.1363 | -42.578 | 2024-11-10 14:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 270.0 |
| 956599c2-2b69-37f4-985a-c3ecbdfeaf05 | -5.2994 | -46.2379 | 2024-11-10 14:20:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 07506784-e306-3b6b-9303-8882f2feff2b | -2.2691 | -46.4835 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3b18af08-dc41-3229-a3c2-ffeca33ad586 | -3.272 | -42.528 | 2024-11-10 14:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 2c43a00b-43e7-3b08-9443-c36b425c643f | -5.7473 | -42.0166 | 2024-11-10 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 2da82bf9-c500-3392-84ce-d1ae54fe745c | -4.3978 | -41.9226 | 2024-11-10 14:20:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 5abf71a5-bcca-36c2-93ce-f45815379edb | -5.1128 | -41.587 | 2024-11-10 14:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| d4ae017f-0e2c-3f8a-93c6-fa76284c0165 | -3.8185 | -44.8369 | 2024-11-10 14:20:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3b444b73-ec26-3674-97d2-c57bc034e852 | -5.5235 | -41.8434 | 2024-11-10 14:20:00 | GOES-16 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 21df502a-8afd-327c-8a6a-07902ce666e0 | -5.9919 | -45.9906 | 2024-11-10 14:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1ec2b809-ce35-308c-a7f1-c25164c10ab1 | -2.455 | -46.3235 | 2024-11-10 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| db7d30bb-8b3d-375a-8ed6-b51601dcae95 | -5.4099 | -46.4088 | 2024-11-10 14:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 69e2104a-cca9-385c-ba55-d43563b76c6f | -4.3059 | -44.379 | 2024-11-10 14:20:00 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2972db74-e08e-34f5-a408-4939fad473fe | -5.8836 | -41.5261 | 2024-11-10 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| b5fdb496-03fd-3af3-9f21-32c21888b287 | -2.3076 | -46.0391 | 2024-11-10 14:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4bc0bbe4-a999-37e4-aa94-e97f3fc368fd | -3.2534 | -42.5052 | 2024-11-10 14:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 372b487d-2db4-3eb8-92e7-2988335d9dc9 | -2.2095 | -47.733 | 2024-11-10 14:20:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 87cf8fcf-d14d-39db-b314-52ae40980b24 | -3.8371 | -44.836 | 2024-11-10 14:20:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 2e030516-7063-3069-b7ca-affc88014a09 | -5.7146 | -43.5261 | 2024-11-10 14:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 4eb91434-7526-37e6-b607-cb4b56f1aa90 | -2.6387 | -46.7817 | 2024-11-10 14:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 1571636e-8e95-37a6-b48c-f32460c02b11 | -2.0954 | -48.8125 | 2024-11-10 14:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 238.0 |
| 04ff19f4-a6cb-354d-ae6c-8c1732ca3a8c | -2.0664 | -46.0676 | 2024-11-10 14:20:00 | GOES-16 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 871443b9-987e-346f-857a-27dd7bc87b12 | -2.2509 | -46.3513 | 2024-11-10 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 02c3e1c2-a52a-3a94-826c-ccff054a4f0e | -2.0768 | -48.8342 | 2024-11-10 14:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ae319527-75f2-356d-8d64-a22dde0e0cc3 | -3.2721 | -42.5044 | 2024-11-10 14:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| cb44357c-2eee-3870-9dd5-f37cf75b4fc5 | -1.5116 | -54.9944 | 2024-11-10 14:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 356c9893-ca74-38a1-9c79-182221adbb19 | -3.6966 | -54.611 | 2024-11-10 14:20:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 89eb3888-b45b-3479-9402-d6307be989a3 | -6.2377 | -45.6809 | 2024-11-10 14:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c9a7672d-a36d-3850-b6da-dabbac92740d | -3.9485 | -48.1508 | 2024-11-10 14:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 1ed0f85a-94bf-38a5-b7d9-2b00d14d9b9f | -2.0842 | -46.3334 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 08c274da-f107-3d67-95ac-c565df532343 | -2.0064 | -47.5857 | 2024-11-10 14:20:00 | GOES-16 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8f222d70-c127-353d-9bbe-d8d273ec423a | -2.5118 | -46.011 | 2024-11-10 14:20:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 452d4891-2dd4-3cf8-acde-6c5002f422d2 | -3.9955 | -46.3981 | 2024-11-10 14:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| caea4cc2-1f59-3380-adfd-973addfaace2 | -1.9912 | -46.4241 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6b8f6775-2d57-331d-99c0-2f73e61ca4b5 | -5.9601 | -45.3635 | 2024-11-10 14:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c2069792-a2ac-3b9b-aa4a-753c5fcafef4 | -2.3256 | -46.2163 | 2024-11-10 14:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c2b71106-68c0-34da-b644-a0e5bd9d53f2 | -2.2876 | -46.483 | 2024-11-10 14:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f580aee7-b5be-3ae7-a02c-9ebcab03eea2 | -2.1562 | -53.7039 | 2024-11-10 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5238c110-d0b4-3340-86a6-269bf752f147 | -1.7691 | -46.2963 | 2024-11-10 14:20:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 24df14b2-15ea-3340-a3a4-39d4cfcb45f4 | -0.4503 | -52.0355 | 2024-11-10 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bc7ba76e-8a7d-3e28-af38-4492df86ccaa | -4.0913 | -49.1323 | 2024-11-10 14:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 9f1b3a06-c9af-3972-9d99-edeafaf91a02 | -2.1199 | -46.7739 | 2024-11-10 14:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7a478fa9-38d6-3998-81f3-4ea48062d395 | -5.1314 | -41.6096 | 2024-11-10 14:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| adb15ecd-1638-36c3-b975-8b6120b5fc07 | -5.1126 | -41.611 | 2024-11-10 14:20:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |


[Clique aqui para ver as próximas entradas](README133.md)
