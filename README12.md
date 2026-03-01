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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00981ce9-6aa5-3ef1-8b0d-4a2f72d44eb2 | 4.4385 | -60.73681 | 2026-03-01 06:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b43cd53-5ff3-30dc-8caf-175779f4a1be | 4.09641 | -59.8923 | 2026-03-01 06:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b006df8e-da4a-3802-af69-b7a7cfa09697 | 4.09547 | -59.887 | 2026-03-01 06:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 695993d6-b9a1-37a1-a0f1-4c316d7e5a86 | 4.09461 | -59.88206 | 2026-03-01 06:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59f3b9c0-b4a2-3c55-a1bf-b29e3404de38 | 4.41994 | -60.74199 | 2026-03-01 06:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad25e737-3018-3e5a-bc2a-57c1854873d0 | 4.09888 | -59.884 | 2026-03-01 06:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ae28cc5-1d36-3ebb-82fa-c3f7480f27d8 | 4.09982 | -59.88922 | 2026-03-01 06:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dcdea69-e751-3264-9406-56caef781a73 | 4.4394 | -60.74191 | 2026-03-01 06:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d802494-9626-30fa-bd7e-6f642d4415c8 | 1.4864 | -59.9117 | 2026-03-01 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 132.8 |
| d2fb9c3c-7f6c-3aad-88d1-f00e139efc2d | 1.5047 | -59.9116 | 2026-03-01 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.8 |
| e5896dab-5fbc-36de-9e90-76eed444cb67 | 1.4864 | -59.9308 | 2026-03-01 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.7 |
| d0b85983-bbcc-3298-9f3e-39d31e2a180d | 1.5046 | -59.9306 | 2026-03-01 06:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 45f9d37c-aa00-340d-b1c1-881ed5080e7a | 3.45307 | -60.7945 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4047b2f-42be-3ed6-8b79-a3e713c24a47 | 3.45034 | -60.81632 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20437e9f-7b3f-34f7-a68a-95fb6530f127 | 1.49224 | -59.93525 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c50684b-8ff5-3adf-a2b6-6d145e275d82 | 2.90881 | -60.42746 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feabb494-12a8-3943-a3a7-772de42cc403 | 3.44605 | -60.80415 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e09819a8-adbb-3b21-9db7-26c549d1fe75 | 2.82281 | -60.7824 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0706caf1-da0a-311c-85ad-7b135bec1e2b | 3.05268 | -60.68377 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7759086-4ed0-39d7-835e-fec4bf514ea5 | 1.49582 | -59.91438 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 76171209-1857-3424-934a-cb73480989cf | 3.45152 | -60.79771 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05c8804c-5bd9-360b-9171-acbfbb021ec1 | 3.44309 | -60.81239 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b2b16c1-818f-398d-bf10-e188eaf473c2 | 0.47043 | -60.39695 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c886dfe-6800-340e-bd00-231258d3a080 | 0.8886 | -59.79107 | 2026-03-01 06:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10104818-36f3-314c-b42b-3bac6647ccfb | 1.51184 | -59.92519 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8d21c0e0-ce2d-3630-ad15-2a949b49bffa | 1.46919 | -59.92492 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 673108b1-f0f0-3ec1-b326-3b0a77b96b96 | 0.44896 | -60.39404 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1c5092c-f35a-3f4f-918e-f5fd5bcaaa6f | 1.49328 | -59.94143 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd81cd3f-0cb1-3367-a6b6-579f9d4fbc45 | 3.4524 | -60.80292 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 175f842f-0237-393a-bd0c-8a8509f00830 | 1.49642 | -59.91466 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2a6a077e-bf8c-317c-a429-3cd2f2db2828 | 1.48998 | -59.9219 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6b49823f-8011-356a-8c06-518d5a1612b1 | 0.47724 | -60.39576 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c802304a-dd76-383c-9030-da2d7f293f7a | 1.8665 | -60.40168 | 2026-03-01 06:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a0e4bc0-9b91-3108-85a7-864b8c0dd623 | 3.15877 | -59.92374 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a107cd7-e8af-376c-a080-a1f8a37c699b | 3.45326 | -60.80807 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78ce6912-8219-3846-96ab-b60177bc0994 | 1.48948 | -59.91563 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 11476a16-6aac-3570-af3d-df45f835298c | 3.16865 | -59.91323 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d9eaed2-4a6d-35ca-a539-f8c9fc70c292 | 3.45064 | -60.79242 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb9b1069-858c-3db1-b698-5e35666c20a3 | 1.49271 | -59.93554 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f76f3e69-5fe4-30e0-8a84-efb4375f3f64 | 1.50603 | -59.93287 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fecf179-d06c-349c-b8a7-d614d54db96a | 3.44944 | -60.81124 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1c09b06-863f-3a3f-8882-bb700d0099c8 | 3.16444 | -59.91651 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92e360fb-a9d3-3034-895d-af54eb7c7708 | 1.49745 | -59.921 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 72585f52-77eb-31ca-82c9-d089935b8522 | 1.51286 | -59.93128 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c50abe46-7796-330b-b015-b0a3d2ea9bfc | 1.49165 | -59.929 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 07649fb0-81b6-3b01-9221-0d7114bf151b | 0.19661 | -60.45007 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf57686c-168f-31d1-954b-68ef3706dab5 | 1.47732 | -59.93097 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4cbe451-3e40-340c-bc79-4d8fc1807e65 | 3.15724 | -59.92776 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcd362ad-2712-3e17-8db8-dbb5532f6a77 | 2.82833 | -60.77596 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6991c981-5631-3f80-8ef9-9a36105f680b | 1.48425 | -59.92999 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fad4b838-1452-3d1b-ba09-cb0fe8133631 | 0.4636 | -60.39798 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c119390b-cc94-32b3-855b-fc496185d9a8 | 1.46976 | -59.92536 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b6d482a-e7fb-395a-ba65-524e667a208f | 0.1956 | -60.44384 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 234946ae-9d9c-3539-8bad-504957bde979 | 1.49913 | -59.934 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0110168e-c2c6-30fe-abad-d88ddd3f92bc | 0.89564 | -59.78999 | 2026-03-01 06:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5780e841-9c7c-3773-9c42-7d054f388306 | 1.49054 | -59.92221 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1379fefb-3537-3a51-bd48-a0759d763a8c | 3.44854 | -60.8061 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abf5ff24-663a-312e-91c0-30b511dd0d15 | 1.48535 | -59.93643 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0a9ac2e-f007-3198-b9ae-da3f895b07c3 | 0.18877 | -60.44498 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 738b73fe-298f-3d7f-a870-77e9c7081b81 | 3.31594 | -59.89413 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8fc2f10-da68-332d-8426-590f3645080b | 3.16191 | -59.91442 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e22ada83-4a72-33e2-bf6a-ff174e249232 | 3.45123 | -60.82143 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09e6e24a-bdac-3cef-b94c-381dea783218 | 3.16294 | -59.9205 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 08801b7a-0bca-3c79-b729-d87f855fd4e8 | 1.49803 | -59.92752 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36f1f3bd-3a40-3710-851c-e3a468c425fc | 0.89461 | -59.79501 | 2026-03-01 06:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ed20a35-f83f-3cad-a963-bdb9723f92e9 | 3.48946 | -60.77725 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84afb377-242b-3170-8556-478abf3369ca | 1.49113 | -59.9287 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09636227-d74e-379f-b3d7-41998e27efb6 | 3.45413 | -60.81321 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e84f2a7-1f2c-3313-8036-f7183a79d0f1 | 3.31699 | -59.90018 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70a91c79-cace-3706-97e6-7b1705df8672 | 1.49855 | -59.92785 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d068858b-fcc8-3f51-b6fc-d6d0fb8c9ddd | 3.45579 | -60.81002 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e3b521e8-cdf3-3784-81ba-91540b65d666 | 0.85535 | -60.40849 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e8cf75c-7731-3c17-8823-332c17e5d87a | 1.48887 | -59.91531 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ad57f640-4453-3c29-9c0d-6a6d9aee95a9 | 1.4762 | -59.92437 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e25d03e6-0d56-3fcf-ad41-7de95ecbab3a | 1.50704 | -59.93888 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a384e1b-0b65-39c6-85c6-dab061b0c217 | 3.1562 | -59.92169 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f64ae61-be95-37a0-95e9-f86689c3516b | 1.86747 | -60.40755 | 2026-03-01 06:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b49d05d5-99bc-3a04-979b-657a88ce32a9 | 1.47085 | -59.93199 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a0a310a-f08e-3efc-bb7a-22b94a903070 | 2.82189 | -60.77705 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9bd3b83c-91c9-3452-ab5c-5674285e9b1a | 2.90977 | -60.43306 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 367b29a7-954f-3200-bf47-997d073f3977 | 3.45669 | -60.81516 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd75f21f-63ba-3c29-8ce5-fa09d30485ad | 1.47677 | -59.92479 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a41a2b1e-d803-3b28-8622-46a84b086261 | 1.50498 | -59.92659 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f682ba86-222a-331c-a320-c6fc4c46e441 | 1.47887 | -59.93767 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a974fbb-eb4b-3966-9e80-701752bf2810 | 1.49688 | -59.9207 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b51a9353-dd95-33c5-a507-db4200328e90 | 3.05914 | -60.68267 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3802b6e0-c5a9-3b6c-86ca-a8477ea9c27c | 3.44692 | -60.80932 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb99d5b7-edd4-3657-a84f-c7673e80910d | 3.32268 | -59.89297 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c93bebf-1329-38ff-8a7a-47ee520684fd | 3.15985 | -59.9298 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5ecd128-18bb-39fb-8e3f-af1ddbefe93e | 0.46451 | -60.39721 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 501d5a49-0828-35d0-95ea-daa23b9799e8 | 3.07561 | -60.01619 | 2026-03-01 06:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a36757bf-2a11-303e-b327-32b204ed6ac2 | 1.47784 | -59.93137 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fec78251-2802-3881-8268-0ebebe18634d | 0.89351 | -59.78848 | 2026-03-01 06:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4145ecf-2b48-34f2-a88d-0cd5567bf4f5 | 3.45499 | -60.81836 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aebcbe65-db5c-3f27-83a2-86622e5f727e | 1.50278 | -59.91354 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| acd774ec-985c-3362-be0b-410c6a894f71 | 0.19515 | -60.44918 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1efb9cbc-b8a1-3ffa-a924-598024c2ca9f | 3.45399 | -60.79972 | 2026-03-01 06:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b843befc-5d59-3b32-adde-09d9dfd48436 | 1.49541 | -59.90841 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| cbfde08a-ec08-3b36-817f-fc0de9b8b47b | 0.85434 | -60.40235 | 2026-03-01 06:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 671e5a55-edcd-3ed1-9c93-7350831906b3 | 1.51391 | -59.93752 | 2026-03-01 06:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README13.md)
