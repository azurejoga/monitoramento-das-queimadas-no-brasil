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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 024c9b99-c812-3116-8e4b-a6b61aa84714 | -11.4735 | -44.2522 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 6ebcbc18-1668-3129-be60-bb89dab9e199 | -11.1403 | -45.8665 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 32f64d4f-dd50-3eb7-843c-7f661e2d30a5 | -11.1212 | -45.8691 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 66efff37-72be-3462-b731-2d7a88dd8948 | -11.5917 | -44.0707 | 2025-10-17 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 784d6887-1eb7-3a2f-bafb-478639b8aeac | -10.2745 | -44.0481 | 2025-10-17 13:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| e6549a83-2f77-3a3e-a71d-2769ad926169 | -12.7182 | -48.6273 | 2025-10-17 13:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6fae4120-6b73-303f-afa7-7e2a3f28cb8c | -9.9828 | -47.0234 | 2025-10-17 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 07796089-76c2-31f8-9dc4-0fb8d8803c7d | -11.3992 | -44.1229 | 2025-10-17 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 30802c74-cac1-36ea-bf70-2ec1c3f358a5 | -11.4547 | -44.2316 | 2025-10-17 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 158.7 |
| efd70e93-ae84-31c3-86c1-481bfba441cf | -12.1678 | -45.0771 | 2025-10-17 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0fa3bdcc-acfe-3d90-9a90-79a048327dbd | -10.6172 | -45.2282 | 2025-10-17 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 87c6a0c0-4dab-3172-a383-a6ed7541a204 | -10.1326 | -44.6008 | 2025-10-17 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 67bfb8c7-4820-3638-b7d3-37815575b55d | -10.938 | -45.4146 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 318.2 |
| 266c81c5-c443-3092-b6d8-507c9807159c | -10.9185 | -45.4401 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8c7fba4f-0734-3950-a39c-e208ea08bdcb | -10.2939 | -44.0221 | 2025-10-17 13:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 0ef342f8-fc54-3e3d-8932-ae266d0f5bab | -12.4866 | -45.4895 | 2025-10-17 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 553fea12-c2a0-3e32-9d2e-6d6077ddeaa9 | -10.2935 | -44.0455 | 2025-10-17 13:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 75027281-4a3d-3460-822c-07cbe4208106 | -9.898 | -47.6758 | 2025-10-17 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 84bf29fd-0ea1-34b7-a859-b1e762687735 | -11.5729 | -44.0501 | 2025-10-17 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 3eb1df39-30eb-35ea-a655-69812e2f5aed | -11.2642 | -45.3011 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 875fc427-0727-3f8f-8edd-98b65e333933 | -10.9189 | -45.4171 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 8dc4c391-5fd4-3a08-83c6-a4e6e62343fc | -11.1021 | -45.8717 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 50a2aefb-8e98-30f0-b5b3-d018c81b7ee0 | -9.9638 | -47.0256 | 2025-10-17 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8e273ba2-76af-3ec6-b29c-171482efb6ab | -10.1063 | -47.6525 | 2025-10-17 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8d836e02-91c3-3736-8c99-e304541f8c04 | -10.5128 | -43.4525 | 2025-10-17 13:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d3adfa93-3c47-3273-898c-6f8cbde8ac54 | -12.487 | -45.4664 | 2025-10-17 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| a5a75fe4-9b8a-36a8-ab04-8175c71f003d | -11.3988 | -44.1464 | 2025-10-17 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 2bd4900c-5d7a-353d-b028-85eb4148a7cc | -10.5132 | -43.4289 | 2025-10-17 13:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 9e69a0ec-3f0c-3cd5-abd6-6b4f5e5f7f39 | -13.9127 | -45.5808 | 2025-10-17 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 6945969f-8c8c-3431-9e9a-40d3ad2527f4 | -9.9831 | -47.0011 | 2025-10-17 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d145ed71-2752-397e-a9f6-ba484936739e | -11.9257 | -46.845 | 2025-10-17 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 5ed11ab7-d614-3d16-801c-28d061fc13f0 | -11.4731 | -44.2756 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 250.1 |
| efbcfd5f-13e8-382d-b31e-8f7e146b44fd | -14.1754 | -47.9252 | 2025-10-17 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6d6af407-c990-3364-bcde-0d738f5bec2d | -11.4919 | -44.2961 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 9f4fee02-7fd7-3a71-a806-e38d329d6a17 | -13.4219 | -47.9511 | 2025-10-17 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f1564eff-dd1b-3222-a1f3-6c472161e11e | -10.4941 | -43.4315 | 2025-10-17 13:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 4db83b6c-d982-3928-8fff-9713b6ad55f1 | -12.284 | -47.1544 | 2025-10-17 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 85d87195-7dc3-3149-b78f-e6c943a0c58c | -10.2554 | -44.0506 | 2025-10-17 13:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 01322569-4631-3705-a090-44754e3398b5 | -10.2748 | -44.0247 | 2025-10-17 13:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b82290e2-56b6-3239-8620-f7056677e306 | -10.5136 | -43.4052 | 2025-10-17 13:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 3045c096-66de-3960-8cc4-c866064e62e4 | -12.2648 | -47.1571 | 2025-10-17 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 7aa75934-5202-3add-81e5-c2dd5139d4a1 | -12.4678 | -45.4694 | 2025-10-17 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 512d1727-fa66-33a4-ba9e-908e3984c2bd | -11.4748 | -44.1819 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 3d46bfa5-0f97-3010-b4fe-2dde2ef1a822 | -11.1399 | -45.8893 | 2025-10-17 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 46c6030d-42d2-39ad-b1f5-73d7a73092dc | -11.4939 | -44.179 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 7cd8cfb0-8add-3987-a706-572306ecef17 | -13.4412 | -47.9483 | 2025-10-17 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 8700a5b9-9a32-3aa3-a2ec-b2cdcf311e6c | -11.4551 | -44.2082 | 2025-10-17 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| f013b7b7-6cf7-36e4-abcf-761d2b18fa1b | -11.496 | -44.0617 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 1acad570-c4d9-3892-896b-ad970ba837fd | -11.5724 | -44.0736 | 2025-10-17 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b8c7e904-6f00-33d0-8bdb-1fbce107d71e | -11.4543 | -44.255 | 2025-10-17 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 13d5c13e-cde7-30df-997b-27c70f02a291 | -11.4935 | -44.2024 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 20de6ccd-7067-366a-806e-9339ee916a46 | -11.4556 | -44.1847 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 85f9b4f4-db3c-36b4-88a6-9b0de2437fd0 | -10.534 | -49.5471 | 2025-10-17 13:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2fff22b8-f285-34b8-aae0-e053f46fd775 | -11.4743 | -44.2053 | 2025-10-17 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 491.9 |
| 54799787-e4b5-3989-aeed-243ba66db448 | -10.2558 | -44.0273 | 2025-10-17 13:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 44447a50-ca3f-3403-9de2-ef9782b62227 | -11.5921 | -44.0472 | 2025-10-17 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 27bc7d82-7bcf-308c-8b14-067a674bc5c1 | -9.9828 | -47.0234 | 2025-10-17 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 52286b66-16de-3ef9-b6c0-6c97fc87c661 | -10.9189 | -45.4171 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| db2ccb85-2102-3e03-a402-e992c5245354 | -10.1326 | -44.6008 | 2025-10-17 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 75ef1a7b-fb43-3bf3-a942-b00bca3029e7 | -10.2558 | -44.0273 | 2025-10-17 13:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| a571f874-65d5-365e-8246-05f3dee5edf1 | -9.9638 | -47.0256 | 2025-10-17 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| aec19a48-f9a0-3239-a621-aa008e5e387a | -10.6172 | -45.2282 | 2025-10-17 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c5dd1866-dae7-30da-8700-aace2f73f509 | -12.7182 | -48.6273 | 2025-10-17 13:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9a3b5b13-cec3-3ae9-abef-ed8bb6eec094 | -10.5128 | -43.4525 | 2025-10-17 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8dd26041-7fdf-34d8-98df-12a975631a18 | -11.2642 | -45.3011 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 96621c76-881f-31c0-928f-e40c16c018f9 | -13.9127 | -45.5808 | 2025-10-17 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| d2c48b85-bbac-38db-affb-95bb3bf38ddc | -11.5724 | -44.0736 | 2025-10-17 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 18a5da76-c129-34f0-b012-2ed7317cb77b | -10.4941 | -43.4315 | 2025-10-17 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 47612e99-1a07-37e0-b02a-126ac8d5e220 | -14.1754 | -47.9252 | 2025-10-17 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| fa58988d-f7d8-30ee-a26f-2aa851f4a093 | -10.1063 | -47.6525 | 2025-10-17 13:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e5ab4ddb-193c-3c06-83e1-68bb27fdc38b | -10.534 | -49.5471 | 2025-10-17 13:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9a406f8d-17f0-3826-b4ce-1de6661975b4 | -11.1212 | -45.8691 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 7a4284ce-c90b-39de-a1a2-fddf79754529 | -13.4219 | -47.9511 | 2025-10-17 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c43fe34c-2868-3bc2-84fd-bbdc133de9d8 | -12.4866 | -45.4895 | 2025-10-17 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| abadc1ad-122b-3831-8e01-a9925189842b | -11.9257 | -46.845 | 2025-10-17 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0aa37657-d1c2-3c4e-99ee-232015ed66a0 | -9.9831 | -47.0011 | 2025-10-17 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 88e117ba-3f88-3c93-8e82-be66539ac50c | -12.9607 | -47.9294 | 2025-10-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e8cae7d1-cce7-3a73-a05d-1e6babbaf8ec | -12.1678 | -45.0771 | 2025-10-17 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4f353ac7-1ecd-38ff-913c-2c95385623d1 | -11.1403 | -45.8665 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 37c8e0f2-8124-381a-8bad-f01b05f00ee5 | -10.2939 | -44.0221 | 2025-10-17 13:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 5d2126c2-65e2-390f-bc82-0d39d75aac97 | -11.5729 | -44.0501 | 2025-10-17 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| d4e8d20d-a1c4-3236-b3e4-c426dbf6a129 | -10.5136 | -43.4052 | 2025-10-17 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f83147a9-efa6-3a14-8122-fca574e55af7 | -12.4678 | -45.4694 | 2025-10-17 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9de89b59-235a-34c1-b681-6dd83f6a362b | -11.5917 | -44.0707 | 2025-10-17 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 714c04a5-882e-3754-8022-b685b89d8b9e | -11.7435 | -51.1472 | 2025-10-17 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8062d816-1ad5-3214-b2d2-e84d8b4a8a41 | -11.1399 | -45.8893 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.8 |
| a304ac55-a519-369c-895f-854898f595b4 | -11.1021 | -45.8717 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a49aa1e3-153f-363d-9ccb-0e5442c722c8 | -12.284 | -47.1544 | 2025-10-17 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6bd1f9e3-718e-3ace-99f0-d05c43328d03 | -10.2935 | -44.0455 | 2025-10-17 13:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| fb8417e2-8b14-3503-a29c-0ef4063d434f | -10.6169 | -45.2512 | 2025-10-17 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b825e9cf-c95a-323b-9990-862e72924346 | -10.9185 | -45.4401 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 133f32ec-c0cc-37db-a869-478cf56d4751 | -10.2745 | -44.0481 | 2025-10-17 13:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 937f1302-b9d4-3a6f-b4b0-218f5c9818d8 | -13.4412 | -47.9483 | 2025-10-17 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 38f96b59-7e02-31a9-ab61-c5ad18ae8ddb | -11.1406 | -45.8437 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 69037d1e-13f5-365f-a336-997aee3e1cc3 | -10.5132 | -43.4289 | 2025-10-17 13:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 568a5f7f-b698-39c8-97f1-40496a5a7d05 | -13.477 | -48.0989 | 2025-10-17 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 46cef056-d6e1-30bf-bb8f-aca57defffe1 | -12.487 | -45.4664 | 2025-10-17 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d09e9c10-8544-38cc-bcee-cc91e3e25e28 | -10.938 | -45.4146 | 2025-10-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| ad46aab1-abb2-31ba-83c9-7a4a1c345fe3 | -10.2554 | -44.0506 | 2025-10-17 13:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 303.8 |
| 281b87e6-0eac-3ee8-bdf9-61c9ebd7fa5c | -9.898 | -47.6758 | 2025-10-17 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |


[Clique aqui para ver as próximas entradas](README123.md)
