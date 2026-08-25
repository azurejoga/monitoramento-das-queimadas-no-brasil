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
| 0c98abf5-d153-3ec7-817a-e4b63fe7d0ae | -13.20616 | -51.47308 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9489778b-48ee-38c9-b4ad-53ba7f833482 | -14.40102 | -52.9572 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc02015c-56d3-3db7-ad60-16dc7c66b4e2 | -14.36004 | -52.9297 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 935a0404-f9bf-3877-9dd0-0b0615fec3a8 | -14.41561 | -53.43727 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f8b3e25-ae80-3a3b-8978-2ad0b3ff7c3e | -12.95078 | -56.61766 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bc38727-1ca0-3c78-8fd0-1b8ee2c68dcf | -15.2457 | -52.79511 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7bd3a97-d990-33a4-8157-0091460cff8e | -13.26105 | -51.45945 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16b3ec7d-4fad-3148-9272-ea206edb9727 | -13.19746 | -51.49731 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e795d8f-26c8-340a-820a-23120eaa8c0a | -14.36337 | -52.90347 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd33f09d-d89c-34ae-bf50-1bad8326e8e3 | -16.41701 | -49.87631 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf4bb957-7e23-3fd1-b875-7f7a13b320af | -13.41559 | -57.02217 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cf82778-3fe3-370e-9faa-570b2d8fe707 | -13.85999 | -54.006 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1928932d-45a3-362e-8790-f1493fde7b7f | -16.38982 | -49.92009 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2b57e42-f32a-3b4c-9158-70b45658c6dc | -16.39921 | -49.9357 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 474899e2-daf6-3872-9f1f-656a4cfae633 | -13.2049 | -51.48349 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 646ae503-d1fd-32c2-ade3-4ba06f54583b | -13.20427 | -51.48869 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 791ef7ff-2b92-3de0-8d49-a41d04d514b4 | -14.91565 | -52.63868 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2daa60cf-e87c-33c1-9c4e-89a29c0b5dca | -16.40634 | -49.92442 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db88f302-10ce-33f0-ba68-ed4f874d0ccd | -16.41772 | -49.92233 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af4528b0-2b49-3c31-83da-c56160a57cfd | -15.30536 | -52.8139 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d06c60c0-4da2-3182-9045-1d1f8cf3b327 | -15.74668 | -48.39744 | 2026-08-25 05:14:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56756682-57b5-3e73-b551-76b7c8bfdad4 | -16.41182 | -49.92538 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5264b265-ea77-3cef-9c37-daf9a01a1824 | -14.35622 | -52.92473 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2198b0c8-8c77-3d58-9197-9e8b71f81bc8 | -16.50024 | -54.6774 | 2026-08-25 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93f7663d-6952-315a-b77e-d510ae79ee5e | -13.40415 | -57.05177 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a36436-20d2-3526-8e99-f1799d7f3ebb | -16.42885 | -49.87021 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4310293d-13b8-3d6e-aefe-cf6d1303577c | -13.89772 | -54.06338 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f62ac418-fcf9-3bf0-85b4-0114688feb20 | -16.17643 | -50.76266 | 2026-08-25 05:14:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e681106-16bd-328a-bb7f-c6522e8eb86b | -13.19306 | -51.37964 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ef3e741-90e0-301f-b801-261f678b894f | -16.39972 | -49.93439 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e6be496f-ac40-3d64-8159-fc93827fad8a | -13.20962 | -51.47784 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f299052d-5a02-307c-a97f-a3ed7491e4b6 | -14.53493 | -53.21078 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2ef30cf-95d2-3a9d-a5e2-271521d1b4fe | -14.7517 | -48.79007 | 2026-08-25 05:14:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 389c3f53-b2cf-38d9-ba68-a0cb33c0afce | -14.40157 | -52.95296 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d5b0f4a-c58e-31c9-9a80-d95b1ed6d850 | -14.49285 | -53.33611 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc4a1f35-4c87-37de-ad21-0ee32b82e354 | -16.40047 | -49.92721 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af0e0c58-74fb-33e0-9fbf-ed73bc057221 | -14.36039 | -51.7556 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db71ae3c-c478-345f-95a3-1cc9b080f45f | -14.75207 | -48.78673 | 2026-08-25 05:14:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8f5bb84-8503-3b9c-b2ca-1c9fb4dd45c1 | -14.40104 | -53.09216 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0a33571-9339-3efd-9db1-fe0b3b8f4fe6 | -14.36775 | -52.90413 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5cde0a81-b986-3b2a-a60d-472514e6957b | -14.35953 | -52.89852 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 553128da-1eb3-3b98-961b-f0fe75329759 | -15.31826 | -52.81994 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c9e5eec-7d8d-3150-a662-ac81f875e74d | -13.65467 | -51.85718 | 2026-08-25 05:14:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d61fba87-aa70-3445-b372-f862cc41dbb0 | -16.41217 | -49.92205 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7899608d-9164-365e-a068-0bcc97b38cf7 | -15.30715 | -52.81256 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90e36017-17a3-30de-affd-69318abb22ab | -16.14132 | -48.90443 | 2026-08-25 05:14:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e65f7f7e-fb98-3ce2-9fc1-b9318093c355 | -13.20364 | -51.4939 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11d579e8-a5af-345b-9261-a8dd30a95e3f | -14.38262 | -51.96656 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 76f23ab6-e187-3456-b36c-84340e0460b0 | -14.3928 | -52.95193 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d396f4d5-3749-31e2-9517-23ec50619f98 | -14.97607 | -52.70319 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bd42e9d-7045-3988-bfdc-f18307dc4215 | -14.39293 | -51.76537 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 90a7d203-6973-39db-aeda-aa3af470707b | -13.87564 | -54.07488 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a9010f0-32fa-34b9-bee9-9ac205e82a55 | -14.35869 | -51.75869 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae83d174-bbb6-3e80-ba23-05bcd34c98b2 | -14.9291 | -52.64092 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4086ca0b-e4fc-335f-9009-b67c0eaa4e48 | -16.06122 | -50.4654 | 2026-08-25 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fdb7724-031a-3754-b19c-655054ea8e64 | -16.41699 | -49.92906 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1423a94-d332-3782-a202-70aa491cb0b5 | -13.93405 | -55.21375 | 2026-08-25 05:14:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39ed7d5b-83ea-317f-acb2-bb5dce78e37b | -15.40913 | -52.84265 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| adbd66e4-8ce9-3c75-8078-76676e54e266 | -13.86857 | -54.00349 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8201550-750c-3969-b7cf-c73cec408881 | -13.19271 | -51.49666 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff5b82e1-2af1-370d-8b61-6d70ff2a320b | -13.40472 | -57.04794 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 594ccff0-fed8-36b7-ba28-7be8b039cf4f | -14.38756 | -51.76991 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cbb242ab-f144-32d4-a7b0-3c31664f470d | -13.19584 | -51.39611 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27ca4490-47c9-3460-825d-bffccd376ed0 | -13.20354 | -51.48757 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 833809ba-9c5c-3dc3-a77d-bc0536df9a14 | -15.24124 | -52.79442 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 159540a0-5309-30d4-96dd-23159d7138c1 | -13.4698 | -57.05718 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17239777-f72b-326c-bf6d-2d16603d880b | -15.30322 | -52.80775 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c566b88d-843f-3a4c-a065-2dd972c1bd8d | -14.382 | -51.97158 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1ed92a83-83d9-32a3-98e3-d391aace285d | -17.31425 | -54.92422 | 2026-08-25 05:14:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 659bf9c5-8391-37ca-868c-42db856e57fa | -14.92014 | -52.6394 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aee61610-f2a4-3499-8d91-80fa38ffe188 | -16.14179 | -48.89995 | 2026-08-25 05:14:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a5ea38a-e789-3eb9-a3a1-d6ff1b92889c | -16.50426 | -54.67801 | 2026-08-25 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3180dbb-778a-3f97-a037-128cf8989c36 | -14.4908 | -53.52143 | 2026-08-25 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eb1745b-d504-3f6d-8c50-2c265d007b9f | -13.87611 | -54.0713 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93d8275d-598d-3c27-9f53-c3dba4d62322 | -15.2507 | -52.7915 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91260811-1adb-3117-b169-8340d73e69a5 | -14.91508 | -52.6433 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1311086f-cfa0-3216-a26a-03dc0508630c | -15.297 | -52.80787 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a520fb3-5a2e-3cdc-bc52-70694bf20b51 | -14.5344 | -53.21499 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68d760a0-4328-3f00-ab7b-268550099548 | -14.36391 | -52.89918 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e9f713a-280d-35e0-8c72-b1645df7de6c | -15.24178 | -52.79007 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df187471-9880-32f4-ab9e-cc0794fb920f | -14.94579 | -52.72641 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 840dad18-9106-389c-88f5-a87e8170d5a6 | -16.42745 | -51.84389 | 2026-08-25 05:14:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dfae05b-4ec3-3b57-b284-18dcadc8c8dd | -13.86404 | -54.00661 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10035cb1-003f-3578-b389-a3949a8763ea | -14.35627 | -52.88905 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54bb2827-facf-3933-a378-40eb75e84a42 | -14.87136 | -52.681 | 2026-08-25 05:14:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77790b52-5a41-3be9-b128-a7b9724bfd94 | -15.33451 | -52.79872 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3776196c-aff7-3bd4-99c8-b8b836265ed1 | -13.16635 | -51.35983 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fcd99d72-b597-30cb-964c-1a33cb80bbdc | -15.27246 | -52.79933 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c9cad62-811e-39d4-8a43-f2143e5e9a0e | -14.38819 | -51.76471 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 740508d4-3f5d-3008-b071-25ac172c7500 | -13.87632 | -55.26428 | 2026-08-25 05:14:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d0bdef7-7593-3f77-9b18-f8ce022eadf8 | -16.0665 | -50.46609 | 2026-08-25 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 708b3ab3-b29f-35dc-bdd7-84b8d9b204dd | -15.86485 | -55.57588 | 2026-08-25 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 212d2d1b-b9e8-374f-afb1-f178840bc8d4 | -13.21028 | -51.47894 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20fd36b2-40da-3064-b4f7-c7164efcb98a | -14.74594 | -48.78902 | 2026-08-25 05:14:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7874b212-9042-3f1e-915a-6e0d16c60d7a | -13.18895 | -51.37369 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52d80d0e-8df7-3a98-9275-c078ab26ea22 | -13.8673 | -54.04466 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2238a8a6-42d8-3e88-a812-16ac1cb9d571 | -13.20965 | -51.48415 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e95f8c17-13f9-3920-8025-9fcc56be10eb | -16.4174 | -49.87268 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0758d824-4ba4-361c-9521-13e7bbf1d2d4 | -14.87544 | -52.64911 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a518b9d-314f-3557-8d51-400cb499bbca | -13.20287 | -51.49277 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README58.md)
