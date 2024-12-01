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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d77aa6c9-59fd-3656-b6f9-434eeb9dacf0 | -2.51278 | -51.83466 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44c6cb58-a45a-3b9d-819a-5ca3bb43cb2a | 1.252 | -50.68337 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66be5a9b-383b-3459-adeb-90edf0679863 | -3.41785 | -50.17673 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 984b536f-37cf-3278-9a9e-20472144f0a6 | -3.51887 | -50.30374 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6da72cff-99d5-3d03-8440-70bb78ce8537 | -2.69393 | -46.86102 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 560095c2-f949-30ae-a6ae-b624a9a8d8f2 | -1.80659 | -44.81314 | 2024-12-01 04:21:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 400280fb-d003-387b-bb67-829b866250a4 | -3.20787 | -53.12701 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 988a924f-d3ae-3dce-9c18-7cc7ad5a3b22 | -3.78865 | -46.70167 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1bbf6c08-6462-3596-82e3-127e46ec5303 | -3.81706 | -46.58905 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46156a08-ea44-321f-ba67-5e321047c97f | -4.03568 | -46.53745 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43d1da73-7f13-364c-9193-0adfc3f792bf | -2.44157 | -53.62899 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44007465-b953-374a-ad65-a4c52546cb0f | -1.52602 | -52.668 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a26453e-7811-3843-8ae7-ea30b9065d10 | -4.03546 | -46.93295 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 97aaa431-9ab1-3529-b3d9-d5a813f031ac | -3.91039 | -46.44129 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8814f94-8cdd-34f8-acb5-bd2034c150fb | -3.98023 | -46.73099 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247d177a-3d10-33af-a697-2c0dfa61378e | -0.83532 | -51.8118 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed0bd1f6-65b7-3fee-9a7f-11146ed24ee5 | -3.84777 | -46.52396 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41de21fc-146b-3ce5-8b58-96f8f2046499 | -3.09442 | -53.72114 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0121ea6-7298-3890-a1e8-5eab08302373 | -2.88757 | -47.44644 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b7491db-4493-3127-b262-b9014c74129d | -2.83521 | -54.09748 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c7f5026-326c-35cc-b210-58aa27446733 | -2.80687 | -45.93761 | 2024-12-01 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df8f7ac3-53ff-3c41-8e1d-ed4c861010d7 | -2.02643 | -52.07666 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3717a537-a9c6-30b3-b60c-c7b1fec83bf2 | -3.89105 | -46.40794 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1865dab8-3ead-30c2-b8dc-0d1582dc5bfd | -2.46009 | -46.57579 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96de0250-231a-3df6-b7dc-0f77cad58b12 | 0.9328 | -50.74402 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf710c49-db11-3f5f-b98a-8673061da8d5 | -3.07398 | -53.81142 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 54842b43-8713-36a5-b906-a534031948fa | -2.23431 | -46.39161 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11adb02f-d373-3fe1-99e5-07e003287c89 | -3.99577 | -46.65549 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 046b30cf-65b7-3374-90d1-fee9c2d9e2ad | -1.70254 | -52.64396 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1653c8d8-c348-3a80-a8b5-4f8497f042f5 | -3.59725 | -50.37897 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7576acbd-5bf4-3e4e-8755-789cce22940c | -3.78579 | -46.69722 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe29a5b3-cd3a-303e-8b7a-c92002f0ab78 | -2.83644 | -46.66856 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b11de0-445e-395a-ad67-323c9865a028 | -2.49978 | -46.23666 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 761daef7-b70e-37c5-b0d2-f2874f6173e6 | -2.67605 | -46.60857 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c11efbb-ae08-3c83-8d38-1eca21e62bcc | -3.45236 | -44.92561 | 2024-12-01 04:21:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eed22df5-d223-3441-966a-08906dcdad8b | -3.37195 | -50.82314 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8631050e-1726-33ca-b956-abe1e947a59d | -1.82158 | -50.90294 | 2024-12-01 04:21:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b524a31f-1edd-3029-94ed-c5d60cca19c0 | -2.72583 | -52.97783 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51019518-78a3-3bf6-96d6-9ed862d3f2c5 | -2.83865 | -54.09741 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46cf20f9-049a-3777-8b7e-030e48a5256e | -1.05385 | -51.76065 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc390313-21ae-3a76-b7ab-3b8177ec2d9f | -4.3487 | -45.93184 | 2024-12-01 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 110c5e77-3a7c-38cc-8017-c057d5f68153 | -3.9878 | -46.63866 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 82cc7f0e-cab4-3d67-9e0d-a606ae7947b9 | -3.16778 | -46.54481 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 989506c3-30a7-3531-aa57-188df8b10df4 | -2.72225 | -46.22852 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ed9bc55-b764-3f17-873f-9e02b1e0e9a2 | -2.90328 | -51.57695 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f932845e-aa51-3989-959b-947cb0bec44f | -2.96712 | -48.04657 | 2024-12-01 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66474e81-18ea-3118-8d03-87e6c1b24619 | -2.60864 | -54.28924 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91ac796d-41ba-366e-82b1-f54715a9921d | -2.62436 | -46.27156 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2d32109-1d38-3a78-9be3-164a740a54f5 | -2.98983 | -45.57639 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 8ce9589f-8864-3201-a291-6f7c73dec401 | -2.75272 | -46.10312 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de5183b0-98bd-32ec-8a29-0b5bb9a21e6c | -3.34382 | -50.23631 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78fbc541-a2d4-3dff-934f-263bf4be9e80 | -2.81109 | -53.04855 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 848efc52-4260-3579-b4cc-f5f77da2d49c | -3.49675 | -52.13255 | 2024-12-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 836b2719-1002-371c-932d-c5a907e6a96e | -1.72324 | -52.48486 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21142550-2acd-3622-8610-b43ff90f5aa0 | -1.10575 | -52.30366 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa5b2577-6586-3eb8-90f1-65b44823d75a | -3.03478 | -48.51811 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 437302e0-9310-3b8d-b77c-fe429d7a9d36 | -3.14468 | -53.83011 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3339a91-8170-3464-a611-b13371cb84b2 | -3.8003 | -46.69555 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50351f10-cac9-3e04-8a6f-91d61d62f34e | -2.89111 | -54.16481 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 240e7e39-15da-39d8-b69a-b62cd5f13329 | -2.92365 | -54.26415 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 376b3db6-7f4e-3807-add9-3d84e69b7664 | -2.84477 | -49.88578 | 2024-12-01 04:21:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e7fbe518-af46-36bf-8dac-986feca5bec9 | -3.8499 | -40.98176 | 2024-12-01 04:21:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 35.0 |
| c5c2d6da-e98d-39af-a83e-e579ea4b75d8 | -2.65499 | -46.12255 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bb03a11-0397-374e-ad83-908e63f706c6 | -1.18137 | -51.77352 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f7165b4-3e0e-3a38-be84-9085700a649d | -1.04855 | -51.73979 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 779f415a-a91b-36b6-af2a-fe43eea5bc41 | -2.59866 | -46.5693 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd99847b-38f6-3c1b-98d9-d03bc3c6d5d1 | -3.00638 | -53.23527 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9200c21c-765b-3b94-a01d-9be5d58efd47 | -4.74643 | -43.71375 | 2024-12-01 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e27a2080-04a4-3ac1-8e91-1dc6375f55c9 | -3.60054 | -49.98649 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31846620-d425-3157-88a2-dc8caeb97633 | -4.5486 | -43.30174 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1cc32d50-2967-3c10-ac4d-a1e5adee8ec5 | -1.07195 | -53.63734 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e82bd7-3cf4-3248-b81b-c8c1f5c5928a | -1.08034 | -46.77594 | 2024-12-01 04:21:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| addd07e7-2279-33cd-a354-83649bfe7496 | -1.09344 | -53.64717 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39ae4213-97a0-3b91-88b8-293e028afd9d | -1.70193 | -52.43952 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6a548dc-c14d-3857-b255-3b36f3878f87 | -3.26845 | -50.21201 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5df80dcb-cf58-382e-aa3a-53c02da4f259 | -3.93569 | -46.72013 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f059648a-7fa1-36e3-94a7-2a366d3e0366 | -3.19966 | -46.58114 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42d705ad-e3b0-3d3b-a925-48a96e13eb82 | -3.77249 | -46.69128 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20df5cba-d6ff-3b22-b324-3f12199c176e | -2.63291 | -46.87983 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e59eb3d0-46ce-37cd-917c-f8a50b7ee1ce | -3.14671 | -49.40511 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 166ade9a-6543-33a4-a355-1f3b8d5c4508 | -3.46979 | -50.26372 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 50814c07-d787-31fa-a63c-3d5f15a3f743 | -3.90981 | -42.42025 | 2024-12-01 04:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c9c1bfc4-0658-3d09-91b0-b70308d893c5 | -1.03756 | -51.73519 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 15c6cdca-250f-363e-a6c7-f8d33dd63d22 | -2.1296 | -46.53392 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ced8ac69-74fe-3bfe-92ba-a7dfb17642cc | -3.99582 | -44.75579 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9b920f0-713b-3f36-979a-9f94ae7561a9 | -1.70505 | -46.20637 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd9df02-cffe-317f-bf60-1b05dfb8b5a3 | -1.85311 | -55.6156 | 2024-12-01 04:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51ed5367-ab71-3b54-8102-3011549de613 | -4.00204 | -46.93977 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d012650-c229-3eb3-b6d6-7155a48fd6f4 | -4.06389 | -46.82222 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3aea501e-3b04-3f20-a7a1-a309f6488a0f | -2.26503 | -53.46102 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90c7cf7a-d10b-3a96-9772-ef21dda6db5c | -3.38928 | -50.11089 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71336342-f391-3344-bf1a-5466a6ffc9b4 | -4.89969 | -41.31734 | 2024-12-01 04:21:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 65b17d14-154b-327b-8206-1ab4329105c1 | -2.47018 | -46.55745 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b1102a2-4b28-3de7-b9e4-4ba0e2a497b3 | -3.26502 | -50.05096 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0eebd734-cb53-3af4-b262-934b90bec7ed | -3.40668 | -50.662 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f84544a-cd60-3e35-a373-3d6a0253080a | -2.31498 | -53.85122 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78b654eb-6db8-3687-b39d-ac5e5760b349 | -2.80057 | -53.04694 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9ea0283-e90b-3a60-bc90-a70bf82488d7 | -0.96265 | -51.6535 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c12a5a1e-5c93-3919-ba48-4ef684b27de7 | -2.57358 | -46.56936 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eb34750-f9ab-3b4a-9cc9-dc1c05b8b24e | -3.00375 | -45.4217 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
