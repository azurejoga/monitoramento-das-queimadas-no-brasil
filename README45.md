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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1f5b682-cfec-3e0a-9476-97bf309fac53 | -3.91061 | -48.3341 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44cbd914-8183-380c-a6c2-e9bf792a7b82 | -3.91004 | -48.33784 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5ee53299-9e90-3c9c-87ba-e3d099a2b9a4 | -3.90793 | -47.95585 | 2024-10-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef9642e5-395f-39e2-a9d5-f3c76d2dd09d | -3.90594 | -48.3372 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b62bfe6-10fd-3703-816d-edca17169e54 | -3.90298 | -48.32904 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c11cbd3-b5d7-36b5-8f27-9562dd753bec | -3.90241 | -48.3328 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73f97e05-b64e-30d7-a887-b8e34e8402b1 | -3.89888 | -48.32844 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5f65653-afc3-3fd3-9c41-d1ec79781bf7 | -3.89831 | -48.33218 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a50bebf-edfc-3829-80bd-9f4d2948a84d | -3.87243 | -49.08177 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f1a87d8-0131-31fa-8891-9d3b0132ffd3 | -3.83929 | -48.88004 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d37f0e28-cc59-3efd-8694-70eaee6d515c | -3.83864 | -48.96265 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 222378cc-e4e5-386f-b8aa-ab1cc1bc0ead | -3.83851 | -48.88511 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a7b3798c-321b-3eb2-b683-a96c53182757 | -3.83785 | -48.96774 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45d0cf94-61fc-3fa5-bc08-f46edd1bf273 | -3.83781 | -48.96455 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 78c647cc-df96-3e2c-913e-4e224d426db1 | -3.83532 | -48.87949 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ed2b8ee-4962-3086-b099-4126299cf7d2 | -3.83471 | -48.96205 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0bb95ef-6e7a-36b0-91a1-c6e46a415f8b | -3.83454 | -48.88456 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bdb6cb27-0453-3b7e-bf1f-17b82ef98f76 | -3.83392 | -48.96712 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ad73a84-0c82-3b83-be9e-dfe2c8776b03 | -3.83388 | -48.96394 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05e19559-03a8-31e1-8b4c-d36224533656 | -3.83377 | -48.88961 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 266c53a6-d5f3-3122-bbed-e7b2bcbf4e40 | -3.83313 | -48.96901 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9aaed559-b495-300e-bd19-c2c2fa0a2197 | -3.83137 | -48.87891 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7cf07ff2-5e5b-3f85-bb41-4547677eb0d4 | -3.83077 | -48.96145 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0dd2149e-3b2b-375c-be2d-f1f5230cfbc3 | -3.83058 | -48.88401 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c18b5208-1598-3c81-8fe1-603abb5d8336 | -3.82999 | -48.9665 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c3f0679-4810-3897-ae73-f1e60a95557e | -3.82981 | -48.88906 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2317197f-cf32-3fdb-a1fd-a5b6b9a0d3de | -3.82026 | -48.87211 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88d721a3-11b4-3077-8e14-2c0a7e61c6cc | -3.8163 | -48.87152 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 688cacbf-e755-35fe-ab2b-aff217c3519e | -3.81553 | -48.87659 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0cc98e73-0111-3fff-9dfa-72e3b04cd6ea | -3.81235 | -48.87093 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6d1bf6c1-1e3a-383a-ae36-0dffb0a4f9b8 | -3.81158 | -48.87599 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0a704525-c3b1-3215-ba07-e08e07eccd07 | -3.80577 | -47.80258 | 2024-10-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c268ef6b-0480-399d-88a1-dff9e1974c5a | -3.80526 | -47.80155 | 2024-10-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a79c3a32-f007-3590-8049-364b085ba07e | -3.77227 | -47.73698 | 2024-10-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd7c2231-cb65-37c9-be02-4d59e979c81e | -3.76032 | -48.89423 | 2024-10-20 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24692094-90dd-3d0b-ae41-e00f919062d4 | -5.33617 | -48.3505 | 2024-10-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6e097b5-511c-3b69-97d1-0f5c77e13840 | -5.33862 | -48.35507 | 2024-10-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97fa47c0-02bf-3306-b61b-9d424262df71 | -5.33501 | -48.35068 | 2024-10-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48e6e093-bff3-31d0-bfa3-883ec37390fd | -2.86257 | -49.36283 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eda77be-3654-331b-94d0-69b8a103f1c8 | -2.83605 | -49.13586 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e2e446f-1fdc-3f9d-927f-462596f7ed88 | -2.78685 | -49.30119 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 761d4d09-9e6f-3268-9d1c-7a73dbf31555 | -2.78613 | -49.30582 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 27f85954-5d56-37b9-b08a-c571a2fa16f8 | -2.78541 | -49.31044 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| dd5784bf-cbaa-37af-b6e2-945a70a05662 | -2.78305 | -49.30061 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a53de61a-c45c-3225-80d4-9fffbbea3f33 | -2.78233 | -49.30525 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4a74b67c-887e-38ab-8068-dd1bb78c6951 | -2.78161 | -49.30987 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d1896804-d141-334a-84ba-9ee42ab61d51 | -2.77854 | -49.30466 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c5eb5d78-523a-3461-845f-8b8ba710d4ef | -2.77782 | -49.3093 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b16bf8c-a368-3c04-8769-c5c2bb4edfe0 | -2.77474 | -49.30408 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 564c7978-59cd-35fa-a20f-ce8f6302df51 | -2.76901 | -49.41616 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1db4f43c-98d2-3345-8d51-fb85e2aacdeb | -2.76594 | -49.41104 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 67f0fe19-7a44-3bd2-8b47-442eb4ece87d | -2.76549 | -49.36396 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57f16f5d-571a-3e3b-b616-c10f83dfe7a7 | -2.76524 | -49.41558 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 274da377-4f39-3175-8bc1-5a5051eeb2f8 | -2.76171 | -49.36338 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 627e4d8f-a46f-3bf3-995b-8fb8da5494aa | -2.71534 | -49.51477 | 2024-10-20 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 37b763bc-be14-3134-aef9-e97045194652 | -2.71228 | -49.50969 | 2024-10-20 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eff692f-dada-31c4-8f3c-01d5cb6e5043 | -2.68394 | -49.31627 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fe5b440-7f2b-37ee-8b14-a5a5487f82ee | -2.66212 | -49.40678 | 2024-10-20 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b5593c-98bb-38c2-a9e5-05a1c7ab322a | -2.66032 | -49.14065 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 6a10f7dd-c81f-364d-9805-2d386141bbed | -2.63993 | -49.09401 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50238490-7ed8-31b9-84e2-7905fa5ff9eb | -2.6371 | -49.09657 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 17da92a3-28b6-30e1-a557-fd5a683a11dd | -2.63609 | -49.09343 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a3770d9-a591-3c1a-99c1-2a96b26428b1 | -2.63438 | -49.07863 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15c3f5d9-e7c3-3271-bce3-43f5d5eda112 | -2.62812 | -49.06794 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cb80530-5df6-31fb-a21a-d0c669394a0d | -2.62741 | -49.07271 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b21b6169-477a-3440-9342-7b3e5ff7e168 | -2.62545 | -49.07059 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7c6a5fe-c1ac-3a47-9a47-959efd6d038b | -2.56989 | -48.94442 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9714282c-cb8b-363e-8c66-c25731418c56 | -2.56676 | -48.93897 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d0972f6-18a4-39a8-a203-151cd62b42ca | -2.55814 | -49.17622 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b97ceb43-d8ce-3aa1-9820-263a6ec36d39 | -2.55432 | -49.17565 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0506aacb-6bd3-336b-a99f-eedd4a3b9394 | -2.49417 | -49.29003 | 2024-10-20 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd32e66a-519f-3416-a52e-5290e6002de2 | -2.49401 | -49.29232 | 2024-10-20 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e874be8-b750-39fe-8f2a-4d9c0ea026df | -2.47738 | -49.0991 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bcc64945-4868-344e-96ab-0b95a1fb5615 | -2.47664 | -49.10384 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c17e4f9b-242e-3cc8-b85f-d5e83fd6c6c0 | -2.47355 | -49.09852 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c0c7eef5-69e3-3484-b612-d5144394a716 | -2.47282 | -49.10326 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 163c149f-b86d-3a1c-ba09-caa003df25f1 | -2.46787 | -49.05891 | 2024-10-20 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91d8e3d5-0a82-3099-b77d-29cec6f6cbd8 | -2.24653 | -49.5201 | 2024-10-20 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14643d41-b203-3a1c-a3f9-1581a568c74d | -2.24462 | -49.52179 | 2024-10-20 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0db3ff9d-d1a6-3458-93f7-09c36982a413 | -3.27152 | -50.22931 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85cf864e-6ad0-32fa-85ea-35716d81d42f | -3.25425 | -50.12318 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dd17e44-bb8b-378f-80ca-53204041f0d5 | -3.2536 | -50.12742 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a53ace-da12-327a-9931-21488228f789 | -3.22153 | -50.36255 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d714d26c-de73-363a-ab7a-b8622adf70db | -3.21856 | -50.35788 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0ab48af-0b50-393c-89d9-e3e961f205b3 | -3.21793 | -50.36199 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf3723a-a486-3be2-bad4-12fc33dc5eba | -3.15838 | -50.3795 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fd9e0ed-01cc-3f96-9d64-1fc7a504f648 | -3.15478 | -50.37897 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc1ad577-953d-31da-b4ad-817fd1ae6935 | -3.11907 | -50.1776 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 044036a2-32ca-37d0-80b3-36a2810811af | -3.11806 | -50.17859 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4d07c6c-d94c-39f2-a503-542da1cace2e | -3.11544 | -50.17703 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c4b648-dc8d-35ea-a29d-8fc0a6331db8 | -3.07007 | -50.36697 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fbbebd3-1f0a-31e4-bb3a-8fa3c122c008 | -3.06712 | -50.3623 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8570f0b5-6e1a-31b9-8542-700d4243f8aa | -2.84453 | -49.6291 | 2024-10-20 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05fe03c0-7119-35bf-90c7-0600081624cd | -2.8042 | -49.61842 | 2024-10-20 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f180084-b412-3435-99f2-d196fed2dfaa | -2.80352 | -49.62286 | 2024-10-20 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18a99721-e46c-3ccb-b2fc-15bbefbff14d | -2.62839 | -49.98468 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6773d585-4f68-3316-94e0-e39cc9a4760c | -2.62539 | -49.97988 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4db767f6-64b6-3da8-a55a-a366888f00e5 | -2.59582 | -50.02732 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60fbf59c-f23d-3464-b177-2d9e13e77063 | -2.59515 | -50.02872 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95013473-4c16-330a-8d29-11e3acefd720 | -2.53191 | -50.10076 | 2024-10-20 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
