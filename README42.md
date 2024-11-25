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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b666e9e-931c-3903-a551-507d83d1e392 | -1.72473 | -53.24987 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5585777b-414c-39bf-8e9e-693427ce1605 | -0.94194 | -53.21551 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c2c235f-091d-3230-b89b-7472619d5dfc | -4.24713 | -47.98865 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e67ea4d-1f95-366e-a4cb-49bdd662cc7e | -3.10489 | -51.50012 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81a94961-1204-310e-bea3-325bb7e99873 | -4.32579 | -46.83252 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9c5a02e-80b8-3530-a1b0-fa2448cf931f | -3.08488 | -51.02457 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61007078-2ed1-3b1c-bdab-232b51d6dee5 | -3.71007 | -52.41503 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 11013bd2-4664-3977-9184-5139634d42df | -3.27282 | -53.82128 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32b10a4d-07e1-3050-bd6a-cb1bf8385dab | -3.34758 | -50.51072 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3850405-d8d3-3b61-a1d4-83cedc05f11d | -1.13052 | -54.17891 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ce5e7e7-bcf0-31ea-8597-37a2be6bb276 | -2.02063 | -51.18281 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8571f49e-d239-3c1d-9309-d9386bcfadf6 | -1.06953 | -53.36967 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6a5a023-9627-361a-9e16-c29289b95967 | -1.66412 | -52.79896 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95a73b37-5d66-3a13-b13a-0b68a869d6e3 | -2.43997 | -53.88977 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a05158b2-2b32-360d-bf7c-971489857338 | -2.45568 | -53.7037 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ff0f381-8dbd-34ab-ba2f-9fc7c41d99d7 | -4.37211 | -48.49903 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa39e41d-bf3f-3d28-8b4a-6ee81a6eab46 | -3.88094 | -51.94291 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64fc7f25-4025-37dd-ae50-ffa27bf31655 | -3.67903 | -54.58651 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03950185-bafa-3044-b3e3-b86720e7d7e8 | 1.36598 | -55.91418 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63c87e5b-b01a-3f90-83bb-c83a874ccf9a | -3.13414 | -52.9831 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11d17237-60aa-3a28-854f-3dcc9b58b4ac | -3.5095 | -53.80194 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdbb9faa-e073-31b2-8538-3ab25e2319b1 | -3.22642 | -53.92417 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1e55899-663f-3ffe-a599-219c1b7c378b | -1.97619 | -56.13998 | 2024-11-25 04:55:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3cd172d4-fb96-302d-8d09-02b8f308b195 | -4.22877 | -53.49032 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ab88a55-1327-34ba-bbec-de3495f45bfc | -1.9357 | -52.3202 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 853fe7bd-c3a9-3090-97fb-a0e7456ad34a | -2.59361 | -54.04991 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c15317e-17c2-3dd9-a27f-e8888276df3d | -2.33408 | -53.87325 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da4bece1-0861-3ea5-a354-0ea181044e1f | -2.60996 | -54.24997 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ad6c861-bb60-338a-bc35-db0829d63326 | -2.63729 | -54.28281 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1883a85-1233-3d15-bd9d-ff0d717e9737 | -2.5865 | -54.22464 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4d565a-354d-372b-909c-193969555708 | -3.50068 | -53.81474 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b5edd0c4-5054-371c-be36-fe8907eb05ff | -2.46397 | -53.69434 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b57debb-155e-3fcf-992e-f31656b32084 | -3.38038 | -54.6823 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6193cce-f780-373c-9280-25d500c4409c | -3.22145 | -53.93409 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23b2411c-147b-3625-9e22-64d8b252367e | -1.55755 | -52.24722 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 382a45ba-178d-30b4-904e-67a137e0e4ed | -2.70075 | -51.99092 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 921e77e5-aede-3abb-ad44-9b2474acaf52 | -2.40383 | -53.85918 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44ec5d6f-803e-392a-b8f0-bc83a1be46e3 | 1.41576 | -55.89308 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f496df2a-5e34-35e0-b657-a8e7b23d9524 | -1.71991 | -52.72346 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e46493d4-50dc-3fad-8614-da6f5b82818d | -3.51619 | -53.82428 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6152478-0c3f-3819-8b34-dd3ef3e94e59 | -2.62523 | -53.97971 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5d7eb49-bafd-36be-915f-e181fddf2f39 | -1.56779 | -52.13801 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62705214-6208-3c3a-8b31-804eb33223c5 | -3.20798 | -51.42059 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d472141e-4970-3d47-944b-801f62fa4150 | -2.85598 | -53.9763 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2e0267-b8f9-324a-8707-3c607ebadd4e | -2.81941 | -54.7161 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce92236d-fae6-3dd5-b35f-872af943370d | -3.56826 | -51.64155 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b753327d-e689-3d7c-892b-4760047251fe | -1.25769 | -51.74781 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb777745-2d3b-30d2-a5e6-b4d5cc88bd11 | -2.53831 | -53.99477 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02db5c27-a08e-3ad7-a23a-15780abe2d4c | -3.26949 | -53.82076 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a91736e-5709-3427-88f1-006f88db06e2 | -0.24237 | -51.61295 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb753108-6988-38d7-b7c4-404ba7e9daca | -2.56857 | -54.05674 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d64dc7cf-771b-3612-9b10-31ffc686e7a8 | -1.47813 | -51.96286 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa1f9ed6-b2c1-3760-b7a5-3973dcf39fc3 | -3.11451 | -54.00626 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15b8d629-8dc7-375a-9296-de3af6d4c72e | -1.73216 | -52.32397 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9680e5a9-5d8d-34d2-a670-257973716f08 | -2.13717 | -51.01647 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ee65521-894f-3de6-931e-4c6dc1aa643b | -1.37275 | -52.00049 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 084a6393-24b2-3c9f-a4a4-240a237477cb | -1.61115 | -52.36241 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 724cb91d-2b10-36c8-b80c-68177f2773fa | -2.459 | -53.70422 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbb1f367-cd23-309a-b9d6-70e422cd8594 | -1.19109 | -53.88428 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcd97a0e-1de8-36a2-973f-49912cac2ab8 | -1.11721 | -53.39127 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6ce8966-5e61-39f8-887c-c5b282e5a8c9 | 0.94802 | -50.74076 | 2024-11-25 04:55:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d42a00d-ead1-3ec9-b06a-17496b35b165 | 0.97294 | -50.12645 | 2024-11-25 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 363a3120-3efd-3df2-9d22-a7700e2dd5bd | -1.24038 | -51.79224 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09a9def7-1f49-3c63-91fa-48a79386b426 | -1.60593 | -52.5849 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2662cb6b-b276-3679-8ec1-f274050e2f3c | -1.31049 | -51.74839 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 307c93cb-36eb-3fff-9339-90b893c96241 | -3.08733 | -54.54525 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d88e669c-616d-3eda-8d95-cb29570bdd87 | -1.63089 | -52.59939 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b4f69dd-48d7-3641-830f-53bf14504827 | 1.50675 | -55.67092 | 2024-11-25 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef4aa070-1826-362f-8345-e0a9bdbad6a6 | -1.52299 | -52.08097 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba68d020-c40b-355f-a281-31b35db778c3 | 1.95125 | -60.85376 | 2024-11-25 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cf14071-599c-3d1d-a9a0-fb77b24b5a05 | -3.24629 | -53.27974 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64641bc9-9c52-3b4a-b0d4-3a7f5179be44 | -3.34478 | -53.21379 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038b9f75-1352-3d46-b035-069aa261bc59 | -2.77088 | -54.0666 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e72f1654-ae44-3f92-80c4-8a9f5e4a2c94 | -2.96073 | -53.93251 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efdcb8a2-e4e4-3ecd-88f9-33c8bae6e1bd | -3.24738 | -53.27285 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23234205-8f79-379a-8382-182df23b108c | -1.19443 | -53.88479 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4005f8e-a6fa-3508-a463-30fb76bdf4e6 | -0.88559 | -51.71977 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f00055b-d38d-376f-bfa8-73c887e55750 | -2.84113 | -54.07038 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d166ef42-7037-391c-a2b8-625e30352e0c | -3.65476 | -50.23025 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 919b1895-44bf-39ae-90b0-28551dad6471 | -1.98874 | -53.29439 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbd0e21b-1e3c-3e63-8723-038faf6ef637 | -1.5188 | -52.62465 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af61ecc7-6fd8-305e-a374-a64f7e5a4d56 | -3.11156 | -53.70765 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb9d3166-1498-3ede-bc37-4fffdb12d8bd | -4.01906 | -48.07796 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a10f1a3-3710-31db-8f2c-4cf4b6fdf71f | -2.20714 | -53.66865 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30896ce-5572-360e-af11-93331b2a3961 | -5.44897 | -46.3416 | 2024-11-25 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5fdedd0-5308-311f-93e1-5b1d57035662 | -3.27004 | -53.8173 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af5272fc-27af-317a-be80-1d28850e999d | -1.06051 | -52.3761 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 020898a3-fa1f-3816-8bc2-cadff2bfd9db | -3.89377 | -52.30528 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95aab25b-4f88-3f07-8c69-bef31432c7ac | -3.6428 | -50.2111 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b224ea37-5926-3229-a1cb-e631bc1c0040 | -3.89754 | -52.12657 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 513cabdf-5956-313c-b2c8-763c75850297 | -0.35902 | -51.97548 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7b056eb-00b8-3796-9d89-32f4b47e8886 | -1.25433 | -51.7473 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3187767a-7685-394c-a687-49aec49a9d26 | -3.47514 | -51.99227 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2979611d-afcf-3215-9264-c635b02b8ca8 | -0.19836 | -51.6425 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55a0e591-f377-3cac-9103-b6df23d8abba | -1.39388 | -52.55572 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4238aa30-a3ad-3624-a5b4-278e5755ba42 | -1.5934 | -52.58316 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a67812bc-7cd4-3646-a22c-5daa5f94bf2b | -0.89621 | -51.7178 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27135db3-e072-3ad8-8f30-c846e7dc9f6c | -4.29565 | -46.90813 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dde05e7f-45ae-3f56-b43e-6959b59a24e3 | 0.95085 | -50.73658 | 2024-11-25 04:55:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b30d1858-eb22-39c4-8dc0-d8fc6b375200 | -2.74246 | -54.02999 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README43.md)
