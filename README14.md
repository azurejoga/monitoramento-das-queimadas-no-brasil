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
| ca4843ca-a035-3756-976a-b9eeeb867a6c | -7.93636 | -44.08609 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47d7d429-3a29-35b5-a06e-65886420a1df | -7.93566 | -44.09045 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e844cc5f-c332-3e82-a94a-c455fa7d60c9 | -10.6988 | -48.86688 | 2025-07-30 04:02:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 193ea87c-e4ac-387d-9c7c-6adad85d811d | -6.5319 | -43.33686 | 2025-07-30 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f24a946a-74bb-3bc0-b14b-d4e8bca28a59 | -6.42494 | -53.31608 | 2025-07-30 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 484842e9-678d-3a42-8099-2f2c0ed0229f | -7.35414 | -43.76651 | 2025-07-30 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67aa6c34-d0df-31a6-9d11-fc5e34d2b79d | -10.61484 | -45.2332 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a06be9fe-7f10-31f3-8ede-b95dab363850 | -6.25851 | -46.11564 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0efec57-f217-3c09-805e-8797d367bfea | -6.62333 | -44.04179 | 2025-07-30 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cb9f8fb-d3d6-34b7-8a7f-2c1dcc27cbd7 | -7.31597 | -43.40572 | 2025-07-30 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cf30706-038d-3d69-a9ab-ffdac4297fe0 | -4.58506 | -48.01627 | 2025-07-30 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ecc3f70-e853-3996-bec2-724c7bd9b1bc | -9.86694 | -44.70921 | 2025-07-30 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7bdaabec-fb9d-3dd4-9a7f-cd3521616eb1 | -6.97435 | -44.24846 | 2025-07-30 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36d931aa-89a1-36cc-95e9-73497c93d093 | -8.02568 | -47.67949 | 2025-07-30 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 692cc783-3b54-3c05-a8d2-29b68371c8fb | -4.85996 | -43.23171 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73969fdb-44b9-3f5d-8e31-e35d13736a9b | -9.40184 | -45.48933 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 64722f74-3aa8-3b89-8c03-de966d6d2e26 | -5.67679 | -43.6781 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5bb14fc0-ee6f-3b07-901f-724d29dac32a | -10.32717 | -39.20982 | 2025-07-30 04:02:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b767e592-6b40-3758-8296-ffc3bd933a43 | -7.09652 | -44.38039 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9313bc06-feb4-3b58-ab6a-4d9342232807 | -9.03996 | -45.07694 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5b0d099-1d8a-3298-8880-6ee81fa91bb5 | -7.34977 | -43.77023 | 2025-07-30 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c9cf940-9b83-3ab4-9145-bf1e23b58444 | -4.37672 | -49.03456 | 2025-07-30 04:02:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3338bf5b-2614-310b-aef7-171715838567 | -10.61784 | -45.23856 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8d1c91b8-6fcc-34f9-a4b0-05135711de02 | -5.67979 | -43.68316 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba40a1d0-44df-3c96-a73f-55ea696cb34a | -10.82465 | -49.37926 | 2025-07-30 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55cbf9da-0991-3e5d-ac1e-877bcac801b1 | -6.90648 | -44.72983 | 2025-07-30 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d66d2880-f6bc-38a1-b475-bfab5a9b1043 | -8.51682 | -39.29243 | 2025-07-30 04:02:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b9f47889-edb7-3b22-a903-a74122a4cd65 | -5.68796 | -43.67982 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 433faf0d-6c2d-33dc-9f5e-b0739f2e7b83 | -5.4826 | -42.15657 | 2025-07-30 04:02:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86798c20-db3d-3ac8-b8ca-f203a60157e6 | -4.64764 | -43.12974 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f97972a-d297-30b0-8294-dd771d06cc0f | -8.51759 | -43.31687 | 2025-07-30 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| bb8c179d-491a-3f34-81d7-57114bf84320 | -9.85202 | -44.70676 | 2025-07-30 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2708c1c1-d97e-385e-9705-b5ba8861ee76 | -7.38239 | -48.17257 | 2025-07-30 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4123678-b271-36ca-b953-1195ec7e2db9 | -6.88626 | -44.73129 | 2025-07-30 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1d483d4d-e8d4-3ae2-b26e-ff40e65bff96 | -7.15041 | -44.0504 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7f11e9b-ef97-3bf7-8832-13e5cb0214c2 | -7.5446 | -39.02605 | 2025-07-30 04:02:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| edb6eb27-cf3f-3152-b6ca-72f6ca2138d2 | -8.63243 | -45.88365 | 2025-07-30 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4ce8111-4fd0-3ad1-9887-b0a6147f773f | -10.61322 | -45.24271 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 71531c4c-28b9-3493-be45-01b738ae9525 | -9.86321 | -44.70859 | 2025-07-30 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2716426e-afe6-3960-9cbf-c3b0e65b45c8 | -9.18117 | -48.84542 | 2025-07-30 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef348736-e6db-3129-b762-4e92e90a5c20 | -9.32253 | -43.34254 | 2025-07-30 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db5e69a1-33f2-37a9-9e82-46573d98325f | -8.95943 | -46.73259 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b7b1d1b-4d12-30ca-a481-1c40e506699b | -4.85354 | -42.99561 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86e769a4-e4dd-353e-bf3a-c8246e3034be | -6.91632 | -38.56404 | 2025-07-30 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 956571ca-f7a3-3859-8253-cf11c935561e | -6.91744 | -38.55672 | 2025-07-30 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 464545df-507e-3736-bf7d-d3cf0a64fc38 | -7.08499 | -44.49884 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4defc8ba-2324-34f3-9eb9-b2e408cd3fa8 | -8.95663 | -46.74881 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50dcefb2-755e-39c3-9ba9-8c65b573a069 | -4.78076 | -43.37717 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d3be22f-6aeb-3791-a507-248aa384e3f3 | -6.89911 | -45.25484 | 2025-07-30 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba02b4fa-b813-35bc-ba45-57a1c1a3bfb1 | -6.30738 | -42.53281 | 2025-07-30 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6213c6d1-d5d2-31d0-a458-b264e0d80869 | -7.77964 | -45.00075 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e45e54c1-ace8-3e4e-afb6-cfd7ce5a31fa | -7.41491 | -43.87814 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86092482-97c7-3207-a20c-6e4716dabef3 | -6.97058 | -44.24781 | 2025-07-30 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 093ff2c0-0455-362d-af7a-a918303c8e10 | -11.45847 | -45.11648 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 305c0513-514b-30b5-965e-c6b61824df0c | -10.61703 | -45.24333 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ee563754-c6d6-3e88-86c0-bc2ec33e8fa1 | -10.9718 | -47.40124 | 2025-07-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddbcd29b-da61-3c83-adb4-886ac9ef7997 | -10.62083 | -45.24396 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d9a7c487-b90c-3506-80e2-07fbc3c4f1cb | -5.82195 | -46.34911 | 2025-07-30 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9779587d-7db6-3d3f-8d9f-5c7f58e10152 | -4.10328 | -48.20026 | 2025-07-30 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07daf8df-69d4-3deb-bfc8-6f0f5c3ddf88 | -5.68424 | -43.67925 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 992a96a6-5dba-3dd6-8f4f-25b615943f35 | -4.49809 | -42.93926 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d709c312-69b4-381b-af64-549627d9e0ab | -11.46668 | -45.11326 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8ef7519b-9480-3b68-835e-9d28066cd494 | -7.77656 | -44.9983 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fcc72c13-afde-31f3-a7b8-c0f808727ba5 | -9.60579 | -40.56379 | 2025-07-30 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69511843-c857-31c8-b203-8d8138f4dd6f | -7.31212 | -44.69214 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fae83b70-4a09-3699-bcd0-57fcba67412e | -7.94212 | -44.09058 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ca5387a-2f00-3824-a162-4fb285483f62 | -8.03724 | -46.9099 | 2025-07-30 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e358ce5-1162-3482-b4a2-349367544602 | -11.46471 | -45.11155 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a8107c07-c275-3826-b33e-c67c46b9f03a | -10.93527 | -44.19765 | 2025-07-30 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 581b4387-82e0-33bf-b4d9-c21221a76721 | -6.94648 | -44.22957 | 2025-07-30 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7212e40d-96d2-34bb-ad50-e8b8839a294a | -9.23239 | -50.04362 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0decb5f-09ef-314a-9354-caf6e8282d34 | -7.09026 | -40.59994 | 2025-07-30 04:02:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11827f5f-77e2-3394-a4ca-935e6a7c0004 | -7.12024 | -44.46846 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e25c8634-0866-3239-8645-66fa511fbd32 | -7.93843 | -44.08998 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c0acd50-f6ae-37df-a833-abc0226050da | -4.30344 | -48.10431 | 2025-07-30 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2142b9a1-1a57-3d89-9f74-9c4bb8b74c7a | -8.62837 | -45.8829 | 2025-07-30 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91c8bc13-d4c0-314b-a9cf-4a330a90e905 | -9.58034 | -44.44564 | 2025-07-30 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86350291-f5ad-3382-a672-f523291c2977 | -5.82126 | -46.35338 | 2025-07-30 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ca8960e-bb27-3122-a6a4-52b6942f614e | -6.89972 | -45.25124 | 2025-07-30 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35cade3e-203a-3fbd-9f08-24eab35aa780 | -6.60664 | -44.79022 | 2025-07-30 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d0e9524e-a889-328e-8984-c9da846ba50c | -4.65337 | -43.1175 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92e7c628-18b8-3c24-8eaf-5438f9846739 | -9.1489 | -49.85004 | 2025-07-30 04:02:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ab4a3858-0f2a-311c-9541-0f6dce66e611 | -5.73989 | -39.77395 | 2025-07-30 04:02:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 087031b3-5175-3323-b908-55496a58e816 | -7.94581 | -44.09119 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70a8c421-8120-3621-b984-3009eaac7cff | -9.02459 | -47.97784 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0eeb69fc-a9cd-3115-b53e-0f34ef52a0f3 | -7.14291 | -44.35677 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dcb574f-b58b-311a-be1b-83cfde342b95 | -9.23834 | -50.04122 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc383120-1447-3ab2-8c00-a7bdedac48f9 | -6.41038 | -41.13515 | 2025-07-30 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06efc438-080f-38f5-82b5-2d0ce9562751 | -7.85894 | -46.73727 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb73eca3-de03-3e61-9fb8-c6b19921e096 | -8.23621 | -44.91612 | 2025-07-30 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef0e81c5-8ede-3c9d-a4ac-faf70e0dbd5b | -7.38332 | -48.16726 | 2025-07-30 04:02:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e03350e7-89a2-3e92-8d51-424aa3ab02a8 | -9.74071 | -48.57529 | 2025-07-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3380abfd-21a9-32ac-aece-6cdac6f6e02d | -10.612 | -42.92958 | 2025-07-30 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4efaf550-55a4-377f-9395-505add56bd06 | -11.53368 | -44.26384 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c6f1119-d3dc-3e97-bd47-a1adb07cb71f | -6.40705 | -41.13464 | 2025-07-30 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0635de20-3ad4-3a63-956c-4ee89247bfbe | -11.46591 | -45.11785 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a23cee7d-d277-35f1-a58b-07258d87b621 | -9.22644 | -50.04602 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b372bd74-dd79-3507-88c8-7520e6571982 | -10.61622 | -45.24809 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f246e024-de69-35e9-a67f-b7957ba57fee | -7.3578 | -43.76711 | 2025-07-30 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef8dd00f-12f2-34e3-8288-bd86e6f8a505 | -7.1368 | -44.36997 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
