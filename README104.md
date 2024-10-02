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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7d33688-c299-3ea0-9c06-576774a5fa3d | -16.84942 | -55.90435 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5846250e-176c-3629-a5a4-a22111740e9f | -16.84875 | -55.90835 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 60df73af-c8a6-3660-9cdc-1eb8aa938084 | -16.84583 | -55.88311 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2f55d4b7-6ca7-37af-8bc0-4932ee73043d | -16.84393 | -55.91573 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 58982539-289f-3c7b-be0a-fe37b0a01e3a | -16.84314 | -55.8991 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d22a268a-e094-3206-be9b-a6b3fea76e2d | -16.84236 | -55.88249 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4a21f681-7186-310c-9e3f-042cd53ff51d | -16.8409 | -55.8699 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5a90a409-7d31-3286-b82e-88cc4e894787 | -16.84046 | -55.9151 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 09ce41f1-b700-3a2c-acda-819f5bf3b259 | -16.83967 | -55.89847 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 69f78ace-696d-3f90-8696-8f714cea75b7 | -16.83956 | -55.87787 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cbe7e0aa-a26c-386e-bffb-d19fbd7959db | -16.83889 | -55.88186 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4b4029a5-0397-329a-9131-6fb6d22f0264 | -16.83766 | -55.91047 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 82de455d-1890-3555-9aa0-345ab928d699 | -16.83553 | -55.90183 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3e5d1384-3678-37ba-8556-91d0e23d705c | -16.83475 | -55.88522 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dfe1ea33-b214-3244-8262-df2e7ac3fc47 | -16.83418 | -55.90983 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 40b7eb50-1c01-37b5-907f-541175b5d50c | -16.83396 | -55.86864 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f9a689a3-1dfa-352f-981e-3178ebde5349 | -16.83061 | -55.88858 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 557a1fa9-83bf-3839-8e0e-ed66aabbe7c8 | -16.83004 | -55.91319 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a66325dd-08b9-3159-b54e-51a1c08d7b1a | -16.82869 | -55.9212 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 73765732-60d8-3b5f-b5d9-3bf0af6a76c0 | -16.82848 | -55.87997 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9e350b60-01d4-323e-bd8c-127aa932fd9e | -16.82792 | -55.90456 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 60080a10-15fe-30eb-9207-a4a33574cb1e | -16.82753 | -55.97062 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| bfbf8e74-2a18-3003-ac0a-2192f2b888b4 | -16.82405 | -55.96999 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a53c3e42-048a-32ad-bfe4-1e2c963ed57e | -16.82376 | -55.90793 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| df17191a-f99b-3d77-bbcc-72d460638705 | -16.82367 | -55.88732 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5b502a03-4b1d-3f3a-8c33-5b6861103d86 | -16.82241 | -55.91594 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 7df4c2a1-f6a8-3901-a357-1677a28af42d | -16.82232 | -55.8953 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 48ec308a-26aa-38af-b7a2-7336aa84f6fc | -16.82057 | -55.96936 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1507be15-06a0-36e3-a021-acc8a5deb9d7 | -16.81942 | -55.87011 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8bfb61ac-a6da-367b-b8ad-f61d523e47c9 | -16.81894 | -55.91532 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 37ccee53-f0ff-37f3-b549-90fb53049460 | -16.81826 | -55.91932 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 649a0416-2dc7-3c35-9498-047fcf40f80e | -16.81808 | -55.87807 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a9c28023-111e-36d8-8491-6bd994dbfc8a | -16.8174 | -55.88206 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0cc134b8-f425-331c-8abf-08feb2233b81 | -16.81605 | -55.89006 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e1939ab1-e17e-3460-94f1-8662fa1ad7e3 | -16.81595 | -55.86948 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5f88ec55-545d-3a21-a779-85beeb577f46 | -16.81537 | -55.89405 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e96240c0-71bd-3e0b-a940-1fefdb49339d | -16.81461 | -55.87744 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 193a3209-9f4d-304a-9143-dcfd275e259b | -16.81258 | -55.88943 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 789ffc03-f59f-3e6e-9faa-56b6473406f9 | -16.81114 | -55.87682 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e501c2d0-befe-31ed-a67e-394572bb0ba6 | -16.81046 | -55.88081 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 41451833-39ff-3b4b-81e6-f45e3f0794f0 | -16.8091 | -55.8888 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 158718d3-081e-3275-b0fe-0c1ed2754e2f | -16.8086 | -55.93407 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0314050b-71ae-3c58-8040-754f02ae125f | -16.80664 | -55.96683 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 81ba2878-8fce-3ec9-b433-52cef5de2541 | -16.80316 | -55.96619 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 52f6ea43-29cf-390f-bfdb-ce6070900dc7 | -16.80248 | -55.97022 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e853e708-560a-3146-9e6d-14e372c465e1 | -16.79817 | -55.93219 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9af3dcd8-a401-3dce-8905-f6cec144db4c | -16.77519 | -55.91978 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 30e5f2ac-b1bb-39f4-bcbb-ceaf6a55ecd9 | -16.7216 | -55.97313 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e224c548-f7a4-3808-832f-4cdc859447be | -16.71811 | -55.9725 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 468f73ab-60a9-3d42-a014-d0038ee6f050 | -16.69408 | -55.88131 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c43bf68f-44b4-318d-8ef9-f8401d165dd5 | -16.68524 | -55.93338 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| aa7e411b-d7e7-3fae-a51c-f3bc4de39e7f | -16.68107 | -55.93677 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 56a1bca6-3769-3d56-9acf-71cf7ac3cece | -16.67616 | -55.92347 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c3674178-7e30-36e7-af8d-d74dc976ab8f | -16.67547 | -55.92748 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c8fec89f-d10d-3699-9c69-eca6a7d1cc6e | -16.67479 | -55.93149 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7fea1df8-295b-317b-a889-3eda7bcc85fd | -16.66851 | -55.92623 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 89db657b-f4e2-36b1-882c-abea626a2b9c | -17.11104 | -56.22899 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c7c3c446-f9c9-35b6-8629-70eb2a80f627 | -17.10471 | -56.22363 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 63efdf2e-20ca-328b-b647-fcd353dcf49f | -17.1019 | -56.21889 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4cfaea18-1624-3bc3-9a5c-8ac8bf9873fd | -17.09912 | -56.23526 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8c29cc74-57b3-37e6-903a-738052be3bfb | -17.0977 | -56.22233 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bddedbd3-d0b0-3f1c-9c1d-f75581e21caf | -17.09068 | -56.22105 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 12d3f042-ca25-3a08-81a2-eb5e6be4b2fc | -17.08787 | -56.21631 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bdacbb8d-26a8-346b-8324-cb031bea7130 | -17.08718 | -56.22041 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f5b186a8-2c3d-3d4a-a2ee-d5d060e59e3b | -17.08648 | -56.2245 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 35a5a849-5ad7-3218-be8e-d43cc8e79c66 | -17.08506 | -56.21158 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 20b57bd9-da70-3be7-a87c-90351db3fc38 | -17.08437 | -56.21568 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d660a219-9cde-39dd-9b6a-8ed0847ed0b5 | -17.08295 | -56.20277 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 44f05e6b-1ca0-3d76-ba2c-ea6af82852a5 | -17.08155 | -56.21095 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aadb639f-f347-3e87-8df5-3b1b499379b5 | -17.07945 | -56.20213 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2e39b91b-2f47-3313-8f23-0bfe5d34a2ab | -17.07805 | -56.2103 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5159eb96-393b-36e0-bca2-eade523277d7 | -17.07524 | -56.20557 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 447a366e-156c-397b-b50a-5dc211bc3ba7 | -17.06893 | -56.2002 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 65ad8669-6496-361a-8b8a-fcdf344fb627 | -17.06543 | -56.19956 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 31ef2402-f57e-3e5a-96f4-65fcf6ec1019 | -17.01669 | -56.3348 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6fb3fcbe-e857-3962-ba3e-6404086bbb54 | -16.97635 | -56.23074 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 213db3af-286a-37d1-923f-58257b77dcf6 | -16.95106 | -56.20919 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a871f730-c5a0-371a-b04e-2c296996438e | -16.95036 | -56.21329 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 079d5dd8-c137-39d2-a7e8-64642cdd4a3b | -16.94685 | -56.21265 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ede777d4-77e1-3302-9106-730ab8a217b4 | -16.94333 | -56.21201 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6cba7323-e24e-330e-8ead-cccf94ce54ab | -16.93982 | -56.21136 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9c27499e-83ff-3e48-b5fe-87dfe9567266 | -11.61169 | -63.67158 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb02b758-1838-3e5a-9a18-a22907b96cf8 | -11.61114 | -63.95745 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67c015c1-f8f1-3ce0-9791-5522a9934fc9 | -11.5722 | -63.77073 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 53ee61e5-f744-34a1-8840-dc53d806875c | -11.57123 | -63.77565 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 314c23ab-e116-30b2-b4a5-f294c16e4594 | -11.5651 | -63.77454 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aef8a537-eb42-35a7-b75a-1e24c1dcdc34 | -11.56414 | -63.77939 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc07064f-eb40-38aa-930c-e8044fc26558 | -11.56318 | -63.78423 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5540735b-ee1e-32df-9d2c-7a099ebc0c8e | -11.56222 | -63.78905 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bc5de28-e7ee-3e56-a3a2-b1b1d92f1d86 | -11.55674 | -63.72096 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b42acae4-7d95-3899-ad50-c36db4ffded7 | -11.5561 | -63.78787 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a922e49-3037-368b-82af-95dbd2be02e9 | -11.55514 | -63.79272 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66c504e9-1c68-3811-8b6c-3f45e2daaaea | -11.55418 | -63.79754 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 267c81a7-422c-33bf-a04a-e930cea7df17 | -11.54934 | -63.7263 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6ca448f-1445-3d67-86b2-014810584f64 | -11.54746 | -63.83132 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19e6fd51-61ee-3fe5-9127-fe8539b796bd | -11.5465 | -63.83617 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a08f2229-180d-3902-958e-6c844c472bd8 | -11.54328 | -63.82032 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3df5f958-6b02-3695-ab03-9b12a2b2dfc4 | -11.54232 | -63.82515 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7767079-4a1c-3c0a-88ff-f02314592283 | -11.54136 | -63.82995 | 2024-10-02 04:49:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf968bf9-5643-39d3-a46c-d8e59d7abb53 | -11.00029 | -63.57992 | 2024-10-02 04:49:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README105.md)
