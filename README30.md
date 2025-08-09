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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5a210c5-6f06-342f-b5e9-5ad5d11c3d11 | -6.93363 | -60.07004 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c43b0465-0e5b-3252-b6b4-6483594af3f5 | -7.40042 | -59.99403 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b8a9af13-a481-303f-a52a-8e49021869c1 | -5.88945 | -57.75184 | 2025-08-09 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ec98e88-8678-3ec1-9dbe-004c7a91a77d | -7.09138 | -59.18272 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a58e4c39-0d5c-361f-9de9-7a2d2c53d6c9 | -8.90621 | -60.54153 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9aee3d9a-b8b5-347e-8b56-141752034eb2 | -7.40477 | -60.00146 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe1ab292-d00c-35bf-b209-7433b260980e | -8.91827 | -60.54467 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ac94f19-0b88-3ed9-ab35-14ebcf626671 | -8.9346 | -60.73994 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1dcc8968-54f4-38f1-84a0-95ad03e7b52f | -7.0945 | -59.20142 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cce8e1e-f212-3b51-bf5a-320fe447b1b2 | -7.089 | -59.20063 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79c5bdb4-9bae-346f-a859-5dbd63d30b6b | -13.04786 | -56.84655 | 2025-08-09 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c466205c-1890-3c0f-ac3b-1579e1aca73e | -7.09641 | -59.18711 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e16e6ca0-0e91-3a08-8b3d-7bf9c79e391d | -9.93925 | -60.50703 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3126a50-dbee-38c1-a356-c1b426e6dcfa | -7.08852 | -59.20421 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eeb70c68-677d-3f47-adfc-ee3f552a78eb | -8.91866 | -60.54158 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b9d1a1d-0d59-3bf1-9c83-87abb6fe3fac | -8.9111 | -60.60048 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b1c3e4a-766e-3163-89de-adf1bb64c116 | -9.94344 | -60.47449 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c824bd92-7fb0-3b42-a84a-85358220a5af | -8.92247 | -60.75339 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 980e8918-bcb8-3a2b-b051-5b8fcebebf06 | -8.92286 | -60.75039 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cb72f86-fb35-35aa-9f54-7a39206cd728 | -9.93442 | -60.50305 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dce4b6cf-1359-3440-8ea1-59bc7747cf82 | -8.91094 | -60.54536 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d0cbda3-f13b-3c23-813b-1ba849474848 | -8.93342 | -60.74892 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fbf06dd8-d6a6-36d3-af9c-2f7e584d301e | -7.0056 | -59.66197 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5670a53d-b493-3764-bb3f-df3de2b19b14 | -7.09689 | -59.18352 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c3fa1a-12cd-3367-927f-7d53b9bb5400 | -9.9293 | -60.45948 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49e8617e-26d3-3e98-bd98-4c9903bdaef0 | -9.94135 | -60.49074 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91e453e5-ffec-34a7-9d5f-5bc29d222142 | -7.09498 | -59.19782 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| adf22726-d75d-36b3-a782-5790e36ec43e | -8.93421 | -60.74294 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e31f9fc8-b105-320c-8a2d-d971e4ef054b | -9.02967 | -59.75565 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80d9727f-59f0-3228-a3d5-59188a0a8877 | -7.39443 | -59.99549 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83d2a2bc-c149-3cb7-917c-9c1faac33c98 | -8.92951 | -60.73923 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 21c6ce94-4534-3fcf-8523-6289fb62e7e6 | -7.39477 | -59.99635 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e460b717-09fb-3773-84a9-c12685119f5b | -8.9161 | -60.5461 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7f39fb9-9d14-3fe0-b305-55c7dedd0dbd | -6.63382 | -59.99981 | 2025-08-09 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89246e4c-de39-3788-bd91-b7f73a1fa952 | -8.92207 | -60.7564 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71d03b37-86e9-3bb9-9173-317f5693d6c9 | -8.9058 | -60.54457 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7d93298-4c4e-3447-aa40-a3e20d1c05cd | -8.90538 | -60.54765 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16cb3796-bf12-3756-bd23-479cc2b6b20a | -9.93416 | -60.46339 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5cf92ca-54e8-3249-97ad-a853ed9e9796 | -9.94302 | -60.47772 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 948c7ec9-4e42-3866-9462-618fc1f30bb9 | -9.93567 | -60.49329 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 281ac1f1-f838-394c-8831-c023df4fc8f0 | -5.89006 | -57.74725 | 2025-08-09 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d3b9cfa-5a42-3a04-9d80-e573ff2baef4 | -8.91136 | -60.54229 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d8723b1-1768-3c01-b941-00c3586227da | -8.92677 | -60.76009 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6938d2c-268d-3444-bd46-4dbac0f234ab | -9.91878 | -60.45802 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 246322aa-7ee8-3b28-8dfa-927d46fd80cc | -8.92168 | -60.75941 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d105744f-4a43-3763-824d-e2d0cd8dea69 | -8.92873 | -60.74517 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7d55849-f3bb-3836-a5ce-f5f9826cb686 | -13.04718 | -56.85297 | 2025-08-09 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd40b176-e7c7-3ff4-b574-52839c77041a | -7.3952 | -59.99315 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad8590f4-fc72-3164-a962-29656505a465 | -7.09546 | -59.19424 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 65c29e20-a1ee-33f5-8d24-aef8678a8319 | -7.10096 | -59.19501 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab080c7c-3fb4-3241-971b-e4c884725303 | -8.9303 | -60.73324 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b2efab7e-e947-3f72-9c74-cc979f927219 | -9.94261 | -60.48096 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f9e952f-2482-387b-91fe-bf7971362677 | -7.39999 | -59.99724 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9478c49c-bc63-3d8f-9627-880816539a5e | -9.93358 | -60.50961 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcfd20c4-f7a7-3a3b-98c5-f31bfb87bb11 | -8.65925 | -63.40143 | 2025-08-09 05:55:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 344923c4-5045-3b1e-a290-bc3b50038f27 | -8.9299 | -60.73624 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0a2a8657-e410-36eb-a505-62b7f03a5356 | -8.92755 | -60.75414 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 51942052-c795-3da9-9a87-8eef359f12ab | -8.92716 | -60.75711 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2e15b7a-ebc1-379a-b5b9-0109d7d479a4 | -7.39435 | -59.99955 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdd74a5e-6c3a-3673-941d-4d0d39ec5230 | -5.88633 | -57.74995 | 2025-08-09 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9627e4e1-5ab1-38b2-9cbe-ee3850485b86 | -9.94177 | -60.48747 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e767ab5-9365-3376-ab50-cac4f3fcc46b | -7.39956 | -60.00049 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea4b4f51-f2c1-3511-bd01-30f5cdde7de5 | -5.88414 | -57.74623 | 2025-08-09 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ab75710-d000-3d26-9a18-9449619b4134 | -8.92482 | -60.73548 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14c899e9-f9b5-3b9c-a809-1b8180cad391 | -8.92834 | -60.74815 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e977bdf5-3968-3c85-9fc3-a31f5f335333 | -9.93609 | -60.49007 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b6bcc1c-e451-3fd1-9831-2e51740a808d | -7.4052 | -59.99819 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e58bdf3f-0aad-37c5-bbd9-7ace12faebf6 | -7.40392 | -60.00784 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 259eb297-4a57-3de3-a877-ece32d0512f9 | -7.09737 | -59.17993 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddfc5afa-1c6e-32a2-9219-0ae0417580c7 | -8.91652 | -60.54302 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae40ee9d-a6c4-32c6-b3e8-746028606e6e | -9.93776 | -60.47704 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e4bd14c-09d3-3674-bb1e-1189b0a328cf | -9.9365 | -60.48683 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f4dbd76-27a9-37ca-884a-be585fbdabbb | -9.93 | -60.49584 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 586f5d11-acdc-356d-ae66-fb515edca9b2 | -8.92912 | -60.7422 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1bcb0059-0d2b-39c0-8c59-1f9b45b9d4af | -9.93967 | -60.50378 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49a2f8d5-ff41-3820-b0d0-dda5bd646f79 | -7.09186 | -59.17914 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e547db7b-ceab-3320-9842-21499f8dd880 | -9.94618 | -60.49473 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6f6939e-431d-369d-9457-50859214ee52 | -8.92365 | -60.74442 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9578b5a2-3254-32df-859b-4e46e5882a8b | -8.91584 | -60.6043 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20b80e11-619d-3914-bcc0-74667a990d96 | -9.92598 | -60.48549 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78508f02-8a77-375b-8ebc-11bbb77fc0e6 | -9.55205 | -62.72031 | 2025-08-09 05:55:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 58c80259-a051-3e54-8768-99446ac168fc | -7.08948 | -59.19704 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 96047db7-1f6b-36e1-873a-925a4bede55e | -9.93883 | -60.51028 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df603621-aea6-3913-8b14-6636b4a87a07 | -7.39913 | -60.00372 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2110f224-821f-3ada-94f8-a4015ad083e7 | -13.6144 | -49.0079 | 2025-08-09 06:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| b4d12665-e6d8-3213-a991-0e4f4c109120 | -8.9399 | -60.7481 | 2025-08-09 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b23723a3-a912-3ef2-b1a1-c41dd22f633e | -8.9213 | -60.7489 | 2025-08-09 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 45342e1c-6f76-3742-8257-fd88d9c1f844 | -13.6144 | -49.0079 | 2025-08-09 06:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e3553c5a-73b4-34d1-a08e-4fdf43fa5b3b | -8.9399 | -60.7481 | 2025-08-09 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| b822e28b-8dbe-3368-9707-4190d5369523 | -8.9213 | -60.7489 | 2025-08-09 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 909983be-6560-3bad-94f8-103e852cfb56 | -19.8124 | -47.0634 | 2025-08-09 06:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 16221322-0d3f-3fef-b727-2a6a4d7f22bb | -13.6148 | -48.9859 | 2025-08-09 06:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 48bace27-5705-3e53-a817-c5a43b80a323 | -8.9399 | -60.7481 | 2025-08-09 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2a6259cc-d485-3664-80a7-d5a0f39532f8 | -8.9215 | -60.7297 | 2025-08-09 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2f68d412-914e-3804-a0a7-fef298745082 | -8.9213 | -60.7489 | 2025-08-09 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| cbe0586e-eb98-3e0a-9ad5-1bf509e667c0 | -13.6144 | -49.0079 | 2025-08-09 06:20:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 3e386aae-695a-3905-b2fb-249f9f2e73d8 | -13.6144 | -49.0079 | 2025-08-09 06:30:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 349eaabc-abf2-3fec-b816-abe82e05d0a3 | -7.08 | -59.1771 | 2025-08-09 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6ed45215-3e1e-3fdb-99de-80d0a05a63f8 | -8.9213 | -60.7489 | 2025-08-09 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ce1ca5a0-74df-39ae-8c87-e65501e99382 | -7.0801 | -59.1578 | 2025-08-09 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |


[Clique aqui para ver as próximas entradas](README31.md)
