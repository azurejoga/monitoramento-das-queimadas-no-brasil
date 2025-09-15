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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45260d58-eec3-3df1-91b9-2d2c7cf6f990 | -16.27882 | -45.68508 | 2025-09-15 05:12:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd3a65d1-a1fb-385f-a49a-bacf8a63b9c3 | -12.7848 | -47.9301 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd2804c5-dcc4-31b6-a3f2-24e2ee0de088 | -18.61764 | -50.39783 | 2025-09-15 05:12:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b799277d-a975-374d-83af-09dd56c07554 | -16.7153 | -54.94704 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f3e6c4d-ff68-3b18-8652-7e10c721276b | -13.18669 | -47.28749 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e5b4987-228f-3da8-a704-fe88537e97b5 | -13.75046 | -48.77218 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6a8ae5f-159b-38d8-a104-5dc2a8bc7993 | -15.79578 | -52.22096 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aa7895b-db00-317b-9e94-b73977fe629b | -18.62527 | -47.32643 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 780c88f3-b3db-311a-a699-cde928e1a66e | -14.42921 | -53.37155 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b0b304e-281e-3973-ac0d-2b22b4f6b106 | -13.19138 | -47.29099 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf11998c-83ae-3917-b194-11b960a33903 | -14.93358 | -46.56497 | 2025-09-15 05:12:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 63d6c896-8b47-3c24-b114-e8c6ea6158ba | -18.48025 | -46.94624 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3d61cb9-1a30-3145-8516-f25a23cdce36 | -16.66803 | -49.77248 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 664e818b-b5c8-359d-a824-b31ed028ff5e | -11.45885 | -58.30198 | 2025-09-15 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d90ffc2-2db3-3fb5-9810-52044e00a579 | -13.18614 | -47.29216 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b098b337-c245-318e-a225-30e3f0293db2 | -16.66741 | -49.77816 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9e39259-33e6-3041-8a49-cb1d71a2cf33 | -14.81923 | -51.63152 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| dc5a59c3-ce57-3616-8ac4-454c86197838 | -15.78779 | -52.2094 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68d024e4-9e3b-3786-a526-62de675c991c | -17.38039 | -53.25497 | 2025-09-15 05:12:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd127300-3b3f-3890-9bbf-d63595e7f74c | -11.77119 | -64.94756 | 2025-09-15 05:12:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34c1fc75-2f57-38e4-bf49-b905df75d8d0 | -18.58937 | -47.20556 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0a06eb9-dfce-391e-8503-9be59fb92e04 | -15.1805 | -56.68463 | 2025-09-15 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7efdfdfa-ec85-37b7-89fc-4a7b73d95bcc | -12.41222 | -63.89233 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3deb72cb-9b75-3161-8897-7ef568c11a47 | -12.85806 | -62.12858 | 2025-09-15 05:12:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7864037a-17fc-3ad8-984f-14528c88738f | -14.93131 | -46.56879 | 2025-09-15 05:12:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 30642645-cd16-3e56-8d96-5a1faa9ed565 | -17.24205 | -49.47228 | 2025-09-15 05:12:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d3e63a2-adf3-3f77-b139-fb4d88bd3742 | -14.82337 | -51.63742 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 27555a1e-9c24-3fad-9e3b-cf6e72b7cce4 | -17.83358 | -50.42197 | 2025-09-15 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 028271b6-fc8e-3236-935c-aae9486f5c5c | -13.87954 | -48.30474 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d52144a9-93b4-357d-bc9e-6b86a20c41d4 | -17.83117 | -50.42213 | 2025-09-15 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b1ddeec-255d-3404-99fb-79aa66696f99 | -14.83834 | -51.63403 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1c2ee795-8ce9-39e7-ab5b-2cd18615d70a | -12.78144 | -47.98035 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8da1635e-4035-3e70-8de2-9bc2f32b1648 | -12.79567 | -47.94057 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51ccfeaa-cd7e-332e-ac47-c04e826d5dd1 | -12.43637 | -63.89682 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 473d72de-c611-3570-9062-e4595c3dce6c | -13.90242 | -48.31303 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47d9ed6c-9e7e-3b07-a216-532c07d39b47 | -15.8008 | -53.4707 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1523c8df-837e-3704-84a5-86b0a41558de | -16.49012 | -55.10444 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1ea14ad9-3382-36c7-a35d-b8f16d507261 | -16.49867 | -55.1656 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bdffc3d9-af34-3f92-a78f-dbcf40185f7d | -14.18032 | -46.15337 | 2025-09-15 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39d0c4a6-d798-37d0-949f-a7eaade6270b | -12.79336 | -47.931 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 211d323e-90d5-325c-9b39-e3fac828b801 | -13.1923 | -47.2826 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d182346-067f-3071-8957-be91d958f35d | -14.81366 | -51.634 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| d729cf7d-c12c-3ab4-b2ac-5a7ba83eb343 | -17.24248 | -49.46826 | 2025-09-15 05:12:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f302ac6-fdbc-3231-ab23-23b64fe2e459 | -15.90325 | -49.96547 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 76ee4a8b-b32a-3158-a06f-a3a67b186009 | -16.7046 | -54.96674 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 295dc819-9a3d-39c8-81a9-595e155cdcef | -15.78845 | -53.46523 | 2025-09-15 05:12:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aaf795e8-af18-39a3-b5f2-d026cbbef8a9 | -10.20825 | -69.05053 | 2025-09-15 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f60b9036-cb97-3ee9-b957-793a665a7083 | -16.58171 | -55.16592 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3a864a9a-c1d7-30c3-bcf5-9ec8f4ad615a | -16.66772 | -49.77531 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cd58196-f71f-3e06-8e62-579ae584910d | -14.43397 | -53.36811 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76e9065f-8b39-33fd-8eef-c9496ab461a9 | -14.14466 | -46.26575 | 2025-09-15 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02da71c0-bb8c-3a59-bed2-b82baa96c8fd | -12.32044 | -64.07906 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92552764-218b-33f5-8629-466172e2d3dc | -13.75089 | -48.76828 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2186545d-b0f4-37f5-b827-dae5c4ed2fb6 | -15.7988 | -52.19709 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f28840e-5549-336f-98c1-ae77cea18313 | -15.0505 | -47.96778 | 2025-09-15 05:12:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 631c5d25-9e56-3cd4-8557-7c91bd0bfe0e | -13.75418 | -48.77248 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60221155-f1c8-36c1-98aa-bad211916d00 | -13.17894 | -47.28965 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a20dc97a-85f7-3500-bc90-c482da0b3a5b | -14.80744 | -51.6085 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afdefff4-6d7e-3c4b-8af8-148c1107de1e | -14.80266 | -51.60785 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3daa4795-41a5-3ae6-bbf4-2e2e3f86b746 | -11.75227 | -63.11419 | 2025-09-15 05:12:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06c65d5a-e723-3e4e-b725-c9d1d2d8faa1 | -16.72644 | -54.95377 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a7434e8-06b5-345c-8a93-1ece317019ca | -13.74903 | -48.76717 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d41c52b4-08d7-3ce5-9d63-2d6901641476 | -15.07827 | -52.47533 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b4865dd-5d03-3278-ad51-237f225c1e12 | -15.79865 | -52.22398 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08271dc3-996d-35bd-b90f-7c4a6a9750a2 | -18.47352 | -46.94572 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e10e8ea1-ad0b-30bd-82e6-7780f216c272 | -18.47049 | -46.94425 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d0a9ee8-6a20-34c7-93ff-83c788996ed0 | -15.89494 | -49.99061 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9dcd4a0-3639-3628-998c-a7f690ddd47f | -14.8068 | -51.61166 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62ba5829-4c71-3dca-bb19-4c11e35f3160 | -13.19187 | -47.28651 | 2025-09-15 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f3d1d04-82af-3729-b889-77bfd54b44d4 | -14.93787 | -46.58788 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 67163a8f-d2d8-3feb-8e2a-150c8ba49f6b | -15.90286 | -49.96898 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 23ac7a06-4f13-3238-8c99-b5d516517111 | -12.77575 | -47.97768 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a0c9c4f-e90c-37a0-a4ef-5819f124d7b9 | -17.8332 | -50.42556 | 2025-09-15 05:12:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecd1fb89-ee12-3660-aa15-8ef07c25c359 | -16.70528 | -54.96172 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eff24430-f5fc-3632-a744-035fd1cbfedf | -15.10407 | -52.48943 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7575406-a4ec-3050-a1d1-f1c3ef94f6f3 | -18.62475 | -47.33211 | 2025-09-15 05:12:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 011731de-be25-369a-901e-bd0f0e9b8d27 | -11.7021 | -59.31652 | 2025-09-15 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12ee1659-3060-3d43-a200-b17244587c54 | -14.19746 | -48.77561 | 2025-09-15 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4566625-c6bf-35a0-bec7-8b6ea8436a64 | -13.74858 | -48.771 | 2025-09-15 05:12:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa66fba4-5e7b-3c79-9a5d-8eccb0fe9dc1 | -14.79724 | -51.61251 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 95a83b6a-f215-38f7-a74a-4ac282d52c0d | -14.93724 | -46.59386 | 2025-09-15 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 784a23c7-1e2f-3dea-8c6f-d429f45de7c1 | -13.8964 | -48.31357 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 10e03428-3813-3104-bf90-ab80bb8fbe74 | -14.83292 | -51.63867 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3bc0e4c3-f7e2-38c7-acd8-61d547a94168 | -18.15758 | -49.20787 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 93a09add-7135-39a4-b951-a097575e7316 | -14.79657 | -51.61569 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a5d2a08e-897c-3c39-a726-98e2417fa72b | -16.67298 | -49.77851 | 2025-09-15 05:12:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f1d40f1-4cb7-3f89-aee6-1fa7dcbc9e64 | -14.81433 | -51.62873 | 2025-09-15 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5545c38f-cf1f-3fb1-b5fb-8e308ad0421e | -15.8555 | -59.40502 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66d76d93-2d73-3698-885e-02540e40877c | -15.90244 | -49.97265 | 2025-09-15 05:12:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f53a5d4-7c2d-3810-8a3c-32bdd3b97f9a | -16.70857 | -54.96709 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f3bff0e-de40-3b5b-a1de-ae86692b5cfb | -18.1627 | -49.20689 | 2025-09-15 05:12:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 76b5af5e-9ab1-3ed2-abd0-250829a19cae | -15.10474 | -52.48425 | 2025-09-15 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab47b23b-b134-3034-9fc3-d346b6c409e7 | -16.71856 | -54.95259 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a87ffe8-c671-34b4-83ee-1f2b514e399a | -13.8811 | -48.13276 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 162a86e8-dc40-3a1b-8a99-e24576addb6f | -13.87561 | -48.12802 | 2025-09-15 05:12:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60bc1460-d38c-3c5f-b4f6-4f268aa15663 | -16.7225 | -54.95319 | 2025-09-15 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7962276a-2172-3dec-9ab1-0a4c3a4f7758 | -14.94135 | -46.55468 | 2025-09-15 05:12:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20bcd6f9-5aad-31bd-abf1-fe5faf27db77 | -12.43893 | -63.88245 | 2025-09-15 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa80d92f-17dc-3fd5-8cd3-6f2d0c5dfac8 | -16.01983 | -59.43919 | 2025-09-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee04ed63-9d5f-37de-bfc5-50008f485c14 | -12.79118 | -47.94921 | 2025-09-15 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README64.md)
