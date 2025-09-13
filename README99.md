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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f83bf93-4cdf-32f1-8b8e-cad21c74fa2f | -17.41078 | -48.21764 | 2025-09-13 05:01:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f465a300-79d0-3cc0-84d0-c0ea11053b5f | -22.32881 | -47.40692 | 2025-09-13 05:01:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 07a24b83-d4ce-30e0-a3f0-5968cdbed097 | -17.42356 | -49.23081 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe9e698b-4b94-314a-9ba0-8d4ee7698d7e | -18.5989 | -47.19477 | 2025-09-13 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34b92604-c4b8-3abd-b53f-d413131dbac6 | -18.15775 | -49.19144 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 1fdb74ca-43bc-3ca5-b952-2381be785149 | -16.87472 | -49.34308 | 2025-09-13 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a8ab223-73d7-39d4-b823-c302b1a5d9dd | -16.49601 | -55.14241 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1f85cb10-3ecf-38c6-ac6e-0b73d312676c | -17.44657 | -49.23958 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c329368-3e58-325a-93eb-7a2eebe80305 | -20.72925 | -56.74044 | 2025-09-13 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b5cbdd0-8f5a-393c-ae55-3f027de082c2 | -16.87415 | -49.34793 | 2025-09-13 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32578060-d703-3e9b-b3f1-12ddf7b90bc7 | -16.33701 | -51.53189 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9affcb49-64c1-37f5-926d-e434ac02fc9b | -21.6124 | -46.81306 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6368a737-6a6a-35fb-9d04-0067a98c884f | -16.86769 | -49.36263 | 2025-09-13 05:01:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06ec4be2-fbd0-3126-bd86-e1a4fa7aac7a | -20.54971 | -45.83182 | 2025-09-13 05:01:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c21020cf-bc1f-3736-8d03-05b740c0eecb | -17.44117 | -49.24461 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5961fc77-3551-3e7e-8f6b-acab424c3181 | -22.66877 | -53.12125 | 2025-09-13 05:01:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cebbcf6f-e2ec-3a18-9d94-649d0e3363fd | -16.53359 | -51.73577 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adf426aa-83f5-34ad-8e40-2c7dc80020c1 | -16.5005 | -55.1354 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ff038003-ad20-3994-8d47-adc525c8fbcb | -20.73315 | -56.73727 | 2025-09-13 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bc25c75-5523-323f-8b93-4b01d73148bd | -18.45295 | -47.19686 | 2025-09-13 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aaf202c1-fde7-38cd-87e5-e45bb118006e | -17.4155 | -48.22146 | 2025-09-13 05:01:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30f5a3aa-4669-3525-a6fd-39c960e3e5e0 | -20.41261 | -46.51253 | 2025-09-13 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33fa0cfb-3239-36d5-b1d5-7133c474223a | -20.72649 | -56.73611 | 2025-09-13 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b914474c-514e-36a9-b67c-3e9340f419be | -20.44759 | -46.45603 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aec26ed-6ff8-3ccb-82a5-6ae0794a936c | -23.85384 | -50.4151 | 2025-09-13 05:01:00 | NOAA-21 | FIGUEIRA | PARANÁ | Brasil | 4107751 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b7c2b0b5-92d4-3d3e-a5ee-70b478556c25 | -16.87005 | -49.34252 | 2025-09-13 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 88bd6324-1cd1-36af-9ac6-c56b7968e2fb | -17.27953 | -47.24971 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e7eaa63-532c-3e7b-adc9-edd83555ce2f | -17.28913 | -46.09861 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75d74f4b-3e24-3786-9306-f1725e03af62 | -17.42293 | -49.23627 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03d924e8-9f48-3ab9-951b-f9a2862af2e8 | -17.44056 | -49.24985 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a135ffb5-1418-306e-90c3-f3b7bda21fd2 | -20.41811 | -46.51706 | 2025-09-13 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 322cadda-898c-3330-ab2a-81dcbc4f2fc2 | -17.54474 | -44.55599 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9341a7f6-3128-31eb-a1ea-2cd3072bc412 | -21.2663 | -57.89125 | 2025-09-13 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ad71be86-e22f-3b85-b30e-0ceb789390db | -17.37425 | -52.90544 | 2025-09-13 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc9601d7-6dc0-36da-9a54-38baa15cfa67 | -20.25972 | -44.1844 | 2025-09-13 05:01:00 | NOAA-21 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9a2bdc11-9e20-3cfa-9cdb-ef4752901a29 | -16.35786 | -51.54138 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8a7343b-7d11-3e90-815d-c2b501190b0d | -17.5435 | -44.55083 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 591f8d4c-7697-39d1-8356-436354aa5d56 | -20.65116 | -48.69901 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6802d8e-aafb-3a9d-b48e-9727f49dbd6c | -24.36122 | -48.69826 | 2025-09-13 05:04:00 | NOAA-21 | RIBEIRÃO BRANCO | SÃO PAULO | Brasil | 3543006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ccac57d-81c0-3aab-a995-f20cdbc638ed | -28.25084 | -54.90153 | 2025-09-13 05:04:00 | NOAA-21 | ROLADOR | RIO GRANDE DO SUL | Brasil | 4315958 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8fd65281-2a24-30e3-9a10-198203ff82cc | -28.24214 | -49.99496 | 2025-09-13 05:04:00 | NOAA-21 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 400a8fe3-4af7-3388-8923-3d6f075eac27 | -25.05548 | -52.08674 | 2025-09-13 05:04:00 | NOAA-21 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f8e42e3a-55e8-349c-ae16-15ee42a6d2f2 | -24.35795 | -48.69773 | 2025-09-13 05:04:00 | NOAA-21 | RIBEIRÃO BRANCO | SÃO PAULO | Brasil | 3543006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 24412a92-8bff-3fbe-8517-1a3f9a3e4383 | -23.80234 | -54.53341 | 2025-09-13 05:04:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4deaa8b5-b1e4-3ff6-9b63-49bead730a8a | -8.9989 | -45.75763 | 2025-09-13 05:08:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 60ea681e-6d3b-3cfb-b83f-333dc7ca7736 | -11.41702 | -45.604 | 2025-09-13 05:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 221.3 |
| ffc047a0-52b7-368d-b3af-1eb99706b2fa | -11.43002 | -45.59863 | 2025-09-13 05:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 426.6 |
| 54f29683-b985-356f-b902-81d6e4250d64 | -11.43356 | -45.60692 | 2025-09-13 05:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 324.4 |
| 85aa12e3-b97a-3107-96df-0c614f79af91 | -11.42334 | -45.63497 | 2025-09-13 05:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f5ec04a5-eca4-3eed-a6bb-81ca43674dd1 | -11.41347 | -45.59575 | 2025-09-13 05:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6ae7ef01-fadd-3da9-aa0f-4b2a21cf26d1 | -9.00039 | -45.74948 | 2025-09-13 05:08:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f702d1f8-4b39-3dc4-a5a0-ebb63800016f | -17.53414 | -44.55217 | 2025-09-13 05:10:00 | AQUA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f8043d8b-d1a5-370f-80eb-0728a855f2fe | -14.22694 | -46.28198 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a993aa9d-25aa-36a9-a5d6-78799cbfc919 | -14.20384 | -46.27055 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 413f4bd7-918f-3911-b808-4180239babbc | -14.28982 | -46.07897 | 2025-09-13 05:10:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1d243e54-89ee-36c7-8655-2f062f397e6e | -14.17803 | -46.22727 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 2b243c92-98f8-36d1-b9e6-493582e64a07 | -14.17105 | -46.26388 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 355.8 |
| 45cb5ed9-d461-3f7e-8b73-5c42824f8e4e | -17.54191 | -44.54584 | 2025-09-13 05:10:00 | AQUA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 30068df3-61ad-3b53-bd92-f4d0db5161bf | -17.27634 | -46.08883 | 2025-09-13 05:10:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 2edfd8fe-e1d7-3468-b1ac-5562816adc2f | -14.18764 | -46.26618 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 353.1 |
| 31350528-7f70-32d8-92f9-b1363305a0b7 | -17.28168 | -46.08091 | 2025-09-13 05:10:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c6465cf8-a2e8-3331-8f2a-cf9743bbd407 | -14.1947 | -46.27253 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 220206f6-14cd-3210-ac44-de7e4a037321 | -17.35277 | -42.69868 | 2025-09-13 05:10:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 043083af-71c9-3bd1-bb01-2a27605a0b31 | -14.17814 | -46.27006 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 543.5 |
| 46c2fede-d8ba-3b74-bb3b-774d136eec5b | -14.19416 | -46.23177 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e2e12d95-efce-3cab-96de-2ea3ecd8c386 | -14.20139 | -46.23834 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 2cd1804c-f376-3e2f-a644-28e35c2b5803 | -14.21071 | -46.27779 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8df04c7b-a939-33b5-97b1-297d5e128bce | -17.27524 | -46.11461 | 2025-09-13 05:10:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7efa8994-7998-3e8e-b352-2952dd78674b | -14.18526 | -46.23391 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 82e6f11a-81e0-3c99-a8d0-b90b77701d6a | -14.16911 | -46.22964 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 839887f3-9b10-3ca9-b7d6-9c393e175043 | -14.2308 | -46.29057 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 614bd3c9-33f7-3210-9679-621b22561bba | -18.46745 | -39.76093 | 2025-09-13 05:10:00 | AQUA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| ed25684a-72a3-3100-8fbf-87e501d719a1 | -14.28453 | -46.07025 | 2025-09-13 05:10:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 40e70cde-4ac9-3f5f-89fa-4e82a77ad990 | -14.16167 | -46.26711 | 2025-09-13 05:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 3d5d020b-606d-3594-a8b1-d9e1102277bd | -19.63704 | -45.06678 | 2025-09-13 05:12:00 | AQUA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 58.4 |
| fd67bc34-2ef7-314e-977b-44734f7c08e8 | -21.58521 | -48.41339 | 2025-09-13 05:12:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 52fcc5cd-3032-3e51-adc1-faf56ab52d5f | -21.57286 | -48.41788 | 2025-09-13 05:12:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d030be22-437d-3474-bb89-2d6ebdab7232 | -19.63248 | -45.09042 | 2025-09-13 05:12:00 | AQUA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1a5b26a9-b12b-3014-85d5-acac9257dc00 | -2.85189 | -49.50455 | 2025-09-13 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48b0cf6f-7e8f-3ced-9752-a384949875ca | -3.23546 | -46.79313 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 343de11e-e107-35c4-90fb-ffeb1eb28de3 | -2.85851 | -49.50379 | 2025-09-13 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ce961a7-4d2d-3c25-bf80-6146da694d3c | -3.23668 | -46.78097 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a21f53f0-e177-3022-a0b9-ea493960934a | -3.2193 | -47.12902 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b5ba044-1ecd-305d-b31f-5f9c0e9b4ccc | 3.83729 | -59.93506 | 2025-09-13 05:23:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0bc0bd6-5aca-37d5-b797-ec2f926d619c | -3.22206 | -47.12949 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54421d0d-3584-3dcc-8a82-a66c095dbaf6 | -3.2233 | -47.62835 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0388f3b5-9b7a-3ba6-af25-dcb4f3d73c64 | 4.1138 | -59.96425 | 2025-09-13 05:23:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8de25a37-b480-3e34-8b43-ea82df2860ca | 4.33158 | -60.3256 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1448c1e4-132b-32ca-bf57-9f9269bec700 | -3.22963 | -47.12469 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6530b446-a425-347c-a414-09509a193037 | -3.22824 | -47.63999 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bed040e5-e87e-3ebe-a74c-1ff305ce51e2 | -3.21534 | -47.12844 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 545ce17a-bcfa-304f-a658-e7cad8829d18 | -3.23363 | -47.12524 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9fb60f8-c5bb-3f6f-a507-83770b1391e2 | 4.31819 | -59.81995 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19f8d292-67c9-3d34-8e99-72cdd7915cb6 | -3.22903 | -47.63469 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6dfe798d-dcf4-38b3-90db-8d7a9b2ee240 | -3.21606 | -47.63216 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ae90735-ebf9-3fd0-aab7-76588ac3ba27 | 4.3142 | -59.81678 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd90c80d-7cbb-34b8-9ca6-e12e5ef7d7ef | -3.23576 | -46.78719 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b2065890-e25d-36b1-ba6e-cfa8dcf16a01 | -3.22293 | -47.12349 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25a85e50-9f53-3f0d-954f-ac8d5c741e90 | -3.21527 | -47.63744 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cea7bab7-2ccd-3b11-8370-65c15ad17d55 | -3.23635 | -46.78683 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README100.md)
