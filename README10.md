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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1258720-e925-3780-9d6b-908025b6a62a | -3.95622 | -41.52254 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f8af773d-cd40-3374-9fa9-29486ca2f31f | -4.73518 | -43.07096 | 2025-12-12 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d404c3f-2f09-3df9-93df-116c7d4d3e1b | -6.12416 | -41.27861 | 2025-12-12 03:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd17db8d-9d21-3be9-8dfe-b615e37ae350 | -9.39872 | -36.01948 | 2025-12-12 03:29:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 23b71e30-eddd-3786-9877-9dabd28e1f7e | -7.31388 | -35.06104 | 2025-12-12 03:29:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ba7019a-0af0-3d1b-a32d-ae396e2d4a4d | -6.12295 | -41.28555 | 2025-12-12 03:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e163e224-3c77-3689-87d0-96d00a863f02 | -3.95945 | -41.52217 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d75c36d3-fba8-3789-b23a-d71f3aeead7f | -5.15918 | -37.70233 | 2025-12-12 03:29:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5025cedb-53cb-3cbc-80f5-0cd6f4162e08 | -9.40907 | -35.80176 | 2025-12-12 03:29:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 55e0f935-79b6-3011-84c1-237409c43285 | -3.95876 | -41.52612 | 2025-12-12 03:29:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 08945f0d-b566-3319-9697-78f28d5e76ad | -7.0673 | -35.21852 | 2025-12-12 03:29:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7c605b96-84ed-33d7-9f6f-2bc6086af0cf | -8.03207 | -43.10176 | 2025-12-12 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 8f1b742a-fe56-3d1c-87f0-c77a87081d38 | -4.14885 | -38.2565 | 2025-12-12 03:29:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fac3b6cf-42a4-384e-9d9d-576a802070db | -4.39062 | -43.6284 | 2025-12-12 03:29:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4adaf713-fa19-38c9-9e66-c7431662fba3 | -4.38424 | -43.6272 | 2025-12-12 03:29:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44effa26-4f6d-3bea-9a69-a25693f102bb | -6.46866 | -35.16836 | 2025-12-12 03:29:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 42d81d59-73cf-36f0-a554-989fdd576bcb | -9.67001 | -36.01824 | 2025-12-12 03:29:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 250c3ac5-e638-33c0-85d8-69f7fe264527 | -4.6924 | -43.24246 | 2025-12-12 03:29:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff43cffc-9fa1-37cf-a750-86ac497c4443 | -3.93588 | -40.73542 | 2025-12-12 03:29:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a5cb617-47e0-30fa-92c9-65d8410b6a68 | -10.18848 | -36.32775 | 2025-12-12 03:29:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5c89c485-a9b0-319f-90d1-f8a10a87d3b2 | -9.66851 | -36.01941 | 2025-12-12 03:29:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| ec5b5a21-93d5-3cf0-9cd7-258d90508866 | -9.41334 | -35.79826 | 2025-12-12 03:29:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6dd37c7b-bd3d-313d-b351-7a3c3c03f81a | -6.95697 | -38.61918 | 2025-12-12 03:29:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e6e327aa-9df0-3444-9057-f47f2df70c02 | -9.40877 | -35.65003 | 2025-12-12 03:29:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b3d108aa-3dd2-3416-9127-6e65fbc389ff | -7.33026 | -34.98182 | 2025-12-12 03:29:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 9dd1c087-1321-3a32-a91c-c3ecdc7678df | -6.47294 | -35.16477 | 2025-12-12 03:29:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5eb4b3a7-69df-32b1-ab16-8db7722a7448 | -6.12355 | -41.28208 | 2025-12-12 03:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97d902a6-d5f3-3193-96c0-ff7e8a812569 | -2.4367 | -51.9274 | 2025-12-12 03:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 562457db-2140-336f-97fc-978ff89fa384 | -14.9134 | -58.1263 | 2025-12-12 03:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| cfe41956-c6dd-3f76-9a06-7bbe5505845c | -2.4367 | -51.948 | 2025-12-12 03:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 80a87b7d-c9f2-3052-b5c3-e55848c41a7e | -8.0513 | -43.1001 | 2025-12-12 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 93d0ce27-a82f-3aa5-9dd1-4a7d424003b8 | -2.4183 | -51.9278 | 2025-12-12 03:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 68452315-7dfe-345d-8c5a-771fbe2594e0 | -2.4183 | -51.9484 | 2025-12-12 03:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 20fecfa4-5a91-3e9e-88c4-4e96afe60bec | -2.5108 | -51.8023 | 2025-12-12 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 3d1cec8e-69ae-3de5-bd7b-e86e5838c1f8 | -8.0324 | -43.1022 | 2025-12-12 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.9 |
| 96cf958c-7853-37e2-8dd8-7a8dccf1bd51 | -2.4923 | -51.8027 | 2025-12-12 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ca5504ad-0816-3af2-8070-0f18c2647d3a | -8.0327 | -43.0786 | 2025-12-12 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 450b5994-80b4-349a-96ec-24dd5bdcb1f6 | -14.8941 | -58.1282 | 2025-12-12 03:30:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 69317923-fd25-37bc-a4b5-27a416034f16 | -12.21214 | -38.98269 | 2025-12-12 03:32:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2bbda274-1164-3156-8ba3-ea461b8e430c | -11.10942 | -40.28148 | 2025-12-12 03:32:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f50a98b6-3949-3a5f-a8ed-91f2fd95a0b0 | -12.25834 | -38.2436 | 2025-12-12 03:32:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f7e60d92-76b5-37d4-976e-dd10317ebe2c | -12.12972 | -39.4044 | 2025-12-12 03:32:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31aab986-aa3d-3364-99e4-bee1d8a70aed | -11.88971 | -43.7066 | 2025-12-12 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cadbae9a-9115-38ac-96b5-28f54606194a | -12.20992 | -38.98265 | 2025-12-12 03:32:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f3aa2022-e04a-3d6a-85b1-61aa79f09faa | -12.12901 | -39.40845 | 2025-12-12 03:32:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a68e764-78ce-341b-9c95-9aa5863037a2 | -11.88767 | -43.70683 | 2025-12-12 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e878368-35fe-3b02-8158-9578826a6d92 | -11.10949 | -40.28398 | 2025-12-12 03:32:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2a96c954-66ea-3ca9-a39a-bc83672d89eb | -20.53771 | -41.83103 | 2025-12-12 03:34:00 | NOAA-21 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 41f0f171-73e4-3252-be3d-3f4fa5165c06 | -22.89498 | -43.58257 | 2025-12-12 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 93317ae5-66d6-3f6c-bc7f-6b7daa4dff2c | -23.3032 | -45.64954 | 2025-12-12 03:34:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 794ece57-ac63-31c5-a712-433030824a89 | -22.95454 | -48.70336 | 2025-12-12 03:34:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d818eaa-674d-339b-9075-4ec90362c9a0 | -22.12313 | -43.2618 | 2025-12-12 03:34:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 26851263-489a-33fb-881e-b1d2b6ab8ee4 | -22.95326 | -48.70871 | 2025-12-12 03:34:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a4a125d-6b3c-33c4-83d3-17e7659a05b0 | -18.69024 | -42.96558 | 2025-12-12 03:34:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7c4e5248-c901-3eb6-a739-b7193c0e6c73 | -19.86709 | -46.56165 | 2025-12-12 03:34:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c3d94af-20f6-3c7f-8327-327ddb2064fa | -23.50215 | -45.93834 | 2025-12-12 03:34:00 | NOAA-21 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 72face17-d56e-32c8-8881-91ba3ebde720 | -22.95197 | -48.70488 | 2025-12-12 03:34:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7dcf58d-47cb-30f9-b102-1748b842b88b | -23.30386 | -45.6465 | 2025-12-12 03:34:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 92c996ba-45b1-3c0d-ba94-c28fdcbe284d | -20.38507 | -41.3348 | 2025-12-12 03:34:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 23299828-a5fe-3c13-8a54-85310597c0a6 | -21.6574 | -42.45654 | 2025-12-12 03:34:00 | NOAA-21 | ESTRELA DALVA | MINAS GERAIS | Brasil | 3124609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80b2d5aa-595a-3478-b326-887d9d7b2af6 | -22.89853 | -43.58554 | 2025-12-12 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ffa1d4ad-a075-3b23-aef2-6a411f49224c | -20.27419 | -41.59313 | 2025-12-12 03:34:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a7c0906-91a1-36cd-b557-1bf739cb86ef | -19.86522 | -46.57015 | 2025-12-12 03:34:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f63daf7d-09b6-367e-a9f6-22af5c9c1be6 | -8.0324 | -43.1022 | 2025-12-12 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.0 |
| dd577b48-b641-3b43-876d-e101016ff440 | -14.8941 | -58.1282 | 2025-12-12 03:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4a86aa56-af19-36f6-945a-b150fcc91b03 | -2.4183 | -51.9278 | 2025-12-12 03:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 5157a7dc-f603-33a3-b3df-98e46f3fa695 | -2.4183 | -51.9484 | 2025-12-12 03:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2021e8a8-6ba3-34af-96f6-9413cf534210 | -8.0513 | -43.1001 | 2025-12-12 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| c6d410c1-3a81-335e-aed5-1409f4dd1b83 | -2.4367 | -51.9274 | 2025-12-12 03:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 3223e182-970d-355e-86e6-5c84c4827732 | -2.4367 | -51.948 | 2025-12-12 03:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4ed984c3-e0de-3f41-90fa-ace88dd8dbe2 | -8.0327 | -43.0786 | 2025-12-12 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 7a865806-70c8-30f5-8a3f-955320c27b2b | -14.9134 | -58.1263 | 2025-12-12 03:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6ed70945-d7fe-3457-a67b-0abff28e2d33 | -14.8941 | -58.1282 | 2025-12-12 03:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 4ebdb3d3-1390-3617-8e63-36fe537ed9a1 | -12.4133 | -58.049 | 2025-12-12 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| c3fe93f6-5df9-3c30-8e17-073224eb841a | -2.4367 | -51.9274 | 2025-12-12 03:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 1772b7e6-3f20-3799-a5c8-a300da5204a6 | -14.9134 | -58.1263 | 2025-12-12 03:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| bad521e2-196f-39c3-800a-bb6c759cda59 | -8.0324 | -43.1022 | 2025-12-12 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 91f61adf-0545-3bda-a6e0-f64c6e5c39f0 | -12.4135 | -58.0292 | 2025-12-12 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 4cf2dfe6-09c9-39dc-a4ae-c2fca3e61de1 | -12.4323 | -58.0475 | 2025-12-12 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 30a2cf37-d0e6-37c4-95e0-d916fa9a2ab6 | -12.3943 | -58.0506 | 2025-12-12 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ad1e1cfc-39ea-3b77-a487-f43ee76ae796 | -12.4325 | -58.0276 | 2025-12-12 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| af1c9590-918a-33d8-8bfa-13dc4a21837f | -12.3946 | -58.0307 | 2025-12-12 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4bfe04a0-5d1d-3fa8-8ef4-a6b31f806c0e | -3.30711 | -42.53371 | 2025-12-12 03:57:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 692a3340-998a-3396-b58a-5c4652138fb9 | -3.26751 | -45.56278 | 2025-12-12 03:57:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| df0f6266-a1c2-3c49-9f2a-873291f98cf5 | -2.21884 | -45.4001 | 2025-12-12 03:57:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3f9f9d6-51ac-38cb-8f6c-14f622927920 | -3.81318 | -47.05569 | 2025-12-12 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b7acc38-c2e4-305b-97de-9defeee3a809 | -4.45214 | -38.25507 | 2025-12-12 03:57:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4d8fff2-5ce1-3760-a63f-84899a70b7b5 | -2.77938 | -45.56851 | 2025-12-12 03:57:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e79d95-1dcc-3e35-8059-69323b2fba35 | -4.38641 | -43.62716 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2c28c5a-0fa3-3b1f-a9a9-09d47c1853ce | -3.97074 | -42.51367 | 2025-12-12 03:57:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4406c397-0b8c-3a9a-95e2-52009590f818 | -3.97469 | -42.51431 | 2025-12-12 03:57:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1bba1739-ccc8-3868-b43b-c3e6dbeb454f | -5.10098 | -39.40976 | 2025-12-12 03:57:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 687ce6e0-56ff-362e-a776-3e609f4e9771 | -3.95669 | -41.52546 | 2025-12-12 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 82f1deaa-fc9d-35f5-aaa4-a48b1483286c | -5.06388 | -44.47047 | 2025-12-12 03:57:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5b553a8-9a80-388f-8c7f-6a470082fb64 | -2.67117 | -46.89748 | 2025-12-12 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d2d985b-171a-3a15-b843-8d929beb7f81 | -3.96486 | -41.52219 | 2025-12-12 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7e740e6d-37a1-3e2d-861a-a3944b442f5b | -2.24165 | -46.51995 | 2025-12-12 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca0d832a-9d03-3d2a-8643-0646c09fbc4d | -3.24079 | -43.2918 | 2025-12-12 03:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3420097-0077-3d0d-81c4-d92fba7c1ba1 | -4.93413 | -43.96346 | 2025-12-12 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c362f66-0ce7-38a0-a3fd-9326148959ff | -2.48313 | -47.77526 | 2025-12-12 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README11.md)
