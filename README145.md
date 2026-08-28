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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e0ca10d-02b3-354c-948c-2a284a9e7f2c | -7.58125 | -61.31113 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bf194a3e-9ff4-38d5-88d2-bb2e990b1090 | -7.7548 | -61.10023 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3427c907-c379-3f20-a699-b25721eaa56b | -8.8772 | -71.27007 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 17.0 |
| dc7f9567-a11d-33ca-8745-12ea7dc1708c | -1.82089 | -55.70511 | 2026-08-28 17:47:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4668fc79-85ce-3893-853d-7faf4b6ae469 | -8.78295 | -70.82984 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 8fb549da-0029-30c0-9320-c8c5a56d7cc4 | -9.01397 | -70.71358 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 5a142bbe-07d9-38bc-8355-5458e60de27e | -6.73689 | -58.70589 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f781820d-53cb-388d-bc6e-5c2f6db72b06 | -6.99001 | -60.66145 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 614b8bf5-00ae-3c5d-9816-fad958126878 | -6.7965 | -59.60319 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b36da270-39df-3f98-aa51-bcae44a19d6a | -6.9481 | -59.48108 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 50c63c65-5ce4-373c-8a7b-eaa04a25afee | -7.4578 | -72.67703 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7ca515d-5425-3113-bddf-74e4a303e776 | -7.2289 | -72.43594 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5e9bd937-36d4-3ee4-9ad1-50b6f3ee782d | -7.21902 | -60.62186 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d44d64a5-9109-3124-9af5-9045bab4e97c | -8.64337 | -66.54102 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2a5ecfab-a0f7-373f-ba93-9791f5f80fa2 | -6.55548 | -56.55639 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| b4108506-a0f6-32a8-89ae-7bc4428ff36e | -8.81692 | -68.99471 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9ff7cb2f-f270-3dbf-a940-e56adae1c314 | -8.37021 | -72.69828 | 2026-08-28 17:47:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9bc61e3-929b-3d71-ad64-e9637f91b948 | -8.89922 | -70.69225 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 25cb3f88-6b9e-38b0-9430-af77c21f60ea | -7.12339 | -56.54777 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 96b0d3f8-8e6e-3e49-94e2-5eeb12cb52a5 | -7.52596 | -61.38483 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8f21e6af-26dc-3cdb-aa2e-b6c699123a0e | -9.04065 | -70.57744 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 40f6510c-745e-3185-a95e-04a3662fd41c | -6.83681 | -59.73742 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1708776f-20fb-3b1c-9095-66dc73e69b45 | -4.30765 | -59.46645 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f2eff8b0-36c8-330d-a2a0-f07714a2e778 | -5.88545 | -57.7715 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| f9836491-16ec-3135-906d-0701825539d8 | -5.91996 | -61.40169 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47baa0dc-a7ec-3452-ae57-efd824c222ab | -8.79496 | -62.48111 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fe048913-3861-3de4-b7aa-096819bc5397 | -8.27972 | -72.82198 | 2026-08-28 17:47:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5229b07d-af54-3b9e-9a40-67cf7f36a1e2 | -8.24771 | -70.09532 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 241.5 |
| 25e43cbd-66be-3136-ad9e-54a2be7d88e7 | -3.41322 | -61.32875 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fc347ae2-ebb1-3fba-b90a-dd3c603b875f | -6.54412 | -58.58885 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3d478414-efef-35f4-b3ab-c1bbe0b7291d | -6.96259 | -59.04877 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7b98212d-f575-3f72-8d28-ef21cf1acf24 | -8.87677 | -69.10635 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9e0dda00-4963-3429-a0b5-d5d05672848d | -8.37819 | -70.84382 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 148.9 |
| da924c26-3670-3334-b351-820ec70de1a9 | -6.9931 | -59.30591 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c37c3a06-ab82-3382-b97d-1f4718db58f1 | -6.8454 | -59.95732 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f1706f0-27d2-395e-97e0-37e71a28539c | -6.37526 | -54.95463 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2533e4b9-0a9d-347b-bd1f-04f76bd59c75 | -8.44844 | -70.70197 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cad2de80-043a-3000-97af-1ef842540003 | -8.55166 | -70.59972 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bfeb9ca2-76b2-34e4-a84c-2f586cda39da | -6.16312 | -53.5029 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 10cebc2d-8827-3e0e-b273-dc8869a4dd39 | -9.24689 | -71.89466 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 929e085c-f8bf-3016-a158-ca1d99701a03 | -8.32339 | -70.07118 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9d9d3b7e-d0f8-32da-8f77-c147c1c3d3bb | -4.29728 | -59.46986 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8ea7817f-3f83-3b89-8df8-8eec8acbb761 | -7.00081 | -59.52324 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| edc62192-effd-3c49-95bb-9b967e2d1ce2 | -9.21581 | -71.90549 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5c487378-9955-3f7a-995b-9da33ef6ce98 | -7.22795 | -73.10461 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 2e1c55c2-7c93-3b94-ba43-4d94ec40254e | -6.94153 | -58.95669 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 56e836be-77d8-354f-87f0-9cfbfc0fe8e9 | -7.00523 | -59.52699 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6b8db89c-7638-3702-b5ff-6b3d3d6c9684 | -9.00701 | -70.73678 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 31de12cc-9d98-36cb-b5c9-904fdf77d386 | -7.51401 | -61.37534 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 936aac2a-d2c9-36c4-ad61-8c8a4094a86b | -7.00897 | -59.52647 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6caf0295-2c09-3394-8395-56111db36032 | -9.20746 | -65.7858 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93177a99-d105-3ae0-a88f-54d1b3c1179e | -9.03232 | -69.58173 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 531394f3-a15a-325d-b9bf-890bcb54199d | -8.11724 | -71.30178 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bb85db36-427b-3fbd-b387-a8800078b7d7 | -4.46703 | -55.66716 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 240f8951-a7c0-3de1-9504-70874564e5ed | -7.58474 | -61.33333 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7068fa7c-591c-3ad4-91a3-e0995a32dcfb | -8.94604 | -70.708 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 38.7 |
| ced76881-53ae-37fe-bb7c-5fa430e7d29e | -9.18044 | -72.67669 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fabfa6fc-d968-3b36-8fed-d179968cf087 | -5.97205 | -57.71711 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f091f6d6-3963-3ea3-9f17-fa5ad3fe7fb7 | -8.63659 | -66.54652 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f3a14472-953b-39da-8bd1-3da1ac3dd2d8 | -6.17031 | -53.47806 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 7625f938-cddf-3125-a5a7-176147c40795 | -6.12651 | -57.86415 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1e4aac54-7041-3f32-b596-345411e600b5 | -6.08271 | -63.43034 | 2026-08-28 17:47:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29ee4f2e-7278-3eea-a9be-67c1db1d1d32 | -7.74331 | -61.09433 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 798ddb7d-d4f9-3635-bea3-de4ec4219e96 | -3.41259 | -61.32476 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d4c87f8e-9ea8-37ae-baa9-4d22366c2897 | -6.93521 | -58.95505 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 50bb5708-c612-3a74-b9da-38ea279b511a | -7.92769 | -61.30899 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7a24cf8-18cc-396a-ab4f-8dcfa9513705 | -7.59333 | -63.36722 | 2026-08-28 17:47:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| af458b2c-b6f9-3420-b116-81d098938575 | -8.68671 | -70.69383 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 86fc375b-502e-39ad-bcfd-be0983050c26 | -6.93229 | -69.79436 | 2026-08-28 17:47:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2ba96d73-97c4-3706-af76-474880883f5c | -9.03064 | -71.42633 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ae70086f-8cc5-39ab-8c89-9e7c80151548 | -6.57977 | -55.44514 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8b32861e-5f8c-3fec-b5d3-5121c4a86259 | -5.15367 | -59.79882 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6d493539-52c2-3d7b-9b5e-51c78a4ef341 | -6.11834 | -57.68553 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 785ab379-7b87-37a1-9e63-8c90e382a655 | -6.21379 | -55.47878 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 470ae55b-0310-3c50-ab54-e41aa23b8228 | -9.37774 | -72.71715 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 61d647fa-bff1-320e-8bf8-0dc0d7107676 | -7.07238 | -59.21928 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c092a9f-ca75-3a85-b33c-445b40361bf6 | -3.22895 | -61.23704 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d2e903d-d8bc-3698-bd77-cd0b77b83e48 | -6.00082 | -57.68361 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a6c385c6-62d9-30b0-bd83-247cc316be3b | -6.27709 | -53.13765 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4133cc5a-eeb8-30f6-abed-9defc47a194f | -3.72887 | -60.60516 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d6b102f-c43b-3697-803d-d897c08d5a22 | -6.80022 | -59.60263 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f55831f3-746c-3ad4-93ab-fe0cc839cacc | -8.8376 | -62.3162 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b4bf8725-1ab1-3939-ad52-d60028e13151 | -4.05607 | -60.64044 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6215c4f4-ff86-362f-8696-ef6295dede4e | -6.91276 | -59.62721 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2a85ceef-f477-3871-b620-ae3bf68f3635 | -8.84656 | -70.84212 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 67719cb2-6df8-3d4d-b7d1-58d0fd56c58e | -6.16365 | -61.77095 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 597d3112-fec7-3daa-bdbd-99fc854041fe | -5.77167 | -57.55637 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6e72f5d6-89a8-3c40-8067-dc429ec22e02 | -8.36054 | -70.74693 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 66.8 |
| aa7b4bb2-d114-3095-9e7a-73db4cbd4342 | -7.00934 | -59.57662 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 25b810e3-3bed-3882-aeca-6407639be23f | -4.16221 | -60.69788 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b10c7304-163c-3296-b54d-4c81180d5e35 | -6.93056 | -58.95088 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 87454bb1-7ba1-3d4d-8df6-daffe67e08fe | -5.77235 | -57.56046 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7a257885-d433-3d36-b29f-0f67edb67f35 | -9.04867 | -68.11893 | 2026-08-28 17:47:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9ee6d335-960a-33a6-b6ed-fbd891e5bf21 | -8.68102 | -62.95533 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d2de9678-59e2-3e07-bcac-df4e07455694 | -7.00863 | -59.57212 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8f19685d-7f45-3b95-8114-a261c2c5bafd | -4.92592 | -55.7662 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b78d96de-9f52-3a78-847d-f5f27a20c0de | -3.22832 | -61.23299 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6231abca-83a2-340d-8e3f-94d0b7f19ccb | -5.81075 | -57.63334 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cedc1659-3b41-35f9-be50-4232a864b8db | -7.74198 | -61.06372 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 12a09f27-e2d1-3335-83cd-d3652a16055b | -6.93827 | -58.94968 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |


[Clique aqui para ver as próximas entradas](README146.md)
