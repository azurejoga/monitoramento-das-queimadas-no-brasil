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
| facbb47b-31b6-32c9-ab7c-901c3c3631b6 | -7.35549 | -37.82063 | 2025-01-05 03:23:00 | NOAA-21 | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2399fcd2-71fc-3aba-944e-d8e216f6aa98 | -12.44113 | -41.75713 | 2025-01-05 03:25:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19050bc6-ed27-33e6-9397-df4a348b1da0 | -12.44182 | -41.75711 | 2025-01-05 03:25:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03e3925b-5c79-3118-af9c-5d68e9209096 | -10.2416 | -36.51205 | 2025-01-05 03:25:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c176ac1f-8431-3ac0-bdd9-efe05f2aef46 | -12.41427 | -41.48941 | 2025-01-05 03:25:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5a431073-c99a-3025-86c4-f1baecabd688 | -12.40889 | -41.48838 | 2025-01-05 03:25:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f9a1524a-42d4-3d62-b814-fa266c2f79ca | -12.44178 | -41.75375 | 2025-01-05 03:25:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2d499381-0d31-3a5d-8aff-e33b8e6392e5 | -15.45903 | -39.15051 | 2025-01-05 03:25:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff7ab520-58c2-3ad9-9fe5-6e74c31c55d5 | -11.0856 | -41.66086 | 2025-01-05 03:25:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6da2d037-3c0b-371c-b8ea-d29e34d4eaf7 | -9.49795 | -40.32428 | 2025-01-05 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7afe9c90-6c23-3cf5-94c7-f139fa17c27e | -12.41499 | -41.48571 | 2025-01-05 03:25:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a8208979-1e7c-3adf-9c38-e1f2fcb254c1 | -9.5032 | -40.32522 | 2025-01-05 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e75a7b93-6ea5-3263-bfbd-1689473e7a17 | -15.45862 | -39.15086 | 2025-01-05 03:25:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a06c4076-70b2-3e9b-b02b-cbc585e291f2 | -9.55459 | -40.31106 | 2025-01-05 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14ace85d-486a-390f-9957-6b395c913c70 | -12.4035 | -41.4874 | 2025-01-05 03:25:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a55fd435-5614-30ed-b9b9-d598590c67b1 | -12.86097 | -38.36583 | 2025-01-05 03:25:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b163102a-1ced-30a1-810e-a515028df491 | -12.05718 | -40.01345 | 2025-01-05 03:25:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4722badc-31de-3974-bee6-57efa9a52d78 | -9.54936 | -40.31008 | 2025-01-05 03:25:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d9dc3f7f-3f56-3cb1-836f-7aa1e54c5961 | -12.40962 | -41.48466 | 2025-01-05 03:25:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3bf92d75-5620-35c5-aa2e-ab00c12c4b5c | -10.24221 | -36.50848 | 2025-01-05 03:25:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6582c51d-5abb-36e2-9425-ad418a1dad06 | -6.07708 | -37.31213 | 2025-01-05 03:46:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6895efb5-b65a-34b4-ba80-918a12913771 | -6.07431 | -37.30812 | 2025-01-05 03:46:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bfbece78-2874-3a08-899e-1182b7a1b6e8 | -4.94042 | -38.72489 | 2025-01-05 03:46:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ab316f1-5ae6-34bc-b3af-e258e68c8447 | -6.81444 | -35.22415 | 2025-01-05 03:46:00 | NPP-375D | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 774e8a59-2bf0-3a03-92ae-7d8301225508 | -7.35372 | -37.81974 | 2025-01-05 03:46:00 | NPP-375D | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5e25ad5-b662-3e12-ae17-6d6023d014a7 | -6.07042 | -37.31107 | 2025-01-05 03:46:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 95c3fc1a-0b23-35db-aab8-3a6feea5279a | -4.86599 | -38.33441 | 2025-01-05 03:46:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e4adf1c2-5ce6-3425-b78c-2e10f5d937e9 | -6.0732 | -37.31509 | 2025-01-05 03:46:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 827dae5f-35f8-3c8a-be8a-4873d534574a | -4.94736 | -38.72599 | 2025-01-05 03:46:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 08d21279-edcd-3529-a1ef-5010ea61b42d | -6.07375 | -37.3116 | 2025-01-05 03:46:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a48cf0f3-d309-3e67-baed-2b2c54afd3a7 | -6.92499 | -35.0311 | 2025-01-05 03:46:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 01cf6330-0f54-3b3e-a198-4db6e72ba610 | -4.94329 | -38.72924 | 2025-01-05 03:46:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1b6aa873-4ab6-36f1-a672-dde51f5e96c1 | -7.47667 | -34.8433 | 2025-01-05 03:46:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4bf01144-fe37-3f52-ae0b-724345006da8 | -6.92557 | -35.02736 | 2025-01-05 03:46:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e94de264-4e5d-346a-a190-5bc9418dfa50 | -6.07098 | -37.30759 | 2025-01-05 03:46:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 380c62c0-fa30-39ca-aa9e-f7a728ce5066 | -4.94389 | -38.72544 | 2025-01-05 03:46:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 59ad397b-1ea8-3baa-8695-1b8ee4c7b975 | -6.07653 | -37.31562 | 2025-01-05 03:46:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f0ede175-332b-3c48-bb0c-3cc122179d20 | -6.92844 | -35.03167 | 2025-01-05 03:46:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e1c24831-9f37-3e62-b2f3-69c8332959b4 | -7.35706 | -37.82028 | 2025-01-05 03:46:00 | NPP-375D | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 98ed68d3-e82a-39eb-bac2-038f63e62800 | -4.9445 | -38.72164 | 2025-01-05 03:46:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 93c6b8e4-eb98-35f4-bacb-da45eb782b13 | -13.78712 | -39.50119 | 2025-01-05 03:49:00 | NPP-375D | GANDU | BAHIA | Brasil | 2911204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b844d910-ae03-3c40-b6ff-94adeb250e25 | -12.41157 | -41.48641 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 953d2b32-70ec-36a8-a5f6-8b61efa5cf1e | -9.39895 | -40.55857 | 2025-01-05 03:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98415d2f-f65c-3a6e-8733-38a144bc398b | -7.12423 | -40.16161 | 2025-01-05 03:49:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2db8a7dc-f28f-3d6e-bb5b-fccf43737418 | -7.12354 | -40.16579 | 2025-01-05 03:49:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8f5ba0c-fc68-3bc8-b41d-7fa3bd66f122 | -8.33325 | -35.96391 | 2025-01-05 03:49:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7b8e647c-9971-3551-bd0b-e49277758b23 | -11.08845 | -41.66005 | 2025-01-05 03:49:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46a5c4d0-de00-3ef4-bb56-e052d94d2c2a | -12.40304 | -41.49026 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac2f40d5-3b73-3c79-a122-89b6d911e896 | -7.12854 | -40.15802 | 2025-01-05 03:49:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a784acc-50bd-330b-9335-caed8ce883c5 | -12.41445 | -41.49135 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8a29d7d5-6582-3813-9060-000c12677ed6 | -12.40432 | -41.48518 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 214502d4-2dfe-3e21-be0a-306704e7f714 | -10.43849 | -44.89032 | 2025-01-05 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea780f02-5782-3ff1-a897-b2d240322ca9 | -12.40795 | -41.48579 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d473aa2c-f20d-33b9-ad94-6f958996ceee | -13.33272 | -41.36501 | 2025-01-05 03:49:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2184b9f1-bc6a-363b-834d-91f65f33fa56 | -10.43475 | -44.88474 | 2025-01-05 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c34bb5e-e24d-36bd-a318-d10575c8fb3b | -3.01617 | -39.99659 | 2025-01-05 03:49:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9ac57224-772b-3e04-8a5f-d37b3084fd67 | -13.33203 | -41.36908 | 2025-01-05 03:49:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3440b30b-8793-3a5e-9c54-e981914e0a87 | -12.40358 | -41.48948 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d09a0cb4-4276-3285-8394-c6844502e8a0 | -10.6489 | -37.02956 | 2025-01-05 03:49:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e778a2a8-578d-3fcd-ad71-9b779bf5e710 | -12.05537 | -40.01335 | 2025-01-05 03:49:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 12635462-c652-30f7-b558-a15ce7327888 | -7.12785 | -40.16219 | 2025-01-05 03:49:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 429ba8b6-e906-36bc-90ff-3e582a17c0fc | -12.41231 | -41.48207 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ff83946-da42-38ed-9b65-2bb6276f8d19 | -7.66823 | -38.13334 | 2025-01-05 03:49:00 | NPP-375D | MANAÍRA | PARAÍBA | Brasil | 2509008 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ecd6716-1ca8-33ed-91c7-caffaca5d8c5 | -9.49822 | -40.32306 | 2025-01-05 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 987143fc-5a9c-39f9-8ddd-9fca9a1ddf96 | -7.12715 | -40.16637 | 2025-01-05 03:49:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dcc38d47-97f4-3aca-9088-2ee249ae8826 | -10.32278 | -42.41995 | 2025-01-05 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 90632a9b-a97b-36e2-943e-46aa9ca089e9 | -3.01621 | -39.99419 | 2025-01-05 03:49:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fba4bfd4-5b28-33ed-920d-ae650beccf3e | -11.5906 | -38.61438 | 2025-01-05 03:49:00 | NPP-375D | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c76d5f7a-f150-380c-8538-c2a1f0c70e30 | -11.38539 | -37.81409 | 2025-01-05 03:49:00 | NPP-375D | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 79e91340-877f-381b-ad70-72c42d8e860e | -9.81186 | -36.32597 | 2025-01-05 03:49:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 97193d5a-a637-3e8f-9d18-e3a5b90cf16a | -2.94001 | -40.18198 | 2025-01-05 03:49:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d9822dd-b627-3aa4-b60f-adc74045f484 | -12.00144 | -41.39312 | 2025-01-05 03:49:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87feccda-9bf4-35c2-86e2-d15c253d4252 | -9.50176 | -40.32365 | 2025-01-05 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 40e37298-d7c4-3773-ae69-df586f03c95f | -9.47472 | -41.02344 | 2025-01-05 03:49:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ea7867a-5c19-36e4-a7d1-238a3a514b09 | -8.4164 | -40.54127 | 2025-01-05 03:49:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 68c0361b-4396-38eb-b490-3528b1b970fc | -9.18693 | -35.41434 | 2025-01-05 03:49:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a2f2123c-a294-38e6-8698-f8fe486bfc39 | -12.41083 | -41.49072 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3241e46b-b3cf-37ea-9355-0e2eb0ca48e4 | -12.41518 | -41.48706 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 389cdcf7-7bd4-306f-8916-489139c7f62e | -9.55111 | -40.31136 | 2025-01-05 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c44f3ac4-846c-3a79-87ea-534c339de430 | -10.6461 | -37.02547 | 2025-01-05 03:49:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3d676aa9-a9d9-3849-93c5-3355f793ccf0 | -12.40376 | -41.48594 | 2025-01-05 03:49:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd0026a7-2bbe-3ea5-b2ab-1470b2f20e8b | -9.49268 | -36.83839 | 2025-01-05 03:49:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a978ca1-a2a3-3195-8499-44764cea80c3 | -13.32916 | -41.3644 | 2025-01-05 03:49:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e4ca037c-d091-3031-abf7-be5e85a595bc | -12.8713 | -41.10347 | 2025-01-05 03:49:00 | NPP-375D | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cdc263b8-efe5-3674-b81c-e71c00692d00 | -19.50679 | -50.14484 | 2025-01-05 03:51:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bca6b577-184b-3a7d-ab71-c893a16d73ef | -23.59976 | -46.92014 | 2025-01-05 03:53:00 | NPP-375D | COTIA | SÃO PAULO | Brasil | 3513009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f5033849-346a-3a6c-97a4-732668bdcfe3 | -23.34031 | -46.77438 | 2025-01-05 03:53:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| acaa4bb7-a6e0-3546-936b-950e9dc28371 | -23.33618 | -46.77351 | 2025-01-05 03:53:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8839bd2-827c-3d52-8ec5-a2d7ac0883a7 | -22.53791 | -48.81293 | 2025-01-05 03:53:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 256b405a-3e6a-32a8-bb27-ad6e4a9a7bc7 | -23.38608 | -47.05308 | 2025-01-05 03:53:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 24a8d308-f6ac-30fc-acd4-585c73e80508 | -2.93938 | -40.18248 | 2025-01-05 04:10:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0ebf33b2-003e-367e-bf84-32ad2872bbc5 | -4.1615 | -42.02257 | 2025-01-05 04:10:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0daff9ea-db34-38c2-8dac-20825d3fd362 | -4.94416 | -38.72591 | 2025-01-05 04:10:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c26b4d90-c3e6-3634-8738-d53c16812c1e | -3.01676 | -39.99615 | 2025-01-05 04:10:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4064f1e0-5324-399a-bd8c-e464fcb04f39 | -4.46182 | -37.79933 | 2025-01-05 04:10:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 405c2e25-fcba-39a8-b567-1f32e49537a3 | -4.16096 | -42.02604 | 2025-01-05 04:10:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 41e2c3c1-6f47-3dd3-aa70-332c96d5f761 | -4.94036 | -38.72533 | 2025-01-05 04:10:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 62e00179-7ad6-38ac-a707-e46020e52508 | -4.07514 | -41.66328 | 2025-01-05 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 423dd671-66b5-3c1a-a080-b40f2714b1b5 | -10.65204 | -44.49714 | 2025-01-05 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eab2a9ad-ef02-3f9e-b7d6-4e7db3ee4673 | -9.54995 | -40.31242 | 2025-01-05 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README3.md)
