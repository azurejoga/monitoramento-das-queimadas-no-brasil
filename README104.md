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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bc513d0-af13-3f3d-9100-a632fef3f3eb | -25.09545 | -49.16892 | 2026-08-28 17:22:00 | NPP-375 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| afa89e1c-8cc1-3b11-8529-f3062e0481a2 | -21.98052 | -55.93994 | 2026-08-28 17:24:00 | NPP-375 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2bcefd9f-0f44-34b0-899d-0e050714f558 | -22.21164 | -55.97877 | 2026-08-28 17:24:00 | NPP-375 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2eb4c916-40fd-38a0-ad69-10806a47100b | -17.34027 | -42.82278 | 2026-08-28 17:24:00 | NPP-375 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e4928b0-b90e-3cb9-9fcd-ac0fbf19cda0 | -21.0541 | -44.42897 | 2026-08-28 17:24:00 | NPP-375 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 04ad047b-bae4-338b-908a-994e95a265d8 | -19.06977 | -57.39687 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.5 |
| 399e7edf-3c1e-3a5c-addb-7c5b69d1ca11 | -19.22421 | -57.66623 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| cef65c40-b512-3b17-a631-095ec2154923 | -20.23302 | -49.19564 | 2026-08-28 17:24:00 | NPP-375 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 01ec4c22-cf4b-3fe6-a94f-88b533bfd8a1 | -18.8399 | -47.40051 | 2026-08-28 17:24:00 | NPP-375 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1f11aeae-8b7a-3a9d-80c4-762270b00d48 | -17.27585 | -46.02295 | 2026-08-28 17:24:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| cae1b2d7-8c24-353a-bece-49db6b30999c | -21.9 | -55.4311 | 2026-08-28 17:24:00 | NPP-375 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9ba9a858-0627-3de8-8873-5d83a9041d0a | -18.43942 | -43.91405 | 2026-08-28 17:24:00 | NPP-375 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b23fdbf-3e5e-3e4e-a4c5-279e874fd50a | -18.83552 | -47.40141 | 2026-08-28 17:24:00 | NPP-375 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58478f33-18c8-3532-842c-a8319189c025 | -19.22737 | -57.66154 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 3151720b-16b0-3771-90cc-dbe4167d1011 | -18.74348 | -46.61631 | 2026-08-28 17:24:00 | NPP-375 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4870ea7b-82c9-3286-8fcf-64ed56541be8 | -17.74091 | -42.25795 | 2026-08-28 17:24:00 | NPP-375 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 75da4b09-af5c-3a8b-b426-192847621db0 | -19.23423 | -57.6562 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| f32b67f1-77f1-3913-9daf-c7ff249f84b3 | -22.0575 | -56.10651 | 2026-08-28 17:24:00 | NPP-375 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4da948c-2580-357e-a8ea-f55fc6e755d9 | -21.04324 | -57.83446 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| e69b8a87-ae33-3c2f-a67b-f8995fe53fa2 | -20.60111 | -56.98826 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 57a8e53a-f899-3bf3-b548-75417ec3dbe5 | -17.06433 | -45.40964 | 2026-08-28 17:24:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9a15cd36-9557-3a5a-8461-59f79ac9fe15 | -20.59556 | -56.98094 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e7143db7-46e2-3203-8f54-54d1cf525851 | -22.20809 | -55.97926 | 2026-08-28 17:24:00 | NPP-375 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0cd9733d-49bd-3c7b-a1f9-94599eac1009 | -24.01014 | -49.05043 | 2026-08-28 17:24:00 | NPP-375 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e994aaa1-eccf-3677-9e81-e4c58dd0b9f3 | -21.04903 | -44.43015 | 2026-08-28 17:24:00 | NPP-375 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| cb9cff77-fe28-3f41-9938-e7d9e3a32d15 | -21.03789 | -57.84157 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| c7e4c475-abe1-334e-8f2e-ad9da21936ed | -20.23281 | -49.19307 | 2026-08-28 17:24:00 | NPP-375 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d9c44222-f087-3551-a637-2e19c6bfd1f8 | -20.47288 | -48.78624 | 2026-08-28 17:24:00 | NPP-375 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9af464d5-2aea-3c63-b4a2-fb07f17840f7 | -17.81099 | -44.33233 | 2026-08-28 17:24:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d54dd791-6257-3378-973a-cedd7857760b | -19.06611 | -57.39741 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.5 |
| 5480e30d-1d97-377a-abd5-5a2766aaea8f | -19.22245 | -57.65294 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 623e4082-b401-3c1d-bcaa-bf0f5196b260 | -22.84659 | -49.34026 | 2026-08-28 17:24:00 | NPP-375 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 559eb53f-d37d-3c78-b016-e3a02e1db792 | -17.93437 | -42.60707 | 2026-08-28 17:24:00 | NPP-375 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2419332f-6bf8-3179-b0aa-1396cb510a5a | -20.69346 | -50.48421 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.7 |
| 5d28e641-7334-3868-bf81-a44839ddfd81 | -22.26654 | -56.06249 | 2026-08-28 17:24:00 | NPP-375 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d8d830b-7ee5-3a5a-9706-eebb45f95e5e | -18.06152 | -44.01191 | 2026-08-28 17:24:00 | NPP-375 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6456acbe-50cb-3787-8413-da15e68bfb77 | -21.05199 | -44.4288 | 2026-08-28 17:24:00 | NPP-375 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| cd02c2b9-3588-3b96-aa3c-ae183f9c8639 | -21.07804 | -56.62408 | 2026-08-28 17:24:00 | NPP-375 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42fab3ed-22a8-38d5-a386-0e363ccff67b | -24.01114 | -49.04775 | 2026-08-28 17:24:00 | NPP-375 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2e41e58-6cbb-3a5c-850f-315460c45bd2 | -20.0195 | -53.00088 | 2026-08-28 17:24:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a14bd56d-6465-3b95-9359-8771f2de70a8 | -23.54371 | -47.30751 | 2026-08-28 17:24:00 | NPP-375 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 956f62e3-41b3-3573-8336-5884620c350a | -20.54583 | -57.24599 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 19122c33-4980-3046-bacc-894070adda71 | -19.23051 | -57.65667 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 52667c36-c5ee-303b-9ac1-542bf1af7dfe | -20.68516 | -50.48508 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 11af2afb-7c3f-3783-a109-f2c9c870ad61 | -20.55321 | -57.24485 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e8796897-ec3f-31fa-b21d-2f408ff5360b | -23.89832 | -50.60021 | 2026-08-28 17:24:00 | NPP-375 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 8f08735a-03d4-384f-bd08-34bee9c1201a | -17.97798 | -50.18782 | 2026-08-28 17:24:00 | NPP-375 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 908ba7b5-4316-370a-852b-39aaade03dc6 | -21.89799 | -41.23241 | 2026-08-28 17:24:00 | NPP-375 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e4c0bad4-eb3c-38c3-8811-456b91cd1903 | -20.46506 | -48.78796 | 2026-08-28 17:24:00 | NPP-375 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 5c58897a-2b6f-3a80-9b42-ed24641b109a | -23.41502 | -47.22581 | 2026-08-28 17:24:00 | NPP-375 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 5abc10e9-1ea1-3146-b85f-4aab2995516a | -19.22797 | -57.66607 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 0d61f8ab-e6e1-33ac-b20a-697ca15b915c | -20.6863 | -50.48569 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 42b10447-3061-3398-8710-5149a019211c | -21.04004 | -57.84001 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 811304c1-d85b-3032-aeaf-b4a367004d3d | -20.68158 | -50.4858 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f01800fc-c505-3b28-b794-d4c9e2e41046 | -19.22481 | -57.67071 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| f9434d9a-3f80-3901-9a39-52076b72426b | -20.90464 | -57.5912 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 99ecc60f-4433-37b2-9dfe-8efaaa56c4d4 | -22.84741 | -49.34491 | 2026-08-28 17:24:00 | NPP-375 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 339a06cc-b7fd-3e3e-9ab9-9ef2f4e75389 | -19.18635 | -44.91604 | 2026-08-28 17:24:00 | NPP-375 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6eb52b93-d98e-3158-917a-ff2f1cd73a57 | -19.06305 | -57.4024 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.0 |
| d6c917af-4070-3917-b88b-9e5adbe3db9f | -19.22362 | -57.66178 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 73861e8e-4ef7-32c0-ab1b-2fb3e72af285 | -22.26713 | -56.06679 | 2026-08-28 17:24:00 | NPP-375 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34197551-7156-3a6e-a1c6-63bad584670d | -17.93379 | -42.60855 | 2026-08-28 17:24:00 | NPP-375 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5b9d2da6-b879-317c-ae8e-77bd1a170534 | -20.6927 | -50.47988 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.7 |
| bc86e0d9-d889-3053-9eb5-31f6dcafefa6 | -18.44645 | -50.18 | 2026-08-28 17:24:00 | NPP-375 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9be13a56-e43c-3bd4-a2e0-571dc5771a5b | -20.46992 | -48.79238 | 2026-08-28 17:24:00 | NPP-375 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c467e9bf-aeb8-334e-adfe-eae49120e6da | -19.22618 | -57.65255 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| e104475e-40ee-31d1-8f9e-7e29d18339aa | -20.56308 | -57.23406 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8555f91a-5d4e-32de-9ad4-edca58fd63df | -17.81024 | -44.32878 | 2026-08-28 17:24:00 | NPP-375 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f1541c91-f7a2-3f99-983e-ac02b98cbc3d | -20.59625 | -56.97991 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4b46a5d6-e9eb-38af-a3d2-4f4cbc4fcb06 | -20.68232 | -50.49014 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f02a773c-02fc-388c-9007-453103b2ef9e | -21.64215 | -49.74632 | 2026-08-28 17:24:00 | NPP-375 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c767ab95-db7e-36b3-9ab2-c05ad6c74514 | -21.05478 | -44.43215 | 2026-08-28 17:24:00 | NPP-375 | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 049f521c-0a43-3527-b0de-1a6b5d7e1af8 | -22.63988 | -52.43618 | 2026-08-28 17:24:00 | NPP-375 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 463e430b-2f8d-3906-87c0-28e8799a823d | -21.20657 | -44.1266 | 2026-08-28 17:24:00 | NPP-375 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 8e2ab7f5-eaf5-3242-8b23-9131ce675298 | -21.90347 | -55.43054 | 2026-08-28 17:24:00 | NPP-375 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d372136c-bc0a-3678-9f7d-ebb80a2ecc02 | -23.20097 | -52.25956 | 2026-08-28 17:24:00 | NPP-375 | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| eb19d932-66d6-3be8-ac90-0d8e00d4a8d6 | -19.22857 | -57.67055 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 32af3b40-6915-333f-8108-3933bce1a80f | -17.30268 | -46.57771 | 2026-08-28 17:24:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 50ed760f-990e-33be-86b0-f9c2c29deedf | -21.54064 | -49.25468 | 2026-08-28 17:24:00 | NPP-375 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ac25a602-e110-3d9e-b726-dcf9447a50cd | -20.81508 | -57.31728 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fce6ebea-8698-3050-b86b-007dc4942735 | -22.21143 | -51.34385 | 2026-08-28 17:24:00 | NPP-375 | REGENTE FEIJÓ | SÃO PAULO | Brasil | 3542404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 29d79523-ec74-3c60-823b-ecc807497bb9 | -22.96091 | -52.59943 | 2026-08-28 17:24:00 | NPP-375 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1000d93c-2761-34d4-8005-c4a296d28b3b | -19.07037 | -57.40132 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 9b3dab6a-edc7-3f2d-ae16-010e5751bd6b | -21.64072 | -49.74771 | 2026-08-28 17:24:00 | NPP-375 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 7e17f239-6dc6-338d-8af0-954e4daed7ce | -22.85108 | -49.34412 | 2026-08-28 17:24:00 | NPP-375 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| deb3f587-fa27-3e52-87b0-70b300c54a23 | -22.64323 | -52.43557 | 2026-08-28 17:24:00 | NPP-375 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 2c7af999-8928-3a59-8dd2-6eff45c34a38 | -23.8814 | -51.4502 | 2026-08-28 17:24:00 | NPP-375 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 36a46a21-1b10-3ce1-a669-cf4a2cb4f09e | -18.48118 | -49.48792 | 2026-08-28 17:24:00 | NPP-375 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 454c118f-cfc1-3790-a3b8-80f5343826d1 | -20.23374 | -49.19811 | 2026-08-28 17:24:00 | NPP-375 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7a371a6e-b766-3f41-bbbd-ad646a9fab18 | -23.25468 | -46.75916 | 2026-08-28 17:24:00 | NPP-375 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 07a33bc2-b5e8-3107-beb6-218135d487da | -19.22304 | -57.65738 | 2026-08-28 17:24:00 | NPP-375 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 3a4f681a-919c-31ec-9091-92d3ede35f12 | -20.68272 | -50.48642 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| e057a055-70d9-3aef-ad2e-005fc52cdd29 | -19.86347 | -55.11909 | 2026-08-28 17:24:00 | NPP-375 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a764536-9c6a-36a8-b1c9-e2b05629f11e | -20.69704 | -50.48352 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 36f3181a-289f-3929-ac4f-930d88669b15 | -20.688 | -50.47998 | 2026-08-28 17:24:00 | NPP-375 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 086fa091-935b-3805-b05b-654f693a50db | -22.85026 | -49.33948 | 2026-08-28 17:24:00 | NPP-375 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a7a620c9-dde9-3052-9504-5f58578a43c6 | -20.91411 | -57.57512 | 2026-08-28 17:24:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 7ad6fa00-ee69-3108-bd84-776f6435f8d8 | -19.59215 | -46.53619 | 2026-08-28 17:24:00 | NPP-375 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4ddb03dc-608e-3c46-a3be-4d70f2a5c670 | -17.74323 | -42.25774 | 2026-08-28 17:24:00 | NPP-375 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 79b0fb54-941a-336e-b898-e6c1a06a7d59 | -21.20555 | -44.12379 | 2026-08-28 17:24:00 | NPP-375 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |


[Clique aqui para ver as próximas entradas](README105.md)
