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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 078fd7e4-94ca-3d77-9fbd-03fda64db969 | -9.73019 | -43.41794 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00773d74-2a71-3530-88c6-3985b043a4db | -5.99613 | -57.69854 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2791e4a-23fb-3a15-a76d-274b637bc70b | -10.74232 | -45.08235 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 9f2e3997-ef17-3ba2-bc9e-476c50cf225b | -4.34568 | -56.27889 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18a2ab2f-a629-3903-ac22-430964cbf35f | -8.75574 | -62.42276 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0594fef-0206-3146-85a2-cc02d8a77c67 | -11.32008 | -45.06757 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25fea3f8-f6e3-372e-865f-bffa58172000 | -7.11332 | -56.51331 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee0cbd5e-d7c2-3247-992c-df2049e5519e | -5.15953 | -55.9621 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5ec488b-381e-3c3b-aad9-428335494410 | -5.16694 | -55.96333 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a05ff23e-b10f-39f7-aa6f-b89fc9d07105 | -6.06004 | -57.78774 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66088535-3128-3244-bb56-6e7409fb368d | -3.76732 | -61.75175 | 2026-09-07 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fea5566-7ca2-32d3-bee7-58e49c2a7601 | -4.48905 | -55.50177 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a05c637e-15a5-3864-88af-7c23f4312ae8 | -6.01762 | -57.69488 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e019816-e253-3c8d-9f13-be1e4af4d21b | -7.10959 | -56.51274 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1fa9bd5-7aae-3864-bdb0-4e01f2d9c681 | -5.29487 | -60.13656 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f33a6a-4bbb-38be-a991-753762f81df3 | -6.44117 | -58.16628 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd4361b7-3718-3ac8-8ba4-e59ac6360111 | -3.61386 | -60.56892 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 270ee121-7c5c-3fc4-88d3-261ded43213d | -3.64493 | -59.54381 | 2026-09-07 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0ffd51b-dde8-3440-9425-37630ad808f5 | -8.75333 | -62.43611 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c62606d6-ab7b-3e3d-837a-ec8b06a52b7b | -5.14398 | -55.96413 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcf106d8-fdda-3202-8e41-05e204bee94f | -5.37032 | -49.05658 | 2026-09-07 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c7bcc79-62a8-3343-b65b-fd3ee90347c4 | -5.36937 | -56.02475 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a46bbd20-7b54-314c-93f2-e332d506b948 | -11.33393 | -45.0832 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b36499c-4047-3c58-a930-6e3bbace23b2 | -9.73583 | -43.41887 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 03b2538d-b2b8-3cba-b1a6-78bf146d7f1a | -5.30228 | -60.13659 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea5cec04-3474-37cc-807f-1f309997ba65 | -5.14246 | -55.95043 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 058bfb4d-4e82-3d15-9998-298545a808d8 | -8.53033 | -63.87511 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6de527c-7685-31dd-9cbc-2bc385db29a6 | -5.16252 | -55.96704 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d31b6c7-959a-3d83-8118-fb18f9e52b9f | -9.7311 | -43.41081 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e833248c-c518-3bb9-836e-334da5e6c187 | -5.36124 | -56.02789 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eed510c-37da-349e-b8b6-fc32277f1cfb | -5.65061 | -60.23724 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59363f39-d50d-32e0-afb2-dd313712a37d | -9.73252 | -43.3997 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddef11b4-0ecb-3e86-a2f0-1216cb1fbbfd | -8.76886 | -62.42509 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c2c4148-4150-3f87-b20d-865be2d8bd58 | -13.30885 | -45.2312 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 82e1f006-609c-36d7-b18e-3290297f1788 | -13.30924 | -45.22791 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 4520333b-f935-3a81-9b5b-e6f6cfc8bdb4 | -8.76226 | -62.41719 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6038b12c-5c03-3621-b7d6-21812ddf5e61 | -5.30535 | -60.14807 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c16b23c9-80f6-3913-8206-023fa2035f78 | -4.54201 | -55.97751 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 652bb973-6f12-3bcc-92ec-73dd99d3d7ac | -5.36276 | -56.04165 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92f0e9bd-3063-3cfa-85de-a7cc19e17c4a | -9.74251 | -43.41182 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46d9b3ad-d56d-30d3-90a5-355c26eeabd2 | -8.74919 | -62.42848 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ad0524f-e2be-3a60-a6ce-d5850c67a254 | -13.30397 | -45.22718 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b0fa1795-f4cc-3c90-aa3c-f3e646e29955 | -9.74552 | -43.38833 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dcd3438e-119c-398e-a06f-5ce5c54a35a1 | -11.52179 | -49.60968 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 129b37cb-ba2f-38c6-91f4-4edb4fab1201 | -8.76292 | -62.42736 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3778f3b8-fb31-36f7-a48a-3f2b13e08ce7 | -3.38782 | -61.32657 | 2026-09-07 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f1cb9b8-c037-3a6d-b709-823c1fa9009c | -6.50651 | -58.29047 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f68e5f38-23f0-3c52-ab90-0ece6a55633d | -8.503 | -54.65165 | 2026-09-07 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23f93b5f-b4c9-33ca-a039-6b9225508acb | -11.51864 | -49.60429 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c2aac50-59ce-3155-be03-0c4b216f5c90 | -13.31295 | -45.24159 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6e7fdb2f-c17a-3157-8746-df8cb0d308fa | -10.74315 | -45.07612 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd97f92f-8912-350f-85bc-f7fb36b91742 | -11.33354 | -45.08622 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb6e981b-18f5-32e4-9852-f8c297b23224 | -8.76636 | -62.42496 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19bc3241-508f-3289-9c6d-957be9cf149a | -7.95154 | -45.24424 | 2026-09-07 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ce1ca21-569d-333b-b87d-79a101edb022 | -11.33746 | -45.09676 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 88c2f74a-62e4-3ca3-b75e-c44fd483687a | -5.28379 | -60.12786 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f45840e5-1a19-35ea-af44-57e5de6938eb | -5.15139 | -55.96532 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea486288-cb9b-36e6-87ce-2abaac09a689 | -12.85242 | -44.38706 | 2026-09-07 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| baeb0e87-05f8-3f55-8978-e345ea6487c5 | -6.51071 | -58.29109 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de594777-d0d2-3433-afb7-ec3205e3f0ba | -13.30963 | -45.22462 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e5a19ca5-02ff-3294-82de-886308f87100 | -6.12962 | -57.74751 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb096c41-bc51-3381-9f69-206d58828342 | -8.50241 | -54.6553 | 2026-09-07 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3350dcdf-7616-32f4-ac93-abfaf4a9e060 | -6.00425 | -57.69995 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f39be8b6-8c6a-3156-b942-2350422a581f | -4.47839 | -55.08232 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aa7a291-7c4d-39e6-951d-83f2329f3a5b | -6.44308 | -58.15501 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b106e67e-4510-31f6-a5f0-51d8b96eb3e1 | -6.13485 | -57.74113 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04f841a0-3176-3da2-9532-6e2842af6827 | -6.05758 | -57.80228 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bef9e699-0bae-36f3-a6a6-72b68ef7b8d6 | -5.99553 | -57.7021 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d6f53509-bd85-3606-ab2c-7417ad777865 | -5.853 | -52.05493 | 2026-09-07 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1fd73cb-bd7b-3e27-a889-95c7d4064f5c | -3.61473 | -60.57587 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81806080-9865-3ab4-a35d-868f61362f66 | -13.29852 | -45.23315 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 6363be8d-0340-36a3-9668-bf6656ffbd42 | -11.50815 | -49.62241 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3eaa5955-ca77-370e-9b0c-89d1ec490083 | -13.30502 | -45.22412 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 24f39b8d-21eb-396a-8e99-2b72c085303e | -8.75824 | -62.42294 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4990ad6c-1611-3505-a2b2-8a8bb197805a | -5.84798 | -52.04346 | 2026-09-07 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf5329ff-31d3-3265-a04c-987de5643afd | -5.16164 | -56.1816 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3356757-00a0-3ebb-a320-953b239d49dc | -4.97414 | -56.28796 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8d91be9-d06e-371b-8a3e-08f8322c9949 | -6.48523 | -57.88083 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3cba8bf-16f7-3bee-bd9b-5cdd30f0eea6 | -10.74191 | -45.08538 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| be0b0295-a0a8-39f2-9987-61b6278f3544 | -4.50697 | -55.71548 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01ca3e93-3a37-3592-add8-7951df016b4e | -5.14914 | -55.95599 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c70f9e8-680a-33e9-afbc-fcdb4960a3ac | -8.7551 | -62.43959 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75fb608e-dce8-3053-a00c-fdeb9e52cbe0 | -9.72972 | -43.42159 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a025feb-7805-3072-bf65-6249c2337d4b | -8.69309 | -62.46338 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 871f3f14-4a03-38db-af34-d5933cef3897 | -4.46573 | -55.09264 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74d4880b-7b20-32bc-8bc3-7287382cd852 | -6.87344 | -55.59849 | 2026-09-07 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6c45036-001f-3347-9494-c6ca57872bdd | -9.73305 | -43.39555 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5c251a3-35f8-38d2-996f-a355cdd1f190 | -5.25401 | -59.98195 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf09ad78-a565-3349-b4da-97aa30663c2c | -9.52509 | -41.98967 | 2026-09-07 05:04:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1876a617-d8f3-327d-9de2-ac13fd8538a7 | -6.06291 | -57.79563 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab5a04b3-150e-343b-b8c9-91d7b7832608 | -8.73075 | -62.43892 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1429b01-aa58-3b03-9b06-cd9e7f169a27 | -9.74871 | -43.40844 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 59f72150-8517-35aa-a51a-3b2d53abdcc8 | -8.75886 | -62.4196 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9905992e-1aa2-34b8-864c-5c500ef0d4c3 | -5.35899 | -56.01851 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e097c6bf-392b-325f-857e-8ae9e3bb4d2d | -5.99789 | -57.68795 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be223b06-374f-3e3b-b90d-47b0e1402291 | -8.75393 | -62.43277 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19c2b4ec-c236-3269-80d0-3d4ec6aaac59 | -11.50884 | -49.61763 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f1de6534-d152-3eff-972c-7070a0c48eeb | -5.36341 | -56.01477 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42b41d73-3d96-3173-aa88-5e8e8d0d3d96 | -10.73802 | -45.07526 | 2026-09-07 05:04:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf1a2cad-c5fc-36b0-a08a-0cc00f3bd3b8 | -13.31412 | -45.2319 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |


[Clique aqui para ver as próximas entradas](README23.md)
