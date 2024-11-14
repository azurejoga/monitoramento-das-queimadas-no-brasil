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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89b8fbaa-d695-374e-bb7e-28e91e36f4ed | -3.50078 | -50.83414 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b50edb1d-194e-3268-a2fc-022adcb3ab7a | -1.93459 | -46.28214 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63c59267-63c2-3713-9338-506b30353c66 | -1.29823 | -52.88485 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d62ca6ce-1e07-389c-b433-351fffed8013 | -2.65798 | -51.68055 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be596197-4002-32fc-8ffc-a8d7513102f9 | -2.34654 | -53.75455 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bc28891-659c-37aa-9ad3-39c28660c7e6 | -0.20344 | -51.5281 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7de8b46d-bacd-3720-9986-2e980834f89c | -2.72609 | -53.19841 | 2024-11-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96d49978-844a-3bda-a76f-a38d0173d1ad | -1.38774 | -51.10232 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41b610e6-bec6-375a-8795-39398f2ec3ec | -1.55968 | -51.85078 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e8532db-7c4a-3f18-b834-ba8ee08f7b41 | -1.40844 | -51.11433 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b43f60b-bff3-3701-931e-ec5353f77f50 | -2.41972 | -46.27136 | 2024-11-14 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98b07ee0-6ab5-3e4a-9cb7-f0b23594d069 | -1.48095 | -52.10055 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f4ff105-7ae4-3bd7-9a81-1a241f300066 | -1.3475 | -51.43229 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee03c072-a075-3ecc-b170-e98d4e0c5896 | -2.77854 | -50.30338 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 891569a9-5555-3bba-b809-4c56039e0ebf | -3.4091 | -50.304 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de6376b9-ad90-3ca6-8302-70e5ab79f8dd | -1.60716 | -52.49369 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85f4742b-cda2-3840-a171-33136be12435 | -2.08899 | -47.73336 | 2024-11-14 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bbfaad0b-fe41-3378-8c35-3ded7ddd4d2a | -5.19281 | -44.35379 | 2024-11-14 05:01:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b7e8fd9-1a1e-3e11-b217-1a060688775d | -3.20651 | -44.4313 | 2024-11-14 05:01:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 110644b3-04e4-3a34-abf4-1b74cb53d954 | -4.0565 | -47.22999 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52aaeea2-e830-38a5-ba92-5e621476d197 | -3.77442 | -51.03102 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fc2d17c-565a-32ef-9d8e-3af71c9624bd | -0.29348 | -48.42649 | 2024-11-14 05:01:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 753ad228-04ed-3c5d-9d71-942e627a64a4 | -1.40063 | -52.38551 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9d65831-231d-337e-9eca-642f7126fb9b | -2.65194 | -46.8314 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1139dacf-3f8e-3640-a6ec-3c6028c8a080 | -2.64033 | -46.18121 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b82e9c0d-ef50-3995-a690-1ec3f6fd14a4 | -1.80046 | -52.17957 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24bed3c4-1d1a-3d7c-b608-0382fb1adfd4 | -0.19588 | -51.50653 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a26f0556-9512-3afc-b9f7-6a157ee722c0 | -0.89712 | -51.73133 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a6abb1a-419f-32fb-9dc4-e36dcea47975 | -1.61803 | -52.51458 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4081e143-97ea-3b38-943d-75132d2a31bd | -1.98697 | -51.11492 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6655eea6-ad68-378b-a1eb-cc99a04a0917 | 1.30483 | -60.41258 | 2024-11-14 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55949461-4d87-3452-a2a7-ccccdea6f573 | -3.66357 | -50.94941 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 895adb9c-912b-3f0c-bf60-6d97d1ee0c4b | -2.05787 | -53.40258 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a94009f-5bef-3b74-baa8-75ef0e38b492 | -4.13424 | -51.0786 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e44caa6-2e56-3b5d-a190-00eacfb8a623 | -3.1708 | -50.45712 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4cce310-bd84-3ad7-8cb2-7ea0075803ed | -4.34882 | -49.68167 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7561442e-2015-3285-a0de-08b68041cc0d | -1.22618 | -51.75034 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3439dc4e-2334-3b23-bbf4-58bf13bee8ed | -1.6347 | -52.52099 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 944d7b3f-000a-3694-bb83-36fa17ae44b5 | -3.7731 | -47.4927 | 2024-11-14 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce83a73e-9d42-3163-9cf7-78eb9a98c740 | -3.41154 | -50.31484 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d955eb5-2ec3-3ee1-a8a7-7a48c1f2e116 | -4.05157 | -47.22926 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b72483f-8595-35c5-b7f7-6dc4655bcc7d | -2.90235 | -46.8618 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49d96c83-7641-36ec-a0c6-be03e195a5c2 | -4.39796 | -47.26976 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 305a6f5c-c268-364c-849d-64544cf978e9 | -2.64376 | -46.16608 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496aecd6-282e-3e4b-83d6-86c1427616b7 | -1.80579 | -52.16851 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 549b3d18-317a-3cc6-9a5d-dee67116ffe6 | -1.66756 | -52.55231 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2637e99-24e8-3394-844b-84d1fc95dff5 | -1.96323 | -52.10733 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99c9a7e2-1aae-3075-a9c1-f0c41435da2b | -1.10812 | -53.02643 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e6eacc8-10b4-312d-8db2-7f2ffdc110a2 | -4.21121 | -50.50029 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d60fcea-61af-36a7-bb6b-6c0875d91994 | -2.51718 | -56.76087 | 2024-11-14 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 855f7b07-7031-386e-9786-624d06914eb1 | -0.20005 | -51.50309 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b46e4a1-64e2-321f-ac9b-ea239df64920 | -2.67354 | -46.82475 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54380109-0296-3c7c-99ed-2cf1d5ec1cd6 | -3.95702 | -49.01896 | 2024-11-14 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09d22bf4-6ded-31a0-868f-89ba18bb002f | -1.21908 | -51.74924 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27d01273-0584-399a-8bb2-a9c6ee9827ee | -2.74909 | -51.96441 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3033378-271e-35c3-9e5d-abf92e248458 | -3.71483 | -50.60997 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 70732a02-ea84-3b20-b0bc-646fb0ee4054 | -2.64757 | -46.17622 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b407eda5-a68f-390e-8c6d-1070c3c2c005 | -2.92604 | -48.06622 | 2024-11-14 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 038b60a1-4d48-39bb-bb15-54cf69123b3e | -1.11962 | -52.26638 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e57a044-ccc7-34e6-9b6b-d577ac425d7c | -0.20175 | -51.5156 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ab128f5-b92e-3a5e-b9ef-fa1aafdfde04 | -1.84351 | -46.28286 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6af21924-d0b0-3152-8af0-1b193363d972 | -3.67388 | -50.16468 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad780bd-f799-343f-9035-521346bcd4d3 | -1.48952 | -51.12065 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23703e70-6e9c-3464-9ca1-6a47ef87080e | -2.87971 | -51.79538 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 893a1436-721d-39d8-a78a-566204d006ee | -1.38902 | -52.18501 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c010d68-34fe-3bf0-b109-3e0dc1a28ee6 | -3.20588 | -44.43546 | 2024-11-14 05:01:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f532f558-9b0d-3e69-980c-443046f8ec34 | -3.04694 | -48.01006 | 2024-11-14 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d5fdde2-c5dd-35ac-9b09-571533589db9 | -3.0517 | -45.52679 | 2024-11-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4eb4e772-8bf6-3404-9293-4c41c2c2ff8d | -3.20368 | -44.43427 | 2024-11-14 05:01:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a10edeb4-4e4d-3538-beda-09383b76de99 | -5.07423 | -45.51228 | 2024-11-14 05:01:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b6f2dc2-b4f7-3772-98e2-0b04a314c3ab | -1.63815 | -52.52152 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b3e49c2-5355-3d0f-8657-9e1511a293af | -1.614 | -52.51779 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd3a77cc-b926-3bee-a40c-966e79b24162 | -3.43285 | -50.30772 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c4ab256-336a-397b-92bd-fa62ca7e83f8 | -5.07478 | -45.50857 | 2024-11-14 05:01:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0bc62ee-3c10-325a-9fd5-16ce1dd013db | -1.24136 | -52.15624 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765c4177-f33a-32b4-aa26-6272a68b83ac | 1.60995 | -55.90219 | 2024-11-14 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 16793ea3-dcde-3e04-9192-515780ac1fc1 | -5.19219 | -44.35817 | 2024-11-14 05:01:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| debdec9b-5220-3322-831d-b0468a8c7d6c | -4.63248 | -48.90367 | 2024-11-14 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e2cc2d9-0058-3e1e-963c-0e77437e1145 | -0.03243 | -50.78298 | 2024-11-14 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5a4611a-e1ba-3552-b9cb-4bdfde0da9d5 | -4.39887 | -49.77814 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83a0a7b9-88b1-3eb7-848a-d93e14430ee9 | -3.94825 | -48.98795 | 2024-11-14 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c22f1945-8ed4-3e06-8758-1171aadbd645 | -4.40289 | -47.27057 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f74e182-ea2f-30b2-af27-df551dc8c1c7 | -2.66776 | -46.8294 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11caf6bf-66ea-3558-ba3c-b24cbd54bd64 | -2.6413 | -46.17497 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32f66438-25bd-3678-9e49-f2134a83066f | -3.16677 | -50.4597 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c7a6381-f1cc-386e-9dde-0c37c5e90ce8 | -3.29406 | -50.23018 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34a939cc-44bd-372f-9fcc-884d5c3a3fee | -3.01671 | -51.44122 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef582f84-06b1-307f-b4a9-8caab16f0285 | -2.37127 | -46.50015 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0f19842-4e30-3bd4-b26f-f1e5802bcccb | -3.32256 | -44.07719 | 2024-11-14 05:01:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 865164a5-c6c1-3b82-a3aa-06c0e04591b2 | -0.19684 | -51.50817 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c3c05b2-4588-31f1-9c1c-f4ef60bc10ad | -3.79941 | -44.8532 | 2024-11-14 05:01:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 143419ac-c662-31e6-86c2-52ad3a17aed2 | -1.63106 | -46.10226 | 2024-11-14 05:01:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b469095f-1d9c-39b5-80d7-1ffbcfe0b3f8 | -2.11043 | -50.69658 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 700c3128-746f-39ee-8eb7-ff9327a66fc3 | -1.10868 | -53.02284 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f744330-6df2-392c-a2b2-6f706c75d2dc | -3.4104 | -50.30764 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1080a771-93b6-31cb-b834-f452f2a50a94 | -0.899 | -51.71946 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7e4caf7-78d7-3da4-9dd3-8f96052d7b83 | -1.60683 | -52.40489 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8fe8fd1-e9cd-3c42-a53c-3d38def90a45 | -0.20066 | -51.4991 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 282f3796-57f5-3d04-8ae9-eae10b640098 | -2.62168 | -48.07432 | 2024-11-14 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 271fd062-b981-351e-8f4d-f6754e57ed0f | -3.74654 | -50.45298 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README45.md)
