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
| 98d58ffd-fd88-3ed0-afba-0591035944be | -8.1633 | -43.2055 | 2025-11-29 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| ff82cbe1-5c9a-3c70-a583-724f431d18d1 | -20.1813 | -52.3754 | 2025-11-29 03:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 236b514d-313e-3d35-a3d2-b0c1e23b0258 | -2.6341 | -48.0249 | 2025-11-29 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 8e718bec-c115-3c35-8129-41ad40ecfe3d | -2.6526 | -48.0244 | 2025-11-29 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 04fc4961-7b35-3314-a5b6-fb24c8d9e194 | -8.051 | -43.1237 | 2025-11-29 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| a155f6b7-5494-38ee-93d0-96ab01a94371 | -8.1822 | -43.2034 | 2025-11-29 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| c75665cb-2f8f-3759-9e05-3726deffca4f | -2.6322 | -48.542 | 2025-11-29 03:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9d8667d6-d1a3-3ed0-a5f6-dbcb6d733d6c | -8.0321 | -43.1257 | 2025-11-29 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 62db1a45-323a-3239-a019-3ed0df283301 | -2.7845 | -47.4343 | 2025-11-29 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 85368791-3310-3a3a-b0e5-b92c3c6aebb2 | -2.6341 | -48.0249 | 2025-11-29 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9ed804ef-49fa-3159-b42d-2bad3ff3508d | -2.6322 | -48.542 | 2025-11-29 03:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 08398b7f-61f1-36fc-94bc-70c8f692accf | -8.051 | -43.1237 | 2025-11-29 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 0b789485-098f-3bb6-a11a-21a108c1007d | -2.7845 | -47.4125 | 2025-11-29 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 34eef1f7-e6cd-3a10-a6b7-abca720bfd83 | -2.6526 | -48.0244 | 2025-11-29 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1c9d9a49-256a-3ff5-866e-f2501ffd6e61 | -2.7845 | -47.4125 | 2025-11-29 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 8aa02716-6f1d-3fec-8f03-24aa7a0b948f | -2.6322 | -48.542 | 2025-11-29 04:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8180523b-a26d-3754-adf3-cfadc847f71f | -8.0321 | -43.1257 | 2025-11-29 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 8b88df1c-f833-392e-9300-de35c002a963 | -2.6341 | -48.0249 | 2025-11-29 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4f8496f4-c682-3a49-bbd2-a005ce043f4b | -2.6526 | -48.0244 | 2025-11-29 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 57c39345-e4e1-3d22-aa80-e7b5b13f5352 | -2.7845 | -47.4343 | 2025-11-29 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0f236310-1fe4-398d-bb46-2e66a83b32a6 | -2.7845 | -47.4343 | 2025-11-29 04:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5410e83e-f8fb-30de-82c0-86e092d0b72f | -2.6322 | -48.542 | 2025-11-29 04:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| aa3dddcf-afb1-3077-b9d5-71d5ca2cffb7 | -2.6526 | -48.0244 | 2025-11-29 04:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a55eb1f4-0268-3c5b-a75d-2bf9fe84999b | -8.1633 | -43.2055 | 2025-11-29 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| f298dea6-1800-3f0e-bbc1-7a8338e1554b | -9.8948 | -36.1314 | 2025-11-29 04:10:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| 01486830-f42e-3240-90ea-19a2af2323ca | -8.1822 | -43.2034 | 2025-11-29 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 197c905e-7c04-3b62-ad17-eb82d21414be | -2.7845 | -47.4125 | 2025-11-29 04:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 27cfc0c6-b522-34d5-a2e8-f76916223ed0 | -2.70417 | -47.41256 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb9d8389-3210-3b63-b305-81f80ddc6d74 | -3.32478 | -44.3246 | 2025-11-29 04:12:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cee5e9c-61ce-3ec6-b56b-34e9c7e2e5c2 | -2.31245 | -46.99273 | 2025-11-29 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56875842-17ba-3d8a-85bd-d93634dc45e6 | -2.53957 | -45.38893 | 2025-11-29 04:12:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2258189b-c44a-3341-976d-76d833609998 | -1.48323 | -45.78992 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 60987216-c6b7-3fe7-b1d5-724d8eb4c1b2 | -2.91409 | -45.50428 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d27964b-d2d5-32a2-bfa6-30803122341f | -3.33322 | -42.49667 | 2025-11-29 04:12:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f3e6b4e-f770-3371-bd71-80fdb0a09ddf | -2.55321 | -44.60361 | 2025-11-29 04:12:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e2b8488-2f3a-3fc4-98bd-c5b1ad446c39 | -2.9616 | -49.18174 | 2025-11-29 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e6408cd-c720-3963-902c-b36d4f618cd1 | -2.63169 | -48.54156 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a2de4c9d-182c-3d4b-8dda-58e4b21abe98 | -2.22838 | -47.51567 | 2025-11-29 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8ffe117-d97a-36b6-8e24-3792204dbefc | -3.35574 | -45.14117 | 2025-11-29 04:12:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb9f276e-38cc-343a-9803-e339546d8e34 | -2.78808 | -43.34447 | 2025-11-29 04:12:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f929fc27-22ed-33ef-8881-fd820008bdef | -2.99883 | -41.78546 | 2025-11-29 04:12:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b195257-1eaf-3d82-a4c5-a35f34388cf9 | -2.6537 | -47.38964 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d07d5bc-6e53-39a5-a23f-3d844114f4c5 | -2.87181 | -40.58781 | 2025-11-29 04:12:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 11387c6e-a5f2-33f5-af18-9052ab653cbc | -3.89331 | -40.76182 | 2025-11-29 04:12:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7f70313d-5aec-3e7d-81da-d1e36833283d | -3.33708 | -41.86301 | 2025-11-29 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c2aa70b3-1dbd-3905-9576-87d7f7e87d28 | -3.8644 | -41.57863 | 2025-11-29 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2746bb28-55d2-385f-bfba-b57a2be58c6c | -2.64047 | -48.543 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 891c75ec-a4d5-39c0-ac3f-ab404449f811 | -2.6727 | -46.95441 | 2025-11-29 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1bfdb82-b67a-3db8-9876-dbbb4a7e0ed3 | -2.78904 | -47.42968 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 100ff0d4-b7c3-3ca6-985c-e6995c45b095 | -3.71926 | -43.45855 | 2025-11-29 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f13d0c72-a5a8-3e8b-8ab0-37d20e4fcbf0 | -2.78266 | -47.4176 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8d4c34e6-b960-3d23-9898-c9603673f529 | -3.3387 | -45.13443 | 2025-11-29 04:12:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb07b26a-25c1-35fe-8f10-a98a511e4226 | -3.006 | -45.42455 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dcb4f13-22d0-3e07-a792-1d190aefca02 | -2.86627 | -39.96284 | 2025-11-29 04:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de83693a-62ec-346a-b4a0-208ca4eb5812 | -3.7585 | -42.51833 | 2025-11-29 04:12:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95e0e638-5e04-3e8c-9053-79f3f1d43a2d | -2.99881 | -45.42342 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18909ff6-936d-32cb-ab27-53212d4f23fd | -2.30673 | -48.40178 | 2025-11-29 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c47c3c7d-45a9-3b80-a6a0-de533ea20dd9 | -3.63284 | -42.75521 | 2025-11-29 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c925c976-481a-31d1-b449-6b3d66181bdb | -1.3771 | -52.5065 | 2025-11-29 04:12:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2b25291-9f07-3189-9d91-002ca610dd1c | -1.913 | -45.67347 | 2025-11-29 04:12:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 697ca9c0-bfd4-399e-8254-fd0f2b067c8b | -2.22426 | -47.51502 | 2025-11-29 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d3a134b-67ad-3b16-b731-8f330d6fd44b | -3.62813 | -42.3496 | 2025-11-29 04:12:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d43b0226-17e7-339a-96aa-dacfb6ef5c06 | -2.42383 | -47.23217 | 2025-11-29 04:12:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 517135a7-92d6-3f37-a669-24915c5ec37a | -2.74479 | -49.3313 | 2025-11-29 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a226fd3-3981-3c9b-bf40-2f17c7543b4c | -3.1025 | -45.78311 | 2025-11-29 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbe8b53e-3629-3fae-ae12-e2e9525250d3 | -2.78672 | -47.41824 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 419f5c58-bd23-3d3e-a768-3f4d05b5fa27 | -3.33268 | -42.5001 | 2025-11-29 04:12:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 277fcf7d-281b-36fb-a495-654e3cb45a39 | -3.69547 | -43.95625 | 2025-11-29 04:12:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 537cca11-efb2-3f2a-b071-979d80613dff | -2.78498 | -47.42902 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 11a08d43-be45-3829-8c8d-3c872efb13e9 | -1.50837 | -52.57431 | 2025-11-29 04:12:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c71fa4f9-42bb-3c1d-8cae-f16a85f7568f | -2.63248 | -48.48075 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe46546a-fa9e-3a8e-bcdb-e4ff036f31ce | -3.6859 | -38.7359 | 2025-11-29 04:12:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 90920ca6-2a4f-3f76-b3c6-44eef0e19219 | -2.9778 | -45.57802 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56111d26-2171-327a-ae9e-22e5f2f4799a | -2.63335 | -48.55931 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9634d59b-6670-3721-9850-7be1e4bed87d | -2.78846 | -47.43327 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c9ee1241-c791-38b4-af41-a31f2c6307aa | -0.87222 | -48.65669 | 2025-11-29 04:12:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bccd094-4fb9-39ba-badb-ed47b5d7e33e | -2.49123 | -47.82374 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01550923-5dc7-3c7f-a25b-d62c3e3a4848 | -3.58439 | -44.5478 | 2025-11-29 04:12:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ba90b62-266e-3b54-8f36-c5887a52ac8f | -3.81819 | -43.41311 | 2025-11-29 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 579d353a-a4a5-351a-9a98-c3df82995a2e | -2.78962 | -47.42607 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 95a753f0-cee0-3178-9ba4-060c6c30a7a9 | -2.64004 | -48.03102 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 754af13a-a71f-3578-b2cf-e3654c45c23a | -2.31109 | -48.4025 | 2025-11-29 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 443cdd02-593f-3292-afb9-4c378b6edbc7 | -2.95704 | -49.18099 | 2025-11-29 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b146ce61-373d-368f-a7fa-67fc490963a4 | -1.12135 | -47.73817 | 2025-11-29 04:12:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc30bcaa-e1f9-3dc9-99e7-c477a843b257 | -3.239 | -43.22502 | 2025-11-29 04:12:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32cccbda-4c20-3028-be2d-35b84dfa62c2 | -2.47631 | -45.8516 | 2025-11-29 04:12:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c094814f-006d-3704-b0db-114eca4203ed | -3.88652 | -40.76077 | 2025-11-29 04:12:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9e6263f-c1fe-3676-999c-764244d7e30f | -3.00241 | -45.42399 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64b3310e-933d-396f-bae9-c69cf6a6cbdc | -1.4841 | -45.79287 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbd5f675-cc0d-3c08-9c10-3488c6451eb2 | -3.73018 | -43.00065 | 2025-11-29 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9afa6bf-c62e-3c5c-96b8-ab9432cd36a8 | -3.10317 | -45.77882 | 2025-11-29 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04e96614-fe34-36ac-aa3d-c865d4329ca5 | -3.8661 | -41.58962 | 2025-11-29 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a2100a6f-111d-3e23-afb7-7c81f1ee0280 | -2.24717 | -46.52441 | 2025-11-29 04:12:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 84f50f7b-09d0-3dca-bb5f-64b2f8c21725 | -2.99227 | -45.41817 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7a7b0ec-0f5d-3c42-bbf7-eeefba583621 | -3.66636 | -43.55836 | 2025-11-29 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17b138c3-3977-3170-a905-eece0e631214 | -3.87916 | -43.35099 | 2025-11-29 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cebc016-136a-3024-b342-336795887a3c | -2.25332 | -46.55996 | 2025-11-29 04:12:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61dee85-835f-3009-85ed-2b60660ae505 | -2.59641 | -46.87844 | 2025-11-29 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e9fecf2-134d-3bee-b300-1a4690c8a712 | -2.97828 | -47.92752 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73875492-de6b-3e13-ad25-aaa2eecf0562 | -2.22898 | -47.51197 | 2025-11-29 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README13.md)
