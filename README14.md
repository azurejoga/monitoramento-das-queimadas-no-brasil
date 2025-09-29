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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b47d02b0-ae24-332e-a18b-ebac198db756 | -8.29777 | -45.49803 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d333fead-83c6-3a9a-9047-5bdd219f4b74 | -8.66158 | -49.4379 | 2025-09-29 03:47:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8113f483-5e79-3d27-a9aa-a15ea4bf34f8 | -11.94139 | -43.91539 | 2025-09-29 03:47:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 363f6477-9d38-3515-93fa-f674c0b2b3f8 | -6.6282 | -45.89864 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be0566f1-0df0-3062-8d33-b0a06691c0b7 | -6.49143 | -44.51468 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c968c930-ce2e-3056-8b08-a9feab27b2c0 | -16.59875 | -45.13283 | 2025-09-29 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e06e1bb0-1db1-39e5-a0aa-65aac2f716ae | -8.29346 | -45.49012 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24a32bef-ae10-3868-a65e-39f50f0c204e | -7.51331 | -44.30259 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d24df3c4-9e19-3422-9707-6113d0499503 | -11.50367 | -43.548 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c679b63d-f682-3ed2-95a9-4fcd71cfd7fe | -9.7872 | -46.93468 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5a7c4fa-1c48-3866-90df-36994a2b5f49 | -12.69852 | -46.8981 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 751a2265-eb0f-390f-ab67-838cfa30775e | -7.4983 | -44.29615 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bfa1992-5bf7-324b-a7f5-8a9951f66310 | -7.89733 | -44.58929 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d8d5fe0-d19d-379d-8eeb-81b4347124ee | -8.29464 | -45.48363 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea0516cf-adb0-3e47-bc4e-c9493167847c | -17.5019 | -43.48286 | 2025-09-29 03:47:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d750fbf-bd72-39e8-abf3-e6ce2dad2325 | -15.84972 | -48.24037 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39b7bb4e-4252-3e85-ae07-2d1eb6606e8b | -15.18905 | -48.472 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cbc3e10d-4ab1-3532-a0ef-5b0d41940d12 | -15.22014 | -50.09809 | 2025-09-29 03:47:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a369d08-ff80-3269-9bce-ba88c1d97415 | -15.27996 | -49.51295 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1460540-871b-3ad7-83f1-1881ad1c3c7a | -15.07662 | -48.33376 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bc51217-ffa8-340c-816c-362261569363 | -7.21842 | -44.77958 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9c9a9337-70e1-3e80-86c2-e3eccae77e10 | -19.00226 | -40.50167 | 2025-09-29 03:47:00 | NPP-375D | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59066c65-2825-397d-b30e-36712e7816e7 | -9.51527 | -47.6946 | 2025-09-29 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54c95f91-aa16-3572-8a7e-71d83ab53c88 | -11.94319 | -46.53625 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70155104-e7cd-3aa5-ae21-1cb13dbea342 | -11.92399 | -48.03971 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 64d7d528-c64f-3320-81f8-58bc1475a7a6 | -15.25874 | -48.77087 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d4b62b7-aa91-365d-948a-be4daeee4a4d | -6.07334 | -42.47073 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d64c209c-ac71-3aff-a1ad-30f4e5747e42 | -9.63422 | -48.12112 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66a6e468-9bfb-30e5-995f-97186b16d44b | -6.06566 | -42.48175 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 89ae367a-9513-3bf5-bb1b-cc200ea30f30 | -11.36263 | -45.06888 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c486511e-451a-3325-b42d-b1e6e49d0b50 | -12.7023 | -46.90854 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dfd15fe-b545-347d-a37f-0dd3c861ab44 | -8.15743 | -46.39978 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94e70ad2-9a40-3f5b-93d4-5d80e799318d | -7.89625 | -44.59528 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d2f6995-13df-3fdb-afdb-5619055bb658 | -11.36727 | -45.0725 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04899aa6-912e-347f-a064-dc147a39d330 | -10.82938 | -45.40609 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bee11e6-f5e5-3a5c-9e2d-41ed9b33be55 | -10.40311 | -48.16109 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64e72110-53df-3de4-b53c-e7f847748745 | -8.8638 | -46.61735 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3a67818c-850c-3faa-883d-ca34bc157afc | -12.65601 | -46.9252 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8df0305d-144d-375f-b83e-8b80b1cb1798 | -20.05026 | -41.34001 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ecc37c21-1c94-37f4-b06c-d4d0f407ab71 | -17.00299 | -43.5069 | 2025-09-29 03:47:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae4d2fca-7dcf-381e-bd15-3984aafb2a1a | -17.08274 | -48.56683 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b59ea8f-8aca-3edc-8857-566d6a088802 | -16.29066 | -45.85184 | 2025-09-29 03:47:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a11c08a-c483-374c-b8f4-ce0671738a86 | -6.14706 | -43.88187 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea4b2f72-c84a-33a2-8d2a-38b029a560d4 | -10.39918 | -48.1478 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2535813e-9e7c-3e70-a0ab-1e00f95c006b | -20.05744 | -41.34099 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| 580a35e1-ae6e-3c41-8856-f855dd812a99 | -9.08975 | -47.62774 | 2025-09-29 03:47:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25c3090d-77ce-3199-b86b-732dc36f8edb | -12.00488 | -46.62355 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9241f1c7-0f61-38fa-bda7-7874d1d8efea | -6.05527 | -42.46275 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a713e1b3-9f71-3cb7-856c-8f2b5970a0fd | -15.54693 | -47.88262 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ad9b605-31ee-3be6-b12b-f66c9ebb514e | -17.08697 | -48.58002 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f88cc03e-9987-34fe-915c-f0784904d012 | -11.44034 | -45.03335 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25152493-4ade-3f6d-b0ca-6e26198f5674 | -15.8707 | -46.22059 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41043bb9-3367-3ab3-aa58-2a087dbc9e91 | -15.07926 | -48.33717 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea856f6-4816-3ca9-95c1-4ab6ccc822ae | -9.30153 | -45.72313 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c142b091-0cd9-3942-ac80-ab54be889df0 | -11.67024 | -45.35279 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d44d1a56-9e0e-3011-b42d-299c9e4a59d8 | -11.67125 | -44.29278 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78b3ca07-4729-3438-b293-7c892841eab5 | -9.46741 | -45.5024 | 2025-09-29 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cc29e2f-9ff7-30bc-b3a7-19d32ef929fb | -11.93094 | -48.03257 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4422040e-ef80-3070-8b27-4773478be94f | -8.24777 | -45.48798 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee9c4a6d-2fd6-350a-8e23-4807e3949706 | -18.1179 | -42.19339 | 2025-09-29 03:47:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 93950a1c-1383-3c4d-bd36-f9f99bfcfb31 | -10.28269 | -45.19583 | 2025-09-29 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2383dc97-6673-37a6-8821-55581ccc8f16 | -11.71781 | -44.43309 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f5b14fa-fed9-3a83-a36d-81482e8ae66c | -12.94654 | -45.1715 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0ea7201-fdf8-3c5b-bdf2-98932f572f8c | -10.40397 | -48.14677 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27c11590-941a-3003-b967-1593c091aa0f | -7.32504 | -44.72025 | 2025-09-29 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae2edac5-a049-3f83-ada3-8553764967c3 | -12.58217 | -41.29374 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| ca4b2425-b5ca-3134-a2b9-9d4a1a274146 | -7.90147 | -44.59664 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44a021f2-9ccc-384d-8d85-692985050b1a | -6.73403 | -43.37807 | 2025-09-29 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ce653550-7b18-3912-a855-49bbf9f010ba | -6.14786 | -43.90779 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9a7b18d-19da-392f-a6a5-574bd36e539f | -8.25828 | -45.4935 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e812570e-a321-3d8c-b085-812319089467 | -6.49202 | -44.51141 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0641d555-2c6f-390c-b78b-8c720181c099 | -6.31672 | -43.44759 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4fa1dc06-6094-3b98-a077-b53bb8356497 | -7.22134 | -44.79448 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7ef88d6f-de4d-32cb-b3c1-7af8dc5766a7 | -6.06125 | -42.48415 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 53db5f39-f000-3f19-8dd2-9e980e528b2c | -10.48548 | -49.36973 | 2025-09-29 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ff10b7d-4997-37ab-815c-d6bcf56a583a | -15.78154 | -43.8596 | 2025-09-29 03:47:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6d49d226-d39c-3402-9ae7-93cc09c40f95 | -7.54862 | -46.10544 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 296b01eb-2b36-3e1a-a08f-c2ec86ffa24b | -17.72513 | -46.69114 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 105ec46d-07bc-376a-b003-4500f31c49be | -8.15464 | -46.39983 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 87cc5d9d-4126-312d-b805-ca7e6d5027e5 | -9.10143 | -45.84706 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ee77ce6-4a6e-3229-9d5a-2d0e8f875bce | -11.48131 | -43.51398 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b5d71a1-c13b-3370-97d7-4167a201a694 | -8.28152 | -45.49242 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1c6215cf-1e5e-3b39-aa83-ee5bd9ad3e83 | -7.10605 | -45.53451 | 2025-09-29 03:47:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92c02336-0665-3834-9a5c-8945dde1a0af | -10.42081 | -46.15352 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47c9b16a-a9d7-3b12-a392-673de527e0fc | -8.15387 | -46.4039 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a596d4d-6ba4-3dc2-af33-a3943e6973dd | -16.85631 | -45.80678 | 2025-09-29 03:47:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd10b6b4-de18-363b-bd15-9d24a4ad8258 | -6.8938 | -44.53178 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c3a2387-2352-3073-96df-372c05719963 | -7.89464 | -44.60423 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37ce1631-17dc-324a-a62a-50d3cefbf65c | -15.86763 | -46.20948 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30e6705f-f0d3-3925-867a-1380d427de93 | -8.29906 | -45.49092 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30059f87-00c4-36ef-8b12-e1da6503e61c | -7.86118 | -41.05979 | 2025-09-29 03:47:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc653039-b891-3133-9f28-400ed57dfd2f | -10.82716 | -47.9393 | 2025-09-29 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b373cf7-6830-3ff7-b9cd-9d27a748928c | -11.48958 | -43.21502 | 2025-09-29 03:47:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4997af0b-f831-3274-b848-f790326f6f70 | -5.82125 | -42.82278 | 2025-09-29 03:47:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8ec35b3f-23a9-381b-a6a5-c27929dab5f7 | -6.1264 | -43.48273 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd8abe87-fc40-3b9b-9fd4-b90fba5adfa0 | -15.5229 | -48.51258 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2a32e0c-4060-30ad-8334-11f3966a88c4 | -6.42558 | -43.50785 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 31adae74-14f6-34dd-8fa2-318763c17479 | -7.8074 | -46.90152 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 395e8289-be2f-3648-b50a-fc674da9c4a3 | -6.83642 | -44.08644 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f66d5ab-2e7c-3e2c-a5f6-5fd4f48e00b0 | -10.79114 | -46.6854 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README15.md)
