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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2a0d92b-e274-306d-8906-9b3e12ba09e4 | -6.88185 | -45.60818 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 770ba271-af13-33f5-85ef-fad6b7733690 | -7.74723 | -48.83082 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 189.2 |
| b78578e2-0ac1-3962-9d1c-f83320a11da4 | -6.23333 | -43.27618 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e8e9dddb-f1b8-3a04-b9ae-18302a0bc28d | -6.12844 | -44.25679 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a2de0ff0-7486-3071-8969-cf562f474c7b | -6.22015 | -42.45567 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| a0af0688-ac99-309f-9d87-aa9843eef04d | -6.20165 | -43.58284 | 2025-09-07 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 71c47c87-45fd-3264-bd89-4c3f9b49be59 | -6.60947 | -43.9977 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 33a16a4e-3bbc-3ed7-8699-d9ca0123ae5c | -10.78459 | -46.01693 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8a544f9c-8e48-34c0-8415-f9132a423f26 | -10.13848 | -46.23233 | 2025-09-07 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b6328f38-9362-35b1-95c7-d5af7290c8a7 | -6.55718 | -42.95356 | 2025-09-07 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 62676e2f-3cc9-38ee-b210-4985b4dbae5f | -10.81328 | -47.74619 | 2025-09-07 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bf354c17-1b9c-3ed9-972e-69b0ca09bd07 | -7.75706 | -48.81182 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 36db3630-c3b3-380d-9ce6-3195b12a3de7 | -5.78612 | -44.91499 | 2025-09-07 00:11:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d481ae6b-a89e-3e5c-8b20-e12ae10fe7bf | -5.75916 | -45.53905 | 2025-09-07 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6c5286a0-341b-3d46-b383-4d8536ddb03d | -6.21167 | -43.5904 | 2025-09-07 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ccb34f0a-1fd7-335b-b8ee-7420b875d8fc | -11.25334 | -46.50764 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a955d97f-20d0-390d-83f2-49b262d890f0 | -6.21487 | -46.75102 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 805a7f7e-6281-3e48-b741-52bf957388bf | -6.28443 | -53.43945 | 2025-09-07 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0e7eb7bb-e4de-3f76-996b-9a52dee4a417 | -5.94521 | -46.17511 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 913fb1ca-7dd1-3718-8c56-5e6652407b2b | -5.47865 | -45.90826 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 70ee91ff-83ed-38b7-96bf-2a535a2b6597 | -6.13676 | -44.24062 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0a3f0044-1c93-3798-ab9d-84d39490fe4d | -5.22169 | -43.6989 | 2025-09-07 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 946f8927-8d02-3abf-9db3-30a8751f2091 | -6.23699 | -43.3026 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 47e3a21b-2c1f-3a31-924f-cac14d6aac0b | -5.41543 | -44.8307 | 2025-09-07 00:11:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a44c4609-adae-3019-b6a0-3f385a89fd7b | -8.14617 | -44.86238 | 2025-09-07 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 42f5eded-34a1-3a7e-824e-06945b3c1b05 | -6.20562 | -53.2587 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 960579e7-1a25-3623-b597-4e2e9239ebea | -7.7395 | -48.82559 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 21.9 |
| bc5a0b5d-a510-388d-8dc6-9026558a3b81 | -6.20273 | -43.37931 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 48145dda-7209-3f76-904b-0729105fae1d | -6.71962 | -45.14983 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1a210ff7-6d8c-3fba-b8dd-f2d21e39f1ca | -7.34431 | -44.31561 | 2025-09-07 00:11:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 72204f30-5378-3359-9b19-93845713e18a | -6.20151 | -43.37051 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 3d0961c6-3c28-3a97-8b93-0da98ece501e | -6.15431 | -43.17647 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.6 |
| ab38180f-7a03-341e-8aaf-34fda75abe2e | -6.60455 | -43.96188 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc59b95f-4bfe-3b91-8086-cde49804a61f | -10.78367 | -46.02386 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 62f1f295-f001-34c1-be27-921bd79dd102 | -5.99371 | -44.14528 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 7af081fe-5518-3bdc-ae74-ee4ddab56f2b | -8.18056 | -44.78226 | 2025-09-07 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b56dbf0f-0deb-330b-8937-fc2244077d7f | -6.00381 | -44.15297 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 4048acc8-4efa-34f6-9456-385ff9322c18 | -4.8984 | -49.93661 | 2025-09-07 00:11:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 5d97f017-5c1f-3c00-ae78-be344262664d | -11.26801 | -46.45247 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| daeea63c-0bfa-3aba-82d4-fe9a0b3ee731 | -5.95629 | -46.18453 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| df4f136e-bb69-367c-a055-e2ecc90471e8 | -5.71601 | -43.93987 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ff0d0f67-547a-3f32-9121-11b9f0a81a3a | -6.83255 | -46.40242 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ef5742be-1467-3c33-a884-cca573ce01d7 | -11.26568 | -46.51959 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 99163700-9c67-3975-aab7-e4516b1a87d9 | -4.67757 | -41.01743 | 2025-09-07 00:11:00 | TERRA_M-M | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| dae757d0-76e2-346d-a562-dfdb0d8a3f18 | -6.83105 | -46.39109 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f8dba59d-7c14-3fcf-94e3-b3e17aa6b92a | -11.58965 | -47.18762 | 2025-09-07 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 6ebeb31c-9000-33ff-bb23-6258330c0e38 | -10.77438 | -46.01827 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 05442de5-fe02-391f-86e8-da6279928b42 | -6.23006 | -42.65586 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 50dcaf04-1d6a-36b3-bb38-0d9ab81048f9 | -5.98608 | -44.15545 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b6026737-0d3c-3da1-be62-a1bc245be25a | -6.1745 | -44.31789 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9e880e02-6871-3e3c-b6b1-7de4af25ca91 | -6.07939 | -43.30124 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6caa88b3-5727-34c5-968f-2267f2964469 | -11.59908 | -47.17076 | 2025-09-07 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| a314019c-602d-3d48-a184-e1b04fed7867 | -5.69339 | -49.19486 | 2025-09-07 00:11:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9569517f-2d03-37d9-88dd-d5996a95dcd1 | -10.80923 | -47.74115 | 2025-09-07 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 9c9829e1-4c41-3c5a-8286-1f8ad92b49d1 | -5.48003 | -45.9185 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| aaa1a020-fd93-31ba-a5dd-7762ce77e285 | -10.34293 | -44.91411 | 2025-09-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 1370ea95-a161-3779-84e5-d830586bc834 | -7.75165 | -48.82411 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 199.8 |
| 09f78ec2-0e4f-31fa-b2fd-54cadc1a5900 | -6.84096 | -46.38978 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a4ace1c4-b749-3470-bbd1-f8de12ac5ef6 | -11.5878 | -47.17226 | 2025-09-07 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 32e11e66-37bf-3a8b-83df-16b04c62a477 | -2.89479 | -40.24166 | 2025-09-07 00:11:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 1aaaade8-e90b-3b9c-9efa-5a5ca907e56a | -5.72903 | -45.37001 | 2025-09-07 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 17fd3460-b336-3d06-a4b8-bbd331512b6b | -4.26821 | -48.18234 | 2025-09-07 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 5dfec6fb-bf6b-36be-9eff-792c702f7666 | -6.21458 | -53.29093 | 2025-09-07 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| eddd19c4-0d03-3cc3-ac81-c85ec91af39a | -5.84366 | -44.1177 | 2025-09-07 00:11:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ffe830f-5da2-3afb-bf61-57d141df6a3d | -5.73372 | -43.92246 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c3448699-1d30-3edd-af51-81b8fb765448 | -6.19 | -43.36905 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a5e9f764-f01a-3f39-b561-2120f128d9c4 | -5.68162 | -45.43595 | 2025-09-07 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 98e10d90-146b-30b6-8e57-b80e5d85a23d | -6.044 | -45.0486 | 2025-09-07 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8c3551b4-32cf-3c89-ac94-cf2f4592143d | -6.27142 | -43.48629 | 2025-09-07 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e98f08d8-4672-366f-988f-081f2395eed6 | -10.60753 | -44.35092 | 2025-09-07 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| aca3c8e4-9bfb-3062-9138-a86d5872476e | -11.85192 | -50.53038 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 625cd333-496b-3b14-b9af-c1aecc341492 | -10.81115 | -47.72939 | 2025-09-07 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a6ad08f2-4130-3017-947a-e3a0e1466030 | -7.61351 | -44.67322 | 2025-09-07 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3e12856-6b61-3769-9b94-324a3b415add | -10.15468 | -48.7323 | 2025-09-07 00:11:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 934f6963-8cbc-328b-8b50-36fc7befec3b | -11.26241 | -46.4936 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 991d228f-c6d1-3b5e-b0bc-f9ef81cb5713 | -6.08402 | -43.12349 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 122d0470-d302-32c9-82fa-51d85b86f12e | -2.89757 | -40.23481 | 2025-09-07 00:11:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 475be281-423d-3c59-ab9c-7b32b27c641a | -8.44646 | -40.60252 | 2025-09-07 00:11:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6a139769-21eb-31e4-a35c-5abf65410f50 | -6.22142 | -42.46473 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 88ba2961-6e01-304a-a545-ec4268173e9f | -6.38 | -42.60383 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5fc30ed7-4a30-3819-871b-e4bb1ed26e09 | -11.57712 | -47.74716 | 2025-09-07 00:11:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 084cbfb5-2e83-35e1-bc2a-cd1813068f67 | -7.21813 | -43.9974 | 2025-09-07 00:11:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bbc6949c-2c0c-37db-aa45-68dea25c4f07 | -6.6006 | -43.99889 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 00136c62-7dcc-3041-9ecd-3ca469bfa0bd | -6.30135 | -51.39965 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c7141f39-d0b0-36d0-b3e6-9ac0974d9cf3 | -6.17974 | -45.43641 | 2025-09-07 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 59c4c5ff-626f-368c-8e7b-1d23f6ddfacd | -10.18571 | -46.68199 | 2025-09-07 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 098e5378-0652-310d-985a-8fc81a2faa63 | -7.75937 | -48.8293 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 684f148a-2dd1-30ef-9cc0-cbe324ebc7ef | -5.04026 | -45.32227 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 468cc269-9dc4-30e4-b07c-4fa9f1296b4c | -8.15407 | -44.86485 | 2025-09-07 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| db391b8a-e822-36c6-b17f-126e19490765 | -6.14687 | -44.24828 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 20a86f8c-d271-36e9-9bc0-e15c7c8f1026 | -5.73251 | -43.91362 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ecb64c3f-84e3-3023-81e6-b17f578a805c | -5.835 | -44.13423 | 2025-09-07 00:11:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eaec1c5a-6d0e-3e04-805a-04a51c88bd59 | -11.77292 | -47.55901 | 2025-09-07 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a9e2726d-65d9-33db-a02a-fe429b7cd48f | -4.44432 | -44.14108 | 2025-09-07 00:11:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef905dc9-f338-3e97-9fa7-f312bff16e15 | -6.19321 | -53.25531 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9f75a4e2-0855-3beb-9e75-89825abecb04 | -5.94664 | -46.18592 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a24ce101-83e0-3e39-a719-718603ce1b24 | -7.72112 | -44.72009 | 2025-09-07 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e14c91b1-40ce-37cd-92cf-f6804fdde80b | -7.25578 | -41.88737 | 2025-09-07 00:11:00 | TERRA_M-M | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a98fc11d-11a0-3268-9bad-ee3beb7f6ca7 | -6.14565 | -44.23934 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0c408be7-3fbb-31f7-8309-1c74b429dfab | -5.69086 | -45.43468 | 2025-09-07 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README5.md)
