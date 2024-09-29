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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27d7f885-4b66-3451-a690-bb531238fac8 | -17.65858 | -53.0971 | 2024-09-29 04:51:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8960555e-b28f-3b7b-a3a8-c0f520f52cae | -18.83588 | -54.50462 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d633cb22-abb7-3243-adc9-b0c57db0ed28 | -11.84995 | -52.51814 | 2024-09-29 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9692cf0-03b1-396b-ab73-53ab904a62a0 | -11.84939 | -52.52176 | 2024-09-29 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27ce50a1-6bd6-3f44-b46e-8da3ea6ec955 | -14.96983 | -53.60673 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81d044d9-d117-3efd-89ed-b147bcc16ea5 | -14.96928 | -53.61033 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3c7ea56-2bf2-3883-a301-842dcc87d799 | -15.78037 | -54.18389 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d87b71c9-aa22-3d06-a778-b3d68ebde3d9 | -15.77981 | -54.18747 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3274126-d49a-362b-a263-b222e3be5ca1 | -15.77705 | -54.18334 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d584f7eb-8969-3656-8b81-a0dabf3b7735 | -15.7765 | -54.18692 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15414ae5-40c1-3c2b-aa93-ba09de159bf2 | -15.77374 | -54.18279 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae75877e-7f76-3613-aae7-febf2d31fc32 | -15.77318 | -54.18638 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dd705aa-ba1c-3f3c-b181-61773affdda6 | -15.77263 | -54.18996 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 936cab8f-fca0-3793-bbe9-fe5158cb0446 | -15.77042 | -54.18225 | 2024-09-29 04:51:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32c0315b-f5bf-3621-887f-4a06447931ec | -18.84178 | -54.50547 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30a954d1-f2df-3a94-a41a-0075e058deb6 | -18.84122 | -54.50914 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3821d26-da63-335b-9ceb-d50653f82575 | -18.83921 | -54.50517 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0184b1e-9d51-32eb-a508-3595bef325ad | -18.83865 | -54.50884 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c1eabc9-12ee-3a7d-ac17-847cbe09763a | -18.83198 | -54.50773 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa6ba6ee-d8e9-3ca9-aac4-1f3e773e9c85 | -18.80752 | -54.5112 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e3c5fea-a0ac-3b83-84f8-c30423d6b613 | -18.80587 | -54.4996 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40de6803-0a88-38ed-a6c2-2634f6b7b73c | -18.80475 | -54.50695 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dfd3536-b263-3ec7-8d8a-84b2d8960bae | -18.80418 | -54.51064 | 2024-09-29 04:51:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3420638a-75cb-303e-93bb-39dd6e334a88 | -11.45485 | -54.45737 | 2024-09-29 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f6c59f01-2d92-3b65-bdf9-e9f6fc49501b | -12.44151 | -55.00144 | 2024-09-29 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e9f6cf4-9e9c-3ad1-ba4a-3aae56f18bf1 | -12.44093 | -55.00505 | 2024-09-29 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a9153cd-6295-3efa-a17e-7cee9b74f28a | -16.65057 | -55.21844 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2774382d-6ce8-30c6-9cbf-06aa15e6fa1d | -16.65 | -55.22203 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b0c604ab-b0d3-3e39-8deb-cb1942b53791 | -16.64726 | -55.21787 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4362edaa-79e0-3162-8903-7bf8d18ba1f3 | -16.64669 | -55.22147 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3ecbd207-ef54-334b-8202-18f17d9cf8f5 | -16.64612 | -55.22507 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 14159290-b781-3192-883b-99d1efdbb22f | -16.64555 | -55.22866 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 13e07ca4-2815-3adc-9591-e9ee457e0592 | -16.64394 | -55.2173 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 21af1218-f914-3f4c-bd62-bbadc83aa05e | -16.64337 | -55.2209 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| be8c7e54-6e4f-32c3-b180-ec89fffa0631 | -16.6428 | -55.2245 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2f6a55fe-06e9-3935-89bf-77625035c37e | -16.64063 | -55.21674 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eb9e9824-daef-31fc-85c2-84a9dc52ea3c | -16.64006 | -55.22033 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6cbf8873-9da8-3f10-83bb-4fc13e67b0f9 | -16.63949 | -55.22393 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d2b86100-b59f-3f32-996d-e4cfe0c9f2d3 | -16.63732 | -55.21617 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f7945780-4e1d-3603-a3ce-a9914790f5f0 | -16.63674 | -55.21977 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 66d57641-7597-3c4f-980f-1dfd2ee6a57d | -16.63617 | -55.22337 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d706963d-525f-3258-b9af-804f73f4f9e9 | -16.63343 | -55.2192 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 46e203c5-e756-3af7-8a1d-b1b7fd160850 | -16.63286 | -55.2228 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| de1d1081-860b-3aa7-8829-befc0016d103 | -16.13803 | -55.42763 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b67191c6-eeb8-35d6-9448-dafcd0f84eb4 | -16.13745 | -55.43126 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3062e81a-d835-324a-bc7a-84cbaecda8ce | -16.13686 | -55.43492 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4473c67-31cc-31e9-b4f5-b4af940b137d | -16.13628 | -55.43857 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f25fe6c-db80-355e-85b0-6547d645bae4 | -16.1347 | -55.42709 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bff2ec61-fcb6-3ebb-8c54-5c891c0ab036 | -16.13295 | -55.438 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5020757-a6c8-34e8-b360-c8c6e46b6b42 | -16.12963 | -55.43743 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fff0fbc-5622-3f4a-a0ce-c1853bd3a6e0 | -16.1204 | -55.40984 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9fcefce-8901-3e74-85cc-48c4b0d6029c | -16.11981 | -55.41351 | 2024-09-29 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c70c2ddf-e837-3de0-ac29-5b61c41b5a60 | -17.25728 | -56.44553 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7c89071b-4e9d-369f-9e7e-5c9541d4dddb | -17.25391 | -56.44493 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b9d9db43-31f4-30c8-a56d-33d2e31c40ac | -17.25054 | -56.44433 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 18e4f21b-af1a-3b67-897e-d75fc8c7ee9f | -17.24717 | -56.44373 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2449d518-6b95-30f2-9b05-7368b5067f9f | -17.16091 | -56.2643 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9282b844-880d-3493-a108-e860e0f13aab | -17.12346 | -56.20856 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 98b2af27-519f-3994-b1cb-87435dce9414 | -17.12286 | -56.21226 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d5fc47bd-ddb5-3099-8ad2-379d57c67de1 | -17.12011 | -56.20796 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 68706296-9059-31e6-90eb-e43673b97bae | -17.1195 | -56.21167 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| efac884c-43a5-3114-a3e5-25201caa9c6c | -17.1189 | -56.21537 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8088f4d1-e2bd-386f-a003-aac9f38f23fc | -17.11675 | -56.20737 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 301d3692-8573-36e8-bc4b-e9a263aea25b | -17.11615 | -56.21107 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 64fa67cd-c47d-3b32-927f-133d0302fa6a | -17.11555 | -56.21478 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| f4e77707-b371-3444-8d24-38c39682f5cb | -17.11494 | -56.21848 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d0c62846-39dd-3b0f-9478-f3ce6bb92b3c | -17.11346 | -56.24873 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 294de314-167e-3f64-97e2-bfeb770d653a | -17.1128 | -56.21048 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| aa29f700-c8c7-3b3c-b0bf-af6b7ad2ecea | -17.11219 | -56.21418 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 707d3be4-d50d-35cf-b3d6-647a5837294e | -17.11159 | -56.21789 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 091ce047-d268-3c07-b4ec-65ae51560a4f | -17.10944 | -56.20989 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9a5eb4ae-fa27-36f0-a360-1b651a4d0922 | -17.10884 | -56.21359 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 803437af-9627-3721-ba2a-d3ac4f24a6ac | -17.10824 | -56.2173 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5bb551ca-87e9-35f7-9244-5aa24b458df5 | -17.10609 | -56.20929 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ee4f8e06-f68c-3933-9cc5-f55bc0743160 | -17.10549 | -56.213 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8d30dd2e-1c9f-361b-a74d-5ae361fa4f16 | -17.1034 | -56.24694 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9458ad2d-54ae-32e9-9e80-9d850609806d | -17.10274 | -56.2087 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b3e952e5-ec78-3b2c-8cd4-fa3198f689aa | -17.09891 | -56.38022 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c05197fb-db25-3671-871f-a568bac7db52 | -17.0983 | -56.38395 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7ea05762-aae9-3e11-ac9b-354a80d3830e | -17.09554 | -56.37962 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0b6909ac-0baf-3833-a983-1448fdd2730f | -17.09493 | -56.38335 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4f71938a-6ce1-328a-acec-760cfbb45433 | -17.09432 | -56.38709 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4343e138-390b-3c92-ac6e-fc5200898dec | -17.09157 | -56.38276 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ea4034bb-a28e-3ec3-a935-eec569d868bd | -17.09096 | -56.38649 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2d33aa1c-97fe-3503-b36c-08048ae80dab | -17.08545 | -56.37783 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c92e1f34-8b58-3d15-a901-d465f7061584 | -17.08483 | -56.38156 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 407b846b-9348-3958-b563-5b537b566987 | -17.08269 | -56.37349 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a4005652-df43-38ae-8523-50a315412817 | -17.08208 | -56.37722 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3b7b4077-248e-3bab-b0fb-f9e0aff8c606 | -17.08147 | -56.38096 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a27a7983-8390-3e4b-a939-3936255c34c8 | -17.12037 | -56.18516 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 78990815-038a-3d10-a653-87791c08a7f0 | -17.11977 | -56.18886 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 00598ab8-2a75-3ce8-bb53-da7af85e6dfa | -17.11917 | -56.19256 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e0f6fe9e-598f-325b-a553-d414977fc2eb | -17.11883 | -56.17348 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6dfb120a-5496-30c7-9083-6a14f658967f | -17.11823 | -56.17717 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 347f24d2-c026-3553-b4aa-44874ff8fbd8 | -17.11762 | -56.18087 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 766e00e0-e3aa-348a-82a9-0c013cde85e7 | -17.11702 | -56.18457 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| db4a33ea-d5e1-378b-a652-6e0cf0820345 | -17.11642 | -56.18827 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2521c58a-fab7-3841-86d6-a9c9ff54de9b | -17.11582 | -56.19197 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dc675fe3-0523-344c-88a1-22dd9e30b076 | -17.11548 | -56.17289 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4ef1eae8-1753-33c0-a387-c6c4aed0d0df | -17.11487 | -56.17658 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README57.md)
