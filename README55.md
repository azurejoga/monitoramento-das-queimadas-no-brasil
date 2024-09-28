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
| 942ce73b-ef93-3414-893d-24b1a9a2a743 | -12.39566 | -50.46303 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f8bb03df-4c85-3e86-a8ae-a3ef0a445939 | -12.39497 | -50.45518 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bab9823-362e-3544-ab83-301156930c0a | -12.39483 | -50.46793 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| df9ac6e2-f21f-3325-98e3-d846184e5019 | -12.39411 | -50.46006 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 15d365b8-57b8-375d-a289-314b5161a960 | -12.39325 | -50.46494 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 88be4f85-71d0-3168-903a-463e79881171 | -12.39265 | -50.45745 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d082e24-a832-3d73-a090-a1866579f58b | -12.39239 | -50.46984 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 445dda77-7f36-3016-a646-b834598c0bcb | -12.39113 | -50.4545 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78382aa7-04d7-32f3-92c5-fba1ce00bd2f | -12.39098 | -50.46724 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a7751eb4-c316-3199-b4f2-e077fb006a9b | -12.39027 | -50.45938 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 41dc4129-70ca-3473-9219-5e9f2e685f82 | -12.39015 | -50.47214 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af962529-85f7-37f2-8252-a401161fb3db | -12.38932 | -50.47704 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3595b6bf-c8f0-3192-99b6-e9177569e905 | -12.38848 | -50.48195 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 980df57c-905f-316c-98b2-99ceeaf0072d | -12.3868 | -50.47894 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a372050e-8f6d-3448-bdab-09facab63c60 | -12.38463 | -50.48127 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b64e1cf4-a78d-3c1d-a55b-2064ceb4b84f | -12.38295 | -50.47826 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac0248bd-798c-3f1c-819b-b8e20b5c426a | -12.38209 | -50.48316 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d742a993-517d-31de-9fd3-82b41adbffe4 | -12.38078 | -50.48058 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cb1e0cd-a221-3936-b237-7928fbb92ca1 | -12.37893 | -50.44493 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e1c8f97-d85c-3408-8bda-cbe288a6f667 | -12.37593 | -50.43936 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4b21eac-dea6-3ed6-a2ea-8da359d13947 | -12.37509 | -50.44425 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3165eaa3-045a-3e2b-81dd-dc0553266088 | -12.32812 | -50.44093 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3febcca-5c89-3882-9aa8-d5ef0d17c349 | -12.32727 | -50.44582 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db0d0c3f-0ffb-3808-8b3c-73b5a6830a2f | -12.32342 | -50.44514 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9de67a2-67e1-39f5-8f11-f923038dfd89 | -12.31957 | -50.44445 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 10e0c47f-1669-3a50-8a2c-2e63d4320261 | -12.31872 | -50.44934 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0440e188-b203-3e3a-a875-021d84a9272d | -12.31402 | -50.45355 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| becfe465-0694-34f5-b8ff-1f8690612595 | -14.87827 | -51.46077 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3ecae4e4-2b44-3184-961f-e67fabfaeb01 | -14.87527 | -51.45486 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 33fcf824-830a-3926-98cc-d93e65d52b44 | -14.87435 | -51.46004 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f31ebb64-6302-355c-aab6-e2c6a9389b85 | -14.87217 | -51.54041 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fad654f-e979-3794-8a09-045ebe193ae2 | -14.87134 | -51.45412 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e6855641-f7e6-3188-9dd0-bf1720609ce7 | -14.86822 | -51.53967 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ba7b3fe-cecb-3f82-a0d6-f06cc2454e62 | -14.86741 | -51.45339 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 106e2058-5a56-3820-bd0b-0bb70b43c904 | -14.86427 | -51.53893 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8373a89a-c1c7-31b4-b5fb-8e4d7cf8ed42 | -14.86009 | -51.40402 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f38128f7-984b-30e3-a76f-bbfb4efd3d05 | -14.85524 | -51.40843 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 687c2040-07ba-3652-9273-41c97d8b21d0 | -14.84741 | -51.40697 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 311cd02f-29a4-3f65-8fc8-db937262220f | -14.84734 | -51.40927 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 86dd5686-62f0-3d7d-a3eb-d4450fb93be0 | -14.84051 | -51.40038 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a0443e1a-f646-3da4-8c0c-dbe9e844015a | -14.838 | -51.43956 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66ed074e-fee5-3480-a9fe-5b2db37bf20c | -14.83693 | -51.44237 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db08e786-6bbf-3e14-b4b2-1a9346149b2f | -14.83378 | -51.41509 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2e71564-c69f-394a-93bd-cd71c60eb247 | -14.83076 | -51.41149 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cc0af00b-2250-3b6a-ad35-e2e3b770a719 | -14.82986 | -51.41435 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 82e4abcc-60be-36b2-a9ba-cb46c17b3b4a | -14.82774 | -51.40561 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3a94cbdd-7fbe-38c2-97e7-0caf6b0f0932 | -14.82382 | -51.40488 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4cbed169-aa3e-37da-ac31-95fb66cc07e2 | -14.8199 | -51.40414 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fdda08b4-ca82-394c-abcd-8acc43354369 | -14.81899 | -51.4093 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7121aa90-77ac-3725-9e7d-04dbdd05dd06 | -13.74551 | -51.10763 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c871f872-4e80-36d6-b025-a3b3ea638379 | -13.7446 | -51.11276 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9918321e-5e87-3250-a7d2-019515e4d779 | -13.70426 | -51.08958 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17dd8d6e-f808-39fd-a609-a0d90b1f3598 | -13.70373 | -51.09261 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1352abcf-7dc8-36c0-a4c5-b205754d5a51 | -13.69982 | -51.09189 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e97a53e7-9c96-3267-a247-3bee4a94e537 | -13.69942 | -51.09398 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb37c17f-285f-3023-b42d-6e52d1cde076 | -13.6959 | -51.09118 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffba4241-4869-39cf-8a09-7f5a9fa24951 | -13.69551 | -51.09327 | 2024-09-28 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ac297ef-d86d-335d-b782-7e3fc692cf98 | -8.7388 | -51.01577 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab89dad5-6416-39a7-8a03-771b5169016a | -8.73096 | -51.01082 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ab6cf63-dd4f-34dd-a720-fb5debffc1a1 | -8.73034 | -51.01443 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ac624a9-d2d6-3e2b-aa5b-6b06552976c7 | -8.65263 | -50.23025 | 2024-09-28 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b0c827d-7811-30a6-bbc7-c2854cecce28 | -8.64922 | -50.22601 | 2024-09-28 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a920e8d-d01a-3abe-9b11-433a107cf680 | -8.64862 | -50.22953 | 2024-09-28 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c50c645e-149d-3bce-a0fe-8cd608f13e9d | -9.35044 | -50.74805 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e394754-1588-352d-a6e8-0e34b2ec523a | -9.3498 | -50.75179 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c519ee08-4bd4-369d-94ea-40e13cefd8ad | -9.34698 | -50.74363 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1887f071-5f90-3512-a697-6c0f06d334f4 | -9.34634 | -50.74734 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51c2c04d-2102-3cb6-8291-fa286b5dd160 | -9.34571 | -50.75099 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e785664e-a3d7-3f18-b23f-6517219fb0b3 | -9.3429 | -50.74275 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56212409-179e-3932-9da9-48cd716b98f0 | -9.34228 | -50.74637 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a5a2bbd-7436-3398-a8d3-5893a743e6d7 | -9.33945 | -50.73825 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c3bf5fd-2260-3528-a824-f3211843751c | -9.31659 | -50.77241 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00892775-56fa-3dbb-a156-98ab9641ed62 | -9.31183 | -50.77543 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12353f1c-9945-389f-a018-eeadd6b37364 | -9.30363 | -50.77381 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f12f98b1-a915-3f4b-bc1b-3d1be54577e9 | -9.30023 | -50.76902 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 703bed7a-49ec-39ff-8d48-0767c4e146ca | -9.04357 | -51.53054 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7734b1d6-bb86-3543-bc24-a7b4c5722a03 | -9.04281 | -51.52739 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6ff0226-6d45-337b-802b-1edafde500a9 | -9.04207 | -51.53173 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19affc6e-c57c-34cc-bed7-079af27e3a1d | -9.03998 | -51.52552 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2027ff7-f5e3-3ae9-8498-884be3316e68 | -9.03921 | -51.52983 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e52bb9c5-dc9b-3cd4-8d03-283abf2142f9 | -9.03846 | -51.52668 | 2024-09-28 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7958809d-ea72-3d55-84e6-478c179259b9 | -9.74498 | -50.6693 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34969030-db1f-3e67-895e-c7f2f2ce0952 | -9.74434 | -50.67293 | 2024-09-28 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 187a6242-8257-34a0-83bb-e5143006b18f | -10.84885 | -51.06491 | 2024-09-28 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85861a17-aebd-354b-aa71-356c442696cc | -10.60957 | -51.09239 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0923cdef-71ed-3a1a-bcbe-eedc7f8cb14b | -10.60892 | -51.09615 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c311f594-ead2-361c-9878-01a5ad45fa8d | -10.60546 | -51.09166 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e03627d7-f4f8-3936-8607-335e875770ee | -10.6048 | -51.09542 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d978406e-a158-3183-9480-baddd58a0a79 | -10.60069 | -51.09468 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 15698f75-2ee7-3757-8c1b-f3d720e558a3 | -10.60004 | -51.09844 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c1b824b-ea7a-3127-9b61-2bfcc8fc7d72 | -10.59938 | -51.1022 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21d46d7a-4f6b-3eb1-bb4e-8b288c25d7e3 | -10.59527 | -51.10146 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62b0fd5c-8c3c-3afb-bd41-4e69d1ba5047 | -10.55346 | -51.09774 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9347aac-9817-300d-8bc3-a861ea74853e | -10.54458 | -51.09993 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 122b824d-34d7-39e5-a818-4f3fd36e3e9a | -10.53981 | -51.10287 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3428ace-e094-3e70-be2e-195ddab0b7de | -10.53745 | -51.10152 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61705874-8b33-3531-8e0e-5831973da618 | -10.53575 | -51.10181 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7631ef2c-f161-30b0-881c-14aaf437ce4c | -10.53278 | -51.10397 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2ef0c64-6a22-34e6-8e8b-6a3ed39e7965 | -10.53108 | -51.10421 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b9b7232-bb4d-37b3-aa5c-46d6f7c8a148 | -10.52809 | -51.10654 | 2024-09-28 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README56.md)
