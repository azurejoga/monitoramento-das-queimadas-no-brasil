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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c44ef937-3731-3031-8516-2124909aa525 | -6.28283 | -59.93249 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0503ec-885c-36fd-9a2a-6746c7176212 | -6.64548 | -58.82817 | 2026-09-13 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1451cdca-0070-314a-aec9-0085a912ac87 | -6.30211 | -59.95977 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bac13367-dd57-30f0-a5be-3f2a0700cbbb | -6.74843 | -59.43441 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eac564c5-48f7-3c50-9210-042a208ab2c5 | -6.1102 | -57.66298 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 58c8184d-5dec-3e53-acd2-9de21aac8c04 | -6.30559 | -59.95784 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6685ace5-1452-3a56-9e6a-e4b05d4d0aaf | -7.96933 | -70.89494 | 2026-09-13 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f27aec-4471-3cf5-8584-64bad56a2de4 | -1.22195 | -54.12925 | 2026-09-13 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5d4b56f-63ba-3175-af68-e2c5f761750f | -6.31243 | -59.96134 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6c791e9-9b43-3727-9af4-8d815e2985cb | -6.67834 | -58.87885 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7563cbb0-c0bd-3702-802f-edc80887d0fa | -1.22914 | -54.12872 | 2026-09-13 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 321f0d6d-16f2-33a0-84b9-20ede3ef4563 | -8.97629 | -70.59872 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1deb3bd2-5cb1-3e38-b093-7d1c033d53d9 | -9.18807 | -59.44894 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f130c81-1b92-3934-a435-8c31ad4ede1c | -6.18794 | -57.71927 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d6a5763-d431-3210-9b3d-a9e205d41271 | -6.28372 | -59.92618 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c3c868f-a709-3cfd-8b96-dc9ae0ffcd9b | 1.3229 | -60.71257 | 2026-09-13 05:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1d8fe14-ad08-39ff-8887-70f94a3fadfb | -6.30736 | -59.99866 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7638797-24f6-3530-82a3-7b54091249c7 | -7.77815 | -73.00964 | 2026-09-13 05:55:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9b96059-ee16-3af0-8db5-74ab8d84480a | -8.75499 | -71.03167 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44e20a28-5f38-3e00-93d6-152eef71c17d | -6.30647 | -59.95169 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b984c01e-03f6-39cc-a026-e78f667a1035 | -6.66516 | -58.88409 | 2026-09-13 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b34e744b-a05e-3110-a81c-93a559a4e7c2 | -8.77367 | -61.40218 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa4995b1-bcef-3a1c-8a5e-529d277bfdfb | -9.18213 | -59.62759 | 2026-09-13 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cefcc6c9-e47d-3a8d-9c3b-309ff75718e6 | -6.30335 | -59.95055 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e92a9d82-5c42-3442-89d0-e4ffd82b013a | -6.11623 | -57.6635 | 2026-09-13 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4501d56-525a-3083-9084-1f3f272686bf | -6.28238 | -59.93565 | 2026-09-13 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5da2ce44-1aeb-3afa-9fa0-939cd475f904 | -8.43367 | -72.6244 | 2026-09-13 05:55:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7817a1c4-e29f-3369-a93f-81ec952d0490 | -8.03926 | -69.88222 | 2026-09-13 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a08e82-cb84-3417-8776-05f4de47e868 | -10.6827 | -54.1679 | 2026-09-13 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7fd92a09-e737-321f-80d4-6569001ef3e6 | -10.6335 | -50.5651 | 2026-09-13 06:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a495b4e2-a724-39b6-aaa4-76a25e78edb1 | -13.616 | -47.8774 | 2026-09-13 06:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 15cb469b-22d2-3633-89b4-82557078d7ef | -10.6827 | -54.1679 | 2026-09-13 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fbf3bc61-d27a-35b1-97b3-2dff84751d74 | -10.6827 | -54.1679 | 2026-09-13 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6fa28205-deaf-366e-8faa-db04077563c4 | -13.616 | -47.8774 | 2026-09-13 06:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 0da46194-e11d-30f4-8b4c-0ba2c9a0eb1c | -10.6827 | -54.1679 | 2026-09-13 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 80f6c6f8-72ba-3b16-9c28-20b8b6c462b4 | -7.77652 | -73.0067 | 2026-09-13 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccf2ebb8-038d-3ffa-abc6-cb947141e45c | -7.69535 | -72.47786 | 2026-09-13 06:31:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1bd8bc-7339-3c79-8669-e53a8a330120 | -8.75436 | -71.0313 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f85100e7-634d-3f8f-b5ab-514d1dd39d10 | -8.59206 | -70.88947 | 2026-09-13 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a305d5f9-adac-392d-87be-5dd59cc84df4 | -7.30856 | -72.74606 | 2026-09-13 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17f8a536-ae59-3a1b-be05-a9a4e7c1af8d | -8.75824 | -71.03187 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39b94884-e67d-3383-b7fc-39e6be5f2528 | -7.93816 | -72.42227 | 2026-09-13 06:31:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5bea13f-1396-3012-b75a-7b54ea73c21c | -9.03327 | -70.90018 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 563e4207-816f-3dc0-9326-09cca84d1f8c | -8.0359 | -70.09151 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8020ea6-0daf-3747-b2a3-7a37a0e252b3 | -8.43303 | -72.62383 | 2026-09-13 06:31:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3efb4d6-c3c3-35e1-8a9a-f68104d81472 | -8.02736 | -72.45138 | 2026-09-13 06:31:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fcc358ac-d91c-3294-87cb-822056213285 | -8.44732 | -70.42374 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8558bc0c-ce1b-3bf5-bf16-ab0892f70fc7 | -8.44331 | -70.42313 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9294c7fa-a8d1-344f-92cc-f2f4bd4b4b67 | -8.59206 | -70.88768 | 2026-09-13 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa5e456e-282a-33fc-9d0f-1532be36704a | -8.14279 | -70.15475 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28300a86-8824-3017-9ddf-cc250452fe94 | -8.5481 | -70.86102 | 2026-09-13 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f834da4d-5ace-3532-b8d9-fa3b0de01e4e | -7.69235 | -73.06083 | 2026-09-13 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9618f782-54a2-3f39-a1b7-8595973042cd | -8.44628 | -70.42213 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3f2f875-c044-3248-9104-cd0748aa16c2 | -8.03944 | -70.09573 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e4374ae-e496-3fc9-9762-6cc2ed031d74 | -8.97669 | -70.5951 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 037521b3-2f72-3dce-a653-ef05c95c32e6 | -7.85289 | -73.09956 | 2026-09-13 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e4fdb06e-4668-35a3-a4c2-aadfe995cc95 | -9.35331 | -68.29295 | 2026-09-13 06:31:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9daef8ed-f812-36e9-9aa1-91d7631ae326 | -8.76853 | -61.40051 | 2026-09-13 06:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b04a324-087d-3f42-b0d9-f6d53311e411 | -8.54737 | -70.86595 | 2026-09-13 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abbbc9c7-6c72-3fff-9dbc-0e558f0b8a34 | -7.64045 | -73.09927 | 2026-09-13 06:31:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdf2a2e7-12d5-39ae-b6d7-c77e68be81cb | -7.77594 | -73.01051 | 2026-09-13 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44d5fd66-1405-3625-bd07-3c603b7eb05c | -8.03715 | -69.88205 | 2026-09-13 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e54aa2f-c430-3956-b592-9c329b3c8b39 | -7.73665 | -73.08228 | 2026-09-13 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2982067-eb77-39e5-beb7-406364e2db36 | -10.58497 | -69.61184 | 2026-09-13 06:33:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5291ba5-16ae-3806-9b2d-62a671d58648 | -10.73939 | -69.43452 | 2026-09-13 06:33:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5210b4c6-0616-3695-8ae2-c1e01a8b6a71 | -10.58557 | -69.60764 | 2026-09-13 06:33:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2177135-2cd4-3010-8f6a-3f37e1d13c77 | -9.84664 | -67.77888 | 2026-09-13 06:33:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c907b1c2-b539-3305-8d29-c54d1b3f4fda | -9.21518 | -71.81588 | 2026-09-13 06:33:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a5ed66-d7cd-3605-8992-5fbca93b6906 | -9.21569 | -71.81812 | 2026-09-13 06:33:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d678dc48-698c-34b4-8cc3-5e0a02084c92 | -9.21196 | -71.81755 | 2026-09-13 06:33:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 474267ad-7002-3114-9752-e79e0f7d2f93 | -10.6827 | -54.1679 | 2026-09-13 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7cb06c25-2d3e-39c0-92f6-f07fbc6d8a0c | -11.354 | -46.7874 | 2026-09-13 06:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 587f5111-9c72-36a1-b2c8-6d396668514c | -10.6827 | -54.1679 | 2026-09-13 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7d2868e5-a6a2-3ab0-9e85-5f80ad5b7e56 | -13.4507 | -48.48 | 2026-09-13 06:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2bd372c6-6478-39d7-87bf-364956133b8b | -2.53976 | -54.65475 | 2026-09-13 06:52:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| a95ccd4e-d9ba-3747-b229-a72efb567dd9 | -6.23435 | -51.68948 | 2026-09-13 06:52:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a558e03f-4e62-387d-84cf-3e8322258e1b | -7.20832 | -46.09937 | 2026-09-13 06:52:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 26a47f25-700d-3d31-9a89-8f92fc30a004 | -4.45711 | -50.15744 | 2026-09-13 06:52:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 82484d51-e26a-318d-97e0-dfe4c1681712 | -2.53891 | -54.64962 | 2026-09-13 06:52:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 69a5ff43-0fe8-3072-9a7f-8ea0edbee2f0 | -2.82427 | -49.22953 | 2026-09-13 06:52:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fa738f6f-babf-3e44-a2b3-d9fa94f6fce6 | -4.41507 | -54.85279 | 2026-09-13 06:52:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 5514473f-11c1-373e-acd7-3952b489809f | -3.33725 | -42.29598 | 2026-09-13 06:52:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e8e072b9-7401-35c4-a4c9-7b0901fa2121 | -7.01796 | -44.61388 | 2026-09-13 06:52:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| df7a119a-adab-3bf4-b291-9cb6b81bf344 | -3.87574 | -51.18219 | 2026-09-13 06:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e999d9b6-72ee-326f-891a-d035f2549903 | -8.54863 | -70.86623 | 2026-09-13 06:52:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e80160a-a897-338b-9fb2-c4c5790359bc | -7.52759 | -47.33194 | 2026-09-13 06:52:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c1ff52d4-6cee-37f3-876a-4c304ff8a072 | -2.95754 | -50.40728 | 2026-09-13 06:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0d8da46a-84ee-35f9-959a-1065415db132 | -1.21624 | -54.11945 | 2026-09-13 06:52:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 35182a70-6bb9-3a10-b844-2efe77d55084 | -2.94829 | -50.40593 | 2026-09-13 06:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2020b406-1ef6-3101-9f5d-421537136078 | -5.81493 | -53.79554 | 2026-09-13 06:52:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ff969c0c-8af1-3936-a353-7d72b3b52d60 | -5.1182 | -55.96145 | 2026-09-13 06:52:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 66e6b8e1-6683-3c9d-969e-e7abffddba06 | -2.95904 | -50.39751 | 2026-09-13 06:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 78a8e53d-955a-3820-97b7-9519e9fb84b2 | -7.3761 | -45.34348 | 2026-09-13 06:52:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3d6c1632-4105-35c7-9af2-3de3594508e0 | -7.64088 | -73.10158 | 2026-09-13 06:52:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d51722d-c3ea-3068-8ffd-72b1af40d81b | -6.72217 | -45.41418 | 2026-09-13 06:52:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 497843b4-5928-39ed-8c02-de10350efc40 | -4.4152 | -54.86021 | 2026-09-13 06:52:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9423b519-3627-3121-90a6-209c725eba7d | -7.77631 | -73.00984 | 2026-09-13 06:52:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1030e3dc-7d92-33aa-bcba-5d4708e9aec2 | -3.87414 | -51.19266 | 2026-09-13 06:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f835bfd4-ff55-32a5-8efd-42cbdcf42b93 | -7.01597 | -44.62825 | 2026-09-13 06:52:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| f52bcecb-7886-3a5e-a008-99ae86d2c12b | -8.44548 | -70.4258 | 2026-09-13 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README58.md)
