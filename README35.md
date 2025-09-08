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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b64953bf-f6c4-3a4a-b490-62f747ec141c | -7.73637 | -44.72788 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5855b61-ef95-3098-ba56-1393aeeeeb66 | -5.94293 | -42.95884 | 2025-09-08 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02af32e9-1b0d-3dd6-9093-d8385d7014fb | -7.73538 | -35.13807 | 2025-09-08 04:00:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a1ce11e2-05ca-3a91-a92c-bfd265dd564e | -7.82615 | -45.42035 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e3de075-a90b-3342-9cf0-3d7017ff7681 | -5.83894 | -44.09555 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 389e615c-c916-357e-b4a9-3d123e890896 | -6.28474 | -44.38794 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a8a95c7-0c34-32e3-bfd6-23a31e1238e1 | -6.8153 | -52.80986 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e737dfbe-7fa8-3071-b2ea-9113e302f504 | -7.75664 | -44.00029 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c333d94-ef8a-3e9a-84f7-23024df4557d | -6.53572 | -44.79589 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e12f9ec-d95f-375e-9a3e-32675246d8cb | -6.30216 | -43.8278 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1381ee10-0aec-35b7-8204-a808f32aa20a | -7.09902 | -39.28335 | 2025-09-08 04:00:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb4867c3-8103-35c3-be5d-f529bd323907 | -4.27078 | -48.18894 | 2025-09-08 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1dd43af7-42dd-3531-a1e3-4be0dfad78aa | -6.23097 | -43.5105 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb1a0666-5c67-307b-8ff5-7cb705f341b4 | -6.21242 | -43.37551 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ab0832be-c38d-32c7-8ccd-577a4e2b53c2 | -4.89684 | -42.21588 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8ec0cdc8-3ebb-37c5-950e-b2eacea697c6 | -6.38528 | -42.5982 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dc4d43c2-bab2-38f3-a1d0-b965b7c89200 | -5.94895 | -45.74898 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1e9d071-a7b4-32bc-972e-0f90d4939a63 | -6.02458 | -45.88905 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f809c847-0b29-319e-8e51-48c99ab36aa8 | -6.22261 | -43.28951 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fae2c5a-a7bb-3e31-94ad-efdf23da0077 | -6.07567 | -43.36375 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a020c25d-7fc2-337a-b434-7377699cf4d7 | -5.94579 | -45.74966 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 188e184b-6074-394a-a928-d8b2938a4712 | -5.43187 | -42.8053 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b53ca87f-0c34-39d2-83b3-e7888b7875aa | -6.40382 | -42.97824 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32d5e7d1-508d-3cca-9513-89bf1383d1b8 | -6.82625 | -52.80689 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48eafaa5-2bd5-32a8-b578-45b22cdfce5a | -7.35091 | -43.94065 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6493a69b-c82d-364a-baf4-e7094196f067 | -6.10078 | -45.46493 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 965f6cfc-a868-304d-b65b-0f79ee49df4e | -5.35741 | -42.63898 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2846508c-7a3b-3ee2-b6f8-da1700a8bfa3 | -6.0592 | -43.30361 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85566794-6677-3d4d-a632-66aba34dbbf7 | -6.0098 | -40.22702 | 2025-09-08 04:00:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f311aba4-d077-325f-85e3-96c036995739 | -5.88378 | -43.96609 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4351d68f-87e0-377c-97f5-2da196fb80fa | -6.20071 | -43.60077 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9eb1ae6-f865-3a6b-992d-b3305fa5ddad | -6.17235 | -44.24142 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8fe1bd93-858d-3b51-b1d7-b4adc9caf725 | -6.20334 | -53.27095 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d7dd76b-92de-30c0-a12f-6f04b33b60fc | -6.83619 | -52.80857 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a17ec6ad-d6b1-3722-bffa-f429d3666bed | -8.13034 | -44.87432 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9c5cb62-c0ba-32ef-b290-4e3cb75f0dad | -7.22551 | -46.20371 | 2025-09-08 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e7558aaa-770a-35ee-8a6a-01576877ccd6 | -6.04011 | -43.69801 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 232cf483-faae-37b7-b8ba-0588ae7332b6 | -7.09628 | -43.90396 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 393ec15c-4fcb-38ee-9e15-8ddb3f742408 | -3.89816 | -38.53769 | 2025-09-08 04:00:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e002001e-623b-3a8a-be6c-e61c8380bba8 | -5.87386 | -43.95508 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aab02d86-a9a8-30f8-8de2-ed55709627af | -6.18139 | -45.42627 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50a680de-e83d-3d55-a1a3-834953820d0c | -7.2928 | -44.14796 | 2025-09-08 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aa42972-801b-306f-b514-5e049d5df604 | -6.36194 | -42.58623 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5dafa985-f2a9-3f97-9cbb-d6dae895d5c5 | -5.84278 | -44.09621 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bef335f6-4568-3507-89be-9bed205dd9fb | -8.61562 | -40.20076 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d4bba13a-5630-3001-84e6-474165be9162 | -6.97729 | -45.5743 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22cf33e1-5da7-30f1-b4b1-11f169507b3e | -4.483 | -48.11634 | 2025-09-08 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c507230-04f7-3503-948e-dd612cd271ca | -5.43222 | -42.66652 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db92d371-d3f8-3f26-a33f-5f85f52268f9 | -6.13372 | -44.23543 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b338fc23-b6a0-308f-a1cf-4b9918bf138e | -7.10743 | -44.14185 | 2025-09-08 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b96f475a-c246-3c00-9e5e-e572cf95c02c | -5.87458 | -43.97452 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 061bd297-af53-3a79-80fb-f87795ab2c79 | -6.87085 | -44.25628 | 2025-09-08 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6329188-d98c-395e-8a2a-c2a4aced4a9d | -6.21172 | -43.37982 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c97da91d-7b6b-38c6-94e8-5268b504d2ac | -6.24417 | -44.8257 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed581315-a845-3f38-ade7-1b9bb2100941 | -6.30594 | -43.57555 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82027279-7a62-39e9-8e94-f242c3a4f386 | -6.63255 | -53.37159 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a47277d-4526-3533-bf6f-43fac820be70 | -7.83213 | -44.85457 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f00919dc-ee4a-3820-9967-0db3a59e74ae | -6.06391 | -43.11693 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5596c47d-00db-3911-83e2-60c778cdcc8c | -7.82209 | -45.41975 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe010857-5a1a-31cf-b9d1-7daad6399d20 | -6.25521 | -43.68718 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09eb069b-7551-3b76-8e24-0df39c945ca0 | -6.10333 | -44.14392 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e75c946-db11-338d-9947-ed5eb3f72ed0 | -5.43973 | -42.80231 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9545eb35-523e-30fd-9297-d2116182da3c | -6.19977 | -42.64708 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3e36fe07-6380-3b7c-b205-8eefb0d89026 | -8.1978 | -44.78734 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7e20a625-b6b3-3e33-b094-5781c0611317 | -4.64476 | -46.31232 | 2025-09-08 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f867f4c-36f6-3694-bfba-524ebf858872 | -5.21835 | -43.69515 | 2025-09-08 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8694b70e-e8bc-3fca-b949-4120d4e737ba | -6.26564 | -43.69369 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fb29a33-f545-3e8b-b58b-bf50e6d83cfa | -5.74081 | -43.7249 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05bcffd4-bfd6-3d0c-9167-840b35f096c8 | -6.30666 | -43.82388 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40417926-2293-39d7-929b-ebe344b41095 | -2.13659 | -47.71024 | 2025-09-08 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d745727e-a123-3000-8a29-df8fbe61b8ee | -4.89914 | -42.22085 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 30a893b3-b97d-39c6-9f21-35f249236ebb | -5.37195 | -42.63184 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d21caaa0-6940-3e75-82f9-5719c814c9b2 | -5.21251 | -43.28138 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a8f7a721-ee37-34d6-bc22-b7796f97681c | -6.40608 | -42.98707 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 186fd36e-9773-31fe-a3d7-780e5bced690 | -6.60516 | -44.01301 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc8283ad-95a1-3921-92e5-f5e68bf8cb7b | -6.9288 | -45.80665 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d8e6962-4f9a-3819-abe8-71b3e6bdab45 | -5.79178 | -45.65515 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41cabfa3-4e0d-3fb2-91b5-b7c74a1c392f | -4.63178 | -37.83317 | 2025-09-08 04:00:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ec89b52a-e78c-356b-b2ef-3898a8c09428 | -4.8921 | -42.21972 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a5124013-b7b6-301c-8c1f-86bcb3fb03a8 | -7.29659 | -44.14853 | 2025-09-08 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59ff66ee-f88b-33fd-80d2-33be35a9be44 | -5.18827 | -43.03905 | 2025-09-08 04:00:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 663a8abe-de52-3741-890a-690679cdd5a3 | -5.86432 | -43.23548 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7816b9fe-f545-3d87-bb6f-ee53e5930b1a | -8.19244 | -44.77208 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a052277c-55e8-3a1f-b225-69da1a3dcdef | -6.46271 | -43.95976 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8df3291-ff52-3f1f-9cba-054e997b1e9c | -6.14173 | -43.30221 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7d534584-26f6-30f3-9019-0af7009049b0 | -5.8242 | -43.97131 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8885ae7-aec8-35b1-93ee-1e433ca0bd6a | -6.2619 | -43.69314 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80b6cc38-806d-3bab-9e97-6929dca0c0f3 | -6.59431 | -44.12531 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b08bcb9e-a510-37d8-9440-7a26e40b3ac0 | -8.20636 | -44.78385 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb95dfae-0ecf-39d0-bb90-e42ed076f5cc | -6.97566 | -43.1538 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eddbe3de-7aba-3056-86a2-81af855a4c22 | -5.98656 | -44.1468 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c904f5af-eb1f-3d38-8396-287677808f0f | -6.82191 | -52.81139 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d80cebcd-1a82-338d-a695-6dc733e67d00 | -5.88184 | -46.02978 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a36a82ab-d137-352e-9fdd-ed2301fbf1e8 | -6.55726 | -42.9418 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75540088-358b-3852-8c0f-59689f2de8da | -4.2713 | -48.18585 | 2025-09-08 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 13c07432-8cdc-3ebc-8205-c413797b8792 | -6.25875 | -42.57389 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de0b16d5-b113-329f-be1b-f6bfb8186183 | -6.85331 | -45.91922 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7582e1b-6416-3533-9542-17a0db1cbddb | -6.18956 | -43.58699 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b9b784b-f767-38ed-99a5-41e269d4653a | -6.17566 | -42.63908 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 91d22ac1-d642-32af-bd5a-e2146c7150dc | -6.53785 | -42.92604 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README36.md)
