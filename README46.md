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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82781021-f671-3959-a8d6-d5c50dfa446d | -14.75877 | -46.13859 | 2025-10-12 12:38:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 64bafb48-27c7-3e8a-8236-859cb1459b09 | -14.96177 | -46.71789 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 34eda4b3-91d1-3e3d-a373-3729789e9afb | -10.19043 | -44.61111 | 2025-10-12 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 678.4 |
| 1bdc3952-6da4-356f-83af-704b78600b3f | -14.95122 | -45.59058 | 2025-10-12 12:38:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| c342ad34-573a-3e90-b94a-4ad6dcc18d60 | -10.1873 | -44.63897 | 2025-10-12 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 55784773-abc6-3883-a733-50115424a488 | -14.95799 | -46.69849 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e10cf130-faf1-3538-a56a-d88f7abfdb1b | -14.94549 | -46.73983 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c195506c-3fad-3026-bf0e-876b9cc6b9e6 | -14.41403 | -47.96341 | 2025-10-12 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 5ffb908a-4e72-3908-b210-84732a982c92 | -10.17628 | -44.60482 | 2025-10-12 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 766.0 |
| 7ae757ec-772c-3212-801f-cc9375085e61 | -14.95528 | -46.72413 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e9d14f75-c70e-3c8a-9937-8b8b8ee7041e | -12.13563 | -45.60548 | 2025-10-12 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| d99a2892-2c3b-32e5-885a-d6cae993a7f2 | -14.94828 | -46.71506 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 37.4 |
| ced559bf-3651-398b-b098-70abfe9ba2ea | -15.05433 | -46.64726 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 0213a336-494d-310c-b919-bb51313d519b | -14.96898 | -46.72506 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9bb0e8a8-fcde-3f29-b8f2-d8bc25187ef3 | -15.0474 | -46.64146 | 2025-10-12 12:38:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 064118ff-5cd0-38b0-9f66-17230a3920e5 | -12.13854 | -45.57999 | 2025-10-12 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7d1c9dbe-729a-3b3e-8874-c69447ee18dd | -10.18801 | -44.63396 | 2025-10-12 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 8af051c0-c5e0-3967-8f07-c68c009d5643 | -19.0319 | -57.5382 | 2025-10-12 12:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 125.9 |
| e6c33b6b-87d5-3a5b-8980-f4fd792d3586 | -10.7715 | -43.9564 | 2025-10-12 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| baa3254e-3855-3830-82e0-ab0dad33b298 | 1.1689 | -50.8939 | 2025-10-12 12:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 107.3 |
| e16c3a02-cd76-37c1-a051-ac6dafb44b31 | -11.3629 | -44.0112 | 2025-10-12 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9965af6c-a874-35fe-811c-a055b1da36b7 | -10.7906 | -43.9537 | 2025-10-12 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| aa9aaa07-e70f-371a-827b-16660d7068b2 | -15.28943 | -57.0883 | 2025-10-12 12:40:00 | TERRA_M-T | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8f8297dd-6eb4-3f98-902e-358360408605 | -17.20086 | -46.95962 | 2025-10-12 12:40:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c13d6e05-ce9f-3d88-b224-a0c68278b387 | -17.54488 | -46.52309 | 2025-10-12 12:40:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3fffe29a-9800-36fd-b470-d7f2268a06e9 | -17.19466 | -46.95348 | 2025-10-12 12:40:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2426a46d-4134-3df1-a4ab-9e4161a5711d | -17.87195 | -57.5746 | 2025-10-12 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c6014a23-887c-304b-912b-4613821d3927 | -17.55656 | -46.51773 | 2025-10-12 12:40:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| de54a21c-c0f5-3850-bece-809b5eb0f864 | -21.0975 | -45.73371 | 2025-10-12 12:42:00 | TERRA_M-T | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| 02ff5387-1db3-3cb3-9e61-a675e33c8ef7 | -21.32859 | -54.43613 | 2025-10-12 12:42:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 03e17510-084c-3e52-a306-881787fa90f8 | -11.5062 | -43.4952 | 2025-10-12 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 13a2ae0e-63de-32dd-81d2-644ed02ac402 | -11.3633 | -43.9877 | 2025-10-12 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 88b215da-1e01-3996-a6bb-d160e5e04d68 | -19.0319 | -57.5382 | 2025-10-12 12:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 6b247335-d1b6-3173-9f61-873fb6e5a1f5 | -10.7906 | -43.9537 | 2025-10-12 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 3aa591c5-417f-334b-8824-ba8e3f51afaf | -11.487 | -43.4981 | 2025-10-12 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| fb3df67a-bee7-3465-8a1e-47b8f90f1e56 | -11.3629 | -44.0112 | 2025-10-12 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| f39b82d4-f314-32a0-8d73-4c74c7780f39 | -19.0519 | -57.5356 | 2025-10-12 13:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| e26bd44c-e620-3406-aad2-c76aeaa197a3 | -17.8773 | -45.0285 | 2025-10-12 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 30f4fc7b-e94b-3be8-afb8-4b07b7a5dde8 | -10.7906 | -43.9537 | 2025-10-12 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 4876d550-a25f-327e-aa8f-d1f88d74ee23 | -11.5062 | -43.4952 | 2025-10-12 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 70afb2cc-9ccf-3aca-85b8-88f5a33877ba | -19.012 | -57.5408 | 2025-10-12 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| abf22f27-9029-38b4-9c76-8bb5a1882721 | -19.0323 | -57.5174 | 2025-10-12 13:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 143.1 |
| c2114f66-0673-3658-99c3-129c1521c83c | -19.0319 | -57.5382 | 2025-10-12 13:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 241.9 |
| 713a557d-a194-32d1-a7d2-585de6159ad5 | -19.0519 | -57.5356 | 2025-10-12 13:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 157.3 |
| 174e5030-cd8e-3378-877d-c90cadd00e28 | -19.012 | -57.5408 | 2025-10-12 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 6b0c80c4-dd94-36c9-94b6-8190a2993654 | -9.1024 | -45.0477 | 2025-10-12 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f4e791e7-874c-35a7-ae8b-9803efcf7d6b | -11.5062 | -43.4952 | 2025-10-12 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 293ea92e-f800-3e66-a03d-49375540525d | -17.397 | -46.6595 | 2025-10-12 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e6d15fe5-6d6f-3a69-b922-fbeaeb4f5785 | -19.0319 | -57.5382 | 2025-10-12 13:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 563.6 |
| 32579e50-f6ec-37e3-97c1-ec042fefe648 | -11.3633 | -43.9877 | 2025-10-12 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| e7655425-ab5d-3a12-8b3e-b78421bb7938 | -17.8773 | -45.0285 | 2025-10-12 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c0fae7f3-55b0-3f48-9a33-add345f85da5 | -11.3629 | -44.0112 | 2025-10-12 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 04749989-83df-3682-837d-99f694bd5dad | -19.0323 | -57.5174 | 2025-10-12 13:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 338.6 |
| 95254a42-cc38-3c25-b5a0-870fa05953de | -17.8773 | -45.0285 | 2025-10-12 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 5e5d1284-1db6-34c0-a6bf-047b8bde05ae | -17.192 | -46.9324 | 2025-10-12 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 0bab0cca-4e1b-3f61-a24d-73c2b4506341 | -11.5062 | -43.4952 | 2025-10-12 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| a882649a-b6f8-3c6f-b883-42cf20a9519f | -9.1024 | -45.0477 | 2025-10-12 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 79addd4f-8296-38b7-b0b6-11de4fff7c16 | -11.3633 | -43.9877 | 2025-10-12 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 52f39558-7b06-3dd8-97b9-c5ec66fb4164 | -9.1214 | -45.0456 | 2025-10-12 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 9d7a51d7-191d-30dc-9481-69156a474167 | -17.1914 | -46.9556 | 2025-10-12 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 828aac16-4314-3857-9df7-67a27d970f89 | -17.8773 | -45.0285 | 2025-10-12 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 121.2 |
| b1996167-79e6-3212-98c6-0785923aec9a | 1.1689 | -50.8939 | 2025-10-12 13:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.6 |
| aad7059b-4d94-3aa9-bdc5-000fa95cd7bb | -9.1024 | -45.0477 | 2025-10-12 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 234.1 |
| efb8c344-d4c4-3a6a-9da6-70c2e9c82aa6 | -19.012 | -57.5408 | 2025-10-12 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 361.9 |
| 2b6f41d8-de80-35a7-a15f-da525fa45be5 | -9.1211 | -45.0685 | 2025-10-12 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 328.4 |
| ba739807-859d-3b84-990e-da4ea990a84c | -17.1914 | -46.9556 | 2025-10-12 13:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 281.7 |
| 969ad979-5fd6-34e0-b432-aa805a3df070 | -19.0515 | -57.5564 | 2025-10-12 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 148.7 |
| b03a9811-b1f8-34e8-9e28-9350722fd8cf | -19.0519 | -57.5356 | 2025-10-12 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 786.8 |
| f6cd514b-6950-37d3-a880-9570d6bb6bdc | -19.0319 | -57.5382 | 2025-10-12 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1293.7 |
| 872ed9c4-a77e-3fb5-bb56-b8cb82886efb | -19.0316 | -57.5589 | 2025-10-12 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 226.8 |
| 16b7cb07-1edc-3b12-b58d-33d444265684 | -17.6397 | -46.4929 | 2025-10-12 13:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 1698fa88-199b-3e7b-b83d-a1d6599083d1 | -9.1217 | -45.0226 | 2025-10-12 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 59da914c-5de4-336f-b52e-6dd12e924ea3 | 1.1689 | -50.8939 | 2025-10-12 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1bd3443a-2d62-3442-870b-4f08a14f00b1 | -17.1914 | -46.9556 | 2025-10-12 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 181.2 |
| a6b647da-be40-300b-855d-3c2997a9354c | -9.1217 | -45.0226 | 2025-10-12 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 825db40d-2f71-3f36-addb-fcfed0e06840 | -17.6397 | -46.4929 | 2025-10-12 13:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 396040f0-4318-303e-80cc-ef064221855b | -9.1024 | -45.0477 | 2025-10-12 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 166.3 |
| c594fcc4-5525-34ed-9926-b80b1d26f919 | -19.012 | -57.5408 | 2025-10-12 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 410.8 |
| 10f6fd03-9ae1-362d-bd72-d6e2e4faaf05 | -17.192 | -46.9324 | 2025-10-12 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 1f6c9338-b9f1-3ee7-a60f-0658f1723084 | -17.8773 | -45.0285 | 2025-10-12 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 2bdf3f27-7627-3aca-b02c-c6e5c2d3d2c2 | -9.1024 | -45.0477 | 2025-10-12 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 6c97b1d3-33fe-3410-9ee5-cff946c18dca | -8.4037 | -45.0555 | 2025-10-12 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 6a4ac2e1-b127-3d0d-8620-980a4ececae2 | -8.4034 | -45.0783 | 2025-10-12 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 2a3a4b02-7705-3c38-8e07-dfbf0a97e029 | -17.8773 | -45.0285 | 2025-10-12 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8673ba36-8c4b-3b60-a9c2-47d15c017758 | 1.1504 | -50.9149 | 2025-10-12 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 5ed0ff96-2adb-36cc-a580-3b010c4cb0a8 | 1.1689 | -50.8939 | 2025-10-12 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 36a02eb5-c3e7-3256-8702-564cdf9f71a7 | 1.1688 | -50.9147 | 2025-10-12 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 3736c1dc-3848-3270-ab9c-db2c9b936f3c | -9.1024 | -45.0477 | 2025-10-12 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 558a94f0-e869-3a09-b73c-9b361786215d | -11.5058 | -43.5189 | 2025-10-12 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 69063487-975b-3a64-946f-01509a52215b | 1.1504 | -50.9149 | 2025-10-12 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 39aaf9e4-ffa6-3684-8c4d-52cfbf1b7374 | -17.6397 | -46.4929 | 2025-10-12 14:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 1950a511-2ecf-30b4-8d4a-3c59bb820e73 | -17.8773 | -45.0285 | 2025-10-12 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 177.1 |
| d06ac598-a6a8-3c0a-b4f6-6a889294fee1 | -3.9147 | -44.3309 | 2025-10-12 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 830f6488-0ca8-3b48-a44f-6861babb3ba1 | -9.1217 | -45.0226 | 2025-10-12 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 189.4 |
| bc4e076c-539b-3581-a86b-a175d89efff6 | -4.4051 | -43.5211 | 2025-10-12 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f42a6c34-d21b-30cb-b09e-8fcad203cda6 | -17.8773 | -45.0285 | 2025-10-12 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 148.9 |
| e41e2fd8-0f5c-374d-8933-b869c16d5434 | -11.487 | -43.4981 | 2025-10-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| daf7fe7c-ce5a-309a-b179-bb85eca14c41 | -11.5058 | -43.5189 | 2025-10-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 9841d2e8-2d86-3e60-96f4-919ff03683ca | -4.4094 | -42.9146 | 2025-10-12 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 53f23c50-e86a-3795-8f5a-ae7baf710f89 | -3.9333 | -44.33 | 2025-10-12 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |


[Clique aqui para ver as próximas entradas](README47.md)
