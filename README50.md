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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 975c5d78-1380-3afa-b597-f21c567ea534 | -1.70682 | -52.45536 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ebae309-eaa1-3c1a-8115-da9ebe1541f5 | -3.81321 | -46.54275 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c03f541a-ed03-3750-a121-ff1f287c66bd | -3.05652 | -53.1712 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52f32f31-149c-319c-b81d-37202161e4fe | -3.04179 | -48.49072 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c6cce92-50aa-3c6b-adda-71a486f06ecb | -2.13477 | -54.87909 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b37f2900-eed3-3e83-8729-99aa54473c3e | -3.73871 | -51.83202 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef7f7477-ecef-38ed-a4a3-8ee885248289 | -3.12131 | -53.27164 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16c63d3c-ed02-3987-99e4-3ff8e1d93f9f | -3.73342 | -52.34095 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6410897a-4f22-39a2-b1a7-034c09c5f53a | -1.6079 | -48.69921 | 2024-11-30 04:40:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccbf16c1-3d5c-33ac-a963-ca365516acb9 | -3.72741 | -49.89357 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36be83bb-96b2-3a77-96b7-86c847b7ebc5 | -2.96296 | -48.03511 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b6e3c0b-c014-31ee-8a6c-ad9905b2e16a | -1.57701 | -53.7502 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6156b7f0-5fc5-3b0c-b565-6c7e58c35f5e | -2.6167 | -48.16293 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb381679-bfa9-3b43-a30e-b66ea3edf25b | -3.14147 | -53.83987 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fb51cf7d-1132-3acf-b66b-68f433a3979b | -2.08426 | -48.54516 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d0d4d1-9921-384e-98d0-c64c172a8758 | -2.6682 | -49.8571 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72397e45-9b0b-3ae3-9901-e62f1e9868d8 | -3.03303 | -48.50348 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08914dea-9604-341d-9937-b38a0d9a38b1 | -3.60374 | -49.98871 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 7c32b23d-b11b-3e6c-9b00-7276b78e7957 | -2.21545 | -47.72588 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20372089-f1b4-343e-9337-f9d135a8c494 | -2.13845 | -54.88395 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 85e92926-882b-3f9f-b314-7b85d16da022 | -1.26882 | -54.55465 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 3332ad1d-1ffd-3cdf-843d-5f99d3c2169f | -2.783 | -52.86729 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c9e08cc-38d8-3e0a-98d3-911597b4d5cf | -4.61144 | -47.00612 | 2024-11-30 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad1b972d-3308-3628-933b-3c9a9b341af7 | -2.72412 | -48.67343 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb4a264-3d9f-31b9-b6e2-402d9064f407 | -2.70759 | -51.99939 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7b776b95-2a02-3fc4-b8c2-3bd4b16aa701 | -2.46201 | -46.54507 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f40fa3d-8cb2-3b6e-b7a5-7c46aefb3518 | -1.07341 | -53.6368 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7b60cd6d-bc41-36fc-b342-76c30a92e799 | -4.48291 | -45.67036 | 2024-11-30 04:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea8b2a65-83af-3d7f-b12d-3710c638eae4 | -2.83454 | -54.10853 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 138aedad-ddd4-3ff9-ae4d-15c69edbbb68 | -1.49989 | -54.95441 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 558e9de8-90ca-38fc-a58f-d267d19fd680 | -3.96054 | -48.09204 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60b6e966-2930-3845-ae53-84082db35501 | -4.15751 | -44.26804 | 2024-11-30 04:40:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42ab847b-e11b-3e2b-850b-d33726b9270c | -3.67905 | -44.70377 | 2024-11-30 04:40:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29cd7cfa-25d8-3340-b3fc-e87d4e4406f0 | -2.85543 | -48.90183 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da354775-9535-3d0d-917f-3ab2e74b7cf1 | -3.10383 | -54.04496 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67b476ad-971e-3f7b-975c-1b4e5179e8ee | -2.22835 | -47.77446 | 2024-11-30 04:40:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc259194-d01b-3712-ba41-5500ff1ecabb | -3.14259 | -45.98285 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0fbcc446-92d6-35a3-a4e5-96624a812399 | -3.60543 | -49.99974 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 215d84fd-3ee6-355a-a653-6c0b5a6d784c | -1.56675 | -51.98312 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ceeb4cd-c1ee-33fd-a9bd-f0a2b77d7990 | -2.95085 | -49.44515 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 523a6dad-8ab0-3ee4-9048-2b2fd3ffacdd | -2.19367 | -48.41097 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 342e428f-f2c0-3cc1-a0ea-e4394e804723 | -2.0043 | -51.17074 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b25a9fa6-ef0a-3d40-8d6f-2759cc2abeea | -2.05634 | -47.56492 | 2024-11-30 04:40:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db11f123-0464-3049-acdb-3f1c656e4e1b | -3.59097 | -49.98314 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31286f7f-106e-310a-921a-74f9e5dcbd62 | -3.61561 | -50.19207 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7aa55c5-3822-3b0b-8e1f-ae43f77484a7 | -1.97818 | -51.15483 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6278935-d74c-30e6-9c73-c026ff1d3b99 | -2.41851 | -50.47509 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da73be06-f6fe-3e7f-948f-8fae66e6d021 | -3.27701 | -50.61866 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56e94474-d644-33e1-8200-aaebf630ec9d | -6.22662 | -47.28005 | 2024-11-30 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecebba40-3a28-32dc-bd75-49c64305087e | -2.37797 | -50.40197 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6c9131d-aab9-3520-8c29-2341e2e34317 | -2.75918 | -54.08469 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9976507-61c8-3a9c-89f8-85d530ca8262 | -2.92505 | -48.58546 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f825e921-a3f2-3102-be0d-d997e66f5793 | -3.02807 | -54.02119 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6109d071-4092-3b2e-a2c9-3e16eb26df60 | -1.71382 | -52.49139 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbb27762-5420-37f1-a0ab-cca54333bddd | -1.62698 | -48.53361 | 2024-11-30 04:40:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a939172b-771c-356d-8077-eb53793b3a09 | -1.42122 | -55.27702 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e934a88a-d838-348e-89a3-c4f8d7838a95 | -4.87186 | -41.31373 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 84e743c5-14f0-3c46-a0ab-00af9998d7c9 | -3.09254 | -48.07641 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 916360c8-a695-3453-9a19-604b2ee52d89 | -3.79755 | -48.96824 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f239812-fb59-386f-a4df-c59050d99ada | -2.14941 | -50.62465 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e75fcb51-2585-3fa6-8357-498bacb248f6 | -1.701 | -52.64314 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cc1a5487-a572-35b5-b637-490ead22db85 | -1.4989 | -48.02396 | 2024-11-30 04:40:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54045522-b672-3723-a972-74fb3e42499c | -4.02658 | -54.63492 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b6fbd8d-f6ef-3412-822e-4de14379530f | -2.61432 | -54.20895 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3675a33e-1e7f-3efc-9ac2-7e2f28d80316 | -3.52673 | -50.48043 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 832f2a82-e376-3d84-a15d-9265327bded0 | -2.20859 | -48.42383 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8db97903-89b1-3e82-af62-5782eac91553 | -2.95832 | -51.69896 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3046737-f137-353e-91d3-f248c6d48b3c | -3.5366 | -54.08136 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b82f9c0a-2fdb-3f62-b342-d3fa3fc5bf53 | -1.67967 | -52.50648 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd5165a5-f229-3399-adeb-c0809b96bcd4 | -4.11347 | -54.40974 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10e6379b-72f2-3081-bef2-9170a6758dbc | -3.21758 | -54.08947 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ec632db-55b6-3da2-b004-a026b69b055a | -2.92981 | -48.00811 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02fd33ac-ea48-3799-a1c7-ef2d5f9bfc65 | -1.33719 | -51.42576 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c0cf9d0-880f-31a1-9731-7b9273d872cb | -4.13475 | -48.94351 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da514454-482d-3fbc-8ced-191406ead9a4 | -5.92077 | -47.81866 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 81e473ac-0922-33b0-9954-39f1b2a9c1d1 | -4.51546 | -48.06558 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c503541-d515-3d1d-9519-0434f5280d78 | -3.26002 | -53.63237 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1c6e74ba-f024-3657-a46c-61617f040297 | -6.70521 | -47.27048 | 2024-11-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47a070c7-2c9c-374b-9e89-49da884a5877 | -3.15054 | -53.83442 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c916ef46-c407-33bb-a25b-9309510ada08 | -4.10442 | -46.11075 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6babdf35-748f-3707-bec9-e85429838911 | -1.94127 | -50.63102 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 318cd7e5-15ca-3461-b6d0-74b43535bea1 | -3.2499 | -50.61448 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4273811f-a011-3dc2-abb5-cde9a2c44c92 | -1.53588 | -51.56685 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac8a0524-7755-30bf-9988-1f3ee3e8207e | -2.27543 | -53.77112 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27f87662-a66a-33b7-a495-e0ddfd547c77 | -3.82669 | -46.60355 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 302986af-209e-39d8-8149-49725ef562cc | -2.28247 | -46.43729 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f586d827-e0e5-3621-8fa3-2fcd14fca4f3 | -2.9888 | -49.59273 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcce589b-009e-3c4d-b36d-2de703793500 | -3.27069 | -48.76632 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c017730-50d9-3079-8f65-49ae8d570e20 | -3.78914 | -50.12932 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a65ec23-a77c-3451-99be-a2deef1457f4 | -3.53411 | -46.40578 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3391a750-7a6c-32da-8df4-8b34f9e5f1a3 | -3.09587 | -48.07692 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30212515-cc3d-3e49-bc79-245f7e03002e | -1.87965 | -48.54806 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46b09881-8176-321c-a546-b531f6ab086c | -3.69657 | -51.80101 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 32349fc0-b8ce-3eb8-8158-70406eb20ce2 | -3.07852 | -51.09892 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 824f5a84-d76e-3e84-9526-789bba824b8f | -2.50065 | -51.95607 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea962d06-aa6c-39af-b5a6-81ad6f2a6075 | -3.77881 | -46.69634 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1821f51c-25ee-35c0-811f-fb039ba44f3e | -3.86364 | -50.1518 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b02b3de2-871f-3347-bb87-d4855156111f | -2.9828 | -46.94512 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3f0c5f7-1037-3b71-9878-89f818adade7 | -3.77287 | -51.6158 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd85b6e2-5698-3415-9721-3f0b0e61fd12 | -7.72136 | -48.72472 | 2024-11-30 04:40:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README51.md)
