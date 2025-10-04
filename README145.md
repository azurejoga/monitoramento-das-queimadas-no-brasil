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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e1064fd-a9e8-3d0c-8650-014e3483d4ba | -10.3343 | -50.3402 | 2025-10-04 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 4215667a-a67c-3f8a-a61d-38e660523ae6 | -12.9471 | -50.9838 | 2025-10-04 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 55d7c42f-8b5d-309b-ac0a-0ed536f55c3e | -8.2314 | -46.8289 | 2025-10-04 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 1eeef654-dfde-3438-bb67-9f9b68007f5c | -11.9335 | -46.3926 | 2025-10-04 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 055dc90b-b4d9-3b88-80c8-08a0faf76f48 | -11.9147 | -46.3726 | 2025-10-04 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 6ae84eea-5d9c-39c2-b3e7-3b6d09c0a502 | -13.3426 | -48.0742 | 2025-10-04 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| d8dfebd3-e496-3b46-a3e8-b04427a9011e | -14.2126 | -46.0827 | 2025-10-04 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 351705f2-8911-38e8-b9f6-8ec13c5750e3 | -12.5866 | -54.7474 | 2025-10-04 12:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ad0d52b3-8062-3db3-acef-47f626fcc111 | -15.3797 | -47.952 | 2025-10-04 12:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b954e61e-6f9d-3941-88d5-ff51f1154437 | -11.5072 | -46.7446 | 2025-10-04 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| dd5a42d9-a38e-34fb-99c6-21412e832c85 | -10.5835 | -48.7178 | 2025-10-04 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f0338c44-159c-3858-93c9-cd733595a281 | -11.8818 | -44.9815 | 2025-10-04 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 42f325e6-d75d-304e-8981-ac0aaf1ea25c | -12.0891 | -45.1814 | 2025-10-04 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f86b2930-a5a5-3b8f-a7b7-b4954f2928c1 | -12.535 | -45.9864 | 2025-10-04 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 382.0 |
| a29f9c40-76e8-3a50-af9d-8371c063c958 | -13.3081 | -47.8565 | 2025-10-04 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 255e8c48-c5e0-3125-950e-e753d4942468 | -12.0314 | -45.1901 | 2025-10-04 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a566e8b4-0109-35a6-9499-265d09c38eb4 | -11.9143 | -46.3953 | 2025-10-04 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| d466c784-4a5c-3fe7-bcfd-0e4c6019e524 | -8.8529 | -46.7897 | 2025-10-04 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3e39ce5f-0e51-3eac-9a36-e97aac530285 | -11.5492 | -47.6773 | 2025-10-04 12:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2c8cc666-0683-3916-a4de-baa14daa98a7 | -14.2131 | -46.0596 | 2025-10-04 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 190.6 |
| d59820f7-95cb-32f0-99e3-699d9dfc66e8 | -7.8593 | -48.2037 | 2025-10-04 12:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 17c1a11e-18db-3512-a6f9-3d9311eda4ef | -9.3379 | -45.7947 | 2025-10-04 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| f80d6e54-b9bd-3607-be1a-c8cef8695f7a | -13.2892 | -47.837 | 2025-10-04 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 931d8116-18bc-3caf-ae5c-a1ad9c442a7a | -14.0509 | -53.9289 | 2025-10-04 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cbebedb3-80d5-3ef2-bdfa-719f005d8997 | -9.3382 | -45.772 | 2025-10-04 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 3ce9b78c-b4f2-36d0-bfab-20598759c97d | -14.2325 | -46.0563 | 2025-10-04 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c3404122-de91-3491-934c-0d99960386e4 | -8.8534 | -46.7451 | 2025-10-04 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3e101c82-0149-3506-9ae4-73fbe935d579 | -12.7194 | -48.5611 | 2025-10-04 12:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| d8ac1eb4-30ea-3429-9b8f-b56c5430c1b3 | -13.2938 | -47.5905 | 2025-10-04 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c254d004-b753-36b6-98a8-cc5396a2c345 | -13.9813 | -45.0815 | 2025-10-04 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6adc5ac6-bd3b-3c96-93a5-99610f86e6ac | -13.114 | -47.9518 | 2025-10-04 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 744759a8-d6d3-35c8-8398-ddf971de3583 | -14.2321 | -46.0794 | 2025-10-04 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f3735759-afef-3ba4-b357-87a33cbac094 | -11.9339 | -46.3699 | 2025-10-04 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 40955863-2d7a-3c89-9cd4-ed42ba523ec6 | -12.8761 | -47.2937 | 2025-10-04 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9638ae8d-318d-3782-b2b3-71753bd4440e | -11.1379 | -47.1959 | 2025-10-04 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 338fcdc2-93d5-3c5c-bd0a-601ac61a47f7 | -7.7687 | -46.2255 | 2025-10-04 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 13b31f96-5d5d-33a6-b747-673bdbdd7315 | -8.5458 | -47.264 | 2025-10-04 12:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3c08d798-dff7-3da5-8f90-26b27734d830 | -13.2938 | -47.5905 | 2025-10-04 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d0b40721-0218-3268-9ad8-9fb1b73135e4 | -12.535 | -45.9864 | 2025-10-04 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 824.2 |
| d7ade506-26b6-3111-abc5-ce52269d4311 | -7.7941 | -42.5369 | 2025-10-04 12:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 141.0 |
| 5fff8b9b-748f-3819-96f0-f1f48722737b | -7.7489 | -46.3168 | 2025-10-04 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 1ad0c89d-579e-3995-b8e5-c213f3bfb86c | -8.2314 | -46.8289 | 2025-10-04 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0a57055a-4ed3-3d32-a5a8-98edaf1e7807 | -13.8283 | -43.1702 | 2025-10-04 12:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 3914cbcb-bbe0-3ce2-b01a-e8bf8845baa9 | -14.2131 | -46.0596 | 2025-10-04 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 355.3 |
| 47eff2f5-4595-3fe1-891e-4fa5384c2cff | -16.0212 | -50.9425 | 2025-10-04 12:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e7883000-174e-32f9-a7f2-d6b7ed68a0c9 | -14.2126 | -46.0827 | 2025-10-04 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 5c964907-199c-3711-b0c7-dd5b45978df4 | -7.5504 | -42.3965 | 2025-10-04 12:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| 11ccdfbe-54ef-3063-bdc0-15a16ffc3efe | -9.3379 | -45.7947 | 2025-10-04 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 017d5422-cfb6-3f0e-ac43-d3b53c0a3428 | -8.8529 | -46.7897 | 2025-10-04 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a1c76ada-6d2e-3e27-9d05-e7cc2a6d5662 | -13.3081 | -47.8565 | 2025-10-04 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 890d9f53-fd46-3f09-bce8-3daec9a292c5 | -12.8761 | -47.2937 | 2025-10-04 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f655ae33-03c1-3789-8fc6-61ee5afc77a5 | -13.3426 | -48.0742 | 2025-10-04 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 5efe90b1-87c2-31cd-926c-3aca7bc74b58 | -10.9314 | -47.021 | 2025-10-04 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 059d5d9b-5a01-3a2b-b83b-29e52929dff9 | -12.8614 | -47.0486 | 2025-10-04 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 53dee18a-e431-335a-8328-f0d4b6c731fe | -12.3853 | -50.2595 | 2025-10-04 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 45b8139c-070f-3107-9b3a-3ab960a19c62 | -8.8526 | -46.812 | 2025-10-04 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7aea1111-8814-339c-b02e-41ec4ea4caaf | -14.3899 | -45.9601 | 2025-10-04 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| af13cd77-bae6-3412-9a7e-e136a2a67a04 | -12.0891 | -45.1814 | 2025-10-04 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| c189bad6-5d6e-3351-aa3f-8611a6856a56 | -11.5492 | -47.6773 | 2025-10-04 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 64e2c529-3f17-385e-ab7a-812142d3a58d | -11.1101 | -47.755 | 2025-10-04 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fad89860-d7f3-374f-a187-141e97d67f3b | -10.3346 | -50.3188 | 2025-10-04 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 232.4 |
| ea0853bf-ac2d-3f2f-8e12-8922e765cd2b | -7.7938 | -42.5607 | 2025-10-04 12:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| e3763811-5e9c-3197-b236-8dfb339090df | -11.9339 | -46.3699 | 2025-10-04 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6a8911c2-c918-3ce5-bd2d-fddf6f8fad8c | -11.0126 | -46.6971 | 2025-10-04 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 55218e92-e8c7-3165-b2fb-e4da57ebd98f | -8.2316 | -46.8066 | 2025-10-04 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3dd33360-4977-3ea4-9d57-1f2caaad7417 | -14.6716 | -48.3157 | 2025-10-04 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d35143bc-036f-3ee3-95ab-f37ea45a9ee0 | -15.5211 | -46.838 | 2025-10-04 12:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 813b523f-60ab-3d1a-81ec-d8dc8dbaecb1 | -13.9383 | -48.1852 | 2025-10-04 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ce048345-7e53-3668-b8ca-f35dc75c11d7 | -11.5683 | -47.6749 | 2025-10-04 12:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| fa96f046-e2e4-3675-ad41-e4f2b2eac29c | -11.4877 | -46.7696 | 2025-10-04 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 95af9945-9ab5-35b0-afec-479fec143cb2 | -11.4414 | -43.9057 | 2025-10-04 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 00dd407f-1ae6-3032-adb5-185cf3b8cf9e | -9.3382 | -45.772 | 2025-10-04 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3eefd33f-d895-3ba2-9c40-b89bd95cd5eb | -11.5072 | -46.7446 | 2025-10-04 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c43f4631-c18d-337a-ac5d-62cee31ef54a | -12.7194 | -48.5611 | 2025-10-04 12:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| d21c9977-ddb1-3845-baf1-36fccadd3db5 | -14.5941 | -52.4976 | 2025-10-04 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 09deb6f2-6a0c-3a63-ae8a-145fbf22099d | -10.334 | -50.3615 | 2025-10-04 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 33e3ed63-22a0-349c-a8ff-be3396f0aeed | -7.7491 | -46.2944 | 2025-10-04 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 03809a93-b056-3c0b-923d-6fc085be5d61 | -7.878 | -48.2021 | 2025-10-04 12:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 92f95475-8253-3758-8dab-d69c1c4ee71a | -12.9471 | -50.9838 | 2025-10-04 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 8cb93f0e-857b-3977-a7d2-0b0c706c4445 | -9.3196 | -45.7515 | 2025-10-04 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 81aaa235-1239-34d1-a616-f9121b5c062c | -15.5408 | -46.8344 | 2025-10-04 12:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 238.9 |
| fe769f89-c830-3d3f-ae1a-59591e85d6e7 | -9.921 | -50.2109 | 2025-10-04 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| c5c2c579-02fe-3bbd-ae30-8a0a88711bc2 | -13.2934 | -47.6129 | 2025-10-04 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 0e8c17cb-a617-33d9-90a2-180ef4a9f82a | -9.9396 | -50.2304 | 2025-10-04 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 374fd7cd-8a88-3bc9-a8a7-cb0562ed0c88 | -7.813 | -42.5349 | 2025-10-04 12:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 158.3 |
| 03c72fba-0f19-3dca-a827-57dcd73b363c | -13.3127 | -47.61 | 2025-10-04 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 176b8457-5924-3c00-a4e3-2c0523c2736d | -13.114 | -47.9518 | 2025-10-04 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 464417f4-a8e2-35cf-a44a-ea241ea6d711 | -12.6512 | -46.9894 | 2025-10-04 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9671ee0a-3921-37a5-9237-586809e8ac95 | -11.8818 | -44.9815 | 2025-10-04 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| da69c0eb-7daf-38bd-852e-fab9bae7d835 | -7.8593 | -48.2037 | 2025-10-04 12:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| a0c1b689-8c48-3d84-a023-40586d12cedb | -12.031 | -45.2132 | 2025-10-04 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 16748079-5643-3014-b0df-d7f775944cea | -8.9948 | -47.4845 | 2025-10-04 12:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 28769165-725d-339b-8aeb-e21882bb9b19 | -14.2321 | -46.0794 | 2025-10-04 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 708582bd-1e6d-33fb-bc03-ee46b42a4c77 | -10.3343 | -50.3402 | 2025-10-04 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 306.8 |
| 7507f585-8358-3d4e-839c-69b64ed68e78 | -14.5748 | -52.5001 | 2025-10-04 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 230c2e21-3690-3f31-bdc5-0d3f858d0b39 | -13.3233 | -48.077 | 2025-10-04 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 89850804-befc-37c5-a244-4861f802982c | -15.958 | -43.318 | 2025-10-04 12:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 0a43a22f-7f53-349b-b67c-df42e275e429 | -7.7303 | -46.2961 | 2025-10-04 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| cf6fa897-94a6-3127-9111-1d2f338843af | -14.672 | -48.2933 | 2025-10-04 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c9798a16-d0c9-3afc-a118-820850580cf7 | -8.5601 | -47.6373 | 2025-10-04 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |


[Clique aqui para ver as próximas entradas](README146.md)
