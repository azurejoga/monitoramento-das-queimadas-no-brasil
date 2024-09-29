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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 805ec791-7912-331d-a965-b5b0b79d9a2d | -10.24907 | -43.57707 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5455cd91-cf6a-3320-a085-4b00effd252b | -10.24841 | -43.58107 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 066fd3d9-db29-3e93-a1ef-25aa4918513a | -10.24775 | -43.58506 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdeb9f80-b427-33d2-a87a-fe8bb966a7ec | -10.24554 | -43.57648 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 841d7d8f-76e9-3f56-a201-0d4f30cb9ace | -10.24488 | -43.58048 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40a19a02-8ec0-35ac-8f94-93d38c55d512 | -10.24422 | -43.58448 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54578341-1717-389f-aec2-714ec7f220e0 | -10.244 | -43.56389 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce07cca9-73dc-3bb7-a926-13a4789081bf | -10.24047 | -43.5633 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c006a8e1-d5ee-3408-a928-df90d6254dac | -11.21475 | -43.32444 | 2024-09-29 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e005aeb9-8d15-391b-98c4-fe0b1dacdb8b | -11.2125 | -43.32405 | 2024-09-29 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f14821b-20e2-39d8-b134-fca035817216 | -11.13582 | -43.27187 | 2024-09-29 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5df735ef-cb32-3fc8-86d5-7e2c04da09e1 | -12.08745 | -44.18679 | 2024-09-29 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eb8b28b-e963-3c0c-92d3-e18ddadd8090 | -12.08675 | -44.19098 | 2024-09-29 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aee59699-3df3-3017-a7fc-d9ce206da726 | -12.08318 | -44.1904 | 2024-09-29 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3716b2a3-958f-3a66-a850-e591fab2682b | -11.88081 | -43.81296 | 2024-09-29 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 405aec6f-2b8c-3139-8cb2-0a39ae14862c | -11.88015 | -43.81696 | 2024-09-29 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 853d4969-20f3-3424-bcf9-0dcc97c381fa | -11.87949 | -43.82097 | 2024-09-29 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b99deea0-6326-3940-bedd-80d854fc3f47 | -11.87665 | -43.81637 | 2024-09-29 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 863faa27-6366-3a25-8d98-00d8b76d9feb | -7.58338 | -45.071 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81448128-be06-36ee-9fc5-101bde1bbc5a | -5.01527 | -43.81203 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 9f482091-aae7-390f-8b7c-381ab2cb2d39 | -5.01221 | -43.80666 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d1d6f9b0-86e0-3bc5-980d-0e42a1b9c971 | -5.01144 | -43.81142 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4e6da4fa-f3e3-3c6b-9660-b4f2b883e105 | -5.01068 | -43.81613 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f0831eed-361f-3968-8486-06a72b725b8c | -5.00227 | -43.81964 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5bed15a9-bbf5-3728-afcc-ce7f11f81b31 | -5.0015 | -43.82438 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 660b23c5-2549-3a1c-aca7-73f640141e3b | -4.99844 | -43.81903 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c34c0842-a508-3b49-a3b0-f1ecabade361 | -4.66177 | -43.76166 | 2024-09-29 04:02:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f93e1253-bac8-3aa5-b71d-68f52e50e950 | -4.65793 | -43.76108 | 2024-09-29 04:02:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84e6f19d-f9dc-327e-82fc-331f00568b8e | -4.81915 | -44.35346 | 2024-09-29 04:02:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90a43509-ce99-3e21-824f-72b8808061c0 | -4.56778 | -44.59021 | 2024-09-29 04:02:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5ba44463-cba5-387a-be3b-f425cc174757 | -6.50801 | -43.78377 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a12eb399-0915-3c23-be60-ad2ecb921b2d | -6.37239 | -43.82915 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9163c785-c966-388e-8c4e-15e7fc2fd528 | -6.34315 | -43.79655 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33bdb23c-1fcb-35f6-84ba-2f3fbee8427d | -6.34236 | -43.80125 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa9790e9-304d-39c9-aea6-ae6c2d362133 | -6.34181 | -43.79831 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 004e1bb4-c40b-3baa-a16c-06e4c65cbb04 | -6.34106 | -43.803 | 2024-09-29 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10b97c76-b1a3-3e31-8e69-63339b3f404c | -6.39761 | -44.78633 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1a37fd4d-72fc-33bc-af4b-03c2e8f0712d | -6.39548 | -44.78473 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3aa63869-0c8c-394e-ae1d-8d4315360888 | -6.39492 | -44.78815 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| da83ec52-55fd-3b32-8d92-5216b5f0642f | -6.3942 | -44.78231 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 151bf28a-f694-3825-a121-a8dbbbbaf087 | -6.39363 | -44.7857 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2fd61551-de47-3d2a-bee2-95857a806844 | -6.39304 | -44.78912 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5c8bafbf-6ba8-33d6-a9b3-91836decb189 | -6.3915 | -44.7841 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6f5358b2-632e-322b-8f43-4644509d10f6 | -6.39094 | -44.78752 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e43710a8-675e-30d8-8a36-f08d30c5a3ba | -6.07139 | -43.65128 | 2024-09-29 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 699ecc40-7bc3-330a-9fc3-5af8b0a3b055 | -6.0479 | -43.93417 | 2024-09-29 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21e24d4e-2c0e-3939-bc8c-3b6707700b9e | -6.04411 | -43.93356 | 2024-09-29 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77330b20-28af-3f76-8428-00d0edf691cc | -5.36049 | -43.43343 | 2024-09-29 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4cc41c7c-d49f-3de4-b36e-0f3292208d34 | -6.17467 | -44.29234 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9e09018-0986-3573-9ac7-5286dd8f15d0 | -6.17382 | -44.29741 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f11301a3-b3f8-30e8-b0b1-d4085a2b72d6 | -6.17082 | -44.29159 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d2c2288-2b69-32d2-9793-e32246e5bf42 | -6.16895 | -44.42219 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5aa129da-9652-39bf-a0d4-2acd5563821e | -6.16613 | -44.29589 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aad38aa-144f-3c06-8b9b-9fc5af745063 | -6.07789 | -44.70763 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f5c91ad-f854-35bf-91eb-e05eee0cbb39 | -6.07447 | -44.70355 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ba537ed-fd04-3a74-b3e9-6202f4976083 | -6.0739 | -44.70704 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2296128-a9ba-3de4-a371-6da833187640 | -6.07333 | -44.71053 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf25af50-1f88-379f-84db-3759213b181f | -6.07048 | -44.70296 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5deb6ed8-5d8e-3e46-a952-5162d817f9f7 | -6.06991 | -44.70644 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 907a7971-bae5-3339-a9cf-5630a21079e4 | -6.0321 | -44.54163 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a77182fc-7f78-30db-9f4d-36db18c6a2c2 | -6.03041 | -44.55174 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20fcf667-f0f6-35da-b062-a78b64481b95 | -6.02955 | -44.55684 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f88c3308-ae98-3d15-b0ae-b0f0963cd7f2 | -5.89624 | -44.9519 | 2024-09-29 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27ba068a-9a1d-3ff0-a73f-83286781a31c | -5.89564 | -44.95553 | 2024-09-29 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9600a63b-03da-39f7-b44f-cf662fa93e48 | -5.87994 | -44.70305 | 2024-09-29 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6adb3fee-20e0-3a73-a2f4-141359752722 | -5.59991 | -44.27958 | 2024-09-29 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b00f9f86-439c-36f4-bfca-f8c3118d73a4 | -7.86131 | -44.5976 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcccdd98-e119-35e6-b95f-24fba97ffd6d | -7.86515 | -44.59822 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 423c7f67-5ebf-3499-b916-0b4b56397c31 | -7.86049 | -44.60239 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95489f37-2f63-3191-8b72-6f3f1f8f8f89 | -7.85746 | -44.59697 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cd29acb-7c9e-340f-af70-572d8150a8d8 | -7.84371 | -44.58482 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33513ad3-4704-3f35-b62c-5da10eba0beb | -7.84192 | -44.5822 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 200a5e95-f10f-3079-a1af-c2fe4c2645c1 | -7.84113 | -44.58701 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c5b0d955-98d3-36de-85fd-bd2af8cb1c60 | -7.84069 | -44.57938 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5715b2fe-8e4b-3ce5-9c09-bb9fa8fa8acd | -7.84034 | -44.59182 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 698663e6-53c2-336f-a164-5f218cdd8c8a | -7.83986 | -44.58419 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a95a7386-707c-3f56-bbda-58dcabc23559 | -7.83904 | -44.58899 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c12e15dc-e836-3c1d-9339-6846b3ff740e | -7.83807 | -44.58156 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 29730cc2-a3c9-30d6-b901-9eaacced993f | -7.83728 | -44.58639 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e00ab153-9fcb-3ef4-852d-e355c0e56c8c | -7.83684 | -44.57876 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5f59c259-0149-329c-8bad-3de823a8e391 | -7.83649 | -44.59119 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 04158b0d-d118-383b-91e4-5a070c5ced61 | -7.83601 | -44.58358 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f17fe4af-480b-37ad-83cb-27c1502a5427 | -7.83519 | -44.58841 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7d077d2d-7d8e-371b-bc73-e8a6ffa5d422 | -7.83422 | -44.58097 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f9c6adfe-de2b-3339-acf4-5163866cf738 | -7.83342 | -44.58582 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0dc72cdb-caf9-3c1f-81b1-4ef293161e0c | -7.83037 | -44.58039 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c2a7bedb-8d59-30e5-8dae-f1c2163bd2f9 | -7.7962 | -44.90959 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21a0f9fa-060e-3bc0-8a69-c82b9a3f0b9b | -7.86434 | -44.60302 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56cb257e-af8e-3e29-b295-3a3e3c96a5a1 | -7.56703 | -44.71266 | 2024-09-29 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff018e9d-0f02-3989-994c-f279a2c35645 | -7.38665 | -44.08741 | 2024-09-29 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 860f90b6-ec70-35d3-9821-03851db3bfd1 | -7.3839 | -44.08506 | 2024-09-29 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4fa812e-18c6-31ec-8daf-354d39c1b099 | -7.38314 | -44.08956 | 2024-09-29 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07a47b5e-41cb-37f4-8b31-cacf374fcea2 | -7.3829 | -44.08677 | 2024-09-29 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09a998fe-0d45-33e2-866b-4fad19b50d42 | -7.19093 | -44.21457 | 2024-09-29 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 747e0eaf-eb69-38e5-bda3-550ce22ab980 | -7.10376 | -43.87678 | 2024-09-29 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd7ed16d-4805-37a0-a720-6c36be397421 | -7.08051 | -44.15412 | 2024-09-29 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a46a9f31-2bc5-334b-afbe-ce6879c6132f | -7.07671 | -44.15356 | 2024-09-29 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e713cb2e-e049-3edd-9781-ef88b2b12627 | -7.04966 | -43.96281 | 2024-09-29 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 94622e71-24c0-3c19-a8ea-d748dea7979e | -7.35447 | -44.77938 | 2024-09-29 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efe590a9-55ca-35aa-bb0d-b06d313d4c4a | -7.35364 | -44.78437 | 2024-09-29 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
