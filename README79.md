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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdeec329-e2d6-3a64-a393-8021ccb3750f | -18.32244 | -51.68511 | 2025-08-16 12:57:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 565c0c29-4bb4-34d2-b894-9d7bba118d96 | -18.32452 | -51.66732 | 2025-08-16 12:57:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ea8f4ce3-1910-35b8-b045-f6309792ec43 | -18.72646 | -48.18351 | 2025-08-16 12:57:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| fb51bd43-c504-3efb-8543-3cfd37212ed8 | -20.40476 | -54.78416 | 2025-08-16 12:57:00 | TERRA_M-T | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a348a536-7a0d-36e1-a01d-b90ddb3408c1 | -19.50394 | -55.35825 | 2025-08-16 12:57:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 693b09f9-8101-3820-844c-7ff78fc42315 | -12.6143 | -46.9047 | 2025-08-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| d8e74314-19de-333b-a6f2-d1e16bff595d | -6.5638 | -43.0357 | 2025-08-16 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 5cedf734-a304-344a-85ea-63c93eeb9008 | -8.9971 | -60.5339 | 2025-08-16 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| cc802c64-5aab-320f-bc9e-47f39d94a379 | -14.9628 | -54.7351 | 2025-08-16 13:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| ec8c5d92-96e4-34af-b436-8c1aa7d9f7ee | -7.9439 | -63.2225 | 2025-08-16 13:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| fa73451d-b03e-316f-a4bd-4d4b8714b383 | -14.9822 | -54.7328 | 2025-08-16 13:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4ad323a4-0737-36df-96f7-55d080c0017a | -12.6139 | -46.9273 | 2025-08-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 7afefd92-7dfb-338d-8da4-346a39f92154 | -6.545 | -43.0373 | 2025-08-16 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| b2009941-b662-3ea4-81d3-fe3befc9951a | -8.9893 | -61.7024 | 2025-08-16 13:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 112.3 |
| be233234-8603-36e5-a05e-05ad219035a0 | -7.9624 | -63.2218 | 2025-08-16 13:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 9fe4d487-2f6f-3b4a-827c-2ce93ff69e55 | -12.5947 | -46.9301 | 2025-08-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 108ce5b6-853e-36f6-8e13-9902d4809de3 | -12.5562 | -46.9357 | 2025-08-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 74e984c5-ffe1-3b2b-a09e-9ac838916d01 | -12.5558 | -46.9583 | 2025-08-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 478cfc50-00d5-30c1-ad0d-33a8f12daf8e | -12.5365 | -46.9611 | 2025-08-16 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 6a417f97-08c6-3410-abe7-31f06b448de5 | -8.9973 | -60.5147 | 2025-08-16 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a0404552-e354-3dfd-b4f4-a7358a059e43 | -13.8748 | -45.5411 | 2025-08-16 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| b344d1e4-0024-3726-82b8-f3693443e2a2 | -12.8045 | -45.9681 | 2025-08-16 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| a47583b4-5bcf-3f78-ac7f-2d99f7b0a6f4 | -7.9439 | -63.2225 | 2025-08-16 13:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| e9474271-f338-3782-90ae-6a9b23719306 | -6.5638 | -43.0357 | 2025-08-16 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| e9643484-a21a-3bfb-a3f1-fa986237df5f | -12.6139 | -46.9273 | 2025-08-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| d4f6a216-5d10-31e1-96c2-e739e72178d3 | -8.9893 | -61.7024 | 2025-08-16 13:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 27cc8f6b-d367-35bb-8d2d-947b0134244f | -13.8748 | -45.5411 | 2025-08-16 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 8eeab4d2-6812-34e4-a7a3-fd21e7f90c48 | -8.9708 | -61.7033 | 2025-08-16 13:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.8 |
| cc67019e-a3f4-360f-8077-1c53ea6c97ea | -12.6143 | -46.9047 | 2025-08-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e5a64d10-f735-3732-ba30-b738584a8e3d | -13.8743 | -45.5643 | 2025-08-16 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 873785ae-7688-3db6-b7d1-f2531fa82fcf | -14.9628 | -54.7351 | 2025-08-16 13:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 833bf474-1f23-3e6a-9410-02f69a34ea7e | -6.545 | -43.0373 | 2025-08-16 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 136e6249-9a6d-3def-ac09-bd4498ce3e13 | -7.9624 | -63.2218 | 2025-08-16 13:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 3a201d6d-d3dd-3fb1-8aa7-b85cc3ce4bc6 | -12.5558 | -46.9583 | 2025-08-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 0a546f3e-f34a-35d3-bae4-601f1ce59418 | -12.8045 | -45.9681 | 2025-08-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 85e6b657-0d2f-3fe8-a17d-c3615aae3db8 | -12.5947 | -46.9301 | 2025-08-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1d82d495-62d2-30b6-a473-1484cb1001ce | -12.6259 | -45.2373 | 2025-08-16 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 35d1c672-94e5-3377-af40-f64caf737f01 | -12.6143 | -46.9047 | 2025-08-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 8221d69a-4243-39c5-b926-94c9158f4922 | -13.8748 | -45.5411 | 2025-08-16 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 52ebaf73-9a9f-3225-a254-7d825e317596 | -12.5558 | -46.9583 | 2025-08-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 306a3b0d-9c24-36e9-993f-aaa7b6e7c465 | -7.9439 | -63.2225 | 2025-08-16 13:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 161.7 |
| 0e7df301-588d-39fc-8516-e2030f7fe8e4 | -14.9822 | -54.7328 | 2025-08-16 13:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ed19ff8c-c492-3440-a3e1-811aa0db3416 | -14.9628 | -54.7351 | 2025-08-16 13:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 11b5fcfa-4c3a-3e12-b783-df4adc02519b | -12.5947 | -46.9301 | 2025-08-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 62b6c7bf-7333-3781-bd89-9162278615fd | -7.9625 | -63.203 | 2025-08-16 13:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| caa191d9-87fe-3d4b-a8ff-aba13894379e | -6.545 | -43.0373 | 2025-08-16 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| a3a53504-8622-3bf3-b843-9aa74b27159f | -7.9624 | -63.2218 | 2025-08-16 13:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 244.4 |
| 152038a5-f6be-3736-aabf-560822ade7ab | -8.9893 | -61.7024 | 2025-08-16 13:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 74f629bc-943b-3fc6-8b47-0306d752e3c3 | -8.9708 | -61.7033 | 2025-08-16 13:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 2b7959b0-8c48-3f7f-a091-85049b9845fc | -15.1899 | -53.853 | 2025-08-16 13:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 231c9be5-1368-3d98-9236-eefc71a62f72 | -6.5638 | -43.0357 | 2025-08-16 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a80a0b02-7733-3373-a1c3-20328ca439c7 | -12.6139 | -46.9273 | 2025-08-16 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| e66698bb-12c8-3246-a62d-b56608f7491e | -12.8045 | -45.9681 | 2025-08-16 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 60074c0e-91b3-3937-aca8-4c5435b0bcfd | -12.5562 | -46.9357 | 2025-08-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ad5cd2a8-cc23-3d83-a41d-44765755e8e4 | -14.9822 | -54.7328 | 2025-08-16 13:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 554178e0-9643-3bf8-9947-35c8e2709010 | -12.6139 | -46.9273 | 2025-08-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |
| b2c8ff28-4658-33a7-8ba5-e0875a4ab546 | -8.9709 | -61.6842 | 2025-08-16 13:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d069c62e-a846-339a-9e58-9813304e0f03 | -15.1899 | -53.853 | 2025-08-16 13:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 54d1de4c-c265-3197-bf83-0d8af4bdf67d | -8.9893 | -61.7024 | 2025-08-16 13:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 70cdd040-c2af-30a5-accc-3418be20aa2e | -12.8234 | -45.988 | 2025-08-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 26f4b26e-2179-38e8-b2ba-19a0fba94ea1 | -12.6259 | -45.2373 | 2025-08-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 3451b560-87de-34db-8dc8-64b2a272eb7e | -8.9892 | -61.7215 | 2025-08-16 13:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| bdc1a586-afd2-35ec-bcbd-945c1a725a72 | -13.1267 | -57.1293 | 2025-08-16 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b11b194a-a2ce-3681-b4a0-a49531f15c37 | -7.9439 | -63.2225 | 2025-08-16 13:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 0ab73431-366a-3599-872a-0537798ca013 | -12.8045 | -45.9681 | 2025-08-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| d731bc98-e754-3398-8008-b5de453fbdda | -12.5558 | -46.9583 | 2025-08-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e51c4184-ae00-3dfd-a8d9-484f32e0fe51 | -6.5638 | -43.0357 | 2025-08-16 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 1b4108d9-c4ff-30cf-94af-f91b15c5536e | -12.6143 | -46.9047 | 2025-08-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 164d5f9a-7cd6-30d0-8a50-9657b9a191e0 | -12.5947 | -46.9301 | 2025-08-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ced3ea20-2c03-3bd5-9fac-1ab511c0541e | -7.9625 | -63.203 | 2025-08-16 13:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0b61dba9-a23c-3815-aa1d-4781c2fdad41 | -6.545 | -43.0373 | 2025-08-16 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| c9e242d3-04a4-3c60-b6be-c9e303a717b2 | -14.9628 | -54.7351 | 2025-08-16 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 88ea2082-0a10-3029-95d6-43cfec779629 | -7.9624 | -63.2218 | 2025-08-16 13:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 211.7 |
| 4b68d117-ebe3-380a-8652-c56242be0637 | -8.9708 | -61.7033 | 2025-08-16 13:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 3c1eb01f-58a6-391d-9073-cad625aea4cb | -13.8748 | -45.5411 | 2025-08-16 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 905ff302-a6d4-3fd5-aee7-c04f1c861daf | -6.5641 | -43.0122 | 2025-08-16 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 755985e2-c850-3995-9a8d-7b1d553bfe8e | -14.9822 | -54.7328 | 2025-08-16 13:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 520be460-ba8b-3abf-8013-55368850308a | -13.1267 | -57.1293 | 2025-08-16 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 6bfe8139-e8c8-36eb-bad4-65b0d886e7b3 | -12.6139 | -46.9273 | 2025-08-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 1f121f3d-7a37-3a5b-9dbf-69210708f164 | -7.6296 | -63.3273 | 2025-08-16 13:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 27b20a9f-dc28-388a-9f77-a7455d63c4e9 | -12.6143 | -46.9047 | 2025-08-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 93c91d32-ef85-3eca-9406-8afc000fb675 | -14.9825 | -54.712 | 2025-08-16 13:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 3d24a414-617d-3abe-a709-d264bc7b0e1c | -7.9624 | -63.2218 | 2025-08-16 13:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| b3346177-586a-3231-a933-7e6e800e33e5 | -13.8748 | -45.5411 | 2025-08-16 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a8997936-0d6c-31ac-b46f-e9bfa8a52bcb | -12.5947 | -46.9301 | 2025-08-16 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9dd15ee8-0e2a-381b-b467-b4ff3f41a395 | -5.9134 | -44.3196 | 2025-08-16 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8032c692-3b72-3440-8226-d0bdbc574a4b | -11.3657 | -55.4107 | 2025-08-16 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d5a63293-9a2f-3a69-934d-02779d46b4b0 | -7.9439 | -63.2225 | 2025-08-16 13:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| baed8198-0877-3c58-97ce-7e4ebea625f8 | -8.9708 | -61.7033 | 2025-08-16 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 145.6 |
| ac5630fc-e3ff-3745-bf3d-77530c13c92f | -14.9628 | -54.7351 | 2025-08-16 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 57cb4e4a-cbe0-37e4-bff3-4a96b5df0edc | -6.545 | -43.0373 | 2025-08-16 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 957e47f8-896c-354b-9769-b8663dd03255 | -6.5638 | -43.0357 | 2025-08-16 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 898b8026-c3db-3599-9096-459f7758497f | -12.8045 | -45.9681 | 2025-08-16 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 04bbce24-8199-3f4d-ac28-8d404526e8a4 | -12.8234 | -45.988 | 2025-08-16 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 475b9f03-2ed9-364a-84e3-3f80330d6849 | -8.9709 | -61.6842 | 2025-08-16 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b9aef5c9-0244-39dc-9cf0-1ccfe34f8cb9 | -8.9893 | -61.7024 | 2025-08-16 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 134.5 |
| b69d5c40-e233-3d4a-abb2-18d409a81b62 | -7.6296 | -63.3273 | 2025-08-16 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2fcf6d14-432f-3030-a49e-53ec8ff5db94 | -5.9134 | -44.3196 | 2025-08-16 13:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 549650ef-f869-3f39-bdc6-093d9dea5295 | -12.8045 | -45.9681 | 2025-08-16 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7faea81c-ae4b-3546-a86b-2e361d7ec0b3 | -7.9624 | -63.2218 | 2025-08-16 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 220.6 |


[Clique aqui para ver as próximas entradas](README80.md)
