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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf748f2c-ade7-3d75-b418-dc1add7f835b | -6.6698 | -45.5118 | 2025-09-16 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 10b66e69-325c-38ae-9976-f7c1b9c974a2 | -3.8415 | -44.1054 | 2025-09-16 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 361.9 |
| b329cdcc-138b-3b2b-b93c-ffd659e14b6e | -6.169 | -41.2114 | 2025-09-16 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 9e1e51e6-da92-3425-89a1-cfe71d103c3d | -9.7325 | -47.3403 | 2025-09-16 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e0c1e67f-6576-3860-90dd-3e6390fd9379 | -11.7151 | -46.8739 | 2025-09-16 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f549f964-bb5d-30d7-a1e5-06dedd309840 | -13.2798 | -54.2435 | 2025-09-16 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 89c3e1c5-465b-3db7-8a35-80471af208b1 | -12.8404 | -47.1417 | 2025-09-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 560274d3-5b06-309a-be88-2e0ebcd7942d | -11.0807 | -49.724 | 2025-09-16 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ffada164-7d8f-3a13-a0bc-82c900ec0351 | -8.6885 | -46.3823 | 2025-09-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ace66d5b-de0c-3db4-8230-637626f47fdd | -6.337 | -43.1727 | 2025-09-16 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| e45ff438-8083-3597-9921-afc104052a6e | -12.7098 | -48.0094 | 2025-09-16 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 187.1 |
| cc0a72c8-8e03-3478-ac47-df4e3262a77b | -9.0759 | -47.0335 | 2025-09-16 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 1105cb83-da36-3499-bb97-9c668533d2bd | -8.917 | -46.2015 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.4 |
| a46c8e68-d830-337d-9cfa-3b37f673c377 | -6.1881 | -41.1855 | 2025-09-16 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 10359b52-2d79-3bcb-b051-c0e0fea0045d | -6.3558 | -43.1711 | 2025-09-16 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 44f00e96-9fff-34d0-b8d2-c063d3fbf759 | -8.5947 | -46.3471 | 2025-09-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e937dd1c-309a-3b57-bf39-7035a4a94e6a | -8.3323 | -44.7426 | 2025-09-16 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 316.0 |
| ed651641-8e17-3deb-a59c-caca45b185a8 | -9.1706 | -47.0014 | 2025-09-16 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d51fe2f4-9a7b-3029-b18a-024898558e52 | -7.2771 | -46.5814 | 2025-09-16 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 851f467f-d615-3848-8989-2965d4f2f2cb | -7.6949 | -44.486 | 2025-09-16 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 8b183e85-9abd-3931-b47e-353530d124ba | -14.6143 | -46.3806 | 2025-09-16 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 8b5f0def-b88a-3093-b646-4ce671ba2f03 | -12.6953 | -47.7446 | 2025-09-16 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 762b845e-10a7-379e-ac56-d6aea0937c13 | -8.9539 | -46.265 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| b2b4d06c-fed4-3907-81ba-49a425fa66fc | -12.6352 | -45.7652 | 2025-09-16 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 9fadff1b-ea98-3604-8f8b-62c7d6c9f182 | -8.6127 | -46.4124 | 2025-09-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 96946c42-2602-3b0c-a281-e3cb8b956524 | -5.7858 | -43.9378 | 2025-09-16 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a9347635-6376-39de-a033-376dcd74f471 | -8.9259 | -45.5231 | 2025-09-16 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 251.7 |
| a153040c-d8a4-3b3e-a318-0f89aebf6390 | -13.2027 | -47.3126 | 2025-09-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 13c24991-74ad-30fe-b366-fe153621255c | -7.2768 | -46.6036 | 2025-09-16 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 7ce461fe-4ab3-3b74-9a66-371779e07412 | -18.5225 | -44.1558 | 2025-09-16 13:40:00 | GOES-19 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 198d8ba9-3f28-3278-81cf-78ff299673e6 | -12.6356 | -45.7422 | 2025-09-16 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ab2135d7-640a-399f-82a1-e90367591bc1 | -7.2581 | -46.6052 | 2025-09-16 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| fed81ca5-7c10-3d5e-a0e9-2b6382a119bd | -5.9942 | -43.6902 | 2025-09-16 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f6691ad0-0bf1-3e88-9487-5cfca556b8bd | -7.4503 | -46.1647 | 2025-09-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 4ea4f58b-04b4-3ee7-a165-c58f0f9f9d47 | -12.1147 | -44.8304 | 2025-09-16 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 92b64f26-a977-3ae1-87ce-9f0c772be98e | -8.3326 | -44.7197 | 2025-09-16 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| d29c39ee-97b9-3f07-85cf-44baeecf9e95 | -13.2801 | -54.2228 | 2025-09-16 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 296.6 |
| 8522cae0-11d5-3233-8186-44bf48411511 | -8.9568 | -46.0398 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 79f2eb45-76d1-3507-b79b-fa27284e2fa8 | -12.8597 | -47.1389 | 2025-09-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 36322b39-6a3c-318c-b0b0-ff224e5cd38c | -12.8409 | -47.1191 | 2025-09-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 4e4c03a2-2080-3608-8836-7ca5bb3023bc | -8.9356 | -46.222 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| bd2c2c39-3656-36f7-b130-04b0d3005cf8 | -11.0804 | -49.7456 | 2025-09-16 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 38e8b3d6-2585-3791-b68e-37c17f3e6c94 | -11.5041 | -43.6136 | 2025-09-16 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b88e3512-e7c5-324d-ac2c-abee575148ae | -8.6885 | -46.3823 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a93f9499-a6d7-3a4f-848d-1441b63b2f0f | -6.356 | -43.1476 | 2025-09-16 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 290.2 |
| 3a61e47a-44ef-3830-89a0-641c39cd62d2 | -7.2581 | -46.6052 | 2025-09-16 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 64f12e6f-a683-386a-ae1b-348fed76e4b7 | -8.22 | -49.4901 | 2025-09-16 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| db0aea00-b04d-32b1-91b7-2c5da372fa8b | -15.5341 | -48.0381 | 2025-09-16 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b2af355e-ae24-3a30-b8fe-bee38d088ced | -7.676 | -44.4879 | 2025-09-16 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 53beb043-7848-35e4-98de-810679471329 | -3.8415 | -44.1054 | 2025-09-16 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 229.2 |
| bc576c89-220d-3c41-bc99-5073a30dcc1e | -5.786 | -43.9147 | 2025-09-16 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0df39a99-7447-3d72-9f16-6317a6280f44 | -8.935 | -46.267 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| f658d207-d4c7-3ae1-af41-f90ad79eebe0 | -8.9568 | -46.0398 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 6b03ecfa-955e-3cff-ac12-da504bea218d | -10.9671 | -47.1729 | 2025-09-16 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d0215378-0316-3499-a39b-cfc17653ce92 | -15.5729 | -47.1483 | 2025-09-16 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1a6bdead-04ef-3242-8249-2240415b7b93 | -11.4665 | -43.5722 | 2025-09-16 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 265.1 |
| c58ffec5-f6d1-340a-8ba2-ff5eff437f21 | -8.8795 | -46.183 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 15d5815a-8786-371c-a5fc-83fd0523bdd9 | -12.6953 | -47.7446 | 2025-09-16 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 4b4cd00a-d767-3647-b224-b380c9fc2050 | -12.1152 | -44.8072 | 2025-09-16 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e67968e7-b76f-302c-b898-405f05aadd33 | -6.1878 | -41.2097 | 2025-09-16 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 22397ab2-7ba9-336e-bb6f-2535e9ca718e | -8.9757 | -46.0378 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| d2641776-7c54-3251-a4cf-3322bcf408dc | -13.2031 | -47.29 | 2025-09-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| e739fb73-ff76-3c46-9c8c-a4ad44ed63ff | -10.08 | -48.1836 | 2025-09-16 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0af40893-b527-33fa-961a-1c465f7a5ec0 | -6.3558 | -43.1711 | 2025-09-16 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 2a89db8e-499b-31a0-b8d1-d31e7e87062d | -10.9004 | -47.8027 | 2025-09-16 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 66cccddd-7ee2-3ee8-96c5-1cc79494aa2c | -8.9728 | -46.263 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7e1d91d2-b1ce-3d03-a4fd-e5d60db709c4 | -12.6356 | -45.7422 | 2025-09-16 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 543fee45-3baa-373f-9693-564e3acb11f7 | -13.222 | -47.3097 | 2025-09-16 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 2f2de015-af04-377b-b8f6-b4db409ebb04 | -9.152 | -46.9812 | 2025-09-16 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 776cdde3-a6f8-3226-9731-046b80af3ce8 | -5.7506 | -43.6859 | 2025-09-16 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 48d05b8d-ab70-32da-82dd-6f034d145523 | -13.7862 | -54.9512 | 2025-09-16 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 35525d20-49ea-3583-8dbe-28235a4d6047 | -8.9539 | -46.265 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 7874df58-c393-314e-aa59-bfc81a2c2b3a | -8.6127 | -46.4124 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 18dddc2a-3611-3e04-acc1-469cacbfda63 | -8.9571 | -46.0172 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 319.6 |
| cf6113bd-1ab0-3636-a3fd-b0f2935d3d96 | -7.6949 | -44.486 | 2025-09-16 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 7eab04db-9586-37c3-b904-cc5cae0e5e65 | -7.6763 | -44.4649 | 2025-09-16 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 54b8abc1-3a04-3987-8c4a-f3d63fa7d8c9 | -8.6124 | -46.4348 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 06a9d011-cb0d-36ea-91b1-90b31fb9cd6d | -6.337 | -43.1727 | 2025-09-16 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 2cad72f9-b80b-3da3-a40e-6909adb94892 | -8.917 | -46.2015 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 362cac87-d3ce-3dad-bc7e-bb1149bb3a53 | -8.6319 | -46.3881 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 366.4 |
| 4cab8cbe-76a4-3cac-bea9-0244127f113a | -11.4849 | -43.6166 | 2025-09-16 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| be950057-cd7a-312f-a8ce-97827d8aa8b0 | -3.8416 | -44.0824 | 2025-09-16 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 211.6 |
| a2c4fb6b-ec72-34ab-9717-a069c35fe6a3 | -10.6551 | -46.4501 | 2025-09-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 62f679f1-1c4d-3f77-a6ea-fa3cd28fb86f | -11.0807 | -49.724 | 2025-09-16 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0c81d17a-a06c-3f85-a994-99211f0a60b1 | -15.9021 | -47.3165 | 2025-09-16 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 41bb5f9d-0641-3fe8-8ede-bf6b634d968c | -13.2801 | -54.2228 | 2025-09-16 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 476.8 |
| 97feba7a-31df-3e31-9cba-baf4f044cf40 | -8.976 | -46.0152 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 26e840bb-340d-3b91-933a-d9ac3bb6bf10 | -6.1881 | -41.1855 | 2025-09-16 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| 903bbec5-5da4-3e32-a044-e26a0d828c54 | -5.7858 | -43.9378 | 2025-09-16 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| c5274834-317a-37f8-805c-68573d572040 | -11.274 | -50.795 | 2025-09-16 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c5fe48ae-5cb1-375c-85e5-af43af0bcd9d | -8.9262 | -45.5004 | 2025-09-16 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| cefe70b1-d40c-3f4f-aa50-c557d46b7f0e | -11.7151 | -46.8739 | 2025-09-16 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 194b61a4-1a76-3ac1-ab9a-d56ab799b930 | -10.7112 | -46.5106 | 2025-09-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 23d5e445-ecf1-340c-b091-d98d17d18315 | -14.1727 | -46.1354 | 2025-09-16 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 539ab0a2-e1bf-3edb-bc0e-87ac0bd5dfe4 | -12.4322 | -49.7135 | 2025-09-16 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c6522dbd-e889-3e7b-88fd-fc9a3b68fe1d | -8.5939 | -46.4143 | 2025-09-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e3cef704-42db-3905-9d20-796ea2c6048b | -8.3323 | -44.7426 | 2025-09-16 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| d1e19503-8a09-3038-9c0e-ab8b3d44013f | -10.7299 | -46.5307 | 2025-09-16 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 56a514a1-ad53-3ca9-a3dd-c7ddcd9cac39 | -5.8086 | -43.4956 | 2025-09-16 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| a1622886-cb28-3cbd-8d3a-bc1c1882e39d | -8.9167 | -46.224 | 2025-09-16 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |


[Clique aqui para ver as próximas entradas](README96.md)
