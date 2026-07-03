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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39bcdb93-2b17-3b1a-afb5-61d68025a9ad | -19.5093 | -52.725498 | 2026-07-03 00:30:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cee30530-3dcc-366f-9442-43e74bb713cb | -1.7854 | -55.517899 | 2026-07-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6331b9a9-4e0d-3650-aa27-72fe642f6eb9 | -5.7872 | -45.031399 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3863364-9fd0-32a9-92ce-bf1390e02d04 | -6.7174 | -48.096802 | 2026-07-03 00:30:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1e59a2-0aa7-34d8-9e70-527b84326999 | -12.7491 | -44.512798 | 2026-07-03 00:30:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c09c11e1-6f5e-3d41-b67d-9cebe4a2dbe0 | -11.8478 | -48.229 | 2026-07-03 00:30:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 167061fd-7285-34d3-8657-7ad96dce0b39 | -17.254101 | -42.630001 | 2026-07-03 00:30:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b1854caa-2e09-3223-9fe6-3dca59409256 | -20.428499 | -47.536598 | 2026-07-03 00:30:00 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 88f15663-3cb7-3554-9585-ee6f3d00c5f9 | -9.1973 | -45.313999 | 2026-07-03 00:30:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ab5c8c1-1b6e-3c54-90e6-f47c55ac299f | -10.932 | -43.0434 | 2026-07-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12255909-752f-3fc1-bfd6-9ab273480336 | -5.7949 | -43.781601 | 2026-07-03 00:30:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b96bc9c7-dd44-3625-8317-1875dd00c0cb | -12.5354 | -57.209702 | 2026-07-03 00:30:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ffac026-7d00-3768-b8db-afaa485d6f5e | -11.5059 | -54.498501 | 2026-07-03 00:30:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e93d98e-5529-3a36-a752-2ae97cba32e2 | -5.7852 | -43.784 | 2026-07-03 00:30:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdfe5f54-6705-3ab3-9250-10a87045ec7e | -5.7916 | -43.809399 | 2026-07-03 00:30:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 800e9567-d575-3d88-86e3-8cc20328a09c | -11.4221 | -56.057201 | 2026-07-03 00:30:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eee2c70c-872f-351f-b560-9b1de5bc7a0b | -5.8065 | -45.026699 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2677f63-e00f-3623-bf97-d6890d6ec3c2 | -11.3639 | -55.4048 | 2026-07-03 00:30:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9585ed7a-2303-3f02-99f4-84edcb0ef976 | -17.2498 | -42.652302 | 2026-07-03 00:30:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af2a0bc2-2d8a-3f28-a2d3-db307bfec1c5 | -11.5043 | -54.491402 | 2026-07-03 00:30:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30305021-79a9-344a-a65f-c1807858665e | -12.5373 | -57.219299 | 2026-07-03 00:30:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9d37247-edc2-3c77-be58-1506a8f284ff | -4.3426 | -47.760399 | 2026-07-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee70478-b451-3570-987b-eada65a0d449 | -8.7018 | -54.569099 | 2026-07-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aeb7fff-cd16-3ef4-ab56-e55f498c77ce | -5.7775 | -45.033798 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41e7f17f-7dd0-3ed9-9b68-0640ec0e2d68 | -17.244499 | -42.632801 | 2026-07-03 00:30:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3c067b56-7fa2-3eba-88b4-916c291d52af | -13.0307 | -57.084599 | 2026-07-03 00:30:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68d6c17b-c4a4-3298-a97b-f776954f86ad | -12.3546 | -47.4231 | 2026-07-03 00:30:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c88918b8-8626-392c-b1fb-75809746aef9 | -4.0129 | -48.060299 | 2026-07-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96704ebb-be14-31e7-8516-c80ab1ba88eb | -8.3779 | -48.228699 | 2026-07-03 00:30:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4701a845-f230-39dc-b3d1-53d5cfddb339 | -6.9137 | -43.712799 | 2026-07-03 00:30:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b872cf6c-56af-3526-96de-7ea3c784746a | -11.3137 | -54.466202 | 2026-07-03 00:30:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df038b84-55a2-31fe-8221-0fe0bb80b58c | -12.7439 | -44.532799 | 2026-07-03 00:30:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64f78418-c540-3adf-9597-a47ea9852ac1 | -21.4914 | -48.534 | 2026-07-03 00:30:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8db4fc6e-6bf7-3794-96ec-ee52618d5772 | -12.7297 | -44.518002 | 2026-07-03 00:30:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9bdaa28-c58d-36ad-81fe-4467362c0db0 | -4.0032 | -48.062599 | 2026-07-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e38dae8d-431f-3b4e-b935-8b55458ebbae | -6.9233 | -43.7103 | 2026-07-03 00:30:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e430753-f866-3de7-8011-7a399598a82d | -12.4945 | -43.811401 | 2026-07-03 00:30:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e47c653-5541-3be8-a285-cc905fe879e6 | -17.259399 | -42.649399 | 2026-07-03 00:30:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 577001cd-c444-3826-873e-dc8081a82e1f | -8.731 | -48.323898 | 2026-07-03 00:30:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 931d3c9a-9aa2-308c-a5df-cb88598330e9 | -5.7878 | -45.075401 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fc4ce36-d9bc-3a35-95d0-fcd82dc287a8 | -11.3558 | -55.414501 | 2026-07-03 00:30:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af89de61-ff72-3237-bd9f-8f949332b84e | -11.31443 | -54.47152 | 2026-07-03 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 643ae94f-3cda-3803-83f9-10d19f8d4a54 | -12.36321 | -47.43192 | 2026-07-03 00:39:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| d6cf4f94-ea2a-344d-9e6c-318dd56c1b23 | -13.03891 | -57.10471 | 2026-07-03 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6a077b22-9247-3ab1-bb5c-c23a89900fda | -12.35744 | -47.4278 | 2026-07-03 00:39:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| a8ea48e9-7783-3910-ba63-58f1d3e88c6c | -13.03002 | -57.106 | 2026-07-03 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 522aa67d-874b-30fe-8d27-e7dca0294066 | -17.54279 | -54.01117 | 2026-07-03 00:39:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dd298b46-8835-3dc2-8c6a-18020fc8ad1d | -12.54018 | -57.23154 | 2026-07-03 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c9af1f61-cd10-30ae-9087-6500a81b261b | -11.50348 | -54.50381 | 2026-07-03 00:39:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 86de0973-d006-3708-8e75-a82e8bb8c108 | -19.51117 | -52.73811 | 2026-07-03 00:39:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d636061b-9c85-3e56-86ae-b775d2ba14ef | -17.54418 | -54.02084 | 2026-07-03 00:39:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 93643504-d4a2-38eb-932f-30b581e9c850 | -13.02879 | -57.09687 | 2026-07-03 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2215df23-2d09-3025-afb6-ed49f7e32a94 | -17.55329 | -54.02304 | 2026-07-03 00:39:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 87c11b2f-1f50-3740-bcc1-6d5230b05387 | -11.70531 | -51.63193 | 2026-07-03 00:39:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 193c8918-bec7-343e-98f8-f90464f2abbc | -12.53895 | -57.22244 | 2026-07-03 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| de63fc36-f24e-3a0e-8857-6a80ef0394b8 | -13.03768 | -57.09558 | 2026-07-03 00:39:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8f34fba-95b4-3d5b-819f-b99c5fe45b80 | -17.55187 | -54.01338 | 2026-07-03 00:39:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7634d06b-f9be-3c71-8673-183d7f1c1170 | -17.2639 | -42.6527 | 2026-07-03 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0220e43a-b7ed-3417-819a-9a8a51a29663 | -5.7945 | -45.0586 | 2026-07-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 159fd07f-27f5-3cc6-abd1-52c903b0c4ae | -10.9401 | -43.0355 | 2026-07-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 52268ed6-5588-3a10-bb78-003f06f2ce3d | -5.8058 | -43.7975 | 2026-07-03 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| da454051-fede-3cfe-b2e4-770be05fbb4f | -10.9588 | -43.0565 | 2026-07-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1eaa9a08-5918-3522-8518-9062ec71c6bb | -5.8134 | -45.0345 | 2026-07-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a26fa51c-86d8-3066-b27b-58aeca81eeab | -5.7947 | -45.0359 | 2026-07-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6ed4446e-7317-3707-b644-e7d8c7206c18 | -12.7548 | -44.5428 | 2026-07-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 55c4aac9-91aa-3a9f-ad0a-f5dee6ac792f | -10.9397 | -43.0593 | 2026-07-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| dbc7ad93-be7f-33fe-a29f-2fd1326ceb0b | -12.7359 | -44.5225 | 2026-07-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 0b317426-e5b2-363a-8828-a6ef21b69c85 | -12.7553 | -44.5194 | 2026-07-03 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 19db5c44-6854-3cf4-a25b-2eb58e3958aa | -8.38819 | -48.24526 | 2026-07-03 00:41:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 1abf9bb1-fbde-3071-8393-eb87bf5dd802 | -8.70989 | -54.57553 | 2026-07-03 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 99d13742-a6a0-3a42-b79e-60dd319d090e | -11.3488 | -55.41619 | 2026-07-03 00:41:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2c16ba74-f8c8-3beb-9e9c-2fb433b07bd1 | -10.58497 | -55.42482 | 2026-07-03 00:41:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b2726990-f07b-3d39-a6ed-0e449f36f8c6 | -10.9054 | -56.85453 | 2026-07-03 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8f06fec3-d1d5-3b27-b2f4-388eab039913 | -8.7258 | -48.33484 | 2026-07-03 00:41:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f1b84dac-6ba5-3e29-9ede-bd63e355f941 | -11.41225 | -56.05801 | 2026-07-03 00:41:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 3d3a9df9-8ca9-33c3-8d88-6b33ac65dd37 | -8.37415 | -48.22082 | 2026-07-03 00:41:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 1608f1b4-33eb-3755-8fb5-551d5130c4d3 | -4.01375 | -48.07315 | 2026-07-03 00:41:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| efd0d0dd-9337-3b5c-9b3b-bfcef32f6c49 | -11.41353 | -56.0671 | 2026-07-03 00:41:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8bac20fb-48cc-3171-bd9f-027666b098cb | -11.42115 | -56.05672 | 2026-07-03 00:41:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 21d491e2-ee99-31df-972a-3426775a5e14 | -8.73583 | -48.32633 | 2026-07-03 00:41:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e80bf7aa-6aaf-3f8f-aa8c-ac565d07b516 | -4.01514 | -48.06795 | 2026-07-03 00:41:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| db727705-80b7-32a6-82f0-574e14af32e9 | -10.5836 | -55.41529 | 2026-07-03 00:41:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 68dbda70-f061-32ea-8b01-9807b55b86f9 | -8.38282 | -48.21278 | 2026-07-03 00:41:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| f46e9e29-cfb2-3ff6-a94e-596ea8c5925e | -11.62762 | -59.02228 | 2026-07-03 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 46e13443-88e1-3b92-852a-649d684bd30e | -1.78408 | -55.52335 | 2026-07-03 00:43:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a6bc3a1-7a7d-3efc-a262-c11b262a7440 | -5.7945 | -45.0586 | 2026-07-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| aa726e69-d8e6-344e-954b-24a66b94af91 | -9.3065 | -40.2614 | 2026-07-03 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.5 |
| e8526740-d0ec-3b73-beab-82152f83e0e0 | -10.9397 | -43.0593 | 2026-07-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 05304561-4d0d-3a5f-a7b2-eff174f25c46 | -12.7548 | -44.5428 | 2026-07-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| dd227b81-f21b-3b69-93e5-3c74d9fd35dc | -5.8058 | -43.7975 | 2026-07-03 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 9eed364c-8809-3d85-8518-39867027c118 | -10.9401 | -43.0355 | 2026-07-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 26053bc3-7223-3775-adad-b5485432ee0b | -9.3069 | -40.2365 | 2026-07-03 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 799fcf30-9aa9-32d8-b7fc-e3ab6e4e6c45 | -5.8132 | -45.0573 | 2026-07-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| a9eda437-84c4-3535-82b6-b9a9aa380738 | -5.8134 | -45.0345 | 2026-07-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6ee5770b-18f8-333d-beda-71a59bc5981d | -12.7553 | -44.5194 | 2026-07-03 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 4a07a39c-e6c2-3523-9cb3-e58b59cea504 | -5.7947 | -45.0359 | 2026-07-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 60ef49ec-f6c4-3e60-85a4-0035324d90ac | -12.5117 | -43.811199 | 2026-07-03 00:56:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba1965c9-ef6c-3108-b330-417929d90e3c | -17.2616 | -42.6371 | 2026-07-03 00:56:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a2f33d96-5008-3603-b090-b027b8706eba | -8.3847 | -48.220798 | 2026-07-03 00:56:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f88c746-8111-3306-8efb-f36c558f22cd | -6.9335 | -43.723801 | 2026-07-03 00:56:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
