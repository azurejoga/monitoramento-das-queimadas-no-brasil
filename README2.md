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
| 338f9dc5-d185-3301-960b-472a3a07da4b | -2.3763 | -47.6419 | 2025-09-17 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7e1beb5a-c6ac-31c1-9fc4-d94a1e0cb395 | -6.8922 | -43.9619 | 2025-09-17 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 61ddfb73-9775-3405-9467-a9ea27132a46 | -11.0164 | -48.9297 | 2025-09-17 00:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 1552975b-144e-37fb-ab1b-fdff2e3f3a7e | -7.5622 | -44.5678 | 2025-09-17 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 98267672-1846-37ee-ab23-ad95fd12ef83 | -6.6808 | -46.2961 | 2025-09-17 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 246.6 |
| c917e0f6-eee7-35b7-a02b-a6f29be29e33 | -6.6806 | -46.3184 | 2025-09-17 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 34aba3e8-fae6-3e38-a8c9-ed102fd2e85d | -15.4001 | -46.1245 | 2025-09-17 00:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 281bcf84-d6ce-39a7-9bc7-f7ec7acddc05 | -9.104 | -44.933 | 2025-09-17 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 95d6543d-7af1-34fb-a4b4-d07669fd9980 | -6.8732 | -43.9868 | 2025-09-17 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d845662f-620e-3326-9c5c-7b7ff3c2ad58 | -7.5996 | -44.5872 | 2025-09-17 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 26534f8e-1424-3591-bfaf-328467dd18e4 | -6.6314 | -45.6051 | 2025-09-17 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f2718c08-ebed-3f58-aef7-5e54b3caf9b8 | -6.6129 | -45.584 | 2025-09-17 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 06bf187f-b643-3ed6-a6be-328d7fd9f9c5 | -11.0201 | -45.059 | 2025-09-17 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c5441cdf-3a98-3aa2-a2c8-e58cea4e3262 | -7.82726 | -46.1524 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0f6acb7a-14ca-334c-b6aa-6015cb975050 | -11.0137 | -48.9388 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 3fcf9c5a-537a-375a-90e6-7b5a769b08d2 | -7.99746 | -45.68353 | 2025-09-17 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 169c2ddd-2bc6-31dd-a7d8-f9035a6453e3 | -6.59686 | -44.32262 | 2025-09-17 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| c2847ba7-7a91-3d49-a0e9-192b960eacfc | -9.05262 | -44.8385 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 37dccc9d-6b8b-3874-a122-099b80f9ae6f | -8.96624 | -44.19733 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e0c71afe-a3ca-30f5-9a7c-be83254ae1d3 | -6.67237 | -46.31293 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| a369dfdf-0876-3185-a143-49f66ef67df2 | -11.50449 | -43.6303 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7bb08646-7a50-3726-8184-803a3de5ec72 | -12.69147 | -45.80325 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d4f2085b-efa9-3882-8503-70568d8289c3 | -11.43698 | -40.65372 | 2025-09-17 00:11:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f6173888-8755-316e-8876-8232c433eed7 | -13.4984 | -43.66914 | 2025-09-17 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6d93b7cd-ea3e-3ae6-9bad-c373cc317d2a | -13.49966 | -43.67866 | 2025-09-17 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cdb42275-2fad-3743-915c-0aadf00cece3 | -12.10494 | -44.81896 | 2025-09-17 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1cdd2fe3-7d5d-3e1b-b9e0-d9a1ca3e77c4 | -12.36748 | -43.20399 | 2025-09-17 00:11:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 608e77ce-a472-31f6-8df0-d0b0eeda433e | -13.04374 | -44.12295 | 2025-09-17 00:11:00 | TERRA_M-M | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f3f6991-e74e-38d5-a765-b29110e1faa0 | -6.62261 | -45.58992 | 2025-09-17 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2ea2df27-ab10-371d-be57-3bf7054a432e | -11.03313 | -45.0606 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 746d4c1a-fdea-3631-b04d-fc51ca20be7f | -11.46178 | -45.19197 | 2025-09-17 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8458b3f-af1c-3c4f-8756-f57a18beefce | -6.98339 | -44.45333 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6d1df8c2-7b00-3b8e-b014-520fe6aaffa1 | -10.70923 | -46.48963 | 2025-09-17 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0a8e5bb0-6efe-3870-b348-fb8e2164a4e4 | -8.9951 | -46.26691 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 7855ef34-1711-3b25-b341-7de8e42e5fb6 | -11.72625 | -46.87846 | 2025-09-17 00:11:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bec7d5c7-6599-32fd-af61-74b597d9f5f6 | -11.46907 | -43.57004 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| acee337c-ed43-3db2-92a3-74ad79967cd9 | -13.33018 | -43.10059 | 2025-09-17 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 15e38d08-5f06-359f-a68f-a2830885d181 | -7.40067 | -44.61023 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 116a5648-4774-3106-9540-40388e8aa08c | -7.76729 | -44.73037 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| efc63d97-5e28-35d5-bdb4-acb5ca14080e | -7.48252 | -46.10586 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9ee0304f-8acc-37cb-b099-ba8212e0c092 | -13.94555 | -43.98613 | 2025-09-17 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8f7b1cec-7476-3b84-bb08-f1967eed55a7 | -9.55175 | -46.30606 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3e88f5ed-0c1b-37a9-9f1f-0ea18c80d734 | -6.67097 | -46.30237 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| fdde1295-ad76-39cd-9056-d666d3301c26 | -7.64928 | -44.47379 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b1e6dd90-d293-3b79-b3af-ebc5dd7b3156 | -6.0469 | -43.14567 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 7d753552-e521-33ae-ac67-02c998e09f6c | -7.06956 | -44.34402 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| e95090a5-2f80-3be5-aaab-70979ed8b59c | -7.48531 | -46.12684 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 72848970-e623-35ab-9bc3-684ec7c60b06 | -6.35333 | -43.16556 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 21ec9cbb-0424-3bc3-819a-d5ad2a0afede | -13.65018 | -44.26891 | 2025-09-17 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5d5827ae-d1f6-37c0-989e-a9b6e6e89697 | -11.49308 | -43.61322 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f11d0ff3-d43d-315e-9cbd-718b52c016e2 | -6.31466 | -42.69429 | 2025-09-17 00:11:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1682dee1-a7fb-3b0e-b8e7-6be2e85b0cd0 | -12.72524 | -48.00935 | 2025-09-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2dacbf3a-b5fe-30b9-8fe5-30be6f2ce036 | -13.21996 | -47.29311 | 2025-09-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b6ae4dfd-58f9-3894-81a1-47371e7b4289 | -6.51332 | -45.74068 | 2025-09-17 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 13b3fb26-1287-37f1-af80-0eef095d16ad | -10.15253 | -46.13517 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 548d9df1-c304-35dd-b204-7d36f3988761 | -9.14361 | -46.93892 | 2025-09-17 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 92e4d5ee-2aa0-3184-91fd-1183fcb5c8fb | -12.69522 | -47.961 | 2025-09-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 049d9d38-ad8b-38a9-93da-2574f8302ba4 | -7.86804 | -48.17888 | 2025-09-17 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| db51f360-ad3f-3d25-8254-af3e0f2cfd2d | -8.67557 | -46.40341 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f7b9a4b4-465d-348a-80e6-29f44778b67b | -12.28646 | -43.82937 | 2025-09-17 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5d18d5c9-429a-3dd5-99ec-a016a57f3d89 | -11.00943 | -48.92637 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 4452b9fe-17b5-3964-9184-2d465566b738 | -7.5798 | -44.57266 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 182.2 |
| aa102b17-bd9c-3827-82d4-ed1bbc81c607 | -6.18745 | -41.20412 | 2025-09-17 00:11:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 5425a9f4-5ac0-3287-b378-b60df596dfc8 | -8.92161 | -44.48093 | 2025-09-17 00:11:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2a4b11b6-6226-34e1-a4cd-a6359e8ded46 | -12.27743 | -43.83051 | 2025-09-17 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f7fe9dbc-09d9-3fc8-a73b-f3efd8d014d1 | -11.02618 | -48.93706 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9498c061-31bc-3706-9609-ec59cdd44883 | -6.40699 | -43.35687 | 2025-09-17 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f9e5bb8b-8273-3e62-b5e5-c593ae4e9038 | -7.63021 | -44.46724 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c0d06ccd-9db2-3061-a930-4eb4b7c821de | -7.89049 | -48.17054 | 2025-09-17 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cd52eed0-efd4-3f8d-8c51-ed4592d78a6a | -11.02192 | -48.92486 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3e077d1a-8820-3bb4-9c36-674d872187dd | -13.32129 | -43.10186 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2a12c5d9-115b-38dd-b1b4-ff42f0dfc2c1 | -7.82865 | -46.16307 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 49ce5cee-bb7c-3056-9fbc-bae57799edc0 | -6.74298 | -47.00146 | 2025-09-17 00:11:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c95b544c-85bb-3486-ab01-1218cee77712 | -6.68195 | -46.31163 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 255.0 |
| 7342e3e5-ae10-3b35-893c-9d3ef8c32c01 | -7.58873 | -44.5714 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| cf5e1dae-7378-3447-8393-76f197857e89 | -12.92777 | -42.78436 | 2025-09-17 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| ed59b18f-b161-30b3-a425-3392cbed167f | -6.87974 | -43.96025 | 2025-09-17 00:11:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| b20fb517-6aac-3cb1-b5b2-b204fe4aa138 | -10.04637 | -44.35484 | 2025-09-17 00:11:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0de4b8e9-72c9-3911-a9d2-b04d1ac723ab | -9.74055 | -47.85385 | 2025-09-17 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d64ae124-1be7-32ad-8f02-c7d872cfda0a | -8.1353 | -43.64259 | 2025-09-17 00:11:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b3fdfd06-c12f-39a1-b225-68bb8950ba1a | -7.88847 | -48.16167 | 2025-09-17 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0124933a-f23f-37b9-b922-1da9951b9bcb | -8.66571 | -46.40495 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 96ea196b-a599-3495-832b-4e21227e004b | -13.34963 | -44.00634 | 2025-09-17 00:11:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6449ab9a-99e5-3b5a-9550-73d5e0159e1d | -6.95406 | -42.45045 | 2025-09-17 00:11:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3964dfb5-befb-3bdd-a2f3-fee9189d31f1 | -8.96302 | -46.32884 | 2025-09-17 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cc533edc-9494-38e9-8417-2b4fc025961c | -11.73703 | -46.87758 | 2025-09-17 00:11:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 89a42df5-2e02-3d7a-872a-fca13786b5bf | -7.52818 | -44.73556 | 2025-09-17 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 48077c47-4f08-34d4-a798-cb66c00fa876 | -7.09662 | -44.54164 | 2025-09-17 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 643afaef-2ce1-3127-8c98-3b0f0244bf55 | -10.62684 | -44.22035 | 2025-09-17 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 640d6128-9cb5-3856-af71-7741d7ff500e | -11.46783 | -43.56092 | 2025-09-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| aacc5cdb-cf7c-3370-b063-e0234839e939 | -6.18893 | -41.21458 | 2025-09-17 00:11:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6bbf6057-99e8-3adf-af74-eb92bd8c45ff | -6.21673 | -43.91407 | 2025-09-17 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5a353a1-7c90-3588-a0d8-55a341f8b36b | -9.09164 | -44.92125 | 2025-09-17 00:11:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 22de4775-55f0-3617-b63d-6648241bf215 | -6.21789 | -39.24881 | 2025-09-17 00:11:00 | TERRA_M-M | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| c9abb62e-6540-3f0a-aefa-0cc8a59c1b25 | -7.87921 | -48.17756 | 2025-09-17 00:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a62f195c-41fa-34b4-8f21-51f96dce79ed | -10.70653 | -46.4833 | 2025-09-17 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7dba655d-b2a3-3992-b48f-d4b6b663bf3e | -12.7213 | -48.02098 | 2025-09-17 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| fd0f0568-77ff-3232-bc96-35b2b96b302a | -9.06365 | -47.03129 | 2025-09-17 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8cca8dbd-4829-31e8-9723-3d4cf46abb3e | -10.81394 | -50.6702 | 2025-09-17 00:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.7 |
| b1e176d5-0132-334d-b18a-86da11a6a0ec | -11.59877 | -49.82875 | 2025-09-17 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |


[Clique aqui para ver as próximas entradas](README3.md)
