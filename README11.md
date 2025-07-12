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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c093fa54-e9e6-3e5f-8762-6e732cfb6153 | -7.84517 | -56.66595 | 2025-07-12 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c30a4af0-623c-30a4-9ae9-86bb7e52e976 | -9.85508 | -47.87341 | 2025-07-12 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beb1a2ce-24ad-3ea3-b877-2d119b35f443 | -8.75192 | -43.95922 | 2025-07-12 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33209fa3-144f-3432-9fd2-19c5e85500d4 | -13.1223 | -47.30799 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9829a1b-b618-37fe-8477-08d29fbf5fab | -11.41931 | -46.40053 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d400c914-002d-3a2b-9c12-103095a28eb4 | -11.41477 | -46.40487 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a38f764-9319-37b8-a182-fa664583102f | -9.62287 | -49.1058 | 2025-07-12 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bfa91b4-c69e-3f48-8f13-d84fdc9a2d14 | -6.86224 | -42.77208 | 2025-07-12 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0400ebde-7b08-34be-a292-ee04fa8d163a | -11.44376 | -45.10271 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c49fd307-832c-348d-9cb5-aa5d055af2b9 | -13.00623 | -46.28209 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6db0cdc2-342b-3f92-acea-363ccc2bbd5e | -10.6725 | -49.50311 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d42eeb1-20f0-3819-a58d-1a983f474b45 | -10.87346 | -45.0792 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89389aad-54f6-3f43-979d-55affbc8448e | -8.96073 | -49.84631 | 2025-07-12 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7fbfb74-a747-38a6-b525-6e197b94f332 | -7.29623 | -43.05164 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 655d8685-d5db-38c6-a9c3-4aa63fe41ca0 | -8.26048 | -46.09745 | 2025-07-12 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bb9b981-3091-3a87-96ae-b3c6df319695 | -10.64774 | -47.26012 | 2025-07-12 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5aa23c8-07de-3672-9986-83b26b5d9af9 | -7.18396 | -42.98519 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9d05472d-41c3-34e3-8537-ebfa67ae9a28 | -12.4149 | -45.35049 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 582af853-5f2a-3f8e-a022-3bbc4b2f3c53 | -10.35699 | -49.92087 | 2025-07-12 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1f41af6-603b-3d39-ad18-56987bd17d78 | -8.6854 | -47.99057 | 2025-07-12 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2964dcaa-fa86-37e4-b576-7383e00c8e8b | -10.39527 | -49.78266 | 2025-07-12 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01fdaf11-f4e7-3cf6-a4e2-fb6194eaa737 | -11.82819 | -48.20827 | 2025-07-12 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8470ad17-0e4f-35b1-9fee-6871b8d8d2f3 | -12.99972 | -46.27063 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18d61c91-9d89-35e0-b604-ffd2d14de53a | -13.01015 | -46.2829 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 483648c8-1b7a-32a8-bc06-8be70dc6360d | -10.89806 | -49.20972 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 66d3bbac-128e-340c-89ff-b496e48376f4 | -10.86413 | -49.11512 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6ae0e90-4037-3bd9-9e5e-974208b07f24 | -12.49232 | -51.27485 | 2025-07-12 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 714e99b0-73dd-3a89-b539-dbefa9049671 | -13.13862 | -47.27382 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40b54acc-ac01-3c6f-a65d-06c0db7be364 | -9.51692 | -47.56627 | 2025-07-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94653d58-e20c-3756-b6fc-f238fe085b7c | -9.65554 | -62.91276 | 2025-07-12 04:40:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf34b432-0335-3705-afb9-2d53415b4bff | -8.71937 | -47.16612 | 2025-07-12 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15b70765-2084-3947-bfb0-46ffdf3e45b3 | -7.98498 | -46.42382 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5efc859f-1e9c-3b8a-83dd-b2740db71cf4 | -10.89525 | -49.20554 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 891022c5-aff2-3852-a355-df3972f32aac | -8.91958 | -47.35016 | 2025-07-12 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 423a1bd4-898e-3dec-bc01-7bcd146d94ad | -10.89861 | -49.20609 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 274ad11b-a435-3c3b-83f5-f1f7daed7688 | -10.09437 | -60.49622 | 2025-07-12 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aafe3e1d-bf47-34fe-8a8c-8c3e594093b3 | -12.99688 | -44.86985 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 641a1d1c-2136-30e6-b5e5-30d75e401f63 | -11.72408 | -47.47239 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 659fc336-52bc-3afe-86d4-5e8078dc2929 | -8.71881 | -47.16431 | 2025-07-12 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8726765a-69be-36c1-95a0-3144d8130589 | -10.85119 | -49.1094 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f58df235-a413-30e2-b4be-daa5320e3e30 | -11.45471 | -45.11612 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18859d7a-b5b4-3b3e-90fe-8a345dc247f4 | -9.79969 | -48.57042 | 2025-07-12 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ccfa73a7-ec72-3588-89cb-c5dd177eecf1 | -7.21371 | -43.10148 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f2023595-bf33-3783-9aeb-53ff44081057 | -9.50926 | -47.56919 | 2025-07-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78a0fdf7-ec20-3f88-beed-62f3f55a4142 | -5.84635 | -48.39595 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 4a59be4d-3bc5-305e-a658-cfa6c4fa9d22 | -7.19284 | -45.32393 | 2025-07-12 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9f3191b-d9ba-34e2-8eda-0d96df6ea862 | -6.71272 | -44.32922 | 2025-07-12 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00497753-964d-3251-be93-7115d5b702d6 | -7.22719 | -43.10355 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 191358e6-7c59-3edf-a290-1f033360a5a6 | -13.13291 | -47.31365 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5433b099-4547-3179-9767-923890835575 | -10.68741 | -48.30801 | 2025-07-12 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 564832c1-017b-3f35-b762-0bbaa1ba51d5 | -10.80585 | -49.6331 | 2025-07-12 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a797d75-097b-3035-9f50-aea0253ba9da | -8.68884 | -47.99111 | 2025-07-12 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de06da54-0af7-39bd-8d78-4468dc0ae05c | -9.11583 | -47.63837 | 2025-07-12 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 18aede17-bbd7-3bc7-a6cc-a64ddae32908 | -6.71683 | -44.32984 | 2025-07-12 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96198421-bd54-31af-8c57-2bc96d07f1f2 | -5.85023 | -48.39294 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 7aaa3d31-11a9-3c73-9d90-3a614be6187b | -8.75626 | -43.95987 | 2025-07-12 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaf8bf8b-5620-39e8-b58d-e567b8b2246f | -6.85265 | -42.77258 | 2025-07-12 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1314997-b2dd-3655-82e3-4515838c9c8f | -10.57472 | -49.12312 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e0ed7b9d-4880-357a-8a71-a5d26041573c | -13.11856 | -47.30755 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe67f8d4-1a45-34df-a4fb-d3a24ff2e669 | -5.8441 | -48.38839 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| de68bb22-e80e-3011-9f5d-9d0cfce9fe02 | -8.03998 | -50.10128 | 2025-07-12 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d239447a-0a34-3faf-8382-75ad51e416c7 | -11.93701 | -51.68794 | 2025-07-12 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f1e780c-cb7d-36f4-b85b-bc8755389ef4 | -12.41735 | -47.50817 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24197093-4344-3449-a431-393de4ecab22 | -10.39532 | -46.99232 | 2025-07-12 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c2b67ac-ed1d-36c5-8905-84a0bc87b54c | -9.50987 | -47.56518 | 2025-07-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d8516a7-c368-3979-83b6-7c3813b7c2f6 | -13.11544 | -47.30275 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16462268-898a-3ff3-a338-e2029df8d084 | -7.98562 | -46.41943 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8c2bc54-9099-3f0e-9310-ae7ee7cb0f60 | -7.84726 | -56.66829 | 2025-07-12 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ba304c-06a6-395b-b134-4774c2d2d7b2 | -6.72093 | -44.33044 | 2025-07-12 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94006c80-aaa5-3471-a77c-e53ce436a407 | -11.42628 | -46.40663 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f55acccf-93d2-354a-adbf-1173cca98b27 | -8.01248 | -50.10405 | 2025-07-12 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5907a20-6970-3d04-a12e-c7ab60b2faca | -7.69218 | -44.37427 | 2025-07-12 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5544dbea-c78e-3b41-8ae4-6a788ef43056 | -12.99044 | -46.2795 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e21ba818-aa6d-3afd-a549-5fe361803925 | -6.88008 | -44.06974 | 2025-07-12 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 156b0f52-2883-3650-b91d-fc153a1eaa31 | -10.04695 | -59.11232 | 2025-07-12 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 966012e4-256f-3cba-b410-d183068fd603 | -10.57582 | -49.11587 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 3cb246dc-4aa6-385c-a512-238ff811d81e | -7.66884 | -56.75149 | 2025-07-12 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdcf80ac-63a4-3655-a7c3-ddd6b954b9f3 | -10.84052 | -49.11146 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ad5bc86d-bcd5-3ef2-9769-bfc373cc8010 | -12.4906 | -45.01787 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f59bbf2-f7b9-3210-9104-6c5a5fd0edaf | -5.84022 | -48.39141 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| cbb59622-1438-36d0-9241-916806d2ea4e | -11.44583 | -45.11878 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70063c8c-cac8-3f7b-9b4e-1415046d64eb | -11.77248 | -43.86777 | 2025-07-12 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7291a09-cab4-3117-9f78-03fd448ea5ee | -13.14476 | -47.31065 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48d7f574-27e4-3d49-a3d3-84303b50cd09 | -8.45647 | -47.52344 | 2025-07-12 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b755a7b-d200-3229-bc58-5b088e0c0316 | -8.89437 | -47.27715 | 2025-07-12 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 122b41b3-eef3-31e2-82c2-f8d0ff83bdf1 | -8.5259 | -54.77229 | 2025-07-12 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a0a1a09-137f-3595-957e-19da8049575d | -13.12545 | -47.31256 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e38732f5-885b-335e-a8c2-f7435e7c0b21 | -13.13663 | -47.31424 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30b249af-5bfd-3c49-acc0-772caf11cca1 | -7.99298 | -46.42049 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4e47bec-72ef-3a26-b1a2-1db56878d73c | -11.00025 | -45.22006 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 311eece3-7ddd-3b9e-9642-bac3f4675d0e | -12.48994 | -45.01684 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fef73f1-09cf-324b-ba7e-667757b20504 | -11.15274 | -49.69843 | 2025-07-12 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 527ecd0e-4856-3758-9404-48ca8fa9b5c0 | -11.42273 | -46.37673 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9688784a-1d8f-3a0a-89ff-5cd75f461e32 | -7.08379 | -49.60553 | 2025-07-12 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c710648-9008-3098-a0c6-6f8165e9c561 | -7.29172 | -43.05093 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 28b8caed-d010-3cd1-8e87-302d015f0d6f | -9.00135 | -47.93976 | 2025-07-12 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b17c6d2-51e9-3254-a90f-a2a02cc4d27e | -13.16296 | -47.30061 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4d47a2a-ae45-3665-bead-4636ee77058a | -13.01751 | -47.83071 | 2025-07-12 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1223c401-d7e7-39bc-8585-310a38cad90a | -6.86682 | -42.77279 | 2025-07-12 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc3ba51c-b271-370e-82ca-378818508827 | -13.1429 | -47.30823 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README12.md)
