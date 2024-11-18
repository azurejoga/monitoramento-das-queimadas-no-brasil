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
| d4dbe567-d6ac-378c-9b55-4b2352c5130c | -2.84643 | -46.62096 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c80eb7ce-cd96-3d97-b2f4-6ca5d6ae402c | -2.83958 | -46.66428 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ea3cfdd-7900-3a63-980f-475ef9532736 | -1.85067 | -50.79945 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cc98067-8084-3147-825a-075218b05496 | -2.85816 | -46.67227 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d70dbc67-8c21-3614-aece-5962cc744bbc | -1.28713 | -51.74157 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56f9cb53-cc23-3cb9-9539-5252a07602d0 | -1.1591 | -49.11285 | 2024-11-18 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e40e7acc-1734-3db6-9b47-6707814b40ab | -3.30764 | -45.69304 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| cfea01b8-37b2-3c28-abc6-d2b5e64a8beb | -2.93404 | -48.06524 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4062462a-2e26-3595-a03f-5d1a2fea8fdb | -2.64204 | -46.8469 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca72bbab-115b-3717-9b9d-894c2d13d29b | -2.59207 | -51.71801 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ae35cbc-d555-3c14-8b1c-87b4654357a9 | -2.35753 | -48.56931 | 2024-11-18 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| decd4669-15ce-3bf4-990e-4e536e2dd3e8 | -2.91413 | -46.85373 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6369de36-f154-3b16-95ad-4a62f4d2d1ce | -2.23121 | -53.60784 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40abf6de-4e57-3bf9-9062-d60e2f62e5a7 | -2.86265 | -51.78939 | 2024-11-18 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b70e0bde-9999-3163-91e8-bdde13cd83e9 | -3.14413 | -45.99049 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35cb7ce7-4f52-3739-8647-d1c50cda5956 | -1.62704 | -53.30477 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b86cef38-74ec-3e95-9d21-cb990519df7d | -2.64743 | -46.21328 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 449e1fb2-5720-3bbd-9b7e-6498340fb631 | -2.34 | -49.13811 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 24ffb644-7920-3a86-a4bd-1987c294b834 | -2.64933 | -46.55757 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1ea2afb-7aa5-3b1b-872d-321c06ee3389 | -3.946 | -44.10289 | 2024-11-18 04:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 970c99ce-cdf0-3372-970d-62280f0492bc | -1.16174 | -49.11078 | 2024-11-18 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 781c625a-7102-322d-987d-1c308a65323c | -2.93044 | -48.06061 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f6b07d3-3f40-3f28-929b-52d582573b70 | -2.92198 | -48.05923 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78ed9eae-48c6-37ea-9d64-71313ba75d59 | -4.79933 | -37.38969 | 2024-11-18 04:10:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4835b98d-3829-329a-ab4a-f8ec9cdc3560 | -2.60211 | -51.79279 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f9d8522-7d7d-351f-9406-75de2543db51 | -2.60152 | -51.79636 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ad5a448-cbd8-3f33-800d-246bc93fa333 | -2.24316 | -45.75101 | 2024-11-18 04:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e199ef5d-56e5-30d1-9727-0deda88be68f | -2.66106 | -46.2249 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b88aa653-f891-3d49-820e-2edbaadf56a4 | -2.85892 | -46.66744 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc42748-961d-3424-8761-02fb321cd6f5 | -1.61594 | -55.15049 | 2024-11-18 04:10:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba64aec4-db74-3ab8-82e1-38e8258c8fa3 | -2.50158 | -46.39742 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5575503-1751-31e7-9449-5e0c4968adf3 | -2.61393 | -46.82188 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 622436ac-fc21-3e6a-94d0-882a9e56609a | -2.66032 | -46.22951 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19e9d22b-9b32-309b-a5ac-92f39db742f8 | -3.80568 | -40.93596 | 2024-11-18 04:10:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd05cbec-52de-3dba-ba8c-a59d9c98b4fc | -2.85505 | -46.6668 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df84d3e1-a990-3c94-affa-708c1ad3617e | -2.86207 | -51.79293 | 2024-11-18 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d0bc2e4-048f-326b-8bfd-e3018383acb5 | -2.17234 | -50.60893 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b204b23-f1e8-3b8f-bf10-dccfb41b7ea2 | -3.04209 | -49.56574 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 195d0544-a70a-379e-b4df-8749196e0272 | -3.32681 | -46.01635 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89af35b2-5c8f-3073-8310-ef2b11c1693d | -1.2977 | -51.74709 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 5ea68361-a431-3810-9c01-e41afd0bd4cc | -1.43231 | -53.38407 | 2024-11-18 04:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9628000a-fa6e-3da8-9e54-9adf06c5c587 | -2.63812 | -46.84624 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd02f0d8-ff22-3ade-91d7-09175d98dbb2 | -3.05689 | -48.00038 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6b27e5fc-3cce-3637-a4f7-23b167869066 | -2.96088 | -48.00544 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a24dd3b8-863c-3b39-9ea7-4882116054d1 | -3.09143 | -45.96414 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ae46418-ec3f-3fcf-b5fb-1df490f6260c | -2.84845 | -46.66753 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84f2d04d-ab93-360b-9805-1c636bc07579 | -2.65385 | -51.71763 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2d50449-5fc8-3ca5-aa8b-75d222789211 | -1.76852 | -50.74737 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a13c0c2d-4597-3a00-b06b-62fc99d00880 | -2.59662 | -51.79188 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cf9a2b0-35ec-3d98-800f-70039ede2e22 | -2.86383 | -51.78217 | 2024-11-18 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5210259f-b91e-3209-b1a8-9a788a8056d1 | -1.77371 | -50.74822 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4095d213-0c27-3c52-9b29-022bfbbe6869 | -2.63483 | -46.56247 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a1bd95e-4f6d-3951-b8e1-8731a4d391c6 | -2.93357 | -46.73107 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22f3082e-d469-36a0-8015-2e74fb82eb4a | -1.76181 | -50.74805 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb1673cf-802c-314e-91d3-7ab71a95d6b2 | -2.58055 | -51.7197 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a9c1254b-4cbb-3730-bb07-3039f785e184 | -2.57894 | -51.72537 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e299f9a-2bc7-3b88-9fdb-64fed02edcae | -2.57995 | -51.72325 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c97184ec-1002-3a76-ba1a-aaf78b1a65c0 | -1.30328 | -51.748 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 167d7042-b52f-3ad9-9373-12681af9e478 | 0.61388 | -51.77852 | 2024-11-18 04:10:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798d05ac-fa20-3123-9034-dc862b90958e | -2.67615 | -46.2274 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fca73d40-44d7-3abe-998f-ae4d5dd74a3c | -2.59395 | -47.55991 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 777f64c5-4412-3a2b-b094-65e51f1b23a4 | -2.50221 | -47.24438 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 638ba994-a9fb-3daa-95ab-33c9e2c2154c | -3.14853 | -45.9867 | 2024-11-18 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6148577-0595-3cf6-aa9e-330dfb28487a | -2.93341 | -48.06919 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8bc87dca-a186-3792-a92e-fff34020b4f7 | -2.55896 | -47.28279 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c73a7e88-f2a9-3560-b840-f695bfb822e8 | -3.25482 | -46.53478 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5e3994c-4675-3c15-95f1-fab9694c12a2 | 0.97145 | -51.14084 | 2024-11-18 04:10:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f18835c2-c09f-3216-8817-b656ebfad704 | -3.14378 | -45.50482 | 2024-11-18 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be19037c-4c82-3972-bb55-f1505481ddd7 | -1.13681 | -51.69815 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 301c49b1-6b6f-349f-9a61-7b0f1be729f3 | -2.21983 | -46.41852 | 2024-11-18 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7abdfe51-1af5-3dae-8bbb-4c7ae10ff91a | -2.59148 | -51.72153 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7267b51-bf45-3e98-bbfd-92e37f4ec3e0 | -2.59505 | -48.30526 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2917f0da-8731-3b1b-8a92-9ca1b18006cb | -2.54507 | -47.29167 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d46b758f-4ee1-3bcc-a799-676fbe94f44e | -3.583 | -44.06516 | 2024-11-18 04:10:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e884129-438d-3365-90d1-69f6d79378a6 | -2.59543 | -51.79902 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01ab97af-5096-31d7-ab17-5eb60f1dada3 | -2.97302 | -48.74858 | 2024-11-18 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52c3d262-e7e1-3605-8c0c-9a7ba56fd5bd | -2.2072 | -46.30013 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d53661b8-0cca-391a-881a-ba72a214bee3 | -3.211 | -46.47267 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 438d83cf-d66f-30b2-b11e-aaff63082e62 | -2.77743 | -51.75694 | 2024-11-18 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fa25889-d877-3f42-8a8a-0f9ce905115f | -2.45782 | -48.81425 | 2024-11-18 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7695a4f9-84a9-33c6-b7cd-b3125c6d37d1 | -3.66634 | -44.4695 | 2024-11-18 04:10:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d9405ac-3bc2-3dfb-b237-ceb31450f76e | -2.91176 | -46.86867 | 2024-11-18 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 63591ea4-2d3a-3dd1-8991-05c765087450 | -1.16642 | -49.11154 | 2024-11-18 04:10:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30423031-22aa-31b5-8325-47fcfec2ed64 | -3.16723 | -46.60077 | 2024-11-18 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bfe41d13-c75d-32fe-9c12-c75780f67f04 | -3.02559 | -48.00707 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97aab1bd-d7e2-34a7-871b-b15fd6080ed0 | -3.05628 | -48.00422 | 2024-11-18 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc9f4e23-ecc1-3e11-8627-5f4aeb9165f7 | -1.85018 | -50.80256 | 2024-11-18 04:10:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f65e36e-a79f-33b3-a734-8bf735d7e464 | -2.74982 | -49.32882 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47d7263f-e967-3a1a-83b3-d7a4f662d2b4 | -2.12261 | -45.35188 | 2024-11-18 04:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b77cb58e-9a88-3ddf-8e9d-c65be0c49802 | -1.21197 | -51.79153 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d00358fa-f06b-3b7d-9760-2dd18cd1a0b4 | -1.70095 | -45.8316 | 2024-11-18 04:10:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2bff1115-7640-340f-9675-7ef04778c2d2 | -2.50278 | -47.24081 | 2024-11-18 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76780f86-58fc-3fdc-829e-2ab62be04e7a | -3.08912 | -45.17664 | 2024-11-18 04:10:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f8c6164-6d4e-3442-9bd7-3a2ff053ada6 | -2.36847 | -53.68365 | 2024-11-18 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45cb77fd-9e2e-36d7-8629-d7f805b9e571 | -3.08494 | -49.20785 | 2024-11-18 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec860c0e-a41b-3679-aae7-f1d3989593c5 | -0.94643 | -51.72713 | 2024-11-18 04:10:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af7aa9b0-92d9-3826-ad15-3fdac2201836 | -3.49442 | -43.31214 | 2024-11-18 04:10:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4c8d385-2261-37f3-879d-80e823c10fdc | -2.94467 | -48.31655 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1aaaedd4-f62b-3961-a3d4-0fe15823890d | -1.13741 | -51.69441 | 2024-11-18 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bcabc2b-c8d7-3fa3-ba3a-c5d56d6d8a37 | -2.93835 | -48.32809 | 2024-11-18 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README20.md)
