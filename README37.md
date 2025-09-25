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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 300dd678-05d4-3c43-a25f-75f2172de733 | -2.18994 | -54.46782 | 2025-09-25 06:16:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f888882-b5b8-33be-b22d-83bfdfb507af | -2.19167 | -54.45638 | 2025-09-25 06:16:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cd824593-0e01-3808-9a25-fddf86f23b30 | -2.92099 | -48.30923 | 2025-09-25 06:16:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| cb0fa012-c220-30b5-95e6-52873fed263f | -5.52059 | -43.86922 | 2025-09-25 06:18:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 33f5f7b0-b3c4-3b2f-bc29-f23a1c1e0a1a | -5.52012 | -43.86193 | 2025-09-25 06:18:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 07a43f7d-98c3-3c29-b25e-5f0128d1bc93 | -6.41649 | -43.0856 | 2025-09-25 06:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 22db8cd8-f37d-3405-9ade-37ca17ee405e | -4.74249 | -44.42912 | 2025-09-25 06:18:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a0745c02-62e2-3630-abc6-c84f941725c3 | -3.81788 | -50.96771 | 2025-09-25 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 267de2af-dc5f-3cc9-8810-8a3dbeb3f4f9 | -3.8267 | -50.96898 | 2025-09-25 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8d8837f4-5685-3dc5-91a6-8d7b08ecaa00 | -4.02647 | -47.76768 | 2025-09-25 06:18:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 46961450-417f-30cc-bd5b-3a9cc2870284 | -6.41552 | -43.05657 | 2025-09-25 06:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c7ea9183-ab9f-33e5-b01f-45e52d30f94c | -4.72874 | -44.427 | 2025-09-25 06:18:00 | AQUA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1982b035-0cae-3fd6-b4ab-1b073bd3bc2f | -3.81657 | -50.9765 | 2025-09-25 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bc6394d6-284e-38f0-9c00-50a6d896db93 | -6.42091 | -43.05269 | 2025-09-25 06:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 44a3725d-6747-3faa-bd8a-628e4408406b | -6.4114 | -43.08923 | 2025-09-25 06:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9a6fbd80-dbb0-3bb5-88d8-080af774ef04 | -3.82538 | -50.9778 | 2025-09-25 06:18:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dbef06d4-dcee-3278-bb03-542f73c494f0 | -6.42713 | -43.09152 | 2025-09-25 06:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5c9ff39b-0feb-376c-a0fb-94a70e83a2c5 | -6.43134 | -43.05856 | 2025-09-25 06:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 30965317-34fd-3663-8db9-653898b59db4 | -7.3752 | -47.04202 | 2025-09-25 06:18:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fc387454-e1bf-3691-97a5-0209d34bf046 | -17.9506 | -55.8731 | 2025-09-25 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.9 |
| 858cfa4f-9180-349c-ac95-0d3e8e3fc113 | -17.911 | -55.8784 | 2025-09-25 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 64c3d35f-2d21-3357-b83c-0bb3353ac03a | -17.9312 | -55.8548 | 2025-09-25 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.5 |
| 93adcb35-e043-3bfa-8937-2fe01ac2b6af | -17.951 | -55.8522 | 2025-09-25 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 2865f7c7-4b33-3aa2-b445-0bde5ead784c | -17.9308 | -55.8758 | 2025-09-25 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 312.2 |
| 5c54aea4-a5b5-3111-a1ab-d21af41db6fa | -12.84296 | -45.27524 | 2025-09-25 06:20:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 935165a5-bb4c-35a8-8856-fdc7c0cb42c4 | -12.83976 | -45.30244 | 2025-09-25 06:20:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 72ca7a87-3b3a-3ebb-8c97-5ad61915371d | -16.84926 | -50.51316 | 2025-09-25 06:22:00 | AQUA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 8759deac-d74b-37f4-9afb-afa1ee617ae1 | -17.92745 | -55.86352 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 242.6 |
| 603ad200-6694-39e9-a2e3-493cea57d2ed | -15.96515 | -59.49799 | 2025-09-25 06:22:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7de50601-58ab-3f53-b47c-8dc17f34250e | -17.93789 | -55.8555 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 6e2c5d80-07c4-36c0-b98d-d2b34366fab4 | -16.84761 | -50.52595 | 2025-09-25 06:22:00 | AQUA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8b5680e8-94b1-3ea2-ab26-045ab5c1cfaa | -20.97407 | -50.02046 | 2025-09-25 06:22:00 | AQUA_M-M | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.1 |
| e5f4e625-2a4d-3780-bb5c-c169f37eb46d | -17.93491 | -55.87457 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 2924545b-96be-37a6-899e-5bb9626ab372 | -18.17778 | -53.32947 | 2025-09-25 06:22:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c5a77e59-131a-3b3d-8c8f-3cd1e1f5cbbf | -15.88877 | -59.34278 | 2025-09-25 06:22:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c7b6940e-df06-3dfb-9e0e-66639098b5f7 | -16.85093 | -50.50031 | 2025-09-25 06:22:00 | AQUA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 39284118-09fd-35e3-b3b7-e4895aff5719 | -20.98748 | -50.00589 | 2025-09-25 06:22:00 | AQUA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 1951d2e9-e988-388a-9786-f6b95e747d7b | -17.9364 | -55.86503 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| ec12164f-1e83-36a5-b928-7a036f03c3fb | -17.92595 | -55.87305 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 248.7 |
| 360e162d-8a17-3a3b-af0b-b08c1b373032 | -15.794 | -59.48605 | 2025-09-25 06:22:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4e306a09-24e2-3658-b528-7562778a961d | -15.90008 | -59.34489 | 2025-09-25 06:22:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 795851d6-17ea-33e0-9fb3-ed776ea25d36 | -15.82026 | -59.59871 | 2025-09-25 06:22:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d7f49af8-b33e-31d9-872f-3d3a22d96dcf | -17.92895 | -55.85399 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 4b27dd15-71c5-3481-bf4c-0578419351d6 | -20.98553 | -50.02213 | 2025-09-25 06:22:00 | AQUA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 6b5e5192-69ff-3de0-a713-0649054506f5 | -17.92445 | -55.8826 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 17e071bd-de99-34a0-a133-1ca3c17cbe92 | -17.93044 | -55.84447 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 4998a0d1-076f-3d18-b698-2d3cd43ec7d6 | -20.69759 | -57.85898 | 2025-09-25 06:22:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 49b405f7-6fdd-35b8-b61d-bdea281daba5 | -15.8774 | -59.34111 | 2025-09-25 06:22:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 25c7195f-1d93-36bc-b64d-a5090c16dd1d | -17.9308 | -55.8758 | 2025-09-25 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 384.2 |
| 6fcb0646-182b-34f5-8a86-bca65b72be8f | -17.9506 | -55.8731 | 2025-09-25 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 965506db-7b9f-323e-876d-10211053b984 | -17.9312 | -55.8548 | 2025-09-25 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.0 |
| 7cd47896-1974-39bf-9b65-5929284e4108 | -16.8538 | -50.5026 | 2025-09-25 06:30:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c7ce4aec-1d7a-3652-9161-efe9ee41e915 | -17.9506 | -55.8731 | 2025-09-25 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| 1d4beb05-5a39-3572-a09a-06dc96c324b0 | -17.9304 | -55.8967 | 2025-09-25 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 090181a4-9a17-3457-b097-ffa1bc552b91 | -17.9312 | -55.8548 | 2025-09-25 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.3 |
| 92a7ce86-fce2-3405-a178-73b6efa45aae | -17.9308 | -55.8758 | 2025-09-25 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 395.2 |
| e2e04a29-2031-3699-94d6-cdb079a321e2 | -17.951 | -55.8522 | 2025-09-25 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 40119d1c-ebdc-38c6-a9fb-dcda15a286ad | -17.9304 | -55.8967 | 2025-09-25 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| b3b380ff-1d5c-3547-bf95-84e6440c3d6b | -17.9308 | -55.8758 | 2025-09-25 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 351.3 |
| 314360c9-f151-3328-a9d8-3a292b7cef9a | -17.9312 | -55.8548 | 2025-09-25 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.6 |
| dbc98456-f699-3035-a77f-7ee4005fe30f | -17.9506 | -55.8731 | 2025-09-25 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 446e1f7e-760f-3d8d-b92b-5d3de7800942 | -17.9304 | -55.8967 | 2025-09-25 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 40bc6fb5-d756-3724-8658-ad4de595615f | -17.9312 | -55.8548 | 2025-09-25 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.6 |
| f060aa46-c42a-39fb-96d9-9827f63f19ca | -17.951 | -55.8522 | 2025-09-25 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 309d1a15-54b2-31df-9d2b-c21ce0fd659e | -17.9308 | -55.8758 | 2025-09-25 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 319.5 |
| 0f56e9b0-3b1d-334b-8479-39e82c512a89 | -17.911 | -55.8784 | 2025-09-25 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 429c5b8c-406e-38c9-b20b-bc005cdf2485 | -17.9506 | -55.8731 | 2025-09-25 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.4 |
| e20aea03-8eb8-3cf6-8115-1b6104703f46 | -17.9312 | -55.8548 | 2025-09-25 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.7 |
| 8776d014-4fff-3341-bce1-f93790ce3548 | -17.9506 | -55.8731 | 2025-09-25 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| a50c4940-388e-36f3-ae2e-60b7702399fc | -17.9304 | -55.8967 | 2025-09-25 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 917ed799-daca-384b-a708-dc26d3caddbd | -17.9308 | -55.8758 | 2025-09-25 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 312.3 |
| 8523198c-51ba-3934-bde1-83cc29ee3b44 | -17.911 | -55.8784 | 2025-09-25 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| d48c0e69-67c2-34c1-aaeb-684aeb29939b | -17.951 | -55.8522 | 2025-09-25 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 7e526692-faf3-3721-b1c5-c5b7d5097d3f | -17.9312 | -55.8548 | 2025-09-25 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.8 |
| d5aab9e7-0862-3118-a852-2a0ad7a2d117 | -17.9506 | -55.8731 | 2025-09-25 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.8 |
| a379ef97-4ab2-3bcf-aca0-e72b448bb13c | -17.9308 | -55.8758 | 2025-09-25 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 213.7 |
| ca99dbdd-5a5f-3242-8287-53b1f6369912 | -17.9308 | -55.8758 | 2025-09-25 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 210.2 |
| 70e94aa1-5922-3eeb-a5c0-d359978d67ad | -17.9506 | -55.8731 | 2025-09-25 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| cb2b4a7e-e178-3175-9fac-454555fd12c5 | -17.9312 | -55.8548 | 2025-09-25 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.9 |
| 05f253f9-e604-3596-bf7b-4e90977c0fc8 | -17.9312 | -55.8548 | 2025-09-25 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| d8a73faa-d0cb-3d72-8662-fa271e62518f | -17.9308 | -55.8758 | 2025-09-25 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.3 |
| ac396373-f26b-3e66-8c52-f4a4ed570168 | -17.9506 | -55.8731 | 2025-09-25 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| b224be5c-a97e-3aa9-9c56-50bdda882a4e | -17.9312 | -55.8548 | 2025-09-25 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 13540c43-9c1e-344d-a716-ee92230752bb | -17.9308 | -55.8758 | 2025-09-25 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 197.4 |
| d38a438c-ef9a-3e1f-bf34-297f1834fb4d | -17.9312 | -55.8548 | 2025-09-25 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 0a63e05b-44d3-3d15-a28f-06e520bb79eb | -17.9308 | -55.8758 | 2025-09-25 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 172.5 |
| 213906c2-592c-3001-9b2a-0ce4b6ba932d | -17.9312 | -55.8548 | 2025-09-25 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| c451d742-b88e-3eaa-bd12-e1d6e4922863 | -17.9308 | -55.8758 | 2025-09-25 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.8 |
| d4a49d16-2230-35f7-befe-504f67f10f81 | -17.9312 | -55.8548 | 2025-09-25 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 8a75236a-59d3-39ec-9f81-27c37bf58286 | -17.9308 | -55.8758 | 2025-09-25 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.8 |
| c4062a4d-023b-30d7-aed0-cb6c6f11aa3c | -17.9308 | -55.8758 | 2025-09-25 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.8 |
| 02875211-e686-3dd8-a05e-a8704693ed76 | -17.9312 | -55.8548 | 2025-09-25 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| b8a4198b-aea2-330d-8595-0686baf65b30 | -17.9308 | -55.8758 | 2025-09-25 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.9 |
| 0901d4e8-8e59-3ec2-92ee-49dd194eacc2 | -17.9312 | -55.8548 | 2025-09-25 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 1e7b0561-c7ca-3c38-b8e3-63d0b288f7c6 | -17.9506 | -55.8731 | 2025-09-25 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 43652df1-e1eb-348f-84ce-b9d2c9717728 | -17.9308 | -55.8758 | 2025-09-25 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.5 |
| a64a3e58-000a-3983-b784-23c85e95504a | -15.8823 | -59.336 | 2025-09-25 08:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 00700d00-65ea-3be9-b972-4043ae847f28 | -17.9312 | -55.8548 | 2025-09-25 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 4e8f908c-6039-373b-96d3-5bbd687fb708 | -17.911 | -55.8784 | 2025-09-25 08:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| b6cfe71d-62b6-3691-9bb4-9bec2beefdd7 | -15.8029 | -59.4835 | 2025-09-25 09:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |


[Clique aqui para ver as próximas entradas](README38.md)
