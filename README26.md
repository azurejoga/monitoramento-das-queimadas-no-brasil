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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b21efc6b-d06b-3c1e-a72f-2c1e050e6b2c | -5.11608 | -44.66275 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 747eb84d-aacd-3323-9320-71d8c262a369 | -5.37715 | -45.94252 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ae86072-cf35-3370-8ab5-30bf2000dc96 | -6.82894 | -43.62362 | 2025-09-09 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd841869-8dac-3c11-bcef-07c4ca523838 | -5.69566 | -43.9235 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01270c3a-5613-3b70-b448-9bff9631216e | -6.0605 | -43.31369 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3afa89c2-f3e4-3af8-9441-62ebb50f5b00 | -5.51275 | -42.67241 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5a8c028-be28-3e72-90c9-fa7376d058ba | -5.37659 | -45.9462 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e0ca4fa-b7e5-3afc-96c8-92f4ea6a7d44 | -5.67302 | -45.31372 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c463d340-fa88-3adc-9428-79bb831e7315 | -6.43375 | -44.06604 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c2f39075-1b2c-3512-a76e-2d343479d863 | -5.69669 | -45.98672 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cf857697-5449-3af7-8cca-14f45758ae80 | -4.53028 | -54.84252 | 2025-09-09 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be4c46c6-979f-3251-bf90-e7f0bceb4c67 | -5.85465 | -44.18238 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f52c4d91-b960-3213-bce7-5d9a76b98fc2 | -4.30168 | -47.57109 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 802977e5-7031-3289-a5af-3f7a8cbfcd34 | -5.79759 | -45.66879 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad55babe-ae79-3f02-b347-ac939865a087 | -6.22215 | -45.62692 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35668dd2-178d-3d9c-9408-9ebb2daecdc7 | -6.17768 | -43.38914 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cc90065-3ba4-3087-8262-ef48a8c3427e | -4.977 | -48.94165 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9693dd34-d956-3a9f-9c00-5af7072f32bf | -5.83999 | -44.10225 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66b5950c-23ab-301b-b5f4-9157ff24d595 | -5.63972 | -45.43935 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd1ed66e-2588-3b7f-a75d-40a498591bde | -6.63165 | -45.10625 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c75b987a-5693-3e3a-9d16-c639c68dde98 | -5.88515 | -43.95303 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3e9d74d-4027-3c89-9553-8d8c422a38b9 | -7.04387 | -43.25024 | 2025-09-09 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94bcf1bd-6c9c-3e3e-a3aa-e92eb1f82bfb | -6.33053 | -44.65288 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dea27d3-87ad-372d-87ef-5d5b20d0ebe1 | -5.4378 | -43.42358 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97899d6b-7ec8-3908-aa5f-3621a31e5061 | -5.57617 | -45.04534 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 54d4338f-6c67-3e9e-b8a9-86e33b96cdac | -6.31322 | -45.67194 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 336e51ec-ec4f-3de2-a4a7-f3c34c17f1eb | -6.78588 | -44.78384 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 415329ff-48cb-33ef-a3cf-484a25a35031 | -5.81601 | -44.84448 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceef227c-127a-3849-b403-0d93dcc4eb67 | -5.76914 | -45.53689 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| deb0dacd-0246-38ff-ae9b-2448f88f559a | -6.40112 | -43.81495 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbcb7b4c-e48b-3928-b031-a4236efdcac9 | -5.69498 | -45.97513 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 261148a9-8147-3169-9ab4-00c8c247566c | -5.93723 | -45.67468 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93668284-f90f-377f-9550-53e75ca0cea6 | -5.93244 | -46.16858 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d523933-2fbd-3f71-ae7b-d6d1269ecb5a | -5.44367 | -42.79618 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 211563c5-fe7a-3560-bd75-3810287086c9 | -5.72229 | -43.10607 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f56cecfa-8ee3-304f-a0d5-b60ca1428afa | -5.81482 | -45.64824 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efe6eda8-0d46-3558-b062-2cd3aab3c85d | -6.3348 | -44.64919 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d378b5-5574-33d7-b342-68de25fadb8a | -3.39391 | -47.49825 | 2025-09-09 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ba882f8-762d-3cfc-948f-9bd7add00e29 | -5.66953 | -45.31318 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aac113f1-8592-3db4-b7a2-195eff40f985 | -3.32694 | -54.91084 | 2025-09-09 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 774e50ec-2794-3d78-891c-30f18bba9191 | -6.40825 | -44.43592 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd02093e-4ec1-3b02-9bec-abbf9ea3752d | -5.45627 | -45.28633 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea6e14db-58ec-3556-9a5f-654d31267c25 | -5.72464 | -45.4081 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8778d35f-6b93-3d6d-b276-249fcfe75629 | -5.82231 | -43.98175 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c079b341-7b67-3ff7-b718-05c0e88b10e4 | -3.32214 | -54.9101 | 2025-09-09 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cce8b51-e23c-3714-b50e-facc0f42e726 | -6.20153 | -45.02916 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16b64f5a-dae6-3fe2-b517-963a2dbe2b32 | -6.17913 | -43.37925 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49a8d11f-affe-3ae8-a552-0e1f9899e840 | -5.83104 | -44.81737 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afb382ac-9818-3bd6-b7de-e2d33d6814e5 | -6.40771 | -44.43439 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf1fc4d4-463c-3823-afeb-5778e29d9ee7 | -4.61307 | -46.59618 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 224702a5-df10-3b14-97b4-132acca1309b | -5.81992 | -43.97221 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39a170bc-0023-3482-aedf-9006513ad443 | -6.27348 | -44.48412 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6debb1e2-1b58-3ca1-91f9-f6331e63f0a4 | -6.05732 | -43.30801 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d1215679-6890-3da2-bfd6-5be2688207b3 | -6.22788 | -43.51541 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf358d41-a714-34a8-826d-d5478632104c | -5.37999 | -45.94673 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64bd48ea-7070-3912-a131-e7c9be6aa139 | -5.44191 | -43.44871 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d684a880-6398-3593-b5ab-94326c624bcc | -4.19272 | -47.5712 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fca0ef4-87e4-34e4-be91-eb3e9080145b | -5.80047 | -45.6731 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a90b379a-a728-3951-8051-c84cd4ea08ab | -5.94065 | -45.7911 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 496fa4af-6d92-3ce1-8fd6-63ed29a4f737 | -5.02281 | -43.60559 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4e89999-2056-376e-bd52-8e1286618f27 | -3.39083 | -52.8396 | 2025-09-09 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a3def61-ca58-36eb-b891-8da67cd78429 | -3.30812 | -48.71623 | 2025-09-09 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ae9d3bd-1efb-3a35-bda9-f5bf2efd5bc2 | -6.20055 | -41.02515 | 2025-09-09 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43f5cc86-bad8-3224-aec6-70b02bab72b2 | -5.1936 | -43.04367 | 2025-09-09 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a93b9c46-641a-33cf-87f4-a7f62c8eedfd | -5.58802 | -44.26196 | 2025-09-09 04:32:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35e06c7d-b44d-37a8-9118-21b6b8431dba | -5.44238 | -43.41939 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b835ea22-3266-3e3f-a206-fc4843d9b17d | -5.04471 | -43.12642 | 2025-09-09 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4a5b7ea-336a-311a-b387-7a25bf41fbfa | -7.19344 | -44.88724 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80217a73-cd27-371c-a240-1b36b60740d0 | -6.06296 | -43.32426 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93d38062-cd2a-3137-b2d2-1718f143e7be | -5.70047 | -43.89164 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94612966-b009-3dca-99e1-f3034d7e7ef8 | -6.22151 | -43.50465 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b89ab8a-20f8-3fe3-97e7-6da0bd6bc9c6 | -5.69534 | -43.90016 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51a75907-3c94-32e9-9bd3-e9cdb7491b32 | -5.86477 | -45.29303 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f02ad902-8292-3355-8de2-8ced853136c2 | -2.43535 | -47.18929 | 2025-09-09 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d5298f-97b0-37f2-b950-962200cffc8f | -5.01495 | -48.46527 | 2025-09-09 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 541b9a9b-32ed-390f-98e9-ca87536e12af | -6.22864 | -45.58477 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 309988ae-74fc-3083-aa82-db10e8899beb | -5.92691 | -45.76578 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d0d6798-c9ef-3cc2-8047-c55cc10b510d | -6.7694 | -46.36182 | 2025-09-09 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a5a3131-3f66-373c-8542-2bb128632e7c | -6.0982 | -44.13234 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5c277ba-630a-39b1-b6f2-05b075e56079 | -6.30314 | -42.20247 | 2025-09-09 04:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aaf90368-9959-3546-844d-b1c548404a3f | -5.5867 | -42.90604 | 2025-09-09 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8ebb9c3-46b4-3fce-8d8d-380b6e0b6b74 | -5.58722 | -42.9025 | 2025-09-09 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e148d883-80e3-3aea-a4b2-6b5530b227c9 | -5.35334 | -44.79616 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4be658f-93f9-33fa-84b5-abc5043f911f | -6.18657 | -45.81214 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d8aeaa2-018a-363c-8f62-57fa4efb1da3 | -5.82299 | -43.97725 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 341f87a1-9e7e-39fc-ba3c-0e480b0553c5 | -5.92003 | -45.76473 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eed89db0-6860-3b0c-9abc-2fa7e0a952d2 | -5.67502 | -45.46443 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8630eee-cc78-36d7-8d14-673a18ff0687 | -2.43479 | -49.30981 | 2025-09-09 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca62960b-7428-3531-b52a-5ebb5f72066f | -6.18225 | -42.64759 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7570a8bf-4a7e-3abc-ad99-ceb566aaec98 | -6.34834 | -44.06527 | 2025-09-09 04:32:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 993016a1-f569-3ab3-9ba6-da077419a969 | -5.71361 | -45.41032 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 041688b3-e8bb-3d68-ac46-fdaad1be6f9f | -5.7509 | -45.25663 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02321ed4-1505-35e0-92dd-3fb971f161b8 | -5.26368 | -44.45395 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03e65e02-13ce-37b9-ad1e-c6df81740943 | -7.04038 | -43.24617 | 2025-09-09 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a05312f8-04ee-3efb-8c56-c4ee308919f5 | -5.0867 | -42.42537 | 2025-09-09 04:32:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e930f0e3-730e-3a99-9c4b-49e3be5cae50 | -5.55011 | -45.17107 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4188ab30-e795-3b96-b0fa-e5c065b144b6 | -5.87528 | -45.62273 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc26d102-bd38-323f-9d31-50ff447461ac | -6.86519 | -45.59396 | 2025-09-09 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4bd2fb3-f05d-3a11-8d35-ff818ecd8df6 | -6.31843 | -44.38137 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10f27d7d-2d58-3727-b79f-2fc309c75854 | -5.62847 | -43.11568 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README27.md)
