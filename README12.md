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
| a6caa7f9-6ea5-3eaf-8e71-0dc8b5dd5916 | -1.03154 | -53.55655 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4c7ee0a-a9f4-3c1f-a451-d55b00404b27 | 1.08742 | -56.01527 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c268129-1dbf-3daa-8046-68ef548fabc5 | -1.44048 | -54.84774 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcd487fe-19d5-3934-9a74-2b4c9a132fca | -1.0795 | -53.45877 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f18d11fc-a723-38f8-b985-0f4ddfaacd58 | -1.35524 | -53.65205 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35991ee1-91bf-3d40-a4b3-ab73aae93dd6 | -1.17054 | -53.42756 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fdca7bb-100a-3779-bc3a-83d31079fce9 | -1.62708 | -53.89861 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a7f87f3-ab34-3b6b-948e-0a98ff502d0e | -2.15325 | -54.61777 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df74d4cd-dc5a-300d-ab0e-78beb2fabf27 | -2.17092 | -54.61673 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a437fdc8-acd4-30d2-9801-bc348bda4e5e | -1.62705 | -52.3607 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02f65657-8905-3c2c-ba62-d8e7f19f416b | -1.07658 | -53.45425 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce6368d-aa4d-3909-afc4-b9f825a90821 | -2.4193 | -54.02103 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 319acbd0-64cb-30fd-a7aa-e8e42578813f | -1.32355 | -54.96832 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a7aa6d-e045-3baf-8300-399b0d012c41 | -1.7589 | -54.18975 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bdc06926-58ed-306d-98d9-8ec11ad8eb4e | -1.59348 | -55.84098 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6f62192-d0b6-32be-9576-e0bf274e9cc4 | -1.87843 | -53.30929 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4525d0b9-5eb9-3287-887a-718cd0cce699 | -1.87547 | -53.30464 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b0c0dea-d52a-3e00-9d94-dd370388d939 | 2.48124 | -60.69361 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d46e2676-774b-3630-a736-81dd3b9c6558 | -1.02801 | -53.55602 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8fea7b5-0fb3-3269-ab3a-e44c6813c4c4 | -1.09656 | -53.64668 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59908aa1-16b6-3368-af79-e16ef681af35 | 1.09364 | -55.9684 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07654628-e428-35e7-b6e2-e7d518251ffc | 1.09696 | -55.96789 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29ca9253-a311-3c49-bcb5-ebb4c9999763 | -1.03568 | -53.55315 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a54463b-73b1-39f0-8ebb-24369c7d162a | -2.16066 | -54.61515 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 088dc942-c695-3ec8-aea7-a43bb287f5af | -1.99959 | -53.27856 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 077bc042-abff-31ef-a784-6589ef192070 | -1.68761 | -53.95018 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60fed64a-52a1-3476-a218-0e4772b11340 | 1.11744 | -59.5836 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e18e2433-57ea-3a56-804b-a68b87f7f453 | -2.15667 | -54.61829 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b10944b8-f018-35c9-9973-4257db072665 | -2.40714 | -53.86451 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f90ebbf-6179-3933-bcdd-5fb349abeb35 | 2.4771 | -60.69423 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20cefa6a-7410-31bd-84aa-eaf06520dcdb | -1.16762 | -53.42299 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1f88e57-224b-32dc-be1f-377fbaa4022c | -2.23906 | -53.69541 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a95fb0f-c113-3247-880f-4e814d8b9963 | -2.16008 | -54.61882 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5bd87f6-b1af-3f23-9db0-2506cbcad070 | -2.1675 | -54.6162 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de698213-8fe5-3106-acc8-8b501f40c8f2 | -1.62045 | -53.82614 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1ecbe55-b8b1-3159-9454-f6ca69baf7ef | -1.0363 | -53.54921 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c7d3ca3-073b-37e0-a2a1-75e037b47be9 | -1.44386 | -54.84824 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d0830ef-4328-34e5-ab8a-6677bb46293b | -2.0032 | -53.27912 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4bc13de-3adf-38f3-ba1c-e4fbe4f43786 | -2.16408 | -54.61568 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fe98490-1b59-36b0-a592-f2a595eb8d45 | -2.16635 | -54.62355 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3b86070a-04b0-3d99-b113-5bbff46e524f | -1.87612 | -53.30053 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18a8bae9-68ee-341b-89b1-d0a22425631c | -2.1635 | -54.61935 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01e7a2b5-62b6-3ec0-8e56-abaa645b3f7f | -1.71031 | -52.78987 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 07ec33c8-1255-3117-9fd3-b0a6b0c9775e | -0.7256 | -52.8669 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e30a2a1-445f-32d7-85ee-effb45f7be6d | 1.03189 | -59.48346 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7e9c08c-06f7-3bcf-b18e-024a5d2b8b9a | -2.4199 | -54.01716 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de1d61b4-7682-3bc4-8c59-a5dc841bbfbc | 1.09087 | -55.97236 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 349044bc-af74-33b5-bbb2-7e572a190e2a | -1.14644 | -53.80897 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94440fd6-2399-30f1-ac24-1f6ea0359267 | -1.03921 | -53.55369 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6bfccc8-2cac-3e68-b713-b6c520ea0a87 | 1.08755 | -55.97288 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 208dcc39-289b-3cb0-bbf1-e8f3f475ae70 | 1.08423 | -55.9734 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8df3894a-b909-3c09-a0cd-320349a1d328 | -2.41905 | -54.01794 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0014fb4f-e8da-3663-9b40-fb10e09c81f6 | -1.87933 | -53.31216 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3856e6ae-bdba-3fb2-a166-f7cee1a96792 | -2.16578 | -54.62722 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 284796b4-265e-39cb-acdb-16e1b404bf0c | 1.13055 | -60.51593 | 2024-12-05 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f17548f-59af-3bfd-96c3-8c6b9895bb93 | -1.88122 | -53.29983 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7468936-dfb8-37ac-b1f1-c573046d6f2b | -2.34887 | -53.86766 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40bc613c-44bc-3b3e-8154-f3478c4e3e50 | -2.16692 | -54.61988 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6a324dbe-9728-38ff-9a03-05cf51cc165b | 0.17138 | -60.59068 | 2024-12-05 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49ad8d75-c678-36de-a9c9-26d7fa929a70 | 2.57667 | -60.69466 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc3bcb3e-77e4-31c3-a660-231ffadcea41 | 0.8974 | -59.38818 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ad190d9-f2ff-34b5-a68c-cca73b3f3756 | 1.03213 | -59.48092 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c10225ba-d4ac-3c78-8511-475c5f20fbb1 | -1.17765 | -53.42861 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f98d957-6bd1-3add-abc6-7a3d68abb1af | -1.15757 | -53.4174 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e83306c-f163-3dec-9ca6-d77bba6d0461 | -1.08013 | -53.4548 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3e734a-1d85-32cc-933b-4cd5dec6a835 | -1.74793 | -54.19199 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 382a6fd2-baf7-34dc-a389-fb28369b55c4 | -2.35167 | -54.50724 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c1f52d9-083f-3011-af48-d29af884203f | -1.87907 | -53.30519 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28a2fc15-b13f-383d-bb1b-efc7388d21e5 | -1.17409 | -53.4281 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cf89e75-7dea-3c87-b472-ef8ab400b820 | -1.35877 | -53.65257 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0315a5a-7bc4-3e5c-8f2b-f96352dab9ec | -1.03507 | -53.55709 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 863922cc-85d4-3061-b70c-12333e05901b | 0.75433 | -59.65678 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc1f222-3719-39d0-bb93-cd71a4e11765 | -2.43054 | -53.97114 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5993621-d0c5-3431-bf1d-474cb146b488 | -2.89013 | -51.5843 | 2024-12-05 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2269bd07-f6c3-3778-8fed-1aff8dff1da0 | -2.32677 | -54.40091 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aaeed1f-fd43-3913-9b0f-a2c992925038 | 1.08477 | -55.97684 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33af43ec-b809-3bc9-a4d5-9f664678bdca | -1.68748 | -52.79078 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c2cb167-e1bb-30b8-ac23-d617012b88a2 | -1.07721 | -53.4503 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef0bbf7-26ef-384d-9be6-b7828024c691 | -2.32618 | -54.40465 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 666ad508-80b5-3209-9840-c78c2c8a8d92 | -2.37611 | -53.83156 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d3f210c-eaba-34e0-ac70-44c51956a63a | -2.89931 | -51.57846 | 2024-12-05 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2e8d1c3-a74a-3dc8-a042-d7755d7aa387 | -2.89876 | -51.58198 | 2024-12-05 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 842db87e-8e55-33c9-b88d-6bc693b496f2 | -2.88958 | -51.58785 | 2024-12-05 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e99557d-daaa-383b-9d5a-9996fd24e6e7 | -1.88059 | -53.30394 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29c6b996-dd18-3cf1-9985-31ef63c6e9e9 | -2.23844 | -53.69938 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f63505c4-d77a-3910-b52a-0a3ed978cadc | -1.57833 | -52.25226 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95bb4bc0-d0f7-3156-8c67-5ff192f7f34a | -1.57905 | -52.24764 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb4f2e64-328b-30b1-b1c2-29996d35dc85 | -2.1724 | -54.6263 | 2024-12-05 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ac1f873d-16eb-3efb-be66-91fa9c21f746 | -4.49132 | -50.24082 | 2024-12-05 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32090b54-ac23-32e4-96d7-961684d87200 | -4.64769 | -46.31908 | 2024-12-05 05:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7382bd16-5ad8-3557-a72d-a06e9a666e8c | -3.1083 | -54.06281 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c5636f4-e52f-3b2f-8886-c055c4a63d44 | -3.26926 | -53.62269 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 774cdbb2-40a0-32a6-9b96-e9c908a5049c | -4.64828 | -46.31505 | 2024-12-05 05:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd80324d-bbaa-3727-8ba1-c5a1051ef401 | -3.11363 | -54.05164 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 609276b7-1141-3040-bac9-8dd9d2f60c66 | -3.11594 | -54.06 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fad557d-58e1-37a1-b1cf-567c62014472 | -3.70796 | -54.19339 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 616ff5db-be59-3934-9378-92dbe7f09d56 | -2.96603 | -58.36912 | 2024-12-05 05:10:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 749906e6-bc74-348c-98dd-68278564a033 | -3.11776 | -54.04825 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06f2a8d3-4c30-396b-8ecd-379ddea35c5c | -3.44672 | -54.08727 | 2024-12-05 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6b1ebfa-a0ba-3852-bfcb-1efd26582cc5 | -3.57342 | -53.01942 | 2024-12-05 05:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
