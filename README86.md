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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5476b90f-8755-316d-a73f-b7322bd060f3 | -18.66659 | -52.60788 | 2025-09-01 05:38:00 | AQUA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 08c4e1d1-6f66-38c1-ba41-ba1683b58414 | -14.42816 | -51.66254 | 2025-09-01 05:38:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 564f0f1e-ec3d-3039-bb57-956b93b9a1f8 | -15.69951 | -48.93165 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8ede5aeb-e118-327c-91f8-a3df30ad1be5 | -12.57815 | -48.19785 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| fc40722e-270c-3392-b852-009ba763fcda | -12.60857 | -48.20991 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 533fffad-76a4-3e5e-a55c-95f1a67b2b84 | -15.73925 | -48.97406 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 0a3c8269-6d7f-35c9-b5e1-fbe5f483ba9a | -12.60582 | -48.22603 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c9b5c570-1a8f-3ccc-b2bb-0e652a79b832 | -16.41128 | -45.64967 | 2025-09-01 05:38:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6531e9d4-8a6a-3165-acf8-6aada641a018 | -12.58286 | -48.22195 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ae4ba7d7-9ea9-3bc0-86ed-d84f46465372 | -12.84086 | -48.06884 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5add4ecc-2e29-3783-b3bf-204fa5b3f254 | -12.86363 | -48.0716 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1b2ce5c3-22a8-3385-af1e-d9cf6afc8d1c | -14.79214 | -46.72367 | 2025-09-01 05:38:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| acfb9bbf-0c69-31cc-919c-c4b2e8de578d | -15.60727 | -48.33822 | 2025-09-01 05:38:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 16b60398-6e68-3c15-9bb4-f99976301819 | -13.17549 | -45.2826 | 2025-09-01 05:38:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c2dc9690-9c8b-3acc-b6fa-f254c2012e3b | -12.86574 | -48.06181 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 9b818049-8803-39be-a60e-94320a9df818 | -15.72219 | -49.00414 | 2025-09-01 05:38:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 3ef1877e-64cc-36b3-8004-47af0f27882d | -12.57412 | -48.20414 | 2025-09-01 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 21d26422-bf9f-33db-af8b-1da7f6373758 | -13.69764 | -46.87776 | 2025-09-01 05:38:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e88011dc-4479-3aed-91a3-cd1637d6699a | -15.59639 | -48.33603 | 2025-09-01 05:38:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| b83fcd50-fab5-30c7-83d6-c043905a1810 | -12.8428 | -48.0795 | 2025-09-01 05:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c9384083-bd3e-3cc3-a67e-9c51b0661785 | -11.0373 | -45.1717 | 2025-09-01 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 938a4ca8-e1d9-3fd2-8676-41cf8ede8d3d | -7.9539 | -46.4542 | 2025-09-01 05:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 0971b215-e173-3147-92aa-e5a6a38f939e | -10.5937 | -44.331 | 2025-09-01 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 560fc343-3401-3427-bda8-fbd8b79b3359 | -18.6503 | -52.6007 | 2025-09-01 05:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 53d31855-85a0-381a-ac84-7c7847934805 | -7.6783 | -61.0908 | 2025-09-01 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 2776b9b6-fc53-3f66-92a4-710b89f7761e | -12.8621 | -48.0768 | 2025-09-01 05:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 4d88004e-397e-35b7-9cde-98d05a4a4775 | -11.0572 | -45.123 | 2025-09-01 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2c82ce68-ee37-3795-be28-126ac88389e3 | -11.0381 | -45.1256 | 2025-09-01 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 10a27357-b7bd-38b0-989a-ae61fff6383e | -15.7289 | -48.9892 | 2025-09-01 05:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 21f23a9c-d732-3177-aa8d-9be999652742 | -15.5862 | -48.3435 | 2025-09-01 05:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 681a744c-8949-3e7f-9931-4780b2da3913 | -11.0457 | -47.0066 | 2025-09-01 05:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8c76b54d-d6d5-3ead-885a-758f00906a2f | -12.8625 | -48.0545 | 2025-09-01 05:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ed76520c-ee24-356b-9b29-be224e494280 | -11.045 | -47.0514 | 2025-09-01 05:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 1231dde7-2763-3bb2-8d80-f5e1806ab0a4 | -10.6128 | -44.3284 | 2025-09-01 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 604044af-1daa-309b-bfa2-e962e526dedb | -11.0454 | -47.029 | 2025-09-01 05:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| cf732446-3a46-3da9-b2d3-402659c15dc0 | -11.0377 | -45.1487 | 2025-09-01 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 240.4 |
| d9fbd9cf-0c47-3c48-b32f-adb5b0a45063 | -10.6131 | -44.3051 | 2025-09-01 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a1d4eb79-fff0-3703-a4ac-8f13c079336c | -7.076 | -44.3376 | 2025-09-01 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 48c7b825-2ae6-3eb6-960b-ff712162caae | -11.0565 | -45.1691 | 2025-09-01 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 035296f4-4951-3f86-a6f8-d54a5170fb93 | -7.0946 | -44.3589 | 2025-09-01 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 047246c5-e784-3811-8b73-7e6692807226 | -7.0948 | -44.3358 | 2025-09-01 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 84bcb861-16c2-3a27-a790-bace36820a50 | -7.0757 | -44.3606 | 2025-09-01 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 5dda4129-3e49-32be-8d35-e745aa3385bd | -18.6708 | -52.5756 | 2025-09-01 05:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| cd08eefe-b42f-3b20-98d3-3af33b3d3c78 | -18.6704 | -52.5973 | 2025-09-01 05:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 41ecdeee-7bf7-3b96-8719-26ad1149a016 | -11.026 | -47.0538 | 2025-09-01 05:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c7607127-2c97-3037-94a0-3f2ab33e923f | -18.6508 | -52.5789 | 2025-09-01 05:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 40.7 |
| eaa2028a-afa0-3169-b89f-fd96d128f8aa | -11.0568 | -45.146 | 2025-09-01 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 326.6 |
| 29263a71-9932-32fd-a1fa-b496872e6c20 | -20.41568 | -46.41739 | 2025-09-01 05:40:00 | AQUA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 19056c3f-431b-3515-827a-411fdc302772 | -23.19241 | -45.74865 | 2025-09-01 05:40:00 | AQUA_M-M | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 40506462-6f93-39ab-b1ee-16431cbf4b19 | -19.97282 | -50.40764 | 2025-09-01 05:40:00 | AQUA_M-M | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| ff8b138d-f853-3ba4-82d5-724969fe4824 | -19.98452 | -50.4101 | 2025-09-01 05:40:00 | AQUA_M-M | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 5dd47013-829f-30bd-897d-b567aba2c600 | -21.88038 | -46.75051 | 2025-09-01 05:40:00 | AQUA_M-M | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| b7e7bb34-5adb-3c8d-8483-2beb8858fd3d | -21.87138 | -46.74841 | 2025-09-01 05:40:00 | AQUA_M-M | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 6da3b85a-a792-379d-b194-085803be496a | -22.57453 | -46.98108 | 2025-09-01 05:40:00 | AQUA_M-M | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a309397e-eb6e-32fb-a733-40e450138ee6 | -18.6704 | -52.5973 | 2025-09-01 05:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 14a0d281-76c9-3a0e-b223-cd09e0059860 | -10.6128 | -44.3284 | 2025-09-01 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| afe7383d-8360-3aa8-81bc-b737436c126e | -11.0568 | -45.146 | 2025-09-01 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 236.0 |
| 63219763-9e3e-3a0b-9def-0d196eba11a1 | -7.0757 | -44.3606 | 2025-09-01 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8225d2c0-11f1-3712-a473-248efdeef184 | -10.0434 | -48.0998 | 2025-09-01 05:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 083d9565-fb36-3b39-9c75-19e0a93c967c | -11.0572 | -45.123 | 2025-09-01 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| dcc4de06-e4b1-3baf-beaa-3ac8ca8b61be | -11.0381 | -45.1256 | 2025-09-01 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7dfd2cd7-a6ff-3bff-bc55-bd89f0efbe1a | -7.076 | -44.3376 | 2025-09-01 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 26692242-b1b3-3cc1-9443-305b0214e171 | -7.0946 | -44.3589 | 2025-09-01 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| cf4af232-b819-3014-85b8-3c41690a06f5 | -15.7289 | -48.9892 | 2025-09-01 05:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 89e4614d-a769-3d94-9b40-fd098edf01ba | -11.0373 | -45.1717 | 2025-09-01 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| af06c860-48c1-304e-856b-c8bf79f7e7e9 | -10.5937 | -44.331 | 2025-09-01 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 92693996-9cf7-30b9-ba5c-22839e0df360 | -18.6503 | -52.6007 | 2025-09-01 05:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 6ce65147-d8bc-3c06-b49b-718014245076 | -7.0948 | -44.3358 | 2025-09-01 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e3382c9b-3dc9-34b9-9f89-9fcaa8b509ed | -15.5862 | -48.3435 | 2025-09-01 05:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 082d142b-3c6e-3d1d-8aec-90b3f89725fc | -15.7112 | -48.9032 | 2025-09-01 05:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8f6d70e9-47a7-3b9d-b07f-6ebee9c6b904 | -12.8625 | -48.0545 | 2025-09-01 05:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 6bbeec98-9bff-362d-9947-4ed28f6d45a4 | -11.0377 | -45.1487 | 2025-09-01 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 298.6 |
| d29d3bf6-c96e-336f-a77c-381bc6b1cc87 | -11.0565 | -45.1691 | 2025-09-01 05:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9b0032c9-568d-3309-b7cb-9934321b4cb3 | -12.8621 | -48.0768 | 2025-09-01 05:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| f1aef77d-c22d-3ea4-ae5d-a45f56ba99d8 | -6.79596 | -52.81426 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33e398d0-a8ba-3194-bc04-a137c9891f6e | -6.81047 | -52.81674 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 401d11f0-64e7-3217-8090-660574a02f5d | -7.28138 | -60.65383 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e674bd9-9eff-38cf-ae52-ce1877d5f998 | -7.09907 | -63.03688 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56b65a13-fa2f-3012-a9bf-ee775b638599 | -7.68326 | -61.08809 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0184429-ff29-38b5-ae45-3c5e76238071 | -6.43683 | -55.6137 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb76de0-c010-32e8-8ca6-2c18e77ff9ae | -7.67773 | -61.09566 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 314453bc-db35-3e71-bd93-c59f3c0ba5ec | -7.09083 | -63.04033 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a69c6702-c9c9-3736-80a8-fb003a7d7b6d | -7.07132 | -63.06796 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2ce2092-b8ba-3093-8f67-8c336dbe5e8d | -7.08772 | -63.03517 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bd59174-7f55-3940-bf80-72bb7798c4a6 | -7.10421 | -63.02826 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 687e372a-77c1-3d24-9045-55f9ae22c634 | -6.82411 | -52.81618 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 96aa5d7d-6cde-3760-aa56-bdae7c94a72b | -7.6792 | -61.09413 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e880836-4f05-32e5-9683-dceb17185ad2 | -7.06208 | -63.05258 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32882d1b-8b9f-3465-8f7b-c9bbecd1d36e | -7.10663 | -63.03801 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fe23d6a-0d33-3c50-bba5-2f93f1234d80 | -6.8032 | -52.81559 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9bfbab7-a726-3db4-ba94-db5ac54d3d36 | -7.07817 | -63.07366 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37b45351-119f-32b7-8c80-a352986d19b6 | -7.28012 | -60.66253 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2771c482-a8d4-3b86-88de-3dd816b61e65 | -7.45445 | -63.15818 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e717d816-8a83-33a9-a97e-4299eb2d6d2e | -7.57219 | -63.04146 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbea6383-b39d-3269-861b-55d36228dbff | -6.43564 | -55.62211 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ef1cace-edf6-3465-b07f-bbc74c8a4ab3 | -7.56567 | -63.41635 | 2025-09-01 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf4308f6-7ecb-3e82-95a1-9c72ea8e2e9a | -6.43551 | -55.623 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 281c4147-6475-34e0-83d8-32f0cab89b3a | -6.99437 | -63.01432 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22402db7-0969-39bc-9287-f0dd51dc7055 | -7.56703 | -63.40747 | 2025-09-01 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bd3688b-6f8e-3a8b-8e9d-cc668b925f16 | -7.67978 | -61.09002 | 2025-09-01 05:50:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README87.md)
