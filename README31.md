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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0c8fa06-f459-3248-beab-da666f378338 | -9.51326 | -60.5317 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d985a7fc-7f74-33cb-9910-46ba30489347 | -9.51083 | -60.52192 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 958dc8cd-63d1-3b71-bc9a-84bc90d62399 | -11.35638 | -55.3941 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd141c5d-1d12-3c4f-800e-cb2b0d452f80 | -11.3185 | -55.21016 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a71b8f-a37a-39fc-ae19-f761967aee7f | -8.47051 | -70.83817 | 2025-08-18 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54b387ff-c517-3080-a61a-c069c0017f4f | -9.5146 | -60.52247 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e83dd95-61c2-312e-8253-c4e38947bdd7 | -12.98333 | -56.85263 | 2025-08-18 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96aa300b-9c16-3668-9273-51a5c51ec29b | -9.51703 | -60.53225 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e03ad834-7b8f-35c1-a520-f1b5319497a4 | -11.31253 | -55.21309 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db617db-d046-3d3d-9f5e-cf101a46a6b5 | -8.97299 | -60.50037 | 2025-08-18 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02030e98-7232-396f-91aa-f21d8fb4c3d0 | -8.87666 | -68.50768 | 2025-08-18 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87cd4d2f-c47e-3ada-8df6-fc2f5eb09603 | -9.51149 | -60.51731 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb6943ba-d1f4-3bfe-a7b6-7f299dcf845e | -9.52148 | -60.5282 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a0c0e8f3-2abd-3a18-ba4a-273f7b816f0d | -9.51569 | -60.54147 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f87f76e-78b0-3a6a-8eb9-2f6f78c77e79 | -9.51393 | -60.52708 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5953de0b-fecd-3bfc-9c7b-fa13b4ae81e4 | -9.52013 | -60.53741 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17be691a-6698-3bb4-a904-ba3bfbb3eab7 | -9.42877 | -68.59535 | 2025-08-18 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2a04af2-13ed-362f-a8fa-6ef3dc2e2a0e | -13.17199 | -54.92858 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a2a9a38-8e44-3c04-bb91-2ba22f9ce4ac | -7.97831 | -70.03397 | 2025-08-18 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7039280f-2aaf-3db3-93ed-a373bf393310 | -9.51771 | -60.52763 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f711bd51-773e-3963-b351-c290d848d175 | -13.16718 | -54.91986 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 405b68d5-d8e2-32a3-932e-6812100ce9ad | -9.51015 | -60.52654 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5605f912-bb9b-392b-98e8-068f920718d5 | -13.17152 | -54.93256 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47258d3f-8bf7-32fe-bd6f-e44cf8569de7 | -13.16624 | -54.92786 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e80e1e1b-1116-3f07-9df5-5b5f86f9cfaa | -8.87286 | -68.507 | 2025-08-18 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea7dc596-7e30-31ab-b5d5-a1aaa1b32c71 | -9.51636 | -60.53687 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66d0de4f-58c5-32c1-a962-3ec91d03c92d | -13.16576 | -54.93187 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7ef3979c-b9b4-32c3-89a9-58b3803e85e0 | -9.80401 | -67.86004 | 2025-08-18 05:36:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34d34949-b01a-3ea6-88a2-40d6da90fde0 | -8.87965 | -68.51307 | 2025-08-18 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91c34e24-a588-31a6-83d0-8ee90c1a8294 | -11.31207 | -55.21677 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72d57887-282a-3de5-b7a1-02788ff23e86 | -12.98411 | -56.84661 | 2025-08-18 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fb8df7b-3396-3185-afa9-79d6a1ee4198 | -13.14077 | -54.89558 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60385b2f-b5d4-3942-814a-37e970f9fd6c | -9.51527 | -60.51786 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66c19dac-b870-3985-9f7b-b858e7b46b7c | -8.97365 | -60.49582 | 2025-08-18 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64378e39-4cc4-3690-a6bd-7c947c434bab | -12.98372 | -56.84962 | 2025-08-18 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60e5aba9-5cbf-3f8e-8aa9-89f39ad4fd8e | -9.62821 | -65.37063 | 2025-08-18 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e12933d4-5147-3318-a255-7d7e742ba7ff | -11.31804 | -55.21388 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bc20e7e-a123-39ff-9746-2ed4e0e89d29 | -13.17293 | -54.92062 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd3e451b-1961-3ebd-bd63-b8f08ad0f6b0 | -8.619 | -62.61201 | 2025-08-18 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dfe5c9a-68c2-373f-ae51-0673c7508102 | -11.85256 | -51.59155 | 2025-08-18 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7a1663f4-6af3-35bb-9485-11af2c0aeca5 | -11.84561 | -51.59071 | 2025-08-18 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e951c84-a961-378d-99c8-bb2bf7408e43 | -12.9845 | -56.84357 | 2025-08-18 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b93113c0-c120-3926-8de3-03584ed681e6 | -11.35776 | -55.39196 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff33cfeb-4c6b-3869-9bce-27361dfed06f | -11.31161 | -55.22044 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48a3cf6b-02d5-3b3f-affb-451f70f55e58 | -12.98295 | -56.85559 | 2025-08-18 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 235c66a1-a7eb-33c9-8942-0bf808fe8644 | -8.35563 | -70.85862 | 2025-08-18 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3826cc1d-d551-3e74-b836-57f77a3e416a | -8.6156 | -62.61148 | 2025-08-18 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a733495c-870f-345d-96b3-0669f08e723d | -13.17246 | -54.9246 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7305325c-93c3-348e-b133-ae352baa363b | -13.16529 | -54.93585 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 03f9ef02-fa3c-37e0-81af-58c60929b63a | -10.00845 | -67.84893 | 2025-08-18 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01255a5f-12a0-30bf-95da-c0fb09b51ea5 | -9.50948 | -60.53116 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70c78f73-de4c-38ed-b3f0-e7f15ddbd2e6 | -13.16671 | -54.92386 | 2025-08-18 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d370f89f-02b0-3225-8691-a236b8f84790 | -11.35685 | -55.39049 | 2025-08-18 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2dc7bca-0a82-3700-a6fd-6c3de44f7133 | -9.42956 | -68.5907 | 2025-08-18 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0799c16-579a-3cb5-befe-62c984bacc64 | -9.52081 | -60.5328 | 2025-08-18 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37986925-109f-3fcc-8087-3060459eb395 | -7.89881 | -63.52428 | 2025-08-18 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 873a3555-a02e-36ca-925f-3596b2ac89ca | -8.35854 | -70.85699 | 2025-08-18 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8ff4d07-3611-3e7f-848b-b52a78092891 | -13.0145 | -56.84261 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d254fa5-7df6-395b-b16f-2af9f441bfe6 | -12.99166 | -56.86119 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 469e1b48-8a25-34fe-9007-9e43b7d6d947 | -13.00399 | -56.84445 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d40562b8-68b0-3f3f-9208-8b43c14823cd | -13.01413 | -56.84563 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b815953c-4c22-315c-a2c4-e4ff6d40ea84 | -14.63483 | -54.913 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d47780af-f85b-3eec-bc08-bf18baf7f3f1 | -12.99422 | -56.84025 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8954e469-ff74-38f6-9838-abaa974157ae | -12.98732 | -56.85471 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56414eac-b23d-3b57-bee3-44c95360aeba | -13.01301 | -56.85469 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8191d8fb-07f9-3a63-adb7-e25d84d8bbfb | -13.47498 | -55.76793 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e29222fe-591d-3569-9972-1b4657d9ac3c | -15.60841 | -54.30711 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad341e7e-5e58-39d8-b4fc-7accf42f43e5 | -14.98586 | -54.77474 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5695c645-9e57-3a26-b677-39f5fc78113d | -13.01376 | -56.84866 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00a2264-ac21-39cf-a6a6-9a34ec987067 | -13.00906 | -56.84502 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d4a46ca-c44b-3f23-9459-d1617f7fbdb0 | -13.13361 | -57.14983 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7eb01a35-d56b-3858-a46a-4df8486c09b8 | -13.01882 | -56.84932 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8760d60-420d-3d13-837d-3f7f66afb3f8 | -13.01844 | -56.85233 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4947d5fd-d178-3aaf-9f67-95b754c27c44 | -12.98878 | -56.84266 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 338c9006-44d3-3dad-b18f-3da01c947013 | -14.97357 | -54.77696 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34ca0f5b-9064-3391-bf7c-ee031a749c3d | -14.87196 | -59.60781 | 2025-08-18 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f63fba8-7ba9-3fc4-ac0b-6f925eab97ba | -15.60797 | -54.30754 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbf4bd3b-8998-35a5-b4a2-090192691a8f | -14.63531 | -54.90867 | 2025-08-18 05:38:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a93225c4-250d-39a3-a5e9-2cabd2b75dc9 | -13.14371 | -57.15855 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e9d5c28-358a-3949-9d6c-bf5cd01fa32a | -13.14302 | -57.16424 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8a9c5f2-706e-3fb9-a5b7-af1d7c8fe860 | -20.40522 | -54.69247 | 2025-08-18 05:38:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2d8d7bf-958a-3e9e-bfbd-235efb64402b | -20.40566 | -54.68719 | 2025-08-18 05:38:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 300ecccc-88ae-36b0-b3ed-c9e302d26809 | -13.01338 | -56.85169 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55f5d683-c532-3586-89f6-32bc37619f97 | -15.0453 | -56.03161 | 2025-08-18 05:38:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01a9c1b6-fdb7-3f00-bf73-c50cacd19df8 | -14.62844 | -54.917 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6bd7653-ea6f-3949-8ab4-adcc364bbc48 | -14.62352 | -54.90769 | 2025-08-18 05:38:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce5f59b6-bdc2-3967-9aae-dec64b19bf27 | -14.73171 | -59.67224 | 2025-08-18 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2db131d-a1be-3d84-adb8-5d8041b683f2 | -20.40862 | -54.6962 | 2025-08-18 05:38:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 949e5b90-7aa3-3549-9a50-9607390a991e | -13.01771 | -56.85822 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95c3c9fb-3422-38ba-adaf-c84c6025b043 | -13.00869 | -56.84804 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8692dcbd-a3d7-343b-94d3-7d22b3ae48df | -14.63435 | -54.91732 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cbf9449-61d5-3a21-b4bf-71e190a76b91 | -15.60844 | -54.30297 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ccf99c2-4b28-3cc9-84ae-f92bbdd52275 | -13.00325 | -56.85044 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb186448-dbad-3fb3-9340-547ae35682d3 | -13.00832 | -56.85105 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e51b7fb6-3113-36e2-a1d0-c798e69dc618 | -14.99123 | -54.78064 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4cfa2326-c84c-362d-b672-c59b0437b2a2 | -13.02426 | -56.84692 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 003c8b71-43e1-33e0-b30b-175183f32c5d | -15.00886 | -54.78459 | 2025-08-18 05:38:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8193f08c-8521-32ab-9a7b-87399760e79f | -20.40278 | -54.6899 | 2025-08-18 05:38:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50123af8-6811-3b0b-8c6d-813edc70a887 | -15.6198 | -54.31397 | 2025-08-18 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2924fe1f-3a88-3f65-b265-f6447f0e94b1 | -12.99275 | -56.8523 | 2025-08-18 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README32.md)
