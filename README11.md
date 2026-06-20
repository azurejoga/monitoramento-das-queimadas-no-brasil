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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9d9923f-ff7a-3062-8fbd-710f28b4ee01 | -17.4493 | -47.16005 | 2026-06-20 05:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e2b787c-77b0-3216-ba37-c110dc60036c | -13.2974 | -45.22734 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5feb5784-3723-31d7-9fbe-9444cfdc47d3 | -12.7899 | -44.49105 | 2026-06-20 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87039189-ae6f-36b7-ab81-b5bcc8d73242 | -10.68261 | -60.76036 | 2026-06-20 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 72107e14-298c-3151-ab32-854210cc5c91 | -11.66605 | -56.76415 | 2026-06-20 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46821b98-7970-3750-b839-e8cb75659be7 | -13.19532 | -50.34854 | 2026-06-20 05:04:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f2cb962d-89b6-39d7-ad02-aad218a18225 | -13.83198 | -47.12866 | 2026-06-20 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36a18aa3-8612-3216-be00-bffc275883d1 | -13.29837 | -45.21898 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 275b8d19-b00e-3dc7-9b70-08659a49a0bd | -10.27701 | -60.54617 | 2026-06-20 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81361ba7-722b-377e-bc32-1cbc64b09b57 | -12.5441 | -45.0199 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 889831be-2eea-328c-8f67-4e596dcdb18c | -11.79607 | -52.51218 | 2026-06-20 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f05ab494-9e33-3fca-9175-d2157c723c47 | -12.54997 | -45.02046 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| fc855081-d2e8-3b04-a634-73081fc80c65 | -13.19996 | -50.34539 | 2026-06-20 05:04:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55a82772-f16b-3549-b259-0493332b63af | -14.85618 | -48.11507 | 2026-06-20 05:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d07558b-2020-315a-84c9-750e00b366e2 | -12.78492 | -44.48111 | 2026-06-20 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a332916-331b-3747-9885-cfe56a9f837e | -12.52103 | -48.29721 | 2026-06-20 05:04:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5f9cc4b-bb1a-313a-b610-5750b4defd59 | -12.5536 | -44.9941 | 2026-06-20 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ca7b43da-8f83-3949-8cfe-e975bf20af54 | -12.5339 | -45.0204 | 2026-06-20 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| d0691f0a-6d4b-3939-93c7-8c1b0af9b986 | -12.5527 | -45.0406 | 2026-06-20 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 760bb30e-d136-3e52-acb8-14f4198a2f06 | -12.5334 | -45.0436 | 2026-06-20 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 92314c1a-5107-302e-8515-a4beb183b25d | -12.5531 | -45.0174 | 2026-06-20 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 424.8 |
| 3dbb3fa3-8714-3822-a68d-ff992e116bd0 | -12.5531 | -45.0174 | 2026-06-20 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 350.6 |
| fa1f42d0-a80f-3829-b24e-022e575646b0 | -12.5339 | -45.0204 | 2026-06-20 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| c6b83eea-e662-3a6a-bdd4-4e44f6a15d5d | -12.5334 | -45.0436 | 2026-06-20 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 0d1ef755-1bdf-3e4e-bc23-893c89e8d509 | -12.5527 | -45.0406 | 2026-06-20 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| bfa38c11-e0c8-3ae9-8428-c14d348b3b28 | -12.5536 | -44.9941 | 2026-06-20 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7003579e-4cc1-3279-9a24-418c3a9212bc | -12.5724 | -45.0143 | 2026-06-20 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d2df6151-2494-3d46-b114-c247eaf5c7e5 | -12.5339 | -45.0204 | 2026-06-20 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 95b084f6-2579-3f5a-831f-add6f6909477 | -12.5527 | -45.0406 | 2026-06-20 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| a7eb277f-92b0-3210-8d19-c033a272e8e3 | -12.5536 | -44.9941 | 2026-06-20 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 33f891f4-134e-355b-84fe-74a322038bfe | -12.5531 | -45.0174 | 2026-06-20 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 451.6 |
| 3e38078e-bb11-30da-a1f1-740f1da4409b | -12.5334 | -45.0436 | 2026-06-20 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c33a78a4-34ca-3fe8-9aeb-0544b81045c4 | -12.5531 | -45.0174 | 2026-06-20 05:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 331.2 |
| 52a0738e-ff34-32e7-ab41-b05be7926dba | -12.5339 | -45.0204 | 2026-06-20 05:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 6a4c9797-6fbe-3cec-889e-658a86d89616 | -12.5334 | -45.0436 | 2026-06-20 05:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| c82accb9-9db8-3e45-bf49-8e0348afa5fc | -12.5527 | -45.0406 | 2026-06-20 05:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 96610034-ff81-3a79-9c84-270c585bbbcb | -7.29647 | -55.32031 | 2026-06-20 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 960913ec-401a-3042-96f8-c43dc9c1285a | -2.32752 | -60.06136 | 2026-06-20 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c156ce1-e854-388f-8673-31654fcbb519 | -7.29711 | -55.31522 | 2026-06-20 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8394db6-0770-3e98-a2bd-a0bbf872b6b3 | -12.5339 | -45.0204 | 2026-06-20 05:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| e775257d-ef3d-33b7-bd9e-e27717829104 | -12.5531 | -45.0174 | 2026-06-20 05:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| b4eb1fc8-5522-3c92-ad75-3afff08ba4e8 | -13.1336 | -53.7833 | 2026-06-20 05:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8ac6638d-6898-3bba-9467-af07f02e70e9 | -12.5334 | -45.0436 | 2026-06-20 05:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b2a4889d-57dc-3234-9b83-d3b60ea722a6 | -12.5527 | -45.0406 | 2026-06-20 05:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dba7b071-9369-3610-8f19-d74eec915164 | -9.21129 | -58.06709 | 2026-06-20 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6afd24d7-c7bd-3a55-b4cd-7db1a3aff83f | -9.20097 | -58.06209 | 2026-06-20 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cad4c562-6e48-3772-9fc6-9bc1b2163649 | -9.20592 | -58.06629 | 2026-06-20 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1af0f17e-889e-3c48-bc2f-fc8295267b43 | -9.02249 | -63.54869 | 2026-06-20 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3339982-bfa3-35a6-9fdf-379e89c77ba4 | -9.02314 | -63.54421 | 2026-06-20 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b5d1068-c67e-368b-b68c-e97115dbff8c | -12.42653 | -58.41746 | 2026-06-20 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d374fe3-ff56-3a3c-aaa3-6381c14c40ca | -9.01812 | -63.55263 | 2026-06-20 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f87b8b2-383b-3d3a-9545-334b088c389c | -9.61642 | -67.31846 | 2026-06-20 05:50:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b201f90-5bc4-394a-9544-f319c4e4e2f0 | -10.71007 | -60.74212 | 2026-06-20 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04c27d15-56ec-3312-b614-e38caa4f85d9 | -9.20961 | -64.08656 | 2026-06-20 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae288eb0-6c88-3f09-aa64-1e35ca2b2eed | -9.20891 | -58.06411 | 2026-06-20 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08190ca-0dc4-37d9-8fcc-17de666ae141 | -9.02185 | -63.55318 | 2026-06-20 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9355c015-e724-3ae2-b003-0d6b45051f2f | -12.43201 | -58.41821 | 2026-06-20 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbbb9bbf-1593-3329-853c-bce9db4b7b84 | -7.34338 | -72.60403 | 2026-06-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 715c3cce-8874-3b0b-b386-36943954f571 | -9.01877 | -63.54814 | 2026-06-20 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 013d32eb-68e3-3587-ad64-3d917c951094 | -9.20636 | -58.06283 | 2026-06-20 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5309eb5-fef8-33be-a345-158a26916559 | -9.01941 | -63.54366 | 2026-06-20 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e28e95a7-727d-36e7-a2e5-e1a02ce620a6 | -10.57705 | -57.323 | 2026-06-20 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac24fc41-a426-34fa-b280-f0350cc1a18c | -9.20844 | -58.06758 | 2026-06-20 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f211a072-a8e4-3d29-a564-7f98439e17b8 | -9.85551 | -61.42699 | 2026-06-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2cf9b06c-9387-3222-afef-03d5066bb393 | -12.5531 | -45.0174 | 2026-06-20 06:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 88bfce26-d8f7-331d-ae6c-dbf7ba301f12 | -12.5527 | -45.0406 | 2026-06-20 06:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c48a0950-7b68-3be5-9673-b425f13791ce | -12.5339 | -45.0204 | 2026-06-20 06:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3615ef8a-e264-3317-933f-1f3dc816ca48 | -12.5536 | -44.9941 | 2026-06-20 06:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 4f50a269-d7f9-32af-9c5a-4aeba7ee351f | -12.5531 | -45.0174 | 2026-06-20 06:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ac9acf10-8d71-33a2-9183-d88c20b541a1 | -12.5339 | -45.0204 | 2026-06-20 06:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0fd4b8bf-039b-39a7-9d90-fe939de41f9b | -12.5527 | -45.0406 | 2026-06-20 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| c8e7978c-f520-30bf-bdd1-b7d87f6b0c0c | -12.5531 | -45.0174 | 2026-06-20 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 008ae5e2-aa02-3af4-84d2-c848c02fc983 | -9.02082 | -63.55373 | 2026-06-20 06:22:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4e5864d-6d62-3dd9-a192-36ceaee61acf | -7.34304 | -72.60272 | 2026-06-20 06:22:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b32fedc2-8f4b-3c30-a629-c5200427720a | -9.01606 | -63.54463 | 2026-06-20 06:22:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46d91ae6-6526-3c0b-a177-d71a18459a6a | -9.02137 | -63.5496 | 2026-06-20 06:22:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60697d02-c579-318a-8b2a-30e8b27228e1 | -7.3464 | -72.60324 | 2026-06-20 06:22:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e162d7e-1273-370c-81ec-30e12e3605c3 | -9.02191 | -63.54548 | 2026-06-20 06:22:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cc5686f-8ef9-300a-9937-cbfada9251bd | -12.5339 | -45.0204 | 2026-06-20 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 91e7aea2-05df-325d-be93-dcdb8c7934b3 | -12.5724 | -45.0143 | 2026-06-20 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5e95a263-730c-3a0d-9d4f-5a3c2c0bf000 | -11.1857 | -46.5847 | 2026-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| edef28d4-af8d-31e5-995c-fc491bdbbcec | -12.5527 | -45.0406 | 2026-06-20 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 0d410caa-7f28-37d9-b3f3-eb28b62f1b13 | -11.1861 | -46.5621 | 2026-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 92b0d643-abe8-3821-a088-50c22d18dc65 | -12.5531 | -45.0174 | 2026-06-20 06:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 265.0 |
| d09828bd-6c0d-395e-8bbf-687b57189b3b | -11.2052 | -46.5596 | 2026-06-20 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1cc992ff-c56b-32f1-a62f-f40fd1b71654 | -12.5531 | -45.0174 | 2026-06-20 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 253.1 |
| bc84f7f4-994c-3cd1-b67b-b07bd0458d26 | -12.5334 | -45.0436 | 2026-06-20 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 8aac503c-1ce2-3971-96c0-cc505f41931e | -12.5527 | -45.0406 | 2026-06-20 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 2021f38c-9eb3-3d1a-bb59-4cad8981756b | -12.5339 | -45.0204 | 2026-06-20 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e4948e28-7787-3aa1-a3e2-754723190039 | -12.5724 | -45.0143 | 2026-06-20 06:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 35431dc7-035c-3a8a-ac0a-87cdc417f31f | -7.34556 | -72.60236 | 2026-06-20 06:44:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cffb576e-fb26-3813-92c7-8e75bbe140c3 | -12.5527 | -45.0406 | 2026-06-20 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 14ad3229-75c7-39b1-8327-f563aa6efc9a | -12.5724 | -45.0143 | 2026-06-20 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3c09f113-4590-38e3-a5b4-63deb718d9ef | -12.5339 | -45.0204 | 2026-06-20 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7c58718b-6e7e-3312-b7af-22ac3ac0f589 | -12.5531 | -45.0174 | 2026-06-20 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 285.8 |
| 5728de72-fbaa-3543-978d-5c6eb16c41c5 | -12.5339 | -45.0204 | 2026-06-20 07:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 46e5c229-6a38-30a0-bd40-cd8ce3c4f262 | -12.5527 | -45.0406 | 2026-06-20 07:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 2da81266-223c-30a8-8b72-8c4d302ae642 | -12.5334 | -45.0436 | 2026-06-20 07:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 84b9ed8b-4cb0-384d-a583-4b1b13038f9b | -12.5724 | -45.0143 | 2026-06-20 07:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d352e836-9e4b-3fde-8301-6973484547a4 | -12.5531 | -45.0174 | 2026-06-20 07:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 234.6 |


[Clique aqui para ver as próximas entradas](README12.md)
