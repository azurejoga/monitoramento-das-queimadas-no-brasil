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

## Dados Diários - Página 205

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ded17d77-f5b2-3fa9-b3c2-9a5309baf8f7 | -10.09242 | -64.83698 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4034b2b7-5d68-39fc-bab2-96f351b3ccf2 | -10.09174 | -64.84186 | 2024-10-09 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3d36fa6-66d2-36e8-a494-a56673866371 | -9.74259 | -65.87778 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36f0a2ec-bc24-35a7-87ca-c3dfa4743a37 | -9.74197 | -65.88207 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e949bea-534e-31cc-afa6-b1c862141df5 | -9.73896 | -65.87725 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edeb1a99-8dc4-3dff-b322-dfe23a755d76 | -9.80403 | -64.4687 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd59fcb9-d531-3a4d-a64e-234c8eddf9da | -9.80309 | -64.47075 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63540b54-c78e-3074-a51e-5ff81e18676c | -9.80082 | -64.46299 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fec7232-9258-39f0-bf0f-2c85741ceb8d | -9.80008 | -64.46814 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9115772-6e72-3bf1-8fcf-c501589d075a | -9.79985 | -64.465 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 116441a1-d79c-3c61-aa78-bd4ee243d717 | -9.59239 | -64.43462 | 2024-10-09 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d548dbc-4fd0-3cba-8690-0f613888b38e | -11.6696 | -65.21936 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2382884-6167-3e55-a1d7-83929b058fb2 | -11.66573 | -65.21878 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45e81074-efc0-38ab-b4cb-9c6119a94b90 | -11.66445 | -64.9665 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eed57612-9d2b-36ba-a69d-61d90701ef4d | -11.66373 | -64.97157 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2a6325d-dda1-3b9b-ad1c-15d921166116 | -11.66053 | -64.96593 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca482320-f720-3ad8-9925-40132d4f9e80 | -11.6566 | -64.96535 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ceb521b3-d6e4-311c-9f4c-843976ef979d | -11.64841 | -65.20116 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8355f71-d0a8-35cc-bdd8-04b575a6a280 | -11.63945 | -64.97327 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5a5063c-6a9c-326e-b20f-c8e636190d89 | -11.63553 | -64.97269 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01041f99-4bae-38bf-bce4-a0e875e909ce | -11.63089 | -64.97716 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ba24990-f90e-36dd-84dc-de6c9b766df4 | -11.62697 | -64.97661 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a516ec73-7079-3a44-b7d0-b8f97bc29bac | -11.62304 | -64.97607 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 120d898e-e1e1-3ac4-ad3c-80c78dff7b0e | -11.61448 | -64.98001 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa8c5c29-de30-3c22-90df-ada68c22d05f | -11.61378 | -64.98505 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6484cd61-3d42-3da1-9107-9e5cec192e56 | -11.61308 | -64.9901 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b17d941e-c566-3531-97a1-b8306babdb3c | -11.61056 | -64.97945 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c5f7e22-d8b7-33fc-8e69-bd0a64bd8e7a | -11.60986 | -64.98449 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 490c3154-27b8-3118-9e61-6e58f6a77652 | -11.60916 | -64.98954 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cf91c3f-3f19-31c8-9441-2e4d155109c4 | -11.60453 | -64.99407 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec205e16-82b8-313c-8f63-83e99fd591c4 | -11.60061 | -64.99348 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ff8c582-918b-39aa-9ef0-c569f32d3342 | -11.57964 | -65.00063 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a90fe35-8ff7-3308-9c6f-d9142c5883cb | -11.5578 | -65.04363 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 483769e9-c526-3dc0-a0d5-06007978552a | -11.53689 | -65.13058 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51a09a31-0038-3748-a229-3cb63f1842ad | -11.53301 | -65.13 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c89afc4-4a1f-3207-a54e-73754b01e420 | -11.52843 | -65.13437 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f66d177f-ba6d-3bb4-9dce-bec5918ba984 | -11.52244 | -65.14856 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6781bd72-7267-36e0-936c-f45eb1569551 | -11.52175 | -65.15341 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69ac99eb-5c51-328d-9703-ac7bd21ad902 | -11.52066 | -65.13326 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59a25769-8e28-3700-9b46-86092cf1ae57 | -11.5196 | -65.11286 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d0aaeb4-389f-3745-ab1d-7765b321fb75 | -11.51926 | -65.14311 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8ab50cd5-e060-34e8-857b-848a5208cb73 | -11.51857 | -65.148 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4533a56e-3899-34bb-9a98-f0830631f05b | -11.51608 | -65.13762 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 067a9375-9b50-3241-91e2-24418d4b2aab | -11.51539 | -65.14253 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f5803187-c969-3882-a2ab-a8e9f028c3cd | -11.51469 | -65.14744 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 432a445d-d8ab-3aa8-9201-4f6f46870e53 | -11.51183 | -65.11172 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e37c0c32-47fa-34ba-a897-5ac1dc843eba | -11.50864 | -65.10618 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05e19836-848b-3c7d-9298-5227a04098fa | -11.50794 | -65.11115 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b36e5af6-c98d-3f5e-b5c7-e18f5744d41f | -11.50616 | -65.09564 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9cf50fad-8a35-3822-8f7c-973d124a7737 | -11.50546 | -65.10062 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f48a0e3-9bef-344e-a2ac-9fd0c0f865ba | -11.50476 | -65.10559 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d75c875-756b-361c-920a-36df68eab5b7 | -11.29541 | -64.99932 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a042237a-78da-38ec-9767-0e740d379d7c | -11.27606 | -64.90892 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| babd5194-1cde-3bf5-a7dc-a3ae9fcbd914 | -11.26822 | -64.90776 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aecbf663-2a10-3ad5-9ab2-c4f6e74e0224 | -11.91519 | -64.92332 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d65da769-b625-3788-86cf-4754fad1d9f6 | -11.91124 | -64.92274 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d28361b-10a3-3b07-9fda-3bf63ca1f994 | -11.91037 | -64.92384 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0278e74-36fd-3bb6-bd6d-fa88eafca795 | -11.90656 | -64.92731 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb426d4-5513-361d-a4e2-99c05adfee87 | -11.90572 | -64.92842 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7403e233-d89f-38be-858b-2a95c2db9a0d | -11.90502 | -64.93358 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 219f2bd7-af8c-3b97-99af-86cdb3a6139b | -11.90187 | -64.93188 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c9ad1204-d2ec-3477-bee2-8232d512862f | -11.80179 | -64.84708 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fec0a5a-e95c-341f-b1f3-6089f904eef2 | -11.80041 | -64.84827 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0086d4c4-bc47-3754-8db1-f331438bef88 | -11.71566 | -65.00183 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a6f3f5ba-01d6-334c-8480-2abd9b4f4973 | -11.71495 | -65.00692 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ff153fb3-2cba-3261-a85c-4dcb4d9cdd6a | -11.71174 | -65.00123 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| dc7e5603-09bf-3195-81ff-fb1e8c897426 | -11.71103 | -65.00632 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c2b88c8c-a8f8-33ae-b139-e112f2dcdfc0 | -11.70781 | -65.00066 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c8708c82-9982-348f-882a-498ba0f236fe | -11.70711 | -65.00574 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ad687326-dbf2-3dba-bd69-b4f3f139f758 | -11.70641 | -65.01086 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a1f5e4f3-6bfb-31a8-99d4-dd363e57dfa7 | -11.70389 | -65.00008 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a1c84619-3765-3693-9dde-0999f6c78db7 | -11.70319 | -65.00515 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 85af117f-b69b-34d9-8b0b-8887a5cf211e | -11.70249 | -65.01027 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d10a693d-4b03-3424-87fe-996aecf317f6 | -11.70179 | -65.01534 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 586e1244-d0bc-37ec-9374-10ab2eea16cf | -11.70093 | -64.96339 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 906ac6f5-8db2-3f35-966a-7183e3482b0c | -11.69927 | -65.00457 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9646dc2d-2648-3003-9af5-23cc7b76780a | -11.69857 | -65.00966 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 101d2507-db86-3840-a2c9-8ae2c5265db4 | -11.69699 | -64.96285 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 80afb215-1e94-37d7-a0e6-a84a7dab1ce1 | -11.69268 | -64.96542 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5070e344-e341-3d63-9588-eb243f1512c9 | -11.69236 | -64.96741 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2802a5ec-bced-3c68-bf32-4382972d1fa0 | -11.68875 | -64.96487 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0146b9dd-fc5b-30fa-b090-b4a1f3242023 | -11.68842 | -64.96686 | 2024-10-09 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3369b832-304d-392a-b730-95177a8880ad | -7.49686 | -69.99444 | 2024-10-09 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5531bc69-47c5-33b3-8167-8e7e5ce2efed | -6.5334 | -69.71609 | 2024-10-09 05:55:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4dc895b-e927-3513-802c-a8227ced0297 | -8.52373 | -70.04671 | 2024-10-09 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb8f836-5b8e-319a-ba79-0563a7973757 | -9.72137 | -69.07928 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed40a95b-77f5-399f-b6f2-30dd376ca8c1 | -9.71806 | -69.07876 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b587f9ee-4d3a-3a01-9945-9e670beba910 | -9.66578 | -69.04183 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91a0e45a-4d22-3763-9b71-49a01bb7a810 | -9.66248 | -69.04131 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1eaa9b0a-469b-31f0-ad89-5848601917a3 | -9.66194 | -69.04478 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58da2a40-e628-3650-a66a-d2cef7b3353d | -10.44107 | -69.17741 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11b7e258-f6f1-3c04-b880-54c4f8a47538 | -10.58625 | -69.59708 | 2024-10-09 05:55:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9026b3a5-3d49-3f09-8ca4-63fe034a6fa1 | -10.52542 | -69.33367 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10996f20-0f68-3224-b2ec-96528f574b5f | -10.44053 | -69.1809 | 2024-10-09 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d9de3e2-3f61-3781-8813-8ea94891cb6c | -10.16122 | -69.35363 | 2024-10-09 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be6c2473-fcfa-3e10-9f22-54d31f5aa56d | -8.90043 | -71.39922 | 2024-10-09 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 411090d2-b2a8-32f1-b0ab-66071c02ac35 | -8.15164 | -70.20242 | 2024-10-09 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21f31948-3728-3cb0-8cde-363410d3804a | -7.56368 | -73.03397 | 2024-10-09 05:55:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aca0f274-4bc6-3b40-a00d-ca2ce42c29ee | -8.9636 | -72.67628 | 2024-10-09 05:55:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26769b68-63da-3e69-9a3a-773d8b72a0cd | -8.92915 | -72.83945 | 2024-10-09 05:55:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README206.md)
