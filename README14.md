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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12e7c2ae-bb62-3043-bb13-959f10c81beb | -5.23004 | -43.19069 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8860d685-66ee-3f7f-b30c-3d03c28a998c | -5.22572 | -43.18203 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 856f1911-1dce-3615-8d47-a977a02f3446 | -5.22508 | -43.18576 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0aa2417a-a6b5-3a58-90a2-e2fa2176d4b1 | -5.22441 | -43.18958 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0eb64509-dca3-3d4e-9a0d-043b3d60f9df | -5.22374 | -43.19349 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c9ca47d-5f39-3fb6-842a-42c820aa38f5 | -5.22008 | -43.18106 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ed9ac4d-e867-3949-9243-81eaf3708122 | -5.21943 | -43.18478 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36588108-cde7-350f-bbe7-f9b58be4f2bc | -5.21878 | -43.18854 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4f1ed25-f4a4-326c-8ec6-d51474481e00 | -5.2181 | -43.19241 | 2024-10-23 03:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c61f0fb6-0ceb-3782-a1d4-d8e9fa76c8a6 | -3.40567 | -44.15821 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cbfcf1b-1722-3dbf-91f9-983d6a9825ae | -3.40496 | -44.1552 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 551ce737-275e-385d-96d1-7eaad2bacf9a | -3.40414 | -44.15992 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b2a8ffa-e050-301b-a619-41fd9aba3316 | -3.39948 | -44.1572 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ebc1c35b-fc1b-3a42-bc7c-40b79a281801 | -3.39795 | -44.15894 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90f16f1d-aa15-3c30-b7fc-e2a355ea895a | -3.30441 | -44.15487 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5eb49f8-5fb3-3440-b3aa-a3f7a01f5596 | -3.30072 | -44.15094 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7d931ed3-5878-31f1-901d-5cddc89a6f8a | -3.29992 | -44.15574 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4831f7a2-5faa-36e3-96c1-6601ad5907e4 | -3.29904 | -44.14905 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d6e8ab08-a8d6-316c-8b5f-9c8ae1edf834 | -3.29822 | -44.1538 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b5176707-382a-3037-aca7-743a53228b20 | -3.23981 | -44.41602 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0d51f82-5cd9-3868-a447-85ec5ed1b84d | -3.23706 | -44.41759 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17687c37-4d41-3df4-b096-54dde5f4f35f | -3.23353 | -44.41489 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 931c2691-6c04-33ef-9925-61bee651f40f | -3.23078 | -44.41641 | 2024-10-23 03:34:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5582937a-8404-38d5-adbc-ea3d8e681a08 | -4.67741 | -44.6008 | 2024-10-23 03:34:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46a36c97-5dd2-3d45-be1b-4dd904d14f44 | -4.67658 | -44.60558 | 2024-10-23 03:34:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5fd642c-9c88-3053-91cf-348d00f41fc4 | -4.67577 | -44.61029 | 2024-10-23 03:34:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44a574b2-5268-3137-9e9f-13c52bc4458b | -4.67119 | -44.59969 | 2024-10-23 03:34:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e56adf0-5a1a-3900-82dd-e35693595b38 | -4.67037 | -44.60439 | 2024-10-23 03:34:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 884b964a-7c71-35b7-a224-44074c63ed47 | -4.66954 | -44.60914 | 2024-10-23 03:34:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1f4d6cf-bf67-392a-9aac-a93c691d785d | -4.66872 | -44.6139 | 2024-10-23 03:34:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 272bad5f-dabd-351b-be27-e5035fcd3993 | -4.85656 | -43.25673 | 2024-10-23 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bca74669-bf6b-3910-aeeb-1c5d7cc4513f | -4.85588 | -43.26061 | 2024-10-23 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 958ba332-17db-3a16-824e-29b82b3b6131 | -4.85084 | -43.25583 | 2024-10-23 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f31b2ac-1cf8-3cd4-b0cc-3d946bd80cb1 | -3.64552 | -44.32956 | 2024-10-23 03:34:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46a07677-1248-32ac-82af-d9d19d776952 | -4.10742 | -44.23287 | 2024-10-23 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b78c615-d85b-32eb-9199-c037bd59f56f | -4.10703 | -44.22918 | 2024-10-23 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aef59be-29e9-306d-8995-93cdc31ec608 | -4.10662 | -44.2375 | 2024-10-23 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 314025d6-dbe9-398f-899f-8f4bd81efa81 | -4.10622 | -44.23378 | 2024-10-23 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d9f92b7-78b9-3b8d-b7a5-17225501f617 | -3.96773 | -44.0571 | 2024-10-23 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed248468-2d37-3c67-b278-1bc8cec45744 | -3.96164 | -44.05608 | 2024-10-23 03:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97255ba8-41dd-3092-a7e0-099cc3e129dd | -6.25812 | -44.14823 | 2024-10-23 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffbb35ed-785e-338c-bb93-0b3a3ae51a1e | -6.2574 | -44.15231 | 2024-10-23 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c908bca3-1cc5-36d7-9eca-79ac75d73d68 | -6.2537 | -44.13883 | 2024-10-23 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba85bcbd-cff7-3444-a2cf-bca9c5d02350 | -6.25297 | -44.14294 | 2024-10-23 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f989033-1c42-3d35-a8e1-b55f385476f6 | -6.25223 | -44.1471 | 2024-10-23 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ad1b6cc-728b-3f06-b80d-60201657c4a8 | -6.25147 | -44.15137 | 2024-10-23 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 825f50b3-d971-3047-99cc-ace141bf31bd | -6.07248 | -44.62735 | 2024-10-23 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95c5ffc2-4ae3-3848-8c2b-ab1af0293ba1 | -6.07197 | -44.6298 | 2024-10-23 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ac8f716-deb4-3d83-bfdc-811fd04a6e05 | -6.0716 | -44.63214 | 2024-10-23 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 126c769d-ce17-3eda-bdb8-363cf2851219 | -6.0664 | -44.62614 | 2024-10-23 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 34e741f3-3f68-348e-9c2a-882d366722cb | -6.06589 | -44.62856 | 2024-10-23 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 42fb2a1f-5bbe-3f2c-88e1-231c4081087e | -6.06553 | -44.63091 | 2024-10-23 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 53ab83e1-8a8a-3354-a6b5-ad2e78c6655b | -5.50646 | -43.68968 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 980a3133-177f-3104-ba67-e51358d9542f | -5.50574 | -43.69384 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69d42085-efea-357d-a68f-862db9b6b0f3 | -5.50508 | -43.69135 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf8820e3-184b-3f8b-bd52-5d472060b0d3 | -5.50502 | -43.69801 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 425f7dde-adb2-3b21-a3a7-5fd751a56a9c | -5.5043 | -43.7022 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10d4075e-4bcf-33a6-8701-8bdeaec5540d | -5.48749 | -43.66109 | 2024-10-23 03:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58ff1457-d55d-35c5-86b7-8cd5fa45babb | -5.58119 | -44.88094 | 2024-10-23 03:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 837ce4f3-ebc3-3272-a893-07cfa3262f11 | -5.58028 | -44.88603 | 2024-10-23 03:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb829af5-5850-3f54-99ae-fd4b81e9fb90 | -5.42115 | -44.79696 | 2024-10-23 03:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 401ed738-f1d1-32ce-b76e-d92ae4228cff | -5.29574 | -44.29659 | 2024-10-23 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41ad2462-aa13-388b-b73e-37cca7f3ad05 | -5.29494 | -44.30103 | 2024-10-23 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8822e4b-ffed-3ab6-99d7-cb5d0f3bee1d | -5.09642 | -44.21557 | 2024-10-23 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d24d7a7-381b-3f4c-a794-8adac80f7577 | -5.09565 | -44.21988 | 2024-10-23 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efa660ba-670a-39cd-a95b-5f451a392653 | -5.09531 | -44.21529 | 2024-10-23 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8d61bd7-219a-3b54-b1a3-fe33a4148979 | -5.09456 | -44.2196 | 2024-10-23 03:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 116c4dfd-e2c4-3cdb-b0f2-cfdd9ed69c6c | -4.96485 | -45.87601 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 225457ab-9dd9-3396-b217-b78c5a3d5595 | -4.95822 | -45.87444 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b808e84-afa7-352b-b2dc-3132ee8b0efc | -4.86229 | -45.85695 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b572729-baf8-3529-ba37-e45b6cc8a20e | -4.86122 | -45.86293 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0436d728-ce44-37b9-8eff-69a0da8a217c | -4.78001 | -45.12046 | 2024-10-23 03:34:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92830ba7-1f61-3272-a76f-3a25346b8d10 | -4.77357 | -45.11942 | 2024-10-23 03:34:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 335f7055-ceb2-35aa-94b5-adb7bb308d33 | -4.75833 | -45.76525 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a87251fe-9e6a-35bc-b378-1639830211ee | -4.75729 | -45.77107 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95b4e307-4fe9-3dc1-860e-824f0bc82be6 | -4.72978 | -45.73269 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf197e7a-35da-34a4-a6d2-a9462b4a73dc | -4.72866 | -45.73893 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69064c78-51a6-3a28-94ff-a971f42e7496 | -4.72797 | -45.7262 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 403e053c-216f-349e-b85c-86c37973fee6 | -4.72692 | -45.73227 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4ee6d9ec-0a00-3097-9021-2c4f59bdf386 | -4.72583 | -45.73856 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2dbc230e-b43c-35d1-8953-151f6e5ccc30 | -4.7242 | -45.72554 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e05cb456-3df2-3ba0-8867-1078e8ade558 | -4.72317 | -45.73124 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1f5d6f80-7629-38dc-afdb-fc2609330535 | -4.72206 | -45.73739 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cffb6416-fcfd-385f-9679-80767efa5c4b | -4.72125 | -45.7254 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc1f7b81-d4e0-3f63-acda-0d681761cc76 | -4.72085 | -45.74408 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 159d74c8-ba30-3756-8a0f-5228b1968762 | -4.72027 | -45.73101 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8b227dd6-d077-30bc-a778-0130e597dc78 | -4.71921 | -45.73709 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f7222d40-e13a-353a-afaf-678afb380b33 | -4.71805 | -45.74375 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ad27ccc4-e9d0-3f66-9b4c-5bebb331697b | -4.71536 | -45.73643 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1e1427ba-0824-3e84-a2a2-e65c3d0a48f6 | -4.71422 | -45.7427 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2d7db717-7aae-3cb9-a3b1-40cdfac38689 | -4.71248 | -45.7363 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 682eacb4-0898-3c11-8770-ce34c602fd40 | -4.7114 | -45.74246 | 2024-10-23 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 708ffb62-8e0a-3160-9a2b-27fe76e1feec | -4.69077 | -45.87195 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 41b0a04b-7c83-3052-9a36-3547d02bde4e | -4.68977 | -45.86631 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cda8d3cc-d0e6-397a-b52d-9c798ec2481e | -4.68975 | -45.87758 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7fcb92e-4344-3784-a726-6e1cac808a15 | -4.68882 | -45.87177 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5041a923-5d9a-35dd-9c7d-faff2c81ddff | -4.68781 | -45.87753 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ac1cc17-8d4b-3e73-b269-45536e36601c | -4.68505 | -45.86526 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7091ddf6-714c-3b92-8e22-341864104819 | -4.68402 | -45.87091 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e5ccab6-b725-35ab-8e62-73cce038986f | -4.68201 | -45.87107 | 2024-10-23 03:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README15.md)
