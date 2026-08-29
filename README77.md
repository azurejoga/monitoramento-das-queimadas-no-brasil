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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cdf5b2c-1abb-3467-a063-df67a1552875 | -8.9428 | -63.2797 | 2026-08-29 12:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| a02447a9-2d02-3381-ad0a-c03ab2a60afa | -7.495 | -55.3262 | 2026-08-29 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 39da3756-3c62-3429-8806-a07bad6de677 | -10.8215 | -50.6519 | 2026-08-29 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0c5c7d0d-51d3-3641-9380-e24a3ab15069 | -8.9613 | -63.279 | 2026-08-29 12:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 50fc9441-f0d6-3cf3-9ae8-9fddd63840b3 | -9.8031 | -46.3505 | 2026-08-29 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 9c94b3ad-3663-359b-8ecf-bb682749f4c9 | -12.2284 | -50.5363 | 2026-08-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 41f203f3-3aaf-324d-935e-0630a63a372b | -20.9414 | -57.5484 | 2026-08-29 13:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| b70bdd1a-df21-3b53-aea9-e358d7aff115 | -8.9613 | -63.279 | 2026-08-29 13:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 64758704-949a-3dee-8e69-42cd4674f359 | -13.3254 | -46.9333 | 2026-08-29 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 7db7c1e6-6105-3230-a259-93691f57eeb1 | -9.9708 | -53.9419 | 2026-08-29 13:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 216.6 |
| 2e943bad-45df-321b-9bf7-6becac5e7dc1 | -10.8025 | -50.6539 | 2026-08-29 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3c52706b-b8cc-3a8c-8d11-d6b7e7987f92 | -7.9838 | -45.5072 | 2026-08-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 079eff09-07c5-3ed6-bfeb-533474805d2c | -9.9896 | -53.9404 | 2026-08-29 13:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e7f7b2d1-1a4d-34a1-b09a-488c33e2946c | -6.6317 | -43.73 | 2026-08-29 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 979.1 |
| 0e80c04f-ab46-3283-ad42-bd8199f5a7c4 | -7.4952 | -55.3062 | 2026-08-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 870814f9-a2a3-3c8b-9470-9e76b95675e5 | -20.941 | -57.5694 | 2026-08-29 13:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 2afb1408-88d0-3a6c-b3e7-eb022e4cd0a8 | -11.2879 | -54.0317 | 2026-08-29 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 6cd6bfc9-6a82-3dac-a09d-6ce9f77680c7 | -10.8804 | -50.4965 | 2026-08-29 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 07209c35-9b9a-3209-a78a-5156ea4e9836 | -11.269 | -54.0334 | 2026-08-29 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 62d921f3-74a4-3abc-858f-af94fee8ef95 | -12.1902 | -50.5409 | 2026-08-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 774ac1df-4e61-3f35-a16c-14d1c2de6c7e | -8.9428 | -63.2797 | 2026-08-29 13:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 94.9 |
| beb0a4c2-19c2-35d4-a91d-838c62c92679 | -12.2093 | -50.5386 | 2026-08-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b7a947dd-57cd-3e00-ab95-92534b958b17 | -12.9221 | -45.8582 | 2026-08-29 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 884e5b3e-d82a-337c-add4-fa416b9247f0 | -6.7885 | -55.6436 | 2026-08-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b86c0f7d-dfbf-3244-bdd4-e061c42c0386 | -11.1639 | -45.5897 | 2026-08-29 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| dc223b91-61a8-358d-bd76-0db8b38a9c7c | -6.77 | -55.6445 | 2026-08-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 8154ceb7-a366-3e58-b74b-992821289c1e | -7.5137 | -55.3051 | 2026-08-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 400.7 |
| a022f868-ead1-33ee-bf03-384217860373 | -6.7884 | -55.6635 | 2026-08-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| c3079735-1160-3fad-9a1c-40ff9e1867fa | -7.495 | -55.3262 | 2026-08-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 955ecc06-8d1c-3072-8ed6-ba3deeae9ae2 | -6.7699 | -55.6644 | 2026-08-29 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 5dc22cfa-0ed3-367c-a6d5-1d7d1d2e4555 | -10.8215 | -50.6519 | 2026-08-29 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 51c3d6ec-977f-3ab6-9683-ed45553e72af | -9.971 | -53.9214 | 2026-08-29 13:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 235.3 |
| 70832d83-e43a-39d6-b215-3014415381ae | -17.2938 | -46.0291 | 2026-08-29 13:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 3bbaad87-a97f-3bd7-bfc4-6e27afe590be | -6.7884 | -55.6635 | 2026-08-29 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 869efb05-82e7-36d1-a457-5ba3fc33fcd4 | -10.8215 | -50.6519 | 2026-08-29 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d1236939-d3a0-322d-97e6-0f65637f6466 | -12.9221 | -45.8582 | 2026-08-29 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 302.1 |
| d40f82df-5eda-364b-90c0-e7c592b41eee | -11.2879 | -54.0317 | 2026-08-29 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 217.9 |
| fcf71cc6-34ed-33ef-bcbe-d3a2a1177126 | -6.7885 | -55.6436 | 2026-08-29 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| ac6e09ae-739f-3d37-bea3-39b83da07bc5 | -20.941 | -57.5694 | 2026-08-29 13:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| dd4e748c-9484-3999-91b0-248bcec7c59e | -9.9708 | -53.9419 | 2026-08-29 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 253.7 |
| 89a63602-0c46-3d28-b194-e768b14c5af2 | -11.2687 | -54.054 | 2026-08-29 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 88971cf2-25da-3757-8cae-805233f7d84f | -8.9428 | -63.2797 | 2026-08-29 13:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 3f6d2daa-164c-3589-8646-70061f249f1f | -13.3061 | -46.9363 | 2026-08-29 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 70a62b7b-f90a-3c68-9ddc-137100d48feb | -6.6129 | -43.7317 | 2026-08-29 13:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 302.2 |
| 9aac2494-da4c-3398-a650-c4bcdc3ad11a | -6.77 | -55.6445 | 2026-08-29 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 1ae845ea-6d2e-3951-8b09-3f640150c4b0 | -6.7699 | -55.6644 | 2026-08-29 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| c7a90f5a-1c4b-3dec-b469-95f080314bd2 | -5.8895 | -57.7513 | 2026-08-29 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d78eae95-ac75-3800-abef-6896de4951e5 | -7.5137 | -55.3051 | 2026-08-29 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| b0f7d1cc-2e14-3ff6-b76f-6edeee9e3da0 | -12.9027 | -45.8612 | 2026-08-29 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 54dd6a0f-c245-3c9c-bb98-331940b736f2 | -9.971 | -53.9214 | 2026-08-29 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 333.6 |
| 57b6c508-7371-3e05-a27a-db983550611a | -14.4057 | -50.0537 | 2026-08-29 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 763d6647-5d60-3140-9be8-6112a5f8d0ab | -10.8804 | -50.4965 | 2026-08-29 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0eb59ca1-46b0-3731-b844-c5e7fc8cd7bf | -8.9613 | -63.279 | 2026-08-29 13:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 04dba61b-cef2-38f8-8379-ec396e056e80 | -11.269 | -54.0334 | 2026-08-29 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| a6eb1778-156b-368b-9bd0-ce60130b1d34 | -13.3254 | -46.9333 | 2026-08-29 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 41f5f13c-50d7-3dd3-9807-23ade8ec5dd1 | -15.3849 | -52.6677 | 2026-08-29 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a0be7161-1e4c-36e9-a937-720718dfbfba | -12.1902 | -50.5409 | 2026-08-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4a03e589-b698-3a88-ad4c-7752a37b6f3e | -11.2877 | -54.0522 | 2026-08-29 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 0fab67ef-d59c-3153-bf72-92e8096286e0 | -12.2093 | -50.5386 | 2026-08-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a5a2d49b-14a8-33c3-89ef-098a5e34a444 | -9.971 | -53.9214 | 2026-08-29 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 184.5 |
| d0031031-2665-3d1a-a8d2-caef837fe1c4 | -6.7885 | -55.6436 | 2026-08-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| eea388f5-0fb2-33f1-b7ee-1c95a19a766d | -7.5661 | -61.3239 | 2026-08-29 13:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 2e415c41-584c-3e60-a671-8a40207f7be3 | -14.2024 | -52.8643 | 2026-08-29 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 907.1 |
| d73ac833-f1f1-3f52-8167-b83599a56a11 | -12.2093 | -50.5386 | 2026-08-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 17976686-e7ca-3ae4-80d7-d3cc1c29606b | -6.6129 | -43.7317 | 2026-08-29 13:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| c78b8247-f3b6-3fe0-9757-27e8d89a1cad | -7.4952 | -55.3062 | 2026-08-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f2b68dd3-1e63-3aa9-98a8-c51da9ff5348 | -13.9919 | -54.0189 | 2026-08-29 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| cc538730-ddae-3939-978e-ac9bff746bbd | -6.77 | -55.6445 | 2026-08-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4d9a52c5-7171-3b7f-93c2-0b46e73c0564 | -11.7024 | -47.6352 | 2026-08-29 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 13e05ce8-ba01-3806-ac19-ba24eadc5c9c | -11.1639 | -45.5897 | 2026-08-29 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f8bb5458-6180-3a1b-8d36-c59a5cec6bae | -11.2879 | -54.0317 | 2026-08-29 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f7b9632e-cf19-31e0-a695-1ece1958de21 | -8.9613 | -63.279 | 2026-08-29 13:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 9bffcc4f-f162-3cf7-986b-b507014be602 | -11.269 | -54.0334 | 2026-08-29 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 35206ee6-6865-3e8e-85b9-22ad2fb9c501 | -9.9708 | -53.9419 | 2026-08-29 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 46f7308f-3940-366c-8781-73c6b1e91b71 | -20.9207 | -57.5723 | 2026-08-29 13:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 63ed0445-ada0-382b-8614-9dfef11a9c54 | -9.9896 | -53.9404 | 2026-08-29 13:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f2798180-79ca-3eb3-959b-dc5a51a04f09 | -13.3061 | -46.9363 | 2026-08-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 3137cdef-eafe-3dad-8e71-1c2a413923de | -12.9221 | -45.8582 | 2026-08-29 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f7079258-d16e-36bf-a845-515184ffef21 | -14.4193 | -52.5625 | 2026-08-29 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cffbab58-c6b5-3131-98a8-4435b0f8e4c2 | -20.9414 | -57.5484 | 2026-08-29 13:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 157.5 |
| 0f02fa77-75f9-3e98-86c4-27d25075a45c | -6.7884 | -55.6635 | 2026-08-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 5f68d206-a0ac-38dc-a706-4300ad3318f5 | -13.3258 | -46.9107 | 2026-08-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 227bbdac-a7b9-32ad-857b-78ece87902c3 | -14.1835 | -52.8456 | 2026-08-29 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 126310cd-1b20-3781-a55d-c04d0fa053b8 | -8.5968 | -54.7957 | 2026-08-29 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 9ae25d5f-2af3-3f98-a03d-e97522f8a772 | -7.495 | -55.3262 | 2026-08-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 688f4319-7d8c-3a69-b210-a051ce90f875 | -10.8215 | -50.6519 | 2026-08-29 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| b02af4da-6375-3d98-a4ef-b27b3010ce96 | -7.5137 | -55.3051 | 2026-08-29 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 869ac601-ca85-33d9-9277-f26641f4993c | -10.8804 | -50.4965 | 2026-08-29 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c70c1440-df43-384c-9a11-95f103971381 | -14.2027 | -52.8432 | 2026-08-29 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| bfe9b8a5-d533-3e5b-b827-44f614aea26e | -14.4057 | -50.0537 | 2026-08-29 13:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| bcaf9b85-9722-3a14-914b-421fab3c4ff4 | -8.9428 | -63.2797 | 2026-08-29 13:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5b50bf95-c392-3097-aab5-9a3d46b09eae | -20.9211 | -57.5513 | 2026-08-29 13:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 1df596c4-b75d-38ad-b196-6eb06f3823ee | -11.7028 | -47.6129 | 2026-08-29 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 8a974cfb-546f-36b9-8a5f-412c9b357e23 | -8.9428 | -63.2797 | 2026-08-29 13:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 2ba983b7-ce7a-354d-ade3-5344af2e6ce9 | -6.6317 | -43.73 | 2026-08-29 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 287.5 |
| 6a4f2ca1-7203-3a00-bfa8-a65d8c0c55bd | -10.8215 | -50.6519 | 2026-08-29 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| acfc2993-9f33-3842-87f3-61489ee01ae6 | -8.5177 | -55.3039 | 2026-08-29 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 541eb070-beb5-3482-b93f-0faeac213768 | -9.971 | -53.9214 | 2026-08-29 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 276.3 |
| b3325f6b-41db-3be8-aa2e-29a4ce5743a8 | -8.9613 | -63.279 | 2026-08-29 13:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 102.5 |
| b186d181-1e50-3b32-8b0a-d3775756cb90 | -6.77 | -55.6445 | 2026-08-29 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |


[Clique aqui para ver as próximas entradas](README78.md)
