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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ea48ed6-d497-34c4-a521-c78ab31dcc9a | -11.8225 | -45.0827 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| de5de23c-72e3-3d4e-8441-82f8c66cd5d0 | -10.3907 | -50.3557 | 2025-10-05 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 5a068d01-9ad8-384d-9611-bcef21dcec38 | -7.8047 | -48.0558 | 2025-10-05 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 89c7b611-a060-3543-a9c1-68cfe15c3be6 | -9.5791 | -46.1286 | 2025-10-05 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| aa153274-0d77-37a9-8725-e89c433f4d24 | -11.8635 | -44.938 | 2025-10-05 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 561d6cbe-20b1-3df8-a349-920faaa89108 | -17.9605 | -57.5904 | 2025-10-05 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 543545be-5034-308d-970b-f2dd9e07c187 | -10.9303 | -47.0882 | 2025-10-05 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| bd3153ed-3c5f-3de6-adbb-edda5b6ca16e | -11.9327 | -46.438 | 2025-10-05 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| b80675c6-c5ef-3a31-9569-c281d797da72 | -19.0155 | -50.6045 | 2025-10-05 13:20:00 | GOES-19 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 245.4 |
| d1425a45-1dfb-3aae-862c-8a7c3a048209 | -7.7935 | -42.5845 | 2025-10-05 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 131.2 |
| 30de0979-e48a-371c-ae66-13eb0c1f796c | -12.5863 | -54.7679 | 2025-10-05 13:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 675e35ee-4bf9-3900-bc2c-304cef538d02 | -7.7933 | -44.1304 | 2025-10-05 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 37c5a7aa-cc30-32b4-a94e-715ad000cac7 | -12.2684 | -49.2126 | 2025-10-05 13:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| dae0079d-e426-382e-8a29-3694aa315e82 | -18.2569 | -53.3329 | 2025-10-05 13:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1e83f91f-bb93-390d-9350-0a65d8518025 | -17.986 | -51.144 | 2025-10-05 13:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 38065e3b-0654-3e2e-b62b-6d6f0db76c32 | -15.1352 | -45.7337 | 2025-10-05 13:20:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 0fbe9a9b-1476-3957-acc2-f5746e1d18ac | -11.8225 | -45.0827 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| db0eee18-c1f6-3ee0-af74-deb6abf68201 | -8.5596 | -47.6813 | 2025-10-05 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 75ecaf26-3e93-3a42-907b-2ea7846665a1 | -7.7306 | -46.2737 | 2025-10-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e873bdc6-5c52-325c-a2c3-b70e2beb48ef | -7.7123 | -46.2307 | 2025-10-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 3cf3001a-4d92-3887-9757-e0784aab7788 | -12.3914 | -51.094 | 2025-10-05 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 35c07977-c7e6-3b42-890a-cf1345de836d | -11.8418 | -45.0799 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 30ece9f5-f337-3d6b-9d5b-e17e5d5f61d1 | -10.0504 | -50.4113 | 2025-10-05 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 539656a7-068a-3dcc-8d37-8ea4bc282bf0 | -18.1769 | -53.3669 | 2025-10-05 13:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 210a0704-5132-364d-8de6-395d20b97649 | -17.9661 | -51.1474 | 2025-10-05 13:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5cf4d89c-ab93-357e-b83a-4c422eca30df | -12.4673 | -45.4925 | 2025-10-05 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6065a812-5b2b-34d5-9335-f77b424fb637 | -9.9207 | -50.2323 | 2025-10-05 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4e14c03d-5d55-36d2-b482-65d3f675277e | -10.3907 | -50.3557 | 2025-10-05 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| fbc7b7cd-1034-3ea0-b9c0-8acd599b15cf | -11.526 | -46.7645 | 2025-10-05 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| e6702e50-2c7a-3e77-bc34-0d2c3769b25f | -11.449 | -43.4803 | 2025-10-05 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c30f548b-3467-367e-94d2-eac0a05be7dd | -8.8803 | -47.6061 | 2025-10-05 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 9ae016e4-fbb1-3555-8d71-739dda6393d3 | -11.7029 | -45.3536 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e2957cd4-d4e5-3b1e-a00d-2c1cebc7a9f7 | -7.7743 | -42.6103 | 2025-10-05 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 227.8 |
| bfabfd2b-e762-38da-be91-9c90661d1514 | -13.7473 | -51.3097 | 2025-10-05 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 045b0e00-38d4-3524-8fa7-f495a8450731 | -11.4298 | -43.4833 | 2025-10-05 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 3750292d-47b0-379c-8ccf-ce5c9d2f39ab | -10.386 | -45.4184 | 2025-10-05 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| d2290673-7374-3ef8-97fa-473dab7f3e95 | -17.9404 | -57.6134 | 2025-10-05 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 85fe00ca-4d4c-3e04-96b9-997c037845f7 | -18.1968 | -53.3638 | 2025-10-05 13:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b1767e7d-e7fe-34cb-8e78-b43ad204b66a | -7.7308 | -46.2513 | 2025-10-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 4c27bad0-bcf5-33b3-87f2-2a60ad0d871a | -7.7311 | -46.2289 | 2025-10-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 94fa2cfb-7157-3a42-9f07-cbc4843136f0 | -13.728 | -51.3122 | 2025-10-05 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 254.1 |
| 003ad67c-9519-3b30-b707-c90f91662ed9 | -11.8442 | -44.9408 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 61fd1a8b-cb96-3f0a-ab39-f3308cdc9d50 | -9.2973 | -46.0026 | 2025-10-05 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 90c0663c-2bf9-3e5c-b899-593a38d8093c | -7.7938 | -42.5607 | 2025-10-05 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| d4473eb6-4fdb-33dc-a27d-5a3080c5efcd | -10.1943 | -45.5339 | 2025-10-05 13:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| fc5f92b1-54e3-31ca-93a5-34f7739c57a9 | -9.5794 | -46.106 | 2025-10-05 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| ca501335-8397-3ece-a4fa-f41094cf554b | -10.9303 | -47.0882 | 2025-10-05 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| fb76d2ab-5844-3818-b62a-b1219a617db2 | -7.8127 | -42.5587 | 2025-10-05 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| dc922a9e-e810-3461-a593-0e6c7155c72b | -7.6993 | -42.5708 | 2025-10-05 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 36723101-c38f-3cd2-81ce-406ff2a52eb6 | -7.4669 | -43.0674 | 2025-10-05 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 166.4 |
| da0123ec-4063-3dba-b6a7-b58d96625da2 | -17.9612 | -57.5492 | 2025-10-05 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 5a4008d8-e221-3823-be93-213e855e106e | -10.8093 | -48.8229 | 2025-10-05 13:20:00 | GOES-19 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 8ee45c59-dfcd-32a9-ab61-e07dd87a736a | -7.4672 | -43.0438 | 2025-10-05 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 2bdee6da-cc8c-3bca-baad-b8bff4575e35 | -10.4054 | -45.3931 | 2025-10-05 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f0a3dcaa-2a19-3769-bb5f-2d6b91267df3 | -8.5384 | -46.3304 | 2025-10-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ee34e62b-082b-3ea7-9891-dc498b9f646b | -7.7932 | -42.6082 | 2025-10-05 13:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| ce6bfb0d-fd2b-3fdb-a135-7c8c57aca30e | -12.5672 | -54.7698 | 2025-10-05 13:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 79cad7ec-635b-391d-8028-763ac42b958e | -15.582 | -52.5129 | 2025-10-05 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 366ccce3-7f04-35f0-be80-3a2e1b2f8744 | -11.5264 | -46.742 | 2025-10-05 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 19e946a4-077f-3c27-8ae4-7b79b7640d31 | -15.6015 | -52.5102 | 2025-10-05 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |
| a8f96660-a312-33c7-bdd9-ec08838bc804 | -9.2439 | -51.8133 | 2025-10-05 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e4ee0b5f-df6d-3157-903a-909f28fcac53 | -8.4683 | -45.9106 | 2025-10-05 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b2c1f8b0-94eb-3049-b775-c44ba37c09a6 | -7.5078 | -41.2719 | 2025-10-05 13:20:00 | GOES-19 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 227b8161-0a47-36ab-8d30-4bff4085744d | -9.6287 | -46.6394 | 2025-10-05 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 166.6 |
| b4faad1d-7db7-3d19-84df-c6041e7b1f1d | -11.5069 | -46.7671 | 2025-10-05 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 5e79193a-64bf-3648-a293-3f3b784ad716 | -11.823 | -45.0596 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| a3cc5651-c03e-3c42-923a-26383271b6f1 | -11.0978 | -49.8513 | 2025-10-05 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| bc5d4260-76d1-3847-89b2-84886097ea99 | -7.7746 | -42.5865 | 2025-10-05 13:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 124.5 |
| cc3c424f-7ab0-34ac-b1e9-71cefcd24ca7 | -7.712 | -46.2531 | 2025-10-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 408.9 |
| 790f32f5-2841-3476-89a1-7389a4316326 | -9.3276 | -54.5215 | 2025-10-05 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9a9e7ef0-10f2-3bd9-aeb9-7e9f155146d4 | -16.077 | -51.0859 | 2025-10-05 13:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| fb3358ef-61cb-314b-bcb4-39f4a3437dc0 | -12.2497 | -49.1932 | 2025-10-05 13:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 47396b2c-0994-38d6-94ed-6233db81977b | -7.4276 | -46.5239 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3fc2f67c-6a3a-389b-bc72-8652b0203589 | -12.2876 | -49.2101 | 2025-10-05 13:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8267f7bf-c126-3de3-8887-372ea1bc802f | -11.8635 | -44.938 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 187.2 |
| ecbd2c65-8588-3fa4-b590-f71a3b5ed40e | -7.2577 | -44.8938 | 2025-10-05 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9759f487-51ed-3272-82dc-c5e9e9fbf7f5 | -12.2688 | -49.1907 | 2025-10-05 13:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 802fbe97-691b-3ef8-adfb-8a67b595b490 | -8.468 | -45.9332 | 2025-10-05 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3ab8a2ff-0ad6-3010-9024-2911c7c93efd | -7.8047 | -48.0558 | 2025-10-05 13:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 10b491b3-849c-3b3b-aed1-78083dc438d1 | -11.8422 | -45.0567 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 3783c5e3-aaf3-30b5-9dcc-a18b87bf4286 | -13.7284 | -51.2908 | 2025-10-05 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| d45e3392-9ece-354a-90b6-542a960fcfb8 | -7.7885 | -44.5228 | 2025-10-05 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 4b4a4bea-bd59-31b0-b57f-f4e85574f06b | -10.9497 | -47.0634 | 2025-10-05 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 8ed0f658-916d-3778-b4bd-c65844ee7318 | -16.0966 | -51.0829 | 2025-10-05 13:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 6797e23f-9f06-3fe6-bf05-3cd8cbe908f0 | -15.5824 | -52.4916 | 2025-10-05 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| f4ff2e89-cd81-3768-a9e5-a89252821df3 | -10.93 | -47.1106 | 2025-10-05 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 199.2 |
| 1b7017aa-5199-3268-a096-ac4983eb517c | -17.9408 | -57.5928 | 2025-10-05 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.0 |
| d7c6ca3d-4306-3c70-9a2e-649ec29a4392 | -12.4669 | -45.5155 | 2025-10-05 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 52de211f-8d56-36a2-a160-4ba509f15988 | -11.1168 | -49.8492 | 2025-10-05 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 362d4d01-30d7-3986-9baa-5a369c25aef2 | -17.9605 | -57.5904 | 2025-10-05 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 4f298b07-fab0-34f2-b443-e47d315e087c | -11.8033 | -45.0856 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 21ed3b79-832c-3ee8-ba47-60be33e0c540 | -14.5755 | -52.4576 | 2025-10-05 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| e4cf51d5-0571-3ebc-8e4d-209fa5487140 | -11.0313 | -46.7171 | 2025-10-05 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| ec73cad2-37f5-307f-a941-0b6e21fb63cd | -11.863 | -44.9612 | 2025-10-05 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 0e8f7399-44e2-31ec-82be-d99f3f5a72fa | -11.0316 | -46.6946 | 2025-10-05 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| df7fd1ec-ff05-3759-acaa-cbfacdd4e3cd | -12.6913 | -45.8482 | 2025-10-05 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| e97e2735-6f77-3a89-9803-e4cb1ea4a2d0 | -8.5407 | -47.6831 | 2025-10-05 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a3a70e56-50fb-3553-bfea-913d903e142a | -7.7118 | -46.2754 | 2025-10-05 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 27396f73-ad32-3f6b-b291-f82e10d5745c | -21.6882 | -50.0788 | 2025-10-05 13:30:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| d51ee8e7-c425-31f3-a99a-dfd6e396d692 | -11.1168 | -49.8492 | 2025-10-05 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |


[Clique aqui para ver as próximas entradas](README158.md)
