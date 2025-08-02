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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae99ffd3-8afe-37af-92c5-d3e194b4851a | -12.6595 | -44.4882 | 2025-08-02 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| cd69fc43-aca0-3a2d-9aa7-54504bcf6d92 | -12.6784 | -44.5085 | 2025-08-02 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 62be592c-21a2-3940-99df-951f28f3566c | -12.6789 | -44.4851 | 2025-08-02 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 896d4160-3b43-3874-80c5-03b2dd3516a6 | -8.0513 | -43.1001 | 2025-08-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 91fd5d47-36aa-3a16-b636-a93839c12534 | -12.6784 | -44.5085 | 2025-08-02 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6d22bf7d-5ef0-3dc1-9d7b-d06df99e9c37 | -12.6591 | -44.5117 | 2025-08-02 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 88d485a0-1713-3cea-97f0-b111a167b904 | -12.6595 | -44.4882 | 2025-08-02 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 12cbebdc-f743-37d2-aee8-b4639a1cb4ee | -12.6789 | -44.4851 | 2025-08-02 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 806648ea-2f9b-3456-89e3-14454ff9f1ec | -8.051 | -43.1237 | 2025-08-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| a0a8be49-76bb-3233-b80b-18fcac07acd2 | -8.0321 | -43.1257 | 2025-08-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 789dd58d-ac7f-39e1-9bbc-31f682e254ff | -8.0324 | -43.1022 | 2025-08-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 3958c789-f23b-37ef-83af-7596a5f6e1b0 | -8.0318 | -43.1493 | 2025-08-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 442587de-b160-3ee6-bed5-06f7045b7f71 | -13.2273 | -42.2438 | 2025-08-02 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 70f3245d-fc9e-361d-9e89-8fccf7a6fedb | -13.2078 | -42.2474 | 2025-08-02 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 493cac6f-884e-3f45-a354-e67c9035e836 | -8.0129 | -43.1513 | 2025-08-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| e87b779a-c71a-38eb-a09b-550c829ca894 | -5.00304 | -38.68606 | 2025-08-02 03:04:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d3a421c-9357-3293-80df-67ebda355004 | -8.49928 | -37.94534 | 2025-08-02 03:06:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 924456bc-a5d2-3405-b599-17f8d69bcf24 | -8.50416 | -37.94599 | 2025-08-02 03:06:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 07766fe4-16f2-3661-9aca-23247be9e61c | -8.50549 | -37.94639 | 2025-08-02 03:06:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 533ac765-64a1-3d50-bfe3-0c180c8a3455 | -16.69123 | -41.01699 | 2025-08-02 03:08:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| bcae4ef3-cb79-33d0-a293-2798f673bc72 | -8.0324 | -43.1022 | 2025-08-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 71057297-8e71-3538-9f13-a1c05a9967be | -12.6591 | -44.5117 | 2025-08-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 66040dae-7c7b-3eda-90cc-e739fb965d09 | -8.0318 | -43.1493 | 2025-08-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| e2b1ea00-7fb5-3cda-845d-ffc80671a582 | -12.6595 | -44.4882 | 2025-08-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 4540d47d-114b-3119-8088-7ec9ea673841 | -8.0513 | -43.1001 | 2025-08-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 5a07fd67-3377-381d-9411-4dffc8f0b5a7 | -8.0132 | -43.1278 | 2025-08-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| aa6f17b5-f5c8-3123-ae28-45346e758f56 | -8.0321 | -43.1257 | 2025-08-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.1 |
| fa57b1f0-fc2f-324c-a0a1-1ccadbe9bba0 | -8.051 | -43.1237 | 2025-08-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| bc11d3a9-84bc-3be7-b7a4-f89506e782d3 | -12.6784 | -44.5085 | 2025-08-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| aa569bd6-8f11-34b1-b712-c7f586b28412 | -12.6789 | -44.4851 | 2025-08-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 66f7d32c-38e1-3b42-9644-fb11315f1045 | -21.65662 | -41.32611 | 2025-08-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2c7a86b1-1909-3221-b8cc-e25719ccab9f | -21.66046 | -41.32683 | 2025-08-02 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ee630538-fca1-35d5-9316-6ad7b25cc699 | -8.0321 | -43.1257 | 2025-08-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| df944b88-8b79-3d9c-bddb-8a19315994d1 | -12.6789 | -44.4851 | 2025-08-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d6fb8bbe-718d-3be6-8a99-935fb1fcdd53 | -12.6595 | -44.4882 | 2025-08-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 0f8f42c9-9ee2-31f6-b488-dc31bf76490b | -13.2273 | -42.2438 | 2025-08-02 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 5d7e2ac3-d42f-3dc2-9fc6-a844a8f98522 | -8.0324 | -43.1022 | 2025-08-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| d752a4f8-71b9-38c0-8cc2-730a1c1a44ae | -8.0318 | -43.1493 | 2025-08-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 3e46beec-0002-36d9-ae85-259801c25097 | -9.1937 | -45.2886 | 2025-08-02 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 1ca77860-c888-3838-a7ec-04eb1e7051c7 | -8.051 | -43.1237 | 2025-08-02 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 400d7c2b-eab8-34eb-9848-190601628757 | -12.6784 | -44.5085 | 2025-08-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 9c12bdc3-b45b-314a-bbad-f13860c833f1 | -12.6591 | -44.5117 | 2025-08-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 6943edd5-bd08-3f9d-a99a-d861e648dc1e | -8.0321 | -43.1257 | 2025-08-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 3fe470e2-10cd-3ce9-92f5-9a80a9411366 | -12.6789 | -44.4851 | 2025-08-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 0c42a6f0-11be-3e35-b235-0da44bd73d56 | -12.6591 | -44.5117 | 2025-08-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c91ba956-6a24-3a51-9a60-0cef89b6445b | -8.0318 | -43.1493 | 2025-08-02 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 2ad357ad-d724-3657-a58c-01da0e7dce52 | -12.6784 | -44.5085 | 2025-08-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 1e20d264-0cf9-352a-941e-b8fefbacaa64 | -12.6595 | -44.4882 | 2025-08-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| c07be7aa-2e20-308c-bfcb-2c1d8e37f70e | -9.1937 | -45.2886 | 2025-08-02 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 424bce7a-442c-32c6-b248-2163f1ea20ad | -4.2538 | -38.12221 | 2025-08-02 03:30:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a35eb62e-a165-38df-940b-1d7650b7eb4e | -2.93954 | -40.09637 | 2025-08-02 03:30:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 24429cf7-5734-3d5b-9beb-4dab3235ecc4 | -3.58488 | -41.65605 | 2025-08-02 03:30:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a985b6f-59fa-3a5b-afb8-37bc957143c3 | -2.88394 | -40.30172 | 2025-08-02 03:30:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e0ebfb3-d37f-3826-b893-b490b5c1f377 | -5.00355 | -38.68275 | 2025-08-02 03:30:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d87a2d02-018a-35ea-9eb8-9219da987305 | -3.77601 | -41.68457 | 2025-08-02 03:30:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c9c84e1d-99ce-3cc3-995b-2b4e78390702 | -3.58558 | -41.65197 | 2025-08-02 03:30:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c43f5dfc-b49b-311a-b481-1d33483f32b3 | -3.2486 | -43.26308 | 2025-08-02 03:30:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0547ab5-7c2d-35a6-88be-1496b81856fa | -4.2569 | -38.12508 | 2025-08-02 03:30:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ae1d0b4c-d676-37e0-a3b6-2a3f6ecbb258 | -2.87857 | -40.30079 | 2025-08-02 03:30:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e48e296b-2df1-3abf-b975-4703a54c4a82 | -3.9916 | -43.23389 | 2025-08-02 03:30:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67280bdb-e795-35d3-9f3f-8e5a3d29abc1 | -3.59137 | -41.65301 | 2025-08-02 03:30:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3f3da72-b664-396c-8e07-b1d8a04791d5 | -3.99247 | -43.22889 | 2025-08-02 03:30:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0c2df3d-68be-3937-9678-8c0f39aed029 | -3.59716 | -41.65409 | 2025-08-02 03:30:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 36e3f0b3-58f4-3d4c-92ca-5ca371e8c4e1 | -2.93901 | -40.09965 | 2025-08-02 03:30:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d0d9c581-3692-3707-92d8-041d93e4ccbf | -5.15108 | -37.73528 | 2025-08-02 03:30:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1c839a9-c9f2-3c99-888b-0c4b8a27606b | -7.24767 | -43.38658 | 2025-08-02 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03380e32-d6b6-3038-978f-2f2f66ccd860 | -6.51992 | -42.8191 | 2025-08-02 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e99f825-8b83-31ee-b35c-b078511498a4 | -8.05485 | -43.10801 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0e228bc7-6673-3880-bafb-8a30411f71a3 | -5.57118 | -43.61163 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 34dd45c6-d04f-3168-a499-03c16aa0d5be | -10.02678 | -44.71478 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| da8b0228-f211-3078-8cc5-48b35a535358 | -9.19694 | -45.29998 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 554f5b6f-fc4a-301c-bfc1-6d9de7654ccd | -10.03156 | -44.71454 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cde7e3d5-2888-32dc-a36a-c6682e7801fa | -5.65765 | -42.58003 | 2025-08-02 03:32:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 770ba63d-e156-3e74-aad9-8e559567d8f6 | -9.58766 | -43.84369 | 2025-08-02 03:32:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c55b5a00-d7c3-3dde-ad73-38458940e50d | -8.02308 | -43.14685 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 99ffeb0d-3c3e-3137-a46d-b3ca36fc0f13 | -9.19147 | -45.29263 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 965b35b0-8bc2-36f7-93e6-63bf47b88f94 | -7.26598 | -43.38995 | 2025-08-02 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 73ffb977-5166-31c3-9870-147798b58f00 | -7.88085 | -45.53658 | 2025-08-02 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9fe9d283-4e95-396a-9748-25fbe8a64fc6 | -10.57719 | -45.27661 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d0a17bf-8e30-3e38-ba5b-97924224fc42 | -5.48316 | -42.15742 | 2025-08-02 03:32:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb926b85-8a64-3f74-a514-ffe600c94e27 | -10.59144 | -45.26804 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e427b98-ddc8-3f67-8f8f-c34081fcab40 | -9.39608 | -45.49755 | 2025-08-02 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 64dda548-68ff-3b8e-bb15-4838b4c10ba1 | -10.03787 | -44.71585 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d63037e5-c5cf-3510-ad3b-833545d33a90 | -9.05423 | -45.06322 | 2025-08-02 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 893e0fd7-5222-3d15-b7b9-8279efb16efd | -9.06082 | -45.06429 | 2025-08-02 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11d55792-83ef-3115-b132-406ceb81ff34 | -9.38568 | -45.50026 | 2025-08-02 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d8dcd21-ceb2-3671-93ad-975effa285df | -8.66671 | -36.23307 | 2025-08-02 03:32:00 | NPP-375D | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0d96e986-d0c8-39a6-a334-86763a181375 | -6.88592 | -40.87772 | 2025-08-02 03:32:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d07c9755-8b82-36fb-8d62-67d94e974d7c | -6.70001 | -43.0801 | 2025-08-02 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d74e057-162a-364e-8ccd-41acd1ad64b6 | -9.38451 | -45.50632 | 2025-08-02 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f32d55e9-325a-3619-88b3-1b495ae804a8 | -8.04141 | -43.11438 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 23991f32-55ce-3f26-a576-2f738258251c | -8.03549 | -43.11327 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 85f910e0-8417-3b24-b2f4-4f0f72b93dfa | -10.5923 | -45.26814 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d6a2076-8bab-3cd6-9721-3bfde2e92036 | -9.18907 | -45.29021 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 23cb908c-0af6-3418-abee-e28070f18d9c | -6.52667 | -42.81577 | 2025-08-02 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5b5f3c2-cf96-31a7-90c8-2bc261a915d6 | -10.59251 | -45.26278 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac074af3-c43f-3249-8edf-4c9f0117906c | -9.58728 | -43.84265 | 2025-08-02 03:32:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10c935c3-419a-346e-ae68-c026ac8c818c | -8.04813 | -43.11119 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b9b0e9c4-faf1-3132-8256-accd8f767ae4 | -10.46171 | -46.9592 | 2025-08-02 03:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfa45da4-cc47-3e1d-a830-1b8835c4d52d | -5.56449 | -43.6042 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
