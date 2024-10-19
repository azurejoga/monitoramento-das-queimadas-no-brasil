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
| 65362115-c55a-3c98-9cf1-e0d078b99383 | -2.83658 | -51.30785 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cfaa60e2-0620-39c8-9a39-d13a5d7c5c31 | -2.83364 | -51.29925 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f35f16ca-7227-3473-bf07-d8c33cb93a49 | -2.83298 | -51.30324 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 994510c6-95cc-3edd-b84c-eaab26df47fc | -2.82149 | -51.3463 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21674aef-6f3d-30b1-867b-c3737bda6149 | -2.81927 | -51.3386 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c49b6b46-cdeb-3f56-85f9-16a5c010ecc8 | -2.81864 | -51.34259 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdb3b167-45ad-3787-8657-d375bf2918d2 | -2.81801 | -51.34658 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc818ec9-eb4e-3cba-aaae-065968896c3a | -2.81788 | -51.34165 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e1554749-3902-3600-a5f5-5da933cf0da5 | -2.81737 | -51.35061 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30503088-76fc-31f9-9b3b-3edc4c3b187d | -2.81722 | -51.34563 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03970350-4daf-3d40-a9b1-d427d11671d6 | -2.81656 | -51.34964 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2aaaa03f-81f3-31b9-945d-32f0f0f4f226 | -2.81438 | -51.34192 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85c5d3e8-b22c-3379-8e06-a2d5b81ea083 | -2.81374 | -51.34592 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 063c5c65-8dd6-3a22-ad92-05293a51bccb | -2.81311 | -51.34993 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d16a2cb5-afe9-3044-a2d4-12ab71044eab | -2.81296 | -51.34497 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8666e925-d985-3688-a566-064565e9bb01 | -2.81229 | -51.34896 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c38165a3-deb8-318b-809f-b888e3ad35bf | -2.80884 | -51.34925 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 978cd7f7-c25d-36a5-9881-989587350f86 | -2.80803 | -51.34831 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02ea2a52-48af-3308-93ee-04051dd7de1f | -2.80632 | -51.59893 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8fd738a-456a-3679-bc46-4b541af6cda3 | -2.80565 | -51.60302 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06d714cb-9996-37a1-886b-ad09241e2254 | -2.80132 | -51.60231 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c92c304-ea7e-342d-a39d-e5a1de483cfb | -2.79839 | -51.35994 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b91f0dd6-be15-39d8-bd80-30e31b016d7e | -2.79775 | -51.36396 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fe0f8f40-f516-31fc-804e-7ee259be72ad | -2.79412 | -51.35927 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 87b9b271-570c-32ec-a4dd-e1540944ff5e | -2.79348 | -51.36328 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2f81a42e-b355-36c0-a652-99aa9cf78781 | -2.78921 | -51.36261 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ba57395-ac22-3f1a-a368-a5dbfbd37b0c | -2.20302 | -51.38958 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858d49a7-945a-366d-a787-80f968244da1 | -2.74224 | -51.62834 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3f4fe928-d0f7-3f99-b1da-b26543d8cc7e | -2.74157 | -51.63253 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 502ebcaf-bdb6-3019-b736-ec64fe4722f3 | -2.73855 | -51.62348 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44bd143d-0539-32a6-956f-25bb8da8fa85 | -2.73788 | -51.62765 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1b28bc47-81f1-3847-8daf-ea2cca87c8d5 | -2.70589 | -51.34216 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2aad22d7-0eff-36fb-9018-5e0d88c33770 | -2.70509 | -51.3412 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2366de43-1735-3d42-a83b-25a2bb175a00 | -2.62571 | -51.76337 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2fba0098-7507-3926-b3fa-de9ec4b796a4 | -2.62502 | -51.76767 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbc45d04-99b1-32e7-910f-7bf43e6087ef | -2.62131 | -51.76264 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 975b5fcf-d881-3505-ad80-bf275edc602c | -2.5867 | -51.92227 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86a3ffab-f039-3105-ac11-8e5b02ba9cc4 | -2.58224 | -51.92161 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29d44513-53d4-351e-8d25-298b325ea1b7 | -2.57503 | -50.53383 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b4ae931-c83a-3fa0-86e2-5cdb02b15273 | -2.55769 | -50.64188 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9a5a351-4e54-3726-bb11-c721ed56caa9 | -2.55209 | -51.24369 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11a1f018-e412-37d0-a188-716d57d235b3 | -2.55145 | -51.24763 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 547966cf-a042-32e1-a553-d087b19b6d1f | -2.51738 | -51.81708 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7ef6909-e411-3d46-aee6-d0a31b9ed7b7 | -2.51349 | -51.81665 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c2d53e51-71c6-3ade-ab38-f78a1512865b | -2.51295 | -51.81639 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d099468f-7046-3e05-ba3e-7f04a67fa42a | -2.5128 | -51.82096 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c68eeeff-815b-3f15-9d5e-476f927c3b8e | -2.51224 | -51.82069 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 36e0d551-0ac5-38d7-b23a-013b0b27d9d7 | -2.50837 | -51.82027 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba992f9-cf18-32b5-9deb-9c7267247dde | -2.48882 | -50.47266 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f129b05-3ae0-3d05-984e-fdb0d9be7ddb | -2.38362 | -50.47717 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d079ded-8353-33fe-900e-550f8efb8a2a | -2.27926 | -50.55643 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 931632b5-0aa7-3ade-9d8e-253978cefaf3 | -3.4393 | -50.79451 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45710760-dbae-318c-b1f3-b09363337942 | -3.4358 | -50.79028 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f8f4382-fe3f-34d4-b58e-2d4f462525db | -3.43172 | -50.78968 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 116f9bc9-5b23-3185-947b-9a7b6dc68452 | -3.38422 | -50.67223 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28720ee8-4155-34c1-b6ba-470d94163246 | -3.28564 | -50.9458 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 764e5961-10c5-3b0c-a0f2-25ea8bcc1723 | -3.28211 | -50.94147 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dbcadab-e105-3242-9f56-b608842b9892 | -3.24733 | -50.9474 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8231f187-8268-35f8-8551-7393ea35323f | -3.24321 | -50.94674 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6459ac11-6241-35db-89b6-9f0cf9e650fd | -3.2384 | -50.84768 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58b27aef-7756-3325-8df8-33bd94ced510 | -3.23779 | -50.85134 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc64e66f-e71a-3e61-ab0d-420c892bcefd | -3.20654 | -51.04073 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5bcb491-f861-3afa-b6f9-c96cabdeabf0 | -3.1858 | -51.29734 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 97f6ddb8-d5e9-3937-95f5-9ebab27a94e5 | -3.16757 | -51.25033 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0655705-554c-36eb-96c8-4fb564332537 | -3.15728 | -51.25726 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50a97050-21d0-34c1-a98b-07adb48b0f28 | -3.153 | -51.31206 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29f997f3-6de8-3485-a01f-2c6bd75de7ee | -3.15068 | -51.35226 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd7292ee-1c4c-3f68-aab8-373cec807f7e | -3.14996 | -51.14112 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d313171-bd8b-3b9c-be5b-cafa1ca2ddb4 | -3.14644 | -51.35156 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a22bea3-897a-30ab-82f5-c812fea38368 | -3.14538 | -51.49018 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ab3b68-58c4-3761-8b5e-a7f5747e1e46 | -3.14469 | -51.49436 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b21099d-aa1f-3404-b645-a9caabdc4289 | -3.10244 | -51.32898 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b051a86f-3c90-3bcc-82d0-9e2331bf5e07 | -3.09367 | -51.22296 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e4aad6a-fd70-33a1-8a38-e76f489750b7 | -3.08714 | -51.21012 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd179f0b-cf38-3dc0-a120-44cb456fb91f | -3.08167 | -51.2171 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d01634e5-b50c-347e-b86b-1361cb9be3c8 | -3.07654 | -51.24837 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06712cb4-c39d-339d-a817-4aba5d0bccfa | -3.06831 | -51.05408 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dacd457f-709d-309c-bd87-a956d338aca0 | -3.06413 | -51.05347 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ec43380-39f7-3c26-aaa5-92332b8177ef | -3.05287 | -51.04384 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bb7a155-985a-3125-938b-31ca673cbf14 | -3.05226 | -51.04763 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6999d332-ba3c-3d82-be7e-f03012fbc45d | -3.05165 | -51.05141 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9e8983d-fe7d-38b6-bfa7-f08ec1fba5e8 | -3.05009 | -50.98162 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f1c8821-40a8-3ccf-9ede-f37439e676c5 | -3.04949 | -50.98536 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80bb2e40-b0d4-3d5d-9ba8-04102b084fd2 | -3.04468 | -51.33618 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 184acdc5-6a70-33d0-9124-e189fe6cd95f | -3.01033 | -50.99068 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 750cc20b-6b6d-3349-b58f-da6bdfe1afe1 | -2.99477 | -51.00757 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f8b68a-2496-323c-93a1-3f1d0851ef5f | -2.99062 | -51.00691 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ae4cae5-be0d-3355-adfb-015979c9a8c7 | -2.98999 | -51.01067 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52f71e5a-3cb8-3bd2-9b85-260555954da1 | -2.98979 | -51.03777 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bdd655c-9a62-3a25-a0cd-66122d5811e5 | -2.98625 | -51.03334 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0052d287-611f-3a1c-bf17-9312f2749bd3 | -2.98563 | -51.03711 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 770d66a9-e140-3784-81d3-9d0da5fa4952 | -2.98146 | -51.03646 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1abb8b17-1fb8-3f55-b9b6-086e72f9a24f | -2.97339 | -51.45685 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e39c59f5-d445-3a4f-b2c2-35f1d105ec83 | -2.96945 | -51.10907 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 532e1a59-a626-3548-85ae-7abb7ec891cc | -2.9691 | -51.45619 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e6f7488-ab09-358b-853a-4e5556928e07 | -2.96414 | -51.45967 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0411d75-ffc8-341d-ae96-d0757e3cc86f | -2.94936 | -51.03881 | 2024-10-19 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8251e352-a86f-3de3-b74c-f1049fd85308 | -3.32405 | -51.06386 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3a456ac-b4b4-31b1-b92f-2ae8919b8bb0 | -3.32051 | -51.05946 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43da887f-5169-31cd-978f-bd657a39b5fb | -3.54038 | -51.38482 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
