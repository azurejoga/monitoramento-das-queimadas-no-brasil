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
| 75af8ae4-0b14-3972-bc5c-fd8c3fa52bb6 | -15.64712 | -39.19151 | 2025-01-03 04:04:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c7857529-a507-3b56-8753-01dd8bae987a | -12.83204 | -41.142 | 2025-01-03 04:04:00 | NOAA-21 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c14b376-6259-34af-8b47-046a19164b43 | -12.18704 | -41.35538 | 2025-01-03 04:04:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29b14642-201d-36d6-8137-cb542013d896 | -15.56891 | -47.85484 | 2025-01-03 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcfbc242-7d0e-384d-9d64-f3fc6125ac62 | -11.85927 | -43.82789 | 2025-01-03 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d240b755-bd8d-3ed8-8eb3-c048fbe60398 | -10.82375 | -45.14952 | 2025-01-03 04:04:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 014e2346-bcf4-33e5-a8e6-c330e2fce7a8 | -11.0366 | -44.33857 | 2025-01-03 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cf96ffc-2c4b-3db4-97dd-a51bd1f181d3 | -21.81715 | -55.34177 | 2025-01-03 04:06:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 097ac5e8-dec6-3c4a-bc92-09b238712bff | -20.65882 | -49.99118 | 2025-01-03 04:06:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 616baee4-1f6b-31e6-9b34-47775f340266 | -25.19169 | -49.32747 | 2025-01-03 04:08:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 27ff032b-0adf-30f6-8ca8-c9eda2400a77 | -23.98305 | -48.91745 | 2025-01-03 04:08:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 685ca6e2-c385-388a-b334-2c81fe41d622 | -31.74862 | -53.33546 | 2025-01-03 04:10:00 | NOAA-21 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ee28653b-ce7d-30b7-879f-0351a56a96ca | -7.20305 | -39.72997 | 2025-01-03 04:25:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1bd27893-079b-3e92-8492-badf8c46897e | -1.71842 | -46.20945 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a2ae19c-e6eb-3c8c-b6d0-5299efacb6e2 | -1.72602 | -46.08184 | 2025-01-03 04:25:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91831e2e-18b6-36c4-b398-c238d23ebee3 | -7.23348 | -39.77811 | 2025-01-03 04:25:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5bdf769-826f-3fa5-9bf1-24578e248bfb | -4.09766 | -46.61429 | 2025-01-03 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3948cf5c-24ea-3640-be3b-5a16d64976bc | -1.72121 | -46.21347 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9feeb7b6-af09-361a-8c41-f67707e8ef08 | -1.25952 | -53.86019 | 2025-01-03 04:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71c2c006-1df3-37d6-80f3-2fe8600fb97b | -6.12267 | -42.54449 | 2025-01-03 04:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 0400d519-3b8b-3579-b183-2f2e5f809c08 | -3.86356 | -40.45494 | 2025-01-03 04:25:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3a40a783-5e38-3b89-bd63-c4cf77372a8e | -2.2988 | -46.41549 | 2025-01-03 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea6e4478-9f59-31fa-b1b9-464e56e2b1af | -1.72383 | -46.09578 | 2025-01-03 04:25:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ac20dbf-675d-31ac-a48b-d5aa3c92f561 | -5.62743 | -44.83305 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3c3a0e2-e3ef-32ba-9717-3f4e97f9e9eb | -1.25449 | -53.86261 | 2025-01-03 04:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b4ae3d5-6cc8-35d0-bff4-5602813fb3f7 | -1.85434 | -45.54472 | 2025-01-03 04:25:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c20f4fae-d312-3692-af32-e31c806c860f | -6.24016 | -39.62005 | 2025-01-03 04:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a87ca419-bcae-301d-9a9a-ed893b562673 | -5.63365 | -44.83772 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d28cf9d-1a12-3655-8a00-96e39cf7436e | -1.55648 | -45.69648 | 2025-01-03 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83830b94-660b-31fa-a003-d0fe6e35cff2 | -1.72401 | -46.23901 | 2025-01-03 04:25:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5009707f-ae6d-3f2b-b353-c6e057cdee77 | -3.85941 | -40.45429 | 2025-01-03 04:25:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c46bc25-8d09-3ec1-8d2c-89276cd81c65 | -5.3837 | -46.29031 | 2025-01-03 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf77d40c-bb07-3d3d-858a-4ec44a23a647 | -1.71452 | -46.23395 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6bf12d1-5244-3435-9594-479e27d15eec | -1.29513 | -52.11104 | 2025-01-03 04:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65db3a0e-02b6-3e44-8642-8715fe50c012 | -6.97559 | -43.55176 | 2025-01-03 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79b17fd1-57ae-3e00-a098-5a5781f41bcb | -1.817 | -45.91084 | 2025-01-03 04:25:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c5ca4c49-4ecb-3e16-ab8c-356fdf013712 | -5.38092 | -46.28632 | 2025-01-03 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6becae66-e2a7-3054-8526-494eb61d086c | -1.25499 | -53.85956 | 2025-01-03 04:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2ba530d-6ba1-3161-8ca2-16aa5b53f4cf | -5.15452 | -38.48293 | 2025-01-03 04:25:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 63ab82be-6db5-3180-a794-e7c3fabbab0e | -4.26537 | -46.68401 | 2025-01-03 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56ea0974-a54a-3f65-a9b3-2c21cfb91120 | -2.296 | -46.41145 | 2025-01-03 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 61d9636c-b48e-3af9-8c78-abd89d3b0f9d | -5.63026 | -44.83719 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93f441d0-cf85-3897-a381-c1bad6e52bfd | -4.72478 | -46.99388 | 2025-01-03 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ade81a4-af5a-369e-93f2-5e5176152d75 | -1.81367 | -45.91032 | 2025-01-03 04:25:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 98f750d3-36b2-3824-b1e1-ca101d412428 | -5.3121 | -46.05912 | 2025-01-03 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a102032-0c05-306f-9cf3-f9e1c45b3d51 | -5.92591 | -43.77219 | 2025-01-03 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1b8a1ea-0916-32a2-a0f3-4d7f64caf216 | -5.30878 | -46.0586 | 2025-01-03 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e9285e0-29e8-379f-ba01-fcf91cd19523 | -3.97949 | -40.92046 | 2025-01-03 04:25:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 10cd3e47-a641-365e-b84c-4c270d0b6850 | -3.90493 | -47.21098 | 2025-01-03 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa54a2f8-7402-3eac-9cbb-39addb935c40 | -4.26019 | -42.60825 | 2025-01-03 04:25:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 358a2b50-1cde-3815-be5b-f5657a1422cc | -4.26084 | -42.60399 | 2025-01-03 04:25:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31ffe799-5001-362c-abdd-caf7f6972bcf | -3.00686 | -46.70976 | 2025-01-03 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41bbab14-2cf2-3c0d-b4b2-9ff0528841ab | -1.82944 | -45.7673 | 2025-01-03 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fc57dd45-d6fd-3db6-9d84-eded65bb3263 | -6.97496 | -43.55587 | 2025-01-03 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bab27efa-38c6-3ced-b9e3-11ee0afc21c8 | -1.15734 | -53.77088 | 2025-01-03 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81e1694b-07e0-36d6-a8c2-87706413bf79 | -6.76294 | -35.31936 | 2025-01-03 04:25:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b7d7b868-1bac-3396-8922-9c0056588ef0 | -5.37014 | -44.84531 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5c2b0b9-fbee-3511-867d-c8b0587fcd2e | -5.50526 | -44.82971 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebb391e9-801e-3ac3-b676-798b950a7fe3 | -4.89225 | -40.82819 | 2025-01-03 04:25:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 175cfd30-82b6-3e59-b140-9146f3250480 | -2.29545 | -46.41496 | 2025-01-03 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 186dff86-9b34-3fcc-85a2-9d03668ca953 | -6.16348 | -43.16409 | 2025-01-03 04:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6e1d2117-dbc4-3e0f-9494-d81c51f54d8b | -6.69535 | -43.06622 | 2025-01-03 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f1df089-65a7-33ab-872e-43abef07c67b | -5.70193 | -44.80028 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e89e588-eec4-38c0-80c3-63a016739fb5 | -1.72528 | -53.23917 | 2025-01-03 04:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc382dd0-2c9a-34eb-a298-bc51a85d4b51 | -2.57797 | -51.9082 | 2025-01-03 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d39358a2-5b92-359c-a544-da436f3622f1 | -2.29935 | -46.41198 | 2025-01-03 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b16d9bfb-e504-3a40-82f3-d78c6531b064 | -5.5013 | -44.8328 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21b057c4-97ba-358d-9005-7f78bad0fcb2 | -5.15206 | -38.48364 | 2025-01-03 04:25:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4bad42e5-0f63-3f84-b116-7f4c7eb33125 | -4.12945 | -46.85679 | 2025-01-03 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f31324a-195d-3164-b7af-7e198cfb9f93 | -1.25386 | -53.86246 | 2025-01-03 04:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bf71dd3-44ee-310d-861c-29da9d57affa | -5.38038 | -46.28978 | 2025-01-03 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd798824-cdd1-360a-b7cf-d0041dc63e1f | -6.97199 | -43.5512 | 2025-01-03 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16b8d20b-2aee-3f4e-ad57-0f04c1769ec5 | -1.37772 | -45.8634 | 2025-01-03 04:25:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e53ae2b-7d76-3c71-8f4f-ffc36ab2d2c7 | -7.20758 | -39.73102 | 2025-01-03 04:25:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6bca8644-f18b-372c-8988-8625033e6e39 | -2.55352 | -45.5097 | 2025-01-03 04:25:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04debe6d-4082-3bde-a0f6-32c06860d580 | -4.16665 | -42.03129 | 2025-01-03 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 67d84dbe-e261-3a9a-80e5-51d57162523a | -4.16287 | -42.03073 | 2025-01-03 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| f19c93e0-f42c-36d7-b23b-abcd37d2fac2 | -1.77761 | -45.92247 | 2025-01-03 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 805ef261-b5c5-3b86-8d56-8ef7efae2dac | -2.55684 | -45.51022 | 2025-01-03 04:25:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a489c7a-c44f-3a4a-8cc5-5c9347e93c3b | -4.16735 | -42.02675 | 2025-01-03 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| aca8882e-099a-3ef4-9b90-c59229a39f9e | -3.97545 | -40.9199 | 2025-01-03 04:25:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 759129c8-84d3-3d5a-837d-770eb370fd4e | -1.82611 | -45.76678 | 2025-01-03 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8778676-3014-3954-9028-b47501bfb75f | -3.00742 | -46.70623 | 2025-01-03 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22337c35-b464-3fe4-893d-ac894df6e378 | -3.90629 | -47.05005 | 2025-01-03 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 348eedf6-ecb1-3950-94fc-00f69f4cd842 | -7.23393 | -39.77504 | 2025-01-03 04:25:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5aabd78a-c240-38b4-a18a-ad765e2004e7 | -4.87222 | -39.04945 | 2025-01-03 04:25:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cdc0ad60-21d4-3092-a06e-748f6be5ec7c | -4.80565 | -43.30427 | 2025-01-03 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d907be8e-f960-396b-becd-d9ea107a9fe8 | -4.40233 | -43.37675 | 2025-01-03 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 058469cc-38df-35cd-92d5-6f9dfd479731 | -4.16356 | -42.0262 | 2025-01-03 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 1f4cb473-de38-33a7-8afa-8aae063c3307 | -5.92411 | -43.78399 | 2025-01-03 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 734b1bdd-d78f-3d5b-9e0f-3e759f2578c6 | -3.00406 | -46.70571 | 2025-01-03 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f089654a-90a7-3fff-b67a-5ee456b323f8 | -1.68564 | -45.90452 | 2025-01-03 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19a91e9-b52e-355f-b894-f534dbd008b2 | -5.18456 | -41.53139 | 2025-01-03 04:25:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8bf2ce86-313d-3dab-89cf-37cb0ccf87a4 | -7.88563 | -42.44419 | 2025-01-03 04:25:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d1fe8337-10d0-39f3-8bd7-ceeb1ca9abf8 | -2.86715 | -45.25388 | 2025-01-03 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df1a3ebb-f7ea-323c-9135-3e2cf960de60 | -5.38425 | -46.28684 | 2025-01-03 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d26fae50-1741-3647-9c2c-cfabc7027fe1 | -1.25433 | -53.85942 | 2025-01-03 04:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e51309e-bca0-3f30-b316-9729cb3ad134 | -5.63082 | -44.83359 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0189eb2-6dc5-30ea-a321-5f44f3e7c339 | -5.18812 | -37.63768 | 2025-01-03 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 36512869-d496-3a16-9537-2923979b5c4c | -3.90572 | -47.05361 | 2025-01-03 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)
