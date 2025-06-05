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
| f60cd97d-5ac5-3960-b209-e6e482cc23dc | -13.52397 | -56.56123 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 47ad07f7-d421-3cf6-9035-a27723b929e2 | -12.12435 | -54.65988 | 2025-06-05 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d56728d1-b87f-3844-ba4d-596557494d52 | -13.06986 | -46.74824 | 2025-06-05 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b415b50-c4bf-3fab-a95c-fc3ee0cfb979 | -13.52559 | -56.57253 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d04a73e-0a3a-32cc-9941-2165ec71f198 | -12.66888 | -58.21554 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e95122f0-ba47-3fc4-adf3-e5cba12859d4 | -11.54441 | -56.42953 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaffb9a5-078b-3b84-84cd-814bc518db84 | -13.53008 | -56.56592 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bf38480-baa6-3497-9903-e2c70b2a7443 | -18.8394 | -53.61925 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51a634db-484f-3f4e-ae7b-ffaee58eb5e8 | -13.71638 | -57.48655 | 2025-06-05 05:01:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 328515cf-785a-32f0-8655-d407a0a04587 | -19.39977 | -54.47032 | 2025-06-05 05:01:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 355ec02b-2911-310f-a8a2-8d2e85433d5a | -13.53342 | -56.56648 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 581b30c4-1f7f-3821-b865-eed63f022a0c | -13.50774 | -56.5769 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b01e4fe8-ec1b-3aa8-9edc-281b39ce2972 | -19.06396 | -53.44334 | 2025-06-05 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59e6d02d-d1dd-3906-b3ed-54a195fc8a1c | -11.89252 | -56.41252 | 2025-06-05 05:01:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f011c9f7-0939-3bb6-b6bc-425ee7791516 | -13.52836 | -56.57667 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36405706-ede6-39ee-a47e-8b8efb94366e | -11.54777 | -56.43009 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dff54f12-5726-350c-b2b3-46dacaed7645 | -14.22728 | -45.48726 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cbfd830-3e5d-30a8-a446-9e12965dfa3e | -14.72754 | -45.09402 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9daa398-dc58-3379-ade0-9805325ce7ab | -13.52063 | -56.56067 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f7ad9e16-ade3-3274-8e99-ee0b742ef458 | -18.84369 | -53.61539 | 2025-06-05 05:01:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9daad71b-3247-31e4-b76f-1ba140ee4b9c | -12.17235 | -54.32316 | 2025-06-05 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 457c7e4d-5ec8-3d91-b316-4ee0f7de8697 | -12.65163 | -54.1263 | 2025-06-05 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 854b8740-04bd-301e-91a1-2de78720717f | -11.54718 | -56.43367 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a873bc8e-7bae-38c3-ae9c-5a17d7ace8b2 | -13.51223 | -56.5703 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6738e917-4124-3acf-afa0-f5f74dea6d4c | -11.5326 | -56.43864 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10257c40-c078-3c85-8caf-4254694e9004 | -12.64878 | -54.12208 | 2025-06-05 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 977e063a-3fff-3605-b35c-414fd08fa809 | -13.52893 | -56.57309 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83d5656f-01d1-3620-ba21-88316ef460dd | -11.54105 | -56.42899 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3890c80a-2ed9-3a2d-975c-72fd98fd9316 | -13.52778 | -56.58026 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 087e58ad-ad33-3aa9-a904-c28337ef009c | -13.52387 | -56.58329 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b3ebe7f-b629-38c8-b8c3-27affbf2c35b | -13.80834 | -59.68233 | 2025-06-05 05:01:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49545592-d782-3284-baee-28b3a78a6537 | -19.2843 | -55.15593 | 2025-06-05 05:01:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9667f997-373a-3aa6-8d2f-853d19e3b210 | -13.50831 | -56.57332 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a531110d-1623-3d67-adae-8541d8a50731 | -13.09446 | -52.03831 | 2025-06-05 05:01:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f49bb4fb-cca5-3ef2-ba15-f838e3805755 | -13.52168 | -56.57555 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| dfb6744a-17ea-37cc-b2f0-5403856f52a8 | -13.5128 | -56.56672 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b720ac3c-9fa9-337b-ae96-c455b3f0e3b3 | -11.54047 | -56.43257 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c27e5c41-a344-35d2-bb54-573a7ed565b4 | -12.66403 | -58.22287 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8e549354-f32e-3d82-9ed4-7d51073c3895 | -11.53931 | -56.43974 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fc42894-84c5-3114-be67-040054f1bf1d | -12.66754 | -58.2235 | 2025-06-05 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b1c8dac9-f252-3726-8399-f508949af0c7 | -12.37812 | -54.16079 | 2025-06-05 05:01:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42328a68-de28-3d93-9983-12f07bf22207 | -11.8253 | -57.8149 | 2025-06-05 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92fd1c1f-ac93-389f-afb4-1d3ad2f0cd33 | -12.08255 | -54.58739 | 2025-06-05 05:01:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3da047af-4746-3ad6-b53c-7f18b4590254 | -14.15695 | -45.48274 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfa1ea1d-872e-3c0b-9a34-06b1dbc4ecac | -11.54267 | -56.4403 | 2025-06-05 05:01:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e417ad43-3c48-3429-b21d-dc4d8526b2ca | -19.07627 | -53.46407 | 2025-06-05 05:01:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 712a29a1-49b9-3da1-88cf-4fffa7a3ec3b | -14.23235 | -45.4851 | 2025-06-05 05:01:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf226e78-f431-38a0-8ebd-1d1366e1b38f | -13.50278 | -56.56504 | 2025-06-05 05:01:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5367f49e-cfad-3b97-8a6e-30cefe04196b | -11.63123 | -55.37769 | 2025-06-05 05:01:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32103469-a7da-35bc-84d1-8810a8908dd6 | -14.7391 | -45.09952 | 2025-06-05 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66d9348c-7674-32b5-9fc7-d8748c3de05f | -13.71698 | -57.48285 | 2025-06-05 05:01:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b9e32ef-bb62-3cca-9d8f-b4114ba1a3eb | -20.37503 | -55.03705 | 2025-06-05 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 344f00a8-f3d4-3795-b555-7770713aff1b | -20.82143 | -54.95446 | 2025-06-05 05:04:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0fa9c3c-60b0-3359-9bbb-c7bb79bfb391 | -21.79708 | -52.76423 | 2025-06-05 05:04:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4e613a8-3048-328e-af36-0b336bdf7f18 | -20.8211 | -54.95361 | 2025-06-05 05:04:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d419329-15ad-3508-b55b-55fe9db34102 | -20.37853 | -55.03764 | 2025-06-05 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2d9d5db-3f73-30b9-9c1b-5c5e2efe2aab | -21.481 | -56.59653 | 2025-06-05 05:04:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58aab34e-9ac6-351d-8ce1-1604147126c5 | -20.37499 | -55.0398 | 2025-06-05 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d842b78-478d-3214-9bd3-1888541cb240 | -21.79776 | -52.75879 | 2025-06-05 05:04:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e81bc85-c953-33fd-93c5-b4367ff84246 | -19.43533 | -54.77747 | 2025-06-05 05:04:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6a793a9-bf27-345b-9a00-6ccaac4dcb27 | -21.95789 | -57.58539 | 2025-06-05 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560f748f-351e-3b4b-80c2-a32613cda310 | -20.19201 | -55.06293 | 2025-06-05 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7653660f-19b6-310e-8ef6-c5213a27794a | -20.37849 | -55.04039 | 2025-06-05 05:04:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2d6e7c7-f28b-3310-9bba-f5715f2f7ec4 | -21.80108 | -52.76483 | 2025-06-05 05:04:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71fe453b-f90c-3c33-8adb-03068f00ee11 | -19.43884 | -54.77802 | 2025-06-05 05:04:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a88f197c-ddb5-3500-b7d4-177b472ff2aa | -20.69363 | -56.66448 | 2025-06-05 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de1a2cad-8e21-3a72-bc0a-b46d1905f583 | -18.8479 | -53.6251 | 2025-06-05 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ed3c02b8-7673-3d14-ad3b-6e857f16eda6 | -13.5346 | -56.5469 | 2025-06-05 05:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| f191f1e4-96c3-337e-be91-1e2b11be9f59 | -13.5344 | -56.5672 | 2025-06-05 05:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 602698ed-31aa-3529-bb8c-5479f101d692 | -13.5341 | -56.5874 | 2025-06-05 05:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 13fb508d-d3a0-3978-898d-f9826a74b2e8 | -13.515 | -56.5893 | 2025-06-05 05:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b2406519-c17f-371f-b276-abf7ec9e20fa | -18.8479 | -53.6251 | 2025-06-05 05:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a69d2943-eea9-33f6-869a-4e63eff376be | -13.5152 | -56.569 | 2025-06-05 05:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 329.7 |
| b04b98b0-800d-32c9-a631-5730b61403fc | -13.5155 | -56.5488 | 2025-06-05 05:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d6a1f197-c46a-37a4-b7a5-91b7823278d7 | -2.53192 | -53.95728 | 2025-06-05 05:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4f5be83-4d81-3871-9fed-266cc39846c0 | -4.55505 | -50.30066 | 2025-06-05 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc5bedd0-f994-3649-877c-03996df69666 | -11.13133 | -54.22175 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b965ce64-19e4-30ee-9418-39bdc3159d1c | -10.64465 | -49.43726 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a319ab8-358e-323b-8899-ceb3fc5f5463 | -10.70211 | -48.78018 | 2025-06-05 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51a3fc3e-aa54-3f2d-b117-2050c300eeb6 | -9.96053 | -64.93581 | 2025-06-05 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24647ad9-5518-3fcd-b445-085d2753a148 | -11.70864 | -56.45084 | 2025-06-05 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bc0f9ee-677d-39aa-9d52-af3addaa2735 | -10.49799 | -53.66039 | 2025-06-05 05:23:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5cb71032-a26b-3d77-8839-b30379d2a0e8 | -10.30542 | -57.14271 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1591f325-d446-3bb9-8017-b46362657963 | -10.53965 | -56.38645 | 2025-06-05 05:23:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bbec6a4-824e-3462-bc79-9649e592e249 | -15.11326 | -59.32828 | 2025-06-05 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bf46609-5c56-346d-b8f3-57ed1d36dbcf | -8.95971 | -47.97366 | 2025-06-05 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e70ef4bf-8e7c-3aec-b382-9ad144e2a3be | -9.84072 | -62.37869 | 2025-06-05 05:23:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78479740-8523-3538-b28d-ac3692abc45b | -10.6849 | -57.59563 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b51ab1f5-e45d-35e0-b684-57bf9aa82b8f | -11.13451 | -54.21967 | 2025-06-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5367725a-bb03-3e49-88e6-7d88341aa748 | -10.69708 | -57.64408 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70b83c4f-1ab3-330c-98a7-b12e6a750237 | -11.54545 | -56.43287 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc988abe-c319-3734-ae73-861b1f3ae2c4 | -10.6497 | -49.43545 | 2025-06-05 05:23:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29ee60aa-b9ad-3a2e-b092-f5301351823c | -10.68893 | -57.64758 | 2025-06-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae6fc9b7-84b3-33a8-9b3b-313d0f8696b2 | -9.41153 | -62.44881 | 2025-06-05 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ed79ff9-1d12-336e-b602-35215afdcb44 | -10.29957 | -57.13927 | 2025-06-05 05:23:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f88dbe09-0d51-3eaf-85b2-6f0eca63bacc | -11.54441 | -56.44026 | 2025-06-05 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a01a051f-ebd9-3e1d-b694-6ba9d85ba414 | -11.62347 | -55.38166 | 2025-06-05 05:23:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02f2dda2-cac1-38e6-8411-27440ca019fd | -10.5615 | -59.20445 | 2025-06-05 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00d60267-b56e-308b-b274-5dffb120208d | -7.92721 | -61.5559 | 2025-06-05 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e93b0e4b-54f9-394d-af04-bd99235ccd66 | -11.55005 | -56.42978 | 2025-06-05 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
