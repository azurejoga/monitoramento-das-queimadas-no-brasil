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
| f968295f-afc9-32e2-854f-97de6a00ef78 | -13.8864 | -54.6519 | 2025-06-12 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6b9e5adb-5d18-3a0d-80fb-d0ade52f36d6 | -5.50029 | -35.5841 | 2025-06-12 03:08:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c98fe15-3f5e-3ff6-810b-521b87ce5a2b | -13.2989 | -57.0734 | 2025-06-12 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| cf9e26ab-2ce9-3469-b2ec-489b0e020f44 | -13.9056 | -54.6498 | 2025-06-12 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 5fecd14f-e514-3372-9453-c281210aa980 | -13.8864 | -54.6519 | 2025-06-12 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 14700c8b-03fd-36c4-b3c6-2ce290b1781f | -13.32923 | -40.30815 | 2025-06-12 03:10:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f89d34d2-f087-3b4d-bab2-f06344d20047 | -9.04971 | -40.66614 | 2025-06-12 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 86dc9c92-9872-3d8c-931c-5fd336cadcc5 | -8.52339 | -36.2083 | 2025-06-12 03:10:00 | NOAA-20 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4e30c8e8-4f57-3b41-abcd-df084ad0c917 | -13.32996 | -40.30922 | 2025-06-12 03:10:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 646bfa9e-ecab-3072-a976-9ff5b1731963 | -9.0524 | -40.6693 | 2025-06-12 03:10:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 39ede79b-5e35-30b9-b063-ac5849ba09b0 | -13.03925 | -42.00568 | 2025-06-12 03:13:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 13cfc41c-d74d-34f8-bb90-fc6bf9e92a4a | -17.28472 | -42.66557 | 2025-06-12 03:13:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c3b881fc-73fd-3a13-aa8b-72e6b6176509 | -13.03786 | -42.01225 | 2025-06-12 03:13:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 344d0fe2-e2af-3461-aadb-2b1b247c9bca | -13.9056 | -54.6498 | 2025-06-12 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 4012aa38-6d81-3581-9abb-e3d93eeb348f | -13.8864 | -54.6519 | 2025-06-12 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 052fe00e-5661-34cd-bf33-7586e728a957 | -13.2989 | -57.0734 | 2025-06-12 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 86d8b410-1e59-3793-bc4b-d0a0c626643c | -13.8864 | -54.6519 | 2025-06-12 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 6f544b22-03ad-300f-a330-a07e1040ed8f | -13.9056 | -54.6498 | 2025-06-12 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 050c8438-2e6a-36c0-9379-61d275a40c4e | -13.9056 | -54.6498 | 2025-06-12 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9f98cbed-2dc1-39a9-8e30-bd26e364e367 | -13.2989 | -57.0734 | 2025-06-12 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 3dfb3b5c-e3c4-3a50-aa0a-e5ac0aebf02e | -13.8864 | -54.6519 | 2025-06-12 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 95f699cd-d778-313e-aaf5-e965a06bc172 | -13.8864 | -54.6519 | 2025-06-12 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 82e5aae1-140e-34e9-a4ae-500f82b3f695 | -13.9056 | -54.6498 | 2025-06-12 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7e2c551f-e660-39f3-a363-b81dd07c256b | -13.2989 | -57.0734 | 2025-06-12 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2dec4f36-12a1-30bf-a7f5-5aa87b94b560 | -13.9056 | -54.6498 | 2025-06-12 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5097e28c-b216-3f77-8bf8-64048e29f04f | -13.8864 | -54.6519 | 2025-06-12 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e85577db-77a5-3983-ad8e-9d57f7a2886b | -3.77788 | -41.6084 | 2025-06-12 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 507aedf5-8fa8-360d-a5f0-260546078bc5 | -5.06549 | -43.72612 | 2025-06-12 04:00:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 25ff1de5-87e3-39e8-91ef-09555fce790b | -5.50409 | -35.58357 | 2025-06-12 04:00:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11a8ca37-e317-3e73-bf4a-1d0fa322a380 | -5.06927 | -43.72669 | 2025-06-12 04:00:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 76db1da5-ddb9-3c46-a113-17a62b19f938 | -5.21372 | -43.31738 | 2025-06-12 04:00:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f2fdea0-05e9-37ed-b540-248485da545c | -2.87344 | -40.02426 | 2025-06-12 04:00:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e3996ab-f882-3355-bd49-c415d9e49af1 | -5.50073 | -35.58619 | 2025-06-12 04:00:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f6427998-3520-3b0d-80c7-0ba8594b1941 | -3.77099 | -41.60733 | 2025-06-12 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| edcc43ec-8fff-34b7-bafa-af6be269feb1 | -3.77443 | -41.60787 | 2025-06-12 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a18866db-db0c-3070-a6fa-12b9bf4501f3 | -4.98257 | -37.40301 | 2025-06-12 04:00:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2551625b-ec46-3139-8eb6-b8c87c55aa16 | -11.56677 | -51.3066 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ba898fc-1668-331f-abfa-f7968ad5b372 | -10.65377 | -49.4211 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9b7fc18a-6c7c-3099-a79c-9d03bdbb5f39 | -6.68858 | -43.68813 | 2025-06-12 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc9493d0-6d4a-3d46-ae1f-72ba357b5ed3 | -9.85518 | -47.87865 | 2025-06-12 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6bf710a-e1a3-372b-9698-b1171f9e291b | -11.00979 | -47.76287 | 2025-06-12 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f3a868b-9093-30d8-a4d3-8272a53ac31b | -11.8448 | -43.80358 | 2025-06-12 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e22f2c33-1166-355d-b77d-7dd320006c61 | -7.01275 | -44.61496 | 2025-06-12 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45ef3bed-280a-3dc9-b53c-50f7fd58a95a | -10.19809 | -49.59237 | 2025-06-12 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dfb47bb-67b2-377d-8714-e1915af984d2 | -11.13686 | -53.94431 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3526b5d-a4c6-348b-b56c-34652c592324 | -8.66432 | -47.13744 | 2025-06-12 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e65d1097-a0a0-3b75-917c-80c6ab4d1a5c | -9.39971 | -48.43064 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1adb19c5-83fe-3856-a144-cb333b607bbe | -9.40035 | -48.42865 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6360e670-4fa4-3407-8f88-fa451bfb94a7 | -12.38278 | -45.77487 | 2025-06-12 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b0810c8-1476-3c6f-8381-fd5f36e4675c | -9.40515 | -48.42948 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0dac66f5-3db9-3fe6-8763-4383c3ae3fdf | -11.13931 | -53.94279 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf372b5a-0f07-3ba8-b91f-43440746940a | -10.65878 | -49.42205 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d203c895-1187-3e32-a026-4273f35e2d17 | -9.40548 | -48.42616 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e672e3c-0c82-3238-a9f2-7b32a37d5768 | -11.5754 | -47.43877 | 2025-06-12 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 51003450-0feb-3fee-b403-ba09a83a0a82 | -12.10895 | -48.87453 | 2025-06-12 04:02:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ba807ba-0052-382d-887e-361123f015ca | -6.94391 | -44.5663 | 2025-06-12 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84165094-357c-3f21-bfaf-0542b55aa10f | -10.87525 | -54.74748 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 640b9931-ce3c-37cd-b909-f8823e20c7dd | -12.38363 | -45.77002 | 2025-06-12 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfd5713c-5417-3c41-bca8-0e9d14b3bb26 | -6.6808 | -43.759 | 2025-06-12 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39f89ba3-4e65-32b5-8978-0030751094fb | -8.96939 | -47.97046 | 2025-06-12 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14970f45-f933-381a-8af1-bf7fa1a4f667 | -11.33768 | -45.22298 | 2025-06-12 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c1feed6-8c2a-3518-9f7e-ab03fd410058 | -10.7003 | -49.50638 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 161b13e9-b8a4-302f-85b3-22c567cd1204 | -11.77771 | -47.40128 | 2025-06-12 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b3a9a34-4661-38e2-ae38-d5e1243e36aa | -5.77936 | -43.62027 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b42d10c-ce5b-3c41-ae37-fb58b1058695 | -10.86389 | -42.25112 | 2025-06-12 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f9616940-12d8-356d-8a82-2020da45efdd | -11.57304 | -51.304 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5236348-3b85-3888-9a1e-7f50ebf5c4be | -10.88357 | -54.7452 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 71f1bb62-feae-3b0b-bab7-56888a5f8836 | -7.0109 | -44.61736 | 2025-06-12 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129e7681-4a8d-36b3-9e0c-b7b6f6ebe318 | -5.64846 | -43.60199 | 2025-06-12 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1441bc60-5539-333a-8569-7140528ad809 | -9.60723 | -48.54212 | 2025-06-12 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4da3ec6-be6e-30dd-abe6-7a57a747d763 | -11.61171 | -46.98947 | 2025-06-12 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 175128bb-3b63-3255-bd4d-84c2edd1a609 | -11.57067 | -51.30885 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06c657d8-a278-37d3-bca0-b39476291181 | -6.94472 | -44.5615 | 2025-06-12 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbc1510f-6bf3-3f17-9d2b-68e229231f60 | -10.24033 | -52.23536 | 2025-06-12 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 291b45d3-6096-3f09-aa26-7b61dcc51fb2 | -11.57234 | -51.30773 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8628cca3-7fb0-3d50-8160-9d55f116ee5d | -10.8822 | -54.74876 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8f2a9ce9-0136-30bb-9652-fd098426e402 | -11.84131 | -43.803 | 2025-06-12 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f3082f0-2352-31b4-b58d-b9b2588bfcd7 | -10.86942 | -54.31945 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3df81e9-eca0-3a22-8a00-1d9469368d81 | -12.35184 | -38.19474 | 2025-06-12 04:02:00 | NOAA-21 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| da97f1a5-fbbc-347d-97b7-ee559bd47ff4 | -10.03722 | -48.78083 | 2025-06-12 04:02:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f34127f-cc71-3f01-8a8c-349a03378c8b | -6.13215 | -39.44757 | 2025-06-12 04:02:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 54d636f0-1afb-3752-aa4f-34bc796ef980 | -12.23514 | -44.16241 | 2025-06-12 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a8e8ef9a-b60c-3035-93bd-1a7ae2383bb2 | -10.88218 | -54.75205 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2ed5a0f9-bee1-333c-9d8c-6e8aea535f10 | -10.63068 | -49.43534 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29466b3c-82e3-3dd8-b7c5-83b228102788 | -12.05517 | -48.07565 | 2025-06-12 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c5d6f60-0f1d-3d2a-9216-661cfc0a0c2f | -9.85059 | -47.87793 | 2025-06-12 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3660e91-d913-3f02-a4b6-f265cfc5baab | -10.69922 | -49.51229 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a43d1d61-8c50-3257-a053-3df93674ed18 | -8.95277 | -47.28209 | 2025-06-12 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f71cc88-abe3-3ffd-9bf4-878a0cafca26 | -11.57162 | -51.31149 | 2025-06-12 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d20e7bcc-f358-39e7-9259-239edfaf3f83 | -11.01211 | -49.57969 | 2025-06-12 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee24faf0-bc22-307a-9ca2-f7100d29f4d2 | -10.65052 | -49.43846 | 2025-06-12 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9275c63d-addd-3760-b22f-37fb6ccb1aa5 | -10.86266 | -54.31808 | 2025-06-12 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ac5a8d1-d10c-3ac5-a447-5fad2df23a40 | -9.05641 | -49.5187 | 2025-06-12 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04ffcbb3-fa47-3dab-a50d-943b279fd1d3 | -7.24026 | -43.10894 | 2025-06-12 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d6b1c438-7893-3672-875f-e3025cf793ab | -11.96101 | -46.9425 | 2025-06-12 04:02:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a9d8244-987f-3a2a-ae3b-4fd0a6382adf | -11.62829 | -41.8337 | 2025-06-12 04:02:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7b29c7d5-857e-3dec-8624-10c3d1d6b4f5 | -6.94858 | -44.5621 | 2025-06-12 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4fd8048-a65a-30f9-a222-43cf37de1e7e | -11.06487 | -38.43703 | 2025-06-12 04:02:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 657a2d50-3bbf-381b-9024-1ec5e77cdaca | -6.60284 | -44.25925 | 2025-06-12 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1a585ba-ef32-3d6f-9d85-32f8d69ba430 | -10.69867 | -49.51528 | 2025-06-12 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README7.md)
