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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9461a53-7dd7-3a91-8125-dec09841cee1 | -1.5447 | -51.18726 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c262ce42-3ced-3dbb-88da-b49def0ebbd9 | -1.34676 | -51.39283 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad5e3f91-d6f2-3461-91fa-afdddf13073e | -3.52958 | -52.99273 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c95b07c-4fcc-3121-b4b7-c18cf69b0afd | -2.44704 | -53.68459 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2237be41-e5cd-3343-bd80-54324f276367 | -2.95762 | -51.41157 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75e53a0f-fe21-3037-a47e-416206c1f3f5 | -2.06064 | -53.43826 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54f520da-3b2d-3208-bc67-9b1e6b5bd32c | -5.38342 | -45.44884 | 2024-11-20 04:50:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a590608-783d-3e36-b3f9-b870f281f09a | -1.25547 | -51.77775 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b73e0db3-8680-36a7-a19d-c2fa40e5c4a2 | -0.72805 | -52.8798 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a921564-7099-373c-93d3-65258a9f7145 | -1.05413 | -52.49539 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abd3da79-e19c-3991-83e7-9fb5d0bf0580 | -1.5085 | -51.18159 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89dbcc92-0de7-37e9-af40-83677da668d9 | -1.24714 | -51.61725 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 826ff1bf-f15f-39d0-a20c-9055911d2bfc | -1.2488 | -52.03614 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6deb51d5-231f-31bf-9e9f-e0744869779f | -2.69317 | -46.23867 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0e28b23-9ad4-3980-8f2e-a1597a2d4c5f | -2.25238 | -49.2034 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01102d15-de8b-3a8f-964d-065e333b3bab | -1.20018 | -53.67068 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 475bd5e6-cbad-3570-9394-10077e3f790c | -1.62752 | -52.62083 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbf9933c-4bb9-37a5-a8c2-4fc6db2828e6 | -2.44802 | -48.552 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2b3e985-4cf7-31e6-bdf0-9cc1e8c74152 | -1.3781 | -51.55632 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36fe4d0a-9335-3430-8085-19498589d873 | -0.81581 | -52.48009 | 2024-11-20 04:50:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 214537cc-1f9e-3ab0-aa47-1b4e4a37554d | -1.61225 | -52.41194 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8bd500b-8dc8-34e2-b6ab-5999eb6aa421 | -1.39268 | -52.4315 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed69a154-d4c7-399c-8f6b-acf38330e85e | -2.60507 | -48.21082 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec141c73-c33e-3a83-a43b-00d72a048d0c | -1.6703 | -50.17559 | 2024-11-20 04:50:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ec58394-1154-313e-9e93-69264cd83b17 | -1.24436 | -51.61329 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 478e8f34-9fab-3571-8c52-3646af12a23e | -2.82495 | -54.09377 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fc27162c-8815-30ef-b54d-f9763d9f0c52 | -3.73032 | -47.36967 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 966b0bee-e967-3efa-b935-4070cce7e246 | -2.64129 | -46.20903 | 2024-11-20 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 177241a9-cce1-32c1-8da1-3a742850b69d | -2.62324 | -51.79755 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64753a22-11b5-3411-b424-d489f9c9933c | -1.21709 | -51.74343 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a5d1570-eeae-358e-86d7-df519b626d7b | -2.73349 | -49.33666 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e9bbd2d-bd9f-3589-a6fc-8baa0fd134bf | -4.24817 | -49.18762 | 2024-11-20 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1bf9624-fa2b-3728-b1c6-ff15d0d16ec7 | -1.8899 | -52.6216 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fba52b2c-c381-38d6-88c3-43a4d1b5054c | -2.45196 | -49.15023 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 616a2b8e-99e4-3d10-8fc5-f633313ca9c0 | -3.38729 | -53.27137 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d216d0d6-d1e1-30fa-bd0a-ce5af6ebc747 | -0.92752 | -51.64486 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9efecb15-978e-3a16-aa2d-2ae83462fc1e | -2.89417 | -53.05121 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd16ecfc-dccf-3d40-9a39-445421db83c5 | -1.70881 | -52.4845 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3fa4163-6a5e-3972-94fb-fe60b0c5e1b2 | -1.45947 | -51.98688 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64625b22-7be7-320f-a288-3e44724b2f3e | -2.66044 | -48.48084 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bef513f-0d97-3790-82f0-370010487bd0 | -1.48846 | -51.13612 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfa11ac1-53f5-3385-a5eb-d5e97f5bbbb9 | -1.04407 | -51.74499 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74a05f59-a159-3b17-823d-5de96098952f | -3.23337 | -48.8751 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1799c2d-9b4e-37f1-b3ec-e25ef94afb86 | -3.77106 | -51.68381 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16caee78-47f1-3018-ae61-a247eb07a7ae | -3.04295 | -52.43799 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b06eca4-1017-3472-8416-913d1ca7a6c4 | -3.3839 | -53.27084 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c1d705a-36b0-3e1f-ab6d-c92d9d5bc14e | -2.05779 | -53.43401 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85bc4157-ac1e-383d-863b-b63ed2d437d1 | -2.96094 | -51.41209 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6a11cdc-53ad-3fdc-9cd1-70933682d6e0 | -1.74853 | -50.47649 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 454d29f8-a2d9-3d63-9382-dde0f9be0f37 | -3.28821 | -53.84386 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc19fe8e-da7a-39fb-9a15-27ceab069295 | -2.07706 | -48.52 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9108a4c0-3efe-3ebb-82fc-eb5558c984a1 | -1.81871 | -52.69398 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf947f4c-6526-3244-aef3-7fc53229dde0 | -2.28449 | -50.58841 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbdc2134-485e-3f2e-888b-a5e3d54000c6 | -5.69395 | -45.84153 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbcf538b-284f-350f-85d3-906105036ab6 | -2.90936 | -53.06454 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ef1df9df-1442-3308-bebe-ad3c302633c3 | -1.30581 | -52.40368 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 20d085bb-2bec-3056-8966-35bad4469c54 | -2.79432 | -54.01059 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 056af8a8-22b1-39cd-bb17-fb44909cf773 | -3.28481 | -53.82851 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ba04bdf1-7eff-3131-bf75-769212e431c4 | -2.7427 | -54.10947 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f774ea58-4c15-321b-a503-9c1762cf8515 | -4.33365 | -50.42794 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb7325b8-c456-3503-bb60-3bc43ed32884 | -1.64157 | -52.6045 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7685dbc-f99f-3669-a1f9-c11766b4ad06 | -0.90856 | -51.72703 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd49bfef-6077-3598-b88f-73f54b670a74 | -2.62602 | -51.80151 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ceab5eeb-5123-3ed7-9014-9722969196ee | -1.71216 | -52.48502 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec342836-6735-36d3-b653-07893f0867cc | -2.51972 | -44.99308 | 2024-11-20 04:50:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ea636b2-2973-3da7-9a60-6671395ba7f9 | -2.62047 | -51.79358 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ce58380-d674-32e6-9eef-02e825bfb3b3 | -5.6904 | -47.66102 | 2024-11-20 04:50:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7995f1a-83e1-3de7-bd7c-0a36575364ce | -4.65241 | -49.02114 | 2024-11-20 04:50:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7207c76c-97dc-3f4e-bfe9-c78b4f90a38f | -6.18516 | -47.08116 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81177b3e-e845-3ab3-b147-a068a1833f51 | -1.95763 | -53.32059 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e52196b2-9a89-315f-8392-e592484a453c | -2.59573 | -54.01199 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddd3e3c2-f13c-3bca-9164-d660cce03df8 | -3.06333 | -53.28382 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af98b268-859b-34c1-9a1f-9dd70863f169 | -1.51409 | -55.4835 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b839a292-6f2b-389d-84aa-bf92fec414dd | -2.31245 | -46.85054 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07dccdda-1682-31f3-af18-af2856035752 | -2.99426 | -51.45969 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93aa52f4-db37-39e9-b7c4-72484643e8df | -1.25433 | -51.76341 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1943abff-dcda-3b00-a29c-f4108fbfd9a3 | -3.46289 | -48.25271 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10bd1db6-06a7-3f73-8ab3-888a5805e1d8 | -1.41572 | -52.0477 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 554766ea-b960-36ab-9f45-1e4b46041bad | -1.1358 | -51.68138 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e7812c4-72a1-31ce-8fa6-1526f4612477 | -3.3661 | -54.09678 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5dabfb9-2bf4-30af-b0aa-810f2f5f9725 | -3.75372 | -51.34476 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7905a5f4-3cc1-3955-b77b-730d51780146 | -1.27234 | -52.1255 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b92bbbf-e096-333e-bfaa-858fb669c64d | -3.75994 | -52.05677 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e5001b9-89bb-365d-b693-59c39d9cefff | -1.54138 | -51.18675 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9dd24b4-16c0-346f-9630-c3bea7c4eaae | -4.44156 | -46.58865 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5bb62dcb-e6b5-3b86-b111-701e62b26eb9 | -0.82176 | -52.83802 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 354bf020-8856-3598-94f4-c4c8fe210c99 | -3.36183 | -45.10748 | 2024-11-20 04:50:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a53ee29-33d8-3317-8463-b1a051266e88 | -9.99377 | -55.65311 | 2024-11-20 04:53:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f2c85ae-043a-3b0f-b9bf-f323591050c9 | -12.03841 | -54.64558 | 2024-11-20 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1f238a3-4d4d-3ee9-92f4-a3c3b38121ce | -10.62738 | -54.61049 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d7c0dad-bf02-34b2-9a6b-a29645587d22 | -11.43362 | -44.68879 | 2024-11-20 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a1af42e-c711-30b3-b381-71e7d7f681e6 | -17.6039 | -57.40372 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 811762eb-0f2b-3c01-bee7-bf3e7b9ecff9 | -11.03918 | -44.56993 | 2024-11-20 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 980c0a9b-5bd0-3dd7-b280-8582fa13a6e8 | -10.42207 | -44.48687 | 2024-11-20 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 010a78e6-3acb-35f1-8575-3c3d70e37f83 | -11.06062 | -41.62223 | 2024-11-20 04:53:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3504c006-48ea-3ccc-b5fd-609da8103f90 | -12.58359 | -52.49155 | 2024-11-20 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a747693-cee6-3a4d-9454-4ecb6d6d98f7 | -11.10375 | -54.62872 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3ac58283-1da0-3289-9f38-6e3e771e49e7 | -20.0538 | -57.20748 | 2024-11-20 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09d40122-c057-3202-8c65-1cbad4acee63 | -17.55906 | -57.51954 | 2024-11-20 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b1be2be9-0bbc-3445-ad42-169f329192d0 | -11.09761 | -54.62404 | 2024-11-20 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README62.md)
