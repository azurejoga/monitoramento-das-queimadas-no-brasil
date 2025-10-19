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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3220e4c-f7b8-3fd4-92ea-6644b6b01f2b | -11.65253 | -47.31435 | 2025-10-19 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcd6892a-ec57-3939-b065-00f91804181d | -5.30306 | -44.84589 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed5e618a-cc06-3146-a265-65a2a754baed | -11.47659 | -42.21951 | 2025-10-19 04:32:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a6acce08-eb43-3711-a9a2-0e748ea59518 | -10.45451 | -45.02871 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd8b8466-800f-3cf6-acf1-e6d0ac6051ee | -12.48929 | -45.42617 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e564ad15-3092-313e-98ac-a1504184779f | -7.15065 | -45.80216 | 2025-10-19 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f97fbab0-c52e-3e57-b18e-902617fce2aa | -8.87833 | -47.97231 | 2025-10-19 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4126e2b6-c7fa-3678-8d79-cc5f1c58050b | -7.47341 | -47.07504 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0153754-c721-33ae-b5f1-f5e5d30884fa | -8.31714 | -49.49097 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4725823-a5f4-399c-bdf1-809083aaaeda | -5.93173 | -42.2549 | 2025-10-19 04:32:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5d0c128b-3657-3288-84bf-6cd23b0a032d | -6.14818 | -44.29972 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 642631b1-6c13-3171-aa6b-8786a0aa03a2 | -6.60981 | -44.20955 | 2025-10-19 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fdd3ddbe-5858-3be0-b3f4-d06d93af3ae9 | -7.19314 | -42.18666 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e3873969-60a4-3243-be58-9799f0039212 | -11.43461 | -44.93702 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f81a2318-1bad-329a-9aa5-2571bd316290 | -10.36919 | -47.46827 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5316a31a-27d0-352f-8255-fd426fde8421 | -5.52275 | -44.10928 | 2025-10-19 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ad03479-740f-3697-8d25-dda984727044 | -6.02267 | -41.92463 | 2025-10-19 04:32:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa95193f-3493-3b5e-b023-23ea49a28115 | -7.4164 | -40.0797 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bcf2215f-1e25-372e-9fc4-90e12a3425cd | -8.69974 | -47.07075 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33ba0bb2-3c5b-39e2-a7b1-559a249079e9 | -5.66467 | -44.7067 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 651a2228-4374-3128-bc2a-d2a78c2c5d84 | -7.94043 | -39.85001 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04d5e927-98a1-39d9-a03d-1d96cc580036 | -9.98511 | -47.05135 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4501400-5f4b-3953-8b88-116472e524b8 | -5.59739 | -50.05775 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df141636-1117-3f62-a934-1dc4309783a4 | -5.36984 | -45.92836 | 2025-10-19 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8636d36a-be13-39f5-a488-847ee4b9dce6 | -7.32644 | -47.25633 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47d509b9-193d-3906-b51c-53c668b71014 | -9.0777 | -48.02212 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9324973c-8540-3d0b-92dd-ca6b68384df2 | -5.64194 | -44.80942 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3956b3df-1f79-3a65-9c7a-d7559dafabdf | -13.21413 | -43.15425 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0c48264-c835-3a97-b4e1-f73dfd0e782e | -7.15668 | -42.37621 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 445af7b9-eda0-3492-b073-5d8b9d76cb27 | -5.30817 | -44.79405 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6af30e1-d0bc-3898-b2bc-43e6b54610c7 | -7.15778 | -42.36874 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 74ed8a73-4398-3696-b942-1d85a8a5c6ce | -11.79075 | -49.31979 | 2025-10-19 04:32:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cace2dfe-d162-359b-926d-376d5bb5b4b5 | -10.88898 | -46.08846 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| da00096c-f287-30d1-8c74-256e4191700f | -10.88782 | -46.07198 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3b1b65f6-cc9b-3e03-b365-5d2c718cab87 | -9.23728 | -48.5607 | 2025-10-19 04:32:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d67fa58-4035-3137-84d3-5909273762a5 | -12.31529 | -46.79811 | 2025-10-19 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db3489ca-a29e-3539-88a5-ca8354621edb | -12.15388 | -45.06517 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0053d6f5-24a5-33fb-9e0f-47a92d5113db | -5.3151 | -44.84335 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15645f12-2b62-3520-b6c4-0def9e468f04 | -11.98444 | -46.92974 | 2025-10-19 04:32:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 899aefb2-56fa-3e55-b0e6-cb5ae1cacc83 | -7.15833 | -42.36499 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 61af1a6c-d689-383b-9c98-404f71a61def | -6.86105 | -46.29659 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f19145be-d25f-3bf7-8564-f009915ab40a | -10.30237 | -44.04512 | 2025-10-19 04:32:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6684733d-263e-3194-afd0-3db7c651f15c | -7.92933 | -50.00041 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d342118-4fd1-39d5-8d16-c0c821afa3c3 | -11.89116 | -45.43765 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d23fde9f-8aa3-39b6-b55d-967da695f8aa | -7.64749 | -46.67433 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 326d0eaf-61fd-32bc-bcf7-ddbd42fac8aa | -7.18441 | -42.21685 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c99452ec-8a94-39bd-8fe4-711ac4809fe2 | -10.80709 | -44.01577 | 2025-10-19 04:32:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51dae7a7-0e60-3839-a4e2-c560dc4047ac | -9.25721 | -44.34164 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ad37ace-de95-3640-a25f-5fd00483b502 | -10.23431 | -44.90028 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4d21f92-29bf-36f5-ad08-c96d3ed6c7b6 | -12.15455 | -45.0605 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df4cea61-7453-3b21-b5d0-ca2cbdb20b32 | -4.96544 | -56.27372 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 991e10e5-a5ea-3e92-a3f3-786431cc3ea4 | -6.26162 | -44.34102 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8026b21a-a6fb-3373-b0c4-c722c1b1637b | -12.44676 | -44.74742 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff5bbd1f-d4c6-328c-b934-81fea2f53682 | -5.46332 | -44.88847 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d91da9ba-c424-3137-ac0b-e16c8d33d16e | -7.31192 | -42.47379 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0551fa76-aa45-3d75-b173-72a658cfe1c3 | -11.55898 | -46.89715 | 2025-10-19 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b1d164-03c4-3235-bfe2-e7f114323b71 | -4.96458 | -56.27918 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ec0f5e2-d7fa-3692-a0ce-db478afc9233 | -9.33 | -46.11289 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 872594c4-a6bd-3012-9272-cdf45ba6296f | -8.8977 | -48.02167 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3090b75e-7338-3e2a-b163-d0152b3d5b2a | -10.62967 | -48.02171 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d002312f-67c7-3caf-b81b-38c21aa00e75 | -11.79131 | -49.31626 | 2025-10-19 04:32:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d006244-9302-3ae4-a687-2dc2fd3e8c6c | -8.25306 | -43.32543 | 2025-10-19 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2b44fda0-01ab-32c9-9414-58c66836cd53 | -5.33447 | -50.99766 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd8f8ea1-e5b6-3c17-800e-f04912c6fcaf | -8.60807 | -40.19784 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 358f7bf9-3ca0-3e2a-907a-42eced2d54ee | -9.22966 | -46.05884 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b249710-7e60-3bdf-9e34-68bb5c3d09b3 | -12.14704 | -45.05942 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 46f378ba-be28-3c02-89ef-826b18178f75 | -12.46186 | -45.44204 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d0f048c-5a58-3ea7-a159-d904b14b00bf | -5.61313 | -47.86804 | 2025-10-19 04:32:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60980923-331e-3001-a366-ff035f7708a3 | -5.64253 | -44.80545 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0ff574c2-d2b9-351d-a5d7-d51807bd38e3 | -5.40302 | -44.05971 | 2025-10-19 04:32:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7327b00e-018f-3340-a2a2-568f651f27bc | -7.44914 | -46.84027 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28d258c8-ad35-33b4-84b6-13c5cd223752 | -11.63022 | -44.07661 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 204fdc6b-661b-37af-b038-3271d0bef576 | -10.6788 | -44.55421 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad27f44e-a963-332a-93bd-3bf5b26bf168 | -6.67397 | -58.74631 | 2025-10-19 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02998818-bfb9-3cb7-b7ec-06a7d8f9e113 | -7.40999 | -40.07473 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 227d2531-e10b-3983-86ca-264deae9e6a7 | -8.43651 | -44.14315 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f8fb9bb-a73f-3801-8316-fcdd9a267b8f | -10.68861 | -47.94822 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe5955fa-5340-3f72-9666-06e9b41ab54d | -7.32698 | -47.25284 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29d8570b-6396-30df-8179-95007256111d | -7.65305 | -46.66054 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51ab9265-e2cb-382d-927b-ba1096b4b2da | -6.86443 | -46.2971 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 924f27af-1168-3e01-b509-f3f40a0d31ae | -8.6466 | -47.06584 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2044cd68-54d9-37a8-b6d0-c47f739cbfd9 | -6.67313 | -58.75079 | 2025-10-19 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f76de7e-a411-3e34-9142-ed0105ef3195 | -7.18167 | -42.17709 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd6850c1-8bde-3293-9ff6-48478ddac2fd | -10.5943 | -48.00875 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3526d0c4-e835-3214-88c1-371973e01061 | -11.87208 | -45.46596 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ebd3dadb-29b9-30bb-9921-2bb98d97961d | -4.75807 | -50.69645 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1cd9f4c5-b962-3c39-a9d2-49c4c47d7ca0 | -6.1495 | -44.28846 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e799475c-32db-3a42-b50e-3700aa05aa91 | -12.18355 | -45.09834 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73e381f3-93f4-3941-b1e1-03d45eb4b5f4 | -7.40082 | -46.69444 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57ce4ddb-f6ca-33ec-8369-cc644ea4e9aa | -7.44859 | -46.8438 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac63695-6242-3036-9d79-2bb4328650bb | -5.32441 | -45.78796 | 2025-10-19 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75224455-96df-3729-973c-742116d4be9a | -5.5309 | -46.98884 | 2025-10-19 04:32:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe9f1d0c-c94c-3785-9b5b-5ff9d32fc712 | -9.25345 | -44.34107 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd9c2c8b-5dac-3920-94c0-a0d997c51eeb | -10.61365 | -48.01545 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 24e74bab-e146-37b4-aecb-c6259cc8d846 | -10.22421 | -44.06395 | 2025-10-19 04:32:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d0e810a-511a-3928-abcb-b234c55a15c6 | -6.261 | -44.34519 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5705948f-ca62-3984-aeef-c959ff59ac88 | -6.41994 | -43.91638 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4eb5622e-de9c-37f2-9d6e-ae523ccb7028 | -7.05397 | -44.23701 | 2025-10-19 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e68e6591-22f7-347a-a5a2-6f995aa4cec1 | -8.31378 | -49.49043 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6dc7af2-4d6e-3d8d-a6dc-32ee98b8ceb4 | -9.7598 | -43.9561 | 2025-10-19 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
