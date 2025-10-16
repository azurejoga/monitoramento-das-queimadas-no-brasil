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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61e4290b-3a50-307c-871a-56e1582f3d59 | -6.37884 | -41.4795 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 92b0e892-3f1e-38a6-9fa6-f84a3688e5e2 | -6.0379 | -44.31918 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd4d383b-c4ae-36bd-b5fc-dbcc834df861 | -5.85396 | -43.8716 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcb1e062-50e4-33b5-8536-5eed77f4892f | -5.91853 | -42.83908 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c3b50978-f026-30db-8974-7f36f7103d1c | -4.66155 | -44.09535 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| bdb35cff-dc35-3f1c-9b5a-9818dedd1401 | -10.81611 | -44.01726 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fa7b8b2-0658-3d9d-b582-845565f2673b | -6.04977 | -41.94283 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f8a78bde-cead-3693-ac39-67065956a677 | -6.05933 | -41.9367 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9575603-bdf7-3004-860e-2b58446a62a3 | -6.12197 | -44.28485 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b084697-3b9d-31df-8169-ed56e393e644 | -6.17986 | -41.72075 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c698348a-c1a1-334a-ba76-4e09c78483da | -5.44563 | -44.26981 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6d40d1f-5d3d-3d6e-8668-1f1efc1f8c23 | -10.14502 | -44.54251 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b42be77-a6e9-3d78-97df-8ee07b077874 | -10.12809 | -44.58942 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 753d0cc9-77cf-3263-8612-7ce5eac21678 | -6.24471 | -42.91237 | 2025-10-16 03:47:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6978fc4-e4b6-3fc0-9db1-22091df47162 | -11.44047 | -44.1694 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a87831e4-4c16-364f-961e-20b361639921 | -5.76711 | -47.9133 | 2025-10-16 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c88b5ebc-0caf-3346-af5f-785bf9e0dbc4 | -4.6625 | -44.0897 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72be6dde-71c2-3279-aad0-f5517b225a24 | -12.64945 | -41.24754 | 2025-10-16 03:47:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29bf0c3a-c95c-344c-a098-365d89a01221 | -4.56389 | -44.00344 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fc5d141-cce4-3ee7-bcf3-6d9eb8e34749 | -10.80968 | -44.00261 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49f0831f-e42f-31b4-ba07-c6e0b60fc6a0 | -5.8988 | -42.8219 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a95abcc1-8b61-3765-bd35-268130c48863 | -6.67963 | -40.03199 | 2025-10-16 03:47:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abc1f904-3e87-3d30-be4e-d1d0446d5dc3 | -6.05105 | -41.93534 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1a28a5f2-1dd3-3d8f-94fe-b3fb0438d1f5 | -4.95472 | -45.10308 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8f3d61d-5c96-379b-8eea-e6c7326e4758 | -3.27339 | -45.84423 | 2025-10-16 03:47:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69e85f43-aa43-361b-8bb0-302be7249aff | -6.10333 | -40.88525 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 45d29399-c4b4-3981-9155-1234296098e7 | -10.82873 | -43.94725 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6887e1a0-f735-3fd8-92d9-6460bd9c8eaa | -4.38844 | -43.38679 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95d36101-33be-3a52-96d6-a6260e494be1 | -10.65106 | -45.24819 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ebec2598-0c93-3ee7-8a33-fea26e58b9c3 | -11.57568 | -44.07324 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62ac6101-f4fc-37a8-926b-505f6ffcba71 | -6.06666 | -41.91862 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9025c18f-280c-3a00-a38e-9ed111981fc6 | -10.66534 | -45.32907 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 712c64b9-420a-3a84-a243-5518ac1f1f56 | -4.94276 | -41.7071 | 2025-10-16 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0eef34aa-4572-3737-8a8c-5ac05fce8792 | -5.35256 | -43.75551 | 2025-10-16 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a8dd0b5a-4988-3563-8a7c-3b1996fe9a29 | -5.4061 | -40.89811 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa830492-42cb-3fb7-88ed-e9d9f227b55b | -6.57089 | -42.9602 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d73038c2-22a3-38d7-a8b4-3db9bd104685 | -6.52675 | -42.19576 | 2025-10-16 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6d4b1f33-c2a8-3fe7-9975-0e284cb72b71 | -4.66343 | -44.08419 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5a3f750-8b62-3585-ad37-71b7cb147129 | -4.41962 | -40.17356 | 2025-10-16 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6b08061-32a2-3f3d-b397-70d4fadee7cb | -4.9611 | -45.09745 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ae69178-ab41-3aef-ac15-035014cde2d8 | -4.4168 | -42.88895 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5f56dfe-a508-3f87-bdbf-a53bd342dbd4 | -4.91317 | -45.98007 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11cabb0f-7af5-3ab6-8a52-95372745b7be | -4.82824 | -45.65376 | 2025-10-16 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b796179b-f2f9-366b-a117-59f8fbb016c4 | -5.73859 | -41.31474 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 113c41f8-1f5a-3405-94f5-f6e9cf4e2d36 | -4.11312 | -48.02057 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95a8da1e-affd-3d62-8d42-e811c70dd1a5 | -6.90524 | -38.26197 | 2025-10-16 03:47:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b95551f-5751-3e19-8a47-e0ce7fd8e3b9 | -5.4286 | -44.23809 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84c2cf7f-3f0c-37b1-b304-a864a5f2196b | -6.22049 | -44.60432 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f16b69fb-ac44-3054-b75b-3d23636dbee1 | -9.71387 | -44.52559 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a601d77a-cb66-31bc-9cfd-051d116f2882 | -6.04417 | -41.93826 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c8fdea76-3cb2-36ac-ba31-00119ec97475 | -10.81204 | -43.93962 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9635f4b5-c199-39ff-9114-eaec2ef07d60 | -4.92177 | -45.89952 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e72a6e61-60bf-3f2c-b03c-39e57a67a425 | -6.21556 | -41.55346 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a67d434f-57cb-3ea1-83a2-942ff0fedb9e | -5.33007 | -42.90899 | 2025-10-16 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83f5e27f-9b30-363e-a5ea-ff249060f959 | -10.64245 | -45.24111 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93c62ed5-db97-3089-be5a-1d07d2108648 | -3.96877 | -44.30354 | 2025-10-16 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c81d58e9-7a61-398a-896e-1c15b4c839ea | -11.57645 | -44.06896 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32a1b26b-c809-391f-a32f-8ce2a4106770 | -4.64362 | -43.13395 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d06a2e04-cb55-324b-9241-93edbf28847c | -10.67004 | -45.33059 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cce3c8e4-b376-337f-bd6d-0ea4a80ee8dd | -11.50797 | -44.07043 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc759ac2-b25c-3f98-bc2b-36d63ce13648 | -4.64452 | -43.13203 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 038e1cc4-c6bc-354d-94d7-ae82960a14b1 | -6.13485 | -41.76458 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f89bea10-9107-3d73-8ccd-41379e6747c7 | -6.03422 | -41.92105 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1700f801-f8bc-3ca6-a78d-9df7cb832af2 | -5.09548 | -42.63404 | 2025-10-16 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14ff43fb-4e08-34b5-abdb-5e213e04ea94 | -5.89214 | -42.83422 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 43545d3d-8e3c-364e-b452-103003956bc2 | -3.01775 | -45.37919 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| fef51f45-c66c-3abf-b4be-a6200bf6ac0a | -5.86954 | -42.80904 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6daab7c5-a340-3f36-9493-4ce768d00e9a | -5.88787 | -43.8729 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0598d11-7a3b-30f8-80de-5de5e10b3935 | -3.01655 | -45.38631 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 94731be7-b800-3a86-b465-6044eb2bc4eb | -5.53994 | -41.32727 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 04987c49-8dfc-34b6-b7d7-e4d90028b9ef | -2.43799 | -49.37667 | 2025-10-16 03:47:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90fa36b3-7c24-338c-9035-6d9e31e7fea2 | -6.15033 | -42.06429 | 2025-10-16 03:47:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b7fda00-e09b-36ae-8bc6-b26336c66595 | -5.38362 | -42.79758 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| af2c4557-a3af-36f8-b60e-0c0f6a3d9f3c | -4.11207 | -48.02644 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 865c4076-32ba-32b0-87d5-988bcfe679ec | -5.41883 | -44.23631 | 2025-10-16 03:47:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a26e249d-4545-3d85-8910-fa355be6df84 | -7.11152 | -37.97663 | 2025-10-16 03:47:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d90286a4-cbba-3f0c-9a76-a40e91fb64ba | -5.84934 | -44.67035 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a96352f-e366-389b-b2f4-039ecd0f0909 | -6.04212 | -41.93773 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27dbfa91-8021-3c1e-b072-53345fdf94d1 | -5.87393 | -42.80989 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1944ebc-c878-3bc1-85a8-f5a17fe209d7 | -10.61157 | -47.41157 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9abdf669-056a-3c30-bac1-2766c50eeea9 | -9.08145 | -47.95406 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3e61f7a5-8aaa-3de3-9ca3-09a7fbcb6bad | -6.33528 | -44.01548 | 2025-10-16 03:47:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc6d54f4-5ab5-3ddb-96e8-e588adcc260a | -5.88143 | -43.88205 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92e6aead-303b-397d-855b-85d52b054eb8 | -10.61657 | -45.24727 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56e1fd27-f104-3a65-8036-1afaa888c8bd | -4.3782 | -43.39015 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 58aca579-5bb9-33cd-9dcd-6f242ff3e2a6 | -5.73002 | -41.31685 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62cb3bad-7760-33f1-bfb0-2cea786ce342 | -5.40368 | -40.91279 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c370571c-7b71-3855-99f7-26d86a68326e | -4.91602 | -37.21073 | 2025-10-16 03:47:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 98d9736f-826c-3385-9325-c69689292a7e | -11.50002 | -44.06451 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dac9b277-9548-3656-bfdb-6357617630e9 | -6.40666 | -42.52126 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7a9ab5d-1d5c-3281-82c6-1e5da2d3bb5f | -10.98657 | -43.72349 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 606029fe-e8d7-33f0-b83a-b2bea021ffb9 | -4.67231 | -44.09136 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95a195a6-5a94-3fc3-a0c3-dd988066c090 | -6.45342 | -43.37432 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fc2b951-6f93-3d85-9225-67e3da64be0a | -10.59771 | -47.4295 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de0781f3-61e5-3ba5-b8ed-c24fc00d1cdf | -4.41757 | -42.88435 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 523470b9-4b46-34a0-bb88-a7f82bc331eb | -3.15811 | -41.99076 | 2025-10-16 03:47:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 1d2f514f-4de2-3ede-811e-4917dc26a762 | -4.39555 | -43.39136 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6db0482e-a9ca-3473-8c42-dc36c86169c8 | -11.63516 | -47.56475 | 2025-10-16 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e18e43f-e016-3874-865b-dadb74a60543 | -4.66553 | -44.10169 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 8dfed1e6-7fac-3218-8dff-bb267ea8b433 | -5.62757 | -43.92943 | 2025-10-16 03:47:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README29.md)
