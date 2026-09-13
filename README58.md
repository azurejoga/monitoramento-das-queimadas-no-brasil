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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 005290d0-d985-3937-a8a4-d819d67e50cd | -3.38627 | -50.75578 | 2026-09-13 06:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 57e04e06-d6fe-38f2-a3cc-98f555c25ffb | -8.75424 | -71.03165 | 2026-09-13 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e71df9eb-8fc8-3469-aa53-78923660c18c | -7.6413 | -73.09854 | 2026-09-13 06:52:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44423b29-c0d5-32e4-8598-587bfba29dfc | -8.54201 | -70.86993 | 2026-09-13 06:52:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02c2b5f0-e31d-3f45-9b4f-52fe8bd09d97 | -7.37433 | -45.3562 | 2026-09-13 06:52:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d953bc59-850c-3843-a998-d19098d3eb70 | -10.46599 | -48.63276 | 2026-09-13 06:54:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a4706c5-d091-3fff-9f28-a72ca00c8b2c | -13.61152 | -47.87479 | 2026-09-13 06:54:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 23d870a9-c74f-3cf6-b925-164b87fd5934 | -10.67657 | -54.16155 | 2026-09-13 06:54:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0f840dd8-7f8e-3881-a8d2-7f683b36949f | -8.12003 | -54.7973 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4a117f0f-6131-3fd2-8c8c-bf38a8b7cd7f | -8.54219 | -54.69644 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 8e5040fa-6392-3473-90d3-4fb7302f88cc | -13.45037 | -48.48884 | 2026-09-13 06:54:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| df717416-48bc-3063-b5e5-bc5948fdba29 | -8.04448 | -54.84464 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fbe20582-67ed-3062-aaff-144aaaf9a63a | -7.86865 | -54.71959 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c85756fc-97c9-38e0-bb28-cd2ff5039740 | -13.44891 | -48.49892 | 2026-09-13 06:54:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fab49d07-a088-3189-98a0-855bf24e70a5 | -13.45181 | -48.47883 | 2026-09-13 06:54:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 48d32bb2-a8a2-3890-8c45-410fb1a23922 | -7.1836 | -50.83302 | 2026-09-13 06:54:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 58e3f03c-6fb8-3d34-a404-36914e0035ec | -7.86238 | -54.69667 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a97a421b-9030-37a8-aba1-2a3501f1f89d | -9.37592 | -50.11586 | 2026-09-13 06:54:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e181f84a-6e30-359f-87a3-17baf4a8a07c | -11.34862 | -46.79149 | 2026-09-13 06:54:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6c985141-654a-37ba-b9bb-9c5cfaa410ee | -12.66148 | -54.66395 | 2026-09-13 06:54:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e21196a8-edea-337e-8afb-a7011ea7045a | -8.53961 | -54.71194 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| d06df6bc-373c-326e-8fff-6295fa10e478 | -11.81214 | -46.40749 | 2026-09-13 06:54:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 216636da-a33b-3234-9adf-67e7519f380c | -10.54931 | -51.32336 | 2026-09-13 06:54:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7740cc1f-d181-35f6-8dc1-d603c64dc7e5 | -10.68712 | -54.16322 | 2026-09-13 06:54:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 9f72f535-73a9-3556-8c6f-85651d7c6f4a | -11.81389 | -46.39498 | 2026-09-13 06:54:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 503b4294-f726-3d37-9301-3ae1521f8114 | -10.68495 | -54.17643 | 2026-09-13 06:54:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 534a8ea2-510b-3784-8f46-9fda3d50e2a1 | -13.61973 | -47.88633 | 2026-09-13 06:54:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4130e65d-3deb-3acf-a16e-274f6089dd9f | -10.53508 | -51.29566 | 2026-09-13 06:54:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4fa9ff5c-8b2c-33b5-ac1f-041d3e4122e1 | -13.45965 | -48.4753 | 2026-09-13 06:54:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 336605af-7304-33a8-a84f-76301c577b5b | -11.81966 | -46.40277 | 2026-09-13 06:54:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| be4f211b-5b80-391b-9d29-3456da51557f | -10.68926 | -54.15017 | 2026-09-13 06:54:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 7ad64488-5c48-3019-af3d-f27d1fe936f2 | -13.45821 | -48.48555 | 2026-09-13 06:54:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 90742b69-80f5-3577-bdb9-b46655b0268e | -8.12236 | -54.80733 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ed90359d-cb18-3796-9c29-b5c19e37a327 | -11.35023 | -46.77993 | 2026-09-13 06:54:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 220c6d74-7ba5-31d1-a9ae-60d4e0e04909 | -13.2938 | -51.6417 | 2026-09-13 06:54:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 40079a56-287d-39ac-bf9a-c7060e03eda9 | -13.62118 | -47.87604 | 2026-09-13 06:54:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 67c17579-4b35-304b-b448-2c058e5faa0e | -7.87132 | -54.70364 | 2026-09-13 06:54:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 892fbca3-40a7-3400-a386-788933f266e2 | -18.59844 | -48.65989 | 2026-09-13 06:57:00 | AQUA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e935bf52-6c5c-34b3-9051-ee2b5c9506ae | -10.6827 | -54.1679 | 2026-09-13 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 037ecc70-5006-31ab-ad59-4439e1ca246d | -10.6827 | -54.1679 | 2026-09-13 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b1edb717-0fd2-32b1-ac35-80588b3068e1 | -6.1111 | -57.6645 | 2026-09-13 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 785214f0-4b2f-3887-aa86-cb9ed773e199 | -11.354 | -46.7874 | 2026-09-13 07:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 077c5aa9-cd9b-3318-92eb-c50b413e6f73 | -6.1111 | -57.6645 | 2026-09-13 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9dac46c4-155c-37d1-be3f-23bbd445e8db | -10.6827 | -54.1679 | 2026-09-13 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 054d9c31-4155-3e84-b411-aa2cf3331176 | -11.3349 | -46.7899 | 2026-09-13 07:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 61c9c4cb-f246-355e-943d-1aaa4ce7543e | -6.1111 | -57.6645 | 2026-09-13 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 03e3f2c1-852d-3801-91f3-e7cb996a4430 | -11.354 | -46.7874 | 2026-09-13 07:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 7ac7c0e4-4aca-3fd1-9559-8043c02487d8 | -13.4507 | -48.48 | 2026-09-13 07:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a7279c87-6a19-35f6-8361-5b3879d42370 | -6.1111 | -57.6645 | 2026-09-13 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 76b47372-8df1-315b-8656-973a2e38757b | -6.1111 | -57.6645 | 2026-09-13 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 76fe53e9-13f6-32dd-b35b-759199973267 | -13.4507 | -48.48 | 2026-09-13 08:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c1eb0a8a-96c1-373c-a702-5c6b2abe5bbe | -6.1111 | -57.6645 | 2026-09-13 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| df159e00-dfa7-3b19-92e6-c4ab98fce5fb | -10.6827 | -54.1679 | 2026-09-13 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 8e2b873d-4a49-3e79-b8a7-6a53cdc4afe5 | -13.4503 | -48.5022 | 2026-09-13 08:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b6d690ad-43db-38e1-939d-b526578df176 | -10.6827 | -54.1679 | 2026-09-13 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 6e0ed8f1-752a-3de9-9dc3-ded70df23f64 | -6.1111 | -57.6645 | 2026-09-13 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 52cb4c04-a4f3-3a54-9298-d1e9a1889968 | -6.1111 | -57.6645 | 2026-09-13 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 7ea7eaca-8226-3a8c-8a5d-aeb55cdb38f5 | -10.6827 | -54.1679 | 2026-09-13 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8e561d33-a0fd-3e3d-a77a-27e7e02dbbf6 | -13.4507 | -48.48 | 2026-09-13 08:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0ecdb425-ca8b-34b7-895e-b40629e715c3 | -13.4503 | -48.5022 | 2026-09-13 08:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 772ccf5a-f646-33f3-957a-7e6761e2ae82 | -6.1111 | -57.6645 | 2026-09-13 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fdebb56d-ca7c-3819-bd84-1a3553b4eb12 | -6.1111 | -57.6645 | 2026-09-13 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9b3a5e0f-2cfc-3321-a4ec-f9f746daa0ac | -7.0164 | -44.6413 | 2026-09-13 09:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 0f49e10b-dcb5-3d7b-b735-76947cdbe89a | -7.0164 | -44.6413 | 2026-09-13 09:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f6df98e2-66b8-305b-bde8-51569cfcb392 | -7.0164 | -44.6413 | 2026-09-13 09:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 36bb7257-603d-3748-9ecf-7e7d91d90c19 | -7.0164 | -44.6413 | 2026-09-13 09:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 27efa97b-4abc-3d37-8f40-cccd335c3052 | -7.0352 | -44.6396 | 2026-09-13 09:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c04f0861-7726-3c02-9f79-6c0bed9b5ef4 | -7.0164 | -44.6413 | 2026-09-13 09:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 270.5 |
| f25cee7a-f40a-3162-bab6-8307a1028cb8 | -7.0161 | -44.6642 | 2026-09-13 09:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 06414ee1-2c67-36ab-be04-5b7e01aa2170 | -7.0164 | -44.6413 | 2026-09-13 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 239.2 |
| 31ab8bf5-fd33-37f7-9635-6c0c2af23fcf | -7.0161 | -44.6642 | 2026-09-13 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e5ec8d0d-1f01-3138-94ab-4225d2b4fca5 | -7.0352 | -44.6396 | 2026-09-13 10:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| a7f3f3c5-0b51-3021-83ac-ac7d28aac0c7 | -7.0166 | -44.6184 | 2026-09-13 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| fd37e916-dcd2-3d5e-ab82-a828bf370daf | -7.0161 | -44.6642 | 2026-09-13 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| fc1d3a1a-b76d-3e9c-a76d-72e0c4ab4739 | -7.0164 | -44.6413 | 2026-09-13 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 341.1 |
| 454cdbed-b92a-3684-af5b-ccf097c0b225 | -7.0352 | -44.6396 | 2026-09-13 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 4cbc2e53-b520-33cc-936b-17ad3a4c5d2c | -7.0352 | -44.6396 | 2026-09-13 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 369e5dd7-55ee-37b7-8fa0-71ae2fea5c19 | -7.0164 | -44.6413 | 2026-09-13 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 338.6 |
| 989c486c-96d1-3530-8251-108dc4f44ec2 | -7.0161 | -44.6642 | 2026-09-13 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| fc4cc60e-6d5c-3438-bd31-9882ddf02e2b | -7.0166 | -44.6184 | 2026-09-13 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| eecf8ba6-809b-3080-b408-11a8626ba7c9 | -7.0164 | -44.6413 | 2026-09-13 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 318.6 |
| ad0e0a21-fe65-3744-ac4e-e94698aa30d5 | -7.0352 | -44.6396 | 2026-09-13 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 219.8 |
| 4f3bc394-48eb-3bcd-a582-8b6fc17bb2b0 | -7.0166 | -44.6184 | 2026-09-13 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c2a37093-f24f-378b-bf84-a442e3855dee | -7.0161 | -44.6642 | 2026-09-13 10:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b4f05125-2146-38f6-a825-df3d6043efa8 | -7.0352 | -44.6396 | 2026-09-13 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4c9d820c-ae51-3e02-a722-706e9868a997 | -7.0161 | -44.6642 | 2026-09-13 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 3b19ffbb-9538-35e8-8152-70838a004d4a | -7.0166 | -44.6184 | 2026-09-13 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 9e8af2bc-fadf-3eb8-91d4-74b5efbee617 | -7.0164 | -44.6413 | 2026-09-13 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 444.1 |
| a5d891a7-f2cf-328f-a29d-ed3a83c8799d | -5.43342 | -37.02308 | 2026-09-13 10:49:00 | TERRA_M-M | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 3460c2a7-bbfb-3111-995e-d870f4b3bea1 | -9.55618 | -37.33201 | 2026-09-13 10:49:00 | TERRA_M-M | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6ffb59c0-97f2-3916-8b24-fa0063b37be8 | -7.0352 | -44.6396 | 2026-09-13 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 199.5 |
| a1a046dc-3d92-3c99-858c-336196460f3d | -7.0161 | -44.6642 | 2026-09-13 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| b9abc1f5-7afe-36dd-9eae-c9e22480d3f6 | -7.0166 | -44.6184 | 2026-09-13 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 05a32b92-10b4-3d84-8a51-12bd4aa580a1 | -7.0164 | -44.6413 | 2026-09-13 10:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 393.5 |
| a2af43c2-17aa-3ff8-9932-1b9c980dd77b | -7.0166 | -44.6184 | 2026-09-13 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 3c185cde-60d5-3fff-ab00-72e9806c7f87 | -10.6335 | -50.5651 | 2026-09-13 11:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 85620734-6f71-3318-96f5-9e937c562a0b | -7.0352 | -44.6396 | 2026-09-13 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e5402ed5-9c7c-35b2-a979-f2ba02175e4f | -7.0164 | -44.6413 | 2026-09-13 11:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 449.1 |
| fc3cd9ac-e11a-3398-9a6d-b1b8ae75776e | -7.0164 | -44.6413 | 2026-09-13 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 473.5 |
| 00a78f5a-5e7b-3ed9-be06-1807dca5f572 | -7.0166 | -44.6184 | 2026-09-13 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |


[Clique aqui para ver as próximas entradas](README59.md)
