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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d55b18e1-236c-34a5-9c8c-5ead8b24b1c9 | -10.29073 | -57.00032 | 2025-06-28 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e1ec5319-7a2d-3acf-b47d-729d377591a4 | -6.90587 | -44.00551 | 2025-06-28 01:02:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 79e950a1-fefe-38bc-99bc-66aa4cd1011d | -10.82399 | -53.75303 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2c741fe1-b090-355e-b027-196f93a481b5 | -9.68766 | -48.33336 | 2025-06-28 01:02:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 54c163c2-a455-3044-b7c9-43f831b353f3 | -8.00755 | -49.70612 | 2025-06-28 01:02:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 11c83606-8b1b-3d92-b2b7-e23ce3fd45d0 | -10.2984 | -57.14069 | 2025-06-28 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 1aba95d4-1143-3af7-bd30-c56213fc976d | -9.11706 | -49.49648 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 264.2 |
| d14f3e12-353a-3962-9e94-9d30e512ab06 | -8.56029 | -51.57296 | 2025-06-28 01:02:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 66dc866f-acee-30b9-b8ea-5f8fd9b35d21 | -10.82275 | -53.7441 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6aa9f78c-f5c1-3935-be69-db6e2af48f9c | -5.85885 | -46.48145 | 2025-06-28 01:02:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a081b622-06a3-33e1-8a39-9311bf2eb8e5 | -11.87995 | -58.73944 | 2025-06-28 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 49f5801b-fa6d-34da-b97a-7fbb17be9098 | -12.25652 | -46.77631 | 2025-06-28 01:02:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 165993ca-b2a1-37e3-8120-4309017df8c3 | -9.11356 | -49.48817 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 276.4 |
| ab152586-7335-3b50-b07e-0043dc655118 | -7.59348 | -50.01564 | 2025-06-28 01:02:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6d100609-fbf5-34cb-bb1f-8e4447055906 | -11.05143 | -55.08169 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0c67e7f8-25bd-3d84-9e15-2f8459fb401c | -11.44047 | -54.4835 | 2025-06-28 01:02:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 15255692-81e1-320d-890e-0b829567eec6 | -9.11569 | -49.50248 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 38ff2145-915d-3ca5-887a-36061c8319fb | -9.69559 | -48.34235 | 2025-06-28 01:02:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6e251c4a-61c5-34c1-a644-cc27ca61d3c3 | -12.31239 | -53.25821 | 2025-06-28 01:02:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e89a483-7d43-3302-a9e0-2c967816cb06 | -9.70792 | -56.19525 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1796a752-f9ca-32f0-96bd-e70a4d99b6dc | -8.86282 | -50.16605 | 2025-06-28 01:02:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 74a64371-8fbb-3f98-9eea-99ecee90e6ff | -11.44692 | -54.46391 | 2025-06-28 01:02:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 05ef7fb7-802c-3b10-b1ba-165a6f0aa059 | -10.81792 | -57.75751 | 2025-06-28 01:02:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| d355383e-a38c-356d-b032-a43701844f71 | -8.85551 | -50.15986 | 2025-06-28 01:02:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5687936-8e19-3f18-a4c5-3691a8ca3d8c | -12.2532 | -46.75599 | 2025-06-28 01:02:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b3fe46df-23c0-3704-9ac8-ca34ff2783f1 | -9.12454 | -49.48652 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5bb29eff-3d86-318e-8d44-797a593f997b | -11.26465 | -52.7463 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e77df177-b7c5-3392-801a-729997a3854d | -13.14157 | -56.80795 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| bace33aa-da83-3ca3-8b3e-4506e96942cf | -11.04472 | -55.37173 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 279.6 |
| 6468a340-e540-3872-bc3f-e6bff2099649 | -12.65932 | -54.10216 | 2025-06-28 01:02:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d086dfc7-4b1c-31ce-9e4c-4dae5a57d1c3 | -9.71734 | -56.1939 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 4175d873-98d2-3c17-84d1-2f1e61b7e6e0 | -10.03863 | -54.3318 | 2025-06-28 01:02:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9fe6dd9e-339a-3ea5-a65f-debf38f28161 | -10.84288 | -53.7594 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 4b481ca5-7371-330b-a181-39eb87005ff3 | -11.57846 | -52.10682 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7cf71964-c96f-35ad-89e7-54c1ebf067db | -10.29691 | -57.12895 | 2025-06-28 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| fc710334-aac5-3796-855f-2d7329315c72 | -7.0843 | -49.61246 | 2025-06-28 01:02:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e4707f11-386d-3fb7-b15d-e9ab6ce15f9d | -11.43923 | -54.47433 | 2025-06-28 01:02:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d612b513-24cd-33da-ae82-b1e262b5d749 | -10.02977 | -54.33306 | 2025-06-28 01:02:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec68023b-9f5e-3137-9295-841ad8f68c4e | -11.57982 | -52.11626 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 8e08a712-fce8-398d-bddd-c5771b191a24 | -11.80604 | -56.96427 | 2025-06-28 01:02:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e4f96d0b-26e7-3348-b22e-0d317e5445b3 | -6.90621 | -43.99857 | 2025-06-28 01:02:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 342.7 |
| 20ed025b-179a-3f76-844a-17fe829f1d3a | -9.11142 | -49.47386 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 868bf1ec-40f9-3e22-a353-802134797acb | -10.81066 | -50.10069 | 2025-06-28 01:02:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d21ee0f5-18f1-3859-8835-f8121cde6e16 | -11.05521 | -55.38018 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| c57279a6-0946-34b7-9ebc-6e787addd151 | -10.50688 | -53.58992 | 2025-06-28 01:02:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 74db279d-8e41-3277-b25d-16949c435f2a | -12.10708 | -54.58189 | 2025-06-28 01:02:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| bbac6ccd-fd41-30b5-8e63-bea9a44b931c | -11.58117 | -52.12567 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 43c24086-a679-3a89-a18d-242dc88a5ed8 | -7.54237 | -45.829 | 2025-06-28 01:02:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 56e1a5de-c25c-3d22-981d-e1f124a19b73 | -10.83529 | -53.76962 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 31a66cb2-3f1f-30f4-86ed-38c289177e13 | -7.08207 | -49.59748 | 2025-06-28 01:02:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b8dc2285-e03a-3776-8a56-7ba22f1fef24 | -9.11482 | -49.48217 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 253.0 |
| 4ad833d7-3547-388c-a2aa-4cf952bbe043 | -11.27356 | -52.74497 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 8bb4658e-d0b7-36a9-b246-6683b9cee2af | -11.27485 | -52.75408 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 304.8 |
| ce24789b-da08-38ab-b5c4-9825b798b3d1 | -9.72544 | -56.18243 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d0c65c45-a51b-3317-b878-060cfe21c028 | -9.71601 | -56.18367 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| e2c29bf6-5214-312b-a542-f63f4828e29f | -6.55372 | -54.98281 | 2025-06-28 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ed43bf03-2a71-339f-828e-1eea546c6fb2 | -11.05017 | -55.07226 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f6b2d9d0-c4d4-3f22-bb91-09bac9157f0a | -7.53998 | -45.8226 | 2025-06-28 01:02:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 2384ee77-2ae3-3135-b2c3-d54e73e4b2c1 | -6.89921 | -43.9563 | 2025-06-28 01:02:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 67123277-8bc7-3cfe-9543-41652b5c8d98 | -11.26595 | -52.75541 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 77a4bf0a-10d8-3e02-8684-6a3965305ca7 | -12.02525 | -47.77745 | 2025-06-28 01:02:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| bab76bfa-d753-3fa8-bf03-60de747fa295 | -11.04602 | -55.38141 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 240.7 |
| 2551e1df-a5a6-3775-9517-1e0c05d1bcc5 | -11.43799 | -54.46518 | 2025-06-28 01:02:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a3474571-4ac6-35ca-a423-847feffd451e | -9.72677 | -56.19263 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2b1cc539-20b4-3c9e-9240-e22f1b61d98f | -9.70659 | -56.18498 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 5958b93c-f1e4-3dc2-a3f4-f38a88aebc34 | -8.56183 | -51.58355 | 2025-06-28 01:02:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 966af8ec-d69a-3ddd-86a1-0d88ab341bb6 | -11.32742 | -51.45094 | 2025-06-28 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 195e9dd1-a973-3c87-8fa1-46bc56b60d63 | -9.11259 | -49.46796 | 2025-06-28 01:02:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 76014ab7-975e-3f13-9913-d904fe540581 | -10.83281 | -53.75175 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9fd73614-1a8f-3978-b5c4-85e72280fc81 | -9.70191 | -56.19155 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9fb1735e-c632-3333-916c-ddf9ebc886e8 | -11.04732 | -55.39114 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5ba65dc8-16e3-3d1f-afdc-2bd382ba7f44 | -10.83405 | -53.76068 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 770e97c0-47fe-3b60-a093-aa78394c6950 | -10.2922 | -57.01183 | 2025-06-28 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3331c7eb-5419-3d39-8a9e-20d2c707669b | -11.05391 | -55.37049 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 0128122e-fc11-3c9c-97f0-42964e889955 | -11.03555 | -55.37306 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 8ecd6c20-7f69-3927-a560-86aa12e27d35 | -11.91707 | -54.81226 | 2025-06-28 01:02:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d0be42e4-5dcd-34e8-a50e-f5c17a4db9f2 | -8.57139 | -51.58208 | 2025-06-28 01:02:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 00dcd95c-2251-3aec-9ee9-6fbfe3ae48d9 | -6.89915 | -43.9632 | 2025-06-28 01:02:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 3988c9f8-5078-348b-8e5c-f93653a18bda | -8.0463 | -47.64702 | 2025-06-28 01:02:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 4b51940e-8cea-30a3-990a-40d2c2b67058 | -11.05287 | -56.74415 | 2025-06-28 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| db8fc882-0ef4-324d-88a2-814f5a485f87 | -8.84861 | -49.85933 | 2025-06-28 01:02:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5cce8c17-9e89-3f48-8109-87b1a570fbd6 | -10.95522 | -48.15158 | 2025-06-28 01:02:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| be6acf4d-7c57-3a56-ac0b-13751dc90bc5 | -10.87426 | -53.77642 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0584f23f-e659-373f-bc1b-f0cd7a9b9740 | -9.70053 | -56.18134 | 2025-06-28 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c7864627-9746-3533-9a7a-eb97a5cb46e4 | -9.69317 | -48.32719 | 2025-06-28 01:02:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5d48486f-65a8-31b0-ab6f-675b54a1cf3d | -11.03684 | -55.38274 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d298db18-4667-3b94-86da-ab46c47cc7df | -8.56986 | -51.57151 | 2025-06-28 01:02:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 297c5e1b-45de-3c88-8935-3b8cac40c83d | -12.11733 | -54.58996 | 2025-06-28 01:02:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86c21cda-0509-322a-908e-5857d01848d8 | -10.52951 | -53.62307 | 2025-06-28 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0d979dc3-67e2-372a-907e-7396d041f499 | -12.10834 | -54.59124 | 2025-06-28 01:02:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0a605226-5675-3730-982d-41ce206b79cd | -11.19135 | -55.92548 | 2025-06-28 01:02:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 172f4766-13e4-38f9-ab20-64a5a559d351 | -10.02854 | -54.32409 | 2025-06-28 01:02:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c4dcd394-cc5f-3ea8-b777-b8008035e994 | -3.87689 | -54.22369 | 2025-06-28 01:05:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1677b499-1e86-31b2-b127-aefca18b5a70 | -2.49985 | -54.13075 | 2025-06-28 01:05:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 322a43a7-9d9a-3359-8ced-fdcf904e3be7 | -9.102 | -49.4761 | 2025-06-28 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 43cf9cfb-5ec3-36db-80bb-de91f5f10a35 | -7.2219 | -43.0682 | 2025-06-28 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.3 |
| 8e609020-17c6-3366-b428-62e1a7745a36 | -6.892 | -43.9851 | 2025-06-28 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 29b1292a-c8b6-31d1-a137-38a8e3f97e3e | -11.0644 | -55.3757 | 2025-06-28 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 5ee4aa7d-949e-39be-aa3d-749e7e9ec051 | -6.9416 | -42.8834 | 2025-06-28 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| acac98e4-35c6-39a4-b470-8f152cb6bfaf | -6.8922 | -43.9619 | 2025-06-28 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |


[Clique aqui para ver as próximas entradas](README6.md)
