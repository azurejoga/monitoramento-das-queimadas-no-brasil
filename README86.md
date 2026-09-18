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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b57d84b9-1041-3ca9-9540-687ecc453e6c | -9.71539 | -54.80829 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bedb948e-a49d-3b41-b97e-21d1f2f867c6 | -8.93701 | -51.46304 | 2026-09-18 05:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b9ed7db-c128-34eb-9614-a2f993a61be3 | -10.52015 | -46.73306 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d8811c7-07aa-327f-a9aa-12e17d43a7a1 | -9.94519 | -45.28696 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e508bb0-b2ae-3ed9-a2ed-c118d3cb4ec1 | -8.90581 | -45.01472 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 99fe2136-6130-3bb8-8ceb-22502169e159 | -9.71574 | -47.09822 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f90d9d10-3953-338e-9824-78d50d28cde0 | -12.52974 | -47.09687 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57af7be3-90dd-30be-85e0-308cdcbed40c | -9.76675 | -46.60229 | 2026-09-18 05:18:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9abdcdee-b9d6-3e07-a742-db4d43d548b9 | -12.17828 | -46.98291 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4314b6a2-19f7-3df5-a4b2-0dcf0cafbdde | -10.52337 | -46.73073 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ca21f2d-0f8e-3044-bb31-9b77c5a5bc33 | -9.75936 | -46.08421 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa981731-be35-3ff3-a358-b7c37d4951b7 | -9.94189 | -45.32381 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8594ccd4-62b3-37a0-9d4f-2e6c513b9da9 | -8.85937 | -62.39263 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deebbee3-4a70-36cf-bdb5-257601bf2ced | -8.8632 | -62.39329 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bc27154-c773-3011-a257-bf1fcb0447c1 | -9.91352 | -46.55661 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c91b4337-af83-3cc4-ad3a-958a23e57026 | -9.70608 | -54.82032 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68dbae7a-c14c-3623-9a9a-1661630d4401 | -12.56005 | -50.73286 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d6dd8ad-46ef-3b11-a61d-44244933a71a | -7.74912 | -54.74383 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98297f08-439c-3b9f-8411-0c3b0c9e104c | -11.55124 | -46.896 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5c0c8f0-8ae8-3148-ba94-dc13104ed521 | -9.15408 | -50.00097 | 2026-09-18 05:18:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3c7c1b0-d127-397b-9521-41d591ec3b8a | -9.1873 | -45.69393 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd9af8fa-12db-30e3-87b7-1b92066a76ba | -12.99524 | -46.94442 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90ad1645-8b8f-3ca9-8a93-1d5b898022b5 | -10.51772 | -46.72473 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6fa20f9-16b0-3b57-b02a-ad536424784c | -11.06633 | -48.29953 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b061e6b9-d7e1-31bd-ae68-1a6e6b4740a2 | -13.25002 | -46.91349 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08963a79-926a-34a5-a1b9-38679b28dfd0 | -10.91471 | -53.98216 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8da310b6-8582-3eda-a8a8-379716ca697d | -10.12367 | -45.56825 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 58d92c12-2a15-3e5f-bc96-fe9857526eff | -9.83359 | -49.23037 | 2026-09-18 05:18:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7f886bb-6962-3c48-97c9-615a8abea242 | -8.49763 | -57.63546 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fb8e8d6-c8a9-30e2-aba2-4e40ac5bd3d4 | -9.91375 | -46.53018 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0af0324d-4741-361a-a588-ab40b4da6f85 | -11.06091 | -48.30404 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 66cf3508-e922-32b0-a2d9-a2696f7e11e7 | -9.7503 | -46.58047 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ac72b1a-88b7-3da2-a315-9e4ae67f4cf0 | -6.92868 | -63.02964 | 2026-09-18 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68589231-5f4f-39fd-bbd0-4f2a037f91ba | -10.49403 | -46.28358 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfed6643-5639-3c66-bbcc-1c7b822f8537 | -11.00098 | -57.05684 | 2026-09-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a931708d-f3cb-3552-acfc-5d95a27ea35a | -12.16799 | -46.98659 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93c56dec-d02b-3c4b-9eb8-e0523e2af5f7 | -8.16325 | -54.82291 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c466df1-97cc-3b28-9f44-bb3009240e42 | -14.17156 | -47.85589 | 2026-09-18 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e642503-5467-3cd3-9bd0-2dc049bf0bc0 | -10.49269 | -46.29477 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e99fdcad-bb18-3852-a362-75566074033f | -9.15485 | -49.99523 | 2026-09-18 05:18:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cef40bac-83e1-3725-a914-fedd078beae0 | -13.24945 | -46.91871 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2b1022a8-96a1-3e96-9336-f4b79dfde11c | -12.56326 | -50.74333 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b388f4f-0dd1-3bd2-b952-b05ba3ac7b07 | -9.71406 | -54.81714 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f3fc10ee-43c3-3ae8-86f2-115d4f276233 | -9.54556 | -45.46132 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8999a126-93c9-3342-9c22-684623a50130 | -12.5177 | -47.0901 | 2026-09-18 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7196ce5-bb7e-3ebf-8328-c632d7d206aa | -9.75925 | -46.08662 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13e68cf1-67f2-3fe6-a912-c90b7174c48e | -12.16463 | -46.98959 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a880bf2-eb29-3b8d-a249-713daaea3687 | -10.63282 | -46.06186 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a31688e3-7ede-36e0-8dba-a3d96a77d3ae | -9.91242 | -46.56565 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 600d4f2d-ba52-3e75-a71a-e76b3f7bee6a | -10.51518 | -46.74485 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95dc3a8e-0c4d-3221-986e-88ad62867feb | -7.95103 | -54.89075 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0aacefe-e0ed-358f-99af-a9d042240d99 | -11.06027 | -48.30119 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 536aa6c3-b10f-3cfa-b150-a7fc9cd77fb7 | -10.52135 | -46.723 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 168bf62c-74c2-3632-93dc-70f100eefa3d | -6.93341 | -63.02666 | 2026-09-18 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a67ce7c-27f4-32f0-83d8-df66c07f7e60 | -8.93491 | -51.46496 | 2026-09-18 05:18:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff34755-7453-3813-a3e9-903ea6d1bcb6 | -7.74849 | -54.748 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 936db9db-1d91-3bd5-9eee-18c0b1671099 | -9.08452 | -45.72437 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e42ea16-f2d6-3dd2-ac78-76b665121ec4 | -9.70543 | -54.82467 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 17faa05d-a000-3257-ac7c-b51c2c593060 | -7.57795 | -57.69604 | 2026-09-18 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07675102-7aba-35d4-9a55-f3283dd77086 | -14.22467 | -48.50837 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecdf0512-cd79-36ea-b88e-496b03b7b787 | -11.06962 | -48.28035 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6c71c1c-7373-3106-b7cc-1eecef1e39e7 | -11.02195 | -54.15139 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27cf160f-e608-3ac7-9deb-d57142cf52c5 | -10.12959 | -45.57603 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc9f98b8-f57e-3352-82d5-bd782199e745 | -12.39627 | -50.6981 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec412531-d090-3dd1-b5ad-391714a4727f | -12.31758 | -47.95607 | 2026-09-18 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91217884-f22a-3750-a37b-265a3f549211 | -10.611 | -46.5679 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a30502d8-1b84-32ce-a7f5-c7967bf0f7f0 | -8.87915 | -45.88914 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95c49b18-407e-3385-96f5-09c2ff501b06 | -10.10774 | -45.64599 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f9a0c0df-cbe3-3b6f-a908-fe8dd73b4357 | -9.59438 | -45.87053 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7654a899-3520-35ec-9297-0e8768ad0e90 | -9.94147 | -45.31693 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74ac4815-a6c0-3b1e-b740-55970b0e6b9f | -12.26813 | -50.78432 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f7b6d6b-d480-3128-8c94-a6ee0ad82288 | -12.55827 | -50.74268 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14df9106-c68c-33e3-91e1-33290383f80a | -9.95265 | -45.69164 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c1dcdfda-18e3-3b59-836a-6fed1afc247c | -9.90986 | -46.56052 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acbe2aac-4816-3b16-b1ac-19c81c68f6ea | -9.93558 | -46.53403 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18904682-d499-3317-8881-640131c454ca | -8.86425 | -62.40108 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e70cb30-b5a2-3910-8a18-383dffbb5a64 | -8.48969 | -46.88068 | 2026-09-18 05:18:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a8c6e68f-30f5-3f15-8919-44097be608e8 | -7.94744 | -54.89021 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e382aa4-894d-3e69-9c1a-7fc10d25a448 | -13.74943 | -48.80553 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6831071-0996-3aa6-a36c-c78d17d43194 | -9.95195 | -45.69744 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b3dedb60-6567-397a-99c0-e49af6709006 | -8.1645 | -54.81459 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7aab169-1c60-3a7b-ae61-83d18177c8df | -9.94554 | -46.60936 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4245c698-b106-3766-86b2-ec714ee8f21e | -8.12056 | -54.81221 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c9e9762-5014-3f21-8e7d-3cf6a42e68f6 | -10.89686 | -53.99496 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10a19d4a-d71f-37bf-bb50-4f8ec8dc96ee | -10.49336 | -46.28922 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e8d94ad-526e-37fb-a69f-41bbd8bef49b | -14.13045 | -48.72383 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ce530ad-e04c-38a2-bc54-1951d5a185c0 | -9.93422 | -46.59721 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e4e45cb-6de0-3a25-81e2-e166a2aa4444 | -9.75862 | -46.09184 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 418e6a98-ca71-342c-b269-bd75e82ab735 | -12.17442 | -46.98648 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63a36112-3acc-37d9-8cdf-091f0c2fbae1 | -19.18916 | -48.78823 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e5800626-b9e0-32a1-befa-b4a90c3cd114 | -17.77555 | -46.48381 | 2026-09-18 05:21:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13adfad5-054e-3276-8cdb-41eaf36a722f | -14.9623 | -47.53298 | 2026-09-18 05:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4a712e4-81c6-31da-8e19-8e9e0a0503a8 | -21.4628 | -48.68628 | 2026-09-18 05:21:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 079b3ac2-4711-35cb-bfaa-8829890e6915 | -14.89161 | -48.15039 | 2026-09-18 05:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d763f049-c8a0-37a7-90ee-e672c18ccf40 | -14.89644 | -48.15668 | 2026-09-18 05:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c0c9208-37a4-38a4-92a6-32d82a528976 | -19.18869 | -48.79316 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 78730534-d860-3298-a7d3-0fbc1d9df97b | -21.0504 | -48.47417 | 2026-09-18 05:21:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21fafd74-c008-32e0-9576-b0cc49f70ff4 | -19.55307 | -47.64266 | 2026-09-18 05:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 68959ba8-cb7f-37e1-85e8-b372a4341d4d | -15.4728 | -52.87768 | 2026-09-18 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51278854-6fc0-3fdb-bd78-f05da9be4b2d | -14.71209 | -50.30791 | 2026-09-18 05:21:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README87.md)
