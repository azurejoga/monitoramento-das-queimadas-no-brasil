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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce4c1efe-cbc4-33da-aa38-4173e052a95f | -21.19488 | -44.9387 | 2024-11-10 04:21:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e88d070c-a232-3336-b2c6-d25511bb52ba | -23.63311 | -46.42594 | 2024-11-10 04:21:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3836eacf-2b08-392e-92f7-3c57496d8018 | -23.90385 | -54.07183 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 54f2790f-f87a-3712-8afa-68b6f69a9c19 | -23.90813 | -54.07283 | 2024-11-10 04:21:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 726e9124-947d-3efa-8cf7-d94a8b95760f | -21.19427 | -44.93893 | 2024-11-10 04:21:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8632163c-1f8e-3fb8-970a-5bb5d95e0f97 | -31.98279 | -52.0362 | 2024-11-10 04:23:00 | NOAA-21 | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 41c06a01-8b0e-34fb-9f19-75e3502c5d14 | -29.67942 | -51.16607 | 2024-11-10 04:23:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| c068dcea-ab71-3fc9-9dd8-485435696c82 | -29.68 | -51.16778 | 2024-11-10 04:23:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 34f1ca7d-5cbb-3bca-a322-74da515b4d9a | -3.9483 | -48.1724 | 2024-11-10 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 99f8eac1-3526-3da4-8530-2657495bbb20 | -3.9669 | -48.1716 | 2024-11-10 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 89d4d3ad-017d-378f-b6e9-bcc17349a879 | -4.1099 | -49.1315 | 2024-11-10 04:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 91f1a34e-1bcc-3667-8730-826849964389 | -8.397 | -44.1133 | 2024-11-10 04:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 47.7 |
| f27a20a3-594a-3761-96f9-60c76f73b485 | -17.6069 | -57.5304 | 2024-11-10 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 274.3 |
| 77bd6288-8a73-322d-9adb-084f0e0535b9 | -12.433 | -64.1272 | 2024-11-10 04:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2b8a55e9-6ccd-35e8-940e-f4a1e24b802a | -3.4383 | -50.2999 | 2024-11-10 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3c0bbcdf-8983-313f-af02-06fe2f1c9621 | -17.6266 | -57.5281 | 2024-11-10 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 213.9 |
| ce60c948-1c01-30e9-844d-18fb0c5e6e43 | -17.5872 | -57.5328 | 2024-11-10 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| b3e317ca-fa1b-39d6-9ed8-523bfb0e2231 | -3.1422 | -50.4562 | 2024-11-10 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 156.2 |
| d8a001c8-6d07-3734-b0ca-04e8db3068e8 | -2.9171 | -51.4825 | 2024-11-10 04:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c82f2f16-33e6-33fc-abce-2995e3e280ed | -2.8803 | -51.4628 | 2024-11-10 04:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 79077d7a-32b9-3a4d-8aa7-ee635b7d8f83 | -2.8802 | -51.4835 | 2024-11-10 04:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| bf595982-49d9-3d81-9f94-a4923e262911 | -2.418 | -46.3024 | 2024-11-10 04:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 13a9b274-c5cb-38fe-8615-42b7f68ef1fe | -2.7772 | -49.3492 | 2024-11-10 04:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 657249dd-f733-374c-9c1f-56f6647f6d7e | -3.1238 | -50.4568 | 2024-11-10 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 157a38e1-2fe2-3e4b-9ce4-add6d601878c | -2.9494 | -52.7748 | 2024-11-10 04:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f4dbdfcd-92d5-39ff-bab2-bbd037443c09 | -17.6073 | -57.5099 | 2024-11-10 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 233.4 |
| a3d4f90d-9d9a-3457-803f-27fb0b8f7299 | -12.4329 | -64.1462 | 2024-11-10 04:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 726a798e-381d-3bc3-8d08-ac5cfa97ce29 | -3.9485 | -48.1508 | 2024-11-10 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 05423832-d728-3384-8b67-d48b5e218cb7 | -2.7587 | -49.3497 | 2024-11-10 04:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4537e912-cb3e-3535-9a10-d97cc247962c | -3.525 | -44.0286 | 2024-11-10 04:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ee2051cf-843b-32e7-9694-69bdda4c4701 | -2.931 | -52.7753 | 2024-11-10 04:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f6c908b7-bf19-3621-a9af-64ff5456b688 | -17.627 | -57.5075 | 2024-11-10 04:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 221.3 |
| 9677ebf7-11e7-35e2-b632-c5a680e6fb2f | -1.5347 | -52.2104 | 2024-11-10 04:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d8bdf132-aff0-3703-b5c2-50fe55b5dd29 | -3.967 | -48.15 | 2024-11-10 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 47a6f868-d695-313d-a937-953989163d8a | -17.2933 | -57.4857 | 2024-11-10 04:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 28d1305c-4d60-3740-878a-b3c928a46f55 | -3.1423 | -50.4352 | 2024-11-10 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 330.4 |
| 69a52de0-c9f1-3b61-a6db-6e2f46077812 | -8.3967 | -44.1365 | 2024-11-10 04:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 808c15fe-e136-36d0-92c9-569efb38afd8 | -3.1239 | -50.4358 | 2024-11-10 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| facc780f-77f1-3f10-946a-3eb37d3fbbca | -3.1424 | -50.4143 | 2024-11-10 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| fe9d9d60-b789-3f39-8ebd-008c06e1adf0 | -2.9355 | -51.482 | 2024-11-10 04:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| b9e5b4af-8cb6-3590-8bc8-8f2ec7ce9572 | -3.52031 | -44.01617 | 2024-11-10 04:36:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b5e197b7-31c6-3bc3-a880-aa184bba1c42 | -3.50629 | -44.01827 | 2024-11-10 04:36:00 | AQUA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| eefa4d21-0d10-3612-9e86-178629d8ca96 | -5.56479 | -43.9569 | 2024-11-10 04:36:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 77388dc1-3295-3f2b-b32e-e85877d73141 | -4.12694 | -43.57524 | 2024-11-10 04:36:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| dcf910bf-5373-3679-9212-93ab92e50abe | -4.12006 | -43.56956 | 2024-11-10 04:36:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 2b668df8-f8a4-3696-a4b0-d63d70d75927 | -2.18693 | -48.55036 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64273aea-33c1-3dad-a67c-122c77b60442 | -2.33982 | -48.93196 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1e1a652-259d-3900-b909-de01152c2a35 | -2.04996 | -47.72615 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac017ced-5f20-35bb-b399-6a003c145186 | -2.32415 | -48.54004 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b36edca6-52fe-3d21-aff8-a31af3531810 | -0.1544 | -51.55579 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98a6ac75-71c8-3cd0-9b07-f26838ec07f4 | 3.36692 | -51.26772 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e69965c-3467-396c-b08d-79210a5fe6d7 | -1.88607 | -47.97006 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d1a1db6-9951-39ee-af34-b6f525c1fe75 | -2.299 | -48.63498 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70029a83-0f04-36b1-b677-246aefed3fdf | -2.33723 | -46.56766 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88391bbd-8382-3264-80c3-dbe555b2af1d | -1.65063 | -52.05044 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a754833d-ca04-3790-9921-08e07d961adb | -1.23072 | -54.15889 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 617510f2-e3d6-3842-8ad2-d16cd80be59d | -2.10047 | -48.96878 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34d9938e-1946-3192-bd6b-daf230281a49 | -1.30189 | -54.66805 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09bf5b43-860a-393c-8e40-b07ebef3f060 | 0.98802 | -51.28494 | 2024-11-10 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e15f8c4-f8a3-37df-8f1b-3e3f9707792e | -2.31382 | -48.2385 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ac2d164-a438-3894-81b1-46dca0336ed8 | 2.42456 | -50.77841 | 2024-11-10 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4445cddc-9730-3a0c-909e-c8b5a56acdf0 | -2.66916 | -46.78664 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1149ef38-18a6-3617-9678-a1dd8870f4a3 | -3.0024 | -40.28471 | 2024-11-10 04:36:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be7ce6c7-0f38-3891-871d-f71445240081 | -2.57469 | -47.34923 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c86ee91-3070-3b87-bcd6-d99585eb1bfa | -1.47575 | -52.08265 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32f5f3b4-37b1-3e68-afcd-44f1fbb7cab3 | -0.03283 | -51.12623 | 2024-11-10 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca2a7d67-4cf0-31a6-9219-1696c31407d3 | -2.22568 | -48.39057 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ca3a91-cb97-3cab-bb22-28a66655aa59 | -1.67618 | -52.05911 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 14212632-ec76-35af-a7bb-8eb5ff482176 | -2.68394 | -46.78139 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd17fcb6-a34b-3975-9cfd-589d1ef4d08e | -1.67381 | -52.12339 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d2684af-a88f-3e8a-a634-1e81ada97732 | -1.77587 | -52.35189 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d2d8d3a-a7c6-3c1d-99af-d4228fa67649 | -2.25275 | -46.50166 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b27dcdaa-10e3-3ae1-83ad-aa829c919329 | -1.0578 | -51.74578 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65e72185-875f-3cc6-b7a5-b3b12ef3e671 | -2.38497 | -47.82827 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| facb54a8-4073-36b0-b326-305ff1b263e4 | -1.18045 | -51.99796 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b8f75e2-3367-3a3e-bbd8-aedbed153d56 | -1.62489 | -52.23738 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc638aa3-1f00-3308-bbd5-5970d39d6daf | -1.67089 | -50.48839 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d935d67-afdb-3578-825d-5fd0952fff0e | -2.90303 | -45.14788 | 2024-11-10 04:36:00 | NPP-375D | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78bcc4bb-60f7-3444-be8c-731cfbacc5d8 | -2.69358 | -46.80908 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9a6c0fc-f3ec-3675-848c-3628bd2b58a9 | -2.46112 | -46.33463 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd8c13c8-82bb-3fcc-9b0f-dad915f6f531 | -2.1146 | -50.15461 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b14d89a7-704f-3566-8582-c395a75aa68f | -1.4473 | -54.29296 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7ca96c9-2a1a-3ba6-b668-8d5c433b2e17 | -1.51776 | -52.63695 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bd62bf3-d58a-34eb-8c7f-600cff7ed58d | -1.13267 | -54.20996 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c813aad9-db2e-3ebf-841c-5440896627ae | -1.40059 | -52.36411 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2fdf753f-50fc-3e14-b070-d3340d0f3044 | -1.33721 | -51.41662 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875fa102-1778-3821-b511-81ec77b693c4 | -2.14369 | -48.11677 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 463ff74f-156d-3deb-b7c9-2973c0136e1f | -2.07477 | -50.34564 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92593943-fbae-3f9a-868b-4f740e9209f1 | -2.10942 | -48.29146 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42e79e88-f8a1-3dde-afb4-b42c214e148d | -2.52465 | -46.30122 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9012400-dfde-398c-aec4-c3ce95e0efb4 | -2.33566 | -48.51006 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 771f041a-9487-333f-bbf8-b060cee60df7 | -2.64725 | -46.54948 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e82f914c-6e34-30d3-8d86-406c71598353 | -2.34756 | -48.92607 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fc009b8-284d-3d99-89ae-37b98a66e0c3 | -2.63281 | -46.79597 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 429a8a6a-dc84-3feb-a625-46c681854a34 | -1.28357 | -53.71311 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 09577206-9b70-33b7-985c-ddffedb4d1f7 | -1.05497 | -47.89408 | 2024-11-10 04:36:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| befd1771-0b22-3473-bd4d-c0b92664e6b5 | -2.2912 | -48.42552 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aeb0f967-48e5-352b-9657-5e9f07ee0c7c | -2.33021 | -49.12251 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b9ad186-15ff-31da-b8ee-d7c848c1837b | -1.33117 | -54.59991 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62c459e4-2c9c-3e00-ac0b-80b9ee6b70b1 | -2.21343 | -48.36044 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README56.md)
