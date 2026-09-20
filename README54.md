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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a1d0f7-6ea5-3d03-bdd7-2893f7e36205 | -4.84658 | -40.52697 | 2026-09-20 04:38:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de0fd539-57c8-3ee5-81f4-8b5e43cb968f | -3.01004 | -54.18092 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e0cb02-d6c5-34d5-a42b-4946c086d3a7 | -4.68181 | -40.14387 | 2026-09-20 04:38:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5bc27064-94ab-35e1-9cac-1769dc27a66a | -5.81198 | -49.08848 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d70446d5-5335-3ca9-a6c4-8d35d57179d7 | -4.26325 | -48.63927 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec9c8446-7c7e-314c-9cab-f9ccf558b506 | -6.40405 | -43.17715 | 2026-09-20 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c06ebf57-6575-3447-9f85-74d7978fa085 | -4.81237 | -45.7745 | 2026-09-20 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04980e57-6a8c-3ce5-9403-3210bd87d67d | -1.25847 | -55.76691 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a37edaea-6988-3eac-939f-519c7e754e08 | -6.39854 | -43.18694 | 2026-09-20 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6441f75-6810-3104-9163-0bcdb1d73660 | -3.16652 | -48.61153 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 21f9d83a-6e28-3912-96b5-6f465becb256 | -6.18472 | -47.49367 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17fe1003-b9cd-3e49-8ce4-dae91fa33c84 | -3.85065 | -45.42791 | 2026-09-20 04:38:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9535329-a2a0-3b09-bcd2-7c75da0b7f92 | -5.79566 | -43.77158 | 2026-09-20 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0c1ce5f-ee00-30e8-b7c0-dc9afb833bae | -3.74403 | -51.81945 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| f6133eff-e043-321d-8254-764a66ab1d47 | -6.20079 | -47.52111 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f668b20f-41fe-3f98-8b50-6bb79298845b | -4.84191 | -40.52627 | 2026-09-20 04:38:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8dd6603-16b9-3253-b710-3df5730c7700 | -5.54185 | -51.32988 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2360a0fc-d56f-3f63-a2ea-4b0bbec25467 | -3.73522 | -51.81686 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 262ba797-7de7-3a0b-a5ab-6db9ece142da | -6.16764 | -47.51587 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9e6ad6b-86c3-3c62-a469-9dc1be16ad93 | -5.57565 | -45.52948 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6adc118-4d8a-30b8-80c8-6266dcffb48a | -3.3991 | -54.07551 | 2026-09-20 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdd6ce1c-f118-3b88-b9ce-a146a577bfcf | -5.82709 | -44.13067 | 2026-09-20 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cc41248-a2fb-30d9-bb11-cea8e4813908 | -5.86542 | -51.5688 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3330579e-be4c-34f3-bae1-f388edcfbb91 | -3.56461 | -43.48645 | 2026-09-20 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 458c14fa-d832-3473-9e7a-9e35ced32a1c | -2.25578 | -52.02827 | 2026-09-20 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9dd7ea64-1815-3d7a-9070-962ff5e39431 | -3.39611 | -54.06567 | 2026-09-20 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f36383a1-87c1-3c51-aa8a-b19fdf80284e | -3.45929 | -50.61213 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41742dbc-b7a9-3212-94c1-7358e6bab5cf | -3.00696 | -54.17096 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01ede449-4f64-3e9a-a68c-fe5a89e86ba5 | -6.95182 | -43.09613 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d7c883b-868d-30f3-bea8-f9a7e14b6610 | -4.07206 | -52.12125 | 2026-09-20 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 974b5ce5-c6f8-3e8e-ac7f-927de54bae08 | -4.48823 | -55.49185 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9815b14-499e-390f-bea8-2ee19dae385a | -6.29931 | -47.62939 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0b7030e-a1f6-3f33-87ff-03a606592336 | -3.50042 | -53.4386 | 2026-09-20 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 299bf86b-d3a0-3a4c-9ec0-9a790104672c | -5.31552 | -45.24603 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a94019c-79cc-38b8-8844-66cc3920772e | -4.84709 | -48.64544 | 2026-09-20 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 274adf10-79f7-3cb1-b7bc-4707a58a89f5 | -5.45906 | -44.3196 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a74ea983-f00c-3e21-adbc-b3972dd8202d | -6.92577 | -42.9041 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d89e80d9-cbe8-388e-93b3-35cda6f3f2a4 | -6.31973 | -47.62905 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0ac50c29-b37b-3824-b834-4c1011a9e8f9 | -4.51137 | -55.47363 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4faeb6b-f269-3d69-9a72-2d864c2d604d | -2.64269 | -54.69537 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 181a470d-5df5-3e53-ad65-c55299fa7db6 | -4.89158 | -45.62587 | 2026-09-20 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56cefde7-0e58-3d6b-b766-5d631e51eb1a | -5.28932 | -49.34327 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9021c60f-59ae-3afe-aea2-8558372c782a | -3.45338 | -50.60263 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3af5d1de-a269-305e-b829-32a1e6baaaa6 | -3.03516 | -48.41703 | 2026-09-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5232f86c-2c12-313a-a710-840d0e784ad9 | -3.16988 | -48.61206 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca37da8e-2c20-36c7-8e2e-31ae646e8e08 | -5.99803 | -45.25512 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e294bab-7760-3284-99de-a00748d18194 | -2.45914 | -49.21433 | 2026-09-20 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 13835f8b-0791-35c3-bb90-92f35430b3ea | -2.61307 | -54.75758 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0f6b2957-a41a-353a-b9a0-325f71e5e9d0 | -5.83016 | -44.13571 | 2026-09-20 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c5d7cd5-ba9a-3b48-a666-ef427c3288c8 | -6.14958 | -43.83655 | 2026-09-20 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fef4bdcc-3c38-3cbb-91fa-1faf247339b5 | -5.79636 | -43.76691 | 2026-09-20 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0764739a-19db-3c11-9896-4585f5c35cac | -6.19693 | -47.52406 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2eee330f-c4aa-3f52-a036-a4850379294d | -4.80895 | -45.77398 | 2026-09-20 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc46a623-e478-3250-8e69-035eb728ac2b | -3.74016 | -51.81886 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 237dab75-d7a8-333d-be56-fe98f3688e4f | -6.60692 | -43.75379 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4bd23dc-1a42-36e4-a50c-9eb822c6cd81 | -2.87699 | -51.73452 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cb2a3ea-a29b-3729-983e-8a844a970837 | -1.32278 | -54.66207 | 2026-09-20 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2adb52cd-52a2-3191-b4e1-124ff034e9e5 | -5.7324 | -52.23726 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8fcd855-8067-3abe-9c2e-9b6c1bf87d90 | -3.95576 | -49.04091 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f25f4617-b7f0-38dd-a488-95035a1a0164 | -3.68965 | -60.57112 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79deb78d-7964-39e4-961d-c5b398b7e5d9 | -3.08349 | -51.28679 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fec9dbf0-3db7-3b47-8fab-1c3209ec6197 | -6.25848 | -42.7212 | 2026-09-20 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f7314f48-ed9d-3195-a19b-b46598f1dad1 | -5.32931 | -48.98611 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe1ebc1b-572e-3d6a-abe2-bfa9d85c7ae7 | -6.29265 | -47.60703 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 343d0866-ee0b-3f89-9f96-4d4b5c2452ef | -6.97084 | -42.17665 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3455ba69-4827-3059-ad95-61f3547d4a5b | -5.23301 | -47.58481 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14e397dc-b361-3ba0-a0df-29b29dd14469 | -3.03822 | -51.37614 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc8c9a86-4a5b-3418-a4f6-f6bfcefb854e | -3.34877 | -42.77117 | 2026-09-20 04:38:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3c4751b9-0e36-3326-8acc-c6bd1ba090cc | -5.80981 | -52.09092 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fe95ff1-ea28-3915-bb6e-8a08e11bf64a | -3.39535 | -54.07022 | 2026-09-20 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad09e64-4a1f-30e6-8551-f7d508d2ba59 | -2.5815 | -59.99548 | 2026-09-20 04:38:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6462ef8b-df02-3d1c-9ed6-cbfac2cab598 | -3.09215 | -48.67731 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95db03a3-ac0a-3958-b1ea-2f3a3e1435fc | -2.17325 | -48.32482 | 2026-09-20 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69204bb2-d93b-363d-99f0-97b61f269a83 | -3.4814 | -59.59286 | 2026-09-20 04:38:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ba35d51-13e0-3888-8699-3efa1fc22e42 | -5.58945 | -45.55511 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2efd0006-6446-34b5-877b-298ff973c012 | -5.87058 | -51.56064 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcf3d2e6-83e5-38d9-a111-c09a015fd74e | -1.18661 | -55.67916 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48ba0712-8a55-384c-91a4-4b81b67ec848 | -5.63843 | -43.37489 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d133cf7-220a-3da8-bdb5-6ea6b40dd488 | -5.89162 | -46.58676 | 2026-09-20 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 022af085-3cc6-35f0-ae18-e0e03ed1fa4d | -5.3149 | -45.25 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce4dcaca-c57a-37c5-807f-3500a4d37d1c | -1.11481 | -48.0365 | 2026-09-20 04:38:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5f188c8-225f-3cc3-b343-e60de735ca9c | -3.07347 | -51.20274 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5562db5c-6376-3547-a1e4-4f4ee168f550 | -1.6374 | -55.15111 | 2026-09-20 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 395f2b99-afcb-38ad-9398-8cf3f7bce11c | -6.98888 | -42.20414 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f36930b-6862-3470-b3b0-b94175872652 | -4.1847 | -49.40908 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3be4371f-9c2a-389b-8ebd-a42fa62c1623 | -2.82669 | -46.71064 | 2026-09-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c123422d-d329-3419-84c7-e0fc97aa68e6 | -6.20697 | -45.35485 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04b6ca03-e4e9-383e-92f3-21ed1a5d78d3 | -3.4491 | -50.60618 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ea58045-900e-3cec-9d79-472cecc022c8 | -5.92372 | -42.68142 | 2026-09-20 04:38:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7db95546-7c46-3c9c-b182-00ae4022dc45 | 1.26185 | -50.74267 | 2026-09-20 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b6c6b4c-88eb-3057-800f-590c4cf41b8a | -1.25276 | -55.76902 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bad127a-eb8d-3303-862f-04ecaa6c1731 | -2.1699 | -48.32429 | 2026-09-20 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d5142da-0af9-318f-94f7-63d4175da3d3 | -4.25933 | -48.64228 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70bf6e97-1b69-3a66-8cda-4935dd24ada8 | -4.77493 | -37.74713 | 2026-09-20 04:38:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8cb4935-6d45-33a9-a7d1-13592eb03f6a | -6.15339 | -43.83714 | 2026-09-20 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d66aa76e-6cb4-3717-9f74-c10d5f68cfb8 | -3.99041 | -46.95689 | 2026-09-20 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 420a9694-4f29-3c82-8241-3a4751189d2f | -3.44357 | -58.23365 | 2026-09-20 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 957d9c65-519f-3dc4-bbd4-e6ee3ebb43fc | -5.34396 | -44.82894 | 2026-09-20 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a6f62f5-7315-3bff-874d-1d48b625436c | -5.45648 | -44.31693 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a581d560-e6c2-36aa-b408-5c59a9f15d83 | -2.72166 | -49.79051 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README55.md)
