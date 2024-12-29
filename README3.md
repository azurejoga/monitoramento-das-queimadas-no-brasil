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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30931e70-3514-364c-8915-2bf66e091132 | -4.71101 | -44.61952 | 2024-12-29 04:21:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75b1d03-9e9f-340f-ad46-446952aad700 | -3.94098 | -43.51472 | 2024-12-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9fa5dac-6af2-3cd5-a32d-376b3d3952f8 | -6.98499 | -47.08676 | 2024-12-29 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f711548f-a4ad-39fc-9137-324cbec64f9d | -5.48616 | -45.47395 | 2024-12-29 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 316688a7-59d9-3f67-9576-5402988ea168 | -12.71663 | -47.62607 | 2024-12-29 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f2d9438-5800-3d02-9693-8bdd6ba09e24 | -10.43439 | -44.88915 | 2024-12-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 734f5abc-448c-30b5-9863-072933ff6599 | -13.11332 | -43.37115 | 2024-12-29 04:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed3e7ac3-f3c0-3c28-a629-597c1d19f5de | -12.64088 | -38.56802 | 2024-12-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e38aa7e5-7908-3ed2-b93f-3b33f5dd1222 | -11.95942 | -44.21877 | 2024-12-29 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29d5bda8-4993-36f0-8926-53fb7fa1ba9c | -22.5404 | -48.81382 | 2024-12-29 04:23:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a16a6879-312d-3316-8184-72d6e4859ff9 | -12.93473 | -41.11549 | 2024-12-29 04:23:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 92f29240-c7ea-3234-8afc-ae1c399d1eda | -13.11272 | -43.37532 | 2024-12-29 04:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8debfda6-293f-3522-a441-748ead5fbc26 | -12.41151 | -38.83656 | 2024-12-29 04:23:00 | NPP-375D | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d9357ba7-2e4a-3e2a-b6f6-4530be3dc0b8 | -19.08377 | -57.71051 | 2024-12-29 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d9332662-a4a6-37b7-af8d-0dafd89e5654 | -12.93064 | -41.11501 | 2024-12-29 04:23:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 38c2c458-9b09-3981-a541-e0fe8ef15305 | -9.94486 | -44.12397 | 2024-12-29 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 194ff04f-2fac-3abe-9ab8-fb4c7aa43d42 | -16.89483 | -40.55244 | 2024-12-29 04:23:00 | NPP-375D | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b7234efa-2e64-3703-8b66-68e52225283d | -22.78589 | -43.75471 | 2024-12-29 04:23:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ef31a493-2c71-3f25-8836-f2e43122aa82 | -18.78649 | -52.58308 | 2024-12-29 04:23:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0261dca-6227-3274-9c5d-f6113db2973d | -11.88683 | -40.95734 | 2024-12-29 04:23:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 31f8de7d-ad7e-363a-8473-5d622b14b509 | -16.8904 | -40.55148 | 2024-12-29 04:23:00 | NPP-375D | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 14aa024c-ebee-3c25-890c-b62723df3fde | -20.56054 | -54.65245 | 2024-12-29 04:23:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95c99499-2e63-3dd4-a0cc-c3b3b50296a5 | -18.79043 | -52.58384 | 2024-12-29 04:23:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f875877a-7687-36a7-9b12-8b548b70f1c2 | -19.083 | -57.71412 | 2024-12-29 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| e91ac618-4442-37b6-b94f-9ca47ed15aee | -12.64157 | -38.56269 | 2024-12-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ef326062-5431-3f98-ae50-f399e1c356c6 | -10.73181 | -42.69772 | 2024-12-29 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 69c5d3b4-4176-3c0b-a6aa-b0f02d87f91e | -20.99718 | -51.79302 | 2024-12-29 04:23:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8f2e1899-9a43-34c3-b89b-c29cb115b5b4 | -25.69369 | -51.56026 | 2024-12-29 04:25:00 | NPP-375D | PINHÃO | PARANÁ | Brasil | 4119301 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e4089fde-fa4e-3f01-8748-1c779ff79357 | -23.98269 | -54.18783 | 2024-12-29 04:25:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 79ad126d-dc98-30f4-8ad9-5b459912284c | -23.98071 | -54.19204 | 2024-12-29 04:25:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 47dcd705-eca3-3acc-b203-d1f729f0850c | -29.57847 | -51.98642 | 2024-12-29 04:25:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3712876d-356b-3209-a772-8887ffdbc3da | -23.70602 | -46.47598 | 2024-12-29 04:25:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 906796bb-1fef-3d7f-8867-a48735ed73f7 | -23.33665 | -46.77118 | 2024-12-29 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bcd5e550-a924-37f7-bb4b-e480be18ff85 | -23.34009 | -46.77178 | 2024-12-29 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9623947f-1761-321c-8128-20a27e0b36e7 | -23.98161 | -54.19335 | 2024-12-29 04:25:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb6e4278-e104-3804-92cb-f3d0c498b600 | -29.87362 | -51.15655 | 2024-12-29 04:25:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 85c6ce41-c3a1-36b4-8d64-e9c0551e31ab | -29.58185 | -51.98717 | 2024-12-29 04:25:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f97395c-cdc1-3668-9091-d1cc438ab9a0 | -23.40648 | -46.5573 | 2024-12-29 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c483a5ed-7129-36b2-b25b-a30828edbebf | -2.15218 | -53.73886 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9762bb4-4dab-3e02-b888-c634ad16289e | -1.89615 | -53.33052 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1837713-0553-32b8-8ac1-0295fd65c374 | -2.14846 | -53.73829 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f497e91-b2be-3216-8223-3e5c11ad9b1a | 1.57774 | -55.85067 | 2024-12-29 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00d3646c-ea26-3c7c-bc70-37edd7f4e79b | -5.49493 | -43.98465 | 2024-12-29 04:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b07a04c1-a3e2-3833-8247-e4e0f17c5734 | 1.58156 | -55.84543 | 2024-12-29 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 126fcbc5-f05d-32d6-8235-f15571daea13 | -5.48726 | -45.47646 | 2024-12-29 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53f4d586-0996-3718-8cd9-f28402409954 | -4.54657 | -50.18836 | 2024-12-29 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2e51bd4-d213-37cc-9e36-939d35aa312e | -5.49439 | -43.98164 | 2024-12-29 04:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2dbe7054-a4c2-3bd2-a8c4-8462a7a65879 | -5.76325 | -37.56499 | 2024-12-29 04:42:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 13de1c47-025e-3e36-9254-e51e4f27fa1f | 1.11122 | -59.19638 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45cb1833-47f7-3303-8578-1055c6d644a9 | -1.71388 | -52.41196 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bc99d3d-2e77-3355-9490-91f917c456e7 | -2.58482 | -51.9203 | 2024-12-29 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1ae218c-be33-3cf1-9637-1c6ba8385f04 | -2.85229 | -51.8236 | 2024-12-29 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 523cfb5f-ee84-3985-b313-47ee94a56d0b | -1.87472 | -53.30104 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3777d0a2-acd8-358c-bfde-8956875fda47 | -4.52018 | -42.07047 | 2024-12-29 04:42:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 51dad41c-75b7-3e45-a199-5b9f2628ad87 | -2.37869 | -51.8057 | 2024-12-29 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89841a89-3acd-3451-b0ff-ec9374bed36d | -1.79665 | -53.1348 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 186af7a9-2513-3412-8747-d4c3e3dfd9cb | -5.49137 | -45.47705 | 2024-12-29 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f300f0b-6f0c-317a-baa0-5a1f8e8545a3 | -1.7075 | -52.40699 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceacdf66-79d8-336b-9692-015d9f69fb6e | -5.13083 | -45.1629 | 2024-12-29 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47bd3d4c-dfb3-35cb-8a6a-af0cf8b29b66 | -1.71038 | -52.41141 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3694b749-a63e-3ec7-b8ee-73bd96166f80 | -2.58423 | -51.92398 | 2024-12-29 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf19d9e8-683d-34d1-ba07-9c7adab7a291 | -4.78653 | -46.39452 | 2024-12-29 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 874d63ce-a425-3447-93ed-b0e2ea6f7658 | -2.38744 | -51.90471 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cb5090f-619a-33e0-9f34-1baab74510c3 | -2.21968 | -53.65 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dfc3f1e-950e-38c5-9be6-543e7856c4f0 | -1.15129 | -53.59396 | 2024-12-29 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00929b95-71f7-3876-9680-ed1470b6f37e | 1.10791 | -59.19586 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0740334-ba92-3015-bb43-883f40320e0d | -1.79915 | -53.13665 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17d3662b-611f-30cf-bb53-403f5ee3e1cc | -2.11242 | -53.66671 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f47bd650-abb9-3ef7-aaf0-2c08115bfb03 | -3.24645 | -44.30436 | 2024-12-29 04:42:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db088d26-da5d-3996-af27-78df4c10a893 | -4.82169 | -45.37305 | 2024-12-29 04:42:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bd1f4c8-60ad-34ef-a5c8-640fc1520cf3 | -2.3689 | -53.88386 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c913d7-299e-3a89-b9d1-48df6f82c774 | -1.69077 | -45.84057 | 2024-12-29 04:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 340924d8-2023-3024-8781-8308505cd5b2 | -4.79038 | -46.39501 | 2024-12-29 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05f0a5d7-128d-36c0-a7b3-0766916b433e | -5.49558 | -43.98006 | 2024-12-29 04:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5bced8e-f4a7-34fb-9a64-1792addd0501 | -4.79424 | -46.39546 | 2024-12-29 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f102e6c5-0e2b-304a-8cfe-cee89cfc524e | 1.03876 | -59.73666 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 131841cc-7f92-3293-877f-31f245a8b606 | 1.57705 | -55.84613 | 2024-12-29 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1c8d0d76-33ac-3130-b14f-cc53a1853b65 | 1.11414 | -59.19875 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b87a36ba-34ba-342e-859a-bdb68398af67 | -2.30936 | -53.89035 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60632291-56b0-39ba-8836-60c41cfc6022 | -2.18123 | -53.55914 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74eff72e-862a-3c8c-820a-c998e0f051b3 | -1.8998 | -53.3311 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ed6e66c-4a05-3c15-825e-7fe18676799c | -1.71162 | -52.40367 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2a20739-60ac-37b7-a0da-6fd56d215d57 | 1.11353 | -59.19496 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de48486-66bb-36b9-88f9-a795faa2f990 | -2.38686 | -51.90839 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a035ce1a-0762-3fa1-9a1a-d52c9a81fb79 | -2.17755 | -53.55854 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03113a70-a86d-33cb-8356-ae13960d2095 | -3.25075 | -44.305 | 2024-12-29 04:42:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27e96662-1eb3-3ee9-b5a0-5d51a1cc72cc | 1.10851 | -59.19965 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc540eae-cfa6-3200-8dd7-e6dcde966c35 | -3.24583 | -44.30842 | 2024-12-29 04:42:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23f9f2da-7cb1-3a5e-ba7c-bc5dba7dcf19 | -2.83664 | -51.74682 | 2024-12-29 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b10764c4-57ad-3bca-945b-7b065cbda033 | -1.79553 | -53.13608 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c5a5dcd-4d17-39d8-a505-3b531b6db442 | -4.19889 | -42.89906 | 2024-12-29 04:42:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bee2e0a7-da56-3e9f-a3d2-bbf215547e03 | 1.1118 | -59.20019 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edb9b6ec-77f9-3bc0-b5ce-569f22cdf742 | -1.93733 | -54.42058 | 2024-12-29 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a62b954-89f1-376d-bd02-e13153060851 | -2.25391 | -53.55305 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 100aecf1-c52b-30f3-8750-5f4a685fafeb | 1.03294 | -59.73757 | 2024-12-29 04:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64f46eeb-faa5-39d7-92d4-5d747e2dad51 | -2.25759 | -53.55365 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a80442d1-0228-34e7-9d3d-9e9e8b50f6c8 | -1.70813 | -52.40312 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27d989a5-42c1-36fb-8af7-1b042ab42a70 | -2.58082 | -51.92345 | 2024-12-29 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d9a632b-3018-32c2-83a7-dcbed1144d1f | -1.711 | -52.40754 | 2024-12-29 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8093fd15-b60c-3e48-8bb3-e9c4f0711920 | -2.25691 | -53.55798 | 2024-12-29 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README4.md)
