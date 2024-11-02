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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60d1eb33-eb64-3abe-9771-ab728696ffc2 | -3.2719 | -50.3473 | 2024-11-02 02:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 067f7bd8-9c61-3a5c-9c3e-c563f0064336 | -3.7701 | -43.5554 | 2024-11-02 02:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3e75adc5-9a8f-3337-a0b1-3d0cb5402272 | -3.9289 | -48.3458 | 2024-11-02 02:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 44ce1630-79fa-3eb2-8fca-07384a513a0f | -3.9473 | -48.3666 | 2024-11-02 02:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ca89972c-a0a0-3f40-a309-961213a1b89c | -3.9474 | -48.3451 | 2024-11-02 02:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| dd1ea278-0b81-3c07-bfd8-d4c69d74eef7 | -4.4054 | -43.4746 | 2024-11-02 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a19acee9-9549-3a62-987c-9e1130bc691b | -4.9438 | -49.1564 | 2024-11-02 02:45:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b0660851-5093-3fa2-8a48-e3c339b361c6 | -2.2568 | -50.4376 | 2024-11-02 02:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d59b7cdc-77c7-3ccc-8eb1-207fe3b4e2dc | -2.2663 | -53.7422 | 2024-11-02 02:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 65f1ff9c-89bb-38d9-a102-cfa48591ab6c | -2.8061 | -51.6095 | 2024-11-02 02:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a50e5d8f-77aa-3cff-b11c-fa8f6b1e747d | -3.0088 | -51.5834 | 2024-11-02 02:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 8d33059a-612b-3080-b4c4-c612b9d26e98 | -3.055 | -54.1675 | 2024-11-02 02:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e1731b6d-c31c-39d2-94fe-534ffd1e3ffa | -3.0734 | -54.167 | 2024-11-02 02:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 825edfc9-a7de-36b3-8629-56cede3013ba | -3.1097 | -54.2865 | 2024-11-02 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8ba349bd-d68c-38d9-ad25-9e6add1f31da | -3.1098 | -54.2665 | 2024-11-02 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 91473e17-24ab-35fa-a926-d3f32bebaac9 | -3.1281 | -54.266 | 2024-11-02 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f3f269d1-bc64-3158-a094-5db04a9f103d | -3.1282 | -54.2459 | 2024-11-02 02:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b6a95698-d42f-3502-af1f-c50f076c5c1a | -3.202 | -45.3158 | 2024-11-02 02:55:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c0d8d041-bd7c-3ebd-aa5c-90a698bb0594 | -3.2021 | -45.2932 | 2024-11-02 02:55:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 147.3 |
| b1830b7d-7b57-3cad-ad3d-465d007f9a23 | -3.2205 | -45.315 | 2024-11-02 02:55:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 137.3 |
| e629406a-f6d8-315d-bab6-ea3b50501e0b | -3.2207 | -45.2925 | 2024-11-02 02:55:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 287.4 |
| ac50772b-015c-3a5f-a6f6-2fa3d21384d9 | -3.2719 | -50.3473 | 2024-11-02 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 17b54a73-680d-3175-9139-fc3e5485c385 | -3.7701 | -43.5554 | 2024-11-02 02:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c5b5bd14-b9fb-3b35-8c18-783df30b0758 | -3.9473 | -48.3666 | 2024-11-02 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| afd7c49d-d2b5-3db7-8dd5-8f63078605af | -3.9474 | -48.3451 | 2024-11-02 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b4c9e060-a06a-3add-a5cc-778ac703c80f | -4.4054 | -43.4746 | 2024-11-02 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 59cf14eb-7980-3271-8dfb-9164c64f0b6d | -4.3537 | -48.6068 | 2024-11-02 02:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 315898fe-2e29-36b8-8677-42819da61049 | -4.5575 | -43.1162 | 2024-11-02 02:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ade25a82-02dd-3bf9-b899-d36c294845d6 | -4.5577 | -43.0928 | 2024-11-02 02:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f9523d69-d23a-31fe-9c76-8f810d3b0708 | -3.22 | -45.26 | 2024-11-02 03:05:08 | MSG-03 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d31fd7b0-159b-3ef1-89b7-abd82d72e6a9 | -3.22 | -45.31 | 2024-11-02 03:05:08 | MSG-03 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a12261d4-9b8a-30d6-aca7-e14d4ea8ea30 | -2.2568 | -50.4376 | 2024-11-02 03:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8fd679dc-68e9-3391-beb3-359e903f9f98 | -2.2663 | -53.7422 | 2024-11-02 03:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 20b60384-7019-300e-a2a4-3b7370fb1af9 | -2.8061 | -51.6095 | 2024-11-02 03:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5918374e-6afe-32a2-a587-97f2f2762da8 | -2.8386 | -52.8794 | 2024-11-02 03:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 715b1306-bfea-323c-97fb-1b51b3e88c03 | -3.0734 | -54.167 | 2024-11-02 03:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| cecbfecb-5f99-3b5b-b104-300037c797f0 | -3.1097 | -54.2865 | 2024-11-02 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fd843099-8b48-3a29-aab9-7d4a52b12511 | -3.1098 | -54.2665 | 2024-11-02 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 098fbfb5-b976-3b69-8ef8-35320ee526be | -3.1281 | -54.266 | 2024-11-02 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5cf9ad61-a178-3c9a-9f76-2df473ee8786 | -3.1282 | -54.2459 | 2024-11-02 03:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| af936dc8-05ef-308d-a78b-f09b6404cd0c | -3.202 | -45.3158 | 2024-11-02 03:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f5ada957-50cd-3004-8a8f-ce66fe177607 | -3.2021 | -45.2932 | 2024-11-02 03:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 48ca9c23-1b65-310d-80d5-7b54136300b7 | -3.2205 | -45.315 | 2024-11-02 03:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 205ea5b8-10fa-34b6-b268-ad8fc8107229 | -3.2207 | -45.2925 | 2024-11-02 03:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 282.5 |
| 3296abab-8693-34e7-b4eb-3a412716a0fe | -3.2208 | -45.27 | 2024-11-02 03:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| edc1f829-bc5b-36d7-8c5a-dfffb779eed6 | -3.2393 | -45.2918 | 2024-11-02 03:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d85a1c1b-4f0d-3fc5-9c4d-8b28805c07a4 | -3.7701 | -43.5554 | 2024-11-02 03:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 403d3991-e288-3d2e-9605-7a98cf2e55b2 | -3.7888 | -43.5545 | 2024-11-02 03:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 46bbbec2-4833-30f2-b9f5-07ed5ca32e2f | -3.9288 | -48.3674 | 2024-11-02 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 1784d9c4-5613-36e6-ba39-d2b029b56f70 | -3.9289 | -48.3458 | 2024-11-02 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| de4eec99-6d54-30b2-a1c8-0d8d86223655 | -3.9473 | -48.3666 | 2024-11-02 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f3b4cb24-e78e-390d-99d6-cc1e93fd3384 | -3.9474 | -48.3451 | 2024-11-02 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 31fb1b42-2dde-3a89-910c-583321e0c214 | -4.4054 | -43.4746 | 2024-11-02 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4d5013c1-3f67-3634-82d1-8729f96a7f7d | -4.3537 | -48.6068 | 2024-11-02 03:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a19841ce-372a-312a-8fb9-1050c800e84f | -1.2014 | -53.9184 | 2024-11-02 03:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6d8358ba-92c3-34db-9532-342ebb472195 | -2.2663 | -53.7422 | 2024-11-02 03:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| fe30243e-78db-30e5-90d5-ebcf84752041 | -2.8386 | -52.8794 | 2024-11-02 03:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 450b0d79-52bc-30ca-90e3-b853bc5e1f2c | -3.0734 | -54.167 | 2024-11-02 03:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 74685490-0e0a-3c00-b34a-0c2575c4c441 | -3.1097 | -54.2865 | 2024-11-02 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| aaa946c4-88b2-3156-8e15-cbad1acce569 | -3.1098 | -54.2665 | 2024-11-02 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9578b285-a2eb-37af-9d65-642bbab51d12 | -3.1281 | -54.266 | 2024-11-02 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 40f1de66-c85e-3b46-89fd-534d4b272dd3 | -3.1282 | -54.2459 | 2024-11-02 03:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 659a62ac-1d6a-3c85-bbd8-55ce06745ad5 | -3.1767 | -51.0812 | 2024-11-02 03:15:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7dc90323-e9fa-33de-97a6-e12d749ff7ba | -3.202 | -45.3158 | 2024-11-02 03:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f735065b-fffe-371d-9a6d-eff6030c1701 | -3.2021 | -45.2932 | 2024-11-02 03:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| b630039f-a926-3a72-a551-088592718525 | -3.2205 | -45.315 | 2024-11-02 03:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 115.1 |
| ded0153e-6577-3e4f-9cc5-02015b9e9890 | -3.2207 | -45.2925 | 2024-11-02 03:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 349.4 |
| e64b6fc8-1517-399d-948a-6eba44c8a9ed | -3.2208 | -45.27 | 2024-11-02 03:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b6c1ff34-e3c8-377d-be98-ea4a9d4f468b | -3.2719 | -50.3473 | 2024-11-02 03:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ebcb8133-7acf-37fc-9355-a37b4a4abd22 | -3.7701 | -43.5554 | 2024-11-02 03:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 364894c3-03af-3a8f-bce2-fe3397150913 | -3.7888 | -43.5545 | 2024-11-02 03:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f8a77495-6356-3e68-97d7-9510f1a1b330 | -3.9289 | -48.3458 | 2024-11-02 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 79aca40d-cb34-3083-810a-a08bef3bad0e | -3.9473 | -48.3666 | 2024-11-02 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e9044ce5-c572-36d1-b5cd-c2ed03b6fa46 | -3.9474 | -48.3451 | 2024-11-02 03:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9e1d4601-0a05-387e-bb09-92665765c3bd | -4.3867 | -43.4757 | 2024-11-02 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 40900785-625c-3ea3-8cf3-3bf4d545baee | -4.4054 | -43.4746 | 2024-11-02 03:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0b66107a-41fe-325a-8268-6fd9b1469426 | -4.3537 | -48.6068 | 2024-11-02 03:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| b2e6515f-5091-3545-9a13-b4f1c5183aa0 | -9.3817 | -40.3252 | 2024-11-02 03:15:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 80876661-aa00-378e-b2e6-6432c712ef52 | -8.73968 | -40.58667 | 2024-11-02 03:23:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6358a6e3-79c4-32db-bf1d-c63aad638dd7 | -8.73213 | -40.56659 | 2024-11-02 03:23:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b7b6d5c4-d7f1-3d9b-8dfc-43d786bdb0a9 | -8.6107 | -40.50929 | 2024-11-02 03:23:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 936701bb-bd58-3e3a-861e-258a58116b74 | -8.60725 | -40.50486 | 2024-11-02 03:23:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c642351-f225-3c73-97d8-fd2783f427b2 | -8.60657 | -40.50847 | 2024-11-02 03:23:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9eb422f9-fd1c-3d8e-9822-d401edce45b9 | -7.083 | -39.30508 | 2024-11-02 03:23:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f5342d8-3d75-3d6b-9c2b-0c338fc069fa | -6.86623 | -38.35845 | 2024-11-02 03:23:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a7d9320b-1898-328e-8bad-c865ba18cce8 | -6.77673 | -37.54248 | 2024-11-02 03:23:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f41bedde-8eec-3635-8204-503476a3ddda | -6.77214 | -37.54162 | 2024-11-02 03:23:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1a97a3d-2e14-3e37-ad33-11fcf357c510 | -6.76756 | -37.54077 | 2024-11-02 03:23:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe634251-8617-3e25-8f2b-4d47b3a6d768 | -6.70201 | -37.48326 | 2024-11-02 03:23:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5aee2a08-81e8-3be3-a931-c95e84862389 | -6.62168 | -39.74781 | 2024-11-02 03:23:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e84a6b69-0fc2-3611-96d4-7707bd6614c9 | -6.62109 | -39.75116 | 2024-11-02 03:23:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 21cafeaf-856e-3d5e-b1ff-3e6073a3e7c5 | -6.00126 | -41.8322 | 2024-11-02 03:23:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 58e4ba01-eb1f-3463-9968-e2aefa14cf21 | -6.00041 | -41.83703 | 2024-11-02 03:23:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ecd6fb05-ca55-353c-8e6e-d8b8696d3ea2 | -5.99998 | -41.83428 | 2024-11-02 03:23:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| ef241876-9a3f-3b62-bc68-fe4a518817d2 | -5.72135 | -43.53204 | 2024-11-02 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ee4629f8-e99e-3e5b-89bc-d214f4436b8f | -5.31246 | -43.07439 | 2024-11-02 03:23:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abcd24e1-1431-3ea1-9a2a-18b5e6fa4b35 | -5.11577 | -43.96361 | 2024-11-02 03:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a17f17d-8112-3a3f-ba23-13222a8dc5fc | -5.11158 | -43.96593 | 2024-11-02 03:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5e105db8-89fc-3f0c-96ad-b1aab4e61718 | -4.78935 | -40.06827 | 2024-11-02 03:23:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 57ad3909-dc8b-34bb-9feb-6340ff0a708a | -4.66063 | -43.81976 | 2024-11-02 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README20.md)
