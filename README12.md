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
| c74ac924-7050-3fee-93cb-ed464f77415a | -4.9566 | -43.71128 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b696bd38-f872-3d86-ab3c-b0160f500f9e | -4.43149 | -38.96213 | 2025-11-12 04:31:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| edd2c493-8206-33ce-b73c-75f1cb21f69d | -4.10704 | -48.01472 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c0edbe5-cbae-3ae1-b1e3-5ffae342d1cb | -2.64213 | -49.1992 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e50a7677-1a1e-3418-bcd7-0685bacec761 | -3.71827 | -45.82489 | 2025-11-12 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3715b091-1add-34bc-958f-1e335f9f6889 | -6.87835 | -42.85081 | 2025-11-12 04:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 3ffa54df-4ee3-39ac-a1cb-53ed900a8f63 | -4.10262 | -48.02117 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 937b8201-45a6-3b00-a61c-9d0cc7407b17 | -6.09184 | -41.58677 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 794364dd-0caf-30a2-9821-1459c4694f69 | -4.22189 | -42.52603 | 2025-11-12 04:31:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c66d4abb-79d5-3350-8b34-caf06df7afce | -7.06478 | -41.58851 | 2025-11-12 04:31:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dec482a2-4725-34d9-8bba-a96fa71132b9 | -3.78261 | -52.22738 | 2025-11-12 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8b9e1a7-9c1c-30d3-bccd-6d8c923576f5 | -7.0971 | -40.44839 | 2025-11-12 04:31:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8c9f9121-807d-3bc5-befe-e6030e2c82e6 | -4.44284 | -50.15427 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 454bb75a-18d8-3eee-af98-d0ba7e46d57c | -8.29268 | -43.8487 | 2025-11-12 04:31:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cbcb52f3-74b1-35df-8719-2a99534240a3 | -10.5231 | -44.203 | 2025-11-12 04:31:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4354053-1073-3e11-9447-540ee5208900 | -7.83724 | -41.75256 | 2025-11-12 04:31:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 33f0dc96-cf76-32bd-a5a6-68b913760490 | -5.22894 | -38.58889 | 2025-11-12 04:31:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5756ad87-c7ad-3f76-af87-ff347da39c8d | -9.00665 | -44.82753 | 2025-11-12 04:31:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 540fa1ab-8a31-3d07-932b-58b0779c9e5b | -6.78283 | -42.84692 | 2025-11-12 04:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef0a879f-ca65-3f52-9d07-76a7a1479001 | -3.13032 | -50.17633 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f02e9a4f-af2d-3774-8755-9a7d541b3385 | -9.86545 | -47.87009 | 2025-11-12 04:31:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ff46f89-082d-3b1d-9a92-055f7bc60ef8 | -3.958 | -45.34853 | 2025-11-12 04:31:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54f0a886-5298-3403-9579-79af5dbdd3a6 | -3.49343 | -49.96609 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95f91e2c-c0ca-3f16-9d05-37e75d491ef1 | -2.90937 | -51.47317 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28e99941-0f10-3b60-984e-68b6ae10a78c | -3.81937 | -50.14705 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea9ef318-1749-3cdf-9cf5-03ab512d4de1 | -2.61484 | -49.21453 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f19e5c99-5ef6-3184-bbe8-a916151858d6 | -8.48403 | -49.8732 | 2025-11-12 04:31:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3093ccab-81e1-3d7e-b3b4-47d22c671e4c | -4.14329 | -47.65499 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8853ee43-6683-3cd5-ac25-f19d9184dc62 | -4.99784 | -46.86929 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c6f6f6-cd91-3383-a1a4-e358d9b41842 | -4.41089 | -43.11224 | 2025-11-12 04:31:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7d5a2a5-4e2e-35ab-b63c-b1d8fbdbd4bd | -5.00483 | -46.82436 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8149c775-6ee3-3727-a3b3-dc5e8fa02b74 | -4.09875 | -48.02414 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3fc4bdc3-e0d1-31bc-ac2b-23742977c746 | -4.9131 | -44.31831 | 2025-11-12 04:31:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46aa1bba-acc6-310a-a683-8498f23fce05 | -7.13799 | -41.25581 | 2025-11-12 04:31:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0fdcca6-1992-3c42-83a8-0d3cfe948d01 | -4.90703 | -49.32925 | 2025-11-12 04:31:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 983edad6-73c1-38e3-b626-a490721f56b1 | -10.45247 | -44.96417 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4f6abf5-bd93-3a9b-a27c-a122cba149f6 | -3.09031 | -49.267 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 029b79ea-ba3c-37ab-a101-084531e396c6 | -2.63866 | -49.19867 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40954d3a-74c0-356e-bc0b-74101970e9c5 | -2.43928 | -49.2304 | 2025-11-12 04:31:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c893a730-ce30-3620-8f38-03cd6cd6e6ce | -7.25184 | -41.62979 | 2025-11-12 04:31:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c210bbc4-8aac-3945-b6f3-0753fe807ada | -9.18758 | -41.03076 | 2025-11-12 04:31:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5dc5767-bd84-3be7-af5e-3c20c2083980 | -7.40833 | -43.33528 | 2025-11-12 04:31:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29f87734-9184-302d-8bea-d6a2597077cc | -2.81706 | -51.34533 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd998191-f68e-36be-868c-1cd7e754cc59 | -4.10317 | -48.01768 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89af5fcc-e7fa-399e-9e7a-12a45d41b7db | -6.99635 | -42.78468 | 2025-11-12 04:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d6b08d2d-beee-3db0-b19c-2e9dd8aa8a80 | -4.95897 | -43.72075 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 67dee10d-8acf-34f7-8ca7-3e68c486c9a2 | -6.48021 | -43.54204 | 2025-11-12 04:31:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99413d10-c9c9-34de-9fec-3b8aa81d313b | -4.08025 | -50.31284 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a3ff46f-2b45-376c-a87e-4322b04d1307 | -3.10369 | -45.26772 | 2025-11-12 04:31:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82b60bdb-745c-3b64-9821-e07ce5ee75b2 | -6.31751 | -43.80883 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b0bbf333-cb37-3763-9c24-fe7655d6f367 | -7.28558 | -41.58225 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ab57a02d-9c79-381c-8437-d228d7b7b3dd | -2.72879 | -47.41022 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b374fe80-2a70-3df4-a8d1-48e63984d6fb | -9.45615 | -44.87321 | 2025-11-12 04:31:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15b3c44c-9a59-3d00-a79c-ba4104f3981c | -7.13359 | -41.87151 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4aef526f-8cc5-389f-bd98-0017f80988f5 | -4.94721 | -43.7234 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e981f344-7053-3b9f-a179-4786fbb12b96 | -5.21492 | -49.14014 | 2025-11-12 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fa6e38f-39a8-3887-9d34-362ef5d810f1 | -2.55035 | -47.3754 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 533e7fac-aa15-3725-ab15-9b974387a066 | -9.3231 | -47.83789 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69a88cbe-ad93-3658-bb89-f46ab765c265 | -2.53035 | -47.80573 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 382b34f9-81bc-3d85-bbc5-2c578f7ea4e7 | -3.44386 | -52.64034 | 2025-11-12 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af4a22a3-c596-378d-b812-339ef7cc3047 | -5.71772 | -46.50275 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95a4a0a3-9da1-39bf-b586-090abd22202b | -2.81319 | -51.34472 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ab14631-9f6f-3a60-bf24-562125e0b30d | -7.92452 | -43.31272 | 2025-11-12 04:31:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6253170b-3e8a-3094-bd95-fd957424b120 | -3.90138 | -52.11261 | 2025-11-12 04:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ce2ca8-9f1a-3da8-84fd-77b60440ccbd | -4.10868 | -48.00429 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ade8b7f-2890-30a6-9737-916fddfc21d9 | -2.89612 | -51.45599 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f106c6c-0019-38a9-b837-dbfe4cd480bb | -4.43093 | -38.96078 | 2025-11-12 04:31:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6018702a-bcfb-3af0-9c77-8237e520087c | -4.95223 | -43.71514 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e19c1efa-18cc-3115-b0af-16da8e0b13ed | -7.47391 | -42.55922 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ea54cc50-e529-3384-a90d-f5c9ad53c5f3 | -3.96976 | -43.77684 | 2025-11-12 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c81ac55d-23b1-32a5-8732-1396c6f77544 | -3.21033 | -43.52596 | 2025-11-12 04:31:00 | NOAA-21 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15741f15-8758-3d8c-bde4-b1701ab3a119 | -5.14353 | -49.63069 | 2025-11-12 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84ed4c79-b378-38ed-bbfa-a00559c0b0bb | -3.49913 | -55.41833 | 2025-11-12 04:31:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6da9485e-192b-329f-8b0b-3987bb6fce87 | -4.14275 | -47.65843 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c90e38e2-dc8c-395c-a98d-5d88dcc5094a | -7.47911 | -42.5522 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f520e5c0-5b80-3afa-896e-c7ca42d94025 | -10.3278 | -44.27555 | 2025-11-12 04:31:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 794c4aa6-0bab-3fb6-8578-4c6b485d2b33 | -4.62893 | -49.46564 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab960939-503a-316e-8212-c78f41d8eebb | -3.28673 | -50.02961 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0eac5a6b-9989-3f01-90b5-ef5139b337c9 | -3.3539 | -42.15635 | 2025-11-12 04:31:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0f2022cc-05ad-31ce-9ce1-a09870b56aa1 | -2.97782 | -44.58204 | 2025-11-12 04:31:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbc94f75-de18-3369-b244-033712f6b099 | -6.10777 | -41.53892 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8191dafe-aeb3-3504-b303-a9e662ca703a | -4.64611 | -45.75798 | 2025-11-12 04:31:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef5ba172-d9bd-3132-bdf2-faa58b11fb42 | -2.40095 | -49.39559 | 2025-11-12 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3335e09e-03c8-3a37-9513-844a73bb9dfd | -3.44449 | -52.6365 | 2025-11-12 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71f1e4a8-cf78-36c7-ad95-d661c8fe844d | -5.75168 | -42.73309 | 2025-11-12 04:31:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4688fc7d-9399-3335-afc6-e9cb4d97cc50 | -7.47511 | -42.55976 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b2d36b99-667a-3406-99d5-64cf5632c774 | -6.88289 | -42.84781 | 2025-11-12 04:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dbd2fab3-4ad7-3e45-99ab-0e3bb732e077 | -7.48913 | -40.12115 | 2025-11-12 04:31:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d0ef3c0c-0baa-3fb8-bb84-5abc1c8f8632 | -4.95831 | -43.72519 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 54ea9c8a-6bef-3905-8507-9b5b073c7ff5 | -4.93547 | -44.29227 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a841b719-d6e0-34a9-9c98-f0d69086beb1 | -10.45182 | -44.96861 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ab0f8dc-5dfb-3089-9a2f-8667699ab524 | -5.64941 | -45.98103 | 2025-11-12 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3237daa3-468d-3ce8-adbc-2ae664292796 | -7.45744 | -44.75266 | 2025-11-12 04:31:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1de15310-8dcb-3b15-8f4c-b1fd334f3f7c | -6.09614 | -41.58751 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cda5caab-4148-31ad-a9c6-99e195779021 | -6.6041 | -43.85606 | 2025-11-12 04:31:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d969a80-67e8-3cda-aac2-501b41e5a8a7 | -3.08391 | -49.46267 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 24b507b4-553d-3323-85a3-ed3d546eba1e | -5.37203 | -48.92385 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2abd4fe4-2184-3141-be7b-620155473096 | -4.93686 | -44.29595 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee05fe96-05e2-3c08-8aa9-404838cbe45c | -4.21858 | -45.95298 | 2025-11-12 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28875a80-e69a-37b9-88e4-67f7b92fc34b | -4.82545 | -45.54721 | 2025-11-12 04:31:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
