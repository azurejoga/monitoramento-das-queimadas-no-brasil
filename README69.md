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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 057008b4-cbe0-3df5-96bd-2a7c8fe1090f | 4.44075 | -60.46962 | 2026-09-19 04:55:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e64c771b-8b99-32c3-bb7e-49ade0da0ef8 | -1.19837 | -54.21755 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5cdf8ce-9f00-3404-a8b2-42859f3d3359 | 0.7914 | -59.20061 | 2026-09-19 04:55:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efaf8a88-f635-3afd-a084-6f0e5c7c58e3 | -2.83182 | -50.45993 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79f45b43-b164-3092-9526-b0caf6ee5cad | -1.96542 | -54.69439 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec3ef286-6997-3d59-b2b0-d0aa8b5bf6dd | -1.99886 | -49.45348 | 2026-09-19 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4885e3f6-33d7-36d4-9398-3d2eb06f9b86 | -2.81659 | -50.46862 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8f30f0d-152d-3d88-b539-0617e5ee3416 | -3.16394 | -48.61072 | 2026-09-19 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13838c8a-5909-3fa2-a282-9dbb65a47341 | -1.70358 | -54.89101 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1626f353-87fb-3d66-8afd-7e808aaa2bcb | -2.59931 | -49.50602 | 2026-09-19 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1f9efe8-db2a-3d82-bead-0ba7f27da47f | -2.73248 | -49.46232 | 2026-09-19 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79d28e77-07c2-3c3e-8bd5-c0bc374865b7 | -1.70784 | -54.88743 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4089fbd5-c303-3d9c-9cdb-f32896876423 | -1.22435 | -55.72145 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 478d4c3e-ce04-3115-9ae3-b9c30b90959e | 1.31625 | -60.40764 | 2026-09-19 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7766b41c-372a-397f-9964-84444acf85c5 | -2.82176 | -49.23842 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 172ca29b-aa87-3903-962b-d023347ad3b2 | -2.82279 | -50.47327 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0c8fc75-78c3-328d-9b50-5bb808a76004 | 1.22849 | -50.99963 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58012389-fac4-33fc-98ae-f8a42d195c98 | -1.58522 | -54.42508 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7f6ce369-70d7-3401-b26a-1afc124b65e9 | -1.84162 | -54.8549 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48d6d2f6-d386-3dba-b510-a58f7a6eb103 | -2.81603 | -50.47221 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e50384b1-1e48-3f9b-9b29-91318bf56d17 | -1.71144 | -54.88799 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78b0c74c-dee2-3fe2-9f8b-516e5493335c | -2.62518 | -49.1082 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c045b16-263b-31d1-9163-2b53e1b87b0c | 1.3157 | -60.40419 | 2026-09-19 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32fa253-1729-3cd3-bc89-61e9b12440c4 | -1.58105 | -54.42848 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ba0758b-6f85-3b40-8364-041ee990fed2 | -1.62952 | -55.2656 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97993ffd-cd6b-3c1a-9234-29607934b0c5 | -1.67962 | -54.92546 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3f10078-bc74-300f-96fb-b37766a0ae7b | -2.83068 | -50.46713 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4e313b00-734e-36e2-a95c-9b45ea02cfe5 | -2.8149 | -50.4794 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62c8fc1a-a6fb-31bd-93f3-c27199898133 | -1.49204 | -54.97823 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8218f7f4-339d-3040-b14b-f37a3cc186ca | 1.31286 | -60.40919 | 2026-09-19 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1abd6a62-4c06-31a7-9785-521c93de97b8 | -0.26242 | -48.41028 | 2026-09-19 04:55:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d16f3fc-85dc-3ea7-b907-fac1fd11248e | -1.57368 | -54.45162 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb9ab915-622b-3aec-9e87-76c9429908b1 | -2.14331 | -50.90234 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e7d0004-cae4-3632-8046-56af67d20ca4 | 1.31234 | -60.40574 | 2026-09-19 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff2d5204-1a74-3588-8d6e-708110e0ae4b | -1.94845 | -51.53522 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f45d1271-4e89-39a5-92dc-820d40331f0c | -2.14665 | -50.90286 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd243b1-b53c-3852-b7cc-42d3a114c778 | -2.02816 | -48.77693 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d012ca02-50ea-37ba-80f9-c84ac99af9df | -1.18011 | -54.17457 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2b85176-221a-3bff-aeb4-1ea60a57aa53 | -1.57886 | -54.46447 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3373a04d-a8f8-3b19-945f-0979ff36c8cc | -2.1461 | -50.90636 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abfe1437-509e-3c00-a1c2-2c1e50f84cf9 | 1.25301 | -50.98162 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40a47dc4-db9c-3f12-877b-7852c9782202 | -1.63989 | -55.15255 | 2026-09-19 04:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44b4f02b-4c0d-3ad6-8da4-243294a894df | -1.63623 | -55.15199 | 2026-09-19 04:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5eee930e-4979-3aa2-b02a-dcad910a2ffd | -2.82617 | -50.47379 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a659d3f0-67cb-3a51-95b3-a0aaf86c5f50 | 1.21912 | -51.00461 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a464bd0-559c-36c7-877a-60260143f74b | 2.51629 | -50.84958 | 2026-09-19 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dcff966-9c55-3932-8358-2dde58d57649 | -1.22332 | -54.12901 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4474a41-5ec3-3310-8f42-5d4e563cfaef | -1.69991 | -53.69133 | 2026-09-19 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1225247f-d952-3147-b69c-0971098e7faf | 1.26282 | -50.74428 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f0012d0-045f-309c-bdc9-790a67390775 | -2.58502 | -48.43894 | 2026-09-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cf3854f-80c2-3825-8d86-dc11137e524d | 1.21581 | -51.00512 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 31fdbb9a-0c2f-31c8-b6fb-ae996c8d1156 | 1.25193 | -50.97476 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f56cd0e2-1821-3c82-921a-906a1e3a433b | -1.62583 | -55.26502 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 573f4cf9-70c5-3900-ae3f-6bda0158e725 | -3.02111 | -51.19646 | 2026-09-19 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2187272d-ba0a-39b0-a516-73ed05493112 | -2.03175 | -48.77749 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7131bd6f-e16f-3cb0-9f4f-d117d253edde | -3.23394 | -46.94255 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c94df28b-af96-3b04-98a2-b5b0e6bfb3aa | 1.13893 | -50.99292 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa76f9c1-2aec-3f6d-a195-bfc6eae32a8a | -2.82111 | -50.46194 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a5a6a804-8d5a-31be-9e1c-ca25d33130a7 | -0.52516 | -49.15531 | 2026-09-19 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19a9de8a-af77-33be-9178-7cea0434a482 | -0.9467 | -51.38098 | 2026-09-19 04:55:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 785a2d44-388b-379c-b87d-33f245e1b03e | -2.82674 | -50.4702 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2cdcade-0b95-3865-ba0b-1de1d8e78d69 | -2.38813 | -48.52576 | 2026-09-19 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31e86e8a-9211-3740-bfc1-1090ff983755 | -2.81997 | -50.46915 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5d2ffcf-1542-3d62-a873-bb577a8a2f5c | -1.65498 | -54.91725 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ac05316-4462-3035-9fe0-e056dea09184 | 1.03546 | -51.11118 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69d7cc8-b9cb-352e-b261-4b7a911b407a | -3.02166 | -51.19297 | 2026-09-19 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 897c7318-0308-386c-88a2-86d8dd2b80fc | 1.2169 | -51.01199 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee62161c-5c94-30bd-bf9c-b02aff8880bd | -2.81884 | -50.47634 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cac017b2-d5f8-3f02-830b-5af2b048ab1b | -1.59614 | -55.54937 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fb910fc-d55d-3818-9520-4399804ae63d | -2.93851 | -50.49499 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4843ee13-7f17-3c55-93fe-e53682874371 | -2.48265 | -50.40981 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9596ecb-9304-3f87-ab40-b316ff8d7ff6 | -2.66008 | -49.48372 | 2026-09-19 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26328a3c-6296-39fb-b2c8-17490289fa85 | -1.6953 | -53.69819 | 2026-09-19 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad44a1e6-b0e7-3d85-bcf6-a3702a98500d | 1.25523 | -50.97424 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7d4c4a38-f848-32db-891c-52b7deea068b | -3.03451 | -48.41163 | 2026-09-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3c41a532-c262-3ace-b368-ca79d9b76fae | -2.25779 | -52.02753 | 2026-09-19 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02a2be91-4e79-376d-8605-75304552962c | -2.83463 | -50.46405 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f5c18f-a417-3506-9620-15e3fa8bed31 | -2.81941 | -50.47275 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4eec42f-2204-3cee-94e3-6e57fef086a2 | -1.57305 | -54.45556 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80087901-8568-3d3a-8590-c336a0ad34ed | -3.23691 | -46.9504 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e20aa578-7477-316b-824a-509ecfa84199 | -2.66069 | -49.47985 | 2026-09-19 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab7b1035-a92e-3fd7-a3b4-083b4ea1319a | -2.73598 | -49.46286 | 2026-09-19 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9056ad0f-8b6f-3b0a-aa58-80c78ba2241c | 0.00976 | -51.17783 | 2026-09-19 04:55:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41fb2063-7edc-3540-a725-9febba528c77 | 1.26336 | -50.74772 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 250365b8-76da-39a9-ab5c-969306bc1a6e | -1.21923 | -47.71278 | 2026-09-19 04:55:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf60fab-d118-38fc-98f2-0d865949843e | 1.22519 | -51.00014 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c706662b-b553-32e9-a687-218ab4b33822 | -1.21847 | -47.71568 | 2026-09-19 04:55:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6326943b-6a1c-38a1-96bc-2092c7d1cf0c | 2.65456 | -50.86262 | 2026-09-19 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa413d11-2c69-3169-9982-e72dddccfc84 | -1.65432 | -54.92141 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 554d11cc-c08f-3aa1-be1d-0c47d35a1b22 | -2.93651 | -51.06481 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8547aa53-9dcf-3d23-af35-e0d5a40db388 | 2.31804 | -51.6368 | 2026-09-19 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f411eeec-6a6c-3c0b-ac47-731acabd7bf9 | -2.82955 | -50.47432 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9472c073-66e5-3887-a905-0126d1d8bfb0 | -2.8273 | -50.4666 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6597d33d-e5f0-3532-83de-b198f9243fbb | -2.66358 | -49.48425 | 2026-09-19 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ff4bfa00-c596-304e-8795-3c11b490c568 | -3.23229 | -46.95338 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bde06e3d-e93c-3243-b350-02daae30f76a | 1.26005 | -50.74823 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd9e6cbb-92dc-3a13-847a-fdbac680c08c | -2.82506 | -50.45887 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bc0caed-a362-3a24-9923-95de818a3e2c | -1.78259 | -52.15359 | 2026-09-19 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c8f7483-31d7-34ab-b7a3-501b37fc7513 | -1.58458 | -54.42903 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e6e232f7-20e8-30d7-b61b-320e64a4a8da | -0.75494 | -48.70927 | 2026-09-19 04:55:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README70.md)
