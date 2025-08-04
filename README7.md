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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f18d6030-527b-3395-8b84-a80a28277c52 | -6.6329 | -59.9649 | 2025-08-04 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 56ac994d-a83d-39f3-b1ec-b22500978c67 | -8.0129 | -43.1513 | 2025-08-04 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 766da5c1-ad14-3630-bc85-aa0cb8ff66a0 | -7.9937 | -43.1769 | 2025-08-04 03:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| ce59e0e8-322b-3e3d-af62-bc21a9a25af2 | -6.6329 | -59.9649 | 2025-08-04 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 0b854c74-9296-31c7-85d2-4be1b3fc894d | -8.0132 | -43.1278 | 2025-08-04 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| fd821185-c49a-35e3-80d6-2e30caa8e3bc | -7.994 | -43.1534 | 2025-08-04 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 156.6 |
| da50b48d-ac91-3f2d-bc5f-febd2c92906e | -7.9943 | -43.1298 | 2025-08-04 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 46af148b-f963-339c-9217-32353f5914de | -4.7346 | -44.4457 | 2025-08-04 03:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 59932800-e533-319f-8bd1-73647fb77016 | -4.7346 | -44.4457 | 2025-08-04 03:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b0f20590-f439-3398-9970-91676ed3d87b | -8.0129 | -43.1513 | 2025-08-04 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.3 |
| 62361151-c30f-3399-add6-2dc78cd0957b | -7.994 | -43.1534 | 2025-08-04 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| 97e8008e-73d1-3d4c-87b6-f626fbb2a624 | -6.6329 | -59.9649 | 2025-08-04 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 7aef4dcb-60f1-3051-9855-d13f8e56eaff | -7.9937 | -43.1769 | 2025-08-04 03:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| b793a246-5f5a-315f-b18e-7d716d7bd429 | -8.0132 | -43.1278 | 2025-08-04 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| b8ec2ceb-1f30-34d5-bb22-766084c52d0d | -13.0535 | -56.8947 | 2025-08-04 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a1145170-b5db-3b42-9a04-878aeabed176 | -7.994 | -43.1534 | 2025-08-04 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 3e1283a9-02ac-3796-b7d2-8f1edd33159f | -7.9943 | -43.1298 | 2025-08-04 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.7 |
| 0ece04aa-b86b-3e8c-82f8-c602847836ed | -8.0132 | -43.1278 | 2025-08-04 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| f706782a-bd44-30ea-b44d-443ed4b459ac | -8.0129 | -43.1513 | 2025-08-04 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 0e0ef57d-df02-3ea3-abe0-53ebde4566a7 | -6.6329 | -59.9649 | 2025-08-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| c7bf0fde-cf28-3e91-bf47-6526c0a9a7eb | -7.69195 | -45.12864 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ee77ca4-7c62-35b3-95ab-3e7352398d3a | -5.98586 | -45.52348 | 2025-08-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b310ced8-f8e9-3ac8-b857-f59bfdc49d16 | -8.02017 | -43.173 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c321496-6210-31e8-ae67-d13447e30ed2 | -8.01217 | -43.14252 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| a72daeab-c86e-34b1-b560-b285050b6ca0 | -4.12368 | -47.64599 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35931572-62ee-3158-98c4-a7a0ff6eb7ac | -8.38247 | -46.941 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 99ca928e-e02b-39f5-8a80-c49ca3c461b9 | -3.66264 | -41.12605 | 2025-08-04 04:08:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38c03535-2d44-3dfc-9f27-f90946c7bd1c | -6.19688 | -43.76231 | 2025-08-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b50c3026-5d97-315c-91f7-5c0167d04329 | -8.73645 | -46.4191 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3a860a2-3348-3267-b94d-a2abd063cabb | -10.57487 | -45.26939 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2cd5db5-90e5-3a36-a908-6992f7816714 | -7.56189 | -44.89649 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4abcee5-fa8b-33a7-bc8d-a8d0c438da05 | -10.8128 | -44.34803 | 2025-08-04 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a33760d1-77d7-3b6e-b8ca-b4011a7badf9 | -4.73838 | -44.43922 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 69711c73-0f07-328c-9e00-4df80f31f62f | -8.30761 | -47.52213 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f379840-1f53-348b-a6f4-d673cb2e1e51 | -7.09378 | -44.36274 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c14619a-d57c-3772-b21e-8f090fdf6261 | -6.69174 | -44.35618 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdfaf65b-5888-360f-b359-eab2d31eebad | -6.19749 | -43.75856 | 2025-08-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 843a200f-3653-3a70-8e2d-54d72843d1d6 | -7.48464 | -45.05277 | 2025-08-04 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55bb5cac-d420-31a7-932d-2bcc2528a812 | -4.74132 | -44.44394 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 23b8abee-ca31-320a-8aa7-b0839583b0ad | -4.7433 | -44.43151 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71624627-2345-35d8-a8ff-7b9af51df9d7 | -6.69892 | -44.2448 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf161b74-4a37-3d28-90ef-a7a98a77d768 | -8.73725 | -46.4143 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 298a13c1-a04e-3a12-98d9-b9d28b28e5e3 | -6.55835 | -43.91957 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0483d956-d141-3963-8973-c2e544fc0317 | -7.21102 | -41.85588 | 2025-08-04 04:08:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c1bd761-0721-34a6-8895-c67bf5bca9cd | -7.9943 | -43.16887 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ccc2b74-9c4d-3bea-a0b7-518f7a148f08 | -3.28273 | -48.81384 | 2025-08-04 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1067fcfd-7fbf-3303-b4f6-719506a73390 | -7.82986 | -44.94711 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29e96fbd-5b83-3555-a9b7-3f8e9a7a44ef | -4.13515 | -46.4603 | 2025-08-04 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d93348b1-d0f3-3351-9658-60687d6a5e68 | -7.11251 | -44.66987 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0ed1a6c-2834-3fe4-83cd-6a1cbb1d9c65 | -6.26262 | -44.07311 | 2025-08-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f60f768d-30d7-3a44-837a-d6762e4a6f47 | -8.88968 | -44.78862 | 2025-08-04 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef685976-0e7b-31d1-ab7b-2725b7af8660 | -6.56444 | -43.37952 | 2025-08-04 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df053d12-1a67-3769-a65c-6aadd5077fd3 | -6.57295 | -43.36984 | 2025-08-04 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf043f58-8750-3db2-bc09-d5d28c14c038 | -4.31012 | -48.10206 | 2025-08-04 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fad0eed2-a273-31eb-bce4-5f9a0a2e5b8f | -4.74918 | -44.44091 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a58a770b-4d07-3dc3-b70f-2ed08f7b4fd6 | -7.69367 | -45.1278 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92d9dd68-a696-3618-8a64-c1601e9f3828 | -4.11929 | -47.6502 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 210f40f1-2f24-3a10-8120-1cea123ca343 | -8.02031 | -43.12931 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ef6cd86-5c5c-3dfb-9529-42f9e9c991d7 | -8.38643 | -46.94163 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 6dd12e4a-393c-36ec-a0a2-3325cb110b0e | -7.41478 | -45.26704 | 2025-08-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 335ee92a-9feb-3131-b6b4-b55e59ff7ebf | -6.5211 | -44.87624 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18b4d0bd-36d8-3a04-9624-2f957b1f6a50 | -7.34237 | -44.68514 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01883d1d-3102-3008-9027-f1c7b07feb0e | -8.01683 | -43.17247 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc13e0df-01b8-35db-90b0-86b7a1b4d10a | -6.6911 | -44.36015 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac2f45f0-761a-3f4d-926a-ad59f2729526 | -3.28035 | -48.8167 | 2025-08-04 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77256490-34c2-35b3-85d5-29b0d71d1e13 | -9.62303 | -43.85797 | 2025-08-04 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b4f4d61-f719-3848-9674-3824f361ea49 | -7.33883 | -44.68456 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f2a45f6-5788-3fbc-9f42-1701087e6553 | -6.32285 | -45.65033 | 2025-08-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81375892-5c00-3568-b1ac-5e3fe07d73f6 | -4.74559 | -44.44033 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25184a51-7ca8-35ad-9391-2ba37b31de6a | -5.87579 | -50.14736 | 2025-08-04 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1512545-79a0-3a64-8611-ac2929d6832a | -4.13925 | -46.46092 | 2025-08-04 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ebad39-219e-3d0d-b6d2-9f91acd623cb | -7.30418 | -44.6752 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa631d3c-d984-3b78-bdf4-a501572a6ef3 | -7.69263 | -45.12439 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc62540f-fb6b-3c88-9bd7-5a4ece0be704 | -7.78248 | -45.22649 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ccab7f3-b652-316e-971b-17a2f5c9be3e | -7.99758 | -43.21317 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ac2818e4-8e3f-3c80-8e1e-d3a335abd543 | -7.08077 | -44.3765 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc41842e-1b66-3b93-9ea1-b3ca4940e730 | -6.06589 | -44.68061 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 406fd412-7ea8-3c22-8997-cf0ce80e2d48 | -8.7358 | -46.3996 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d03bcc0d-9a79-3d5e-9a08-261169cc16df | -10.56368 | -45.27167 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2a63801-4534-330d-96e2-35277c92b934 | -7.78302 | -45.21506 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d695d425-c014-345d-928c-bc8c1e6c4065 | -8.00159 | -43.14448 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.9 |
| bb8f3413-4b86-310c-8fa3-26900008832a | -8.27115 | -47.3688 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 421a6788-e65a-3030-bb58-cd5e2617fe98 | -6.06656 | -44.67647 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 667b43ce-cedd-3e7a-976b-13347e919175 | -6.24953 | -44.42173 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc3db4c8-06e4-310f-a231-7d2f9240c443 | -8.38818 | -46.93139 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4945fa4-e8ed-3f08-b24c-2c7583847c78 | -4.73904 | -44.43507 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa57a1d4-ea42-314d-9393-b1c7f3a8b284 | -10.2515 | -47.99561 | 2025-08-04 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3253a48-40a5-3844-b949-be44e999ed45 | -5.88092 | -43.74025 | 2025-08-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ae1e098-76c5-3770-a1be-7a9c87d7c033 | -9.40045 | -45.49866 | 2025-08-04 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04482a7d-4048-3357-85ed-e308002cfb28 | -7.99374 | -43.17244 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4fc6eed4-a4f8-3aa0-8f8f-a3ea2b95ef0d | -6.62649 | -43.66874 | 2025-08-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98dc517c-7c7e-303f-ab3b-2ac1bf7da5a4 | -8.51615 | -44.74541 | 2025-08-04 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b39f9cfd-bd01-3937-bcbd-e3200c6b2e89 | -9.39546 | -45.50639 | 2025-08-04 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1915289b-f8d2-3927-a454-a492e75db129 | -7.21379 | -41.85986 | 2025-08-04 04:08:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21baa011-d578-39b2-a6c1-77f31c557454 | -7.40681 | -45.27006 | 2025-08-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2866c6a-2109-3980-b70f-6974813562ce | -10.24444 | -43.88481 | 2025-08-04 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7967fc82-0dfb-3223-9db1-1842cfe8f07a | -8.36258 | -46.91978 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9603422d-c959-381b-a49c-6580be14c648 | -7.11274 | -44.67067 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 900d9307-52f2-38df-8899-64bddb4e35e9 | -7.65056 | -49.84219 | 2025-08-04 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c585e2f0-edb2-3e1f-a592-a0cb7d1d3dbd | -8.0049 | -43.16687 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
