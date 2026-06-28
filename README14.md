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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e390a6ca-6ca8-3f1c-86e4-9354e87efa35 | -6.9792 | -42.88845 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2a0cecfb-13cf-3909-9579-1ba0d4b0d05a | -4.34959 | -47.76388 | 2026-06-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 709588cb-02ac-3fe4-9457-e469e5ee2262 | -4.28475 | -48.36274 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37e11e4e-b323-307d-a7dd-bedfba2d3120 | -10.13423 | -52.11202 | 2026-06-28 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ac30e5f-c922-30f6-9113-c499fb544890 | -8.78662 | -46.92096 | 2026-06-28 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 779282d8-f7d9-3604-bf4b-ba0970e219fc | -6.99994 | -45.00317 | 2026-06-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2cd64101-dbfa-379d-a8db-c0686dffed87 | -10.13415 | -52.11257 | 2026-06-28 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c682ace-6000-3f06-9843-b68f693c9fa6 | -6.99903 | -45.0098 | 2026-06-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 64527c4e-8a29-3772-9e3a-247854a311d2 | -6.9779 | -42.89809 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f356add9-4275-3805-b0f7-2a095d0ad1a3 | -3.51219 | -48.03988 | 2026-06-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f583dbbf-b417-370f-bc45-724a274f83e3 | -9.16521 | -58.07098 | 2026-06-28 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80d8de17-3648-3da5-b941-123c66df4fa4 | -9.12 | -58.25417 | 2026-06-28 04:57:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30aee987-f994-34b9-9ec0-2ada0ed44654 | -9.19203 | -58.06662 | 2026-06-28 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37578e9b-3bf3-328b-986b-d89f06414704 | -6.98494 | -42.89386 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 6566a373-15d0-3dcd-aec6-bc58d9fc00d6 | -7.7504 | -49.46612 | 2026-06-28 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 562dfeae-e63b-3b27-a597-2b37bdd2a2ec | -6.97855 | -42.8933 | 2026-06-28 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 63e4397a-1f4a-3ae2-afc4-22c63c5deb28 | -9.02566 | -59.54101 | 2026-06-28 04:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b0f13b0-be2f-304a-bc79-cb1c78d82060 | -9.16885 | -58.07154 | 2026-06-28 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 563d72b1-d471-3866-a183-75061c72138a | -4.28883 | -48.3633 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 14c153d2-2738-38d0-9161-82d50d5dc109 | -3.5174 | -48.0332 | 2026-06-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8979ea59-056d-3f45-8ec8-acfede4ed6a6 | -10.78847 | -46.47877 | 2026-06-28 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa425585-9caf-3d54-9041-889d6881f508 | -4.28537 | -48.35824 | 2026-06-28 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 803f6d80-8f85-3947-85ad-2cc4842d96ea | -10.28876 | -46.66752 | 2026-06-28 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12bec6ae-09ee-37ba-9580-a817f12e3e86 | -3.50861 | -48.0356 | 2026-06-28 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810df23e-a74f-3113-ace9-aedba1c24c3a | -10.36574 | -50.18249 | 2026-06-28 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2fda4e9-b2f9-3066-8e12-4e9dcc14d182 | -12.19135 | -52.89262 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1ea2cb0-dcf6-3c9d-af7a-5f96d775398d | -12.08994 | -52.02455 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 293efe46-2427-3d0c-a8bc-ec8c82b9512d | -11.22093 | -54.30927 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b86aff9-c630-3032-ad6d-9f7b8dda71fb | -11.31006 | -53.94661 | 2026-06-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c88d35f9-512f-327e-a67d-dea454505eb9 | -11.95343 | -58.6149 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05e652fe-dfa8-3120-86f5-c694382bd91b | -12.18977 | -52.86922 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9d90845a-4962-3dbd-9d66-ff79778497fc | -12.19363 | -52.8768 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b50ff85-dd53-326d-b2f3-4c54ba1e3fa6 | -11.91987 | -57.40995 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eddacc88-db86-31c1-8b41-0a64405629c0 | -10.9353 | -56.85197 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8db4cb37-964a-392c-801d-67ac6c6176a6 | -12.1909 | -52.88558 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d9ecfad-0ef0-3c9d-a777-42141d780445 | -12.18855 | -52.90134 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f19c98e-ed44-3326-838d-0cb6f1cb2837 | -11.32651 | -54.46339 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 957a758a-2a45-368f-bb21-37a883501e6c | -12.58118 | -57.81515 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73e96b81-8741-345f-9f43-e1ae1c2777ee | -12.18247 | -57.15991 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ce0ee9f-e01e-3d81-9887-7e6d52bdbbc8 | -11.52433 | -54.79061 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c455bd6e-abda-351d-acd0-1c71505174a8 | -10.90254 | -56.85447 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4b4edc4-4c62-3635-b646-2114f5d4ff41 | -12.17152 | -57.13547 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 548eef65-aeec-3c7f-b6eb-74deafbcd377 | -12.18566 | -52.89687 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c13e9e99-e40e-3748-933b-6e0c52fb4fe0 | -12.55049 | -57.18632 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c101eb1d-db35-3d5d-ba08-f17f961f6c7a | -12.17551 | -57.1323 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 890ffc11-984e-3503-89a9-efca759cf97d | -9.08942 | -59.40155 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80e41cbc-aa33-3aee-8aa0-bc868487b69b | -11.90825 | -57.11462 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a753ca5-2def-33e1-90a4-b8ec4a6b15e9 | -12.19015 | -52.87626 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90c1664e-b69f-3fde-9e3c-7cc498463223 | -12.19032 | -52.88953 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3fe7503-56aa-328a-80f9-89651da69048 | -12.1837 | -57.15246 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f3e3b7-5307-31ec-85bc-14cf43928a3f | -12.54711 | -57.18574 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 619bfd9e-646d-35eb-bebc-3e4416c0ac2a | -12.16813 | -57.13491 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d12eefc7-8828-3857-aa97-186155f8056b | -12.23179 | -56.54573 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e0b5872-1f2f-31f1-8160-3aef1289f444 | -9.08423 | -59.40887 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69759cad-f7b0-3747-826a-a339f7cfac43 | -10.05385 | -59.114 | 2026-06-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85fc2842-f195-37a3-9868-dea415c6cb3f | -10.30271 | -57.13027 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 41124ce9-534c-3d50-8f70-5785fe99189d | -12.61006 | -57.89128 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8427ac27-2ad5-3373-beed-abfb5d130efc | -12.7913 | -54.88797 | 2026-06-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0b06e22d-5452-3736-b09d-fed914a4eda6 | -12.20525 | -52.87049 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a6f5785a-c58f-3a8a-8651-da406b2c653f | -11.21769 | -54.33052 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b86d7b-7edf-37ba-af47-a00649afc8d1 | -12.99185 | -57.77546 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00123d74-7a68-321a-b535-c8cb7965914c | -12.59931 | -57.87828 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c5732cd4-7bac-3fb0-8a86-2f0f80f4e0ed | -11.2167 | -53.82162 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b3bdfad5-50e7-3159-bdf7-1f5f2370f1ac | -11.93899 | -58.61249 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61b979ac-758c-3ee3-8bd1-7c05e65854bf | -12.60496 | -57.88728 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdc4f1bf-da7a-343e-94b5-7c7294f8333a | -11.93177 | -58.62571 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0185c50-1101-37fd-8368-39ecca2d3d19 | -14.04529 | -46.33138 | 2026-06-28 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea2dd85d-7697-3956-8383-f442f7e7d99a | -12.18492 | -57.14501 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb249473-7c76-3a6e-9136-3ec10eae0abd | -11.93107 | -58.62996 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 201e2ed6-4c43-32d7-8b27-73abe37ec395 | -10.93868 | -56.85254 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dd03fc5-bcd5-32a5-95d6-489356912af7 | -12.1783 | -57.13659 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef025a4f-5215-3faf-9913-3382014deb17 | -11.32597 | -54.46693 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d3f694-1fa9-312c-8013-b82729a69d55 | -9.08681 | -59.4167 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f680915b-e481-3235-8e2f-4741e5076901 | -12.98778 | -57.77871 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b877471-3186-35a3-a3f3-0c6e78c2a6cf | -11.20535 | -54.29986 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 001bfca4-df23-3898-a856-3f0a80bd7cb0 | -11.21531 | -54.30143 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 9fb6593f-a70d-3222-a50c-b89cecdcad8f | -17.34907 | -42.61313 | 2026-06-28 04:59:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc926882-cd1f-3e02-854e-af8471dc38c4 | -9.09161 | -59.41227 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7f184cf6-d792-3449-ba8e-1d7a18e7a12e | -12.18844 | -52.88813 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b744d4b9-61a1-3259-a8be-7fed6d2b8bcf | -9.09148 | -59.38943 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1665c375-cf48-3b28-8a9c-dafe88daf26f | -12.4542 | -58.49428 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f2a9a7c-c345-3bbf-80b4-8e4bcfa9270d | -12.19326 | -52.86976 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d0e1251c-4950-3f79-9d6c-1c7360614541 | -10.05765 | -59.11465 | 2026-06-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fe749ba-cf34-3584-8269-7f391dc94f6e | -12.09119 | -52.016 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3082c9f2-184d-31da-99fa-b3ce667d334c | -10.05926 | -59.10514 | 2026-06-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04d64a8d-733f-3eaa-a126-7063ab5f9bf8 | -10.84562 | -49.12272 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d043d59-f1ab-3183-8258-fbb62cb500ed | -11.21422 | -54.30852 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4b56fda4-653f-31c2-9cdf-e8836aeddd49 | -14.63336 | -54.46029 | 2026-06-28 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea32e908-ba71-3267-9a8a-64f40c4b5842 | -11.92906 | -58.66458 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adda65d5-6d2a-3848-8f63-d9fc1c6457d2 | -11.91644 | -57.40937 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01e281aa-3ff2-3d0c-b14a-cac3dc1bd5ed | -12.181 | -52.90422 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 50d89e42-70ee-3aaa-b3a1-bdaa5e746c31 | -10.83654 | -49.12548 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9b7ada3-3eef-3480-89d7-fec43fc11cce | -11.21477 | -54.30498 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 74f1a033-c4e3-38e6-b156-2b1ad9c1db4a | -12.17092 | -57.13919 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccc16e5b-f4b5-3fba-8803-b101462288cc | -11.21335 | -53.82109 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b4ca8b12-244f-3c8b-ba8e-c16de6b5d078 | -9.09507 | -59.39221 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 490e0719-c4ad-390f-b17b-ee541c9304d3 | -12.16912 | -57.15036 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac46a9cd-bc68-3eb2-85ea-82439b895721 | -16.04553 | -50.5591 | 2026-06-28 04:59:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9814f909-89b7-3aae-87ce-65ac60b1c77d | -9.09074 | -59.41735 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb121bad-9362-3086-9a93-0b189937f5a0 | -10.3021 | -57.13408 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README15.md)
