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
| 9f2adbcd-23d8-3be0-ad22-6fe1799c3760 | -12.4345 | -58.392601 | 2026-06-22 00:56:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5c52849-ed9e-3a90-a270-fecc37fa4f5c | -6.5094 | -44.6847 | 2026-06-22 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| bfc8d0f2-3492-39a6-b42a-84cb86d8b6cf | -6.5092 | -44.7076 | 2026-06-22 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| fff4e001-27a6-3b3b-9c85-6e14c3485ee4 | -3.5228 | -48.0383 | 2026-06-22 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 9e9c7f83-6822-39dd-a5bd-b859e59585d0 | -6.5094 | -44.6847 | 2026-06-22 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 623b7786-07de-3e27-a146-9e890da31ec9 | -18.0019 | -50.436 | 2026-06-22 01:10:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 38cb7e18-07b8-32b8-96f8-dda43f59c171 | -10.5634 | -46.2362 | 2026-06-22 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a98a8086-e0ad-3c64-8713-548a101dbce2 | -17.9819 | -50.4396 | 2026-06-22 01:10:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a965a28c-9daa-35bb-ac51-d0b308ca1961 | -6.5092 | -44.7076 | 2026-06-22 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 803c6ac9-20d4-38b2-95a9-d2a9fe0eba02 | -6.5094 | -44.6847 | 2026-06-22 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 9abb48db-c9c2-32de-9ebf-e3157e9797a2 | -6.5092 | -44.7076 | 2026-06-22 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| fbee427c-5356-34dd-8485-6440630d560a | -11.0506 | -52.476501 | 2026-06-22 01:21:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec37d739-6576-34a4-8bdd-a9ad9e415df0 | -11.0859 | -54.1325 | 2026-06-22 01:21:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a909090-e819-3d17-9ab0-3cb6eb7f8881 | -11.0409 | -52.478901 | 2026-06-22 01:21:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc6d170e-94d3-3f3c-90bc-1475cec03ef4 | -12.2141 | -57.285099 | 2026-06-22 01:21:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b386e11-39a0-3a4d-aa70-46a15a954aa1 | -12.4274 | -58.401402 | 2026-06-22 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4f54a44-1af6-3ba5-8b35-c4b0a661a2e3 | -11.0883 | -54.142399 | 2026-06-22 01:21:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2623aaad-e9ab-3768-8f6b-532087eec2f0 | -11.0981 | -54.139999 | 2026-06-22 01:21:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad1c9694-6f80-38c8-9c9e-b73de492172a | -12.4258 | -58.394402 | 2026-06-22 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25d9caad-ee4a-3a78-8da8-15d049edd7d7 | -10.5595 | -46.2257 | 2026-06-22 01:21:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c25733e5-9fa0-3496-b0bf-f28454a19d34 | -11.1005 | -54.150002 | 2026-06-22 01:21:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82189745-5753-3c99-ac9a-d02144188404 | -12.4192 | -58.410599 | 2026-06-22 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9772eabc-a894-3bd9-b93f-69c8d7d16298 | -11.0957 | -54.1301 | 2026-06-22 01:21:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 529ca04a-11bd-3fb8-a924-93a9749e1c7f | -11.0474 | -52.463799 | 2026-06-22 01:21:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb872134-698f-3491-bbbb-2abc9d938dad | -11.1078 | -54.1376 | 2026-06-22 01:21:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89a59c51-1d06-3c91-a05c-fa3624634931 | -12.429 | -58.408401 | 2026-06-22 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eedfbfab-5717-305f-aff0-a5c6c5edb36c | -12.2125 | -57.277901 | 2026-06-22 01:21:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c500725-38e0-33b8-940c-8c9548494317 | -12.4176 | -58.403702 | 2026-06-22 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83a3dbd0-bb91-311e-8652-c4947548b702 | -17.976601 | -50.430401 | 2026-06-22 01:21:00 | METOP-C | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6bb22fed-1a29-39fd-823c-3a89b22c216c | -17.9863 | -50.4277 | 2026-06-22 01:21:00 | METOP-C | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fff0a7f6-4e65-30e6-b7e3-cbf007c2aa88 | -3.5228 | -48.0383 | 2026-06-22 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7adcab38-3d94-33e2-b8ac-84cda5e32c3c | -6.5094 | -44.6847 | 2026-06-22 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| cd272784-d574-311d-b450-1832173e21a7 | -3.5228 | -48.0383 | 2026-06-22 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 769c15bf-1af3-330f-b23d-599d2d479e54 | -18.0019 | -50.436 | 2026-06-22 01:40:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ee288bc9-0470-3de1-a53a-70a831825e76 | -6.5094 | -44.6847 | 2026-06-22 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 4b755d98-c276-3836-b1da-705a60b05a4b | -6.5094 | -44.6847 | 2026-06-22 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 31a4e2b7-82df-351f-a765-3ff74dff855d | -10.5634 | -46.2362 | 2026-06-22 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 48b5bc87-864d-3580-90e4-5ee4a85415d0 | -3.5228 | -48.0383 | 2026-06-22 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 28dd4120-6bec-3e02-b255-f7235459b3be | -3.5228 | -48.0383 | 2026-06-22 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1736297d-488a-3228-8acf-3a1fa90120af | -6.5094 | -44.6847 | 2026-06-22 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 90b780a2-07d9-34d4-940f-57c593edffa1 | -3.5228 | -48.0383 | 2026-06-22 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4667f138-090d-3a45-9a8d-79838081b263 | -3.5228 | -48.0383 | 2026-06-22 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0aece6e0-6af1-38a4-9bcd-6718a1228b2f | -3.98185 | -39.81135 | 2026-06-22 03:28:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f8d8fa6e-32d6-3123-a1f6-aa2a8f7314f8 | -3.98695 | -39.81211 | 2026-06-22 03:28:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93c68ffd-736c-3d92-8730-812de8c09f5b | -9.08225 | -44.75787 | 2026-06-22 03:30:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a533eaf5-4761-3978-8562-d6ea1456f128 | -6.50836 | -42.21998 | 2026-06-22 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 2c6243f5-319b-3313-b129-2db0ed5868a7 | -6.50612 | -44.69439 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 22566b39-1ea8-3d6b-8407-06ffc82dff0d | -6.50984 | -44.69422 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7413a282-4072-3d91-8a88-eb6d17b540e7 | -6.50206 | -44.69892 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| d6be5f89-0edc-397b-8a40-4a5e279917fe | -6.50863 | -44.70062 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 41ee907a-5ee2-34bb-84bb-562b38b0c9fb | -6.50612 | -42.23268 | 2026-06-22 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 016017ae-c413-3f56-bed9-acc5f9646838 | -6.50326 | -44.6926 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 24376851-f3d4-32cf-ae01-97bc3b4b0a67 | -6.50747 | -44.70673 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6b9069ba-ccfb-3962-8d30-c92ca6cf99f4 | -6.50494 | -44.70086 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 39c3311d-d730-317d-9d57-3f1dadee764a | -6.5115 | -44.70267 | 2026-06-22 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08cdc448-e815-3dca-b07c-c1ec42fd6307 | -7.14173 | -34.99335 | 2026-06-22 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f4595ad8-926b-3333-96d8-f55756beca21 | -17.2198 | -43.68132 | 2026-06-22 03:32:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4d6b5f42-3346-396e-ad24-d298785c4b55 | -10.5521 | -46.24717 | 2026-06-22 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e1167fe-76b9-3fd5-b984-cc13d4cffca9 | -13.2983 | -45.22826 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 617fca4b-ff3a-351c-93e6-e4b533bd3242 | -16.02588 | -43.4199 | 2026-06-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f829f0b5-03a6-3556-92f2-8fb1a86b8388 | -13.2956 | -45.20721 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21d099f7-52b1-3b6c-941d-ffb7e5627e60 | -10.5588 | -46.24918 | 2026-06-22 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f525dbf-7586-39dc-8eb3-b983e4508903 | -13.29149 | -45.19635 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bc42171-6d2c-3eb5-ae64-573778fffc08 | -12.85139 | -44.39507 | 2026-06-22 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43b433a6-c602-3042-bcb3-d70a22b7308d | -10.90932 | -46.32032 | 2026-06-22 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 78c9835a-0517-389b-a3b9-5345b496ddc4 | -13.29617 | -45.20724 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deb56926-b178-38a5-a814-730758fea209 | -10.5603 | -46.24178 | 2026-06-22 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 256c2dbd-e69c-3512-875a-0d3df26c9714 | -16.02521 | -43.42327 | 2026-06-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28633d94-19d4-35fd-b08d-d12fb45c9cb1 | -15.72702 | -41.35748 | 2026-06-22 03:32:00 | NOAA-21 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5b205e4-a390-3356-9521-32ea2daf1e45 | -13.37093 | -41.35178 | 2026-06-22 03:32:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64402386-333d-3c31-828f-184fb905d91f | -17.2205 | -43.67793 | 2026-06-22 03:32:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 682094dd-c0d6-3692-b0fb-d98e21426295 | -13.30547 | -45.22444 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 356bc506-dbb8-31c7-9592-a6445d5d1179 | -13.3003 | -45.21838 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 449c95a0-8b77-389d-b81f-81e6cdda16c2 | -13.292 | -45.19633 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe12fee9-83f7-3fe9-ba5a-013344aaa5c3 | -13.29966 | -45.2183 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a86664d-17dd-3a48-97db-fd63dfa627ea | -13.3048 | -45.22432 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7938d555-d6b5-3d06-9729-bd035d12a32d | -12.85049 | -44.39948 | 2026-06-22 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc97808d-f4fe-3417-927e-d0122e032851 | -10.56167 | -46.23503 | 2026-06-22 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 866c2f2e-5648-3b78-b7db-7074a037fc4f | -16.03043 | -43.42437 | 2026-06-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a15e8b5-5076-36d2-af15-fd8c46f4a5d3 | -16.03111 | -43.42099 | 2026-06-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cfcc2e7-f2f8-369a-9ff6-1ea56350e75e | -13.30447 | -45.22935 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eaa57a68-0f91-3fc3-85a2-d4eb854bf159 | -16.02656 | -43.41652 | 2026-06-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03756d3b-1201-3f89-ac0c-50ec8b2ca76d | -13.30378 | -45.22921 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3dcd859d-34db-3113-9c6b-a1f766144440 | -13.30071 | -45.21332 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d96d493-7286-3a1a-9f11-5382b7f2e823 | -10.56843 | -46.23672 | 2026-06-22 03:32:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fa8460f9-057d-33da-9931-aba858a557f3 | -13.30131 | -45.21338 | 2026-06-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc09fcfa-12e5-32a7-b873-67100451ad3e | -15.38834 | -40.8241 | 2026-06-22 03:32:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d621d3f3-1a4a-38af-9131-4ac46cf5d131 | -20.15634 | -40.87822 | 2026-06-22 03:34:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6e012489-2a9e-311c-b8b3-54662d1e4a8e | -7.9616 | -47.4287 | 2026-06-22 03:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| df7ba13d-70d6-3bc0-8055-acbb55e1962c | -7.9616 | -47.4287 | 2026-06-22 03:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1c2fe10f-53b3-36cd-89b7-e6cf910101ad | -7.9616 | -47.4287 | 2026-06-22 04:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| bdc52f67-e74a-33f5-b5e4-32709fe95a15 | -6.23829 | -48.53075 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 51887ec8-c142-387d-9572-9ecde307d418 | -3.51593 | -48.04893 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d070194d-62f7-3b8a-94d4-9897836da342 | -3.50379 | -48.05111 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94122232-3226-3e39-bc8c-464ae804a4c3 | -6.23564 | -48.52811 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c21cb2f-2777-366d-947a-f0c216178cf4 | -3.35569 | -43.16997 | 2026-06-22 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8262ae4-c535-34c5-8973-713f2fb3b168 | -3.5109 | -48.04385 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccc9b51e-7b1d-37c0-81bb-66ce2917ee83 | -6.24145 | -48.52822 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac2a0fda-ff0d-3c61-9176-3f14fb284299 | -6.24023 | -48.53497 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f1eafa5-2087-3903-afbb-82c3cb215f3f | -3.50953 | -48.052 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
