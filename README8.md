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
| 2183abe5-2e46-3751-80ec-224661d52c93 | -14.34442 | -48.03893 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcb49a07-317b-3331-bb8a-a358db437322 | -14.06836 | -46.25734 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e60d8a0f-5de9-325a-b577-320996ef5815 | -14.07464 | -46.25889 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 527f145e-a19e-377b-b40e-506b7ee62797 | -14.07401 | -46.27123 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 36252eb5-798c-3987-9c6e-c4c246dd9379 | -18.86708 | -41.98882 | 2026-08-01 03:38:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| abf82242-1072-3c10-a4da-07d9a3e370ae | -14.07359 | -46.24269 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a685073c-3edf-367f-a51c-377841d79808 | -14.34315 | -48.04453 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 643c6d30-63bc-337d-8335-fc528105f9ae | -15.4434 | -41.37904 | 2026-08-01 03:38:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c9fff4c1-c2a7-3f7d-bf74-d835c1d8dd36 | -14.07067 | -46.24632 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 780ce5d4-8138-3538-9675-73ee083c7fa6 | -13.95441 | -47.8314 | 2026-08-01 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9dd1c3e4-1f50-3a21-b6c6-e922dc50b3ee | -15.44246 | -41.38397 | 2026-08-01 03:38:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4a878465-753f-3e23-ae6c-0a4e97f3d774 | -14.08454 | -46.24313 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bb254633-255a-31a2-ac4c-6f285b246586 | -14.06765 | -46.27004 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1eaa8e96-2b23-368d-9890-0aa838c60e35 | -14.08037 | -46.27245 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6b3c5a75-200d-3a16-be48-72096c5ba745 | -14.08587 | -46.23679 | 2026-08-01 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f1dbd61-cd3f-3612-bc0b-9eb148138592 | -14.35384 | -48.03823 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fcc0927a-19a1-327a-a6dd-9e0a7a531e91 | -18.97572 | -41.0307 | 2026-08-01 03:38:00 | NOAA-20 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 07c8f6c7-4495-3e5d-bbc1-aaf0878f907c | -15.02263 | -47.05921 | 2026-08-01 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a71b485-3c00-3994-b2b1-49118556769f | -14.07238 | -46.24825 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbfde591-3f8b-3533-be75-83202fda6ed7 | -13.95465 | -47.82401 | 2026-08-01 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bf57257-4157-377f-996e-afefb9c4e28e | -15.63677 | -46.43913 | 2026-08-01 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b9add37-6ef1-38e7-ba26-115766ca24ee | -14.07961 | -46.29837 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2f5784ce-2907-3c28-8585-f5515b338cbe | -18.51198 | -42.89596 | 2026-08-01 03:38:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1b02533d-072c-3a1a-89d4-9813bdc36920 | -14.07767 | -46.27598 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6475693d-ae5b-370a-9bbf-d09cf7bcefb8 | -14.34419 | -48.04895 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9938441c-5f8e-35e3-9bc8-1e7569459368 | -19.90653 | -42.24969 | 2026-08-01 03:38:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72d49f3c-b302-3974-8f0d-3b90e9528240 | -14.07659 | -46.28117 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e41793bb-9198-39fc-8a32-519a561fac4c | -14.06949 | -46.29208 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 984bce19-f7ea-32f7-beae-d842c6a3ed7a | -14.0929 | -46.2407 | 2026-08-01 03:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 1df7df4a-22ce-3454-831b-175b5678544d | -14.0925 | -46.2637 | 2026-08-01 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1edb45d8-da62-3019-a903-116020b22135 | -4.2578 | -38.0284 | 2026-08-01 03:40:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 111.2 |
| dcc6bb9b-8eab-36d4-8ec9-b7b5dd54862f | -11.2399 | -54.8737 | 2026-08-01 03:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| f14b3241-e5c3-3b0e-80fb-bb1b5fdac063 | -14.0735 | -46.2439 | 2026-08-01 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| df66adb5-8483-3fe4-88a0-ab33f25e2848 | -11.2402 | -54.8534 | 2026-08-01 03:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 25e1ec89-6b0c-3121-a13c-eb416d785af5 | -11.2588 | -54.8721 | 2026-08-01 03:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 8a1f39c3-8f11-3459-abe2-8402e46cd2d0 | -11.2591 | -54.8517 | 2026-08-01 03:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6e3e97a1-6b89-3a00-add7-ad0dd59cc461 | -14.073 | -46.2669 | 2026-08-01 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 721b46c1-6ede-3660-9715-1f2c356313f8 | -14.0725 | -46.2899 | 2026-08-01 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| fd23a3a1-5488-3fb1-879e-5d9f145e41e6 | -14.092 | -46.2866 | 2026-08-01 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| f83d1d94-4db6-3159-93cb-f056e31ab1f4 | -22.12873 | -43.24951 | 2026-08-01 03:40:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5cee12ab-b6ab-30b0-92b1-cf3ff61065cf | -22.55131 | -42.11772 | 2026-08-01 03:40:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 325511f4-686a-305d-b8d2-f7c25a15a10b | -22.23138 | -43.11474 | 2026-08-01 03:40:00 | NOAA-20 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 68a12d7b-4b1d-3238-a263-453bbe339812 | -22.55211 | -42.11358 | 2026-08-01 03:40:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a78e6169-ec6d-32ee-9ad4-5144bd0d1492 | -22.23039 | -43.11965 | 2026-08-01 03:40:00 | NOAA-20 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9eed7c6d-da56-3a9e-87ef-fd11f4b35f43 | -22.12775 | -43.25425 | 2026-08-01 03:40:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0fbe0906-99b6-340c-8107-9df01ab10087 | -22.67262 | -43.78807 | 2026-08-01 03:40:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1e2af6c8-9914-380a-aac9-9087cc183fe0 | -28.2938 | -49.9893 | 2026-08-01 03:42:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a489b626-0e7c-3668-8a35-3a9c61f04930 | -28.29512 | -49.98415 | 2026-08-01 03:42:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 84579f08-014d-3215-a3e9-71bf1c3b9e9e | -14.0725 | -46.2899 | 2026-08-01 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 2e612d43-3e58-3adc-b92a-94834bbfc150 | -11.2399 | -54.8737 | 2026-08-01 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 95ef6201-1e28-3856-aa89-20665fefe48f | -11.2588 | -54.8721 | 2026-08-01 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9f324025-526c-393e-862b-6f18b545c9ed | -14.0735 | -46.2439 | 2026-08-01 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e6459f01-2c92-3739-bc7b-a968d84ee170 | -14.092 | -46.2866 | 2026-08-01 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 8ea0e6cb-5611-3c5d-8ca3-b26a05c6c406 | -4.2578 | -38.0284 | 2026-08-01 03:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 99.3 |
| cf5e8be2-ddaf-3b24-b572-a9d097b056d7 | -11.2402 | -54.8534 | 2026-08-01 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 898e4d81-00eb-3ef0-8f5b-50ec16435e44 | -11.2591 | -54.8517 | 2026-08-01 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ea9a188e-d3e2-3464-b9d6-ed81c0e80d0f | -14.073 | -46.2669 | 2026-08-01 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| fc1d19e8-2cc9-37a9-9e8c-c646aea2d6f0 | -4.2576 | -38.0541 | 2026-08-01 03:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 9dfd7e88-30b1-3eb6-9ae3-c82bccf4cfa2 | -14.0925 | -46.2637 | 2026-08-01 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 26da2765-00b8-3d5e-86e9-56be29b08b99 | -11.2399 | -54.8737 | 2026-08-01 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a8ce8cf7-49f7-3ec7-a567-71ac40f2939a | -14.0925 | -46.2637 | 2026-08-01 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 41758fed-351a-3b7d-8b26-7db2254cf5e0 | -14.073 | -46.2669 | 2026-08-01 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| f6a1fa7e-f0df-378f-826d-4ca25d99709d | -11.2591 | -54.8517 | 2026-08-01 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 02232e8c-c267-31a5-bd6f-35b234e24a30 | -14.092 | -46.2866 | 2026-08-01 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| cc4fff9b-aaa2-3737-b990-43da066a388c | -4.2578 | -38.0284 | 2026-08-01 04:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 47ef8dc1-d64f-3aa3-8dc7-6d712b65143d | -14.0725 | -46.2899 | 2026-08-01 04:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6c9ef65a-e3d9-3e2c-97a2-f2d94342db5e | -11.2402 | -54.8534 | 2026-08-01 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| fdb56c80-6bc1-3db4-bac2-c5cfd88f3f8c | -11.2402 | -54.8534 | 2026-08-01 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e89c310e-fb70-377b-a957-f449d24d7379 | -14.073 | -46.2669 | 2026-08-01 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 568a3244-5a35-3387-904e-c0c557ea2cbb | -11.2591 | -54.8517 | 2026-08-01 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0ffa7e42-252a-34fa-96bd-54a1cc398f7c | -4.2578 | -38.0284 | 2026-08-01 04:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 0382e442-02d3-3b0a-880e-e9357570f7dc | -11.2399 | -54.8737 | 2026-08-01 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6a940534-5f77-3827-a714-5631edd5688b | -14.092 | -46.2866 | 2026-08-01 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| d4b5a7d0-b5c0-3328-8682-108e601795b1 | -14.0735 | -46.2439 | 2026-08-01 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ceeecea6-0ab4-347d-a2c9-14cc587415a0 | -14.0925 | -46.2637 | 2026-08-01 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ee34319c-9004-3ffd-9afc-bea2ef2e740f | -21.2623 | -49.1436 | 2026-08-01 04:10:00 | GOES-19 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| e7435a70-8c73-3902-b527-59a70b74bc39 | -14.0725 | -46.2899 | 2026-08-01 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ae0c7cee-d441-32fc-b118-ded77aba31c1 | -6.64371 | -44.58255 | 2026-08-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6899035c-0b7a-3383-befd-aa1695204fb5 | -5.63812 | -47.10423 | 2026-08-01 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00140262-a9da-3d01-8a09-a3a6b94ef7db | -6.27746 | -41.8768 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 94754723-08ec-392f-8fbf-ffbe6077453c | -7.5515 | -43.98987 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d71e5196-10ed-32fc-b3c0-0eaa0d6025ef | -6.19253 | -46.69375 | 2026-08-01 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9045d0b7-cf90-378e-8dec-c7ca1b89053f | -3.85491 | -44.10201 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1e0c007-b2a9-32be-96fa-08a8d516b46c | -3.05516 | -48.74437 | 2026-08-01 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c61fc707-93e0-3772-96b2-910e0ac5450f | -7.04215 | -43.21157 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13aae4ed-05e2-365c-9dab-3c574d54a341 | -7.34322 | -43.00786 | 2026-08-01 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d567dac8-c95f-3350-bdb3-1e513414902d | -6.56219 | -55.16236 | 2026-08-01 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fda1d84a-848b-3b15-bb61-b1764300d743 | -6.01101 | -47.401 | 2026-08-01 04:19:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a8b597d-d097-3094-a74c-3550fe41e206 | -3.03297 | -48.41115 | 2026-08-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81b865e2-3a0c-3923-a584-22ecd32ba9d7 | -6.76027 | -41.00805 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| fbc4c1fc-7131-37cb-86b0-52ccc43ede5b | -5.81746 | -44.75629 | 2026-08-01 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66e418ba-2f0b-3290-9d1e-8e69aaf90bcf | -5.55809 | -43.9768 | 2026-08-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 68beb34c-9d04-3b20-b91a-19267f19e696 | -5.55442 | -43.97635 | 2026-08-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fedc63c-c39c-3826-b52a-57d45e1aa2f1 | -4.26519 | -38.03723 | 2026-08-01 04:19:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 71b5b7e3-6d8a-3d3e-b81d-e43b30d67dd0 | -7.14377 | -43.65483 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33734d38-3457-395e-9275-dc73c224e382 | -7.60387 | -42.58489 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5d1e8aaf-5f1f-35bd-b02b-078950dad79e | -5.66583 | -43.56482 | 2026-08-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4e7996e-56d2-34b7-9b89-14320788527d | -6.5564 | -55.16152 | 2026-08-01 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 622eae3b-51ea-32ef-9f44-3382dc8d1c4b | -2.88685 | -48.01813 | 2026-08-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a83a8888-fa23-3a5c-adb3-247e13f9914e | -6.54333 | -41.86438 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
