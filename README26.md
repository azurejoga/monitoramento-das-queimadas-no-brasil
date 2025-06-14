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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7547a23b-21a6-3282-be4b-64b0335aff2c | -10.04584 | -64.98705 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bda8c61-a35f-33a3-9ef1-38be083aca8a | -10.30009 | -60.55313 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 716d9811-722d-3e99-9d34-4334ca2696fa | -12.27479 | -57.27577 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e328c4e-a223-3792-9a1d-64f68624467a | -12.62115 | -57.8848 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edb4d61d-f548-3e0b-90a9-1a1d081a3cfa | -10.29245 | -67.41915 | 2025-06-14 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8fb088fe-f3c8-33a2-af54-7561edf64437 | -9.17987 | -61.86945 | 2025-06-14 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 736c3224-f1b8-340c-85d9-fde245e12228 | -12.27397 | -57.27094 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9236dfb3-3c2e-349a-8294-370471f15c3d | -11.91699 | -57.46246 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35d79513-b0f1-335d-90f5-1aa4c0d8606e | -10.28969 | -60.55187 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3390fa99-2b5f-322e-b0d1-bb1e5a9f4cf6 | -9.91768 | -59.9076 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e539e628-a243-38db-bb90-62bc1af9fb4e | -10.36164 | -57.22507 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f986b11-d000-3cf9-8c86-4223e2c58183 | -9.84319 | -63.66761 | 2025-06-14 05:53:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ba57114-df38-3370-8cd9-f4b1e199d585 | -10.29447 | -60.55575 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2216ccd5-6bb3-3414-b389-313abcfa3be7 | -12.61481 | -57.88392 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7882707a-ecae-36e0-ae78-30b6233edcb2 | -10.28927 | -60.55515 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d77ba9b6-38d3-3569-9568-d16c44af2dc1 | -10.29531 | -60.54927 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67d96b32-d3be-3f0b-8204-7c6a6943dcf9 | -9.75461 | -66.61725 | 2025-06-14 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b949386-eda2-347b-895c-6a12d7420faf | -12.61424 | -57.88908 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24201127-fddd-3d89-8855-33055b2eeab7 | -9.88223 | -61.40386 | 2025-06-14 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d8dc5c8-fe1a-3858-9c92-38e2e28fc532 | -9.64047 | -67.28767 | 2025-06-14 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 738f3019-0762-34b1-8701-cac63b3baa09 | -10.361 | -57.23056 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f04ecc-e914-3d1f-acee-70853e818cb6 | -12.27545 | -57.27022 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9253ef5d-e53c-3cb6-ac24-39084680ef36 | -12.6188 | -57.88565 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef6cf990-7ad7-3e40-82d5-8a56966d3678 | -10.94028 | -56.83908 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74d3b0b9-1fa7-3178-b16a-c73b650ec38d | -11.91637 | -57.46804 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77d23f41-f055-383f-ad74-5750dbbd346e | -12.56843 | -57.76147 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dcc0131-358e-3b05-85a4-1339fb575680 | -9.45991 | -57.84433 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42ae52f1-51bf-3a2b-a3d7-37853ad49821 | -9.38817 | -57.51758 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca18dc06-c3f8-3c46-a52d-67e0eecd45f9 | -10.36608 | -57.23544 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15a2660b-db57-3c24-8ae7-f6b2b2beea4c | -10.04654 | -64.98225 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25881807-b8af-34c3-ba27-3975f39d4f51 | -11.91575 | -57.47358 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4abfbe9-fac9-37d0-9d73-d351fe236946 | -12.62002 | -57.89507 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f6dd77b-a882-329a-9d0e-57ae60163e75 | -9.46547 | -57.84974 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f36df9b9-95de-3eb8-b4e2-9b0e094360cd | -9.40128 | -65.51429 | 2025-06-14 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6234fa02-f4aa-3153-82d6-a2988b743969 | -11.91591 | -57.46563 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 968d97a9-c543-323a-83bc-013482a87a5c | -9.18055 | -61.86455 | 2025-06-14 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 933f17de-6894-3d80-bcd0-ec8f524c2e14 | -9.38697 | -57.52742 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9f7b56a3-cf50-33c2-bf5c-5964e9ce07cd | -9.87737 | -61.40316 | 2025-06-14 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| affeefe7-4bab-39ab-a5a1-d2b26f48dc82 | -9.3938 | -57.52345 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 928627c5-4f5a-3626-b8fd-be8bf3f8cd24 | -12.28055 | -57.27174 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7ef070c-e8d4-3e62-b4f3-8d1a039a9d58 | -10.93361 | -56.83844 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6c310168-1af7-3755-ba0d-db12d65da82f | -10.93535 | -56.84226 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 754d3f0d-e093-360e-a984-566092f5b043 | -9.84736 | -63.66823 | 2025-06-14 05:53:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e52833a2-2c4c-397b-861e-7eebd496ac44 | -12.61246 | -57.88477 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90740718-70c7-3c73-bdbc-09bd0adb2329 | -10.93962 | -56.84479 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3ecc04f8-9a33-33c1-9fd5-aeb811837ced | -10.29967 | -60.55643 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f1505d3-56ea-3801-a245-7c3af94e3a86 | -12.6176 | -57.89589 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 193c3c36-ca16-3332-b84d-a889ec77dc8c | -9.38976 | -57.51995 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 463a926a-f5f9-3aa0-a538-b60347d437b5 | -9.84571 | -63.66831 | 2025-06-14 05:53:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e7e9661-032e-3fe5-99c2-3f7dbe30616e | -12.27993 | -57.27731 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f3f7c62-52f7-36c5-b086-8269ac6a440f | -9.46604 | -57.84514 | 2025-06-14 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8d0b8d9-518d-3dd4-a323-ca63e6d13003 | -12.56202 | -57.76075 | 2025-06-14 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad51fd9f-b434-3710-9c8c-26a01e93cac0 | -12.28117 | -57.26611 | 2025-06-14 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c05bf421-41fa-3c80-8c50-880eb803fb51 | -10.2949 | -60.55245 | 2025-06-14 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fae99720-4e82-3258-a941-496612b2ec24 | -10.36743 | -57.23147 | 2025-06-14 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58e129b0-65f9-399a-b375-a9fd2add496a | -14.20724 | -57.40103 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88f98cb3-0c91-3863-92f3-cf913c58a7e2 | -14.21996 | -57.40824 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06ad3b69-054f-37a0-ba92-d118a2fa4e07 | -14.21748 | -57.40685 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cbbdd17f-b743-3f98-b1e7-ab8bd0755029 | -14.21809 | -57.40075 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4e96a4c0-c8ce-344d-b0ce-ec6bcbece7f0 | -14.20595 | -57.41318 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7b771e98-8c6e-3812-8ad8-0a068780091c | -16.14259 | -60.08078 | 2025-06-14 05:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1400ad9-eb25-3ff9-a318-c6fbf2405812 | -14.21934 | -57.41402 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 083e4927-b11c-379f-b5a0-71770917f3a1 | -14.20658 | -57.40719 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ad2baa4-8bfa-3984-9af3-15528ba92def | -14.2139 | -57.4018 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 498bc7e5-90c1-30f0-8cb4-e911c09a5ef2 | -14.21872 | -57.39439 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 021bd412-ca3a-3759-93bc-4e1462520798 | -14.2206 | -57.40223 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2e19cb5a-eff0-3349-96ec-c6a3f7c00198 | -14.21458 | -57.3954 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8959b5b3-9dae-337b-94e9-c116ea199346 | -14.21265 | -57.41357 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 426e4e60-3f8f-3a6a-b5f1-3f5585c72505 | -16.14836 | -60.0816 | 2025-06-14 05:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ff6981a-68f9-366e-a78a-779251f65dc5 | -14.2169 | -57.41258 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc8050f3-6836-3009-bf19-bdc111e45dbe | -14.21326 | -57.4078 | 2025-06-14 05:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b52b8599-b7a9-3ef1-a599-d13baeb66b48 | -13.72017 | -58.681 | 2025-06-14 05:55:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d7d9e82-f158-337d-bfe0-d2b68331d5ee | -14.2121 | -57.4098 | 2025-06-14 06:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ffda5991-e3f9-36cb-82fc-f574ac1cfb85 | -13.9062 | -54.6084 | 2025-06-14 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| f44af734-dcac-3616-8e90-020a4b2a092b | -14.2121 | -57.4098 | 2025-06-14 06:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 5b22a5ce-a1ea-3b77-9443-08e283ad1310 | -14.2121 | -57.4098 | 2025-06-14 06:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| df6fbe37-01a3-3dde-a2aa-3170ed596021 | -13.9062 | -54.6084 | 2025-06-14 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 49373beb-43cb-3989-ab9a-a4e0a708a7cf | -10.9355 | -56.8322 | 2025-06-14 06:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 2ad043de-60a8-3530-9f74-a832709e4747 | -12.60974 | -57.88195 | 2025-06-14 06:54:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e43936b9-1865-3cac-946a-cf130f71dae7 | -14.2015 | -57.41124 | 2025-06-14 06:54:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 496e5dab-33ac-3602-8ea1-c3b15365d3ea | -10.28379 | -60.55012 | 2025-06-14 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9ea2f80-4acd-3be4-910d-8a3aa80f281f | -10.29215 | -60.54523 | 2025-06-14 06:54:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b86ed1b7-0ab1-387a-abae-2c0854d9244d | -9.8756 | -61.3994 | 2025-06-14 06:54:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6c6ecb40-b496-36fd-adb3-fb0bd2ed224f | -9.5707 | -46.7353 | 2025-06-14 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b0b2c145-de68-3594-b6b9-d41875a7aa05 | -5.90392 | -43.44857 | 2025-06-14 12:23:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3c50a753-5422-3d38-8c37-0d13a03b4346 | -5.78869 | -43.61856 | 2025-06-14 12:23:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9f09351b-89da-35c0-a9b9-ff14476b9c95 | -5.78719 | -43.62949 | 2025-06-14 12:23:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 87c93428-16cd-3f49-a76a-30138f914d8b | -6.60846 | -43.89557 | 2025-06-14 12:23:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 15a553d0-c898-3fe0-acd3-7425ba5c709f | -6.43591 | -44.79607 | 2025-06-14 12:23:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5294e514-88df-3f1c-9bd2-e7aa22b19014 | -5.77653 | -43.47573 | 2025-06-14 12:23:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 908fe922-9f85-3b82-8663-1075817681ef | -8.6097 | -51.5731 | 2025-06-14 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 4595724a-e2a6-32f9-af80-2c394282daee | -10.8696 | -54.2947 | 2025-06-14 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 1aeff9a1-ee7c-367d-bc54-42c32943b258 | -10.8696 | -54.2947 | 2025-06-14 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 9c8a343f-475e-33f2-a636-6b8e7fd6dd7f | -11.8963 | -47.4537 | 2025-06-14 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ac5bf534-8915-32ec-a8a2-ffbf8f332071 | -10.8696 | -54.2947 | 2025-06-14 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 3521350a-1565-3ec5-b7d1-f2a9a011ca19 | -10.8696 | -54.2947 | 2025-06-14 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 7f71e701-a111-39e6-b395-17345e6a43db | -10.8604 | -46.694 | 2025-06-14 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 8b316fbb-1a8c-30c6-9ab6-c56a16b6e2d3 | -12.6236 | -57.8926 | 2025-06-14 13:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 9b1e0fea-0865-369c-9e64-ad0944ff0d83 | -13.9056 | -54.6498 | 2025-06-14 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 70588f49-8585-3b91-ba57-8ec67a408f68 | -12.5177 | -57.2031 | 2025-06-14 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |


[Clique aqui para ver as próximas entradas](README27.md)
