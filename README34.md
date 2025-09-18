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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02dbe2b2-99d1-35d8-92d0-173bbf4b6316 | -8.7863 | -46.1029 | 2025-09-18 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8f43a6b9-4450-32ea-bd32-f7a78c0cd770 | -7.5993 | -44.6102 | 2025-09-18 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 4d61c11f-4005-363a-bf0f-4c5acef5992a | -8.6268 | -45.3054 | 2025-09-18 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 548abaf7-da20-36dd-b620-cacf5c1e0fb0 | -8.7073 | -46.3804 | 2025-09-18 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 47fd1c4d-2020-315b-bc76-7ef3e32efc62 | -8.899 | -46.136 | 2025-09-18 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 73c78d16-f51d-39cd-9224-5ad4f3d3286c | -17.1976 | -45.9089 | 2025-09-18 12:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| f9d75e6b-8767-3663-a7d2-247061089e8b | -17.1777 | -45.9131 | 2025-09-18 12:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 166.6 |
| ee432ed1-32c8-36ee-bdc9-06108efcf5d5 | -8.7076 | -46.3579 | 2025-09-18 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2b6ea4f6-7136-3cea-8fde-ec0a83bb9036 | -8.6504 | -46.4086 | 2025-09-18 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| cd97817a-627c-347b-8745-a9d5e4350441 | -8.7073 | -46.3804 | 2025-09-18 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6405d2e9-9f0f-3a0a-a6c6-d63f186bd24f | -7.5162 | -45.3024 | 2025-09-18 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c3f8e616-93f3-36ee-839a-702fbbb6d3a1 | -9.1883 | -47.0884 | 2025-09-18 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 37fe7bad-81cd-368f-8b75-031d28f2b4cd | -9.1886 | -47.0662 | 2025-09-18 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| efeba474-b6da-30d8-86b9-8f15e9b6dab4 | -12.1152 | -44.8072 | 2025-09-18 12:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c6065f47-3ffc-31f9-8205-7219a4af3c48 | -10.6551 | -46.4501 | 2025-09-18 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 47816a23-285d-367d-970b-7e6792cdb87b | -10.6741 | -46.4477 | 2025-09-18 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 81635d73-cc88-332a-b7eb-4c8b853b0787 | -7.5598 | -44.7743 | 2025-09-18 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 29a76981-0f48-3e6d-9258-82615f2243e8 | -8.0281 | -44.957 | 2025-09-18 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 8995e638-ab16-357b-bc12-d3ecc86ba2e6 | -17.1976 | -45.9089 | 2025-09-18 12:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 292b0cfb-8bf4-3fc0-8f13-a6dc26dd2200 | -8.899 | -46.136 | 2025-09-18 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| f72a482a-ccbe-38c1-97c3-754d3b8b7200 | -8.4645 | -44.7286 | 2025-09-18 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 710b0c15-72db-38e1-908e-59be27a71fa6 | -8.0095 | -44.936 | 2025-09-18 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f01bf5b5-7577-3986-9b44-b43a5b20e433 | -8.6268 | -45.3054 | 2025-09-18 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| a61b6065-7e7c-33bd-9d22-c06a3e739a38 | -17.1777 | -45.9131 | 2025-09-18 12:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 9aa8729e-6d53-3ca4-83c1-87640412f4c5 | -8.9347 | -46.2894 | 2025-09-18 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 885013a5-787f-3a90-ae2b-329d3f0212bb | -18.5781 | -45.0334 | 2025-09-18 12:50:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ced7f6b9-e7bd-319e-9fa3-614593726234 | -7.5598 | -44.7743 | 2025-09-18 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c8c1bab0-f81d-31de-87d8-3701abd3bfdf | -8.0092 | -44.9589 | 2025-09-18 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 9dcce53d-8cd3-3b6c-80fe-19a717f700d0 | -7.5162 | -45.3024 | 2025-09-18 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9f90ce15-05d5-35c0-8ccb-0516b2abb960 | -8.7262 | -46.3784 | 2025-09-18 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 3e6593e9-ec13-3477-aa39-2fbf56a5a677 | -10.6551 | -46.4501 | 2025-09-18 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 61fe4fc4-879f-32a0-8385-8455831722ba | -8.899 | -46.136 | 2025-09-18 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| ae626c95-95e3-3f4e-b5b3-74084fb3ce28 | -8.6885 | -46.3823 | 2025-09-18 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 79c8a09f-3929-3ef6-bba5-bde593f32fdf | -5.642 | -45.4087 | 2025-09-18 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1838f816-592e-3ebb-a581-b0c73f59b96e | -7.5601 | -44.7514 | 2025-09-18 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c417345e-b10e-3cd7-87b2-7acc7fc46958 | -8.7076 | -46.3579 | 2025-09-18 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| a1cbf012-32d1-308a-b031-abb938bdf16e | -10.6741 | -46.4477 | 2025-09-18 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 3371e98a-11b9-3c62-b0b6-a00201db6877 | -9.2084 | -46.9974 | 2025-09-18 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| ed8b9838-6d37-39a7-aa22-1214bf27f680 | -9.1895 | -46.9994 | 2025-09-18 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| e5039abd-4d30-3414-9cb3-90e12ccf0941 | -8.7073 | -46.3804 | 2025-09-18 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| fcab2ca6-60f5-3181-9266-460f28d90de1 | -13.1626 | -42.5468 | 2025-09-18 12:50:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 93.5 |
| c7e941a3-8742-34d7-880d-4085b9802476 | -8.0095 | -44.936 | 2025-09-18 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 60ea6747-d5c2-393b-a249-886e676841e1 | -8.6268 | -45.3054 | 2025-09-18 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| f91e0f5a-bd82-30e3-b861-769f0ee1b5c3 | -8.9179 | -46.134 | 2025-09-18 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5c91b2f5-2214-357b-9d20-43cfce050fa6 | -9.1904 | -46.9326 | 2025-09-18 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3fa39db2-20b1-3cb2-8d6f-ea83dfa28291 | -8.0281 | -44.957 | 2025-09-18 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 705fd62d-25bb-372a-8268-5ffbd70716e5 | -9.1901 | -46.9549 | 2025-09-18 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 79362691-db18-31c5-9036-348619e4991a | -8.669 | -46.4291 | 2025-09-18 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 015a6bf0-bf97-3eec-915b-ae9246313576 | -8.6687 | -46.4515 | 2025-09-18 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 91cfd511-cfe7-3e60-bf68-e2fb9628b605 | -8.6268 | -45.3054 | 2025-09-18 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 8ca41326-4440-31af-a199-827e092cd91f | -9.01 | -46.3039 | 2025-09-18 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| e5a22735-ef43-39db-8c2c-19c2d29c94ac | -19.5869 | -57.7765 | 2025-09-18 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 74555e7e-b86f-3615-81dd-af829b9771aa | -7.5162 | -45.3024 | 2025-09-18 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 363fb3e0-7357-33b2-bf2e-76e1a6399376 | -9.1895 | -46.9994 | 2025-09-18 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| bcdaaaa1-af60-37f7-8704-acaeb59654e9 | -8.899 | -46.136 | 2025-09-18 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b4c7d34a-483f-3919-8b01-0be47bc37827 | -8.9638 | -45.519 | 2025-09-18 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| f1494b1e-2de7-3981-a6a4-16e30aed06cf | -8.9347 | -46.2894 | 2025-09-18 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 0831c87c-12e2-3932-a4bc-08993ef9a3fa | -10.6551 | -46.4501 | 2025-09-18 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 241.1 |
| c6c12e58-cc3d-3a6b-9db8-abfac226340d | -10.6741 | -46.4477 | 2025-09-18 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| bc9bdac0-7203-3cd7-91d3-481f8ea82585 | -7.5993 | -44.6102 | 2025-09-18 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1f337dcc-686b-325f-95cc-670c88e80e40 | -7.5412 | -44.7532 | 2025-09-18 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b25069f8-f2bc-3523-84c1-35060a9114ee | -8.3334 | -44.6507 | 2025-09-18 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ca7de9ee-8631-34a7-81ff-3915fcbd32fb | -7.5598 | -44.7743 | 2025-09-18 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 19abd564-1b36-3663-9e5f-d59d4e373953 | -6.9805 | -44.484 | 2025-09-18 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1037a451-9a20-38d9-a518-268ffe7ea610 | -8.0095 | -44.936 | 2025-09-18 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e06a6fcd-b95f-360d-bbb9-3ffbc7ff10d1 | -8.9719 | -46.3304 | 2025-09-18 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 453f195d-901a-3127-8b2d-aaa3f6772082 | -8.9911 | -46.3059 | 2025-09-18 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| c91bd22f-7c09-3195-a7bf-aa0bc88b9923 | -9.2084 | -46.9974 | 2025-09-18 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 6803d9d8-ed3e-31b0-b089-0f75d6c24bc5 | -8.0281 | -44.957 | 2025-09-18 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 396.7 |
| 89150933-2e3c-3f07-8bc5-63a37ed53287 | -8.0092 | -44.9589 | 2025-09-18 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 0c05ae87-1cec-3e95-bc9b-c29920d4d702 | -9.1901 | -46.9549 | 2025-09-18 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 85c900a1-2225-31bc-83cb-46173e615330 | -7.5601 | -44.7514 | 2025-09-18 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 252a1730-5067-3085-9a61-140da61cabe6 | -9.0481 | -44.8706 | 2025-09-18 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 87381e9c-8b32-3e2d-977f-ca03e7ddb181 | -6.0069 | -44.3354 | 2025-09-18 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a625dcab-3db1-3103-a3af-174e25a75bf7 | -8.9722 | -46.3079 | 2025-09-18 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c35598ef-88ca-345c-90e0-88cc736be112 | -7.5162 | -45.3024 | 2025-09-18 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 462916f1-54bc-31ea-b7a0-8891383325dc | -9.2084 | -46.9974 | 2025-09-18 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 2244a9e8-57aa-38cd-ace1-c8ce1004289f | -8.9719 | -46.3304 | 2025-09-18 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 11ded7a3-d856-35c1-911e-dc7abb019e84 | -8.899 | -46.136 | 2025-09-18 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fe2c6ecf-33f4-30df-ae52-6a9d8d3b093c | -8.6885 | -46.3823 | 2025-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 432e815f-3036-3ae6-a4a2-99a394adb5cc | -7.5598 | -44.7743 | 2025-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 94b8b147-5ca2-3f78-8b6a-33b5164bc350 | -8.7076 | -46.3579 | 2025-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b1e55d69-d5ca-36a7-a49b-42d41f4237e9 | -6.0599 | -44.6747 | 2025-09-18 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2e37c5b4-9cb4-3a15-934d-fac3d53bf6fd | -15.8236 | -59.3816 | 2025-09-18 13:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 37de583c-a7c5-315d-a089-1f056f767b47 | -6.9024 | -44.7656 | 2025-09-18 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 80b8c6d7-e7ef-3d4b-b31d-5aae5d0a7da1 | -7.5412 | -44.7532 | 2025-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 63232e0c-bd4f-359f-9869-5ab4b2deb643 | -19.5869 | -57.7765 | 2025-09-18 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 8bd777a2-b221-3006-8a5c-a2cd1cccff32 | -8.7262 | -46.3784 | 2025-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| df6abd0f-5351-34f9-9217-0b1d7cccf9c3 | -8.3334 | -44.6507 | 2025-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 57cf8292-ea4a-35e0-ab76-981a8e202f30 | -6.0069 | -44.3354 | 2025-09-18 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f73bfd8e-3a52-3344-9439-e0c24b7bd30d | -10.6741 | -46.4477 | 2025-09-18 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| cc21323d-25bb-3290-8622-138617c1b4e0 | -7.5601 | -44.7514 | 2025-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8f8a0556-36a3-312a-b3a5-bbe694151026 | -19.5872 | -57.7557 | 2025-09-18 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.3 |
| fc28f9e1-49ed-3e35-a805-551c5ab79592 | -8.6687 | -46.4515 | 2025-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6aa88220-4bc2-3ff4-a366-523a8262cef7 | -7.541 | -44.7761 | 2025-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 77ac81aa-f415-390a-bfc3-bd5e5da55bbd | -8.6268 | -45.3054 | 2025-09-18 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 5c1b91c8-971d-352e-9b71-02742065eb18 | -8.7073 | -46.3804 | 2025-09-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| d57f1d11-7597-3c16-ab50-55b21d0caebe | -9.01 | -46.3039 | 2025-09-18 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 0c04c746-0f0b-34b3-98e1-10c57a8780d3 | -7.5818 | -44.4971 | 2025-09-18 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 0fe7668d-f0e4-37f8-8eac-5ed61762a3ca | -8.9911 | -46.3059 | 2025-09-18 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |


[Clique aqui para ver as próximas entradas](README35.md)
