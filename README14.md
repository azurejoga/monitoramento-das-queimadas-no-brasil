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
| fa409227-06cd-3343-a41f-02529c4079e7 | -11.80068 | -57.35622 | 2026-05-28 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd48db75-c9f3-3c67-a4d9-378ec3d7b550 | -11.29515 | -54.02784 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ceb83442-0ac6-36b1-8a3b-2f6f8d3bb8c4 | -12.72337 | -54.19611 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57e4b0e4-f562-33e7-a65a-593e7f01c5af | -15.42082 | -56.3112 | 2026-05-28 05:33:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41982244-6748-3cbd-8049-562615985c89 | -12.72003 | -54.19838 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f28ef456-d35c-346b-b792-facabd9febb1 | -13.21301 | -54.51077 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccf45c64-7eb0-3701-9a1d-43d0332c863a | -11.72746 | -56.83608 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37389b39-0b30-3326-8128-28c5ab234c52 | -12.09224 | -64.2588 | 2026-05-28 05:33:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0300fb78-3ec3-3a95-9ce5-5239ce0e1179 | -13.20731 | -54.51347 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 177b2a05-52a2-392d-b717-aa9374dd3ff3 | -16.16565 | -58.47626 | 2026-05-28 05:33:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0907b809-b959-351c-b7b0-13d0283db14f | -13.2085 | -54.50338 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa6d7f85-beb9-3fbd-89e1-28ea1e90d3fe | -13.21858 | -54.518 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5618a7dc-82db-38d3-85ea-14dd36d2bedb | -13.20965 | -54.50349 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 504c1a50-c7d2-3dc1-aeee-1ba3efe5fe79 | -11.80551 | -57.35275 | 2026-05-28 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d8ccbcf-3d3e-3547-81f3-66723b20fcbe | -11.80979 | -57.35332 | 2026-05-28 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e1f479-53f6-38d3-950a-4a64de1ffa80 | -13.22482 | -54.5019 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b500b98-2aa6-3396-936d-2bee6d0b1192 | -12.72669 | -54.18889 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd148193-dac3-3725-8e24-5b63f242ed56 | -11.73188 | -56.83669 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d46e619e-9eb8-328c-9a14-cf55e63f9552 | -10.9143 | -54.12422 | 2026-05-28 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6879c1f8-27a2-3ba8-a5db-4af6c202b015 | -12.72297 | -54.19949 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3da0ac-f373-3cbe-a665-9bbe39e4666f | -12.72581 | -54.1958 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 938b815a-0f3f-3684-8d5a-1b9a167e2a9b | -11.27486 | -53.97348 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 828f7376-5e18-3279-a22f-9098a42d360b | -13.22363 | -54.51193 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f39f292-0c38-3655-b42b-812491b54752 | -11.41225 | -57.80647 | 2026-05-28 05:33:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46e3680-733c-3ef0-9e50-54e47a968369 | -13.21581 | -54.49732 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b82f687c-378f-364b-84fa-e74f1e0e9de1 | -10.90943 | -54.12027 | 2026-05-28 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dde8f38-72ef-33e7-9ba7-1b432fbf13b8 | -13.21381 | -54.50404 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 021263f2-3437-3c22-891e-f74b1391200c | -11.29192 | -54.01054 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7807227-5504-3a8a-8f71-54f24206705d | -10.05036 | -51.68274 | 2026-05-28 05:33:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5ab4641-6bd2-3ec5-9a50-ddc9f7a04858 | -13.22111 | -54.49799 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a5b3da3-10e3-3f9a-ad88-f4a906af9bf6 | -5.95003 | -43.47726 | 2026-05-28 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 772eb824-6671-3990-9ee5-c5ae5db0e796 | -13.22323 | -54.51523 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2ba8882-375f-31f9-af8f-d21286ec6224 | -13.20881 | -54.51022 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42eb09c3-9611-335b-b576-d77b0d0dcb13 | -13.21341 | -54.50741 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 714b2da1-b20e-3144-a8dd-845fa59c981b | -11.28062 | -53.97087 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa51a0cd-3dba-35fd-975a-0c9ffcadd181 | -11.93272 | -57.04146 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ea9df11-ea71-3d0f-a3ac-ce02392cf1b2 | -13.20811 | -54.50676 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d92dbf-fb19-3ec7-aea4-94739c4e4a9d | -13.22284 | -54.51853 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80acfa79-033c-305c-ad25-cbbc79e41cdf | -13.21421 | -54.50062 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba79e150-36e3-3100-be1f-6c5ae176d7ef | -13.21753 | -54.51797 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92e11966-9cc0-3a5a-a0ee-74d0288782e2 | -13.21792 | -54.51468 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bbb42fa-f4cb-359a-95c0-3cfc8dc523b8 | -11.6346 | -56.86043 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c1248d8d-46e3-31ab-ab82-ae2794808054 | -11.63766 | -58.24175 | 2026-05-28 05:33:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 096cfa04-bab6-3421-9e3f-a3d2d4d18999 | -13.21262 | -54.5141 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 099618aa-5453-307b-aec9-82ce543e3f5a | -11.46804 | -52.92221 | 2026-05-28 05:33:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78b03991-be42-37e9-a892-5aa515df88e8 | -11.30006 | -54.03182 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2bd2a86-7f34-3e6b-bcb2-90eab7513ea6 | -12.72378 | -54.19267 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67aa1fee-d06f-3a40-9242-aabd513e797a | -11.29474 | -54.03113 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a731dfa-6473-3ae6-a186-6b3fdac620b1 | -11.72182 | -56.84426 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8da3804b-cb0a-3cb6-8361-12e7639d8b13 | -10.13972 | -52.40193 | 2026-05-28 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da5be19c-2a16-32fd-b071-7fb5296dc2f9 | -10.0255 | -59.34475 | 2026-05-28 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9065927b-508a-394e-afcd-e9e49950f779 | -13.21495 | -54.50413 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4183efd1-195a-38f1-b71e-a08bd17a227d | -11.46855 | -52.91817 | 2026-05-28 05:33:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4505e7db-e92c-37f1-b4c4-d160f6a6ba56 | -11.63399 | -56.86478 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2e68b7e6-7877-3bb1-b215-7bd5cd0b5aa6 | -11.7315 | -56.83519 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06586152-bfb3-3dfe-b159-cf7808ffdafa | -10.05581 | -51.68281 | 2026-05-28 05:33:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43b8a9c4-3176-3ed3-96e1-028a961e76ff | -13.21984 | -54.5081 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d5bbdf1-d327-3deb-b141-e16c8f244c6c | -12.72539 | -54.19917 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b8a417f-a790-31ee-a666-9c173efb9dad | -12.7242 | -54.18921 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0d4b943-ac58-3c5c-8648-749425deb606 | -12.54289 | -57.20346 | 2026-05-28 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 113104e5-8af0-31a8-a032-4955290fefac | -13.22473 | -54.51196 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e7b2a93-8752-301a-beb9-9c9523a98d38 | -16.16143 | -58.47564 | 2026-05-28 05:33:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1a000189-445c-358f-9189-718c80671012 | -13.219 | -54.51472 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 579e9bb9-4b6f-3bf5-bf93-30367f54afb1 | -13.19781 | -54.51217 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ef9ad0b-01ec-3a94-89ec-9f6c00aaf15c | -13.21453 | -54.50749 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5381498-1f06-3f73-9581-5484bfe21d68 | -13.21369 | -54.51416 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7991e33-d8dd-3c43-b0da-d82e79b85d81 | -10.71002 | -56.04422 | 2026-05-28 05:33:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa0a158d-9464-3b47-bf71-384eeae18c0c | -11.4623 | -52.92149 | 2026-05-28 05:33:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97a8c354-59e7-32eb-89bb-31996dee7be8 | -11.79683 | -57.01647 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e606a2c5-6c85-32ac-8511-8321a51e7ac5 | -11.63437 | -56.85848 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d16b0271-18e4-346c-b667-a135dbc8334f | -13.21411 | -54.51084 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e2c98b2-2915-3cb6-a4ca-2123be72406e | -13.21951 | -54.5013 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 044cc7e8-23eb-3e02-b424-c852ca2cd7a7 | -11.6382 | -56.86353 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 62634e4e-aed4-3e3b-a4e9-44a95b235f14 | -13.21538 | -54.50073 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21f0ca02-27f7-3f61-89a8-36df513d9e40 | -13.226 | -54.50195 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c54b1b5a-2abf-305d-b237-e6f1cf4bc251 | -13.21327 | -54.51745 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ac2eed7-8758-337e-b535-970e01dd21f5 | -14.01783 | -53.35993 | 2026-05-28 05:33:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34cd5d7f-942e-35d3-be99-dc989a47aa10 | -13.22442 | -54.50526 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 737c55e4-051d-301b-863d-fde93ade78ff | -13.22523 | -54.4985 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ebdcae8-bcff-3cdc-8e4c-210fb69f686f | -10.44623 | -59.42754 | 2026-05-28 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 485ea330-b7e7-3697-a188-a9b0402f7592 | -13.21222 | -54.5174 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e29c726-2ece-3a93-977b-a323b847bc00 | -13.20268 | -54.5162 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a03fe6a7-d236-3205-9056-3eaec25e602e | -11.63379 | -56.86287 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 60b4953b-0626-308c-9dee-7c280e5678ea | -11.30048 | -54.02852 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98f2baf3-8c1f-3544-9fc7-786bd7df842b | -13.22515 | -54.50864 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d15e07e5-6dd4-33a0-9b24-5a1e896e590c | -11.72242 | -56.8399 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d70da2b-40bf-35b2-a6ed-f3c9db969b0d | -13.21911 | -54.50468 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 409bc6e4-cdd6-3ec9-bb61-d3b1b35a563c | -13.22154 | -54.49459 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7277221-52ab-342e-a27a-d5abd96a7e63 | -9.60322 | -58.34 | 2026-05-28 05:33:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8d6d477-c51f-38f6-81cf-677409aa60c4 | -13.21941 | -54.51142 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 173dc7d1-b343-3897-8e85-a84dc510a072 | -13.22557 | -54.50531 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93b81fa8-c845-306a-b6a4-36d3cd6c2d2a | -13.20839 | -54.51355 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccbd7f40-b11f-3d84-9f45-ac664f229f15 | -13.19822 | -54.50883 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4249d745-04fb-3517-ab4e-ce62b1ca736d | -10.13389 | -52.40113 | 2026-05-28 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 388b0fd1-34ca-31fc-862b-442d517e19f8 | -13.22563 | -54.49511 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b50618de-a313-34e5-bf71-5fcdbad13c0b | -11.63019 | -56.85978 | 2026-05-28 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d91d42b2-c949-332e-abab-cf2f5aa898ce | -13.20351 | -54.50956 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6ccad33-4244-3083-b19d-e2bfe61e53d7 | -13.22026 | -54.50476 | 2026-05-28 05:33:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecc761f1-0642-344b-9e76-2396587d88cd | -11.48004 | -52.91961 | 2026-05-28 05:33:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dac7ff9-ac26-357b-8aed-04622a3461ff | -11.27527 | -53.97017 | 2026-05-28 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
