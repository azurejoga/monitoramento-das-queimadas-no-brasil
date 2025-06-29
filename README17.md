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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4635dd4-29f9-3635-bb84-6257f2f93177 | -7.1924 | -43.71146 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738a6a7e-3c0c-32de-b9ee-2470169f1466 | -10.56468 | -52.03084 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be4a8755-b430-3c70-bffe-23906ce9c27a | -7.2173 | -43.07936 | 2025-06-29 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2a65cec0-1659-38e4-9043-7a99516541fb | -7.18723 | -43.56031 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a882bdb6-f01e-35dd-aa3f-1944230abd5a | -4.31991 | -48.0739 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23df6b4c-c2dc-3c7f-8251-6b674ac05873 | -9.1587 | -46.35409 | 2025-06-29 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1688f69b-f9ef-3702-bcd7-2a0f1284a21b | -4.18402 | -48.13748 | 2025-06-29 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe0f5f70-bee4-3b7f-9c6d-b296b1402fd8 | -10.97748 | -45.11156 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 275952d3-2e68-3862-8b7f-3ad1a0e56f7c | -5.06089 | -43.2516 | 2025-06-29 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4d5559e-4834-3b6f-9777-0c77a4630f6d | -10.6256 | -48.69855 | 2025-06-29 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f299ae2f-82f5-3e54-bb10-e1f32753b4f2 | -9.79014 | -48.56779 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47e74991-f751-3abf-8638-7f369aefed40 | -9.11772 | -59.05453 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b2ab94-fe91-308b-ae6b-e4b8a1e3cba8 | -12.12896 | -45.57522 | 2025-06-29 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9bf4550-dfad-38cc-8138-f41832c316f9 | -10.56828 | -52.03147 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ed0e777-df46-3b3b-8daf-3e8a7ab12675 | -9.08651 | -59.47451 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b8715b4-77ab-3ef0-a9c6-e302db3e79df | -10.56552 | -52.04824 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca25188e-2d6c-31b5-955a-81e8089ffa49 | -5.74849 | -46.25941 | 2025-06-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a4436ce-a9d5-33c2-8a83-61abdd3e7bca | -5.79297 | -46.30682 | 2025-06-29 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78db18e3-7a28-3ad5-85e4-744a5b41752e | -10.86017 | -53.75071 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a85b8d8b-deed-32ba-95c4-5a33561efcc8 | -7.29748 | -55.31476 | 2025-06-29 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ccf0f20c-1193-3f4e-afb4-74e729b9d038 | -10.53676 | -42.53798 | 2025-06-29 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 29b1e711-4168-38e8-b0eb-5cbed65094e5 | -10.83289 | -53.76702 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ab111b9-733d-324e-91dc-2b5d99660243 | -5.57098 | -45.21957 | 2025-06-29 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f3390e4-a6cb-3fd0-a0b8-fcaeeeb3a0f2 | -5.3241 | -55.94368 | 2025-06-29 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68da924b-2606-3c20-9c45-666bb04b7142 | -9.64631 | -48.79108 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb1e5aaf-b22f-3a97-ab2a-603d3eb737ef | -7.09722 | -44.36537 | 2025-06-29 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9afeb16-a724-39bc-911f-4065002bb319 | -10.94666 | -45.60172 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d6e85b-95e7-3e69-a522-d7588f14d1be | -10.8205 | -51.2972 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66d6a8aa-183d-3cfa-ae76-a7b6d45de14b | -11.82137 | -47.5115 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9a6ccc3-dd70-3540-abbc-f8d45ff3d52f | -10.5597 | -52.03859 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 755fe7c4-3057-3af8-9c67-96ff8b1288ec | -9.71062 | -56.18843 | 2025-06-29 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ea292c7-49bc-3bee-a55d-b00c3d5608fb | -10.61948 | -48.08585 | 2025-06-29 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ec29950-ee3d-3d68-89ae-fea2a2771ea3 | -10.83865 | -53.7574 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0002595f-ea38-34e2-8662-5223347cbd70 | -10.87289 | -53.74777 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c1741ff-a1fb-34cc-913b-159e3f85e348 | -10.92817 | -44.15701 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac80202a-f17e-3589-becf-0271ebc1c36a | -10.8426 | -53.75811 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25ec4149-aa8f-386c-875b-2969e956b8ff | -11.84328 | -47.53289 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0e29f9e-608f-3c39-9ff3-cf7c5138ecf1 | -8.01832 | -47.41088 | 2025-06-29 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43f3b770-4899-3fa6-ab19-7b0b23d328f8 | -7.48872 | -45.44668 | 2025-06-29 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75fbf811-e0c3-31ba-80c5-321c0d6a72b4 | -7.55881 | -45.84494 | 2025-06-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 484f9a3b-6c89-369f-8226-cb9b54fcba34 | -9.10699 | -59.04813 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7225073-868c-349f-8eb1-0a2d6e859fdb | -10.5604 | -52.0344 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ed19930-67f0-3be3-bf20-cd2731c34eaf | -9.42084 | -47.95449 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ab4bba5-ab7b-3ddc-8139-8a2ddc638631 | -7.17578 | -43.6639 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 863e2c5b-200a-37d3-b9bc-d4f41dfa0643 | -4.1071 | -47.93721 | 2025-06-29 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b3cde26-cc87-3b8d-b151-b933dd0ab446 | -10.56759 | -52.03564 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40a95125-f462-3276-953c-a31f3119aa82 | -7.49165 | -45.45126 | 2025-06-29 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 089a42be-a842-3324-9d3b-f319ee3a0697 | -10.8338 | -53.76183 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68a4a4a5-1d9e-37e0-ac0d-88da1e7532b6 | -7.16007 | -49.51134 | 2025-06-29 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51bb865c-bf0e-3d8c-88d1-f1f015d0a16f | -11.57268 | -44.83588 | 2025-06-29 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82d74642-86af-3425-8f9d-30fc07418d3c | -10.98122 | -45.11214 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 62bc4fa4-33a8-3af8-81ae-5261892d1033 | -11.57449 | -44.834 | 2025-06-29 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b70bc1d2-309b-3ec2-a8c8-565e3c6cf8d2 | -7.22561 | -43.51736 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c7fa415-ca4d-3cb4-ac6d-22887b5d2ee6 | -11.56854 | -47.45008 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2c85541-3a2f-3b6f-a478-f833fe1f1b77 | -9.08914 | -59.49312 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57a71e48-99da-3078-8e44-dbd77f147131 | -7.19484 | -43.70395 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ff09031-03af-34a7-b9ea-92defb508a67 | -4.45834 | -48.99504 | 2025-06-29 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23593315-b5ed-3140-b141-a902f364c1ff | -10.55762 | -52.05122 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 79754b05-20a2-39a6-813f-4890cf8cd401 | -11.04821 | -44.34988 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0a57c60-d062-3b85-88c0-d07a7195bab9 | -7.19072 | -43.42839 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6a907ba-1b66-338e-b91c-dd1e6b4e482f | -10.93133 | -49.42936 | 2025-06-29 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3031a521-e7ed-3119-9fb8-9e35170f550c | -10.86983 | -53.74196 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56901eb0-d364-3096-83a3-916273b2ed11 | -8.69977 | -48.22264 | 2025-06-29 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 770c9ba9-930c-34da-95ac-eda5716f491b | -9.4247 | -47.95151 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7db85b84-6495-367f-bcbe-22f4e1ce0e49 | -10.54961 | -52.03254 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f5802dd-7821-3de5-8acf-e9e5f005fa4f | -11.8433 | -43.79623 | 2025-06-29 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71dcdbf0-3b56-3ca2-ac19-aa83a339cda4 | -9.70207 | -56.18168 | 2025-06-29 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d114102-810c-3e59-be13-ac50c5657674 | -10.97682 | -45.1161 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fcd979ad-1846-3b66-b60d-442c2f0fcf50 | -7.18927 | -43.70601 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a52f781c-f4fb-3404-94df-6e3b9c73cfe0 | -9.10621 | -59.0522 | 2025-06-29 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ccd1733-0727-3b79-bcf5-e117e64906c0 | -10.5568 | -52.03377 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e431234d-a475-3fd2-9f0b-69b8d8e99687 | -8.09105 | -46.85344 | 2025-06-29 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc03de84-4743-3b9b-af67-bd4a39401d74 | -10.98055 | -45.11668 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 16af3e17-4365-324d-bd99-b535ddfefa3a | -11.57832 | -44.83457 | 2025-06-29 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf7f460e-e0d5-3cde-a76f-e5fa9ef49246 | -9.43189 | -47.94905 | 2025-06-29 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 63569250-eff5-340a-a70a-fbfdc840eba7 | -10.56122 | -52.05184 | 2025-06-29 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d8115a4e-3a7a-30fe-9a1f-0e2480cd9b67 | -10.84655 | -53.75882 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5ac3da6-0629-33ea-a04e-6ec5bbd23f0f | -10.8505 | -53.75952 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af33d6c5-373b-3525-bb23-eb47dd9a22f8 | -10.95865 | -48.15343 | 2025-06-29 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35dfd213-81ed-3cf7-9250-346cf4f654a2 | -10.29754 | -57.13979 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6be7835-c3f8-341f-a479-9bf40f442e4c | -12.1269 | -45.57312 | 2025-06-29 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43a1a991-4a5f-335e-b7bc-b35b2862e699 | -7.09638 | -43.65584 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81ecfae2-4c17-36d1-8650-a44945a66e63 | -10.83775 | -53.76254 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92e54666-21fd-3869-8980-e74f9627e0e9 | -8.85033 | -50.17312 | 2025-06-29 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfe481e0-ba49-3a64-a65c-0e6e09318afe | -10.79691 | -47.99031 | 2025-06-29 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b78580a-b6a3-355c-887a-093c3075d434 | -4.28842 | -48.05827 | 2025-06-29 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 037b0ea7-5728-3dbb-918f-c94a1fdb436f | -10.98188 | -45.10763 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d831435e-e62f-3653-9058-e444fc069fb5 | -10.97308 | -45.11551 | 2025-06-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abff7cc1-11f8-3630-957b-ca2851eb4316 | -7.29538 | -55.31635 | 2025-06-29 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 74dcf7f1-9059-379e-87e0-5e796b24754c | -7.10397 | -44.37091 | 2025-06-29 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f343f361-5d8d-3304-9445-9359a90b0159 | -7.17505 | -43.66879 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d53b1d8-1c30-30e8-a3bb-8a0fa6cd2d92 | -6.62566 | -47.28278 | 2025-06-29 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f9730cac-6314-35c0-bd34-4200f63566c7 | -7.19701 | -43.70715 | 2025-06-29 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe976235-9c13-344b-a495-7b2ca531d209 | -10.29314 | -57.02327 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad3304e9-7d46-311c-8a08-625d4a6681f9 | -10.8417 | -53.76324 | 2025-06-29 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d598d3c6-e1d9-3bbf-a5f7-47d9d2fa76ef | -10.30356 | -57.13505 | 2025-06-29 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daa89f5f-ded4-3d83-9432-a06a1ce99a41 | -9.79397 | -48.56487 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0220096a-51b3-3f7c-a9c4-3cd22325889e | -11.8332 | -47.52481 | 2025-06-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eedbc471-c2ef-3e1e-b84b-7f2efe0d9168 | -7.09359 | -43.65708 | 2025-06-29 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c820e489-6ade-3dcd-aebd-3d1c22681ebc | -9.79067 | -48.56434 | 2025-06-29 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
