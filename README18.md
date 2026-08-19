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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c233a722-1596-3a5a-8ea5-5c0bf8d1a8fa | -6.0912 | -57.9187 | 2026-08-19 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 8924e1b8-47c5-35bd-afa0-10257bd4cdfd | -19.7643 | -57.9399 | 2026-08-19 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| b701d533-d57c-30aa-96a8-3439542a6c05 | -6.6938 | -58.942 | 2026-08-19 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b703cc02-8042-3ed1-94c3-5eadd227f38b | -5.4319 | -48.3996 | 2026-08-19 03:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 17835139-0b6f-36bd-a94a-57fc0ada1cc8 | -5.9994 | -57.8639 | 2026-08-19 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 9b91061a-1498-3e81-8e83-36c064a50f3d | -5.4317 | -48.4212 | 2026-08-19 03:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 4eb3d25e-4cd1-36de-b7ce-2e70a0b49e01 | -5.9011 | -43.6279 | 2026-08-19 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 497ab995-f11e-387a-ac29-848f19d96477 | -5.4503 | -48.4201 | 2026-08-19 03:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| bed482ce-ff8d-3f9a-8509-8d1aec1b831c | -9.4257 | -60.416 | 2026-08-19 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| fae29940-cf48-3e17-8152-4e4f2045f235 | -19.7438 | -57.9633 | 2026-08-19 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 295.8 |
| ca5db85c-a848-31ba-bd8f-6cc48ac3a903 | -9.3875 | -60.5528 | 2026-08-19 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| ae42f624-e805-3607-b795-23aa6b88d6fd | -6.0912 | -57.9187 | 2026-08-19 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 4ebf3aa1-92ec-3d5e-94cd-8401a4f93170 | -19.7639 | -57.9607 | 2026-08-19 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 239.6 |
| 30c048a2-6ec4-354a-96ef-2cf939a97000 | -6.0913 | -57.8992 | 2026-08-19 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8ee5b7c5-9bec-3af9-957e-aed6fd3a9faf | -6.0178 | -57.8631 | 2026-08-19 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| baea08f3-8a53-38d1-adb9-b7f2e1e8db96 | -19.7643 | -57.9399 | 2026-08-19 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.1 |
| a03e6e94-b73b-3ea6-876a-9b5b45f1a4fb | -6.6938 | -58.942 | 2026-08-19 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7a938222-7164-3c2c-85be-6e60c7cbc9fe | -5.9198 | -43.6264 | 2026-08-19 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| d247f98b-5541-3303-8b07-c853e67607a1 | -19.7442 | -57.9425 | 2026-08-19 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 234.8 |
| 707e0074-8bb3-39f6-9b53-1d6697f54a0c | -5.78864 | -43.92503 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3437713-ec22-34b1-bc1b-653ad56f92a7 | -5.4308 | -48.40567 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| c364e88e-d997-3a3a-8e73-52fa0b65b78e | -5.44238 | -48.41844 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| f6688ec8-9fe2-3bc1-8179-75f59da5a3b3 | -5.79932 | -43.64576 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 111dee81-3296-3cd3-b9b1-0d613187ed7e | -6.29342 | -43.6438 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aac38cb7-2ba2-3301-aa41-40f0c16decf8 | -5.79491 | -43.91951 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25a9b62e-2646-33c4-afc3-c61013e3083e | -2.90853 | -40.46452 | 2026-08-19 03:42:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f9ad06fc-74b1-3fda-aad6-5c4995839ec3 | -4.00638 | -48.0638 | 2026-08-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0712c6d7-81ad-326e-b5c0-2d4da0d12673 | -4.70971 | -47.15845 | 2026-08-19 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d7065561-5555-3f75-aa8d-7600d41e74d9 | -5.43548 | -48.41722 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 33e2cd50-1211-3a6c-9cc4-7cc42d4bd9b6 | -5.42154 | -48.41758 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dd07aec-7695-3cc3-a4e6-799ad3f382d3 | -5.42733 | -48.42268 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e698ae76-fef4-3a9e-9f87-c5ddf0b5d546 | -6.28993 | -43.64023 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc61533d-6241-371e-ab8f-68bd7fb8c965 | -4.01346 | -48.06403 | 2026-08-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdbf805b-8437-3258-8b54-f62dedfb91c4 | -2.9112 | -40.46416 | 2026-08-19 03:42:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68582c5f-09a9-30a2-bd46-577aa0d20b85 | -5.42976 | -48.40958 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 33f86553-0e9c-3a58-ba18-e914f24e5c3d | -6.29043 | -43.63731 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ecfd92d-3336-38da-a4a1-0437310843b3 | -3.68068 | -47.65253 | 2026-08-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| aeda46e3-fa6d-3baa-b2af-4c17bb0937c6 | -6.28536 | -43.63659 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 149b5118-4e46-3904-8ff1-a069da71bf28 | -2.49875 | -48.13705 | 2026-08-19 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25652ff2-7a35-340c-8a69-ae3ff220239a | -6.28432 | -43.63646 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7136a748-5e1a-370b-adf7-7a9ed7558179 | -5.5058 | -40.76262 | 2026-08-19 03:42:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c63b67e-c3e3-3bec-9268-1a6efcb7229e | -5.42856 | -48.41603 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| b1db7d4b-7971-36eb-af05-5952a96184a0 | -5.42161 | -48.41508 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| e789becd-14a0-37ec-8bbc-99c4235764d0 | -6.21253 | -42.13689 | 2026-08-19 03:42:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 779a93da-086a-33e5-843b-d7f0d98c9f2b | -5.66244 | -43.56954 | 2026-08-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1418e73c-0e2e-3962-9506-0b70203a4465 | -6.27028 | -43.27571 | 2026-08-19 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 68a454e1-8272-333d-b8b8-cf2b1f9354f9 | -5.7988 | -43.64878 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ea057c4-4b46-341b-8631-759a8d9df26f | -5.91177 | -43.61981 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| aee2e902-b6dc-3d53-9f6a-f4a7635f8bea | -5.65736 | -43.56871 | 2026-08-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a18bd774-2586-3eb3-bba2-2832858cc723 | -5.82033 | -43.40338 | 2026-08-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4416165d-89aa-3fb9-8925-71ff4bcb096f | -5.42849 | -48.41856 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 62c639be-05a3-3b85-b5a8-aefd49ee1c7b | -5.44346 | -48.41454 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 611aad5c-dfaf-38ba-8a30-6d160d60c5c2 | -3.67925 | -47.6509 | 2026-08-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f7806290-d8c7-34ce-8981-c97ce754d4ef | -5.43427 | -48.42373 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| a7f7a8d7-e87d-3b37-9a5e-352306e67475 | -5.9214 | -43.62454 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3c9b170-c034-321f-9d79-b8994badc700 | -6.28837 | -43.64295 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4113c84c-1e36-3e12-8c4d-5c3100db1731 | -4.71001 | -47.15726 | 2026-08-19 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6d582d98-2da9-3e90-8d7e-35067e703841 | -5.82182 | -43.39478 | 2026-08-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 327a7746-d1c6-3795-8833-da45289af428 | -5.91684 | -43.62069 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b1bc07f2-3114-32dc-b6cd-7b0c69d4ddde | -5.80545 | -43.64059 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2238a550-453c-3434-ad42-18824dfd8441 | -5.80063 | -43.91725 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 258a3563-2a64-35a8-a994-dc6b209715dc | -6.28944 | -43.64317 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b7c0baa-72dd-323f-9192-17883f0d5938 | -5.50708 | -40.75494 | 2026-08-19 03:42:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c21266d-7bd6-37cc-b924-f7ba80e5bcbc | -4.01402 | -48.05848 | 2026-08-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af2a598a-5f99-33a5-9790-c352ec4b76ab | -3.68854 | -47.64749 | 2026-08-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4cda77ad-c3c4-3d09-89cc-7ec130761aff | -5.79437 | -43.92267 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a1e75b2-f132-39d8-a7ba-12eb02eae4cb | -6.27284 | -39.68309 | 2026-08-19 03:42:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 44927543-d708-34d8-b5e4-319020583401 | -5.43657 | -48.41326 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| df955573-adb1-35b4-9cf2-a679267980f3 | -5.79639 | -43.91764 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b52d0cdd-71dd-31c8-9ba9-eba96966079a | -5.91073 | -43.62584 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| f5ce2d63-840e-372b-8153-197bcc23221c | -5.787 | -43.93465 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cead5e86-3b7c-3884-8b0a-ad9e7ab8bff3 | -5.91581 | -43.62669 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 01f61407-8e55-3cbc-bb39-7a0fa79c72e2 | -5.43541 | -48.41972 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 891927e5-cdcb-3bd3-bcda-8ac3e995bdba | -5.82083 | -43.4005 | 2026-08-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95dd6aa9-7939-3f2b-b639-856843e2648a | -6.28889 | -43.64001 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3324a680-b9fd-39c5-98f0-72747d99606b | -6.64006 | -41.43611 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fe7f7425-cef2-34a5-a40c-a9e284b1084c | -6.04837 | -43.89657 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b15c1aef-7975-3e17-87d0-a7e091341cc3 | -5.43667 | -48.4108 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 055090b2-5b92-3af9-8b31-9eef15ed9947 | -5.44232 | -48.42095 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab159f94-06f6-3ccb-a5f1-44118bb433e1 | -5.50644 | -40.75879 | 2026-08-19 03:42:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0ec9275e-5ad6-374f-aa5a-22db5299146d | -3.68742 | -47.65392 | 2026-08-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c3440e2c-4148-3511-a6c3-be347ed5ab1c | -6.2929 | -43.64673 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b82703a3-e12b-3a51-a448-c2bb23acb0ea | -3.02944 | -41.16767 | 2026-08-19 03:42:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5305b218-1583-3e4e-842d-61400a355e9e | -5.91125 | -43.62281 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| be3e0833-710a-3507-84ec-330ef46a2a7d | -5.14566 | -40.654 | 2026-08-19 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4d277fe0-1b93-34f4-bbea-44b0d0671b53 | -5.82133 | -43.39763 | 2026-08-19 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f885bd3-4711-3cee-b8cb-69c8dd77667b | -6.27521 | -43.27652 | 2026-08-19 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 47d434a8-16d5-3cd8-b6d1-02b05eaf083b | -5.79584 | -43.92072 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9381fabe-83e2-3b25-a759-0220682e34f2 | -5.14503 | -40.65787 | 2026-08-19 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d05b8979-89fa-3e2e-b522-9a00109a6c8a | -6.2894 | -43.63711 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23531f9e-3c38-33f3-a47c-364b4f483661 | -5.7881 | -43.92817 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 822561b8-8c81-31c3-9074-9313ad08a926 | -4.007 | -48.05787 | 2026-08-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6f63528-48f5-3448-a34f-50647f1df9ea | -5.78756 | -43.93139 | 2026-08-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8207a42-91af-387c-b918-4f3cd227a734 | -6.21177 | -42.13781 | 2026-08-19 03:42:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ad270317-8500-3afe-a393-9cee55ea5c2c | -5.79984 | -43.64275 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae3f731-1b77-357f-b82e-c5a81451f045 | -3.67819 | -47.65717 | 2026-08-19 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4f4cb17f-bfdb-3301-99c0-8d041a264022 | -5.91529 | -43.62971 | 2026-08-19 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 09aaf901-60aa-3c8e-aea7-81193029b3ce | -5.42967 | -48.41198 | 2026-08-19 03:42:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 9adaa5c5-7aad-3ede-bb5f-fef2f4be76b1 | -6.22968 | -43.68827 | 2026-08-19 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93292bce-295e-389c-ba4a-c9238e04a6c3 | -4.71067 | -47.15285 | 2026-08-19 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README19.md)
