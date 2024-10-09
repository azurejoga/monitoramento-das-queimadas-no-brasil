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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36a52b0a-a4d1-37f2-be1e-a5b2f5154e2f | -13.40702 | -61.91952 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5eed090-78df-3645-a0f1-0259caf57713 | -13.40698 | -61.96802 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82b455cd-2972-3114-b411-23dc522582ea | -13.40616 | -61.92452 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 08dae4c1-6557-3081-b54f-64f6fa19d13f | -13.40529 | -61.92953 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f415431b-4e43-3ad1-8ead-d7dc9c8bdee2 | -13.40442 | -61.93456 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bf8d7c8-8711-38c9-831d-134808180bf6 | -13.40228 | -61.92381 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f4ecd462-434d-3777-a3a6-42bb724747cf | -13.40141 | -61.92881 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ef1c7332-0f95-329a-8d33-6b0872232092 | -13.40054 | -61.93384 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95f3d76e-5122-3cfd-884a-b621a3dcf96c | -13.39881 | -61.94386 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d87330e-b419-363a-b1fe-36fc881d4334 | -13.3984 | -61.92308 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ca0b2d9c-0643-36fe-ab87-0f86e5e8fe67 | -13.39753 | -61.9281 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1cdc254e-6643-317c-bafe-5ded2d86e16d | -13.39666 | -61.93311 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fc38694-ed37-3dc1-8ffd-fea405637f23 | -13.39579 | -61.93814 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48681977-c3f7-3419-a921-e52f705af6a7 | -13.39492 | -61.94313 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35719b96-f86f-381a-b572-07334f4f6338 | -13.39365 | -61.92738 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ae7bdce4-295f-3f69-a80d-4a5f92fa3a32 | -13.39278 | -61.93239 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01e00300-216f-39a6-8e41-4cf5b43cdf2f | -13.38977 | -61.92665 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9e8e6e14-2119-3445-a52d-21a61ab3ed4a | -13.38889 | -61.93167 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 408ef089-28d4-3832-aa3b-f3789e3b2883 | -13.38589 | -61.92593 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f6554205-90ff-39db-9ae3-834dca09b7de | -13.38579 | -61.97261 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 25.3 |
| fb709f90-56c5-3102-a8de-a2f3910d6fc8 | -13.38501 | -61.93094 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6421fac5-a830-38c4-9655-a454b930b884 | -13.38414 | -61.93596 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 141bee75-8381-34df-9652-c5ca93aa0618 | -13.3819 | -61.97189 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3a9fe703-2324-3a4e-be62-1d09840d2d3a | -13.37851 | -61.94526 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dc1fc64-9ef1-3672-b14f-4df4ff5a2261 | -13.37763 | -61.95029 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ec7d3a0-5f7a-3737-aa2c-4129db7b3125 | -13.47676 | -61.28896 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78f2c6ed-3d5a-327e-b4ba-ade58088f4c2 | -13.35942 | -60.57341 | 2024-10-09 05:04:00 | NOAA-20 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ce6aa4a-5003-3b56-a2d0-73bb01467b05 | -12.70532 | -60.84431 | 2024-10-09 05:04:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c0b2dc-1f11-3929-8eca-39bd39c90a64 | -12.67756 | -60.91792 | 2024-10-09 05:04:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9c60cf0-38e7-3bc3-a92a-1bb9260ddb4d | -13.52309 | -61.73927 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f8df1cc-96a0-3bfe-aa4a-9a68b5c4537a | -13.52224 | -61.74414 | 2024-10-09 05:04:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39b55df6-9483-3576-95b4-82919f7b84ae | -9.16547 | -61.5723 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a2faedf-4664-37d7-9d1f-7effc758deee | -9.16142 | -61.57159 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e370d977-dc56-3322-9405-c8574fd42d6e | -9.16079 | -61.57522 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e527fa85-e95d-3310-9920-b710092662f6 | -9.15736 | -61.5709 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 17f952d6-09f4-3af4-84b7-ed8fefed97d4 | -9.15673 | -61.57452 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9b16689c-5fc5-3f08-b24b-58d97ccd20aa | -9.14345 | -61.21227 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5399ceb-eb7a-3b38-8ca1-7d7eeb276af7 | -9.13949 | -61.21157 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f99d6a83-8997-3a52-99ac-c4f8ce234967 | -9.123 | -61.42936 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4f43090-3fad-30be-92cb-915f81e84e06 | -9.1224 | -61.43293 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b05196b-0c1e-32ba-83b5-c0d1992fe6b6 | -9.11837 | -61.43222 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 173b67e2-7e16-367d-afdb-822ef29ca3b9 | -9.10762 | -61.27817 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81325e79-9813-3271-bd95-4e40d33ca695 | -9.10403 | -61.13945 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2098eb16-53f7-3a72-9871-789abaebbba8 | -9.10263 | -61.14153 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b4479ec-215e-3b19-863c-f425e4394bac | -9.10116 | -61.36362 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4388a50-f75d-3e16-8d66-4798196ebf1c | -9.10054 | -61.36721 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af598362-f364-3dda-965d-84778c98461c | -9.10008 | -61.13875 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f7415e4-c654-3fe5-9ad8-d103aa2b1a56 | -9.09957 | -61.1357 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dce7a7c-0d68-3d17-ad95-a506eaa1c901 | -9.09868 | -61.14083 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d74bd490-8f79-3043-b308-5483d6cf8a7d | -9.09699 | -61.13291 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a436b1b4-0631-32ee-a9d6-71e661c0c510 | -9.09613 | -61.13805 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65a28fa8-867e-3b5e-a0ed-1f7ea04dcf6c | -9.09562 | -61.13501 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7522c7a-48e7-3d1c-b9c5-7dc4799908cf | -9.09473 | -61.14014 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 722d9b25-fc21-350a-a671-1ba650bc5db7 | -9.09304 | -61.13224 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68794326-23db-37c5-a110-44cf8628aac6 | -9.09218 | -61.13738 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e74ad56f-f32f-3a84-831d-da092c1b4ad2 | -9.09167 | -61.13435 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c86c34-650d-3b94-9862-92e73f970bb7 | -9.09078 | -61.13948 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b28bcb7-bed6-31ae-89c2-745d724f5b9c | -9.08909 | -61.13157 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e33d3213-ef9e-3205-90ca-fc7c1a48014f | -9.08823 | -61.13671 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dfd1f0d-7a78-3bfa-bb29-1b9220341199 | -9.08426 | -61.38979 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf643a08-56e8-3f01-a99d-c37a541b0fc3 | -9.08365 | -61.39331 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58f2b7e6-aeac-3fbc-ba47-90480363e6d1 | -9.08025 | -61.38907 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 780b7282-bb5e-327e-8fb0-4f50a9f0df20 | -9.07964 | -61.39259 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7a10887-5976-3ce0-b2ca-e2d51f84c62e | -9.06265 | -61.37145 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 494a193d-29a9-39ad-877c-132867562875 | -9.06204 | -61.37496 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 415607ff-90fd-3674-b2bb-d46a6c772a78 | -9.06174 | -61.40039 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3377ebd-d30b-3d13-a356-05553572bdf2 | -9.0608 | -61.3744 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cb84323-751d-3d10-b5a7-5d9f37359a7a | -9.00931 | -61.55741 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b89c2efd-99d4-3ae0-b951-3754047728aa | -9.00869 | -61.56105 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22f16f59-01ab-3bb4-955f-2ba3a8893936 | -8.98385 | -61.4376 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aed4e814-72c0-3c83-881d-c6077c00ec7e | -8.84518 | -61.49141 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e34392e-6664-369d-882d-26c17a5b6298 | -8.84456 | -61.49502 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a434c402-106a-350c-aa4d-7255c0dd3e65 | -8.84113 | -61.4907 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b262156e-8d2e-36dd-b37b-c7dd556396ba | -8.16872 | -61.51112 | 2024-10-09 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e7efe26-3327-3b5c-9019-bf88d349b354 | -8.16578 | -61.51058 | 2024-10-09 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 594de47a-354c-39e9-a4ff-f8e506efa71f | -9.28206 | -62.32675 | 2024-10-09 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaa61789-b13a-376e-a2e4-d0d7ac0332ad | -9.268 | -62.38251 | 2024-10-09 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2efccad-1450-3491-aba3-fe84b42467ce | -9.2645 | -62.45357 | 2024-10-09 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6313645d-f108-325b-8ef0-090801a66c4f | -9.26379 | -62.45768 | 2024-10-09 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98754125-6be1-31a4-ae60-cce04dfab7cb | -9.25949 | -62.45692 | 2024-10-09 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ed2a905-8d27-337a-8711-6f2d1ab6fcef | -9.1815 | -62.28114 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68b01b22-b433-36e4-a860-488787c009ac | -9.18081 | -62.28515 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f191597-d24b-342e-91fe-7f823841dcb3 | -9.17725 | -62.2804 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab042a3e-f0de-3f07-bdaa-3dfac4a1873f | -9.17655 | -62.28442 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58a5c99-aeaa-334c-9f88-481fd41baa16 | -9.16155 | -62.21996 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35071a2e-f8ac-3da7-b10c-40340c438740 | -9.15732 | -62.21923 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3197ed7-e21f-3136-a8ae-35c84c8e964f | -9.15309 | -62.21849 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10fb8639-fe9c-3605-8846-a59b629b22e6 | -8.90061 | -62.17304 | 2024-10-09 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 21fad936-a1f9-366d-81f9-48c2e90d01b5 | -10.47589 | -62.89938 | 2024-10-09 05:04:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1cd31fd-f067-39a0-b42b-fcf52eb482d2 | -10.47153 | -62.89875 | 2024-10-09 05:04:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74163976-6af9-307f-b7d6-3d41049f8af4 | -10.09135 | -62.5168 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9758aa2-9a57-3e3a-8060-2e195f1e6484 | -10.08711 | -62.516 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3fc5df90-f7c0-3e27-9251-93b7cf5019d4 | -10.0864 | -62.51998 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75b7c529-e214-37b5-adfa-863ad69331e5 | -10.08286 | -62.51522 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a76ce26b-cd51-3441-a956-e0f662fc116d | -10.08216 | -62.51921 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a7216bd-3d6d-3e0a-abcc-1015c80d36d7 | -10.07861 | -62.51446 | 2024-10-09 05:04:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b629fc78-4c32-3300-8e52-ab6b48f811a0 | -10.7754 | -61.51063 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 033aa8d0-1a61-3c11-b16f-39207714b4e5 | -10.77452 | -61.51586 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4fdc1266-b9dd-3e82-810b-04d39a62d54c | -10.77422 | -61.51279 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fde10bc4-5171-3e78-9d96-f046a21dda22 | -10.65325 | -61.74505 | 2024-10-09 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README183.md)
