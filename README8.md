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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94359334-0e75-3636-841e-c7424b529b3c | -3.47576 | -39.56754 | 2025-07-23 04:32:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9dace8c8-30ae-3810-a711-d75b2b28a85b | -6.93272 | -44.30723 | 2025-07-23 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e46303f9-9b1f-38ef-ba06-2f821b1f1ef5 | -3.83053 | -47.74011 | 2025-07-23 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ab994f-d5f4-3eee-adba-7e32c86a7992 | -3.82834 | -43.0202 | 2025-07-23 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52e1ad3d-551b-3cba-b3ea-8e1e53afe960 | -3.18132 | -49.4552 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0c61f0b6-efb7-3849-993c-d83e33d52cd7 | -4.20855 | -40.7476 | 2025-07-23 04:32:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6c09c542-1914-31cb-8bca-c2c7356926fe | -3.20212 | -49.16883 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c770419a-a244-3020-8149-e4b452829bb3 | -3.97886 | -47.88032 | 2025-07-23 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69243869-38d5-3a1e-8590-834d83f00890 | -5.36574 | -36.89395 | 2025-07-23 04:32:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e1fe04ac-eedb-366b-8aa0-6df8f2df18ec | -4.77571 | -45.34008 | 2025-07-23 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6481c524-cbe8-3b4b-a784-dc554a86d2fb | -4.30122 | -48.10096 | 2025-07-23 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9345bc89-27ec-3e65-95ce-238efb176ef3 | -6.06171 | -47.54477 | 2025-07-23 04:32:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67936ada-4091-338c-9dac-2133b475417e | -5.6766 | -43.66113 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 801c4fc5-a4f9-3802-988a-92ee66c24cff | -6.60675 | -42.40693 | 2025-07-23 04:32:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 30fb7616-969c-38bc-97fe-085f1cedd84e | -3.29856 | -43.45533 | 2025-07-23 04:32:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b60dc766-f472-35fb-a119-56e2aa93c1a8 | -5.67905 | -43.6712 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4559b931-f7af-382f-835a-f2a48dbffa98 | -3.40789 | -49.53278 | 2025-07-23 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ef96225-18ba-3a49-813b-6220454e1166 | -6.61162 | -42.34438 | 2025-07-23 04:32:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b631c6c5-3bd9-3b8f-bb73-c924bf943354 | -6.42443 | -47.22414 | 2025-07-23 04:32:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 696f57c6-1520-31de-8433-385d79f0aa08 | -4.25964 | -39.23156 | 2025-07-23 04:32:00 | NOAA-21 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 27be6d8b-3a73-3ec2-ab09-7f09e0f3b246 | -3.17503 | -49.45034 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a2046079-c50a-3404-9ea0-c553f39c8856 | -3.94542 | -41.48582 | 2025-07-23 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e4f61a4-4cc0-3199-b0d4-dd61f539daa4 | -3.14455 | -53.13845 | 2025-07-23 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e19a011a-4b0e-343c-b821-eb48f2c80aaf | -6.92656 | -44.29707 | 2025-07-23 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a792adae-10eb-3d8a-9aae-c8b87a1a4ceb | -6.60731 | -42.4031 | 2025-07-23 04:32:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6ce56427-973b-325f-9643-9f43c395bafe | -5.67947 | -43.6745 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fead6a35-647b-3da2-b4d0-77a721250c93 | -6.18754 | -44.39148 | 2025-07-23 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40c11f3d-eaf0-3e04-a3cf-1f58dcb64f6f | -5.11315 | -43.78088 | 2025-07-23 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f3d5559-e766-313e-8470-e75b67cf6921 | -3.17443 | -49.45411 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3714b587-7495-339f-a671-e820d4dc1aaa | -3.48482 | -51.18745 | 2025-07-23 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 056ef436-152b-35a4-a1fa-b373b6655701 | -5.28173 | -44.94856 | 2025-07-23 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbfaf5f5-3938-3957-95ee-50615e4c64b0 | -5.11246 | -43.7854 | 2025-07-23 04:32:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fba979da-4db9-3e4c-a540-c2da93da4b1d | -5.35975 | -36.89308 | 2025-07-23 04:32:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6813f44e-37d5-3ff3-bf19-681c74d41f2a | -6.92589 | -44.30164 | 2025-07-23 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8a82b5d-7789-36b5-a259-be7c2162623b | -5.67327 | -43.66386 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5aededf5-3712-3a32-b98c-85d8a7da5ade | -5.28114 | -44.95255 | 2025-07-23 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 073e99fc-da6f-3c40-9c32-4b457912bf55 | -3.41134 | -49.53331 | 2025-07-23 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50a8a0fa-f220-30fe-ad95-0248c16b4832 | -3.04253 | -47.38386 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a66aaa8-6715-3f36-b8df-e66ec39398ba | -5.67399 | -43.6591 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf362389-76a5-362f-a9e8-a08bef93fa8b | -6.35591 | -42.61253 | 2025-07-23 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c71e805-c1a3-3dc0-b975-d3a11d393cf6 | -3.18192 | -49.45142 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 86aa31f5-39d1-324f-8376-447392d038c5 | -3.47885 | -39.56852 | 2025-07-23 04:32:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6e1f0df9-700b-3433-8e14-41d2fa2673ba | -5.36185 | -36.89837 | 2025-07-23 04:32:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cce7d9de-24bb-3875-b827-c035e557f234 | -2.90442 | -48.99109 | 2025-07-23 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f9df3b8-0e25-34c6-a905-3182d9208c30 | -4.50163 | -42.94209 | 2025-07-23 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa20e9b8-4177-3b3d-a308-2c9281937b22 | -5.73328 | -43.95866 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 732cd634-3dd7-3e63-b932-96de7a7e28f9 | -6.93116 | -43.95142 | 2025-07-23 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5135bd6c-55cc-302a-8199-6e754c200c78 | -4.04702 | -42.51828 | 2025-07-23 04:32:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 4fb69438-46a1-344a-ae5b-2f3093ab0e3e | -4.05103 | -42.51891 | 2025-07-23 04:32:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| d8a7cd70-3409-3594-9128-857a224f4c20 | -7.12374 | -43.40691 | 2025-07-23 04:32:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0c0237c-30a0-3445-81b9-b7ebe279e6e3 | -6.686 | -43.00118 | 2025-07-23 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f42efd9-3292-30fa-bdaa-ae5f8ed5dfb6 | -6.94396 | -43.96471 | 2025-07-23 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc8e47b4-dddc-3e6e-96bf-cf23845a29bf | -0.75899 | -50.27025 | 2025-07-23 04:32:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3808709e-07ac-3793-bb85-29779654641a | -3.12794 | -47.0139 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68e8a12f-2f38-3d2d-8cde-5dffc165e9e5 | -2.27538 | -48.56755 | 2025-07-23 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f73c146-33bd-39bf-b994-29e305717e24 | -4.84409 | -45.30244 | 2025-07-23 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87b9ea9a-1cc1-31e4-836a-fa5cec7f3c59 | -2.9184 | -48.23998 | 2025-07-23 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e59bba1-4835-35fc-adc1-ce74dcfa2acc | -6.61207 | -42.3999 | 2025-07-23 04:32:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 05976d85-bcf7-33a4-907a-f74094f26cba | -5.43056 | -47.53754 | 2025-07-23 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04933405-d278-3f7d-aac1-65c6f8c056b3 | -3.11856 | -47.00893 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77ed5270-634c-3cde-8b62-b06a0b5fbb6b | -5.7294 | -44.50176 | 2025-07-23 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 511d924f-fa58-3142-b54d-366001df78c7 | -4.67707 | -48.15669 | 2025-07-23 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5c857ac-d2c5-3c7d-88c5-31a26181b150 | -3.27208 | -53.02161 | 2025-07-23 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1c466d3-867b-375f-b30e-250c0a5a323c | -4.58612 | -43.31785 | 2025-07-23 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f16cd04a-ef37-3f29-8a9b-f0dfa56e5dee | -6.04604 | -43.02239 | 2025-07-23 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97658259-b713-3fbc-aa5f-71d05a5cdd3d | -6.18557 | -44.40467 | 2025-07-23 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 436ef90f-edd8-33eb-ae88-ff374864c646 | -6.61151 | -42.40372 | 2025-07-23 04:32:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 57363723-e8ea-38af-8367-7476260b481a | -3.75165 | -49.04491 | 2025-07-23 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4ba56c5-aa71-3f3b-b7ba-120211ccf4b0 | -3.0324 | -47.86208 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8349911-8a6e-34b3-846d-2c225f6fee82 | -3.17848 | -49.45088 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 88a955fc-a2f0-3b0b-b42b-e08f3afadb85 | -3.82447 | -43.0196 | 2025-07-23 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0321e46-9f1f-39c9-af8f-798c8f600629 | -6.96441 | -44.37664 | 2025-07-23 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed6b8355-9db5-3f29-a143-e3d52b31ac3e | -6.2715 | -45.27405 | 2025-07-23 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0583c67-afff-336d-ab2a-fcfe5554db88 | -6.87 | -43.11144 | 2025-07-23 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa1fc7ca-903c-30d7-944f-e5caec321202 | -5.68019 | -43.66979 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80ff4eab-0dc1-3a94-a5d8-ad4fc334b783 | -4.86376 | -45.31337 | 2025-07-23 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3891ccb-030c-32ba-b7f9-d3c9abd68e44 | -3.03957 | -47.85964 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7c84289a-acda-3a68-9b59-f8784b871824 | -4.7763 | -45.33628 | 2025-07-23 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8da851aa-b45c-3733-b448-03c447663d15 | -5.87964 | -50.14732 | 2025-07-23 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21679973-5883-3e7f-81ee-08c76ba585aa | -6.9786 | -42.79211 | 2025-07-23 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e309cf8c-b124-3f7d-b457-2f759a993609 | -4.09051 | -46.92453 | 2025-07-23 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2da0a043-6576-3243-9c99-b3f8344f2446 | -2.45956 | -48.1533 | 2025-07-23 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da44547b-45fd-363f-93a5-837cd748e030 | -6.36058 | -42.60949 | 2025-07-23 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 752e8026-52bf-3c29-9b37-6cd92c7b9754 | -5.68599 | -43.67717 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06fec1eb-b401-3236-9e49-7a6a35985c42 | -4.91485 | -45.31714 | 2025-07-23 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1393ec51-c109-3f6e-82de-8c35f479a98d | -6.36003 | -42.6132 | 2025-07-23 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 95bb3526-dbc4-343e-8808-0f64c3f861ef | -5.68168 | -42.2023 | 2025-07-23 04:32:00 | NOAA-21 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| df68c4df-33b7-3ffa-928f-f50c8c6f9171 | -5.88104 | -42.40945 | 2025-07-23 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c9b25b2-d172-3436-b00c-8f0b20a7e32e | -3.17098 | -49.45357 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 42033f03-40f3-3ebe-9481-ded2a9211a4a | -6.92963 | -44.3022 | 2025-07-23 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f4c06e5-9ef6-3ca8-a2f6-4c4495b77fc2 | -2.99582 | -49.31964 | 2025-07-23 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b4aa657-b0a1-3c8b-998f-f21f1525dfc8 | -6.27503 | -45.27457 | 2025-07-23 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6033afd5-b325-3683-afbd-09f2135fa4c9 | -6.8705 | -43.10791 | 2025-07-23 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5f678fb-2920-3f6e-8c7b-bc643637a766 | -3.03571 | -47.86259 | 2025-07-23 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9ccd0556-fce5-39eb-907c-0bf3eb0bd96f | -6.84922 | -42.73484 | 2025-07-23 04:32:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cbf0676a-a435-3ec7-ae6c-dab94c9913d4 | -4.77806 | -45.3394 | 2025-07-23 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e67fe0d1-2301-33a2-9cc9-7dff5d63c1f0 | -3.94971 | -41.48648 | 2025-07-23 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a28c4b5-2e55-3a90-bcf4-ef4ab96ca10c | -6.94572 | -43.95844 | 2025-07-23 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d542f90-4a56-3936-a089-ee7c16eba04b | -4.04133 | -48.06695 | 2025-07-23 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1c444a1-888d-31cc-8686-69f854c07772 | -5.66945 | -43.66326 | 2025-07-23 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)
