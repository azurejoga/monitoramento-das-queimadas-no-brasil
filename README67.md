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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ffe0ec0-f888-3286-b7c1-d9c5ecc69878 | -12.8888 | -44.5909 | 2024-10-27 13:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 04bd9fdf-3355-34dc-bcf4-88558c234da0 | -13.0747 | -42.1261 | 2024-10-27 13:46:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 0680e112-cd7b-3b96-96c2-22572e630625 | -13.9069 | -43.1313 | 2024-10-27 13:46:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 411ac737-d372-3023-a647-6d7a584fe866 | -13.9074 | -43.1072 | 2024-10-27 13:46:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 196.6 |
| eb08b561-5560-3574-8626-19dafdee8cb8 | -14.5498 | -42.3017 | 2024-10-27 13:46:26 | GOES-16 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 94.3 |
| dfe93183-4394-32f2-a9cb-10cafef35ab5 | -2.0094 | -46.5562 | 2024-10-27 13:55:16 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a406b0a5-3471-378f-828b-c54a6bafbbd4 | -2.9215 | -50.274 | 2024-10-27 13:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 791d796c-12b9-317d-9f72-f2704234f6e4 | -3.1278 | -45.2736 | 2024-10-27 13:55:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6bb88b11-852b-3cae-b581-07f577705b4b | -3.4431 | -45.4184 | 2024-10-27 13:55:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f06a63a2-d80f-3a37-b298-3311130d4a41 | -3.5564 | -45.098 | 2024-10-27 13:55:25 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c58d7905-ddbc-3db9-98e7-01c79d121015 | -3.7573 | -45.7858 | 2024-10-27 13:55:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 752c865c-c29f-33c2-a81d-e6621ffee04d | -6.9593 | -41.3296 | 2024-10-27 13:55:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 167.8 |
| f9e799ba-5eff-312c-83b6-ee0ce4c46bfa | -6.9405 | -41.3315 | 2024-10-27 13:55:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 130.0 |
| 4048b089-acd0-3456-beb8-63ccc1b1bbf2 | -12.8883 | -44.6143 | 2024-10-27 13:56:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 156b91dc-e76e-3a48-a075-a886ee369e3a | -12.8695 | -44.5941 | 2024-10-27 13:56:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e6476c6a-fb2f-3ffb-b8c0-94be6f86faac | -12.869 | -44.6175 | 2024-10-27 13:56:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 5375a60f-e793-3ab0-b79a-3767ef95a6e8 | -12.8888 | -44.5909 | 2024-10-27 13:56:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 0970465c-9224-3380-ab43-7ba46b13f938 | -12.9082 | -44.5877 | 2024-10-27 13:56:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 5ee522e0-d507-3a51-95c0-fcb197fde1ca | -12.9565 | -42.2208 | 2024-10-27 13:56:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 596230a2-e2e1-3237-be44-8f5e4fbbedae | -13.0747 | -42.1261 | 2024-10-27 13:56:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 149.3 |
| 460da9ac-d69f-37ef-a0dd-d73038ed29a4 | -13.9074 | -43.1072 | 2024-10-27 13:56:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 188.0 |
| b2d02ea2-4d16-3ed7-a3f0-8dacdd2de769 | -13.7523 | -43.0884 | 2024-10-27 13:56:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 51bc9acc-ebac-3fd2-9f10-e2f4ffda937e | -13.9069 | -43.1313 | 2024-10-27 13:56:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 105.2 |
| d78126fc-e1e1-3bbe-a1c5-1ce553a7b25a | 0.1196 | -51.0873 | 2024-10-27 14:05:04 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 80.1 |
| fbe8a907-4a7e-3a1a-86bd-52ce0553aeba | -0.1195 | -51.625 | 2024-10-27 14:05:06 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 74c56eb1-c4eb-384f-b708-005639f4b278 | -1.5262 | -47.2029 | 2024-10-27 14:05:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 623ccb72-0afe-3194-bab3-7a0b989e1d44 | -3.4617 | -45.4176 | 2024-10-27 14:05:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| cef1e809-77c9-304f-afa4-9fa5651c3e50 | -3.4405 | -42.4494 | 2024-10-27 14:05:24 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 927904b2-49e4-3bf9-9fd5-75d4ab402fc6 | -3.6264 | -45.9256 | 2024-10-27 14:05:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a0261605-136b-38d3-b6fd-54aeff79281f | -3.7573 | -45.7858 | 2024-10-27 14:05:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f98c3031-ce20-36d6-a8d7-c9b2c70f1531 | -6.2549 | -43.8778 | 2024-10-27 14:05:40 | GOES-16 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 411d1d75-cb9e-31bf-bd1b-97bdc6caeef2 | -6.4067 | -38.4547 | 2024-10-27 14:05:41 | GOES-16 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 163.0 |
| 0e09f01a-5974-307f-b41d-afd1bf97bbfc | -6.6813 | -40.8958 | 2024-10-27 14:05:42 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| ba1902aa-e8b5-3c30-a940-a9d42f30f190 | -6.9593 | -41.3296 | 2024-10-27 14:05:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 161.1 |
| 975f098f-f872-3fb2-8cb3-a62d35549c3d | -6.9405 | -41.3315 | 2024-10-27 14:05:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 24cad638-8a4d-3991-9677-dab3482b55ee | -9.9851 | -38.5667 | 2024-10-27 14:06:00 | GOES-16 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 165.2 |
| d4666017-da81-3924-bacb-b3e7de03f520 | -12.8888 | -44.5909 | 2024-10-27 14:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 83aec3c7-5e37-345d-9c97-1afa5558c70a | -12.869 | -44.6175 | 2024-10-27 14:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c657604f-dad9-33e2-81ec-6220d56aaf3a | -12.8695 | -44.5941 | 2024-10-27 14:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3033b5fb-a349-3953-bc6f-143e3d0beb0a | -12.8883 | -44.6143 | 2024-10-27 14:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 3ad00bac-fa1b-3032-823d-338769c99742 | -12.9565 | -42.2208 | 2024-10-27 14:06:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 98.9 |
| b31264f3-0e83-37d6-a03b-ec845996080e | -12.9082 | -44.5877 | 2024-10-27 14:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4d411ea1-11d0-3106-94c8-f4afe86126b3 | -13.0747 | -42.1261 | 2024-10-27 14:06:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 139.0 |
| bb7d6766-f4ef-3de0-afe3-94d193116f01 | -13.9074 | -43.1072 | 2024-10-27 14:06:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 208.3 |
| 6d8a33ca-ed74-3225-839a-1e44bb6e87c0 | -1.5262 | -47.2029 | 2024-10-27 14:15:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 4482ecb4-04e1-3cf3-bb43-e7917cdfeb74 | -2.2278 | -54.4855 | 2024-10-27 14:15:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 8c09cc5a-6e65-3874-bd8a-8caf6c541f23 | -3.4431 | -45.4184 | 2024-10-27 14:15:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f09f5ae0-b840-3ad7-939c-5eba8c40e644 | -3.4617 | -45.4176 | 2024-10-27 14:15:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 24f74cce-8573-32f3-8058-e2669f6d54bb | -3.5564 | -45.098 | 2024-10-27 14:15:25 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3f4f84d3-4809-32fb-99c4-3680594601f4 | -3.6264 | -45.9256 | 2024-10-27 14:15:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| bed33201-dcc9-337b-bf17-68e420b2e94c | -4.0621 | -44.5974 | 2024-10-27 14:15:28 | GOES-16 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0c34d902-716d-3424-b4e3-c42e6eab5699 | -6.2549 | -43.8778 | 2024-10-27 14:15:40 | GOES-16 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f5b7cbac-47bd-3f3b-8de6-6b3f586932ef | -6.6813 | -40.8958 | 2024-10-27 14:15:42 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 168.7 |
| e620d922-40b0-3220-b588-b37d3b9a954a | -6.9593 | -41.3296 | 2024-10-27 14:15:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 210.2 |
| ffffc378-699a-3024-ad95-e99cfc6b7b7d | -9.9659 | -38.5699 | 2024-10-27 14:16:00 | GOES-16 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 126.3 |
| 4a1342b4-5737-3d3e-936b-0bcb6367fa71 | -9.9851 | -38.5667 | 2024-10-27 14:16:00 | GOES-16 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 232.9 |
| a244b3f9-f8fa-320b-bca3-f47ee0744f92 | -12.8888 | -44.5909 | 2024-10-27 14:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.4 |
| f6738566-12b8-3a7f-ad3b-4b8ae78ecd10 | -12.9565 | -42.2208 | 2024-10-27 14:16:17 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 9958d6f2-7fd3-3526-ab6b-e8bbde14d397 | -12.8695 | -44.5941 | 2024-10-27 14:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6881288c-bdbc-39ef-a4c3-8fe899593737 | -12.869 | -44.6175 | 2024-10-27 14:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 5170ee83-bca6-3ebf-925e-c3f02d42bf58 | -12.9082 | -44.5877 | 2024-10-27 14:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 40a76a30-fe86-3ed1-b834-2376ed7bf0eb | -13.0747 | -42.1261 | 2024-10-27 14:16:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 41221012-3c91-3bf9-9aaa-e16dd7cbe01e | -13.9074 | -43.1072 | 2024-10-27 14:16:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 162.1 |
| 3a666148-1520-372e-9312-c0fbbf1ea211 | 0.1197 | -50.5042 | 2024-10-27 14:25:04 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 84af96b2-cbb3-3600-b95c-bedf5e38a818 | -1.4397 | -54.0564 | 2024-10-27 14:25:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 1e8dff90-6ef4-363a-a981-a74b957844fe | -1.5262 | -47.2029 | 2024-10-27 14:25:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| f9ba9c04-1e9b-3097-ad32-ba0b3f0c4747 | -2.2278 | -54.4855 | 2024-10-27 14:25:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 5866e4a1-4e6a-31a5-9c87-7ff77e65ebee | -3.4617 | -45.4176 | 2024-10-27 14:25:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 6f013c92-a75f-3cf1-9c6d-eeec2b411389 | -3.4431 | -45.4184 | 2024-10-27 14:25:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c6124988-2fbd-303e-8140-4cea2848dba3 | -3.6264 | -45.9256 | 2024-10-27 14:25:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| b969107c-fea9-3fcc-aea8-f357b18889f3 | -3.5566 | -45.0754 | 2024-10-27 14:25:25 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4ab52732-53e0-3923-9739-f2827bc091a1 | -3.5564 | -45.098 | 2024-10-27 14:25:25 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 3237d638-2e19-3290-aa5a-94be9e145571 | -3.5775 | -41.3948 | 2024-10-27 14:25:25 | GOES-16 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 01d1cb81-e95a-39f9-b2d2-feac97ee6b69 | -5.5682 | -45.3009 | 2024-10-27 14:25:36 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ba1a3f35-0bce-3771-83e8-bec2769101e1 | -5.568 | -45.3235 | 2024-10-27 14:25:36 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| dcdb0be6-8657-3585-aa09-c7f2188c9547 | -6.0108 | -45.9668 | 2024-10-27 14:25:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f750481e-f32f-3864-a024-07902bc78785 | -6.6813 | -40.8958 | 2024-10-27 14:25:42 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 158.1 |
| bcb1132c-da8a-314c-90c4-dcdeac15f669 | -6.9593 | -41.3296 | 2024-10-27 14:25:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 345.1 |
| d560314a-44a8-3910-a87b-f7799510169c | -7.5893 | -39.3611 | 2024-10-27 14:25:47 | GOES-16 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 6c90e979-d921-3ce3-a315-8693f17f83e4 | -7.5594 | -38.7576 | 2024-10-27 14:25:47 | GOES-16 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 971d48c2-e9c0-3795-8ba6-1804bcf80f1a | -9.9851 | -38.5667 | 2024-10-27 14:26:00 | GOES-16 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 336.5 |
| af742bb4-e3e0-3ac5-b420-20ed6eda351a | -9.9659 | -38.5699 | 2024-10-27 14:26:00 | GOES-16 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 160.5 |
| 86690c58-b234-3089-a82b-7a075649a212 | -12.8888 | -44.5909 | 2024-10-27 14:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 46062d03-3481-3a9e-9add-adb792f2989e | -12.9082 | -44.5877 | 2024-10-27 14:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ca325e86-15ef-31ff-aaf9-fdfe439614dd | -12.8695 | -44.5941 | 2024-10-27 14:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f511c63a-d4fe-375b-b3cf-d1de4fd205aa | -12.869 | -44.6175 | 2024-10-27 14:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 43d1abc1-b237-3f4f-bdb3-55f50b297edd | -13.0747 | -42.1261 | 2024-10-27 14:26:18 | GOES-16 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 120.2 |
| a664bc1c-3e0f-3b90-b926-fb7671d67c0f | -13.9074 | -43.1072 | 2024-10-27 14:26:22 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 176.2 |
| 247f8ded-d4e8-3a63-8eec-f9cc4a3f42d4 | 0.1197 | -50.5042 | 2024-10-27 14:35:04 | GOES-16 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 18b530c9-1f04-3fdc-ba10-aef7f3b90586 | -1.4397 | -54.0564 | 2024-10-27 14:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 51646033-277e-3050-a3f9-66e554eaa123 | -1.4397 | -54.0765 | 2024-10-27 14:35:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 377.2 |
| 411129b4-251a-3975-b095-7038d22e5ea9 | -1.5262 | -47.2029 | 2024-10-27 14:35:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| ca5dc571-3174-3476-89f9-7b2082c3d9d3 | -2.5312 | -51.1609 | 2024-10-27 14:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 08939d62-a4e0-3c5c-9829-d9e58ef72251 | -3.4617 | -45.4176 | 2024-10-27 14:35:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| afe61c8e-2f0c-3176-ad35-3c5075292976 | -3.5564 | -45.098 | 2024-10-27 14:35:25 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d49f1497-8673-3d42-a426-b4a39bbc37ca | -3.5775 | -41.3948 | 2024-10-27 14:35:25 | GOES-16 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 120.8 |
| 2c4d40bb-db7c-3499-82c6-b811120cd5a3 | -4.0621 | -44.5974 | 2024-10-27 14:35:28 | GOES-16 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| eae1e9ac-20a8-3fff-91cd-a198404edbab | -4.3336 | -45.8472 | 2024-10-27 14:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 1c384af2-6fc9-332e-81dc-dbcfb67bb126 | -5.5682 | -45.3009 | 2024-10-27 14:35:36 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7ebdbb85-99cb-3bcd-a833-6ed7975faec0 | -5.568 | -45.3235 | 2024-10-27 14:35:36 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |


[Clique aqui para ver as próximas entradas](README68.md)
