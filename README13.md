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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 217337ab-1eaa-3216-85d1-92815fed4cb7 | -7.60899 | -47.29229 | 2026-09-08 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71797a55-1ce8-3018-92f3-c2e115b0fe46 | -3.33423 | -44.58747 | 2026-09-08 04:44:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f28fc8cc-a27c-396f-b57a-980332c755df | -4.03854 | -50.88129 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eec4a202-0572-37c9-9553-fa5384b912f9 | -7.37535 | -47.01906 | 2026-09-08 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c41f9dda-813d-3344-844a-134c4ccddd21 | -5.79623 | -46.22397 | 2026-09-08 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2715f1db-31f6-3dc0-8fa1-de8d618c1dd5 | -1.98356 | -48.37999 | 2026-09-08 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da57ad29-8c6d-3cd1-b1ff-19dc57e37784 | -6.38412 | -43.74348 | 2026-09-08 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba7d09a3-78ae-3ef5-8f9a-51fca93b76a0 | -2.30837 | -48.57915 | 2026-09-08 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66c1ca57-9e51-3272-98cb-2477b9039b7f | -4.34658 | -55.21619 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 714d60fd-78f1-384f-a902-44ea5ba3c0b4 | -2.63715 | -46.77664 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2caf5c4b-df91-302d-8b5c-7ad6b003ecf2 | -2.96909 | -49.55802 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe370347-7e4d-3969-82b8-71d61b8adba8 | -2.87122 | -50.44748 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e02d1e52-7340-3f4d-9abf-9986df0342b5 | -5.37086 | -56.02431 | 2026-09-08 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcda187d-cbc1-3bff-ae87-dc614306ce49 | -3.70184 | -58.94584 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa0098dd-7249-3dd0-8135-68ce2ba622b2 | -6.69549 | -47.41384 | 2026-09-08 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df563628-2a9a-3219-bb21-2dcbd7df169f | -4.66898 | -55.63344 | 2026-09-08 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48afebdb-059c-3479-908e-9e2c5596609b | -4.05031 | -50.87882 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a31eb1f-3e3a-3f5e-9fe6-95df95a06e44 | -2.87622 | -50.43957 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df01dfd5-80d1-33d1-82e3-74342439ec8c | -3.7036 | -58.93591 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f65efb9c-cad9-3c93-8bb2-d716b370947f | -6.01359 | -45.81113 | 2026-09-08 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69618669-909c-349a-9e5a-f94ff9bdfb14 | -4.51883 | -46.40625 | 2026-09-08 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a62dd12-8c25-3f51-99e6-9abec118a460 | -5.52456 | -44.20574 | 2026-09-08 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64cfb63d-9e7e-3426-8de0-65cd8ea10e78 | -2.88155 | -50.44793 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b231c75c-61cf-34d5-902d-09e43ede18a2 | -3.54942 | -48.17397 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c11ae73b-6483-330a-8036-2254def576f5 | -2.87128 | -50.44191 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c767901-ebca-3d13-a592-2f17917395e9 | -3.69814 | -58.94847 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a49f4068-d911-3c00-8bf6-3da17178265b | -3.70528 | -58.94461 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf2180db-fb59-37e7-b81c-c8fdc04e8289 | -5.94464 | -51.70297 | 2026-09-08 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7faaa83-6139-3fc1-a2b0-ec149159f791 | -6.30773 | -46.0566 | 2026-09-08 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e90187c-48a0-3261-8fd1-6e1d9b13be29 | -1.20472 | -55.74686 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed9dbce6-3f76-38fe-a56b-122d9ce59f59 | -4.57255 | -47.2056 | 2026-09-08 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1ae5fad-f144-3e0c-91f9-346fa65a72db | -6.41814 | -46.19866 | 2026-09-08 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2620a301-4848-3287-a6d3-4d033fe77a44 | -3.36736 | -50.39906 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe3b1039-8b03-38ca-b7d8-48647add8c6c | -4.36685 | -47.77906 | 2026-09-08 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 17cacbbe-c991-3ee5-bb11-ad289ac1a119 | -3.24898 | -50.8239 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4748c0b3-6459-35e5-9825-90df83405c22 | -3.89009 | -55.82317 | 2026-09-08 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9368444f-b055-3251-9e4a-8c22cad14be2 | -2.30157 | -48.57807 | 2026-09-08 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa2f331c-a080-336f-8a97-b3af1a9a7330 | -7.31793 | -49.61855 | 2026-09-08 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c7442bf-900b-3369-8f2a-1959ce090c2f | -2.63051 | -46.7756 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f161201-dc6d-3e82-937c-6a35afbd0ecd | -1.19571 | -55.7351 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa99d6f7-59cf-31f3-aa18-591143157fce | -5.59403 | -45.37543 | 2026-09-08 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c27af9f5-449d-35d0-8662-715baa0b67ab | -3.5548 | -54.69513 | 2026-09-08 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 329dd8df-550c-35ee-9f29-8804c156093d | -1.19317 | -55.71726 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ddbf30ba-7a02-3f45-9425-111028167db9 | -4.8194 | -42.92065 | 2026-09-08 04:44:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19c2bc64-9110-37ca-9976-b4144cb861f0 | -3.81184 | -47.47837 | 2026-09-08 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d754d57-1c2e-3bc3-9717-4ca607010066 | -4.34733 | -55.22593 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dce3925e-1a46-39b6-b8a6-37de33376323 | -2.75813 | -49.47868 | 2026-09-08 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1a11070-047f-3760-bb03-44dc331b0515 | -3.38766 | -50.45818 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6605b27-d8f8-3d1e-a3a1-2d1ce355606b | -4.04364 | -50.87323 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0004ebec-0c09-32ec-af53-bbfc14498df9 | -4.11034 | -49.06163 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 545961c3-0ebc-3c28-b479-ffa0fae72802 | -7.61009 | -47.28522 | 2026-09-08 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 922948c3-a1b8-30b9-8a87-fcb9127f0cfc | -1.19625 | -55.7318 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1816159-774a-37ad-8728-92e40c8b654f | -3.323 | -44.58978 | 2026-09-08 04:44:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc25da11-5fda-32ae-ba92-1da3ee113229 | -4.78312 | -44.40067 | 2026-09-08 04:44:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da265d3d-4eaf-37f1-ad41-d8ebcf95bfd3 | -5.65141 | -44.3028 | 2026-09-08 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b580903-b28a-3acc-b868-8646df4d41bb | -3.14943 | -60.66003 | 2026-09-08 04:44:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c66cdf64-fd11-3105-9ca6-236648219ca8 | -2.9804 | -49.26597 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 006969e7-fc79-3429-a4f5-1195265d95b7 | -1.1904 | -55.73423 | 2026-09-08 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e8d7f60-bd34-3565-9ace-67a2b0edd409 | -6.38341 | -43.7482 | 2026-09-08 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23a95c35-f2c1-39fc-b476-3cc928b96408 | -3.44541 | -47.27187 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62908003-cc74-36cc-9b4b-ab4d34ee9405 | -3.54831 | -48.18099 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| e7df29d1-e016-3dd5-9191-0960be5eb74e | -1.11829 | -47.73803 | 2026-09-08 04:44:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83bd3c35-a496-3e59-9ae6-211bc2d52d2a | -7.72517 | -44.30293 | 2026-09-08 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ead75d4f-58f4-3d2b-a9e1-d4cc062ea833 | -3.26882 | -50.02281 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a52770a2-31be-3271-a30e-b6d86ba40bce | -2.87423 | -50.44675 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b85254d4-3ad2-3d76-ac2c-24e8c6ef12f6 | -6.75907 | -45.48526 | 2026-09-08 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 171398cf-db3a-35ab-8d72-6cd23355cd25 | -2.63383 | -46.77612 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e891e01b-5e94-3393-8a69-f4f3da9e0816 | -2.63825 | -46.76973 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f039e40e-bb1c-32c4-916c-31e7d7b2392f | -3.06572 | -49.51759 | 2026-09-08 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e829b4c-648d-3992-9f0c-3e44b6949653 | -3.26635 | -50.02356 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b6d8090-fb4f-30aa-87f6-72bed6fa6b92 | -3.33069 | -44.58693 | 2026-09-08 04:44:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ad837823-07eb-3f39-afa0-12a819a6fb26 | -2.87988 | -50.44017 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15ab13e7-1ef0-36f3-a014-2c9eaa5f0fa8 | -5.30934 | -56.10796 | 2026-09-08 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1fffca9-7765-31ef-b4ca-2b43c691ea29 | -4.81681 | -42.91846 | 2026-09-08 04:44:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfad4e38-fec5-39c5-ac9a-fae5defef2a1 | -4.9843 | -50.64484 | 2026-09-08 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cbde454-df01-3715-af32-e21b6de46130 | -4.33982 | -55.22619 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6dcb9f9-1a12-3afe-b572-11f9f183ce0b | -5.84577 | -45.1687 | 2026-09-08 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dba4e931-cd4a-3091-b795-fe54aa2d206b | -3.86587 | -48.97434 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eedfe9d-ea8d-3835-a2c9-c01f1b9acd37 | -6.33525 | -43.35576 | 2026-09-08 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2c6b6b09-2326-387d-a22a-fca65697a4f4 | -7.38287 | -49.60609 | 2026-09-08 04:44:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| faad2bec-e82d-3f18-a0d7-3f2c75d1b97f | -2.84236 | -53.98895 | 2026-09-08 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ab18a97-9b4c-3ded-8728-b6ae97a55972 | -7.37199 | -47.01853 | 2026-09-08 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78436d81-3af9-3175-a798-2c0fcab9cd71 | -7.93153 | -49.73839 | 2026-09-08 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d7d83f4-7a1b-37ad-9f42-abf3d4a35cbd | -2.73136 | -51.38474 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21a5822b-cc2f-30ae-9212-ee08feab4a2f | -3.33976 | -53.40671 | 2026-09-08 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 441ebbbb-8dd2-355e-98ac-045544dc4e38 | -3.46277 | -59.50941 | 2026-09-08 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3813e8db-7763-35b4-9e2e-26e248ced191 | -2.83409 | -48.65348 | 2026-09-08 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 770a3e3f-8116-37ca-8ae8-77afb73a2bf9 | -4.98069 | -50.64426 | 2026-09-08 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87b9fd1f-175f-3331-9b07-a05dd4f7ee41 | -5.70454 | -52.29997 | 2026-09-08 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2137adf5-6951-3633-919e-27bb6cb786a0 | -7.75901 | -49.98164 | 2026-09-08 04:44:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f399a77-3824-391c-b70b-0a8cb563bae7 | -4.04662 | -50.87818 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8308c61f-bb14-3e4d-8e16-5fe576e0e481 | -2.88085 | -50.45217 | 2026-09-08 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad62e9a4-61ad-3097-a9ce-2efe4d7aae5e | -3.83447 | -40.10935 | 2026-09-08 04:44:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d726cb10-6e2c-3d71-a2fa-ce331fc81d07 | -2.64048 | -46.77716 | 2026-09-08 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f13c118-ada5-3f5f-b235-76816bc1787d | -4.34643 | -55.23139 | 2026-09-08 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39c832cc-158c-345a-b514-927b069ce9e8 | -4.08158 | -48.95655 | 2026-09-08 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ce3277-6935-3dc6-83c6-3b570e208b24 | -4.05101 | -50.87448 | 2026-09-08 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4bfebf4-b5c3-35a3-bd62-e776f16bd451 | -5.49553 | -48.17125 | 2026-09-08 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8aff9f0-bdfc-3a10-822e-1ce9ad413462 | -3.70272 | -58.94088 | 2026-09-08 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ef97094-d7b5-3ce9-a552-e3e02c44fbab | -2.8378 | -53.99086 | 2026-09-08 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README14.md)
