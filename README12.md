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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85f75bce-6ba1-3891-aeae-8acf0c084271 | -1.5755 | -53.1204 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c51aa155-7185-3779-9d44-6ad7ca7c3019 | -5.00132 | -41.32493 | 2025-12-11 04:38:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e93ae76f-88c7-3b67-a884-144a558c8a36 | -4.95142 | -45.08241 | 2025-12-11 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75395ca8-7aef-3f74-9c53-543955a658ef | -3.49516 | -44.88942 | 2025-12-11 04:38:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65bf5433-05bf-3997-9f8d-595ba88edc7e | -4.06828 | -47.94958 | 2025-12-11 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9af8dd0-ff67-3dc8-bb70-a1395037211c | -2.09045 | -52.11688 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eef20c3-3853-320c-9f82-a05a34b9587b | -3.67979 | -47.63248 | 2025-12-11 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 645d882a-7edd-3e23-898a-7b3d49973519 | -3.34752 | -45.14176 | 2025-12-11 04:38:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e500c485-d781-368b-bffc-494d48bbe237 | -1.19909 | -47.53312 | 2025-12-11 04:38:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6d5097e-dde6-3c47-a7b4-fcc099338c54 | -3.8829 | -42.52439 | 2025-12-11 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd645407-b559-3c6b-b24c-981aebcc2341 | -0.92625 | -46.88735 | 2025-12-11 04:38:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aff9680-b7fc-380b-9c38-d37b2af9ecda | -1.71008 | -47.02667 | 2025-12-11 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b17c5cff-ae7c-3d97-9b06-4223692e0f53 | -2.27767 | -52.78201 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41a0d09c-9748-355e-83cd-1f3044279f54 | -3.26072 | -46.41331 | 2025-12-11 04:38:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad0f79f6-d318-3bcf-80da-bfafca31c3f5 | -3.699 | -50.94411 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30f30969-29d3-39ab-b06f-fba4fdf8fa78 | -3.54006 | -45.46687 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67a960a0-2314-38b4-9a85-ce21809234a5 | -3.53988 | -45.46516 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75c7a261-5d4a-3a1b-ba08-405aae58f263 | -2.41095 | -56.01917 | 2025-12-11 04:38:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff20d63a-6fc0-31ed-9b63-5af121adbc22 | -2.44422 | -49.03088 | 2025-12-11 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e3118b4-76ff-3b72-84d5-e90f8e6bb3c9 | -3.03835 | -50.49067 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b162b9c4-7f8b-3f41-9e44-e555604e8e44 | -1.01387 | -53.73034 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb6e6fb9-f97d-35fa-b7eb-c51370d3fb03 | -2.62741 | -45.55939 | 2025-12-11 04:38:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e354437-9a26-32be-b4cd-0db16e2fa1b6 | -1.10817 | -53.68576 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56b2c21d-3055-34b6-aac8-21d566246f04 | -2.77296 | -45.51889 | 2025-12-11 04:38:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8355847c-3f43-3755-9ba6-cbc1b47829b0 | -2.14701 | -53.75595 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c8354b9-e03c-38cb-830e-11324c000e94 | -3.10603 | -45.22629 | 2025-12-11 04:38:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 93bd9b41-89e0-3cf0-803e-9c73e8e4c49a | -3.69557 | -50.94356 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec549f5c-28a4-32fc-b5f0-e1c229ff9cbd | -4.10777 | -50.0041 | 2025-12-11 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b60decb-1eb6-3132-9b55-995acd85d045 | -5.00694 | -41.28702 | 2025-12-11 04:38:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 525f3442-5fdf-3082-a11a-771ec0aa4484 | -5.00613 | -41.29245 | 2025-12-11 04:38:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6403f2d0-66ef-303e-b0c9-a6c70f176335 | -3.74318 | -50.79949 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eba4dd2c-b575-34b9-ae15-4d889583479a | -2.07924 | -48.37123 | 2025-12-11 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 388d6e35-17c1-3d65-85dd-26e5dbdb419c | -1.4342 | -45.66625 | 2025-12-11 04:38:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1af3aa5-1b60-3dd4-9881-89734f5a65bc | -1.30671 | -53.48663 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33e1c328-af32-3bd1-8940-25f3a8f36b1e | -3.10943 | -54.1731 | 2025-12-11 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 454303fb-9f28-3e1d-8822-5d4af43ad615 | -1.61636 | -54.71372 | 2025-12-11 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9eb5da92-5656-3f58-946e-7bd8ca5c30e0 | -1.19521 | -47.53608 | 2025-12-11 04:38:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c76e094f-09d0-366b-a041-56151f02bf44 | -3.74659 | -50.80002 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca2ce93c-fec2-3075-83bc-f038b01213a4 | -1.20132 | -47.5406 | 2025-12-11 04:38:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cb5d19a-4cbb-33ba-8e4f-090bcd36b9af | -1.31017 | -53.49086 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f8f8efd-36c4-38a8-ab9c-65e880545f4c | 1.16097 | -50.7098 | 2025-12-11 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d7c8216-55d7-32d9-880e-c57a885a9ba3 | -2.08309 | -48.36831 | 2025-12-11 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7adc43ee-3bdb-3e71-9f7b-265132334fb3 | -3.04117 | -50.49484 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c443538-ea27-32a9-a233-711220cd246c | -2.89462 | -49.53403 | 2025-12-11 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76808a09-d92c-3dac-bfcc-857bee65daf9 | -3.33269 | -48.8462 | 2025-12-11 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1b15af8-8751-3588-8b8e-c73e15a225ae | -2.87735 | -52.71902 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b5b71fa-3810-33f8-800b-242f35f8385a | -1.79686 | -53.857 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aab8e63f-d484-3847-a590-42871dafe745 | -2.93621 | -53.02728 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d6a300bc-881a-3319-8479-8003547ca9a5 | -2.31007 | -46.48275 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e3340f-4c27-315e-a518-8a30427a0b5f | -3.48816 | -51.53421 | 2025-12-11 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3ac7ed-351c-3f9b-9aee-3f0b4b3ec346 | -4.93346 | -43.96061 | 2025-12-11 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 895d02ee-8ad7-3524-b62c-be09c1df7e25 | -3.48689 | -51.54208 | 2025-12-11 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 486da29e-eca8-3099-b817-cdf5f2bce315 | -3.0881 | -44.89545 | 2025-12-11 04:38:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7696b4b-2f09-31e1-958f-b8fbb1380392 | -3.39435 | -42.10431 | 2025-12-11 04:38:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 40e4c346-0a8a-31dd-b46f-4cf9ad99626b | -3.70183 | -50.94841 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1dacf72-effb-30df-a4a3-b9ddd92b103c | -3.84369 | -47.8207 | 2025-12-11 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f454f76-3f6c-3fa1-8eef-42540f5e27d1 | -3.3506 | -46.2112 | 2025-12-11 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c805a55b-a957-3a66-9cdc-c936e503af03 | -3.70243 | -50.94468 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a10424a-4b86-3e39-80f2-93190cb55e77 | -3.5776 | -52.11235 | 2025-12-11 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f01233e0-90ed-3a84-a32c-691a22fc7882 | -3.18741 | -52.02756 | 2025-12-11 04:38:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a851f8ac-b358-30a7-8374-b5e4bbd3d5e8 | -2.08255 | -48.37174 | 2025-12-11 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c34fc2f-7d1c-3fa4-a7f8-2e4b49f2c576 | -3.24318 | -44.91686 | 2025-12-11 04:38:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77c21f91-a24a-39a3-bed3-29bbc8c068bc | -4.31761 | -44.50274 | 2025-12-11 04:38:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47d150b4-1119-3a54-acd1-a0d79754cf85 | -3.84258 | -47.82779 | 2025-12-11 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31a4d644-4459-3ca6-b97e-3ccaba4270a6 | -3.26011 | -46.41721 | 2025-12-11 04:38:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1bf0f73-5f26-3802-b4d0-71a832b4fba2 | -2.23893 | -46.51463 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64a9495f-0c06-3cae-accd-40d7cec7a21e | -3.6984 | -50.94785 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f96f0b98-2818-3260-b927-205247aef2b2 | -1.58761 | -53.75877 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84487fc8-82dc-378a-9260-b6039f0b3e55 | -3.52203 | -47.20647 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19d1bdb9-0218-30fc-91d4-bd88cf35faed | 0.46088 | -60.4295 | 2025-12-11 04:38:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a98a3e3f-821a-3dc2-83fd-214ac0eb55bd | -1.74676 | -54.60063 | 2025-12-11 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b60e75b-f2b3-31b3-bc2b-36b4af31da06 | -3.11354 | -54.17382 | 2025-12-11 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae8bc5ab-40a1-37b0-8ba9-21c34ae85be4 | -3.48401 | -51.53759 | 2025-12-11 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaeaa664-96b9-38a9-8d2a-b8d5d4fa87c4 | -0.64685 | -52.39246 | 2025-12-11 04:38:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9701404e-1fd7-32dc-8c66-573536f6ba9a | -2.28807 | -45.59896 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 639becef-51f9-390d-89c2-f7b9c1057bec | -4.20888 | -44.4788 | 2025-12-11 04:38:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9779e52-4a1a-3861-ab51-a2f8c053db85 | -3.95415 | -41.52416 | 2025-12-11 04:38:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| be0330bd-d09a-3c13-98db-9cc47309bac1 | -1.16453 | -48.85032 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e59ed7a7-c689-3760-97db-43fdd88a3d37 | -2.01911 | -52.04963 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30b6341d-99e8-3339-b385-59d9affa9ca1 | -2.4756 | -52.14652 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21cd3aa4-1fb3-3f0d-a04a-16b5c963416f | -2.02842 | -47.14109 | 2025-12-11 04:38:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056ebc44-83f2-30fb-be5f-8834414d87f1 | -3.47756 | -52.98679 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb7c9a2c-cdd6-36ff-b3f7-14faa9756251 | -3.53686 | -45.46031 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a33c7cc3-de28-3633-a23b-13de004f8a69 | -2.31696 | -46.48383 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e868033f-82f0-3d46-9636-884c4b4a0ad9 | -5.143 | -43.86572 | 2025-12-11 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2eaf9a7d-9cd0-3306-84ae-865a569f49f9 | -1.28708 | -53.16403 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49e182b6-bb33-3520-9be0-2470e69a78ba | -3.26359 | -46.41774 | 2025-12-11 04:38:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1b640eb-c7a8-32d1-8c9f-2b5ea5596f3f | -3.88207 | -42.52295 | 2025-12-11 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b003a9e9-f262-3442-b1ad-d4f5523a9440 | -1.19854 | -47.5366 | 2025-12-11 04:38:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7868afe-9ec4-36ab-b1f7-b0c886280120 | -1.66418 | -54.57991 | 2025-12-11 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e069879-1050-367d-ac3a-60433594df78 | -1.11579 | -53.69086 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 95265d41-c00f-3006-ab8e-bcd9bd89cfc3 | -1.69971 | -48.66656 | 2025-12-11 04:38:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a146814a-3e37-324f-898e-da9375c02b08 | -1.82665 | -46.52926 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fa0059b-51ac-3101-a887-b0b8a55ca3d6 | -3.48175 | -52.36186 | 2025-12-11 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c0d3e62-4c01-3a78-ae7f-c47c6468be9b | -2.10275 | -48.05041 | 2025-12-11 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b09c886-2c88-36a0-b602-cf3afc15076b | -1.58702 | -53.7624 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1818427-9864-3317-9efc-22ae15d13526 | -3.22683 | -52.64343 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1de1e40-8430-34b0-96ee-7b1a08a17a87 | -0.64304 | -52.39185 | 2025-12-11 04:38:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8030d7ef-145b-3311-a7d8-805265d0ab5a | -3.75597 | -45.49436 | 2025-12-11 04:38:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 94882ccf-3e29-34bf-9d50-8bdfc7f2959e | -0.98211 | -48.0687 | 2025-12-11 04:38:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
