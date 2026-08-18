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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbd849bd-448a-3167-9bc0-50f5c63370bd | -8.5855 | -50.3331 | 2026-08-18 02:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 145089f4-f071-35f9-a78a-974c0df12838 | -6.7477 | -59.1909 | 2026-08-18 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| a296ec47-ce95-3d56-a699-b70ee387f062 | -8.5853 | -50.3543 | 2026-08-18 02:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| aa2c9f8d-2823-3861-95af-d3cef758e64e | -6.7478 | -59.1716 | 2026-08-18 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| bfb6fad5-a7d3-323f-a68c-3e325fc61af2 | -14.2763 | -51.902 | 2026-08-18 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 77af3b04-9855-3cb0-8872-6caaa51ae005 | -6.42723 | -35.07013 | 2026-08-18 02:56:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 397d7a94-69b2-3843-959e-61c0ece9e46f | -8.604 | -50.3527 | 2026-08-18 03:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 0bf24bd8-e851-3218-9c81-0b30fd2353b0 | -8.5853 | -50.3543 | 2026-08-18 03:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 4007b2fd-4bb5-379b-b4f4-92f9463e3a64 | -6.748 | -59.1523 | 2026-08-18 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| fab396be-80b8-3338-b44f-f9e175a5f48e | -6.841 | -59.0132 | 2026-08-18 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| e9c80877-9bcc-38b4-ba7b-77fecdfa3c33 | -14.1628 | -52.9323 | 2026-08-18 03:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 01b26da5-8260-39ea-bc6f-6e6a5cfe5405 | -6.8411 | -58.9939 | 2026-08-18 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 71c7161a-e18e-3b62-bb0a-53ea5ec80a78 | -14.1631 | -52.9113 | 2026-08-18 03:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 9b12936a-57e8-3356-8c60-b5effecfac99 | -14.1824 | -52.9089 | 2026-08-18 03:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 44b1498a-f490-35d3-b591-c8f680b360f3 | -14.1828 | -52.8878 | 2026-08-18 03:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f7820d9a-67b6-3c52-bab7-35f8e41fcb18 | -14.1821 | -52.93 | 2026-08-18 03:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 053c936e-bc5e-348d-8aa0-3e6b81cac53c | -8.5855 | -50.3331 | 2026-08-18 03:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 43dfde3a-3915-333f-aa56-01bb73c13629 | -6.7477 | -59.1909 | 2026-08-18 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 582e0d95-d489-363c-aaf8-1c1b2d06c42b | -8.6042 | -50.3315 | 2026-08-18 03:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 458fcac9-dcdf-3ff7-a7e0-77d729773399 | -14.8228 | -46.6419 | 2026-08-18 03:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 3f83daa7-ed75-3897-a8ce-68023ece2c1a | -14.2755 | -51.9447 | 2026-08-18 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2095195d-490f-3db5-a3fb-0baebda44636 | -6.8594 | -59.0125 | 2026-08-18 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 596947ea-c54e-3bee-8358-3cae4094a6de | -6.7478 | -59.1716 | 2026-08-18 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 467ce4fe-081c-3dce-8166-d61bcb5a1092 | -14.2759 | -51.9234 | 2026-08-18 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 28a5bcc9-4562-39c3-b341-1a7b70963180 | -14.1821 | -52.93 | 2026-08-18 03:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| f5a0ceb3-6ebf-3c58-8a49-8d0e83c036a6 | -14.1824 | -52.9089 | 2026-08-18 03:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| b9eb9efb-d175-39c4-b7e0-983f06660eb8 | -6.7478 | -59.1716 | 2026-08-18 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| fa6d0e53-2b85-3c81-8a41-a299d29fb8e9 | -8.5853 | -50.3543 | 2026-08-18 03:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 157e1892-6e8d-37b9-8ac8-701cdb7e9982 | -14.1631 | -52.9113 | 2026-08-18 03:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a8940382-794c-39b1-ba9f-4e70d7b5b5de | -6.7663 | -59.1708 | 2026-08-18 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 127a2793-60c1-3de3-b1ab-191efeae56ab | -9.4254 | -60.4545 | 2026-08-18 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e54fe42f-2130-36d4-9e0d-4ba5af9800f3 | -8.604 | -50.3527 | 2026-08-18 03:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 4a5cbd07-74ff-3ef7-9a72-d9a9e061337b | -6.748 | -59.1523 | 2026-08-18 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 34f7373a-aeb3-3c9e-a957-4562eec2dd62 | -6.841 | -59.0132 | 2026-08-18 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 43c69b26-0e1d-3792-ab95-8f39a802eeee | -8.6042 | -50.3315 | 2026-08-18 03:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f3fff3c0-9227-321a-83eb-b59a083322b7 | -6.8594 | -59.0125 | 2026-08-18 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 404fed81-2cf9-367c-bb89-616a26f8025d | -8.5855 | -50.3331 | 2026-08-18 03:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a0584479-d027-3e11-98a6-cf533dd50586 | -6.7477 | -59.1909 | 2026-08-18 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f87f8d66-1551-3d64-ace5-8780bed54758 | -9.4256 | -60.4353 | 2026-08-18 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e86471f5-8a6e-3995-bb51-f15eeeee18a6 | -14.8228 | -46.6419 | 2026-08-18 03:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ae5afa1f-5326-389b-93f3-96908f4bf886 | -8.57 | -54.73 | 2026-08-18 03:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78bf354-e190-3759-84a6-077532329217 | -8.6 | -54.74 | 2026-08-18 03:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f43bd2c-7daf-34fe-8a47-40da85991dd4 | -6.42727 | -35.07077 | 2026-08-18 03:17:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| e31cba70-1488-3b6b-8c42-cd6aa0d606bd | -4.15328 | -38.41839 | 2026-08-18 03:17:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9cbe5364-33a2-3124-867f-6f63a70873dd | -4.99178 | -37.09793 | 2026-08-18 03:17:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 341bcfbf-08ae-3d2b-b3f2-17808866fe2e | -6.42818 | -35.06557 | 2026-08-18 03:17:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| cd786e7e-222d-3375-8880-902f23969707 | -4.9911 | -37.10179 | 2026-08-18 03:17:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 03f0b36c-6903-330f-b606-41d174b01ac9 | -15.43411 | -41.3869 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2f86b2b-c713-316e-b4a1-d5b723a47513 | -17.9753 | -44.43081 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2979bc2-fd62-34db-8c76-fdecbe3a68c4 | -17.98068 | -44.439 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 406e67ae-d46a-307f-be68-58f61a738821 | -15.43476 | -41.38794 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 226ae93e-778f-39f3-881e-05fba99a6f31 | -15.43372 | -41.3928 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 449f8ba7-e8b1-34a4-af8e-12837cbce216 | -17.98236 | -44.43188 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e84f5be-78b0-3c2d-b429-c6f6b41abff5 | -17.97909 | -44.43824 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef1fcc24-175a-33c8-85a6-e5b217b19da5 | -17.97892 | -44.44644 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b7bf16ca-9f24-311e-8c24-a8d2ce7d69fe | -20.61949 | -45.92505 | 2026-08-18 03:19:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 686d45fd-a55c-30ac-a8e6-57322e43d1c0 | -15.43304 | -41.39177 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ee34de13-8ddf-37ef-a339-c312715da015 | -15.4402 | -41.38838 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51a32968-6134-384d-8793-9ce69f88ec63 | -17.97355 | -44.43818 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb9b563e-faa6-373b-92b7-98d74b33c988 | -17.98081 | -44.43118 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12c200ed-b7da-356b-b47d-60e88bb838b6 | -15.44084 | -41.38947 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f415c88b-510c-3f23-8ddd-9f0641513a02 | -15.43913 | -41.39329 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e237b49-5653-31d4-aac1-ee858754556a | -15.4398 | -41.39439 | 2026-08-18 03:19:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| baf89589-9e1b-3dd5-9960-e5439ffb1ca5 | -17.97728 | -44.44572 | 2026-08-18 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c9377e7a-df19-3d37-9bd0-9711dede46a7 | -6.7478 | -59.1716 | 2026-08-18 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 25178dcd-5d3d-3e8e-94b3-1e4f4127c0fa | -8.6042 | -50.3315 | 2026-08-18 03:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 36bddefa-e9de-3314-9958-09c484371186 | -6.8411 | -58.9939 | 2026-08-18 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 9c54624f-f029-3c0f-8274-16af26c6f238 | -6.7477 | -59.1909 | 2026-08-18 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| d48f69ef-b7a1-36f1-ab0e-fd05bd30c9d7 | -6.748 | -59.1523 | 2026-08-18 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 81134e9b-d21b-311a-9ea4-93ca3693c479 | -6.8594 | -59.0125 | 2026-08-18 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| cf0e09cb-81b3-3672-849d-a69fedaec77e | -8.5855 | -50.3331 | 2026-08-18 03:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f478f2ac-6d38-32ef-bf75-939bfe92102a | -8.5853 | -50.3543 | 2026-08-18 03:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7e17b8fd-2cf5-30bf-9d3d-30555c2c3cee | -14.1821 | -52.93 | 2026-08-18 03:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| aa52b9bf-35e6-3bf6-a1e6-e451ce37132c | -6.7663 | -59.1708 | 2026-08-18 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 815397d0-dad2-3157-95aa-f9015ce7223f | -21.3689 | -54.6253 | 2026-08-18 03:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4314af87-cdd8-3b38-8f63-1e5c095aa6fb | -6.841 | -59.0132 | 2026-08-18 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 25608120-d4b2-3849-a2d3-56c96c362374 | -14.1824 | -52.9089 | 2026-08-18 03:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1fb07662-9f40-30e1-99a6-dcb1aca1a5ac | -8.604 | -50.3527 | 2026-08-18 03:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 3e1d7334-ef9f-3c71-bc70-430b437fe996 | -6.748 | -59.1523 | 2026-08-18 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e26e610d-0b4e-3078-b600-77a2fdc6d927 | -14.1821 | -52.93 | 2026-08-18 03:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 9d62b945-6ba8-368b-8fa9-af0e5cec6ad7 | -4.0185 | -48.9004 | 2026-08-18 03:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 63a42968-e91c-3008-af73-4501039dfa9a | -6.7478 | -59.1716 | 2026-08-18 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| c40b71c9-b06e-386d-87dd-609a1943d21f | -14.1628 | -52.9323 | 2026-08-18 03:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f8982bd1-507d-39ee-bc65-bc9cb311cbe0 | -20.2971 | -46.4536 | 2026-08-18 03:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 51.2 |
| e05fcaed-046b-315c-8792-6358edddd7ed | -13.5858 | -51.7781 | 2026-08-18 03:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4bb278a8-398e-377b-b80c-d21941ebb4e2 | -14.1817 | -52.951 | 2026-08-18 03:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d385f9f8-f9bb-3da9-afdf-0aaaefdcdd23 | -6.8594 | -59.0125 | 2026-08-18 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 7a876df4-cbf7-3f29-b655-ac2c332cd8f6 | -14.1631 | -52.9113 | 2026-08-18 03:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 19d3f2bd-fc0e-3dc9-a8dd-bb99d298d230 | -6.8411 | -58.9939 | 2026-08-18 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c03a3521-d886-37e8-9ea7-f9aad3be50ad | -6.7477 | -59.1909 | 2026-08-18 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 533d9c36-c60f-3064-85a5-6469721895ef | -6.841 | -59.0132 | 2026-08-18 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| bb868fee-0748-3b1d-b3e6-c04cdfd03c56 | -8.6042 | -50.3315 | 2026-08-18 03:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6a9c2d7d-9477-3e67-a3f5-0d3ccd8c79e1 | -20.3176 | -46.4486 | 2026-08-18 03:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 5dc26e9e-3c79-3390-a2de-4430b7d09cdf | -8.604 | -50.3527 | 2026-08-18 03:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 6b335a76-e1c0-3c51-8aa9-0003a5199a68 | -14.1824 | -52.9089 | 2026-08-18 03:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 64d9b241-f183-3433-a3cf-1b8b15643d39 | -8.5853 | -50.3543 | 2026-08-18 03:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b8e53f18-03d9-3df8-ad61-506a9976c279 | -6.7663 | -59.1708 | 2026-08-18 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 8577cee6-9d82-395c-acaf-d6c9ad4b1dc1 | -8.6042 | -50.3315 | 2026-08-18 03:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 29b2383b-fa6d-303d-8bfc-e2a67456ef38 | -6.748 | -59.1523 | 2026-08-18 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 2427feb9-d52d-3b9d-9f12-e4be093d7b6d | -6.7478 | -59.1716 | 2026-08-18 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |


[Clique aqui para ver as próximas entradas](README8.md)
