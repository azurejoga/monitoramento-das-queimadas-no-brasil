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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 776d7d86-1b7e-31c4-98e5-743a6ebc283d | -15.61924 | -56.26302 | 2026-09-21 05:08:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 428b6b5c-969c-3521-8983-a5ed589c3c46 | -15.45376 | -48.46584 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 116f9ff6-f7c4-36c9-82ce-b02125f487fd | -15.75652 | -56.45022 | 2026-09-21 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5437555-a1f3-3545-b029-8a03950c1e8a | -16.04615 | -52.53027 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f22da9f0-1cf5-30e9-8169-9325550d4b9b | -14.66032 | -54.45306 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a0b298a-c170-3847-a618-1f4ec2eb7aa0 | -16.68623 | -47.88794 | 2026-09-21 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f27b47b4-1d28-3870-8ede-95c9c55c90c5 | -15.45594 | -48.47628 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22d1cd7e-593c-33c5-aa2d-6b416f91008b | -15.45025 | -48.44754 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8deb742e-02de-3328-bb5f-ee1c70299a2f | -15.46222 | -48.4384 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f1f0bcc-9755-3878-9bb6-ae4cf4964bb0 | -14.6144 | -52.06806 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7b80bbd-07ff-3f3f-ac85-f6621bc41911 | -16.10701 | -49.81771 | 2026-09-21 05:08:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef833354-8f07-3ae3-9635-2d0aed1750b1 | -16.39722 | -54.71403 | 2026-09-21 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ec00451-4e66-3c40-b736-54cdea1bb30a | -14.1801 | -51.79634 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd3fca87-a548-3f0d-8682-0447841e2e81 | -14.66817 | -54.47626 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14564229-12ee-3709-a78f-a421ea704fc0 | -15.4471 | -48.45771 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c8cf630-4222-3350-a33b-67eb5da3c359 | -14.17639 | -51.79166 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d675774-9917-3fde-a98a-76821702f678 | -16.01815 | -52.53623 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e553d8e-a739-3f17-b6f5-6c202bd71f64 | -15.46037 | -48.43797 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c87ba157-53f2-3ecf-bfb9-9e3bf39ff5c7 | -15.4479 | -48.45081 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13e60426-ac2a-3a61-9e64-f07a594f502a | -16.04257 | -52.51152 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a7b62461-7dba-30f9-a92b-fcd92a4636d6 | -15.46428 | -48.46999 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a03fca59-578c-3a46-9c58-5f722e1ace6f | -16.68876 | -47.88522 | 2026-09-21 05:08:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d45c5c6-d039-3990-913b-313f60820dbd | -14.61022 | -52.06728 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2257b4b9-8fdb-31ef-9aaf-8a35ed11b64f | -14.65849 | -54.46597 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c98e0bf-160f-3f58-bb5d-148fa663a01f | -16.04296 | -52.52198 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbe5f494-18bd-39dd-ab76-14480dcc5ab8 | -16.33108 | -53.85094 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d22ce1c7-6525-3a5f-90ad-8dc5cd302ead | -14.08045 | -52.13044 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a6c43f-2ae4-3e28-a389-43e0f6ff6663 | -16.32788 | -53.84552 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ab11557-a20e-3811-9bb1-5cb52c5917fb | -15.47666 | -48.40677 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61601218-69ad-3591-ae96-c9eba344d4e7 | -14.03893 | -52.07725 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f4478ff-e4f6-3a13-a590-28bb2be7fcc4 | -16.39965 | -54.7212 | 2026-09-21 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1021e065-a860-375c-8df1-a5389f7e52d5 | -16.01138 | -52.5233 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62dc0833-6e2a-3a5c-bb05-b45193cbabdf | -16.04153 | -52.51937 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f49fdfd-7899-3b66-a0d5-c10e6cf74dbc | -16.05227 | -52.51528 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 59b395ff-29e0-3550-abec-f36205504282 | -16.32467 | -53.84015 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3e4c81b-4d04-3985-a073-15dc27e9f611 | -16.40026 | -54.71898 | 2026-09-21 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ab9c3d8-b322-3904-ba42-2a749d34d076 | -15.45772 | -48.47988 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a132aad-1312-3913-a31a-0d313ba1302e | -14.05656 | -52.11898 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02825110-ace1-3dbe-8fdb-b3f60b334252 | -14.62281 | -52.06911 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01b6264f-09ee-3056-817c-63383e119097 | -15.86306 | -49.90437 | 2026-09-21 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7cd2fd4b-efe4-30b3-a466-aa287d49d4f3 | -16.04981 | -52.5348 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1986e93-a8fc-31ee-b291-4b54342d5b36 | -15.45173 | -48.46523 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa39d7aa-c699-35df-9c0c-359b897a5ffc | -15.47198 | -48.39911 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 976cd756-3931-383c-ab22-4a54cb9387eb | -16.03929 | -52.51749 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d0b00ea-1d63-353d-8d16-21b9cdc9ac70 | -16.32528 | -53.86509 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57aa5920-77d3-35f3-b09c-561cfbd45604 | -15.45335 | -48.4697 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f327034e-14b4-342d-beed-86d376e0c28d | -16.30858 | -53.84336 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24489538-8635-3341-9682-599f2ddbc568 | -15.40858 | -53.00294 | 2026-09-21 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edd6b316-cc73-3b46-a096-82cc77e02334 | -16.05346 | -52.53938 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7224b2d7-2d89-3eec-8933-d4518dd5d41f | -14.61674 | -52.1162 | 2026-09-21 05:08:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d6ffa0f0-525c-30d3-8ab0-642af8edacd6 | -14.03005 | -52.08023 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b58b2e15-4bb7-39eb-bac2-75e83378b6c0 | -14.65366 | -54.44752 | 2026-09-21 05:08:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdcfa2c7-17f4-3709-914e-d742dfa20388 | -15.75708 | -56.44648 | 2026-09-21 05:08:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea15bdec-8a35-3562-a5cf-41384d8f8e07 | -15.45128 | -48.46916 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ec339a1-9d16-3b64-a3cb-d20b907d1e03 | -16.03977 | -52.51357 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| dff60683-da7e-32ad-b62a-624a7e973706 | -16.30922 | -53.83857 | 2026-09-21 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9be057e3-8d10-32b6-abbb-9b338a4256ce | -16.05177 | -52.51921 | 2026-09-21 05:08:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 650d7792-40a0-36ce-a5d2-5ab3dc5fa91d | -15.61948 | -52.72738 | 2026-09-21 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e7900ca-7960-35ae-92bd-5f8937177e1b | -16.99526 | -56.45602 | 2026-09-21 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 32177b06-92e7-31a6-ab94-38e2e752c80f | -15.4081 | -53.00653 | 2026-09-21 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b850caaf-c281-314b-b321-091f303030a6 | -14.0763 | -52.12981 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2d7f9db-dc2c-3b90-9697-4a9617c1f3dc | -15.88588 | -49.92366 | 2026-09-21 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a26d23f6-1fc3-33a2-9259-0dc41e4ff306 | -15.44748 | -48.45449 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f22a2ffe-1549-302d-ab02-3df12faa0b13 | -15.45263 | -48.47633 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24ca9d3b-b521-39d6-a11b-013568cde34f | -16.3966 | -54.71844 | 2026-09-21 05:08:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 01cddfb4-cf9d-302a-8bc8-47250f9dd83e | -15.46353 | -48.47692 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92f01265-ecf4-3845-9b2d-e6ccdc35e559 | -15.45923 | -48.46603 | 2026-09-21 05:08:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c3e02d2-cdd6-389d-bb69-0ef690f44bf2 | -14.03422 | -52.08073 | 2026-09-21 05:08:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f441e3d-ecb6-3baf-a765-a70d96d3faf1 | -26.75165 | -49.599 | 2026-09-21 05:10:00 | NOAA-21 | DOUTOR PEDRINHO | SANTA CATARINA | Brasil | 4205159 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 78a41541-a370-3d71-a35b-869511ce803c | -21.28405 | -56.13805 | 2026-09-21 05:10:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bda00aca-b314-31c4-a40d-2e92633fa3e6 | -25.02495 | -52.99732 | 2026-09-21 05:10:00 | NOAA-21 | CAMPO BONITO | PARANÁ | Brasil | 4104055 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 02100965-f306-3d42-8efa-4aba1e8c9641 | -22.03658 | -56.05422 | 2026-09-21 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31e7fe92-42c4-3e07-8d60-446186b45cae | -21.28295 | -56.13575 | 2026-09-21 05:10:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65c0fbe5-37ff-3aa2-840c-6477744a26cc | -26.35938 | -51.68429 | 2026-09-21 05:10:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 03e204df-2432-3052-9052-08db66aeac4c | 4.3596 | -60.99761 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce1ac1a5-abea-3e7c-8f8b-6923db037c1e | 3.67903 | -61.8683 | 2026-09-21 05:38:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1fa16c-753f-30c6-9f90-b1a2a49812ce | 2.65354 | -50.86063 | 2026-09-21 05:38:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a97beb9-c16e-3438-ab89-8be89cf16e9a | 2.12255 | -50.68367 | 2026-09-21 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0206212b-574b-30d3-b2a2-6baf6b86a349 | 4.07755 | -61.40366 | 2026-09-21 05:38:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d66813f-ef45-3444-b569-e31613c277c8 | 4.12684 | -61.29547 | 2026-09-21 05:38:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1c8be97-a292-3485-9aa1-8bef5c7f7fa3 | 4.53459 | -60.86349 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e927b103-668e-3e8e-bf1e-ace25d6e7c33 | 4.70273 | -60.89223 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34b71731-a7f9-302c-b571-e58d2d01096e | 4.12741 | -61.2991 | 2026-09-21 05:38:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 463ee955-5874-329b-9ebc-5674dd8c832d | 4.32532 | -60.69057 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0affec8-a8d0-3a8e-98d2-78a1ba18b5fb | 4.70437 | -60.9027 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a20c3269-8809-3763-92b2-d45363001c3e | 2.65411 | -50.86405 | 2026-09-21 05:38:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| badbe519-335b-3d72-9a91-38135c179570 | 4.08095 | -61.40311 | 2026-09-21 05:38:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5657eebf-e356-3a90-b101-5d4fe1d02ab7 | 2.12275 | -50.68417 | 2026-09-21 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26a15b5f-e759-3fcc-b4ce-bd57896b16bc | 4.65265 | -60.94706 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5157960a-8abc-3802-8e56-0f674be796d2 | 4.52615 | -60.86199 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15eabc82-5ff6-3302-9ac0-5e117d2975ef | 2.12215 | -50.68061 | 2026-09-21 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb223732-94d8-35a1-896c-57ed80e85bc9 | 4.5307 | -60.86077 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80f6d613-c7d5-3b53-b415-1939e4f9a965 | 4.35568 | -60.99458 | 2026-09-21 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 931285ca-ee38-3779-92ec-c0337d065a05 | -3.22801 | -60.81066 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0200437e-21ed-347b-85dc-ad701dc5542c | -3.3697 | -61.34737 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c523d0f-25aa-31f6-9542-5c1e9d09cebd | -2.901 | -59.22536 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| da13eb52-621c-3207-a60a-2def1ce245bf | -4.30097 | -56.26272 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d7c57ea8-de12-36d8-99d1-b498fddceb37 | -3.49941 | -59.61671 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ef6d623-63c1-301c-91de-ebf64740ed1b | -3.82069 | -59.33089 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6bd0a35-7daf-3bdc-9b1c-0274010ce9f6 | -1.91265 | -58.26424 | 2026-09-21 05:40:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README85.md)
