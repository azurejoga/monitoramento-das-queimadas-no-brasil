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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cce716b-3dac-3d53-9b37-c6278aa46e3a | -3.76807 | -51.77468 | 2024-11-09 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0cf699d6-3332-3366-8066-c10e28e8aeee | -3.833 | -46.51418 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5254986-7de3-30f6-b67e-c153bf9b11c5 | -2.21887 | -46.43213 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dbb61536-1eee-368c-92de-bfb675d3e6d3 | -5.63419 | -44.82389 | 2024-11-09 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bf606814-6601-3ee2-bca6-f90a9038ac0a | -4.03189 | -47.14536 | 2024-11-09 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0a0f3437-4483-3920-a491-896c6c4ad0e5 | -1.5581 | -51.17948 | 2024-11-09 00:39:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 2b63921c-e119-3e40-852d-28ce4db4fc56 | -5.83946 | -46.23846 | 2024-11-09 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2cd60b3a-c863-3802-98c6-4d064b2ef703 | -3.53339 | -45.7485 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 6d500bb7-b40e-3e1c-b723-4364b436cf21 | -2.09807 | -48.90278 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b901c53f-f07a-3f12-a5d5-9a0054cee92a | -2.08199 | -52.05122 | 2024-11-09 00:39:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 65764d1b-dd43-3975-88ba-296ec0d26307 | -2.11441 | -46.21082 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 12edb51d-0586-33ed-831b-018d08033aca | -2.46052 | -46.31449 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6de4d819-379b-374f-9704-ab554804bf52 | -3.60707 | -51.24865 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8e3b1a10-9bc8-375b-b66d-d907b7cce6c6 | -4.23357 | -47.55727 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d9d1a77d-5132-3e9e-a43d-d01c884f6d88 | -4.35468 | -46.81846 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 66331eda-f6d1-3b13-956e-9b1538596a19 | -2.88409 | -48.29873 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 04023265-8ccd-3da2-92a5-9e10f8d44dbb | -3.97025 | -48.17101 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 8c96f29b-5b2b-34ea-97ad-5ce5e5101ca2 | -6.29013 | -47.35047 | 2024-11-09 00:39:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f6f7e2c6-a838-3565-86cf-c3ed8dcec1f3 | 0.047 | -49.54644 | 2024-11-09 00:39:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1f51f05c-0ff3-3510-835c-0134b84f7911 | -3.10374 | -45.77489 | 2024-11-09 00:39:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f50ab30e-cb37-3ede-bebc-99330ece70c5 | -2.45024 | -46.30656 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a34b8b8a-b3cb-3454-a463-45d3364f6eac | -5.44406 | -43.26233 | 2024-11-09 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| db1efada-8e39-3f13-b721-7924567bd98a | -3.15125 | -52.96916 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 545.4 |
| ab9f2a40-dad4-3dc9-abde-02a8bc8a2e98 | -3.40547 | -50.00332 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ce1246ed-717f-3a92-80bf-f4ec7ec7f88e | -4.25762 | -47.58727 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7f59206d-8b6a-3247-adc9-23a9376987be | -4.42048 | -43.38893 | 2024-11-09 00:39:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 66b1c42b-d78c-3c51-a2b2-29e5b6af50ac | -2.67326 | -46.78419 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b4805fff-b7a4-3ec9-92fc-b9612135cf9e | -2.10796 | -46.23025 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d38c0b0e-db6d-3aa4-aac8-fe7b3561c1c5 | -4.01723 | -44.58939 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ef71132-de6c-3cef-95af-f9744e77eec4 | -5.14529 | -47.72379 | 2024-11-09 00:39:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 31312be0-195a-3989-8722-79974233845f | -2.40409 | -48.52722 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 61138af0-3ed4-3338-9a24-2564b3c5629b | -4.1729 | -45.37244 | 2024-11-09 00:39:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 53cf6bbd-0d65-3b25-a5b8-9ed99b8df1d0 | -6.26989 | -44.54936 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e8d4ea38-09ef-3ea8-bc50-35d1e12b9530 | -4.64881 | -46.02197 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84d029eb-757e-3b23-b62e-0d5e273b7a8f | -1.94911 | -46.41346 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 91aa0bb7-ede3-323a-be82-06bcbb733b31 | -4.2018 | -45.8521 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 270.3 |
| d3d80d7f-96e9-3010-aac6-d8792fec8a2e | -2.84181 | -46.73883 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 722a051e-ba15-3e8a-9d29-c5271604602c | -4.43839 | -43.64752 | 2024-11-09 00:39:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| a73a73ba-01b6-3874-b058-796e437499a3 | -3.2159 | -50.37708 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9a0c388c-ee19-3d7d-a39b-0aa3d6d902f0 | -4.25366 | -48.53632 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4ba7c9e9-0da7-37df-845a-d8224f3c6ed4 | -3.61409 | -48.92158 | 2024-11-09 00:39:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 050de08d-623d-3f90-b85f-1b3ca40480f2 | -4.21483 | -48.69049 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 4efb364f-971e-310f-8de9-96b086ce09b5 | -5.08212 | -47.94005 | 2024-11-09 00:39:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e8200189-9ad1-3830-8d99-0b771bbf236d | -4.75364 | -43.85997 | 2024-11-09 00:39:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2d6f8d8-9ba9-35f6-a9d1-16686aa83d23 | -2.39755 | -46.59381 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 74694068-0ca1-3dba-ba89-45d41f8adde8 | -3.09175 | -53.32562 | 2024-11-09 00:39:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 4de9c37c-d051-35ff-8051-4d2a86841da5 | -3.97351 | -48.19465 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b292d0e3-e96c-3f5a-9e0b-16e15dab2a95 | -1.51254 | -47.18304 | 2024-11-09 00:39:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 058f3e1f-4ca0-32ea-8ed6-2dc6e13441cf | -2.68247 | -46.78293 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9b86302f-75cb-3e09-b4ab-e5d7358e6480 | -4.50578 | -46.39113 | 2024-11-09 00:39:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a4d33cdc-87a5-3814-8dcb-8c4fea410d5c | -2.62199 | -46.14926 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9ed54278-8422-3ae4-855b-a19a92070db2 | -2.82182 | -45.46364 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c20a21c4-5a93-3d4e-8763-98621a396486 | -3.15011 | -46.50697 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2f7aadd5-62ee-3e59-9031-8b0711d7bec2 | -3.72548 | -54.22748 | 2024-11-09 00:39:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fafd4529-a09c-3d7b-89c1-bf0aa87897d2 | -2.30827 | -46.47966 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b1bf5c0f-668b-3fc4-ac0e-63c699929411 | -5.62656 | -44.83403 | 2024-11-09 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| fb908d7b-239f-3721-8f83-704d2950b234 | -2.30181 | -46.69592 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| db57831e-2442-386a-9107-42178ddfedcf | -2.12818 | -46.37622 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c7a10999-3005-3ce8-9917-b80f7f3e2f4d | -6.61876 | -43.61909 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33f08007-0d73-36c5-ac40-499c2ba70560 | -2.96581 | -49.28428 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 11a67f7b-7f6c-3193-8834-3957d92fca01 | -4.14881 | -44.40557 | 2024-11-09 00:39:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 482f72ec-f935-385e-8044-6518b12e6a8a | -4.03585 | -47.13899 | 2024-11-09 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 54e207d9-c7bf-3c2c-880b-6b6d6d85b523 | -3.57968 | -47.34374 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 07dffd92-9d37-3a0f-ae5a-25cbbf1278cc | -3.11097 | -45.95761 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 248ea61e-115d-3b30-9080-388bda4fe774 | -2.955 | -46.75632 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2fad347e-9526-35ca-8769-26a34f641b43 | -4.20613 | -48.54887 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 269.5 |
| 1cf1e282-b2dc-3c55-b7d4-d223d1ce3673 | -2.53267 | -46.30439 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 39653e59-2ca5-3464-826c-19ee232bc765 | -5.04201 | -45.86723 | 2024-11-09 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7d9fafc8-96ac-3c5f-8067-b3de28fbf5a9 | -3.53214 | -45.73951 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| de22d326-2138-397b-984e-0373606312a4 | -3.58781 | -47.3321 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 180fbf12-26a6-3f7b-b9da-796532f36fee | -2.15231 | -46.68485 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 61e76940-558b-3042-a281-3045b95dbb41 | -4.82568 | -47.32272 | 2024-11-09 00:39:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |
| c3a6d78f-bd8c-3aa1-9089-57e9e3c45878 | -3.55191 | -43.56867 | 2024-11-09 00:39:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 144e0528-781d-3120-9e68-4454ed170527 | -2.79695 | -49.65445 | 2024-11-09 00:39:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7ee17403-40db-3bc0-adde-1de89f0f438c | -0.40702 | -51.47464 | 2024-11-09 00:39:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f9672191-8692-3ae3-918d-260dd93a8a39 | -4.38482 | -48.58953 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f498b40b-fbd2-354f-a163-17f7ec9ca092 | -3.17021 | -48.37271 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f8265996-95dc-3e80-8c25-3cf282419e22 | -2.56822 | -47.35232 | 2024-11-09 00:39:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| e212363d-cf24-310c-9db7-c6ff19b96255 | -3.08445 | -50.57978 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e0e1746d-b744-3760-839e-25bc545d4d95 | -3.40753 | -50.01904 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| d428f08d-2a42-3e94-a92a-120f4a5535e4 | -3.04267 | -50.36223 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| ff5ab091-266a-37a0-a3ec-73245012c65f | -2.94778 | -52.72064 | 2024-11-09 00:39:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 378f0050-c38f-39b7-9e31-ac6aa862ad4a | -3.06573 | -48.05769 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0a4f574c-187a-3cc3-a8c9-0e9bffe4b4ef | -3.04492 | -50.37879 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 950ddb1f-48bc-3002-b77a-5cf1505c7d64 | -2.88248 | -48.28714 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 51b3fd65-9fb9-339e-a671-f52d8d0397c4 | -3.95688 | -48.14891 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c55bc4a1-4d74-36b5-a761-7931f89087ee | -3.54232 | -45.74726 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| dbac9b90-4155-369c-b48d-b094bfc6e837 | -5.27302 | -45.87331 | 2024-11-09 00:39:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| aba7e2d5-5b0e-3d03-9eea-1e36784f68a5 | -2.0837 | -46.51974 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0077a56a-a375-387a-b962-11deef81835c | -0.82515 | -47.81584 | 2024-11-09 00:39:00 | TERRA_M-M | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c07e49f4-2750-34f1-8d3f-06e6d7284bb8 | -3.17199 | -51.31849 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| b6a7fd47-10d4-34a2-9abf-92f11b8895ae | -3.54288 | -43.56996 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a87ce10b-4e51-3744-ba98-dc64b6acf738 | -6.23123 | -47.29556 | 2024-11-09 00:39:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3c7dad60-ab33-32cb-9c4b-e05ff2323bfb | -3.25151 | -49.11706 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2f273d60-8568-38d0-8e07-a248cce9abe9 | -3.13082 | -45.76521 | 2024-11-09 00:39:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 835fda7c-e7a6-357c-bb8c-8ea3dacb3421 | -2.744 | -49.16277 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b378f9f7-1371-3dbd-aa4e-ed8f5b5546c9 | -4.82365 | -48.22587 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5056b742-5661-3512-939f-147467c4e617 | -6.21319 | -41.6622 | 2024-11-09 00:39:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bd0d1d19-55a8-3f6d-bad8-8401e4b44bb2 | -4.49045 | -48.48504 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6d350494-6e35-31ab-8005-731aedc90dd2 | -3.24613 | -46.46832 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README6.md)
