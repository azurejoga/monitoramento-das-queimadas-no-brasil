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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc48861b-ba96-361c-aac9-75b043c6384d | -1.63803 | -53.31594 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ddc7515-ea17-3e85-8dcd-90955c2e6bcf | -1.74731 | -52.38231 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7fe3e8c-d073-33a9-984a-80490bd5d035 | -2.58517 | -54.23064 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0989ee65-1ecf-3b82-9167-97081a03b9cc | -2.96089 | -53.92157 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 061d4e01-d339-34cc-973c-a0f049093d7d | -3.86431 | -50.05289 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9ca014c-9409-3d97-97c2-b26acde46010 | -3.84563 | -46.64688 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8dbc999-881c-3e9b-8933-e7580686fe78 | -3.28012 | -53.83619 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dca3905c-9564-3163-a2a3-8cf31688cbfb | -1.2101 | -51.94625 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4287a3bb-20ab-3881-8ff3-b2c9da68f74d | -2.19576 | -49.30091 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64f5c2aa-2c78-3c4f-9c99-45391bd09fd4 | -1.5218 | -51.62568 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 74a60479-1a40-38fb-adae-f137a4e12b37 | -3.95765 | -50.20143 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a282a36f-ae91-358a-b0d4-09a6c0aa5d66 | -3.84203 | -46.64215 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4796049-9fe8-3bc2-a3a2-eb4bdb239114 | -2.08926 | -50.35636 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 882c82da-5006-31fa-96ae-ddfef1f76cd2 | -1.4389 | -54.89803 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6648c7c5-101b-3332-bad7-96f86ecc6bcf | -2.85909 | -51.273 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 192676d0-4862-3025-a65f-0e18aaa2628c | -0.28326 | -51.60782 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 388bafcf-6007-30df-9483-b436ef448925 | -2.45282 | -49.09086 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f4620e96-84b0-32aa-b710-a3dd54f8fe97 | -3.94472 | -45.99416 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cda33e8a-2e47-3443-8be4-7798cd80a679 | -2.03997 | -52.10054 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d33d487-345b-33fd-adfa-4d0839d36eb0 | -0.8813 | -52.76494 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c71db756-737b-33d6-914d-7cdfd54a712b | -4.51956 | -45.73529 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b8bf5c5-ef9c-38b3-882b-d0eca6fd07fa | -3.77516 | -52.09812 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75d6144b-d075-33dd-afc9-5713099049cf | -4.38383 | -55.07314 | 2024-11-24 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a16b991f-8482-39bd-ac42-e745b9708b10 | -1.30932 | -51.74379 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a680383-2edf-3da2-89ab-f76f0ceb2c25 | -1.4812 | -51.10151 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 692d7776-eead-3553-a109-03c53e0464f0 | -3.08883 | -51.3266 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fccb4b08-ace9-3562-b591-86c03089845b | -3.26145 | -53.26875 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54c0df6e-4358-349b-afc7-b35b6392427c | -3.28596 | -53.26529 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dabe05d-126b-3eb3-a58d-95447c5453a6 | -3.30122 | -50.04713 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7240f27c-0b1c-348b-b85e-6b03c1fbcb43 | 0.41327 | -50.8591 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb19f05c-43d9-3d02-86fe-78a44ca4e889 | -2.16209 | -53.77625 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b728684b-63c4-319c-86f6-74cfa0bc2583 | -2.97079 | -53.85925 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9b3e887-d191-3158-a01c-017f8b3123f6 | -0.80206 | -51.5975 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bab25e1-2198-32c0-9c99-9b108d5cd6f5 | -1.08718 | -51.64215 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23d1289e-9902-3869-8f0d-1341c35a8e39 | -1.49649 | -45.85914 | 2024-11-24 04:53:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73b3e530-1d55-3bc4-a6bf-94d9f3a93d18 | -3.10289 | -45.78117 | 2024-11-24 04:53:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 062e6cb2-395a-3ce3-a390-36810a0ab702 | -3.29419 | -53.85698 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 779207b9-1828-318e-8866-eeff16fdab87 | -4.69547 | -45.84951 | 2024-11-24 04:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff955174-089f-366b-be28-0a47af7b844d | -2.44571 | -49.08979 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bce0514a-358c-35f9-82c0-f04c70f148eb | -0.8125 | -51.5956 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 618a356a-40cf-3c80-91fa-a5466d2a53c8 | -1.0532 | -53.66264 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90479a71-c70d-3f74-b16e-3221893a8134 | -3.19135 | -46.55748 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0da25d10-dce2-3d87-876d-103692d68a8a | -2.23917 | -46.81546 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2d30b71-cc7b-312d-b394-87a6c5572ed9 | -1.98179 | -46.42669 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4091b6ef-d997-3627-9d26-edbdab402378 | -2.77288 | -54.06678 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b999d42-4553-3f44-912b-cd6f551d9746 | -3.10045 | -53.03911 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93bd6bfc-cb63-3e3d-be8e-32235915be54 | -3.69152 | -51.56255 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a756521a-942f-3fcc-a453-b2f8d3c2b209 | 0.41827 | -50.84777 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4011331-6650-3e7b-ac1f-4c5b0569107d | -2.83959 | -54.06605 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba58242f-4f34-3942-acf7-c99d73393df5 | -2.17431 | -49.08702 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fdd20a8-709e-36f4-9e22-95d4bf0289e1 | -3.89479 | -46.66234 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0f65f9d-fb7a-347d-bca0-a3502207db03 | -1.6195 | -53.30199 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 715f25b1-b275-33b8-af16-d620b0bcfb98 | -3.2976 | -50.36815 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc30b7ce-ba4a-3ec2-8a1f-41a80c95846a | -2.63262 | -51.7471 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 062ce53d-abd4-3577-8adb-a7012a1903a1 | -2.57647 | -53.97617 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9df14fca-b567-375c-ae86-b4b413baa93c | -4.5402 | -42.90644 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15cc81cd-9b2b-3569-a12e-a56169979163 | -2.17459 | -53.78572 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69680c65-4918-30c5-a1a5-2f60e70edebc | -3.68122 | -54.58485 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73bf46d7-5e45-3d8a-b126-8643483f5cd7 | -1.2309 | -51.79139 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cb4157e-ff9a-3e74-a5d0-5288de0fbd7a | -1.61405 | -53.30433 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbe3bd9b-b0b2-3996-86d5-1811fbcf3d05 | -2.68088 | -46.15791 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1149c00c-a265-384f-b938-90d2217936f7 | -2.69941 | -48.82925 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 411a9b9b-2c41-31c1-8915-558ff6f78195 | -2.73801 | -49.11884 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0996fddd-4cf2-3682-9c5d-df425fc6566a | -5.00169 | -42.94986 | 2024-11-24 04:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 391c32ba-32c2-3216-90ea-0be4bfbfce87 | -3.98238 | -49.93038 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 490abcfc-7b43-3482-bb24-63ca9df9a1b9 | -1.13375 | -48.34071 | 2024-11-24 04:53:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8a5abea-0e7e-36f9-a5c4-038b62b860ba | -2.30321 | -49.04877 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db5deb62-ec26-3498-9eac-32a8fc871e9e | -1.92619 | -54.42685 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73a96d94-e007-38c6-9f78-68951d4ce666 | -1.31228 | -49.38894 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| caae4358-aa9a-3554-a9e1-83c8816a783d | -0.57476 | -51.72384 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99b5f92c-00e2-3058-b5d3-4b81a4dc1cbc | -3.23127 | -54.16411 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cf1474f-38c3-3d88-bad2-fb393de5de86 | -2.86996 | -45.82952 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1c37747c-ac81-323a-91e2-39b4a06aa94c | -1.5251 | -51.62619 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2e48d6d-6f39-30c8-9216-02fc9a9a90f7 | -2.51573 | -54.11627 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c675c17-a7cb-332c-b1c9-459c4326db70 | -3.29886 | -50.08508 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48afd6ce-d698-31e4-a354-be3cfc0aea97 | -3.08296 | -54.54459 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7201afe4-6593-3cbb-8465-632eef7d58cc | -4.0387 | -54.62713 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75dad591-14ef-35dc-8125-2fd713348f11 | -3.77846 | -52.09863 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 531a596b-7011-3fc3-b424-eaf80b8114e9 | -2.28954 | -50.58065 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5db1a964-35f1-383c-ad8d-4c428413732c | -2.57911 | -54.04925 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c619f403-6d65-32c7-9739-a07bb78e800f | -3.64168 | -50.22722 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a66d217-a9c9-30e2-bd4b-fbf67f7f4c87 | -2.41298 | -49.11352 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edda3da6-49db-343d-b3e1-ee04da9a8733 | -1.04669 | -51.81493 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a22c725-3137-3fed-81d0-886ce069379c | -3.62195 | -55.30167 | 2024-11-24 04:53:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f717df6-4ecf-3848-a086-2cdbe7dadfe0 | -2.62183 | -51.79468 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7320c344-513f-3e99-8778-fe63cc3b4eac | -3.05514 | -45.1729 | 2024-11-24 04:53:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e919f22c-4c40-3b40-ac73-4d217b7d7d67 | -2.94653 | -51.41125 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76ec4d9b-929d-3e6d-a505-2f2639dd1bc0 | -1.77916 | -53.64248 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fc5a8e3-aee2-30f1-a763-3779b39e00b9 | -2.24249 | -50.47133 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3095539-ba44-33c9-8add-1fc89b9b0ae6 | -3.55415 | -44.97992 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd1f498-1ab1-34f6-953e-e9fa6155274f | -3.91509 | -50.57335 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43323037-9a7b-3177-a426-eeb3bae2a327 | -4.63166 | -49.66777 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0a5ec3-dd66-3ab0-b42d-4653a401e520 | -2.59908 | -47.02933 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a03ea14a-845a-3e3a-a71c-a6720f90fd9e | -3.86848 | -47.06169 | 2024-11-24 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7fc1f4e-8dbd-306d-9538-9e40bd6b1c05 | -1.11909 | -53.39852 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72bbc91b-6e92-35e3-b687-18d173bb64a8 | -3.54585 | -50.39461 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a86292d3-aebb-3ab5-bb43-9738780ea330 | -2.64694 | -49.85371 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e2f6aa1-f006-38cb-be60-4c5607cf5d43 | -1.46865 | -51.13851 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0c3e7df-0c79-3740-8e15-139d57c0e43f | -2.71356 | -48.66385 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 34518866-4451-3746-bba5-164f3ee518af | -2.08399 | -48.87762 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README58.md)
