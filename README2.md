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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c13d21c-1616-3e30-b435-4211fc2564ec | -18.9669 | -42.0909 | 2025-09-19 00:30:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.6 |
| 1aa75ec1-b28b-32d9-94b1-058716231fd0 | -14.2472 | -51.3505 | 2025-09-19 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 1e869f1b-48ad-390e-816f-d1aa269706b0 | -6.2732 | -43.9225 | 2025-09-19 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2e220cee-af65-335b-9bee-e61f6f82036a | -5.3374 | -46.1464 | 2025-09-19 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8e6dc947-e75f-38d5-976a-b58fd65e748c | -8.1381 | -46.771 | 2025-09-19 00:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 2c890012-9e22-3600-bb5c-5d34f83f81bb | -14.2859 | -51.3453 | 2025-09-19 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 7ecfc735-9686-3254-b55f-784b6a4b1687 | -5.356 | -46.1452 | 2025-09-19 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| bb5fcd75-9e35-3b59-8346-361ec2ab5395 | -6.2544 | -43.9241 | 2025-09-19 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 254129a6-ef8f-33cd-b27f-bb51a325d427 | -14.2666 | -51.3479 | 2025-09-19 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 918d5bbe-7a03-374c-9806-776806623d75 | -9.1933 | -45.3114 | 2025-09-19 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 255.5 |
| a530b9ff-21b2-3357-90e5-c7b3f8ae4b42 | -22.3449 | -46.7648 | 2025-09-19 00:30:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8c8c4c9f-e771-3976-b48e-bf64c5ea657e | -18.9677 | -42.0655 | 2025-09-19 00:30:00 | GOES-19 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 7416b03f-8ef9-374e-9397-50a86e686686 | -9.1744 | -45.3135 | 2025-09-19 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 258.9 |
| e6f0e452-6fc3-333d-9dec-961d770c7946 | -9.1933 | -45.3114 | 2025-09-19 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 231.4 |
| e03654f5-5c0d-348c-9dcc-cb8973bb01ae | -6.2547 | -43.9009 | 2025-09-19 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 46bcbc88-7399-3ffc-874f-b6168ba72515 | -5.3374 | -46.1464 | 2025-09-19 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 78717d49-90e1-3de1-9704-b7594ae6fefa | -9.1744 | -45.3135 | 2025-09-19 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 4dfcaeb0-5a32-3b54-a455-4156a0e28bcc | -7.5708 | -45.4559 | 2025-09-19 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 340.7 |
| 41eeedf4-4529-3414-91e8-e2e39d060496 | -14.2472 | -51.3505 | 2025-09-19 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7358a158-011c-31d6-877b-1ac0a41fdd16 | -6.2732 | -43.9225 | 2025-09-19 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8a307fc0-cc6a-3c95-aa41-ac3447b9ada6 | -14.2666 | -51.3479 | 2025-09-19 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 5028e82a-690c-3131-a639-5da80c503212 | -20.8052 | -47.2273 | 2025-09-19 00:40:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 7c9eca3c-06fa-3d85-80be-a45032feb830 | -20.555 | -44.0203 | 2025-09-19 00:40:00 | GOES-19 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| 96adb90b-f240-32b8-beb0-18d9f39fb5c5 | -7.5896 | -45.4542 | 2025-09-19 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| c6cac1a6-1ae6-3556-948e-f51395a80150 | -7.5705 | -45.4786 | 2025-09-19 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 340.8 |
| ea5dc796-cbd1-3e82-983a-1c0ac96cec8f | -9.193 | -45.3342 | 2025-09-19 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| cb45c87c-bd29-3027-a2eb-3c8e6e6adb96 | -14.2662 | -51.3694 | 2025-09-19 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a32144b0-71ad-3b41-9d9d-2d4ccf579407 | -9.1747 | -45.2907 | 2025-09-19 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b8be182f-1b7d-3cde-83bd-12b42b691c9f | -6.2544 | -43.9241 | 2025-09-19 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0299cb9d-df68-39bb-9645-3db7ca6b1baa | -6.2734 | -43.8994 | 2025-09-19 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 678a0cc7-2539-3838-9cfe-d9ad9dcf6376 | -5.7241 | -49.0917 | 2025-09-19 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 33321901-afb9-3a8a-8508-3a7ff0a54adc | -13.7734 | -52.0517 | 2025-09-19 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3394c79c-42a5-3a0f-8ec6-a193bba94294 | -5.3043 | -43.3234 | 2025-09-19 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| efdd1325-4b36-3719-9db2-e3afc19b59fd | -8.1381 | -46.771 | 2025-09-19 00:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 4f0b78d1-c01a-3409-8757-3ec7466d85ba | -13.7737 | -52.0304 | 2025-09-19 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f934b2ca-0190-34cf-bec5-2ce59ba19bb5 | -9.1741 | -45.3364 | 2025-09-19 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ff9183cb-fe53-3d18-b949-459490676979 | -2.9435 | -49.3443 | 2025-09-19 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 9abdcf2c-e53f-39f9-a6f0-4fe7fbc8b5ea | -5.7055 | -49.0928 | 2025-09-19 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 4fa1e6ff-2bec-37f4-afd7-c924a4fd69e2 | -7.5893 | -45.4768 | 2025-09-19 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 65f7ba5a-e273-39ae-be41-29721ca198da | -13.7541 | -52.0541 | 2025-09-19 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d057ddb9-5d91-3a53-947a-785caf5beb29 | -9.1937 | -45.2886 | 2025-09-19 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 26b369d1-fbd5-3246-a15a-9f08809481f3 | -20.8052 | -47.2273 | 2025-09-19 00:50:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 3ccfd439-1d1b-3d75-b069-a03807fac7a4 | -9.1647 | -44.6504 | 2025-09-19 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c8088efc-8245-3add-9656-d765ab0f0958 | -7.5705 | -45.4786 | 2025-09-19 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 3ff0e8ea-7676-35e8-97ff-52cc92940de4 | -9.1933 | -45.3114 | 2025-09-19 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 8211b965-0289-3c9f-b7af-e34d5440754b | -8.1381 | -46.771 | 2025-09-19 00:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 73df6cc4-c8b5-3c93-b5be-fa55e215ea9e | -9.1747 | -45.2907 | 2025-09-19 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a36eef6e-bffb-3080-b060-dd9b75fcf9c9 | -20.7846 | -47.2323 | 2025-09-19 00:50:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 27b7ac3e-027f-3e69-a6ed-400fe66d0711 | -7.5703 | -45.5012 | 2025-09-19 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 0737f8c8-468a-375a-ac58-c7c87523753e | -5.7055 | -49.0928 | 2025-09-19 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9d48d437-822c-3fc1-a2e8-1bfaba09dea2 | -7.5896 | -45.4542 | 2025-09-19 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7448de95-a302-3150-b62f-4e04d52b2fd2 | -9.1644 | -44.6735 | 2025-09-19 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9ec23d87-ff35-34be-92bf-b8c6691e2095 | -9.1741 | -45.3364 | 2025-09-19 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 3d6602bb-0267-3b7f-a452-251b80fd04ab | -9.1937 | -45.2886 | 2025-09-19 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| db1c012a-1d19-3dc4-b52d-e92ceb71ac48 | -14.2666 | -51.3479 | 2025-09-19 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 814e46bf-e16f-3e75-a4ed-91fde38ba637 | -18.4144 | -50.6714 | 2025-09-19 00:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b5bb9368-8c6b-34ff-90af-775bcf0561b5 | -9.1744 | -45.3135 | 2025-09-19 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 0fd5bf82-0bac-32cc-912d-378478b6c5be | -14.2472 | -51.3505 | 2025-09-19 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c5dc8c5f-743c-3e27-84dd-c800eca5ba8b | -5.356 | -46.1452 | 2025-09-19 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 10116243-4048-3bc6-9909-14bbf3fe7cd5 | -14.2662 | -51.3694 | 2025-09-19 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 6323e877-5333-3020-be04-ace4050e43b8 | -5.3374 | -46.1464 | 2025-09-19 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6b3aeab5-f15d-37a8-a0a3-2060b330b518 | -7.5708 | -45.4559 | 2025-09-19 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 6901cee7-1cd7-3cf2-9407-e92c5a8227f2 | -7.5893 | -45.4768 | 2025-09-19 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| b07fd518-a03a-3470-aa28-931d4ac1c1fb | -20.8052 | -47.2273 | 2025-09-19 01:00:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 88e81cf1-b482-39cf-8c59-30a286f890fa | -6.2734 | -43.8994 | 2025-09-19 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 54dbe3ba-d4e4-3e10-8391-95091a152481 | -9.1933 | -45.3114 | 2025-09-19 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 55627cff-d4a6-3061-b49c-57660c2e6256 | -7.5705 | -45.4786 | 2025-09-19 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| bf1d7be7-e4d6-3d08-8a54-ec88c942e033 | -6.2057 | -45.096 | 2025-09-19 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d19e36f4-a195-3a75-8986-0e4343e04492 | -6.2055 | -45.1187 | 2025-09-19 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 68083d1d-e694-3a0d-9248-d5c4f957b11a | -9.1937 | -45.2886 | 2025-09-19 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| ef3e6eda-42de-3508-a876-25b36359b97e | -9.1741 | -45.3364 | 2025-09-19 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| f98a9d0b-cfc2-3777-8577-244449b5d53f | -9.1747 | -45.2907 | 2025-09-19 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 4cacb2b8-a406-3aa0-8f2e-81dc0ae3643d | -9.1744 | -45.3135 | 2025-09-19 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 28064d30-79db-344b-8357-0cf2f23ba585 | -5.3374 | -46.1464 | 2025-09-19 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ac008b80-5cf5-32b8-aa3b-7f62e9b7c8fd | -6.2732 | -43.9225 | 2025-09-19 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ec08c817-cb1d-3080-b72d-cee5b7d47ff4 | -14.2666 | -51.3479 | 2025-09-19 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| be8eba2c-96df-3fc7-83fb-85aded558f9e | -8.1381 | -46.771 | 2025-09-19 01:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| fdf03322-17ca-33cd-aec6-cc40a364a9e1 | -6.2544 | -43.9241 | 2025-09-19 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f8b0e3ab-bc1d-3393-94dc-31dcd4e02293 | -6.2547 | -43.9009 | 2025-09-19 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| cb99b026-47a7-3248-ad07-cb7be3561c7f | -9.1933 | -45.3114 | 2025-09-19 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1dd943fd-8325-3680-95bb-ffd0bdf20250 | -9.1432 | -44.8368 | 2025-09-19 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fa6a61c9-632b-31a2-849f-1fa66c2b5342 | -14.2666 | -51.3479 | 2025-09-19 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f80e090b-7ab0-37c4-969c-1108b31ba84d | -7.5708 | -45.4559 | 2025-09-19 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 9bbbc325-2b9b-384e-a423-90807482cda2 | -6.2732 | -43.9225 | 2025-09-19 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| baf394e1-f18e-314b-8749-2d41c6fb6715 | -6.2734 | -43.8994 | 2025-09-19 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| ca484b19-36c5-34f5-8d22-aff47e1c24b5 | -9.1747 | -45.2907 | 2025-09-19 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| fd9fec20-8413-39c4-a60d-984eb3f895e5 | -6.2544 | -43.9241 | 2025-09-19 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3b3adb0b-0a5b-33da-843e-5c42ce502c91 | -7.5705 | -45.4786 | 2025-09-19 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 63a6270b-2aeb-3916-83ff-37ead491f74a | -8.1381 | -46.771 | 2025-09-19 01:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ac281c25-b205-3def-9972-8a8e1813e30a | -9.1744 | -45.3135 | 2025-09-19 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 0b070800-219c-3218-b4c1-0335261d13d0 | -20.8052 | -47.2273 | 2025-09-19 01:10:00 | GOES-19 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 40653b36-f0e2-3c42-ae46-269711ab7861 | -10.6594 | -48.7092 | 2025-09-19 01:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7a69ae89-dae6-37f2-b76c-4a94da37aee6 | -9.1429 | -44.8598 | 2025-09-19 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 1b0c16fd-c2e4-3c68-96f9-0658976fc6b7 | -9.1618 | -44.8576 | 2025-09-19 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 7a97614a-0da2-3c54-8521-850944c26ab1 | -9.1937 | -45.2886 | 2025-09-19 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| c8590206-3f4a-3d84-a594-6716d55bf95e | -14.2666 | -51.3479 | 2025-09-19 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8a552f09-f331-3496-94f6-7ad9e42ebc83 | -17.2163 | -45.9518 | 2025-09-19 01:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 310.9 |
| 577a8fed-da9f-3d30-b322-b55c028f6cc6 | -10.9155 | -45.6232 | 2025-09-19 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 79c7f2d0-aba0-3148-9bc5-871c487ad758 | -9.1937 | -45.2886 | 2025-09-19 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 26ebae6f-8e1b-369b-bf2f-658f75f8c071 | -5.5113 | -43.2151 | 2025-09-19 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |


[Clique aqui para ver as próximas entradas](README3.md)
