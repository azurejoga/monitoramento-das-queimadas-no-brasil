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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f925e67-60aa-3630-98c6-8aa60351069e | -11.6743 | -64.9983 | 2024-10-01 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 2787334d-ec80-37a1-8185-bd526a635d6b | -11.6556 | -64.9802 | 2024-10-01 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 195121d5-c9cd-3f5c-8a9a-361c2b2b6913 | -11.6555 | -64.9991 | 2024-10-01 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 187.5 |
| ff193c60-2865-3f9c-8411-11319d264561 | -11.6554 | -65.018 | 2024-10-01 02:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| eada5587-918f-3095-923e-41fd82be32c6 | -12.1593 | -50.0717 | 2024-10-01 02:56:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 9dea61c7-f9c1-3729-9767-f145fd3d78e6 | -12.1406 | -50.0524 | 2024-10-01 02:56:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| d95e0542-fb34-3bbd-9896-3e5294f56184 | -12.1402 | -50.074 | 2024-10-01 02:56:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| d2c45ee4-5771-3e29-8ecf-2b5806a2544a | -12.6039 | -53.4879 | 2024-10-01 02:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 170097c4-b828-373a-9c30-a572811a33f2 | -12.9591 | -51.4303 | 2024-10-01 02:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bc7cbad2-4b84-3b97-9a91-2019e1996708 | -12.9588 | -51.4517 | 2024-10-01 02:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e6d2ff92-cd7c-3696-ab05-97bb464f232c | -12.9396 | -51.454 | 2024-10-01 02:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a4e377f9-fb98-3500-914d-25ae5d5de57f | -12.9245 | -51.2002 | 2024-10-01 02:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 4b9eb095-c1a0-34a7-9d9c-ebf171af7585 | -12.7826 | -62.9025 | 2024-10-01 02:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0af2b924-6dad-3b59-80dd-59ea5e40bb8f | -12.7636 | -62.9036 | 2024-10-01 02:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 848fdc70-d720-3a2c-ba24-368682df3c9c | -13.2308 | -51.2048 | 2024-10-01 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 94287dc9-1b24-3197-8eca-15a97589a4a4 | -13.2304 | -51.2262 | 2024-10-01 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4dbe91c3-e818-3f7d-b083-d828e83c3b91 | -13.2116 | -51.2073 | 2024-10-01 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 2ef260bd-8488-3add-b845-8f7a0704ae97 | -13.2112 | -51.2287 | 2024-10-01 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 3ee41f18-0af5-3212-9941-b9a778d54a8f | -12.9925 | -62.6976 | 2024-10-01 02:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| eaac3bf1-5613-3e2e-a60b-922e4afda3b3 | -13.5954 | -51.2011 | 2024-10-01 02:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 52b38d1e-e9d4-3bcc-a7cd-34e5f6e7b377 | -14.7406 | -48.7498 | 2024-10-01 02:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| be26e5c6-bf98-33dc-b270-2f952cb8698a | -15.9127 | -57.1733 | 2024-10-01 02:56:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 15cddecf-2622-3b07-8d65-3598525fddc0 | -16.1859 | -58.4215 | 2024-10-01 02:56:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| 72e5dbcf-7b20-3d9c-89d8-69e92c2233d3 | -16.5134 | -57.3305 | 2024-10-01 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| b2b48996-71c1-3dcb-941b-503a6fd9eaf7 | -16.5131 | -57.3509 | 2024-10-01 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 60e6f7bb-3a39-335b-813d-d942a8986e04 | -16.4939 | -57.3327 | 2024-10-01 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 472d676a-a280-3206-a446-709e53e9b665 | -16.4935 | -57.3531 | 2024-10-01 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 85724d03-3e8c-3c53-9c37-328a4200a02d | -16.4743 | -57.3349 | 2024-10-01 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 5633d03b-dc18-3594-b9f1-b9102393f1cb | -16.474 | -57.3553 | 2024-10-01 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| b31af85b-8a5d-3ee3-8dff-b20b7039a243 | -16.7471 | -57.3651 | 2024-10-01 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 4898b343-bbb0-3092-a86c-bbf9ecd7d518 | -16.7467 | -57.3855 | 2024-10-01 02:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 3a8a016d-2fde-3ba1-acc4-ccba1a4a0956 | -16.7464 | -57.406 | 2024-10-01 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 6b23b361-836f-36e6-8662-98d07a19eafd | -16.7461 | -57.4265 | 2024-10-01 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 670ca774-bd82-3463-8096-ca215f6ef3af | -17.7046 | -53.2261 | 2024-10-01 02:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| c5af89d8-56e1-39f4-8dc6-79094a54bf34 | -17.705 | -53.2046 | 2024-10-01 02:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 5824e0f9-57f6-3f0c-9fdc-966465e1516c | -17.7248 | -53.2016 | 2024-10-01 02:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 34dcf62d-4361-370c-b4a4-098621e5db2b | -18.6973 | -57.333 | 2024-10-01 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.2 |
| 4dea2e3a-cfc8-361a-b843-e1bc7b0384d8 | -18.6977 | -57.3123 | 2024-10-01 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.7 |
| 07a86429-0ab1-3fd2-9879-4536b5bff258 | -18.7172 | -57.3305 | 2024-10-01 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.0 |
| 6e1ab614-ccbc-3982-977c-cc1d3f3134c8 | -18.7176 | -57.3097 | 2024-10-01 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.6 |
| e7616033-aeb7-3989-a89e-417c6850a132 | -21.3212 | -46.4349 | 2024-10-01 02:57:03 | GOES-16 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.2 |
| e40d781e-8b48-3915-9963-8f4f91109c37 | -21.342 | -46.4296 | 2024-10-01 02:57:03 | GOES-16 | MONTE BELO | MINAS GERAIS | Brasil | 3143005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.3 |
| 625ba23d-cd72-3982-b71c-1c3e6cd8a98b | -22.3498 | -49.3293 | 2024-10-01 02:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| 72736353-d131-38b6-8731-4b83cbee68fd | -22.37 | -49.3477 | 2024-10-01 02:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.3 |
| f19632b0-aceb-3557-a4c8-811c33b9fb2b | -22.3707 | -49.3244 | 2024-10-01 02:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 380.7 |
| 4a07a42c-a340-33ce-975e-b6609d5fa603 | -22.3713 | -49.3011 | 2024-10-01 02:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.8 |
| f4f82e35-e579-3d1d-bac5-50cd6f60f12b | -22.3916 | -49.3194 | 2024-10-01 02:57:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.9 |
| 1611f8b8-7629-390c-8221-48c1d6682ba3 | -23.0793 | -45.3951 | 2024-10-01 02:57:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| cc0a6d6a-d0af-372e-a7aa-dcc50f1687ea | -22.37 | -49.34 | 2024-10-01 03:03:17 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa876ed0-0d38-3b39-9f69-0a130c8d7c6a | -21.56 | -47.83 | 2024-10-01 03:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 374bc1b7-cc1c-3a77-ab85-c8bc09cbe7ff | -21.59 | -47.9 | 2024-10-01 03:03:20 | MSG-03 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 50fefc65-db31-33d5-85bb-530f5a76803e | -21.59 | -47.84 | 2024-10-01 03:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 62113c95-86ce-3c03-8654-fc6a186549e8 | -21.59 | -47.79 | 2024-10-01 03:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| adf828c9-428f-3d39-9854-e3d49439eaca | -16.76 | -55.72 | 2024-10-01 03:03:49 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a806a0dc-b23b-3dae-a9b2-466fe75e1d85 | -17.16 | -56.23 | 2024-10-01 03:03:49 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5238d90f-40e2-377d-a60d-6279d7fe22dc | -16.74 | -55.84 | 2024-10-01 03:03:49 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c7bb624-7c4c-3061-a045-bfdee73de7a8 | -16.74 | -55.77 | 2024-10-01 03:03:49 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| deb47a21-c3b0-3d0a-ac19-192969b167a2 | -16.77 | -55.86 | 2024-10-01 03:03:49 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 819badba-db4d-3d04-b5dd-5d8bd435dc67 | -16.77 | -55.79 | 2024-10-01 03:03:49 | MSG-03 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4ef1ff9-8afd-371a-abd2-a16cc27e0849 | -12.93 | -51.47 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b915537-b0b1-3cae-862e-6f8a8c33d499 | -12.93 | -51.41 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf6d2202-a065-3f36-9fbf-2fe57e6f97e2 | -12.96 | -51.48 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a08f6ac-d9e8-37e2-b31b-d252f2456579 | -12.99 | -51.38 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0364a86-1b9b-3b93-baef-329af73fd16d | -12.98 | -51.32 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f32fc63-e5c7-3fdd-b66a-7d997b0f232f | -12.98 | -51.26 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad87b597-d095-3064-b428-88e0f19919c9 | -12.98 | -51.2 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be319b96-4cab-3824-b752-23f9f4017b14 | -13.01 | -51.33 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85de0141-e339-3c31-927a-53b6d5c9fead | -13.01 | -51.27 | 2024-10-01 03:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 896c98db-8252-3a95-bc74-c2b478215b84 | -2.82 | -50.72 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d14fd4-aa63-30a4-826e-da7dfdd055ed | -2.85 | -50.78 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60de2dd9-8a1e-3c74-9931-1f3b2f86b7e4 | -2.85 | -50.72 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5dda9f8-8cf6-3a7d-b67e-5577d7be23fa | -2.85 | -50.67 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1db3cc9-9671-3d43-ba92-7d9bf5091058 | -2.88 | -50.78 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 594e1cef-702d-37e6-b1e3-400ad0b70b4e | -2.88 | -50.73 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 203dab92-8f0d-3fe0-9800-acf791603905 | -2.88 | -50.67 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73ed250-2489-3ae3-8686-d4974d792acf | -2.91 | -50.78 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff3c1aa2-efb8-39b6-ba00-6df56155f628 | -2.91 | -50.73 | 2024-10-01 03:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba64552-7689-3076-9069-981857352166 | -2.4048 | -50.3085 | 2024-10-01 03:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8eba7a13-cade-3c68-9bd3-fe25dbff1fee | -2.4047 | -50.3295 | 2024-10-01 03:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 238.2 |
| 9842ea68-25e4-3472-9c66-4ea647f593c4 | -2.4046 | -50.3505 | 2024-10-01 03:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| da7923ec-6dbe-3b1d-ba93-9c2e5df1e07f | -2.3863 | -50.3299 | 2024-10-01 03:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 1aeb77fc-92ab-35a2-ad0e-d2d0bb70f189 | -2.4231 | -50.3291 | 2024-10-01 03:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6752f041-1baa-38c2-82e6-714048ced1c4 | -3.0282 | -51.3345 | 2024-10-01 03:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ae23f51c-7ee3-392f-a7c5-63c89740953f | -5.9786 | -45.3847 | 2024-10-01 03:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9f4aebc9-1871-3b81-a5e5-49fb8727e70b | -5.9788 | -45.3621 | 2024-10-01 03:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 02fed8da-8961-3df7-8fec-f635067450e7 | -6.545 | -43.0373 | 2024-10-01 03:05:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 867ee4a9-9bee-3425-acd0-67b4b10defa7 | -11.258 | -45.6682 | 2024-10-01 03:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8c7587eb-f3f1-3c3b-ac58-6fcc064d7482 | -11.2584 | -45.6453 | 2024-10-01 03:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| fc2627d2-dc8b-3fb0-b928-bda03f10fc2f | -11.6555 | -64.9991 | 2024-10-01 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 154.5 |
| f6053b7b-0150-35de-9b6d-0c50996394ee | -11.6556 | -64.9802 | 2024-10-01 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 1ce022b4-670b-3c34-9508-83d930baec7b | -11.6743 | -64.9983 | 2024-10-01 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 676f5024-ebd7-3014-8a83-f081d7bad29a | -11.6744 | -64.9793 | 2024-10-01 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7cfa9b14-ed25-34f7-aac8-59d4d2b6e674 | -12.1402 | -50.074 | 2024-10-01 03:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 974355f2-d6c1-350f-b957-800d5fe3f547 | -12.1406 | -50.0524 | 2024-10-01 03:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7920a6db-9c95-3c67-9ab5-e4a5b0342e64 | -12.1593 | -50.0717 | 2024-10-01 03:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| faff7219-24f8-3687-b3bb-a48a43a74a95 | -12.6039 | -53.4879 | 2024-10-01 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e0abbf5c-e08f-372c-bedf-cea689d2159d | -12.7636 | -62.9036 | 2024-10-01 03:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 10bf9f46-b71d-3e5d-8cbc-85bbfbd24315 | -12.7638 | -62.8843 | 2024-10-01 03:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e9ef741f-92f2-3790-a30a-439f98b0c418 | -12.7826 | -62.9025 | 2024-10-01 03:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| bd80bb7d-d7d3-3c37-9b7e-bab7382a38b6 | -12.7827 | -62.8832 | 2024-10-01 03:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |


[Clique aqui para ver as próximas entradas](README34.md)
