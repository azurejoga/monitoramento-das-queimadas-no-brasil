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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eec673dc-ea42-3457-9c83-9662a04cbc13 | -18.36499 | -50.66208 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d76920c5-86ae-3cd9-b150-12c5e48276fb | -18.37286 | -50.65868 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea5f0826-31a5-3244-bd50-bd9ea129887d | -18.36738 | -50.67138 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 02f80db0-ca5b-3ad2-84a8-ed871e89c0cf | -18.37038 | -50.67628 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8908460d-4928-3966-a19f-26206c1ea562 | -18.37224 | -50.6631 | 2026-07-28 04:55:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 237c1fac-ccbd-3114-b6fa-a7d7d1fe0b28 | -27.34749 | -50.73045 | 2026-07-28 04:55:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5c0482c1-a3e2-35cb-bb08-b9aae04f4de8 | -17.35831 | -47.08154 | 2026-07-28 04:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a742757-63f5-3017-a3ff-23d173fab772 | -19.17103 | -42.99121 | 2026-07-28 04:55:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1cc5c98-522c-3238-96e7-beb222995592 | -17.35362 | -50.3779 | 2026-07-28 04:55:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90ebc737-5df7-3941-8832-7b34ae49d6a9 | -10.9588 | -43.0565 | 2026-07-28 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 571c137f-e7d7-3697-936a-302e317e0d44 | -10.9397 | -43.0593 | 2026-07-28 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 00277cbe-a6be-3e86-804a-5a7d72e43d7c | -10.9401 | -43.0355 | 2026-07-28 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 301c0170-7327-34e4-9efd-f0f6fa21e8d7 | -20.723 | -49.4242 | 2026-07-28 05:00:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7d31e93a-3d58-3a73-b7d3-6b088eca61bd | -13.3032 | -45.1045 | 2026-07-28 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 85e47e96-c3ad-343b-a2b1-2325ccaf91d8 | -10.9588 | -43.0565 | 2026-07-28 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 58c628b2-922c-390e-835e-162aff070f79 | -10.9397 | -43.0593 | 2026-07-28 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| e6c731b2-e1a1-3d09-a893-cab3c9c0191b | -20.723 | -49.4242 | 2026-07-28 05:20:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 1dba93f9-6bcd-34eb-a291-bb421f446f5a | -10.9588 | -43.0565 | 2026-07-28 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| cf6406cc-6f1c-3ea3-98aa-559602d56d7b | -10.9397 | -43.0593 | 2026-07-28 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 2e2e419d-6159-3ba8-84c3-58f9f357ff16 | -10.9401 | -43.0355 | 2026-07-28 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 12836bd1-7f72-3c50-9eb4-2f345d862b9f | -20.723 | -49.4242 | 2026-07-28 05:30:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 6afe84c1-53ce-32f6-9056-fa1783b1f5b9 | -10.9397 | -43.0593 | 2026-07-28 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 4ea02764-b7d7-37f0-8c63-654224c330ed | -10.9401 | -43.0355 | 2026-07-28 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d27b0d82-2688-3fc0-b184-1e0bde06bae5 | -3.14135 | -51.09882 | 2026-07-28 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4bd485ca-2412-3c82-8a12-96e549a6cfeb | -3.14311 | -51.09998 | 2026-07-28 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 119d1cea-c73a-339e-9209-33665ab8981c | -1.67608 | -54.46707 | 2026-07-28 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f5865fb-12ad-3561-be3a-f98e0cba06b9 | -3.14385 | -51.09482 | 2026-07-28 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| baeca0de-2852-3638-a0bf-e2082bd2fe65 | -3.26524 | -54.87942 | 2026-07-28 05:36:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4cc79c1-941f-37f0-8c8e-eb11aa175a40 | -7.17344 | -59.31434 | 2026-07-28 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54e71787-ef1a-3494-997c-7517acb2dffa | -7.16879 | -59.31876 | 2026-07-28 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da452110-c0a0-3804-a411-a79a2632ea38 | -12.93985 | -56.63734 | 2026-07-28 05:38:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec048394-dd17-34fc-9cea-2897f3aa48e2 | -14.30945 | -58.97036 | 2026-07-28 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bab9df0f-0784-389c-beba-2561a09a2769 | -8.85623 | -65.02132 | 2026-07-28 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2be9d953-785b-3cf9-8f45-352ae984be08 | -9.47325 | -63.37149 | 2026-07-28 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| addfa8df-22a8-3d71-afc3-899eb6cff9d8 | -7.80407 | -64.48737 | 2026-07-28 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3abba752-cca3-320a-9a66-519a04535ea0 | -11.65902 | -61.21974 | 2026-07-28 05:38:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a787d9d9-4a75-3290-b5d6-a40fb812cf1b | -15.40768 | -55.92083 | 2026-07-28 05:38:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f0c6272-cbf8-39e9-ad48-a7b6dc7c1d64 | -12.94023 | -56.63432 | 2026-07-28 05:38:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9362fa1c-a762-3174-af3c-b1ddc0c07554 | -11.64066 | -60.44899 | 2026-07-28 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15b19b09-7f44-3dc3-a46c-0a8f780e6f08 | -14.21792 | -58.98724 | 2026-07-28 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55f337c6-9337-3f20-8c95-671c9b0ebb97 | -14.41129 | -52.11739 | 2026-07-28 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 352ac2fc-d226-3dc3-9f9a-240cb7e4520c | -9.48034 | -57.31889 | 2026-07-28 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e90c194-9cc3-3944-9e0b-5e62933638a5 | -9.75811 | -66.25297 | 2026-07-28 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb1fdc67-aae6-30e3-91d9-9b027d5fecde | -9.1129 | -56.85324 | 2026-07-28 05:38:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43aa04fd-3d58-38fc-9e74-cc0d4e2c8091 | -8.70377 | -62.87178 | 2026-07-28 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a94a0928-ec09-33a4-97d2-e06e750f0b43 | -14.22288 | -58.98358 | 2026-07-28 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e787302a-ce73-383d-b13d-b64de242025b | -7.80076 | -64.48685 | 2026-07-28 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9ee5713-d5e7-3efa-80ea-d1ff1a13ddab | -13.35075 | -54.28746 | 2026-07-28 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aae48ab3-fc79-37dd-8d77-dced948cc3b2 | -9.11221 | -56.85836 | 2026-07-28 05:38:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a6a4544-1804-3025-9c43-0b9d0f968518 | -9.74772 | -66.20962 | 2026-07-28 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a601478d-897b-39f0-94c4-20721d720604 | -14.21735 | -58.99168 | 2026-07-28 05:38:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc72bcaa-1d74-34bc-8d30-69e43bab9aed | -9.75751 | -66.25667 | 2026-07-28 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09220309-2160-3107-ad53-3fe5d05feca5 | -8.89752 | -60.59887 | 2026-07-28 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9936431-a0a2-30ac-b045-655a837fd19a | -9.47012 | -63.27979 | 2026-07-28 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ff37ef1-faa5-3e8a-b426-a673fb32a962 | -15.41286 | -55.92455 | 2026-07-28 05:38:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76656ff3-66d8-37af-a43c-035bc2618ddf | -12.73038 | -52.06023 | 2026-07-28 05:38:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b9b966f-d2ca-39dc-b48c-68b57c740425 | -9.47969 | -57.32372 | 2026-07-28 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e63a202-750e-30ec-ada8-8cfb2fd7578e | -13.35671 | -54.28836 | 2026-07-28 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 986ceca2-aaaa-37c4-9800-d7d49a4400e9 | -11.64134 | -60.44415 | 2026-07-28 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28bdc7af-ffa1-3d50-bec3-52ce6c312480 | -8.88557 | -65.008 | 2026-07-28 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3933b27-cf4d-39bc-81cb-898faff5cd06 | -15.40731 | -55.92419 | 2026-07-28 05:38:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0eb09d1-045b-3e93-8faf-8d92d30a8149 | -20.723 | -49.4242 | 2026-07-28 05:40:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 89516866-8f3f-3e5c-aef5-12365570e62a | -13.9215 | -41.6192 | 2026-07-28 05:40:00 | GOES-19 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 60.3 |
| f81153ce-4f93-3124-bd79-922183db4cdf | -10.9397 | -43.0593 | 2026-07-28 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 668c722c-af35-30fd-b6ea-055ff3fd689c | -20.6513 | -57.27798 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e240349-65b3-3502-9409-698c2af1de5a | -22.067 | -56.52521 | 2026-07-28 05:40:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3590910-bd34-319f-9e1e-ec098520dc21 | -20.5911 | -57.27977 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a12434dd-368d-37f5-afac-16642fbc0e72 | -20.61981 | -57.26529 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9ec4eb2-80c9-3713-ba1a-f372fec6da65 | -22.06125 | -56.52459 | 2026-07-28 05:40:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91f5d928-0bc9-36e5-9b5b-a84322bdb5bd | -20.65382 | -57.27611 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f95809f4-e3fc-3079-8daf-3963b75c3c05 | -20.62483 | -57.26973 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cca7c01b-d4a4-330b-91b8-c095cc417793 | -20.60975 | -57.25661 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9600505-b22a-3fe2-8d2d-b9cc0b7a275f | -20.65092 | -57.28168 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 50768c75-812f-3efb-b34d-542182542e42 | -20.6531 | -57.28369 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb53e19c-8854-3a1c-8c2f-e9a5cb36e58f | -20.65346 | -57.27995 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5880312-cffe-3074-88c8-f7d92c815c90 | -20.64805 | -57.27939 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0cc33026-0b8a-377a-9210-9347b23b192d | -20.61515 | -57.25725 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaf8c035-c696-38b4-b990-b81a022e5100 | -20.6252 | -57.26602 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 345537ae-0fcf-3cd9-a6be-039d71b127f2 | -20.65672 | -57.27834 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 486d4015-e4f5-3df2-bc3b-a940f71f8eb8 | -20.64772 | -57.2829 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ed8fffc-7fc7-3979-ae92-782291767229 | -22.06087 | -56.52882 | 2026-07-28 05:40:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f812eeb0-4f1e-3744-b6a1-e65d90a77e63 | -20.61478 | -57.26097 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d2aff12-dad8-3061-87c8-f362a5aef1a7 | -20.64554 | -57.28098 | 2026-07-28 05:40:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2dfe5f8d-e0c4-3970-ab44-509f24966fea | -10.9588 | -43.0565 | 2026-07-28 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 010fca7f-352d-33c0-8257-0200b8391a40 | -10.9397 | -43.0593 | 2026-07-28 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 45261089-94a8-3851-8b02-a08b2bdc7b20 | -18.3749 | -50.6564 | 2026-07-28 06:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2c23a0a1-adaa-35bf-af11-619b7097bc8a | -10.9588 | -43.0565 | 2026-07-28 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e5d0857c-ec7c-30e4-a2e0-774128ddb66b | -10.9397 | -43.0593 | 2026-07-28 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 14b823d1-1a12-309e-b2b7-106c965e2e20 | -10.9397 | -43.0593 | 2026-07-28 06:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| b68603b9-059a-375f-a797-cb064acd7c73 | -8.6616 | -64.8961 | 2026-07-28 06:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cafb7489-f768-3664-ad0f-9cf6d2a3459b | -8.65791 | -64.89146 | 2026-07-28 06:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c30d77c-75b6-3d0b-b034-a1c78bed47f0 | -8.88756 | -65.02371 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40f861da-2f7c-31d6-94f2-47815193f93d | -8.93604 | -65.01859 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dc5b963-d959-3e4c-90a4-7f6ae58811ad | -8.93546 | -65.02258 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 102a1780-f05f-3dde-90b6-a0fbb3734117 | -8.68273 | -64.92245 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 524eef7a-d123-320a-af4e-de6d90037f73 | -8.8955 | -65.02895 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3db0a0d3-b997-394e-b326-4de95098191d | -8.89125 | -65.02831 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 311e4b4e-396e-3424-8567-77589d5a5c40 | -8.93235 | -65.01399 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6897de5f-7caf-38ac-90c7-54f03f359ac9 | -8.65992 | -64.89864 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d510a80e-e0d6-3486-9175-3f90d25901d1 | -8.89181 | -65.02434 | 2026-07-28 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
