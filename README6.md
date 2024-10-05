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
| b5c0ad27-82ca-3872-84c6-8e167376b163 | -14.0341 | -46.370998 | 2024-10-05 00:21:43 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0efffd33-b14e-3306-b967-b0dc8652e859 | -14.5535 | -49.289501 | 2024-10-05 00:21:44 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2334477d-58b0-38ca-95ad-504098884cec | -14.5402 | -49.272499 | 2024-10-05 00:21:44 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c4c3734c-61fc-3824-842d-052f59b43e6f | -14.5437 | -49.291302 | 2024-10-05 00:21:44 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57436b01-c6b2-3552-8c4e-6d36e08632b2 | -14.2751 | -48.151699 | 2024-10-05 00:21:45 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1e5c13ac-f761-3f87-b8d7-c065fcb70e5b | -14.2781 | -48.1674 | 2024-10-05 00:21:45 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd696fe0-49bb-3c03-b3ff-1e5c74435249 | -14.2654 | -48.153702 | 2024-10-05 00:21:45 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77646328-3065-3247-b541-01f830dd8c39 | -13.1557 | -44.058701 | 2024-10-05 00:21:49 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da2f3090-0f60-37ac-a309-18d3b02a0d97 | -13.1575 | -44.067101 | 2024-10-05 00:21:49 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7fd7d7b-21b5-3997-a82a-1cca3a1755d5 | -12.8739 | -44.6119 | 2024-10-05 00:21:56 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| abf504e1-adc9-3450-8835-1a5f2ce3092d | -12.8758 | -44.620899 | 2024-10-05 00:21:56 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0138ba7-7846-3e33-b8be-4c5fbcc17b70 | -13.1174 | -46.319599 | 2024-10-05 00:21:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46a29671-1813-37f7-8d44-fe295bc74c92 | -13.1052 | -46.310299 | 2024-10-05 00:21:58 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a986718e-a3bd-3bf1-abcd-8c56c82a6dcb | -13.1076 | -46.321701 | 2024-10-05 00:21:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3626ad36-a481-3d5e-b52c-9b7567f5a1ed | -13.1099 | -46.333099 | 2024-10-05 00:21:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5aebf725-f1f8-3c8f-9621-55ed9f08d870 | -13.1002 | -46.335098 | 2024-10-05 00:21:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6d877acb-097b-32e3-bfdb-8cd2953c0649 | -13.1025 | -46.346401 | 2024-10-05 00:21:58 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff052fb8-5a72-3576-881a-7b4514096174 | -11.6803 | -40.5956 | 2024-10-05 00:22:01 | METOP-C | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 34c5211c-5b89-31c4-b1db-f97a0bee3a40 | -11.6771 | -40.5816 | 2024-10-05 00:22:01 | METOP-C | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3979b614-5e00-3f8d-ba2d-80870ed72a9e | -11.6787 | -40.5886 | 2024-10-05 00:22:01 | METOP-C | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a0a84551-a9e4-3d64-8705-e443d9f43862 | -10.7025 | -37.058201 | 2024-10-05 00:22:03 | METOP-C | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 25796070-4e95-3e52-83f7-cb820f734533 | -13.1786 | -48.6506 | 2024-10-05 00:22:04 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 606b9ede-2a07-38ab-bb1f-2c643ef24cc9 | -11.2005 | -39.900398 | 2024-10-05 00:22:06 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab399f90-0471-3294-9929-d6a8c79cab12 | -11.2021 | -39.9076 | 2024-10-05 00:22:06 | METOP-C | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 75fec4fc-ecc8-3c19-b054-df2bca8bebf0 | -13.6013 | -51.234798 | 2024-10-05 00:22:06 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55f3fc00-54c2-372a-82a8-60fe829e3647 | -11.7499 | -42.923302 | 2024-10-05 00:22:08 | METOP-C | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2cf23690-87f0-3d08-8072-70b14060ff32 | -11.7515 | -42.930698 | 2024-10-05 00:22:08 | METOP-C | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 435b2814-ee0f-3534-aa42-be47bc2c98c9 | -12.2313 | -45.638901 | 2024-10-05 00:22:10 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c767817-c0ad-3dbb-8af3-31c1e83a12bf | -12.2215 | -45.6409 | 2024-10-05 00:22:10 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b32f146e-ed32-30c5-9fd0-a75bf63c83b6 | -12.2565 | -45.954201 | 2024-10-05 00:22:11 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8d029f-8947-314d-9b2a-9204f471c53f | -12.2586 | -45.964699 | 2024-10-05 00:22:11 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18f3d668-b2d4-318d-a738-32a6429cfcc7 | -12.2608 | -45.975201 | 2024-10-05 00:22:11 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4332048-a05e-3412-96cc-277513c6b940 | -13.1338 | -51.1455 | 2024-10-05 00:22:13 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6eabfb46-8249-3dfe-ba62-10c9f91476f3 | -13.1383 | -51.169601 | 2024-10-05 00:22:13 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9259d69e-cd37-3c8a-a3cf-3341952097fc | -13.1429 | -51.193901 | 2024-10-05 00:22:13 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a69f04e7-d9d7-3be5-8d56-8648ea6231cc | -13.1196 | -51.123402 | 2024-10-05 00:22:13 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8b3df83-fa30-32f4-9985-d110c0588bdd | -13.1241 | -51.1474 | 2024-10-05 00:22:13 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2be47743-a9dd-381c-a1aa-fac33f650e07 | -13.1286 | -51.171501 | 2024-10-05 00:22:13 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbab77cf-c4c2-3058-afe3-e50b0424b35f | -11.7538 | -44.641399 | 2024-10-05 00:22:14 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1caeccb1-9a61-34a3-839c-79a60769bd9d | -11.7557 | -44.650101 | 2024-10-05 00:22:14 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd2980e-12a2-38bf-9514-1d555ba7217f | -12.9846 | -51.0994 | 2024-10-05 00:22:15 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d9e6458-317f-3f80-a267-ee95d90a187c | -12.8051 | -50.523899 | 2024-10-05 00:22:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fddadf0a-88ea-30a3-bbf8-61c355dc2852 | -12.8092 | -50.545502 | 2024-10-05 00:22:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec7ef16f-2cf1-3b92-aaab-3f9121857cef | -12.7954 | -50.5257 | 2024-10-05 00:22:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35bd1d66-81ff-3eb3-9ac3-99793b0ff72f | -12.7995 | -50.547298 | 2024-10-05 00:22:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfa6276b-7b84-3c77-bc96-4f60d89ce09f | -12.7566 | -50.533199 | 2024-10-05 00:22:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04afdb14-bf4d-3931-84db-ca98020ff685 | -12.7607 | -50.554798 | 2024-10-05 00:22:17 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc720415-f41c-3493-95c3-e021947f975d | -11.2097 | -43.317699 | 2024-10-05 00:22:18 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e2975e67-c535-38d4-ba1e-ca9748152382 | -11.2114 | -43.325199 | 2024-10-05 00:22:18 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 83b83d99-9572-3ea9-9f1d-6e8ca2af6e4c | -12.7468 | -50.535 | 2024-10-05 00:22:18 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f897c8b-fa01-3162-9fb8-9038c37580cd | -12.751 | -50.556599 | 2024-10-05 00:22:18 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25afcbe1-3d20-35de-8431-ca262d736e1b | -12.044 | -47.3433 | 2024-10-05 00:22:19 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6715baa-47e3-3460-84d3-3e9cb31e2634 | -12.0466 | -47.355999 | 2024-10-05 00:22:19 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e46b62b3-1223-3849-90e0-7f5d7eb8eac7 | -12.0342 | -47.345299 | 2024-10-05 00:22:19 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38477740-7c32-305e-86f4-fd40774c1bdc | -12.0368 | -47.358002 | 2024-10-05 00:22:19 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| feb3350f-3ba2-321a-ae78-83d3adc7298a | -10.8374 | -42.8424 | 2024-10-05 00:22:23 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7123cc76-c35e-3793-917b-34e3c315e78e | -10.839 | -42.849701 | 2024-10-05 00:22:23 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71a4b7a2-41ce-35f6-bd10-a04db39e0158 | -10.8276 | -42.844601 | 2024-10-05 00:22:23 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1ad566e-85f9-37a9-9557-453957e1ec30 | -10.8292 | -42.851898 | 2024-10-05 00:22:23 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2a63693-19f5-3472-82b6-53b1a6753f6c | -10.9797 | -44.426899 | 2024-10-05 00:22:26 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03e9f0d0-74e0-3676-97b5-169be17b5621 | -10.9816 | -44.435299 | 2024-10-05 00:22:26 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab77a597-1d48-3ae7-90b1-b950ccb15973 | -11.7062 | -47.7808 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bf1f272-98cd-3b41-b3dd-10aa60929a7f | -11.709 | -47.794201 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4022681-8b78-34c3-9dea-33bb1add0ddc | -11.7118 | -47.807701 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42bcfdb7-456a-39f5-a756-e12c8dbae19e | -11.6964 | -47.782799 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1fbd9e7-fb62-361a-90cf-f2d5adceace7 | -11.6992 | -47.7962 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2e0abb5-1a0f-3bf4-91b5-e8990ed27a7b | -11.702 | -47.8097 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96e73b4f-8e2d-3931-886b-a23a4fcc6731 | -11.6894 | -47.798199 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 464d9f61-7655-3ec2-bf76-63fc4703f0ce | -11.6922 | -47.811699 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc27a3d9-1d2a-3b38-857d-88433dcbd3dc | -11.6769 | -47.786701 | 2024-10-05 00:22:26 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3926c568-160d-37b9-85cc-1396edff0838 | -12.6068 | -53.043598 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b877ab4-dbf4-3b06-a1e9-c1e6d3994429 | -12.6127 | -53.0755 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6da5250f-1306-36b3-ac42-66c791771266 | -12.6186 | -53.1077 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcdc779-a1b5-3115-98fe-2e5f0284a7c2 | -12.5972 | -53.0453 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d0946dc-6150-3275-93a0-b8b64875fba8 | -12.6031 | -53.077301 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40086fb3-56a1-32a5-92e4-8dff42c40aae | -12.609 | -53.109402 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89fed62b-e9cb-3d28-a2d4-fd3e2a38b076 | -12.5876 | -53.0471 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67de699b-b27c-3994-8aab-0dc2f75f0104 | -12.5934 | -53.079102 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc6cc66-fe77-37b2-8a52-d73fc038022b | -12.5993 | -53.111198 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7946daa0-812c-3aee-8ecf-bb4a68ebb8c7 | -12.578 | -53.048801 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9717c3c6-23bc-3007-9229-d798c7f861b6 | -12.5838 | -53.080799 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e22ca2c5-14d4-3c2e-9933-a7f484c20c16 | -12.5897 | -53.1129 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 064f2910-c81c-3351-8766-dc6072b7cb87 | -12.5741 | -53.0826 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 666f0e2c-077c-3808-b6d6-208d2bc1f41b | -12.58 | -53.1147 | 2024-10-05 00:22:28 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94cbeba5-80e5-38f9-b5e2-c01c4753b9cb | -11.9268 | -50.098202 | 2024-10-05 00:22:30 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9042972-f8ab-35bb-baa0-0ff8bf50c44b | -11.9171 | -50.100101 | 2024-10-05 00:22:30 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 323f74d2-0c0d-368d-ae72-ac2bf8172ea1 | -11.921 | -50.119701 | 2024-10-05 00:22:30 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca0295ca-76cd-39d2-a1eb-2766ee16451d | -10.867 | -45.474201 | 2024-10-05 00:22:32 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7f6f60a-0169-3a30-9a39-516e834ab1d3 | -10.8143 | -45.514999 | 2024-10-05 00:22:33 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70297972-d8cc-36b4-bb33-796cc2da483a | -10.8088 | -45.5853 | 2024-10-05 00:22:33 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d6ebb0a-a693-3d48-ba1e-e8fed8e72d76 | -10.8109 | -45.594799 | 2024-10-05 00:22:33 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4bef6aca-2813-3c6f-9109-c05a9f612941 | -10.7305 | -45.602001 | 2024-10-05 00:22:34 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46e4ec0d-46d2-3b61-a033-aa265bb6e2ce | -10.7326 | -45.6115 | 2024-10-05 00:22:34 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 791c35b8-a39b-3c2d-b1fa-114618e3c251 | -10.9146 | -46.663399 | 2024-10-05 00:22:35 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0991f9d-8fd5-379f-9d7c-2799fd37db07 | -10.9024 | -46.6544 | 2024-10-05 00:22:35 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00842235-c858-3115-91c1-c2f85e4c786a | -10.9048 | -46.665501 | 2024-10-05 00:22:35 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83db1477-c7a3-32c6-a0f1-c1f9b81cf8f0 | -10.8811 | -46.601398 | 2024-10-05 00:22:35 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 055024fd-723b-37b1-8d42-2d636acd8f31 | -9.4613 | -40.366699 | 2024-10-05 00:22:36 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 21e39e1c-7c54-38c9-96b0-0d28383da8c8 | -9.463 | -40.373798 | 2024-10-05 00:22:36 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| af571e1c-2eb5-36b6-bc1f-f9400b6bc435 | -10.7503 | -46.175201 | 2024-10-05 00:22:36 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
