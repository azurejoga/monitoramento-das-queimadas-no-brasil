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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e4d6e2e-71de-3dc6-a991-c42041689966 | -4.4061 | -43.3816 | 2025-10-17 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 3cf8a764-68c4-3255-a669-9a471c26b7fe | -10.5132 | -43.4289 | 2025-10-17 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| a5bf530b-20a9-3a6e-8bd1-e1787c5b7b7a | -10.4945 | -43.4079 | 2025-10-17 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| e367ef39-3976-3f49-90b2-94ffbde47883 | -4.4058 | -43.4282 | 2025-10-17 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 8ecd0020-bdff-3d3c-8f3d-96aed43ab242 | -4.4248 | -43.3805 | 2025-10-17 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9bbda749-ad2c-36c1-8c01-ac51dfc19821 | -10.5136 | -43.4052 | 2025-10-17 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 74f658a4-d552-3b66-bde8-add3ae330e08 | -4.4059 | -43.4049 | 2025-10-17 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 333.7 |
| 07770e79-d161-3d61-ac82-70ae2f8fc30d | -3.2359 | -45.9862 | 2025-10-17 01:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 323.5 |
| 91e520b2-7e1d-3a6a-9086-5031c158cf4c | -4.3872 | -43.406 | 2025-10-17 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| a48b9698-b7a7-3749-827b-b2b2dba25b6c | -2.7585 | -49.3922 | 2025-10-17 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3cd4f0fd-65f5-3ac7-ba4f-97894373ed6a | -3.236 | -45.9639 | 2025-10-17 01:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 524.1 |
| a0d88073-08ec-380c-a95d-13268c97d6e8 | -3.5212 | -52.4932 | 2025-10-17 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| b3c94d87-bba2-3f1f-b655-de9ad9b1763c | -11.5733 | -48.5568 | 2025-10-17 01:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b56d7d98-745e-353a-8bc4-95ddfea14aee | -12.9175 | -47.1303 | 2025-10-17 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8c1737f1-ddb5-3010-b133-b4c8d6b8ef0e | -4.4246 | -43.4038 | 2025-10-17 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 9df412a3-0f22-3012-bf0e-db4b16d8fbf3 | -4.9548 | -44.956 | 2025-10-17 01:10:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| dd67579f-f97d-31da-ba9b-4a2ea2598af6 | -10.2935 | -44.0455 | 2025-10-17 01:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| fe3d985a-fdef-3787-9abe-3ca70a267cdb | -10.5831 | -47.4423 | 2025-10-17 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 444c7f6a-2c12-3f2c-82d2-6cf2de23babb | -3.5028 | -52.4734 | 2025-10-17 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e959ebd0-3743-36a8-b6f7-de90ed2968d6 | -9.1378 | -46.6261 | 2025-10-17 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 53240003-c30d-337f-a557-9fae7d357d0b | -9.0821 | -48.0252 | 2025-10-17 01:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 91f10e54-8adc-3ad2-8894-d388346c5eef | -10.2939 | -44.0221 | 2025-10-17 01:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 856c8128-31a6-33bb-975d-1d42592dc738 | -10.5128 | -43.4525 | 2025-10-17 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| f4524e11-bd4c-32f3-bb6d-8de69ddf2090 | -9.879 | -47.6779 | 2025-10-17 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 5c05eba9-2fe7-3b9e-99f1-e5261ad22bcd | -10.2745 | -44.0481 | 2025-10-17 01:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 3ee16909-bb5c-3675-87fe-0ed9e015b7a9 | -10.4941 | -43.4315 | 2025-10-17 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 61330ff0-a8dd-360a-9702-f89bac8a72d5 | -11.4939 | -44.179 | 2025-10-17 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 00f43e50-db84-3308-b10a-69c7c1d08410 | -3.5028 | -52.4938 | 2025-10-17 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| c5555de0-7a80-36b6-8d98-b3e89f14cdc2 | -12.9368 | -47.1275 | 2025-10-17 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| eef4e560-dad9-3e0c-bd80-767c78e22646 | -10.5834 | -47.42 | 2025-10-17 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 0a1c5643-3377-3835-92c9-d1b17fa8d59f | -11.398 | -44.1933 | 2025-10-17 01:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 5b43189c-b913-3137-b86f-7d742859ebfd | -10.5644 | -47.4223 | 2025-10-17 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 99ca5354-c7da-322f-a94a-cb29ec05be9d | -8.7215 | -43.868 | 2025-10-17 01:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| eeb852ab-54e2-3160-8dea-4c263e545af7 | -2.7401 | -49.3927 | 2025-10-17 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5a6f3824-3127-3c96-9fb8-217886c674f2 | -10.2748 | -44.0247 | 2025-10-17 01:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 11664d34-e5dc-3607-8bf2-797c417f1987 | -16.0125 | -43.4996 | 2025-10-17 01:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 131.7 |
| e6e858fb-b505-314c-9173-8e39fc5e5c33 | -9.1375 | -46.6485 | 2025-10-17 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 64df7613-81b9-3682-a087-b39263084305 | -3.2546 | -45.9632 | 2025-10-17 01:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 199.0 |
| 182c1174-d479-3d08-8f6f-3348cc5c7d03 | -4.3874 | -43.3827 | 2025-10-17 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 57115be2-0d9c-3c1d-8d2f-3cfee36200b6 | -11.4748 | -44.1819 | 2025-10-17 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 4c224403-a054-3175-9985-29ffe4041d6e | -3.2545 | -45.9855 | 2025-10-17 01:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 4f4a0681-27da-3343-9faf-b53c8652afab | -11.398 | -44.1933 | 2025-10-17 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 2cf049ab-c955-304e-a50e-75dac594a1c7 | -3.7937 | -49.4211 | 2025-10-17 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| d87e54dc-dde9-3b6d-8a52-e75cc4d95dd8 | -3.2546 | -45.9632 | 2025-10-17 01:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 217.1 |
| 5eef9911-d5b1-3a00-9d6a-3ae80b0a0e7e | -11.5729 | -44.0501 | 2025-10-17 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1baa4c0d-b488-312d-99ee-ead4553dec71 | -3.2359 | -45.9862 | 2025-10-17 01:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 240.7 |
| 9d138c0d-5ae6-3205-a9b0-ffed866e2b71 | -2.8644 | -50.7361 | 2025-10-17 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 6980d763-567d-3640-aa8b-471a924e0a12 | -3.5212 | -52.4932 | 2025-10-17 01:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c49dbd6b-f05e-32d0-88dc-92bce0a96bc4 | -9.879 | -47.6779 | 2025-10-17 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 0787c9a4-dfef-3e32-804e-6bc05b723f43 | -3.236 | -45.9639 | 2025-10-17 01:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 303.8 |
| ccb52053-3da7-39c7-a239-e288cb168547 | -10.2748 | -44.0247 | 2025-10-17 01:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 9dd2562f-8ac8-3e9d-b5ac-deb07e09006f | -10.9475 | -49.7605 | 2025-10-17 01:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 5bfe44c8-0dbc-325c-99de-778664c0e393 | -11.5921 | -44.0472 | 2025-10-17 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| f6f663c4-1d31-3a2e-bf2d-349223bc8269 | -3.5028 | -52.4938 | 2025-10-17 01:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 3175a31a-fa59-34bd-801f-9825282546e6 | -10.5136 | -43.4052 | 2025-10-17 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4f924ec7-de47-3f5a-8704-749b77f2cf5d | -8.4079 | -46.2314 | 2025-10-17 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| bdc26bf1-853a-3131-ad57-15898f29a9cd | -10.5132 | -43.4289 | 2025-10-17 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ed698d6a-c4ab-3003-8d7f-2a3328832c64 | -4.4248 | -43.3805 | 2025-10-17 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bcf0aaf2-d49e-3ced-bec9-92dc40844ae8 | -4.9735 | -44.9549 | 2025-10-17 01:20:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2f20161e-f14d-3a2b-9f2d-e7cd48baf626 | -7.9442 | -44.115 | 2025-10-17 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b3a6515c-5eb8-3e00-af39-426d4d3b011c | -16.0324 | -43.4953 | 2025-10-17 01:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 0d2f9f6b-3391-382f-9f54-cd1f11ef3301 | -10.5128 | -43.4525 | 2025-10-17 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 0ed5e73b-2d61-312a-8899-21de3f121c76 | -10.2939 | -44.0221 | 2025-10-17 01:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 175.2 |
| dd47f8d3-c0d5-37db-a973-8c1da30e7660 | -11.4748 | -44.1819 | 2025-10-17 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 46e999d2-164c-3269-a9d8-e33ce18837bb | -4.4061 | -43.3816 | 2025-10-17 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 6ea1e465-8ba2-316c-a932-9f20605a798f | -10.2745 | -44.0481 | 2025-10-17 01:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 143.3 |
| a2d4cae1-a978-362b-b21e-841fde53cb17 | -4.3874 | -43.3827 | 2025-10-17 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3e486f60-19dd-30f7-8b86-52ac2c324065 | -9.0821 | -48.0252 | 2025-10-17 01:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3a80263c-7956-3f5e-ab51-b039a4ba2a62 | -4.4059 | -43.4049 | 2025-10-17 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 322.5 |
| 683d145a-a4e7-3de6-a4cf-15adf1caf846 | -12.9754 | -47.1217 | 2025-10-17 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| fd68219a-229c-3760-90ea-0f96238f0db3 | -2.7401 | -49.3927 | 2025-10-17 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6dd94745-3966-36ae-b2df-4a5c9b7b41e4 | -3.7752 | -49.4219 | 2025-10-17 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 3bd55c74-ab24-380d-887e-1457300f8e1d | -3.5028 | -52.4734 | 2025-10-17 01:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 19fcb51b-39e9-3d01-9f80-e5a3ec97a7ba | -4.4058 | -43.4282 | 2025-10-17 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a7f5533a-11b2-311c-b57c-fc99b36f5b23 | -10.2935 | -44.0455 | 2025-10-17 01:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 44c2bce9-e9a9-3d42-985b-593618dfb148 | -16.033 | -43.471 | 2025-10-17 01:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| eff66ec0-0ea1-3356-b71a-d8163811b8f6 | -11.4581 | -44.0439 | 2025-10-17 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| bafbe10b-54af-3c49-ab7c-353ab3591192 | -3.2545 | -45.9855 | 2025-10-17 01:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 206.5 |
| a5ad5dae-4f16-31ec-bf53-d915279e33c9 | -2.7585 | -49.3922 | 2025-10-17 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2f5ffe1e-312e-3ed9-ae09-d3edb5fccad5 | -11.3976 | -44.2167 | 2025-10-17 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9732906a-f1b8-3cc3-8c61-974e8ef786ad | -9.1375 | -46.6485 | 2025-10-17 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 22c26014-2bf0-3a0b-8258-b14c434e1f99 | -10.4941 | -43.4315 | 2025-10-17 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4f6d4d7b-73fb-37ca-a211-66d8c788373f | -10.4937 | -43.4552 | 2025-10-17 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 386cdf6b-e634-3151-99f7-71fd6d55c624 | -8.1996 | -43.3189 | 2025-10-17 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 891e1c08-fa67-3eb1-9150-775f66780459 | -11.4939 | -44.179 | 2025-10-17 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ffdb0c2d-469e-37c9-9ac2-5d48a718734e | -16.0125 | -43.4996 | 2025-10-17 01:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 1923555e-a845-3314-bd0f-9b124e753ed5 | -9.1378 | -46.6261 | 2025-10-17 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 629d18aa-67a4-3c63-86a9-9773aeabb772 | -10.4945 | -43.4079 | 2025-10-17 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| d5c721a7-8166-3c8b-bcfe-68556e8a4537 | -4.4246 | -43.4038 | 2025-10-17 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 206.1 |
| f0dd77da-0390-376d-8434-0305d2b6d5f6 | -4.3872 | -43.406 | 2025-10-17 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4e6059b4-82b7-33a3-822e-d5edd88a93fb | -3.5213 | -52.4728 | 2025-10-17 01:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| beaa1e42-7c71-3a55-8d4c-1a60d47f66f3 | -9.898 | -47.6758 | 2025-10-17 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7879ff07-ee5a-3285-af8e-3ea984cd1fd7 | -11.5917 | -44.0707 | 2025-10-17 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 5a1530a8-c567-394c-add4-b552eef2eb33 | -4.9548 | -44.956 | 2025-10-17 01:20:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| f43380fe-e7bb-3773-a913-c4210fa74e1e | -3.7751 | -49.4431 | 2025-10-17 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 91108089-93a4-3ed3-8579-e980e608afe8 | -10.2935 | -44.0455 | 2025-10-17 01:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| af87642b-e58a-3535-9d58-9fd23fcd7ddc | -2.7585 | -49.3922 | 2025-10-17 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ce99ed9e-9444-32db-8da9-284363f1fbde | -8.4453 | -46.2501 | 2025-10-17 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b27d695e-a8c0-3c63-8b4e-c8fd9ceff017 | -3.5212 | -52.4932 | 2025-10-17 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 1368caa7-6736-3180-9fe2-9de9e1648eab | -11.5917 | -44.0707 | 2025-10-17 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |


[Clique aqui para ver as próximas entradas](README17.md)
