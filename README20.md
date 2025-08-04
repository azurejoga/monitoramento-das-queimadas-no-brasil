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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a33a700a-ee54-3f33-9174-97aa9276a0ff | -22.51247 | -46.30494 | 2025-08-04 04:38:00 | NPP-375D | BUENO BRANDÃO | MINAS GERAIS | Brasil | 3109105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4307919-7e96-3f4e-9249-c093cbea1911 | -20.08184 | -44.01439 | 2025-08-04 04:38:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a58682f6-2be0-3b45-af5b-3dffa973223a | -19.32718 | -44.15833 | 2025-08-04 04:38:00 | NPP-375D | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf103dcf-b1a0-3258-a548-2c26d3abb14d | -20.32326 | -42.89141 | 2025-08-04 04:38:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b5badc16-f25a-3106-a453-a0ede18e2137 | -17.9957 | -44.33462 | 2025-08-04 04:38:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 299b0365-af16-38ea-9905-dc1c5243f7e0 | -15.75801 | -49.94254 | 2025-08-04 04:38:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a65ab8a-b6c9-3884-a6d4-8bb747e5a7f3 | -20.72042 | -47.29434 | 2025-08-04 04:38:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adeb1c8f-d712-33bb-bcc0-9f6767125f62 | -19.32664 | -44.16287 | 2025-08-04 04:38:00 | NPP-375D | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09d41ddf-fdb8-3465-907c-b5238022b011 | -22.91993 | -43.71075 | 2025-08-04 04:38:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| f007105d-22e8-36bf-95bd-24c4ced82fad | -17.46232 | -47.10128 | 2025-08-04 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 452f51b0-f9bf-3593-8dd2-26fe2df3c581 | -18.63287 | -46.44252 | 2025-08-04 04:38:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08b5d615-700f-30e7-be26-ee3dfd4a6093 | -19.94147 | -43.62616 | 2025-08-04 04:38:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ac5a280f-0dd6-38e1-83ae-5edda4e3090b | -22.91573 | -43.70463 | 2025-08-04 04:38:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 8c97aa27-1479-39b3-b3a5-26c4403d66d9 | -20.32812 | -42.89219 | 2025-08-04 04:38:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| abb4d7af-315b-39b7-a408-53a18eb3bd52 | -17.36409 | -46.0887 | 2025-08-04 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28c0db37-7db7-3568-b3fa-47339ecea5dc | -22.82951 | -47.3341 | 2025-08-04 04:38:00 | NPP-375D | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a804fec-9ee0-3ade-933f-c5cc556056b1 | -13.0535 | -56.8947 | 2025-08-04 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 9e4d07cf-b39a-3aa1-98cc-3dd59a2b42b1 | -8.0132 | -43.1278 | 2025-08-04 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| a64ffac3-d5be-3925-b4ad-6a25f18b297f | -13.0538 | -56.8746 | 2025-08-04 04:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d01411b3-5b43-3062-b9e8-8641b9297781 | -7.9943 | -43.1298 | 2025-08-04 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| 18f0f356-4488-372e-82fd-80ff937c9360 | -7.994 | -43.1534 | 2025-08-04 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| ec0d423d-7acd-3171-992d-a70469c26a0e | -8.0129 | -43.1513 | 2025-08-04 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| c741f310-9ae4-3bc4-8077-4f98a2e82846 | -23.71845 | -47.47688 | 2025-08-04 04:40:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 497285f4-26c8-3c11-9ed7-939d90414c42 | -7.9943 | -43.1298 | 2025-08-04 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 3c5b6df8-28eb-3fc2-8815-65f8d6cfd9ba | -13.0535 | -56.8947 | 2025-08-04 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5da15202-1837-3055-835f-f4e0521bf2ef | -6.1997 | -43.7665 | 2025-08-04 04:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 83e883bb-f577-340d-9dc3-61a538455613 | -7.994 | -43.1534 | 2025-08-04 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 81ebca0e-f2f3-3dc6-b81d-806968393c9f | -8.0129 | -43.1513 | 2025-08-04 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| aeae6fd3-f5e5-3faa-9d54-b5515135bace | -8.0132 | -43.1278 | 2025-08-04 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| d29e9c06-a6c1-3f3f-b305-74155df57b4c | -5.28481 | -44.8821 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a81a38eb-d610-38ec-8265-844323159feb | -4.13093 | -47.64902 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95522b85-b334-3fa5-b213-79cb38751fc8 | -6.20053 | -43.7623 | 2025-08-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b90d45a-0cb8-3252-86b8-7eb811ef5232 | -4.1257 | -47.64522 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ba8a5c3-65d5-37ae-8469-7091731ef667 | -4.12715 | -47.64446 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cfe986db-f244-391a-997d-4eceabaff2d3 | -6.06467 | -44.67636 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bb79f71-c364-3eae-b07c-35455c33f83d | -3.91153 | -49.08357 | 2025-08-04 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ff82db1-206c-36ad-9852-76d09cbdfa6c | -6.06968 | -44.67662 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f46a529-7bee-3cf9-a9ad-e39a7178826a | -4.74646 | -44.44427 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 974b1167-6bd4-380d-93eb-45cc92001f3a | -5.28432 | -44.88538 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2ad9b53-480e-3606-8a98-52b7cc32e7fb | -4.12071 | -47.6488 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e769b713-0d80-31a1-9be0-d53d442cd862 | -6.52434 | -44.52906 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2263da29-d2e6-33e2-8830-fd4dc6e0e7ab | -4.12446 | -47.65334 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 423a418a-b6d3-3f03-bbb8-1cab57dfb380 | -4.13652 | -46.45852 | 2025-08-04 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bffcae9-4b6d-3af5-9b7b-e78c716faf11 | -4.74251 | -44.43282 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 760101d9-0128-3ce0-9c50-7895406529be | -6.19581 | -43.75756 | 2025-08-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ce801b9f-7f78-3147-baec-d18bfec567c0 | -1.40191 | -54.12175 | 2025-08-04 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6a852f7-d732-3a51-be62-7acb7f36386a | -4.7415 | -44.43993 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 206b898f-6354-324f-806a-b59198726869 | -5.27944 | -44.88138 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ef0ec41-5dbd-3911-be42-378db12a175c | -4.74697 | -44.44077 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3da9d2c3-1203-3456-81a5-c43745a29cf4 | -5.28774 | -44.88257 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aedce4b5-c323-3906-aaed-891db1d12f5d | -5.87559 | -50.14971 | 2025-08-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df216a17-a29e-36a7-8b1f-b63225afaa53 | -4.13071 | -47.64162 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36c64265-0347-3dbc-acd9-505708593f9b | -4.12508 | -47.64928 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bd174ee-2e97-3176-8af6-9e0f20b31fbd | -4.12536 | -47.6567 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c71bef6f-40fd-3636-9d33-d318cc4cd5ac | -6.06368 | -44.67936 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 212f5045-dc64-37bb-8de7-d486e8d40321 | -6.31918 | -45.65818 | 2025-08-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 005e1fab-5f06-39c3-a9c3-fa91177362f8 | -6.1952 | -43.76183 | 2025-08-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| aba35e21-b86b-325d-9e78-97d559432a66 | -5.27897 | -44.88464 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cacf0641-dd5c-361a-931b-c98e903898f1 | -4.12946 | -47.64976 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21b827fb-c6dc-31f6-aa99-0ff3ae29cdc3 | -4.12884 | -47.6538 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2040e16-c077-3100-9bec-2a09ea1eb6be | -4.13152 | -47.64494 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f6876e99-14e0-3464-8910-e5847bb5de1a | -4.02753 | -48.05928 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 830045c6-0861-3fc6-968d-3c92e705766d | -5.87629 | -50.14503 | 2025-08-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b806caff-347e-3da7-b693-396ef1ef7410 | -4.12973 | -47.65723 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6203643-4463-38bd-a2a7-385fa15ee073 | -6.32006 | -45.65197 | 2025-08-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 130ce2c9-c36b-3e81-ae24-316229453b06 | -6.05919 | -44.67157 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2de30b6a-91e3-3d95-93d0-f4bc3cbc37b7 | -0.90215 | -50.67168 | 2025-08-04 04:55:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9128b81b-1e17-3725-81e5-80b3ffe970d1 | -3.91233 | -49.08132 | 2025-08-04 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eb7504c-b8e1-3996-bbfa-596f14c45d03 | -4.02331 | -48.05861 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aa5e055-0b0a-316f-baab-8417e35b110e | -4.12656 | -47.64853 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 589b1d0b-2ef1-32fb-8428-a86d169fbe32 | -6.06419 | -44.67987 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84c90564-efe4-3e32-a2cd-1b0bd0cfbcdb | -4.02692 | -48.06328 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07131b97-f354-3f62-abaf-d6088a5492ce | -4.73603 | -44.43904 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6965868b-6531-3cc0-acd3-593d54dca54d | -6.19474 | -43.76107 | 2025-08-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| fd50156d-825d-36ee-95d3-4b05f75946e8 | -5.28238 | -44.88183 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41a747cb-db86-3341-bdee-6e70137054f5 | -4.7405 | -44.4469 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3a0f36c-f9ba-399b-b87a-5180e23738bc | -5.28728 | -44.88589 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83233bcb-b5fd-313c-be8b-3c9b34450d79 | -4.73704 | -44.432 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f84f134e-2e11-3e81-af45-863701dedd64 | -4.12218 | -47.64804 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 41c3f396-3e45-344b-bda0-80c82c07e135 | -4.1282 | -47.65796 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a46d5bc-16e1-3c2a-a582-fd39f4dfc7b6 | -4.21512 | -46.35749 | 2025-08-04 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df51959-0e9a-30ed-bc9a-3a2774385667 | -6.06014 | -44.66852 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1022b198-5111-35a9-b90a-e1a3cbb6fa69 | -6.06918 | -44.68012 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5019e35-290e-3e3f-9841-0492bec27924 | -5.277 | -44.88118 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e600bef6-3c9a-3f83-9f44-4879e3c9d67d | -6.19641 | -43.75329 | 2025-08-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68e56ab2-7775-3633-999b-1f1328855f64 | -6.32521 | -45.65283 | 2025-08-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48ffcc5b-7a5b-3fb7-ace6-4f074065afdd | -6.51881 | -44.52787 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da29f8f5-9d58-3510-9616-f7839212f255 | -6.06418 | -44.67588 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2104e8f-78dc-39bb-8381-b6e58eb3cb22 | -4.741 | -44.44341 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27f0051b-86eb-3d6f-b5c5-88c0c3d3ad3d | -6.07017 | -44.67713 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1a4af2d-69b3-3450-aa0f-a9d8723eaa18 | -4.73653 | -44.43552 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f634c1bc-a8ac-356b-bc43-c49b923eeedc | -4.73554 | -44.44253 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8a2252df-d19e-34cb-857a-7796f6e61457 | -5.28284 | -44.87853 | 2025-08-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1387eaf4-e829-324b-83df-557eca4a2ab1 | -4.742 | -44.43641 | 2025-08-04 04:55:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c08a97b-3b25-381c-94ee-859fad7ca193 | -3.88394 | -54.24199 | 2025-08-04 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65ca967a-8ba7-3249-9470-2963b400af5f | -6.06515 | -44.67289 | 2025-08-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9cfa3dd-3ff6-3100-b950-9190f6007106 | -4.12159 | -47.65212 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a9fc6b14-2742-36d8-9757-49303137f107 | -6.19532 | -43.75677 | 2025-08-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| caa5bdca-5c26-3aa7-97a8-d952d91df9df | -4.13008 | -47.64571 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40f5624b-6b12-3795-9e6e-7ff6c30b7cf9 | -4.12596 | -47.65258 | 2025-08-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README21.md)
