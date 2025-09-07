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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65068995-0903-3c5d-b3d8-330e47e5f43f | -8.07563 | -52.34685 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7afa5091-8e0c-32b8-be72-84468ada7297 | -13.65795 | -47.91613 | 2025-09-07 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f45f0f0-2d9d-369e-84a8-a329ec75c481 | -10.83933 | -55.10019 | 2025-09-07 05:12:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0b1805d8-ac4b-36f3-b00c-00fb4b0e563d | -13.01046 | -45.2286 | 2025-09-07 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cfe2dc63-a32f-308a-9353-632a3a866275 | -11.77767 | -47.56202 | 2025-09-07 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5eec821-1864-3c83-9230-d7067d97b6a6 | -9.74669 | -48.97429 | 2025-09-07 05:12:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a38fb4ab-723c-3732-822f-f17c060a4f4a | -12.82133 | -52.93735 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8146fb2-f593-3ca0-abde-f93b00b0bf1a | -12.63091 | -56.98006 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98a291cf-9092-39df-a038-0df31679435c | -12.81919 | -48.01529 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6e8d63dd-2f08-35b6-b9bc-4b7d589809fd | -11.16163 | -59.1566 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 157c936b-31dd-3ae5-8840-5cb5da1b7fcf | -11.15655 | -48.39385 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15084630-e398-32d3-a7d7-13012fd819f5 | -10.72932 | -48.58118 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a03dc80c-92a8-3a01-b6c8-33c5245b0ce7 | -11.05242 | -54.17615 | 2025-09-07 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b1ef8909-d3eb-31b9-8474-cd59791b97c9 | -8.62391 | -54.65357 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba0631e9-85dd-36b1-9483-c168785d3a47 | -8.07009 | -52.38471 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ac951aa2-9473-3935-9540-993ec36a6e24 | -12.54896 | -48.07028 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6653abee-51e3-34a0-a924-d28724d5ef9b | -13.83371 | -46.28406 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 42a0799b-f5f8-3f51-822d-6cb038abdae8 | -8.62755 | -54.65414 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab53069f-44e9-3d0e-8a00-c6bed2362577 | -13.91984 | -48.03284 | 2025-09-07 05:12:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13f6bb04-d820-3574-a250-4c943881ad25 | -12.81015 | -48.01337 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9b7d69f2-c7f9-3a7a-9a54-0e71d28f0d7b | -10.06944 | -49.29721 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| afaf6b31-392d-3d14-8745-21a06a2297a8 | -11.57622 | -47.75016 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f4e96c3-f3b5-3f63-bcc1-f18afdd976b2 | -10.72183 | -48.59534 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a8dea3f-50f0-3b3f-a1e6-ffb35b9f228c | -9.45719 | -56.03663 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90b9e0cf-4627-3aac-84f0-9932e86c0ce2 | -10.58119 | -61.2538 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a80f531-33e3-3a32-a193-a09f462ff33f | -13.8302 | -46.28527 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c8bc2512-0d05-33d0-a9c6-013c84e5b956 | -12.82206 | -48.01489 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4425a1e-f84a-3137-aafe-16af971eb006 | -12.81609 | -48.01422 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9568a82a-9fcc-3254-9a0f-d55414b6bb66 | -11.22503 | -55.01818 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 826756b6-7e68-3de1-b41d-b38b64aa9292 | -9.99321 | -51.64661 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6c79c4d-e963-3bcd-85a6-eb2b2edea9bf | -13.92035 | -48.02817 | 2025-09-07 05:12:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53ff6b1f-89ed-3bb0-8c88-67360a682c77 | -11.1677 | -59.16116 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e042cf90-8927-32e2-8679-476335fa4865 | -11.81911 | -46.76795 | 2025-09-07 05:12:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c1d01b2-bab3-3024-a420-8dde3868a68e | -11.7789 | -60.89316 | 2025-09-07 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2947022d-2ded-39eb-84d4-e971ec5cc20b | -12.03017 | -63.36381 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fbf010d-cafc-3253-90ad-c9db2b3ee3c8 | -10.76852 | -59.84813 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18a986cf-809a-3423-bda1-9315b1ef4445 | -10.46322 | -53.61766 | 2025-09-07 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d25731d1-c96c-3f53-88e7-5ecdd220d618 | -12.55438 | -48.07528 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc38a4fc-9761-3275-8fad-8b97330d0df6 | -8.51264 | -51.31216 | 2025-09-07 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbaebc84-1f4d-32e9-87b6-08f9c5b0fbd9 | -13.83076 | -46.28003 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fed182c5-1aee-3a46-b9e5-e650cf57e4da | -13.00578 | -54.81853 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72ec8714-6dfe-31cd-90a1-c933d19d15a2 | -11.78233 | -60.89375 | 2025-09-07 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82b07b85-103e-33e6-bb40-0d8cae5544e1 | -9.98807 | -51.65072 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0f1ad8c-d361-321c-96d7-88daa00617e6 | -12.71744 | -56.56031 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c15033cc-bac5-3ae8-8378-162bc3dff924 | -7.23247 | -56.07321 | 2025-09-07 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee181ae7-2447-3847-8282-803cf4f66a68 | -12.19614 | -53.90339 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47e6a3cc-bf6c-3880-9528-18ad6cfeb5d3 | -10.35247 | -46.45448 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58b52fc3-2151-3569-af98-4f8be524288e | -12.82475 | -56.51945 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce9299de-46a1-35e5-893b-8cb22eabd43b | -13.06243 | -48.06178 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef082fa8-ab0d-3f6d-8cce-6292c4af2d27 | -9.46293 | -56.0453 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa63a71c-9f3c-3725-893c-087fdb28932c | -8.07244 | -52.38392 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d549264f-b8e1-352b-810b-6be29935a946 | -12.62351 | -56.98278 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d66455d-2e5b-325e-b90e-0cbf643ed1a5 | -13.83769 | -46.2786 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71f23e6d-a049-3fc0-9759-84f0e1d5a7c6 | -10.32755 | -52.55704 | 2025-09-07 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1107ed3-a6a2-365c-ac92-915170b44042 | -10.15056 | -61.13464 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7566e17e-497f-3ff2-b958-f955b6083163 | -8.97311 | -62.96137 | 2025-09-07 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45f3f0ad-6fb6-3fd0-b0ff-e5ee63f1bdff | -8.62453 | -54.64928 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbfd5cef-ffb2-3cff-93ee-36e3c5f27f65 | -11.47998 | -55.55169 | 2025-09-07 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d8ae1be-b6ce-3dab-adbf-f9c7460e773f | -8.36037 | -52.56194 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99914522-db1d-39ee-a8b2-e56c68036323 | -7.81298 | -52.13496 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8bab09f-d221-3e03-b60a-206ad015bdf5 | -12.79692 | -48.02309 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0cbd56a8-959f-38e4-bc5c-3420b9a24085 | -10.72223 | -48.59223 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a901a93-e1e8-37f3-a7a5-981dc1a633d9 | -9.44181 | -59.20641 | 2025-09-07 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dd496fc-ba30-349b-ae64-21d8d514ae8c | -11.22135 | -55.01766 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 777fb6cb-b532-3732-a8db-b9cc6623ed87 | -12.12474 | -59.84187 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d42c7af2-57f3-345b-88af-0eb691cb2fb7 | -11.04927 | -54.1707 | 2025-09-07 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3ffaf582-ea57-3c20-b574-b944ae7c6f96 | -13.83963 | -46.26033 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4abd1c78-65c5-34f9-9704-4989bb68ed25 | -12.63377 | -56.98439 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2d529fe-4e90-37bd-8355-18d7acaee345 | -13.01584 | -54.82985 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d2a91b3-b011-3421-9b8d-01288c740998 | -10.57476 | -61.24877 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a66ea915-adbb-3cbd-9ece-30265d37aab5 | -12.95327 | -54.77662 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fe6d690f-a968-3b48-8dda-fc25a6014040 | -8.04688 | -52.36935 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2e86304-f229-3f6f-8cda-6b9a0ce60fd2 | -12.81649 | -52.9409 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d5290d6-99b8-313c-981c-c37663c2096a | -13.02404 | -48.08129 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ddf15f7-f21d-31d2-a79d-1bf74c509ee3 | -11.04856 | -54.17561 | 2025-09-07 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fd2e81c1-ebe9-3b10-a370-761cae1cb742 | -9.33256 | -55.20031 | 2025-09-07 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75eb64b4-36cb-3d87-8ec6-ef6aaba31d9b | -13.84115 | -46.27746 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97aa39d2-773f-34a2-8d6a-64a83a54a046 | -10.32302 | -46.37708 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e843416-545e-359e-a22a-60114b42a3ee | -10.35472 | -46.45683 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b71762c-8f9d-3bd9-9a9a-9deec1c6997f | -12.61325 | -56.98116 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59e59b93-8ccb-334c-bd20-323104cf75b5 | -11.14517 | -48.39241 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 882e6117-49f5-3a9e-9a9d-b264fd0269aa | -9.70705 | -49.4901 | 2025-09-07 05:12:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48200886-53e6-3c7f-aa81-8480060282e4 | -10.46718 | -53.61827 | 2025-09-07 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74b1063b-61a1-330b-b350-0abe89fa59dc | -10.22336 | -50.53259 | 2025-09-07 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3887e8c3-29d1-388b-8bd4-cad0b41b0598 | -11.21639 | -55.02593 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6aee185-e9d5-3bc4-b11a-f1e523dd1a7c | -13.78035 | -52.78025 | 2025-09-07 05:12:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 36bdb068-7a67-3280-bdf4-975254e63e2f | -12.43997 | -63.9319 | 2025-09-07 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff57449-56a8-361d-a2be-4b99ff19990a | -19.55809 | -49.73423 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 16d1d07a-1cad-3bcd-9b2d-84cf8a585466 | -13.91372 | -54.00433 | 2025-09-07 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf5bdf62-0a59-33b1-8876-72c6ddbc1e8b | -14.59093 | -48.10064 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6894d902-76e2-3fff-92b2-fa67858fc9ea | -14.48781 | -48.76094 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44510dd1-bce2-3fad-8b89-84fd53103c04 | -14.35217 | -60.32336 | 2025-09-07 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abc82982-1fd3-32fa-8b11-1fa6c05604bd | -15.50561 | -52.77565 | 2025-09-07 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5f0604a-905d-32ec-b6a5-846db85b9127 | -14.49549 | -53.24639 | 2025-09-07 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9724e456-517d-36d7-b547-5c4439aec29b | -14.59461 | -48.08206 | 2025-09-07 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 02f7e061-577e-3342-ae29-df94c85f143e | -19.88727 | -57.90165 | 2025-09-07 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 56973f97-f3a8-36d2-bd59-3437d4961dc1 | -15.3724 | -46.42807 | 2025-09-07 05:14:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3937f3c9-d763-3139-92d8-7bc6286b5e92 | -16.29074 | -58.11848 | 2025-09-07 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 33852ce8-e39e-3117-b8ca-821b237c869d | -17.70591 | -47.65564 | 2025-09-07 05:14:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 388c50a7-752b-399c-a4d6-a8feb8a976b3 | -16.2883 | -45.6826 | 2025-09-07 05:14:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README74.md)
