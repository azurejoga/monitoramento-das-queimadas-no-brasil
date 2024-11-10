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
| 99c4835c-3d3f-3432-a256-fdb77b8d4321 | -2.25218 | -46.50536 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4895573d-8619-35db-a817-ffa48e655439 | -1.98115 | -46.43423 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e59c2762-c243-30bf-a359-d528ad7d9041 | -1.71671 | -47.88371 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77c8ba77-11df-36a5-b792-4111bda57e86 | 0.43863 | -51.84101 | 2024-11-10 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5418aa6-4256-36fd-892e-1ffae507a7b1 | -2.29392 | -46.50803 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cb6f034-f918-32a0-b440-ff066083dcdc | -2.19854 | -48.36871 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c7af2991-7baf-33b3-811f-22c1fbd9bd12 | -2.1692 | -48.32192 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2772ee1d-89f7-3f75-94a2-4e433e817300 | -2.39037 | -46.78556 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01ddf126-abdc-34c5-8565-40c16aabac41 | -3.51791 | -40.90603 | 2024-11-10 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5a068e9-3ac1-371b-9b0d-5882603e693e | -0.90321 | -51.65638 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| def70d8c-d827-3866-99a6-2aed027c2f92 | -1.46675 | -54.31401 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e8cc03b5-5678-391e-8d7c-ac6dd7b65f9a | -1.53733 | -52.20726 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b9af2f2f-1d0b-3806-99ed-1b11cdb99822 | -2.15701 | -48.52453 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 863b3caa-8556-3b11-a46f-aae4cebd34cd | -0.40867 | -51.48449 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c042a3b-ef75-3531-8613-312f6dec5af8 | -1.21971 | -51.75369 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a1925cb-3c1e-35d3-b5ea-07b8e03a001a | -1.6613 | -51.91094 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7585e7c4-968c-3caf-8665-e0142704e06a | -1.28418 | -53.70926 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e5cca04a-142d-3307-87de-8e135907d7ea | -2.30551 | -46.74669 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db468b89-a790-3869-a49c-eef7a6446a81 | -2.05304 | -48.88695 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd2980e3-bdea-32d0-9dc9-149c91eedde2 | -0.2931 | -51.72559 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9cd7c322-2a18-387d-a112-d712ce382cf6 | -1.05037 | -51.74463 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d67f00-0286-311f-9561-c502b17fcde9 | -0.045 | -50.78394 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87a463a3-a74f-38c3-9530-8172e3bc37a2 | -2.46153 | -47.84015 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f99e37f-196e-367f-9383-92efa2bf65bb | -2.43317 | -48.46923 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9468d34-613c-3cc4-b54e-6f37321f45cf | 0.05198 | -49.54588 | 2024-11-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 620ae21b-0916-3211-b52b-deb5869d0ad8 | -2.36806 | -48.92572 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2800278f-e1f7-30e6-9c84-7850ce85a2ab | -2.36976 | -47.92532 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7e9846d-28f7-3258-ba48-c6e243a14186 | -2.15703 | -48.74004 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e24ce768-9b0e-3f38-abc5-4427c6b36ae6 | -2.24042 | -46.36256 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d1be6b3-cfbe-3a38-8ecd-c4ec4f1240a1 | -1.35463 | -54.65318 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63089918-752b-3795-a19d-a73895cc0e13 | -2.20077 | -48.37612 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 421cdb7a-119d-3382-bf44-8cda86340d87 | -2.63477 | -46.7626 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dffee07-7882-3539-8d72-ae029d2323e2 | -2.07633 | -50.3496 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1d16860-6764-3c4d-b43a-c56f75aea3ac | -1.33953 | -51.42558 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 793e1efa-73eb-35b3-b9ec-84414f39564f | -1.34547 | -54.62453 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e2b334ff-5c1c-365a-839a-144ea254f868 | -2.46356 | -46.87436 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ad6f9bc-68f0-33db-8853-41e2a405eaad | -1.47472 | -52.08983 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 647cca44-f491-392e-b59c-2a72d5903c7a | -2.37676 | -46.78345 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67f94a1c-6f9b-3a05-8998-8935d2c1e757 | -1.27521 | -52.17902 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92ecfcb0-a7e4-34db-b379-bd60eab6a382 | -2.16533 | -48.53641 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fe83308-5aff-38c6-bd06-98eda2ee4372 | -2.38943 | -46.59048 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cae8f09-2e51-3348-9116-b34edfe19840 | -0.4527 | -52.03571 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db72ca28-39f1-3df0-937e-a5f9c6ca5fb1 | -2.54688 | -47.12276 | 2024-11-10 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 330b58bc-82a5-3e07-bf18-1634f85c00d3 | -1.20215 | -53.7082 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a7084dd-6852-3f9b-a815-db6ad94543e1 | -1.7027 | -48.16759 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6107750a-ad0b-3632-aa63-84b49ba0c228 | -2.04138 | -49.58105 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa823fae-096f-33b9-88a8-2b89e9b4558a | -2.28842 | -48.42156 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49f24b0c-031a-3812-995c-eb63279fa112 | -2.07692 | -50.34587 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3532f321-75e1-3d22-86f1-f317444de73d | -1.64163 | -53.38823 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 232d48b0-3db0-33ce-941f-ca0834c5e922 | -0.45797 | -52.02702 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ddd74de-f0b4-3b76-9a32-c26bee6ec0dd | -2.6737 | -46.80233 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78fc8726-2daa-35cb-9da1-453a87862db2 | -2.32688 | -49.12199 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b339a146-4084-3ca6-8b1f-42996c20f1a2 | -2.04323 | -51.16782 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f618fc4b-f8c5-3b6c-bdd4-c38d8a136210 | -2.3584 | -47.78502 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3daee5c-7f06-36c4-80c1-22824fd8ae00 | -2.06143 | -48.20974 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5712a920-0c86-3947-9daf-2481e2343162 | -2.15927 | -48.74746 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 949f4ace-e843-3890-9579-744af8242aa1 | -2.20161 | -48.8639 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26361512-e1a5-31cb-ac93-e28fe1cd24e6 | -1.62224 | -52.53722 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 860f40af-4443-3b44-a7d9-18760b152a49 | -2.09057 | -46.51498 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84458f02-8ee1-3e31-b4d1-14df7ca9bbcc | -2.10192 | -46.55438 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aab8df1-df85-371a-9981-b60dd4a57e44 | -1.35009 | -51.40575 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cba271eb-2b6f-391a-82c2-74723c7b0b9b | -2.56963 | -47.33758 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc77ef1f-82f0-3d45-a77e-cffe357cf68b | -2.08612 | -48.82827 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69b8e842-b3e2-344d-b5f8-3e8acf61bdfa | -2.314 | -48.47493 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb3aaf4c-4a3a-3a74-a303-42e5d4c3f640 | -0.2924 | -51.73008 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00214495-2063-3833-8772-f38a505efb5f | -1.52144 | -52.20946 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 27defe5e-effc-3194-a781-528a71139ed4 | -2.50271 | -46.30555 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 518c0cbc-7b86-3012-8f49-78a61e4be7c6 | -2.30609 | -46.74305 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc2e644-2d33-3a73-a9aa-1b97b9a60b43 | -2.28216 | -48.54762 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93cd0d72-40e1-35f1-9fd6-2484394e74f5 | -2.21235 | -48.36733 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 389df0d7-3a0b-3506-ac8f-c27d8846ccb9 | -1.669 | -53.13984 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce0411a0-6f55-3ee5-8cc4-c5cede98273a | -1.34408 | -54.63329 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38fc5f93-89c9-3c39-b785-0f743502317a | -2.40947 | -48.49024 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aeed4d1e-740a-3279-8e19-b40187c568e8 | -2.29334 | -46.51173 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dab6bcf4-c1be-399d-aa51-9a456d2786b5 | -1.67314 | -52.054 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cddb06bb-0de8-3c54-b1fe-f699a2574025 | -2.89811 | -45.56619 | 2024-11-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40a57144-d05a-39bc-bfcb-692526727515 | -2.35121 | -46.65612 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24aa58bb-a27a-3d13-a79d-53c298da8e3e | -2.67768 | -46.79916 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7f909f7-5c9a-35de-9e41-b7d59cddf469 | -2.16893 | -46.7067 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbda08d4-cd50-3fcd-9ffd-a0e81916d81c | -1.06026 | -53.65361 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a5dde2f-f0d4-31d2-b49c-f9f70103087c | -0.41061 | -51.93604 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632b50bc-3b30-35b2-bce8-03da2c19c54c | -2.67996 | -46.78453 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 779137c9-15ef-3d76-b1d6-984a0e7987c9 | -2.23524 | -46.55186 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4395b5b3-0473-3454-9da9-9d1b768c7cd8 | -2.18835 | -49.77964 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 134316d4-f277-316f-b081-f0a6bcd3bdba | -1.28775 | -53.71382 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 238695fe-80ea-33fd-8e08-ddee28349ac2 | -2.31365 | -48.54193 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9243f9d-3aa2-35b2-a524-8e1beb9a2f90 | -2.51245 | -46.35717 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16bc95fa-c642-3b74-8f24-e62403a131de | -1.99389 | -46.35256 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28c0ecc7-10e9-3513-9bfe-648141956099 | -2.10091 | -48.90135 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b51a855-b5ba-3d5a-bf56-129560e68e7a | -1.39164 | -54.65027 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b90cce35-7317-3aa3-b4bf-aa35253f6018 | -1.46369 | -51.49113 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 545ab45d-03cb-3aa2-8f44-e4b9b544496d | -1.31088 | -54.66916 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc81a7f0-9df9-31d3-bae3-69934ec8d9af | -2.05026 | -48.88297 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5b27382-1ea2-3a5b-a9a1-7aa805b8d7d0 | -2.17979 | -48.37991 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2839726f-73d8-397d-a770-0ce740ee3847 | -1.97073 | -45.71148 | 2024-11-10 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88451cb9-2a24-3a17-bea4-fbcf292a8c38 | -2.17197 | -48.32588 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54e2d2ae-2677-3555-b13e-298b66f98e9d | -1.59619 | -52.7469 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb8616f0-b69f-371a-be6c-4987df3e638c | -2.12462 | -48.56195 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0188fb30-c8f7-30da-b8ad-de228f2a99ee | -2.52049 | -46.37378 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19bc7cce-1029-3553-a692-8a5af302b93b | -2.31709 | -48.58482 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README70.md)
