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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a142f70-3254-37c3-8f43-9632c1acf01d | -20.47222 | -45.09635 | 2025-05-18 04:21:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 077f8ce0-ea31-3bf8-8143-a381285ae1e6 | -16.41849 | -53.66766 | 2025-05-18 04:21:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 882c36f4-40db-3e56-a3d4-b7e57584bf07 | -20.17101 | -54.18117 | 2025-05-18 04:21:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 789a7ab3-349c-308e-a5af-6e6b1d2af90a | -20.99467 | -51.79071 | 2025-05-18 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ead51533-9ff1-3a17-a418-1971ac2e5543 | -17.04471 | -49.06179 | 2025-05-18 04:21:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7560bcba-8c2f-3c50-9753-1f28a4d57846 | -17.14681 | -44.81318 | 2025-05-18 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6422512b-5c92-3d10-a499-ff50fec5ed9e | -17.9179 | -45.52835 | 2025-05-18 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32b905fd-5e22-3d60-96b1-4d7f6b771f5b | -23.09623 | -45.72981 | 2025-05-18 04:21:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 457caf85-5615-3727-bc04-1cb1bdee1283 | -20.47497 | -45.09885 | 2025-05-18 04:21:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c079229c-8df6-3d00-b7ea-11bcc622f3c9 | -17.59558 | -43.1974 | 2025-05-18 04:21:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e566830e-756a-372b-b9d4-8cefaaea1bd7 | -18.94682 | -52.09091 | 2025-05-18 04:21:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65668b5a-5008-31f1-b4c9-bcc5c1cb3452 | -19.68249 | -45.3787 | 2025-05-18 04:21:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e704d1e-db57-37d5-9b2b-4dbd9c1362d8 | -22.53973 | -48.81253 | 2025-05-18 04:21:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df58d7b2-9c75-3324-81a1-45c4a5056d24 | -17.40899 | -48.11547 | 2025-05-18 04:21:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ec6a3e5-260e-37ee-968d-0831a92fc66a | -20.95489 | -56.60595 | 2025-05-18 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| acdf2dd8-e71d-3b16-88d4-9f71df7396a6 | -17.39194 | -46.64165 | 2025-05-18 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af0743d7-d5fb-368c-8d89-72ac86715981 | -17.13987 | -44.81208 | 2025-05-18 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 707e0cb5-0b27-3e2b-84e4-11a53487de2a | -17.39138 | -46.64528 | 2025-05-18 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d81e53cc-0c8b-3023-8d12-4477eb64ab6e | -20.9526 | -56.60131 | 2025-05-18 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a23587f8-9bc2-339a-a0df-c1147e730d47 | -17.7515 | -56.30882 | 2025-05-18 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d2731af1-e833-3d32-8c65-54442924a299 | -20.93043 | -44.40764 | 2025-05-18 04:21:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c1a68d36-5564-31fa-8afe-cabb78471e81 | -19.06578 | -53.46131 | 2025-05-18 04:21:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34830d70-dcd4-3fc9-a3d7-f9bc07f6636d | -17.38805 | -46.64472 | 2025-05-18 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 556790af-cfc7-3ea2-b2c9-68186d4b9846 | -20.95 | -56.60485 | 2025-05-18 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fa661f01-9e3c-3fcf-bcba-b98e70f9af5e | -20.94882 | -56.61056 | 2025-05-18 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3a9b194b-8b8b-3ac7-9458-0f595c7d87ef | -23.94477 | -51.94522 | 2025-05-18 04:23:00 | NOAA-20 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2bae74b1-1860-3e65-b541-d7bec622c0de | -23.98397 | -48.91645 | 2025-05-18 04:23:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 362da5d7-785d-3501-8397-2290b9cac06a | -29.34052 | -50.49823 | 2025-05-18 04:23:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9d01afa6-b5a8-3764-aa81-f587873200e0 | -28.74763 | -49.46864 | 2025-05-18 04:23:00 | NOAA-20 | FORQUILHINHA | SANTA CATARINA | Brasil | 4205456 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e26e61b6-24ce-325e-946d-fccc6b886304 | -23.94712 | -51.94369 | 2025-05-18 04:23:00 | NOAA-20 | SÃO JOÃO DO IVAÍ | PARANÁ | Brasil | 4125001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2457ae3e-227d-3a1e-9691-26635cc1e699 | -25.192 | -49.32849 | 2025-05-18 04:23:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42e81437-84fd-306f-8bfb-9fab88170883 | -29.95085 | -51.61597 | 2025-05-18 04:25:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 2b6c2fdf-8d48-3bd7-a8d2-b30e04f86d97 | -30.14867 | -52.02671 | 2025-05-18 04:25:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| aa22c97e-fc4f-3001-a74d-f02360905a0e | -30.22493 | -54.93959 | 2025-05-18 04:25:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 66244590-5cc2-33ea-88b5-2b3bf44287f2 | -30.14956 | -52.02585 | 2025-05-18 04:25:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d1ae32b4-0ca3-393f-8ca2-c60bcc432ee1 | -31.7564 | -52.66831 | 2025-05-18 04:25:00 | NOAA-20 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 51f99c62-40e5-3079-a3e7-a6a98ac74ede | -29.89111 | -51.23568 | 2025-05-18 04:25:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 9d9a3a38-24ef-3708-8360-81fee22537e3 | -30.66722 | -52.80083 | 2025-05-18 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 3943760c-c864-314b-8569-cd6deddac755 | -30.00743 | -51.12651 | 2025-05-18 04:25:00 | NOAA-20 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| aeeccfaf-9c14-3c28-8cc3-79c141caee5b | -6.49892 | -47.49472 | 2025-05-18 05:10:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16eca519-44c4-36a3-8d95-d055952a17c8 | -7.95385 | -49.75585 | 2025-05-18 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 71caa53a-3fb6-3d57-b542-76f80644c85f | -7.08212 | -44.91973 | 2025-05-18 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9705236a-3eb9-3fdf-82f7-afbd1953eb0a | -8.31286 | -49.42233 | 2025-05-18 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b356f99-bb0b-334d-bec2-48d63ff771ed | -9.57094 | -47.58081 | 2025-05-18 05:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d3e694-7188-3712-9964-1505ef76f912 | -9.57146 | -47.57668 | 2025-05-18 05:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6268790-62e5-3e2e-9adb-327cd290c8ef | -8.3119 | -49.42206 | 2025-05-18 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32605973-777c-36c4-bfe0-76ee2d0d9419 | -7.07734 | -44.38509 | 2025-05-18 05:10:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5c04c41-0a37-3d71-80fa-d94d220fc0c2 | -7.95124 | -49.75547 | 2025-05-18 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 414bae7e-e51e-3200-8428-daa9988ca185 | -9.32127 | -44.83686 | 2025-05-18 05:10:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdfdcccc-d7e2-344f-a1fb-556e877b18df | -7.07546 | -44.91888 | 2025-05-18 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13c3e339-9ecc-3644-a65d-70984c0d1c10 | -10.48105 | -46.51479 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2d2f8f5c-f89a-37b9-9908-077aed4a7de9 | -10.47821 | -46.50739 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 394fbecd-6dad-3d3c-934f-c315a78d8dfd | -9.24541 | -63.29046 | 2025-05-18 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a564184-01b6-3bd4-b7e7-a05facf38d4e | -10.3056 | -58.44947 | 2025-05-18 05:12:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa8e61e7-e938-3717-b2f6-255aad859cad | -11.42568 | -54.2982 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| daedaede-d2ae-3d46-8ad5-5fd23cccc98d | -12.04201 | -54.96887 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b1df828-603b-3635-87cc-7457ff819369 | -12.45342 | -57.19508 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b66d667f-8c07-3e56-aa5a-a8b99f6d7ffd | -13.1447 | -56.81212 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dfb0def4-062f-3dff-b03a-28a8932547c8 | -14.02158 | -55.14106 | 2025-05-18 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 774d8e9b-730f-39ad-8809-c1a315135c23 | -13.14813 | -56.81265 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e24a9d7c-b594-3f6a-bc5f-5fb6d6758aeb | -10.47793 | -49.14692 | 2025-05-18 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c233fe6-22dd-3aea-ae10-f41b2045cf95 | -11.40075 | -52.95391 | 2025-05-18 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1b2b93f-3806-3440-92a8-9efbf3b74eda | -12.12395 | -54.6647 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 390b280d-0998-3574-8c96-3f64e1aede61 | -12.36483 | -56.40144 | 2025-05-18 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d706be49-853c-3825-a649-e21d7e95c1e7 | -12.15518 | -57.23938 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08ccc28f-cac7-3eae-a0c3-5d366bb7655e | -12.12548 | -54.65747 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd343361-9527-3800-a16c-e961879fc44c | -11.57627 | -47.60762 | 2025-05-18 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cfcca513-1b51-335c-b06d-154a814f3bcf | -10.37144 | -57.50079 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7faab3d6-eb51-3f77-a79f-ead14a605c0b | -10.47695 | -46.51775 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a23eb03-a079-3a41-9030-08e45a053723 | -10.05366 | -64.99595 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 331c1377-b888-33d3-b08e-31a67d08ef51 | -10.05449 | -64.99136 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 425aca45-6f05-3835-aeab-d6e885eeb08f | -10.49012 | -46.51468 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ce7d59d8-a0b6-3092-9a26-5bf9e4675417 | -13.04111 | -53.72215 | 2025-05-18 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b4404b9-cc60-37ae-adbf-59787bc41aa8 | -10.48321 | -46.51891 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d98a9155-80cb-31df-ad14-b12b4e008080 | -12.03461 | -54.96777 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98b9a469-51f6-37eb-b0fc-5a583bcfcde6 | -12.12419 | -54.66682 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8623f244-d87b-38de-a637-8dbe6b3f6ffd | -14.01911 | -55.1311 | 2025-05-18 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0a8e8f6-7ebf-3c8a-bcee-275ef4ad29bd | -11.41924 | -54.31665 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a2a87bc-b71a-3421-b5b6-7a13f4e95a4f | -14.02662 | -55.13226 | 2025-05-18 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a02a8e4-4bde-3801-aad9-b6cc5c60212b | -12.12462 | -54.66004 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38e608a2-e469-3a74-871a-36e6da607041 | -10.75594 | -57.23378 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30564a93-8481-3e63-b741-32b4075871f8 | -10.47221 | -49.14935 | 2025-05-18 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12b5500a-7ab0-3fe0-9eca-a5ae1c4bbc60 | -10.4867 | -46.52124 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 542482fb-0f9f-3e94-97b7-71ce4f87821a | -10.48384 | -46.5137 | 2025-05-18 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 944d4b42-494a-31e3-91c1-01ac92aae1b7 | -10.37198 | -57.49726 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c2cb8f5-d181-3ed4-ba89-96cd9796f1f7 | -12.40949 | -55.00584 | 2025-05-18 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2cf7afdb-b905-303a-866a-c71eeb706abc | -12.4506 | -57.19086 | 2025-05-18 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39bf208f-45b9-3dd3-8007-cb9d5a906657 | -13.38839 | -56.65481 | 2025-05-18 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ed4e019-eac8-3606-8d35-36cb2780b480 | -11.58122 | -47.61695 | 2025-05-18 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8bb6f8c6-c9f1-3628-8af1-2a673f2e237d | -10.68304 | -57.59686 | 2025-05-18 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9839b3c7-5492-31e4-9c40-41272c681629 | -11.42015 | -54.31438 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8c5fa8b-c19e-37c4-a9bb-1edc7aff449b | -11.29338 | -53.97669 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7765a7ca-d689-3a8e-bfb3-669fca17ea70 | -12.03398 | -54.97219 | 2025-05-18 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ade21221-e6f3-3e93-bee3-2385a9ae1f5a | -10.48226 | -49.14477 | 2025-05-18 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51e63217-d949-3844-b093-15e6419b5929 | -14.01847 | -55.13579 | 2025-05-18 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba04e06f-bdb2-34c1-92f8-ae5a66a04a09 | -9.24008 | -63.29704 | 2025-05-18 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab864d20-6053-3cb6-8dcf-c3097f40365c | -9.24135 | -63.28976 | 2025-05-18 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd66b97f-45bb-3f65-9267-36aebd90fe91 | -13.85073 | -59.72634 | 2025-05-18 05:12:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5c3ab67-3fa5-3974-b0a8-b7b2b2ade13b | -11.41945 | -54.31916 | 2025-05-18 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b605263-c1f5-3274-a1f9-2f1cd2edf01c | -10.47836 | -49.14362 | 2025-05-18 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README7.md)
