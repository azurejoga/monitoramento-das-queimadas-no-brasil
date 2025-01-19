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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fa04cc2-e21e-33ee-8026-b293dcf789bc | 4.4993 | -60.6987 | 2025-01-19 00:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ccc04f64-ee65-362a-aa13-6573a1022250 | 4.5177 | -60.6982 | 2025-01-19 00:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 8c2f7985-5daa-3cd3-a869-00eae0f15041 | 4.5176 | -60.7172 | 2025-01-19 00:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 743fc176-a44f-31d0-a205-48b096fef206 | -15.64288 | -39.19138 | 2025-01-19 00:15:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| b3df2b8b-8b98-386e-b307-41b25277c9a3 | -8.47244 | -35.05386 | 2025-01-19 00:17:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| edddeed8-0ac4-37c8-a650-e6b74e1754f4 | -9.24518 | -36.80685 | 2025-01-19 00:17:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 37703dbd-0b52-3861-a353-0eb7dec9cb47 | -11.02959 | -45.05133 | 2025-01-19 00:17:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d6a38397-b557-39bb-85c6-c69b29bb8f71 | -8.47433 | -35.05935 | 2025-01-19 00:17:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| de1c770f-dcf3-3a87-9c78-c5bd69943fc6 | -9.93219 | -36.06553 | 2025-01-19 00:17:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| a4818ab5-7ff6-351c-af20-a06aaf59552f | 4.5177 | -60.6982 | 2025-01-19 00:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a1eae5c9-af17-3400-a3de-143bb082ab0a | -17.837601 | -40.148499 | 2025-01-19 00:20:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 400f277f-ccb7-3310-9a67-c9bf798a1f04 | -15.6503 | -39.191299 | 2025-01-19 00:20:00 | METOP-C | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30188fea-0b3d-3161-8378-01556c6270ba | -9.5095 | -35.752899 | 2025-01-19 00:20:00 | METOP-C | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ba98aa0-7125-365b-b941-21d8b0fce281 | -15.6523 | -39.199501 | 2025-01-19 00:20:00 | METOP-C | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42a690c2-ac63-3a96-9fd0-f4bc3d06d7b9 | -17.841 | -40.1633 | 2025-01-19 00:20:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 977245d9-e53a-33cb-801a-2b0ddf07e827 | -9.5174 | -35.784 | 2025-01-19 00:20:00 | METOP-C | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 639c3937-ee19-36a7-82b2-90ecbb21c544 | -9.5135 | -35.768501 | 2025-01-19 00:20:00 | METOP-C | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ddd0c8b9-5720-3052-8b7f-5443e6a63309 | -17.8393 | -40.155899 | 2025-01-19 00:20:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 13303edb-7932-3e9f-87f8-b5d276adae16 | -20.3325 | -47.739201 | 2025-01-19 00:20:00 | METOP-C | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e25095a8-d7e6-3e5f-b5ad-178dadfc83f8 | -9.5172 | -35.7363 | 2025-01-19 00:30:00 | GOES-16 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.5 |
| 263e5feb-3224-3a88-b33d-385c0c7e3e92 | -9.5168 | -35.7636 | 2025-01-19 00:30:00 | GOES-16 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 129.9 |
| cad05e36-c490-3534-8438-401971564a3d | 4.4993 | -60.6987 | 2025-01-19 00:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 3aa67aad-ca91-35e1-8403-9b37885e270c | 4.5177 | -60.6982 | 2025-01-19 00:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 85.0 |
| eeffa1b6-2009-375c-8bef-2ee95cc30eea | 4.4993 | -60.6987 | 2025-01-19 00:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7b0ad416-e659-3db0-83b4-76e9bb140056 | 4.5177 | -60.6982 | 2025-01-19 00:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 148.5 |
| d783f127-d912-3178-bba3-c52bb8b98de5 | 4.5176 | -60.7172 | 2025-01-19 00:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 87e78e51-0f5b-3e68-9b35-7f7f0f373259 | 4.4993 | -60.6987 | 2025-01-19 00:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 117.7 |
| c1fcd4e2-a347-34cc-9a3d-47b20288f9d5 | 4.5176 | -60.7172 | 2025-01-19 00:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b1caa55c-4b6e-355d-8430-6c21ff27495f | 4.5177 | -60.6792 | 2025-01-19 00:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 24aea9a8-ca9d-34b7-a86e-928a12f15c14 | 4.5177 | -60.6982 | 2025-01-19 00:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 20916513-a487-3cb9-828a-e19125b21c27 | 4.5177 | -60.6982 | 2025-01-19 01:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 2b66aa86-f43b-3aea-af73-a4c8c91a5a99 | 4.4993 | -60.7177 | 2025-01-19 01:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 57372c52-e7af-3534-9df5-0c4089ca05e7 | 4.5176 | -60.7172 | 2025-01-19 01:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0c8e7aca-9ab5-3d11-b7ee-986edba72db9 | 3.2942 | -59.9443 | 2025-01-19 01:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2e38ca29-5ebd-34c2-8a36-7089261259b7 | 4.4993 | -60.6987 | 2025-01-19 01:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 107.9 |
| adcf96ff-47d1-3da7-9809-02c05b331dc8 | 3.2759 | -59.9447 | 2025-01-19 01:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 57f6849e-8ac8-33c9-9e87-414277d2d065 | 4.5157 | -60.672199 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f63e5e7c-4922-315a-9911-572c07fe6397 | 3.1171 | -60.755299 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 529310f5-671b-3960-a871-489ad4c5aeb1 | 4.5141 | -60.679298 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aa3c44d5-5d14-3cde-878f-713a7aa39dfc | 3.1073 | -60.753101 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c2ce52c-6eeb-3cb7-85dd-64ebdbb34488 | 4.5011 | -60.691399 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 023de073-d43b-3fb7-b1a3-22a640f081dc | 3.1202 | -60.741299 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b4130b5a-8783-33d4-b578-71fa813e03e0 | 3.112 | -60.732101 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3892ca7d-1e2a-3a28-950e-09bf89ae5aa3 | 4.5322 | -60.6908 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb0079d-e16f-3ba9-b54a-6ba6d7736c56 | 4.5208 | -60.695702 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f012f5d0-24a5-3697-a0b8-5b3a38c52b67 | 4.1119 | -60.820599 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 76787498-b369-3c9e-8011-817f5f3f6da7 | 4.3729 | -60.804298 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d8ee5419-dafd-3071-9671-3a72592c13d1 | 3.2697 | -59.9356 | 2025-01-19 01:07:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 008a2eea-2e1e-3805-bd52-fc47f4f2bb81 | 3.1151 | -60.718201 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c90430c6-4a9b-394c-ba27-191cd7ef6d6d | 4.3745 | -60.797298 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8bca847b-6bba-3d85-8916-66aba41b35bd | 3.2828 | -59.9231 | 2025-01-19 01:07:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 42ade883-fd18-34fa-ba3b-3736c5937ff5 | 3.1088 | -60.746101 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9482e397-999d-3c63-b704-d44d608ffc38 | -28.682301 | -55.950802 | 2025-01-19 01:07:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| a7695171-6ec0-3a8f-936a-4173bf69172c | 4.5338 | -60.683701 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 271bc79c-c2b7-3e19-8290-0274066b8522 | 3.1218 | -60.734299 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d9937267-1c9d-3c4a-9aa6-2f1be602abbd | -28.683901 | -55.959 | 2025-01-19 01:07:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 73a2ed95-6259-3bd0-8745-e4d7c7e6920d | 4.5093 | -60.700699 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f21488e2-f20e-331a-8a19-32b372bb5581 | -26.3188 | -52.234299 | 2025-01-19 01:07:00 | METOP-B | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6c43807-ad11-3323-bf8b-c344fcc86d7c | 4.5109 | -60.6936 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba90d13-b356-3fef-8b93-406ab9447af9 | 4.5027 | -60.684299 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b132e82b-6a1c-331d-b3f6-f85bc567a4aa | 4.6151 | -60.872601 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 36de9b9e-4d40-310a-835e-f6ea6e3df671 | 3.2812 | -59.9305 | 2025-01-19 01:07:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| adf7a7df-0c07-300d-a4e0-42b6d2466d49 | 3.2714 | -59.928299 | 2025-01-19 01:07:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3686846a-b6b0-34b0-8636-24f222c8ee89 | 4.6167 | -60.865501 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 485e9a8c-16cf-3bc1-9431-0ef89a302516 | 3.1186 | -60.748299 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d22353fb-ded0-3efe-9250-76599acbda60 | 3.2845 | -59.915798 | 2025-01-19 01:07:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4e53e556-acae-339d-8dc9-b70ea0bd41e1 | 4.1103 | -60.827702 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 802166eb-edda-39c7-be50-7c6e48d603a6 | -28.6399 | -56.0471 | 2025-01-19 01:07:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 7414136e-e3d0-3067-81fa-f7527eb2d905 | 3.1104 | -60.739101 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 28a63012-a19b-3b1b-be77-978fa0932e53 | 4.5224 | -60.688599 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 08a548b8-b630-391e-a38a-0c6fd32fe536 | 4.5125 | -60.686401 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c4f8ef9d-d54c-3248-91d8-35bdc1509234 | 3.1135 | -60.725201 | 2025-01-19 01:07:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1f95d8e6-5d50-3406-a02b-8fc75e69140d | 3.2681 | -59.943001 | 2025-01-19 01:07:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1d0aceaf-5339-3156-955f-793d3b48eaa3 | -28.6383 | -56.038898 | 2025-01-19 01:07:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 7c9d91f5-db2e-3f9f-b8b4-bf39fd7bf3f1 | 4.5043 | -60.6772 | 2025-01-19 01:07:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3f8c161a-6a81-328d-8a9c-c15b499eb4aa | 4.5176 | -60.7172 | 2025-01-19 01:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| dc0782b4-82e7-35c4-a626-a56db09ce424 | 3.2759 | -59.9447 | 2025-01-19 01:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 885a0d7f-7b6f-3121-bfc8-776138a6ca33 | 4.4993 | -60.7177 | 2025-01-19 01:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2be35481-5090-3cc7-b908-c78c4b9c8d22 | 4.5177 | -60.6982 | 2025-01-19 01:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fded9796-97d3-3dc7-beb3-07a61faacd86 | 4.4993 | -60.6987 | 2025-01-19 01:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 679ef589-4ac8-3059-a829-cfbf6f9f1bb5 | 3.2759 | -59.9447 | 2025-01-19 01:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c40f1616-969b-33f2-b96a-bfbcaa6116df | 4.4993 | -60.6987 | 2025-01-19 01:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 41240da0-25a2-3704-8487-0661ca4a21d3 | 4.4993 | -60.7177 | 2025-01-19 01:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8f141670-9e1a-38ab-8f90-caa575e2dd66 | 4.5176 | -60.7172 | 2025-01-19 01:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a1a3891a-652b-317e-b6e5-39a1cc606a15 | 4.5177 | -60.6982 | 2025-01-19 01:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f12da93c-6fcc-3d8e-9fc1-4b51de4504f4 | 4.5177 | -60.6982 | 2025-01-19 01:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ff86d39e-9b06-38fc-8467-f478ca233485 | 4.4993 | -60.6987 | 2025-01-19 01:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 5c930289-262f-3787-97b0-fac56d53ddae | 4.5176 | -60.7172 | 2025-01-19 01:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 99e7f130-9097-389f-b03e-385a2845b1d3 | 4.4993 | -60.7177 | 2025-01-19 01:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| f8690272-2bfd-3114-b901-849a449dfefc | 4.5176 | -60.7172 | 2025-01-19 01:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a017d2f0-cdb6-3cf3-8024-c30ab267da9a | 4.4993 | -60.6987 | 2025-01-19 01:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1efcd9be-bb9e-3779-bc4d-d75cb3e2f078 | 4.5177 | -60.6982 | 2025-01-19 01:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1609f441-2fe0-3e25-b54c-59f0c1f108ee | 4.4993 | -60.7177 | 2025-01-19 01:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2d236e3d-67e7-3501-9399-047c49b7a469 | 4.5177 | -60.6982 | 2025-01-19 01:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ec31b3be-f9ba-33eb-a450-870e04ecb0e5 | 4.5176 | -60.7172 | 2025-01-19 01:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 88fc4b23-8023-362d-94de-d94410aed652 | -17.797 | -40.1431 | 2025-01-19 01:50:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| fb679646-98d9-3e35-b650-922b34a54e0b | 4.4993 | -60.6987 | 2025-01-19 01:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 203d0eaa-2d3d-3d90-995a-0aaa77edd7f8 | 4.4993 | -60.7177 | 2025-01-19 01:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 73bb6ece-3bf4-3113-b3d3-ba487c4a5fcb | -15.03638 | -57.60567 | 2025-01-19 01:53:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d5ee2395-fc09-33da-9aa6-75dab3c29e4c | 4.4993 | -60.7177 | 2025-01-19 02:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |


[Clique aqui para ver as próximas entradas](README2.md)
