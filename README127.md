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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0290f1e-f367-3de0-a2c6-a686f5c4acc9 | -2.74352 | -54.12288 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 931ca52b-3823-37ec-8379-127c9dc918bd | 0.99754 | -50.15972 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b698cca-f7c9-3b4f-9e21-ae9648408227 | -1.21312 | -54.01627 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10a6237c-699c-37cd-8d4e-e715dad0a7c5 | -1.4711 | -54.5449 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a51dce-7c7b-35eb-8b3c-c874108b2f05 | 0.5002 | -50.78037 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f6b440d-e749-375d-9ca2-973145fdf4bf | -2.05829 | -54.30285 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5abaf773-b833-3bdc-a8ab-2b946c297157 | -2.04422 | -56.38358 | 2026-10-09 05:01:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1976d1bb-0370-3f3a-b33b-da3e846becd0 | -1.28467 | -55.41597 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 353bfaf1-7999-370f-969c-8bb6e6e1d1ee | -2.48458 | -45.6737 | 2026-10-09 05:01:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac635f29-3ee1-3342-8e65-d8c725e76ffc | -1.11316 | -54.16958 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a0582d2f-1637-3979-b978-73f4aa85a9ac | -1.62856 | -55.12684 | 2026-10-09 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be5e4fab-d23f-3296-afaa-85bd050f2a56 | -1.12744 | -57.27952 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fab975fe-2de2-3e71-bf6e-3cc60be21977 | -3.29075 | -49.5121 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bd1dce2-8652-3b29-81fe-de3960175abd | -2.84382 | -54.12591 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 600dad0b-f786-3a1d-b64b-a9fe07425814 | -1.53406 | -54.54993 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58341461-e736-387d-a74c-431c88fd6548 | -1.30446 | -54.1884 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ee9f5a5-9936-3bd5-b1b4-61c40b506c3e | -2.73712 | -54.11787 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ed34639-4991-3e42-b1e2-99a0f23ef453 | -1.70766 | -55.43396 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ca65b17-03e3-31da-a224-e25517055fa9 | 0.45289 | -60.5406 | 2026-10-09 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92d2b9c9-b5f3-397b-9f38-dcd1bd953b45 | -2.23456 | -51.92553 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8516a54-182d-3b75-8fe9-b28cf6252adf | -1.38585 | -55.19793 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c4914a2-719a-3c21-9fe6-c0fb43481ece | 1.68926 | -55.61575 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 690a576c-5712-3f36-91d8-244abd019cc4 | -3.27067 | -50.39186 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5415518-9694-37bd-b2ff-f213bf4480cf | -4.07835 | -44.11365 | 2026-10-09 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1f01ee1-de7e-3b16-8b7b-531054f1838e | -3.11676 | -45.61813 | 2026-10-09 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ce840a7-4145-3cc2-ae5c-f278459bc858 | 1.82489 | -55.5308 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2988ef0-b89f-342d-bf44-24719b87f9a2 | -2.43513 | -55.97052 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72cb4160-b118-3c01-bbe3-82f9dbbb949b | -3.27727 | -50.03568 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2d85cd9-260b-34a1-8db8-d8a5eab6e8a6 | -2.74228 | -54.13064 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e384eec-b630-31a4-9fea-8484b72bc785 | -2.84856 | -54.11873 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a9fee42-ea25-369c-afc9-67c8de7734d6 | -1.32802 | -52.44868 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e892211-d88d-38d4-a71e-21e7b0e1e82f | -1.28541 | -55.42269 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af024db-c046-3525-a65a-8255ae23bd5c | -2.51588 | -56.26298 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b67d9d6a-b665-332a-be4d-eb05b8c84e9e | -2.33942 | -48.86474 | 2026-10-09 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e2c3ee-1c6f-3635-b7fa-73c036b3c710 | -2.751 | -49.52547 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a932bb3-250f-3b7b-9b91-6f17d8efd454 | -2.77959 | -54.07702 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5c1e647-9186-3c40-b32b-d5c37ae59484 | -2.82816 | -54.11151 | 2026-10-09 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf10f20d-2fdd-3249-ba2b-9b255fa38a7f | -1.53768 | -54.55051 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa973ae7-ddba-376e-a1ce-1e0d0a93068f | -3.26982 | -50.39211 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 663f2192-bb52-314d-bc01-a07ab514eb6c | -1.39522 | -53.23137 | 2026-10-09 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c476179-9e47-38cd-ab9f-515cc7e2d0bf | -3.34747 | -50.41121 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e03added-6135-3bab-b59a-89720ae7362d | -1.79409 | -47.84885 | 2026-10-09 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acf97729-f8b3-3ed4-8980-1a4ef9fc20cc | 3.33838 | -51.61484 | 2026-10-09 05:01:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 546df382-3bc2-3805-a24d-617e002e8d3e | -2.50056 | -56.13295 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d0b26ee-ee34-301d-83b5-713c609d4632 | -3.17277 | -50.45787 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aceb4e7-3e4f-36da-b3e7-750ba5ca349c | -3.19308 | -50.54887 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aaa1b0b-d850-3776-a798-ce2c9fbb21a3 | -2.75239 | -54.11237 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f7f6e334-704b-38af-a7cb-f246970224f9 | -1.37399 | -54.64117 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b16645c6-9e82-39da-9723-0c8bea3fe944 | -3.37335 | -50.47002 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e133feb2-1c7b-309c-b19f-b87854ab09a1 | -3.35474 | -50.47489 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9210c16a-b44e-3e44-9a4b-c1bd7bcf75cc | -1.3354 | -56.4044 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27f51436-666c-3d56-b377-d62c08f93b93 | 1.05561 | -50.03624 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae1c92b4-59ae-3c81-be4f-f0209100ecf2 | -2.47491 | -56.07162 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d4b4d22a-9e4c-3202-9c44-e36ad1f20519 | -3.27888 | -50.09234 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13547677-a76b-3980-bbf3-eccc2c2deeb2 | -2.86806 | -40.00949 | 2026-10-09 05:01:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6c8372b8-c67b-312e-9068-7e32b42786b2 | -2.4641 | -56.06166 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f586c7de-83af-3c79-bfcd-5097a7ace788 | -2.41058 | -56.53297 | 2026-10-09 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2005d43b-96d3-3bb5-8d61-2deacc12cb7f | -3.3582 | -50.40919 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4deb88c-5d2d-3622-b98d-6429d4695c3c | -3.34465 | -50.40707 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab7347e4-e2f0-3093-a679-e1d6f99bd77d | -3.36322 | -50.49049 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bff00748-f011-3ff8-949f-b55be3e8d474 | -3.26925 | -50.39569 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8861d276-1efe-3c81-a92d-f06d9d587f1b | -3.20264 | -50.55402 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4625ab5e-3e57-3537-a50c-61b862222b67 | 0.94969 | -50.20288 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa21b6d-82f0-3780-814b-9a1dd3c55cd1 | -1.47917 | -55.86771 | 2026-10-09 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf39d458-9ca3-376d-b092-ca5767522377 | -2.33046 | -48.48965 | 2026-10-09 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3761d356-7f2c-3946-a6d2-a99138985be0 | -2.49844 | -56.07216 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b6ce4fef-eebd-30fe-a623-114419d05baf | -1.5241 | -54.5654 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da39cfd0-18bc-383e-a9c8-aa9e496212b2 | -2.46788 | -56.06543 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d211275-a273-3518-a3df-e7afff4c33f5 | 2.41837 | -50.81802 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f53cc2c5-7904-3de7-a477-c39d3c1ef260 | -2.76353 | -54.11019 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eff0911-5f58-3961-88d1-745aa408b86e | -2.50038 | -56.18362 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69092c1b-41da-3a09-95c4-88bf85d1ff08 | -2.05473 | -54.30228 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3888d10-4997-3d4c-9058-712133112537 | -3.21051 | -50.54794 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69376405-b822-3a70-b292-3ff6bb46f711 | -3.25003 | -50.40745 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf5f8647-e666-3cbe-a170-cec568709c60 | -2.57491 | -54.96431 | 2026-10-09 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62be1b4a-312c-3ed8-baab-50a14cd22343 | -2.07695 | -46.57589 | 2026-10-09 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa2dd259-7303-35d6-bb13-141dcbd715db | -1.52316 | -54.82584 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9144863f-7174-3a80-a34f-4f0d4384c558 | 2.41336 | -50.82943 | 2026-10-09 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0e07f89-08ea-3a47-863f-358eded483ec | -2.7898 | -51.40732 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95bad7d5-9690-3188-867c-058cfb468b41 | -2.75013 | -54.03676 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d30a7ec-d791-323a-aa90-948871c77b95 | -3.2032 | -50.55045 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d002a27e-1794-3968-8802-eff4cb63a9ec | -3.26621 | -49.5318 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66575452-fc7c-3c2e-97f7-d0365d915f07 | -1.54359 | -54.55994 | 2026-10-09 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a0a7013-0526-3190-ba2c-53e370a07ece | -3.29136 | -49.50829 | 2026-10-09 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec28205b-9203-37ad-89a0-23e6b1adda03 | -2.96056 | -48.74818 | 2026-10-09 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6bb2fe8-3c74-36ec-bd37-7bc92e4bc87d | -2.47419 | -56.07336 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 384d5a68-491d-312e-8cc4-b3ccf04f499d | -3.2023 | -50.82944 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d7e5272-8146-3f6c-be70-8432ea5ed397 | -3.17164 | -50.44296 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c98aa279-662a-3b37-8b4c-bf3ba99476e0 | 0.18925 | -51.35618 | 2026-10-09 05:01:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 832b12e3-a87b-3a42-bf9a-ce2f8e7e747d | -3.36602 | -50.4693 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97750e2d-5033-3683-91b0-7d85d4729093 | -1.10473 | -54.17645 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f4b42ee-4c0f-34bd-b094-30d16390edd5 | 0.70133 | -51.43179 | 2026-10-09 05:01:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11418a08-505c-353d-9353-c7b99e9324a5 | -2.77547 | -54.08032 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce9150d8-b111-3619-8185-ddf02ac6d2af | -2.47183 | -56.09113 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78fe185d-8c0e-3454-8193-a16968a9aafd | -3.52458 | -49.26393 | 2026-10-09 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9efc4da5-3a44-3375-97c7-caba0ca4d5ef | -2.50394 | -56.06301 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3973623f-7bc0-34be-954b-b0dc8876ba52 | -1.28614 | -55.41806 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a4d1d3b-c526-3c84-97c1-e6a87d6e3399 | -3.01476 | -51.01606 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8d801ed-9c3a-35c9-801e-d0791572bb06 | -3.20096 | -50.82584 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 682293b9-c0cc-3319-b3f2-f76791dbc8f7 | -3.1102 | -51.03078 | 2026-10-09 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README128.md)
