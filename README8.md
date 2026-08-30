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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eba7478b-095a-38cf-8cce-65cc7f19230f | -11.0396 | -57.234798 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5759914f-714e-3bfd-8b85-10348209feea | -6.3281 | -44.085602 | 2026-08-30 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e3698e7-f760-3f8d-aff4-2b9c386c50c2 | -8.5921 | -54.75 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afadd9b7-6366-3208-9610-40b61265b0ab | -10.7399 | -50.644402 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8481947e-f329-38d8-b2cd-5549a90640d2 | -6.95 | -55.6908 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71b7d994-7be5-3b46-b237-a7648f315ac9 | -19.092501 | -57.374699 | 2026-08-30 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7071abcc-72fe-3ebf-ba58-5e75757223f9 | -6.7808 | -55.670601 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb55d18-ea31-3e8c-9c1f-a9d03cdda908 | -13.8503 | -54.096001 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65b6041c-854e-301a-bd3f-fc77c43c9060 | -6.6141 | -55.433201 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f97fd654-ff88-3fd4-af27-189f7fb74117 | -8.605 | -54.7616 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4f45aaa-62a8-313f-8db9-67ca6e00f01c | -14.2005 | -52.848701 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 397cac75-e7af-3802-9cd0-09892b3278f9 | -14.1502 | -52.807999 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71415a31-8325-3420-8e2a-b8ff64cc46a3 | -14.2021 | -52.855801 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c827240-5d3a-3d48-abb3-5e4f0a5f5ef6 | -5.4844 | -57.144699 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5410e314-dbdd-3916-bc38-081b9d5c4384 | -10.7516 | -54.0481 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca1f2769-86e7-397f-83c5-2ed0bcd61da2 | -14.4343 | -52.560101 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30b1953f-9674-3d6a-b37b-b70d5d5d6ec1 | -5.4942 | -57.142502 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c81c1d-025f-3348-95a7-9a3842b77f1a | -8.194 | -54.948502 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d22e32d-fc73-3db4-b9a1-f43d8dc902f4 | -6.9417 | -55.699902 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51375612-2f0e-33b1-a192-a6649d03b843 | -14.2851 | -53.1796 | 2026-08-30 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 61fdd78b-aac1-3234-92df-825042dce4f5 | -8.5936 | -54.756901 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54be4fdd-e65c-30a1-941e-31baa06ef093 | -13.8632 | -54.108002 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9dbac2bc-09d3-3b65-8f31-ff783d96a10a | -6.6259 | -53.174702 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02889864-6274-3822-9b37-9f34c63a2345 | -4.9601 | -55.816898 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc9007e2-dd8f-3fe9-8bb9-38efdbfe758f | -6.7823 | -55.677502 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 386330cf-77bd-3553-bf29-db6a39316d7c | -5.9702 | -57.665199 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b50aad32-15f0-3129-93d8-96440ee05c55 | -9.0983 | -50.597599 | 2026-08-30 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4458c8a-f1ac-3024-ba32-2c95661b9f27 | -3.616 | -60.5298 | 2026-08-30 00:32:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b27a2d4-7e29-3bab-b8b8-c18af06763fb | -9.3103 | -56.782398 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34dae6fe-b869-3f9c-91db-f6abeaadc670 | -6.2545 | -55.391102 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e30eeb1-a825-3d8a-9476-adc19e1b684a | -4.6981 | -55.659698 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0d7901d-8d67-3d6e-b2a2-0adb4e5c0ed6 | -6.0932 | -57.7099 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36b99a5e-1d4a-34ec-9f2e-49d1fe84e9d9 | -10.7444 | -50.8381 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79c0570b-a58d-3f02-924b-7b7b2be67718 | -6.7875 | -55.654598 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4910dc8-3038-3d73-850d-774d03747844 | -5.4812 | -57.130199 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60cc74f0-a5f3-308a-a1b8-eb3313999b12 | -7.5218 | -55.3022 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 067a67fe-52a0-31b3-afb9-0e5c665a3dd5 | -11.0027 | -50.533699 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c10d76e4-75e2-3c08-a55f-5887c0cc8db5 | -14.2475 | -54.6422 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae1d600-0e3b-345b-9359-e2adca221b1c | -6.8653 | -59.454399 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6238d670-4806-369e-8b3a-de3d31be94c3 | -7.5006 | -55.299702 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 896e893b-6223-3e3f-96d8-8ce27ab94162 | -9.7045 | -60.702 | 2026-08-30 00:32:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d91a28d-562d-38b7-b1ed-b40a1f85fe45 | -14.3951 | -52.569401 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8553cb6-2d98-3b53-9b69-4dfb56ef8dc6 | -6.1823 | -55.4361 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e69a516-cdde-3352-835f-4e3f36eafe5d | -7.3158 | -60.596802 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b521966-b35d-37f3-9995-4622c137c3d1 | -23.202 | -46.962601 | 2026-08-30 00:32:00 | METOP-B | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8363c355-1d32-38d8-80e4-a93a8482c3ed | -8.5575 | -54.779499 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0349f385-de5f-3fe1-9f20-6e1bd9986cd0 | -13.8518 | -54.1031 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 68949ecb-4d5a-31dc-90ff-a4ce5f3b96d0 | -7.3231 | -60.583401 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7daca720-22b1-336f-bad7-c7a6c65e8af7 | -9.7143 | -60.700001 | 2026-08-30 00:32:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2e892d-d5a5-35c7-9eb9-c254733e188c | -10.9887 | -50.5182 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e1dd3e6-0a64-3497-b44e-1d712b5d0729 | -3.6378 | -60.5354 | 2026-08-30 00:32:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2574ec5-a898-3483-a05f-8005c71d7431 | -11.2099 | -53.979698 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f0f3335-41eb-3090-8a67-8c8207d373e3 | -14.4017 | -52.552799 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 016926c9-0acc-3125-be38-7fe65947b499 | -8.503 | -55.270802 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4760e12f-890d-38b5-9346-700b610bf291 | -9.1231 | -50.5718 | 2026-08-30 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e538ed7-c978-3081-9cf3-381e3ac4ff0d | -5.491 | -57.128101 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d53bb6e-32ad-3639-ae35-0e3f8b88f098 | -11.2357 | -54.003101 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d310431d-0b0c-3311-a753-e22ba1973265 | -5.4828 | -57.137501 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af162d4-da04-3729-a287-19307c359c41 | -13.8761 | -54.119801 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44ffa5a7-c3c0-3874-875b-a8a5a23419a8 | -7.3427 | -55.147099 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 533c93ee-c81a-3655-a063-68bcd1fbb569 | -5.8938 | -57.737701 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f89bbaa-d33e-3b55-b98a-11d2d303e71c | -6.8436 | -59.4492 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4338e345-a3a2-3952-abc2-8697720193e2 | -5.8856 | -57.747398 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb000aa3-b781-3bda-ae95-365ed5c96f9d | -6.5496 | -55.2384 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2966456d-b872-3d26-948d-730ac852ba45 | -7.5151 | -55.318199 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 679482ab-c31d-3b17-92b1-4859c616950e | -5.755 | -51.683498 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0375a01b-5c43-3285-96bc-3bcffe73234f | -11.8267 | -51.094601 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46b9fcbc-b2e9-3013-9227-8570d243be30 | -16.1334 | -43.034801 | 2026-08-30 00:32:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f39e255f-1b91-3408-9cf9-911a23310588 | -8.5518 | -54.708302 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7d62f85-b083-30f0-9565-c80514a2fac6 | -11.0326 | -57.202099 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c16522d-e55f-378f-935c-e82d8a39c270 | -14.4099 | -52.543301 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbf6c6c-cb2b-3324-a28d-ef99522e963e | -8.2476 | -54.958099 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0863b86-5a0e-3e99-a1c0-f8a565dbc5c4 | -6.3235 | -54.739498 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af9931d3-00a8-315c-a1eb-3afe06ffde6b | -14.8893 | -47.721298 | 2026-08-30 00:32:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f60b354a-3b41-3ac0-be7a-e8c4ec4a5f34 | -16.1273 | -43.0126 | 2026-08-30 00:32:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8128ada0-901e-346e-a698-e6fe2476aace | -14.1908 | -52.851002 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0511d61-e739-3555-a667-63a3384a862b | -13.8445 | -54.023201 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 912c432d-db59-3d24-916f-c4fd734e4532 | -5.4926 | -57.1353 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6908c55-80f9-3e41-8185-aabc45fed0dc | -5.8601 | -57.539501 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff0cde2-11f0-354f-8653-969cce36d17f | -15.4567 | -52.799599 | 2026-08-30 00:32:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e389fa7-c1da-32fe-af9f-a6fe9cf3aa5a | -19.090401 | -57.363998 | 2026-08-30 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c41b11a-5b08-308b-9b4e-f523de391d12 | -8.7561 | -50.459702 | 2026-08-30 00:32:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66e64eb9-91c5-3e25-a1eb-2fb6513c3d74 | -6.3377 | -44.083099 | 2026-08-30 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 919986a7-29ae-3ea2-aff6-3cfe0c5c52bc | -22.015301 | -56.0163 | 2026-08-30 00:32:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| be0616c6-7b7f-3402-8829-a9fcf77e3bb2 | -10.7385 | -50.682201 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 61923749-6ef3-3c1c-877f-895166abef3f | -6.321 | -44.057701 | 2026-08-30 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 641dc92b-d529-30bb-ae54-a4d6e11b23a1 | -14.1616 | -52.812801 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e55f58b6-3dcd-307b-8c63-5eead8a389cb | -6.7436 | -55.6427 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7912eab-e7e7-3d62-a5e1-75d470f8b0d1 | -7.0165 | -59.632801 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5a96c4c-eb94-30b3-ad37-44597f91e81e | -7.0089 | -59.6446 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6f94b33-e197-33bb-b4d2-a68d1c69283b | -5.8695 | -52.0872 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b335a94a-ac9f-3f8e-ad18-b6e55a2b6c82 | -3.4918 | -54.657001 | 2026-08-30 00:32:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba49bef1-b1f5-3ed6-ab49-1308458acf96 | -5.9834 | -57.6782 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20444f63-e19c-36ce-8501-0557d8a48a55 | -7.5156 | -55.2747 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc8b128a-2375-373f-8c2c-386eac0f551e | -6.6472 | -53.1777 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3418c764-b3d2-36f0-b316-6825147b02ea | -10.8079 | -50.495602 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a617fe15-58eb-3712-9cb6-a1cea636a461 | -12.5522 | -55.729198 | 2026-08-30 00:32:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c29e896a-72ca-3e40-8515-aa7b57bad9b2 | -6.4273 | -55.518299 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acfb7246-b884-3e38-a45a-66e3083bec3f | -4.9266 | -55.759701 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc8ec286-8530-3e8d-aa99-d6150631cdac | -9.1253 | -50.5811 | 2026-08-30 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
