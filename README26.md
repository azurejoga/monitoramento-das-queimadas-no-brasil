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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df6be32f-1224-34ff-bac3-f327fc15bc03 | -19.78104 | -47.38645 | 2025-10-21 12:02:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cdd50a23-11d6-3d63-8e91-64f003f000b3 | -26.86853 | -49.74661 | 2025-10-21 12:04:00 | TERRA_M-T | VITOR MEIRELES | SANTA CATARINA | Brasil | 4219358 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 68137563-9183-33dd-b348-1197fe1bf288 | -33.18108 | -53.19933 | 2025-10-21 12:04:00 | TERRA_M-T | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 7.1 |
| 188c9627-0d0a-35c3-bab9-7ffa80d73964 | -33.18571 | -53.19381 | 2025-10-21 12:04:00 | TERRA_M-T | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 6.0 |
| c48166c8-956d-3ec8-8197-a76b01f26edf | -26.87035 | -49.73539 | 2025-10-21 12:04:00 | TERRA_M-T | VITOR MEIRELES | SANTA CATARINA | Brasil | 4219358 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e84c8009-5c84-328c-859f-bc6241cbac64 | -17.4131 | -55.0678 | 2025-10-21 12:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 130.7 |
| 45a8e04c-4731-3aff-ae49-e27c15666a18 | -17.4332 | -55.0441 | 2025-10-21 12:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 2c0d2d0e-604c-30e6-b047-2e4982ea6456 | -17.4529 | -55.0414 | 2025-10-21 12:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 08a8ac4d-dd68-38e3-948b-9fa2fdfcf704 | -17.4131 | -55.0678 | 2025-10-21 12:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 5d9d3475-3dd0-390d-a46d-a3eed1e82ba2 | -17.4332 | -55.0441 | 2025-10-21 13:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 77f7c011-84fa-33ba-99c2-451576afcb6e | -17.4131 | -55.0678 | 2025-10-21 13:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| d2d0e0b6-676b-3ee6-ae04-b052457e2b5c | -17.4332 | -55.0441 | 2025-10-21 13:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 122.9 |
| 432967c9-01ca-33e2-abb2-f4b59fd2f743 | -17.4529 | -55.0414 | 2025-10-21 13:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| aa237d3a-35f7-3c6d-914c-613a550d4a41 | -17.4131 | -55.0678 | 2025-10-21 13:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| ada481b1-494d-33d4-b7a3-34e777f00def | -17.4332 | -55.0441 | 2025-10-21 13:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| c883ae91-0cc9-3383-a086-b96b472c05b4 | -17.4529 | -55.0414 | 2025-10-21 13:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 340ce909-053b-3662-85b5-fb25e0f17954 | -17.4131 | -55.0678 | 2025-10-21 13:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| f5d7bae3-d8dc-377d-af1c-accc025fd9fe | -17.4332 | -55.0441 | 2025-10-21 13:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 200.9 |
| b5d0f5c1-2d2e-3d03-b669-fbe760aa6f6e | 1.4453 | -50.7446 | 2025-10-21 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 74fcb0eb-8cc6-32f7-864f-882ce52ec6da | 1.4453 | -50.7655 | 2025-10-21 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 5fdd94f2-b9ad-3c67-8f75-86908ec47ce9 | -4.1525 | -42.1989 | 2025-10-21 13:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| ae99cfea-b24c-3ca6-abe6-3710b58ac1a0 | -17.4529 | -55.0414 | 2025-10-21 13:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 73b2f191-7016-3d98-9421-ef55517a36a6 | -17.4332 | -55.0441 | 2025-10-21 13:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 166.9 |
| 3c38d67f-f60f-39ff-9460-cdc7645c2ac3 | -17.4131 | -55.0678 | 2025-10-21 13:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| e4d1ffe5-fba7-3974-bd25-32f1e8a7accc | -4.115 | -42.2011 | 2025-10-21 13:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 2117571c-3b31-3c74-adfc-c9e4a20208b0 | -4.171 | -42.2215 | 2025-10-21 13:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| ec5bfec1-3cb1-3722-af18-805ab6972e0b | -4.1526 | -42.1752 | 2025-10-21 13:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| d3de9458-b836-3808-90de-da25a35283e8 | -17.4131 | -55.0678 | 2025-10-21 13:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| 2fbd3122-f356-3846-bba9-53e816cd24ff | -4.115 | -42.2011 | 2025-10-21 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| b0086fb9-1901-3657-b105-a34c632238d6 | -17.4529 | -55.0414 | 2025-10-21 13:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 5c7024de-b058-3aa7-a044-4d50676d9b4f | -17.4332 | -55.0441 | 2025-10-21 13:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 170.3 |
| 68f3683e-7b50-36d0-8477-3f0759c8237c | -19.0918 | -57.5304 | 2025-10-21 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| f1ea79c3-2492-3938-bc71-b15e89d05de9 | -4.1526 | -42.1752 | 2025-10-21 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| d0a448c3-a147-3fa0-8373-948d3ece9eee | 1.1133 | -51.1437 | 2025-10-21 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f04b0b00-6630-358b-9bf4-da425565549f | -17.4332 | -55.0441 | 2025-10-21 14:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 164.8 |
| 7142911d-aa65-377d-88d5-ffa328221fb3 | -4.1526 | -42.1752 | 2025-10-21 14:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 057c53f5-4462-39b5-8105-654b942e3235 | -19.0918 | -57.5304 | 2025-10-21 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 95.9 |
| de90a378-44d4-3c02-a552-16880dba309a | -4.1525 | -42.1989 | 2025-10-21 14:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| c4b036d2-0ddf-3d3b-93f3-7578e8c0d472 | -17.4529 | -55.0414 | 2025-10-21 14:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 02b48536-0b16-3744-bc3a-d0f03e1e399c | -3.8372 | -41.7644 | 2025-10-21 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 0fe037b8-9e47-3182-9b53-01a9d904cf01 | -17.4135 | -55.0468 | 2025-10-21 14:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| db895e68-282d-3d7f-9be3-a4e011d9d99c | -17.4131 | -55.0678 | 2025-10-21 14:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 131.6 |
| f31345cc-cc9e-3066-a714-beaf1e3ad4cf | -17.4135 | -55.0468 | 2025-10-21 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| bba41c96-2c0a-3b48-a313-ab3c7832531b | -4.1526 | -42.1752 | 2025-10-21 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 0fa0e22a-98e4-311f-bced-5caa2018e758 | -17.4131 | -55.0678 | 2025-10-21 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 9343ac63-fe62-3e57-83e0-8d9b92010abd | -17.4529 | -55.0414 | 2025-10-21 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 2241bdfc-05c4-34e2-9d24-afc33abfdfcd | -4.1338 | -42.2 | 2025-10-21 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 350ff168-990c-3b21-b8c2-215f9ef120b2 | -17.4332 | -55.0441 | 2025-10-21 14:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 170.0 |
| c4e549d7-f6c4-3b55-be6a-e83f9a6f3ea9 | -19.0918 | -57.5304 | 2025-10-21 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| deb2d430-cadd-3d0f-9958-17785b741b89 | -17.4131 | -55.0678 | 2025-10-21 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 121.6 |
| 4b9d2a91-aff1-3b04-9f70-5168168a89ed | 1.1133 | -51.1437 | 2025-10-21 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3bde21b6-a833-3b5c-baca-24a24ce36a4f | -17.4529 | -55.0414 | 2025-10-21 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| cb1549f0-7460-3407-b692-b93049b7eabf | 1.4453 | -50.7655 | 2025-10-21 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 311f198f-7c5d-3a54-b457-c76b61c3d5c8 | -17.4135 | -55.0468 | 2025-10-21 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 48bbdddc-507e-3611-b698-cc76b1020212 | -17.4332 | -55.0441 | 2025-10-21 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 136.0 |
| 07512142-dd79-3409-a7f5-fd0bd745e6fd | -17.4135 | -55.0468 | 2025-10-21 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 513cce65-5e74-372f-84d2-ea656eb82d7c | 1.4453 | -50.7655 | 2025-10-21 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 965d1760-2e58-30c6-9325-7a77660bcbc8 | -17.4332 | -55.0441 | 2025-10-21 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 145.8 |
| 21d8c535-e3ce-3c69-bd59-b094c9f38aed | 1.1133 | -51.1437 | 2025-10-21 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 90.2 |
| b5059a7a-f595-3f5a-892b-df33cdf093a3 | 1.4453 | -50.7446 | 2025-10-21 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6b0b5c94-8405-3469-916b-cd16ec84db82 | -17.4131 | -55.0678 | 2025-10-21 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| 7a676565-a3af-3ea3-a4ae-209c4752cc11 | -19.0915 | -57.5512 | 2025-10-21 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 115.9 |
| 0059e4f4-4103-3da1-89d9-f65f665ed9d8 | -17.4529 | -55.0414 | 2025-10-21 14:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 1f0bae54-6d6b-3fba-ba77-e4fd1b7f4f19 | -19.0918 | -57.5304 | 2025-10-21 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 204.5 |
| 9d9990e3-f354-3612-95ab-0fd538c13728 | 1.4269 | -50.7449 | 2025-10-21 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 3638fbf9-7696-39f6-920f-3ae4054f2097 | 1.4453 | -50.7655 | 2025-10-21 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 09e4cdfc-40d7-335f-8514-a0a0a3622e34 | -17.4135 | -55.0468 | 2025-10-21 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 4d435b88-4465-3c98-8748-0b14336820d1 | -19.0915 | -57.5512 | 2025-10-21 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 65db4a46-1e39-3705-8d19-0e1a9e9e3721 | -17.4332 | -55.0441 | 2025-10-21 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 164.3 |
| f85953c8-92e6-3169-b144-ebf99c83b216 | -19.0918 | -57.5304 | 2025-10-21 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 166.0 |
| 3a31e448-e295-34e5-a3fe-4584387fdf44 | -17.4529 | -55.0414 | 2025-10-21 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 72a5deb9-ce72-3da9-bf61-02e38a917bca | 0.8925 | -51.1251 | 2025-10-21 14:40:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 7db1ad24-9ca8-30e4-a1df-3065beb6a9d7 | -17.4131 | -55.0678 | 2025-10-21 14:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 134.5 |


