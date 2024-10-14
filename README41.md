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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59787d42-17fa-3434-854e-9198c9b66f0e | -6.22104 | -44.21691 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2066f926-a3c2-3edd-a0ca-bb15f81f70d4 | -6.21779 | -44.21276 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1683df98-fca8-3c0f-9c22-0b237eb0533e | -6.21305 | -44.09157 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 291533ae-330a-3c02-8480-4803b7e2dd0a | -6.19934 | -44.11432 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 695e8785-2807-3bdf-a8c6-bc999592438d | -6.19604 | -44.1138 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 412083ad-2cd2-3cf5-9c7c-6e7b51f2664c | -6.19569 | -44.18105 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51c42103-4917-39f7-8ad3-49a463a828c6 | -6.19539 | -44.26943 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff0ae7dd-fc5a-3cf6-9ae4-bbabe38288c1 | -6.17344 | -44.10673 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef5c6dc8-115a-3cd2-aa4c-37d3f7a685d1 | -6.15598 | -44.15351 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb330ef1-0cfa-3003-bd20-39d0ce26f35e | -6.14689 | -44.23352 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c306fca-c340-3bf3-9ee5-cb52a2a01808 | -6.14469 | -44.07384 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfafdb52-2f2b-3804-87ee-6add93480226 | -6.14138 | -44.07334 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecf27bb3-a3d5-33f4-b4fa-2be679d6428c | -5.32081 | -44.83333 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7063729-1c0f-3987-8c62-01f9220c4f72 | -5.19699 | -44.75671 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4af30f9c-2088-34fe-9851-bdc9f405f128 | -7.83622 | -43.99907 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c50e2c8f-afdd-3a1c-a6c3-36d9d97f866a | -5.19645 | -44.76016 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56cb413a-50da-3ed3-84a1-83399075d6ec | -5.19591 | -44.7636 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d922d27-50ce-35bf-8061-a01724ecc30f | -5.19315 | -44.75964 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 157e7ead-2d67-3bc7-a1ef-790b8ffc298c | -5.1926 | -44.76309 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 019f0c03-32b2-3ae9-948c-98f029d70482 | -5.09851 | -44.81896 | 2024-10-14 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57d9256b-003a-37e2-a78b-9aa27c47304e | -5.09521 | -44.81844 | 2024-10-14 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd1a65a4-1e35-3060-a17a-08ea35251c93 | -5.0134 | -44.64669 | 2024-10-14 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe58efce-6d55-32e4-a9f2-18e03174b3ea | -6.26661 | -43.90068 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55492337-a229-3d8c-8b8b-4141b69cd22c | -6.37028 | -44.08828 | 2024-10-14 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 27088e76-ba59-33cf-ad8e-fa190c03cf5d | -6.36974 | -44.09177 | 2024-10-14 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e33cc00a-b27a-30a4-b04a-03c53f637330 | -6.36217 | -44.48692 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0953f86b-c0ec-3e70-ad2e-b7c47ead028c | -6.35833 | -44.48986 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 694ec912-f837-3178-b221-e13b371e85d2 | -6.26241 | -44.08159 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 802fed71-1217-34d5-99e3-35a546812bcf | -7.92927 | -44.51857 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00166180-b35c-3a06-985b-5490c184295f | -6.25964 | -44.07761 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbf41d2a-b26b-34f5-a133-9e6054777679 | -6.22158 | -44.21346 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 705376a5-35e9-3c9e-a3e7-5884dc32a956 | -6.20974 | -44.09106 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47093ea7-b7f0-3f64-931b-1821e93bb6be | -6.20872 | -44.11931 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4bdba84-f21b-323a-acfb-9d55cca883f5 | -6.20265 | -44.11483 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d35ecaf-1a04-30e5-9437-b943a4ad2deb | -6.19953 | -44.17811 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b32779da-44d8-3682-bdd6-de6b95354db8 | -6.19292 | -44.17707 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dab106a-0af4-38d8-a73e-3db68ef08a38 | -6.19238 | -44.18052 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b956f0f1-09cb-3cf1-bca2-5eba889dac90 | -6.17164 | -44.59763 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cb50a14-a4d7-3559-84e0-7b494284f458 | -6.17013 | -44.1062 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03ff6883-9711-3341-90f0-8061c671a9d3 | -6.15544 | -44.15696 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7356657-83f6-3458-867f-1888f5237521 | -6.15131 | -44.07486 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f26477e-1d63-352d-a87f-15ad20a6ccb6 | -6.15077 | -44.07834 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 232145f7-4b63-3e78-9c4c-691da515653a | -6.14119 | -44.72696 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47a8bf32-7cab-38fb-8be7-2e361b6e39fa | -6.092 | -44.86376 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 548f8b1d-acb8-3096-9fe7-48cb853a050d | -6.0887 | -44.86325 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 58b8e3b9-b38c-365d-8836-e9349129f3db | -6.05394 | -44.80487 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 728c11da-3aa1-31ac-8e83-6e0f1f3a127e | -6.04147 | -44.01532 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81878d97-e10e-3cac-8044-b7a6d27b7fcb | -6.02981 | -44.30718 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1168a7b-4c13-37bc-875e-2e22e7f61ea5 | -6.0241 | -44.08346 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e7c50ee-69be-3cb8-b81a-09db8a75161b | -6.02356 | -44.08691 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca1992fc-152d-3356-8b85-78dbd3e5d88d | -6.09146 | -44.86721 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67f83988-9bf1-36d4-bcd3-68bef9934d41 | -6.0534 | -44.80831 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5e751936-5de6-3af4-9e54-7b74c107ecfa | -6.02927 | -44.31063 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c6d4ad5-f3bb-3655-a145-f95ade2faac6 | -5.96807 | -44.24397 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94467855-cb49-3cb6-baf0-fe326bfc1ebc | -5.89124 | -44.95248 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fedc40fa-3e9a-37f0-b65c-6f371aa5831f | -5.8907 | -44.95594 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad87c525-9cc1-3fb9-aa95-170efa83c5ce | -5.89015 | -44.95939 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 628c6721-67fa-3ec4-80b4-678e3d315f5b | -5.88913 | -44.31644 | 2024-10-14 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49e913b0-ba01-3502-8666-3c371618b23b | -5.87711 | -44.04233 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5f93697-ea60-36bc-b6ca-e2417c0aa4d3 | -5.87381 | -44.04181 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d98698d-3025-3963-8756-7149cd98bef9 | -5.87327 | -44.04527 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6dcf37fc-daea-3343-9c6d-c22fbf976cf1 | -5.87273 | -44.04873 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fafab09a-dd88-3cd1-8e38-0d0ee353c925 | -5.86996 | -44.04477 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7b1e553-ea21-3a24-9e59-a9419d6a6a95 | -5.76112 | -44.06668 | 2024-10-14 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b2caae4-1fcf-3e50-9d02-4ef5261fda5a | -5.75781 | -44.06617 | 2024-10-14 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52344d74-8630-3964-8679-7d5e934fd301 | -5.69454 | -44.23305 | 2024-10-14 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58cde8a0-1b28-33b7-9022-9c26e9f1032d | -5.59071 | -44.89398 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c18e1ef-4df2-33e0-b9b0-0059a962474c | -5.59017 | -44.89743 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce43bda1-66db-392e-bfc6-39035e3fe555 | -5.58687 | -44.89691 | 2024-10-14 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 094dae86-411f-394a-8aa8-379c0dc0a462 | -5.55569 | -44.53154 | 2024-10-14 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48881737-433e-3f85-83b0-5349c61a844a | -5.52465 | -44.643 | 2024-10-14 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2b4d0cd-4a77-3766-83a1-c73fa50650aa | -5.4918 | -44.15844 | 2024-10-14 04:19:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1521840e-e130-3b1f-94ce-f2f31383257e | -5.40159 | -44.21142 | 2024-10-14 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6abf5c6-99bb-3ce9-8170-4fe7b3c8c51e | -6.84394 | -44.38603 | 2024-10-14 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67f68083-8877-3955-84ed-1f834f710895 | -6.84063 | -44.38552 | 2024-10-14 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad2981d3-3cbd-37e3-a1d4-c9dd892ec0d6 | -6.62643 | -44.69072 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 951e26bf-aa90-3d28-81ef-59539261661d | -6.61653 | -44.68917 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c80885eb-b048-37d1-9e51-c5f5b1deec1d | -6.61256 | -44.47306 | 2024-10-14 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 741d5ab4-aa5a-3856-a9e0-01b46cf30bfd | -6.51037 | -44.69368 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe24f8f5-ded1-34d1-ba8b-a040f0079d18 | -6.50983 | -44.69712 | 2024-10-14 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 705e4f6d-6e85-3db2-83ac-7534c7eabcd6 | -7.93865 | -44.52359 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae46d5c1-3e8a-39e1-883c-3c3cd46cc6e5 | -7.93366 | -44.51218 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 666c8611-6eb1-3073-b861-aee08071400b | -7.93312 | -44.51564 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1aad076a-be7f-37c6-909d-9f0601ab5f02 | -7.9265 | -44.51461 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d25f4be-b8c6-3ae2-85d8-791b0a3bb702 | -7.92596 | -44.51806 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 772c72a1-85ec-3d1b-a5d0-d16e0a7a92a1 | -7.9232 | -44.5141 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0480337d-cae5-3b91-8476-eed0f7d37c8d | -7.92266 | -44.51755 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b52ef76-878b-3080-97f7-dc14f1f50940 | -7.92043 | -44.51013 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0acbe6f9-abdf-372c-842a-2b064bdf01e2 | -7.90849 | -44.51882 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d24a2405-a813-3328-91ce-ab2c5c094414 | -7.90796 | -44.52227 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cae874a-b004-3f3b-870c-6b37879a4b82 | -7.90519 | -44.5183 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bfb4f39-c843-37c1-878b-8cdff460e9df | -7.9029 | -44.48954 | 2024-10-14 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e52ddd28-c246-3d31-96c9-5630d173ea86 | -7.87006 | -44.00074 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dbb57d7-2b25-3098-b037-40a5368d3d8e | -7.8645 | -43.99263 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0122087e-2120-36b2-ab85-39bffeee7d4f | -7.86117 | -43.99211 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5970e39e-3aca-3a66-ba64-8d37f76794b3 | -7.84233 | -44.00365 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1536156-e6c5-33c5-8534-d87e839b2d00 | -7.84179 | -44.00717 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c274743d-35d4-34f7-955d-1109187d5aaf | -7.84065 | -43.99249 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95128b6c-15e3-3c86-88a9-d2a43b80cbc2 | -7.83786 | -43.98841 | 2024-10-14 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66fb1e21-beea-3f06-a793-fd80c3aa6469 | -7.83732 | -43.99198 | 2024-10-14 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README42.md)
