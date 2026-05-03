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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35b7cad7-38d1-3183-83be-692d5e0ee697 | -8.32931 | -45.35766 | 2026-05-03 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdb30d0e-f014-36b6-b515-3896f6395539 | -11.64117 | -52.56163 | 2026-05-03 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d69117f-0fab-3cda-808e-12b7b61844b2 | -12.35559 | -50.02692 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60a80523-1c7e-3b66-a57b-6576e0d2704a | -9.67564 | -43.79212 | 2026-05-03 04:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd40a58d-b9c6-3527-8159-121175d81ffb | -9.56612 | -50.6793 | 2026-05-03 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acd72f30-5da6-3297-8bdc-091e2ebf7b7e | -12.37724 | -50.0415 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c83873-c4ef-3d73-802d-0ebc494feb4a | -12.36561 | -50.02858 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a5840f8e-a9d9-3a55-bc7b-4b597f77e0a2 | -12.37676 | -50.02313 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9eadae40-ccb1-3e2f-af7e-1fdb9d0a7b1c | -11.88844 | -43.81175 | 2026-05-03 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63082a86-4a8a-3e48-bc8a-253ca8e4db9f | -11.30417 | -54.73348 | 2026-05-03 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8098d429-3dbc-3f6b-86be-da05ea279472 | -12.46426 | -44.30097 | 2026-05-03 04:42:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2424dffa-aeac-3921-a099-818df639fd50 | -7.86474 | -61.49953 | 2026-05-03 04:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c458af4-4552-3c21-b26d-e5b7fac33031 | -10.63905 | -48.00547 | 2026-05-03 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 90265aae-b698-3286-8f8b-e6b19174865b | -10.58916 | -44.32514 | 2026-05-03 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8df673fd-04d3-37a3-ac74-6d7fa766704f | -12.37733 | -50.01957 | 2026-05-03 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 028943e5-715d-38d0-bf3d-2c3e5d1543b2 | -8.33291 | -45.3583 | 2026-05-03 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bde03837-7a5e-3c94-9015-3eb91a26be3b | -9.67161 | -43.79156 | 2026-05-03 04:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4c1c1f4f-b1c2-328b-bb32-f94a6a205cb7 | -13.22277 | -54.53945 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 871fc9b7-c697-3eb6-95eb-fab06ca9e5c7 | -13.23167 | -54.53574 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b4759df-5100-3aa0-a252-a6bf737cb9aa | -18.25703 | -47.01647 | 2026-05-03 04:44:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fab73166-b4c8-32e8-874c-cd98e7a4df01 | -20.19392 | -46.46546 | 2026-05-03 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90c9043a-2bb3-3fb8-9c01-d10063699e37 | -13.22581 | -54.54554 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a94fcba-7769-31c1-83a0-027ce46c5b25 | -17.94852 | -52.97972 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8d0ee5c-25e1-30fc-bc8d-84717cedf95c | -13.20189 | -54.54091 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24d1f275-ac2e-3538-906f-b66aa550ab72 | -18.25661 | -51.26255 | 2026-05-03 04:44:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0927a58-d730-37ce-acb3-f8c6a29b4401 | -13.21785 | -54.54395 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48c75102-9014-30fa-a7ee-abe454900925 | -13.19978 | -54.52966 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdf85c1c-614b-31f6-829c-44870f86ad50 | -13.22089 | -54.55008 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c36087ce-8869-3583-99b4-39196f07dfd8 | -14.06598 | -53.39637 | 2026-05-03 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f51d4e11-877b-30cf-9bd7-cf62b37e15f0 | -17.94717 | -52.98766 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b14f90f-eccd-3d6c-a4e9-4fe21fdb263f | -13.79452 | -48.23994 | 2026-05-03 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e85a395-40bc-381d-917d-6b1fb9991b0a | -17.94303 | -52.99097 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08494884-e4fe-3232-92c1-d1c105e683fc | -17.94573 | -52.97509 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66c8c2e7-66c2-3284-adbe-971dc1fd54fd | -17.9465 | -52.99163 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14d2533c-0d2a-3ded-b6de-5b1bc0d06ba1 | -13.21879 | -54.53867 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 471b5b65-48ff-38ff-9bbe-4bd900d2cbf8 | -17.94371 | -52.987 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93693ed9-7177-37b4-a4e3-01c408d55eb2 | -13.2169 | -54.54928 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38c268f3-b824-37d0-b927-86c3b519cddd | -20.18679 | -46.45858 | 2026-05-03 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed7b1872-5f72-3497-83b6-86b82cb62f5f | -20.19 | -46.46479 | 2026-05-03 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96d533f6-56f4-3958-98ab-ecb4faa22abe | -20.22515 | -50.91433 | 2026-05-03 04:44:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f96eb5c3-b846-3533-833a-d322e2dc1491 | -18.25327 | -51.26197 | 2026-05-03 04:44:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec9872f8-e239-35e5-8210-bec4eacb933b | -18.25687 | -47.01753 | 2026-05-03 04:44:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b0a4bb6-3b49-3195-af97-0d64d2bf9a07 | -13.20377 | -54.53038 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72d68785-81f9-376b-bff8-fb9a89cc7bb2 | -20.18749 | -46.45316 | 2026-05-03 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0981e34-db63-39a6-963d-5eb13ff71350 | -13.20398 | -54.55235 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc56d1e5-504a-38a4-816f-abc530f8f32a | -13.21386 | -54.54317 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bed0ffb-d8d0-3f0f-9a64-5209ac6ec4c3 | -13.19579 | -54.52894 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12ab351f-fee6-3d67-a045-df3d288964e5 | -13.1074 | -51.72684 | 2026-05-03 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5ce37e-d633-3c73-b680-be5cd8d8d3b6 | -13.21175 | -54.53189 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09a7464d-f493-3506-b5cd-90dac93c6f00 | -13.11087 | -51.72744 | 2026-05-03 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffde2526-dcb0-31bb-a36f-7f0b07603ec5 | -17.94438 | -52.98304 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2262b1e3-fa12-3d83-be41-d0caf65a7c67 | -13.20094 | -54.54623 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b05d4e2b-db8b-3d36-ad9e-1fff5ae29fc2 | -13.22675 | -54.54023 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6e356d3-4891-3306-bedd-ba4a937d8887 | -18.2523 | -49.30861 | 2026-05-03 04:44:00 | NPP-375D | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ead89e38-aed8-3d93-b27e-a37dd9c214de | -13.1979 | -54.54019 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffe7b5fd-f0d2-3ec1-bee0-f5bee25ebcb3 | -13.21082 | -54.53711 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af4534f1-f56c-3c70-ac28-c7f07bde6809 | -13.1939 | -54.53948 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfbf18c4-2745-3a51-98fd-38bdca00748d | -13.20776 | -54.53113 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 081abb54-e65a-390b-bbc8-dfc1f7c40b01 | -13.21197 | -54.55383 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb2bc2c5-a846-3002-84f7-70e99714b146 | -13.20893 | -54.54773 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b4be57-af04-38b4-acb7-82ae53c2b3e8 | -17.94988 | -52.97174 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc130197-c07f-37f8-899b-5e642dc04ee8 | -13.20797 | -54.5531 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 456eac90-3ea4-3cb9-951c-0579ebabf2ba | -13.21573 | -54.53265 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| babf04fd-bc0f-3adb-a869-9b382daa134e | -13.23074 | -54.54103 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ce359ca-ace7-31e0-ae14-41393c794c3b | -13.2148 | -54.53789 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1442279b-7d2b-34f9-b581-70d702932923 | -14.68909 | -52.94841 | 2026-05-03 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ba32fc7-62e7-33f6-9535-fb3f796b00c6 | -20.22458 | -50.91801 | 2026-05-03 04:44:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4c677521-1632-3563-bce3-0d32e91f0914 | -17.94236 | -52.99494 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f2f0636-46c6-3e83-a897-ed5c5c0404c5 | -13.21972 | -54.53343 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c31d7c4-3a30-35ae-9b8b-bba9512a656f | -13.20284 | -54.53563 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04343198-f2a1-317a-8111-b80cbaeaf0ee | -13.7962 | -48.25175 | 2026-05-03 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9136c256-2193-3fa6-a187-6d1f9eba686d | -13.19884 | -54.53491 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b79e5d6f-8e8b-3fd1-b410-ec44a6f33c8a | -13.21101 | -54.55921 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccf36580-bda9-3853-bf2d-3347de1ca62f | -13.99674 | -56.63277 | 2026-05-03 04:44:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d099b92c-69f6-3ed5-8b81-76e6f32d8a1f | -19.39925 | -41.97675 | 2026-05-03 04:44:00 | NPP-375D | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7182ccf3-064d-3aba-8cfa-6440f9be3275 | -17.94515 | -52.99957 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8830ec85-9aff-3b6a-bc8b-20c4b3fde97d | -20.1907 | -46.45933 | 2026-05-03 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b6e613b-1738-3988-bdc2-f512ed5a6187 | -17.99741 | -52.97565 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 646e72b4-c4b8-3736-b837-a1422fb68f4b | -13.79282 | -48.25116 | 2026-05-03 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d28ec8b-0139-3001-8907-8337a1346392 | -13.22769 | -54.53497 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8db589a-b596-340d-92db-4c1c6c8edf20 | -13.22183 | -54.54475 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c44ce657-5dcf-3916-a638-031fdf09c7e0 | -13.22463 | -54.52897 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77776673-bd70-3f46-a27b-84c2c2041d1f | -13.19484 | -54.53419 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d80e45a9-84d6-3747-a70e-31c7c2a9a375 | -18.05611 | -52.94572 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ecc8b15-7112-3fa0-91ec-d59da76b5e99 | -13.20589 | -54.54165 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61579f14-64f6-36dc-923e-f2a44078a00c | -13.20987 | -54.5424 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dbfdea6-a723-359f-904d-f6c47f1cbae5 | -13.2237 | -54.5342 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6081553-b343-3b25-9642-3397dc3ddd2f | -18.05544 | -52.94968 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57d0884d-cfd1-3cc0-a304-ef4d1771a48e | -13.21666 | -54.52743 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ee78bf-9ae2-3915-ba59-8271431f6277 | -13.21595 | -54.55462 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08757e0b-d1e7-3bc4-ab90-07354aea7d62 | -13.21292 | -54.54848 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb48bae2-e65e-3478-9331-3803e2e57963 | -17.96644 | -52.95838 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8414d6e-265f-34c3-9cd3-019aa9ea13f5 | -17.94785 | -52.98369 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfbd8e59-24db-3e81-bdbd-5931f09014e9 | -13.20494 | -54.54696 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 527cefce-b422-3b25-bd94-c78d455bada0 | -13.20702 | -54.55845 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 456c1b2f-beeb-374d-8137-07902b86b5df | -20.18361 | -46.45214 | 2026-05-03 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17d4b277-a0cc-3380-9717-d5ad8519d5f5 | -17.96509 | -52.96634 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff326cc7-40ef-3894-91f5-4f7e3c1a9253 | -17.96163 | -52.96569 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df9de7e1-785c-352b-a8a4-1812aa77849e | -13.20683 | -54.53637 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23f235ec-eb10-3273-afda-6c470d76834d | -13.22064 | -54.5282 | 2026-05-03 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
