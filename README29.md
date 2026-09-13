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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b80f26be-2b14-3a64-8d59-f3052ec0bf02 | -2.67186 | -57.53799 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 31975e13-d001-3079-af11-b3e4e03ef421 | -3.05064 | -51.26995 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6c43cf8-f84b-302b-bfac-ec167824db64 | -1.19049 | -55.71987 | 2026-09-13 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a199425f-a9f6-3506-b4c2-c996fd620cb0 | -7.46703 | -42.11387 | 2026-09-13 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d0c0adbd-3849-3ed9-90c1-e5a0bbf083b9 | -6.20761 | -45.40094 | 2026-09-13 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0400891-48c0-3905-b130-d5c0e6d28d97 | -3.23005 | -43.04118 | 2026-09-13 04:49:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ddf6cb8-4f6d-35a4-ba1c-9c29b118087a | -3.21252 | -53.94447 | 2026-09-13 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9038be30-219c-3fdb-8aa9-c295409ec6e9 | 0.14409 | -51.46934 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83b53f4e-8b3a-3117-a267-29cb6c871bfe | -7.37341 | -45.35311 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9bdf2a7-ed8a-3de4-a3a6-28c7ff359c83 | -6.08213 | -51.75641 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07e1819c-32b7-3d63-aec6-a4657997679b | -2.66875 | -57.52425 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d78a6b8d-cfb3-3e7f-aef4-0f85a4a1f762 | -2.95755 | -50.39621 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 800be77c-4a91-31e4-85fd-63373efbabfa | -4.45819 | -50.16325 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9827dc3-60f9-3acc-a2d3-9632bcb98e8c | -3.89689 | -55.81892 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e43bd180-90c6-3a9e-9963-35d0c427b7f5 | -2.96214 | -50.38945 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eef71ba8-c1cd-359d-8868-149443fc404e | -5.13187 | -55.96616 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cd0e7ee1-1843-3c20-9a91-087b365b92ce | -4.87323 | -55.99846 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43f3dc08-99e3-3d24-b6c4-28304b5cf1ae | -7.13221 | -43.75378 | 2026-09-13 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41209505-7744-310f-8eb8-7532666ad145 | -6.22814 | -51.68433 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bbc036d-9895-3763-85a5-e42dc0f3faac | -6.09414 | -49.66273 | 2026-09-13 04:49:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08c22ab1-94ae-3c91-b213-ccf73164aed5 | -2.95637 | -50.40353 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d76e45fa-ad1f-340f-b11e-f93b8fa51cc6 | -2.89023 | -48.27644 | 2026-09-13 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e64bda3d-ec61-37de-bb82-7f719c0ce915 | -6.23023 | -43.52202 | 2026-09-13 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4458fe38-893d-3ba2-bbf5-e73ae8fe931c | -4.4096 | -54.85836 | 2026-09-13 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 348cd697-7aed-359a-92dc-19b9f1f50665 | -6.08631 | -51.75603 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1882baa6-5daa-30a6-8695-efad42885379 | -3.04775 | -51.26548 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c368612-a307-3628-8a91-71e17005d33c | -6.6838 | -45.48013 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 523ae6f6-d86d-33a2-b5a2-4f89c66de8c9 | -2.94613 | -50.40191 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdaa7c48-01ea-3b1e-9a1c-d2c3ae892a59 | -2.38943 | -47.5516 | 2026-09-13 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf511c86-9c85-3a8a-8e0a-c3e2b359704d | -6.23383 | -51.69314 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d28b050a-e0d1-34e3-9851-6e629e54a683 | -2.67821 | -57.53245 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e803c263-a67f-3e2a-b2c9-3cb1d6524267 | -3.64388 | -58.63208 | 2026-09-13 04:49:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed8c6b25-71fa-3d94-825e-11244ca38913 | -2.94777 | -50.41343 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 322229b1-7ac9-39a7-ac45-bd3622aa50a7 | -6.23098 | -51.68874 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26e6fc33-83e6-3761-9622-0dab898f6aba | -2.01976 | -47.55143 | 2026-09-13 04:49:00 | NPP-375D | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12d5262d-3bbd-39f5-b380-00dc9ff3b3a8 | -3.73628 | -61.75417 | 2026-09-13 04:49:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f614a024-dd57-3aaa-92f9-32464359f2ce | -5.29164 | -49.20129 | 2026-09-13 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b87086ad-ea93-3690-9e59-cd4e8e4defcf | -2.66348 | -57.52336 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64e944db-93f2-3bb9-ac8f-cc0c0524e0d5 | -2.94268 | -50.40171 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e971dc8-6c9c-384d-85bd-f183681e19d9 | -5.89151 | -52.25726 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62219cb5-c2da-3c02-8d9e-417c342ffd4b | -2.96555 | -50.38998 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bfd7fc2-32f5-3940-8dde-397be1d304f9 | -2.95414 | -50.39568 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4b0ded9-8593-307d-8de8-a7728fec6bf6 | -3.73728 | -61.75407 | 2026-09-13 04:49:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d88e726-b2ab-3ff0-9ee8-f1caa2066f9c | -6.23653 | -51.80813 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20be82c5-946c-348f-9660-dae5880c5530 | -7.13279 | -43.74974 | 2026-09-13 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e75f9587-b477-323e-b405-ea3e08ff453e | -2.07297 | -48.45591 | 2026-09-13 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02b2bf33-9f5a-34e4-9eb6-36b0b6c08d13 | -6.23161 | -51.6849 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43750a30-dffd-3796-a70f-2ad432bf9557 | -3.72951 | -61.75294 | 2026-09-13 04:49:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72aeabde-894c-32f6-b634-7bc5e3d0c6a7 | -3.63187 | -55.31936 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4123465-a58b-3851-81a2-3ee3afbbeefe | -6.542 | -47.28897 | 2026-09-13 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f51b8da-bb7c-3332-8d6c-6ec62e3b3616 | -2.61352 | -54.76202 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f61ebf6-e38e-3bf5-bf36-bb84a5dcbfe2 | -5.61729 | -44.84971 | 2026-09-13 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8812b8a5-9d5c-3131-9ceb-381ef30c6e01 | -5.60947 | -44.84858 | 2026-09-13 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff59476e-6bc7-3c46-8e81-b45fdbb7c8bd | -1.37894 | -49.41482 | 2026-09-13 04:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2920aaa-0135-3758-8fe8-ddde2ef2133d | -1.02798 | -53.73909 | 2026-09-13 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22e429de-36e7-3651-a01a-a010efab01a1 | -7.38116 | -45.3543 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed2cb85c-2664-39d0-b427-57dc714e4e03 | -3.40482 | -48.89245 | 2026-09-13 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bfb1aa24-cfff-371d-8d85-8121bb6cca07 | -3.06414 | -47.77196 | 2026-09-13 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda54b67-d947-3fd0-a01a-fd70f2e1cc0a | -3.33529 | -42.30061 | 2026-09-13 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7bbea658-cf72-318a-b9e5-de32514d5442 | -7.38504 | -45.35492 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bf6e6f1-fcf8-3690-ab4f-a3583edea1fe | -3.22455 | -50.58507 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d686f3c-caee-3c39-9e7e-ca0198f47f97 | -2.94042 | -50.39383 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb0f66d2-b905-3e0d-9da3-2a35b17bc956 | -6.72504 | -45.41402 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bf365df-d378-30cb-bf4b-901220f21488 | -3.22112 | -50.58453 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd11b8bd-25f2-3d62-84fb-7bd6c758bc6c | -3.36527 | -50.75081 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15f172ff-b77a-3871-9db8-e3a507c9d80a | -2.53627 | -54.65803 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3386d5d7-36a2-3627-bbd2-1704ec9e3bf7 | -6.85112 | -47.4318 | 2026-09-13 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44345c92-a5dc-328c-be0a-ea1294d67cd0 | -6.22562 | -51.69966 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 330bbc1a-9c05-3088-8807-aadd50b53034 | -6.07932 | -51.75488 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcede136-9834-325a-bc54-8eb02d88b3f4 | -3.87631 | -51.1818 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5758c70-8624-3ba8-87b9-7ec274c58139 | -3.45441 | -47.46512 | 2026-09-13 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c9c29d3-2693-3ca2-abf7-2ac682c9163d | -3.33793 | -53.2657 | 2026-09-13 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410088cd-8ca0-3b08-adb4-dacf4775501f | -2.95296 | -50.40299 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7e4c455-fa85-3d07-8161-07d84de7eb28 | -5.27886 | -56.03985 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e85033b8-4a08-3105-806d-8bf63e63bfb3 | -6.84994 | -47.43938 | 2026-09-13 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d10cd942-5931-3f11-9c62-cd305d65a58f | -2.72336 | -49.7886 | 2026-09-13 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cd57bb5-73b2-32e9-abc6-9b34d5c3817b | -6.23717 | -51.80424 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9398e7c6-d3c1-32c4-b5f0-a5f72e0d82c7 | -4.40893 | -54.86231 | 2026-09-13 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80692f1d-eb8c-3e87-8375-87758883f312 | -3.87448 | -51.19327 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19c7a049-8b25-399d-8227-e02fafce0653 | -2.56798 | -49.1146 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8e2a67e-8815-31bd-bbdb-24e605c70aa7 | -3.04423 | -51.26491 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d55ea578-9ea7-3483-8980-8c4494b1e166 | -3.38817 | -50.7621 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ac4c95b-7be5-39f9-a10d-be6812ffc6e2 | -2.71002 | -54.52172 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 764ce77c-3d23-34b6-97ab-8236a9117b3c | -3.39222 | -50.75891 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e49902a-772c-3ba8-8ead-1a6a992aa5c9 | -5.47962 | -45.60056 | 2026-09-13 04:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ace06286-bcbd-322e-8e8d-c9a6d8eab75e | -3.73051 | -61.75287 | 2026-09-13 04:49:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38ef9b08-7302-35a7-b7f1-c0f86a9ffe47 | -3.22581 | -43.04052 | 2026-09-13 04:49:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ee30a77-10f4-3afb-948c-d85e20490a93 | -2.90531 | -51.93474 | 2026-09-13 04:49:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfb0f16e-a314-32a9-be12-abc70f8938fe | -5.81123 | -53.80592 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed22a24b-6374-3cbc-9993-ef00284417f0 | -3.64211 | -58.62813 | 2026-09-13 04:49:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54ca9812-508c-37fc-a817-9dabf828ae24 | -4.41386 | -54.85911 | 2026-09-13 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b9129343-41b3-344e-9e5e-0bedc6b70d9b | -2.78266 | -51.36736 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4da0f7d0-e287-3053-b916-305025fe04b1 | -3.05128 | -51.26604 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92205fc5-a240-3dc5-8f57-f1fab732e5a4 | -2.67401 | -57.52514 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b697b0b-6b1a-3a0a-8379-4ae0a6b033cd | -5.61412 | -44.84425 | 2026-09-13 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0def2222-ce72-3a23-9a12-17522c286b43 | -5.907 | -52.10321 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a17f014f-5f67-3327-a381-7444ed14bdb9 | -2.94209 | -50.40538 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a7a0655-891b-351a-821e-e89f0a52335b | -5.82066 | -53.79736 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeacfae1-66d0-3271-b1e9-83ab9fea8d93 | -6.51168 | -47.5975 | 2026-09-13 04:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acde2c30-cf68-3b04-82ef-0985f8b933ee | -4.13576 | -56.33387 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
