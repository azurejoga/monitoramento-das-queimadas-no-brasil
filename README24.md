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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3dd827a-a087-3532-9d7f-8629f11ee793 | -25.97246 | -48.95401 | 2025-07-19 04:40:00 | NPP-375D | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 95386b40-a37b-3691-b1fa-0bfab4b1b5fa | -23.32743 | -50.13153 | 2025-07-19 04:40:00 | NPP-375D | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9f208b37-4b69-3ddd-82f3-855f8485fc7f | -25.98587 | -48.95879 | 2025-07-19 04:40:00 | NPP-375D | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a629654-41ac-39c8-8913-d8693246794a | -27.53388 | -48.65725 | 2025-07-19 04:40:00 | NPP-375D | BIGUAÇU | SANTA CATARINA | Brasil | 4202305 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7129f5e6-fc7f-331b-84a8-b9d84d5a97b4 | -6.7899 | -42.9917 | 2025-07-19 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 6f9c1eba-db1b-3faa-b08b-824e80214d06 | -11.7317 | -48.1849 | 2025-07-19 04:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 5fc15b90-1816-3c39-9dba-0ad0b54fe481 | -5.6567 | -43.7161 | 2025-07-19 04:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 48cfdb77-b049-3340-b326-1bdd940a0b37 | -2.9108 | -48.254 | 2025-07-19 04:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d7535562-b4ad-3e82-9b5b-2e3e03b6645c | -2.9109 | -48.2325 | 2025-07-19 04:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d9d7046a-be34-348b-8225-4fa901c6d071 | -3.39346 | -47.48002 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56fd627a-2a0d-3ee5-904e-fd7b3e86d26e | -6.979 | -42.80688 | 2025-07-19 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 37b85c19-f016-3387-ae2b-a797fdc5a977 | -3.57386 | -49.50163 | 2025-07-19 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6b0af7e-314b-345e-a619-be9a911c81c2 | -5.66091 | -43.71718 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1804485d-d10b-398a-9910-4b5a04bd01e7 | -3.82735 | -47.74072 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1fed8e12-93a3-3ec1-9c52-78f1baebdeb1 | -3.11831 | -47.01514 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f8f16ae4-7885-347e-8060-a8fe9bbaf1df | -5.75021 | -46.18937 | 2025-07-19 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c6458d9-31e2-3fd9-87aa-1332fa308e75 | -5.88546 | -45.1988 | 2025-07-19 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a07c8916-9b02-393c-b665-44b8c6ecec7d | -4.81907 | -47.32103 | 2025-07-19 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21ab018e-9321-3f97-9807-013fc2c39765 | -6.15923 | -43.75214 | 2025-07-19 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3da07f94-3e33-3ac3-bab2-ca49203e5911 | -6.16827 | -48.05538 | 2025-07-19 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2c401d69-6e15-3e13-8765-34a8efa81b13 | -3.13692 | -47.01336 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 267fa122-359f-3cbb-8eaa-e7fab124afad | -3.5268 | -51.57959 | 2025-07-19 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 50be752e-8ed1-33e4-82de-9f256bb2d4b8 | -6.16452 | -48.05047 | 2025-07-19 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ccd7f991-ca32-3fef-9f12-6fefe42cc48e | -3.39459 | -47.47871 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14dd6a11-4b9c-345b-bf33-4fa7a93f252e | -3.36083 | -49.16472 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a57439c1-f872-3136-99b0-379bae1f164d | -2.44774 | -47.33261 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cc8cd76-23a3-3d15-9e35-af0d05518f3f | -4.77996 | -45.349 | 2025-07-19 04:55:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fced6029-51f3-355f-b0e8-2f7392679253 | -2.90744 | -48.24784 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f045755c-fd43-3915-b267-ecde64bb7dd0 | -6.1689 | -48.05104 | 2025-07-19 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b616a1b0-4d87-30b5-bbcd-12b6734071c6 | -4.02926 | -48.0668 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cf4bf72-da60-35e8-b4f6-b8e617203519 | -6.15733 | -47.76534 | 2025-07-19 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e065e189-f064-385a-a840-6c40ded374bd | -6.15866 | -43.75623 | 2025-07-19 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd81d455-1658-310f-b0c7-fe0a185fd44b | -3.3878 | -47.48775 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2442492-a6aa-305e-9e07-6f557b3e71d8 | -3.39281 | -47.48419 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f1402e1-512d-3956-b8c6-91ceab164809 | -3.06224 | -40.04315 | 2025-07-19 04:55:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1dcde695-efd2-3e48-a709-dbb659774d68 | -5.6545 | -43.7204 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a444ef39-ffd7-3aff-bbf0-63bd0b8373ce | -4.12855 | -47.65482 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b92ffe1e-ff70-38e6-a0a2-d3fd8247d0ef | -5.64231 | -43.72255 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e11b110d-f03a-37a5-8c26-3996cb4fdde8 | -3.04024 | -49.4235 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3af7b795-88f5-39b4-8b0b-9c3d7db59516 | -3.13523 | -47.01156 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e899970f-f489-36d7-922c-a407ffe2122c | -2.9121 | -48.24482 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| dff11623-6bfb-329f-afe5-e983e3bd396a | -4.25139 | -48.54773 | 2025-07-19 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 330443b3-18d1-317d-8895-ee8a9a134c9d | -2.9039 | -48.24353 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 6d50aae3-78f9-3e65-9909-5369fa91fd13 | -3.95121 | -49.44377 | 2025-07-19 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c19eefd-d333-3849-a8f5-38b8004d2774 | -3.12279 | -47.01581 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 114fbe71-1946-3b5f-8157-4fc40b921dff | -6.78264 | -43.00179 | 2025-07-19 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 1e12e0d3-379a-36e6-8e1b-79214944c376 | -5.64924 | -43.71161 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c116844d-b003-3e0d-a293-c0e18c3b62ce | -5.53034 | -43.88116 | 2025-07-19 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0db48683-9def-3e13-91e3-6b4bd996aa46 | -3.38909 | -47.47942 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70e0ab19-5d1d-3bea-a872-1bc0001ab260 | -2.44098 | -47.32967 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| affc2d79-62fc-3bad-ad96-e78014432dc0 | -4.11036 | -47.92847 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a657f95-834d-3f1c-9f1d-28a636259537 | -2.4434 | -47.33194 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08919486-9792-3008-a259-91be111a2406 | -2.91267 | -48.24115 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b58b58e4-f869-3ac1-a1b2-a1157b2c145c | -3.67921 | -49.57312 | 2025-07-19 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f780db3-5220-358f-98a6-b481359ebdd6 | -5.65449 | -43.7167 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4732949b-8aa2-39f3-b565-3b540f1af666 | -4.87168 | -47.76168 | 2025-07-19 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00d95e56-bb52-3bc8-869c-2ad86c93a30a | -2.92503 | -49.07288 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| febbdb12-51a5-30c8-b7dc-164947705a10 | -4.25549 | -48.54834 | 2025-07-19 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c6555a0-c24f-3cc1-9fa7-a8ec79e4db6c | -5.6487 | -43.71942 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4f4e1d84-806a-315a-83dd-9c234f764a42 | -3.38961 | -47.48228 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6985af77-232f-3656-8416-f0f787732b82 | -3.13457 | -47.01603 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0f534834-cd18-316c-a103-271b89e4cd35 | -3.96613 | -48.89767 | 2025-07-19 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bc8d08c-fb02-3452-a9b7-21cc5c878a8d | -6.97271 | -42.80606 | 2025-07-19 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d4554be-c371-3c90-a185-1ca36ca9b17a | -5.66031 | -43.71764 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b7b7b34-c3e7-34b4-8b23-e514c217b12b | -3.57314 | -49.50631 | 2025-07-19 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 768ec99f-c067-3d62-a936-60f8847423b3 | -3.39022 | -47.47809 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72f04a3e-f7a0-312c-8b33-e03942afd4ff | -3.12796 | -47.012 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 539af60d-3196-3501-9b37-f9c9d2f5ac4d | -2.74446 | -48.25053 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abba05b3-f88d-3e6a-8763-a81c0726d5da | -2.91621 | -48.24543 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 089750e2-8835-3b6d-a0e1-627ec927dfd2 | -5.18558 | -44.95443 | 2025-07-19 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0dc07f3-1c18-3df0-b9e4-f4a6a68d725c | -2.91154 | -48.24847 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e81e0a49-570b-31d6-a5e0-485f7fce48eb | -5.66031 | -43.72138 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 527df06b-87ce-3507-a356-5efabf70f3d5 | -6.16015 | -48.04984 | 2025-07-19 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b4b46710-e15d-3f75-8819-999f76e29022 | -5.75081 | -46.19477 | 2025-07-19 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1c401a7-5c51-344f-9d6b-3344f116b3ac | -2.63248 | -47.3061 | 2025-07-19 04:55:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0669651-2d76-35b2-946f-73c3cd14a04d | -5.64812 | -43.72345 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bb535a06-73b9-3ec4-a126-5b9129b01497 | -5.88015 | -45.19811 | 2025-07-19 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 944a9e15-8260-34c1-ba98-b58699b560c5 | -3.03952 | -49.42819 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4354d832-c604-3e24-ac76-220e4ccf7174 | -5.65393 | -43.72082 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 704759b3-5cc9-318f-8c4f-1bd9f2cbe8b9 | -5.74941 | -46.19477 | 2025-07-19 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e9ddbe4-207d-3d0b-9ed6-df2263011653 | -3.83165 | -47.74143 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4cd88548-81da-341b-9bdf-a824c2f24656 | -4.12777 | -47.65151 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cede9601-8f51-39c2-b248-61ab42e40f80 | -4.82191 | -47.31863 | 2025-07-19 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42634bec-7905-38c9-86bd-d0ea80decb41 | -3.39781 | -47.48065 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7ef7f0-0569-307b-be44-f28ac4a84bb4 | -3.61565 | -43.54239 | 2025-07-19 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2abc553a-c84a-34b0-b9b1-21635e32bf5d | -3.58758 | -48.94106 | 2025-07-19 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c2bc6ce-34f4-3760-a2ee-7f619f3360d9 | -2.58635 | -51.92287 | 2025-07-19 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8b096f1-1d36-3fe9-a8dd-4860008b65a1 | -5.64988 | -43.7112 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6e260b69-52e0-3d02-916c-9551a9d8d50a | -5.80284 | -43.63013 | 2025-07-19 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35eadfc9-83b8-3f9c-a2e3-cca655132746 | -3.82674 | -47.74477 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 696c1e4e-b3b9-3b64-bb94-29cd04ca537f | -2.44405 | -47.32782 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80d795ff-1ef6-35a2-9ca2-fb5e5f5dfb8f | -3.50908 | -47.22437 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3312b990-2f9f-33b0-888b-36956f3b302a | -3.83104 | -47.74547 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd696415-1751-376e-b066-68b939498222 | -3.13971 | -47.01226 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a4f7a954-5720-3899-80fd-51be20d2866f | -4.87248 | -47.76027 | 2025-07-19 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad37e391-fe1b-33be-bc5c-bc813dcb0e5f | -4.31283 | -48.10759 | 2025-07-19 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 29c4313f-cf82-39cf-9533-d92ff63f97e4 | -3.04787 | -49.42467 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e10fb55-b168-32c3-8507-88533546e4cf | -3.39587 | -47.50024 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc33af8e-d3cb-3247-81dc-6006bdd0a21a | -2.44594 | -47.32619 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6494830-c7c9-356a-8a3a-9ea3da9528e3 | -3.12348 | -47.01133 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README25.md)
