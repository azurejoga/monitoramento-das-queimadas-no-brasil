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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f656ff36-0323-3702-826f-4a2d7822430f | -2.56775 | -54.01699 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7529f3a-1083-3956-9463-d3aea44a2ed8 | -2.56665 | -54.02398 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22fac950-9ec2-3c9f-9519-07c3a9030dc1 | -2.56441 | -54.01648 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38b27960-ed0f-3d44-9efd-219da2e1dce1 | -2.56386 | -54.01997 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 009b3b33-5064-3735-846e-48708968616d | -2.56332 | -54.02346 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4941130f-3541-36e8-8f43-500c216b86d3 | -2.56217 | -54.00898 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a0251a3-fa2a-3d49-8366-008b3e543dcc | -2.56162 | -54.01247 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d372873c-2118-3847-ba11-c0f312d9d4b5 | -2.56053 | -54.01945 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ee478a4-b392-3c0c-addc-57b4f48cfe5b | -2.55883 | -54.00846 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 382a7ea8-3575-3a98-93bd-e69079949865 | -2.55828 | -54.01196 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df7d430e-ab76-3f8f-9e4d-8422ed20eedd | -2.55773 | -54.01545 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18236c3b-a117-3c61-afc4-758289152abb | -2.55719 | -54.01894 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c285160d-f53d-3798-91e8-75f8de6d6cf1 | -2.49807 | -54.13458 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30f56cc8-f50b-3dd5-a936-337ef7f275ea | -3.33958 | -54.6172 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32d9bf09-e015-31dc-9f39-a9f691699132 | -3.33626 | -54.61668 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 929f7e70-c3b9-3f6f-8128-31f2ce9987b2 | -3.33127 | -54.79987 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b9e78eeb-69c0-3a5b-aaa6-93beeebb2b54 | -3.33073 | -54.80332 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b17907f-4d96-3b5d-a232-a91839ba8db4 | -3.3033 | -54.69654 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce5a566c-990e-3be0-bb00-f6d7f6889894 | -3.29638 | -54.78383 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71c30950-b81c-31b2-9d08-889e12e3ab95 | -3.29009 | -54.71566 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95aabf49-9d0c-321f-bfaa-8ca3ed171b40 | -3.27442 | -54.14803 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db6d5fae-6558-3944-b233-192dff4cd733 | -3.27393 | -54.17299 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1231f79f-a7a1-31f4-954a-a3ecf8c36d3b | -3.27163 | -54.14401 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18872ccd-1520-3447-814b-d0d97032df7c | -3.27114 | -54.16897 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f44b4f15-8c4a-322f-93db-61291010cc44 | -3.27059 | -54.17248 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f46df49-75ca-3007-b9a9-620266b83459 | -3.26616 | -54.17897 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bc800eb-23e9-3ebe-be97-7edc031fac08 | -3.26282 | -54.17845 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3338c06-f353-3acf-a0b5-0c6aebb63506 | -3.25948 | -54.17794 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c2cf1a8-4b5b-3be4-8bdb-689eae138bac | -3.25614 | -54.17743 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24807d57-1b5e-3285-9ed3-082374a7d24b | -3.13795 | -54.28358 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73819d73-02c1-3925-91cd-b8c450781df8 | -3.1374 | -54.28706 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f741f4bd-46c1-3f15-8a2d-8356b5ca1761 | -3.1368 | -54.26913 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3101a06d-a005-3495-98ef-7c934e507970 | -3.1357 | -54.27611 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a547c659-a82f-3599-9909-a2b358b63800 | -3.13516 | -54.27959 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af67c74c-f209-3e76-beaf-9cc6dc648818 | -3.13346 | -54.26862 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99e0eab0-7f26-348d-96aa-6bc503fea23d | -3.03097 | -54.14587 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b97cba53-3382-3578-ad3f-b688810658b7 | -3.13292 | -54.27211 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 520e3b57-0bad-3fb5-89be-ac22950bcbd2 | -3.13237 | -54.27559 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b85d845b-e67e-3514-9485-e7a7a8468bd3 | -3.13068 | -54.26461 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea080129-689e-38a4-9b82-491eb1ab3f01 | -3.13013 | -54.2681 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e41beadc-01f0-33e4-822e-9374d0c17abe | -3.12958 | -54.2716 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6a13d1a-3b9d-3ef6-8519-5561ed87a9fc | -3.12904 | -54.27508 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94270eea-46f2-342b-9c40-958a3ae1248d | -3.12734 | -54.2641 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83afe372-60b3-3aeb-9cf4-8ab3df5c1739 | -3.1268 | -54.26759 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8e821a7-9e83-371a-9dfa-dee1abea0014 | -3.12625 | -54.27108 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52d7734f-eb33-3117-a78c-c8e08921144e | -3.12571 | -54.27457 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d39a0950-8110-3741-8a64-3ba525f64e80 | -3.12516 | -54.27805 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5ec8d79-15f4-38df-bb58-d4ea945bcc9d | -3.12462 | -54.28152 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9272bc35-9d41-341d-a8db-b1f595f5379c | -3.12394 | -54.24216 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd27a8fd-9632-3fb4-a84c-055f9fcd94ec | -3.12346 | -54.26708 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e8c816d-4991-3610-873a-72e19cb29683 | -3.12292 | -54.27057 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b98d9de-e3c6-33be-ba6c-38af042a9626 | -3.12237 | -54.27405 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6206d97-a2b3-34ba-b4c4-a5a48da7ba82 | -3.12183 | -54.27753 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c852d04f-1473-3a5b-ba7f-e915a6152b42 | -3.12129 | -54.28101 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99b9a17e-ba49-3aab-914f-fe8c59c66cc8 | -3.1185 | -54.27702 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0fa330d0-21ce-32cb-bee3-d1a1909dbea8 | -3.11795 | -54.28049 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1365ef4a-2cff-3021-82a4-69f8403b17f8 | -3.11673 | -54.24462 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d459bc87-550c-3884-b36f-9a8dfe4429ad | -3.11462 | -54.27998 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0060530-d632-3629-8146-35d94145c5fa | -3.11408 | -54.28345 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 809d1e19-20b1-30ab-98d6-b8bc90cb0d5e | -3.11354 | -54.28693 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 305e363f-a9e6-30d4-b47c-178fd2a46cba | -3.1134 | -54.24411 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0f0e03f-cb31-382c-b4c7-e04606a7a8de | -3.11276 | -54.16928 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 713ca42b-ac11-3124-9619-c43a1dc37fdc | -3.11129 | -54.27946 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a261e4e-a3b6-3fdf-85bf-adfea9bd0dc3 | -3.11075 | -54.28294 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ae0c29-a6d5-3fdb-9173-db0b2778e0df | -3.1102 | -54.28642 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 38be6cca-48de-3c85-a016-4dd4e5374517 | -3.10832 | -54.17574 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15543312-8aca-3e27-b361-7942cac46c53 | -3.10796 | -54.27894 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4c573c9b-853d-3d2f-8024-b3409e60dd7a | -3.10777 | -54.17923 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb704ecf-e483-3b09-9d77-e7c8794188f6 | -3.10742 | -54.28242 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bdf5d6b8-18cb-3c29-9c6c-3145dcdef2bb | -3.10687 | -54.2859 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 95b4570c-8471-3f71-822f-46d73c762f9d | -3.10571 | -54.27147 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 303a9b56-f6df-34a6-bdf0-2e84909763b3 | -3.1055 | -54.15022 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e89af4b0-7659-3589-a7b7-ac684c946c61 | -3.10517 | -54.27495 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a86aa114-dc15-3c32-a04c-0a19ca6edc12 | -3.10463 | -54.27842 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3e3dffc8-2a06-3fee-9f25-9793db499547 | -3.10408 | -54.2819 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4942fa96-0a22-3e29-afdd-0b2f4ef33bc3 | -3.1013 | -54.2779 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5d640076-1e11-3d9b-855b-32935824072d | -3.10075 | -54.28138 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6625cb09-c3a4-3c8a-a186-7293f88bb1d8 | -3.10021 | -54.28486 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4c34d397-0b7f-378c-a32b-4956846fbee9 | -3.09967 | -54.28834 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 66fb62af-f498-3675-9a76-287ef7066f76 | -3.09634 | -54.28783 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7a6decd3-8cf8-3b6a-b9eb-3296ce446d00 | -3.08946 | -54.54952 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b08685d-6914-3890-aebe-275356d501a4 | -3.0872 | -54.17963 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c6f3142-a720-3cb1-864c-9aea909d1800 | -3.08387 | -54.17911 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa552f07-8ba8-3e3d-b1c0-0b6a5501de56 | -3.07884 | -54.16758 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6a290e2-86c1-3b36-9bee-754fa329133b | -3.07829 | -54.17109 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 990c3fc1-2ab3-3f32-bdf3-96216d4ccb74 | -3.07551 | -54.16707 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57621149-1d69-3693-9bb3-1af690880e9f | -3.07496 | -54.17057 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc83727f-7a50-3336-86d0-46844cda71c4 | -3.07217 | -54.16656 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 99d8b5ed-b9eb-3aff-b17e-b4c93bdb896e | -3.07162 | -54.17005 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a8375d9a-0e28-36ad-94fd-97bdaf4cbb32 | -3.03485 | -54.14291 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 899d7ff9-8c08-3420-b973-34367b214fc8 | -2.88588 | -54.89968 | 2024-10-29 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b76d540-4324-3f93-8022-f5c135ba994f | -2.77995 | -54.73503 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be287cae-23fc-3bbb-a3ea-6828b8594a6b | -2.77663 | -54.73452 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cab636a4-1b21-3e79-bf98-b4f5f2068992 | -2.68335 | -54.96006 | 2024-10-29 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3497021-d46e-344c-8bad-3ff32a0db870 | -2.6828 | -54.96351 | 2024-10-29 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cf097d4-b388-3403-af2d-5f235a75d03c | -2.55952 | -54.62971 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74c5e44e-56e7-3f02-b592-a0a83b507575 | -2.4668 | -54.76704 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e1d33a3-1ab9-362d-9086-b474237fb2f3 | -2.38853 | -54.65956 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0dd57c0-b49c-304f-9542-dd84513d44d5 | -2.38799 | -54.66301 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4bcea4cf-ee9d-320b-a4ec-c3d52c949164 | -2.16296 | -54.63465 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README87.md)
