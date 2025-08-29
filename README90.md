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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5abd2a69-b8dd-3fae-b7e7-bebc6a68b053 | -10.99 | -46.9242 | 2025-08-29 07:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 28421789-f966-39b3-ae4a-1e7d49e6d270 | -12.7067 | -48.1873 | 2025-08-29 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 931eddd7-443d-35ff-b4f4-8ecf73ac15a2 | -9.773 | -64.2469 | 2025-08-29 07:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 843dbc5c-eb91-384b-8454-1919926efcb3 | -10.9709 | -46.9266 | 2025-08-29 07:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| bd15d79d-ae5c-3abc-a182-2383ece8f5b5 | -11.5515 | -46.3778 | 2025-08-29 07:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 1c701b50-9c4e-3e8d-9571-c42dd479b614 | -12.6875 | -48.1899 | 2025-08-29 07:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| d77ad4d1-7377-34b6-99f8-7f4e91d42147 | -9.4618 | -60.5682 | 2025-08-29 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| bd5d619d-b3c2-371a-9155-6a857b9ba987 | -11.5707 | -46.3751 | 2025-08-29 07:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 446b8dd3-f58f-3eb9-97b1-4f64a4ba7ccb | -10.3624 | -57.8258 | 2025-08-29 07:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 0f67ca49-db5f-37a3-a97f-7ba5293bce31 | -14.3149 | -51.8969 | 2025-08-29 07:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 990eb75c-afc1-3fd2-9d95-92418d1cab42 | -11.571 | -46.3525 | 2025-08-29 07:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| f8a29ec6-32da-3d33-854a-e5f9218a77cc | -14.2949 | -51.9422 | 2025-08-29 07:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c60c810b-7827-3f8b-9513-4ca885d1f495 | -9.4433 | -60.5499 | 2025-08-29 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 45b14f37-ff48-3d44-9acb-a91ba7fec82a | -9.1155 | -65.7699 | 2025-08-29 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2d7aa19c-1f6b-3eed-894b-186a0b4e9ca1 | -11.5519 | -46.3551 | 2025-08-29 07:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 67950f04-27b4-3089-b608-1c80b79019d7 | -11.571 | -46.3525 | 2025-08-29 07:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 8d64527b-a01c-3ea3-a113-dc2a47dcdd1a | -11.5707 | -46.3751 | 2025-08-29 07:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 33c8ad2e-8a02-3bf7-b2b4-9c8eddbd3f82 | -10.9709 | -46.9266 | 2025-08-29 07:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| df57fa97-bc85-38c6-8fd7-b15064f1ddad | -10.99 | -46.9242 | 2025-08-29 07:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 259.6 |
| 4a9de54b-e81a-3b50-a40a-b890182d8c0b | -9.4618 | -60.5682 | 2025-08-29 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1389c4cb-590d-3eb6-b2a6-eb15d66adbad | -10.3812 | -57.8245 | 2025-08-29 07:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| bcd0885b-3b76-3dcf-8d2f-4e5f336a7415 | -10.3624 | -57.8258 | 2025-08-29 07:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 9c673f2c-a8af-385f-b86b-767df6e562a9 | -10.9893 | -46.969 | 2025-08-29 07:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| e70e9746-0f4a-311a-97ba-bd637a3a1d5f | -9.1154 | -65.7886 | 2025-08-29 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8d800c04-9ee6-3497-8709-198dd1275e1a | -9.462 | -60.549 | 2025-08-29 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2a9b858c-2503-3922-869e-7d54d2a2351c | -10.9896 | -46.9466 | 2025-08-29 07:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 526.4 |
| be8c126b-91c3-351c-b910-e60a849a52d3 | -9.773 | -64.2469 | 2025-08-29 07:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f88e4583-1816-3a55-b3bf-b950953f943c | -9.7728 | -64.2657 | 2025-08-29 07:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 41402663-b583-34a2-84cf-e101ee6413f2 | -10.9702 | -46.9714 | 2025-08-29 07:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 722e44b1-6eb7-3923-8931-769b44ae2980 | -10.9705 | -46.949 | 2025-08-29 07:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 43025b08-8308-3e38-862f-99cae45a7a84 | -11.5515 | -46.3778 | 2025-08-29 07:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ae405af9-f154-3a29-a8c8-a69fe425b933 | -9.4618 | -60.5682 | 2025-08-29 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b2f902fd-d4ef-3b8e-b2ae-292f30d43d1f | -10.3812 | -57.8245 | 2025-08-29 07:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1c4d5fae-c1aa-34b7-bc58-16622d270e10 | -10.3624 | -57.8258 | 2025-08-29 07:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 5d97d819-4350-337f-9ac9-fca12dbd2525 | -13.4212 | -46.9637 | 2025-08-29 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 7a828352-4fab-38b1-b839-2e7ee65c7f15 | -9.1155 | -65.7699 | 2025-08-29 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6ac89589-68d3-3c1d-8883-231dbb30c7f6 | -13.4208 | -46.9864 | 2025-08-29 07:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cdd3fd1c-e7c7-35f0-a3fb-e58b157c4037 | -9.1154 | -65.7886 | 2025-08-29 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| aa1af9ca-c04d-316b-a509-15b894e9eb2e | -11.5515 | -46.3778 | 2025-08-29 07:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 77331189-b357-399b-9378-c7228fc87059 | -9.462 | -60.549 | 2025-08-29 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 84b1b4a1-6c02-349f-8c3b-56798e923283 | -9.773 | -64.2469 | 2025-08-29 07:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 1f0e7670-5026-3aee-8dae-3a183293972f | -10.3626 | -57.8061 | 2025-08-29 07:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0daad6b4-88c9-332f-b6bf-0ab2f3c51389 | -12.8413 | -48.1685 | 2025-08-29 07:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 26f112ac-7a11-3db4-91b1-cf6f3cd89fd2 | -11.5519 | -46.3551 | 2025-08-29 07:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| ea5ccd50-ec9e-395d-b09c-90378d58138a | -10.9893 | -46.969 | 2025-08-29 07:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 1219b562-618b-3194-b0cd-b06469ebc844 | -11.5722 | -46.2844 | 2025-08-29 07:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8ae941c5-6aba-3f88-bcd7-aefc4301b99f | -10.9702 | -46.9714 | 2025-08-29 07:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| acd6b7b2-5093-3b9f-8131-d10d9ce82fb0 | -12.8413 | -48.1685 | 2025-08-29 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d83416ba-ac1a-3d30-a393-85a3b9902adb | -11.5726 | -46.2617 | 2025-08-29 07:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ef395396-ab40-37f3-8b63-ea6fcf3013db | -9.773 | -64.2469 | 2025-08-29 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 976034ac-4357-35cd-8f6a-595fe0f0e554 | -10.99 | -46.9242 | 2025-08-29 07:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b9ddf0a4-9e1d-3c79-a7d7-869fce4b8a5b | -9.4618 | -60.5682 | 2025-08-29 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4dada1f6-78b7-3e7a-b249-f2e34af2a556 | -10.3812 | -57.8245 | 2025-08-29 07:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 430b9f21-fa72-3eec-965d-658d238eb2fd | -12.8994 | -48.1381 | 2025-08-29 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 29c4ff1f-339d-3d7d-ba79-05717f6b9732 | -10.9896 | -46.9466 | 2025-08-29 07:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 248.3 |
| ed259c6d-1087-3f6e-ae62-035af0795c33 | -10.9705 | -46.949 | 2025-08-29 07:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 23cf73fd-6049-3d37-91e9-ebb13ab84a7c | -10.9709 | -46.9266 | 2025-08-29 07:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 098ae3f6-c699-3272-86b6-dd6729fde5db | -9.462 | -60.549 | 2025-08-29 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cd65f09f-a6c3-3146-8184-c16a5e769f88 | -10.3624 | -57.8258 | 2025-08-29 07:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4cc1c97e-f97a-3ca3-9e14-a1ca0f3fccea | -10.3626 | -57.8061 | 2025-08-29 07:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7d362165-f7cc-327e-ad6c-a81a4146d54d | -9.1155 | -65.7699 | 2025-08-29 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 01fb1f5f-cc53-332e-b8b1-2b7835632fb0 | -9.7728 | -64.2657 | 2025-08-29 07:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 4ca9e183-d888-3f5a-b186-5681987233e6 | -10.9896 | -46.9466 | 2025-08-29 07:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 62529b82-f6b7-3636-b9b8-3d70f41c7511 | -10.3624 | -57.8258 | 2025-08-29 07:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ab0e8592-6c19-3cce-bc50-8b14b440bd44 | -9.773 | -64.2469 | 2025-08-29 07:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3c3010ae-c7ac-33eb-b73a-db28beef59c0 | -10.99 | -46.9242 | 2025-08-29 07:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 648f54d3-6e71-3066-a37e-de6827d6a25f | -10.9705 | -46.949 | 2025-08-29 07:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 65d9b621-98a2-3b0c-bdb4-21065c5c3cb7 | -14.2956 | -51.8995 | 2025-08-29 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2535ad44-dd66-356e-8b82-32d0496ca140 | -9.4433 | -60.5499 | 2025-08-29 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ec6a58b2-5bad-3133-ae5b-14a3409d779b | -14.3149 | -51.8969 | 2025-08-29 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 76539b17-3702-3e6a-a7b1-725b967bfda0 | -10.3812 | -57.8245 | 2025-08-29 07:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 64eb3135-4b42-3732-9839-fe20c55f1714 | -9.1155 | -65.7699 | 2025-08-29 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5503f6a5-9fc0-33f3-b309-68fd94d5b223 | -12.8994 | -48.1381 | 2025-08-29 07:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8bdd4566-fe1a-3ec1-b09c-1f4f5ada2f2d | -9.462 | -60.549 | 2025-08-29 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 67fed207-e207-3b17-b702-80aa90ea35db | -10.99 | -46.9242 | 2025-08-29 07:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 241e2101-b72e-3416-a7f3-b4991fb472f5 | -10.3812 | -57.8245 | 2025-08-29 07:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| b110c052-e2f8-3b4f-bcee-50c30397ecd9 | -10.3624 | -57.8258 | 2025-08-29 07:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 7e18eff1-fd38-3de2-9a77-15717ffea3c9 | -9.462 | -60.549 | 2025-08-29 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0ce1ae2a-99f8-32f6-b556-cea3ce1774f7 | -10.9896 | -46.9466 | 2025-08-29 07:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 43073a6a-e722-37cc-8892-0806e25e3650 | -14.2952 | -51.9208 | 2025-08-29 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e925914c-5e54-3735-92ec-49a72e717193 | -10.9705 | -46.949 | 2025-08-29 07:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| e8e3b31c-36a9-3b99-8169-6e4913253d45 | -9.4618 | -60.5682 | 2025-08-29 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 4c954529-8d04-3c3e-b345-b20ce8e6c3e8 | -9.1155 | -65.7699 | 2025-08-29 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0427b45d-cb64-3220-8f4e-9bae4894d39c | -14.2956 | -51.8995 | 2025-08-29 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e954ff34-3b14-3182-9ed8-436bfe948095 | -9.1155 | -65.7699 | 2025-08-29 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c3970a59-428e-3d79-8f11-ceb47bcdaf32 | -9.4433 | -60.5499 | 2025-08-29 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7d92ea45-1a35-3356-bf45-20500a66de71 | -10.99 | -46.9242 | 2025-08-29 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c48c4e76-dcc6-3b50-a75d-e683501db5e2 | -14.2956 | -51.8995 | 2025-08-29 08:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 57b52355-37e2-3fb6-9b36-1a414cb7da2a | -10.9896 | -46.9466 | 2025-08-29 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 275.9 |
| de00812d-7270-3a87-a823-0427ed226a4c | -12.8994 | -48.1381 | 2025-08-29 08:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 04160c45-45b2-3fcb-b75b-6b15322462d4 | -9.773 | -64.2469 | 2025-08-29 08:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0fdb4f6a-d969-3a10-81a7-3c89ea842ac0 | -10.3624 | -57.8258 | 2025-08-29 08:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 2cc71cc9-2a38-373f-8da6-8bec1b07e123 | -9.4432 | -60.5692 | 2025-08-29 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ff7dd0d3-84ab-32d4-9a5d-eeaf47c986d3 | -10.9893 | -46.969 | 2025-08-29 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 6ed47ac1-b3ca-3a0b-a7ae-0d72b8b894c5 | -10.3812 | -57.8245 | 2025-08-29 08:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 396ac16a-a5c8-3523-9844-0eaa5cd8587a | -10.9705 | -46.949 | 2025-08-29 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| aab45ec3-5127-31d9-b09a-513c256499e3 | -9.564 | -45.8594 | 2025-08-29 08:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f1afc12b-3baf-36fd-96d9-af8d4c928391 | -9.462 | -60.549 | 2025-08-29 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| cdad042b-2a66-3692-9e16-3630c508fff4 | -10.9896 | -46.9466 | 2025-08-29 08:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 66c889cf-c414-3835-b105-bcb26474436c | -12.8413 | -48.1685 | 2025-08-29 08:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |


[Clique aqui para ver as próximas entradas](README91.md)
