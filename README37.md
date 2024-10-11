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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38bbf32d-296b-3a97-bc95-372482a83421 | -5.27436 | -44.20829 | 2024-10-11 04:00:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22a84770-d5f8-36f2-9ec3-ed03250037b3 | -5.20263 | -44.75772 | 2024-10-11 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d173736-7b5a-3cb4-8916-d8a703e67939 | -5.19851 | -44.75708 | 2024-10-11 04:00:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83286b4c-3afe-3bd5-90ab-c7b1ee423f4e | -6.42634 | -43.65579 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1452268f-c5dc-3702-8171-f32bd77e2a3d | -6.42257 | -43.6552 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0fd1fdf-51c0-38be-aae6-4afb3fab3672 | -6.35545 | -43.73314 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79ee52a7-5222-3f0c-b738-60bc26a41bf7 | -6.17429 | -43.70843 | 2024-10-11 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9425fbe7-5e68-3c58-9bd9-19f935f13bdc | -6.17049 | -43.70783 | 2024-10-11 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4713a4a-4430-3871-b85d-967a1a34dc4d | -6.16974 | -43.71242 | 2024-10-11 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8456c380-8d90-345a-baa7-948abe73ed2a | -6.1667 | -43.70721 | 2024-10-11 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 735335e9-0bd7-3e96-a970-b5d8d5399a27 | -6.16291 | -43.70658 | 2024-10-11 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98040155-d811-317d-b0b6-8bb8c45e05a0 | -6.16215 | -43.71123 | 2024-10-11 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b9cf27f-c808-3890-8432-bb7d67822134 | -6.02563 | -43.62538 | 2024-10-11 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5cbda03-bb02-36b5-a5cc-91b1a569e920 | -5.95987 | -43.69655 | 2024-10-11 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ad10232-0f8e-3931-a3f0-24722fb60f3f | -5.74533 | -43.47337 | 2024-10-11 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35c36dfe-ed0c-3aa8-9b27-8ab60f9da7ee | -5.70061 | -43.63289 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a71bb8c5-0f99-3f9a-afe6-f748f40ab2b1 | -5.69986 | -43.63756 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9c24b4a-115a-3dd3-8821-80312ed07ec7 | -5.69911 | -43.64219 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6473b6e-3b95-35a9-8eb5-5230b66f38e2 | -5.69907 | -43.63475 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a9160d8-7092-3b5a-a674-23b028251751 | -5.69829 | -43.63939 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9dec2e8-aac2-3a67-9bc7-4e95410b3c66 | -5.69752 | -43.644 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eee4354f-1dde-367d-a9b5-7291947e98ac | -5.69605 | -43.63697 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee929cb2-ac89-31b9-9d83-9a028babb583 | -5.69531 | -43.64158 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4b5b5e8-f011-3c8e-8bc9-921b41e10525 | -5.69526 | -43.63417 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfcf18e5-2232-3283-9656-269f40b6754e | -5.69449 | -43.63879 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59cc7b0d-0b90-3d41-869d-813eb1f5e176 | -5.69372 | -43.64339 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21bd28b5-b14d-3786-a2ce-bec6604e1193 | -5.69225 | -43.63636 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0b4b960-dc93-3d49-971a-67bd5143e293 | -5.69151 | -43.64098 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9d9181d-d871-35bb-9a09-b8b4d0364165 | -5.69069 | -43.63819 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e261880a-df9b-30bd-861e-2664b6946b83 | -5.68991 | -43.6428 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cbf2d6a-5229-3046-99d7-01c5d3f98b4e | -5.68771 | -43.64037 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11183f37-a2c9-3811-b0fa-6bdfc66f2d0b | -5.68085 | -43.63453 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58407c70-0d1a-3a38-ac51-ea7182ac49e7 | -5.37732 | -43.64151 | 2024-10-11 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 721550af-5b1d-3a9f-af51-c1aa93962808 | -5.28834 | -43.54814 | 2024-10-11 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 87f0eea7-1756-3381-819b-20ff0c3c915b | -7.17537 | -44.87283 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a6cbfd0-9c97-3ecf-b04b-018493b9a489 | -7.17137 | -44.87212 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4dc9044-e894-3ebe-bb22-c96b961d840e | -7.1208 | -45.04922 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7482addd-e0fe-32e1-a5f3-28de69a18f48 | -6.96157 | -44.83373 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf775e81-cd19-32a5-864a-8467a088b540 | -6.96099 | -44.8372 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0bb83cf-b0bb-3995-932e-a3d3d79d0662 | -6.95698 | -44.83653 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c5f661d5-39b8-3539-b42d-107bf1d8ac53 | -6.95296 | -44.83584 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5bfd36b4-4090-3795-9b92-4ee52c26fad3 | -6.95016 | -45.21704 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 748a0b7e-f3fd-3643-ab9d-166e8d60168e | -6.93946 | -44.60915 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd84796a-f2aa-32e6-a224-f6c4efa449c3 | -6.93867 | -44.60562 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a29b5f1-61b3-31fb-b5e5-7a2cf2c3d8bd | -6.93692 | -44.83305 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dc5360f-0942-3c3b-b6d4-7b6cf882b64d | -6.93636 | -44.60317 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 636038c8-7ee5-35f1-8028-cf40b7e50797 | -6.93633 | -44.83652 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73cf3472-32f1-3acc-a3ba-0a5a3ede1c18 | -6.93474 | -44.6048 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5a48b19-3d10-3972-8216-ddca1053061e | -6.81454 | -44.46576 | 2024-10-11 04:00:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb3c20ef-3fdd-3a9f-91ec-9d5e609111b9 | -6.58176 | -44.18026 | 2024-10-11 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1da02b3-ceca-3d36-9c20-53e31498e132 | -6.58132 | -44.17794 | 2024-10-11 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dd7f0716-7874-37f8-91c5-962e1f228a66 | -6.57872 | -44.17466 | 2024-10-11 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 085cc0ec-26cb-3c6d-93a6-0901dcb938ff | -6.57747 | -44.17719 | 2024-10-11 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb2eadd0-2d1c-3dbb-9c6e-52ef065c5a01 | -6.57101 | -44.24374 | 2024-10-11 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d4fe023-1f89-3d17-ac40-186f06abcac7 | -6.57017 | -44.24671 | 2024-10-11 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3e51617-8099-3c17-a0a7-780554b58d1e | -9.57725 | -44.39682 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4c92a11-0132-3993-b0d7-39c7e503b38b | -9.57677 | -44.39901 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a0babeb-fd90-3961-a302-c3ee3ad29ca4 | -9.57646 | -44.40142 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ee148e1-2e27-38fe-9921-b0e7535c698f | -9.57377 | -44.39379 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bf629ce-e5da-36a4-964a-c647bee05714 | -9.57348 | -44.3962 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef67f6c1-72af-3199-8174-cc2835f59028 | -9.57301 | -44.3984 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6260d269-3eea-35e9-9355-039618fa2d41 | -3.61631 | -44.7864 | 2024-10-11 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5593e36a-5961-3736-8f57-b3fa729f13cf | -3.61209 | -44.78571 | 2024-10-11 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1f1eb663-2fbe-33f0-b660-57162f6c2820 | -3.61146 | -44.78957 | 2024-10-11 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 758fd3ce-8142-3deb-811e-176333cc9e71 | -3.60788 | -44.78502 | 2024-10-11 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| eddaaab5-984c-3d43-947b-22b8578ddcf5 | -3.60725 | -44.78887 | 2024-10-11 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 22d4afb2-efdb-31f1-a7dd-9e1da72b39f3 | -5.05292 | -45.59177 | 2024-10-11 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 264a5115-967e-3210-b9c3-983bd0ff853c | -5.05189 | -45.59299 | 2024-10-11 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94dd3ec6-59cb-3508-bf73-cebc785f5227 | -4.938 | -45.73765 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b22920e8-1eec-3801-ad40-0ee0124343e0 | -4.9212 | -45.7834 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80c847fa-e7be-3a7a-979e-743d5edbb6f5 | -4.91678 | -45.78266 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71f65d60-4f47-3ec5-ae44-416044826949 | -4.87225 | -45.78551 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 606c20e2-8eb0-314f-8d52-9aed39961755 | -4.86663 | -45.84714 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 245a0085-be76-3e28-adc9-221b62fb5089 | -4.85955 | -45.38065 | 2024-10-11 04:00:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebfd8d91-07a7-3513-bf3e-f222873c2f08 | -4.7989 | -45.3347 | 2024-10-11 04:00:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2120045a-d825-38c5-b9ed-6b5df1cf66ef | -4.71994 | -45.40151 | 2024-10-11 04:00:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26616d99-0134-3f56-b6c3-fe87ba08c194 | -4.70586 | -45.43301 | 2024-10-11 04:00:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3af90b3c-ed1d-3465-9629-926fe7ce8304 | -4.67355 | -46.05375 | 2024-10-11 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0193b8be-a013-3471-8b7a-da84994ef87d | -4.50476 | -45.59108 | 2024-10-11 04:00:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e77b815-ef88-3858-9c5b-01c4a1e37c55 | -4.50407 | -45.59538 | 2024-10-11 04:00:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4b26f42-fcd6-3e9c-9e9d-297dd20a45c0 | -4.50375 | -45.59331 | 2024-10-11 04:00:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bbc65eb-1909-3a3c-a812-3ff282da0c3d | -4.49428 | -45.71181 | 2024-10-11 04:00:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea0d68c7-1f26-3684-813b-e851968a72ca | -4.37991 | -46.10109 | 2024-10-11 04:00:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99fe34a1-cdb5-3910-8b3b-ba7f5caa9a18 | -3.73098 | -44.66704 | 2024-10-11 04:00:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca9450cf-cece-3557-ab3b-e5f397f16024 | -6.36382 | -46.15954 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc086742-b3f4-32be-ae98-f6db14c25676 | -6.36307 | -46.16391 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8701900-bcee-30cc-85c9-b518c3a5e881 | -6.36053 | -46.16135 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cff0cdd-be7a-30bc-b2a0-35a7d7616b0a | -6.33188 | -46.34408 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 056d3547-3dd7-3831-80d9-d864a6b34e41 | -6.33067 | -46.34194 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d67c0eb1-1107-3b80-9147-5135e9953f94 | -6.32993 | -46.34639 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae9184fd-a13d-3687-8a1a-c880db96f2de | -6.32788 | -45.7043 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7242223-8619-3a0d-b819-8ea56aba0af3 | -6.3259 | -45.70276 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 78f4b207-a935-36b0-a113-d5579ae7ef24 | -6.3252 | -45.70682 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e2ad932-0724-35d2-b273-e316e3e45da7 | -6.32361 | -45.70346 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 977f6d14-e9c1-3f47-aa8a-e71065ead488 | -6.32293 | -45.70755 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 519eb379-a3bd-3dab-afbd-b34306329319 | -6.32225 | -45.7117 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4296c419-b380-38c7-adb7-57a9c14d8be3 | -6.32092 | -45.70599 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0b0b76c-58b0-383a-98d1-94317ae62539 | -6.32021 | -45.71015 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3755e960-601e-3051-8b09-12b528ee10cc | -6.31376 | -45.72184 | 2024-10-11 04:00:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b76a967-6a7e-3ab3-90ea-c4b34362f527 | -6.08226 | -45.99383 | 2024-10-11 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README38.md)
